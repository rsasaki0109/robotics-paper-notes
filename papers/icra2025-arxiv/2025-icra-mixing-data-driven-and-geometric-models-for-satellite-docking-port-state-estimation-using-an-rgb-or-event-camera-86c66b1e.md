# Mixing Data-Driven and Geometric Models for Satellite Docking Port State Estimation Using an RGB or Event Camera

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Space Robotics 2 |
| arXiv | [http://arxiv.org/abs/2409.15581](http://arxiv.org/abs/2409.15581) |
| Authors | Le Gentil, Cedric;Naylor, Jack;Munasinghe, Nuwan;Mehami, Jasprabhjit;Dai, Benny;Asavkin, Mikhail;Dansereau, Donald;Vidal-Calleja, Teresa A. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In-orbit automated servicing is a promising path towards lowering the cost of satellite operations and reducing the amount of orbital debris.
- For this purpose, we present a pipeline for automated satellite docking port detection and state estimation using monocular vision data from standard RGB sensing or an event camera.
- Rather than taking snapshots of the environment, an event camera has independent pixels that asynchronously respond to light changes, offering advantages such as high dynamic range, low power consumption and latency.

## Task

* Localization
* Visual-Inertial
* Control
* Perception

## Keywords

* Space Robotics and Automation
* Visual Tracking
* Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* In-orbit automated servicing is a promising path towards lowering the cost of satellite operations and reducing the amount of orbital debris.

## 何が新しい？

* For this purpose, we present a pipeline for automated satellite docking port detection and state estimation using monocular vision data from standard RGB sensing or an event camera.

## どうやってる？

* By leveraging shallow data-driven techniques to preprocess the incoming data to highlight the LM-MAP's reflective navigational aids and then using basic geometric models for state estimation, we present a lightweight and data-efficient pipeline that can be used independently with either RGB or event cameras.

## どこが強い？

* We demonstrate the soundness of the pipeline and perform a quantitative comparison of the two modalities based on data collected with a photometrically accurate test bench that includes a robotic arm to simulate the target satellite's uncontrolled motion.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* For this purpose, we present a pipeline for automated satellite docking port detection and state estimation using monocular vision data from standard RGB sensing or an event camera.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
