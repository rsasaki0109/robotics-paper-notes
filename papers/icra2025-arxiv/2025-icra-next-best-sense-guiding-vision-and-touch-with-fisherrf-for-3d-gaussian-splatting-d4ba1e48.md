# Next Best Sense: Guiding Vision and Touch with FisherRF for 3D Gaussian Splatting

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Radiance Fields for Manipulation |
| arXiv | [http://arxiv.org/abs/2410.04680](http://arxiv.org/abs/2410.04680) |
| Authors | Strong, Matthew;Lei, Boshu;Swann, Aiden;Jiang, Wen;Daniilidis, Kostas;Kennedy, Monroe |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We propose a framework for active next best view and touch selection for robotic manipulators using 3D Gaussian Splatting (3DGS).
- 3DGS is emerging as a useful explicit 3D scene representation for robotics, as it has the ability to represent scenes in a both photorealistic and geometrically accurate manner.
- However, in real-world, online robotic scenes where the number of views is limited given efficiency requirements, random view selection for 3DGS becomes impractical as views are often overlapping and redundant.

## Task

* Manipulation
* Perception

## Keywords

* Perception for Grasping and Manipulation
* Reactive and Sensor-Based Planning
* Semantic Scene Understanding

## AI依存度

* AI-heavy

## 何を解決？

* We propose a framework for active next best view and touch selection for robotic manipulators using 3D Gaussian Splatting (3DGS).

## 何が新しい？

* We propose a framework for active next best view and touch selection for robotic manipulators using 3D Gaussian Splatting (3DGS).

## どうやってる？

* We first elevate the performance of few-shot 3DGS with a novel semantic depth alignment method using Segment Anything Model 2 (SAM2) that we supplement with Pearson depth and surface normal loss to improve color and depth reconstruction of real-world scenes.

## どこが強い？

* We motivate our improvements to few-shot GS scenes, and extend depth-based FisherRF to them, where we demonstrate both qualitative and quantitative improvements on challenging robot scenes.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a framework for active next best view and touch selection for robotic manipulators using 3D Gaussian Splatting (3DGS).

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
