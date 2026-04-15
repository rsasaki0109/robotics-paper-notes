# Joint 3D Point Cloud Segmentation Using Real-Sim Loop: From Panels to Trees and Branches

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Agricultural Automation 1 |
| arXiv | [http://arxiv.org/abs/2503.05630](http://arxiv.org/abs/2503.05630) |
| Authors | Qiu, Tian;Du, Ruiming;Spine, Nikolai;Cheng, Lailiang;Jiang, Yu |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Modern orchards are planted in structured rows with distinct panel divisions to improve management.
- Accurate and efficient joint segmentation of point cloud from Panel to Tree and Branch (P2TB) is essential for robotic operations.
- However, most current segmentation methods focus on single-instance segmentation and depend on a sequence of deep networks to perform joint tasks.

## Task

* LiDAR
* Visual-Inertial
* Perception
* Software Tools

## Keywords

* Robotics and Automation in Agriculture and Forestry
* Field Robots
* Data Sets for Robotic Vision

## AI依存度

* Hybrid

## 何を解決？

* Modern orchards are planted in structured rows with distinct panel divisions to improve management.

## 何が新しい？

* In this study, we proposed a novel approach that incorporated a Real2Sim L-TreeGen for training data generation and a joint model (J-P2TB) designed for the P2TB task.

## どうやってる？

* However, most current segmentation methods focus on single-instance segmentation and depend on a sequence of deep networks to perform joint tasks.

## どこが強い？

* Compared to representative methods, our model outperformed them in most segmentation metrics while using 40% fewer learnable parameters.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this study, we proposed a novel approach that incorporated a Real2Sim L-TreeGen for training data generation and a joint model (J-P2TB) designed for the P2TB task.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
