# Flying Calligrapher: Contact-Aware Motion and Force Planning and Control for Aerial Manipulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planning with Contact |
| arXiv | [http://arxiv.org/abs/2407.05587](http://arxiv.org/abs/2407.05587) |
| Authors | Guo, Xiaofeng;He, Guanqi;Xu, Jiahe;Mousaei, Mohammadreza;Geng, Junyi;Scherer, Sebastian;Shi, Guanya |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Aerial manipulation has gained interest in completing high-altitude tasks that are challenging for human workers, such as contact inspection and defect detection, etc.
- Previous research has focused on maintaining static contact points or forces.
- This letter addresses a more general and dynamic task: simultaneously tracking time-varying contact force in the surface normal direction and motion trajectories on tangential surfaces.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Manipulation

## Keywords

* Aerial Systems: Applications
* Aerial Systems: Mechanics and Control
* Integrated Planning and Control

## AI依存度

* Non-AI

## 何を解決？

* Aerial manipulation has gained interest in completing high-altitude tasks that are challenging for human workers, such as contact inspection and defect detection, etc.

## 何が新しい？

* We propose a pipeline that includes a contact-aware trajectory planner to generate dynamically feasible trajectories, and a hybrid motion-force controller to track such trajectories.

## どうやってる？

* Experiments show our method can effectively draw diverse letters, achieving an IoU of 0.59 and an end-effector position (force) tracking RMSE of 2.9 cm (0.7 N).

## どこが強い？

* We demonstrate the approach in an aerial calligraphy task using a novel sponge pen design as the end-effector, whose stroke width is positively related to the contact force.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a pipeline that includes a contact-aware trajectory planner to generate dynamically feasible trajectories, and a hybrid motion-force controller to track such trajectories.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
