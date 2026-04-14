# PROBE: Proprioceptive Obstacle Detection and Estimation While Navigating in Clutter

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Identifcation and Estimation for Legged Robots |
| arXiv | [http://arxiv.org/abs/2505.11848](http://arxiv.org/abs/2505.11848) |
| Authors | Metha Ramesh, Dhruv, Sivaramakrishnan, Aravind, Keskar, Shreesh, Bekris, Kostas E., Yu, Jingjin, Boularias, Abdeslam |
| Source | ICRA 2025 / arXiv |

## TL;DR

- To enable robots to tackle these challenges, we propose a new approach, Proprioceptive Obstacle Detection and Estimation while navigating in clutter (PROBE), which instead relies only on the robots proprioception to infer the presence or absence of occluded rectangular obstacles while predicting their dimensions and poses in SE(2).
- In critical applications, including search-and- rescue in degraded environments, blockages can be prevalent and prevent the effective deployment of certain sensing modalities, particularly vision, due to occlusion and the constrained range of view of onboard camera sensors.
- The proposed approach is a Transformer neural network that receives as input a history of applied torques and sensed whole-body movements of the robot and returns a parameterized representation of the obstacles in the environment.

## Task

* Mapping
* Perception
* Legged Robotics

## Keywords

* Legged Robots / Sensorimotor Learning / Mapping

## AI依存度

* AI-heavy

## 何を解決？

* To enable robots to tackle these challenges, we propose a new approach, Proprioceptive Obstacle Detection and Estimation while navigating in clutter (PROBE), which instead relies only on the robots proprioception to infer the presence or absence of occluded rectangular obstacles while predicting their dimensions and poses in SE(2).

## 何が新しい？

* To enable robots to tackle these challenges, we propose a new approach, Proprioceptive Obstacle Detection and Estimation while navigating in clutter (PROBE), which instead relies only on the robots proprioception to infer the presence or absence of occluded rectangular obstacles while predicting their dimensions and poses in SE(2).

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: map / localization, perception, limited direct use; estimator / controller design reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
