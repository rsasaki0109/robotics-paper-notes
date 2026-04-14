# WcDT: World-Centric Diffusion Transformer for Traffic Scene Generation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Exploration |
| arXiv | [http://arxiv.org/abs/2404.02082](http://arxiv.org/abs/2404.02082) |
| Authors | Yang, Chen, He, Yangfan, Tian, Aaron Xuxiang, Chen, Dong, Wang, Jianhui, Shi, Tianyu, Heydarian, Arsalan, Liu, Pei |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we introduce a novel approach for autonomous driving trajectory generation by harnessing the complementary strengths of diffusion probabilistic models (a.k.a., diffusion models) and transformers.
- Our proposed framework, termed the "World-centric Diffusion Transformer"(WcDT), optimizes the entire trajectory generation process, from feature extraction to model inference.
- Comprehensive experimental results show that the proposed approach exhibits superior performance in generating both realistic and diverse trajectories, showing its potential for integration into automatic driving simulation systems.

## Task

* Sensor Fusion
* Motion Planning
* Intelligent Vehicles

## Keywords

* Path Planning for Multiple Mobile Robots or Agents / Planning under Uncertainty / Deep Learning Methods

## AI依存度

* AI-heavy

## 何を解決？

* In this paper, we introduce a novel approach for autonomous driving trajectory generation by harnessing the complementary strengths of diffusion probabilistic models (a.k.a., diffusion models) and transformers.

## 何が新しい？

* In this paper, we introduce a novel approach for autonomous driving trajectory generation by harnessing the complementary strengths of diffusion probabilistic models (a.k.a., diffusion models) and transformers.

## どうやってる？

* Our proposed framework, termed the "World-centric Diffusion Transformer"(WcDT), optimizes the entire trajectory generation process, from feature extraction to model inference.

## どこが強い？

* Comprehensive experimental results show that the proposed approach exhibits superior performance in generating both realistic and diverse trajectories, showing its potential for integration into automatic driving simulation systems.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: perception / localization fusion, planning, planning / control / perception
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
