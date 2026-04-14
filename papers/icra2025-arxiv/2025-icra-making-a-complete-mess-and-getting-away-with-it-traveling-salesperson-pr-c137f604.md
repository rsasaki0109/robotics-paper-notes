# Making a Complete Mess and Getting Away with It: Traveling Salesperson Problems with Circle Placement Variants

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 4 |
| arXiv | [http://arxiv.org/abs/2410.08627](http://arxiv.org/abs/2410.08627) |
| Authors | Woller, David, Mansouri, Masoumeh, Kulich, Miroslav |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper explores a variation of the Traveling Salesperson Problem, where the agent places a circular obstacle next to each node once it visits it.
- We propose several novel solvers to address the TSP-CP, its variant tailored for Dubins vehicles, and a crucial subproblem known as the Traveling Salesperson Problem on self-deleting graphs (TSP-SD).
- Our extensive experimental results show that the proposed solvers outperform the current state-of-the-art on related problems in solution quality.

## Task

* Motion Planning
* Intelligent Vehicles

## Keywords

* Task and Motion Planning / Constrained Motion Planning / Computational Geometry

## AI依存度

* Non-AI

## 何を解決？

* This paper explores a variation of the Traveling Salesperson Problem, where the agent places a circular obstacle next to each node once it visits it.

## 何が新しい？

* We propose several novel solvers to address the TSP-CP, its variant tailored for Dubins vehicles, and a crucial subproblem known as the Traveling Salesperson Problem on self-deleting graphs (TSP-SD).

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* Our extensive experimental results show that the proposed solvers outperform the current state-of-the-art on related problems in solution quality.

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
* どのモジュールに効くか: planning, planning / control / perception
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
