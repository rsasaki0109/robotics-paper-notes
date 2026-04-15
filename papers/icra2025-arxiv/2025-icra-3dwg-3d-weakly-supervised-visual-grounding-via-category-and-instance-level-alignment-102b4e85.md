# 3DWG: 3D Weakly Supervised Visual Grounding Via Category and Instance-Level Alignment

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception Systems |
| arXiv | [http://arxiv.org/abs/2505.01809](http://arxiv.org/abs/2505.01809) |
| Authors | Li, Xiaoqi;Liu, Jiaming;Han, Nuowei;Heng, Liang;Guo, Yandong;Dong, Hao;Liu, Yang |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The 3D weakly-supervised visual grounding task aims to localize oriented 3D boxes in point clouds based on natural language descriptions without requiring annotations to guide model learning.
- This setting presents two primary challenges: category-level ambiguity and instance-level complexity.
- Category-level ambiguity arises from representing objects of fine-grained categories in a highly sparse point cloud format, making category distinction challenging.

## Task

* LiDAR
* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* RGB-D Perception
* Visual Learning

## AI依存度

* Hybrid

## 何を解決？

* The 3D weakly-supervised visual grounding task aims to localize oriented 3D boxes in point clouds based on natural language descriptions without requiring annotations to guide model learning.

## 何が新しい？

* To address these challenges, we propose a novel weakly-supervised grounding approach that explicitly differentiates between categories and instances.

## どうやってる？

* Compared to previous methods, our approach achieves state-of-the-art performance on three widely used benchmarks: Nr3D, Sr3D, and ScanRef.

## どこが強い？

* The 3D weakly-supervised visual grounding task aims to localize oriented 3D boxes in point clouds based on natural language descriptions without requiring annotations to guide model learning.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these challenges, we propose a novel weakly-supervised grounding approach that explicitly differentiates between categories and instances.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
