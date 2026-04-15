# Safe Quadrotor Navigation Using Composite Control Barrier Functions

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Mechanics and Control 1 |
| arXiv | [http://arxiv.org/abs/2502.04101](http://arxiv.org/abs/2502.04101) |
| Authors | Harms, Marvin Chayton;Jacquet, Martin;Alexis, Kostas |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper introduces a safety filter to ensure collision avoidance for multirotor aerial robots.
- The proposed formalism leverages a single Composite Control Barrier Function from all position constraints acting on a third-order nonlinear representation of the robot's dynamics.
- We analyze the recursive feasibility of the safety filter under the composite constraint and demonstrate that the infeasible set is negligible.

## Task

* LiDAR
* Control
* Aerial Robotics
* Perception

## Keywords

* Aerial Systems: Mechanics and Control
* Aerial Systems: Perception and Autonomy

## AI依存度

* Non-AI

## 何を解決？

* This paper introduces a safety filter to ensure collision avoidance for multirotor aerial robots.

## 何が新しい？

* The proposed formalism leverages a single Composite Control Barrier Function from all position constraints acting on a third-order nonlinear representation of the robot's dynamics.

## どうやってる？

* The proposed method allows computational scalability against thousands of constraints and, thus, complex scenes with numerous obstacles.

## どこが強い？

* We experimentally demonstrate its ability to guarantee the safety of a quadrotor with an onboard LiDAR, operating in both indoor and outdoor cluttered environments against both naive and adversarial nominal policies.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* The proposed formalism leverages a single Composite Control Barrier Function from all position constraints acting on a third-order nonlinear representation of the robot's dynamics.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
