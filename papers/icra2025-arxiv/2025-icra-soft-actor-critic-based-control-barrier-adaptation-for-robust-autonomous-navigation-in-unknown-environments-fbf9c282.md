# Soft Actor-Critic-Based Control Barrier Adaptation for Robust Autonomous Navigation in Unknown Environments

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 2 |
| arXiv | [http://arxiv.org/abs/2503.08479](http://arxiv.org/abs/2503.08479) |
| Authors | Mohammad, Nicholas;Bezzo, Nicola |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Motion planning failures during autonomous navigation often occur when safety constraints are either too conservative, leading to deadlocks, or too liberal, resulting in collisions.
- To improve robustness, a robot must dynamically adapt its safety constraints to ensure it reaches its goal while balancing safety and performance measures.
- To this end, we propose a Soft Actor-Critic (SAC)-based model for adapting Control Barrier Function (CBF) constraint parameters at runtime, ensuring safe yet non-conservative motion.

## Task

* Visual-Inertial
* Motion Planning
* Control

## Keywords

* Machine Learning for Robot Control
* Motion and Path Planning
* Collision Avoidance

## AI依存度

* Hybrid

## 何を解決？

* Motion planning failures during autonomous navigation often occur when safety constraints are either too conservative, leading to deadlocks, or too liberal, resulting in collisions.

## 何が新しい？

* To this end, we propose a Soft Actor-Critic (SAC)-based model for adapting Control Barrier Function (CBF) constraint parameters at runtime, ensuring safe yet non-conservative motion.

## どうやってる？

* The proposed approach is designed for a general high-level motion planner, low-level controller, and target system model, and is trained in simulation only.

## どこが強い？

* Through extensive simulations and physical experiments, we demonstrate that our framework effectively adapts CBF constraints, enabling the robot to reach its final goal without compromising safety.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we propose a Soft Actor-Critic (SAC)-based model for adapting Control Barrier Function (CBF) constraint parameters at runtime, ensuring safe yet non-conservative motion.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
