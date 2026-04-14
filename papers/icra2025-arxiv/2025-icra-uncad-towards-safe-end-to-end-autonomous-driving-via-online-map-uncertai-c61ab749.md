# UncAD: Towards Safe End-To-End Autonomous Driving Via Online Map Uncertainty

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Vision-Based Navigation 2 |
| arXiv | [http://arxiv.org/abs/2504.12826](http://arxiv.org/abs/2504.12826) |
| Authors | Yang, Pengxuan, Zheng, Yupeng, Zhang, Qichao, Zhu, Kefei, Xing, Zebin, Lin, Qiao, Liu, Yun-Fu, Su, Zhiguo, Zhao, Dongbin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- End-to-end autonomous driving aims to produce planning trajectories from raw sensors directly.
- Currently, most approaches integrate perception, prediction, and planning modules into a fully differentiable network, promising great scalability.
- Finally, to achieve safer autonomous driving, UncAD proposes an uncertainty-collision-aware planning selection strategy according to the online map uncertainty to evaluate and select the best trajectory.

## Task

* Perception
* Motion Planning
* Intelligent Vehicles

## Keywords

* Vision-Based Navigation / Integrated Planning and Learning / Computer Vision for Transportation

## AI依存度

* Hybrid

## 何を解決？

* End-to-end autonomous driving aims to produce planning trajectories from raw sensors directly.

## 何が新しい？

* To address this issue, we delve into the importance of online map uncertainty for enhancing autonomous driving safety and propose a novel paradigm named UncAD.

## どうやってる？

* Specifically, UncAD first estimates the uncertainty of the online map in the perception module.

## どこが強い？

* Finally, to achieve safer autonomous driving, UncAD proposes an uncertainty-collision-aware planning selection strategy according to the online map uncertainty to evaluate and select the best trajectory.

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
* どのモジュールに効くか: perception, planning, planning / control / perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
