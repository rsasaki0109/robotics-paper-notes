# Tracking Everything in Robotic-Assisted Surgery

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Tracking and Prediction 3 |
| arXiv | [http://arxiv.org/abs/2409.19821](http://arxiv.org/abs/2409.19821) |
| Authors | Zhan, Bohan, Zhao, Wang, Fang, Yi, Du, Bo, Vasconcelos, Francisco, Stoyanov, Danail, Elson, Daniel, Huang, Baoru |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Furthermore, we propose a new tracking method, namely SurgMotion, to solve the challenges and further improve the tracking performance.
- To address this gap, we introduce a new annotated surgical tracking dataset for benchmarking tracking methods for surgical scenarios, comprising real-world surgical videos with complex tissue and instrument motions.
- Recently, the Tracking Any Point (TAP) algorithm was proposed to overcome these limitations and achieve dense accurate long-term tracking.

## Task

* Perception

## Keywords

* Computer Vision for Medical Robotics / Surgical Robotics: Laparoscopy

## AI依存度

* Non-AI

## 何を解決？

* Furthermore, we propose a new tracking method, namely SurgMotion, to solve the challenges and further improve the tracking performance.

## 何が新しい？

* To address this gap, we introduce a new annotated surgical tracking dataset for benchmarking tracking methods for surgical scenarios, comprising real-world surgical videos with complex tissue and instrument motions.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* Recently, the Tracking Any Point (TAP) algorithm was proposed to overcome these limitations and achieve dense accurate long-term tracking.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Our proposed method outperforms most TAP-based algorithms in surgical instruments tracking, and especially demonstrates significant improvements over baselines in challenging medical videos.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: perception
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
