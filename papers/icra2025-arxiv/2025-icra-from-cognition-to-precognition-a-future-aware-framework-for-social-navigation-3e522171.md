# From Cognition to Precognition: A Future-Aware Framework for Social Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Social Navigation 1 |
| arXiv | [http://arxiv.org/abs/2409.13244](http://arxiv.org/abs/2409.13244) |
| Authors | Gong, Zeying;Hu, Tianshuai;Qiu, Ronghe;Liang, Junwei |
| Source | ICRA 2025 / arXiv |

## TL;DR

- To navigate safely and efficiently in crowded spaces, robots should not only perceive the current state of the environment but also anticipate future human movements.
- In this paper, we propose a reinforcement learning architecture, namely Falcon, to tackle socially-aware navigation by explicitly predicting human trajectories and penalizing actions that block future human paths.
- To facilitate realistic evaluation, we introduce a novel SocialNav benchmark containing two new datasets, Social-HM3D and Social-MP3D.

## Task

* Motion Planning
* Software Tools

## Keywords

* Vision-Based Navigation
* Human-Aware Motion Planning

## AI依存度

* Hybrid

## 何を解決？

* To navigate safely and efficiently in crowded spaces, robots should not only perceive the current state of the environment but also anticipate future human movements.

## 何が新しい？

* In this paper, we propose a reinforcement learning architecture, namely Falcon, to tackle socially-aware navigation by explicitly predicting human trajectories and penalizing actions that block future human paths.

## どうやってる？

* We conduct a detailed experimental analysis with the state-of-the-art learning-based method and two classic rule-based path-planning algorithms on the new benchmark.

## どこが強い？

* We conduct a detailed experimental analysis with the state-of-the-art learning-based method and two classic rule-based path-planning algorithms on the new benchmark.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we propose a reinforcement learning architecture, namely Falcon, to tackle socially-aware navigation by explicitly predicting human trajectories and penalizing actions that block future human paths.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
