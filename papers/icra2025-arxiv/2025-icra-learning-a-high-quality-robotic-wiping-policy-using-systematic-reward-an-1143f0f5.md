# Learning a High-Quality Robotic Wiping Policy Using Systematic Reward Analysis and Visual-Language Model Based Curriculum

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 2 |
| arXiv | [http://arxiv.org/abs/2502.12599](http://arxiv.org/abs/2502.12599) |
| Authors | Liu, Yihong, Kang, Dongyeop, Ha, Sehoon |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Instead of relying on manual tuning, we first analyze the convergence of quality-critical robotic wiping, which requires both high-quality wiping and fast task completion, to show the poor convergence of the problem and propose a new bounded reward formulation to make the problem feasible.
- Autonomous robotic wiping is an important task in various industries, ranging from industrial manufacturing to sanitization in healthcare.
- We demonstrate that the combined method can find a desirable wiping policy on surfaces with various curvatures, frictions, and waypoints, which cannot be learned with the baseline formulation.

## Task

* Control

## Keywords

* Reinforcement Learning / AI-Enabled Robotics / Force Control

## AI依存度

* Hybrid

## 何を解決？

* Instead of relying on manual tuning, we first analyze the convergence of quality-critical robotic wiping, which requires both high-quality wiping and fast task completion, to show the poor convergence of the problem and propose a new bounded reward formulation to make the problem feasible.

## 何が新しい？

* Then, we further improve the learning process by proposing a novel visual-language model (VLM) based curriculum, which actively monitors the progress and suggests hyperparameter tuning.

## どうやってる？

* Deep reinforcement learning (Deep RL) has emerged as a promising algorithm, however, it often suffers from a high demand for repetitive reward engineering.

## どこが強い？

* We demonstrate that the combined method can find a desirable wiping policy on surfaces with various curvatures, frictions, and waypoints, which cannot be learned with the baseline formulation.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* We demonstrate that the combined method can find a desirable wiping policy on surfaces with various curvatures, frictions, and waypoints, which cannot be learned with the baseline formulation.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: control
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
