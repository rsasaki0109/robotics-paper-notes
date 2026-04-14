# Addition of a Peristaltic Wave Improves Multi-Legged Locomotion Performance on Complex Terrains

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Legged Locomotion: Novel Platforms |
| arXiv | [http://arxiv.org/abs/2410.01046](http://arxiv.org/abs/2410.01046) |
| Authors | Iaschi, Massimiliano, Chong, Baxi, Wang, Tianyu, Lin, Jianfeng, Xu, Zhaochen, Soto, Daniel, He, Juntao, Goldman, Daniel |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Characterized by their elongate bodies and relatively simple legs, multi-legged robots have the potential to locomote through complex terrains for applications such as search-and-rescue and terrain inspection.
- Seeking effective alternative waves for obstacle-climbing, we designed a five-segment robot with static (non-actuated) legs, where each cable-driven joint has a rotational degree-of-freedom (DoF) in the sagittal plane (vertical wave) and a linear DoF (peristaltic wave).
- Our results demonstrate an alternative actuation mechanism for multi-legged robots, paving the way towards all-terrain multi-legged robots.

## Task

* Legged Robotics

## Keywords

* Legged Robots / Search and Rescue Robots / Biologically-Inspired Robots

## AI依存度

* Non-AI

## 何を解決？

* Characterized by their elongate bodies and relatively simple legs, multi-legged robots have the potential to locomote through complex terrains for applications such as search-and-rescue and terrain inspection.

## 何が新しい？

* Seeking effective alternative waves for obstacle-climbing, we designed a five-segment robot with static (non-actuated) legs, where each cable-driven joint has a rotational degree-of-freedom (DoF) in the sagittal plane (vertical wave) and a linear DoF (peristaltic wave).

## どうやってる？

* We hypothesize that such limitations stem from the two-wave template that we used to prescribe the multi-legged locomotion.

## どこが強い？

* Our results demonstrate an alternative actuation mechanism for multi-legged robots, paving the way towards all-terrain multi-legged robots.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: limited direct use; estimator / controller design reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
