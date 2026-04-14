# Learning Object Properties Using Robot Proprioception Via Differentiable Robot-Object Interaction

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning for Robot Control |
| arXiv | [http://arxiv.org/abs/2410.03920](http://arxiv.org/abs/2410.03920) |
| Authors | Chen, Peter Yichen, Liu, Chao, Ma, Pingchuan, Eastman, John, Rus, Daniela, Randle, Dylan Labatt, Ivanov, Yuri, Matusik, Wojciech |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Differentiable simulation has become a powerful tool for system identification.
- We demonstrate the effectiveness of our method on a low-cost robotic platform, achieving accurate mass and elastic modulus estimations of manipulated objects with just a few seconds of computation on a laptop.
- While prior work has focused on identifying robot properties using robot-specific data or object properties using object-specific data, our approach calibrates object properties by using information from the robot, without relying on data from the object itself.

## Task

* Perception
* Control

## Keywords

* Machine Learning for Robot Control / Sensorimotor Learning / Learning from Demonstration

## AI依存度

* Hybrid

## 何を解決？

* Differentiable simulation has become a powerful tool for system identification.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* While prior work has focused on identifying robot properties using robot-specific data or object properties using object-specific data, our approach calibrates object properties by using information from the robot, without relying on data from the object itself.

## どこが強い？

* Differentiable simulation has become a powerful tool for system identification.

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
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
