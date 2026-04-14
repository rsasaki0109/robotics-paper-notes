# Exact Imposition of Safety Boundary Conditions in Neural Reachable Tubes

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Safe Control 1 |
| arXiv | [http://arxiv.org/abs/2404.00814](http://arxiv.org/abs/2404.00814) |
| Authors | Singh, Aditya, Feng, Zeyuan, Bansal, Somil |
| Source | ICRA 2025 / arXiv |

## TL;DR

- To overcome these challenges, DeepReach,a recently proposed learning-based approach, approximates high-dimensional reachable tubes using neural networks (NNs).
- In this work, we propose ExactBC, a variant of DeepReach that imposes safety constraints exactly during the learning process by restructuring the overall value function as a weighted sum of the boundary condition and the NN output.
- While shown to be effective, the accuracy of the learned solution decreases with system complexity.

## Task

* Control

## Keywords

* Robot Safety / Machine Learning for Robot Control

## AI依存度

* Hybrid

## 何を解決？

* To overcome these challenges, DeepReach,a recently proposed learning-based approach, approximates high-dimensional reachable tubes using neural networks (NNs).

## 何が新しい？

* In this work, we propose ExactBC, a variant of DeepReach that imposes safety constraints exactly during the learning process by restructuring the overall value function as a weighted sum of the boundary condition and the NN output.

## どうやってる？

* To overcome these challenges, DeepReach,a recently proposed learning-based approach, approximates high-dimensional reachable tubes using neural networks (NNs).

## どこが強い？

* We demonstrate the efficacy of the proposed approach in significantly improving the accuracy of the learned value function for four challenging reachability tasks: a rimless wheel system with state resets, collision avoidance in a cluttered environment, autonomous rocket landing, and multi-aircraft collision avoidance.

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
