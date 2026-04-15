# Single-Shot Metric Depth from Focused Plenoptic Cameras

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Deep Learning for Visual Perception 2 |
| arXiv | [http://arxiv.org/abs/2412.02386](http://arxiv.org/abs/2412.02386) |
| Authors | Lasheras-Hernandez, Blanca;Strobl, Klaus H.;Izquierdo, Sergio;Bodenmueller, Tim;Triebel, Rudolph;Civera, Javier |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Metric depth estimation from visual sensors is crucial for robots to perceive, navigate, and interact with their environment.
- Traditional range imaging setups, such as stereo or structured light cameras, face hassles including calibration, occlusions, and hardware demands, with accuracy limited by the baseline between cameras.
- Single- and multiview monocular depth offers a more compact alternative, but is constrained by the unobservability of the metric scale.

## Task

* LiDAR
* Calibration
* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* Data Sets for Robotic Vision

## AI依存度

* Hybrid

## 何を解決？

* Metric depth estimation from visual sensors is crucial for robots to perceive, navigate, and interact with their environment.

## 何が新しい？

* We propose a novel pipeline that predicts metric depth from a single plenoptic camera shot by first generating a sparse metric point cloud using a neural network, which is then used to scale and align a dense relative depth map regressed by a foundation depth model, resulting in a dense metric depth.

## どうやってる？

* However, its application to single-view dense metric depth is under-addressed mainly due to the technologys high cost, the lack of public benchmarks, and proprietary geometrical models and software.

## どこが強い？

* Experimental results show that our pipeline produces accurate metric depth predictions, laying a solid groundwork for future research in this field.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a novel pipeline that predicts metric depth from a single plenoptic camera shot by first generating a sparse metric point cloud using a neural network, which is then used to scale and align a dense relative depth map regressed by a foundation depth model, resulting in a dense metric depth.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
