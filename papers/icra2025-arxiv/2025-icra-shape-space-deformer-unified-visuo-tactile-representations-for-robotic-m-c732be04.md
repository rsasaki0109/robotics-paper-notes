# Shape-Space Deformer: Unified Visuo-Tactile Representations for Robotic Manipulation of Deformable Objects

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Vision-Based Tactile Sensors 2 |
| arXiv | [http://arxiv.org/abs/2409.12419](http://arxiv.org/abs/2409.12419) |
| Authors | Collins, Sean Michael Varian, Tidd, Brendan, Baktashmotlagh, Mahsa, Moghadam, Peyman |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Accurate modeling of object deformations is crucial for a wide range of robotic manipulation tasks, where interacting with soft or deformable objects is essential.
- We propose Shape-Space Deformer, a unified representation for encoding a diverse range of object deformations using template augmentation to achieve robust, fine-grained reconstructions that are resilient to outliers and unwanted artifacts.
- We perform extensive experiments to test a range of force generalisation settings and evaluate our methods ability to reconstruct unseen deformations, demonstrating significant improvements in reconstruction accuracy and robustness.

## Task

* Perception
* Manipulation

## Keywords

* Perception for Grasping and Manipulation / Deep Learning in Grasping and Manipulation / Representation Learning

## AI依存度

* Hybrid

## 何を解決？

* Accurate modeling of object deformations is crucial for a wide range of robotic manipulation tasks, where interacting with soft or deformable objects is essential.

## 何が新しい？

* We propose Shape-Space Deformer, a unified representation for encoding a diverse range of object deformations using template augmentation to achieve robust, fine-grained reconstructions that are resilient to outliers and unwanted artifacts.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* We propose Shape-Space Deformer, a unified representation for encoding a diverse range of object deformations using template augmentation to achieve robust, fine-grained reconstructions that are resilient to outliers and unwanted artifacts.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Our method improves generalization to unseen forces and can rapidly adapt to novel objects, significantly outperforming existing approaches.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: perception, limited direct use; integration pattern reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
