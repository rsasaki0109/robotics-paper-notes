# Angular Divergent Component of Motion: A Step towards Planning Spatial DCM Objectives for Legged Robots

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Legged Locomotion: Novel Methods |
| arXiv | [http://arxiv.org/abs/2409.12796](http://arxiv.org/abs/2409.12796) |
| Authors | Herron, Connor, Schuller, Robert, Beiter, Benjamin, Griffin, Robert J., Leonessa, Alexander, Englsberger, Johannes |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 従来 linear CoM motion 中心だった DCM を、**角運動側へ拡張した angular DCM** の論文。
- 1D 回転については linear DCM とかなり似た形になり、orientation planning を同じ枠組みで扱える。
- humanoid walking で並進と回転を一緒に考えたい人にはかなり自然な拡張。

## Task

* Legged Locomotion
* Humanoid Control
* DCM
* Angular Momentum Planning

## Keywords

* Divergent Component of Motion / Angular DCM / SRBM / VRP / CoP Constraint

## AI依存度

* Non-AI

## 何を解決？

* DCM は humanoid locomotion で強力だが、主に CoM 並進の計画に使われ、姿勢回転側は別扱いになりがちだった。
* 歩行中は swing leg による angular momentum が無視できず、orientation も同時に見たい。
* そこで、**DCM の考え方を角運動へ拡張**したい。

## 何が新しい？

* flywheel 的な 1D 回転モデルから **angular DCM** を導いた点。
* linear DCM と対応のある形で、angular objective planning をできるようにした点。
* hardware で linear + angular DCM の併用を見せた点。

## どうやってる？

* SRBM に基づいて、並進側と角運動側の簡約ダイナミクスを作る。
* linear DCM に対応する形で、角速度から先読み的な angular DCM 状態を定義する。
* VRP / VRO 的な setpoint を使いながら、CoP 制約のもとで orientation tracking を行う。
* 実験では humanoid 上で並進と pitch 方向の回転計画を組み合わせて検証している。

## どこが強い？

* DCM 系の理論を壊さずに、**orientation objective** を追加できるのが綺麗。
* MPC より軽い closed-form 系の良さを保ちつつ、回転まで見られる。
* 実機での orientation tracking まで出しているので説得力がある。

## 弱そうなところ

* 現状は 1D angular motion に限定されている。
* linear と angular を同時に欲張ると CoP 制約がきつくなり、並進側が犠牲になることがある。
* acrobatic motion や full 3D orientation まで行くにはまだ距離がある。

## 関連研究との違い

* linear-only DCM より、**angular momentum planning** を同じ思想で扱える。
* CAM を learned/predicted 補正で扱う方法より、より明示的な template dynamics ベース。
* full-body MPC より、ずっと軽くて見通しが良い。

## non-AIとして見る価値

* locomotion control の classic tool を、**数理的に少し広げるだけで新しい制御対象へ拡張できる**好例。
* DCM をちゃんと理解したい人にかなり良い論文。

## 難易度

★★★☆☆

## 自分の理解/感想

* extension として非常に素直で、読むと「確かに欲しかったやつ」という感じ。
* 1D 限定でも、humanoid walking では十分価値があると思う。
