# Towards Autonomous Wood-Log Grasping with a Forestry Crane: Simulator and Benchmarking

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Field Robotics: Forestry and Mining |
| arXiv | [http://arxiv.org/abs/2502.01304](http://arxiv.org/abs/2502.01304) |
| Authors | Vu, Minh Nhat;Wachter, Alexander;Ebmer, Gerald;Ecker, Marc-Philip;Glück, Tobias;Nguyen, Anh;Kemmetmueller, Wolfgang;Kugi, Andreas |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Forestry machines operated in forest production environments face challenges when performing manipulation tasks, especially regarding the complicated dynamics of underactuated crane systems and the different sizes of logs to be grasped.
- This study investigates the feasibility of using reinforcement learning for forestry crane manipulators in grasping and lifting a varying-diameter wood log in a simulation environment.
- The Mujoco physics engine creates realistic scenarios, including modeling a forestry crane with 8 degrees of freedom from CAD data and wood logs of different sizes.

## Task

* Visual-Inertial
* Control
* Manipulation
* Software Tools

## Keywords

* Robotics and Automation in Agriculture and Forestry
* Agricultural Automation

## AI依存度

* Hybrid

## 何を解決？

* Forestry machines operated in forest production environments face challenges when performing manipulation tasks, especially regarding the complicated dynamics of underactuated crane systems and the different sizes of logs to be grasped.

## 何が新しい？

* Given the six degrees of freedom (DoF) poses of the wood log, i.e., the 3D Cartesian position and the orientation, the proposed control strategy exhibits a success rate of 96% when grasping logs of different diameters and under random initial configurations of the forestry crane.

## どうやってる？

* The Mujoco physics engine creates realistic scenarios, including modeling a forestry crane with 8 degrees of freedom from CAD data and wood logs of different sizes.

## どこが強い？

* Our results show the successful implementation of a velocity controller for log grasping by deep reinforcement learning using a curriculum strategy.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Given the six degrees of freedom (DoF) poses of the wood log, i.e., the 3D Cartesian position and the orientation, the proposed control strategy exhibits a success rate of 96% when grasping logs of different diameters and under random initial configurations of the forestry crane.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
