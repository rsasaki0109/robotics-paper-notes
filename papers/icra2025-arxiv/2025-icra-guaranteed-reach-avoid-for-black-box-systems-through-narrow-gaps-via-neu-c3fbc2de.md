# Guaranteed Reach-Avoid for Black-Box Systems through Narrow Gaps Via Neural Network Reachability

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Mechanism Design and Control |
| arXiv | [http://arxiv.org/abs/2409.13195](http://arxiv.org/abs/2409.13195) |
| Authors | Chung, Long Kiu, Jung, Wonsuhk, Pullabhotla, Srivatsank, Shinde, Parth Kishor, Sunil, Yadu Krishna, Kota, Saihari, Batista, Luis F. W., Pradalier, Cedric, Kousik, Shreyas |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In the classical reach-avoid problem, autonomous mobile robots are tasked to reach a goal while avoiding obstacles.
- However, it is difficult to provide guarantees on the robot's performance when the obstacles form a narrow gap and the robot is a black-box (i.e. the dynamics are not known analytically, but interacting with the system is cheap).
- The method extends the authors' prior Piecewise Affine Reach-avoid Computation (PARC) method to systems modeled by rectified linear unit (ReLU) neural networks, which are trained to represent parameterized trajectory data demonstrated by the robot.

## Task

* Motion Planning
* Control
* Intelligent Vehicles

## Keywords

* Robot Safety / Model Learning for Control / Motion Control

## AI依存度

* Hybrid

## 何を解決？

* In the classical reach-avoid problem, autonomous mobile robots are tasked to reach a goal while avoiding obstacles.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* NeuralPARC is shown to outperform PARC, generating provably-safe extreme vehicle drift parking maneuvers in simulations and in real life on a model car, as well as enabling safety on an autonomous surface vehicle (ASV) subjected to large disturbances and controlled by a deep reinforcement learning (RL) policy.

## どこが強い？

* The method extends the authors' prior Piecewise Affine Reach-avoid Computation (PARC) method to systems modeled by rectified linear unit (ReLU) neural networks, which are trained to represent parameterized trajectory data demonstrated by the robot.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
