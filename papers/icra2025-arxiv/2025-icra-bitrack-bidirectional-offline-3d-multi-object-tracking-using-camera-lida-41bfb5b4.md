# BiTrack: Bidirectional Offline 3D Multi-Object Tracking Using Camera-LiDAR Data

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Tracking and Prediction 2 |
| arXiv | [http://arxiv.org/abs/2406.18414](http://arxiv.org/abs/2406.18414) |
| Authors | Huang, Kemiao, Chen, Yinqi, Zhang, Meiying, Hao, Qi |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Compared with real-time multi-object tracking (MOT), offline multi-object tracking (OMOT) has the advantages to perform 2D-3D detection fusion, erroneous link correction, and full track optimization but has to deal with the challenges from bounding box misalignment and track evaluation, editing, and refinement.
- This paper proposes ``BiTrack'', a 3D OMOT framework that includes modules of 2D-3D detection fusion, initial trajectory generation, and bidirectional trajectory re-optimization to achieve optimal tracking results from camera-LiDAR data.
- The novelty of this paper includes threefold: (1) development of a point-level object registration technique that employs a density-based similarity metric to achieve accurate fusion of 2D-3D detection results; (2) development of a set of data association and track management skills that utilizes a vertex-based similarity metric as well as false alarm rejection and track recovery mechanisms to generate reliable bidirectional object trajectories; (3) development of a trajectory re-optimization scheme that re-organizes track fragments of different fidelities in a greedy fashion, as well as refines each trajectory with completion and smoothing techniques.

## Task

* LiDAR
* Perception
* Sensor Fusion
* Motion Planning

## Keywords

* Visual Tracking / Sensor Fusion

## AI依存度

* Non-AI

## 何を解決？

* Compared with real-time multi-object tracking (MOT), offline multi-object tracking (OMOT) has the advantages to perform 2D-3D detection fusion, erroneous link correction, and full track optimization but has to deal with the challenges from bounding box misalignment and track evaluation, editing, and refinement.

## 何が新しい？

* The novelty of this paper includes threefold: (1) development of a point-level object registration technique that employs a density-based similarity metric to achieve accurate fusion of 2D-3D detection results; (2) development of a set of data association and track management skills that utilizes a vertex-based similarity metric as well as false alarm rejection and track recovery mechanisms to generate reliable bidirectional object trajectories; (3) development of a trajectory re-optimization scheme that re-organizes track fragments of different fidelities in a greedy fashion, as well as refines each trajectory with completion and smoothing techniques.

## どうやってる？

* Compared with real-time multi-object tracking (MOT), offline multi-object tracking (OMOT) has the advantages to perform 2D-3D detection fusion, erroneous link correction, and full track optimization but has to deal with the challenges from bounding box misalignment and track evaluation, editing, and refinement.

## どこが強い？

* This paper proposes ``BiTrack'', a 3D OMOT framework that includes modules of 2D-3D detection fusion, initial trajectory generation, and bidirectional trajectory re-optimization to achieve optimal tracking results from camera-LiDAR data.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Compared with real-time multi-object tracking (MOT), offline multi-object tracking (OMOT) has the advantages to perform 2D-3D detection fusion, erroneous link correction, and full track optimization but has to deal with the challenges from bounding box misalignment and track evaluation, editing, and refinement.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: sensing / localization / perception, perception, perception / localization fusion
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
