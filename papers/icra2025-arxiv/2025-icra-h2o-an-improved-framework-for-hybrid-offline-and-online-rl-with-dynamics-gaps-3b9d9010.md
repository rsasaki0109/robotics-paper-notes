# H2O+: An Improved Framework for Hybrid Offline-And-Online RL with Dynamics Gaps

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Transfer and Continual Learning |
| arXiv | [http://arxiv.org/abs/2309.12716](http://arxiv.org/abs/2309.12716) |
| Authors | Niu, Haoyi;Ji, Tianying;Bingqi, Liu;Zhao, Haocheng;Zhu, Xiangyu;Zheng, Jianying;Huang, Pengfei;Zhou, Guyue;Hu, Jianming;Zhan, Xianyuan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Solving real-world complex tasks using reinforcement learning (RL) without high-fidelity simulation environments or large amounts of offline data can be quite challenging.
- Online RL agents trained in imperfect simulation environments can suffer from severe sim-to-real issues.
- Offline RL approaches although bypass the need for simulators, often pose demanding requirements on the size and quality of the offline datasets.

## Task

* Visual-Inertial
* Control
* Software Tools

## Keywords

* Transfer Learning
* Reinforcement Learning
* Machine Learning for Robot Control

## AI依存度

* Hybrid

## 何を解決？

* Solving real-world complex tasks using reinforcement learning (RL) without high-fidelity simulation environments or large amounts of offline data can be quite challenging.

## 何が新しい？

* In this paper, we develop a new algorithm, called H2O+, which offers great flexibility to bridge various choices of offline and online learning methods, while also accounting for dynamics gaps between the real and simulation environment.

## どうやってる？

* In this paper, we develop a new algorithm, called H2O+, which offers great flexibility to bridge various choices of offline and online learning methods, while also accounting for dynamics gaps between the real and simulation environment.

## どこが強い？

* Through extensive simulation and real-world robotics experiments, we demonstrate superior performance and flexibility of H2O+ over advanced cross-domain online and offline RL algorithms.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we develop a new algorithm, called H2O+, which offers great flexibility to bridge various choices of offline and online learning methods, while also accounting for dynamics gaps between the real and simulation environment.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
