# Visuo-Tactile Object Pose Estimation for a Multi-Finger Robot Hand with Low-Resolution In-Hand Tactile Sensing

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Manipulation 1 |
| arXiv | [http://arxiv.org/abs/2503.19893](http://arxiv.org/abs/2503.19893) |
| Authors | Mack, Lukas;Grüninger, Felix;Richardson, Benjamin A.;Lendway, Regine;Kuchenbecker, Katherine J.;Stueckler, Joerg |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Accurate 3D pose estimation of grasped objects is an important prerequisite for robots to perform assembly or in-hand manipulation tasks, but object occlusion by the robot's own hand greatly increases the difficulty of this perceptual task.
- Here, we propose that combining visual information and proprioception with binary, low-resolution tactile contact measurements from across the interior surface of an articulated robotic hand can mitigate this issue.
- The visuo-tactile object-pose-estimation problem is formulated probabilistically in a factor graph.

## Task

* Visual-Inertial
* Manipulation
* Perception

## Keywords

* Perception for Grasping and Manipulation
* Sensor Fusion
* Force and Tactile Sensing

## AI依存度

* Non-AI

## 何を解決？

* Accurate 3D pose estimation of grasped objects is an important prerequisite for robots to perform assembly or in-hand manipulation tasks, but object occlusion by the robot's own hand greatly increases the difficulty of this perceptual task.

## 何が新しい？

* Here, we propose that combining visual information and proprioception with binary, low-resolution tactile contact measurements from across the interior surface of an articulated robotic hand can mitigate this issue.

## どうやってる？

* The advantages of the proposed approach are first demonstrated in simulation: a custom 15-DoF robot hand with one binary tactile sensor per link grasps 17 YCB objects while observed by an RGB-D camera.

## どこが強い？

* The advantages of the proposed approach are first demonstrated in simulation: a custom 15-DoF robot hand with one binary tactile sensor per link grasps 17 YCB objects while observed by an RGB-D camera.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Here, we propose that combining visual information and proprioception with binary, low-resolution tactile contact measurements from across the interior surface of an articulated robotic hand can mitigate this issue.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
