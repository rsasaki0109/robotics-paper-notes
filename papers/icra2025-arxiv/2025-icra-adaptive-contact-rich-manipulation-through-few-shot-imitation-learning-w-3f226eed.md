# Adaptive Contact-Rich Manipulation through Few-Shot Imitation Learning with Force-Torque Feedback and Pre-Trained Object Representations

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation 4 |
| arXiv | [http://arxiv.org/abs/2505.06451](http://arxiv.org/abs/2505.06451) |
| Authors | Tsuji, Chikaha, Coronado, Enrique, Osorio, Pablo, Venture, Gentiane |
| Source | ICRA 2025 / arXiv |

## TL;DR

- However, challenges arise from the need for extensive demonstrations and the disparity between training and real-world environments.
- To address these challenges, we propose a novel method that integrates real-time force-torque (FT) feedback with pre-trained object representations.
- In real-world experiments, our method achieved 96% accuracy in applying the average reference force, significantly outperforming the previous method that lacked an FT feedback loop, which only achieved 4% accuracy.

## Task

* Control
* Manipulation

## Keywords

* Deep Learning in Grasping and Manipulation / Imitation Learning / Force Control

## AI依存度

* Hybrid

## 何を解決？

* However, challenges arise from the need for extensive demonstrations and the disparity between training and real-world environments.

## 何が新しい？

* To address these challenges, we propose a novel method that integrates real-time force-torque (FT) feedback with pre-trained object representations.

## どうやってる？

* Imitation learning offers a pathway for robots to perform repetitive tasks, allowing humans to focus on more engaging and meaningful activities.

## どこが強い？

* In real-world experiments, our method achieved 96% accuracy in applying the average reference force, significantly outperforming the previous method that lacked an FT feedback loop, which only achieved 4% accuracy.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* This approach allows robots to dynamically adjust to previously unseen changes in surface heights and sponges' physical properties.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
