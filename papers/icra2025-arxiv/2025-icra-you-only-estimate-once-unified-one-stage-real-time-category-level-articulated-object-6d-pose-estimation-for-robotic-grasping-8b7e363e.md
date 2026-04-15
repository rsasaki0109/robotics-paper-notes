# You Only Estimate Once: Unified, One-Stage, Real-Time Category-Level Articulated Object 6D Pose Estimation for Robotic Grasping

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Grasping 4 |
| arXiv | [http://arxiv.org/abs/2506.05719](http://arxiv.org/abs/2506.05719) |
| Authors | Huang, Jingshun;Lin, Haitao;Wang, Tianyu;Fu, Yanwei;Jiang, Yu-Gang;Xue, Xiangyang |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper addresses the problem of category-level pose estimation for articulated objects in robotic manipulation tasks.
- Recent works have shown promising results in estimating part pose and size at the category level.
- However, these approaches primarily follow a complex multi-stage pipeline that first segments part instances in the point cloud and then estimates the Normalized Part Coordinate Space (NPCS) representation for 6D poses.

## Task

* LiDAR
* Visual-Inertial
* Manipulation
* Perception

## Keywords

* Deep Learning for Visual Perception
* Perception for Grasping and Manipulation
* Deep Learning in Grasping and Manipulation

## AI依存度

* Hybrid

## 何を解決？

* This paper addresses the problem of category-level pose estimation for articulated objects in robotic manipulation tasks.

## 何が新しい？

* To address these limitations, we propose YOEO, a single-stage method that simultaneously outputs instance segmentation and NPCS representations in an end-to-end manner.

## どうやってる？

* To address these limitations, we propose YOEO, a single-stage method that simultaneously outputs instance segmentation and NPCS representations in an end-to-end manner.

## どこが強い？

* Experimental results on the GAPart dataset demonstrate the pose estimation capabilities of our proposed single-shot method.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these limitations, we propose YOEO, a single-stage method that simultaneously outputs instance segmentation and NPCS representations in an end-to-end manner.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
