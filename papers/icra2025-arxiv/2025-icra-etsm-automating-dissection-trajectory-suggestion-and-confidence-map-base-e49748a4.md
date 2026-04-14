# ETSM: Automating Dissection Trajectory Suggestion and Confidence Map-Based Safety Margin Prediction for Robot-Assisted Endoscopic Submucosal Dissection

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Surgical Robotics: Planning |
| arXiv | [http://arxiv.org/abs/2411.18884](http://arxiv.org/abs/2411.18884) |
| Authors | Xu, Mengya, Mo, Wenjin, Wang, Guankun, Gao, Huxin, Wang, An, Bai, Long, Li, Zhen, Yang, Xiaoxiao, Ren, Hongliang |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Robot-assisted Endoscopic Submucosal Dissection (ESD) improves the surgical procedure by providing a more comprehensive view through advanced robotic instruments and bimanual operation, thereby enhancing dissection efficiency and accuracy.
- Additionally, we propose the Regression-based Confidence Map Prediction Network (RCMNet), which utilizes a regression approach to predict confidence maps for dissection areas, thereby delineating various levels of safety margins.
- We evaluate our RCMNet using three distinct experimental setups: in-domain evaluation, robustness assessment, and out-of-domain evaluation.

## Task

* Motion Planning

## Keywords

* Surgical Robotics: Planning / Data Sets for Robotic Vision / AI-Enabled Robotics

## AI依存度

* Non-AI

## 何を解決？

* Robot-assisted Endoscopic Submucosal Dissection (ESD) improves the surgical procedure by providing a more comprehensive view through advanced robotic instruments and bimanual operation, thereby enhancing dissection efficiency and accuracy.

## 何が新しい？

* Additionally, we propose the Regression-based Confidence Map Prediction Network (RCMNet), which utilizes a regression approach to predict confidence maps for dissection areas, thereby delineating various levels of safety margins.

## どうやってる？

* Additionally, we propose the Regression-based Confidence Map Prediction Network (RCMNet), which utilizes a regression approach to predict confidence maps for dissection areas, thereby delineating various levels of safety margins.

## どこが強い？

* Experimental results show that our approach excels in the confidence map-based safety margin prediction task, achieving a mean absolute error (MAE) of only 3.18.

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
* どのモジュールに効くか: planning
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
