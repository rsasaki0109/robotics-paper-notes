# CGTrack: Cascade Gating Network with Hierarchical Feature Aggregation for UAV Tracking

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Tracking and Prediction 3 |
| arXiv | [http://arxiv.org/abs/2505.05936](http://arxiv.org/abs/2505.05936) |
| Authors | Li, Weihong;Liu, Xiaoqiong;Fan, Heng;Zhang, Libo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recent advancements in visual object tracking have markedly improved the capabilities of unmanned aerial vehicle (UAV) tracking, which is a critical component in real-world robotics applications.
- While the integration of hierarchical lightweight networks has become a prevalent strategy for enhancing efficiency in UAV tracking, it often results in a significant drop in network capacity, which further exacerbates challenges in UAV scenarios, such as frequent occlusions and extreme changes in viewing angles.
- To address these issues, we in this paper introduce a novel family of UAV trackers, termed CGTrack, which combines both explicit and implicit techniques to expand network capacity within a coarse-to-fine framework.

## Task

* Aerial Robotics
* Perception
* Software Tools

## Keywords

* Visual Tracking
* Computer Vision for Automation
* Visual Learning

## AI依存度

* Hybrid

## 何を解決？

* Recent advancements in visual object tracking have markedly improved the capabilities of unmanned aerial vehicle (UAV) tracking, which is a critical component in real-world robotics applications.

## 何が新しい？

* Specifically, we first introduce a Hierarchical Feature Cascade (HFC) module that leverages the spirit of feature reuse to increase network capacity by integrating the deep semantic cues with the rich spatial information, incurring minimal computational costs while enhancing feature representation.

## どうやってる？

* To address these issues, we in this paper introduce a novel family of UAV trackers, termed CGTrack, which combines both explicit and implicit techniques to expand network capacity within a coarse-to-fine framework.

## どこが強い？

* Extensive experiments on three challenging UAV tracking benchmarks demonstrate that CGTrack achieves state-of-the-art performance while running fast.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Specifically, we first introduce a Hierarchical Feature Cascade (HFC) module that leverages the spirit of feature reuse to increase network capacity by integrating the deep semantic cues with the rich spatial information, incurring minimal computational costs while enhancing feature representation.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
