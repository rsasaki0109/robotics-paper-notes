# Text2Robot: Evolutionary Robot Design from Text Descriptions

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Software Tools 1 |
| arXiv | [http://arxiv.org/abs/2406.19963](http://arxiv.org/abs/2406.19963) |
| Authors | Chen, Boyuan, Charlick, Zachary Samuel Charlick, Ringel, Ryan, Liu, Jiaxun, Xia, Boxi |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robot design has traditionally been costly and labor-intensive.
- We introduce Text2Robot, a framework that converts user text specifications and performance preferences into physical quadrupedal robots.
- Despite advancements in automated processes, it remains challenging to navigate a vast design space while producing physically manufacturable robots.

## Task

* Control
* Legged Robotics

## Keywords

* Methods and Tools for Robot System Design / Evolutionary Robotics

## AI依存度

* Non-AI

## 何を解決？

* Robot design has traditionally been costly and labor-intensive.

## 何が新しい？

* We introduce Text2Robot, a framework that converts user text specifications and performance preferences into physical quadrupedal robots.

## どうやってる？

* We introduce Text2Robot, a framework that converts user text specifications and performance preferences into physical quadrupedal robots.

## どこが強い？

* 評価条件や比較対象の強さは本文確認が必要。

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: control, limited direct use; estimator / controller design reference
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
