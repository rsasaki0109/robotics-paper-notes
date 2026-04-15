# LiftFeat: 3D Geometry-Aware Local Feature Matching

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Localization 5 |
| arXiv | [http://arxiv.org/abs/2505.03422](http://arxiv.org/abs/2505.03422) |
| Authors | Liu, Yepeng;Lai, Wenpeng;Zhao, Zhou;Xiong, Yuxuan;Zhu, Jinchi;Cheng, Jun;Xu, Yongchao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robust and efficient local feature matching plays a crucial role in applications such as SLAM and visual localization for robotics.
- Despite great progress, it is still very challenging to extract robust and discriminative visual features in scenarios with drastic lighting changes, low texture areas, or repetitive patterns.
- In this paper, we propose a new lightweight network called LiftFeat, which lifts the robustness of raw descriptor by aggregating 3D geometric feature.

## Task

* SLAM
* Localization
* Perception

## Keywords

* Deep Learning for Visual Perception
* Visual Learning
* Localization

## AI依存度

* Hybrid

## 何を解決？

* Robust and efficient local feature matching plays a crucial role in applications such as SLAM and visual localization for robotics.

## 何が新しい？

* In this paper, we propose a new lightweight network called LiftFeat, which lifts the robustness of raw descriptor by aggregating 3D geometric feature.

## どうやってる？

* Extensive experimental results on relative pose estimation, homography estimation, and visual localization tasks, demonstrate that our LiftFeat outperforms some lightweight state-of-the-art methods.

## どこが強い？

* Extensive experimental results on relative pose estimation, homography estimation, and visual localization tasks, demonstrate that our LiftFeat outperforms some lightweight state-of-the-art methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we propose a new lightweight network called LiftFeat, which lifts the robustness of raw descriptor by aggregating 3D geometric feature.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
