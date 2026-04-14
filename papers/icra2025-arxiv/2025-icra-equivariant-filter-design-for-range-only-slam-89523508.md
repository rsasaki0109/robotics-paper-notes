# Equivariant Filter Design for Range-Only SLAM

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | SLAM 3 |
| arXiv | [http://arxiv.org/abs/2503.03973](http://arxiv.org/abs/2503.03973) |
| Authors | Ge, Yixiao, Pearce, Arthur, van Goor, Pieter, Mahony, Robert |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We derive an equivariant filter (EqF) for the RO-SLAM problem based on a symmetry Lie group that is compatible with the range measurements.
- Range-only Simultaneous Localisation and Mapping (RO-SLAM) is of interest in the robotics community due to its practical applications; for example, ultra-wideband (UWB) and Bluetooth Low Energy (BLE) localisation in terrestrial and aerial applications and acoustic beacon localisation in marine applications.
- The proposed filter does not require bootstrapping or initialisation of landmark positions, and demonstrates robustness to the no-prior situation.

## Task

* SLAM
* Localization
* Mapping
* Aerial Robotics

## Keywords

* SLAM / Range Sensing / Mapping

## AI依存度

* Non-AI

## 何を解決？

* We derive an equivariant filter (EqF) for the RO-SLAM problem based on a symmetry Lie group that is compatible with the range measurements.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* The proposed filter does not require bootstrapping or initialisation of landmark positions, and demonstrates robustness to the no-prior situation.

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
