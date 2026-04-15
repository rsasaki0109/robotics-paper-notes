# Environment As Policy: Learning to Race in Unseen Tracks

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Learning 1 |
| arXiv | [http://arxiv.org/abs/2410.22308](http://arxiv.org/abs/2410.22308) |
| Authors | Wang, Hongze;Xing, Jiaxu;Messikommer, Nico;Scaramuzza, Davide |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Reinforcement learning (RL) has achieved outstanding success in complex robot control tasks, such as drone racing, where the RL agents have outperformed human champions in a known racing track.
- However, these agents fail in unseen track configurations, always requiring complete retraining when presented with new track layouts.
- This work aims to develop RL agents that generalize effectively to novel track configurations without retraining.

## Task

* Visual-Inertial
* Control
* Aerial Robotics
* Perception

## Keywords

* Aerial Systems: Perception and Autonomy
* Reinforcement Learning
* AI-Enabled Robotics

## AI依存度

* Hybrid

## 何を解決？

* Reinforcement learning (RL) has achieved outstanding success in complex robot control tasks, such as drone racing, where the RL agents have outperformed human champions in a known racing track.

## 何が新しい？

* To enhance the generalizability of the RL agent, we propose an adaptive environment-shaping framework that dynamically adjusts the training environment based on the agents performance.

## どうやってる？

* Experimental results validated in both simulation and the real world show that our method enables drones to successfully fly complex and unseen race tracks, outperforming existing environment-shaping techniques.

## どこが強い？

* Experimental results validated in both simulation and the real world show that our method enables drones to successfully fly complex and unseen race tracks, outperforming existing environment-shaping techniques.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To enhance the generalizability of the RL agent, we propose an adaptive environment-shaping framework that dynamically adjusts the training environment based on the agents performance.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
