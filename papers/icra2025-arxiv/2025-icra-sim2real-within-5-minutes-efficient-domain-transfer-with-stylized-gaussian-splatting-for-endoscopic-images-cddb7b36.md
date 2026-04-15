# Sim2Real within 5 Minutes: Efficient Domain Transfer with Stylized Gaussian Splatting for Endoscopic Images

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Medical Robotics |
| arXiv | [http://arxiv.org/abs/2403.10860](http://arxiv.org/abs/2403.10860) |
| Authors | Wu, Junyang;Gu, Yun;Yang, Guang-Zhong |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robot assisted endoluminal intervention is an emerging technique for both benign and malignant luminal lesions.
- With vision-based navigation, when combined with pre-operative imaging data as priors, it is possible to recover position and pose of the endoscope without the need of additional sensors.
- In practice, however, aligning pre-operative and intra-operative domains is complicated by significant texture differences.

## Task

* LiDAR
* Medical Robotics
* Software Tools

## Keywords

* Computer Vision for Medical Robotics
* Surgical Robotics: Laparoscopy
* Surgical Robotics: Planning

## AI依存度

* AI-heavy

## 何を解決？

* Robot assisted endoluminal intervention is an emerging technique for both benign and malignant luminal lesions.

## 何が新しい？

* This paper proposes an efficient domain transfer method based on stylized Gaussian splatting, only requiring a few of real images (10 images) with very fast training time.

## どうやってる？

* Although methods such as style transfer can be used to address this issue, they require large datasets from both source and target domains with prolonged training times.

## どこが強い？

* Detailed validation was performed to demonstrate the performance advantages of the proposed method compared to that of the current state-of-the-art, highlighting the potential for intra-operative surgical navigation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This paper proposes an efficient domain transfer method based on stylized Gaussian splatting, only requiring a few of real images (10 images) with very fast training time.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
