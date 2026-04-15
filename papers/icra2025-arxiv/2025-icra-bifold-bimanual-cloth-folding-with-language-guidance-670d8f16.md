# BiFold: Bimanual Cloth Folding with Language Guidance

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Bimanual Manipulation 1 |
| arXiv | [http://arxiv.org/abs/2501.16458](http://arxiv.org/abs/2501.16458) |
| Authors | Barbany, Oriol;Colomé, Adrià;Torras, Carme |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Cloth folding is a complex task due to the inevitable self-occlusions of clothes, their complicated dynamics, and the disparate materials, geometries, and textures that garments can have.
- In this work, we learn folding actions conditioned on text commands.
- Translating high-level, abstract instructions into precise robotic actions requires sophisticated language understanding and manipulation capabilities.

## Task

* Manipulation
* Perception
* Software Tools

## Keywords

* Perception for Grasping and Manipulation
* Deep Learning in Grasping and Manipulation
* Data Sets for Robot Learning

## AI依存度

* AI-heavy

## 何を解決？

* Cloth folding is a complex task due to the inevitable self-occlusions of clothes, their complicated dynamics, and the disparate materials, geometries, and textures that garments can have.

## 何が新しい？

* To address the lack of annotated bimanual folding data, we introduce a novel dataset with automatically parsed actions and language-aligned instructions, enabling better learning of text-conditioned manipulation.

## どうやってる？

* To do that, we leverage a pre-trained vision-language model and repurpose it to predict manipulation actions.

## どこが強い？

* BiFold attains the best performance on our dataset and demonstrates strong generalization to new instructions, garments, and environments.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address the lack of annotated bimanual folding data, we introduce a novel dataset with automatically parsed actions and language-aligned instructions, enabling better learning of text-conditioned manipulation.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
