#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover - optional dependency
    Image = None


SOURCE_EXTS = {".png", ".jpg", ".jpeg", ".pdf", ".eps", ".ps"}
PRIORITY_KEYS = [
    "overview",
    "system",
    "pipeline",
    "framework",
    "architecture",
    "teaser",
    "method",
    "approach",
    "main",
    "main_figure",
    "flow",
    "graphical",
    "problem_structure",
    "timeoffset",
    "misalignment",
    "linearization",
    "fig1",
    "figure1",
]
PENALTY_KEYS = [
    "bio",
    "author",
    "logo",
    "admin",
    "review",
    "rebuttal",
    "hist",
    "plot",
    "error",
    "vel",
    "trajectory",
    "dataset",
    "results",
    "ablation",
    "appendix",
    "supp",
    "supplement",
    "table",
    "legend",
]


def download(url: str, path: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=90) as response:
        path.write_bytes(response.read())


def extract_source(source_path: Path, out_dir: Path) -> None:
    with tarfile.open(source_path, "r:*") as archive:
        archive.extractall(out_dir)


def score_candidate(path: Path, root: Path) -> float:
    rel = path.relative_to(root).as_posix().lower()
    score = min(path.stat().st_size / 50_000, 12)
    if "/fig" in rel or "/image" in rel or "/pic" in rel:
        score += 3
    if "/sub/" in rel:
        score -= 4
    for key in PRIORITY_KEYS:
        if key in rel:
            score += 12
    for key in PENALTY_KEYS:
        if key in rel:
            score -= 10
    return score


