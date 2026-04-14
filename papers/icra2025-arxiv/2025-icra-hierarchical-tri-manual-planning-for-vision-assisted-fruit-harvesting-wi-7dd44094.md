# Hierarchical Tri-Manual Planning for Vision-Assisted Fruit Harvesting with Quadrupedal Robots

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Agricultural Automation 1 |
| arXiv | [http://arxiv.org/abs/2409.17116](http://arxiv.org/abs/2409.17116) |
| Authors | Liu, Zhichao, Zhou, Jingzong, Karydis, Konstantinos |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper addresses the challenge of developing a multi-arm quadrupedal robot capable of efficiently harvesting fruit in complex, natural environments.
- To overcome the inherent limitations of traditional bimanual manipulation, we introduce the first three-arm quadrupedal robot LocoHarv-3, that builds on top of the Spot quadruped, and propose a novel hierarchical tri-manual planning approach for automated fruit harvesting with collision-free trajectories between the built-in end-effector of Spot and our custom-made bimanual manipulator.
- Validation is conducted through a series of controlled indoor experiments using motion capture and extensive field tests in natural settings.

## Task

* Localization
* LiDAR
* Mapping
* Perception

## Keywords

* Robotics and Automation in Agriculture and Forestry / Field Robots / Bimanual Manipulation

## AI依存度

* Hybrid

## 何を解決？

* This paper addresses the challenge of developing a multi-arm quadrupedal robot capable of efficiently harvesting fruit in complex, natural environments.

## 何が新しい？

* To overcome the inherent limitations of traditional bimanual manipulation, we introduce the first three-arm quadrupedal robot LocoHarv-3, that builds on top of the Spot quadruped, and propose a novel hierarchical tri-manual planning approach for automated fruit harvesting with collision-free trajectories between the built-in end-effector of Spot and our custom-made bimanual manipulator.

## どうやってる？

* Our comprehensive semi-autonomous framework integrates teleoperation, supported by LiDAR-based odometry and mapping, with learning-based visual perception for accurate fruit detection and pose estimation.

## どこが強い？

* Validation is conducted through a series of controlled indoor experiments using motion capture and extensive field tests in natural settings.

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
* どのモジュールに効くか: localization, sensing / localization / perception, map / localization
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
