# Local Policies Enable Zero-Shot Long-Horizon Manipulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Big Data |
| arXiv | [http://arxiv.org/abs/2410.22332](http://arxiv.org/abs/2410.22332) |
| Authors | Dalal, Murtaza;Liu, Min;Talbott, Walter;Chen, Chen;Pathak, Deepak;Zhang, Jian;Salakhutdinov, Ruslan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Sim2real for robotic manipulation is difficult due to the challenges of simulating complex contacts and generating realistic task distributions.
- To tackle the latter problem, we introduce ManipGen, which leverages a new class of policies for sim2real transfer: local policies.
- Locality enables a variety of appealing properties including invariances to absolute robot and object pose, skill ordering, and global scene configuration.

## Task

* Visual-Inertial
* Motion Planning
* Control
* Manipulation

## Keywords

* Big Data in Robotics and Automation
* Machine Learning for Robot Control
* Deep Learning Methods

## AI依存度

* AI-heavy

## 何を解決？

* Sim2real for robotic manipulation is difficult due to the challenges of simulating complex contacts and generating realistic task distributions.

## 何が新しい？

* To tackle the latter problem, we introduce ManipGen, which leverages a new class of policies for sim2real transfer: local policies.

## どうやってる？

* We combine these policies with foundation models for vision, language and motion planning and demonstrate SOTA zero-shot performance of our method to Robosuite benchmark tasks in simulation (97%).

## どこが強い？

* We combine these policies with foundation models for vision, language and motion planning and demonstrate SOTA zero-shot performance of our method to Robosuite benchmark tasks in simulation (97%).

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To tackle the latter problem, we introduce ManipGen, which leverages a new class of policies for sim2real transfer: local policies.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
