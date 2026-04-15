# Pushing through Clutter with Movability Awareness of Blocking Obstacles

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Motion Planning 1 |
| arXiv | [http://arxiv.org/abs/2502.20106](http://arxiv.org/abs/2502.20106) |
| Authors | Weeda, Joris J., Bakker, Saray, Chen, Gang, Alonso-Mora, Javier |
| Source | ICRA 2025 / arXiv |

## TL;DR

- NAMO を binary movable / immovable でなく、**mass ベースの continuous movability** で扱う論文。
- global path planning は **Semantic Visibility Graph**, local control は **MPPI + physics engine** でまとめている。
- 「どの障害物なら押しても得か」を cost に素直に入れていて、interactive navigation としてかなり実用寄り。

## Task

* Motion Planning
* Interactive Navigation
* NAMO
* Model Predictive Control

## Keywords

* Movability / Visibility Graph / MPPI / Contact Force / Physics-Based Planning

## AI依存度

* Non-AI

## 何を解決？

* cluttered environment では、押せる障害物を少し動かせば通れる場面が多い。
* 既存 NAMO は障害物を動かせる/動かせないの binary で見ることが多く、**押しやすさの差**を十分使えていない。
* その結果、不要に重い物体を押そうとしたり、遠回りしすぎたりする。

## 何が新しい？

* obstacle mass を使って **movability を連続量**として path cost に入れる点。
* passage node を持つ Semantic Visibility Graph で、どの gap を抜けるかを global に決める点。
* local control 側は MPPI を physics engine 上で回し、contact force を直接 cost に入れている点。

## どうやってる？

* global では visibility graph を作り、通れない gap 周辺に passage node を置く。
* node や edge の cost は、距離だけでなく押す必要がある障害物の mass に応じて重くする。
* local では MPPI の rollout を simulator 上で評価し、waypoint 追従・progress・rotation に加えて **contact force** も罰する。
* 実際に押せない/重すぎると分かったときは online replanning で扱いを変える。

## どこが強い？

* binary で雑に分けず、**押しやすさを cost として使う**のがとても自然。
* obstacle placement planning を別問題として解かずに済み、NAMO の現実感が上がっている。
* local control が physics-aware なので、見た目だけでなく interaction effort も抑えられる。

## 弱そうなところ

* obstacle mass が既知 or 推定できる前提に依存する。
* holonomic platform 寄りで、非ホロ台車や humanoid にそのまま行けるかは不明。
* real-world validation はまだ限定的で、dense clutter 全般での強さはもっと見たい。

## 関連研究との違い

* 従来の binary NAMO より、**continuous movability** を導入しているのが本質。
* RRT ベースより graph planner と MPPI の役割分担が明快。
* ただ push できる前提でなく、push effort を明示 cost にしている点が良い。

## non-AIとして見る価値

* interactive navigation を学習 policy ではなく、**geometry + cost design + physics** で解いている。
* clutter 中で「何を動かすと得か」をどう planning に入れるかが分かりやすい。

## 難易度

★★★☆☆

## 自分の理解/感想

* 発想はシンプルだがかなり効いていて、binary movability の雑さをうまく突いている。
* 実システムに近い NAMO の入口としてかなり良い論文。
