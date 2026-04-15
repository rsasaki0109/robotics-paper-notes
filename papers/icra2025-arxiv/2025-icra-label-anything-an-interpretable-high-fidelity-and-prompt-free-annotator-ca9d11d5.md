# Label Anything: An Interpretable, High-Fidelity and Prompt-Free Annotator

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Large Models for Autonomous Vehicles |
| arXiv | [http://arxiv.org/abs/2502.02972](http://arxiv.org/abs/2502.02972) |
| Authors | Kou, Wei-Bin;Zhu, Guangxu;Ye, Rongguang;Wang, Shuai;Tang, Ming;Wu, Yik-Chung |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Learning-based street scene semantic understanding in autonomous driving (AD) has advanced significantly recently, but the performance of the AD model is heavily dependent on the quantity and quality of the annotated training data.
- However, traditional manual labeling involves high cost to annotate the vast amount of required data for training robust model.
- To mitigate this cost of manual labeling, we propose a Label Anything Model (denoted as LAM), serving as an interpretable, high-fidelity, and prompt-free data annotator.

## Task

* Visual-Inertial
* Perception
* Software Tools

## Keywords

* Semantic Scene Understanding
* Object Detection
* Segmentation and Categorization
* Intelligent Transportation Systems

## AI依存度

* AI-heavy

## 何を解決？

* Learning-based street scene semantic understanding in autonomous driving (AD) has advanced significantly recently, but the performance of the AD model is heavily dependent on the quantity and quality of the annotated training data.

## 何が新しい？

* To mitigate this cost of manual labeling, we propose a Label Anything Model (denoted as LAM), serving as an interpretable, high-fidelity, and prompt-free data annotator.

## どうやってる？

* On top of ViT, we propose a semantic class adapter (SCA) and an optimization-oriented unrolling algorithm (OptOU), both with a quite small number of trainable parameters.

## どこが強い？

* Extensive experiments clearly demonstrate that the proposed LAM can generate high-fidelity annotations (almost 100% in mIoU) for multiple real-world datasets (i.e., Camvid, Cityscapes, and Apolloscapes) and CARLA simulation dataset.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To mitigate this cost of manual labeling, we propose a Label Anything Model (denoted as LAM), serving as an interpretable, high-fidelity, and prompt-free data annotator.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
