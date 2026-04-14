# MAC-VO: Metrics-Aware Covariance for Learning-Based Stereo Visual Odometry

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | SLAM 2 |
| arXiv | [http://arxiv.org/abs/2409.09479](http://arxiv.org/abs/2409.09479) |
| Authors | Qiu, Yuheng, Chen, Yutian, Zhang, Zihao, Wang, Wenshan, Scherer, Sebastian |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We propose the MAC-VO, a novel learning-based stereo VO that leverages the learned metrics-aware matching uncertainty for dual purposes: selecting keypoint and weighing the residual in pose graph optimization.
- In contrast to the learning-based algorithms that model the scale-agnostic diagonal weight matrix for covariance, we design a metrics-aware covariance model to capture the spatial error during keypoint registration and the correlations between different axes.
- Compared to traditional geometric methods prioritizing texture-affluent features like edges, our keypoint selector employs the learned uncertainty to filter out the low-quality features based on global inconsistency.

## Task

* SLAM
* Localization
* Mapping

## Keywords

* SLAM / Localization / Mapping

## AI依存度

* Hybrid

## 何を解決？

* We propose the MAC-VO, a novel learning-based stereo VO that leverages the learned metrics-aware matching uncertainty for dual purposes: selecting keypoint and weighing the residual in pose graph optimization.

## 何が新しい？

* We propose the MAC-VO, a novel learning-based stereo VO that leverages the learned metrics-aware matching uncertainty for dual purposes: selecting keypoint and weighing the residual in pose graph optimization.

## どうやってる？

* We propose the MAC-VO, a novel learning-based stereo VO that leverages the learned metrics-aware matching uncertainty for dual purposes: selecting keypoint and weighing the residual in pose graph optimization.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Compared to traditional geometric methods prioritizing texture-affluent features like edges, our keypoint selector employs the learned uncertainty to filter out the low-quality features based on global inconsistency.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: localization / mapping, localization, map / localization
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
