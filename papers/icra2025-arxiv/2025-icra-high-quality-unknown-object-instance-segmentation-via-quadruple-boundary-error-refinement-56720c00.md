# High-Quality Unknown Object Instance Segmentation Via Quadruple Boundary Error Refinement

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Manipulation 2 |
| arXiv | [http://arxiv.org/abs/2306.16132](http://arxiv.org/abs/2306.16132) |
| Authors | Back, Seunghyeok;Lee, Sangbeom;Kim, Kangmin;Lee, Joosoon;Shin, Sungho;Maeng, Jemo;Lee, Kyoobin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Accurate and efficient segmentation of unknown objects in unstructured environments is essential for robotic manipulation.
- Unknown Object Instance Segmentation (UOIS), which aims to identify all objects in unknown categories and backgrounds, has become a key capability for various robotic tasks.
- However, existing methods struggle with over-segmentation and under-segmentation, leading to failures in manipulation tasks such as grasping.

## Task

* Manipulation
* Perception
* Software Tools

## Keywords

* Object Detection
* Segmentation and Categorization
* Deep Learning for Visual Perception
* Perception for Grasping and Manipulation

## AI依存度

* Hybrid

## 何を解決？

* Accurate and efficient segmentation of unknown objects in unstructured environments is essential for robotic manipulation.

## 何が新しい？

* To address these challenges, we propose QuBER (Quadruple Boundary Error Refinement), a novel error-informed refinement approach for high-quality UOIS.

## どうやってる？

* However, existing methods struggle with over-segmentation and under-segmentation, leading to failures in manipulation tasks such as grasping.

## どこが強い？

* Extensive evaluations on three public benchmarks demonstrate that QuBER outperforms state-of-the-art methods and consistently improves various UOIS methods while maintaining a fast inference time of less than 0.1 seconds.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these challenges, we propose QuBER (Quadruple Boundary Error Refinement), a novel error-informed refinement approach for high-quality UOIS.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
