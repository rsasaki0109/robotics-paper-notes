# Search-Based Path Planning in Interactive Environments among Movable Obstacles

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 1 |
| arXiv | [http://arxiv.org/abs/2410.18333](http://arxiv.org/abs/2410.18333) |
| Authors | Ren, Zhongqiang;Suvonov, Bunyod;Chen, Guofei;He, Botao;Liao, Yijie;Fermuller, Cornelia;Zhang, Ji |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper investigates Path planning Among Movable Obstacles (PAMO), which seeks a minimum cost collision-free path among static obstacles from start to goal while allowing the robot to push away movable obstacles (i.e., objects) along its path when needed.
- To develop planners that are complete and optimal for PAMO, the planner has to search a giant state space involving both the location of the robot as well as the locations of the objects, which grows exponentially with respect to the number of objects.
- This paper leverages a simple yet under-explored idea that, only a small fraction of this giant state space needs to be searched during planning as guided by a heuristic, and most of the objects far away from the robot are intact, which thus leads to runtime efficient algorithms.

## Task

* Visual-Inertial
* Motion Planning

## Keywords

* Motion and Path Planning

## AI依存度

* Non-AI

## 何を解決？

* This paper investigates Path planning Among Movable Obstacles (PAMO), which seeks a minimum cost collision-free path among static obstacles from start to goal while allowing the robot to push away movable obstacles (i.e., objects) along its path when needed.

## 何が新しい？

* Based on this idea, this paper introduces two PAMO formulations, i.e., bi-objective and resource constrained problems in an occupancy grid, and develops PAMO*, a planning method with completeness and solution optimality guarantees, to solve the two problems.

## どうやってる？

* Based on this idea, this paper introduces two PAMO formulations, i.e., bi-objective and resource constrained problems in an occupancy grid, and develops PAMO*, a planning method with completeness and solution optimality guarantees, to solve the two problems.

## どこが強い？

* Our results show that, PAMO* can often find optimal solutions within a second in cluttered maps with up to 400 objects.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Based on this idea, this paper introduces two PAMO formulations, i.e., bi-objective and resource constrained problems in an occupancy grid, and develops PAMO*, a planning method with completeness and solution optimality guarantees, to solve the two problems.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
