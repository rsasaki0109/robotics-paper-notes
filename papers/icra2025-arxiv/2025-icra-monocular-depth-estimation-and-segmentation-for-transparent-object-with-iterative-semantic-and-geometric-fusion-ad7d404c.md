# Monocular Depth Estimation and Segmentation for Transparent Object with Iterative Semantic and Geometric Fusion

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Image and 3D Segmentation 1 |
| arXiv | [http://arxiv.org/abs/2502.14616](http://arxiv.org/abs/2502.14616) |
| Authors | Liu, Jiangyuan;Ma, Hongxuan;Guo, Yuxin;Zhao, Yuhao;Zhang, Chi;Sui, Wei;Zou, Wei |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Transparent object perception is indispensable for numerous robotic tasks.
- However, accurately segmenting and estimating the depth of transparent objects remain challenging due to complex optical properties.
- Existing methods primarily delve into only one task using extra inputs or specialized sensors, neglecting the valuable interactions among tasks and the subsequent refinement process, leading to suboptimal and blurry predictions.

## Task

* Manipulation
* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* Perception for Grasping and Manipulation
* Object Detection
* Segmentation and Categorization

## AI依存度

* Hybrid

## 何を解決？

* Transparent object perception is indispensable for numerous robotic tasks.

## 何が新しい？

* To address these issues, we propose a monocular framework, which is the first to excel in both segmentation and depth estimation of transparent objects, with only a single-image input.

## どうやってる？

* Existing methods primarily delve into only one task using extra inputs or specialized sensors, neglecting the valuable interactions among tasks and the subsequent refinement process, leading to suboptimal and blurry predictions.

## どこが強い？

* Experiments on two challenging synthetic and real-world datasets demonstrate that our model surpasses state-of-the-art monocular, stereo, and multi-view methods by a large margin of about 38.8%-46.2% with only a single RGB input.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these issues, we propose a monocular framework, which is the first to excel in both segmentation and depth estimation of transparent objects, with only a single-image input.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
