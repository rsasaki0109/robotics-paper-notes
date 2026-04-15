# Hierarchical Contact-Rich Trajectory Optimization for Multi-Modal Manipulation Using Tight Convex Relaxations

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation Planning |
| arXiv | [http://arxiv.org/abs/2503.07963](http://arxiv.org/abs/2503.07963) |
| Authors | Shirai, Yuki;Raghunathan, Arvind;Jha, Devesh |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Designing trajectories for manipulation through contact is challenging as it requires reasoning of object & robot trajectories as well as complex contact sequences simultaneously.
- In this paper, we present a novel framework for simultaneously designing trajectories of robots, objects, and contacts efficiently for contact-rich manipulation.
- We propose a hierarchical optimization framework where Mixed-Integer Linear Program (MILP) selects optimal contacts between robot & object using approximate dynamical constraints, and then a NonLinear Program (NLP) optimizes trajectory of the robot(s) and object considering full nonlinear constraints.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Manipulation

## Keywords

* Manipulation Planning
* Multi-Contact Whole-Body Motion Planning and Control
* Optimization and Optimal Control

## AI依存度

* Non-AI

## 何を解決？

* Designing trajectories for manipulation through contact is challenging as it requires reasoning of object & robot trajectories as well as complex contact sequences simultaneously.

## 何が新しい？

* We propose a hierarchical optimization framework where Mixed-Integer Linear Program (MILP) selects optimal contacts between robot & object using approximate dynamical constraints, and then a NonLinear Program (NLP) optimizes trajectory of the robot(s) and object considering full nonlinear constraints.

## どうやってる？

* In this paper, we present a novel framework for simultaneously designing trajectories of robots, objects, and contacts efficiently for contact-rich manipulation.

## どこが強い？

* We also demonstrate our framework in hardware experiments using a bimanual robot system.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a hierarchical optimization framework where Mixed-Integer Linear Program (MILP) selects optimal contacts between robot & object using approximate dynamical constraints, and then a NonLinear Program (NLP) optimizes trajectory of the robot(s) and object considering full nonlinear constraints.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
