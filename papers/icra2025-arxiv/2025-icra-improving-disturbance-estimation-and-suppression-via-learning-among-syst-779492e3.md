# Improving Disturbance Estimation and Suppression Via Learning among Systems with Mismatched Dynamics

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Planning and Control |
| arXiv | [http://arxiv.org/abs/2404.10231](http://arxiv.org/abs/2404.10231) |
| Authors | Modi, Harsh Jashvantbhai, Chen, Zhu, Liang, Xiao, Zheng, Minghui |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Iterative learning control (ILC) is a method for reducing system tracking or estimation errors over multiple iterations by using information from past iterations.
- The disturbance observer (DOB) is used to estimate and mitigate disturbances within the system, while the system is being affected by them.
- ILC enhances system performance by introducing a feedforward signal in each iteration.

## Task

* Perception
* Motion Planning
* Control
* Intelligent Vehicles

## Keywords

* Aerial Systems: Applications / Motion Control

## AI依存度

* Hybrid

## 何を解決？

* Iterative learning control (ILC) is a method for reducing system tracking or estimation errors over multiple iterations by using information from past iterations.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* Iterative learning control (ILC) is a method for reducing system tracking or estimation errors over multiple iterations by using information from past iterations.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: perception, planning, control
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
