# CANVAS: Commonsense-Aware Navigation System for Intuitive Human-Robot Interaction

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Navigation 2 |
| arXiv | [http://arxiv.org/abs/2410.01273](http://arxiv.org/abs/2410.01273) |
| Authors | Suhwan, Choi;Cho, Yongjun;Kim, Minchan;Jung, Jaeyoon;Joe, Myunchul;Park, Yu Been;Kim, Minseo;Kim, Sungwoong;Lee, Sungjae;Park, Whiseong;Chung, Jiwan;Yu, Youngjae |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Real-life robot navigation involves more than just reaching a destination; it requires optimizing movements while addressing scenario-specific goals.
- An intuitive way for humans to express these goals is through abstract cues like verbal commands or rough sketches.
- Such human guidance may lack details or be noisy.

## Task

* Visual-Inertial
* Human-Robot Interaction
* Software Tools

## Keywords

* Autonomous Vehicle Navigation
* Human-Robot Collaboration
* Imitation Learning

## AI依存度

* Hybrid

## 何を解決？

* Real-life robot navigation involves more than just reaching a destination; it requires optimizing movements while addressing scenario-specific goals.

## 何が新しい？

* We present COMMAND, a comprehensive dataset with human-annotated navigation results, spanning over 48 hours and 219 km, designed to train commonsense-aware navigation systems in simulated environments.

## どうやってる？

* To this end, we introduce CANVAS, a novel framework that combines visual and linguistic instructions for commonsense-aware navigation.

## どこが強い？

* Our experiments show that CANVAS outperforms the strong rule-based system ROS NavStack across all environments, demonstrating superior performance with noisy instructions.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We present COMMAND, a comprehensive dataset with human-annotated navigation results, spanning over 48 hours and 219 km, designed to train commonsense-aware navigation systems in simulated environments.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
