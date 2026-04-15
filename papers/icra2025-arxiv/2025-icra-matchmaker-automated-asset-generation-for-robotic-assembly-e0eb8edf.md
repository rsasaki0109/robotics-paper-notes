# MatchMaker: Automated Asset Generation for Robotic Assembly

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Manufacturing and Assembly Processes |
| arXiv | [http://arxiv.org/abs/2503.05887](http://arxiv.org/abs/2503.05887) |
| Authors | Wang, Yian;Tang, Bingjie;Gan, Chuang;Fox, Dieter;Mo, Kaichun;Narang, Yashraj;Akinola, Iretiayo |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robotic assembly remains a significant challenge due to complexities in visual perception, functional grasping, contact-rich manipulation, and performing high-precision tasks.
- Simulation-based learning and sim-to-real transfer have led to recent success in solving assembly tasks in the presence of object pose variation, perception noise, and control error; however, the development of a generalist (i.e., multi-task) agent for a broad range of assembly tasks has been limited by the need to manually curate assembly assets, which greatly constrains the number and diversity of assembly problems that can be used for policy learning.
- Inspired by recent success of using Generative AI to scale up robot learning, we propose MatchMaker, a pipeline to automatically generate diverse, simulation-compatible assembly asset pairs to facilitate learning assembly skills.

## Task

* Visual-Inertial
* Control
* Manipulation
* Perception

## Keywords

* Assembly
* AI-Enabled Robotics
* Computer Vision for Manufacturing

## AI依存度

* Hybrid

## 何を解決？

* Robotic assembly remains a significant challenge due to complexities in visual perception, functional grasping, contact-rich manipulation, and performing high-precision tasks.

## 何が新しい？

* Inspired by recent success of using Generative AI to scale up robot learning, we propose MatchMaker, a pipeline to automatically generate diverse, simulation-compatible assembly asset pairs to facilitate learning assembly skills.

## どうやってる？

* Simulation-based learning and sim-to-real transfer have led to recent success in solving assembly tasks in the presence of object pose variation, perception noise, and control error; however, the development of a generalist (i.e., multi-task) agent for a broad range of assembly tasks has been limited by the need to manually curate assembly assets, which greatly constrains the number and diversity of assembly problems that can be used for policy learning.

## どこが強い？

* Robotic assembly remains a significant challenge due to complexities in visual perception, functional grasping, contact-rich manipulation, and performing high-precision tasks.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Inspired by recent success of using Generative AI to scale up robot learning, we propose MatchMaker, a pipeline to automatically generate diverse, simulation-compatible assembly asset pairs to facilitate learning assembly skills.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
