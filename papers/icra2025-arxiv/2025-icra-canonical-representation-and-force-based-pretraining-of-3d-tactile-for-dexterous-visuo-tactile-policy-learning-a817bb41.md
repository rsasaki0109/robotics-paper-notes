# Canonical Representation and Force-Based Pretraining of 3D Tactile for Dexterous Visuo-Tactile Policy Learning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Multifingered Hands |
| arXiv | [http://arxiv.org/abs/2409.17549](http://arxiv.org/abs/2409.17549) |
| Authors | Wu, Tianhao;Li, Jinzhou;Zhang, Jiyao;Mingdong Wu, Aaron;Dong, Hao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Tactile sensing plays a vital role in enabling robots to perform fine-grained, contact-rich tasks.
- However, the high dimensionality of tactile data, due to the large coverage on dexterous hands, poses significant challenges for effective tactile feature learning, especially for 3D tactile data, as there are no large standardized datasets and no strong pretrained backbones.
- To address these challenges, we propose a novel canonical representation that reduces the difficulty of 3D tactile feature learning and further introduces a force-based self-supervised pretraining task to capture both local and net force features, which are crucial for dexterous manipulation.

## Task

* Manipulation
* Software Tools

## Keywords

* Dexterous Manipulation
* Multifingered Hands
* Force and Tactile Sensing

## AI依存度

* Hybrid

## 何を解決？

* Tactile sensing plays a vital role in enabling robots to perform fine-grained, contact-rich tasks.

## 何が新しい？

* To address these challenges, we propose a novel canonical representation that reduces the difficulty of 3D tactile feature learning and further introduces a force-based self-supervised pretraining task to capture both local and net force features, which are crucial for dexterous manipulation.

## どうやってる？

* Our method achieves an average success rate of 78% across four fine-grained, contact-rich dexterous manipulation tasks in real-world experiments, demonstrating effectiveness and robustness compared to other methods.

## どこが強い？

* Our method achieves an average success rate of 78% across four fine-grained, contact-rich dexterous manipulation tasks in real-world experiments, demonstrating effectiveness and robustness compared to other methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address these challenges, we propose a novel canonical representation that reduces the difficulty of 3D tactile feature learning and further introduces a force-based self-supervised pretraining task to capture both local and net force features, which are crucial for dexterous manipulation.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
