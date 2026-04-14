# From Ceilings to Walls: Universal Dynamic Perching of Small Aerial Robots on Surfaces with Variable Orientations

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots 1 |
| arXiv | [http://arxiv.org/abs/2412.19765](http://arxiv.org/abs/2412.19765) |
| Authors | Habas, Bryan, Brown, Aaron C., Lee, Donghyeon, Goldman, Mitchell, Cheng, Bo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This work demonstrates universal dynamic perching capabilities for quadrotors of various sizes and on surfaces with different orientations.
- By employing a non-dimensionalization framework and deep reinforcement learning, we systematically assessed how robot size and surface orientation affect landing capabilities.
- We hypothesized that maintaining geometric proportions across different robot scales ensures consistent perching behavior, which was validated in both simulation and experimental tests.

## Task

* Aerial Robotics

## Keywords

* Aerial Systems: Applications / Surveillance Robotic Systems / AI-Enabled Robotics

## AI依存度

* Hybrid

## 何を解決？

* This work demonstrates universal dynamic perching capabilities for quadrotors of various sizes and on surfaces with different orientations.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* By employing a non-dimensionalization framework and deep reinforcement learning, we systematically assessed how robot size and surface orientation affect landing capabilities.

## どこが強い？

* This work demonstrates universal dynamic perching capabilities for quadrotors of various sizes and on surfaces with different orientations.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: out of direct Autoware scope, but architecture reference
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
