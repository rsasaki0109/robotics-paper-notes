# Robotic Sim-To-Real Transfer for Long-Horizon Pick-And-Place Tasks in the Robotic Sim2Real Competition

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation 1 |
| arXiv | [http://arxiv.org/abs/2503.11012](http://arxiv.org/abs/2503.11012) |
| Authors | Yang, Ming, Cao, Hongyu, Zhao, Lixuan, Zhang, Chenrui, Chen, Yaran |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper presents a fully autonomous robotic system that performs sim-to-real transfer in complex long-horizon tasks involving navigation, recognition, grasping, and stacking in an environment with multiple obstacles.
- The key feature of the system is the ability to overcome typical sensing and actuation discrepancies during sim-to-real transfer and to achieve consistent performance without any algorithmic modifications.
- The visual perception system achieves the speed of 11 ms per frame due to its lightweight nature, and the servo system achieves sub-centimeter accuracy with the proposed controller.

## Task

* Perception
* Control
* Manipulation

## Keywords

* Engineering for Robotic Systems / Mobile Manipulation / Perception for Grasping and Manipulation

## AI依存度

* Non-AI

## 何を解決？

* Our robotic system took first place in the mineral searching task of the Robotic Sim2Real Challenge hosted at ICRA 2024.

## 何が新しい？

* Abstract ベースでは、提案手法のコア設計を本文で要確認。

## どうやってる？

* The visual perception system achieves the speed of 11 ms per frame due to its lightweight nature, and the servo system achieves sub-centimeter accuracy with the proposed controller.

## どこが強い？

* The key feature of the system is the ability to overcome typical sensing and actuation discrepancies during sim-to-real transfer and to achieve consistent performance without any algorithmic modifications.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
