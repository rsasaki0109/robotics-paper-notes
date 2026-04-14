# A Data-Driven Contact Estimation Method for Wheeled-Biped Robots

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | State Estimation |
| arXiv | [http://arxiv.org/abs/2410.12345](http://arxiv.org/abs/2410.12345) |
| Authors | Gökbakan, Umit Bora, Dümbgen, Frederike, Caron, Stephane |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Contact estimation is a key ability for limbed robots, where making and breaking contacts has a direct impact on state estimation and balance control.
- We design a contact estimator that is suitable for the emerging wheeled-biped robot types that do not have these features.
- We evaluate this approach in extensive real-robot and simulation experiments.

## Task

* Control
* State Estimation
* Legged Robotics

## Keywords

* Contact Modeling / Legged Robots / Probabilistic Inference

## AI依存度

* Hybrid

## 何を解決？

* Contact estimation is a key ability for limbed robots, where making and breaking contacts has a direct impact on state estimation and balance control.

## 何が新しい？

* We design a contact estimator that is suitable for the emerging wheeled-biped robot types that do not have these features.

## どうやってる？

* Contact estimation is a key ability for limbed robots, where making and breaking contacts has a direct impact on state estimation and balance control.

## どこが強い？

* To this end, we propose a Bayes filter in which update steps are learned from real-robot torque measurements while prediction steps rely on inertial measurements.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Existing approaches typically rely on gate-cycle priors or designated contact sensors.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: control, state estimation / localization, limited direct use; estimator / controller design reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
