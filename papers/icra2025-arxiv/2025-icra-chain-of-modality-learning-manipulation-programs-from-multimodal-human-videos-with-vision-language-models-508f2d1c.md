# Chain-Of-Modality: Learning Manipulation Programs from Multimodal Human Videos with Vision-Language-Models

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Representation Learning 2 |
| arXiv | [http://arxiv.org/abs/2504.13351](http://arxiv.org/abs/2504.13351) |
| Authors | Wang, Chen;Xia, Fei;Yu, Wenhao;Zhang, Tingnan;Zhang, Ruohan;Liu, Karen;Fei-Fei, Li;Tan, Jie;Liang, Jacky |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Learning to perform manipulation tasks from human videos is a promising approach for teaching robots.
- However, many manipulation tasks require changing control parameters during task execution, such as force, which visual data alone cannot capture.
- In this work, we leverage sensing devices such as armbands that measure human muscle activities and microphones that record sound, to capture the details in the human manipulation process, and enable robots to extract task plans and control parameters to perform the same task.

## Task

* Control
* Manipulation

## Keywords

* Machine Learning for Robot Control
* Embodied Cognitive Science
* AI-Enabled Robotics

## AI依存度

* AI-heavy

## 何を解決？

* Learning to perform manipulation tasks from human videos is a promising approach for teaching robots.

## 何が新しい？

* To achieve this, we introduce Chain-of-Modality (CoM), a prompting strategy that enables Vision Language Models to reason about multimodal human demonstration data --- videos coupled with muscle or audio signals.

## どうやってる？

* Learning to perform manipulation tasks from human videos is a promising approach for teaching robots.

## どこが強い？

* Our experiments show that CoM delivers a threefold improvement in accuracy for extracting task plans and control parameters compared to baselines, with strong generalization to new task setups and objects in real-world robot experiments.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To achieve this, we introduce Chain-of-Modality (CoM), a prompting strategy that enables Vision Language Models to reason about multimodal human demonstration data --- videos coupled with muscle or audio signals.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
