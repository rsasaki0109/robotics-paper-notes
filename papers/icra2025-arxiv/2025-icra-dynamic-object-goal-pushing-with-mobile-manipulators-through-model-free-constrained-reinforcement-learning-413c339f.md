# Dynamic Object Goal Pushing with Mobile Manipulators through Model-Free Constrained Reinforcement Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Mobile Manipulation: Planning and Control |
| arXiv | [http://arxiv.org/abs/2502.01546](http://arxiv.org/abs/2502.01546) |
| Authors | Dadiotis, Ioannis;Mittal, Mayank;Tsagarakis, Nikos;Hutter, Marco |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Non-prehensile pushing to move and reorient objects to a goal is a versatile loco-manipulation skill.
- In the real world, the object's physical properties and friction with the floor contain significant uncertainties, which makes the task challenging for a mobile manipulator.
- In this paper, we develop a learning-based controller for a mobile manipulator to move an unknown object to a desired position and yaw orientation through a sequence of pushing actions.

## Task

* Visual-Inertial
* Control
* Manipulation
* Legged Robotics

## Keywords

* Mobile Manipulation
* AI-Enabled Robotics
* Deep Learning in Grasping and Manipulation

## AI依存度

* Hybrid

## 何を解決？

* Non-prehensile pushing to move and reorient objects to a goal is a versatile loco-manipulation skill.

## 何が新しい？

* The proposed controller for the robotic arm and the mobile base motion is trained using a constrained Reinforcement Learning (RL) formulation.

## どうやってる？

* Through our extensive hardware experiments, we show that the approach demonstrates high robustness against unknown objects of different masses, materials, sizes, and shapes.

## どこが強い？

* We demonstrate its capability in experiments with a quadrupedal robot equipped with an arm.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* The proposed controller for the robotic arm and the mobile base motion is trained using a constrained Reinforcement Learning (RL) formulation.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
