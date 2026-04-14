# CoDynTrust: Robust Asynchronous Collaborative Perception Via Dynamic Feature Trust Modulus

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Mobile Robots 1 |
| arXiv | [http://arxiv.org/abs/2502.08169](http://arxiv.org/abs/2502.08169) |
| Authors | Xu, Yunjiang, Li, Lingzhi, Wang, Jin, Yang, Benyuan, Wu, ZhiWen, Chen, Xinhong, Wang, Jianping |
| Source | ICRA 2025 / arXiv |

## TL;DR

- To tackle this challenge, we propose CoDynTrust, an uncertainty-encoded asynchronous fusion perception framework that is robust to the information mismatches caused by temporal asynchrony.
- Collaborative perception, fusing information from multiple agents, can extend perception range so as to improve perception performance.
- Experimental results demonstrate that CoDynTrust significantly reduces performance degradation caused by temporal asynchrony across multiple datasets, achieving state-of-the-art detection performance even with temporal asynchrony.

## Task

* Perception
* Sensor Fusion
* Motion Planning
* Control

## Keywords

* Object Detection / Segmentation and Categorization / Multi-Robot Systems / Intelligent Transportation Systems

## AI依存度

* Non-AI

## 何を解決？

* To tackle this challenge, we propose CoDynTrust, an uncertainty-encoded asynchronous fusion perception framework that is robust to the information mismatches caused by temporal asynchrony.

## 何が新しい？

* To tackle this challenge, we propose CoDynTrust, an uncertainty-encoded asynchronous fusion perception framework that is robust to the information mismatches caused by temporal asynchrony.

## どうやってる？

* However, temporal asynchrony in real-world environments, caused by communication delays, clock misalignment, or sampling configuration differences, can lead to information mismatches.

## どこが強い？

* Experimental results demonstrate that CoDynTrust significantly reduces performance degradation caused by temporal asynchrony across multiple datasets, achieving state-of-the-art detection performance even with temporal asynchrony.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Compared to existing works that also consider asynchronous collaborative perception, CoDynTrust combats various low-quality information in temporally asynchronous scenarios and allows uncertainty to be propagated to downstream tasks such as planning and control.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: perception, perception / localization fusion, planning
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
