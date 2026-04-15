# ReloPush: Multi-Object Rearrangement in Confined Spaces with a Nonholonomic Mobile Robot Pusher

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation Planning and Control 2 |
| arXiv | [http://arxiv.org/abs/2409.18231](http://arxiv.org/abs/2409.18231) |
| Authors | Ahn, Jeeho;Mavrogiannis, Christoforos |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We focus on the problem of rearranging a set of objects within a confined space with a nonholonomically constrained mobile robot pusher.
- This problem is relevant to many real-world domains, including warehouse automation and construction.
- These domains give rise to instances involving a combination of geometric, kinematic, and physics constraints, which make planning particularly challenging.

## Task

* Motion Planning
* Manipulation

## Keywords

* Mobile Manipulation
* Task and Motion Planning
* Manipulation Planning

## AI依存度

* Non-AI

## 何を解決？

* We focus on the problem of rearranging a set of objects within a confined space with a nonholonomically constrained mobile robot pusher.

## 何が新しい？

* ReloPush exhibits orders of magnitude faster runtimes and significantly more robust execution in the real world, evidenced in lower execution times and fewer losses of object contact, compared to two baselines lacking our proposed graph structure.

## どうやってる？

* Based on this graph, we develop ReloPush, a planning framework that leverages Dubins curves and standard graph search techniques to generate an efficient sequence of object rearrangements to be executed by the pusher.

## どこが強い？

* We evaluate ReloPush across a series of challenging scenarios, involving the rearrangement of densely cluttered workspaces with up to eight objects by a 1tenth mobile robot pusher.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* ReloPush exhibits orders of magnitude faster runtimes and significantly more robust execution in the real world, evidenced in lower execution times and fewer losses of object contact, compared to two baselines lacking our proposed graph structure.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
