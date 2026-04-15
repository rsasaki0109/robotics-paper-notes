# CRAB: Camera-Radar Fusion for Reducing Depth Ambiguity in Backward Projection Based View Transformation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 6 |
| arXiv | [http://arxiv.org/abs/2509.05785](http://arxiv.org/abs/2509.05785) |
| Authors | Lee, In-Jae;Hwang, Sihwan;Kim, Youngseok;Kim, Wonjune;Kim, Sanmin;Kum, Dongsuk |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recently, camera-radar fusion-based 3D object detection methods in bird's eye view (BEV) have gained attention due to the complementary characteristics and cost-effectiveness of these sensors.
- Previous approaches using forward projection struggle with sparse BEV feature generation, while those employing backward projection overlook depth ambiguity, leading to false positives.
- In this paper, to address the aforementioned limitations, we propose a novel camera-radar fusion-based 3D object detection and segmentation model named CRAB (Camera-Radar fusion for reducing depth Ambiguity in Backward projection-based view transformation), using a backward projection that leverages radar to mitigate depth ambiguity.

## Task

* Perception
* Software Tools

## Keywords

* Object Detection
* Segmentation and Categorization
* Computer Vision for Transportation
* Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* Recently, camera-radar fusion-based 3D object detection methods in bird's eye view (BEV) have gained attention due to the complementary characteristics and cost-effectiveness of these sensors.

## 何が新しい？

* In this paper, to address the aforementioned limitations, we propose a novel camera-radar fusion-based 3D object detection and segmentation model named CRAB (Camera-Radar fusion for reducing depth Ambiguity in Backward projection-based view transformation), using a backward projection that leverages radar to mitigate depth ambiguity.

## どうやってる？

* Recently, camera-radar fusion-based 3D object detection methods in bird's eye view (BEV) have gained attention due to the complementary characteristics and cost-effectiveness of these sensors.

## どこが強い？

* When evaluated on the nuScenes open dataset, our proposed approach achieves a state-of-the-art performance among backward projection-based camera-radar fusion methods with 62.4% NDS and 54.0% mAP in 3D object detection.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, to address the aforementioned limitations, we propose a novel camera-radar fusion-based 3D object detection and segmentation model named CRAB (Camera-Radar fusion for reducing depth Ambiguity in Backward projection-based view transformation), using a backward projection that leverages radar to mitigate depth ambiguity.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
