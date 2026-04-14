# SurgPose: Generalisable Surgical Instrument Pose Estimation Using Zero-Shot Learning and Stereo Vision

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Surgical Robotics: Laparoscopy |
| arXiv | [http://arxiv.org/abs/2505.11439](http://arxiv.org/abs/2505.11439) |
| Authors | Rai, Utsav, Xu, Haozheng, Giannarou, Stamatia |
| Source | ICRA 2025 / arXiv |

## TL;DR

- While traditional marker-based methods offer accuracy, they face challenges with occlusions, reflections, and tool-specific designs.
- Accurate pose estimation of surgical tools in Robot-assisted Minimally Invasive Surgery (RMIS) is essential for surgical navigation and robot control.
- Similarly, supervised learning methods require extensive training on annotated datasets, limiting their adaptability to new tools.

## Task

* Localization
* Perception
* Control

## Keywords

* Surgical Robotics: Laparoscopy / Localization / Visual Tracking

## AI依存度

* AI-heavy

## 何を解決？

* While traditional marker-based methods offer accuracy, they face challenges with occlusions, reflections, and tool-specific designs.

## 何が新しい？

* This paper presents a novel 6 Degrees of Freedom (DoF) pose estimation pipeline for surgical instruments, leveraging state-of-the-art zero-shot RGB-D models like the FoundationPose and SAM-6D.

## どうやってる？

* Accurate pose estimation of surgical tools in Robot-assisted Minimally Invasive Surgery (RMIS) is essential for surgical navigation and robot control.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

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
