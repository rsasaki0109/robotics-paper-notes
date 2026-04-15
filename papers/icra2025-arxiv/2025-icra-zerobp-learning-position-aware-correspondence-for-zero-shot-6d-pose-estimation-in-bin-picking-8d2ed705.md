# ZeroBP: Learning Position-Aware Correspondence for Zero-Shot 6D Pose Estimation in Bin-Picking

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Pose Estimation |
| arXiv | [http://arxiv.org/abs/2502.01004](http://arxiv.org/abs/2502.01004) |
| Authors | Chen, Jianqiu;Zhou, Zikun;Li, Xin;Bao, Tianpeng;Zheng, Ye;He, Zhenyu |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Bin-picking is a practical and challenging robotic manipulation task, where accurate 6D pose estimation plays a pivotal role.
- The workpieces in bin-picking are typically textureless and randomly stacked in a bin, which poses a significant challenge to 6D pose estimation.
- Existing solutions are typically learning-based methods, which require object-specific training.

## Task

* Manipulation
* Perception
* Software Tools

## Keywords

* Deep Learning for Visual Perception
* Computer Vision for Automation
* RGB-D Perception

## AI依存度

* Hybrid

## 何を解決？

* Bin-picking is a practical and challenging robotic manipulation task, where accurate 6D pose estimation plays a pivotal role.

## 何が新しい？

* In this paper, we propose ZeroBP, a zero-shot pose estimation framework designed specifically for the bin-picking task.

## どうやってる？

* Existing solutions are typically learning-based methods, which require object-specific training.

## どこが強い？

* Extensive experiments on the ROBI dataset demonstrate that ZeroBP outperforms state-of-the-art zero-shot pose estimation methods, achieving an improvement of 9.1% in average recall of correct poses.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* In this paper, we propose ZeroBP, a zero-shot pose estimation framework designed specifically for the bin-picking task.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
