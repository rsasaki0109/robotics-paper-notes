#!/usr/bin/env python3

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


STRICT_EXCLUDE_TERMS = [
    "deep ",
    " neural",
    "transformer",
    "diffusion",
    "llm",
    "large language model",
    "vision-language",
    "vision language",
    "foundation model",
    "gaussian splatting",
    "3dgs",
    "learning-based",
    "learning based",
    "learned ",
    "neural network",
    "policy learning",
    "language-guided",
    "language guided",
    "multimodal",
    "mllm",
    "prompt",
    "reinforcement learning",
    "radiance field",
    "object detection",
    "feature aggregation",
]
TERM_WEIGHTS = [
    ("gnss", 9),
    ("lidar", 8),
    ("slam", 8),
    ("localization", 8),
    ("odometry", 7),
    ("sensor fusion", 7),
    ("state estimation", 7),
    ("factor graph", 7),
    ("calibration", 6),
    ("place recognition", 6),
    ("radar", 5),
    ("visual-inertial", 5),
    ("mapping", 5),
    ("motion planning", 5),
    ("path planning", 5),
    ("imu", 4),
    ("range-only", 4),
    ("optimal control", 4),
    ("mpc", 4),
    ("control", 3),
    ("vehicle", 3),
    ("aerial", 3),
    ("legged", 3),
    ("quadruped", 3),
    ("manipulator", 2),
    ("robot hand", 2),
]
SESSION_WEIGHTS = {
    "localization": 6,
    "slam": 6,
    "sensor fusion": 5,
    "state estimation": 5,
    "visual-inertial odometry": 5,
    "calibration": 4,
    "motion planning": 4,
    "optimization and optimal control": 4,
    "place recognition": 4,
    "point cloud registration": 4,
}
TOP12_ORDER = [
    "2025-icra-gnss-multi-sensor-fusion-using-continuous-time-factor-graph-optimization-9a389d82",
    "2025-icra-equivariant-filter-for-tightly-coupled-lidar-inertial-odometry-2e53b464",
    "2025-icra-genz-icp-generalizable-and-degeneracy-robust-lidar-odometry-using-an-ada-ba370ba1",
    "2025-icra-dynavins-robust-visual-inertial-state-estimator-in-dynamic-environments-a88daf2a",
    "2025-icra-universal-online-temporal-calibration-for-optimization-based-visual-iner-ab7c16cf",
    "2025-icra-equivariant-imu-preintegration-with-biases-a-galilean-group-approach-1c90d227",
    "2025-icra-a-hessian-for-gaussian-mixture-likelihoods-in-nonlinear-least-squares-6e9814a0",
    "2025-icra-narrowing-your-fov-with-solid-spatially-organized-and-lightweight-global-587da81c",
    "2025-icra-a-complete-and-bounded-suboptimal-algorithm-for-a-moving-target-traveling-salesman-problem-with-obstacles-in-3d-918c2b36",
    "2025-icra-endpoint-explicit-differential-dynamic-programming-via-exact-resolution-b7c9c9f2",
    "2025-icra-variable-time-step-mpc-for-agile-multi-rotor-uav-interception-of-dynamic-aa48ddef",
    "2025-icra-kinodynamic-model-predictive-control-for-energy-efficient-locomotion-of-legged-robots-with-parallel-elasticity-881862ea",
]
TOP12_META = {
    "2025-icra-gnss-multi-sensor-fusion-using-continuous-time-factor-graph-optimization-9a389d82": {
        "why": "GNSS + LiDAR + continuous-time factor graph を一本で見られる。expanded corpus を見ても、現場ローカライゼーション直結度は依然として最上位。",
        "focus": "localization / gnss integration",
    },
    "2025-icra-equivariant-filter-for-tightly-coupled-lidar-inertial-odometry-2e53b464": {
        "why": "LiDAR-IMU の tightly coupled 推定を EqF でどう扱うかが明快。古典推定を追う材料として強い。",
        "focus": "localization / lidar odometry",
    },
    "2025-icra-genz-icp-generalizable-and-degeneracy-robust-lidar-odometry-using-an-ada-ba370ba1": {
        "why": "退化ケースに強い LiDAR odometry という、実運用で刺さる問題設定が良い。実装価値も高い。",
        "focus": "localization / lidar odometry",
    },
    "2025-icra-dynavins-robust-visual-inertial-state-estimator-in-dynamic-environments-a88daf2a": {
        "why": "動的環境で壊れやすい VINS をロバスト推定で立て直している。学習に寄らない改善として見やすい。",
        "focus": "visual-inertial / robust estimation",
    },
    "2025-icra-universal-online-temporal-calibration-for-optimization-based-visual-iner-ab7c16cf": {
        "why": "時間ずれ補正は地味だが効く。オンライン temporal calibration をどう扱うかの価値が大きい。",
        "focus": "calibration / localization",
    },
    "2025-icra-equivariant-imu-preintegration-with-biases-a-galilean-group-approach-1c90d227": {
        "why": "IMU preintegration は多くの推定器の基礎部品。bias を含む幾何的扱い方を押さえられる。",
        "focus": "state estimation / preintegration",
    },
    "2025-icra-a-hessian-for-gaussian-mixture-likelihoods-in-nonlinear-least-squares-6e9814a0": {
        "why": "推定と最適化の地力を上げる一本。SLAM や sensor fusion の裏側の計算を深められる。",
        "focus": "estimation / optimization",
    },
    "2025-icra-narrowing-your-fov-with-solid-spatially-organized-and-lightweight-global-587da81c": {
        "why": "狭視野 LiDAR の place recognition という実機制約に近いテーマ。再局在化の観点で学びやすい。",
        "focus": "place recognition / localization",
    },
    "2025-icra-a-complete-and-bounded-suboptimal-algorithm-for-a-moving-target-traveling-salesman-problem-with-obstacles-in-3d-918c2b36": {
        "why": "expanded corpus の planning 側でかなり強い一本。完全性と bounded-suboptimality を明示していて読み筋が良い。",
        "focus": "motion planning",
    },
    "2025-icra-endpoint-explicit-differential-dynamic-programming-via-exact-resolution-b7c9c9f2": {
        "why": "DDP の見通しを良くするタイプで、optimal control の勘所を押さえるのに向いている。",
        "focus": "optimal control",
    },
    "2025-icra-variable-time-step-mpc-for-agile-multi-rotor-uav-interception-of-dynamic-aa48ddef": {
        "why": "可変 time-step と horizon 設計が面白い。MPC をより実践的に使う発想が取れる。",
        "focus": "planning / control",
    },
    "2025-icra-kinodynamic-model-predictive-control-for-energy-efficient-locomotion-of-legged-robots-with-parallel-elasticity-881862ea": {
        "why": "legged 制御側の広がりとして入れる価値が高い。運動学とエネルギー効率を MPC でどう扱うかを見られる。",
        "focus": "legged control / MPC",
    },
}
GOOD_NEXT_PICKS = [
    "2025-icra-superloc-the-key-to-robust-lidar-inertial-localization-lies-in-predicting-alignment-risks-450d6bdd",
    "2025-icra-kinematic-icp-enhancing-lidar-odometry-with-kinematic-constraints-for-wheeled-mobile-robots-moving-on-planar-surfaces-c7ecb98b",
    "2025-icra-introspective-loop-closure-for-slam-with-4d-imaging-radar-2151239e",
    "2025-icra-ptz-calib-robust-pan-tilt-zoom-camera-calibration-b24578c8",
]


