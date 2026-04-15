# DVLO4D: Deep Visual-Lidar Odometry with Sparse Spatial-Temporal Fusion

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning-Based SLAM 2 |
| arXiv | [http://arxiv.org/abs/2509.06023](http://arxiv.org/abs/2509.06023) |
| Authors | Liu, Mengmeng;Yang, Michael Ying;Liu, Jiuming;Zhang, Yunpeng;Li, Jiangtao;Sander, Oude Elberink;Vosselman, George;Cheng, Hao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Visual-LiDAR odometry is a critical component for autonomous system localization, yet achieving high accuracy and strong robustness remains a challenge.
- Traditional approaches commonly struggle with sensor misalignment, fail to fully leverage temporal information, and require extensive manual tuning to handle diverse sensor configurations.
- To address these problems, we introduce DVLO4D, a novel visual-LiDAR odometry framework that leverages sparse spatial-temporal fusion to enhance accuracy and robustness.

## Task

* SLAM
* Localization
* LiDAR
* Software Tools

## Keywords

* Localization
* Autonomous Agents
* SLAM

## AI依存度

* Non-AI

## 何を解決？

* Visual-LiDAR odometry is a critical component for autonomous system localization, yet achieving high accuracy and strong robustness remains a challenge.

## 何が新しい？

* Our approach proposes three key innovations: (1) Sparse Query Fusion, which utilizes sparse LiDAR queries for effective multi-modal data fusion; (2) a Temporal Interaction and Update module that integrates temporally-predicted positions with current frame data, providing better initialization values for pose estimation and enhancing model's robustness against accumulative errors; and (3) a Temporal Clip Training strategy combined with a Collective Average Loss mechanism that aggregates losses across multiple frames, enabling global optimization and reducing the scale drift over long sequences.

## どうやってる？

* Additionally, our method has high efficiency, with an inference time of 82 ms, possessing the potential for the real-time deployment.

## どこが強い？

* Extensive experiments on the KITTI and Argoverse Odometry dataset demonstrate the superiority of our proposed DVLO4D, which achieves state-of-the-art performance in terms of both pose accuracy and robustness.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Our approach proposes three key innovations: (1) Sparse Query Fusion, which utilizes sparse LiDAR queries for effective multi-modal data fusion; (2) a Temporal Interaction and Update module that integrates temporally-predicted positions with current frame data, providing better initialization values for pose estimation and enhancing model's robustness against accumulative errors; and (3) a Temporal Clip Training strategy combined with a Collective Average Loss mechanism that aggregates losses across multiple frames, enabling global optimization and reducing the scale drift over long sequences.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
