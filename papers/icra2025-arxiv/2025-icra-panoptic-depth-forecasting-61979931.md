# Panoptic-Depth Forecasting

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 4 |
| arXiv | [http://arxiv.org/abs/2409.12008](http://arxiv.org/abs/2409.12008) |
| Authors | Juana Valeria, Hurtado, Mohan, Riya, Valada, Abhinav |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Extensive evaluations demonstrate the effectiveness of netname across two datasets and three forecasting tasks, consistently addressing the primary challenges.
- In this work, we propose the panoptic-depth forecasting task for jointly predicting future panoptic segmentation and depth maps from monocular camera images.
- Forecasting the semantics and 3D structure of scenes is essential for robots to navigate and plan actions safely.

## Task

* LiDAR
* Perception
* Intelligent Vehicles

## Keywords

* Deep Learning for Visual Perception / RGB-D Perception / Visual Learning

## AI依存度

* AI-heavy

## 何を解決？

* Extensive evaluations demonstrate the effectiveness of netname across two datasets and three forecasting tasks, consistently addressing the primary challenges.

## 何が新しい？

* In this work, we propose the panoptic-depth forecasting task for jointly predicting future panoptic segmentation and depth maps from monocular camera images.

## どうやってる？

* Furthermore, we present two baselines and propose the novel netname architecture that learns rich spatio-temporal representations by incorporating a transformer-based encoder, a forecasting module, and task-specific decoders to predict future panoptic-depth outputs.

## どこが強い？

* Extensive evaluations demonstrate the effectiveness of netname across two datasets and three forecasting tasks, consistently addressing the primary challenges.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* Furthermore, we present two baselines and propose the novel netname architecture that learns rich spatio-temporal representations by incorporating a transformer-based encoder, a forecasting module, and task-specific decoders to predict future panoptic-depth outputs.

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: sensing / localization / perception, perception, planning / control / perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
