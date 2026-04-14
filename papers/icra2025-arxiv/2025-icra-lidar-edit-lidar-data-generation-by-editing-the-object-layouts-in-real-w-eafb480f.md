# LiDAR-EDIT: LiDAR Data Generation by Editing the Object Layouts in Real-World Scenes

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | 3D Content Capture and Generation 1 |
| arXiv | [http://arxiv.org/abs/2412.00592](http://arxiv.org/abs/2412.00592) |
| Authors | Ho, Shing-Hei, Thach, Bao, Zhu, Minghan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We present LiDAR-EDIT, a novel paradigm for generating synthetic LiDAR data for autonomous driving.
- Our method also provides object labels for the generated data.
- Experimental results demonstrate that our framework produces realistic LiDAR scans with practical value for downstream tasks.

## Task

* LiDAR
* Perception
* Control
* Intelligent Vehicles

## Keywords

* Computer Vision for Transportation / Data Sets for Robotic Vision / Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* We present LiDAR-EDIT, a novel paradigm for generating synthetic LiDAR data for autonomous driving.

## 何が新しい？

* We present LiDAR-EDIT, a novel paradigm for generating synthetic LiDAR data for autonomous driving.

## どうやってる？

* Compared to end-to-end frameworks that generate LiDAR point clouds from scratch, LiDAR-EDIT offers users full control over the object layout, including the number, type, and pose of objects, while keeping most of the original real-world background.

## どこが強い？

* Experimental results demonstrate that our framework produces realistic LiDAR scans with practical value for downstream tasks.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Compared to end-to-end frameworks that generate LiDAR point clouds from scratch, LiDAR-EDIT offers users full control over the object layout, including the number, type, and pose of objects, while keeping most of the original real-world background.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: sensing / localization / perception, perception, control
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
