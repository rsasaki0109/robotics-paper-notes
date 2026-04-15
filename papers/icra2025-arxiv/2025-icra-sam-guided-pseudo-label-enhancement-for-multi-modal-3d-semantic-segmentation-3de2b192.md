# SAM-Guided Pseudo Label Enhancement for Multi-Modal 3D Semantic Segmentation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Image and 3D Segmentation 1 |
| arXiv | [http://arxiv.org/abs/2502.00960](http://arxiv.org/abs/2502.00960) |
| Authors | Yang, Mingyu;Lu, Jitong;Kim, Hun-Seok |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Multi-modal 3D semantic segmentation is vital for applications such as autonomous driving and virtual reality (VR).
- To effectively deploy these models in real-world scenarios, it is essential to employ cross-domain adaptation techniques that bridge the gap between training data and real-world data.
- Recently, self-training with pseudo-labels has emerged as a predominant method for cross-domain adaptation in multi-modal 3D semantic segmentation.

## Task

* LiDAR
* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* Sensor Fusion

## AI依存度

* Hybrid

## 何を解決？

* Multi-modal 3D semantic segmentation is vital for applications such as autonomous driving and virtual reality (VR).

## 何が新しい？

* We propose an image-guided pseudo-label enhancement approach that leverages the complementary 2D prior knowledge from the Segment Anything Model (SAM) to introduce more reliable pseudo-labels, thereby boosting domain adaptation performance.

## どうやってる？

* Recently, self-training with pseudo-labels has emerged as a predominant method for cross-domain adaptation in multi-modal 3D semantic segmentation.

## どこが強い？

* Experiments conducted across multiple datasets and domain adaptation scenarios demonstrate that our proposed method significantly increases the quantity of high-quality pseudo-labels and enhances the adaptation performance over baseline methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose an image-guided pseudo-label enhancement approach that leverages the complementary 2D prior knowledge from the Segment Anything Model (SAM) to introduce more reliable pseudo-labels, thereby boosting domain adaptation performance.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
