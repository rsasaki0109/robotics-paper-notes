# Multi-Agent Inverse Q-Learning from Demonstrations

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multi-Robot Systems 6 |
| arXiv | [http://arxiv.org/abs/2503.04679](http://arxiv.org/abs/2503.04679) |
| Authors | Haynam, Nathaniel;Khoja, Adam;Kumar, Dhruv;Myers, Vivek;Bıyık, Erdem |
| Source | ICRA 2025 / arXiv |

## TL;DR

- When reward functions are hand-designed, deep reinforcement learning algorithms often suffer from reward misspecification, causing them to learn suboptimal policies.
- In the single-agent case, Inverse Reinforcement Learning (IRL) techniques attempt to address this issue by inferring the reward function from expert demonstrations.
- However, in multi-agent problems, misalignment between the learned and true objectives is exacerbated due to increased environment non-stationarity and variance that scale with multiple agents.

## Task

* Visual-Inertial

## Keywords

* Multi-Robot Systems
* Imitation Learning

## AI依存度

* Hybrid

## 何を解決？

* When reward functions are hand-designed, deep reinforcement learning algorithms often suffer from reward misspecification, causing them to learn suboptimal policies.

## 何が新しい？

* To address these issues, we propose Multi-Agent Marginal Q-Learning from Demonstrations (MAMQL), a novel sample-efficient framework for multi-agent IRL.

## どうやってる？

* Across our experiments on three different simulated domains, MAMQL significantly outperforms previous multi-agent methods in average reward, sample efficiency, and reward recovery by often more than 2-5x.

## どこが強い？

* Across our experiments on three different simulated domains, MAMQL significantly outperforms previous multi-agent methods in average reward, sample efficiency, and reward recovery by often more than 2-5x.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these issues, we propose Multi-Agent Marginal Q-Learning from Demonstrations (MAMQL), a novel sample-efficient framework for multi-agent IRL.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
