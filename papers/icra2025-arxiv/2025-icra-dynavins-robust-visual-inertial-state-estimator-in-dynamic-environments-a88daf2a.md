# DynaVINS++: Robust Visual-Inertial State Estimator in Dynamic Environments by Adaptive Truncated Least Squares and Stable State Recovery

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Visual-Inertial Odometry |
| arXiv | [http://arxiv.org/abs/2410.15373](http://arxiv.org/abs/2410.15373) |
| Authors | Song, Seungwon, Lim, Hyungtae, Lee, Alex, Myung, Hyun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- To overcome these problems, we propose a robust VINS framework called DynaVINS++, which employs a) adaptive truncated least square method that adaptively adjusts the truncation range using both feature association and IMU preintegration to effectively minimize the effect of the dynamic objects while reducing the computational cost, and b) stable state recovery with bias consistency check to correct misestimated IMU bias and to prevent the divergence caused by abruptly dynamic objects.
- Despite extensive research in robust visual-inertial navigation systems(VINS) in dynamic environments, many approaches remain vulnerable to objects that suddenly start moving, which are referred to as abruptly dynamic objects.
- As verified in both public and real-world datasets, our approach shows promising performance in dynamic environments, including scenes with abruptly dynamic objects.

## Task

* SLAM
* Localization
* Sensor Fusion
* State Estimation

## Keywords

* Visual-Inertial SLAM / Sensor Fusion / SLAM

## AI依存度

* Non-AI

## 何を解決？

* To overcome these problems, we propose a robust VINS framework called DynaVINS++, which employs a) adaptive truncated least square method that adaptively adjusts the truncation range using both feature association and IMU preintegration to effectively minimize the effect of the dynamic objects while reducing the computational cost, and b) stable state recovery with bias consistency check to correct misestimated IMU bias and to prevent the divergence caused by abruptly dynamic objects.

## 何が新しい？

* To overcome these problems, we propose a robust VINS framework called DynaVINS++, which employs a) adaptive truncated least square method that adaptively adjusts the truncation range using both feature association and IMU preintegration to effectively minimize the effect of the dynamic objects while reducing the computational cost, and b) stable state recovery with bias consistency check to correct misestimated IMU bias and to prevent the divergence caused by abruptly dynamic objects.

## どうやってる？

* To overcome these problems, we propose a robust VINS framework called DynaVINS++, which employs a) adaptive truncated least square method that adaptively adjusts the truncation range using both feature association and IMU preintegration to effectively minimize the effect of the dynamic objects while reducing the computational cost, and b) stable state recovery with bias consistency check to correct misestimated IMU bias and to prevent the divergence caused by abruptly dynamic objects.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: localization / mapping, localization, perception / localization fusion
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
