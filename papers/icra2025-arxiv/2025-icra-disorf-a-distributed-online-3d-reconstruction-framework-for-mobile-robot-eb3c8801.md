# DISORF: A Distributed Online 3D Reconstruction Framework for Mobile Robots

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Mobile Robots 1 |
| arXiv | [http://arxiv.org/abs/2403.00228](http://arxiv.org/abs/2403.00228) |
| Authors | Li, Chunlin, Fan, Hanrui, Huang, Xiaorui, Liang, Ruofan, Durvasula, Sankeerth, Vijaykumar, Nandita |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We identify a key challenge with online training where naive image sampling strategies can lead to significant degradation in rendering quality.
- We present a framework, DISORF, to enable online 3D reconstruction and visualization of scenes captured by resource-constrained mobile robots and edge devices.
- We demonstrate the effectiveness of our framework in enabling high-quality real-time reconstruction and visualization of unknown scenes as they are captured and streamed from cameras in mobile robots and edge devices.

## Task

* SLAM
* Mapping
* Perception

## Keywords

* Visual Learning / Incremental Learning / Mapping

## AI依存度

* Hybrid

## 何を解決？

* We identify a key challenge with online training where naive image sampling strategies can lead to significant degradation in rendering quality.

## 何が新しい？

* We present a framework, DISORF, to enable online 3D reconstruction and visualization of scenes captured by resource-constrained mobile robots and edge devices.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* We demonstrate the effectiveness of our framework in enabling high-quality real-time reconstruction and visualization of unknown scenes as they are captured and streamed from cameras in mobile robots and edge devices.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: localization / mapping, map / localization, perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
