# Long-Term Upper-Limb Prosthesis Myocontrol Via High-Density sEMG and Incremental Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Wearable Robotics 2 |
| arXiv | [http://arxiv.org/abs/2412.16271](http://arxiv.org/abs/2412.16271) |
| Authors | Di Domenico, Dario, Boccardo, Nicolò, Marinelli, Andrea, Canepa, Michele, Gruppioni, Emanuele, Laffranchi, Matteo, Camoriano, Raffaello |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this work, we address both challenges by introducing a novel myoelectric prosthetic system integrating a high density-sEMG (HD-sEMG) setup and incremental learning methods to accurately control 7 motions of the Hannes prosthesis.
- First, we present a newly designed, compact HD-sEMG interface equipped with 64 dry electrodes positioned over the forearm.
- Noninvasive human-machine interfaces such as surface electromyography (sEMG) have long been employed for controlling robotic prostheses.

## Task

* Perception
* Control

## Keywords

* Prosthetics and Exoskeletons / Intention Recognition / Incremental Learning

## AI依存度

* Hybrid

## 何を解決？

* In this work, we address both challenges by introducing a novel myoelectric prosthetic system integrating a high density-sEMG (HD-sEMG) setup and incremental learning methods to accurately control 7 motions of the Hannes prosthesis.

## 何が新しい？

* In this work, we address both challenges by introducing a novel myoelectric prosthetic system integrating a high density-sEMG (HD-sEMG) setup and incremental learning methods to accurately control 7 motions of the Hannes prosthesis.

## どうやってる？

* Noninvasive human-machine interfaces such as surface electromyography (sEMG) have long been employed for controlling robotic prostheses.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

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
* どのモジュールに効くか: perception, control
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
