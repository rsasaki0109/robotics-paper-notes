# Discovering Object Attributes by Prompting Large Language Models with Perception-Action APIs

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Foundation Models for Manipulation |
| arXiv | [http://arxiv.org/abs/2409.15505](http://arxiv.org/abs/2409.15505) |
| Authors | Mavrogiannis, Angelos;Yuan, Dehao;Aloimonos, Yiannis |
| Source | ICRA 2025 / arXiv |

## TL;DR

- There has been a lot of interest in grounding natural language to physical entities through visual context.
- While Vision Language Models (VLMs) can ground linguistic instructions to visual sensory information, they struggle with grounding non-visual attributes, like the weight of an object.
- Our key insight is that non-visual attribute detection can be effectively achieved by active perception guided by visual reasoning.

## Task

* Control
* Perception
* Software Tools

## Keywords

* AI-Based Methods
* Computer Architecture for Robotic and Automation
* Software
* Middleware and Programming Environments

## AI依存度

* AI-heavy

## 何を解決？

* There has been a lot of interest in grounding natural language to physical entities through visual context.

## 何が新しい？

* To this end, we present a perception-action API that consists of VLMs and Large Language Models (LLMs) as backbones, together with a set of robot control functions.

## どうやってる？

* Online testing in realistic household scenes on AI2-THOR and a real robot demonstration on a DJI RoboMaster EP robot highlight the efficacy of our approach.

## どこが強い？

* Offline testing on the Odd-One-Out dataset demonstrates that our framework outperforms vanilla VLMs in detecting attributes like relative object location, size, and weight.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we present a perception-action API that consists of VLMs and Large Language Models (LLMs) as backbones, together with a set of robot control functions.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
