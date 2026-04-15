# Digital Model-Driven Genetic Algorithm for Optimizing Layout and Task Allocation in Human-Robot Collaborative Assemblies

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Human-Robot Collaboration 1 |
| arXiv | [http://arxiv.org/abs/2503.02774](http://arxiv.org/abs/2503.02774) |
| Authors | Cella, Christian;Robin, Matteo Bruce;Faroni, Marco;Zanchettin, Andrea Maria;Rocco, Paolo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper addresses the optimization of human-robot collaborative work-cells before their physical deployment.
- Most of the times, such environments are designed based on the experience of the system integrators, often leading to sub-optimal solutions.
- Accurate simulators of the robotic cell, accounting for the presence of the human as well, are available today and can be used in the pre-deployment.

## Task

* Visual-Inertial
* Human-Robot Interaction
* Software Tools

## Keywords

* Human-Robot Collaboration
* Design and Human Factors

## AI依存度

* Non-AI

## 何を解決？

* This paper addresses the optimization of human-robot collaborative work-cells before their physical deployment.

## 何が新しい？

* We propose an iterative optimization scheme where a digital model of the work-cell is updated based on a genetic algorithm.

## どうやってる？

* The methodology focuses on the layout optimization and task allocation, encoding both the problems simultaneously in the design variables handled by the genetic algorithm, while the task scheduling problem depends on the result of the upper-level one.

## どこが強い？

* The final solution balances conflicting objectives in the fitness function and is validated to show the impact of the objectives with respect to a baseline, which represents possible initial choices selected based on the human judgement.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose an iterative optimization scheme where a digital model of the work-cell is updated based on a genetic algorithm.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
