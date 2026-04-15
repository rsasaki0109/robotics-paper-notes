# A Complete and Bounded-Suboptimal Algorithm for a Moving Target Traveling Salesman Problem with Obstacles in 3D

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Motion Planning 3 |
| arXiv | [http://arxiv.org/abs/2504.14680](http://arxiv.org/abs/2504.14680) |
| Authors | Bhat, Anoop;Gutow, Geordan;Vundurthy, Bhaskar;Ren, Zhongqiang;Rathinam, Sivakumar;Choset, Howie |
| Source | ICRA 2025 / arXiv |

## TL;DR

- moving target TSP with obstacles in 3D に対して、初めて **complete かつ bounded-suboptimal** なアルゴリズム `FMC*-TSP` を与えた論文。
- target order を決める高レベル探索と、GCS 上で軌跡を解く低レベル探索を組み合わせ、訪問順序と時空間 feasibility を両方見る。
- 3D 障害物環境・時間窓付き moving targets を、理論保証つきで扱っているのが大きい。

## Task

* Motion Planning
* Control

## Keywords

* MT-TSP / GCS / Focal Search / Time Windows / Complete Algorithm

## AI依存度

* Non-AI

## 何を解決？

* moving targets を time window 内に捕捉しつつ障害物回避して帰還する問題は、順序計画と幾何計画が強く結び付く。
* 既存法は 2D 前提だったり、sampling 近似で完全性や suboptimality 保証を失いやすい。

## 何が新しい？

* MT-TSP-O を **3D** で扱い、complete + bounded-suboptimal を同時に出している点。
* target-window graph による高レベル順序探索と、GCS 上の low-level FMC* を分けた設計。
* infeasible な順序や prefix を forbidden set として蓄積し、探索を剪定する枠組み。

## どうやってる？

* 高レベルでは、target と time window をまとめた graph 上で GTSP-TW 風に候補 tour を探索する。
* 低レベルでは、free space の convex decomposition を用いた GCS を作り、FMC* で時間最小軌跡を探索する。
* infeasible tour は forbidden prefix として記録し、次の高レベル探索に返して無駄探索を減らす。
* 焦点探索と lower bound を組み合わせ、bounded-suboptimality の保証を作っている。

## どこが強い？

* 3D moving-target planning で complete / bounded-suboptimal をちゃんと明示しているのが強い。
* 順序計画と軌跡計画を疎結合にしすぎず、相互に infeasibility 情報を返す設計が良い。
* UAV 補給や空中インターセプトのような応用へ直結しやすい。

## 弱そうなところ

* 高レベル MILP / combinatorial search が大きくなると、ターゲット数や窓長の増大に敏感そう。
* 実験はそこまで超大規模ではなく、実用スケールでの計算時間はさらに見たい。
* target motion model が比較的単純なので、複雑な予測誤差まで入ると難しさが増す。

## 関連研究との違い

* 既存の moving target planning は 2D 化や point sampling に寄るものが多く、3D での保証が弱い。
* 単なる route-first / plan-second ではなく、low-level infeasibility を上位へ返すのが本手法の肝。
* GCS を動的 target 問題へ持ち込んで、幾何と combinatorics を両方整えた点が特徴。

## non-AIとして見る価値

* 「順序最適化」と「軌跡最適化」をどうつなぐかの設計がかなり勉強になる。
* planning 側の Top 12 枠として、保証のある classical algorithm を読むならかなり良い一本。

## 難易度

★★★★☆

## 自分の理解/感想

* 理論保証を崩さずに 3D へ持って行っているのが偉い。泥臭いが価値の高い planning 論文。
* 実機へ直結するには計算時間との戦いが残るが、読み筋がはっきりしていて好き。
