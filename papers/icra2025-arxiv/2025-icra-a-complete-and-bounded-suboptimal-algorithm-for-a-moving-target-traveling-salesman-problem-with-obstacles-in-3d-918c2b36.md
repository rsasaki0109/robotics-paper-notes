# A Complete and Bounded-Suboptimal Algorithm for a Moving Target Traveling Salesman Problem with Obstacles in 3D

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 3 |
| arXiv | [http://arxiv.org/abs/2504.14680](http://arxiv.org/abs/2504.14680) |
| Authors | Bhat, Anoop;Gutow, Geordan;Vundurthy, Bhaskar;Ren, Zhongqiang;Rathinam, Sivakumar;Choset, Howie |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The moving target traveling salesman problem with obstacles (MT-TSP-O) seeks an obstacle-free trajectory for an agent that intercepts a given set of moving targets, each within a specified time windows, and returns to the agent's starting position.
- Each target moves with a constant velocity within its time windows, and the agent has a speed limit no smaller than any target's speed.
- We present FMC*-TSP, the first complete and bounded-suboptimal algorithm for the MT-TSP-O, and results for an agent whose configuration space is in R^3.

## Task

* Motion Planning
* Control

## Keywords

* Motion and Path Planning
* Constrained Motion Planning
* Optimization and Optimal Control

## AI依存度

* Non-AI

## 何を解決？

* The moving target traveling salesman problem with obstacles (MT-TSP-O) seeks an obstacle-free trajectory for an agent that intercepts a given set of moving targets, each within a specified time windows, and returns to the agent's starting position.

## 何が新しい？

* We present FMC*-TSP, the first complete and bounded-suboptimal algorithm for the MT-TSP-O, and results for an agent whose configuration space is in R^3.

## どうやってる？

* We present FMC*-TSP, the first complete and bounded-suboptimal algorithm for the MT-TSP-O, and results for an agent whose configuration space is in R^3.

## どこが強い？

* We test FMC*-TSP on 280 problem instances with up to 40 targets and demonstrate its smaller median runtime than a baseline based on prior work.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We present FMC*-TSP, the first complete and bounded-suboptimal algorithm for the MT-TSP-O, and results for an agent whose configuration space is in R^3.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
