# robotics-paper-notes

ロボティクス論文（主に2025年）を高速に整理・理解するための、軽量な論文まとめリポジトリです。実験や実装は行わず、読解・要点整理・自分の解釈の言語化に特化します。

## 対象分野

- SLAM
- GNSS
- LiDAR
- Intelligent Vehicles

## 運用ルール

- 1論文 = 1Markdownファイル
- 1論文は60分以内で読める粒度にする
- 完璧を目指さず、スピードと継続を優先する
- 要点整理だけで終わらせず、自分の解釈を必ず書く

## ディレクトリ構成

```text
.
├── index.md
├── papers/
│   ├── .gitkeep
│   └── index.md
├── templates/
│   └── paper.md
└── README.md
```

- `papers/`: 論文ごとのまとめを1ファイルずつ追加する場所
- `templates/paper.md`: 論文メモの共通テンプレート
- `README.md`: このリポジトリの目的と運用ルール
- `index.md`: GitHub Pages 用のトップページ

## 使い方

1. 新しく読む論文ごとに `templates/paper.md` を複製する
2. `papers/` に 1論文 = 1Markdown で保存する
3. `TL;DR` と `自分の理解/感想` を最低限埋める

## 今後

今後 `papers/` に論文まとめを追加し、SLAM / GNSS / LiDAR / Intelligent Vehicles を中心に、継続的に整理していきます。
