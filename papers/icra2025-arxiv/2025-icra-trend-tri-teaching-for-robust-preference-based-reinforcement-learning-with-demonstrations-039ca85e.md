# TREND: Tri-Teaching for Robust Preference-Based Reinforcement Learning with Demonstrations

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Deep Learning for Visual Perception 2 |
| arXiv | [http://arxiv.org/abs/2505.06079](http://arxiv.org/abs/2505.06079) |
| Authors | Huang, Shuaiyi;Levy, Mara;Gupta, Anubhav;Ekpo, Daniel;Zheng, Ruijie;Shrivastava, Abhinav |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Preference feedback collected by human or VLM annotators is often noisy, presenting a significant challenge for preference-based reinforcement learning that relies on accurate preference labels.
- To address this challenge, we propose TREND, a novel framework that integrates few-shot expert demonstrations with a tri-teaching strategy for effective noise mitigation.
- Our method trains three reward models simultaneously, where each model views its small-loss preference pairs as useful knowledge and teaches such useful pairs to its peer network for updating the parameters.

## Task

* Visual-Inertial
* Manipulation
* Perception

## Keywords

* Deep Learning for Visual Perception
* Deep Learning Methods

## AI依存度

* AI-heavy

## 何を解決？

* Preference feedback collected by human or VLM annotators is often noisy, presenting a significant challenge for preference-based reinforcement learning that relies on accurate preference labels.

## 何が新しい？

* To address this challenge, we propose TREND, a novel framework that integrates few-shot expert demonstrations with a tri-teaching strategy for effective noise mitigation.

## どうやってる？

* Our method trains three reward models simultaneously, where each model views its small-loss preference pairs as useful knowledge and teaches such useful pairs to its peer network for updating the parameters.

## どこが強い？

* We evaluate TREND on various robotic manipulation tasks, achieving up to 90% success rates even with noise levels as high as 40%, highlighting its effective robustness in handling noisy preference feedback.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this challenge, we propose TREND, a novel framework that integrates few-shot expert demonstrations with a tri-teaching strategy for effective noise mitigation.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
