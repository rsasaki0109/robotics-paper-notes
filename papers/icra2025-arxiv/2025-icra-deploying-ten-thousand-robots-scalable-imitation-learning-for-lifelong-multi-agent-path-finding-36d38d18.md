# Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Path Planning 3 |
| arXiv | [http://arxiv.org/abs/2410.21415](http://arxiv.org/abs/2410.21415) |
| Authors | Jiang, He;Wang, Yutong;Veerapaneni, Rishi;Duhan, Tanishq Harish;Sartoretti, Guillaume Adrien;Li, Jiaoyang |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Lifelong Multi-Agent Path Finding (LMAPF) repeatedly finds collision-free paths for multiple agents that are continually assigned new goals when they reach current ones.
- Recently, this field has embraced learning-based methods, which reactively generate single-step actions based on individual local observations.
- However, it is still challenging for them to match the performance of the best search-based algorithms, especially in large-scale settings.

## Task

* Motion Planning

## Keywords

* Path Planning for Multiple Mobile Robots or Agents
* Imitation Learning
* Integrated Planning and Learning

## AI依存度

* AI-heavy

## 何を解決？

* Lifelong Multi-Agent Path Finding (LMAPF) repeatedly finds collision-free paths for multiple agents that are continually assigned new goals when they reach current ones.

## 何が新しい？

* This work proposes an imitation-learning-based LMAPF solver that introduces a novel communication module as well as systematic single-step collision resolution and global guidance techniques.

## どうやってる？

* Recently, this field has embraced learning-based methods, which reactively generate single-step actions based on individual local observations.

## どこが強い？

* Lifelong Multi-Agent Path Finding (LMAPF) repeatedly finds collision-free paths for multiple agents that are continually assigned new goals when they reach current ones.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This work proposes an imitation-learning-based LMAPF solver that introduces a novel communication module as well as systematic single-step collision resolution and global guidance techniques.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
