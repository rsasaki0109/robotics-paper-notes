# PIP-Loco: A Proprioceptive Infinite Horizon Planning Framework for Quadrupedal Robot Locomotion

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planinng and Control for Legged Robots 3 |
| arXiv | [http://arxiv.org/abs/2409.09441](http://arxiv.org/abs/2409.09441) |
| Authors | Shirwatkar, Aditya;Saxena, Naman;Chandra, Kishore P;Kolathaya, Shishir |
| Source | ICRA 2025 / arXiv |

## TL;DR

- A core strength of Model Predictive Control (MPC) for quadrupedal locomotion has been its ability to enforce constraints and provide interpretability of the sequence of commands over the horizon.
- However, despite being able to plan, MPC struggles to scale with task complexity, often failing to achieve robust behavior on rapidly changing surfaces.
- On the other hand, model-free Reinforcement Learning (RL) methods have outperformed MPC on multiple terrains, showing emergent motions but inherently lack any ability to handle constraints or perform planning.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Legged Robotics

## Keywords

* Legged Robots
* Reinforcement Learning
* Machine Learning for Robot Control

## AI依存度

* Hybrid

## 何を解決？

* A core strength of Model Predictive Control (MPC) for quadrupedal locomotion has been its ability to enforce constraints and provide interpretability of the sequence of commands over the horizon.

## 何が新しい？

* To address these limitations, we propose a framework that integrates proprioceptive planning with RL, allowing for agile and safe locomotion behaviors through the horizon.

## どうやってる？

* On the other hand, model-free Reinforcement Learning (RL) methods have outperformed MPC on multiple terrains, showing emergent motions but inherently lack any ability to handle constraints or perform planning.

## どこが強い？

* We validate the robustness of our training framework through ablation studies on internal model components and demonstrate improved robustness to training noise.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these limitations, we propose a framework that integrates proprioceptive planning with RL, allowing for agile and safe locomotion behaviors through the horizon.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
