# Effective Tuning Strategies for Generalist Robot Manipulation Policies

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning Based Planning for Manipulation 2 |
| arXiv | [http://arxiv.org/abs/2410.01220](http://arxiv.org/abs/2410.01220) |
| Authors | Zhang, Wenbo, Li, Yang, Qiao, Yanyuan, Huang, Siyuan, Liu, Jiajun, Dayoub, Feras, Ma, Xiao, Liu, Lingqiao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Generalist robot manipulation policies (GMPs) have the potential to generalize across a wide range of tasks, environments, and devices.
- However, existing policies continue to struggle with out-of-distribution scenarios, considering that the action data remains notoriously hard to collect.
- The results presented in this work establish a new baseline for future studies on fine-tuned GMPs.

## Task

* Motion Planning
* Manipulation

## Keywords

* Deep Learning in Grasping and Manipulation / Transfer Learning

## AI依存度

* Hybrid

## 何を解決？

* Generalist robot manipulation policies (GMPs) have the potential to generalize across a wide range of tasks, environments, and devices.

## 何が新しい？

* While fine-tuning offers a practical way to quickly adapt a GMP to novel domains and tasks with limited samples, we observe that the performance of the resulting GMP differs significantly with respect to the design choices of fine-tuning strategies.

## どうやってる？

* We observe that in a low-data regime, with carefully chosen fine-tuning strategies, a GMP significantly outperforms the state-of-the-art imitation learning algorithms.

## どこが強い？

* The results presented in this work establish a new baseline for future studies on fine-tuned GMPs.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* The results presented in this work establish a new baseline for future studies on fine-tuned GMPs.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: planning, limited direct use; integration pattern reference
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
