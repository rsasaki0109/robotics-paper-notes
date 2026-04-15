# TCAFF: Temporal Consistency for Robot Frame Alignment

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot SLAM and Mapping |
| arXiv | [http://arxiv.org/abs/2405.05210](http://arxiv.org/abs/2405.05210) |
| Authors | Peterson, Mason B.;Lusk, Parker C.;Avila, Antonio;How, Jonathan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In the field of collaborative robotics, the ability to communicate spatial information like planned trajectories and shared environment information is crucial.
- When no global position information is available (e.g., indoor or GPS-denied environments), agents must align their coordinate frames before shared spatial information can be properly expressed and interpreted.
- Coordinate frame alignment is particularly difficult when robots have no initial alignment and are affected by odometry drift.

## Task

* SLAM
* Localization
* GNSS
* Perception

## Keywords

* Localization
* Multi-Robot SLAM

## AI依存度

* Non-AI

## 何を解決？

* In the field of collaborative robotics, the ability to communicate spatial information like planned trajectories and shared environment information is crucial.

## 何が新しい？

* To this end, we develop a novel multiple hypothesis algorithm, called TCAFF, for aligning the coordinate frames of neighboring robots.

## どうやってる？

* To this end, we develop a novel multiple hypothesis algorithm, called TCAFF, for aligning the coordinate frames of neighboring robots.

## どこが強い？

* We demonstrate TCAFF being used for frame alignment in a collaborative object tracking application on a team of four robots tracking six pedestrians and show that TCAFF enables robots to achieve a tracking accuracy similar to that of a system with ground truth localization.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we develop a novel multiple hypothesis algorithm, called TCAFF, for aligning the coordinate frames of neighboring robots.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
