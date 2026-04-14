# CurricuLLM: Automatic Task Curricula Design for Learning Complex Robot Skills Using Large Language Models

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Large Models for Manipulation |
| arXiv | [http://arxiv.org/abs/2409.18382](http://arxiv.org/abs/2409.18382) |
| Authors | Ryu, Kanghyun, Liao, Qiayuan, Li, Zhongyu, Delgosha, Payam, Sreenath, Koushil, Mehr, Negar |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Curriculum learning is a training mechanism in reinforcement learning (RL) that facilitates the achievement of complex policies by progressively increasing the task difficulty during training.
- In this work, we propose CurricuLLM, which leverages the high-level planning and programming capabilities of LLMs for curriculum design, thereby enhancing the efficient learning of complex target tasks.
- Additionally, the demonstrated success of LLMs in translating natural language into executable code for RL agents strengthens their role in generating task curricula.

## Task

* Motion Planning
* Control
* Manipulation

## Keywords

* Incremental Learning / Continual Learning / Transfer Learning

## AI依存度

* AI-heavy

## 何を解決？

* Curriculum learning is a training mechanism in reinforcement learning (RL) that facilitates the achievement of complex policies by progressively increasing the task difficulty during training.

## 何が新しい？

* In this work, we propose CurricuLLM, which leverages the high-level planning and programming capabilities of LLMs for curriculum design, thereby enhancing the efficient learning of complex target tasks.

## どうやってる？

* Curriculum learning is a training mechanism in reinforcement learning (RL) that facilitates the achievement of complex policies by progressively increasing the task difficulty during training.

## どこが強い？

* Curriculum learning is a training mechanism in reinforcement learning (RL) that facilitates the achievement of complex policies by progressively increasing the task difficulty during training.

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
* どのモジュールに効くか: planning, control, limited direct use; integration pattern reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
