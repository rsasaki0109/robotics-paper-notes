#!/usr/bin/env python3

from __future__ import annotations

import csv
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ATOM_NS = {
    "a": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}
ARXIV_QUERIES = [
    'all:"ICRA 2025"',
    'all:"Accepted by ICRA 2025"',
    'all:"IEEE ICRA 2025"',
    'all:"International Conference on Robotics and Automation 2025"',
]
AI_HEAVY_TERMS = [
    "transformer",
    "diffusion",
    "foundation model",
    "large language model",
    "language model",
    "vision-language",
    "vision language",
    "vlm",
    "llm",
    "gaussian splatting",
    "3dgs",
    "neural radiance",
    "nerf",
    "prompt tuning",
    "multimodal",
]
HYBRID_TERMS = [
    "deep learning",
    "neural network",
    "neural",
    "learned",
    "learning",
    "data-driven",
    "data driven",
    "reinforcement learning",
    "federated learning",
]
TASK_PATTERNS = [
    ("SLAM", ["slam"]),
    ("Localization", ["localization", "localisation", "odometry", "place recognition", "state estimator", "state estimation"]),
    ("GNSS", ["gnss", "gps", "uwb"]),
    ("LiDAR", ["lidar", "point cloud"]),
    ("Visual-Inertial", ["visual inertial", "visual-inertial", "vins", "imu"]),
    ("Calibration", ["calibration", "extrinsic", "temporal calibration"]),
    ("Motion Planning", ["motion planning", "path planning", "trajectory", "planner", "mpc"]),
    ("Control", ["control", "controller", "whole-body", "whole body"]),
    ("Manipulation", ["manipulation", "grasp", "pick-and-place", "pick and place", "palletization", "robot hand"]),
    ("Aerial Robotics", ["uav", "drone", "aerial", "multirotor", "quadrotor"]),
    ("Legged Robotics", ["quadruped", "biped", "legged", "walking", "locomotion"]),
    ("Perception", ["perception", "segmentation", "tracking", "detection", "reconstruction"]),
    ("Human-Robot Interaction", ["human-robot", "human robot", "teleoperation", "assistive", "prosthesis"]),
    ("Medical Robotics", ["surgery", "endoscopic", "surgical", "medical"]),
    ("Software Tools", ["dataset", "simulator", "benchmark", "ros2", "web"]),
]


@dataclass
class PaperRow:
    session: str
    title: str
    authors: str
    keywords: str
    abstract: str


def normalize_title(text: str) -> str:
    text = text.lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def note_filename(title: str) -> str:
    digest = hashlib.md5(title.encode("utf-8")).hexdigest()[:8]
    return f"2025-icra-{slugify(title)}-{digest}.md"


def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [part.strip() for part in parts if part.strip()]


def bulletize(text: str, limit: int = 3) -> list[str]:
    sentences = split_sentences(text)
    return sentences[:limit] or [text.strip()]


def pick_sentence(text: str, preferred_terms: list[str]) -> str:
    sentences = split_sentences(text)
    lowered = [sentence.lower() for sentence in sentences]
    for term in preferred_terms:
        for sentence, lower in zip(sentences, lowered):
            if term in lower:
                return sentence
    return sentences[0] if sentences else ""


def author_surnames(text: str) -> set[str]:
    names = set()
    for chunk in text.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "," in chunk:
            names.add(chunk.split(",", 1)[0].strip().lower())
        else:
            names.add(chunk.split()[-1].strip().lower())
    return {name for name in names if name}


def classify_ai_dependency(text: str) -> str:
    lowered = text.lower()
    if any(term in lowered for term in AI_HEAVY_TERMS):
        return "AI-heavy"
    if any(term in lowered for term in HYBRID_TERMS):
        return "Hybrid"
    return "Non-AI"


def infer_tasks(text: str) -> list[str]:
    lowered = text.lower()
    tasks = [label for label, patterns in TASK_PATTERNS if any(pattern in lowered for pattern in patterns)]
    if not tasks:
        tasks = ["Robotics"]
    return tasks[:4]


