# Robo-DM: Data Management for Large Robot Datasets

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Big Data |
| arXiv | [http://arxiv.org/abs/2505.15558](http://arxiv.org/abs/2505.15558) |
| Authors | Chen, Kaiyuan;Fu, Letian;Huang, David;Zhang, Yanxiang;Chen, Lawrence Yunliang;Huang, Huang;Hari, Kush;Balakrishna, Ashwin;Xiao, Ted;Sanketi, Pannag;Kubiatowicz, John;Goldberg, Ken |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recent work suggests that very large datasets of teleoperated robot demonstrations can train transformer-based models that have the potential to generalize to new scenes, robots, and tasks.
- However, curating, distributing, and loading large datasets of robot trajectories, which typically consist of video, textual, and numerical modalities - including streams from multiple cameras - remains challenging.
- We propose Robo-DM, an efficient cloud-based data management toolkit for collecting, sharing, and learning with robot data.

## Task

* Motion Planning
* Manipulation
* Software Tools

## Keywords

* Big Data in Robotics and Automation
* Methods and Tools for Robot System Design
* Engineering for Robotic Systems

## AI依存度

* AI-heavy

## 何を解決？

* Recent work suggests that very large datasets of teleoperated robot demonstrations can train transformer-based models that have the potential to generalize to new scenes, robots, and tasks.

## 何が新しい？

* We propose Robo-DM, an efficient cloud-based data management toolkit for collecting, sharing, and learning with robot data.

## どうやってる？

* Compared to LeRobot, a framework that also uses lossy video compression, Robo-DM is up to 50x faster.

## どこが強い？

* We physically evaluate a model trained by Robo-DM with lossy compression, a pick-and-place task, and In-Context Robot Transformer.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We propose Robo-DM, an efficient cloud-based data management toolkit for collecting, sharing, and learning with robot data.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
