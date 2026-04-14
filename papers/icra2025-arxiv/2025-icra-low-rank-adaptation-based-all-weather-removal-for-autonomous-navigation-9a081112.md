# Low-Rank Adaptation-Based All-Weather Removal for Autonomous Navigation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 3 |
| arXiv | [http://arxiv.org/abs/2411.17814](http://arxiv.org/abs/2411.17814) |
| Authors | Rajagopalan, Sudarshan, Patel, Vishal |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we propose using Low-Rank Adaptation (LoRA) to efficiently adapt a pre-trained all-weather model to novel weather restoration tasks.
- To address this issue, we introduce a LoRA-based fine-tuning method called LoRA-Align (LoRA-A) which seeks to align the singular vectors of the fine-tuned and pre-trained weight matrices using Singular Value Decomposition (SVD).
- We show that images restored with LoRA and LoRA-A can be effectively used for computer vision tasks in autonomous navigation, such as semantic segmentation and depth estimation.

## Task

* Perception
* Calibration
* Intelligent Vehicles

## Keywords

* Computer Vision for Automation / Autonomous Vehicle Navigation

## AI依存度

* Non-AI

## 何を解決？

* To overcome this issue, existing models must either be retrained or fine-tuned, both of which are inefficient and impractical, with retraining needing access to large datasets, and fine-tuning involving many parameters.

## 何が新しい？

* In this paper, we propose using Low-Rank Adaptation (LoRA) to efficiently adapt a pre-trained all-weather model to novel weather restoration tasks.

## どうやってる？

* But this causes them to often struggle with out-of-distribution (OoD) samples or unseen degradations which limits their effectiveness for real-world autonomous navigation.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