def normalize(text: str) -> str:
    return " ".join(text.split())


def score_record(record: dict[str, str]) -> tuple[int, list[str]]:
    text = " ".join([record["session"], record["title"], record["keywords"], record["abstract"]]).lower()
    score = 0
    hits: list[str] = []
    for term, weight in TERM_WEIGHTS:
        if term in text:
            score += weight
            hits.append(term)
    for term, weight in SESSION_WEIGHTS.items():
        if term in record["session"].lower():
            score += weight
            hits.append(f"session:{term}")
    title_lower = record["title"].lower()
    if "survey" in title_lower:
        score -= 2
    if "dataset" in text:
        score -= 2
    if "benchmark" in text:
        score -= 2
    if "challenge" in text:
        score -= 2
    return score, hits


def is_strict_non_ai(record: dict[str, str]) -> bool:
    text = " ".join([record["session"], record["title"], record["keywords"], record["abstract"]]).lower()
    title_lower = record["title"].lower()
    if record["ai_dependency"] != "Non-AI":
        return False
    if any(term in text for term in STRICT_EXCLUDE_TERMS):
        return False
    if "dataset" in title_lower or "survey" in title_lower:
        return False
    return True


def load_note_meta(root: Path, note_path: str) -> dict[str, str]:
    path = root / note_path
    text = path.read_text(encoding="utf-8")
    arxiv_match = re.search(r"\| arXiv \| \[(http://arxiv\.org/abs/[^\]]+)\]", text)
    difficulty_match = re.search(r"## 難易度\s+(.+)", text, re.S)
    return {
        "arxiv_url": arxiv_match.group(1).strip() if arxiv_match else "",
        "difficulty": difficulty_match.group(1).strip().splitlines()[0] if difficulty_match else "",
    }


def choose_non_ai_60(records: list[dict[str, str]]) -> list[dict[str, str]]:
    scored = []
    for record in records:
        if not is_strict_non_ai(record):
            continue
        score, hits = score_record(record)
        item = dict(record)
        item["score"] = score
        item["hits"] = hits
        scored.append(item)
    scored.sort(key=lambda item: (-item["score"], item["session"], item["title"]))

    selected: list[dict[str, str]] = []
    session_counts: Counter[str] = Counter()
    for item in scored:
        if session_counts[item["session"]] >= 3:
            continue
        selected.append(item)
        session_counts[item["session"]] += 1
        if len(selected) == 60:
            break
    if len(selected) != 60:
        raise RuntimeError(f"Expected 60 selected papers, got {len(selected)}")
    return selected


