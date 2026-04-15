# Estimating Control Barriers from Offline Data

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Collision Avoidance 1 |
| arXiv | [http://arxiv.org/abs/2503.10641](http://arxiv.org/abs/2503.10641) |
| Authors | Yu, Hongzhan;Farrell, Seth;Yoshimitsu, Ryo;Qin, Zhizhen;Christensen, Henrik;Gao, Sicun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Learning-based methods for constructing control barrier functions (CBFs) are gaining popularity, for enforcing safety in practical robot control under complex dynamics and uncertainty that are hard to model.
- A major limitation of existing methods is their reliance on extensive sampling over the state space, making it hard to construct CBFs on real robots.
- In this work we introduce methods for learning neural CBFs through a fixed, sparsely-labeled dataset collected prior to training either the CBFs or the controllers.

## Task

* Control
* Software Tools

## Keywords

* AI-Based Methods
* Robot Safety
* Collision Avoidance

## AI依存度

* Hybrid

## 何を解決？

* Learning-based methods for constructing control barrier functions (CBFs) are gaining popularity, for enforcing safety in practical robot control under complex dynamics and uncertainty that are hard to model.

## 何が新しい？

* We propose novel annotation techniques based on out-of-distribution analysis to effectively propagate the information from the limited labeled data to the unlabeled data.

## どうやってる？

* Learning-based methods for constructing control barrier functions (CBFs) are gaining popularity, for enforcing safety in practical robot control under complex dynamics and uncertainty that are hard to model.

## どこが強い？

* We evaluate the proposed algorithm on real-world platforms.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose novel annotation techniques based on out-of-distribution analysis to effectively propagate the information from the limited labeled data to the unlabeled data.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
