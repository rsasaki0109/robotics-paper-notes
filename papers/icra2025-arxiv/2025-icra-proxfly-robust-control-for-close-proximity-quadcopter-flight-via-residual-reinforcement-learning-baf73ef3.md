# ProxFly: Robust Control for Close Proximity Quadcopter Flight Via Residual Reinforcement Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Learning 2 |
| arXiv | [http://arxiv.org/abs/2409.13193](http://arxiv.org/abs/2409.13193) |
| Authors | Zhang, Ruiqi;Zhang, Dingqi;Mueller, Mark Wilfried |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper proposes the ProxFly, a residual deep Reinforcement Learning (RL)-based controller for close proximity quadcopter flight.
- Specifically, we design a residual module on top of a cascaded controller (denoted as basic controller) to generate high-level control commands, which compensate for external disturbances and thrust loss caused by downwash effects from other quadcopters.
- First, our method takes only the ego state and controllers' commands as inputs and does not rely on any communication between quadcopters, thereby reducing the bandwidth requirement.

## Task

* Visual-Inertial
* Control
* Aerial Robotics

## Keywords

* Reinforcement Learning
* Aerial Systems: Mechanics and Control
* Robust/Adaptive Control

## AI依存度

* Hybrid

## 何を解決？

* This paper proposes the ProxFly, a residual deep Reinforcement Learning (RL)-based controller for close proximity quadcopter flight.

## 何が新しい？

* This paper proposes the ProxFly, a residual deep Reinforcement Learning (RL)-based controller for close proximity quadcopter flight.

## どうやってる？

* First, our method takes only the ego state and controllers' commands as inputs and does not rely on any communication between quadcopters, thereby reducing the bandwidth requirement.

## どこが強い？

* Finally, we show that ProxFly can be used for challenging quadcopter mid-air docking, where two quadcopters fly in extreme proximity, and strong airflow significantly disrupts flight.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This paper proposes the ProxFly, a residual deep Reinforcement Learning (RL)-based controller for close proximity quadcopter flight.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
