# Kinodynamic Model Predictive Control for Energy Efficient Locomotion of Legged Robots with Parallel Elasticity

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Model Predictive Control for Legged Robots 1 |
| arXiv | [http://arxiv.org/abs/2503.05666](http://arxiv.org/abs/2503.05666) |
| Authors | Zhuang, Yulun;Wang, Yichen;Ding, Yanran |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we introduce a kinodynamic model predictive control (MPC) framework that exploits unidirectional parallel springs (UPS) to improve the energy efficiency of dynamic legged robots.
- The proposed method employs a hierarchical control structure, where the solution of MPC with simplified dynamic models is used to warm-start the kinodynamic MPC, which accounts for nonlinear centroidal dynamics and kinematic constraints.
- The proposed approach enables energy efficient dynamic hopping on legged robots by using UPS to reduce peak motor torques and energy consumption during stance phases.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Legged Robotics

## Keywords

* Legged Robots
* Optimization and Optimal Control
* Compliant Joints and Mechanisms

## AI依存度

* Non-AI

## 何を解決？

* In this paper, we introduce a kinodynamic model predictive control (MPC) framework that exploits unidirectional parallel springs (UPS) to improve the energy efficiency of dynamic legged robots.

## 何が新しい？

* The proposed method employs a hierarchical control structure, where the solution of MPC with simplified dynamic models is used to warm-start the kinodynamic MPC, which accounts for nonlinear centroidal dynamics and kinematic constraints.

## どうやってる？

* The proposed method employs a hierarchical control structure, where the solution of MPC with simplified dynamic models is used to warm-start the kinodynamic MPC, which accounts for nonlinear centroidal dynamics and kinematic constraints.

## どこが強い？

* Additionally, preliminary hardware experiments show a 14.8% reduction in energy consumption.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* The proposed method employs a hierarchical control structure, where the solution of MPC with simplified dynamic models is used to warm-start the kinodynamic MPC, which accounts for nonlinear centroidal dynamics and kinematic constraints.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
