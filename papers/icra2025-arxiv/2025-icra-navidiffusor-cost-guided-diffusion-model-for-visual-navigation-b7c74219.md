# NaviDiffusor: Cost-Guided Diffusion Model for Visual Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Diffusion Models |
| arXiv | [http://arxiv.org/abs/2504.10003](http://arxiv.org/abs/2504.10003) |
| Authors | Zeng, Yiming;Ren, Hao;Wang, Shuhang;Huang, Junlong;Cheng, Hui |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Visual navigation, a fundamental challenge in mobile robotics, demands versatile policies to handle diverse environments.
- Classical methods leverage geometric solutions to minimize specific costs, offering adaptability to new scenarios but are prone to system errors due to their multi-modular design and reliance on hand-crafted rules.
- Learning-based methods, while achieving high planning success rates, face difficulties in generalizing to unseen environments beyond the training data and often require extensive training.

## Task

* Visual-Inertial

## Keywords

* Vision-Based Navigation
* Integrated Planning and Learning
* Imitation Learning

## AI依存度

* AI-heavy

## 何を解決？

* Visual navigation, a fundamental challenge in mobile robotics, demands versatile policies to handle diverse environments.

## 何が新しい？

* To address these limitations, we propose a hybrid approach that combines the strengths of learning-based methods and classical approaches for RGB-only visual navigation.

## どうやってる？

* Classical methods leverage geometric solutions to minimize specific costs, offering adaptability to new scenarios but are prone to system errors due to their multi-modular design and reliance on hand-crafted rules.

## どこが強い？

* Extensive experiments in both indoor and outdoor settings, across simulated and real-world scenarios, demonstrate zero-shot transfer capability of our approach, achieving higher success rates and fewer collisions compared to baseline methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these limitations, we propose a hybrid approach that combines the strengths of learning-based methods and classical approaches for RGB-only visual navigation.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
