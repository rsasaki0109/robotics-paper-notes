# Dynamic Non-Prehensile Object Transport Via Model-Predictive Reinforcement Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 3 |
| arXiv | [http://arxiv.org/abs/2412.00086](http://arxiv.org/abs/2412.00086) |
| Authors | Jawale, Neel Anand, Boots, Byron, Sundaralingam, Balakumar, Bhardwaj, Mohak |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We investigate the problem of teaching a robot manipulator to perform dynamic non-prehensile object transport, also known as the robot waiter task, from a limited set of real-world demonstrations.
- We propose an approach that combines batch reinforcement learning (RL) with model-predictive control (MPC) by pretraining an ensemble of value functions from demonstration data, and utilizing them online within an uncertainty-aware MPC scheme to ensure robustness to limited data coverage.
- We validate the proposed approach through extensive simulated and real-world experiments on a Franka Panda robot performing the robot waiter task and demonstrate robust deployment of value functions learned from 50-100 demonstrations.

## Task

* Control
* Manipulation

## Keywords

* Reinforcement Learning / Optimization and Optimal Control / Learning from Demonstration

## AI依存度

* Hybrid

## 何を解決？

* We investigate the problem of teaching a robot manipulator to perform dynamic non-prehensile object transport, also known as the robot waiter task, from a limited set of real-world demonstrations.

## 何が新しい？

* We propose an approach that combines batch reinforcement learning (RL) with model-predictive control (MPC) by pretraining an ensemble of value functions from demonstration data, and utilizing them online within an uncertainty-aware MPC scheme to ensure robustness to limited data coverage.

## どうやってる？

* We propose an approach that combines batch reinforcement learning (RL) with model-predictive control (MPC) by pretraining an ensemble of value functions from demonstration data, and utilizing them online within an uncertainty-aware MPC scheme to ensure robustness to limited data coverage.

## どこが強い？

* We validate the proposed approach through extensive simulated and real-world experiments on a Franka Panda robot performing the robot waiter task and demonstrate robust deployment of value functions learned from 50-100 demonstrations.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: control, limited direct use; integration pattern reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
