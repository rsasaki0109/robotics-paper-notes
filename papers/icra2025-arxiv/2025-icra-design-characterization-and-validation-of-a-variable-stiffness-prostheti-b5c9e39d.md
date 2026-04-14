# Design, Characterization, and Validation of a Variable Stiffness Prosthetic Elbow

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Wearable Robotics 2 |
| arXiv | [http://arxiv.org/abs/2412.03985](http://arxiv.org/abs/2412.03985) |
| Authors | Milazzo, Giuseppe, Lemerle, Simon, Grioli, Giorgio, Bicchi, Antonio, Catalano, Manuel Giuseppe |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Intuitively, prostheses with user-controllable stiffness could mimic the intrinsic behavior of the human musculoskeletal system, promoting safe and natural interactions and task adaptability in real-world scenarios.
- In addition, we introduce a variant of this design where the two motors are split in the upper arm and forearm to distribute mass and volume more evenly along the bionic limb, enhancing comfort for patients with more proximal amputation levels.
- The system attains the desired 120�?range of motion, achieves the target stiffness range of [2, 60] N �?m/rad, and can actively lift up to 3 kg.

## Task

* Control

## Keywords

* Prosthetics and Exoskeletons / Variable Stiffness Actuators / Compliant Joint/Mechanism / Mechanism Design

## AI依存度

* Non-AI

## 何を解決？

* However, prosthetic design often disregards compliance because of the additional complexity, weight, and needed control channels.

## 何が新しい？

* In addition, we introduce a variant of this design where the two motors are split in the upper arm and forearm to distribute mass and volume more evenly along the bionic limb, enhancing comfort for patients with more proximal amputation levels.

## どうやってる？

* Intuitively, prostheses with user-controllable stiffness could mimic the intrinsic behavior of the human musculoskeletal system, promoting safe and natural interactions and task adaptability in real-world scenarios.

## どこが強い？

* The system attains the desired 120�?range of motion, achieves the target stiffness range of [2, 60] N �?m/rad, and can actively lift up to 3 kg.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Our novel design reduces weight by up to 50% compared to existing VSAs for elbow prostheses while achieving performance comparable to the state of the art.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: control
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
