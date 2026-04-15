# A Skeleton-Based Topological Planner for Exploration in Complex Unknown Environments

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planning under Uncertainty 1 |
| arXiv | [http://arxiv.org/abs/2412.13664](http://arxiv.org/abs/2412.13664) |
| Authors | Niu, Haochen;Ji, Xingwu;Zhang, Lantao;Wen, Fei;Ying, Rendong;Liu, Peilin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The capability of autonomous exploration in complex, unknown environments is important in many robotic applications.
- While recent research on autonomous exploration have achieved much progress, there are still limitations, e.g., existing methods relying on greedy heuristics or optimal path planning are often hindered by repetitive paths and high computational demands.To address such limitations, we propose a novel exploration framework that utilizes the global topology information of observed environment to improve exploration efficiency while reducing computational overhead.Specifically, global information is utilized based on a skeletal topological graph representation of the environment geometry.
- We first propose an incremental skeleton extraction method based on wavefront propagation, based on which we then design an approach to generate a lightweight topological graph that can effectively capture the environment's structural characteristics.

## Task

* Motion Planning

## Keywords

* Motion and Path Planning
* Reactive and Sensor-Based Planning

## AI依存度

* Non-AI

## 何を解決？

* The capability of autonomous exploration in complex, unknown environments is important in many robotic applications.

## 何が新しい？

* While recent research on autonomous exploration have achieved much progress, there are still limitations, e.g., existing methods relying on greedy heuristics or optimal path planning are often hindered by repetitive paths and high computational demands.To address such limitations, we propose a novel exploration framework that utilizes the global topology information of observed environment to improve exploration efficiency while reducing computational overhead.Specifically, global information is utilized based on a skeletal topological graph representation of the environment geometry.

## どうやってる？

* While recent research on autonomous exploration have achieved much progress, there are still limitations, e.g., existing methods relying on greedy heuristics or optimal path planning are often hindered by repetitive paths and high computational demands.To address such limitations, we propose a novel exploration framework that utilizes the global topology information of observed environment to improve exploration efficiency while reducing computational overhead.Specifically, global information is utilized based on a skeletal topological graph representation of the environment geometry.

## どこが強い？

* Experimental results demonstrate the superiority of our method in comparison with state-of-the-art methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* While recent research on autonomous exploration have achieved much progress, there are still limitations, e.g., existing methods relying on greedy heuristics or optimal path planning are often hindered by repetitive paths and high computational demands.To address such limitations, we propose a novel exploration framework that utilizes the global topology information of observed environment to improve exploration efficiency while reducing computational overhead.Specifically, global information is utilized based on a skeletal topological graph representation of the environment geometry.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
