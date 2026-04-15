# SurgPLAN++: Universal Surgical Phase Localization Network for Online and Offline Inference

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception Systems |
| arXiv | [http://arxiv.org/abs/2409.12467](http://arxiv.org/abs/2409.12467) |
| Authors | Chen, Zhen;Luo, Xingjian;Wu, Jinlin;Bai, Long;Lei, Zhen;Ren, Hongliang;Ourselin, Sebastien;Liu, Hongbin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Surgical phase recognition is critical for assisting surgeons in understanding surgical videos.
- Existing studies focused more on online surgical phase recognition, by leveraging preceding frames to predict the current frame.
- Despite great progress, they formulated the task as a series of frame-wise classification, which resulted in a lack of global context of the entire procedure and incoherent predictions.

## Task

* Localization
* Perception
* Medical Robotics

## Keywords

* Recognition
* Visual Learning
* Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* Surgical phase recognition is critical for assisting surgeons in understanding surgical videos.

## 何が新しい？

* To overcome these challenges and enhance both online and offline inference capabilities, we propose a universal Surgical Phase Localization Network, named SurgPLAN++, with the principle of temporal detection.

## どうやってる？

* We perform extensive experiments to validate the effectiveness, and our SurgPLAN++ achieves remarkable performance in both online and offline modes, which outperforms state-of-the-art methods.

## どこが強い？

* We perform extensive experiments to validate the effectiveness, and our SurgPLAN++ achieves remarkable performance in both online and offline modes, which outperforms state-of-the-art methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To overcome these challenges and enhance both online and offline inference capabilities, we propose a universal Surgical Phase Localization Network, named SurgPLAN++, with the principle of temporal detection.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
