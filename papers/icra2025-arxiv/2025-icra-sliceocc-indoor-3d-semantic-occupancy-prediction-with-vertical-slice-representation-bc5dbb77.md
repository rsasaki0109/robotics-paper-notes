# SliceOcc: Indoor 3D Semantic Occupancy Prediction with Vertical Slice Representation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Visual Perception and Learning |
| arXiv | [http://arxiv.org/abs/2501.16684](http://arxiv.org/abs/2501.16684) |
| Authors | Li, Jianing;Lu, Ming;Liu, Juntao;Wang, Hao;Gu, Chenyang;Zheng, Wenzhao;Du, Li;Zhang, Shanghang |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 3D semantic occupancy prediction is a crucial task in visual perception, demanding a simultaneous understanding of both scene geometry and semantics.
- It plays a pivotal role in 3D scene comprehension and holds great potential for various applications, such as robotic vision perception and autonomous driving.
- Many previous works leverage planar-based representations like Birds Eye View (BEV) and Tri-Perspective View (TPV), which aim to simplify the complexity of 3D scenes while preserving essential object information, thereby facilitating efficient scene representation.

## Task

* Visual-Inertial
* Perception
* Software Tools

## Keywords

* Computer Vision for Manufacturing
* Deep Learning for Visual Perception
* Visual Learning

## AI依存度

* Hybrid

## 何を解決？

* 3D semantic occupancy prediction is a crucial task in visual perception, demanding a simultaneous understanding of both scene geometry and semantics.

## 何が新しい？

* To harness these slice features, we propose SliceOcc, a camera-based model specifically tailored for indoor 3D semantic occupancy prediction.

## どうやってる？

* However, in dense indoor environments where occlusions are prevalent, directly applying these planar-based methods often leads to difficulties in capturing global semantic occupancy, ultimately degrading model performance.

## どこが強い？

* Experimental results on the EmbodiedScan dataset demonstrate that SliceOcc achieves a mIoU of 15.45% across 81 indoor categories, setting a new state-of-the-art performance among RGB-based models for indoor 3D semantic occupancy prediction.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To harness these slice features, we propose SliceOcc, a camera-based model specifically tailored for indoor 3D semantic occupancy prediction.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
