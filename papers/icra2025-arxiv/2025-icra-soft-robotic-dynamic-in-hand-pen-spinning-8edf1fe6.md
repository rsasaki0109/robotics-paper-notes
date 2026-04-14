# Soft Robotic Dynamic In-Hand Pen Spinning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Soft Robotic Grasping 1 |
| arXiv | [http://arxiv.org/abs/2411.12734](http://arxiv.org/abs/2411.12734) |
| Authors | Yao, Yunchao, Yoo, Uksang, Oh, Jean, Atkeson, Christopher, Ichnowski, Jeffrey |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Dynamic in-hand manipulation remains a challenging task for soft robotic systems that have demonstrated advantages in safe compliant interactions but struggle with high-speed dynamic tasks.
- In this work, we present SoftSpin, a system for dynamic spinning using a soft and compliant robotic hand.
- After 130 sampled actions, SoftSpin achieves 100 % success rate across three pens with different weights and weight distributions, demonstrating the systems generalizability and robustness to changes in object properties.

## Task

* Control
* Manipulation

## Keywords

* In-Hand Manipulation / Modeling / Control / and Learning for Soft Robots / Dexterous Manipulation

## AI依存度

* Hybrid

## 何を解決？

* Dynamic in-hand manipulation remains a challenging task for soft robotic systems that have demonstrated advantages in safe compliant interactions but struggle with high-speed dynamic tasks.

## 何が新しい？

* In this work, we present SoftSpin, a system for dynamic spinning using a soft and compliant robotic hand.

## どうやってる？

* Unlike previous works that rely on quasi-static actions and precise object models, the proposed system learns to spin a pen through trial-and-error using only real-world data without requiring explicit prior knowledge of the pens physical attributes.

## どこが強い？

* Dynamic in-hand manipulation remains a challenging task for soft robotic systems that have demonstrated advantages in safe compliant interactions but struggle with high-speed dynamic tasks.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Unlike previous works that rely on quasi-static actions and precise object models, the proposed system learns to spin a pen through trial-and-error using only real-world data without requiring explicit prior knowledge of the pens physical attributes.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: control, limited direct use; integration pattern reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
