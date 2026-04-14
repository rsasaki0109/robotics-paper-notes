# GeMuCo: Generalized Multisensory Correlational Model for Body Schema Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Representation Learning 2 |
| arXiv | [http://arxiv.org/abs/2409.06427](http://arxiv.org/abs/2409.06427) |
| Authors | Kawaharazuka, Kento, Okada, Kei, Inaba, Masayuki |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Humans can autonomously learn the relationship between sensation and motion in their own bodies, estimate and control their own body states, and move while continuously adapting to the current environment.
- In this study, we propose a Generalized Multisensory Correlational Model (GeMuCo), in which the robot itself acquires a body schema describing the correlation between sensors and actuators from its own experience, including model structures such as network input/output.
- We demonstrate the effectiveness of this method by applying it to tool-use co.

## Task

* Perception
* Control
* State Estimation
* Manipulation

## Keywords

* Learning from Experience / Software Architecture for Robotic and Automation / Cognitive Control Architectures

## AI依存度

* Hybrid

## 何を解決？

* Humans can autonomously learn the relationship between sensation and motion in their own bodies, estimate and control their own body states, and move while continuously adapting to the current environment.

## 何が新しい？

* In this study, we propose a Generalized Multisensory Correlational Model (GeMuCo), in which the robot itself acquires a body schema describing the correlation between sensors and actuators from its own experience, including model structures such as network input/output.

## どうやってる？

* Humans can autonomously learn the relationship between sensation and motion in their own bodies, estimate and control their own body states, and move while continuously adapting to the current environment.

## どこが強い？

* In addition, the network model does not adapt to changes in the robot's body, the tools that are grasped, or the environment, and there is no unified theory, not only for control but also for state estimation, anomaly detection, simulation, and so on.

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
* どのモジュールに効くか: perception, control, state estimation / localization
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
