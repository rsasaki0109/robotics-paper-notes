# Learning Robust Policies Via Interpretable Hamilton-Jacobi Reachability-Guided Disturbances

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Design and Robust Control |
| arXiv | [http://arxiv.org/abs/2409.19746](http://arxiv.org/abs/2409.19746) |
| Authors | Hu, Hanyang, Zhang, Xilun, Lyu, Xubo, Chen, Mo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- However, its vulnerability to unknown disturbances and adversarial attacks remains a significant challenge.
- In this paper, we propose a robust policy training framework that integrates model-based control principles with adversarial RL training to improve robustness without the need for external black-box adversaries.
- Deep Reinforcement Learning (RL) has shown remarkable success in robotics with complex and heterogeneous dynamics.

## Task

* Control
* Aerial Robotics

## Keywords

* Robust/Adaptive Control / Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* However, its vulnerability to unknown disturbances and adversarial attacks remains a significant challenge.

## 何が新しい？

* In this paper, we propose a robust policy training framework that integrates model-based control principles with adversarial RL training to improve robustness without the need for external black-box adversaries.

## どうやってる？

* Deep Reinforcement Learning (RL) has shown remarkable success in robotics with complex and heterogeneous dynamics.

## どこが強い？

* We evaluated its effectiveness across three distinct tasks: a reach-avoid game in both simulation and real-world settings, and a highly dynamic quadrotor stabilization task in simulation.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: control, out of direct Autoware scope, but architecture reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
