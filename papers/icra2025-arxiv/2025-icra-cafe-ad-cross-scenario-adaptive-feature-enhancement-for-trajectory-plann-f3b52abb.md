# CAFE-AD: Cross-Scenario Adaptive Feature Enhancement for Trajectory Planning in Autonomous Driving

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Navigation 1 |
| arXiv | [http://arxiv.org/abs/2504.06584](http://arxiv.org/abs/2504.06584) |
| Authors | Zhang, Junrui, Wang, Chenjie, Peng, Jie, Li, Haoyu, Ji, Jianmin, Zhang, Yu, Zhang, Yanyong |
| Source | ICRA 2025 / arXiv |

## TL;DR

- These issues introduce challenges for imitation learning.
- To tackle these problems, we introduce CAFE-AD, a Cross-Scenario Adaptive Feature Enhancement for Trajectory Planning in Autonomous Driving method, designed to enhance feature representation across various scenario types.
- We evaluate our method CAFE-AD, on the challenging public nuPlan Test14-Hard closed-loop simulation benchmark.

## Task

* Sensor Fusion
* Motion Planning
* Intelligent Vehicles

## Keywords

* Autonomous Vehicle Navigation / Motion and Path Planning / Intelligent Transportation Systems

## AI依存度

* Hybrid

## 何を解決？

* These issues introduce challenges for imitation learning.

## 何が新しい？

* To tackle these problems, we introduce CAFE-AD, a Cross-Scenario Adaptive Feature Enhancement for Trajectory Planning in Autonomous Driving method, designed to enhance feature representation across various scenario types.

## どうやってる？

* Imitation learning based planning tasks on the nuPlan dataset have gained great interest due to their potential to generate human-like driving behaviors.

## どこが強い？

* We evaluate our method CAFE-AD, on the challenging public nuPlan Test14-Hard closed-loop simulation benchmark.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: perception / localization fusion, planning, planning / control / perception
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
