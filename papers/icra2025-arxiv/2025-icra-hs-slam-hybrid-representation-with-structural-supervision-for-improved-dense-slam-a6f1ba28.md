# HS-SLAM: Hybrid Representation with Structural Supervision for Improved Dense SLAM

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning-Based SLAM 1 |
| arXiv | [http://arxiv.org/abs/2503.21778](http://arxiv.org/abs/2503.21778) |
| Authors | Gong, Ziren;Tosi, Fabio;Zhang, Youmin;Mattoccia, Stefano;Poggi, Matteo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- NeRF-based SLAM has recently achieved promising results in tracking and reconstruction.
- However, existing methods face challenges in providing sufficient scene representation, capturing structural information, and maintaining global consistency in scenes emerging significant movement or being forgotten.
- To this end, we present HS-SLAM to tackle these problems.

## Task

* SLAM
* Localization
* Perception

## Keywords

* SLAM
* Mapping
* Localization

## AI依存度

* AI-heavy

## 何を解決？

* NeRF-based SLAM has recently achieved promising results in tracking and reconstruction.

## 何が新しい？

* To enhance scene representation capacity, we propose a hybrid encoding network that combines the complementary strengths of hash-grid, tri-planes, and one-blob, improving the completeness and smoothness of reconstruction.

## どうやってる？

* However, existing methods face challenges in providing sufficient scene representation, capturing structural information, and maintaining global consistency in scenes emerging significant movement or being forgotten.

## どこが強い？

* Experimental results demonstrate that HS-SLAM outperforms the baselines in tracking and reconstruction accuracy while maintaining the efficiency required for robotics.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To enhance scene representation capacity, we propose a hybrid encoding network that combines the complementary strengths of hash-grid, tri-planes, and one-blob, improving the completeness and smoothness of reconstruction.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
