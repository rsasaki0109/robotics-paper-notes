# QuasiNav: Asymmetric Cost-Aware Navigation Planning with Constrained Quasimetric Reinforcement Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 2 |
| arXiv | [http://arxiv.org/abs/2410.16666](http://arxiv.org/abs/2410.16666) |
| Authors | Hossain, Jumman, Faridee, Abu-Zaher, Asher, Derrik, Freeman, Jade, Gregory, Timothy, Trout, Theron T., Roy, Nirmalya |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we introduce QuasiNav, a novel reinforcement learning framework that integrates quasimetric embeddings to explicitly model asymmetric costs and guide efficient, safe navigation.
- Autonomous navigation in unstructured outdoor environments is inherently challenging due to the presence of asymmetric traversal costs, such as varying energy expenditures for uphill versus downhill movement.
- Experimental results show that QuasiNav significantly outperforms conventional methods, achieving higher success rates, improved energy efficiency (13.6% reduction in energy consumption compared to baseline methods), and better adherence to safety constraints.

## Task

* Motion Planning
* Intelligent Vehicles

## Keywords

* Reinforcement Learning / Autonomous Vehicle Navigation / Motion and Path Planning

## AI依存度

* Hybrid

## 何を解決？

* QuasiNav formulates the navigation problem as a constrained Markov decision process (CMDP) and employs quasimetric embeddings to capture directionally dependent costs, allowing for a more accurate representation of the terrain.

## 何が新しい？

* In this paper, we introduce QuasiNav, a novel reinforcement learning framework that integrates quasimetric embeddings to explicitly model asymmetric costs and guide efficient, safe navigation.

## どうやってる？

* Traditional reinforcement learning methods often assume symmetric costs, which can lead to suboptimal navigation paths and increased safety risks in real-world scenarios.

## どこが強い？

* Experimental results show that QuasiNav significantly outperforms conventional methods, achieving higher success rates, improved energy efficiency (13.6% reduction in energy consumption compared to baseline methods), and better adherence to safety constraints.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Experimental results show that QuasiNav significantly outperforms conventional methods, achieving higher success rates, improved energy efficiency (13.6% reduction in energy consumption compared to baseline methods), and better adherence to safety constraints.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: planning, planning / control / perception
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
