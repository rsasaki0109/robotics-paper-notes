# Tactile Functasets: Neural Implicit Representations of Tactile Datasets

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Radiance Fields for Manipulation |
| arXiv | [http://arxiv.org/abs/2409.14592](http://arxiv.org/abs/2409.14592) |
| Authors | Li, Sikai, Rodriguez, Samanta, Dou, Yiming, Owens, Andrew, Fazeli, Nima |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we introduce a novel representation for tactile sensor feedback based on neural implicit functions.
- Rather than directly using raw tactile images, we propose neural implicit functions trained to reconstruct the tactile dataset, producing compact neural representations that capture the underlying structure of the sensory inputs.
- We demonstrate the efficacy of this representation on the downstream task of in-hand object pose estimation, achieving improved performance over image-based methods while simplifying downstream models.

## Task

* Localization
* Perception
* Manipulation

## Keywords

* Deep Learning in Grasping and Manipulation / Perception for Grasping and Manipulation / Force and Tactile Sensing

## AI依存度

* Hybrid

## 何を解決？

* Modern incarnations of tactile sensors produce raw, high-dimensional data such as images, making it challenging to efficiently process and generalize across sensors.

## 何が新しい？

* In this paper, we introduce a novel representation for tactile sensor feedback based on neural implicit functions.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* We demonstrate the efficacy of this representation on the downstream task of in-hand object pose estimation, achieving improved performance over image-based methods while simplifying downstream models.

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
* どのモジュールに効くか: localization, perception, limited direct use; integration pattern reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
