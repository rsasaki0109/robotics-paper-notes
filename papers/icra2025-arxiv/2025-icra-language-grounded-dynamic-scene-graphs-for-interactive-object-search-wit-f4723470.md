# Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Large Models for Manipulation |
| arXiv | [http://arxiv.org/abs/2403.08605](http://arxiv.org/abs/2403.08605) |
| Authors | Honerkamp, Daniel, Büchner, Martin, Despinoy, Fabien, Welschehold, Tim, Valada, Abhinav |
| Source | ICRA 2025 / arXiv |

## TL;DR

- To fully leverage the capabilities of mobile manipulation robots, it is imperative that they are able to autonomously execute long-horizon tasks in large unexplored environments.
- In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from open-vocabulary scene graphs, dynamically updated as the environment is explored.
- While large language models (LLMs) have shown emergent reasoning skills on arbitrary tasks, existing work primarily concentrates on explored environments, typically focusing on either navigation or manipulation tasks in isolation.

## Task

* Perception
* Motion Planning
* Manipulation

## Keywords

* Mobile Manipulation / Integrated Planning and Learning / Domestic Robotics

## AI依存度

* AI-heavy

## 何を解決？

* To fully leverage the capabilities of mobile manipulation robots, it is imperative that they are able to autonomously execute long-horizon tasks in large unexplored environments.

## 何が新しい？

* In this work, we propose MoMa-LLM, a novel approach that grounds language models within structured representations derived from open-vocabulary scene graphs, dynamically updated as the environment is explored.

## どうやってる？

* The resulting approach, given object detections, is zero-shot, open-vocabulary, and readily extendable to a spectrum of mobile manipulation and household robotic tasks.

## どこが強い？

* We demonstrate the effectiveness of MoMa-LLM in a novel semantic interactive search task in large realistic indoor environments.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* In extensive experiments in both simulation and the real world, we show substantially improved search efficiency compared to conventional baselines and state-of-the-art approaches, as well as its applicability to more abstract tasks.

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
