# Topo-Geometrically Distinct Path Computation Using Neighborhood-Augmented Graph, and Its Application to Path Planning for a Tethered Robot in 3D

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Motion Planning 4 |
| arXiv | [http://arxiv.org/abs/2306.01203](http://arxiv.org/abs/2306.01203) |
| Authors | Sahin, Alp, Bhattacharya, Subhrajit |
| Source | ICRA 2025 / arXiv |

## TL;DR

- **Neighborhood-Augmented Graph** を使って、topologically だけでなく geometrically も異なる複数経路を計算する手法。
- 明示的な homotopy invariant や複雑な 3D 幾何構造を前計算せず、**経路近傍集合の重なり具合**で経路の違いを判定するのが核。
- tethered robot in 3D への応用まで見せていて、複数の有意味な path を出したい場面にかなり向く。

## Task

* Multi-Path Planning
* Topological Motion Planning
* Tethered Robot Planning
* 3D Path Computation

## Keywords

* Neighborhood-Augmented Graph / Homotopy / Geodesic Path / Tether Constraint / Graph Search

## AI依存度

* Non-AI

## 何を解決？

* 従来の topological path planning は、異なる homotopy class を区別するのは得意だが、同一 class の中の幾何的に違う良い経路を落としやすい。
* しかも 3D では、homotopy invariant や skeleton をちゃんと作るのが重くて実装障壁が高い。
* tethered robot では cable の回り込み方も効くので、「別の path が欲しい」がより切実になる。

## 何が新しい？

* 各 graph vertex に単なる位置だけでなく **path neighborhood set** を持たせる発想。
* これにより、「同じ点に来たが別の経路として残すべきか」を、近傍集合の重なりで判定できる。
* 低曲率領域で path の分岐が消えやすい問題に対して、**cut-point 的な補助処理**で分化を促している。
* tether length constraint を扱う 2 段階探索へ自然につなげている。

## どうやってる？

* ベースは通常の graph search だが、探索中の各頂点に「そこへ来るまでの path neighborhood」を持たせる。
* 新しい経路が同じ空間点へ到達しても、近傍集合が十分に違えば **別頂点コピーとして残す**。
* 逆に近傍が重なるなら merge し、不要な重複 path を抑える。
* tethered robot 応用では、まず cable length 内で到達可能な graph を作り、その上で goal への長さ制約つき経路を引く。

## どこが強い？

* topology をガチガチに記述しなくても、**複数の意味ある経路**を取り出せるのが強い。
* 3D で explicit homotopy machinery を避けているので、実装の心理的ハードルが下がる。
* tethered robot という「複数経路を区別する意味が大きい」応用で価値が見えやすい。
* 既存の graph search を拡張する設計なので、発想の再利用先が多い。

## 弱そうなところ

* neighborhood radius などのパラメータに依存し、設定で出る経路が変わりそう。
* 計算時間は軽くなく、リアルタイムにガンガン回すより offline / deliberative 寄り。
* 低曲率領域向けの補助処理はやや heuristic で、理論的に完全にきれいな話ではない。

## 関連研究との違い

* 典型的な homotopy-based planning より、**経路の違いを invariant でなく neighborhood で見る**のが新しい。
* PRM で複数 path をサンプリングして後から分類する方法より、探索そのものの中で path distinction を扱っている。
* tether planning 文脈では、ケーブル長制約と経路多様性を 1 つの graph 的枠組みへ持ち込んでいるのが特徴。

## non-AIとして見る価値

* graph search と topology の間を、かなり実装しやすい形でつないでいる。
* 「複数 path が欲しい」ときに learned diversity へ行かず、構造側で解く好例。
* tethered robot のような niche 応用でも、コアは汎用的な planning design として読める。

## 難易度

★★★★☆

## 自分の理解/感想

* かなり知的に面白い論文で、トポロジーの重さをうまく graph search 側へ寄せて吸収している。
* path diversity をちゃんと扱いたい人には刺さるし、3D でそこまで大仰な前計算をしたくない現場には特に合いそう。
