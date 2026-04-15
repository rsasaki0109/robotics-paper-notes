# FGO-SLAM: Enhancing Gaussian SLAM with Globally Consistent Opacity Radiance Field

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | SLAM 5 |
| arXiv | [http://arxiv.org/abs/2509.01547](http://arxiv.org/abs/2509.01547) |
| Authors | Zhu, Fan;Zhao, Yifan;Chen, Ziyu;Yu, Biao;Zhu, Hui |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Visual SLAM has regained attention due to its ability to provide perception capabilities and simulation test data for Embodied AI.
- However, traditional SLAM systems struggle to meet the demands of high-quality scene reconstruction, and Gaussian SLAM systems, despite their rapid rendering and high-quality mapping capabilities, lack effective pose optimization methods and face challenges in geometric reconstruction.
- To address these issues, we introduce FGO-SLAM, a Gaussian SLAM system that employs an opacity radiance field as the scene representation to enhance geometric mapping performance.

## Task

* SLAM
* LiDAR
* Visual-Inertial
* Perception

## Keywords

* Mapping
* SLAM
* Embodied Cognitive Science

## AI依存度

* Non-AI

## 何を解決？

* Visual SLAM has regained attention due to its ability to provide perception capabilities and simulation test data for Embodied AI.

## 何が新しい？

* To address these issues, we introduce FGO-SLAM, a Gaussian SLAM system that employs an opacity radiance field as the scene representation to enhance geometric mapping performance.

## どうやってる？

* However, traditional SLAM systems struggle to meet the demands of high-quality scene reconstruction, and Gaussian SLAM systems, despite their rapid rendering and high-quality mapping capabilities, lack effective pose optimization methods and face challenges in geometric reconstruction.

## どこが強い？

* Results across various real-world and large-scale synthetic datasets demonstrate that our method achieves state-of-the-art tracking accuracy and mapping performance.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these issues, we introduce FGO-SLAM, a Gaussian SLAM system that employs an opacity radiance field as the scene representation to enhance geometric mapping performance.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
