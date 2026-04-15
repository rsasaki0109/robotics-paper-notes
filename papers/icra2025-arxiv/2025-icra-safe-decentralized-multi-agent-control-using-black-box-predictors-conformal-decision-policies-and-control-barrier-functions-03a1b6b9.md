# Safe Decentralized Multi-Agent Control Using Black-Box Predictors, Conformal Decision Policies, and Control Barrier Functions

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Mechanism Design 3 |
| arXiv | [http://arxiv.org/abs/2409.18862](http://arxiv.org/abs/2409.18862) |
| Authors | Huriot, Sacha;Sibai, Hussein |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We address the challenge of safe control in decentralized multi-agent robotic settings, where agents use uncertain black-box models to predict other agents' trajectories.
- We use the recently proposed conformal decision theory to adapt the restrictiveness of control barrier functions-based safety constraints based on observed prediction errors.
- We use these constraints to synthesize controllers that balance between the objectives of safety and task accomplishment, despite the prediction errors.

## Task

* Control
* Aerial Robotics
* Software Tools

## Keywords

* Robust/Adaptive Control
* Robot Safety
* Machine Learning for Robot Control

## AI依存度

* Hybrid

## 何を解決？

* We address the challenge of safe control in decentralized multi-agent robotic settings, where agents use uncertain black-box models to predict other agents' trajectories.

## 何が新しい？

* We use the recently proposed conformal decision theory to adapt the restrictiveness of control barrier functions-based safety constraints based on observed prediction errors.

## どうやってる？

* We address the challenge of safe control in decentralized multi-agent robotic settings, where agents use uncertain black-box models to predict other agents' trajectories.

## どこが強い？

* We validate our theory through experimental results showing the performance of our controllers when navigating a robot in the multi-agent scenes in the Stanford Drone Dataset.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We use the recently proposed conformal decision theory to adapt the restrictiveness of control barrier functions-based safety constraints based on observed prediction errors.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
