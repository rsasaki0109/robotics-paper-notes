# Constrained Nonlinear Kaczmarz Projection on Intersections of Manifolds for Coordinated Multi-Robot Mobile Manipulation

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Multi-Robot Path Planning 3 |
| arXiv | [http://arxiv.org/abs/2410.21630](http://arxiv.org/abs/2410.21630) |
| Authors | Agrawal, Akshaya;Mayer, Parker;Kingston, Zachary;Hollinger, Geoffrey |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 多ロボ協調搬送の大量制約を、**constrained nonlinear Kaczmarz (cNKZ)** で順番に投影して解く論文。
- 各 constraint family を manifold として書き、**constraint ごとの residual threshold** を持たせるのがポイント。
- 80 以上の heterogeneous constraint をまとめて扱えるのがかなり強い。

## Task

* Multi-Robot Manipulation
* Constraint Projection
* Motion Planning
* Coordinated Transportation

## Keywords

* Nonlinear Kaczmarz / Manifold Intersection / RRT Projection / Mobile Manipulation / Cooperative Transport

## AI依存度

* Non-AI

## 何を解決？

* 複数の mobile manipulator が剛体構造物を運ぶと、距離・角度・姿勢・非ホロ拘束など大量の制約が同時に掛かる。
* Newton-Raphson や null-space ベースでは、多数の heterogeneous constraint をうまく同時に満たしにくい。
* そのため、**多種類 constraint の交差集合へ高速に投影する方法**が欲しい。

## 何が新しい？

* nonlinear Kaczmarz を multi-robot manipulation の manifold constraint に拡張した **cNKZ**。
* 距離/角度/姿勢など constraint のスケールが違うので、manifold ごとに residual threshold を持たせる点。
* RRT の steer / projection に cNKZ を組み込み、constraint-satisfying planning を実現している点。

## どうやってる？

* 構造拘束・タスク拘束・各 robot の非ホロ拘束を、それぞれ implicit manifold として書く。
* cNKZ は、全制約の巨大 Jacobian を毎回まとめて解く代わりに、1 constraint を1回ずつ cyclic に投影していく。
* しきい値は manifold ごとに設定し、距離と角度のような異種 residual を同じ土俵で扱わない。
* motion planning では RRT の候補状態を cNKZ で constraint manifold へ引き戻して使う。

## どこが強い？

* constraint 数が多い問題に対して、**1行ずつ解く Kaczmarz 的発想**がかなりスケールする。
* manifold threshold の考え方が実務的で、多種 constraint を無理なく混ぜられる。
* hardware demo まであり、理論だけでなく本当に運べている。

## 弱そうなところ

* threshold tuning はかなり経験的で、タスク依存が強い。
* payload dynamics や compliance は明示的に入っていない。
* centralized 計画なので、さらに大規模な team へそのまま伸ばすには限界がありそう。

## 関連研究との違い

* TSR / null-space 的処理より、**constraint を正面から manifold intersection として扱う**。
* Newton-Raphson より、1 constraint ごとの Jacobian しか見ないので大規模で安定しやすい。
* sampling-based planning と projection solver の結合としてかなり自然。

## non-AIとして見る価値

* 多ロボ拘束問題を learning で近似せず、**数値解法と manifold 記述**で押しているのが良い。
* multi-robot mobile manipulation の constraint explosion を理解するのに役立つ。

## 難易度

★★★★☆

## 自分の理解/感想

* Kaczmarz をこういう形で robotics constraint projection に使うのはかなりうまい。
* 地味に見えるけど、多ロボ協調搬送の本丸に効く手法だと思う。
