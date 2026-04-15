# Integrating Field of View in Human-Aware Collaborative Planning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Human-Robot Collaboration 2 |
| arXiv | [http://arxiv.org/abs/2505.14805](http://arxiv.org/abs/2505.14805) |
| Authors | Hsu, Ya-Chuan;Michael, Defranco;Patel, Rutvik Rakeshbhai;Nikolaidis, Stefanos |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In human-robot collaboration (HRC), it is crucial for robot agents to consider humans' knowledge of their surroundings.
- In reality, humans possess a narrow field of view (FOV), limiting their perception.
- However, research on HRC often overlooks this aspect and presumes an omniscient human collaborator.

## Task

* Motion Planning
* Perception
* Human-Robot Interaction

## Keywords

* Human-Robot Collaboration
* Planning under Uncertainty
* Human-Aware Motion Planning

## AI依存度

* Non-AI

## 何を解決？

* In human-robot collaboration (HRC), it is crucial for robot agents to consider humans' knowledge of their surroundings.

## 何が新しい？

* To account for large state spaces due to considering FOV, we propose a hierarchical online planner that efficiently finds approximate solutions while enabling the robot to explore low-level action trajectories that enter the human FOV, influencing their intended subtask.

## どうやってる？

* We integrate FOV within the human-aware probabilistic planning framework.

## どこが強い？

* Through user study with our adapted cooking domain, we demonstrate our FOV-aware planner reduces human's interruptions and redundant actions during collaboration by adapting to human perception limitations.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To account for large state spaces due to considering FOV, we propose a hierarchical online planner that efficiently finds approximate solutions while enabling the robot to explore low-level action trajectories that enter the human FOV, influencing their intended subtask.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
