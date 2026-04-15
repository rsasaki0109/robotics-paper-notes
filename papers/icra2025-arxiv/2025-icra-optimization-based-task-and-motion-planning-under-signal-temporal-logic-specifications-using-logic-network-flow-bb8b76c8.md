# Optimization-Based Task and Motion Planning under Signal Temporal Logic Specifications Using Logic Network Flow

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Task and Motion Planning 1 |
| arXiv | [http://arxiv.org/abs/2409.19168](http://arxiv.org/abs/2409.19168) |
| Authors | Lin, Xuan;Ren, Jiming;Coogan, Samuel;Zhao, Ye |
| Source | ICRA 2025 / arXiv |

## TL;DR

- STL 付き TAMP を MILP で解くとき、logic tree の代わりに **logic network flow (LNF)** で論理を表す論文。
- predicate を leaf でなく **edge 上の flow constraint** として持つことで、convex relaxation を tighter にしている。
- 理論は綺麗だが、wall-clock では per-node cost も増えるので、常に速いわけではないのが正直なところ。

## Task

* Task and Motion Planning
* Formal Methods
* Mixed-Integer Optimization
* Temporal Logic

## Keywords

* STL / MILP / Logic Network Flow / Branch-and-Bound / Dynamic Network Flow

## AI依存度

* Non-AI

## 何を解決？

* STL 制約付き TAMP は expressiveness が高い一方、MILP 化すると branch-and-bound が重い。
* 従来の logic tree 表現は relaxation が緩く、探索木が膨らみやすい。
* そこで、**同じ論理仕様をもっと締まった形で MILP に載せたい**。

## 何が新しい？

* STL の論理構造を tree ではなく **network flow** として書き直す LNF。
* predicate を edge に持たせ、flow conservation と組み合わせて logic satisfaction を表す点。
* Dynamic Network Flow と接続して、論理仕様と motion graph を比較的すっきりつなぐ点。

## どうやってる？

* STL formula を再帰的に分解し、and/or 構造を network flow graph に変換する。
* 各 edge に「この predicate が満たされるならこの flow が通れる」という制約を載せる。
* motion 側は別の dynamic network flow として離散化された feasible trajectory graph を持つ。
* その両者を MILP で結合し、branch-and-bound で globally optimal な plan を探す。

## どこが強い？

* formal methods と optimization の接続がきれいで、考え方がかなり整理されている。
* root relaxation gap を小さくできるので、探索木を減らす方向には確かに効いている。
* STL 仕様を持つ multi-robot / locomotion 例まで見せていて、適用範囲のイメージが湧く。

## 弱そうなところ

* tighter でも per-node solve が重くなるので、**実時間が必ず勝つわけではない**。
* trajectory graph を事前に用意する必要があり、continuous state-space へそのまま行くのはまだ遠い。
* predicate を凸っぽく書ける前提が強い。

## 関連研究との違い

* logic tree ベースの STL-MILP より、**論理を flow graph に移す**のが本質的な違い。
* sampling-based TAMP より、global optimality / infeasibility certificate を持てる。
* GCS 的な graph optimization と formal logic encoding の中間にいる感じの論文。

## non-AIとして見る価値

* TAMP を learned policy でなく、**temporal logic + MILP** で押し切る formal planning の良い例。
* branch-and-bound の効き方まで含めて、数理最適化の視点で仕様駆動 planning を理解できる。

## 難易度

★★★★☆

## 自分の理解/感想

* かなり数理っぽいが、logic tree を flow に言い換える発想は美しい。
* 実務でそのまま使うには重いが、「仕様を持つ planning をどう最適化問題に落とすか」の教材として良い。
