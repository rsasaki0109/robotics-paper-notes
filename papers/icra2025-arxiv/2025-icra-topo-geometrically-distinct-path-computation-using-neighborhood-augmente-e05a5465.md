# Topo-Geometrically Distinct Path Computation Using Neighborhood-Augmented Graph, and Its Application to Path Planning for a Tethered Robot in 3D

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 4 |
| arXiv | [http://arxiv.org/abs/2306.01203](http://arxiv.org/abs/2306.01203) |
| Authors | Sahin, Alp, Bhattacharya, Subhrajit |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we propose an approach to compute k geodesic paths using the concept of a novel neighborhood-augmented graph, on which graph search algorithms can compute multiple optimal paths that are topo-geometrically distinct.
- Many robotics applications benefit from being able to compute multiple geodesic paths in a given configuration space.
- We demonstrate the application of our algorithm to planning shortest traversible paths for a tethered robot in 3D with cable-length constraint.

## Task

* Motion Planning
* Control

## Keywords

* Motion and Path Planning / Optimization and Optimal Control / Foundations of Automation / Multi Path Planning

## AI依存度

* Non-AI

## 何を解決？

* Our approach does not require complex geometric constructions, and the resulting paths are not restricted to distinct topological classes, making the algorithm suitable for problems where finding and distinguishing between geodesic paths are of interest.

## 何が新しい？

* In this paper, we propose an approach to compute k geodesic paths using the concept of a novel neighborhood-augmented graph, on which graph search algorithms can compute multiple optimal paths that are topo-geometrically distinct.

## どうやってる？

* Existing paradigm is to use topological path planning, which can compute optimal paths in distinct topological classes.

## どこが強い？

* We demonstrate the application of our algorithm to planning shortest traversible paths for a tethered robot in 3D with cable-length constraint.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
