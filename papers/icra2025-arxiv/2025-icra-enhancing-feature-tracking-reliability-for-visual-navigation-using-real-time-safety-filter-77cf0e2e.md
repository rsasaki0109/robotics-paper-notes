# Enhancing Feature Tracking Reliability for Visual Navigation Using Real-Time Safety Filter

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Localization 6 |
| arXiv | [http://arxiv.org/abs/2502.01092](http://arxiv.org/abs/2502.01092) |
| Authors | Kim, Dabin;Jang, Inkyu;Han, Youngsoo;Hwang, Sunwoo;Kim, H. Jin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Vision sensors are extensively used for localizing a robot's pose, particularly in environments where global localization tools such as GPS or motion capture systems are unavailable.
- In many visual navigation systems, localization is achieved by detecting and tracking visual features or landmarks, which provide information about the sensor's relative pose.
- For reliable feature tracking and accurate pose estimation, it is crucial to maintain visibility of a sufficient number of features.

## Task

* SLAM
* Localization
* GNSS
* Visual-Inertial

## Keywords

* Sensor-based Control
* Reactive and Sensor-Based Planning
* View Planning for SLAM

## AI依存度

* Non-AI

## 何を解決？

* Vision sensors are extensively used for localizing a robot's pose, particularly in environments where global localization tools such as GPS or motion capture systems are unavailable.

## 何が新しい？

* By leveraging the invariance properties of visibility constraints within the robot's kinematic model, we propose a real-time safety filter based on quadratic programming.

## どうやってる？

* In this paper, we approach it as a constrained control problem.

## どこが強い？

* Numerical simulations demonstrate that the proposed safety filter preserves the invariance condition and ensures the visibility of more features than the required minimum.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* By leveraging the invariance properties of visibility constraints within the robot's kinematic model, we propose a real-time safety filter based on quadratic programming.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
