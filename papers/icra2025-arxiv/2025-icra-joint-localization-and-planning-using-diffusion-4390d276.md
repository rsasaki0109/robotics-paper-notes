# Joint Localization and Planning Using Diffusion

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Diffusion for Manipulation |
| arXiv | [http://arxiv.org/abs/2409.17995](http://arxiv.org/abs/2409.17995) |
| Authors | Lao Beyer, Lukas;Karaman, Sertac |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Diffusion models have been successfully applied to robotics problems such as manipulation and vehicle path planning.
- In this work, we explore their application to end-to-end navigation -- including both perception and planning -- by considering the problem of jointly performing global localization and path planning in known but arbitrary 2D environments.
- In particular, we introduce a diffusion model which produces collision-free paths in a global reference frame given an egocentric LIDAR scan, an arbitrary map, and a desired goal position.

## Task

* Localization
* LiDAR
* Visual-Inertial
* Motion Planning

## Keywords

* Deep Learning Methods
* Localization
* Autonomous Vehicle Navigation

## AI依存度

* AI-heavy

## 何を解決？

* Diffusion models have been successfully applied to robotics problems such as manipulation and vehicle path planning.

## 何が新しい？

* In our evaluation, we show that the proposed conditioning techniques enable generalization to realistic maps of considerably different appearance than the training environment, demonstrate our model's ability to accurately describe ambiguous solutions, and run extensive simulation experiments showcasing our model's use as a real-time, end-to-end localization and planning stack.

## どうやってる？

* Diffusion models have been successfully applied to robotics problems such as manipulation and vehicle path planning.

## どこが強い？

* In our evaluation, we show that the proposed conditioning techniques enable generalization to realistic maps of considerably different appearance than the training environment, demonstrate our model's ability to accurately describe ambiguous solutions, and run extensive simulation experiments showcasing our model's use as a real-time, end-to-end localization and planning stack.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In our evaluation, we show that the proposed conditioning techniques enable generalization to realistic maps of considerably different appearance than the training environment, demonstrate our model's ability to accurately describe ambiguous solutions, and run extensive simulation experiments showcasing our model's use as a real-time, end-to-end localization and planning stack.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
