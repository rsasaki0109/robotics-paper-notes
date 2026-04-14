# CaDRE: Controllable and Diverse Generation of Safety-Critical Driving Scenarios Using Real-World Trajectories

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Safe Control 1 |
| arXiv | [http://arxiv.org/abs/2403.13208](http://arxiv.org/abs/2403.13208) |
| Authors | Huang, Peide, Ding, Wenhao, Stoler, Benjamin, Francis, Jonathan, Chen, Bingqing, Zhao, Ding |
| Source | ICRA 2025 / arXiv |

## TL;DR

- An outstanding challenge with simulation-based testing is the generation of safety-critical scenarios, which are essential to ensure that AVs can handle rare but potentially fatal situations.
- Simulation is an indispensable tool in the development and testing of autonomous vehicles (AVs), offering an efficient and safe alternative to road testing.
- The results demonstrate superior performance in generating diverse and high-quality scenarios with greater sample efficiency than existing reinforcement learning (RL) and sampling-based methods.

## Task

* Control
* Intelligent Vehicles

## Keywords

* Robot Safety / Intelligent Transportation Systems / Autonomous Vehicle Navigation

## AI依存度

* Hybrid

## 何を解決？

* An outstanding challenge with simulation-based testing is the generation of safety-critical scenarios, which are essential to ensure that AVs can handle rare but potentially fatal situations.

## 何が新しい？

* This paper addresses this challenge by introducing a novel framework, CaDRE, to generate realistic, diverse, and controllable safety-critical scenarios.

## どうやってる？

* This paper addresses this challenge by introducing a novel framework, CaDRE, to generate realistic, diverse, and controllable safety-critical scenarios.

## どこが強い？

* Simulation is an indispensable tool in the development and testing of autonomous vehicles (AVs), offering an efficient and safe alternative to road testing.

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
* どのモジュールに効くか: control, planning / control / perception
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
