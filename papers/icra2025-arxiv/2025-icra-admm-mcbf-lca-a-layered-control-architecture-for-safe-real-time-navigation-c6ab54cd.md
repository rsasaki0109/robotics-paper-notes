# ADMM-MCBF-LCA: A Layered Control Architecture for Safe Real-Time Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Optimization and Trajectory Planning |
| arXiv | [http://arxiv.org/abs/2503.02208](http://arxiv.org/abs/2503.02208) |
| Authors | Srikanthan, Anusha;Xue, Yifan;Kumar, Vijay;Matni, Nikolai;Figueroa, Nadia |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We consider the problem of safe real-time navigation of a robot in a dynamic environment with moving obstacles of arbitrary smooth geometries and input saturation constraints.
- We assume that the robot detects and models nearby obstacle boundaries with a short-range sensor and that this detection is error-free.
- This problem presents three main challenges: i) input constraints, ii) safety, and iii) real-time computation.

## Task

* Visual-Inertial
* Control
* Perception

## Keywords

* Optimization and Optimal Control
* Integrated Planning and Control

## AI依存度

* Non-AI

## 何を解決？

* We consider the problem of safe real-time navigation of a robot in a dynamic environment with moving obstacles of arbitrary smooth geometries and input saturation constraints.

## 何が新しい？

* Our experiments demonstrate that among all algorithms, only our proposed LCA is able to complete tasks such as reaching a goal, safely.

## どうやってる？

* To overcome the limitations of reactive methods, our offline path library consists of feasible controllers, feedback gains, and reference trajectories.

## どこが強い？

* Our experiments demonstrate that among all algorithms, only our proposed LCA is able to complete tasks such as reaching a goal, safely.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Our experiments demonstrate that among all algorithms, only our proposed LCA is able to complete tasks such as reaching a goal, safely.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
