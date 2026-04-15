#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter
from pathlib import Path


LIST_ITEM_RE = re.compile(r"- \[([^\]]+)\]\((\./[^)]+\.md)\)\s+—\s+\[arXiv\]\((https?://arxiv\.org/abs/([^)]+))\)")


def load_manifest(path: Path) -> dict[str, dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {item["id"]: item for item in data}


def extract_table_value(text: str, key: str) -> str:
    match = re.search(rf"\|\s*{re.escape(key)}\s*\|\s*(.*?)\s*\|", text)
    return match.group(1).strip() if match else ""


def extract_section(text: str, heading: str) -> str:
    match = re.search(rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s+|\Z)", text, re.M)
    return match.group(1).strip() if match else ""


def section_points(section: str) -> list[str]:
    points: list[str] = []
    for raw_line in section.splitlines():
        line = raw_line.strip()
        if line.startswith(("- ", "* ")):
            points.append(line[2:].strip())
    if points:
        return points
    paragraphs = [line.strip() for line in section.splitlines() if line.strip()]
    return paragraphs[:1]


def first_sentence(text: str) -> str:
    stripped = re.sub(r"\s+", " ", text).strip()
    if not stripped:
        return ""
    match = re.search(r"(.+?[。.!?])(?:\s|$)", stripped)
    return match.group(1).strip() if match else stripped


def compact_text(section: str) -> str:
    points = section_points(section)
    if points:
        return points[0]
    return first_sentence(section)


def slug_anchor(stem: str) -> str:
    return re.sub(r"[^a-z0-9\-]+", "-", stem.lower()).strip("-")


def parse_list(root: Path, list_path: Path, manifest: dict[str, dict[str, str]]) -> list[dict[str, str | list[str]]]:
    text = list_path.read_text(encoding="utf-8")
    papers: list[dict[str, str | list[str]]] = []
    group = ""
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            group = line[3:].strip()
            continue
        match = LIST_ITEM_RE.match(line)
        if not match:
            continue
        note_abs = (list_path.parent / match.group(2)).resolve()
        note_rel = note_abs.relative_to(root).as_posix()
        note_text = note_abs.read_text(encoding="utf-8")
        note_id = Path(match.group(2)).stem
        tasks = section_points(extract_section(note_text, "Task"))[:4]
        keywords = section_points(extract_section(note_text, "Keywords"))
        tldr = section_points(extract_section(note_text, "TL;DR"))[:3]
        problem = compact_text(extract_section(note_text, "何を解決？"))
        novelty = compact_text(extract_section(note_text, "何が新しい？"))
        method = compact_text(extract_section(note_text, "どうやってる？"))
        strengths = compact_text(extract_section(note_text, "どこが強い？"))
        non_ai_value = compact_text(extract_section(note_text, "non-AIとして見る価値"))
        impression = compact_text(extract_section(note_text, "自分の理解/感想"))
        difficulty = compact_text(extract_section(note_text, "難易度"))
        session = extract_table_value(note_text, "Session") or group
        ai_level = compact_text(extract_section(note_text, "AI依存度"))
        manifest_item = manifest.get(note_id, {})
        papers.append(
            {
                "id": note_id,
                "anchor": slug_anchor(note_id),
                "title": match.group(1),
                "group": group,
                "session": session,
                "detail_path": note_rel,
                "arxiv_url": match.group(3),
                "arxiv_id": match.group(4),
                "tasks": tasks,
                "keywords": keywords[:3],
                "tldr": tldr,
                "problem": problem,
                "novelty": novelty,
                "method": method,
                "strengths": strengths,
                "non_ai_value": non_ai_value,
                "impression": impression,
                "difficulty": difficulty,
                "ai_level": ai_level,
                "asset": manifest_item.get("asset", ""),
            }
        )
    if not papers:
        raise RuntimeError(f"Failed to parse list: {list_path}")
    return papers


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def render_bullets(items: list[str], klass: str = "bullet-list") -> str:
    lis = "".join(f"<li>{esc(item)}</li>" for item in items if item)
    return f'<ul class="{klass}">{lis}</ul>' if lis else '<p class="empty">No summary yet.</p>'


def render_tags(items: list[str], extra_class: str = "") -> str:
    tags = "".join(f'<span class="chip {extra_class}">{esc(item)}</span>' for item in items if item)
    return tags


def build_html(papers: list[dict[str, str | list[str]]]) -> str:
    total = len(papers)
    group_counts = Counter(str(paper["group"]) for paper in papers)
    cover_groups = "".join(
        f'<li><strong>{esc(group)}</strong><span>{count} {"paper" if count == 1 else "papers"}</span></li>'
        for group, count in group_counts.most_common(12)
    )

    slides = []
    for index, paper in enumerate(papers, start=1):
        tasks = paper["tasks"] if isinstance(paper["tasks"], list) else []
        keywords = paper["keywords"] if isinstance(paper["keywords"], list) else []
        tldr = paper["tldr"] if isinstance(paper["tldr"], list) else []
        image_html = (
            f'<img src="../../{esc(str(paper["asset"]))}" alt="{esc(str(paper["title"]))} representative figure" loading="lazy">'
            if paper["asset"]
            else '<div class="figure-fallback">Figure not extracted</div>'
        )
        slides.append(
            f"""
      <section class="slide" id="{esc(str(paper["anchor"]))}" data-index="{index}" data-group="{esc(str(paper["group"]))}">
        <div class="card">
          <div class="slide-grid">
            <div class="main-column">
              <div class="meta-row">
                <span class="rank-pill">{index:02d} / {total}</span>
                <span class="chip group-chip">{esc(str(paper["group"]))}</span>
                {render_tags(tasks, "task-chip")}
              </div>
              <h1 class="paper-title">{esc(str(paper["title"]))}</h1>
              <p class="hook">{esc(str(paper["novelty"] or paper["problem"] or (tldr[0] if tldr else "")))}</p>
              <div class="summary-grid">
                <section class="panel">
                  <h2>TL;DR</h2>
                  {render_bullets(tldr)}
                </section>
                <section class="panel">
                  <h2>何を解決？</h2>
                  <p>{esc(str(paper["problem"]))}</p>
                </section>
                <section class="panel">
                  <h2>何が新しい？</h2>
                  <p>{esc(str(paper["novelty"]))}</p>
                </section>
                <section class="panel">
                  <h2>どうやってる？</h2>
                  <p>{esc(str(paper["method"]))}</p>
                </section>
              </div>
              <div class="detail-grid">
                <section class="panel">
                  <h2>どこが強い？</h2>
                  <p>{esc(str(paper["strengths"]))}</p>
                </section>
                <section class="panel">
                  <h2>non-AI として見る価値</h2>
                  <p>{esc(str(paper["non_ai_value"]))}</p>
                </section>
                <section class="panel">
                  <h2>自分の理解 / 感想</h2>
                  <p>{esc(str(paper["impression"]))}</p>
                </section>
              </div>
              <div class="facts">
                <div class="fact"><span>Session</span><strong>{esc(str(paper["session"]))}</strong></div>
                <div class="fact"><span>Difficulty</span><strong>{esc(str(paper["difficulty"]))}</strong></div>
                <div class="fact"><span>AI依存度</span><strong>{esc(str(paper["ai_level"]))}</strong></div>
                <div class="fact"><span>Keywords</span><strong>{esc(" / ".join(keywords) if keywords else "-")}</strong></div>
              </div>
              <div class="links">
                <a href="../../{esc(str(paper["detail_path"]))}">Detail note</a>
                <a href="{esc(str(paper["arxiv_url"]))}">arXiv</a>
              </div>
            </div>
            <aside class="visual-column">
              <div class="figure-card">
                {image_html}
              </div>
              <div class="visual-meta panel">
                <h2>読むときの観点</h2>
                <p>{esc(str(paper["strengths"] or paper["non_ai_value"]))}</p>
              </div>
            </aside>
          </div>
        </div>
      </section>"""
        )

    return f"""<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>robotics-paper-notes | ICRA 2025 Non-AI 60 Feed</title>
    <meta name="description" content="ICRA 2025 Non-AI 60 を figure 付き縦スクロール feed で読む GitHub Pages">
    <style>
      :root {{
        --bg: #040816;
        --bg-2: #091223;
        --panel: rgba(8, 15, 30, 0.84);
        --panel-soft: rgba(255, 255, 255, 0.05);
        --line: rgba(255, 255, 255, 0.1);
        --text: #f8fbff;
        --muted: #b7c0d8;
        --cyan: #7dd3fc;
        --violet: #c4b5fd;
        --green: #86efac;
      }}

      * {{ box-sizing: border-box; }}
      html {{ scroll-behavior: smooth; }}
      body {{
        margin: 0;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        color: var(--text);
        background:
          radial-gradient(circle at top left, rgba(125, 211, 252, 0.14), transparent 22rem),
          radial-gradient(circle at top right, rgba(196, 181, 253, 0.12), transparent 26rem),
          linear-gradient(180deg, var(--bg), var(--bg-2) 42%, #020611);
      }}

      a {{ color: inherit; text-decoration: none; }}

      .topbar {{
        position: fixed;
        inset: 0 0 auto 0;
        z-index: 30;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        padding: 0.8rem 1rem;
        background: rgba(3, 7, 15, 0.68);
        backdrop-filter: blur(14px);
        border-bottom: 1px solid var(--line);
      }}

      .brand {{
        font-size: 0.95rem;
        font-weight: 800;
        letter-spacing: 0.02em;
      }}

      .toplinks {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        justify-content: flex-end;
        align-items: center;
      }}

      .toplinks a,
      .counter {{
        padding: 0.55rem 0.85rem;
        border-radius: 999px;
        border: 1px solid var(--line);
        background: rgba(255, 255, 255, 0.04);
        color: var(--muted);
        font-size: 0.82rem;
        font-weight: 700;
      }}

      .counter strong {{
        color: var(--text);
        margin-right: 0.4rem;
      }}

      .feed {{
        height: 100vh;
        overflow-y: auto;
        scroll-snap-type: y mandatory;
      }}

      .slide {{
        min-height: 100vh;
        scroll-snap-align: start;
        display: grid;
        align-items: center;
        padding: 5.2rem 1rem 2rem;
      }}

      .card {{
        width: min(100%, 1280px);
        margin: 0 auto;
        padding: clamp(1.2rem, 2vw, 1.6rem);
        border-radius: 2rem;
        border: 1px solid var(--line);
        background: var(--panel);
        box-shadow: 0 24px 70px rgba(0, 0, 0, 0.34);
      }}

      .cover .card {{
        background:
          radial-gradient(circle at top right, rgba(125, 211, 252, 0.14), transparent 18rem),
          radial-gradient(circle at bottom left, rgba(196, 181, 253, 0.14), transparent 22rem),
          rgba(7, 13, 27, 0.92);
      }}

      .eyebrow {{
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        color: var(--muted);
      }}

      .hero-title,
      .paper-title {{
        margin: 0.55rem 0 0;
        line-height: 1.04;
      }}

      .hero-title {{ font-size: clamp(2.2rem, 7vw, 4.8rem); }}
      .paper-title {{ font-size: clamp(1.65rem, 3.8vw, 2.9rem); }}

      .lead,
      .hook,
      .panel p,
      .bullet-list li,
      .group-list li,
      .figure-fallback {{
        color: var(--muted);
        line-height: 1.72;
      }}

      .cover-grid,
      .slide-grid,
      .summary-grid,
      .detail-grid,
      .facts {{
        display: grid;
        gap: 0.95rem;
      }}

      .cover-grid {{ grid-template-columns: 1.25fr 0.75fr; margin-top: 1.2rem; }}
      .slide-grid {{ grid-template-columns: minmax(0, 1.18fr) minmax(300px, 0.82fr); align-items: stretch; }}
      .summary-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .detail-grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); margin-top: 0.95rem; }}
      .facts {{ grid-template-columns: repeat(4, minmax(0, 1fr)); margin-top: 0.95rem; }}

      .meta-row {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
        align-items: center;
      }}

      .rank-pill,
      .chip {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 999px;
        border: 1px solid rgba(255, 255, 255, 0.14);
      }}

      .rank-pill {{
        min-width: 4.2rem;
        padding: 0.45rem 0.8rem;
        font-size: 0.92rem;
        font-weight: 800;
        background: rgba(255, 255, 255, 0.1);
      }}

      .chip {{
        padding: 0.38rem 0.7rem;
        background: rgba(255, 255, 255, 0.05);
        color: var(--muted);
        font-size: 0.84rem;
        font-weight: 700;
      }}

      .group-chip {{ color: var(--text); }}
      .task-chip {{ color: var(--cyan); }}

      .hook {{
        margin: 0.95rem 0 1.05rem;
        font-size: clamp(0.98rem, 1.8vw, 1.1rem);
      }}

      .panel,
      .figure-card,
      .stat-block {{
        border-radius: 1.35rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: var(--panel-soft);
      }}

      .panel {{ padding: 1rem; }}
      .panel h2 {{
        margin: 0 0 0.45rem;
        font-size: 0.96rem;
      }}

      .bullet-list {{
        margin: 0;
        padding-left: 1.1rem;
      }}

      .bullet-list li + li {{ margin-top: 0.45rem; }}

      .facts .fact {{
        padding: 0.95rem 1rem;
        border-radius: 1.15rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: rgba(255, 255, 255, 0.04);
      }}

      .fact span {{
        display: block;
        margin-bottom: 0.3rem;
        font-size: 0.76rem;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: var(--muted);
      }}

      .fact strong {{
        font-size: 0.96rem;
        line-height: 1.5;
      }}

      .links {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
        margin-top: 1rem;
      }}

      .links a {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.8rem 1rem;
        border-radius: 999px;
        border: 1px solid rgba(255, 255, 255, 0.14);
        background: rgba(255, 255, 255, 0.05);
        font-weight: 700;
      }}

      .visual-column {{
        display: grid;
        gap: 0.95rem;
      }}

      .figure-card {{
        display: grid;
        place-items: center;
        min-height: 360px;
        padding: 1rem;
        overflow: hidden;
      }}

      .figure-card img {{
        width: 100%;
        max-height: 72vh;
        object-fit: contain;
        border-radius: 1rem;
        background: rgba(255, 255, 255, 0.03);
      }}

      .figure-fallback {{
        font-weight: 700;
        text-align: center;
      }}

      .group-list {{
        list-style: none;
        padding: 0;
        margin: 0;
        display: grid;
        gap: 0.7rem;
      }}

      .group-list li {{
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        padding: 0.85rem 1rem;
        border-radius: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        background: rgba(255, 255, 255, 0.04);
      }}

      .group-list strong {{ color: var(--text); }}

      @media (max-width: 980px) {{
        .cover-grid,
        .slide-grid,
        .summary-grid,
        .detail-grid,
        .facts {{
          grid-template-columns: 1fr;
        }}

        .figure-card {{
          min-height: 260px;
        }}
      }}

      @media (max-width: 720px) {{
        .topbar {{
          align-items: flex-start;
          flex-direction: column;
        }}

        .toplinks {{
          justify-content: flex-start;
        }}
      }}
    </style>
  </head>
  <body>
    <header class="topbar">
      <div class="brand">robotics-paper-notes / Non-AI 60</div>
      <div class="toplinks">
        <a href="../../index.html">Top 12</a>
        <a href="./non-ai.md">Markdown list</a>
        <a href="./index.md">All arXiv 521</a>
        <a href="https://github.com/rsasaki0109/robotics-paper-notes">GitHub</a>
        <div class="counter"><strong id="counter">00 / {total}</strong><span id="counter-group">cover</span></div>
      </div>
    </header>
    <main class="feed" id="feed">
      <section class="slide cover" data-index="0" data-group="cover">
        <div class="card">
          <div class="eyebrow">ICRA 2025 / public arXiv / non-AI first</div>
          <h1 class="hero-title">Non-AI 60 feed</h1>
          <p class="lead">
            60 本の Non-AI 論文を、代表 figure と主要ポイント付きで 1 論文 1 画面に並べた feed。
            Top 12 より広く、markdown list より深く眺めるためのページです。
          </p>
          <div class="cover-grid">
            <section class="panel">
              <h2>このページの見方</h2>
              <ul class="bullet-list">
                <li>左側で TL;DR / 問題設定 / 新規性 / 手法をざっと確認</li>
                <li>右側で representative figure を見て、論文の絵としての輪郭を掴む</li>
                <li>刺さったものだけ detail note と arXiv に飛ぶ</li>
              </ul>
            </section>
            <section class="panel">
              <h2>Topic spread</h2>
              <ul class="group-list">
                {cover_groups}
              </ul>
            </section>
          </div>
        </div>
      </section>
{''.join(slides)}
    </main>
    <script>
      const slides = [...document.querySelectorAll('.slide[data-index]')];
      const counter = document.getElementById('counter');
      const counterGroup = document.getElementById('counter-group');
      const observer = new IntersectionObserver((entries) => {{
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (!visible) return;
        const index = Number(visible.target.dataset.index || 0);
        const group = visible.target.dataset.group || 'cover';
        counter.textContent = index === 0 ? '00 / {total}' : `${{String(index).padStart(2, '0')}} / {total}`;
        counterGroup.textContent = group;
      }}, {{ threshold: [0.35, 0.6, 0.85] }});
      slides.forEach((slide) => observer.observe(slide));
    </script>
  </body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Build ICRA 2025 Non-AI feed page from markdown notes and figure manifest.")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--list-path", required=True, help="Markdown list of target papers")
    parser.add_argument("--manifest-path", required=True, help="Figure manifest JSON path")
    parser.add_argument("--output-path", required=True, help="HTML output path")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest = load_manifest((root / args.manifest_path).resolve())
    papers = parse_list(root, (root / args.list_path).resolve(), manifest)
    output_path = (root / args.output_path).resolve()
    output_path.write_text(build_html(papers), encoding="utf-8")


if __name__ == "__main__":
    main()
