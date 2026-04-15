# Robot Navigation in Unknown and Cluttered Workspace with Dynamical System Modulation in Starshaped Roadmap

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning and Control |
| arXiv | [http://arxiv.org/abs/2403.11484](http://arxiv.org/abs/2403.11484) |
| Authors | Chen, Kai;Liu, Haichao;Li, Yulin;Duan, Jianghua;Zhu, Lei;Ma, Jun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Compared to conventional decomposition methods that use ellipses or polygons to represent free space, starshaped representation can better capture the natural distribution of sensor data, thereby exploiting a larger portion of traversable space.
- This paper introduces a novel motion planning and control framework for navigating robots in unknown and cluttered environments using a dynamically constructed starshaped roadmap.
- Our approach generates a starshaped representation of the surrounding free space from real-time sensor data using piece-wise polynomials.

## Task

* Visual-Inertial
* Motion Planning
* Control

## Keywords

* Integrated Planning and Control
* Autonomous Vehicle Navigation
* Sensor-based Control

## AI依存度

* Non-AI

## 何を解決？

* Compared to conventional decomposition methods that use ellipses or polygons to represent free space, starshaped representation can better capture the natural distribution of sensor data, thereby exploiting a larger portion of traversable space.

## 何が新しい？

* To ensure safe and efficient movement within the starshaped roadmap, we propose a reactive controller based on Dynamic System Modulation (DSM).

## どうやってる？

* Compared to conventional decomposition methods that use ellipses or polygons to represent free space, starshaped representation can better capture the natural distribution of sensor data, thereby exploiting a larger portion of traversable space.

## どこが強い？

* Comprehensive evaluations in both simulations and real-world experiments show that the proposed method achieves higher success rates and reduced travel times compared to other methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To ensure safe and efficient movement within the starshaped roadmap, we propose a reactive controller based on Dynamic System Modulation (DSM).

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
