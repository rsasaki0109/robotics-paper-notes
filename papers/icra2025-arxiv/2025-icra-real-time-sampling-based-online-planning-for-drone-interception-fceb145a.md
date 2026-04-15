# Real-Time Sampling-Based Online Planning for Drone Interception

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Trajectory Planning and Control |
| arXiv | [http://arxiv.org/abs/2502.14231](http://arxiv.org/abs/2502.14231) |
| Authors | Ryou, Gilhyun;Lao Beyer, Lukas;Karaman, Sertac |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper studies high-speed online planning in dynamic environments.
- The problem requires finding time-optimal trajectories that conform to system dynamics, meeting computational constraints for real-time adaptation, and accounting for uncertainty from environmental changes.
- To address these challenges, we propose a sampling-based online planning algorithm that leverages neural network inference to replace time-consuming nonlinear trajectory optimization, enabling rapid exploration of multiple trajectory options under uncertainty.

## Task

* Visual-Inertial
* Motion Planning
* Aerial Robotics
* Perception

## Keywords

* Aerial Systems: Perception and Autonomy
* Planning under Uncertainty
* AI-Based Methods

## AI依存度

* Hybrid

## 何を解決？

* This paper studies high-speed online planning in dynamic environments.

## 何が新しい？

* To address these challenges, we propose a sampling-based online planning algorithm that leverages neural network inference to replace time-consuming nonlinear trajectory optimization, enabling rapid exploration of multiple trajectory options under uncertainty.

## どうやってる？

* The proposed method is applied to the drone interception problem, where a defense drone must intercept a target while avoiding collisions and handling imperfect target predictions.

## どこが強い？

* Through extensive validation in both simulated and real-world environments, we demonstrate our method's capability for high-rate online planning and its adaptability to unpredictable movements in unstructured settings.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these challenges, we propose a sampling-based online planning algorithm that leverages neural network inference to replace time-consuming nonlinear trajectory optimization, enabling rapid exploration of multiple trajectory options under uncertainty.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
