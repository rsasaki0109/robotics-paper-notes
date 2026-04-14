# Curb Your Attention: Causal Attention Gating for Robust Trajectory Prediction in Autonomous Driving

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Tracking and Prediction 1 |
| arXiv | [http://arxiv.org/abs/2410.07191](http://arxiv.org/abs/2410.07191) |
| Authors | Ahmadi, Ehsan, Mercurius, Ray Coden, Mohamad Alizadeh Shabestary, Soheil, Rezaee, Kasra, Rasouli, Amir |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Motivated by this challenge, we propose Causal tRajecTory predICtion (CRiTIC), a novel model that utilizes a causal discovery network to identify inter-agent causal relations over a window of past time steps.
- To incorporate discovered causal relationships, we propose a novel Causal Attention Gating mechanism to selectively filter information in the proposed Transformer-based architecture.
- We conduct extensive experiments on two autonomous driving benchmark datasets to evaluate the robustness of our model against non-causal perturbations and its generalization capacity.

## Task

* Perception
* Motion Planning
* Intelligent Vehicles

## Keywords

* Intelligent Transportation Systems / Autonomous Vehicle Navigation / Autonomous Agents

## AI依存度

* AI-heavy

## 何を解決？

* Motivated by this challenge, we propose Causal tRajecTory predICtion (CRiTIC), a novel model that utilizes a causal discovery network to identify inter-agent causal relations over a window of past time steps.

## 何が新しい？

* Motivated by this challenge, we propose Causal tRajecTory predICtion (CRiTIC), a novel model that utilizes a causal discovery network to identify inter-agent causal relations over a window of past time steps.

## どうやってる？

* Motivated by this challenge, we propose Causal tRajecTory predICtion (CRiTIC), a novel model that utilizes a causal discovery network to identify inter-agent causal relations over a window of past time steps.

## どこが強い？

* We conduct extensive experiments on two autonomous driving benchmark datasets to evaluate the robustness of our model against non-causal perturbations and its generalization capacity.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: perception, planning, planning / control / perception
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
