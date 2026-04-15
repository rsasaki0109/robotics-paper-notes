# Learning Quadrotor Control from Visual Features Using Differentiable Simulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Planning and Control |
| arXiv | [http://arxiv.org/abs/2410.15979](http://arxiv.org/abs/2410.15979) |
| Authors | Heeg, Johannes;Song, Yunlong;Scaramuzza, Davide |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The sample inefficiency of reinforcement learning (RL) remains a significant challenge in robotics.
- RL requires large-scale simulation and can still cause long training times, slowing research and innovation.
- This issue is particularly pronounced in vision-based control tasks where reliable state estimates are not accessible.

## Task

* Visual-Inertial
* Control
* Aerial Robotics

## Keywords

* Aerial Systems: Mechanics and Control
* Machine Learning for Robot Control
* Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* The sample inefficiency of reinforcement learning (RL) remains a significant challenge in robotics.

## 何が新しい？

* Second, combining state representation learning with policy learning enhances convergence speed in tasks where only visual features are observable.

## どうやってる？

* These findings highlight the potential of differentiable simulation for real-world robotics and offer a compelling alternative to conventional RL approaches.

## どこが強い？

* This work demonstrates the great potential of differentiable simulation for learning quadrotor control.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Second, combining state representation learning with policy learning enhances convergence speed in tasks where only visual features are observable.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
