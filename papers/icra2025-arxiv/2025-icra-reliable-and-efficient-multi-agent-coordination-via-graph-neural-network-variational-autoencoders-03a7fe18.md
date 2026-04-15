# Reliable and Efficient Multi-Agent Coordination Via Graph Neural Network Variational Autoencoders

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planning, Scheduling and Coordination |
| arXiv | [http://arxiv.org/abs/2503.02954](http://arxiv.org/abs/2503.02954) |
| Authors | Meng, Yue;Majcherczyk, Nathalie;Liu, Wenliang;Kiesel, Scott;Fan, Chuchu;Pecora, Federico |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Multi-agent coordination is crucial for reliable multi-robot navigation in shared spaces such as automated warehouses.
- In regions of dense robot traffic, local coordination methods may fail to find a deadlock-free solution.
- In these scenarios, it is appropriate to let a central unit generate a global schedule that decides the passing order of robots.

## Task

* Robotics

## Keywords

* Planning
* Scheduling and Coordination
* Multi-Robot Systems
* Deep Learning Methods

## AI依存度

* Hybrid

## 何を解決？

* Multi-agent coordination is crucial for reliable multi-robot navigation in shared spaces such as automated warehouses.

## 何が新しい？

* In this paper, we propose to leverage Graph Neural Network Variational Autoencoders (GNN-VAE) to solve the multi-agent coordination problem faster than through centralized optimization at scale.

## どうやってる？

* In regions of dense robot traffic, local coordination methods may fail to find a deadlock-free solution.

## どこが強い？

* Numerical results show that our approach trained on small-scale problems can achieve high-quality solutions even for large-scale problems with 250 robots, being much faster than other baselines.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we propose to leverage Graph Neural Network Variational Autoencoders (GNN-VAE) to solve the multi-agent coordination problem faster than through centralized optimization at scale.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
