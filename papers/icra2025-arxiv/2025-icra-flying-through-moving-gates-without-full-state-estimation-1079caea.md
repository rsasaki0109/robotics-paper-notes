# Flying through Moving Gates without Full State Estimation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots 3 |
| arXiv | [http://arxiv.org/abs/2410.15799](http://arxiv.org/abs/2410.15799) |
| Authors | Römer, Ralf;Emmert, Tim;Schoellig, Angela P. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Autonomous drone racing requires powerful perception, planning, and control and has become a benchmark and test field for autonomous, agile flight.
- Existing work usually assumes static race tracks with known maps, which enables offline planning of time-optimal trajectories, performing localization to the gates to reduce the drift in visual-inertial odometry (VIO) for state estimation or training learning-based methods for the particular race track and operating environment.
- In contrast, many real-world tasks like disaster response or delivery need to be performed in unknown and dynamic environments.

## Task

* Localization
* Visual-Inertial
* Control
* Aerial Robotics

## Keywords

* Aerial Systems: Mechanics and Control
* Vision-Based Navigation

## AI依存度

* Hybrid

## 何を解決？

* Autonomous drone racing requires powerful perception, planning, and control and has become a benchmark and test field for autonomous, agile flight.

## 何が新しい？

* To make drone racing more robust against unseen environments and moving gates, we propose a control algorithm that operates without a race track map or VIO, relying solely on monocular measurements of the line of sight to the gates.

## どうやってる？

* Existing work usually assumes static race tracks with known maps, which enables offline planning of time-optimal trajectories, performing localization to the gates to reduce the drift in visual-inertial odometry (VIO) for state estimation or training learning-based methods for the particular race track and operating environment.

## どこが強い？

* Through simulations and real-world experiments, we demonstrate that our algorithm can navigate through moving gates at high speeds while being robust to different gate movements, model errors, wind, and delays.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To make drone racing more robust against unseen environments and moving gates, we propose a control algorithm that operates without a race track map or VIO, relying solely on monocular measurements of the line of sight to the gates.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
