# Reference-Free Formula Drift with Reinforcement Learning: From Driving Data to Tire Energy-Inspired, Real-World Policies

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 3 |
| arXiv | [http://arxiv.org/abs/2410.20990](http://arxiv.org/abs/2410.20990) |
| Authors | Djeumou, Franck;Thompson, Michael;Suminaka, Makoto;Subosits, John |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The skill to drift a car--i.e., operate in a state of controlled oversteer like professional drivers-- could give future autonomous cars maximum flexibility when they need to retain control in adverse conditions or avoid collisions.
- We investigate real-time drifting strategies that put the car where needed while bypassing expensive trajectory optimization.
- To this end, we design a reinforcement learning agent that builds on the concept of tire energy absorption to autonomously drift through changing and complex waypoint configurations while safely staying within track bounds.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Perception

## Keywords

* Reinforcement Learning
* Model Learning for Control
* Planning under Uncertainty

## AI依存度

* Hybrid

## 何を解決？

* The skill to drift a car--i.e., operate in a state of controlled oversteer like professional drivers-- could give future autonomous cars maximum flexibility when they need to retain control in adverse conditions or avoid collisions.

## 何が新しい？

* To this end, we design a reinforcement learning agent that builds on the concept of tire energy absorption to autonomously drift through changing and complex waypoint configurations while safely staying within track bounds.

## どうやってる？

* We achieve zero-shot deployment on the car by training the agent in a simulation environment built on top of a neural stochastic differential equation vehicle model learned from pre-collected driving data.

## どこが強い？

* Experiments on a Toyota GR Supra and Lexus LC 500 show that the agent is capable of drifting smoothly through varying waypoint configurations with tracking error as low as 10 cm while stably pushing the vehicles to sideslip angles of up to 63°.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we design a reinforcement learning agent that builds on the concept of tire energy absorption to autonomously drift through changing and complex waypoint configurations while safely staying within track bounds.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
