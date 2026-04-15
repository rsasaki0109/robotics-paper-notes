# BoxMap: Efficient Structural Mapping and Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Vision-Based Navigation 2 |
| arXiv | [http://arxiv.org/abs/2410.06263](http://arxiv.org/abs/2410.06263) |
| Authors | Wang, Zili;Allum, Christopher;Andersson, Sean;Tron, Roberto |
| Source | ICRA 2025 / arXiv |

## TL;DR

- While humans can successfully navigate using abstractions, ignoring details that are irrelevant to the task at hand, most of the existing approaches in robotics require detailed environment representations which consume a significant amount of sensing, computing, and storage; these issues become particularly important in resource-constrained settings with limited power budgets.
- Deep learning methods can learn from prior experience to abstract knowledge from novel environments, and use it to more efficiently execute tasks such as frontier exploration, object search, or scene understanding.
- We propose BoxMap, a Detection-Transformer-based architecture that takes advantage of the structure of the sensed partial environment to update a topological graph of the environment as a set of semantic entities (rooms and doors) and their relations (connectivity).

## Task

* Motion Planning
* Perception

## Keywords

* Deep Learning Methods
* Autonomous Agents
* Task and Motion Planning

## AI依存度

* AI-heavy

## 何を解決？

* While humans can successfully navigate using abstractions, ignoring details that are irrelevant to the task at hand, most of the existing approaches in robotics require detailed environment representations which consume a significant amount of sensing, computing, and storage; these issues become particularly important in resource-constrained settings with limited power budgets.

## 何が新しい？

* We propose BoxMap, a Detection-Transformer-based architecture that takes advantage of the structure of the sensed partial environment to update a topological graph of the environment as a set of semantic entities (rooms and doors) and their relations (connectivity).

## どうやってる？

* Deep learning methods can learn from prior experience to abstract knowledge from novel environments, and use it to more efficiently execute tasks such as frontier exploration, object search, or scene understanding.

## どこが強い？

* Moreover, our high-level topological representation results in 30.9% shorter trajectories in the exploration task with respect to a standard method.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose BoxMap, a Detection-Transformer-based architecture that takes advantage of the structure of the sensed partial environment to update a topological graph of the environment as a set of semantic entities (rooms and doors) and their relations (connectivity).

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
