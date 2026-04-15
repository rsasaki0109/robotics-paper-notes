# DynaVINS++: Robust Visual-Inertial State Estimator in Dynamic Environments by Adaptive Truncated Least Squares and Stable State Recovery

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Visual-Inertial Odometry |
| arXiv | [http://arxiv.org/abs/2410.15373](http://arxiv.org/abs/2410.15373) |
| Authors | Song, Seungwon, Lim, Hyungtae, Lee, Alex, Myung, Hyun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 動的環境の VINS が急に動き出す物体で壊れる問題に対して、`DynaVINS++` は adaptive truncated least squares と state recovery を組み合わせて立て直す。
- 視覚残差の外れ値処理だけでなく、IMU bias の崩れも監視して rollback する構成になっているのがポイント。
- public / real-world dataset で、abruptly dynamic object が出る場面でも既存 robust VINS より安定している。

## Task

* SLAM
* Localization
* Sensor Fusion
* State Estimation

## Keywords

* VINS / Dynamic Objects / Truncated Least Squares / IMU Bias / Robust Estimation

## AI依存度

* Non-AI

## 何を解決？

* 動的環境向け VINS は多数あるが、「途中から急に動き出す物体」による外れ値は依然つらい。
* 視覚対応の崩れが IMU bias 推定まで連鎖すると、単なる outlier rejection では回復しきれず divergence する。

## 何が新しい？

* 視覚残差に対して truncation range を固定せず、状況に応じて調整する **adaptive TLS** を入れた点。
* IMU bias consistency check と stable state recovery を組み合わせ、bias が壊れたときに状態を戻せるようにした点。
* dynamic feature rejection と state recovery を別々でなく一つの robust VINS pipeline にまとめた点。

## どうやってる？

* bundle adjustment / VINS optimization の中で、feature association と IMU preintegration を見ながら truncation range を調整する。
* 静的特徴の残差分布を使って外れ値の切り方を適応的に決め、急な動的物体に引きずられにくくする。
* bias consistency を監視し、異常な偏りが出たら直前の安定状態に戻す recovery 機構を入れる。
* つまり「外れ値を減らす」だけでなく、「壊れた state を復元する」まで面倒を見る構成。

## どこが強い？

* abruptly dynamic objects に対して、既存の robust VINS より failure mode をよく捉えている。
* bias 崩壊を明示的に扱っているので、単なる視覚 front-end 改善より一段深い。
* 学習モデルに頼らず classical robust estimation でここまで攻めているのが良い。

## 弱そうなところ

* truncation 関連や recovery 判定に複数の閾値があり、環境依存の調整は残りそう。
* 動的物体が非常に多い、あるいは長時間 scene を支配するケースでは recovery 頻発の可能性がある。
* ORB-SLAM3 系など他の強い baseline との比較は、さらに見てみたい。

## 関連研究との違い

* 既存 robust VINS は視覚残差の downweighting / filtering に寄ることが多く、bias の壊れ方まで踏み込まない。
* learning-based dynamic object removal と違い、未知クラスの動体にも classical residual design で対応しようとしている。
* 前作 DynaVINS よりも、計算コストと recovery の両面で実用寄りに整理されている。

## non-AIとして見る価値

* dynamic environment の VINS を、semantic segmentation なしでどこまで守れるかを見る上で価値が高い。
* residual / bias / recovery を一つの推定器として設計する発想が、そのまま他の state estimator にも効く。

## 難易度

★★★☆☆

## 自分の理解/感想

* これはかなり実装寄りで、動的物体に強い VINS を作るときの failure analysis がうまい。
* learned dynamic masking に行く前に、まずここまで classical に詰める価値は大きいと感じた。
