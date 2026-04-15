# Ergodic Exploration Over Meshable Surfaces

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Active Sensing |
| arXiv | [http://arxiv.org/abs/2503.05026](http://arxiv.org/abs/2503.05026) |
| Authors | Dong, Dayi, E;Xu, Albert;Gutow, Geordan;Choset, Howie;Abraham, Ian |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robotic search and rescue, exploration, and inspection require trajectory planning across a variety of domains.
- A popular approach to trajectory planning for these types of missions is ergodic search, which biases a trajectory to spend time in parts of the exploration domain that are believed to contain more information.
- Most prior work on ergodic search has been limited to searching simple surfaces, like a 2D Euclidean plane or a sphere, as they rely on projecting functions defined on the exploration domain onto analytically obtained Fourier basis functions.

## Task

* Motion Planning

## Keywords

* Motion and Path Planning
* Search and Rescue Robots
* Computational Geometry

## AI依存度

* Non-AI

## 何を解決？

* Robotic search and rescue, exploration, and inspection require trajectory planning across a variety of domains.

## 何が新しい？

* We demonstrate that on domains where analytical basis functions are available (plane, sphere), the proposed method obtains equivalent results, and while on other domains (torus, bunny, wind turbine), the approach is versatile enough to still search effectively.

## どうやってる？

* The basis functions are approximated through finite element methods on a triangle mesh of the domain.

## どこが強い？

* We demonstrate that on domains where analytical basis functions are available (plane, sphere), the proposed method obtains equivalent results, and while on other domains (torus, bunny, wind turbine), the approach is versatile enough to still search effectively.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We demonstrate that on domains where analytical basis functions are available (plane, sphere), the proposed method obtains equivalent results, and while on other domains (torus, bunny, wind turbine), the approach is versatile enough to still search effectively.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
