# Inference-Time Policy Steering through Human Interactions

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Diffusion for Manipulation |
| arXiv | [http://arxiv.org/abs/2411.16627](http://arxiv.org/abs/2411.16627) |
| Authors | Wang, Yanwei;Wang, Lirui;Du, Yilun;Sundaralingam, Balakumar;Yang, Xuning;Chao, Yu-Wei;Pérez-D'Arpino, Claudia;Fox, Dieter;Shah, Julie A. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Generative policies trained with human demonstrations can autonomously accomplish multimodal, long-horizon tasks.
- However, during inference, humans are often removed from the policy execution loop, limiting the ability to guide a pre-trained policy towards a specific sub-goal or trajectory shape among multiple predictions.
- Naive human intervention may inadvertently exacerbate distribution shift, leading to constraint violations or execution failures.

## Task

* Visual-Inertial
* Motion Planning
* Human-Robot Interaction
* Software Tools

## Keywords

* Imitation Learning
* Human-Robot Collaboration
* Deep Learning Methods

## AI依存度

* AI-heavy

## 何を解決？

* Generative policies trained with human demonstrations can autonomously accomplish multimodal, long-horizon tasks.

## 何が新しい？

* To better align policy output with human intent without inducing out-of-distribution errors, we propose an Inference-Time Policy Steering (ITPS) framework that leverages human interactions to bias the generative sampling process, rather than fine-tuning the policy on interaction data.

## どうやってる？

* To better align policy output with human intent without inducing out-of-distribution errors, we propose an Inference-Time Policy Steering (ITPS) framework that leverages human interactions to bias the generative sampling process, rather than fine-tuning the policy on interaction data.

## どこが強い？

* We evaluate ITPS across three simulated and real-world benchmarks, testing three forms of human interaction and associated alignment distance metrics.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To better align policy output with human intent without inducing out-of-distribution errors, we propose an Inference-Time Policy Steering (ITPS) framework that leverages human interactions to bias the generative sampling process, rather than fine-tuning the policy on interaction data.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
