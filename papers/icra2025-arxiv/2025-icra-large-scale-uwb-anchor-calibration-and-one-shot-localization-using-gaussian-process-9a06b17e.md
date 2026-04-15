# Large-Scale UWB Anchor Calibration and One-Shot Localization Using Gaussian Process

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Calibration 3 |
| arXiv | [http://arxiv.org/abs/2412.16880](http://arxiv.org/abs/2412.16880) |
| Authors | Yuan, Shenghai;Lou, Boyang;Nguyen, Thien-Minh;Yin, Pengyu;Li, Jianping;Xu, Xinhang;Cao, Muqing;Xu, Jie;Chen, Siyu;Xie, Lihua |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Ultra-wideband (UWB) is gaining popularity with devices like AirTags for precise home item localization but faces significant challenges when scaled to large environments like seaports.
- The main challenges are calibration and localization in obstructed conditions, which are common in logistics environments.
- Traditional calibration methods, dependent on line-of-sight (LoS), are slow, costly, and unreliable in seaports and warehouses, making large-scale localization a significant pain point in the industry.

## Task

* Localization
* GNSS
* LiDAR
* Calibration

## Keywords

* Range Sensing
* Localization
* Factory Automation

## AI依存度

* Non-AI

## 何を解決？

* Ultra-wideband (UWB) is gaining popularity with devices like AirTags for precise home item localization but faces significant challenges when scaled to large environments like seaports.

## 何が新しい？

* To overcome these challenges, we propose a UWB-LiDAR fusion-based calibration and one-shot localization framework.

## どうやってる？

* Traditional calibration methods, dependent on line-of-sight (LoS), are slow, costly, and unreliable in seaports and warehouses, making large-scale localization a significant pain point in the industry.

## どこが強い？

* We demonstrate that by applying a UWB-range filter, the search range for LiDAR loop closure descriptors is significantly reduced, improving both accuracy and speed.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To overcome these challenges, we propose a UWB-LiDAR fusion-based calibration and one-shot localization framework.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
