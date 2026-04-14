# Sim-Grasp: Learning 6-DOF Grasp Policies for Cluttered Environments Using a Synthetic Benchmark

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning Based Planning for Manipulation 2 |
| arXiv | [http://arxiv.org/abs/2405.00841](http://arxiv.org/abs/2405.00841) |
| Authors | Li, Juncheng, Cappelleri, David |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we present Sim-Grasp, a robust 6-DOF two-finger grasping system that integrates advanced language models for enhanced object manipulation in cluttered environments.
- We introduce the Sim-Grasp-Dataset, which includes 1,550 objects across 500 scenarios with 7.9 million annotated labels, and develop Sim-GraspNet to generate grasp poses from point clouds.
- The Sim-Grasp-Polices achieve grasping success rates of 97.14% for single objects and 87.43% and 83.33% for mixed clutter scenarios of Levels 1-2 and Levels 3-4 objects, respectively.

## Task

* Motion Planning
* Manipulation

## Keywords

* Mobile Manipulation / Deep Learning in Grasping and Manipulation / Grasping

## AI依存度

* Hybrid

## 何を解決？

* In this paper, we present Sim-Grasp, a robust 6-DOF two-finger grasping system that integrates advanced language models for enhanced object manipulation in cluttered environments.

## 何が新しい？

* In this paper, we present Sim-Grasp, a robust 6-DOF two-finger grasping system that integrates advanced language models for enhanced object manipulation in cluttered environments.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* The Sim-Grasp-Polices achieve grasping success rates of 97.14% for single objects and 87.43% and 83.33% for mixed clutter scenarios of Levels 1-2 and Levels 3-4 objects, respectively.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

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
