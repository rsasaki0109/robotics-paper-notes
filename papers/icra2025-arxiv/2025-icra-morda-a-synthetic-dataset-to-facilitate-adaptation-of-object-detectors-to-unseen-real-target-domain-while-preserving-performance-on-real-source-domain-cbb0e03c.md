# MORDA: A Synthetic Dataset to Facilitate Adaptation of Object Detectors to Unseen Real-Target Domain While Preserving Performance on Real-Source Domain

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 1 |
| arXiv | [http://arxiv.org/abs/2501.04950](http://arxiv.org/abs/2501.04950) |
| Authors | Lim, Hojun;Yoo, Heecheol;Lee, Jinwoo;Jeon, Seungmin;Jeon, Hyeongseok |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Deep neural network (DNN) based perception models are indispensable in the development of autonomous vehicles (AVs).
- However, their reliance on large-scale, high-quality data is broadly recognized as a burdensome necessity due to the substantial cost of data acquisition and labeling.
- Further, the issue is not a one-time concern as AVs might need a new dataset if they are to be deployed to another region (real-target domain) that the in-hand dataset within the real-source domain cannot incorporate.

## Task

* Visual-Inertial
* Perception
* Software Tools

## Keywords

* Data Sets for Robotic Vision
* Deep Learning for Visual Perception
* Object Detection
* Segmentation and Categorization

## AI依存度

* Hybrid

## 何を解決？

* Deep neural network (DNN) based perception models are indispensable in the development of autonomous vehicles (AVs).

## 何が新しい？

* To mitigate this burden, we propose leveraging synthetic environments as an auxiliary domain where the characteristics of real domains are reproduced.

## どうやってる？

* As a practical demonstration of our methodology, nuScenes and South Korea are employed to represent real-source and real-target domains, respectively.

## どこが強い？

* Our experiments present that MORDA can significantly improve mean Average Precision (mAP) on AI-Hub dataset while that on nuScenes is retained or slightly enhanced.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To mitigate this burden, we propose leveraging synthetic environments as an auxiliary domain where the characteristics of real domains are reproduced.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
