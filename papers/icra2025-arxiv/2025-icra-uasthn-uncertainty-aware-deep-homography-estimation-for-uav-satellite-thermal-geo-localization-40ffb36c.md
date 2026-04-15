# UASTHN: Uncertainty-Aware Deep Homography Estimation for UAV Satellite-Thermal Geo-Localization

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Localization 6 |
| arXiv | [http://arxiv.org/abs/2502.01035](http://arxiv.org/abs/2502.01035) |
| Authors | Xiao, Jiuhong;Loianno, Giuseppe |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Geo-localization is an essential component of Unmanned Aerial Vehicle (UAV) navigation systems to ensure precise absolute self-localization in outdoor environments.
- To address the challenges of GPS signal interruptions or low illumination, Thermal Geo-localization (TG) employs aerial thermal imagery to align with reference satellite maps to accurately determine the UAV's location.
- However, existing TG methods lack uncertainty measurement in their outputs, compromising system robustness in the presence of textureless or corrupted thermal images, self-similar or outdated satellite maps, geometric noises, or thermal images exceeding satellite maps.

## Task

* Localization
* GNSS
* Aerial Robotics
* Perception

## Keywords

* Deep Learning for Visual Perception
* Aerial Systems: Applications
* Localization

## AI依存度

* Hybrid

## 何を解決？

* Geo-localization is an essential component of Unmanned Aerial Vehicle (UAV) navigation systems to ensure precise absolute self-localization in outdoor environments.

## 何が新しい？

* To overcome these limitations, this paper presents UASTHN, a novel approach for Uncertainty Estimation (UE) in Deep Homography Estimation (DHE) tasks for TG applications.

## どうやってる？

* However, existing TG methods lack uncertainty measurement in their outputs, compromising system robustness in the presence of textureless or corrupted thermal images, self-similar or outdated satellite maps, geometric noises, or thermal images exceeding satellite maps.

## どこが強い？

* Extensive experiments across multiple DHE models demonstrate the effectiveness and efficiency of CropTTA in TG applications.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To overcome these limitations, this paper presents UASTHN, a novel approach for Uncertainty Estimation (UE) in Deep Homography Estimation (DHE) tasks for TG applications.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
