# Prompt-Responsive Object Retrieval with Memory-Augmented Student-Teacher Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation 4 |
| arXiv | [http://arxiv.org/abs/2505.02232](http://arxiv.org/abs/2505.02232) |
| Authors | Mosbach, Malte, Behnke, Sven |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paradigm holds significant potential for robotics problems, such as targeted manipulation amidst clutter.
- In this work, we present a novel approach to combine promptable foundation models with reinforcement learning (RL), enabling robots to perform dexterous manipulation tasks in a prompt-responsive manner.
- Our approach successfully learns prompt-responsive policies, demonstrated in picking objects from cluttered scenes.

## Task

* Perception
* Control
* State Estimation
* Manipulation

## Keywords

* Reinforcement Learning / Dexterous Manipulation / Grasping

## AI依存度

* AI-heavy

## 何を解決？

* This paradigm holds significant potential for robotics problems, such as targeted manipulation amidst clutter.

## 何が新しい？

* In this work, we present a novel approach to combine promptable foundation models with reinforcement learning (RL), enabling robots to perform dexterous manipulation tasks in a prompt-responsive manner.

## どうやってる？

* Building models responsive to input prompts represents a transformative shift in machine learning.

## どこが強い？

* Our approach successfully learns prompt-responsive policies, demonstrated in picking objects from cluttered scenes.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: perception, control, state estimation / localization
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
