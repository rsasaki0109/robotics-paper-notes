# Chameleon: Fast-Slow Neuro-Symbolic Lane Topology Extraction

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 1 |
| arXiv | [http://arxiv.org/abs/2503.07485](http://arxiv.org/abs/2503.07485) |
| Authors | Zhang, Zongzheng;Li, Xinrun;Zou, Sizhe;Chi, Guoxuan;Li, Siqi;Qiu, Xuchong;Wang, Guoliang;Zheng, Guantian;Wang, LeiChen;Zhao, Hang;Zhao, Hao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Lane topology extraction involves detecting lanes and traffic elements and determining their relationships, a key perception task for mapless autonomous driving.
- This task requires complex reasoning, such as determining whether it is possible to turn left into a specific lane.
- To address this challenge, we introduce neuro-symbolic methods powered by visionlanguage foundation models (VLMs).

## Task

* Perception
* Software Tools

## Keywords

* Cognitive Modeling
* Object Detection
* Segmentation and Categorization

## AI依存度

* AI-heavy

## 何を解決？

* Lane topology extraction involves detecting lanes and traffic elements and determining their relationships, a key perception task for mapless autonomous driving.

## 何が新しい？

* To this end, we propose a fast-slow neuro-symbolic lane topology extraction algorithm, named Chameleon, which alternates between a fast system that directly reasons over detected instances using synthesized programs and a slow system that utilizes a VLM with a chainof-thought design to handle corner cases.

## どうやってる？

* To address this challenge, we introduce neuro-symbolic methods powered by visionlanguage foundation models (VLMs).

## どこが強い？

* We evaluate the method on the OpenLane-v2 dataset, showing consistent improvements across various baseline detectors.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we propose a fast-slow neuro-symbolic lane topology extraction algorithm, named Chameleon, which alternates between a fast system that directly reasons over detected instances using synthesized programs and a slow system that utilizes a VLM with a chainof-thought design to handle corner cases.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
