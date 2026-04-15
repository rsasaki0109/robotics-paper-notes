# Planning with Adaptive World Models for Autonomous Driving

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Task and Motion Planning 3 |
| arXiv | [http://arxiv.org/abs/2406.10714](http://arxiv.org/abs/2406.10714) |
| Authors | Vasudevan, Arun Balajee;Peri, Neehar;Schneider, Jeff;Ramanan, Deva |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Motion planning is crucial for safe navigation in complex urban environments.
- Historically, motion planners (MPs) have been evaluated with procedurally-generated simulators like CARLA.
- However, such synthetic benchmarks do not capture real-world multi-agent interactions.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Software Tools

## Keywords

* Task and Motion Planning
* Behavior-Based Systems
* Robust/Adaptive Control

## AI依存度

* Hybrid

## 何を解決？

* Motion planning is crucial for safe navigation in complex urban environments.

## 何が新しい？

* Finally, we present AdaptiveDriver, a model-predictive control (MPC) based planner that unrolls different world models conditioned on BehaviorNet's predictions.

## どうやってる？

* We learn to model such unique behaviors with BehaviorNet, a graph convolutional neural network (GCNN) that predicts reactive agent behaviors using features derived from recently-observed agent histories; intuitively, some aggressive agents may tailgate lead vehicles, while others may not.

## どこが強い？

* Our extensive experiments demonstrate that AdaptiveDriver achieves state-of-the-art results on the nuPlan closed-loop planning benchmark, improving over prior work by 2% on Test-14 Hard R-CLS, and generalizes even when evaluated on never-before-seen cities.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Finally, we present AdaptiveDriver, a model-predictive control (MPC) based planner that unrolls different world models conditioned on BehaviorNet's predictions.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
