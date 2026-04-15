# Deformable Multibody Modeling for Model Predictive Control in Legged Locomotion with Embodied Compliance

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Legged Robots |
| arXiv | [http://arxiv.org/abs/2504.20301](http://arxiv.org/abs/2504.20301) |
| Authors | Ye, Keran;Karydis, Konstantinos |
| Source | ICRA 2025 / arXiv |

## TL;DR

- compliant spine を持つ脚ロボを rigid body 近似で済ませず、**deformable multibody model** を MPC に入れようとする論文。
- 変形に応じて inertia が変わることを、**predictive deformed inertia / CCPDI** で horizon 内へ持ち込むのが肝。
- locomotion with embodied compliance を真面目にモデル化したい人にはかなり刺さる。

## Task

* Legged Robots
* Model Predictive Control
* Multibody Dynamics
* Embodied Compliance

## Keywords

* Centroidal Dynamics / Deformable Multibody / Compliance / Inertia Prediction / MPC

## AI依存度

* Non-AI

## 何を解決？

* 標準的な legged MPC は rigid-body 前提が強く、柔らかい spine や compliance を持つ robot では inertia 予測がズレやすい。
* compliance を完全に無視すると、GRF 配分や姿勢安定化が悪くなる。
* そこで、**変形が MPC の中でどう inertia を変えるか**を予測したい。

## 何が新しい？

* deformable body を複数 sub-body に分けて扱う一般的な multibody 表現。
* 予測 horizon 内で inertia の変化を追う **predictive deformed inertia**。
* centroidal composite inertia を compliant system に拡張した **CCPDI** を MPC にそのまま差し込める形にした点。

## どうやってる？

* deformable spine などを、相対運動する rigid sub-body 群として近似する。
* 各 sub-body の相対 twist から、horizon 先の姿勢と inertia 変化を予測する。
* それらをまとめて centroidal inertia に反映し、MPC の dynamics constraint を更新する。
* 実験では rigid 近似との比較で、GRF 分布や姿勢安定性の改善を見ている。

## どこが強い？

* compliance を「余計なノイズ」でなく、**モデルに入れるべき構造**として扱っているのが良い。
* rigid robot と compliant robot を同じ枠組みで扱える見通しがある。
* centroidal MPC 系とつながるので、既存 legged control 文脈に乗せやすい。

## 弱そうなところ

* sub-body twist を horizon 中でほぼ一定とみなす近似には限界がある。
* parameter sensitivity があり、柔らかすぎる条件では厳しい。
* 実機 validation がまだ薄く、現時点では simulation 色が強い。

## 関連研究との違い

* rigid-body centroidal MPC より、**compliance に伴う inertia 変化**をちゃんと入れている。
* 材料依存の特殊モデルより、もう少し一般的な deformable multibody 記述に寄せている。
* full-body FEM 的な重さと rigid 近似の雑さの中間を狙った立ち位置。

## non-AIとして見る価値

* embodied compliance を「学習で吸収」せず、**ダイナミクスを増やしてでもモデルで扱う**方向性が明快。
* legged robot の mechanics と control の接点としてかなり面白い。

## 難易度

★★★★☆

## 自分の理解/感想

* かなりまっとうな問題設定で、compliant legged system を rigid MPC の外側に置かないのが良い。
* hardware まで強く出るとさらに面白くなりそうだが、理論の筋はかなりいい。
