# Decentralized Nonlinear Model Predictive Control for Safe Collision Avoidance in Quadrotor Teams with Limited Detection Range

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Planning and Navigation |
| arXiv | [http://arxiv.org/abs/2409.17379](http://arxiv.org/abs/2409.17379) |
| Authors | Goarin, Manohari;Li, Guanrui;Saviolo, Alessandro;Loianno, Giuseppe |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Multi-quadrotor systems face significant challenges in decentralized control, particularly with safety and coordination under sensing and communication limitations.
- State-of-the-art methods leverage Control Barrier Functions (CBFs) to provide safety guarantees but often neglect actuation constraints and limited detection range.
- To address these gaps, we propose a novel decentralized Nonlinear Model Predictive Control (NMPC) that integrates Exponential CBFs (ECBFs) to enhance safety and optimality in multi-quadrotor systems.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Aerial Robotics

## Keywords

* Aerial Systems: Applications
* Distributed Robot Systems
* Collision Avoidance

## AI依存度

* Non-AI

## 何を解決？

* Multi-quadrotor systems face significant challenges in decentralized control, particularly with safety and coordination under sensing and communication limitations.

## 何が新しい？

* To address these gaps, we propose a novel decentralized Nonlinear Model Predictive Control (NMPC) that integrates Exponential CBFs (ECBFs) to enhance safety and optimality in multi-quadrotor systems.

## どうやってる？

* State-of-the-art methods leverage Control Barrier Functions (CBFs) to provide safety guarantees but often neglect actuation constraints and limited detection range.

## どこが強い？

* We validate our approach through extensive simulations with up to 10 quadrotors and 20 obstacles, as well as real-world experiments with 3 quadrotors.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these gaps, we propose a novel decentralized Nonlinear Model Predictive Control (NMPC) that integrates Exponential CBFs (ECBFs) to enhance safety and optimality in multi-quadrotor systems.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
