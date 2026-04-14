# Thermal Chameleon: Task-Adaptive Tone-Mapping for Radiometric Thermal-Infrared Images

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Novel Sensors |
| arXiv | [http://arxiv.org/abs/2410.18340](http://arxiv.org/abs/2410.18340) |
| Authors | Lee, DongGuw, Kim, Jeongyun, Cho, Younggun, Kim, Ayoung |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we present the Thermal Chameleon Network (TCNet), a task-adaptive tone-mapping approach for RAW 14-bit TIR images.
- Thermal Infrared (TIR) imaging provides robust perception for navigating in challenging outdoor environments but faces issues with poor texture and low image contrast due to its 14/16-bit format.
- Conventional methods utilize various tone-mapping methods to enhance contrast and photometric consistency of TIR images, however, the choice of tone-mapping is largely dependent on knowing the task and temperature dependent priors to work well.

## Task

* Mapping
* Perception

## Keywords

* Object Detection / Segmentation and Categorization / Representation Learning / Deep Learning for Visual Perception

## AI依存度

* Hybrid

## 何を解決？

* Thermal Infrared (TIR) imaging provides robust perception for navigating in challenging outdoor environments but faces issues with poor texture and low image contrast due to its 14/16-bit format.

## 何が新しい？

* In this paper, we present the Thermal Chameleon Network (TCNet), a task-adaptive tone-mapping approach for RAW 14-bit TIR images.

## どうやってる？

* Conventional methods utilize various tone-mapping methods to enhance contrast and photometric consistency of TIR images, however, the choice of tone-mapping is largely dependent on knowing the task and temperature dependent priors to work well.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* 学習データ依存性と、古典部分との寄与分解は本文・ablation を確認したい。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 学習要素はあるが、どこまでが古典手法でどこからが学習依存かを切り分けて読む価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と古典手法の分担がどこで効いているかを見極めたい。
