# Agile Mobility with Rapid Online Adaptation Via Meta-Learning and Uncertainty-Aware MPPI

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Design and Control |
| arXiv | [http://arxiv.org/abs/2410.06565](http://arxiv.org/abs/2410.06565) |
| Authors | Kalaria, Dvij;Xue, Haoru;Xiao, Wenli;Tao, Tony;Shi, Guanya;Dolan, John M. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Modern non-linear model-based controllers require an accurate physics model and model parameters to be able to control mobile robots at their limits.
- Also, due to surface slipping at high speeds, the friction parameters may continually change (like tire degradation in autonomous racing), and the controller may need to adapt rapidly.
- Many works derive a task-specific robot model with a parameter adaptation scheme that works well for the task but requires a lot of effort and tuning for each platform and task.

## Task

* Visual-Inertial
* Control
* Software Tools

## Keywords

* Robust/Adaptive Control
* Machine Learning for Robot Control
* Representation Learning

## AI依存度

* Hybrid

## 何を解決？

* Modern non-linear model-based controllers require an accurate physics model and model parameters to be able to control mobile robots at their limits.

## 何が新しい？

* In this work, we design a full model-learning-based controller based on meta pre-training that can very quickly adapt using few-shot dynamics data to any wheel-based robot with any model parameters, while also reasoning about model uncertainty.

## どうやってる？

* Modern non-linear model-based controllers require an accurate physics model and model parameters to be able to control mobile robots at their limits.

## どこが強い？

* We demonstrate our results in small-scale numeric simulation, the large-scale Unity simulator, and on a medium-scale hardware platform with a wide range of settings.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this work, we design a full model-learning-based controller based on meta pre-training that can very quickly adapt using few-shot dynamics data to any wheel-based robot with any model parameters, while also reasoning about model uncertainty.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