def write_non_ai_md(root: Path, selected: list[dict[str, str]], output_path: Path) -> None:
    lines = [
        "# ICRA 2025 Non-AI 60",
        "",
        "ICRA 2025 の arXiv 公開済み 521 本の下書き群から、**classical / model-based 寄り** の論文を強めに残して **60 本** に絞った入口です。",
        "",
        "- Base corpus: expanded arXiv drafts 521",
        "- Filter: `Non-AI` 判定 + `deep / neural / transformer / diffusion / llm` などを除外する stricter pass",
        "- Selection: localization / SLAM / GNSS / LiDAR / calibration / planning / control を強めに重み付けして 60 本を抽出",
        "- figure 付きで流し見したい場合は [Non-AI 60 feed](./non-ai-feed.html) を開く",
        "- まず読む順番が欲しい場合は [Non-AI Top 12](./non-ai-top.md) から入る",
        "",
    ]
    grouped: dict[str, list[dict[str, str]]] = {}
    for item in selected:
        grouped.setdefault(item["session"], []).append(item)
    for session in sorted(grouped):
        lines.append(f"## {session}")
        lines.append("")
        for item in grouped[session]:
            note_name = Path(item["note_path"]).name
            lines.append(f"- [{item['title']}](./{note_name}) — [arXiv]({item['arxiv_url']})")
        lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_top_md(root: Path, selected_by_id: dict[str, dict[str, str]], output_path: Path) -> None:
    top12 = [selected_by_id[item_id] for item_id in TOP12_ORDER]
    lines = [
        "# ICRA 2025 Non-AI Top 12",
        "",
        "expanded 521 corpus を見直したうえで、**最初に読むべき 12 本** を優先順で並べたページです。",
        "",
        "- 軸: **いま読む価値 / classical な学びの濃さ / 実装や設計に効くか / 分野の広がり**",
        "- 前提: full paper 精読前。draft note と abstract ベースの暫定キュレーション",
        "- 方針: localization / SLAM / GNSS / LiDAR を厚めにしつつ、planning / control も今回の corpus から入れ直した",
        "- 縦スクロールで見たい場合は [Top 12 slide feed](../../index.html) を開く",
        "",
        "## Recommended reading path",
        "",
        "1. **Localization / estimation core**: 1-6",
        "2. **SLAM / place recognition / mapping**: 7-8",
        "3. **Planning / control expansion**: 9-12",
        "",
        "## Top 12",
        "",
        "| Rank | Paper | Why read now | Focus area |",
        "| --- | --- | --- | --- |",
    ]
    for rank, item in enumerate(top12, start=1):
        meta = TOP12_META[item["id"]]
        note_name = Path(item["note_path"]).name
        lines.append(f"| {rank} | [{item['title']}](./{note_name}) | {meta['why']} | {meta['focus']} |")
    lines.extend(
        [
            "",
            "## Why these 12",
            "",
            "- **推定の芯が強い**: GNSS-FGO, Eq-LIO, DynaVINS++, temporal calibration, IMU preintegration, Hessian",
            "- **SLAM 側の広がりがある**: GenZ-ICP, SOLiD",
            "- **localization 以外も読める**: moving-target planning, DDP, aerial MPC, legged MPC",
            "",
            "## Good next picks",
            "",
        ]
    )
    for item_id in GOOD_NEXT_PICKS:
        item = selected_by_id[item_id]
        note_name = Path(item["note_path"]).name
        lines.append(f"- [{item['title']}](./{note_name})")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_selection_json(selected: list[dict[str, str]], output_path: Path) -> None:
    minimal = []
    for item in selected:
        minimal.append(
            {
                "id": item["id"],
                "session": item["session"],
                "title": item["title"],
                "note_path": item["note_path"],
                "arxiv_url": item["arxiv_url"],
                "score": item["score"],
                "hits": item["hits"],
            }
        )
    output_path.write_text(json.dumps(minimal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent
    matches_path = root / "data" / "icra2025" / "icra2025_arxiv_matches.json"
    records = json.loads(matches_path.read_text(encoding="utf-8"))

    selected = choose_non_ai_60(records)
    for item in selected:
        item["id"] = Path(item["note_path"]).stem
        item.update(load_note_meta(root, item["note_path"]))
    selected_by_id = {item["id"]: item for item in selected}

    missing_top12 = [item_id for item_id in TOP12_ORDER if item_id not in selected_by_id]
    if missing_top12:
        raise RuntimeError(f"Top12 IDs missing from selected set: {missing_top12}")

    write_non_ai_md(root, selected, root / "papers" / "icra2025-arxiv" / "non-ai.md")
    write_top_md(root, selected_by_id, root / "papers" / "icra2025-arxiv" / "non-ai-top.md")
    write_selection_json(selected, root / "data" / "icra2025" / "icra2025_non_ai60_selection.json")

    print(
        json.dumps(
            {
                "selected": len(selected),
                "top12": len(TOP12_ORDER),
                "sessions": len({item['session'] for item in selected}),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
