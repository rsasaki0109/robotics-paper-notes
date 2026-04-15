# Safety-Critical Traffic Simulation with Adversarial Transfer of Driving Intentions

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Planning Around People for Social Navigation |
| arXiv | [http://arxiv.org/abs/2503.05180](http://arxiv.org/abs/2503.05180) |
| Authors | Huang, Zherui;Gao, Xing;Zheng, Guanjie;Wen, Licheng;Yang, Xuemeng;Sun, Xiao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Traffic simulation, complementing real-world data with a long-tail distribution, allows for effective evaluation and enhancement of the ability of autonomous vehicles to handle accident-prone scenarios.
- Simulating such safety-critical scenarios is nontrivial, however, from log data that are typically regular scenarios, especially in consideration of dynamic adversarial interactions between the future motions of autonomous vehicles and surrounding traffic participants.
- To address it, this paper proposes an innovative and efficient strategy, termed IntSim, that explicitly decouples the driving intentions of surrounding actors from their motion planning for realistic and efficient safety-critical simulation.

## Task

* Visual-Inertial
* Motion Planning
* Software Tools

## Keywords

* Collision Avoidance
* Intelligent Transportation Systems
* Deep Learning Methods

## AI依存度

* Hybrid

## 何を解決？

* Traffic simulation, complementing real-world data with a long-tail distribution, allows for effective evaluation and enhancement of the ability of autonomous vehicles to handle accident-prone scenarios.

## 何が新しい？

* To address it, this paper proposes an innovative and efficient strategy, termed IntSim, that explicitly decouples the driving intentions of surrounding actors from their motion planning for realistic and efficient safety-critical simulation.

## どうやってる？

* Simultaneously, intention-conditioned motion planning benefits from powerful deep models and large-scale real-world data, permitting the simulation of realistic motion behaviors for actors.

## どこが強い？

* Finally, extensive open-loop and closed-loop experiments on real-world datasets, including nuScenes and Waymo, demonstrate that the proposed IntSim achieves state-of-the-art performance in simulating realistic safety-critical scenarios and further improves planners in handling such scenarios.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address it, this paper proposes an innovative and efficient strategy, termed IntSim, that explicitly decouples the driving intentions of surrounding actors from their motion planning for realistic and efficient safety-critical simulation.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
