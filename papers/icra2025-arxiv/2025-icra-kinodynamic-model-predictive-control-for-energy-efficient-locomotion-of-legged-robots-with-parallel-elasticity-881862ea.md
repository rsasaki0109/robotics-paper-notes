# Kinodynamic Model Predictive Control for Energy Efficient Locomotion of Legged Robots with Parallel Elasticity

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Model Predictive Control for Legged Robots 1 |
| arXiv | [http://arxiv.org/abs/2503.05666](http://arxiv.org/abs/2503.05666) |
| Authors | Zhuang, Yulun;Wang, Yichen;Ding, Yanran |
| Source | ICRA 2025 / arXiv |

## TL;DR

- unidirectional parallel spring (UPS) を持つ脚ロボットに対して、その弾性を活かす kinodynamic MPC を設計した論文。
- SLIP → SRB MPC → kinodynamic MPC の階層 warm-start 構造で、非凸な locomotion NLP を実時間で解きやすくしている。
- energy efficiency と peak motor torque の両方を下げており、parallel elasticity を controller がちゃんと使う設計になっている。

## Task

* Motion Planning
* Control
* Legged Robotics

## Keywords

* Kinodynamic MPC / Parallel Elasticity / UPS / SLIP / Energy Efficiency

## AI依存度

* Non-AI

## 何を解決？

* ばね機構を持つ脚ロボットは、機械としては省エネ余地があるのに、controller 側がその弾性を十分活かせないことが多い。
* full kinodynamic MPC で弾性まで含めると非凸で重く、リアルタイム制御が難しい。

## 何が新しい？

* UPS の torque contribution を kinodynamic MPC の中へ明示的に入れた点。
* SLIP / SRB / kinodynamic の 3 段階 warm-start により、重い問題を実時間へ持ち込んだ点。
* energy efficiency だけでなく peak motor torque の削減まで定量的に見ている点。

## どうやってる？

* 最上位では SLIP で CoM 的な粗い reference を出し、中段で SRB MPC により torso dynamics を入れた reference に整える。
* 最下段の kinodynamic MPC では joint angle・torque・spring effect を含む nonlinear problem を解く。
* spring torque は motor torque と合成して扱い、stance phase のエネルギー再利用を controller 側で引き出す。
* warm-start によって、いきなり full NLP を解くより安定して高速化している。

## どこが強い？

* 機構設計（parallel elasticity）と controller 設計をきちんとつないでいる。
* simulation だけでなく hardware でも CoT 改善を出していて説得力がある。
* torque 軽減が見えているので、単なる「省エネっぽい」ではなく actuator 負荷の実利もある。

## 弱そうなところ

* sim-to-real gap は残っており、摩擦や spring の非線形性など未モデル化要素の影響が大きい。
* 単脚ホッパー中心の検証なので、多脚・不整地への一般化はまだ先。
* spring stiffness の設計にかなり依存しそうで、mechanical co-design 問題が残る。

## 関連研究との違い

* SLIP ベース制御は弾性の恩恵を使うが、関節 torque 分配まで最適化しないことが多い。
* standard SRB / whole-body MPC は rigid body 寄りで、parallel elasticity を controller に活かし切れない。
* 本論文は hardware design と MPC を一体で見て、エネルギー再利用を最適化対象へ入れている。

## non-AIとして見る価値

* 「良い機構を作る」だけでは足りず、「その機構を活かす controller」が必要だとよくわかる。
* legged MPC を設計するときに、モデル簡略化と warm-start の使い方がかなり参考になる。

## 難易度

★★★★☆

## 自分の理解/感想

* parallel elasticity をちゃんと control 側まで落としていて、mechanics と control の接続がきれい。
* まだ単脚寄りだが、legged control の広がりを見る枠として Top 12 に入るのは納得。
