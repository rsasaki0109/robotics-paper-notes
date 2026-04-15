# SSF: Sparse Long-Range Scene Flow for Autonomous Driving

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Vision-Based Navigation 2 |
| arXiv | [http://arxiv.org/abs/2501.17821](http://arxiv.org/abs/2501.17821) |
| Authors | Khoche, Ajinkya;Zhang, Qingwen;Pereira Sanchez, Laura;Asefaw, Aron;Sharif Mansouri, Sina;Jensfelt, Patric |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Scene flow enables an understanding of the motion characteristics of the environment in the 3D world.
- It gains particular significance in the long-range, where object-based perception methods might fail due to sparse observations far away.
- Although significant advancements have been made in scene flow pipelines to handle large-scale point clouds, a gap remains in scalability with respect to long-range.

## Task

* LiDAR
* Perception
* Software Tools

## Keywords

* Deep Learning Methods
* Computer Vision for Transportation
* Object Detection
* Segmentation and Categorization

## AI依存度

* Hybrid

## 何を解決？

* Scene flow enables an understanding of the motion characteristics of the environment in the 3D world.

## 何が新しい？

* In this paper, we propose Sparse Scene Flow (SSF), a general pipeline for long-range scene flow, adopting a sparse convolution based backbone for feature extraction.

## どうやってる？

* It gains particular significance in the long-range, where object-based perception methods might fail due to sparse observations far away.

## どこが強い？

* Our method, SSF, achieves state-of-the-art results on the Argoverse2 dataset, demonstrating strong performance in long-range scene flow estimation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we propose Sparse Scene Flow (SSF), a general pipeline for long-range scene flow, adopting a sparse convolution based backbone for feature extraction.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
