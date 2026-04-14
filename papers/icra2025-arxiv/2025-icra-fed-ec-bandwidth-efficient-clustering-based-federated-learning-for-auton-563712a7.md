# Fed-EC: Bandwidth-Efficient Clustering-Based Federated Learning for Autonomous Visual Robot Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Vision-Based Navigation 2 |
| arXiv | [http://arxiv.org/abs/2411.04112](http://arxiv.org/abs/2411.04112) |
| Authors | Gummadi, Shreya, Valverde Gasparino, Mateus, Vasisht, Deepak, Chowdhary, Girish |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Centralized learning requires data to be aggregated at a central server, which poses significant challenges in terms of data privacy and bandwidth consumption.
- Federated learning presents a compelling alternative, however, vanilla Federated Learning methods deployed in robotics aim to learn a single global model across robots that works ideally for all.
- Extensive real-world experiments validate that Fed-EC reduces the communication size by 23x for each robot while matching the performance of centralized learning for goal-oriented navigation and outperforms local learning.

## Task

* Robotics

## Keywords

* Distributed Robot Systems / Vision-Based Navigation / Field Robots

## AI依存度

* Hybrid

## 何を解決？

* Centralized learning requires data to be aggregated at a central server, which poses significant challenges in terms of data privacy and bandwidth consumption.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* Centralized learning requires data to be aggregated at a central server, which poses significant challenges in terms of data privacy and bandwidth consumption.

## どこが強い？

* Extensive real-world experiments validate that Fed-EC reduces the communication size by 23x for each robot while matching the performance of centralized learning for goal-oriented navigation and outperforms local learning.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Fed-EC can transfer previously learnt models to new robots that join the cluster.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
