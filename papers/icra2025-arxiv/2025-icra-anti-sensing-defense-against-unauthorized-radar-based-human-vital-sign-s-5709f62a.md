# Anti-Sensing: Defense against Unauthorized Radar-Based Human Vital Sign Sensing with Physically Realizable Wearable Oscillators

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Wearable Robotics 1 |
| arXiv | [http://arxiv.org/abs/2505.10864](http://arxiv.org/abs/2505.10864) |
| Authors | Tasnim Oshim, Md Farhan, Doering, Nigel, Islam, Bashima, Weng, Tsui-Wei, Rahman, Tauhidur |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we present Anti-Sensing, a novel defense mechanism designed to prevent unauthorized radar-based sensing.
- Recent advancements in Ultra-Wideband (UWB) radar technology have enabled contactless, non-line-of-sight vital sign monitoring, making it a valuable tool for healthcare.
- Through both simulations and real-world experiments with radar data and neural network-based HR sensing models, we demonstrate the effectiveness of Anti-Sensing in significantly degrading model accuracy, offering a practical solution for privacy preservation.

## Task

* Robotics

## Keywords

* Wearable Robotics / Physically Assistive Devices / Human-Centered Robotics

## AI依存度

* Hybrid

## 何を解決？

* Recent advancements in Ultra-Wideband (UWB) radar technology have enabled contactless, non-line-of-sight vital sign monitoring, making it a valuable tool for healthcare.

## 何が新しい？

* In this paper, we present Anti-Sensing, a novel defense mechanism designed to prevent unauthorized radar-based sensing.

## どうやってる？

* We develop a gradient-based algorithm to optimize the frequency and spatial amplitude of these oscillations for maximal disruption while ensuring physiological plausibility.

## どこが強い？

* Through both simulations and real-world experiments with radar data and neural network-based HR sensing models, we demonstrate the effectiveness of Anti-Sensing in significantly degrading model accuracy, offering a practical solution for privacy preservation.

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: architecture reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
