# Anomalies-By-Synthesis: Anomaly Detection Using Generative Diffusion Models for Off-Road Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Diffusion-Based Visual Perception and Learning |
| arXiv | [http://arxiv.org/abs/2505.22805](http://arxiv.org/abs/2505.22805) |
| Authors | Ancha, Siddharth;Jiang, Sunshine;Manderson, Travis;Brandt, Laura Eileen;Du, Yilun;Osteen, Philip;Roy, Nicholas |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In order to navigate safely and reliably in off-road environments, robots must detect anomalies that are out-of- distribution (OOD) with respect to the training data.
- We present an analysis-by-synthesis approach for pixel-wise anomaly detection without making any assumptions about the nature of OOD data.
- Given an input image, we use a generative diffusion model to synthesize an edited image that removes anomalies while keeping the remaining image unchanged.

## Task

* Perception

## Keywords

* Deep Learning for Visual Perception
* Deep Learning Methods
* Visual Learning

## AI依存度

* AI-heavy

## 何を解決？

* In order to navigate safely and reliably in off-road environments, robots must detect anomalies that are out-of- distribution (OOD) with respect to the training data.

## 何が新しい？

* We propose a novel inference approach for guided diffusion by analyzing the ideal guidance gradient and deriving a principled approximation that bootstraps the diffusion model to predict guidance gradients.

## どうやってる？

* Our diffusion-based analysis-by-synthesis method enables accurate anomaly detections for off-road navigation.

## どこが強い？

* In order to navigate safely and reliably in off-road environments, robots must detect anomalies that are out-of- distribution (OOD) with respect to the training data.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a novel inference approach for guided diffusion by analyzing the ideal guidance gradient and deriving a principled approximation that bootstraps the diffusion model to predict guidance gradients.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
