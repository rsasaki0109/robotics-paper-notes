# Fast Global Localization on Neural Radiance Field

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Localization 2 |
| arXiv | [http://arxiv.org/abs/2406.12202](http://arxiv.org/abs/2406.12202) |
| Authors | Kong, Mangyu;Lee, Jaewon;Lee, Seongwon;Kim, Euntai |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Neural Radiance Fields (NeRF) presented a novel way to represent scenes, allowing for high-quality 3D reconstruction from 2D images.
- Following its remarkable achievements, global localization within NeRF maps is an essential task for enabling a wide range of applications.
- Recently, Loc-NeRF demonstrated a localization approach that combines traditional Monte Carlo Localization with NeRF, showing promising results for using NeRF as an environment map.

## Task

* SLAM
* Localization
* Perception
* Software Tools

## Keywords

* Localization
* Mapping
* SLAM

## AI依存度

* AI-heavy

## 何を解決？

* Neural Radiance Fields (NeRF) presented a novel way to represent scenes, allowing for high-quality 3D reconstruction from 2D images.

## 何が新しい？

* We propose a particle rejection weighting strategy that estimates the uncertainty of particles by leveraging NeRFs inherent characteristics and incorporates them into the particle weighting process to reject abnormal particles.

## どうやってる？

* Recently, Loc-NeRF demonstrated a localization approach that combines traditional Monte Carlo Localization with NeRF, showing promising results for using NeRF as an environment map.

## どこが強い？

* Recently, Loc-NeRF demonstrated a localization approach that combines traditional Monte Carlo Localization with NeRF, showing promising results for using NeRF as an environment map.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a particle rejection weighting strategy that estimates the uncertainty of particles by leveraging NeRFs inherent characteristics and incorporates them into the particle weighting process to reject abnormal particles.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
