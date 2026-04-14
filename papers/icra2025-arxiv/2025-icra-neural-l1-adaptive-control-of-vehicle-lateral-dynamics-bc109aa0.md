# Neural L1 Adaptive Control of Vehicle Lateral Dynamics

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Design and Robust Control |
| arXiv | [http://arxiv.org/abs/2405.16358](http://arxiv.org/abs/2405.16358) |
| Authors | Mukherjee, Pratik, Gonultas, Burak M, Poyrazoglu, Oguzhan Goktug, Isler, Volkan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We address the problem of stable and robust control of vehicles with lateral error dynamics for the application of lane keeping.
- In this work, we introduce a Neural L1 Adaptive controller which learns the uncertainties in the lateral error dynamics of a front-steered Ackermann vehicle and guarantees stability and robustness.
- Traditional linear feedback controllers achieve satisfactory tracking performance, however, they exhibit unstable behavior when uncertainties are induced into the system.

## Task

* Perception
* Motion Planning
* Control
* Intelligent Vehicles

## Keywords

* Robust/Adaptive Control / Machine Learning for Robot Control / Autonomous Vehicle Navigation

## AI依存度

* Hybrid

## 何を解決？

* We address the problem of stable and robust control of vehicles with lateral error dynamics for the application of lane keeping.

## 何が新しい？

* In this work, we introduce a Neural L1 Adaptive controller which learns the uncertainties in the lateral error dynamics of a front-steered Ackermann vehicle and guarantees stability and robustness.

## どうやってる？

* We address the problem of stable and robust control of vehicles with lateral error dynamics for the application of lane keeping.

## どこが強い？

* Traditional linear feedback controllers achieve satisfactory tracking performance, however, they exhibit unstable behavior when uncertainties are induced into the system.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Our contributions are threefold: i) We extend the theoretical results for guaranteed stability and robustness of conventional L1 Adaptive controllers to Neural L1 Adaptive controller; ii) We implement a Neural L1 Adaptive controller for the lane keeping application which learns uncertainties in the dynamics accurately; iii) We evaluate the performance of Neural L1 Adaptive controller on a physics-based simulator, PyBullet, and conduct extensive real-world experiments with the F1TENTH platform to demonstrate superior reference trajectory tracking performance of Neural L1 Adaptive controller compared to other state-of-the-art controllers, in the presence of uncertainties.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: perception, planning, control
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
