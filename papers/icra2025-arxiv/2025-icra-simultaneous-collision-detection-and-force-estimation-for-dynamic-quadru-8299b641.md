# Simultaneous Collision Detection and Force Estimation for Dynamic Quadrupedal Locomotion

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Identifcation and Estimation for Legged Robots |
| arXiv | [http://arxiv.org/abs/2504.17201](http://arxiv.org/abs/2504.17201) |
| Authors | Zhou, Ziyi, Di Cairano, Stefano, Wang, Yebin, Berntorp, Karl |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper we address the simultaneous collision detection and force estimation problem for quadrupedal loco- motion using joint encoder information and the robot dynamics only.
- We design an interacting multiple-model Kalman filter (IMM-KF) that estimates the external force exerted on the robot and multiple possible contact modes.
- Simulation ablatation studies and experiments show the efficacy of the approach.

## Task

* Perception
* Control
* State Estimation
* Legged Robotics

## Keywords

* Legged Robots / Motion Control

## AI依存度

* Non-AI

## 何を解決？

* In this paper we address the simultaneous collision detection and force estimation problem for quadrupedal loco- motion using joint encoder information and the robot dynamics only.

## 何が新しい？

* We design an interacting multiple-model Kalman filter (IMM-KF) that estimates the external force exerted on the robot and multiple possible contact modes.

## どうやってる？

* We design an interacting multiple-model Kalman filter (IMM-KF) that estimates the external force exerted on the robot and multiple possible contact modes.

## どこが強い？

* Simulation ablatation studies and experiments show the efficacy of the approach.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
