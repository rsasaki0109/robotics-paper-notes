# PhysPart: Physically Plausible Part Completion for Interactable Objects

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Manipulation 1 |
| arXiv | [http://arxiv.org/abs/2408.13724](http://arxiv.org/abs/2408.13724) |
| Authors | Luo, Rundong;Geng, Haoran;Deng, Congyue;Li, Puhao;Wang, Zan;Jia, Baoxiong;Guibas, Leonidas;Huang, Siyuan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Interactable objects are ubiquitous in our daily lives.
- Recent advances in 3D generative models make it possible to automate the modeling of these objects, benefiting a range of applications from 3D printing to the creation of robot simulation environments.
- However, while significant progress has been made in modeling 3D shapes and appearances, modeling object physics, particularly for interactable objects, remains challenging due to the physical constraints imposed by inter-part motions.

## Task

* Visual-Inertial
* Manipulation
* Perception

## Keywords

* Perception for Grasping and Manipulation
* Manipulation Planning

## AI依存度

* AI-heavy

## 何を解決？

* Interactable objects are ubiquitous in our daily lives.

## 何が新しい？

* To this end, we propose a diffusion-based part generation model that utilizes geometric conditioning through classifier-free guidance and formulates physical constraints as a set of stability and mobility losses to guide the sampling process.

## どうやってる？

* Recent advances in 3D generative models make it possible to automate the modeling of these objects, benefiting a range of applications from 3D printing to the creation of robot simulation environments.

## どこが強い？

* Additionally, we demonstrate the generation of dependent parts, paving the way toward sequential part generation for objects with complex part-whole hierarchies.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To this end, we propose a diffusion-based part generation model that utilizes geometric conditioning through classifier-free guidance and formulates physical constraints as a set of stability and mobility losses to guide the sampling process.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
