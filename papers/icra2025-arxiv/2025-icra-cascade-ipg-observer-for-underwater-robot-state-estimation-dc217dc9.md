# Cascade IPG Observer for Underwater Robot State Estimation

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Marine Robotics 3 |
| arXiv | [http://arxiv.org/abs/2504.15235](http://arxiv.org/abs/2504.15235) |
| Authors | Joshi, Kaustubh;Liu, Tianchen;Chopra, Nikhil |
| Source | ICRA 2025 / arXiv |

## TL;DR

- underwater robot の state estimation を、**2 段の IPG observer を cascade** する形で設計している。
- IMU preintegration を使うことで、厳密な hydrodynamic model に依りすぎない **model-light observer** にしているのがポイント。
- EKF / InEKF 系より精度面でかなり健闘しており、underwater らしい「GPS なし・モデル不確か」をよく意識している。

## Task

* Marine Robotics
* State Estimation
* Underwater Localization
* Nonlinear Observers

## Keywords

* IPG Observer / IMU Preintegration / DVL / AHRS / Underwater State Estimation

## AI依存度

* Non-AI

## 何を解決？

* underwater では GPS が使えず、vision も濁りや照明で不安定になりやすい。
* 一方で model-based filter は hydrodynamic parameter に依存しやすく、機体ごとの差や drag 変化で苦しくなる。
* そこで、比較的少ない sensor 構成で、かつ dynamics model に強く依存しない estimator を作りたい。

## 何が新しい？

* rotation 推定と translation / velocity 推定を分けた **cascade IPG observer**。
* IMU preintegration を observer 側に入れて、更新周期の異なる IMU・DVL・AHRS を扱いやすくしている点。
* InEKF のように群構造を強く押すより、**model uncertainty に耐える observer design** を前に出している点。

## どうやってる？

* 第1段で quaternion / rotation を IPG ベースの observer で推定する。
* その推定姿勢を使って、第2段で velocity と position を推定する。
* IMU は高レートなので preintegration し、DVL や AHRS の低レート更新と整合を取る。
* 要するに、姿勢を先に安定化させてから並進側へ渡す cascade 設計で、joint に全部抱え込まない。

## どこが強い？

* hydrodynamic model への依存を減らしているので、platform 変更に強そう。
* underwater の現実的 sensor 構成を前提にしていて、研究用の豪華センサ依存が薄い。
* public dataset と実機の両方で比較しており、observer 論文として説得力がある。

## 弱そうなところ

* yaw / heading の長期安定性はまだ弱く、magnetometer など追加情報が欲しくなる。
* cascade なので、上流の姿勢誤差が下流へそのまま効く。
* EKF より計算負荷は軽くないので、超小型計算機では tuning が必要そう。

## 関連研究との違い

* EKF / InEKF に比べ、**厳密な vehicle dynamics model への依存を下げている**。
* visual SLAM や sonar SLAM と違い、より軽量な慣性・速度計ベースの estimator として位置づけられる。
* 一体型の observer でなく、rotation と translation を分ける cascade 構成が特徴。

## non-AIとして見る価値

* sensor fusion を learned black box でなく、**observer design と preintegration** で詰める王道の論文。
* underwater robotics で state estimation がどこで難しくなるかを理解する入口として良い。

## 難易度

★★★☆☆

## 自分の理解/感想

* 新奇性は爆発的ではないが、underwater という難しい条件に対してかなり筋の良い設計。
* 「モデルを入れすぎると壊れ、入れなさすぎると漂う」という underwater estimation の難しさがよく見える。
