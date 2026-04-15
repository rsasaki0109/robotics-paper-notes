# PTZ-Calib: Robust Pan-Tilt-Zoom Camera Calibration

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Calibration 2 |
| arXiv | [http://arxiv.org/abs/2502.09075](http://arxiv.org/abs/2502.09075) |
| Authors | Guo, Jinhui, Fan, Lubin, Wu, Bojian, Gu, Jiaqi, Cao, Shen, Ye, Jieping |
| Source | ICRA 2025 / arXiv |

## TL;DR

- PTZ camera の calibration を、offline と online に分けた二段構成で解く `PTZ-Calib`。
- offline では reference views から feature tracks と ray landmarks を作って self-calibration し、online では新視点を relocalization として解く。
- pan / tilt / zoom に加えて focal length や distortion もまとめて扱い、real / synthetic の両方で強い。

## Task

* Calibration
* Localization
* Vision

## Keywords

* PTZ Camera / Bundle Adjustment / Relocalization / Ray Landmarks / Georeferencing

## AI依存度

* Non-AI

## 何を解決？

* PTZ camera は pan / tilt / zoom が変わるたびに内外部パラメータ推定が面倒で、既存法は既知初期値や単純化仮定に寄りがち。
* 実運用では arbitrary viewpoint から素早く calibration / relocalization したい。

## 何が新しい？

* offline-heavy / online-light な **two-stage** 設計で、実運用に向いた PTZ calibration にした点。
* translation を持たない PTZ 特性に合わせて、ray landmark ベースの incremental bundle adjustment を作った点。
* local calibration だけでなく georeferencing まで視野に入れている点。

## どうやってる？

* offline では、最低 zoom で 360 度をカバーする reference images を集め、SuperPoint / SuperGlue で feature tracks を構築する。
* track を ray landmark としてまとめ、PTZ-IBA と global BA で camera parameters を最適化する。
* online では、新しい viewpoint を relocalization 問題として解き、frustum overlap で reference candidates を絞る。
* 少数の 2D-3D annotation で local system を geographic frame へ写す georeferencing も行える。

## どこが強い？

* PTZ の実用運用をかなり意識した構成で、online stage を軽くしている。
* 内部パラメータや distortion までまとめて扱い、仮定を減らしている。
* synthetic だけでなく real data でも強く、feature matching 部分も modern pipeline を使って堅牢。

## 弱そうなところ

* offline stage の feature matching コストは重く、reference set が大きいと時間が伸びる。
* georeferencing には手注釈が必要で、完全自動ではない。
* principal point 固定など camera model 側の仮定が合わない特殊レンズでは厳しいかもしれない。

## 関連研究との違い

* 既存 PTZ calibration は known initial pose や rotation-only などの仮定を置くものが多い。
* 学習ベース手法と違い、幾何と BA を主軸にしていて汎化性を狙っている。
* 本手法は calibration だけでなく online relocalization と地理座標合わせまでつないでいるのが特徴。

## non-AIとして見る価値

* calibration を「一回の最適化」でなく、offline asset 構築と online inference に分ける設計が勉強になる。
* 実システムで効く camera calibration の組み立て方として、かなり実務的。

## 難易度

★★★☆☆

## 自分の理解/感想

* calibration 論文としてかなりバランスが良く、theory と system design の距離が近い。
* PTZ を扱う監視・放送・ロボット視覚で、そのまま参考にしやすいタイプの論文だと思う。
