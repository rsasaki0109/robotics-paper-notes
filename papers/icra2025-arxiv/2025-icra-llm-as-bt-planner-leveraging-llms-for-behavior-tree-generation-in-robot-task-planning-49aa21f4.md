# LLM-As-BT-Planner: Leveraging LLMs for Behavior Tree Generation in Robot Task Planning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning Based Planning for Manipulation 1 |
| arXiv | [http://arxiv.org/abs/2409.10444](http://arxiv.org/abs/2409.10444) |
| Authors | Ao, Jicong;Wu, Fan;Wu, Yansong;Swikir, Abdalla;Haddadin, Sami |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robotic assembly tasks remain an open challenge due to their long horizon nature and complex part relations.
- Behavior trees (BTs) are increasingly used in robot task planning for their modularity and flexibility, but creating them manually can be effort-intensive.
- Large language models (LLMs) have recently been applied to robotic task planning for generating action sequences, yet their ability to generate BTs has not been fully investigated.

## Task

* Visual-Inertial
* Motion Planning

## Keywords

* Behavior-Based Systems
* AI-Enabled Robotics
* Assembly

## AI依存度

* AI-heavy

## 何を解決？

* Robotic assembly tasks remain an open challenge due to their long horizon nature and complex part relations.

## 何が新しい？

* To this end, we propose LLM-as-BT-Planner, a novel framework that leverages LLMs for BT generation in robotic assembly task planning.

## どうやってる？

* Four in-context learning methods are introduced to utilize the natural language processing and inference capabilities of LLMs for producing task plans in BT format, reducing manual effort while ensuring robustness and comprehensibility.

## どこが強い？

* Experiments in both simulated and real-world settings demonstrate that our framework enhances LLMs' ability to generate BTs, improving success rate through in-context learning and supervised fine-tuning.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we propose LLM-as-BT-Planner, a novel framework that leverages LLMs for BT generation in robotic assembly task planning.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
