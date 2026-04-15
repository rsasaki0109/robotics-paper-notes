# robotics-paper-notes

ロボティクス論文（主に2025年）を高速に整理・理解するための、軽量な論文まとめリポジトリです。実験や実装は行わず、読解・要点整理・自分の解釈の言語化に特化します。

まずは **AI偏重ではない論文**、つまり幾何・最適化・推定・制御・システム設計など、古典的かつ実装に近い知見を含む論文を優先して整理します。

現在、**ICRA 2025 の arXiv 公開済みと判定できた 521本** について abstract ベースの自動下書きを作成済みです。
さらに、**まず読むべき Non-AI Top 12** の curated feed と、**Non-AI 60 全体** を figure 付きで眺める縦スクロール feed も追加しています。どちらも **expanded 521 corpus を見直して再選定した curated subset** をベースにしています。

## 対象分野

中心テーマ:

- SLAM
- Localization
- GNSS
- LiDAR
- Intelligent Vehicles

関連して扱うテーマ:

- Perception
- Mapping
- Sensor Fusion
- Motion Planning
- Control
- Autonomous Driving

## 運用ルール

- 1論文 = 1Markdownファイル
- 1論文は60分以内で読める粒度にする
- 完璧を目指さず、スピードと継続を優先する
- 要点整理だけで終わらせず、自分の解釈を必ず書く
- まずは non-AI / classical / model-based な論文を優先する

## 優先して拾う論文

- 幾何ベースのSLAM / Visual Odometry / LiDAR Odometry
- 状態推定、GNSS統合、カルマンフィルタ、因子グラフ最適化
- 地図生成、キャリブレーション、センサアライメント
- Motion Planning / Trajectory Optimization / MPC
- 制御、システム統合、実運用で効く設計論

## ディレクトリ構成

```text
.
├── assets/
│   └── figures/
│       ├── icra2025-non-ai/
│       └── icra2025-top12/
├── build_icra2025_arxiv_dataset.py
├── build_non_ai_selection.py
├── build_non_ai_feed.py
├── data/
│   └── icra2025/
│       ├── ICRA2025_Paper_List_with_Abstract.csv
│       ├── icra2025_arxiv_matches.csv
│       ├── icra2025_arxiv_matches.json
│       └── icra2025_non_ai60_selection.json
├── extract_paper_figures.py
├── extract_top12_figures.py
├── index.html
├── index.md
├── papers/
│   ├── .gitkeep
│   ├── icra2025-arxiv/
│   │   ├── index.md
│   │   ├── non-ai-feed.html
│   │   ├── non-ai-top.md
│   │   └── non-ai.md
│   └── index.md
├── templates/
│   └── paper.md
└── README.md
```

- `assets/figures/icra2025-non-ai/`: Non-AI 60 用に arXiv source から自動抽出した図
- `assets/figures/icra2025-top12/`: Top 12 用に arXiv source から自動抽出した図
- `build_icra2025_arxiv_dataset.py`: ICRA 2025 CSV と arXiv ICRA query corpus から note / index / match data を再構築するスクリプト
- `build_non_ai_selection.py`: expanded 521 corpus から Non-AI 60 / Top 12 を再選定するスクリプト
- `build_non_ai_feed.py`: Non-AI 60 の note と manifest から feed HTML を生成するスクリプト
- `data/icra2025/`: 元 CSV と再構築した arXiv match data
- `extract_paper_figures.py`: 任意の論文セットから代表図を自動抽出して PNG 化するスクリプト
- `extract_top12_figures.py`: Top 12 向けの互換ラッパー
- `papers/`: 論文ごとのまとめを1ファイルずつ追加する場所
- `papers/icra2025-arxiv/`: ICRA 2025 の arXiv 公開済み論文の自動下書き
- `papers/icra2025-arxiv/non-ai-feed.html`: Non-AI 60 を figure 付き縦 feed で眺めるページ
- `templates/paper.md`: 論文メモの共通テンプレート
- `README.md`: このリポジトリの目的と運用ルール
- `index.html`: GitHub Pages 用の縦スクロール richer feed（自動抽出図つき）
- `index.md`: GitHub 上で読むための案内ページ

## 現在の入口

- `papers/icra2025-arxiv/index.md`: ICRA 2025 arXiv 下書き 521本の一覧
- `papers/icra2025-arxiv/non-ai.md`: expanded 521 corpus から再選定した Non-AI 60 本の優先読みリスト
- `papers/icra2025-arxiv/non-ai-top.md`: 最初に読むべき Top 12
- `papers/icra2025-arxiv/non-ai-feed.html`: Non-AI 60 全体を figure 付きで眺める feed
- `index.html`: GitHub Pages のトップで開く 1スライド richer feed（自動抽出図つき）

## 使い方

1. 新しく読む論文ごとに `templates/paper.md` を複製する
2. `papers/` に 1論文 = 1Markdown で保存する
3. `TL;DR` と `自分の理解/感想` を最低限埋める

## 今後

今後 `papers/` に論文まとめを追加し、まずは non-AI な SLAM / Localization / GNSS / LiDAR / Planning / Control の論文から整理し、その後必要に応じて AI 系の論文も比較対象として扱います。ICRA 2025 については、arXiv 公開済み論文の下書きを順に精読版へ育てつつ、Non-AI 60 / Top 12 も必要に応じて見直していきます。
