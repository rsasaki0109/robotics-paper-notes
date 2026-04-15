# Deformable Gaussian Splatting for Efficient and High-Fidelity Reconstruction of Surgical Scenes

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Deformable Objects |
| arXiv | [http://arxiv.org/abs/2501.01101](http://arxiv.org/abs/2501.01101) |
| Authors | Shan, Jiwei;Cai, Zeyu;Hsieh, Cheng-Tai;Han, Lijun;Cheng, Shing Shin;Wang, Hesheng |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Efficient and high-fidelity reconstruction of deformable surgical scenes is a critical yet challenging task.
- Building on recent advancements in 3D Gaussian splatting, current methods have seen significant improvements in both reconstruction quality and rendering speed.
- However, two major limitations remain: (1) difficulty in handling irreversible dynamic changes, such as tissue shearing, which are common in surgical scenes; and (2) the lack of hierarchical modeling for surgical scene deformation, which reduces rendering speed.

## Task

* Perception
* Medical Robotics
* Software Tools

## Keywords

* Computer Vision for Medical Robotics
* Surgical Robotics: Laparoscopy

## AI依存度

* AI-heavy

## 何を解決？

* Efficient and high-fidelity reconstruction of deformable surgical scenes is a critical yet challenging task.

## 何が新しい？

* We propose a deformation modeling approach that incorporates the life cycle of 3D Gaussians, effectively capturing both regular and irreversible deformations, thus enhancing reconstruction quality.

## どうやってる？

* Building on recent advancements in 3D Gaussian splatting, current methods have seen significant improvements in both reconstruction quality and rendering speed.

## どこが強い？

* Extensive experiments on public datasets captured with static endoscopes demonstrate that our method surpasses existing state-of-the-art approaches in both reconstruction quality and rendering speed.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a deformation modeling approach that incorporates the life cycle of 3D Gaussians, effectively capturing both regular and irreversible deformations, thus enhancing reconstruction quality.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
