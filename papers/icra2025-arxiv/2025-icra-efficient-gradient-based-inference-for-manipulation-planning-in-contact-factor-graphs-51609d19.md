# Efficient Gradient-Based Inference for Manipulation Planning in Contact Factor Graphs

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planning with Contact |
| arXiv | [http://arxiv.org/abs/2503.06300](http://arxiv.org/abs/2503.06300) |
| Authors | Lee, Jeongmin;Park, Sunkyung;Lee, Minji;Lee, Dongjun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper presents a framework designed to tackle a range of planning problems arise in manipulation, which typically involve complex geometric-physical reasoning related to contact and dynamic constraints.
- We introduce the Contact Factor Graph (CFG) to graphically model these diverse factors, enabling us to perform inference on the graphs to approximate the distribution and sample appropriate solutions.
- We propose a novel approach that can incorporate various phenomena of contact manipulation as differentiable factors, and develop an efficient inference algorithm for CFG that leverages this differentiability along with the conditional probabilities arising from the structured nature of contact.

## Task

* Manipulation

## Keywords

* Manipulation Planning
* Contact Modeling
* Dexterous Manipulation

## AI依存度

* Non-AI

## 何を解決？

* This paper presents a framework designed to tackle a range of planning problems arise in manipulation, which typically involve complex geometric-physical reasoning related to contact and dynamic constraints.

## 何が新しい？

* We propose a novel approach that can incorporate various phenomena of contact manipulation as differentiable factors, and develop an efficient inference algorithm for CFG that leverages this differentiability along with the conditional probabilities arising from the structured nature of contact.

## どうやってる？

* We propose a novel approach that can incorporate various phenomena of contact manipulation as differentiable factors, and develop an efficient inference algorithm for CFG that leverages this differentiability along with the conditional probabilities arising from the structured nature of contact.

## どこが強い？

* Our results demonstrate the capability of our framework in generating viable samples and approximating posterior distributions for various manipulation scenarios.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a novel approach that can incorporate various phenomena of contact manipulation as differentiable factors, and develop an efficient inference algorithm for CFG that leverages this differentiability along with the conditional probabilities arising from the structured nature of contact.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
