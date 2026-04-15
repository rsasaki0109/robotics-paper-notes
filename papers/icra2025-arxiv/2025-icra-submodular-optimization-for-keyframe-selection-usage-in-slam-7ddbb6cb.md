# Submodular Optimization for Keyframe Selection & Usage in SLAM

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | SLAM 3 |
| arXiv | [http://arxiv.org/abs/2410.05576](http://arxiv.org/abs/2410.05576) |
| Authors | Thorne, David;Chan, Nathan;Ma, Yanlong;Robison, Christopher, Christa;Osteen, Philip;Lopez, Brett |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Keyframes are LiDAR scans saved for future reference in Simultaneous Localization And Mapping (SLAM), but despite their central importance most algorithms leave choices of which scans to save and how to use them to wasteful heuristics.
- This work proposes two novel keyframe selection strategies for localization and map summarization, as well as a novel approach to submap generation which selects keyframes that best constrain localization.
- Our results show that online keyframe identification and submap generation reduce the number of saved keyframes and improve per scan computation time without compromising localization performance.

## Task

* SLAM
* Localization
* LiDAR
* Visual-Inertial

## Keywords

* SLAM
* Optimization and Optimal Control
* Field Robots

## AI依存度

* Non-AI

## 何を解決？

* Keyframes are LiDAR scans saved for future reference in Simultaneous Localization And Mapping (SLAM), but despite their central importance most algorithms leave choices of which scans to save and how to use them to wasteful heuristics.

## 何が新しい？

* This work proposes two novel keyframe selection strategies for localization and map summarization, as well as a novel approach to submap generation which selects keyframes that best constrain localization.

## どうやってる？

* This work proposes two novel keyframe selection strategies for localization and map summarization, as well as a novel approach to submap generation which selects keyframes that best constrain localization.

## どこが強い？

* Our results show that online keyframe identification and submap generation reduce the number of saved keyframes and improve per scan computation time without compromising localization performance.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This work proposes two novel keyframe selection strategies for localization and map summarization, as well as a novel approach to submap generation which selects keyframes that best constrain localization.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
