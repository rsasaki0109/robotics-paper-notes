# ZeroMimic: Distilling Robotic Manipulation Skills from Web Videos

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Imitation Learning for Manipulation 2 |
| arXiv | [http://arxiv.org/abs/2503.23877](http://arxiv.org/abs/2503.23877) |
| Authors | Shi, Junyao;Zhao, Zhuolun;Wang, Tianyou;Pedroza, Ian;Luo, Amy;Wang, Jie;Ma, Yecheng Jason;Jayaraman, Dinesh |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Many recent advances in robotic manipulation have come through imitation learning, yet these rely largely on mimicking a particularly hard-to-acquire form of demonstrations: those collected on the same robot in the same room with the same objects as the trained policy must handle at test time.
- In contrast, large pre-recorded human video datasets demonstrating manipulation skills in-the-wild already exist, which contain valuable information for robots.
- Is it possible to distill a repository of useful robotic skill policies out of such data without any additional requirements on robot-specific demonstrations or exploration?

## Task

* Visual-Inertial
* Manipulation
* Software Tools

## Keywords

* Imitation Learning
* Sensorimotor Learning
* Transfer Learning

## AI依存度

* Hybrid

## 何を解決？

* Many recent advances in robotic manipulation have come through imitation learning, yet these rely largely on mimicking a particularly hard-to-acquire form of demonstrations: those collected on the same robot in the same room with the same objects as the trained policy must handle at test time.

## 何が新しい？

* We present the first such system ZeroMimic, that generates immediately deployable image goal-conditioned skill policies for several common categories of manipulation tasks (opening, closing, pouring, pick&place, cutting, and stirring) each capable of acting upon diverse objects and across diverse unseen task setups.

## どうやってる？

* Many recent advances in robotic manipulation have come through imitation learning, yet these rely largely on mimicking a particularly hard-to-acquire form of demonstrations: those collected on the same robot in the same room with the same objects as the trained policy must handle at test time.

## どこが強い？

* After training ZeroMimic on the popular EpicKitchens dataset of ego-centric human videos, we evaluate its out-of-the-box performance in varied real-world and simulated kitchen settings with two different robot embodiments, demonstrating its impressive abilities to handle these varied tasks.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We present the first such system ZeroMimic, that generates immediately deployable image goal-conditioned skill policies for several common categories of manipulation tasks (opening, closing, pouring, pick&place, cutting, and stirring) each capable of acting upon diverse objects and across diverse unseen task setups.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
