# FuzzRisk: Online Collision Risk Estimation for Autonomous Vehicles Based on Depth-Aware Object Detection Via Fuzzy Inference

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Collision Avoidance 1 |
| arXiv | [http://arxiv.org/abs/2411.08060](http://arxiv.org/abs/2411.08060) |
| Authors | Liao, Brian Hsuan-Cheng;Xu, Yingjie;Cheng, Chih-Hong;Esen, Hasan;Knoll, Alois |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper presents a novel monitoring framework that infers the level of collision risk for autonomous vehicles (AVs) based on their object detection performance.
- The framework takes two sets of predictions from different algorithms and associates their inconsistencies with the collision risk via fuzzy inference.
- The first set of predictions is obtained by retrieving safety-critical 2.5D objects from a depth map, and the second set comes from the ordinary AV's 3D object detector.

## Task

* Visual-Inertial
* Perception
* Software Tools

## Keywords

* Object Detection
* Segmentation and Categorization
* Robot Safety
* Intelligent Transportation Systems

## AI依存度

* Non-AI

## 何を解決？

* This paper presents a novel monitoring framework that infers the level of collision risk for autonomous vehicles (AVs) based on their object detection performance.

## 何が新しい？

* This paper presents a novel monitoring framework that infers the level of collision risk for autonomous vehicles (AVs) based on their object detection performance.

## どうやってる？

* This paper presents a novel monitoring framework that infers the level of collision risk for autonomous vehicles (AVs) based on their object detection performance.

## どこが強い？

* We experimentally validate that, based on Intersection-over-Union (IoU) and a depth discrepancy measure, the inconsistencies between the two sets of predictions strongly correlate to the error of the 3D object detector against ground truths.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This paper presents a novel monitoring framework that infers the level of collision risk for autonomous vehicles (AVs) based on their object detection performance.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
