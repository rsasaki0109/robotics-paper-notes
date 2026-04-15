# FLEX: A Framework for Learning Robot-Agnostic Force-Based Skills Involving Sustained Contact Object Manipulation

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Reinforcement Learning 4 |
| arXiv | [http://arxiv.org/abs/2503.13418](http://arxiv.org/abs/2503.13418) |
| Authors | Fang, Shijie;Gao, Wenchang;Goel, Shivam;Thierauf, Christopher;Scheutz, Matthias;Sinapov, Jivko |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Learning to manipulate objects efficiently, particularly those involving sustained contact (e.g., pushing, sliding) and articulated parts (e.g., drawers, doors), presents significant challenges.
- Traditional methods, such as robot-centric reinforcement learning (RL), imitation learning, and hybrid techniques, require massive training and often struggle to generalize across different objects and robot platforms.
- We propose a novel framework for learning object-centric manipulation policies in textit{force space}, decoupling the robot from the object.

## Task

* Visual-Inertial
* Control
* Manipulation

## Keywords

* Machine Learning for Robot Control
* Reinforcement Learning
* Deep Learning in Grasping and Manipulation

## AI依存度

* Hybrid

## 何を解決？

* Learning to manipulate objects efficiently, particularly those involving sustained contact (e.g., pushing, sliding) and articulated parts (e.g., drawers, doors), presents significant challenges.

## 何が新しい？

* We propose a novel framework for learning object-centric manipulation policies in textit{force space}, decoupling the robot from the object.

## どうやってる？

* Traditional methods, such as robot-centric reinforcement learning (RL), imitation learning, and hybrid techniques, require massive training and often struggle to generalize across different objects and robot platforms.

## どこが強い？

* Our evaluations demonstrate that the method significantly outperforms baselines, achieving over an order of magnitude improvement in training efficiency compared to other state-of-the-art methods.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose a novel framework for learning object-centric manipulation policies in textit{force space}, decoupling the robot from the object.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
