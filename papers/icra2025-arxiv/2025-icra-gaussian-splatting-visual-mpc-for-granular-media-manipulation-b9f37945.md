# Gaussian Splatting Visual MPC for Granular Media Manipulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Radiance Fields for Manipulation |
| arXiv | [http://arxiv.org/abs/2410.09740](http://arxiv.org/abs/2410.09740) |
| Authors | Tseng, Wei-Cheng, Zhang, Ellina, Jatavallabhula, Krishna Murthy, Shkurti, Florian |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recent advancements in learned 3D representations have enabled significant progress in solving complex robotic manipulation tasks, particularly for rigid-body objects.
- In this work, we propose a novel approach that learns a visual dynamics model over Gaussian splatting representations of scenes and leverages this model for manipulating granular media via Model-Predictive Control.
- We evaluate our approach in both simulated and real-world settings, demonstrating its ability to solve unseen planning tasks and generalize to new environments in a zero-shot transfer.

## Task

* Motion Planning
* Control
* Manipulation

## Keywords

* Manipulation Planning / AI-Based Methods / AI-Enabled Robotics

## AI依存度

* AI-heavy

## 何を解決？

* Recent advancements in learned 3D representations have enabled significant progress in solving complex robotic manipulation tasks, particularly for rigid-body objects.

## 何が新しい？

* In this work, we propose a novel approach that learns a visual dynamics model over Gaussian splatting representations of scenes and leverages this model for manipulating granular media via Model-Predictive Control.

## どうやってる？

* Recent advancements in learned 3D representations have enabled significant progress in solving complex robotic manipulation tasks, particularly for rigid-body objects.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* We also show significant prediction and manipulation performance improvements compared to existing granular media manipulation methods.

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: planning, control, limited direct use; integration pattern reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
