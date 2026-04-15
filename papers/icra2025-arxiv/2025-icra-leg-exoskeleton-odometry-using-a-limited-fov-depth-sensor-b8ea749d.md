# Leg Exoskeleton Odometry Using a Limited FOV Depth Sensor

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Visual-Inertial Odometry |
| arXiv | [http://arxiv.org/abs/2502.19237](http://arxiv.org/abs/2502.19237) |
| Authors | Elnecave Xavier, Fabio;Viozelange, Matis;Burger, Guillaume;Petriaux, Marine;Deschaud, Jean-Emmanuel;Goulette, François |
| Source | ICRA 2025 / arXiv |

## TL;DR

- For leg exoskeletons to operate effectively in real-world environments, they must be able to perceive and understand the terrain around them.
- However, unlike other legged robots, exoskeletons face specific constraints on where depth sensors can be mounted due to the presence of a human user.
- These constraints lead to a limited Field Of View (FOV) and greater sensor motion, making odometry particularly challenging.

## Task

* Localization
* LiDAR
* Legged Robotics

## Keywords

* Sensor Fusion
* Mapping
* Prosthetics and Exoskeletons

## AI依存度

* Non-AI

## 何を解決？

* For leg exoskeletons to operate effectively in real-world environments, they must be able to perceive and understand the terrain around them.

## 何が新しい？

* To address this, we propose a novel odometry algorithm that integrates proprioceptive data from the exoskeleton with point clouds from a depth camera to produce accurate elevation maps despite these limitations.

## どうやってる？

* Our method builds on an extended Kalman filter (EKF) to fuse kinematic and inertial measurements, while incorporating a tailored iterative closest point (ICP) algorithm to register new point clouds with the elevation map.

## どこが強い？

* Experimental validation with a leg exoskeleton demonstrates that our approach reduces drift and enhances the quality of elevation maps compared to a purely proprioceptive baseline, while also outperforming a more traditional point cloud map-based variant.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this, we propose a novel odometry algorithm that integrates proprioceptive data from the exoskeleton with point clouds from a depth camera to produce accurate elevation maps despite these limitations.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
