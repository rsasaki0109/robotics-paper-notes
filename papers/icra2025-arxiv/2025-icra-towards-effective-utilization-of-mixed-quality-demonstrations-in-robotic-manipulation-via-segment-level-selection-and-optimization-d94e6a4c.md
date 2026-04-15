# Towards Effective Utilization of Mixed-Quality Demonstrations in Robotic Manipulation Via Segment-Level Selection and Optimization

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Imitation Learning for Manipulation 2 |
| arXiv | [http://arxiv.org/abs/2409.19917](http://arxiv.org/abs/2409.19917) |
| Authors | Chen, Jingjing;Fang, Hongjie;Fang, Hao-Shu;Lu, Cewu |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Data is crucial for robotic manipulation, as it underpins the development of robotic systems for complex tasks.
- While high-quality, diverse datasets enhance the performance and adaptability of robotic manipulation policies, collecting extensive expert-level data is resource-intensive.
- Consequently, many current datasets suffer from quality inconsistencies due to operator variability, highlighting the need for methods to utilize mixed-quality data effectively.

## Task

* Visual-Inertial
* Motion Planning
* Manipulation
* Perception

## Keywords

* Learning from Demonstration
* Imitation Learning
* Deep Learning in Grasping and Manipulation

## AI依存度

* Hybrid

## 何を解決？

* Data is crucial for robotic manipulation, as it underpins the development of robotic systems for complex tasks.

## 何が新しい？

* To mitigate these issues, we propose "Select Segments to Imitate" (S2I), a framework that selects and optimizes mixed-quality demonstration data at the segment level, while ensuring plug-and-play compatibility with existing robotic manipulation policies.

## どうやってる？

* Consequently, many current datasets suffer from quality inconsistencies due to operator variability, highlighting the need for methods to utilize mixed-quality data effectively.

## どこが強い？

* We evaluate S2I through comprehensive experiments in simulation and real-world environments across six tasks, demonstrating that with only 3 expert demonstrations for reference, S2I can improve the performance of various downstream policies when trained with mixed-quality demonstrations.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To mitigate these issues, we propose "Select Segments to Imitate" (S2I), a framework that selects and optimizes mixed-quality demonstration data at the segment level, while ensuring plug-and-play compatibility with existing robotic manipulation policies.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
