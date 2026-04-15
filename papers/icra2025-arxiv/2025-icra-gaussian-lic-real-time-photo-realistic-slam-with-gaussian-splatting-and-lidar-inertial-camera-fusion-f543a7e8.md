# Gaussian-LIC: Real-Time Photo-Realistic SLAM with Gaussian Splatting and LiDAR-Inertial-Camera Fusion

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning-Based SLAM 1 |
| arXiv | [http://arxiv.org/abs/2404.06926](http://arxiv.org/abs/2404.06926) |
| Authors | Lang, Xiaolei;Li, Laijian;Wu, Chenming;Zhao, Chen;Liu, Lina;Liu, Yong;Lv, Jiajun;Zuo, Xingxing |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we present a real-time photo-realistic SLAM method based on marrying Gaussian Splatting with LiDAR-Inertial-Camera SLAM.
- Most existing radiance-field-based SLAM systems mainly focus on bounded indoor environments, equipped with RGB-D or RGB sensors.
- However, they are prone to decline when expanding to unbounded scenes or encountering adverse conditions, such as violent motions and changing illumination.

## Task

* SLAM
* LiDAR
* Visual-Inertial

## Keywords

* Mapping
* Sensor Fusion
* SLAM

## AI依存度

* AI-heavy

## 何を解決？

* In this paper, we present a real-time photo-realistic SLAM method based on marrying Gaussian Splatting with LiDAR-Inertial-Camera SLAM.

## 何が新しい？

* To compensate for regions unobserved by the LiDAR, we propose to integrate both the triangulated visual points from images and LiDAR points for initializing 3D Gaussians.

## どうやってる？

* In this paper, we present a real-time photo-realistic SLAM method based on marrying Gaussian Splatting with LiDAR-Inertial-Camera SLAM.

## どこが強い？

* Extensive experiments demonstrate that our method outperforms its counterparts while maintaining real-time capability.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To compensate for regions unobserved by the LiDAR, we propose to integrate both the triangulated visual points from images and LiDAR points for initializing 3D Gaussians.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
