# Robust Planning for Autonomous Driving Via Mixed Adversarial Diffusion Predictions

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning and Control |
| arXiv | [http://arxiv.org/abs/2505.12327](http://arxiv.org/abs/2505.12327) |
| Authors | Zhao, Albert;Soatto, Stefano |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We describe a robust planning method for autonomous driving that mixes normal and adversarial agent predictions output by a diffusion model trained for motion prediction.
- We first train a diffusion model to learn an unbiased distribution of normal agent behaviors.
- We then generate a distribution of adversarial predictions by biasing the diffusion model at test time to generate predictions that are likely to collide with a candidate plan.

## Task

* Motion Planning
* Legged Robotics

## Keywords

* Planning under Uncertainty
* Robot Safety
* Autonomous Vehicle Navigation

## AI依存度

* AI-heavy

## 何を解決？

* We describe a robust planning method for autonomous driving that mixes normal and adversarial agent predictions output by a diffusion model trained for motion prediction.

## 何が新しい？

* We show the effectiveness of our method on single-agent and multi-agent jaywalking scenarios as well as a red light violation scenario.

## どうやってる？

* We describe a robust planning method for autonomous driving that mixes normal and adversarial agent predictions output by a diffusion model trained for motion prediction.

## どこが強い？

* We show the effectiveness of our method on single-agent and multi-agent jaywalking scenarios as well as a red light violation scenario.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We show the effectiveness of our method on single-agent and multi-agent jaywalking scenarios as well as a red light violation scenario.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
