# Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-Driven Surface Normal-Aware Tracking and Mapping

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Medical Robotics |
| arXiv | [http://arxiv.org/abs/2501.19319](http://arxiv.org/abs/2501.19319) |
| Authors | Huang, Yiming;Cui, Beilei;Bai, Long;Chen, Zhen;Wu, Jinlin;Li, Zhen;Liu, Hongbin;Ren, Hongliang |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Simultaneous Localization and Mapping (SLAM) is essential for precise surgical interventions and robotic tasks in minimally invasive procedures.
- While recent advancements in 3D Gaussian Splatting (3DGS) have improved SLAM with high-quality novel view synthesis and fast rendering, these systems struggle with accurate depth and surface reconstruction due to multi-view inconsistencies.
- Simply incorporating SLAM and 3DGS leads to mismatches between the reconstructed frames.

## Task

* SLAM
* Localization
* Visual-Inertial
* Perception

## Keywords

* SLAM
* Surgical Robotics: Laparoscopy
* Computer Vision for Medical Robotics

## AI依存度

* AI-heavy

## 何を解決？

* Simultaneous Localization and Mapping (SLAM) is essential for precise surgical interventions and robotic tasks in minimally invasive procedures.

## 何が新しい？

* In this work, we present Endo-2DTAM, a real-time endoscopic SLAM system with 2D Gaussian Splatting (2DGS) to address these challenges.

## どうやってる？

* Simultaneous Localization and Mapping (SLAM) is essential for precise surgical interventions and robotic tasks in minimally invasive procedures.

## どこが強い？

* Extensive experiments on public endoscopic datasets demonstrate that Endo-2DTAM achieves an RMSE of 1.87±0.63 mm for depth reconstruction of surgical scenes while maintaining computationally efficient tracking, high-quality visual appearance, and real-time rendering.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this work, we present Endo-2DTAM, a real-time endoscopic SLAM system with 2D Gaussian Splatting (2DGS) to address these challenges.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
