# Adaptive Distance Functions Via Kelvin Transformation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 3 |
| arXiv | [http://arxiv.org/abs/2406.03200](http://arxiv.org/abs/2406.03200) |
| Authors | Cabral Muchacho, Rafael Ignacio;Pokorny, Florian T. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The term safety in robotics is often understood as a synonym for avoidance.
- Although this perspective has led to progress in path planning and reactive control, a generalization of this perspective is necessary to include task semantics relevant to contact-rich manipulation tasks, especially during teleoperation and to ensure the safety of learned policies.
- We introduce the semantics-aware distance function and a corresponding computational method based on the Kelvin Transformation.

## Task

* Motion Planning
* Control
* Manipulation
* Human-Robot Interaction

## Keywords

* Computational Geometry
* Robot Safety

## AI依存度

* Hybrid

## 何を解決？

* The term safety in robotics is often understood as a synonym for avoidance.

## 何が新しい？

* The semantics-aware distance generalizes signed distance functions by allowing the zero level set to lie inside of the object in regions where contact is allowed, effectively incorporating task semantics, such as object affordances, in an adaptive implicit representation of safe sets.

## どうやってる？

* We introduce the semantics-aware distance function and a corresponding computational method based on the Kelvin Transformation.

## どこが強い？

* In numerical experiments we show the computational viability of our method for real applications and visualize the computed function on a wrench with various semantic regions.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* The semantics-aware distance generalizes signed distance functions by allowing the zero level set to lie inside of the object in regions where contact is allowed, effectively incorporating task semantics, such as object affordances, in an adaptive implicit representation of safe sets.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
