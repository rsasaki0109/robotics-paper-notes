# PseudoTouch: Efficiently Imaging the Surface Feel of Objects for Robotic Manipulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception for Manipulation 4 |
| arXiv | [http://arxiv.org/abs/2403.15107](http://arxiv.org/abs/2403.15107) |
| Authors | Röfer, Adrian;Heppert, Nick;Ayad, Abdallah;Chisari, Eugenio;Valada, Abhinav |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Tactile sensing is vital for human dexterous manipulation, however, it has not been widely used in robotics.
- Compact, low-cost sensing platforms can facilitate a change, but unlike their popular optical counterparts, they are difficult to deploy in high-fidelity tasks due to their low signal dimensionality and lack of a simulation model.
- To overcome these challenges, we introduce PseudoTouch which links high-dimensional structural information to low-dimensional sensor signals.

## Task

* LiDAR
* Visual-Inertial
* Manipulation
* Perception

## Keywords

* Perception for Grasping and Manipulation
* Force and Tactile Sensing
* Representation Learning

## AI依存度

* Hybrid

## 何を解決？

* Tactile sensing is vital for human dexterous manipulation, however, it has not been widely used in robotics.

## 何が新しい？

* To overcome these challenges, we introduce PseudoTouch which links high-dimensional structural information to low-dimensional sensor signals.

## どうやってる？

* Our approach yields a 32% absolute improvement in accuracy compared to the baseline relying on partial point cloud data.

## どこが強い？

* We demonstrate the utility of our trained PseudoTouch model in two downstream tasks: object recognition and grasp stability prediction.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To overcome these challenges, we introduce PseudoTouch which links high-dimensional structural information to low-dimensional sensor signals.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
