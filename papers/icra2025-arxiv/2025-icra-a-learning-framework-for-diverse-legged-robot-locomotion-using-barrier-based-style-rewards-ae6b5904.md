# A Learning Framework for Diverse Legged Robot Locomotion Using Barrier-Based Style Rewards

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Learning for Legged Locomotion 1 |
| arXiv | [http://arxiv.org/abs/2409.15780](http://arxiv.org/abs/2409.15780) |
| Authors | Kim, Gijeong;Lee, Yonghoon;Park, Hae-Won |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This work introduces a model-free reinforcement learning framework that enables various modes of motion (quadruped, tripod, or biped) and diverse tasks for legged robot locomotion.
- We employ a motion-style reward based on a relaxed logarithmic barrier function as a soft constraint, to bias the learning process toward the desired motion style, such as gait, foot clearance, joint position, or body height.
- The predefined gait cycle is encoded in a flexible manner, facilitating gait adjustments throughout the learning process.

## Task

* Legged Robotics

## Keywords

* Legged Robots
* Humanoid and Bipedal Locomotion
* Reinforcement Learning

## AI依存度

* Hybrid

## 何を解決？

* This work introduces a model-free reinforcement learning framework that enables various modes of motion (quadruped, tripod, or biped) and diverse tasks for legged robot locomotion.

## 何が新しい？

* Extensive experiments demonstrate that KAIST HOUND, a 45 kg robotic system, can achieve biped, tripod, and quadruped locomotion using the proposed framework; quadrupedal capabilities include traversing uneven terrain, galloping at 4.67 m/s, and overcoming obstacles up to 58 cm (67 cm for HOUND2); bipedal capabilities include running at 3.6 m/s, carrying a 7.5 kg object, and ascending stairs-all performed without exteroceptive input.

## どうやってる？

* This work introduces a model-free reinforcement learning framework that enables various modes of motion (quadruped, tripod, or biped) and diverse tasks for legged robot locomotion.

## どこが強い？

* Extensive experiments demonstrate that KAIST HOUND, a 45 kg robotic system, can achieve biped, tripod, and quadruped locomotion using the proposed framework; quadrupedal capabilities include traversing uneven terrain, galloping at 4.67 m/s, and overcoming obstacles up to 58 cm (67 cm for HOUND2); bipedal capabilities include running at 3.6 m/s, carrying a 7.5 kg object, and ascending stairs-all performed without exteroceptive input.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* Extensive experiments demonstrate that KAIST HOUND, a 45 kg robotic system, can achieve biped, tripod, and quadruped locomotion using the proposed framework; quadrupedal capabilities include traversing uneven terrain, galloping at 4.67 m/s, and overcoming obstacles up to 58 cm (67 cm for HOUND2); bipedal capabilities include running at 3.6 m/s, carrying a 7.5 kg object, and ascending stairs-all performed without exteroceptive input.

## non-AIとして見る価値

* 学習要素は含むが、周辺のシステム設計や問題設定の切り方には実装上の学びがある。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、学習と従来手法のつなぎ方を見る材料として良さそう。
