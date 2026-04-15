# A Helping (Human) Hand in Kinematic Structure Estimation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manipulation Planning and Control 1 |
| arXiv | [http://arxiv.org/abs/2503.05301](http://arxiv.org/abs/2503.05301) |
| Authors | Pfisterer, Adrian;Li, Xing;Mengers, Vito;Brock, Oliver |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Visual uncertainties such as occlusions, lack of texture, and noise present significant challenges in obtaining accurate kinematic models for safe robotic manipulation.
- We introduce a probabilistic real-time approach that leverages the human hand as a prior to mitigate these uncertainties.
- By tracking the constrained motion of the human hand during manipulation and explicitly modeling uncertainties in visual observations, our method reliably estimates an objects kinematic model online.

## Task

* Manipulation
* Perception
* Software Tools

## Keywords

* RGB-D Perception
* Probability and Statistical Methods
* Learning from Demonstration

## AI依存度

* Hybrid

## 何を解決？

* Visual uncertainties such as occlusions, lack of texture, and noise present significant challenges in obtaining accurate kinematic models for safe robotic manipulation.

## 何が新しい？

* Visual uncertainties such as occlusions, lack of texture, and noise present significant challenges in obtaining accurate kinematic models for safe robotic manipulation.

## どうやってる？

* By tracking the constrained motion of the human hand during manipulation and explicitly modeling uncertainties in visual observations, our method reliably estimates an objects kinematic model online.

## どこが強い？

* The results demonstrate that by incorporating an appropriate prior and explicitly accounting for uncertainties, our method produces accurate estimates, outperforming two recent baselines by 195% and 140%, respectively.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Visual uncertainties such as occlusions, lack of texture, and noise present significant challenges in obtaining accurate kinematic models for safe robotic manipulation.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
