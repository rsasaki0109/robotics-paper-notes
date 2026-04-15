# Physics-Aware Robotic Palletization with Online Masking Inference

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Logistics and Task Planning |
| arXiv | [http://arxiv.org/abs/2502.13443](http://arxiv.org/abs/2502.13443) |
| Authors | Zhang, Tianqi;Wu, Zheng;Chen, Yuxin;Wang, Yixiao;Liang, Boyuan;Moura, Scott;Tomizuka, Masayoshi;Ding, Mingyu;Zhan, Wei |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The efficient planning of stacking boxes, especially in the online setting where the sequence of item arrivals is unpredictable, remains a critical challenge in modern warehouse and logistics management.
- Existing solutions often address box size variations, but overlook their intrinsic and physical properties, such as density and rigidity, which are crucial for real-world applications.
- We use reinforcement learning (RL) to solve this problem by employing action space masking to direct the RL policy towards valid actions.

## Task

* Motion Planning
* Manipulation

## Keywords

* Task Planning
* Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* The efficient planning of stacking boxes, especially in the online setting where the sequence of item arrivals is unpredictable, remains a critical challenge in modern warehouse and logistics management.

## 何が新しい？

* Extensive experiments demonstrate that our proposed method outperforms existing state-of-the-arts.

## どうやってる？

* Unlike previous methods that rely on heuristic stability assessments which are difficult to assess in physical scenarios, our framework utilizes online learning to dynamically train the action space mask, eliminating the need for manual heuristic design.

## どこが強い？

* Extensive experiments demonstrate that our proposed method outperforms existing state-of-the-arts.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Extensive experiments demonstrate that our proposed method outperforms existing state-of-the-arts.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
