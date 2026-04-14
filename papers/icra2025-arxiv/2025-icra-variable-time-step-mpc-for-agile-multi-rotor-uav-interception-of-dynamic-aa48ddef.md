# Variable Time-Step MPC for Agile Multi-Rotor UAV Interception of Dynamic Targets

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Planning and Control |
| arXiv | [http://arxiv.org/abs/2503.14184](http://arxiv.org/abs/2503.14184) |
| Authors | Ghotavadekar, Atharva, Nekovar, Frantisek, Saska, Martin, Faigl, Jan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we propose to address these limitations by introducing variable time-steps and coupling them with the prediction horizon length.
- Agile trajectory planning can improve the efficiency of multi-rotor Uncrewed Aerial Vehicles (UAVs) in scenarios with combined task-oriented and kinematic trajectory planning, such as monitoring spatio-temporal phenomena or intercepting dynamic targets.
- Based on evaluation results and experimentally validated deployment, the proposed method increases the solution quality by enabling planning for long flight segments but allowing tightly sampled maneuvering.

## Task

* Motion Planning
* Control
* Intelligent Vehicles
* Aerial Robotics

## Keywords

* Aerial Systems: Applications / Motion and Path Planning / Autonomous Vehicle Navigation

## AI依存度

* Non-AI

## 何を解決？

* Agile trajectory planning can improve the efficiency of multi-rotor Uncrewed Aerial Vehicles (UAVs) in scenarios with combined task-oriented and kinematic trajectory planning, such as monitoring spatio-temporal phenomena or intercepting dynamic targets.

## 何が新しい？

* In this paper, we propose to address these limitations by introducing variable time-steps and coupling them with the prediction horizon length.

## どうやってる？

* Agile planning using existing non-linear model predictive control methods is limited by the number of planning steps as it becomes increasingly computationally demanding.

## どこが強い？

* Based on evaluation results and experimentally validated deployment, the proposed method increases the solution quality by enabling planning for long flight segments but allowing tightly sampled maneuvering.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: planning, control, planning / control / perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
