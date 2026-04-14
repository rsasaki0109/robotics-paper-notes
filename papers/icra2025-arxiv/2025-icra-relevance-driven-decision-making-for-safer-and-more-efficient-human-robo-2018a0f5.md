# Relevance-Driven Decision Making for Safer and More Efficient Human Robot Collaboration

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Human Motion Sensing |
| arXiv | [http://arxiv.org/abs/2409.13998](http://arxiv.org/abs/2409.13998) |
| Authors | Zhang, Xiaotong, Huang, Dingcheng, Youcef-Toumi, Kamal |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we present an enhanced two-loop framework that integrates real-time and asynchronous processing to quantify relevance and leverage it for safer and more efficient human-robot collaboration (HRC).
- Inspired by this cognitive mechanism, we introduced a novel concept termed relevance for Human-Robot Collaboration (HRC).
- Simulations and experiments show that our methodology for relevance quantification can accurately and robustly predict the human objective and relevance, with an average accuracy of up to 0.90 for objective prediction and up to 0.96 for relevance prediction.

## Task

* Perception
* Motion Planning

## Keywords

* Human-Robot Collaboration / Cognitive Modeling / Collision Avoidance

## AI依存度

* AI-heavy

## 何を解決？

* Human brain possesses the ability to effectively focus on important environmental components, which enhances perception, learning, reasoning, and decision-making.

## 何が新しい？

* Inspired by this cognitive mechanism, we introduced a novel concept termed relevance for Human-Robot Collaboration (HRC).

## どうやってる？

* Human brain possesses the ability to effectively focus on important environmental components, which enhances perception, learning, reasoning, and decision-making.

## どこが強い？

* Simulations and experiments show that our methodology for relevance quantification can accurately and robustly predict the human objective and relevance, with an average accuracy of up to 0.90 for objective prediction and up to 0.96 for relevance prediction.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* Moreover, our motion generation methodology reduces collision cases by 63.76% and collision frames by 44.74% when compared with a state-of-the-art (SOTA) collision avoidance method.

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: perception, planning
* 実用性: 少なくともシミュレーション評価はあるが、実運用への外挿は追加確認が必要。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
