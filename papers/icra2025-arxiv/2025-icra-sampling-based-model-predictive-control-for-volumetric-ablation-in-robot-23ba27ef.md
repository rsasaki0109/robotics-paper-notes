# Sampling-Based Model Predictive Control for Volumetric Ablation in Robotic Laser Surgery

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Surgical Robotics: Planning |
| arXiv | [http://arxiv.org/abs/2410.03152](http://arxiv.org/abs/2410.03152) |
| Authors | Wang, Vincent, Prakash, Ravi, Oca, Siobhan, LoCicero, Ethan, Codd, Patrick, Bridgeman, Leila |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper describes a sampling-based model predictive control (MPC) scheme to plan ablation sequences for arbitrary tissue volumes.
- Laser-based surgical ablation relies heavily on surgeon involvement, restricting precision to the limits of human error and perception.
- The interaction between laser and tissue is governed by various laser parameters that control the laser irradiance on the tissue, including the power, distance, spot size, orientation, and exposure time.

## Task

* Perception
* Motion Planning
* Control

## Keywords

* Surgical Robotics: Planning / Constrained Motion Planning / Integrated Planning and Control

## AI依存度

* Non-AI

## 何を解決？

* Laser-based surgical ablation relies heavily on surgeon involvement, restricting precision to the limits of human error and perception.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* The interaction between laser and tissue is governed by various laser parameters that control the laser irradiance on the tissue, including the power, distance, spot size, orientation, and exposure time.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: perception, planning, control
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
