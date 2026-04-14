# LoRD: Adapting Differentiable Driving Policies to Distribution Shifts

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Intelligent Transportation Systems and AI-Based Methods |
| arXiv | [http://arxiv.org/abs/2410.09681](http://arxiv.org/abs/2410.09681) |
| Authors | Diehl, Christopher, Karkus, Peter, Veer, Sushant, Pavone, Marco, Bertram, Torsten |
| Source | ICRA 2025 / arXiv |

## TL;DR

- While this is a well-established problem, prior work has mostly explored naive solutions such as fine-tuning, focusing on the motion prediction task.
- Specifically, we introduce two simple yet effective techniques: a low-rank residual decoder (LoRD) and multi-task fine-tuning.
- Through experiments across three models conducted on two real-world autonomous driving datasets (nuPlan, exiD), we demonstrate the effectiveness of our methods and highlight a significant performance gap between open-loop and closed-loop evaluation in prior approaches.

## Task

* Motion Planning
* Control
* Intelligent Vehicles

## Keywords

* Intelligent Transportation Systems / Integrated Planning and Learning / Transfer Learning

## AI依存度

* Hybrid

## 何を解決？

* While this is a well-established problem, prior work has mostly explored naive solutions such as fine-tuning, focusing on the motion prediction task.

## 何が新しい？

* In this work, we explore novel adaptation strategies for differentiable autonomy stacks (structured policy) consisting of prediction, planning, and control, perform evaluation in closed-loop, and investigate the often-overlooked issue of catastrophic forgetting.

## どうやってる？

* Distribution shifts between operational domains can severely affect the performance of learned models in self-driving vehicles (SDVs).

## どこが強い？

* Through experiments across three models conducted on two real-world autonomous driving datasets (nuPlan, exiD), we demonstrate the effectiveness of our methods and highlight a significant performance gap between open-loop and closed-loop evaluation in prior approaches.

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
