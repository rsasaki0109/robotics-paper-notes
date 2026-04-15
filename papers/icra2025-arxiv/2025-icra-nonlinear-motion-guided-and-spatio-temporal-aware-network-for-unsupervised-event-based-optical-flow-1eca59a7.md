# Nonlinear Motion-Guided and Spatio-Temporal Aware Network for Unsupervised Event-Based Optical Flow

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception 2 |
| arXiv | [http://arxiv.org/abs/2505.05089](http://arxiv.org/abs/2505.05089) |
| Authors | Liu, Zuntao;Zhuang, Hao;Jiang, Junjie;Song, Yuhang;Fang, Zheng |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Event cameras have the potential to capture continuous motion information over time and space, making them well-suited for optical flow estimation.
- However, most existing learning-based methods for event-based optical flow adopt frame-based techniques, ignoring the spatio-temporal characteristics of events.
- Additionally, these methods assume linear motion between consecutive events within the loss time window, which increases optical flow errors in long-time sequences.

## Task

* Perception
* Software Tools

## Keywords

* Computer Vision for Transportation
* Visual Learning
* Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* Event cameras have the potential to capture continuous motion information over time and space, making them well-suited for optical flow estimation.

## 何が新しい？

* Therefore, we propose E-NMSTFlow, a novel unsupervised event-based optical flow network focusing on long-time sequences.

## どうやってる？

* However, most existing learning-based methods for event-based optical flow adopt frame-based techniques, ignoring the spatio-temporal characteristics of events.

## どこが強い？

* Extensive experiments demonstrate the effectiveness and superiority of our method.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Therefore, we propose E-NMSTFlow, a novel unsupervised event-based optical flow network focusing on long-time sequences.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
