# Towards Latency-Aware 3D Streaming Perception for Autonomous Driving

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 1 |
| arXiv | [http://arxiv.org/abs/2504.19115](http://arxiv.org/abs/2504.19115) |
| Authors | Peng, Jiaqi, Wang, Tai, Pang, Jiangmiao, Shen, Yuan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Although existing 3D perception algorithms have demonstrated significant improvements in performance, their deployment on edge devices continues to encounter critical challenges due to substantial runtime latency.
- We propose a new benchmark tailored for online evaluation by considering runtime latency.
- Based on the benchmark, we build a Latency-Aware 3D Streaming Perception (LASP) framework that addresses the latency issue through two primary components: 1) latency-aware history integration, which extends query propagation into a continuous process, ensuring the integration of historical data regardless of varying latency; 2) latency-aware predictive detection, a mechanism that compensates the detection results with the predicted trajectory and the posterior accessed latency.

## Task

* Perception
* Sensor Fusion
* Motion Planning
* Intelligent Vehicles

## Keywords

* Deep Learning for Visual Perception / Sensor Fusion

## AI依存度

* Hybrid

## 何を解決？

* Although existing 3D perception algorithms have demonstrated significant improvements in performance, their deployment on edge devices continues to encounter critical challenges due to substantial runtime latency.

## 何が新しい？

* We propose a new benchmark tailored for online evaluation by considering runtime latency.

## どうやってる？

* By incorporating the latency-aware mechanism, our method shows generalization across various latency levels, achieving an online performance that closely aligns with 80% of its offline evaluation on the Jetson AGX Orin without any acceleration techniques.

## どこが強い？

* Although existing 3D perception algorithms have demonstrated significant improvements in performance, their deployment on edge devices continues to encounter critical challenges due to substantial runtime latency.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
