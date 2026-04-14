# GNSS/Multi-Sensor Fusion Using Continuous-Time Factor Graph Optimization for Robust Localization

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Localization 1 |
| arXiv | [http://arxiv.org/abs/2309.11134](http://arxiv.org/abs/2309.11134) |
| Authors | Zhang, Haoming, Chen, Chih-Chun, Vallery, Heike, Barfoot, Timothy |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper introduces GNSS-FGO, an online trajectory estimator that fuses GNSS observations alongside multiple sensor measurements for robust vehicle localization.
- In a test sequence containing a 17km route through Aachen, our method results in a mean 2-D positioning error of 0.48m while fusing raw GNSS observations with lidar odometry in tight coupling.
- Our results show that the proposed approach enables robust trajectory estimation in dense urban areas, where the classic multi-sensor fusion method fails.

## Task

* Localization
* GNSS Fusion
* LiDAR
* Sensor Fusion

## Keywords

* Sensor Fusion / Localization / Autonomous Vehicle Navigation / Factor Graph Optimization

## AI依存度

* Non-AI

## 何を解決？

* Accurate and robust vehicle localization in highly urbanized areas is challenging.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* This paper introduces GNSS-FGO, an online trajectory estimator that fuses GNSS observations alongside multiple sensor measurements for robust vehicle localization.

## どこが強い？

* Our results show that the proposed approach enables robust trajectory estimation in dense urban areas, where the classic multi-sensor fusion method fails.

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
* どのモジュールに効くか: localization, localization / gnss integration, sensing / localization / perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
