# Adaptive Task Allocation in Multi-Human Multi-Robot Teams under Team Heterogeneity and Dynamic Information Uncertainty

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot and Human-Robot Teams |
| arXiv | [http://arxiv.org/abs/2409.13824](http://arxiv.org/abs/2409.13824) |
| Authors | Yuan, Ziqin, Wang, Ruiqi, Kim, Taehyeon, Zhao, Dezhong, Obi, Ike, Min, Byung-Cheol |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Task allocation in multi-human multi-robot (MH-MR) teams presents significant challenges due to the inherent heterogeneity of team members, the dynamics of task execution, and the information uncertainty of operational states.
- To tackle this, we propose an adaptive task allocation method using hierarchical reinforcement learning (HRL), incorporating initial task allocation (ITA) that leverages team heterogeneity and conditional task reallocation in response to dynamic operational states.
- Through an extensive case study in large-scale environmental monitoring tasks, we demonstrate the benefits of our approach.

## Task

* Motion Planning

## Keywords

* Human-Robot Teaming / Task Planning / Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* Task allocation in multi-human multi-robot (MH-MR) teams presents significant challenges due to the inherent heterogeneity of team members, the dynamics of task execution, and the information uncertainty of operational states.

## 何が新しい？

* To tackle this, we propose an adaptive task allocation method using hierarchical reinforcement learning (HRL), incorporating initial task allocation (ITA) that leverages team heterogeneity and conditional task reallocation in response to dynamic operational states.

## どうやってる？

* To tackle this, we propose an adaptive task allocation method using hierarchical reinforcement learning (HRL), incorporating initial task allocation (ITA) that leverages team heterogeneity and conditional task reallocation in response to dynamic operational states.

## どこが強い？

* Through an extensive case study in large-scale environmental monitoring tasks, we demonstrate the benefits of our approach.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Existing approaches often fail to address these challenges simultaneously, resulting in suboptimal performance.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: planning
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
