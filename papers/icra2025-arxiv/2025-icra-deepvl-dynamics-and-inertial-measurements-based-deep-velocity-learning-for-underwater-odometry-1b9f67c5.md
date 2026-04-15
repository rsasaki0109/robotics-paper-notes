# DeepVL: Dynamics and Inertial Measurements-Based Deep Velocity Learning for Underwater Odometry

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Marine Robotics 2 |
| arXiv | [http://arxiv.org/abs/2502.07726](http://arxiv.org/abs/2502.07726) |
| Authors | Singh, Mohit;Alexis, Kostas |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper presents a learned model to predict the robot-centric velocity of an underwater robot through dynamics-aware proprioception.
- The method exploits a recurrent neural network using as inputs inertial cues, motor commands, and battery voltage readings alongside the hidden state of the previous time-step to output robust velocity estimates and their associated uncertainty.
- An ensemble of networks is utilized to enhance the velocity and uncertainty predictions.

## Task

* SLAM
* Localization
* Visual-Inertial

## Keywords

* Marine Robotics
* Visual-Inertial SLAM

## AI依存度

* Hybrid

## 何を解決？

* This paper presents a learned model to predict the robot-centric velocity of an underwater robot through dynamics-aware proprioception.

## 何が新しい？

* This paper presents a learned model to predict the robot-centric velocity of an underwater robot through dynamics-aware proprioception.

## どうやってる？

* The method exploits a recurrent neural network using as inputs inertial cues, motor commands, and battery voltage readings alongside the hidden state of the previous time-step to output robust velocity estimates and their associated uncertainty.

## どこが強い？

* Tested onboard an underwater robot deployed both in a laboratory pool and the Trondheim Fjord, the method takes less than 5ms for inference either on the CPU or the GPU of an NVIDIA Orin AGX and demonstrates less than 4% relative position error in novel trajectories during complete visual blackout, and approximately 2% relative error when a maximum of 2 visual features from a monocular camera are available.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This paper presents a learned model to predict the robot-centric velocity of an underwater robot through dynamics-aware proprioception.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
