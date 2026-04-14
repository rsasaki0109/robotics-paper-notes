# Real-Time Planning of Minimum-Time Trajectories for Agile UAV Flight

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Planning and Control |
| arXiv | [http://arxiv.org/abs/2409.16074](http://arxiv.org/abs/2409.16074) |
| Authors | Teissing, Krystof, Novosad, Matej, Penicka, Robert, Saska, Martin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We address the challenge of real-time planning of minimum-time trajectories over multiple waypoints, onboard multirotor UAVs.
- Previous works demonstrated that achieving a truly time-optimal trajectory is computationally too demanding to enable frequent replanning during agile flight, especially on less powerful flight computers.
- Our approach overcomes this stumbling block by utilizing a point-mass model with a novel iterative thrust decomposition algorithm, enabling the UAV to use all of its collective thrust, something previous point-mass approaches could not achieve.

## Task

* Perception
* Motion Planning
* Control
* Aerial Robotics

## Keywords

* Aerial Systems: Applications / Motion and Path Planning

## AI依存度

* Non-AI

## 何を解決？

* We address the challenge of real-time planning of minimum-time trajectories over multiple waypoints, onboard multirotor UAVs.

## 何が新しい？

* Our approach overcomes this stumbling block by utilizing a point-mass model with a novel iterative thrust decomposition algorithm, enabling the UAV to use all of its collective thrust, something previous point-mass approaches could not achieve.

## どうやってる？

* Our approach overcomes this stumbling block by utilizing a point-mass model with a novel iterative thrust decomposition algorithm, enabling the UAV to use all of its collective thrust, something previous point-mass approaches could not achieve.

## どこが強い？

* Previous works demonstrated that achieving a truly time-optimal trajectory is computationally too demanding to enable frequent replanning during agile flight, especially on less powerful flight computers.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Previous works demonstrated that achieving a truly time-optimal trajectory is computationally too demanding to enable frequent replanning during agile flight, especially on less powerful flight computers.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
