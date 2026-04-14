# ORB-SfMLearner: ORB-Guided Self-Supervised Visual Odometry with Selective Online Adaptation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Visual-Inertial Odometry |
| arXiv | [http://arxiv.org/abs/2409.11692](http://arxiv.org/abs/2409.11692) |
| Authors | Jin, Yanlin, Ju, Rui-Yang, Liu, Haojun, Zhong, Yuzhong |
| Source | ICRA 2025 / arXiv |

## TL;DR

- To address these challenges, we propose an Oriented FAST and Rotated BRIEF (ORB)-guided visual odometry with selective online adaptation named ORB-SfMLearner.
- We present a novel use of ORB features for learning-based ego-motion estimation, leading to more robust and accurate results.
- Experimental results on KITTI and vKITTI datasets show that our method outperforms previous state-of-the-art deep visual odometry methods in terms of ego-motion accuracy and generalizability.

## Task

* SLAM
* Localization
* Perception
* Intelligent Vehicles

## Keywords

* Deep Learning for Visual Perception / Computer Vision for Automation / SLAM

## AI依存度

* Hybrid

## 何を解決？

* To address these challenges, we propose an Oriented FAST and Rotated BRIEF (ORB)-guided visual odometry with selective online adaptation named ORB-SfMLearner.

## 何が新しい？

* To address these challenges, we propose an Oriented FAST and Rotated BRIEF (ORB)-guided visual odometry with selective online adaptation named ORB-SfMLearner.

## どうやってる？

* To address these challenges, we propose an Oriented FAST and Rotated BRIEF (ORB)-guided visual odometry with selective online adaptation named ORB-SfMLearner.

## どこが強い？

* We present a novel use of ORB features for learning-based ego-motion estimation, leading to more robust and accurate results.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Experimental results on KITTI and vKITTI datasets show that our method outperforms previous state-of-the-art deep visual odometry methods in terms of ego-motion accuracy and generalizability.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: localization / mapping, localization, perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
