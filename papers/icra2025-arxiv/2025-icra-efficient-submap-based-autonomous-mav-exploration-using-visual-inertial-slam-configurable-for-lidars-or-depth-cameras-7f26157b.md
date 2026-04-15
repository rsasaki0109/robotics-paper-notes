# Efficient Submap-Based Autonomous MAV Exploration Using Visual-Inertial SLAM Configurable for LiDARs or Depth Cameras

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 4 |
| arXiv | [http://arxiv.org/abs/2409.16972](http://arxiv.org/abs/2409.16972) |
| Authors | Papatheodorou, Sotiris;Boche, Simon;Barbas Laina, Sebastián;Leutenegger, Stefan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Autonomous exploration of unknown space is an essential component for the deployment of mobile robots in the real world.
- Safe navigation is crucial for all robotics applications and requires accurate and consistent maps of the robot's surroundings.
- To achieve full autonomy and allow deployment in a wide variety of environments, the robot must rely on on-board state estimation which is prone to drift over time.

## Task

* SLAM
* Localization
* LiDAR
* Visual-Inertial

## Keywords

* Aerial Systems: Perception and Autonomy
* Reactive and Sensor-Based Planning

## AI依存度

* Non-AI

## 何を解決？

* Autonomous exploration of unknown space is an essential component for the deployment of mobile robots in the real world.

## 何が新しい？

* We propose a Micro Aerial Vehicle (MAV) exploration framework based on local submaps to allow retaining global consistency by applying loop-closure corrections to the relative submap poses.

## どうやってる？

* Our method seamlessly supports using either a LiDAR sensor or a depth camera, making it suitable for different kinds of MAV platforms.

## どこが強い？

* Finally, we demonstrate the applicability of our method to real-world MAVs, one equipped with a LiDAR and the other with a depth camera.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a Micro Aerial Vehicle (MAV) exploration framework based on local submaps to allow retaining global consistency by applying loop-closure corrections to the relative submap poses.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
