# AiSDF: Structure-Aware Neural Signed Distance Fields in Indoor Scenes

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Deep Learning for Visual Perception 1 |
| arXiv | [http://arxiv.org/abs/2403.01861](http://arxiv.org/abs/2403.01861) |
| Authors | Jang, Jaehoon, Lee, Inha, Kim, Minje, Joo, Kyungdon |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Indoor scenes we are living in are visually homogenous or textureless, while they inherently have structural forms and provide enough structural priors for 3D scene reconstruction.
- Motivated by this fact, we propose a structure-aware online signed distance fields (SDF) reconstruction framework in indoor scenes, especially under the Atlanta world (AW) assumption.
- We evaluate the proposed AiSDF on the ScanNet and ReplicaCAD datasets, where we demonstrate that the proposed framework is capable of reconstructing fine details of objects implicitly, as well as structures explicitly in room-scale scenes.

## Task

* Mapping
* Perception

## Keywords

* Deep Learning for Visual Perception / Mapping / Incremental Learning

## AI依存度

* Hybrid

## 何を解決？

* Indoor scenes we are living in are visually homogenous or textureless, while they inherently have structural forms and provide enough structural priors for 3D scene reconstruction.

## 何が新しい？

* Motivated by this fact, we propose a structure-aware online signed distance fields (SDF) reconstruction framework in indoor scenes, especially under the Atlanta world (AW) assumption.

## どうやってる？

* Within the online framework, we infer the underlying Atlanta structure of a given scene and then estimate planar surfel regions supporting the Atlanta structure.

## どこが強い？

* We evaluate the proposed AiSDF on the ScanNet and ReplicaCAD datasets, where we demonstrate that the proposed framework is capable of reconstructing fine details of objects implicitly, as well as structures explicitly in room-scale scenes.

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
* どのモジュールに効くか: map / localization, perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
