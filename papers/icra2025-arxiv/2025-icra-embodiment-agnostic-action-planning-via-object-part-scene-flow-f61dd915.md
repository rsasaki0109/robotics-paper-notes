# Embodiment-Agnostic Action Planning Via Object-Part Scene Flow

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation 2 |
| arXiv | [http://arxiv.org/abs/2409.10032](http://arxiv.org/abs/2409.10032) |
| Authors | Tang, Weiliang, Pan, Jia-Hui, Zhan, Wei, Zhou, Jianshu, Yao, Huaxiu, Liu, Yunhui, Tomizuka, Masayoshi, Ding, Mingyu, Fu, Chi-Wing |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Observing that the key for robotic action planning is to understand the target-object motion when its associated part is manipulated by the end effector, we propose to generate the 3D object-part scene flow and extract its transformations to solve the action trajectories for diverse embodiments.
- Also, beyond policies trained on embodiment-centric data, our method is embodiment-agnostic, generalizable across diverse embodiments, and being able to learn from human demonstrations.
- Furthermore, we conducted real-world experiments, showing that our policy, trained only with human demonstration, can be deployed to various embodiments.

## Task

* Motion Planning
* Manipulation

## Keywords

* AI-Based Methods / Deep Learning in Grasping and Manipulation / Manipulation Planning

## AI依存度

* Hybrid

## 何を解決？

* Observing that the key for robotic action planning is to understand the target-object motion when its associated part is manipulated by the end effector, we propose to generate the 3D object-part scene flow and extract its transformations to solve the action trajectories for diverse embodiments.

## 何が新しい？

* Observing that the key for robotic action planning is to understand the target-object motion when its associated part is manipulated by the end effector, we propose to generate the 3D object-part scene flow and extract its transformations to solve the action trajectories for diverse embodiments.

## どうやってる？

* Also, beyond policies trained on embodiment-centric data, our method is embodiment-agnostic, generalizable across diverse embodiments, and being able to learn from human demonstrations.

## どこが強い？

* Furthermore, we conducted real-world experiments, showing that our policy, trained only with human demonstration, can be deployed to various embodiments.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
