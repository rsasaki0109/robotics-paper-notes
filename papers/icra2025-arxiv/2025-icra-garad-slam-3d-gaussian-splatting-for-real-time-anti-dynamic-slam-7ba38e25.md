# GARAD-SLAM: 3D GAussian Splatting for Real-Time Anti Dynamic SLAM

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | SLAM 5 |
| arXiv | [http://arxiv.org/abs/2502.03228](http://arxiv.org/abs/2502.03228) |
| Authors | Li, Mingrui;Chen, Weijian;Cheng, Na;Xu, Jingyuan;Li, Dong;Wang, Hongyu |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The 3D Gaussian Splatting (3DGS)-based SLAM system has garnered widespread attention due to its excellent performance in real-time high-fidelity rendering.
- However, in real-world environments filled with dynamic objects, existing 3DGS-based SLAM systems often face mapping errors and tracking drift issues.
- To address this, we propose GARAD-SLAM, a real-time 3DGS-based SLAM system tailored for dynamic scenes.

## Task

* SLAM
* Localization
* Perception
* Software Tools

## Keywords

* SLAM
* Mapping
* Localization

## AI依存度

* AI-heavy

## 何を解決？

* The 3D Gaussian Splatting (3DGS)-based SLAM system has garnered widespread attention due to its excellent performance in real-time high-fidelity rendering.

## 何が新しい？

* To address this, we propose GARAD-SLAM, a real-time 3DGS-based SLAM system tailored for dynamic scenes.

## どうやってる？

* In terms of tracking, unlike traditional methods, we directly perform dynamic segmentation on Gaussians and map them back to the front end to obtain dynamic point labels through a Gaussian pyramid network, achieving precise dynamic removal and robust tracking.

## どこが強い？

* Our results on real-world datasets demonstrate that our method is competitive in tracking compared to baseline methods, generating fewer artifacts and higher-quality reconstructions in rendering.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this, we propose GARAD-SLAM, a real-time 3DGS-based SLAM system tailored for dynamic scenes.

## non-AIとして見る価値

* AI 寄りの論文だが、評価設定やタスク設計を比較対象として読む価値はある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、AI 系の流れを把握する比較対象として押さえておく価値がありそう。
