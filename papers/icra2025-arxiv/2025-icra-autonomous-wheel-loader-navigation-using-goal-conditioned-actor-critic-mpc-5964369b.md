# Autonomous Wheel Loader Navigation Using Goal-Conditioned Actor-Critic MPC

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Navigation 1 |
| arXiv | [http://arxiv.org/abs/2409.15717](http://arxiv.org/abs/2409.15717) |
| Authors | Mäki-Penttilä, Aleksi;Toulkani, Naeim Ebrahimi;Ghabcheloo, Reza |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper proposes a novel control method for an autonomous wheel loader, enabling time-efficient navigation to an arbitrary goal pose.
- Unlike prior works which combine high-level trajectory planners with Model Predictive Control (MPC), we directly enhance the planning capabilities of MPC by incorporating a cost function derived from Actor-Critic Reinforcement Learning (RL).
- Specifically, we first train an RL agent to solve the pose reaching task in simulation, then transfer the learned planning knowledge to an MPC by incorporating the trained neural network critic as both the stage and terminal cost.

## Task

* Visual-Inertial
* Motion Planning
* Control

## Keywords

* Autonomous Vehicle Navigation
* Optimization and Optimal Control
* Motion and Path Planning

## AI依存度

* Hybrid

## 何を解決？

* This paper proposes a novel control method for an autonomous wheel loader, enabling time-efficient navigation to an arbitrary goal pose.

## 何が新しい？

* This paper proposes a novel control method for an autonomous wheel loader, enabling time-efficient navigation to an arbitrary goal pose.

## どうやってる？

* This paper proposes a novel control method for an autonomous wheel loader, enabling time-efficient navigation to an arbitrary goal pose.

## どこが強い？

* We also deploy our method on a real-world wheel loader, where we demonstrate successful navigation in various scenarios.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This paper proposes a novel control method for an autonomous wheel loader, enabling time-efficient navigation to an arbitrary goal pose.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
