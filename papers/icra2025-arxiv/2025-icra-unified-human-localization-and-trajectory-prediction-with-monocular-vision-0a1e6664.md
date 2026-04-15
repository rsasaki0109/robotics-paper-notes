# Unified Human Localization and Trajectory Prediction with Monocular Vision

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Robot Vision 2 |
| arXiv | [http://arxiv.org/abs/2503.03535](http://arxiv.org/abs/2503.03535) |
| Authors | Luan, Po-Chien;Gao, Yang;Demonsant, Céline;Alahi, Alexandre |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Conventional human trajectory prediction models rely on clean curated data, requiring specialized equipment or manual labeling, which is often impractical for robotic applications.
- The existing predictors tend to overfit to clean observation affecting their robustness when used with noisy inputs.
- In this work, we propose MonoTransmotion (MT), a Transformer-based framework that uses only a monocular camera to jointly solve localization and prediction tasks.

## Task

* Localization
* Motion Planning
* Software Tools

## Keywords

* Intelligent Transportation Systems
* Localization
* Computer Vision for Transportation

## AI依存度

* AI-heavy

## 何を解決？

* Conventional human trajectory prediction models rely on clean curated data, requiring specialized equipment or manual labeling, which is often impractical for robotic applications.

## 何が新しい？

* In this work, we propose MonoTransmotion (MT), a Transformer-based framework that uses only a monocular camera to jointly solve localization and prediction tasks.

## どうやってる？

* We show that by jointly training both tasks with our unified framework, our method is more robust in real-world scenarios made of noisy inputs.

## どこが強い？

* On real-world non-curated dataset, experimental results indicate that MT maintains similar performance levels, highlighting its robustness and generalization capability.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this work, we propose MonoTransmotion (MT), a Transformer-based framework that uses only a monocular camera to jointly solve localization and prediction tasks.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
