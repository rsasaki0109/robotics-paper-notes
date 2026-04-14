# Pinto: A Latched Spring Actuated Robot for Jumping and Perching

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Mechanism Design 2 |
| arXiv | [http://arxiv.org/abs/2409.09203](http://arxiv.org/abs/2409.09203) |
| Authors | Xu, Christopher, Yan, Huihan, Yim, Justin K. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Arboreal environments challenge current robots but are deftly traversed by many familiar animals such as squirrels.
- We present a small, 450 g robot "Pinto" developed for tree-jumping, a behavior seen in squirrels but rarely in legged robots: jumping from the ground onto a vertical tree trunk.
- We consider the effects of scaling down conventional quadrupeds and experimentally show how storing energy in a parallel-elastic fashion using a latch increases jump energy compared to series-elastic or springless strategies.

## Task

* Control
* Legged Robotics
* Manipulation

## Keywords

* Mechanism Design / Legged Robots / Compliant Joints and Mechanisms

## AI依存度

* Non-AI

## 何を解決？

* Arboreal environments challenge current robots but are deftly traversed by many familiar animals such as squirrels.

## 何が新しい？

* We present a small, 450 g robot "Pinto" developed for tree-jumping, a behavior seen in squirrels but rarely in legged robots: jumping from the ground onto a vertical tree trunk.

## どうやってる？

* By switching between series and parallel-elastic modes with our latched 5-bar leg mechanism, Pinto executes energetic jumps as well as maintains continuous control during shorter bounding motions.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We consider the effects of scaling down conventional quadrupeds and experimentally show how storing energy in a parallel-elastic fashion using a latch increases jump energy compared to series-elastic or springless strategies.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: control, limited direct use; estimator / controller design reference, limited direct use; integration pattern reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
