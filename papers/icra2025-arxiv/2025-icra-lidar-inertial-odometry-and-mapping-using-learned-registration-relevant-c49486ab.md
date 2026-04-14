# LiDAR Inertial Odometry and Mapping Using Learned Registration-Relevant Features

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Mobile Robots 1 |
| arXiv | [http://arxiv.org/abs/2410.02961](http://arxiv.org/abs/2410.02961) |
| Authors | Dong, Zihao, Pflueger, Jeff, Jung, Leonard, Thorne, David, Osteen, Philip, Robison, Christopher, Christa, Lopez, Brett, Everett, Michael |
| Source | ICRA 2025 / arXiv |

## TL;DR

- To address these issues, this paper presents DFLIOM with several key innovations.
- Unlike previous methods that rely on handcrafted heuristics and hand-tuned parameters for feature extraction, we propose a learning-based approach that select points relevant to LiDAR SLAM pointcloud registration.
- We demonstrate that DFLIOM performs well on multiple public benchmarks, achieving a 2.4% decrease in localization error and 57.5% decrease in memory usage compared to state-of-the-art methods (DLIOM).

## Task

* SLAM
* Localization
* LiDAR
* Mapping

## Keywords

* AI-Based Methods / Localization / SLAM

## AI依存度

* Hybrid

## 何を解決？

* SLAM is an important capability for many autonomous systems, and modern LiDAR-based methods offer promising performance.

## 何が新しい？

* Unlike previous methods that rely on handcrafted heuristics and hand-tuned parameters for feature extraction, we propose a learning-based approach that select points relevant to LiDAR SLAM pointcloud registration.

## どうやってる？

* Unlike previous methods that rely on handcrafted heuristics and hand-tuned parameters for feature extraction, we propose a learning-based approach that select points relevant to LiDAR SLAM pointcloud registration.

## どこが強い？

* We demonstrate that DFLIOM performs well on multiple public benchmarks, achieving a 2.4% decrease in localization error and 57.5% decrease in memory usage compared to state-of-the-art methods (DLIOM).

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* Unlike previous methods that rely on handcrafted heuristics and hand-tuned parameters for feature extraction, we propose a learning-based approach that select points relevant to LiDAR SLAM pointcloud registration.

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 一部は使える。特に classical backbone が強ければ実装の参考になる。
* どのモジュールに効くか: localization / mapping, localization, sensing / localization / perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
