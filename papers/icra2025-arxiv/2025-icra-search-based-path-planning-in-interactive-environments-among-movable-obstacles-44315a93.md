# Search-Based Path Planning in Interactive Environments among Movable Obstacles

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Motion Planning 1 |
| arXiv | [http://arxiv.org/abs/2410.18333](http://arxiv.org/abs/2410.18333) |
| Authors | Ren, Zhongqiang;Suvonov, Bunyod;Chen, Guofei;He, Botao;Liao, Yijie;Fermuller, Cornelia;Zhang, Ji |
| Source | ICRA 2025 / arXiv |

## TL;DR

- movable obstacle を押してどけてもよい path planning を、**PAMO\*** という search-based formulation でかなり真面目に解いている。
- robot 位置だけでなく object 配置まで入るので状態空間は爆発するが、**heuristic と dominance pruning** で実用域まで持っていく。
- multi-objective / resource-constrained の両方を扱っており、「押す回数」と「移動コスト」の trade-off を見せられるのが良い。

## Task

* Motion Planning
* Search
* Navigation Among Movable Obstacles
* Interactive Environments

## Keywords

* NAMO / A* / Multi-Objective Planning / Resource Constraints / Hybrid Planning

## AI依存度

* Non-AI

## 何を解決？

* movable obstacle を含む環境では、単なる collision-free planning では足りず、「どの障害物を押すか」まで計画する必要がある。
* しかし object 配置まで状態に入れると、状態空間は robot x objects で爆発的に増える。
* 既存の NAMO 系は heuristic や sampling でなんとかすることが多く、完全性や最適性が弱くなりがち。

## 何が新しい？

* PAMO を **bi-objective** と **resource-constrained** の 2 つの見方で定式化している点。
* EMOA* / resource-constrained A* 系の枠組みを使い、**completeness / optimality を残した search** にしている点。
* continuous space まで広げた H-PAMO* を用意して、離散理論と実装の橋渡しをしている点。

## どうやってる？

* 状態は robot 位置に加えて、各 movable object の位置も含む複合状態。
* ただし全空間を本気で探索するのではなく、goal からの heuristic と dominance check で不要な枝をかなり刈る。
* bi-objective 版では移動コストと押し回数の Pareto frontier を、resource-constrained 版では押し回数上限付き最小コスト解を求める。
* hybrid / continuous 版では、実際の運動学や物理シミュレーションに寄せた実装も試している。

## どこが強い？

* 「押してよい環境」の planning を、理論保証つき search として整理しているのが強い。
* scalarization でごまかさず、trade-off を Pareto 的に見せられる。
* object が多い状況でも、全部の object を常に動かすわけではないという構造をうまく使っている。

## 弱そうなところ

* continuous / hybrid 版では、理論保証がかなり薄くなる。
* interaction は主に pushing に限られ、grasping や複雑接触を扱うわけではない。
* heuristic が object をかなり粗く見ているので、密な clutter では効きが落ちる可能性がある。

## 関連研究との違い

* sampling-based NAMO より、**search の保証**を前に出している。
* Sokoban 的な object goal planning ではなく、「robot が通るために object をどかす」ことに集中している。
* manipulation planning より接触の自由度は少ないが、そのぶん planning guarantee を出しやすい。

## non-AIとして見る価値

* movable obstacle planning を learned interaction policy でなく、**状態空間設計と探索戦略**で解いているのが面白い。
* planning の観点で「何を state に持つと爆発するか」がよく見える論文。

## 難易度

★★★★☆

## 自分の理解/感想

* かなり王道な search 論文で、interactive environment をちゃんと planning problem として扱っている。
* continuous 版の保証の薄さはあるが、NAMO を整理して理解する入口としてかなり良い。
