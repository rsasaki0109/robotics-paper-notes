# Distributed Multi-Robot Source Seeking in Unknown Environments with Unknown Number of Sources

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Systems 3 |
| arXiv | [http://arxiv.org/abs/2503.11048](http://arxiv.org/abs/2503.11048) |
| Authors | Chen, Lingpeng;Kailas, Siva;Deolasee, Srujan;Luo, Wenhao;Sycara, Katia;Kim, Woojun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We introduce a novel distributed source seeking framework, DIAS, designed for multi-robot systems in scenarios where the number of sources is unknown and potentially exceeds the number of robots.
- Traditional robotic source seeking methods typically focused on directing each robot to a specific strong source and may fall short in comprehensively identifying all potential sources.
- DIAS addresses this gap by introducing a hybrid controller that identifies the presence of sources and then alternates between exploration for data gathering and exploitation for guiding robots to identified sources.

## Task

* Visual-Inertial
* Motion Planning
* Control

## Keywords

* Multi-Robot Systems
* Path Planning for Multiple Mobile Robots or Agents
* Robust/Adaptive Control

## AI依存度

* Non-AI

## 何を解決？

* We introduce a novel distributed source seeking framework, DIAS, designed for multi-robot systems in scenarios where the number of sources is unknown and potentially exceeds the number of robots.

## 何が新しい？

* We introduce a novel distributed source seeking framework, DIAS, designed for multi-robot systems in scenarios where the number of sources is unknown and potentially exceeds the number of robots.

## どうやってる？

* Traditional robotic source seeking methods typically focused on directing each robot to a specific strong source and may fall short in comprehensively identifying all potential sources.

## どこが強い？

* The numerical results show that DIAS outperforms the baseline methods in both the efficiency of source identification by the robots and the accuracy of the estimated environmental density function.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We introduce a novel distributed source seeking framework, DIAS, designed for multi-robot systems in scenarios where the number of sources is unknown and potentially exceeds the number of robots.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
