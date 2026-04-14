# SYNERGAI: Perception Alignment for Human-Robot Collaboration

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Human-Robot Collaboration 1 |
| arXiv | [http://arxiv.org/abs/2409.15684](http://arxiv.org/abs/2409.15684) |
| Authors | Chen, Yixin, Zhang, Guoxi, Zhang, Yaowei, Xu, Hongming, Zhi, Peiyuan, Li, Qing, Huang, Siyuan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Recently, large language models (LLMs) have shown strong potential in facilitating human-robotic interaction and collaboration.
- To address this issue, we introduce SYNERGAI, a unified system designed to achieve both perceptual alignment and human-robot collaboration.
- In a zero-shot manner, SYNERGAI achieves comparable performance with the data-driven models in ScanQA.

## Task

* Perception
* Calibration

## Keywords

* Domestic Robotics

## AI依存度

* AI-heavy

## 何を解決？

* Recently, large language models (LLMs) have shown strong potential in facilitating human-robotic interaction and collaboration.

## 何が新しい？

* To address this issue, we introduce SYNERGAI, a unified system designed to achieve both perceptual alignment and human-robot collaboration.

## どうやってる？

* However, existing LLM-based systems often overlook the misalignment between human and robot perceptions, which hinders their effective communication and real-world robot deployment.

## どこが強い？

* To address this issue, we introduce SYNERGAI, a unified system designed to achieve both perceptual alignment and human-robot collaboration.

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
* どのモジュールに効くか: perception, sensor calibration / sensing
* 実用性: 実機または実環境評価があり、実用性は比較的高そう。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
