# Fast LiDAR Data Generation with Rectified Flows

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception 3 |
| arXiv | [http://arxiv.org/abs/2412.02241](http://arxiv.org/abs/2412.02241) |
| Authors | Nakashima, Kazuto;Liu, Xiaowen;Miyawaki, Tomoya;Iwashita, Yumi;Kurazume, Ryo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Building LiDAR generative models holds promise as powerful data priors for restoration, scene manipulation, and scalable simulation in autonomous mobile robots.
- In recent years, approaches using diffusion models have emerged, significantly improving training stability and generation quality.
- Despite their success, diffusion models require numerous iterations of running neural networks to generate high-quality samples, making the increasing computational cost a potential barrier for robotics applications.

## Task

* LiDAR
* Visual-Inertial
* Manipulation
* Perception

## Keywords

* Deep Learning for Visual Perception
* Computer Vision for Transportation
* Representation Learning

## AI依存度

* AI-heavy

## 何を解決？

* Building LiDAR generative models holds promise as powerful data priors for restoration, scene manipulation, and scalable simulation in autonomous mobile robots.

## 何が新しい？

* We also propose an efficient Transformer-based model architecture for processing the image representation of LiDAR range and reflectance measurements.

## どうやってる？

* Our method is based on rectified flows that learn straight trajectories, simulating data generation with significantly fewer sampling steps compared to diffusion models.

## どこが強い？

* Our experiments on unconditional LiDAR data generation using the KITTI-360 dataset demonstrate the effectiveness of our approach in terms of both efficiency and quality.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We also propose an efficient Transformer-based model architecture for processing the image representation of LiDAR range and reflectance measurements.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
