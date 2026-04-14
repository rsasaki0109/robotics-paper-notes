# Distributed Certifiably Correct Range-Aided SLAM

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | SLAM 4 |
| arXiv | [http://arxiv.org/abs/2503.03192](http://arxiv.org/abs/2503.03192) |
| Authors | Thoms, Alexander, Papalia, Alan, Velasquez, Jared, Rosen, David, Narasimhan, Sriram |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The state estimation problem for these systems takes the form of range-aided (RA) SLAM.
- To this end, we present the first distributed algorithm for RA-SLAM that can efficiently recover certifiably globally optimal solutions.
- Our algorithm, distributed certifiably correct RA-SLAM (DCORA), achieves this via the Riemannian Staircase method, where computational procedures developed for distributed certifiably correct pose graph optimization are generalized to the RA-SLAM problem.

## Task

* SLAM
* Localization
* Mapping
* Motion Planning

## Keywords

* Multi-Robot SLAM / Range Sensing

## AI依存度

* Non-AI

## 何を解決？

* The state estimation problem for these systems takes the form of range-aided (RA) SLAM.

## 何が新しい？

* To this end, we present the first distributed algorithm for RA-SLAM that can efficiently recover certifiably globally optimal solutions.

## どうやってる？

* In the communication-constrained multi-agent setting, navigation systems increasingly use point-to-point range sensors as they afford measurements with low bandwidth requirements and known data association.

## どこが強い？

* Our algorithm, distributed certifiably correct RA-SLAM (DCORA), achieves this via the Riemannian Staircase method, where computational procedures developed for distributed certifiably correct pose graph optimization are generalized to the RA-SLAM problem.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
