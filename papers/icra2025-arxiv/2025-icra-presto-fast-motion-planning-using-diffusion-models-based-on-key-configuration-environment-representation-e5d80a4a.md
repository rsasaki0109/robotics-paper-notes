# PRESTO: Fast Motion Planning Using Diffusion Models Based on Key-Configuration Environment Representation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Integrating Motion Planning and Learning 2 |
| arXiv | [http://arxiv.org/abs/2409.16012](http://arxiv.org/abs/2409.16012) |
| Authors | Seo, Mingyo;Cho, Yoonyoung;Sung, Yoonchang;Stone, Peter;Zhu, Yuke;Kim, Beomjoon |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We introduce a learning-guided motion planning framework that generates seed trajectories using a diffusion model for trajectory optimization.
- Given a workspace, our method approximates the configuration space (C-space) obstacles through an environment representation consisting of a sparse set of task-related key configurations, which is then used as a conditioning input to the diffusion model.
- The diffusion model integrates regularization terms that encourage smooth, collision-free trajectories during training, and trajectory optimization refines the generated seed trajectories to correct any colliding segments.

## Task

* Motion Planning

## Keywords

* Motion and Path Planning
* Collision Avoidance
* Integrated Planning and Learning

## AI依存度

* AI-heavy

## 何を解決？

* We introduce a learning-guided motion planning framework that generates seed trajectories using a diffusion model for trajectory optimization.

## 何が新しい？

* Given a workspace, our method approximates the configuration space (C-space) obstacles through an environment representation consisting of a sparse set of task-related key configurations, which is then used as a conditioning input to the diffusion model.

## どうやってる？

* Given a workspace, our method approximates the configuration space (C-space) obstacles through an environment representation consisting of a sparse set of task-related key configurations, which is then used as a conditioning input to the diffusion model.

## どこが強い？

* Our experimental results demonstrate that high-quality trajectory priors, learned through our C-space-grounded diffusion model, enable the efficient generation of collision-free trajectories in narrow-passage environments, outperforming previous learning- and planning-based baselines.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Given a workspace, our method approximates the configuration space (C-space) obstacles through an environment representation consisting of a sparse set of task-related key configurations, which is then used as a conditioning input to the diffusion model.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
