# Model Predictive Control with Visibility Graphs for Humanoid Path Planning and Tracking against Adversarial Opponents

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Model Predictive Control |
| arXiv | [http://arxiv.org/abs/2504.02184](http://arxiv.org/abs/2504.02184) |
| Authors | Hou, Ruochen;Fernandez, Gabriel Ikaika;Zhu, Mingzhang;Hong, Dennis |
| Source | ICRA 2025 / arXiv |

## TL;DR

- humanoid soccer の path planning / tracking を、**turning-cost-aware visibility graph + collision-free MPC** で解く論文。
- visibility graph 側で turning cost を入れるのが humanoid 向けにかなり重要。
- obstacle avoidance と tracking を mode switching で分けず、**1つの MPC でなめらかに扱う**のが実践的。

## Task

* Humanoid Navigation
* Model Predictive Control
* Path Planning
* Obstacle Avoidance

## Keywords

* Visibility Graph / Turning Cost / Collision-Free MPC / RoboCup / Humanoid Path Tracking

## AI依存度

* Non-AI

## 何を解決？

* humanoid は turning が高コストなので、単純な Euclidean shortest path では走りにくい。
* また RoboCup のような動的・視野制限あり環境では、obstacle avoidance を mode switching で入れると挙動が不安定になりやすい。
* そこで、**global path でも local control でも turning と obstacle を自然に扱いたい**。

## 何が新しい？

* visibility graph の node/state に heading を持たせた **Dynamic Augmented Visibility Graph**。
* global planning で turning cost を明示的に加える点。
* obstacle avoidance を switch せず、slack 付きの **unified collision-free MPC** で扱う点。

## どうやってる？

* global 側では、active obstacle だけを抜き出して visibility graph を作る。
* edge cost に移動距離だけでなく turning penalty を加え、Dijkstra/A* 的に経路を引く。
* local 側は MPC で reference path tracking と obstacle avoidance を同時に最適化する。
* slack を入れることで、視界に突然 obstacle が出入りしても mode jump せず連続的に挙動を変えられる。

## どこが強い？

* humanoid にとって本当に重要な **turning cost** を graph planning に入れている。
* mode switching を避ける設計が、実環境ノイズのある football setting に合っている。
* RoboCup 実機運用まで行っていて、system paper として強い。

## 弱そうなところ

* turning weight は humanoid 特化で、他 platform にそのまま通るとは限らない。
* obstacle 形状はかなり単純化しており、複雑形状には追加工夫が要る。
* uncertainty を明示的に伝播しているわけではない。

## 関連研究との違い

* RRT 系より、visibility graph ベースで解釈しやすく速い。
* GCS や spline smoothing 系より、**turning-aware shortest path** をシンプルに出す立場。
* switching MPC / CBF 系より、tracking と avoidance を単一 MPC で連続的に扱うのが特徴。

## non-AIとして見る価値

* competition-level humanoid navigation でも、**visibility graph + MPC** の王道構成がまだ非常に強いと分かる。
* locomotion-aware path planning の実践例としてかなり良い。

## 難易度

★★★☆☆

## 自分の理解/感想

* 新理論というより、必要な工夫をちゃんと実機へ落とした良い system paper。
* humanoid の「曲がるコスト」を軽視しないのが本当に大事だと分かる。
