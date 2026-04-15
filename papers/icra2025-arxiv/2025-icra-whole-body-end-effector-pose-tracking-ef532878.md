# Whole-Body End-Effector Pose Tracking

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planinng and Control for Legged Robots 3 |
| arXiv | [http://arxiv.org/abs/2409.16048](http://arxiv.org/abs/2409.16048) |
| Authors | Portela, Tifanny;Cramariuc, Andrei;Mittal, Mayank;Hutter, Marco |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Combining manipulation with the mobility of legged robots is essential for a wide range of robotic applications.
- However, integrating an arm with a mobile base significantly increases the systems complexity, making precise end-effector control challenging.
- Existing model-based approaches are often constrained by their modeling assumptions, leading to limited robustness.

## Task

* Motion Planning
* Control
* Manipulation
* Legged Robotics

## Keywords

* Whole-Body Motion Planning and Control
* Reinforcement Learning
* Legged Robots

## AI依存度

* Hybrid

## 何を解決？

* Combining manipulation with the mobility of legged robots is essential for a wide range of robotic applications.

## 何が新しい？

* Our proposed method involves a terrain-aware sampling strategy for the robots initial configuration and end-effector pose commands, as well as a game-based curriculum to extend the robots operating range.

## どうやってる？

* Our proposed method involves a terrain-aware sampling strategy for the robots initial configuration and end-effector pose commands, as well as a game-based curriculum to extend the robots operating range.

## どこが強い？

* Through our experiments, we show that the learned controller achieves precise command tracking over a large workspace and adapts across varying terrains such as stairs and slopes.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Our proposed method involves a terrain-aware sampling strategy for the robots initial configuration and end-effector pose commands, as well as a game-based curriculum to extend the robots operating range.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
