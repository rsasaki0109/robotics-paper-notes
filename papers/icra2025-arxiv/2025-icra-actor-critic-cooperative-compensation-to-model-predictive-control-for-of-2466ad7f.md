# Actor-Critic Cooperative Compensation to Model Predictive Control for Off-Road Autonomous Vehicles under Unknown Dynamics

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 2 |
| arXiv | [http://arxiv.org/abs/2503.00577](http://arxiv.org/abs/2503.00577) |
| Authors | Gupta, Prakhar, Smereka, Jonathon M., Jia, Yunyi |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This study presents an Actor-Critic Cooperative Compensated Model Predictive Controller (AC3MPC) designed to address unknown system dynamics.
- To avoid the difficulty of modeling highly complex dynamics and ensuring real-time control feasibility and performance, this work uses deep reinforcement learning with a model predictive controller in a cooperative framework to handle unknown dynamics.
- We evaluate this framework for off-road autonomous driving on unknown deformable terrains that represent sandy deformable soil, sandy and rocky soil, and cohesive clay-like deformable soil.

## Task

* Perception
* Control
* Intelligent Vehicles

## Keywords

* Machine Learning for Robot Control / Motion Control / Autonomous Vehicle Navigation

## AI依存度

* Hybrid

## 何を解決？

* This study presents an Actor-Critic Cooperative Compensated Model Predictive Controller (AC3MPC) designed to address unknown system dynamics.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* This study presents an Actor-Critic Cooperative Compensated Model Predictive Controller (AC3MPC) designed to address unknown system dynamics.

## どこが強い？

* Our findings demonstrate that our controller statistically outperforms standalone model-based and learning-based controllers by upto 29.2% and 10.2%.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* This framework generalized well over varied and previously unseen terrain characteristics to track longitudinal reference speeds with lower errors.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
