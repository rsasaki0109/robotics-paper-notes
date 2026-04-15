# Implicit Articulated Robot Morphology Modeling with Configuration Space Neural Signed Distance Functions

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation 4 |
| arXiv | [http://arxiv.org/abs/2309.16085](http://arxiv.org/abs/2309.16085) |
| Authors | Chen, Yiting;Gao, Xiao;Yao, Kunpeng;Niederhauser, Loïc;Bekiroglu, Yasemin;Billard, Aude |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we introduce a novel approach to implicitly encode precise robot morphology using forward kinematics based on a configuration space signed distance function.
- Our proposed Robot Neural Distance Function (RNDF) optimizes the balance between computational efficiency and accuracy for signed distance queries conditioned on the robot's configuration for each link.
- Compared to the baseline method, the proposed approach achieves an 81.1% reduction in distance error while utilizing only 47.6% of model parameters.

## Task

* Manipulation

## Keywords

* Manipulation Planning
* Collision Avoidance
* Grasping

## AI依存度

* Hybrid

## 何を解決？

* In this paper, we introduce a novel approach to implicitly encode precise robot morphology using forward kinematics based on a configuration space signed distance function.

## 何が新しい？

* Our proposed Robot Neural Distance Function (RNDF) optimizes the balance between computational efficiency and accuracy for signed distance queries conditioned on the robot's configuration for each link.

## どうやってる？

* Compared to the baseline method, the proposed approach achieves an 81.1% reduction in distance error while utilizing only 47.6% of model parameters.

## どこが強い？

* Specifically, we apply RNDF to robotic arm-hand modeling and demonstrate its potential as a core platform for whole-arm, collision-free grasp planning in cluttered environments.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Our proposed Robot Neural Distance Function (RNDF) optimizes the balance between computational efficiency and accuracy for signed distance queries conditioned on the robot's configuration for each link.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
