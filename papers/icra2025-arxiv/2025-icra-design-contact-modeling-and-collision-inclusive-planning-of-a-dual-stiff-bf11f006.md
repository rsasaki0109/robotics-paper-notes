# Design, Contact Modeling, and Collision-Inclusive Planning of a Dual-Stiffness Aerial RoboT (DART)

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Planning and Control |
| arXiv | [http://arxiv.org/abs/2504.18780](http://arxiv.org/abs/2504.18780) |
| Authors | Kumar, Yogesh, Patnaik, Karishma, Zhang, Wenlong |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper introduces DART, a Dual-stiffness Aerial RoboT, that adapts its post-collision response by either engaging a locking mechanism for a rigid mode or disengaging it for a flexible mode, respectively.
- To understand and harness the collision dynamics, we propose a novel collision response prediction model based on the linear complementarity system theory.
- We demonstrate the accuracy of predicting collision forces for both the rigid and flexible modes of DART.

## Task

* Motion Planning
* Control
* Aerial Robotics

## Keywords

* Aerial Systems: Mechanics and Control / Aerial Systems: Applications / Motion Control

## AI依存度

* Non-AI

## 何を解決？

* Collision-resilient quadrotors have gained significant attention for operating in cluttered environments and leveraging impacts to perform agile maneuvers.

## 何が新しい？

* To understand and harness the collision dynamics, we propose a novel collision response prediction model based on the linear complementarity system theory.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* We demonstrate the accuracy of predicting collision forces for both the rigid and flexible modes of DART.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Comprehensive characterization tests highlight the significant difference in post-collision responses between its rigid and flexible modes, with the rigid mode offering seven times higher stiffness compared to the flexible mode.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: planning, control, out of direct Autoware scope, but architecture reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
