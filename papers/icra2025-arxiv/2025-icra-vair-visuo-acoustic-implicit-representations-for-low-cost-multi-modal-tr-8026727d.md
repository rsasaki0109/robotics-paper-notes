# VAIR: Visuo-Acoustic Implicit Representations for Low-Cost, Multi-Modal Transparent Surface Reconstruction in Indoor Scenes

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Sensor Fusion 1 |
| arXiv | [http://arxiv.org/abs/2411.04963](http://arxiv.org/abs/2411.04963) |
| Authors | Venkatramanan Sethuraman, Advaith, Bagoren, Onur, Seetharaman, Harikrishnan, Richardson, Dalton, Taylor, Joseph, Skinner, Katherine |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper proposes a novel method for the fusion of acoustic and visual sensing modalities through implicit neural represen- tations to enable dense reconstruction of transparent surfaces in indoor scenes.
- We propose a novel model that leverages generative latent optimization to learn an implicit representation of indoor scenes consisting of transparent surfaces.
- We demonstrate that we can query the implicit representation to enable volumetric rendering in image space or 3D geometry reconstruction (point clouds or mesh) with transparent surface prediction.

## Task

* Perception
* Sensor Fusion

## Keywords

* RGB-D Perception / Deep Learning for Visual Perception / Sensor Fusion

## AI依存度

* Hybrid

## 何を解決？

* Mobile robots operating indoors must be prepared to navigate challenging scenes that contain transparent surfaces.

## 何が新しい？

* This paper proposes a novel method for the fusion of acoustic and visual sensing modalities through implicit neural represen- tations to enable dense reconstruction of transparent surfaces in indoor scenes.

## どうやってる？

* We propose a novel model that leverages generative latent optimization to learn an implicit representation of indoor scenes consisting of transparent surfaces.

## どこが強い？

* We demonstrate that we can query the implicit representation to enable volumetric rendering in image space or 3D geometry reconstruction (point clouds or mesh) with transparent surface prediction.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: perception, perception / localization fusion
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
