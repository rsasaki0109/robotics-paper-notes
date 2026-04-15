# Multi-Layered Safety of Redundant Robot Manipulators Via Task-Oriented Planning and Control

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Safety and Control in HRI |
| arXiv | [http://arxiv.org/abs/2410.17742](http://arxiv.org/abs/2410.17742) |
| Authors | Jia, Xinyu;Wang, Wenxin;Yang, Jun;Pan, Yongping;Yu, Haoyong |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Ensuring safety is crucial to promote the application of robot manipulators in open workspaces.
- Factors such as sensor errors or unpredictable collisions make the environment full of uncertainties.
- In this work, we investigate these potential safety challenges on redundant robot manipulators, and propose a task-oriented planning and control framework to achieve multi-layered safety while maintaining efficient task execution.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Manipulation

## Keywords

* Safety in HRI
* Collision Avoidance
* Motion Control

## AI依存度

* Non-AI

## 何を解決？

* Ensuring safety is crucial to promote the application of robot manipulators in open workspaces.

## 何が新しい？

* In this work, we investigate these potential safety challenges on redundant robot manipulators, and propose a task-oriented planning and control framework to achieve multi-layered safety while maintaining efficient task execution.

## どうやってる？

* Our approach consists of two main parts: a task-oriented trajectory planner based on multiple-shooting model predictive control (MPC) method, and a torque controller that allows safe and efficient collision reaction using only proprioceptive data.

## どこが強い？

* Through extensive simulations and real-hardware experiments, we demonstrate that the proposed framework can effectively handle uncertain static or dynamic obstacles, and perform disturbance resistance in manipulation tasks when unforeseen contacts occur.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this work, we investigate these potential safety challenges on redundant robot manipulators, and propose a task-oriented planning and control framework to achieve multi-layered safety while maintaining efficient task execution.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
