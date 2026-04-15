# Improving Monocular Visual-Inertial Initialization with Structureless Visual-Inertial Bundle Adjustment

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Visual-Inertial Odometry |
| arXiv | [http://arxiv.org/abs/2502.16598](http://arxiv.org/abs/2502.16598) |
| Authors | Song, Junlin;Richard, Antoine;Olivares-Mendez, Miguel A. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- monocular VIO initialization を、**structureless visual-inertial BA** で精度改善する論文。
- 3D point を明示再構成せず、epipolar constraint と IMU preintegration を使って **初期化だけを joint refinement** している。
- full structure-based BA ほど重くしたくないが、従来の decoupled structureless init よりは精度が欲しい、というかなり実務的な狙い。

## Task

* Visual-Inertial Odometry
* Initialization
* Bundle Adjustment
* State Estimation

## Keywords

* Structureless BA / Epipolar Constraint / IMU Preintegration / Monocular VIO / Initialization

## AI依存度

* Non-AI

## 何を解決？

* monocular VIO は初期化が不安定だと、その後全部が崩れる。
* structure-based な initialization/BA は精度は出やすいが、3D point 再構成が重い。
* 一方、従来の structureless 初期化は軽いが、rotation / translation を分けすぎて情報を捨てがちだった。

## 何が新しい？

* 3D landmark を持たない **structureless visual-inertial BA** を初期化 refinement に使う点。
* visual residual を reprojection ではなく epipolar constraint で書き、state を軽く保つ点。
* 既存の structureless initializer の出力を warm start にして、nonlinear optimization で joint に詰める点。

## どうやってる？

* まず既存の structureless 法で初期姿勢・速度・bias などをざっくり求める。
* その後、IMU preintegration residual と visual epipolar residual を束ねた cost を作る。
* 10 keyframe くらいの window で pose / velocity / bias を joint に最適化し、初期化精度を上げる。
* point を持たないので、full BA より state が小さく、real-time で回しやすい。

## どこが強い？

* structureless の軽さを保ちながら、初期化精度をかなり改善している。
* VIO pipeline に組み込みやすく、cold start や re-init 強化にそのまま効く。
* IMU と visual の coupled refinement になっていて、単なる後処理より筋が良い。

## 弱そうなところ

* 速いとはいえ、従来の超軽量 initializer よりは当然重くなる。
* あくまで initialization 改善であり、full odometry 全体を変える論文ではない。
* aggressive motion や feature quality の悪い条件でどこまで頑健かはさらに見たい。

## 関連研究との違い

* VINS-Mono 系の structure-based BA より、**3D point を持たない**のが大きい。
* 既存の structureless initializer より、linear / decoupled 解で終わらず nonlinear refinement を入れている。
* learned depth priors を使う初期化より、完全に幾何と慣性で押している。

## non-AIとして見る価値

* VIO の難所である initialization を、**epipolar geometry と IMU preintegration** で丁寧に詰めている。
* 実装上も「どこまで structureless で引っ張れるか」が見えて面白い。

## 難易度

★★★☆☆

## 自分の理解/感想

* 派手な新機軸ではないが、VIO を実装するときにかなり欲しい改善。
* 初期化だけに絞って丁寧に強くしているのが実務的で好感が持てる。
