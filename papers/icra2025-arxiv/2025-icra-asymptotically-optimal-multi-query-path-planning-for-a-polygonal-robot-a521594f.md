# Asymptotically-Optimal Multi-Query Path Planning for a Polygonal Robot

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 2 |
| arXiv | [http://arxiv.org/abs/2409.03920](http://arxiv.org/abs/2409.03920) |
| Authors | Zhang, Duo, Ye, Zihe, Yu, Jingjin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Shortest-path roadmaps, also known as reduced visibility graphs, provide a highly efficient multi-query method for computing optimal paths in two-dimensional environments.
- Combined with Minkowski sum computations, shortest-path roadmaps can compute optimal paths for a translating robot in 2D.
- The resulting algorithm, rotation-stacked visibility graph(RVG), is shown to be resolution-complete and asymptotically optimal.

## Task

* Motion Planning

## Keywords

* Motion and Path Planning / Constrained Motion Planning / Computational Geometry

## AI依存度

* Non-AI

## 何を解決？

* Shortest-path roadmaps, also known as reduced visibility graphs, provide a highly efficient multi-query method for computing optimal paths in two-dimensional environments.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* Extensive computational experiments show RVG significantly outperforms state-of-the-art single- and multi-query sampling-based methods on both computation time and solution optimality fronts.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: planning
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
