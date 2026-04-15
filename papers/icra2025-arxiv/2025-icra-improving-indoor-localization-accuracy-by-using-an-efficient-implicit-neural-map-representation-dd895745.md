# Improving Indoor Localization Accuracy by Using an Efficient Implicit Neural Map Representation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Localization 4 |
| arXiv | [http://arxiv.org/abs/2503.23480](http://arxiv.org/abs/2503.23480) |
| Authors | Kuang, Haofei;Pan, Yue;Zhong, Xingguang;Wiesmann, Louis;Behley, Jens;Stachniss, Cyrill |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Globally localizing a mobile robot in a known map is often a foundation for enabling robots to navigate and operate autonomously.
- In indoor environments, traditional Monte Carlo localization based on occupancy grid maps is considered the gold standard, but its accuracy is limited by the representation capabilities of the occupancy grid map.
- In this paper, we address the problem of building an effective map representation that allows to accurately perform probabilistic global localization.

## Task

* Localization
* LiDAR
* Perception
* Software Tools

## Keywords

* Localization
* Mapping
* Deep Learning Methods

## AI依存度

* Hybrid

## 何を解決？

* Globally localizing a mobile robot in a known map is often a foundation for enabling robots to navigate and operate autonomously.

## 何が新しい？

* To this end, we propose an implicit neural map representation that is able to capture positional and directional geometric features from 2D LiDAR scans to efficiently represent the environment and learn a neural network that is able to predict both, the non-projective signed distance and a direction-aware projective distance for an arbitrary point in the mapped environment.

## どうやってる？

* We evaluated our approach to indoor localization on a publicly available dataset for global localization and the experimental results indicate that our approach is able to more accurately localize a mobile robot than other localization approaches employing occupancy or existing neural map representations.

## どこが強い？

* We evaluated our approach to indoor localization on a publicly available dataset for global localization and the experimental results indicate that our approach is able to more accurately localize a mobile robot than other localization approaches employing occupancy or existing neural map representations.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we propose an implicit neural map representation that is able to capture positional and directional geometric features from 2D LiDAR scans to efficiently represent the environment and learn a neural network that is able to predict both, the non-projective signed distance and a direction-aware projective distance for an arbitrary point in the mapped environment.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
