# TransDiff: Diffusion-Based Method for Manipulating Transparent Objects Using a Single RGB-D Image

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning Based Planning for Manipulation 2 |
| arXiv | [http://arxiv.org/abs/2503.12779](http://arxiv.org/abs/2503.12779) |
| Authors | Wang, Haoxiao;Zhou, Kaichen;Gu, Binrui;Feng, ZhiYuan;Wang, Weijie;Sun, Peilin;Xiao, Yicheng;Zhang, Jianhua;Dong, Hao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Manipulating transparent objects presents significant challenges due to the complexities introduced by their reflection and refraction properties, which considerably hinder the accurate estimation of their 3D shapes.
- To address these challenges, we, for the first time, propose a single-view RGB-D-based depth completion framework, TransDiff, that leverages the Denoising Diffusion Probabilistic Models(DDPM) to achieve material-agnostic object grasping in desktop.
- Specifically, we leverage features extracted from RGB images, including semantic segmentation, edge maps, and normal maps, to condition the depth map generation process.

## Task

* Manipulation
* Perception
* Software Tools

## Keywords

* AI-Based Methods
* Grippers and Other End-Effectors

## AI依存度

* AI-heavy

## 何を解決？

* Manipulating transparent objects presents significant challenges due to the complexities introduced by their reflection and refraction properties, which considerably hinder the accurate estimation of their 3D shapes.

## 何が新しい？

* To address these challenges, we, for the first time, propose a single-view RGB-D-based depth completion framework, TransDiff, that leverages the Denoising Diffusion Probabilistic Models(DDPM) to achieve material-agnostic object grasping in desktop.

## どうやってる？

* Our method learns an iterative denoising process that transforms a random depth distribution into a depth map, guided by initially refined depth information, ensuring more accurate depth estimation in scenarios involving transparent objects.

## どこが強い？

* Through comprehensive experimental validation, we demonstrate that our method significantly outperforms the baselines in both synthetic and real-world benchmarks with acceptable inference time.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these challenges, we, for the first time, propose a single-view RGB-D-based depth completion framework, TransDiff, that leverages the Denoising Diffusion Probabilistic Models(DDPM) to achieve material-agnostic object grasping in desktop.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
