# Acoustic Wave Manipulation through Sparse Robotic Actuation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation 2 |
| arXiv | [http://arxiv.org/abs/2502.08784](http://arxiv.org/abs/2502.08784) |
| Authors | Shah, Tristan, Smilovich, Noam, Amirkulova, Feruza, Gerges, Samer, Tiomkin, Stas |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this work, we explore a more general problem: the manipulation of acoustic waves, which are partially observed by a robot capable of influencing the waves through spatially sparse actuators.
- Recent advancements in robotics, control, and machine learning have facilitated progress in the challenging area of object manipulation.
- Furthermore our proposed method is competitive with a classical semi-analytical method in acoustics research on the demonstrated tasks.

## Task

* Motion Planning
* Control
* Manipulation

## Keywords

* Manipulation Planning / Model Learning for Control

## AI依存度

* Hybrid

## 何を解決？

* In this work, we explore a more general problem: the manipulation of acoustic waves, which are partially observed by a robot capable of influencing the waves through spatially sparse actuators.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* Recent advancements in robotics, control, and machine learning have facilitated progress in the challenging area of object manipulation.

## どこが強い？

* Furthermore our proposed method is competitive with a classical semi-analytical method in acoustics research on the demonstrated tasks.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* The proposed method is better in terms of a solution quality and computational complexity as compared to a state-of-the-art learning based method for manipulation of dynamical systems governed by partial differential equations.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: planning, control, limited direct use; integration pattern reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
