# Interactive OT Gym: A Reinforcement Learning-Based Interactive Optical Tweezer (OT)-Driven Microrobotics Simulation Platform

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Micro/Nano Robots |
| arXiv | [http://arxiv.org/abs/2505.20751](http://arxiv.org/abs/2505.20751) |
| Authors | Zongcai, Tan, Zhang, Dandan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- However, controlling conventional multi-trap OT to achieve cooperative manipulation of multiple complex-shaped microrobots in dynamic environments poses a significant challenge.
- To address this, we introduce Interactive OT Gym, a reinforcement learning (RL)-based simulation platform designed for OT-driven microrobotics.
- We evaluated the effectiveness of our platform using a cell manipulation task.

## Task

* Control
* Manipulation

## Keywords

* Automation at Micro-Nano Scales / Micro/Nano Robots

## AI依存度

* Hybrid

## 何を解決？

* However, controlling conventional multi-trap OT to achieve cooperative manipulation of multiple complex-shaped microrobots in dynamic environments poses a significant challenge.

## 何が新しい？

* To address this, we introduce Interactive OT Gym, a reinforcement learning (RL)-based simulation platform designed for OT-driven microrobotics.

## どうやってる？

* However, controlling conventional multi-trap OT to achieve cooperative manipulation of multiple complex-shaped microrobots in dynamic environments poses a significant challenge.

## どこが強い？

* However, controlling conventional multi-trap OT to achieve cooperative manipulation of multiple complex-shaped microrobots in dynamic environments poses a significant challenge.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Experimental results show that our shared control system significantly improves micromanipulation performance, reducing task completion time by approximately 67% compared to using pure human or RL control alone and achieving a 100% success rate.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: control, limited direct use; integration pattern reference
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