def parse_keywords(raw_keywords: str, tasks: list[str]) -> list[str]:
    cleaned = raw_keywords.replace("Keywords:", "").strip()
    items = [part.strip() for part in re.split(r",|;", cleaned) if part.strip()]
    if not items:
        items = tasks[:2]
    return items[:4]


def difficulty_for_text(text: str) -> str:
    lowered = text.lower()
    if any(term in lowered for term in ["factor graph", "equivariant", "lie group", "optimal control", "hessian", "certifiably"]):
        return "★★★★★（abstract 初見ベース）"
    if any(term in lowered for term in ["mpc", "trajectory", "state estimation", "calibration", "optimization"]):
        return "★★★★☆（abstract 初見ベース）"
    return "★★★☆☆（abstract 初見ベース）"


def non_ai_value(ai_dependency: str) -> str:
    if ai_dependency == "Non-AI":
        return "幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。"
    if ai_dependency == "Hybrid":
        return "学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。"
    return "AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。"


def impression(ai_dependency: str) -> str:
    if ai_dependency == "Non-AI":
        return "初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。"
    if ai_dependency == "Hybrid":
        return "初見では、学習と従来手法のつなぎ方を見る材料として良さそう。"
    return "初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。"


def escape_md(text: str) -> str:
    return text.replace("|", "\\|")


def fetch_arxiv_entries() -> dict[str, dict[str, str]]:
    entries: dict[str, dict[str, str]] = {}
    for query in ARXIV_QUERIES:
        start = 0
        total = None
        while total is None or start < total:
            url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
                {"search_query": query, "start": start, "max_results": 100}
            )
            with urllib.request.urlopen(url, timeout=60) as response:
                root = ET.fromstring(response.read())
            if total is None:
                total = int(root.findtext("opensearch:totalResults", default="0", namespaces=ATOM_NS))
            batch = root.findall("a:entry", ATOM_NS)
            if not batch:
                break
            for entry in batch:
                title = " ".join(entry.findtext("a:title", default="", namespaces=ATOM_NS).split())
                arxiv_id = entry.findtext("a:id", default="", namespaces=ATOM_NS).split("/abs/")[-1].split("v")[0]
                comment = entry.findtext("arxiv:comment", default="", namespaces=ATOM_NS) or ""
                authors = [node.text.strip() for node in entry.findall("a:author/a:name", ATOM_NS) if node.text]
                entries[normalize_title(title)] = {
                    "title": title,
                    "arxiv_id": arxiv_id,
                    "arxiv_url": f"http://arxiv.org/abs/{arxiv_id}",
                    "comment": comment,
                    "authors": authors,
                }
            start += len(batch)
            time.sleep(1.0)
    return entries


