# SuperQ-GRASP: Superquadrics-Based Grasp Pose Estimation on Larger Objects for Mobile-Manipulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation 3 |
| arXiv | [http://arxiv.org/abs/2411.04386](http://arxiv.org/abs/2411.04386) |
| Authors | Tu, Xun, Desingh, Karthik |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Grasp planning and estimation have been a long-standing research problem in robotics, with two main approaches to find graspable poses on the objects: 1) geometric approach, which relies on 3D models of objects and the gripper to estimate valid grasp poses, and 2) data-driven, learning-based approach, with models trained to identify grasp poses from raw sensor observations.
- The latter assumes comprehensive geometric coverage during the training phase.
- For more qualitative results, refer to the supplementary video and webpage https://bit.ly/3ZrOanU.

## Task

* Localization
* Perception
* Motion Planning
* Manipulation

## Keywords

* Perception for Grasping and Manipulation / Grasping / RGB-D Perception

## AI依存度

* Hybrid

## 何を解決？

* Grasp planning and estimation have been a long-standing research problem in robotics, with two main approaches to find graspable poses on the objects: 1) geometric approach, which relies on 3D models of objects and the gripper to estimate valid grasp poses, and 2) data-driven, learning-based approach, with models trained to identify grasp poses from raw sensor observations.

## 何が新しい？

* This model enables the extraction of explicit mesh model while also capturing the visual appearance from novel viewpoints that is useful for perception tasks like object detection and pose estimation.

## どうやってる？

* Grasp planning and estimation have been a long-standing research problem in robotics, with two main approaches to find graspable poses on the objects: 1) geometric approach, which relies on 3D models of objects and the gripper to estimate valid grasp poses, and 2) data-driven, learning-based approach, with models trained to identify grasp poses from raw sensor observations.

## どこが強い？

* For more qualitative results, refer to the supplementary video and webpage https://bit.ly/3ZrOanU.

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
* どのモジュールに効くか: localization, perception, planning
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
