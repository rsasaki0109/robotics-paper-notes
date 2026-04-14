# Bimanual Grasp Synthesis for Dexterous Robot Hands

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Bimanual Manipulation 1 |
| arXiv | [http://arxiv.org/abs/2411.15903](http://arxiv.org/abs/2411.15903) |
| Authors | Shao, Yanming, Xiao, Chenxi |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Humans naturally perform bimanual skills to handle large and heavy objects.
- To bridge this gap, we propose the BimanGrasp algorithm for synthesizing bimanual grasps on 3D objects.
- This model achieved a grasp synthesis success rate of 69.87% and significant acceleration in computational speed compared to BimanGrasp algorithm.

## Task

* Sensor Fusion
* Manipulation

## Keywords

* Bimanual Manipulation / Grasping / Dexterous Manipulation

## AI依存度

* AI-heavy

## 何を解決？

* Humans naturally perform bimanual skills to handle large and heavy objects.

## 何が新しい？

* To bridge this gap, we propose the BimanGrasp algorithm for synthesizing bimanual grasps on 3D objects.

## どうやってる？

* The BimanGrasp algorithm generates grasp poses by optimizing an energy function that considers grasp stability and feasibility.

## どこが強い？

* Furthermore, the quality of the synthesized grasps is verified using the Isaac Gym physics simulation engine.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* This model achieved a grasp synthesis success rate of 69.87% and significant acceleration in computational speed compared to BimanGrasp algorithm.

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
