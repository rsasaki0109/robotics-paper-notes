# M2Distill: Multi-Modal Distillation for Lifelong Imitation Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Transfer and Continual Learning |
| arXiv | [http://arxiv.org/abs/2410.00064](http://arxiv.org/abs/2410.00064) |
| Authors | Roy, Kaushik;Dissanayake, Akila;Tidd, Brendan;Moghadam, Peyman |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Lifelong imitation learning for manipulation tasks poses significant challenges due to distribution shifts that occur in incremental learning steps.
- Existing methods often focus on unsupervised skill discovery to construct an ever-growing skill library or distillation from multiple policies, which can lead to scalability issues as diverse manipulation tasks are continually introduced and may fail to ensure a consistent latent space throughout the learning process, leading to catastrophic forgetting of previously learned skills.
- In this paper, we introduce M2Distill, a multi-modal distillation-based method for lifelong imitation learning focusing on preserving consistent latent space across vision, language, and action distributions throughout the learning process.

## Task

* Manipulation
* Software Tools

## Keywords

* Continual Learning
* Incremental Learning
* Imitation Learning

## AI依存度

* Hybrid

## 何を解決？

* Lifelong imitation learning for manipulation tasks poses significant challenges due to distribution shifts that occur in incremental learning steps.

## 何が新しい？

* By regulating the shifts in latent representations across different modalities from previous to current steps, and reducing discrepancies in Gaussian Mixture Model (GMM) policies between consecutive learning steps, we ensure that the learned policy retains its ability to perform previously learned tasks while seamlessly integrating new skills.

## どうやってる？

* Existing methods often focus on unsupervised skill discovery to construct an ever-growing skill library or distillation from multiple policies, which can lead to scalability issues as diverse manipulation tasks are continually introduced and may fail to ensure a consistent latent space throughout the learning process, leading to catastrophic forgetting of previously learned skills.

## どこが強い？

* Extensive evaluations on the LIBERO lifelong imitation learning benchmark suites, including LIBERO-OBJECT, LIBERO-GOAL, and LIBERO-SPATIAL, demonstrate that our method consistently outperforms prior state-of-the-art methods across all evaluated metrics.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* By regulating the shifts in latent representations across different modalities from previous to current steps, and reducing discrepancies in Gaussian Mixture Model (GMM) policies between consecutive learning steps, we ensure that the learned policy retains its ability to perform previously learned tasks while seamlessly integrating new skills.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
