# Equivariant Filter for Tightly Coupled LiDAR-Inertial Odometry

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Localization 1 |
| arXiv | [http://arxiv.org/abs/2409.06948](http://arxiv.org/abs/2409.06948) |
| Authors | Tao, Anbo, Luo, Yarong, Xia, Chunxi, Guo, Chi, Li, Xingxing |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Pose estimation is a crucial problem in simultaneous localization and mapping (SLAM).
- To provide a consistent and efficient solution of pose estimation, we propose Eq-LIO, a robust state estimator for tightly coupled LIO systems based on an equivariant filter (EqF).
- However, developing a robust and consistent state estimator remains a significant challenge, as the traditional extended Kalman filter (EKF) struggles to handle the model nonlinearity, especially for inertial measurement unit (IMU) and light detection and ranging (LiDAR).

## Task

* SLAM
* Localization
* LiDAR
* Mapping

## Keywords

* Localization / SLAM

## AI依存度

* Non-AI

## 何を解決？

* Pose estimation is a crucial problem in simultaneous localization and mapping (SLAM).

## 何が新しい？

* To provide a consistent and efficient solution of pose estimation, we propose Eq-LIO, a robust state estimator for tightly coupled LIO systems based on an equivariant filter (EqF).

## どうやってる？

* Compared with the invariant Kalman filter based on the SE_2(3) group structure, the EqF uses the symmetry of the semi-direct product group to couple the system state including IMU bias, navigation state, and LiDAR extrinsic calibration state, thereby suppressing linearization error and improving the behavior of the estimator in the event of unexpected state changes.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Compared with the invariant Kalman filter based on the SE_2(3) group structure, the EqF uses the symmetry of the semi-direct product group to couple the system state including IMU bias, navigation state, and LiDAR extrinsic calibration state, thereby suppressing linearization error and improving the behavior of the estimator in the event of unexpected state changes.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
