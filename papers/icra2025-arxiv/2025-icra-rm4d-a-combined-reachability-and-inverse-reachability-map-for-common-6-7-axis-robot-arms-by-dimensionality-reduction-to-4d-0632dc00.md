# RM4D: A Combined Reachability and Inverse Reachability Map for Common 6-/7-Axis Robot Arms by Dimensionality Reduction to 4D

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Geometric Foundations |
| arXiv | [http://arxiv.org/abs/2410.06968](http://arxiv.org/abs/2410.06968) |
| Authors | Rudorfer, Martin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Knowledge of a manipulators workspace is fundamental for a variety of tasks including robot design, grasp planning and robot base placement.
- Consequently, workspace representations are well studied in robotics.
- Two important representations are reachability maps and inverse reachability maps.

## Task

* Manipulation

## Keywords

* Kinematics
* Mobile Manipulation
* Industrial Robots

## AI依存度

* Non-AI

## 何を解決？

* Knowledge of a manipulators workspace is fundamental for a variety of tasks including robot design, grasp planning and robot base placement.

## 何が新しい？

* We propose Reachability Map 4D (RM4D), a map that only requires a single 4D data structure for both forward and inverse queries.

## どうやってる？

* Typically, the reachability map is built by discretizing the 6D space containing the robots workspace and determining, for each cell, whether it is reachable or not.

## どこが強い？

* Finally, we showcase the efficiency gains by applying RM4D for finding suitable base positions in a scenario with 800 target grasps.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose Reachability Map 4D (RM4D), a map that only requires a single 4D data structure for both forward and inverse queries.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
