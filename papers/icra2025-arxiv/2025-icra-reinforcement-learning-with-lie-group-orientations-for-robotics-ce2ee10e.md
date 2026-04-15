# Reinforcement Learning with Lie Group Orientations for Robotics

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning for Manipulation |
| arXiv | [http://arxiv.org/abs/2409.11935](http://arxiv.org/abs/2409.11935) |
| Authors | Schuck, Martin;Bruedigam, Jan;Hirche, Sandra;Schoellig, Angela P. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Handling orientations of robots and objects is a crucial aspect of many applications.
- Yet, ever so often, there is a lack of mathematical correctness when dealing with orientations, especially in learning pipelines involving, for example, artificial neural networks.
- In this paper, we investigate reinforcement learning with orientations and propose a simple modification of the network's input and output that adheres to the Lie group structure of orientations.

## Task

* Control
* Manipulation

## Keywords

* Deep Learning in Grasping and Manipulation
* Reinforcement Learning
* Grasping

## AI依存度

* Hybrid

## 何を解決？

* Handling orientations of robots and objects is a crucial aspect of many applications.

## 何が新しい？

* In this paper, we investigate reinforcement learning with orientations and propose a simple modification of the network's input and output that adheres to the Lie group structure of orientations.

## どうやってる？

* We briefly introduce Lie theory specifically for orientations in robotics to motivate and outline our approach.

## どこが強い？

* Subsequently, a thorough empirical evaluation of different combinations of orientation representations for states and actions demonstrates the superior performance of our proposed approach in different scenarios, including: direct orientation control, end effector orientation control, and pick-and-place tasks.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we investigate reinforcement learning with orientations and propose a simple modification of the network's input and output that adheres to the Lie group structure of orientations.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
