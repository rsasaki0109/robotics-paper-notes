# Universal Online Temporal Calibration for Optimization-Based Visual-Inertial Navigation Systems

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Calibration 3 |
| arXiv | [http://arxiv.org/abs/2501.01788](http://arxiv.org/abs/2501.01788) |
| Authors | Fan, Yunfei, Zhao, Tianyu, Guo, Linan, Chen, Chen, Wang, Xin, Zhou, Fengyi |
| Source | ICRA 2025 / arXiv |

## TL;DR

- optimization-based VINS の camera-IMU time offset を、追加 state と Jacobian で online に同時推定する手法。
- optical flow に強く依存せず、姿勢・速度由来の補正式を視覚残差へ直接組み込むので、既存 VINS に比較的入れやすい。
- EuRoC と simulation では noisy sensor 条件でも time offset 推定が安定し、収束速度も良いという主張。

## Task

* SLAM
* Localization
* Perception
* Sensor Fusion

## Keywords

* Temporal Calibration / VINS / Time Offset / Jacobian / Online Optimization

## AI依存度

* Non-AI

## 何を解決？

* camera と IMU の時間ずれは、見た目以上に VINS の初期化・追跡・精度に効く。
* offline calibration や optical-flow ベース補正は、ノイズや運動条件によっては不安定で、既存 optimizer にも入れにくい。

## 何が新しい？

* time offset `t_d` を state に足し、視覚残差の Jacobian に明示的に入れて online 最適化できるようにした点。
* optical flow に強く依存しない形で、角速度と並進速度から画像時刻への補正を組み立てた点。
* 「特定の VINS 専用」ではなく optimization-based VINS 全般に乗せやすい universal な書き方を目指している点。

## どうやってる？

* IMU 姿勢・位置を画像タイムスタンプへずらす補正式を導き、視覚因子の residual に `t_d` の寄与を追加する。
* 回転補正は角速度、並進補正は速度を用いた一次近似で書き、最適化内で他 state と一緒に更新する。
* 既存の visual residual 構造を大きく変えずに、`J_td` を加える形で実装できるようにしている。
* 実験では EuRoC と simulation で time offset accuracy / convergence を比較している。

## どこが強い？

* 地味だが効く calibration 問題を、VINS の本体 optimizer の中で自然に扱っている。
* optical flow ベース手法より noisy sensor 条件で安定しやすいという設計意図が明確。
* 「既存 VINS にどう足すか」の見通しが立ちやすく、実装へ持ち込みやすい。

## 弱そうなところ

* 一次近似ベースなので、非常に大きな time offset や激しい運動では線形化の効き方が気になる。
* 初期速度推定や姿勢推定が悪いと、time offset 更新も引きずられそう。
* 計算コスト増加が軽いのは利点だが、rank deficiency や observability の議論はもう少し追いたい。

## 関連研究との違い

* EKF ベースの time calibration と違い、optimization framework の残差・Jacobian に直接組み込んでいる。
* Qin 系の optical-flow 依存補正より、速度・角速度ベースでより一般の optimizer に載せやすい。
* offline factory calibration ではなく、運用中の drift や small offset を拾う online calibration の立場。

## non-AIとして見る価値

* localization の実性能を落とす原因が「アルゴリズム本体」ではなく「時刻ずれ」にあることを再認識できる。
* VINS を本番投入するときの現実的なボトルネックに直結していて、派手さ以上に実務価値がある。

## 難易度

★★★☆☆

## 自分の理解/感想

* かなり実装フレンドリーで、VINS の安定化に効くタイプの論文。こういう論文は後から効いてくる。
* 規模の大きい理論新規性ではないが、「既存システムへ自然に入る calibration」という意味で実戦向き。
