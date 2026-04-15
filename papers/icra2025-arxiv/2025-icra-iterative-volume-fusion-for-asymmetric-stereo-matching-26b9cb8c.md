# Iterative Volume Fusion for Asymmetric Stereo Matching

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Deep Learning for Visual Perception 3 |
| arXiv | [http://arxiv.org/abs/2508.09543](http://arxiv.org/abs/2508.09543) |
| Authors | Gao, Yuanting;Shen, Linghao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Stereo matching is vital in 3D computer vision, with most algorithms assuming symmetric visual properties between binocular visions.
- However, the rise of asymmetric multi-camera systems (e.g., tele-wide cameras) challenges this assumption and complicates stereo matching.
- Visual asymmetry disrupts stereo matching by affecting the crucial cost volume computation.

## Task

* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* Computer Vision for Transportation
* AI-Based Methods

## AI依存度

* Hybrid

## 何を解決？

* Stereo matching is vital in 3D computer vision, with most algorithms assuming symmetric visual properties between binocular visions.

## 何が新しい？

* Based on this, we propose the two-phase Iterative Volume Fusion network for Asymmetric Stereo matching (IVF-AStereo).

## どうやってる？

* To address this, we explore the matching cost distribution of two established cost volume construction methods in asymmetric stereo.

## どこが強い？

* Extensive comparative experiments on benchmark datasets, along with ablation studies, confirm the effectiveness of our approach in asymmetric stereo with resolution and color degradation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Based on this, we propose the two-phase Iterative Volume Fusion network for Asymmetric Stereo matching (IVF-AStereo).

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
