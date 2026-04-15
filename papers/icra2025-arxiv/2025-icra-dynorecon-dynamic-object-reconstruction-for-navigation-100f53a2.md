# DynORecon: Dynamic Object Reconstruction for Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Robot Mapping 2 |
| arXiv | [http://arxiv.org/abs/2409.19928](http://arxiv.org/abs/2409.19928) |
| Authors | Wang, Yiduo;Morris, Jesse;Wu, Lan;Vidal-Calleja, Teresa A.;Ila, Viorela |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper presents DynORecon, a Dynamic Object Reconstruction system that leverages the information provided by Dynamic SLAM to simultaneously generate a volumetric map of observed moving entities while estimating free space to support navigation.
- By capitalising on the motion estimations provided by Dynamic SLAM, DynORecon continuously refines the representation of dynamic objects to eliminate residual artefacts from past observations and incrementally reconstructs each object, seamlessly integrating new observations to capture previously unseen structures.
- Our system is highly efficient (�?0 FPS) and produces accurate (�?0 cm) object reconstructions using simulated and real-world outdoor datasets.

## Task

* SLAM
* Visual-Inertial
* Motion Planning
* Perception

## Keywords

* Mapping
* Vision-Based Navigation
* Motion and Path Planning

## AI依存度

* Non-AI

## 何を解決？

* This paper presents DynORecon, a Dynamic Object Reconstruction system that leverages the information provided by Dynamic SLAM to simultaneously generate a volumetric map of observed moving entities while estimating free space to support navigation.

## 何が新しい？

* This paper presents DynORecon, a Dynamic Object Reconstruction system that leverages the information provided by Dynamic SLAM to simultaneously generate a volumetric map of observed moving entities while estimating free space to support navigation.

## どうやってる？

* This paper presents DynORecon, a Dynamic Object Reconstruction system that leverages the information provided by Dynamic SLAM to simultaneously generate a volumetric map of observed moving entities while estimating free space to support navigation.

## どこが強い？

* This paper presents DynORecon, a Dynamic Object Reconstruction system that leverages the information provided by Dynamic SLAM to simultaneously generate a volumetric map of observed moving entities while estimating free space to support navigation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This paper presents DynORecon, a Dynamic Object Reconstruction system that leverages the information provided by Dynamic SLAM to simultaneously generate a volumetric map of observed moving entities while estimating free space to support navigation.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
