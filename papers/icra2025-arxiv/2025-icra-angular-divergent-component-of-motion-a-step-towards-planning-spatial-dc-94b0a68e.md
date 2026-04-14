# Angular Divergent Component of Motion: A Step towards Planning Spatial DCM Objectives for Legged Robots

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Legged Locomotion: Novel Methods |
| arXiv | [http://arxiv.org/abs/2409.12796](http://arxiv.org/abs/2409.12796) |
| Authors | Herron, Connor, Schuller, Robert, Beiter, Benjamin, Griffin, Robert J., Leonessa, Alexander, Englsberger, Johannes |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this work, the Divergent Component of Motion (DCM) method is expanded to include angular coordinates for the first time.
- This work introduces the idea of spatial DCM, which adds an angular objective to the existing linear DCM theory.
- A simulation in MATLAB and hardware results on the TORO humanoid are presented to validate the framework's performance.

## Task

* Motion Planning
* Control
* Legged Robotics

## Keywords

* Humanoid and Bipedal Locomotion / Body Balancing / Whole-Body Motion Planning and Control

## AI依存度

* Non-AI

## 何を解決？

* In this work, the Divergent Component of Motion (DCM) method is expanded to include angular coordinates for the first time.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* A simulation in MATLAB and hardware results on the TORO humanoid are presented to validate the framework's performance.

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
* どのモジュールに効くか: planning, control, limited direct use; estimator / controller design reference
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
