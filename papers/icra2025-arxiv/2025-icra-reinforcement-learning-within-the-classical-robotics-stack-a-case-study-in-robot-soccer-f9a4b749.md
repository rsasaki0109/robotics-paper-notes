# Reinforcement Learning within the Classical Robotics Stack: A Case Study in Robot Soccer

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Systems 6 |
| arXiv | [http://arxiv.org/abs/2412.09417](http://arxiv.org/abs/2412.09417) |
| Authors | Labiosa, Adam;Wang, Zhihan;Agarwal, Siddhant;Cong, William;Hemkumar, Geethika;Harish, Abhinav Narayan;Hong, Benjamin;Kelle, Josh;Li, Chen;Li, Yuhao;Shao, Zisen;Stone, Peter;Hanna, Josiah |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robot decision-making in partially observable, real-time, dynamic, and multi-agent environments remains a difficult and unsolved challenge.
- Model-free reinforcement learning (RL) is a promising approach to learning decision-making in such domains, however, end-to-end RL in complex environments is often intractable.
- To address this challenge in the RoboCup Standard Platform League (SPL) domain, we developed a novel architecture integrating RL within a classical robotics stack, while employing a multi-fidelity sim2real approach and decomposing behavior into learned sub-behaviors with heuristic selection.

## Task

* Control

## Keywords

* Reinforcement Learning
* Machine Learning for Robot Control
* Multi-Robot Systems

## AI依存度

* Hybrid

## 何を解決？

* Robot decision-making in partially observable, real-time, dynamic, and multi-agent environments remains a difficult and unsolved challenge.

## 何が新しい？

* To address this challenge in the RoboCup Standard Platform League (SPL) domain, we developed a novel architecture integrating RL within a classical robotics stack, while employing a multi-fidelity sim2real approach and decomposing behavior into learned sub-behaviors with heuristic selection.

## どうやってる？

* Model-free reinforcement learning (RL) is a promising approach to learning decision-making in such domains, however, end-to-end RL in complex environments is often intractable.

## どこが強い？

* Our approach demonstrates how RL-based behaviors can be integrated into complete robot behavior architectures.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this challenge in the RoboCup Standard Platform League (SPL) domain, we developed a novel architecture integrating RL within a classical robotics stack, while employing a multi-fidelity sim2real approach and decomposing behavior into learned sub-behaviors with heuristic selection.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
