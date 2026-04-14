# Effective Self-Righting Strategies for Elongate Multi-Legged Robots

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Legged Locomotion: Novel Platforms |
| arXiv | [http://arxiv.org/abs/2410.01056](http://arxiv.org/abs/2410.01056) |
| Authors | Teder, Erik, Chong, Baxi, He, Juntao, Wang, Tianyu, Iaschi, Massimiliano, Soto, Daniel, Goldman, Daniel |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Centipede-like robots offer an effective and robust solution to navigation over complex terrain with minimal sensing.
- However, when climbing over obstacles, such multi-legged robots often elevate their center-of-mass into unstable configurations, where even moderate terrain uncertainty can cause tipping over.
- Robust mechanisms for such elongate multi-legged robots to self-right remain unstudied.

## Task

* Motion Planning
* Control
* Legged Robotics

## Keywords

* Legged Robots / Field Robots / Multi-Contact Whole-Body Motion Planning and Control

## AI依存度

* Non-AI

## 何を解決？

* Centipede-like robots offer an effective and robust solution to navigation over complex terrain with minimal sensing.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* However, when climbing over obstacles, such multi-legged robots often elevate their center-of-mass into unstable configurations, where even moderate terrain uncertainty can cause tipping over.

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
* どのモジュールに効くか: planning, control, limited direct use; estimator / controller design reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