def load_csv_rows(csv_path: Path) -> dict[str, PaperRow]:
    rows: dict[str, PaperRow] = {}
    with csv_path.open(encoding="utf-8", errors="replace", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            title = (row.get("Paper Title") or "").strip()
            if not title:
                continue
            rows[normalize_title(title)] = PaperRow(
                session=(row.get("Session") or "").strip(),
                title=title,
                authors=(row.get("Author List") or "").strip(),
                keywords=(row.get(" Keywords") or "").replace("Keywords:", "").strip(),
                abstract=(row.get(" Abstract") or "").replace("Abstract:", "").strip(),
            )
    return rows


def load_existing_notes(notes_dir: Path) -> dict[str, dict[str, str]]:
    matches: dict[str, dict[str, str]] = {}
    for path in notes_dir.glob("2025-icra-*.md"):
        text = path.read_text(encoding="utf-8")
        title_match = re.search(r"^# (.+)$", text, re.M)
        arxiv_match = re.search(r"\| arXiv \| \[(http://arxiv\.org/abs/[^\]]+)\]", text)
        if not title_match or not arxiv_match:
            continue
        title = title_match.group(1).strip()
        matches[normalize_title(title)] = {
            "title": title,
            "arxiv_url": arxiv_match.group(1).strip(),
            "arxiv_id": arxiv_match.group(1).rstrip("/").split("/")[-1],
            "source": "legacy",
            "note_path": path.name,
        }
    return matches


def merge_matches(rows: dict[str, PaperRow], existing: dict[str, dict[str, str]], corpus: dict[str, dict[str, str]]) -> dict[str, dict[str, str]]:
    matches = dict(existing)
    for normalized, entry in corpus.items():
        if normalized in rows:
            existing_note_path = matches[normalized]["note_path"] if normalized in matches else note_filename(rows[normalized].title)
            matches[normalized] = {
                "title": rows[normalized].title,
                "arxiv_url": entry["arxiv_url"],
                "arxiv_id": entry["arxiv_id"],
                "source": "arxiv-icra-corpus" if normalized not in existing else "legacy+arxiv-icra-corpus",
                "comment": entry["comment"],
                "note_path": existing_note_path,
            }
    for normalized, match in matches.items():
        if normalized not in rows:
            raise RuntimeError(f"Matched title not found in CSV rows: {match['title']}")
    return matches


def render_note(row: PaperRow, arxiv_url: str) -> str:
    analysis_text = " ".join([row.title, row.keywords, row.abstract]).strip()
    ai_dependency = classify_ai_dependency(analysis_text)
    tasks = infer_tasks(analysis_text)
    keywords = parse_keywords(row.keywords, tasks)
    novelty = pick_sentence(row.abstract, [" propose", "present", "introduce", "we develop", "we design", "we show"])
    method = pick_sentence(row.abstract, [" method", " approach", " framework", " algorithm", " model", " by "])
    strengths = pick_sentence(row.abstract, [" experiment", " demonstrate", " results", " outper", " evaluate", " show"])
    problem = split_sentences(row.abstract)[0] if split_sentences(row.abstract) else row.title
    related = novelty or "既存手法との差分は本文で確認したい。"
    tldr = bulletize(row.abstract, 3)
    lines = [
        f"# {row.title}",
        "",
        "> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.",
        "",
        "| Item | Value |",
        "| --- | --- |",
        f"| Session | {escape_md(row.session)} |",
        f"| arXiv | [{arxiv_url}]({arxiv_url}) |",
        f"| Authors | {escape_md(row.authors)} |",
        "| Source | ICRA 2025 / arXiv |",
        "",
        "## TL;DR",
        "",
    ]
    lines.extend([f"- {item}" for item in tldr])
    lines.extend(
        [
            "",
            "## Task",
            "",
        ]
    )
    lines.extend([f"* {task}" for task in tasks])
    lines.extend(
        [
            "",
            "## Keywords",
            "",
        ]
    )
    lines.extend([f"* {keyword}" for keyword in keywords])
    lines.extend(
        [
            "",
            "## AI依存度",
            "",
            f"* {ai_dependency}",
            "",
            "## 何を解決？",
            "",
            f"* {problem}",
            "",
            "## 何が新しい？",
            "",
            f"* {novelty or 'abstract ベースでは、提案手法のコア設計を本文で要確認。'}",
            "",
            "## どうやってる？",
            "",
            f"* {method or 'abstract ベースでは、具体的なアルゴリズム構成を本文で要確認。'}",
            "",
            "## どこが強い？",
            "",
            f"* {strengths or '評価条件や比較対象の強さは本文確認が必要。'}",
            "",
            "## 弱そうなところ",
            "",
            "* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。",
            "",
            "## 関連研究との違い",
            "",
            f"* {related}",
            "",
            "## non-AIとして見る価値",
            "",
            f"* {non_ai_value(ai_dependency)}",
            "",
            "## 難易度",
            "",
            difficulty_for_text(analysis_text),
            "",
            "## 自分の理解/感想",
            "",
            f"* {impression(ai_dependency)}",
            "",
        ]
    )
    return "\n".join(lines)


def write_notes(rows: dict[str, PaperRow], matches: dict[str, dict[str, str]], notes_dir: Path) -> tuple[int, int]:
    created = 0
    retained = 0
    notes_dir.mkdir(parents=True, exist_ok=True)
    for normalized, match in sorted(matches.items(), key=lambda item: item[1]["title"].lower()):
        row = rows[normalized]
        note_path = notes_dir / match.get("note_path", note_filename(row.title))
        if note_path.exists():
            retained += 1
            continue
        note_path.write_text(render_note(row, match["arxiv_url"]), encoding="utf-8")
        created += 1
    return created, retained


def write_matches(rows: dict[str, PaperRow], matches: dict[str, dict[str, str]], data_dir: Path) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    json_path = data_dir / "icra2025_arxiv_matches.json"
    csv_path = data_dir / "icra2025_arxiv_matches.csv"
    records = []
    for normalized, match in sorted(matches.items(), key=lambda item: item[1]["title"].lower()):
        row = rows[normalized]
        text = " ".join([row.title, row.keywords, row.abstract])
        records.append(
            {
                "session": row.session,
                "title": row.title,
                "authors": row.authors,
                "keywords": row.keywords,
                "abstract": row.abstract,
                "arxiv_id": match["arxiv_id"],
                "arxiv_url": match["arxiv_url"],
                "source": match["source"],
                "note_path": f"papers/icra2025-arxiv/{match.get('note_path', note_filename(row.title))}",
                "ai_dependency": classify_ai_dependency(text),
            }
        )
    json_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)


