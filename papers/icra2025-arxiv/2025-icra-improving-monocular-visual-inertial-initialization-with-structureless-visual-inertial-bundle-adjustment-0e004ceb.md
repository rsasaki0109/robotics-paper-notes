# Improving Monocular Visual-Inertial Initialization with Structureless Visual-Inertial Bundle Adjustment

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Visual-Inertial Odometry |
| arXiv | [http://arxiv.org/abs/2502.16598](http://arxiv.org/abs/2502.16598) |
| Authors | Song, Junlin;Richard, Antoine;Olivares-Mendez, Miguel A. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Monocular visual inertial odometry (VIO) has facilitated a wide range of real-time motion tracking applications, thanks to the small size of the sensor suite and low power consumption.
- To successfully bootstrap VIO algorithms, the initialization module is extremely important.
- Most initialization methods rely on the reconstruction of 3D visual point clouds.

## Task

* Localization
* LiDAR
* Visual-Inertial
* Perception

## Keywords

* Localization

## AI依存度

* Non-AI

## 何を解決？

* Monocular visual inertial odometry (VIO) has facilitated a wide range of real-time motion tracking applications, thanks to the small size of the sensor suite and low power consumption.

## 何が新しい？

* To address this issue, some researchers recently proposed a structureless initialization method, which can solve the initial state without recovering 3D structure.

## どうやってる？

* Most initialization methods rely on the reconstruction of 3D visual point clouds.

## どこが強い？

* Extensive experiments on real-world datasets show our method significantly improves the VIO initialization accuracy, while maintaining real-time performance.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this issue, some researchers recently proposed a structureless initialization method, which can solve the initial state without recovering 3D structure.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
