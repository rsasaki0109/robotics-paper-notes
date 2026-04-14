# Multi-Agent Path Planning in Complex Environments Using Gaussian Belief Propagation with Global Path Finding

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Information Gathering, Planning and Control in Challenging Environments |
| arXiv | [http://arxiv.org/abs/2502.20369](http://arxiv.org/abs/2502.20369) |
| Authors | Jensen, Jens Høigaard, Plagborg Bak Sørensen, Kristoffer, le Fevre Sejersen, Jonas, Sarabakha, Andriy |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Multi-agent path planning is a critical challenge in robotics, requiring agents to navigate complex environments while avoiding collisions and optimizing travel efficiency.
- This work addresses the limitations of existing approaches by combining Gaussian belief propagation with path integration and introducing a novel tracking factor to ensure strict adherence to global paths.
- Simulation results demonstrate that the tracking factor reduces path deviation by 28% in single-agent and 16% in multi-agent scenarios, highlighting its effectiveness in improving multi-agent coordination, especially when combined with structured global planning.

## Task

* Perception
* Motion Planning
* Control

## Keywords

* Multi-Robot Systems / Path Planning for Multiple Mobile Robots or Agents / Collision Avoidance

## AI依存度

* Non-AI

## 何を解決？

* Multi-agent path planning is a critical challenge in robotics, requiring agents to navigate complex environments while avoiding collisions and optimizing travel efficiency.

## 何が新しい？

* This work addresses the limitations of existing approaches by combining Gaussian belief propagation with path integration and introducing a novel tracking factor to ensure strict adherence to global paths.

## どうやってる？

* Multi-agent path planning is a critical challenge in robotics, requiring agents to navigate complex environments while avoiding collisions and optimizing travel efficiency.

## どこが強い？

* A simulation environment was developed to validate the proposed method across diverse scenarios, each posing unique challenges in navigation and communication.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This work addresses the limitations of existing approaches by combining Gaussian belief propagation with path integration and introducing a novel tracking factor to ensure strict adherence to global paths.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: perception, planning, control
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
