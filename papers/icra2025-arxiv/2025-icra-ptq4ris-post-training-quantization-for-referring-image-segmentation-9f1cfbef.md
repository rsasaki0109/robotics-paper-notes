# PTQ4RIS: Post-Training Quantization for Referring Image Segmentation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Robot Vision 1 |
| arXiv | [http://arxiv.org/abs/2409.17020](http://arxiv.org/abs/2409.17020) |
| Authors | Jiang, Xiaoyan;Yang, Hang;Zhu, Kaiying;Qiu, Xihe;Zhao, Shibo;Zhou, Sifan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Referring Image Segmentation (RIS), aims to segment the object referred by a given sentence in an image by understanding both visual and linguistic information.
- However, existing RIS methods tend to explore top-performance models, disregarding considerations for practical applications on resources-limited edge devices.
- This oversight poses a significant challenge for on-device RIS inference.

## Task

* Perception
* Software Tools

## Keywords

* Robotics in Under-Resourced Settings
* Object Detection
* Segmentation and Categorization
* Semantic Scene Understanding

## AI依存度

* Non-AI

## 何を解決？

* Referring Image Segmentation (RIS), aims to segment the object referred by a given sentence in an image by understanding both visual and linguistic information.

## 何が新しい？

* To this end, we propose an effective and efficient post-training quantization framework termed PTQ4RIS.

## どうやってる？

* However, existing RIS methods tend to explore top-performance models, disregarding considerations for practical applications on resources-limited edge devices.

## どこが強い？

* Extensive experiments on three benchmarks with different bits settings (from 8 to 4 bits) demonstrates its superior performance.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we propose an effective and efficient post-training quantization framework termed PTQ4RIS.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
