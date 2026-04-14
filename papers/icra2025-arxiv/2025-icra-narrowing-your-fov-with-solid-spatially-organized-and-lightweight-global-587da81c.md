# Narrowing Your FOV with SOLiD: Spatially Organized and Lightweight Global Descriptor for FOV-Constrained LiDAR Place Recognition

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Perception 1 |
| arXiv | [http://arxiv.org/abs/2408.07330](http://arxiv.org/abs/2408.07330) |
| Authors | Kim, Hogyun, Choi, Jiwon, Sim, Taehu, Kim, Giseop, Cho, Younggun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Thus, in this paper, we propose a robust LiDAR-based place recognition method for handling narrow FOV scenarios.
- Based on these representations, our method enables addressing rotational changes and determining the initial heading.
- In addition, we achieve a robust place description through reweighting based on vertical direction information.

## Task

* SLAM
* Localization
* LiDAR
* Perception

## Keywords

* Localization / SLAM / Range Sensing

## AI依存度

* Non-AI

## 何を解決？

* We often encounter limited FOV situations due to various factors such as sensor fusion or sensor mount in real-world robot navigation.

## 何が新しい？

* Thus, in this paper, we propose a robust LiDAR-based place recognition method for handling narrow FOV scenarios.

## どうやってる？

* 手法詳細は本文確認前のため、現時点では abstract 由来の把握に留まる。

## どこが強い？

* In addition, we achieve a robust place description through reweighting based on vertical direction information.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: 比較的使える可能性が高い。モデル化された推定・最適化・制御の知見として転用しやすい。
* どのモジュールに効くか: localization / mapping, localization, sensing / localization / perception
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
