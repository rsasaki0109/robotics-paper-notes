# Generalizable Imitation Learning through Pre-Trained Representations

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Robot Foundation Models 1 |
| arXiv | [http://arxiv.org/abs/2311.09350](http://arxiv.org/abs/2311.09350) |
| Authors | Chang, Wei-Di;Hogan, Francois;Fujimoto, Scott;Meger, David Paul;Dudek, Gregory |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we leverage self-supervised vision transformer models and their emergent semantic abilities to improve the generalization abilities of imitation learning policies.
- We introduce DVK, an imitation learning algorithm that leverages rich pre-trained Visual Transformer patch-level embeddings to obtain better generalization when learning through demonstrations.
- Our learner sees the world by clustering appearance features into groups associated with semantic concepts, forming stable keypoints that generalize across a wide range of appearance variations and object types.

## Task

* Manipulation
* Software Tools

## Keywords

* Imitation Learning
* Learning from Demonstration
* Representation Learning

## AI依存度

* AI-heavy

## 何を解決？

* In this paper, we leverage self-supervised vision transformer models and their emergent semantic abilities to improve the generalization abilities of imitation learning policies.

## 何が新しい？

* We demonstrate how this representation enables generalized behaviour by evaluating imitation learning across a diverse dataset of object manipulation tasks.

## どうやってる？

* To facilitate further study of generalization in Imitation Learning, all of our code for the method and evaluation, as well as the dataset, is made available.

## どこが強い？

* We demonstrate how this representation enables generalized behaviour by evaluating imitation learning across a diverse dataset of object manipulation tasks.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We demonstrate how this representation enables generalized behaviour by evaluating imitation learning across a diverse dataset of object manipulation tasks.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
