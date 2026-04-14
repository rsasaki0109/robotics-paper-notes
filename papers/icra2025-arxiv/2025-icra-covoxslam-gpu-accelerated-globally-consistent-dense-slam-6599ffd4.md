# CoVoxSLAM: GPU Accelerated Globally Consistent Dense SLAM

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | SLAM 4 |
| arXiv | [http://arxiv.org/abs/2410.21149](http://arxiv.org/abs/2410.21149) |
| Authors | Hoss, Emiliano, De Cristóforis, Pablo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- A dense SLAM system is essential for mobile robots, as it provides localization and allows navigation, path planning, obstacle avoidance, and decision making in unstructured environments.
- In this work, we present coVoxSLAM, a novel GPU-accelerated volumetric SLAM system that takes full advantage of the parallel processing power of the GPU to build globally consistent maps even in large-scale environments.
- The results obtained using public datasets show that coVoxSLAM delivers a significant performance improvement considering execution times while maintaining accurate localization.

## Task

* SLAM
* Localization
* Mapping
* Motion Planning

## Keywords

* SLAM / Mapping / Embedded Systems for Robotic and Automation

## AI依存度

* Non-AI

## 何を解決？

* A dense SLAM system is essential for mobile robots, as it provides localization and allows navigation, path planning, obstacle avoidance, and decision making in unstructured environments.

## 何が新しい？

* In this work, we present coVoxSLAM, a novel GPU-accelerated volumetric SLAM system that takes full advantage of the parallel processing power of the GPU to build globally consistent maps even in large-scale environments.

## どうやってる？

* Due to increasing computational demands, the use of GPUs in dense SLAM is expanding.

## どこが強い？

* The results obtained using public datasets show that coVoxSLAM delivers a significant performance improvement considering execution times while maintaining accurate localization.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* It was deployed on different platforms (discrete and embedded GPUs) and compared with the state-of-the-art.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: localization / mapping, localization, map / localization
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
