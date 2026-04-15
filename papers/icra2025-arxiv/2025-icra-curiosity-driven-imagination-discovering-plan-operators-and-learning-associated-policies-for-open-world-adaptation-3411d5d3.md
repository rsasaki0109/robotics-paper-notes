# Curiosity-Driven Imagination: Discovering Plan Operators and Learning Associated Policies for Open-World Adaptation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Task and Motion Planning 1 |
| arXiv | [http://arxiv.org/abs/2503.04931](http://arxiv.org/abs/2503.04931) |
| Authors | Lorang, Pierrick;Lu, Hong;Scheutz, Matthias |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Adapting quickly to dynamic, uncertain environmentsoften called ``open worlds"remains a major challenge in robotics.
- Traditional Task and Motion Planning (TAMP) approaches struggle to cope with unforeseen changes, are data-inefficient when adapting, and do not leverage world models during learning.
- We address this issue with a hybrid planning and learning system that integrates two models: a low-level neural network-based model that learns stochastic transitions and drives exploration via an Intrinsic Curiosity Module (ICM), and a high-level symbolic planning model that captures abstract transitions using operators, enabling the agent to plan in an ``imaginary" space and generate reward machines.

## Task

* Motion Planning
* Manipulation

## Keywords

* Integrated Planning and Learning
* Task and Motion Planning
* Learning from Experience

## AI依存度

* Hybrid

## 何を解決？

* Adapting quickly to dynamic, uncertain environmentsoften called ``open worlds"remains a major challenge in robotics.

## 何が新しい？

* Adapting quickly to dynamic, uncertain environmentsoften called ``open worlds"remains a major challenge in robotics.

## どうやってる？

* Our evaluation in a robotic manipulation domain with sequential novelty injections demonstrates that our approach converges faster and outperforms state-of-the-art hybrid methods.

## どこが強い？

* Our evaluation in a robotic manipulation domain with sequential novelty injections demonstrates that our approach converges faster and outperforms state-of-the-art hybrid methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Adapting quickly to dynamic, uncertain environmentsoften called ``open worlds"remains a major challenge in robotics.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
