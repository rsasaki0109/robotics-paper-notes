# Equivariant IMU Preintegration with Biases: A Galilean Group Approach

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | State Estimation |
| arXiv | [http://arxiv.org/abs/2411.05548](http://arxiv.org/abs/2411.05548) |
| Authors | Delama, Giulio, Fornasier, Alessandro, Mahony, Robert, Weiss, Stephan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This letter proposes a new approach for Inertial Measurement Unit (IMU) preintegration, a fundamental building block that can be leveraged in different optimization-based Inertial Navigation System (INS) localization solutions.
- Our method improves in consistency compared to existing preintegration approaches which treat IMU biases as a separate state-space.
- Inspired by recent advances in equivariant theory applied to biased INSs, we derive a discrete-time formulation of the IMU preintegration on Gal(3) �?gal(3), the left-trivialization of the tangent group of the Galilean group Gal(3).

## Task

* SLAM
* Localization
* Sensor Fusion
* State Estimation

## Keywords

* Localization / Sensor Fusion / Visual-Inertial SLAM

## AI依存度

* Non-AI

## 何を解決？

* This letter proposes a new approach for Inertial Measurement Unit (IMU) preintegration, a fundamental building block that can be leveraged in different optimization-based Inertial Navigation System (INS) localization solutions.

## 何が新しい？

* We define a novel preintegration error that geometrically couples the navigation states and the bias leading to lower linearization error.

## どうやってる？

* This letter proposes a new approach for Inertial Measurement Unit (IMU) preintegration, a fundamental building block that can be leveraged in different optimization-based Inertial Navigation System (INS) localization solutions.

## どこが強い？

* Extensive validation against state-of-the-art methods, both in simulation and with real-world IMU data, implementation in the Lie++ library, and open-source code are provided.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Our method improves in consistency compared to existing preintegration approaches which treat IMU biases as a separate state-space.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: localization / mapping, localization, perception / localization fusion
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
