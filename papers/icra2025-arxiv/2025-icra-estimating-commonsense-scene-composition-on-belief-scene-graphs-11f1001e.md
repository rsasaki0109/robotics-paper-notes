# Estimating Commonsense Scene Composition on Belief Scene Graphs

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Mobile Robots 3 |
| arXiv | [http://arxiv.org/abs/2505.02405](http://arxiv.org/abs/2505.02405) |
| Authors | Valdes Saucedo, Mario Alberto, Kottayam Viswanathan, Vignesh, Kanellakis, Christoforos, Nikolakopoulos, George |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This work establishes the concept of commonsense scene composition, with a focus on extending Belief Scene Graphs by estimating the spatial distribution of unseen objects.
- Specifically, the commonsense scene composition capability refers to the understanding of the spatial relationships among related objects in the scene, which in this article is modeled as a joint probability distribution for all possible locations of the semantic object class.
- For a video of the article, showcasing the experimental demonstration, please refer to the following link: https://youtu.be/f0tqtPVFZ2A.

## Task

* Perception

## Keywords

* Semantic Scene Understanding / Learning Categories and Concepts / AI-Enabled Robotics

## AI依存度

* AI-heavy

## 何を解決？

* This work establishes the concept of commonsense scene composition, with a focus on extending Belief Scene Graphs by estimating the spatial distribution of unseen objects.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* The proposed framework includes two variants of a Correlation Information (CECI) model for learning probability distributions: (i) a baseline approach based on a Graph Convolutional Network, and (ii) a neuro-symbolic extension that integrates a spatial ontology based on Large Language Models (LLMs).

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* The proposed framework includes two variants of a Correlation Information (CECI) model for learning probability distributions: (i) a baseline approach based on a Graph Convolutional Network, and (ii) a neuro-symbolic extension that integrates a spatial ontology based on Large Language Models (LLMs).

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: perception
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
