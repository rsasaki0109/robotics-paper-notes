# PTZ-Calib: Robust Pan-Tilt-Zoom Camera Calibration

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Calibration 2 |
| arXiv | [http://arxiv.org/abs/2502.09075](http://arxiv.org/abs/2502.09075) |
| Authors | Guo, Jinhui, Fan, Lubin, Wu, Bojian, Gu, Jiaqi, Cao, Shen, Ye, Jieping |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we present PTZ-Calib, a robust two-stage PTZ camera calibration method, that efficiently and accurately estimates camera parameters for arbitrary viewpoints.
- Our method includes an offline and an online stage.
- Extensive evaluations demonstrate our robustness and superior performance over state-of-the-art methods on various real and synthetic datasets.

## Task

* SLAM
* Localization
* Calibration

## Keywords

* Surveillance Robotic Systems / Calibration and Identification / SLAM

## AI依存度

* Non-AI

## 何を解決？

* In the online stage, we formulate the calibration of any new viewpoints as a relocalization problem.

## 何が新しい？

* In this paper, we present PTZ-Calib, a robust two-stage PTZ camera calibration method, that efficiently and accurately estimates camera parameters for arbitrary viewpoints.

## どうやってる？

* In this paper, we present PTZ-Calib, a robust two-stage PTZ camera calibration method, that efficiently and accurately estimates camera parameters for arbitrary viewpoints.

## どこが強い？

* Extensive evaluations demonstrate our robustness and superior performance over state-of-the-art methods on various real and synthetic datasets.

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
* どのモジュールに効くか: localization / mapping, localization, sensor calibration / sensing
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
