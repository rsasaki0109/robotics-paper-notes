# In-Context Learning Enables Robot Action Prediction in LLMs

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Foundation Models for Manipulation |
| arXiv | [http://arxiv.org/abs/2410.12782](http://arxiv.org/abs/2410.12782) |
| Authors | Yin, Yida;Wang, Zekai;Sharma, Yuvan;Niu, Dantong;Darrell, Trevor;Herzig, Roei |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recently, Large Language Models (LLMs) have achieved remarkable success using in-context learning (ICL) in the language domain.
- However, leveraging the ICL capabilities within off-the-shelf LLMs to directly predict robot actions remains largely unexplored.
- In this paper, we introduce RobotPrompt, a framework that enables off-the-shelf text-only LLMs to directly predict robot actions through ICL without training.

## Task

* Visual-Inertial

## Keywords

* Deep Learning Methods
* Learning from Demonstration

## AI依存度

* AI-heavy

## 何を解決？

* Recently, Large Language Models (LLMs) have achieved remarkable success using in-context learning (ICL) in the language domain.

## 何が新しい？

* In this paper, we introduce RobotPrompt, a framework that enables off-the-shelf text-only LLMs to directly predict robot actions through ICL without training.

## どうやってる？

* Our approach first heuristically identifies keyframes that capture important moments from an episode.

## どこが強い？

* Through extensive experiments and analysis, RobotPrompt shows stronger performance over zero-shot and ICL baselines in simulated and real-world settings.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we introduce RobotPrompt, a framework that enables off-the-shelf text-only LLMs to directly predict robot actions through ICL without training.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
