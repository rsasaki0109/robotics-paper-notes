# Variable Time-Step MPC for Agile Multi-Rotor UAV Interception of Dynamic Targets

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Planning and Control |
| arXiv | [http://arxiv.org/abs/2503.14184](http://arxiv.org/abs/2503.14184) |
| Authors | Ghotavadekar, Atharva, Nekovar, Frantisek, Saska, Martin, Faigl, Jan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 予測ステップ幅そのものを最適化変数に入れた `variable time-step MPC` を提案し、固定ステップ MPC より長い horizon と細かい maneuver を両立させる。
- dynamic target interception / monitoring のような KOP 的タスクに対して、報酬と機動性を両方見ながら UAV 軌跡を作る。
- onboard 実験まで通していて、agile UAV planning を実践寄りに詰めた MPC 論文。

## Task

* Motion Planning
* Control
* Intelligent Vehicles
* Aerial Robotics

## Keywords

* MPC / Variable Time-Step / KOP / UAV Interception / Differential Flatness

## AI依存度

* Non-AI

## 何を解決？

* fixed time-step MPC は、長い horizon を見たければ step 数を増やす必要があり、計算量がすぐ増える。
* 逆に機動区間を細かく刻みたいときは、長距離計画の見通しが悪くなる。

## 何が新しい？

* prediction step の `Δt_k` を最適化変数にし、horizon 長と sampling density を同時に調整する点。
* Kinematic Orienteering Problem 的な reward collection を、agile UAV trajectory generation と結び付けた点。
* 軸ごとの box 制約でなく、速度・加速度の球面制約を使って機体能力をより自然に使う点。

## どうやってる？

* quadrotor は differential flatness を使って簡略化し、jerk 入力の点質量モデル上で MPC を定式化する。
* cost に target reward と flight time を入れつつ、各 step の時間幅 `Δt_k` も一緒に最適化する。
* NLP は IPOPT 系で解き、前回解の warm start を使って onboard replanning へつなぐ。
* 実験では KOP benchmark と実ドローンで、fixed-step MPC との比較をしている。

## どこが強い？

* アイデアが単純で効き方がわかりやすく、MPC 実装者に刺さる。
* same horizon steps でも、先を見る区間と細かく操る区間を両立できるのが実用的。
* simulation だけでなく onboard 実験まで回しているのが良い。

## 弱そうなところ

* target motion の外部推定に依存するので、perception 誤差込みの robustness は別問題として残る。
* NLP の安定性や warm start 品質に依存し、状況によっては local minima に入りそう。
* obstacle-rich な 3D 環境で多数 target を扱うと、計算コストの伸びが気になる。

## 関連研究との違い

* fixed-step MPC は実装しやすいが、long-horizon と agile maneuver の両立が苦手。
* minimum-snap や spline 系の offline planning より、closed-loop replanning を前提にしている。
* routing と trajectory generation を分離しすぎず、reward-aware MPC として一体化しているのが特徴。

## non-AIとして見る価値

* MPC の性能が cost だけでなく time discretization 設計で変わることがよくわかる。
* UAV planning を classical optimal control で押し切る設計として、かなり実務的。

## 難易度

★★★☆☆

## 自分の理解/感想

* 変数時刻幅は素朴だが強い発想で、agile planning の悩みにかなり素直に効いている。
* 固定離散化を当たり前と思っていた MPC 実装を見直したくなるタイプの論文。
