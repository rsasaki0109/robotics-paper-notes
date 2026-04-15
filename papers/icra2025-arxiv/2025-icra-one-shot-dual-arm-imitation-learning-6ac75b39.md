# One-Shot Dual-Arm Imitation Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Bimanual Manipulation 1 |
| arXiv | [http://arxiv.org/abs/2503.06831](http://arxiv.org/abs/2503.06831) |
| Authors | Wang, Yilong;Johns, Edward |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We introduce One-Shot Dual-Arm Imitation Learning (ODIL), which enables dual-arm robots to learn precise and coordinated everyday tasks from just a single demonstration of the task.
- ODIL uses a new three-stage visual servoing (3-VS) method for precise alignment between the end-effector and target object, after which replay of the demonstration trajectory is sufficient to perform the task.
- This is achieved without requiring prior task or object knowledge, or additional data collection and training following the single demonstration.

## Task

* Motion Planning
* Manipulation

## Keywords

* Dual Arm Manipulation
* Imitation Learning
* Visual Servoing

## AI依存度

* Hybrid

## 何を解決？

* We introduce One-Shot Dual-Arm Imitation Learning (ODIL), which enables dual-arm robots to learn precise and coordinated everyday tasks from just a single demonstration of the task.

## 何が新しい？

* Furthermore, we propose a new dual-arm coordination paradigm for learning dual-arm tasks from a single demonstration.

## どうやってる？

* ODIL uses a new three-stage visual servoing (3-VS) method for precise alignment between the end-effector and target object, after which replay of the demonstration trajectory is sufficient to perform the task.

## どこが強い？

* ODIL was tested on a real-world dual-arm robot, demonstrating state-of-the-art performance across six precise and coordinated tasks in both 4-DoF and 6-DoF settings, and showing robustness in the presence of distractor objects and partial occlusions.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Furthermore, we propose a new dual-arm coordination paradigm for learning dual-arm tasks from a single demonstration.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
