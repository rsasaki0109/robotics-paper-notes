# Boosting Cross-Spectral Unsupervised Domain Adaptation for Thermal Semantic Segmentation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Image and 3D Segmentation 1 |
| arXiv | [http://arxiv.org/abs/2505.06951](http://arxiv.org/abs/2505.06951) |
| Authors | Kwon, SeokJun;Shin, Jeongmin;Kim, Namil;Hwang, Soonmin;Choi, Yukyung |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In autonomous driving, thermal image semantic segmentation has emerged as a critical research area, owing to its ability to provide robust scene understanding under adverse visual conditions.
- In particular, unsupervised domain adaptation (UDA) for thermal image segmentation can be an efficient solution to address the lack of labeled thermal datasets.
- Nevertheless, since these methods do not effectively utilize the complementary information between RGB and thermal images, they significantly decrease performance during domain adaptation.

## Task

* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* Deep Learning Methods
* Recognition

## AI依存度

* Hybrid

## 何を解決？

* In autonomous driving, thermal image semantic segmentation has emerged as a critical research area, owing to its ability to provide robust scene understanding under adverse visual conditions.

## 何が新しい？

* We first propose a novel masked mutual learning strategy that promotes complementary information exchange by selectively transferring results between each spectral model while masking out uncertain regions.

## どうやってる？

* Nevertheless, since these methods do not effectively utilize the complementary information between RGB and thermal images, they significantly decrease performance during domain adaptation.

## どこが強い？

* In experiments, our method achieves higher performance over previous UDA methods and comparable performance to state-of-the-art supervised methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We first propose a novel masked mutual learning strategy that promotes complementary information exchange by selectively transferring results between each spectral model while masking out uncertain regions.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
