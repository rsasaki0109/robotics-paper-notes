# V2X-DG: Domain Generalization for Vehicle-To-Everything Cooperative Perception

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception 2 |
| arXiv | [http://arxiv.org/abs/2503.15435](http://arxiv.org/abs/2503.15435) |
| Authors | Li, Baolu;Xu, Zongzhe;Li, Jinlong;Liu, Xinyu;Fang, Jianwu;Li, Xiaopeng;Yu, Hongkai |
| Source | ICRA 2025 / arXiv |

## TL;DR

- LiDAR-based Vehicle-to-Everything (V2X) cooperative perception has demonstrated its impact on the safety and effectiveness of autonomous driving.
- Since current cooperative perception algorithms are trained and tested on the same dataset, the generalization ability of cooperative perception systems remains underexplored.
- This paper is the first work to study the Domain Generalization problem for LiDAR-based V2X cooperative perception (V2X-DG) based on four widely-used open source datasets: OPV2V, V2XSet, V2V4Real and DAIR-V2X.

## Task

* LiDAR
* Visual-Inertial
* Perception
* Software Tools

## Keywords

* Computer Vision for Transportation
* Intelligent Transportation Systems
* Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* LiDAR-based Vehicle-to-Everything (V2X) cooperative perception has demonstrated its impact on the safety and effectiveness of autonomous driving.

## 何が新しい？

* To this end, we propose Cooperative Mixup Augmentation based Generalization (CMAG) to improve the model generalization capability by simulating the unseen cooperation, which is designed compactly for the domain gaps in cooperative perception.

## どうやってる？

* Extensive experiments demonstrate that our approach achieves significant performance gains when generalizing to other unseen datasets while it also maintains strong performance on the source dataset.

## どこが強い？

* Extensive experiments demonstrate that our approach achieves significant performance gains when generalizing to other unseen datasets while it also maintains strong performance on the source dataset.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we propose Cooperative Mixup Augmentation based Generalization (CMAG) to improve the model generalization capability by simulating the unseen cooperation, which is designed compactly for the domain gaps in cooperative perception.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
