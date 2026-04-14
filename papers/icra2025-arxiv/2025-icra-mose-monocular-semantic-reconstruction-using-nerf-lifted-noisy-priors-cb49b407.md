# MOSE: Monocular Semantic Reconstruction Using NeRF-Lifted Noisy Priors

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Robot Mapping 1 |
| arXiv | [http://arxiv.org/abs/2409.14019](http://arxiv.org/abs/2409.14019) |
| Authors | Du, Zhenhua, Xu, Binbin, Zhang, Haoyu, Huo, Kai, Zhi, Shuaifeng |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we propose MOSE, a neural field semantic reconstruction approach to lift inferred image-level noisy priors to 3D, producing accurate semantics and geometry in both 3D and 2D space.
- The key motivation for our method is to leverage generic class-agnostic segment masks as guidance to promote local consistency of rendered semantics during training.
- Experiments on the ScanNet dataset show that our MOSE outperforms relevant baselines across all metrics on tasks of 3D semantic segmentation, 2D semantic segmentation and 3D surface reconstruction.

## Task

* Mapping
* Perception

## Keywords

* Semantic Scene Understanding / Representation Learning / Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* Accurately reconstructing dense and semantically annotated 3D meshes from monocular images remains a challenging task due to the lack of geometry guidance and imperfect view-dependent 2D priors.

## 何が新しい？

* In this paper, we propose MOSE, a neural field semantic reconstruction approach to lift inferred image-level noisy priors to 3D, producing accurate semantics and geometry in both 3D and 2D space.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* Experiments on the ScanNet dataset show that our MOSE outperforms relevant baselines across all metrics on tasks of 3D semantic segmentation, 2D semantic segmentation and 3D surface reconstruction.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Experiments on the ScanNet dataset show that our MOSE outperforms relevant baselines across all metrics on tasks of 3D semantic segmentation, 2D semantic segmentation and 3D surface reconstruction.

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
