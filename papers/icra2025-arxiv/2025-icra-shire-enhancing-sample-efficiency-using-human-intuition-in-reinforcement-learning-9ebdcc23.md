# SHIRE: Enhancing Sample Efficiency Using Human Intuition in REinforcement Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Bio-Inspired Robot Learning |
| arXiv | [http://arxiv.org/abs/2409.09990](http://arxiv.org/abs/2409.09990) |
| Authors | Joshi, Amogh;Kosta, Adarsh Kumar;Roy, Kaushik |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The ability of neural networks to perform robotic perception and control tasks such as depth and optical flow estimation, simultaneous localization and mapping (SLAM), and automatic control has led to their widespread adoption in recent years.
- Deep Reinforcement Learning (DeepRL) has been used extensively in these settings, as it does not have the unsustainable training costs associated with supervised learning.
- However, DeepRL suffers from poor sample efficiency, i.e., it requires a large number of environmental interactions to converge to an acceptable solution.

## Task

* SLAM
* Localization
* Visual-Inertial
* Control

## Keywords

* Reinforcement Learning
* Bioinspired Robot Learning
* Probabilistic Inference

## AI依存度

* Hybrid

## 何を解決？

* The ability of neural networks to perform robotic perception and control tasks such as depth and optical flow estimation, simultaneous localization and mapping (SLAM), and automatic control has led to their widespread adoption in recent years.

## 何が新しい？

* In this work, we propose SHIRE, a novel framework for encoding human intuition using Probabilistic Graphical Models (PGMs) and using it in the Deep RL training pipeline to enhance sample efficiency.

## どうやってる？

* In this work, we propose SHIRE, a novel framework for encoding human intuition using Probabilistic Graphical Models (PGMs) and using it in the Deep RL training pipeline to enhance sample efficiency.

## どこが強い？

* Our framework achieves 25�?8% sample efficiency gains across the environments we evaluate at negligible overhead cost.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this work, we propose SHIRE, a novel framework for encoding human intuition using Probabilistic Graphical Models (PGMs) and using it in the Deep RL training pipeline to enhance sample efficiency.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
