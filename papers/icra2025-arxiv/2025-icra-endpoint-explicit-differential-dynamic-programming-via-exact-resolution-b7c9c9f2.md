# Endpoint-Explicit Differential Dynamic Programming Via Exact Resolution

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Optimization and Optimal Control |
| arXiv | [http://arxiv.org/abs/2503.03897](http://arxiv.org/abs/2503.03897) |
| Authors | Parilli, Maria;Martinez, Sergi;Mastalli, Carlos |
| Source | ICRA 2025 / arXiv |

## TL;DR

- endpoint constraints を正確に扱える constrained DDP を提案しており、既存の inexact 解法より **quadratic convergence** を狙っている。
- Schur complement と nullspace decomposition を使い、rank-deficient な endpoint / stagewise equality constraints も処理する。
- inverse dynamics や接触制約を含む optimal control 問題で、体操動作のような複雑タスクまで扱っている。

## Task

* Motion Planning
* Control

## Keywords

* DDP / Endpoint Constraints / Riccati Recursion / Schur Complement / Optimal Control

## AI依存度

* Non-AI

## 何を解決？

* constrained DDP で endpoint constraints を入れたいとき、既存法は ADMM 的な inexact resolution に寄りがちで収束が鈍い。
* 制約 Jacobian が rank deficient だと、単純な疑似逆行列処理では数値的に危ない。

## 何が新しい？

* endpoint constraints を **exact** に解く DDP ステップを作り、quadratic convergence を主張している点。
* rank deficiency を nullspace 分解で安全に扱う設計。
* Riccati recursion 構造を壊さずに、endpoint constraint を solver に織り込んでいる点。

## どうやってる？

* 各 iteration で constraint 付き QP を解くが、その KKT 系を Schur complement / nullspace decomposition で解消する。
* 可逆な場合は Schur complement を使い、rank-deficient な場合は nullspace に分けて安定に解く。
* backward pass の Riccati recursion は維持しつつ、endpoint multipliers を明示的に解く構造になっている。
* Crocoddyl 系の流れに近く、MPC や trajectory optimization への接続も意識されている。

## どこが強い？

* endpoint constraints を「ペナルティでごまかす」のではなく、solver 側で正面から解いている。
* quadratic convergence を押し出していて、large-scale OC solver の加速に効きやすい。
* inverse dynamics / contact constraints まで見ているので、legged / humanoid 系への広がりがある。

## 弱そうなところ

* nullspace 分解まわりは実装の難度が高く、数値線形代数の理解がかなり必要。
* 問題定式化に依存する部分が大きく、いつもきれいに効くとは限らなさそう。
* 実ロボットよりシミュレーション寄りなので、実機 MPC での実利はもう少し見たい。

## 関連研究との違い

* ADMM ベースや penalty ベースの constrained DDP は扱いやすいが、収束性では妥協がある。
* endpoint-explicit Riccati 系の先行仕事を、rank-deficient constraint まで含めて押し広げた位置づけ。
* interior-point 系より、DDP / Riccati 構造を活かしたまま constraint を解きたい立場に近い。

## non-AIとして見る価値

* 最適制御ソルバの中身を理解したいときにかなり良い教材。
* 「制約をどう exact に解くか」という話で、MPC 実装の先にある solver design を学べる。

## 難易度

★★★★★

## 自分の理解/感想

* DDP をただ使うだけでなく、solver の core を改善するタイプの論文でかなり好み。
* すぐ実装に入るには重いが、optimal control を本気でやるなら押さえておきたい。