def write_index(rows: dict[str, PaperRow], matches: dict[str, dict[str, str]], index_path: Path) -> Counter:
    records = []
    counts: Counter = Counter()
    for normalized, match in matches.items():
        row = rows[normalized]
        ai_dependency = classify_ai_dependency(" ".join([row.title, row.keywords, row.abstract]))
        counts[ai_dependency] += 1
        records.append(
            {
                "session": row.session,
                "title": row.title,
                "ai_dependency": ai_dependency,
                "note_name": match.get("note_path", note_filename(row.title)),
                "arxiv_url": match["arxiv_url"],
            }
        )
    records.sort(key=lambda item: (item["session"].lower(), item["title"].lower()))
    grouped: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for record in records:
        grouped[record["session"]].append(record)
    lines = [
        "# ICRA 2025 arXiv drafts",
        "",
        f"ICRA 2025 の論文一覧から arXiv 公開済みと判定できた **{len(records)}本** の自動下書きノートです。",
        "",
        "- Source: ICRA 2025 paper list abstract CSV + arXiv ICRA 2025 query corpus + prior verified matches",
        "- Matching: exact normalized title match against arXiv entries mentioning ICRA 2025, then union with previously verified legacy matches",
        "- Note: すべて abstract ベースの初稿であり、精読前のメモです。",
        "- Browse: [Non-AI 60 feed](./non-ai-feed.html) / [Non-AI 60 list](./non-ai.md) / [Non-AI Top 12](./non-ai-top.md)",
        "",
        "## AI dependency overview",
        "",
        f"- Non-AI: {counts['Non-AI']}",
        f"- Hybrid: {counts['Hybrid']}",
        f"- AI-heavy: {counts['AI-heavy']}",
        "",
        "## Papers by session",
        "",
    ]
    for session in sorted(grouped):
        lines.append(f"### {session}")
        lines.append("")
        for record in grouped[session]:
            lines.append(
                f"- [{record['title']}](./{record['note_name']}) — {record['ai_dependency']} — [arXiv]({record['arxiv_url']})"
            )
        lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")
    return counts


def main() -> None:
    root = Path(__file__).resolve().parent
    data_dir = root / "data" / "icra2025"
    csv_path = data_dir / "ICRA2025_Paper_List_with_Abstract.csv"
    notes_dir = root / "papers" / "icra2025-arxiv"
    index_path = notes_dir / "index.md"

    if not csv_path.exists():
        raise SystemExit(f"Missing CSV: {csv_path}")

    rows = load_csv_rows(csv_path)
    existing = load_existing_notes(notes_dir)
    corpus = fetch_arxiv_entries()
    matches = merge_matches(rows, existing, corpus)
    created, retained = write_notes(rows, matches, notes_dir)
    write_matches(rows, matches, data_dir)
    counts = write_index(rows, matches, index_path)

    print(
        json.dumps(
            {
                "rows": len(rows),
                "existing_matches": len(existing),
                "arxiv_corpus_entries": len(corpus),
                "final_matches": len(matches),
                "notes_created": created,
                "notes_retained": retained,
                "non_ai": counts["Non-AI"],
                "hybrid": counts["Hybrid"],
                "ai_heavy": counts["AI-heavy"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
