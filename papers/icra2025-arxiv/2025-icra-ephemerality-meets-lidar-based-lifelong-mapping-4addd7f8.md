# Ephemerality Meets LiDAR-Based Lifelong Mapping

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Robot Mapping 2 |
| arXiv | [http://arxiv.org/abs/2502.13452](http://arxiv.org/abs/2502.13452) |
| Authors | Gil, Hyeonjae;Lee, Dongjae;Kim, Giseop;Kim, Ayoung |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Lifelong mapping is crucial for the long-term deployment of robots in dynamic environments.
- In this paper, we present ELite, an ephemerality-aided LiDAR-based lifelong mapping framework which can seamlessly align multiple session data, remove dynamic objects, and update maps in an end-to-end fashion.
- Map elements are typically classified as static or dynamic, but cases like parked cars indicate the need for more detailed categories than binary.

## Task

* SLAM
* LiDAR
* Software Tools

## Keywords

* Mapping
* SLAM
* Range Sensing

## AI依存度

* Non-AI

## 何を解決？

* Lifelong mapping is crucial for the long-term deployment of robots in dynamic environments.

## 何が新しい？

* In this paper, we present ELite, an ephemerality-aided LiDAR-based lifelong mapping framework which can seamlessly align multiple session data, remove dynamic objects, and update maps in an end-to-end fashion.

## どうやってる？

* Central to our approach is the probabilistic modeling of the world into two-stage ephemerality, which represent the transiency of points in the map within two different time scales.

## どこが強い？

* Extensive real-world experiments on long-term datasets demonstrate the robustness and effectiveness of our system.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we present ELite, an ephemerality-aided LiDAR-based lifelong mapping framework which can seamlessly align multiple session data, remove dynamic objects, and update maps in an end-to-end fashion.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
