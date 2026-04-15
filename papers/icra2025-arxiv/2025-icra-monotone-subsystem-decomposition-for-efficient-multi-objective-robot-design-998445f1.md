# Monotone Subsystem Decomposition for Efficient Multi-Objective Robot Design

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | System Design |
| arXiv | [http://arxiv.org/abs/2505.11624](http://arxiv.org/abs/2505.11624) |
| Authors | Wilhelm, Andrew;Napp, Nils |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Automating design minimizes errors, accelerates the design process, and reduces cost.
- However, automating robot design is challenging due to recursive constraints, multiple design objectives, and cross-domain design complexity possibly spanning multiple abstraction layers.
- Here we look at the problem of component selection, a combinatorial optimization problem in which a designer, given a robot model, must select compatible components from an extensive catalog.

## Task

* Control

## Keywords

* Methods and Tools for Robot System Design
* Optimization and Optimal Control
* Formal Methods in Robotics and Automation

## AI依存度

* Non-AI

## 何を解決？

* Automating design minimizes errors, accelerates the design process, and reduces cost.

## 何が新しい？

* In this paper, we extend our previous constraint programming approach to multi-objective design problems and propose the novel technique of monotone subsystem decomposition to efficiently compute a Pareto front of solutions for large-scale problems.

## どうやってる？

* Using an example quadcopter design problem, we compare our method to a linear programming approach and demonstrate our method scales better for large catalogs, solving a multi-objective problem of 10^25 component combinations in seconds.

## どこが強い？

* Using an example quadcopter design problem, we compare our method to a linear programming approach and demonstrate our method scales better for large catalogs, solving a multi-objective problem of 10^25 component combinations in seconds.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we extend our previous constraint programming approach to multi-objective design problems and propose the novel technique of monotone subsystem decomposition to efficiently compute a Pareto front of solutions for large-scale problems.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
