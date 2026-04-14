# Range-Based 6-DoF Monte Carlo SLAM with Gradient-Guided Particle Filter on GPU

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | SLAM 4 |
| arXiv | [http://arxiv.org/abs/2504.18056](http://arxiv.org/abs/2504.18056) |
| Authors | Nakao, Takumi, Koide, Kenji, Takanose, Aoki, Oishi, Shuji, Yokozuka, Masashi, Date, Hisashi |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper presents range-based 6-DoF Monte Carlo SLAM with a gradient-guided particle update strategy.
- To address this issue, we propose a particle update strategy that improves the sampling efficiency by using the gradient information of the likelihood function to guide particles toward its local maxima.
- Experimental results demonstrate that the proposed method exhibits extreme robustness to state ambiguity and can even deal with kidnapping situations, such as when the sensor moves to different floors via an elevator, with minimal heuristics.

## Task

* SLAM
* Mapping
* Motion Planning
* State Estimation

## Keywords

* SLAM / Mapping / Range Sensing

## AI依存度

* Non-AI

## 何を解決？

* While non-parametric state estimation methods, such as particle filters, are robust in situations with high ambiguity, they are known to be unsuitable for high-dimensional problems due to the curse of dimensionality.

## 何が新しい？

* To address this issue, we propose a particle update strategy that improves the sampling efficiency by using the gradient information of the likelihood function to guide particles toward its local maxima.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* Experimental results demonstrate that the proposed method exhibits extreme robustness to state ambiguity and can even deal with kidnapping situations, such as when the sensor moves to different floors via an elevator, with minimal heuristics.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* The combination of gradient information and keyframe-based map representation significantly enhances sampling efficiency and reduces memory usage compared to traditional RBPF approaches.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
