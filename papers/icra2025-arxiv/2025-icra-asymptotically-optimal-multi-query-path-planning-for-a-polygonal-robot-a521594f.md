# Asymptotically-Optimal Multi-Query Path Planning for a Polygonal Robot

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Motion Planning 2 |
| arXiv | [http://arxiv.org/abs/2409.03920](http://arxiv.org/abs/2409.03920) |
| Authors | Zhang, Duo, Ye, Zihe, Yu, Jingjin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 2D polygonal robot の SE(2) planning を、**rotation-stacked visibility graph (RVG)** で multi-query に解く手法。
- 各回転層で visibility graph を作り、層間の vertex propagation を入れることで、**resolution-complete かつ asymptotically optimal** を狙っている。
- sampling-based planner ではなく、Minkowski 和と visibility graph を押し出した、かなり computational geometry 寄りの論文。

## Task

* Motion Planning
* Computational Geometry
* Multi-Query Planning
* Polygonal Robot

## Keywords

* Visibility Graph / Minkowski Sum / SE(2) Planning / Rotation Layers / Asymptotic Optimality

## AI依存度

* Non-AI

## 何を解決？

* 並進だけなら visibility graph は強いが、回転自由度が入るとそのままでは使いにくい。
* sampling-based planner は汎用性は高い一方、multi-query には重く、品質や実行時間のばらつきも大きい。
* そこで本論文は、polygonal robot に限れば **multi-query で再利用できる deterministic roadmap** を SE(2) でも持ちたい、という狙い。

## 何が新しい？

* 回転角を複数の層に分け、各層で成長障害物に対する visibility graph を作る **RVG** を提案している。
* 隣接回転層のあいだで、使える頂点を移してつなぐ **vertex propagation** がコア。
* これにより、開始・終了姿勢だけを見る粗い近似ではなく、**回転を伴う経路の連結性**を graph 上で表せる。
* 解像度を上げれば最適解へ近づくという理論整理まで入っている。

## どうやってる？

* 各回転区間ごとに robot shape を包み込む形で障害物の Minkowski 差分を取り、reflex vertex を使って visibility graph を構成する。
* つぎに、隣接層で同じ位置を共有できる頂点や、その近傍で代替頂点を置ける箇所をつないで、層間移動を可能にする。
* start / goal は対応する姿勢範囲をもつ各層へ差し込み、全体 graph 上で shortest path を引く。
* 並進距離と回転量の重みづけを変えられるので、path cost の解釈も比較的明快。

## どこが強い？

* sampling-based でなく **visibility graph 系の強い理論と multi-query 性**を保ったまま、SE(2) に拡張しているのが大きい。
* 幾何計算が中心なので、解の意味や失敗理由を追いやすい。
* 論文の価値は実験だけでなく、**なぜそれで漸近最適と言えるのか**まで整理している点にある。
* polygonal robot の搬送・家具移動のような設定ではかなり刺さる。

## 弱そうなところ

* 角度分解能や障害物数が増えると graph 構築コストは重くなる。
* SE(2) にはきれいに効くが、SE(3) や高自由度 manipulation へはそのまま広げにくい。
* polygonal geometry 前提なので、実ロボの接触や柔らかい安全余裕をどう入れるかは別問題。

## 関連研究との違い

* shortest-path roadmap の強みを、**回転自由度ありの robot** に拡張しようとしている点が本質。
* PRM* / RRT* のような sampling 系より、毎回サンプルし直さずに **multi-query 用 graph を前計算**できる。
* configuration-space decomposition の重い厳密解法と sampling の中間で、かなり実用的な落としどころに見える。

## non-AIとして見る価値

* 幾何計画の王道で、visibility graph、Minkowski sum、optimality proof がきれいにつながっている。
* 「古典手法は低次元でしか強くない」を、丁寧な構成で押し返しているのが面白い。
* planning を学ぶなら、かなり良い教材になるタイプ。

## 難易度

★★★★☆

## 自分の理解/感想

* かなり好きなタイプの論文で、手法の核は素朴なのに、層間接続の詰め方で一段レベルが上がっている。
* robot planning の中でも、geometry をちゃんと武器にしている論文として読む価値が高い。
