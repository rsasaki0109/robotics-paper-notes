# Co-MTP: A Cooperative Trajectory Prediction Framework with Multi-Temporal Fusion for Autonomous Driving

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Tracking and Prediction 1 |
| arXiv | [http://arxiv.org/abs/2502.16589](http://arxiv.org/abs/2502.16589) |
| Authors | Zhang, Xinyu, Zhou, Zewei, Wang, Zaoyi, Ji, Yangjie, Huang, Yanjun, Chen, Hong |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we introduce the Co-MTP, a general cooperative trajectory prediction framework with multi-temporal fusion for autonomous driving, which leverages the V2X system to fully capture the interaction among agents in both history and future domains to benefit the planning.
- In the history domain, V2X can complement the incomplete history trajectory in single-vehicle perception, and we design a heterogeneous graph transformer to learn the fusion of the history feature from multiple agents and capture the history interaction.
- Thus, in the future domain, V2X can provide the prediction results of surrounding objects, and we further extend the graph transformer to capture the future interaction among the ego planning and the other vehicles' intentions and obtain the final future scenario state under a certain planning action.

## Task

* Perception
* Sensor Fusion
* Motion Planning
* Intelligent Vehicles

## Keywords

* Computer Vision for Transportation / Sensor Fusion / Deep Learning Methods

## AI依存度

* AI-heavy

## 何を解決？

* Vehicle-to-everything technologies (V2X) have become an ideal paradigm to extend the perception range and see through the occlusion.

## 何が新しい？

* In this paper, we introduce the Co-MTP, a general cooperative trajectory prediction framework with multi-temporal fusion for autonomous driving, which leverages the V2X system to fully capture the interaction among agents in both history and future domains to benefit the planning.

## どうやってる？

* In the history domain, V2X can complement the incomplete history trajectory in single-vehicle perception, and we design a heterogeneous graph transformer to learn the fusion of the history feature from multiple agents and capture the history interaction.

## どこが強い？

* Thus, in the future domain, V2X can provide the prediction results of surrounding objects, and we further extend the graph transformer to capture the future interaction among the ego planning and the other vehicles' intentions and obtain the final future scenario state under a certain planning action.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
