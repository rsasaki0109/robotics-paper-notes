# Kinematic-ICP: Enhancing LiDAR Odometry with Kinematic Constraints for Wheeled Mobile Robots Moving on Planar Surfaces

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Point Cloud Registration |
| arXiv | [http://arxiv.org/abs/2410.10277](http://arxiv.org/abs/2410.10277) |
| Authors | Guadagnino, Tiziano;Mersch, Benedikt;Vizzo, Ignacio;Gupta, Saurabh;Malladi, Meher Venkata Ramakrishna;Lobefaro, Luca;Doisy, Guillaume;Stachniss, Cyrill |
| Source | ICRA 2025 / arXiv |

## TL;DR

- LiDAR odometry is essential for many robotics applications, including 3D mapping, navigation, and simultaneous localization and mapping.
- LiDAR odometry systems are usually based on some form of point cloud registration to compute the ego-motion of a mobile robot.
- Yet, few of today's LiDAR odometry systems consider domain-specific knowledge or the kinematic model of the mobile platform during the point cloud alignment.

## Task

* Localization
* LiDAR
* Visual-Inertial

## Keywords

* Localization
* Mapping

## AI依存度

* Non-AI

## 何を解決？

* LiDAR odometry is essential for many robotics applications, including 3D mapping, navigation, and simultaneous localization and mapping.

## 何が新しい？

* In this paper, we present Kinematic-ICP, a LiDAR odometry system that focuses on wheeled mobile robots equipped with a 3D LiDAR and moving on a planar surface, which is a common assumption for warehouses, offices, hospitals, etc.

## どうやってる？

* Kinematic-ICP has been recently deployed in the Dexory fleet of robots operating in warehouses worldwide at their customers' sites, showing that our method can run in the real world alongside a complete navigation stack.

## どこが強い？

* The experiments show that our approach achieves top performances and is more accurate than wheel odometry and common LiDAR odometry systems.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we present Kinematic-ICP, a LiDAR odometry system that focuses on wheeled mobile robots equipped with a 3D LiDAR and moving on a planar surface, which is a common assumption for warehouses, offices, hospitals, etc.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
