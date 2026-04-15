# Polyhedral Collision Detection Via Vertex Enumeration

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planning with Contact |
| arXiv | [http://arxiv.org/abs/2501.13201](http://arxiv.org/abs/2501.13201) |
| Authors | Cinar, Andrew;Zhao, Yue;Laine, Forrest |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Collision detection is a critical functionality for robotics.
- The degree to which objects collide cannot be represented as a continuously differentiable function for any shapes other than spheres.
- This paper proposes a framework for handling collision detection between polyhedral shapes.

## Task

* Motion Planning
* Perception

## Keywords

* Collision Avoidance
* Constrained Motion Planning

## AI依存度

* Non-AI

## 何を解決？

* Collision detection is a critical functionality for robotics.

## 何が新しい？

* This paper proposes a framework for handling collision detection between polyhedral shapes.

## どうやってる？

* To avoid relying on specialized bilevel solvers, our method exploits the fact that the signed distance is the minimal point of a convex region related to the two bodies.

## どこが強い？

* We demonstrate that our approach more reliably solves difficult collision detection problems with multiple obstacles than other methods, and is faster than existing methods in some cases.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This paper proposes a framework for handling collision detection between polyhedral shapes.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
