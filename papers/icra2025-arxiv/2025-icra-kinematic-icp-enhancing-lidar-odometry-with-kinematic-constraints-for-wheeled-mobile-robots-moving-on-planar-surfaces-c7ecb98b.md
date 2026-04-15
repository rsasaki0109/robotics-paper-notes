# Kinematic-ICP: Enhancing LiDAR Odometry with Kinematic Constraints for Wheeled Mobile Robots Moving on Planar Surfaces

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Point Cloud Registration |
| arXiv | [http://arxiv.org/abs/2410.10277](http://arxiv.org/abs/2410.10277) |
| Authors | Guadagnino, Tiziano;Mersch, Benedikt;Vizzo, Ignacio;Gupta, Saurabh;Malladi, Meher Venkata Ramakrishna;Lobefaro, Luca;Doisy, Guillaume;Stachniss, Cyrill |
| Source | ICRA 2025 / arXiv |

## TL;DR

- wheeled robot が平面上を動くという前提を ICP の**最適化そのもの**に入れた `Kinematic-ICP` を提案している。
- wheel odometry を初期値に使うだけでなく、LiDAR registration の修正量を unicycle 系の運動学制約に沿って制限するのが肝。
- 倉庫や屋外で KISS-ICP 系より安定しており、特徴が薄い corridor 的環境でも wheel 制約が効く。

## Task

* Localization
* LiDAR
* Odometry
* Mapping

## Keywords

* ICP / Wheeled Robots / Kinematic Constraints / Planar Motion / Wheel Odometry

## AI依存度

* Non-AI

## 何を解決？

* LiDAR odometry は 6DoF registration として書かれることが多いが、平面移動する車輪ロボットでは不自然な自由度まで解いてしまう。
* wheel odometry は局所的には強いが単独では drift するため、LiDAR ときれいに融合したい。

## 何が新しい？

* SE(3) の ICP 修正を、そのまま受け入れるのでなく **kinematic model を通して制約**する点。
* wheel odometry を単なる prior でなく、LiDAR 最適化と一体に扱う設計。
* 環境に応じて wheel 情報の効かせ方を変える adaptive weighting を入れている点。

## どうやってる？

* wheel odometry を使って scan alignment の初期姿勢を与える。
* ICP residual の Jacobian に、kinematic model 由来の Jacobian をチェーンルールで掛けて planar motion 制約を入れる。
* regularization 項で wheel odometry との整合も見つつ、重みは状況に応じて調整する。
* 結果として、最適化が「数学的には動けるが実機では動けない」解へ行きにくい。

## どこが強い？

* 問題設定が明快で、車輪ロボットならかなり広く刺さる。
* LiDAR front-end に domain knowledge をきれいに入れていて、実装価値が高い。
* 実運用ロボット群で回っているという話まであるので、単なる benchmark 改善に留まらない。

## 弱そうなところ

* planar motion 仮定が崩れる地形や大きなスリップでは効き方が落ちる。
* extrinsic calibration がずれると、運動学制約が逆にバイアス源になる可能性がある。
* holonomic / skid-steer / legged など別プラットフォームへはそのまま使えない。

## 関連研究との違い

* LeGO-LOAM などは前処理や ground segmentation に寄るが、Kinematic-ICP は運動学制約を registration に直接入れる。
* factor-graph 後段で wheel を足す方法より、front-end の alignment 自体を機械制約に沿わせるのが特徴。
* KISS-ICP 系の「汎用で軽い」路線に、プラットフォーム知識を足して実務寄りにした印象。

## non-AIとして見る価値

* odometry の性能は特徴抽出だけでなく、「どんな運動を許すか」のモデル化で大きく変わるとわかる。
* 倉庫 AMR や屋内搬送のような現実タスクに直結しやすく、かなり再利用価値が高い。

## 難易度

★★★☆☆

## 自分の理解/感想

* ICP をただ頑健化するのでなく、ロボットの動き方そのものを入れているのが良い。
* warehouse 系ではかなり強そうで、実機へ持っていくなら優先して試したくなるタイプの論文。
