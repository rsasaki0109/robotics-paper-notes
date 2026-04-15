# Improving Vision-Language-Action Model with Online Reinforcement Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Imitation Learning 3 |
| arXiv | [http://arxiv.org/abs/2501.16664](http://arxiv.org/abs/2501.16664) |
| Authors | Guo, Yanjiang;Zhang, Jianke;Chen, Xiaoyu;Ji, Xiang;Wang, Yen-Jen;Hu, Yucheng;Chen, Jianyu |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models.
- Although the VLA models are powerful, how to improve these large models during interaction with environments remains an open question.
- In this paper, we explore how to further improve these VLA models via Reinforcement Learning (RL), a commonly used fine-tuning technique for large models.

## Task

* Visual-Inertial
* Control
* Manipulation
* Software Tools

## Keywords

* Imitation Learning
* Continual Learning
* Reinforcement Learning

## AI依存度

* AI-heavy

## 何を解決？

* Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models.

## 何が新しい？

* To address these problems, we propose iRe-VLA framework, which iterates between Reinforcement Learning and supervised learning to effectively improve VLA models, leveraging the exploratory benefits of RL while maintaining the stability of supervised learning.

## どうやってる？

* Experiments in two simulated benchmarks and a real-world manipulation suite validate the effectiveness of our method.

## どこが強い？

* Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these problems, we propose iRe-VLA framework, which iterates between Reinforcement Learning and supervised learning to effectively improve VLA models, leveraging the exploratory benefits of RL while maintaining the stability of supervised learning.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
