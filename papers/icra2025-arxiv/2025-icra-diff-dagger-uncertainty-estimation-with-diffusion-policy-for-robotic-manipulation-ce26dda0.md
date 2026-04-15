# Diff-DAgger: Uncertainty Estimation with Diffusion Policy for Robotic Manipulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Imitation Learning 1 |
| arXiv | [http://arxiv.org/abs/2410.14868](http://arxiv.org/abs/2410.14868) |
| Authors | Lee, Sung-Wook;Kang, Xuhui;Kuo, Yen-Ling |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recently, diffusion policy has shown impressive results in handling multi-modal tasks in robotic manipulation.
- However, it has fundamental limitations in out-of-distribution failures that persist due to compounding errors and its limited capability to extrapolate.
- One way to address these limitations is robot-gated DAgger, an interactive imitation learning with a robot query system to actively seek expert help during policy rollout.

## Task

* Manipulation
* Software Tools

## Keywords

* Imitation Learning
* Deep Learning in Grasping and Manipulation
* Learning from Demonstration

## AI依存度

* AI-heavy

## 何を解決？

* Recently, diffusion policy has shown impressive results in handling multi-modal tasks in robotic manipulation.

## 何が新しい？

* To address this problem, we introduce Diff-DAgger, an efficient robot-gated DAgger algorithm that leverages the training objective of diffusion policy.

## どうやってる？

* While robot-gated DAgger has high potential for learning at scale, existing methods like Ensemble-DAgger struggle with highly expressive policies: They often misinterpret policy disagreements as uncertainty at multi-modal decision points.

## どこが強い？

* Recently, diffusion policy has shown impressive results in handling multi-modal tasks in robotic manipulation.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this problem, we introduce Diff-DAgger, an efficient robot-gated DAgger algorithm that leverages the training objective of diffusion policy.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
