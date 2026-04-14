# A Hessian for Gaussian Mixture Likelihoods in Nonlinear Least Squares

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Sensor Fusion 1 |
| arXiv | [http://arxiv.org/abs/2404.05452](http://arxiv.org/abs/2404.05452) |
| Authors | Korotkine, Vassili, Cohen, Mitchell, Forbes, James Richard |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper proposes a novel Hessian approximation for Maximum a Posteriori estimation problems in robotics involving Gaussian mixture likelihoods.
- Previous approaches manipulate the Gaussian mixture likelihood into a form that allows the problem to be represented as a nonlinear least squares (NLS) problem.
- The proposed Hessian approximation results in improved convergence speed and uncertainty characterization for simulated experiments, and similar performance to the state of the art on real-world experiments.

## Task

* SLAM
* Sensor Fusion
* State Estimation

## Keywords

* Sensor Fusion / Probabilistic Inference / SLAM

## AI依存度

* Non-AI

## 何を解決？

* This paper proposes a novel Hessian approximation for Maximum a Posteriori estimation problems in robotics involving Gaussian mixture likelihoods.

## 何が新しい？

* This paper proposes a novel Hessian approximation for Maximum a Posteriori estimation problems in robotics involving Gaussian mixture likelihoods.

## どうやってる？

* The resulting Hessian approximation used within NLS solvers from these approaches neglects certain nonlinearities.

## どこが強い？

* The proposed Hessian approximation results in improved convergence speed and uncertainty characterization for simulated experiments, and similar performance to the state of the art on real-world experiments.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Previous approaches manipulate the Gaussian mixture likelihood into a form that allows the problem to be represented as a nonlinear least squares (NLS) problem.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
