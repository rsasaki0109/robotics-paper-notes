# NavFormer: A Transformer Architecture for Robot Target-Driven Navigation in Unknown and Dynamic Environments

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning for Navigation |
| arXiv | [http://arxiv.org/abs/2402.06838](http://arxiv.org/abs/2402.06838) |
| Authors | Wang, Haitong, Tan, Aaron Hao, Nejat, Goldie |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we introduce NavFormer, a novel end-to-end transformer architecture developed for robot target-driven navigation in unknown and dynamic environments.
- In unknown cluttered and dynamic environments such as disaster scenes, mobile robots need to perform target-driven navigation in order to find people or objects of interest, where the only information provided about these targets are images of the individual targets.
- Simulated experiments demonstrate that NavFormer can effectively navigate a mobile robot in diverse unknown environments, outperforming existing state-of-the-art methods.

## Task

* Robotics

## Keywords

* Vision-Based Navigation / Search and Rescue Robots / AI-Enabled Robotics

## AI依存度

* AI-heavy

## 何を解決？

* In unknown cluttered and dynamic environments such as disaster scenes, mobile robots need to perform target-driven navigation in order to find people or objects of interest, where the only information provided about these targets are images of the individual targets.

## 何が新しい？

* In this paper, we introduce NavFormer, a novel end-to-end transformer architecture developed for robot target-driven navigation in unknown and dynamic environments.

## どうやってる？

* NavFormer leverages the strengths of both 1) transformers for sequential data processing and 2) self-supervised learning (SSL) for visual representation to reason about spatial layouts and to perform collision-avoidance in dynamic settings.

## どこが強い？

* Simulated experiments demonstrate that NavFormer can effectively navigate a mobile robot in diverse unknown environments, outperforming existing state-of-the-art methods.

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
* どのモジュールに効くか: architecture reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