def convert_to_png(source_path: Path, out_path: Path) -> None:
    ext = source_path.suffix.lower()
    if ext in {".png", ".jpg", ".jpeg"}:
        shutil.copy2(source_path, out_path)
        return
    if ext == ".pdf":
        subprocess.run(
            ["pdftoppm", "-png", "-singlefile", "-r", "180", str(source_path), str(out_path.with_suffix(""))],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return
    if ext in {".eps", ".ps"}:
        subprocess.run(
            [
                "gs",
                "-dSAFER",
                "-dBATCH",
                "-dNOPAUSE",
                "-sDEVICE=pngalpha",
                "-r180",
                f"-sOutputFile={out_path}",
                str(source_path),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return
    raise RuntimeError(f"Unsupported conversion type: {source_path}")


def extract_best_from_source(src_dir: Path, out_path: Path) -> str | None:
    candidates = sorted(
        (
            (score_candidate(path, src_dir), path)
            for path in src_dir.rglob("*")
            if path.is_file() and path.suffix.lower() in SOURCE_EXTS
        ),
        key=lambda item: item[0],
        reverse=True,
    )
    tmp_candidate = out_path.parent / f"{out_path.stem}-tmp.png"
    for _, candidate in candidates[:20]:
        tmp_candidate.unlink(missing_ok=True)
        try:
            convert_to_png(candidate, tmp_candidate)
        except Exception:
            continue
        if tmp_candidate.exists() and tmp_candidate.stat().st_size > 15_000:
            shutil.move(tmp_candidate, out_path)
            return candidate.relative_to(src_dir).as_posix()
    return None


def extract_fallback_from_pdf(pdf_path: Path, out_path: Path) -> str:
    tmp_prefix = out_path.parent / f"{out_path.stem}-pdfimg"
    subprocess.run(
        ["pdfimages", "-f", "1", "-l", "3", "-png", str(pdf_path), str(tmp_prefix)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    pngs = sorted(out_path.parent.glob(f"{tmp_prefix.name}-*.png"))
    if pngs:
        best = max(pngs, key=lambda p: p.stat().st_size)
        shutil.move(best, out_path)
        for png in pngs:
            png.unlink(missing_ok=True)
        return "pdfimages-largest"
    subprocess.run(
        ["pdftoppm", "-f", "1", "-l", "1", "-png", "-singlefile", "-r", "150", str(pdf_path), str(out_path.with_suffix(""))],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return "pdf-first-page"


def normalize_image(path: Path) -> None:
    if Image is None:
        return
    with Image.open(path) as image:
        image = image.convert("RGB")
        image.thumbnail((1600, 1200))
        image.save(path, format="PNG", optimize=True)


def parse_homepage_index(root: Path, index_path: Path) -> list[dict[str, str]]:
    html = index_path.read_text(encoding="utf-8")
    pattern = re.compile(
        r'id: "(p\d+)",.*?title: "([^"]+)".*?detail: "([^"]+)".*?arxiv: "(https?://arxiv\.org/abs/([^"]+))"',
        re.S,
    )
    papers = []
    for match in pattern.finditer(html):
        detail_rel = match.group(3).removeprefix("./")
        papers.append(
            {
                "id": match.group(1),
                "title": match.group(2),
                "detail_path": detail_rel,
                "arxiv_url": match.group(4),
                "arxiv_id": match.group(5),
            }
        )
    if not papers:
        raise RuntimeError("Failed to parse papers from homepage index")
    return papers


def parse_markdown_list(root: Path, list_path: Path) -> list[dict[str, str]]:
    text = list_path.read_text(encoding="utf-8")
    pattern = re.compile(r"\[([^\]]+)\]\((\./[^)]+\.md)\)\s+—\s+\[arXiv\]\((https?://arxiv\.org/abs/([^)]+))\)")
    papers = []
    for match in pattern.finditer(text):
        detail_path = (list_path.parent / match.group(2)).resolve()
        rel_detail = detail_path.relative_to(root).as_posix()
        papers.append(
            {
                "id": Path(match.group(2)).stem,
                "title": match.group(1),
                "detail_path": rel_detail,
                "arxiv_url": match.group(3),
                "arxiv_id": match.group(4),
            }
        )
    if not papers:
        raise RuntimeError(f"Failed to parse papers from markdown list: {list_path}")
    return papers


def extract_figures(root: Path, papers: list[dict[str, str]], asset_dir: Path, manifest_path: Path) -> None:
    asset_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, str]] = []
    for paper in papers:
        out_path = asset_dir / f"{paper['id']}.png"
        with tempfile.TemporaryDirectory(prefix=f"{paper['id']}-") as tmp:
            tmp_dir = Path(tmp)
            source_path = tmp_dir / "source.bin"
            src_dir = tmp_dir / "src"
            pdf_path = tmp_dir / "paper.pdf"
            src_dir.mkdir()

            method = ""
            extracted_from = ""

            try:
                download(f"https://arxiv.org/e-print/{paper['arxiv_id']}", source_path)
                extract_source(source_path, src_dir)
                extracted_from = extract_best_from_source(src_dir, out_path) or ""
                method = "source"
            except Exception:
                extracted_from = ""

            if not out_path.exists():
                download(f"https://arxiv.org/pdf/{paper['arxiv_id']}.pdf", pdf_path)
                extracted_from = extract_fallback_from_pdf(pdf_path, out_path)
                method = "pdf-fallback"

            normalize_image(out_path)
            manifest.append(
                {
                    "id": paper["id"],
                    "title": paper["title"],
                    "detail_path": paper["detail_path"],
                    "arxiv_id": paper["arxiv_id"],
                    "arxiv_url": paper["arxiv_url"],
                    "asset": out_path.relative_to(root).as_posix(),
                    "method": method,
                    "extracted_from": extracted_from,
                }
            )
            print(f"{paper['id']}: {method} -> {extracted_from}")

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract representative figures from arXiv papers.")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--index-path", help="Homepage index.html to parse for paper data")
    parser.add_argument("--list-path", help="Markdown list page to parse for paper links and arXiv URLs")
    parser.add_argument("--asset-dir", required=True, help="Output directory for PNG figures")
    parser.add_argument("--manifest-path", required=True, help="Output JSON manifest path")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    root = Path(args.root).resolve()
    if bool(args.index_path) == bool(args.list_path):
        raise SystemExit("Specify exactly one of --index-path or --list-path")
    if args.index_path:
        papers = parse_homepage_index(root, (root / args.index_path).resolve())
    else:
        papers = parse_markdown_list(root, (root / args.list_path).resolve())
    extract_figures(root, papers, (root / args.asset_dir).resolve(), (root / args.manifest_path).resolve())


if __name__ == "__main__":
    main()
