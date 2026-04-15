# Leveraging Symmetry to Accelerate Learning of Trajectory Tracking Controllers for Free-Flying Robotic Systems

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Control 1 |
| arXiv | [http://arxiv.org/abs/2409.11238](http://arxiv.org/abs/2409.11238) |
| Authors | Welde, Jake;Rao, Nishanth Arun;Kunapuli, Pratik;Jayaraman, Dinesh;Kumar, Vijay |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Tracking controllers enable robotic systems to accurately follow planned reference trajectories.
- In particular, reinforcement learning (RL) has shown promise in the synthesis of controllers for systems with complex dynamics and modest online compute budgets.
- However, the poor sample efficiency of RL and the challenges of reward design make training slow and sometimes unstable, especially for high-dimensional systems.

## Task

* Motion Planning
* Control
* Aerial Robotics
* Perception

## Keywords

* Dynamics
* Reinforcement Learning
* Aerial Systems: Mechanics and Control

## AI依存度

* Hybrid

## 何を解決？

* Tracking controllers enable robotic systems to accurately follow planned reference trajectories.

## 何が新しい？

* Tracking controllers enable robotic systems to accurately follow planned reference trajectories.

## どうやってる？

* We compare this symmetry-informed approach to an unstructured baseline, using Proximal Policy Optimization (PPO) to learn tracking controllers for three systems: the Particle (a forced point mass), the Astrobee (a fully-actuated space robot), and the Quadrotor (an underactuated system).

## どこが強い？

* In particular, reinforcement learning (RL) has shown promise in the synthesis of controllers for systems with complex dynamics and modest online compute budgets.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Tracking controllers enable robotic systems to accurately follow planned reference trajectories.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
