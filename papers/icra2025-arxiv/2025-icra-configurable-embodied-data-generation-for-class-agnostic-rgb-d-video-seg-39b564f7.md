# Configurable Embodied Data Generation for Class-Agnostic RGB-D Video Segmentation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Deep Learning for Visual Perception 1 |
| arXiv | [http://arxiv.org/abs/2410.12995](http://arxiv.org/abs/2410.12995) |
| Authors | Opipari, Anthony, Krishnan, Aravindhan, Gayaka, Shreekant, Sun, Min, Kuo, Cheng-Hao, Sen, Arnab, Jenkins, Odest Chadwicke |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper presents a method for generating large-scale datasets to improve class-agnostic video segmentation across robots with different form factors.
- Specifically, we consider the question of whether video segmentation models trained on generic segmentation data could be more effective for particular robot platforms if robot embodiment is factored into the data generation process.
- Our experimental findings demonstrate that using MVPd for finetuning can lead to performance improvements when transferring foundation models to certain robot embodiments, such as specific camera placements.

## Task

* Mapping
* Perception

## Keywords

* Object Detection / Segmentation and Categorization / Data Sets for Robotic Vision / RGB-D Perception

## AI依存度

* AI-heavy

## 何を解決？

* This paper presents a method for generating large-scale datasets to improve class-agnostic video segmentation across robots with different form factors.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* A resulting massive RGB-D video panoptic segmentation dataset (MVPd) is introduced for extensive benchmarking with foundation and video segmentation models, as well as to support embodiment-focused research in video segmentation.

## どこが強い？

* Our experimental findings demonstrate that using MVPd for finetuning can lead to performance improvements when transferring foundation models to certain robot embodiments, such as specific camera placements.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
