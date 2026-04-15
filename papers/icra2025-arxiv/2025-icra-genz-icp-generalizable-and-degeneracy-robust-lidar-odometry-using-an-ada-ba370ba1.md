# GenZ-ICP: Generalizable and Degeneracy-Robust LiDAR Odometry Using an Adaptive Weighting

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | SLAM 4 |
| arXiv | [http://arxiv.org/abs/2411.06766](http://arxiv.org/abs/2411.06766) |
| Authors | Lee, Daehan, Lim, Hyungtae, Han, Soohee |
| Source | ICRA 2025 / arXiv |

## TL;DR

- LiDAR odometry が corridor のような退化環境で壊れやすい原因を、単一の ICP error metric 依存だと捉え、`GenZ-ICP` を提案している。
- point-to-plane と point-to-point を局所幾何に応じて切り替え、adaptive weighting で混ぜることで、構造化環境と非構造化環境の両方に対応する。
- 一般環境では SOTA 級と同等、長廊下のような退化ケースではかなり強く、ill-posed optimization を避けるのが効いている。

## Task

* SLAM
* Localization
* LiDAR
* Mapping

## Keywords

* ICP / Degeneracy / Point-to-Plane / Point-to-Point / Adaptive Weighting

## AI依存度

* Non-AI

## 何を解決？

* point-to-plane は structured 環境では強いが、normal が信用できない場面では弱い。
* point-to-point は汎用性はあるが、平面構造がはっきりした環境では情報を十分使えない。
* 既存 LiDAR odometry はどちらか一方に寄りがちで、長廊下やトンネルのような退化環境で最適化が不安定になる。

## 何が新しい？

* 対応点ごとの **planarity classification** によって、点対平面と点対点を局所的に使い分ける点。
* planar / non-planar の割合から adaptive weight を決め、環境に応じて cost の混合比を動的に変える点。
* 退化対策を「後段の拘束追加」ではなく、ICP の cost 設計そのものに埋め込んでいる点。

## どうやってる？

* scan-to-map matching の各 correspondence について、局所幾何から planar か non-planar かを判定する。
* planar と判定した対応には point-to-plane residual、そうでないものには point-to-point residual を与える。
* 最適化は両 residual を adaptive weight 付きでまとめて解き、環境構造に応じて point-to-plane 偏重にも point-to-point 偏重にも寄れるようにする。
* corridor 退化では point-to-point の数値的な安定性を活かし、ill-posed な Hessian を避けるのが肝になっている。

## どこが強い？

* 設計がかなり素直で、既存 ICP 系フロントエンドに入れやすい。
* 「なぜ corridor で効くか」を条件数や ill-posedness の観点で説明していて納得感がある。
* Newer College / KITTI / MulRan / HILTI / SubT まで評価範囲が広く、特殊ケース専用手法に見えにくい。

## 弱そうなところ

* planarity 閾値や weighting の設計にパラメータ依存が残る。
* LiDAR 単体 front-end の改善色が強く、IMU や wheel と組み合わせた全体最適化での効き方は別途見たい。
* 雨・霧・強反射のようなセンサ劣化ケースへの強さはこの論文の主題ではない。

## 関連研究との違い

* G-ICP 系は平面近似の仮定が強く、環境によっては approximation error を抱えやすい。
* 既存の degeneracy 対策は detection 後に constraint や外部センサへ逃がすものが多いが、GenZ-ICP は cost 自体で崩れにくくしている。
* point-to-plane / point-to-point の二項対立をやめて、環境依存で両者を混ぜる設計にしたのが本質。

## non-AIとして見る価値

* LiDAR odometry の性能差が「特徴量」よりもまず residual 設計で決まることを実感しやすい。
* 実装負荷が比較的低い改善なので、自前 front-end に持ち込みやすいアイデアとして価値が高い。

## 難易度

★★★★☆

## 自分の理解/感想

* かなり好きなタイプの論文で、派手な新規モデルより「どの residual をどこで使うか」を丁寧に詰めている。
* 実運用でも試しやすそうで、Top 12 に入れる理由がわかりやすい一本だった。
