# A Parameter-Efficient Tuning Framework for Language-Guided Object Grounding and Robot Grasping

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning for Manipulation |
| arXiv | [http://arxiv.org/abs/2409.19457](http://arxiv.org/abs/2409.19457) |
| Authors | Yu, Houjian;Li, Mingen;Rezazadeh, Alireza;Yang, Yang;Choi, Changhyun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The language-guided robot grasping task requires a robot agent to integrate multimodal information from both visual and linguistic inputs to predict actions for target-driven grasping.
- While recent approaches utilizing Multimodal Large Language Models (MLLMs) have shown promising results, their extensive computation and data demands limit the feasibility of local deployment and customization.
- To address this, we propose a novel CLIP-based multimodal parameter-efficient tuning (PET) framework designed for three language-guided object grounding and grasping tasks: (1) Referring Expression Segmentation (RES), (2) Referring Grasp Synthesis (RGS), and (3) Referring Grasp Affordance (RGA).

## Task

* Manipulation
* Perception

## Keywords

* Perception for Grasping and Manipulation
* Semantic Scene Understanding
* Deep Learning in Grasping and Manipulation

## AI依存度

* AI-heavy

## 何を解決？

* The language-guided robot grasping task requires a robot agent to integrate multimodal information from both visual and linguistic inputs to predict actions for target-driven grasping.

## 何が新しい？

* To address this, we propose a novel CLIP-based multimodal parameter-efficient tuning (PET) framework designed for three language-guided object grounding and grasping tasks: (1) Referring Expression Segmentation (RES), (2) Referring Grasp Synthesis (RGS), and (3) Referring Grasp Affordance (RGA).

## どうやってる？

* While recent approaches utilizing Multimodal Large Language Models (MLLMs) have shown promising results, their extensive computation and data demands limit the feasibility of local deployment and customization.

## どこが強い？

* Experiment results demonstrate superior performance in the RES object grounding task compared with existing CLIP-based full-model tuning or PET approaches.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this, we propose a novel CLIP-based multimodal parameter-efficient tuning (PET) framework designed for three language-guided object grounding and grasping tasks: (1) Referring Expression Segmentation (RES), (2) Referring Grasp Synthesis (RGS), and (3) Referring Grasp Affordance (RGA).

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
