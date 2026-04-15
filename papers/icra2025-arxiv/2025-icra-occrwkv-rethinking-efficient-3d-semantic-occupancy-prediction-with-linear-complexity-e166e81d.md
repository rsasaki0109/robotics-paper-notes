# OccRWKV: Rethinking Efficient 3D Semantic Occupancy Prediction with Linear Complexity

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Deep Learning for Visual Perception 3 |
| arXiv | [http://arxiv.org/abs/2409.19987](http://arxiv.org/abs/2409.19987) |
| Authors | Wang, Junming;Yin, Wei;Long, Xiaoxiao;Zhang, Xingyu;Xing, Zebin;Guo, Xiaoyang;Zhang, Qian |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 3D semantic occupancy prediction networks have demonstrated remarkable capabilities in reconstructing the geometric and semantic structure of 3D scenes, providing crucial information for robot navigation and autonomous driving systems.
- However, due to their large overhead from dense network structure designs, existing networks face challenges balancing accuracy and latency.
- In this paper, we introduce OccRWKV, an efficient semantic occupancy network inspired by Receptance Weighted Key Value (RWKV).

## Task

* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* Visual Learning
* Computer Vision for Automation

## AI依存度

* Hybrid

## 何を解決？

* 3D semantic occupancy prediction networks have demonstrated remarkable capabilities in reconstructing the geometric and semantic structure of 3D scenes, providing crucial information for robot navigation and autonomous driving systems.

## 何が新しい？

* Leveraging the sparse nature of real-world 3D occupancy, we reduce computational overhead by projecting features into the bird's-eye view (BEV) space and propose a BEV-RWKV block for efficient feature enhancement and fusion.

## どうやってる？

* Experiments demonstrate that OccRWKV outperforms the state-of-the-art methods on the SemanticKITTI dataset, achieving a mIoU of 25.1 while being 20 times faster than the best baseline, Co-Occ, making it suitable for real-time deployment on robots to enhance autonomous navigation efficiency.

## どこが強い？

* 3D semantic occupancy prediction networks have demonstrated remarkable capabilities in reconstructing the geometric and semantic structure of 3D scenes, providing crucial information for robot navigation and autonomous driving systems.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Leveraging the sparse nature of real-world 3D occupancy, we reduce computational overhead by projecting features into the bird's-eye view (BEV) space and propose a BEV-RWKV block for efficient feature enhancement and fusion.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
