# Pushing through Clutter with Movability Awareness of Blocking Obstacles

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 1 |
| arXiv | [http://arxiv.org/abs/2502.20106](http://arxiv.org/abs/2502.20106) |
| Authors | Weeda, Joris J., Bakker, Saray, Chen, Gang, Alonso-Mora, Javier |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Navigation Among Movable Obstacles (NAMO) poses a challenge for traditional path-planning methods when obstacles block the path, requiring push actions to reach the goal.
- We propose a framework that enables movability-aware planning to overcome this challenge without relying on explicit obstacle placement.
- Qualitative and quantitative experiments suggest that SVG-MPPI outperforms existing paradigm that uses only binary movability for planning, achieving higher success rates with reduced cumulative contact forces.

## Task

* Motion Planning
* Control

## Keywords

* Motion and Path Planning / Collision Avoidance / Integrated Planning and Control

## AI依存度

* Non-AI

## 何を解決？

* Navigation Among Movable Obstacles (NAMO) poses a challenge for traditional path-planning methods when obstacles block the path, requiring push actions to reach the goal.

## 何が新しい？

* We propose a framework that enables movability-aware planning to overcome this challenge without relying on explicit obstacle placement.

## どうやってる？

* Qualitative and quantitative experiments suggest that SVG-MPPI outperforms existing paradigm that uses only binary movability for planning, achieving higher success rates with reduced cumulative contact forces.

## どこが強い？

* Qualitative and quantitative experiments suggest that SVG-MPPI outperforms existing paradigm that uses only binary movability for planning, achieving higher success rates with reduced cumulative contact forces.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
