# TANGO: Traversability-Aware Navigation with Local Metric Control for Topological Goals

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning for Navigation |
| arXiv | [http://arxiv.org/abs/2509.08699](http://arxiv.org/abs/2509.08699) |
| Authors | Podgorski, Stefan, Garg, Sourav, Hosseinzadeh, Mehdi, Mares, Lachlan, Dayoub, Feras, Reid, Ian |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We address key limitations of previous methods by continuously predicting local trajectory rollout using monocular depth and traversability estimation, and incorporating an auto-switching mechanism that falls back to a baseline controller when necessary.
- In this work, we present a novel RGB-only, object-level topometric navigation pipeline that enables zero-shot, long-horizon robot navigation without requiring 3D maps or pre-trained controllers.
- We demonstrate the effectiveness of our method in both simulated environments and real-world tests, highlighting its robustness and deployability.

## Task

* Motion Planning
* Control

## Keywords

* Learning from Demonstration / Machine Learning for Robot Control / Vision-Based Navigation

## AI依存度

* Hybrid

## 何を解決？

* The system operates using foundational models, ensuring open-set applicability without the need for domain-specific fine-tuning.

## 何が新しい？

* In this work, we present a novel RGB-only, object-level topometric navigation pipeline that enables zero-shot, long-horizon robot navigation without requiring 3D maps or pre-trained controllers.

## どうやってる？

* Visual navigation in robotics traditionally relies on globally-consistent 3D maps or learned controllers, which can be computationally expensive and difficult to generalize across diverse environments.

## どこが強い？

* We demonstrate the effectiveness of our method in both simulated environments and real-world tests, highlighting its robustness and deployability.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* We address key limitations of previous methods by continuously predicting local trajectory rollout using monocular depth and traversability estimation, and incorporating an auto-switching mechanism that falls back to a baseline controller when necessary.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
