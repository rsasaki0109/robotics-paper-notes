# Fine-Tuning Hard-To-Simulate Objectives for Quadruped Locomotion: A Case Study on Total Power Saving

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning for Legged Locomotion 2 |
| arXiv | [http://arxiv.org/abs/2502.10956](http://arxiv.org/abs/2502.10956) |
| Authors | Nai, Ruiqian;You, Jiacheng;Cao, Liu;Cui, Hanchen;Zhang, Shiyuan;Xu, Huazhe;Gao, Yang |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Legged locomotion is not just about mobility; it also encompasses crucial objectives such as energy efficiency, safety, and user experience, which are vital for real-world applications.
- However, key factors such as battery power consumption and stepping noise are often inaccurately modeled or missing in common simulators, leaving these aspects poorly optimized or unaddressed by current sim-to-real methods.
- Hand-designed proxies, such as mechanical power and foot contact forces, have been used to address these challenges but are often problem-specific and inaccurate.

## Task

* Visual-Inertial
* Legged Robotics
* Software Tools

## Keywords

* Reinforcement Learning
* Legged Robots

## AI依存度

* Hybrid

## 何を解決？

* Legged locomotion is not just about mobility; it also encompasses crucial objectives such as energy efficiency, safety, and user experience, which are vital for real-world applications.

## 何が新しい？

* In this paper, we propose a data-driven framework for fine-tuning locomotion policies, targeting these hard-to-simulate objectives.

## どうやってる？

* However, key factors such as battery power consumption and stepping noise are often inaccurately modeled or missing in common simulators, leaving these aspects poorly optimized or unaddressed by current sim-to-real methods.

## どこが強い？

* We demonstrate the effectiveness of our framework on power saving for quadruped locomotion, achieving a significant 24-28% net reduction in total power consumption from the battery pack at various speeds.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we propose a data-driven framework for fine-tuning locomotion policies, targeting these hard-to-simulate objectives.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
