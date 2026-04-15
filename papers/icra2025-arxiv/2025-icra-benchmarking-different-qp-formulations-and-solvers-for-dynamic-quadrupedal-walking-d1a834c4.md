# Benchmarking Different QP Formulations and Solvers for Dynamic Quadrupedal Walking

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Legged Robots |
| arXiv | [http://arxiv.org/abs/2502.01329](http://arxiv.org/abs/2502.01329) |
| Authors | Stark, Franek;Middelberg, Jakob;Mronga, Dennis;Vyas, Shubham;Kirchner, Frank |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Quadratic Programs (QPs) are widely used in the control of walking robots, especially in Model Predictive Control (MPC) and Whole-Body Control (WBC).
- In both cases, the controller design requires the formulation of a QP and the selection of a suitable QP solver, both requiring considerable time and expertise.
- While computational performance benchmarks exist for QP solvers, studies comparing optimal combinations of computational hardware (HW), QP formulation, and solver performance are lacking.

## Task

* Motion Planning
* Control
* Legged Robotics
* Software Tools

## Keywords

* Performance Evaluation and Benchmarking
* Whole-Body Motion Planning and Control
* Legged Robots

## AI依存度

* Non-AI

## 何を解決？

* Quadratic Programs (QPs) are widely used in the control of walking robots, especially in Model Predictive Control (MPC) and Whole-Body Control (WBC).

## 何が新しい？

* We introduce the Solve Frequency per Watt (SFPW) as a performance measure to enable a cross-hardware comparison of the efficiency of QP solvers.

## どうやってる？

* In this work, we compare dense and sparse QP formulations, and multiple solving methods on different HW architectures, focusing on their computational efficiency in dynamic walking of four-legged robots using MPC.

## どこが強い？

* Quadratic Programs (QPs) are widely used in the control of walking robots, especially in Model Predictive Control (MPC) and Whole-Body Control (WBC).

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We introduce the Solve Frequency per Watt (SFPW) as a performance measure to enable a cross-hardware comparison of the efficiency of QP solvers.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
