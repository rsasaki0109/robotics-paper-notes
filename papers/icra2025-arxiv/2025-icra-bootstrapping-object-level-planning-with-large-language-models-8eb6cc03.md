# Bootstrapping Object-Level Planning with Large Language Models

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Task and Motion Planning 4 |
| arXiv | [http://arxiv.org/abs/2409.12262](http://arxiv.org/abs/2409.12262) |
| Authors | Paulius, David;Agostini, Alejandro;Quartey, Benedict;Konidaris, George |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We introduce a new method that extracts knowledge from a large language model (LLM) to produce object-level plans, which describe high-level changes to object state, and uses them to bootstrap task and motion planning (TAMP).
- Existing work uses LLMs to directly output task plans or generate goals in representations like PDDL.
- However, these methods fall short because they rely on the LLM to do the actual planning or output a hard-to-satisfy goal.

## Task

* Visual-Inertial
* Motion Planning
* Manipulation

## Keywords

* Task and Motion Planning
* AI-Based Methods
* Task Planning

## AI依存度

* AI-heavy

## 何を解決？

* We introduce a new method that extracts knowledge from a large language model (LLM) to produce object-level plans, which describe high-level changes to object state, and uses them to bootstrap task and motion planning (TAMP).

## 何が新しい？

* Existing work uses LLMs to directly output task plans or generate goals in representations like PDDL.

## どうやってる？

* We introduce a new method that extracts knowledge from a large language model (LLM) to produce object-level plans, which describe high-level changes to object state, and uses them to bootstrap task and motion planning (TAMP).

## どこが強い？

* Our method markedly outperforms alternative planning strategies in completing several pick-and-place tasks in simulation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Existing work uses LLMs to directly output task plans or generate goals in representations like PDDL.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
