# Uncertainty-Aware Visual-Inertial SLAM with Volumetric Occupancy Mapping

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning-Based SLAM 3 |
| arXiv | [http://arxiv.org/abs/2409.12051](http://arxiv.org/abs/2409.12051) |
| Authors | Jung, Jaehyung;Boche, Simon;Barbas Laina, Sebastián;Leutenegger, Stefan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We propose visual-inertial simultaneous localization and mapping that tightly couples sparse reprojection errors, inertial measurement unit pre-integrals, and relative pose factors with dense volumetric occupancy mapping.
- Hereby depth predictions from a deep neural network are fused in a fully probabilistic manner.
- Specifically, our method is rigorously uncertainty-aware: first, we use depth and uncertainty predictions from a deep network not only from the robot's stereo rig, but we further probabilistically fuse motion stereo that provides depth information across a range of baselines, therefore drastically increasing mapping accuracy.

## Task

* SLAM
* Localization
* Visual-Inertial
* Control

## Keywords

* Visual-Inertial SLAM
* SLAM
* Mapping

## AI依存度

* Hybrid

## 何を解決？

* We propose visual-inertial simultaneous localization and mapping that tightly couples sparse reprojection errors, inertial measurement unit pre-integrals, and relative pose factors with dense volumetric occupancy mapping.

## 何が新しい？

* We propose visual-inertial simultaneous localization and mapping that tightly couples sparse reprojection errors, inertial measurement unit pre-integrals, and relative pose factors with dense volumetric occupancy mapping.

## どうやってる？

* Specifically, our method is rigorously uncertainty-aware: first, we use depth and uncertainty predictions from a deep network not only from the robot's stereo rig, but we further probabilistically fuse motion stereo that provides depth information across a range of baselines, therefore drastically increasing mapping accuracy.

## どこが強い？

* Our method is thoroughly evaluated in two benchmark datasets, resulting in localization and mapping accuracy that exceeds the state of the art, while simultaneously offering volumetric occupancy directly usable for downstream robotic planning and control in real-time.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose visual-inertial simultaneous localization and mapping that tightly couples sparse reprojection errors, inertial measurement unit pre-integrals, and relative pose factors with dense volumetric occupancy mapping.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
