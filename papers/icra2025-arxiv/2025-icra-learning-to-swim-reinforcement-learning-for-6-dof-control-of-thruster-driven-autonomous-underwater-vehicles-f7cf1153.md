# Learning to Swim: Reinforcement Learning for 6-DOF Control of Thruster-Driven Autonomous Underwater Vehicles

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Marine Robotics 5 |
| arXiv | [http://arxiv.org/abs/2410.00120](http://arxiv.org/abs/2410.00120) |
| Authors | Cai, Levi;Chang, Kevin;Girdhar, Yogesh |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Controlling AUVs can be challenging because of the effect of complex non-linear hydrodynamic forces acting on the robot, which are significant in water and cannot be ignored.
- The problem is exacerbated for small AUVs for which the dynamics can change significantly with payload changes and deployments under different hydrodynamic conditions.
- The common approach to AUV control is a combination of passive stabilization with added buoyancy on top and weights on the bottom, and a PID controller tuned for simple and smooth motion primitives.

## Task

* Visual-Inertial
* Control
* Software Tools

## Keywords

* Field Robots
* Marine Robotics
* Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* Controlling AUVs can be challenging because of the effect of complex non-linear hydrodynamic forces acting on the robot, which are significant in water and cannot be ignored.

## 何が新しい？

* In this paper, we propose a fast (trainable in minutes), reinforcement learning-based approach for full 6 degree of freedom (DOF) control of a thruster-driven AUVs, taking 6-DOF command-conditioned inputs direct to thruster outputs.

## どうやってる？

* The common approach to AUV control is a combination of passive stabilization with added buoyancy on top and weights on the bottom, and a PID controller tuned for simple and smooth motion primitives.

## どこが強い？

* We demonstrate this approach through zero-shot sim-to-real (with no tuning) transfer onto a real AUV that produces comparable results to hand-tuned PID controllers.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we propose a fast (trainable in minutes), reinforcement learning-based approach for full 6 degree of freedom (DOF) control of a thruster-driven AUVs, taking 6-DOF command-conditioned inputs direct to thruster outputs.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
