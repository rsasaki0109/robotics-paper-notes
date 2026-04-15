# Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planinng and Control for Legged Robots 1 |
| arXiv | [http://arxiv.org/abs/2412.07773](http://arxiv.org/abs/2412.07773) |
| Authors | Lu, Chenhao;Cheng, Xuxin;Li, Jialong;Yang, Shiqi;Ji, Mazeyu;Yuan, Chengjing;Yang, Ge;Yi, Sha;Wang, Xiaolong |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Humanoid robots require both robust lower-body locomotion and precise upper-body manipulation.
- While recent Reinforcement Learning (RL) approaches provide whole-body loco-manipulation policies, they lack precise manipulation with high DoF arms.
- In this paper, we propose decoupling upper-body control from locomotion, using inverse kinematics (IK) and motion retargeting for precise manipulation, while RL focuses on robust lower-body locomotion.

## Task

* Control
* Manipulation
* Legged Robotics

## Keywords

* Humanoid Robot Systems
* Sensorimotor Learning
* Representation Learning

## AI依存度

* Hybrid

## 何を解決？

* Humanoid robots require both robust lower-body locomotion and precise upper-body manipulation.

## 何が新しい？

* In this paper, we propose decoupling upper-body control from locomotion, using inverse kinematics (IK) and motion retargeting for precise manipulation, while RL focuses on robust lower-body locomotion.

## どうやってる？

* While recent Reinforcement Learning (RL) approaches provide whole-body loco-manipulation policies, they lack precise manipulation with high DoF arms.

## どこが強い？

* We show that CVAE features are crucial for stability and robustness, and significantly outperforms RL-based whole-body control in precise manipulation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we propose decoupling upper-body control from locomotion, using inverse kinematics (IK) and motion retargeting for precise manipulation, while RL focuses on robust lower-body locomotion.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
