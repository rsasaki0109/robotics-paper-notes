# Towards Real-Time Generation of Delay-Compensated Video Feeds for Outdoor Mobile Robot Teleoperation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Teleoperation |
| arXiv | [http://arxiv.org/abs/2409.09921](http://arxiv.org/abs/2409.09921) |
| Authors | Chakraborty, Neeloy, Fang, Yixiao, Schreiber, Andre, Ji, Tianchen, Huang, Zhe, Mihigo, Aganze, Wall, Cassidy, Almana, Abdulrahman, Driggs-Campbell, Katherine |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Teleoperation is an important technology to enable supervisors to control agricultural robots remotely.
- We propose a modular learning-based vision pipeline to generate delay-compensated images in real-time for supervisors.
- Our extensive offline evaluations demonstrate that our method generates more accurate images compared to state-of-the-art approaches in our setting.

## Task

* Perception
* Control

## Keywords

* Field Robots / Telerobotics and Teleoperation / Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* Teleoperation is an important technology to enable supervisors to control agricultural robots remotely.

## 何が新しい？

* We propose a modular learning-based vision pipeline to generate delay-compensated images in real-time for supervisors.

## どうやってる？

* Teleoperation is an important technology to enable supervisors to control agricultural robots remotely.

## どこが強い？

* Our extensive offline evaluations demonstrate that our method generates more accurate images compared to state-of-the-art approaches in our setting.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Our extensive offline evaluations demonstrate that our method generates more accurate images compared to state-of-the-art approaches in our setting.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: perception, control
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
