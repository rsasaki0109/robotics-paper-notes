# PrivilegedDreamer: Explicit Imagination of Privileged Information for Rapid Adaptation of Learned Policies

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 3 |
| arXiv | [http://arxiv.org/abs/2502.11377](http://arxiv.org/abs/2502.11377) |
| Authors | Byrd, Morgan, Crandell, Jackson, Das, Mili, Inman, Jessica, Wright, Robert, Ha, Sehoon |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Numerous real-world control problems involve dynamics and objectives affected by unobservable hidden parameters, ranging from autonomous driving to robotic manipulation, which cause performance degradation during sim-to-real transfer.
- We introduce PrivilegedDreamer, a model-based reinforcement learning framework that extends the existing model-based approach by incorporating an explicit parameter estimation module.
- Our empirical analysis on five diverse HIP-MDP tasks demonstrates that PrivilegedDreamer outperforms state-of-the-art model-based, model-free, and domain adaptation learning algorithms.

## Task

* Control
* Intelligent Vehicles
* Manipulation

## Keywords

* Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* Numerous real-world control problems involve dynamics and objectives affected by unobservable hidden parameters, ranging from autonomous driving to robotic manipulation, which cause performance degradation during sim-to-real transfer.

## 何が新しい？

* We introduce PrivilegedDreamer, a model-based reinforcement learning framework that extends the existing model-based approach by incorporating an explicit parameter estimation module.

## どうやってる？

* Numerous real-world control problems involve dynamics and objectives affected by unobservable hidden parameters, ranging from autonomous driving to robotic manipulation, which cause performance degradation during sim-to-real transfer.

## どこが強い？

* Our empirical analysis on five diverse HIP-MDP tasks demonstrates that PrivilegedDreamer outperforms state-of-the-art model-based, model-free, and domain adaptation learning algorithms.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Existing approaches, such as domain randomization, domain adaptation, and meta-learning, simply treat the effect of hidden parameters as additional variance and often struggle to effectively handle HIP-MDP problems, especially when the rewards are parameterized by hidden variables.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: control, planning / control / perception, limited direct use; integration pattern reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
