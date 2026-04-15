# HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning for Legged Locomotion 1 |
| arXiv | [http://arxiv.org/abs/2410.21229](http://arxiv.org/abs/2410.21229) |
| Authors | He, Tairan;Xiao, Wenli;Lin, Toru;Luo, Zhengyi;Xu, Zhenjia;Jiang, Zhenyu;Kautz, Jan;Liu, Changliu;Shi, Guanya;Wang, Xiaolong;Fan, Linxi;Zhu, Yuke |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Humanoid whole-body control requires adapting to diverse tasks such as navigation, loco-manipulation, and tabletop manipulation, each demanding a different mode of control.
- For example, navigation relies on root velocity or position tracking, while tabletop manipulation prioritizes upper-body joint angle tracking.
- Existing approaches typically train individual policies tailored to a specific command space, limiting their transferability across modes.

## Task

* Motion Planning
* Control
* Manipulation
* Legged Robotics

## Keywords

* Reinforcement Learning
* Legged Robots
* Whole-Body Motion Planning and Control

## AI依存度

* Hybrid

## 何を解決？

* Humanoid whole-body control requires adapting to diverse tasks such as navigation, loco-manipulation, and tabletop manipulation, each demanding a different mode of control.

## 何が新しい？

* Building on this, we propose HOVER (Humanoid Versatile Controller), a multi-mode policy distillation framework that consolidates diverse control modes into a unified policy.

## どうやってる？

* Existing approaches typically train individual policies tailored to a specific command space, limiting their transferability across modes.

## どこが強い？

* Humanoid whole-body control requires adapting to diverse tasks such as navigation, loco-manipulation, and tabletop manipulation, each demanding a different mode of control.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Building on this, we propose HOVER (Humanoid Versatile Controller), a multi-mode policy distillation framework that consolidates diverse control modes into a unified policy.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
