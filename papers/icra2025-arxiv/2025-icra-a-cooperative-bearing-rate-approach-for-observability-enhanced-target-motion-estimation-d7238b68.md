# A Cooperative Bearing-Rate Approach for Observability-Enhanced Target Motion Estimation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Systems 4 |
| arXiv | [http://arxiv.org/abs/2502.08089](http://arxiv.org/abs/2502.08089) |
| Authors | Zheng, Canlun;Guo, Hanqing;Zhao, Shiyu |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Vision-based target motion estimation is a fundamental problem in many robotic tasks.
- The existing methods have the limitation of low observability and, hence, face challenges in tracking highly maneuverable targets.
- Motivated by the aerial target pursuit task where a target may maneuver in 3D space, this paper studies how to further enhance observability by incorporating the emph{bearing rate} information that has not been well explored in the literature.

## Task

* Localization
* Visual-Inertial
* Aerial Robotics
* Perception

## Keywords

* Sensor Networks
* Localization

## AI依存度

* Non-AI

## 何を解決？

* Vision-based target motion estimation is a fundamental problem in many robotic tasks.

## 何が新しい？

* The main contribution of this paper is to propose a new cooperative estimator called STT-R (Spatial-Temporal Triangulation with bearing Rate), which is designed under the framework of distributed recursive least squares.

## どうやってる？

* The existing methods have the limitation of low observability and, hence, face challenges in tracking highly maneuverable targets.

## どこが強い？

* This theoretical result is further verified by numerical simulation and real-world experiments.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* The main contribution of this paper is to propose a new cooperative estimator called STT-R (Spatial-Temporal Triangulation with bearing Rate), which is designed under the framework of distributed recursive least squares.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
