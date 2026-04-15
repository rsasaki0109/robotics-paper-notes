# Learning Dynamic Weight Adjustment for Spatial-Temporal Trajectory Planning in Crowd Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Human-Aware Robot Motion |
| arXiv | [http://arxiv.org/abs/2412.00555](http://arxiv.org/abs/2412.00555) |
| Authors | Cao, Muqing;Xu, Xinhang;Yang, Yizhuo;Li, Jianping;Jin, Tongxing;Wang, Pengfei;Hung, Tzu-Yi;Lin, Guosheng;Xie, Lihua |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robot navigation in dense human crowds poses a significant challenge due to the complexity of human behavior in dynamic and obstacle-rich environments.
- In this work, we propose a dynamic weight adjustment scheme using a neural network to predict the optimal weights of objectives in an optimization-based motion planner.
- We adopt a spatial-temporal trajectory planner and incorporate diverse objectives to achieve a balance among safety, efficiency, and goal achievement in complex and dynamic environments.

## Task

* Visual-Inertial
* Motion Planning

## Keywords

* Human-Aware Motion Planning
* Motion and Path Planning
* Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* Robot navigation in dense human crowds poses a significant challenge due to the complexity of human behavior in dynamic and obstacle-rich environments.

## 何が新しい？

* In this work, we propose a dynamic weight adjustment scheme using a neural network to predict the optimal weights of objectives in an optimization-based motion planner.

## どうやってる？

* Simulation results show improved safety compared to the fixed-weight planner and the state-of-the-art learning-based methods, and verify the ability of the learned policy to adaptively adjust the weights based on the observed situations.

## どこが強い？

* The feasibility of the approach is demonstrated in a navigation task using an autonomous delivery robot across a crowded corridor over a 300 m distance.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this work, we propose a dynamic weight adjustment scheme using a neural network to predict the optimal weights of objectives in an optimization-based motion planner.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
