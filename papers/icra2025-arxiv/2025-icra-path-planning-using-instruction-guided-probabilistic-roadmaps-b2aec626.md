# Path Planning Using Instruction-Guided Probabilistic Roadmaps

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning 1 |
| arXiv | [http://arxiv.org/abs/2502.16515](http://arxiv.org/abs/2502.16515) |
| Authors | Bao, Jiaqi, Yonetani, Ryo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- With IG-PRM, we aim to address this problem by allowing robot operators to specify such constraints through natural language instructions, such as ``aim for wider paths'' or ``mind small gaps''.
- This work presents a novel data-driven path planning algorithm named Instruction-Guided Probabilistic Roadmap (IG-PRM).
- Experimental results demonstrate the effectiveness of our approach on both synthetic and real-world indoor navigation environments.

## Task

* Motion Planning
* Intelligent Vehicles

## Keywords

* Integrated Planning and Learning / Motion and Path Planning / Autonomous Vehicle Navigation

## AI依存度

* AI-heavy

## 何を解決？

* With IG-PRM, we aim to address this problem by allowing robot operators to specify such constraints through natural language instructions, such as ``aim for wider paths'' or ``mind small gaps''.

## 何が新しい？

* This work presents a novel data-driven path planning algorithm named Instruction-Guided Probabilistic Roadmap (IG-PRM).

## どうやってる？

* Despite the recent development and widespread use of mobile robot navigation, the safe and effective travels of mobile robots still require significant engineering effort to take into account the constraints of robots and their tasks.

## どこが強い？

* Experimental results demonstrate the effectiveness of our approach on both synthetic and real-world indoor navigation environments.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
