# Certificated Actor-Critic: Hierarchical Reinforcement Learning with Control Barrier Functions for Safe Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Safe Control 1 |
| arXiv | [http://arxiv.org/abs/2501.17424](http://arxiv.org/abs/2501.17424) |
| Authors | Xie, Junjun;Zhao, Shuhao;Hu, Liang;Gao, Huijun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Control Barrier Functions (CBFs) have emerged as a prominent approach to designing safe navigation systems of robots.
- Despite their popularity, current CBF-based methods exhibit some limitations: optimization-based safe control techniques tend to be either myopic or computationally intensive, and they rely on simplified system models; conversely, the learning-based methods suffer from the lack of quantitative indication in terms of navigation performance and safety.
- In this paper, we present a new model-free reinforcement learning algorithm called Certificated Actor-Critic (CAC), which introduces a hierarchical reinforcement learning framework and well-defined reward functions derived from CBFs.

## Task

* Visual-Inertial
* Control

## Keywords

* Robot Safety
* Reinforcement Learning
* Machine Learning for Robot Control

## AI依存度

* Hybrid

## 何を解決？

* Control Barrier Functions (CBFs) have emerged as a prominent approach to designing safe navigation systems of robots.

## 何が新しい？

* We carry out theoretical analysis and proof of our algorithm, and propose several improvements in algorithm implementation.

## どうやってる？

* Despite their popularity, current CBF-based methods exhibit some limitations: optimization-based safe control techniques tend to be either myopic or computationally intensive, and they rely on simplified system models; conversely, the learning-based methods suffer from the lack of quantitative indication in terms of navigation performance and safety.

## どこが強い？

* Our analysis is validated by two simulation experiments, showing the effectiveness of our proposed CAC algorithm.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We carry out theoretical analysis and proof of our algorithm, and propose several improvements in algorithm implementation.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
