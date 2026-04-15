# Data-Driven Sampling Based Stochastic MPC for Skid-Steer Mobile Robot Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Design and Control |
| arXiv | [http://arxiv.org/abs/2411.03289](http://arxiv.org/abs/2411.03289) |
| Authors | Trivedi, Ananya;Prajapati, Sarvesh;Shirgaonkar, Anway Prasad;Zolotas, Mark;Padir, Taskin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Traditional approaches to motion modeling for skid-steer robots struggle to capture nonlinear tire-terrain dynamics, especially during high-speed maneuvers.
- In this paper, we tackle such nonlinearities by enhancing a dynamic unicycle model with Gaussian Process (GP) regression outputs.
- This enables us to develop an adaptive, uncertainty-informed navigation formulation.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Perception

## Keywords

* Model Learning for Control
* Planning under Uncertainty
* Robust/Adaptive Control

## AI依存度

* Hybrid

## 何を解決？

* Traditional approaches to motion modeling for skid-steer robots struggle to capture nonlinear tire-terrain dynamics, especially during high-speed maneuvers.

## 何が新しい？

* The GPU implementation of the proposed method and supplementary video footage are available at https://stochasticmppi.github.io.

## どうやってる？

* We solve the resultant stochastic optimal control problem using a chance-constrained Model Predictive Path Integral (MPPI) control method.

## どこが強い？

* We further validate our approach through hardware experiments on a skid-steer robot platform, demonstrating its effectiveness in high-speed navigation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* The GPU implementation of the proposed method and supplementary video footage are available at https://stochasticmppi.github.io.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
