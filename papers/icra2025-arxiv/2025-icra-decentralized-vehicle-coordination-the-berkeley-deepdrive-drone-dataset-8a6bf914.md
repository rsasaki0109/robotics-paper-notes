# Decentralized Vehicle Coordination: The Berkeley DeepDrive Drone Dataset and Consensus-Based Models

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Navigation 2 |
| arXiv | [http://arxiv.org/abs/2209.08763](http://arxiv.org/abs/2209.08763) |
| Authors | Wu, Fangyu, Wang, Dequan, Hwang, Minjune, Hao, Chenhui, Lu, Jiawei, Zhang, Jiamu, Chou, Christopher, Darrell, Trevor, Bayen, Alexandre |
| Source | ICRA 2025 / arXiv |

## TL;DR

- These understructured roads pose substantial challenges for autonomous vehicle motion planning, where efficient and safe navigation relies on understanding decentralized human coordination for collision avoidance.
- In this paper, we present a novel dataset and modeling framework designed to study motion planning in these understructured environments.
- We demonstrate that a consensus-based modeling approach can effectively explain the emergence of priority orders observed in our dataset, and is therefore a viable framework for decentralized collision avoidance planning.

## Task

* Perception
* Motion Planning
* Intelligent Vehicles
* Aerial Robotics

## Keywords

* Autonomous Vehicle Navigation / Collision Avoidance / Distributed Robot Systems

## AI依存度

* Non-AI

## 何を解決？

* These understructured roads pose substantial challenges for autonomous vehicle motion planning, where efficient and safe navigation relies on understanding decentralized human coordination for collision avoidance.

## 何が新しい？

* In this paper, we present a novel dataset and modeling framework designed to study motion planning in these understructured environments.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* We demonstrate that a consensus-based modeling approach can effectively explain the emergence of priority orders observed in our dataset, and is therefore a viable framework for decentralized collision avoidance planning.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: perception, planning, planning / control / perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
