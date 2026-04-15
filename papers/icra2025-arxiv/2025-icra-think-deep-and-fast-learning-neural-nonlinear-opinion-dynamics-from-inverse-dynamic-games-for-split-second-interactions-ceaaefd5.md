# Think Deep and Fast: Learning Neural Nonlinear Opinion Dynamics from Inverse Dynamic Games for Split-Second Interactions

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planning under Uncertainty 3 |
| arXiv | [http://arxiv.org/abs/2406.09810](http://arxiv.org/abs/2406.09810) |
| Authors | Hu, Haimin;Fernández Fisac, Jaime;Leonard, Naomi;Gopinath, Deepak;DeCastro, Jonathan;Rosman, Guy |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Non-cooperative interactions commonly occur in multi-agent scenarios such as car racing, where an ego vehicle can choose to overtake the rival, or stay behind it until a safe overtaking corridor opens.
- While an expert human can do well at making such time-sensitive decisions, autonomous agents are incapable of rapidly reasoning about complex, potentially conflicting options, leading to suboptimal behaviors such as deadlocks.
- Recently, the nonlinear opinion dynamics (NOD) model has proven to exhibit fast opinion formation and avoidance of decision deadlocks.

## Task

* Visual-Inertial
* Motion Planning
* Software Tools

## Keywords

* Motion and Path Planning
* Human-Aware Motion Planning
* Learning from Demonstration

## AI依存度

* Hybrid

## 何を解決？

* Non-cooperative interactions commonly occur in multi-agent scenarios such as car racing, where an ego vehicle can choose to overtake the rival, or stay behind it until a safe overtaking corridor opens.

## 何が新しい？

* In this work, we propose for the first time a learning-based and game-theoretic approach to synthesize a Neural NOD model from expert demonstrations, given as a dataset containing (possibly incomplete) state and action trajectories of interacting agents.

## どうやってる？

* In this work, we propose for the first time a learning-based and game-theoretic approach to synthesize a Neural NOD model from expert demonstrations, given as a dataset containing (possibly incomplete) state and action trajectories of interacting agents.

## どこが強い？

* We demonstrate Neural NODs ability to make fast and deadlock-free decisions in a simulated autonomous racing example.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this work, we propose for the first time a learning-based and game-theoretic approach to synthesize a Neural NOD model from expert demonstrations, given as a dataset containing (possibly incomplete) state and action trajectories of interacting agents.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
