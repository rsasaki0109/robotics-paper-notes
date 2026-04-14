# Learning Wheelchair Tennis Navigation from Broadcast Videos with Domain Knowledge Transfer and Diffusion Motion Planning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Imitation Learning 1 |
| arXiv | [http://arxiv.org/abs/2409.19771](http://arxiv.org/abs/2409.19771) |
| Authors | Wu, Zixuan, Zaidi, Zulfiqar, Patil, Adithya, Xiao, Qingyu, Gombolay, Matthew |
| Source | ICRA 2025 / arXiv |

## TL;DR

- In this paper, we propose a novel and generalizable zero-shot knowledge transfer framework that distills expert sports navigation strategies from web videos into robotic systems with adversarial constraints and out-of-distribution image trajectories.
- Our pipeline enables diffusion-based imitation learning by reconstructing the full 3D task space from multiple partial views, warping it into 2D image space, closing the planning loop within this 2D space, and transfer constrained motion of interest back to task space.
- Additionally, we demonstrate that the learned policy can serve as a local planner in conjunction with position control.

## Task

* Sensor Fusion
* Motion Planning
* Control

## Keywords

* Learning from Demonstration / Transfer Learning / Vision-Based Navigation

## AI依存度

* AI-heavy

## 何を解決？

* We apply this framework in the wheelchair tennis navigation problem to guide the wheelchair into the ball-hitting region.

## 何が新しい？

* In this paper, we propose a novel and generalizable zero-shot knowledge transfer framework that distills expert sports navigation strategies from web videos into robotic systems with adversarial constraints and out-of-distribution image trajectories.

## どうやってる？

* Our pipeline enables diffusion-based imitation learning by reconstructing the full 3D task space from multiple partial views, warping it into 2D image space, closing the planning loop within this 2D space, and transfer constrained motion of interest back to task space.

## どこが強い？

* Additionally, we demonstrate that the learned policy can serve as a local planner in conjunction with position control.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* 既存手法との差分は abstract だけでは粒度不足。比較設定を本文で確認したい。

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
