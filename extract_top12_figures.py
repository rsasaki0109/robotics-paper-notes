#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    cmd = [
        sys.executable,
        str(root / "extract_paper_figures.py"),
        "--root",
        str(root),
        "--index-path",
        "index.html",
        "--asset-dir",
        "assets/figures/icra2025-top12",
        "--manifest-path",
        "assets/figures/icra2025-top12/manifest.json",
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
