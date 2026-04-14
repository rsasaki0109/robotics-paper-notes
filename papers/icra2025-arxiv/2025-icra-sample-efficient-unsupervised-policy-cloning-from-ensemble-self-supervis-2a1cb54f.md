# Sample-Efficient Unsupervised Policy Cloning from Ensemble Self-Supervised Labeled Videos

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 3 |
| arXiv | [http://arxiv.org/abs/2412.10778](http://arxiv.org/abs/2412.10778) |
| Authors | Liu, Xin, Chen, Yaran, Li, Haoran |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we try to let machines replicate this efficient watching-and-learning process through Unsupervised Policy from Ensemble Self-supervised labeled Videos (UPESV), a novel framework to efficiently learn policies from action-free videos without rewards and any other expert supervision.
- Current advanced policy learning methodologies have demonstrated the ability to develop expert-level strategies when provided enough information.
- Extensive experiments in sixteen challenging procedurally generated environments demonstrate that the proposed UPESV achieves state-of-the-art interaction-limited policy learning performance (outperforming five current advanced baselines on 12/16 tasks) without exposure to any other supervision except for videos.

## Task

* Robotics

## Keywords

* Computer Vision for Automation / Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* Current advanced policy learning methodologies have demonstrated the ability to develop expert-level strategies when provided enough information.

## 何が新しい？

* In this paper, we try to let machines replicate this efficient watching-and-learning process through Unsupervised Policy from Ensemble Self-supervised labeled Videos (UPESV), a novel framework to efficiently learn policies from action-free videos without rewards and any other expert supervision.

## どうやってる？

* Current advanced policy learning methodologies have demonstrated the ability to develop expert-level strategies when provided enough information.

## どこが強い？

* Current advanced policy learning methodologies have demonstrated the ability to develop expert-level strategies when provided enough information.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Extensive experiments in sixteen challenging procedurally generated environments demonstrate that the proposed UPESV achieves state-of-the-art interaction-limited policy learning performance (outperforming five current advanced baselines on 12/16 tasks) without exposure to any other supervision except for videos.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: architecture reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
