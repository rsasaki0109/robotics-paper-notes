# CoL3D: Collaborative Learning of Single-View Depth and Camera Intrinsics for Metric 3D Shape Recovery

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Calibration 2 |
| arXiv | [http://arxiv.org/abs/2502.08902](http://arxiv.org/abs/2502.08902) |
| Authors | Zhang, Chenghao;Fan, Lubin;Cao, Shen;Wu, Bojian;Ye, Jieping |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recovering the metric 3D shape from a single image is particularly relevant for robotics and embodied intelligence applications, where accurate spatial understanding is crucial for navigation and interaction with environments.
- Usually, the mainstream approaches achieve it through monocular depth estimation.
- However, without camera intrinsics, the 3D metric shape can not be recovered from depth alone.

## Task

* LiDAR
* Calibration
* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* RGB-D Perception
* Calibration and Identification

## AI依存度

* Hybrid

## 何を解決？

* Recovering the metric 3D shape from a single image is particularly relevant for robotics and embodied intelligence applications, where accurate spatial understanding is crucial for navigation and interaction with environments.

## 何が新しい？

* Motivated by this, we propose a collaborative learning framework for jointly estimating depth and camera intrinsics, named CoL3D, to learn metric 3D shapes from single images.

## どうやってる？

* Usually, the mainstream approaches achieve it through monocular depth estimation.

## どこが強い？

* In this study, we theoretically demonstrate that depth serves as a 3D prior constraint for estimating camera intrinsics and uncover the reciprocal relations between these two elements.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Motivated by this, we propose a collaborative learning framework for jointly estimating depth and camera intrinsics, named CoL3D, to learn metric 3D shapes from single images.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
