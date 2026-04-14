# Non-Conservative Obstacle Avoidance for Multi-Body Systems Leveraging Convex Hulls and Predicted Closest Points

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 3 |
| arXiv | [http://arxiv.org/abs/2410.12659](http://arxiv.org/abs/2410.12659) |
| Authors | Rassaerts, Lotte, Suichies, Eke Janke, van de Vrande, Bram, Alonso, Marco, Meere, Bastiaan Guillermo Lorenzo, Chong, Michelle S., Torta, Elena |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper introduces a novel approach that integrates future closest point predictions into the distance constraints of a collision avoidance controller, leveraging convex hulls with closest point distance calculations.
- By addressing abrupt shifts in closest points, this method effectively reduces collision risks and enhances controller performance.
- Applied to an Image Guided Therapy robot and validated through simulations and user experiments, the framework demonstrates improved distance prediction accuracy, smoother trajectories, and safer navigation near obstacles.

## Task

* Motion Planning
* Control

## Keywords

* Collision Avoidance / Constrained Motion Planning / Computational Geometry

## AI依存度

* Non-AI

## 何を解決？

* This paper introduces a novel approach that integrates future closest point predictions into the distance constraints of a collision avoidance controller, leveraging convex hulls with closest point distance calculations.

## 何が新しい？

* This paper introduces a novel approach that integrates future closest point predictions into the distance constraints of a collision avoidance controller, leveraging convex hulls with closest point distance calculations.

## どうやってる？

* This paper introduces a novel approach that integrates future closest point predictions into the distance constraints of a collision avoidance controller, leveraging convex hulls with closest point distance calculations.

## どこが強い？

* Applied to an Image Guided Therapy robot and validated through simulations and user experiments, the framework demonstrates improved distance prediction accuracy, smoother trajectories, and safer navigation near obstacles.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: planning, control
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
