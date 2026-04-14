# Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Mechanism Design and Control |
| arXiv | [http://arxiv.org/abs/2503.17678](http://arxiv.org/abs/2503.17678) |
| Authors | Zhou, Hao, Zhang, Yanze, Luo, Wenhao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- An important challenge is accurately quantifying the uncertainty of unknown models to generate provably safe control policies that facilitate the gathering of informative data, thereby achieving both safe and optimal policies.
- In this paper, we propose a provably sample efficient episodic safe learning framework that remains robust across various model choices with quantified uncertainty for online control tasks.
- Theoretical proofs and simulation results are provided to demonstrate the effectiveness and efficiency of the proposed framework.

## Task

* GNSS Fusion
* Motion Planning
* Control

## Keywords

* Robot Safety / Model Learning for Control / Integrated Planning and Learning

## AI依存度

* Hybrid

## 何を解決？

* An important challenge is accurately quantifying the uncertainty of unknown models to generate provably safe control policies that facilitate the gathering of informative data, thereby achieving both safe and optimal policies.

## 何が新しい？

* In this paper, we propose a provably sample efficient episodic safe learning framework that remains robust across various model choices with quantified uncertainty for online control tasks.

## どうやってる？

* Safety is a critical concern in learning-enabled autonomous systems especially when deploying these systems in real-world scenarios.

## どこが強い？

* Theoretical proofs and simulation results are provided to demonstrate the effectiveness and efficiency of the proposed framework.

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
* どのモジュールに効くか: localization / gnss integration, planning, control
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
