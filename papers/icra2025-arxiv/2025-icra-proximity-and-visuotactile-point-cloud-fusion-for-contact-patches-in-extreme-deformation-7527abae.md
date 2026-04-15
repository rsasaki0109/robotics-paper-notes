# Proximity and Visuotactile Point Cloud Fusion for Contact Patches in Extreme Deformation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Soft Sensors |
| arXiv | [http://arxiv.org/abs/2307.03839](http://arxiv.org/abs/2307.03839) |
| Authors | Yin, Jessica;Shah, Paarth;Kuppuswamy, Naveen;Beaulieu, Andrew;Uttamchandani, Avinash;Castro, Alejandro;Pikul, James;Tedrake, Russ |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Visuotactile sensors are a popular tactile sensing strategy due to high-fidelity estimates of local object geometry.
- However, existing algorithms for processing raw sensor inputs to useful intermediate signals such as contact patches struggle in high-deformation regimes.
- This is due to physical constraints imposed by sensor hardware and small-deformation assumptions used by mechanics-based models.

## Task

* LiDAR
* Control
* Perception

## Keywords

* Force and Tactile Sensing
* Soft Sensors and Actuators
* Soft Robot Materials and Design

## AI依存度

* Non-AI

## 何を解決？

* Visuotactile sensors are a popular tactile sensing strategy due to high-fidelity estimates of local object geometry.

## 何が新しい？

* In this work, we propose a fusion algorithm for proximity and visuotactile point clouds for contact patch segmentation, entirely independent from membrane mechanics.

## どうやってる？

* We compare our method against three baselines: proximity-only, tactile-only, and a first principles mechanics model.

## どこが強い？

* We demonstrate our contact patch algorithm in four applications: varied stiffness membranes, torque and shear-induced wrinkling, closed loop control, and pose estimation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this work, we propose a fusion algorithm for proximity and visuotactile point clouds for contact patch segmentation, entirely independent from membrane mechanics.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
