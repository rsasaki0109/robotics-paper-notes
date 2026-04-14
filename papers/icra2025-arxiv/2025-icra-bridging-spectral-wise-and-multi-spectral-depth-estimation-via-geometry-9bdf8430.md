# Bridging Spectral-Wise and Multi-Spectral Depth Estimation Via Geometry-Guided Contrastive Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Sensor Fusion 1 |
| arXiv | [http://arxiv.org/abs/2503.00793](http://arxiv.org/abs/2503.00793) |
| Authors | Shin, Ukcheol, Lee, Kyunghyun, Oh, Jean |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we propose an effective solution, named align-and-fuse strategy, for the depth estimation from multi-spectral images.
- Deploying depth estimation networks in the real world requires high-level robustness against various adverse conditions to ensure safe and reliable autonomy.
- After that, in the fuse stage, we train an attachable feature fusion module that can selectively aggregate the multi-spectral features for reliable and robust prediction results.

## Task

* LiDAR
* Perception
* Sensor Fusion
* Intelligent Vehicles

## Keywords

* Computer Vision for Transportation / Sensor Fusion / Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* Multi-modal fusion can provide high-level reliability, yet it needs a specialized architecture.

## 何が新しい？

* In this paper, we propose an effective solution, named align-and-fuse strategy, for the depth estimation from multi-spectral images.

## どうやってる？

* They mainly adopt two strategies to use multiple sensors: modality-wise and multi-modal fused inference.

## どこが強い？

* Deploying depth estimation networks in the real world requires high-level robustness against various adverse conditions to ensure safe and reliable autonomy.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
