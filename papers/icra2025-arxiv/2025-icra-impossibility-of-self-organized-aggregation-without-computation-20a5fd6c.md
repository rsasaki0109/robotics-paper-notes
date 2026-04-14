# Impossibility of Self-Organized Aggregation without Computation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Swarms 2 |
| arXiv | [http://arxiv.org/abs/2501.00390](http://arxiv.org/abs/2501.00390) |
| Authors | Steinberg, Roy, Solovey, Kiril |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we show that no such controller exists by investigating the geometric structure of controllers.
- In their seminal work, Gauci et al. (2014) studied the fundamental task of aggregation, wherein multiple robots need to gather without an a priori agreed-upon meeting location, using extremely limited hardware.
- That paper considered differential-drive robots that are memoryless and unable to compute.

## Task

* Motion Planning
* Control

## Keywords

* Swarm Robotics / Multi-Robot Systems / Path Planning for Multiple Mobile Robots or Agents

## AI依存度

* Non-AI

## 何を解決？

* In their seminal work, Gauci et al. (2014) studied the fundamental task of aggregation, wherein multiple robots need to gather without an a priori agreed-upon meeting location, using extremely limited hardware.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* Despite those severe limitations, Gauci et al. introduced a controller and proved mathematically that it aggregates a system of two robots for any initial state.

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

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
