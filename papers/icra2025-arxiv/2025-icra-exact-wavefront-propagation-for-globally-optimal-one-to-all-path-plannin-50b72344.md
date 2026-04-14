# Exact Wavefront Propagation for Globally Optimal One-To-All Path Planning on 2D Cartesian Grids

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Path Planning 2 |
| arXiv | [http://arxiv.org/abs/2409.11545](http://arxiv.org/abs/2409.11545) |
| Authors | Ibrahim, Ibrahim, Gillis, Joris, Decré, Wilm, Swevers, Jan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper introduces an efficient mathcal{O}(n) compute and memory complexity algorithm for globally optimal path planning on 2D Cartesian grids.
- Through benchmarking against state-of-the-art any-angle path planners, we demonstrate that our method outperforms existing approaches in both speed and accuracy, particularly in cluttered environments.
- Unlike existing marching methods that rely on approximate discretized solutions to the Eikonal equation, our approach achieves exact wavefront propagation by pivoting the analytic distance function based on visibility.

## Task

* Motion Planning

## Keywords

* Motion and Path Planning / Path Planning for Multiple Mobile Robots or Agents / Computational Geometry

## AI依存度

* Non-AI

## 何を解決？

* Notably, our method inherently provides globally optimal paths to all grid points, eliminating the need for additional gradient descent steps per path query.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* Unlike existing marching methods that rely on approximate discretized solutions to the Eikonal equation, our approach achieves exact wavefront propagation by pivoting the analytic distance function based on visibility.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Through benchmarking against state-of-the-art any-angle path planners, we demonstrate that our method outperforms existing approaches in both speed and accuracy, particularly in cluttered environments.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
