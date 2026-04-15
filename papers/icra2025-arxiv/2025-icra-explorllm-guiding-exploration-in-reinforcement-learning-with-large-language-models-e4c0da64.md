# ExploRLLM: Guiding Exploration in Reinforcement Learning with Large Language Models

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Foundation Models for Manipulation |
| arXiv | [http://arxiv.org/abs/2403.09583](http://arxiv.org/abs/2403.09583) |
| Authors | Ma, Runyu;Luijkx, Jelle Douwe;Ajanovic, Zlatan;Kober, Jens |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In robot manipulation, Reinforcement Learning (RL) often suffers from low sample efficiency and uncertain convergence, especially in large observation and action spaces.
- Foundation Models (FMs) offer an alternative, demonstrating promise in zero-shot and few-shot settings.
- However, they can be unreliable due to limited physical and spatial understanding.

## Task

* Manipulation

## Keywords

* AI-Based Methods
* Reinforcement Learning

## AI依存度

* AI-heavy

## 何を解決？

* In robot manipulation, Reinforcement Learning (RL) often suffers from low sample efficiency and uncertain convergence, especially in large observation and action spaces.

## 何が新しい？

* In our approach, FMs improve RL convergence by generating policy code and efficient representations, while a residual RL agent compensates for the FMs' limited physical understanding.

## どうやってる？

* We introduce ExploRLLM, a method that combines the strengths of both paradigms.

## どこが強い？

* Additionally, real-world experiments show that the policies exhibit promising zero-shot sim-to-real transfer.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In our approach, FMs improve RL convergence by generating policy code and efficient representations, while a residual RL agent compensates for the FMs' limited physical understanding.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
