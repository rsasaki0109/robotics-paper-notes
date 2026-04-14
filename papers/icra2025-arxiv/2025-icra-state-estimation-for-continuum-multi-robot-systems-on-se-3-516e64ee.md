# State Estimation for Continuum Multi-Robot Systems on SE(3)

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | State Estimation |
| arXiv | [http://arxiv.org/abs/2401.13540](http://arxiv.org/abs/2401.13540) |
| Authors | Lilge, Sven, Barfoot, Timothy, Burgner-Kahrs, Jessica |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper presents a novel approach to state estimation for systems with multiple coupled continuum robots, which allows estimating the shape and strain variables of multiple continuum robots in an arbitrary coupled topology.
- In contrast to conventional robots, accurately modeling the kinematics and statics of continuum robots is challenging due to partially unknown material properties, parasitic effects, or unknown forces acting on the continuous body.
- Simulations and experiments demonstrate the capabilities and versatility of the proposed method, while achieving accurate and continuous estimates for the state of such systems, resulting in average end-effector errors of 3.3 mm and 5.02° depending on the sensor setup.

## Task

* Sensor Fusion
* State Estimation

## Keywords

* Flexible Robots / State Estimation / Sensor Fusion / Parallel Robots

## AI依存度

* Non-AI

## 何を解決？

* In contrast to conventional robots, accurately modeling the kinematics and statics of continuum robots is challenging due to partially unknown material properties, parasitic effects, or unknown forces acting on the continuous body.

## 何が新しい？

* This paper presents a novel approach to state estimation for systems with multiple coupled continuum robots, which allows estimating the shape and strain variables of multiple continuum robots in an arbitrary coupled topology.

## どうやってる？

* Consequentially, state estimation approaches that utilize additional sensor information to predict the shape of continuum robots have garnered significant interest.

## どこが強い？

* Simulations and experiments demonstrate the capabilities and versatility of the proposed method, while achieving accurate and continuous estimates for the state of such systems, resulting in average end-effector errors of 3.3 mm and 5.02° depending on the sensor setup.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
