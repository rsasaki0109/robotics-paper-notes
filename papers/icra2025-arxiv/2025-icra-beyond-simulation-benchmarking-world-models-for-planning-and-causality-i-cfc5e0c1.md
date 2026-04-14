# Beyond Simulation: Benchmarking World Models for Planning and Causality in Autonomous Driving

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Navigation 1 |
| arXiv | [http://arxiv.org/abs/2508.01922](http://arxiv.org/abs/2508.01922) |
| Authors | Schofield, Hunter, Elmahgiubi, Mohammed, Rezaee, Kasra, Shan, Jinjun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Specifically, we analyze the metametric employed by the Waymo Open Sim-Agents Challenge (WOSAC) and compare world model predictions on standard scenarios where the agents are fully or partially controlled by the world model (partial replay).
- To address these cases, we propose new metrics to highlight the sensitivity of world models to uncontrollable objects and evaluate the performance of world models as pseudo-environments for policy training and analyze some state-of-the-art world models under these new metrics.
- World models have become increasingly popular in acting as learned traffic simulators.

## Task

* Motion Planning
* Control
* Intelligent Vehicles

## Keywords

* Autonomous Vehicle Navigation / Autonomous Agents / Motion and Path Planning

## AI依存度

* Hybrid

## 何を解決？

* Specifically, we analyze the metametric employed by the Waymo Open Sim-Agents Challenge (WOSAC) and compare world model predictions on standard scenarios where the agents are fully or partially controlled by the world model (partial replay).

## 何が新しい？

* To address these cases, we propose new metrics to highlight the sensitivity of world models to uncontrollable objects and evaluate the performance of world models as pseudo-environments for policy training and analyze some state-of-the-art world models under these new metrics.

## どうやってる？

* World models have become increasingly popular in acting as learned traffic simulators.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Recent work has explored replacing traditional traffic simulators with world models for policy training.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
