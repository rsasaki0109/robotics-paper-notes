# Learning Quiet Walking for a Small Home Robot

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Robot Applications |
| arXiv | [http://arxiv.org/abs/2502.10983](http://arxiv.org/abs/2502.10983) |
| Authors | Watanabe, Ryo;Miki, Takahiro;Shi, Fan;Kadokawa, Yuki;Bjelonic, Filip;Kawaharazuka, Kento;Cramariuc, Andrei;Hutter, Marco |
| Source | ICRA 2025 / arXiv |

## TL;DR

- As home robotics gains traction, robots are increasingly integrated into households, offering companionship and assistance.
- Quadruped robots, particularly those resembling dogs, have emerged as popular alternatives for traditional pets.
- However, user feedback highlights concerns about the noise these robots generate during walking at home, particularly the loud footstep impact sound.

## Task

* Control
* Legged Robotics

## Keywords

* Domestic Robotics
* Legged Robots
* Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* As home robotics gains traction, robots are increasingly integrated into households, offering companionship and assistance.

## 何が新しい？

* To address this issue, we propose a reinforcement learning (RL) based approach to minimize the foot contact velocity highly related to the footstep sound.

## どうやってる？

* To address this issue, we propose a reinforcement learning (RL) based approach to minimize the foot contact velocity highly related to the footstep sound.

## どこが強い？

* Experiments demonstrate that our learned policy achieves superior quietness compared to a RL baseline and the carefully handcrafted Sony commercial controller baselines.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this issue, we propose a reinforcement learning (RL) based approach to minimize the foot contact velocity highly related to the footstep sound.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
