# Single-Stage Optimization of Open-Loop Stable Limit Cycles with Smooth, Symbolic Derivatives

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Legged Locomotion: Novel Methods |
| arXiv | [http://arxiv.org/abs/2312.10647](http://arxiv.org/abs/2312.10647) |
| Authors | Saud Ul Hassan, Muhammad;Hubicki, Christian |
| Source | ICRA 2025 / arXiv |

## TL;DR

- open-loop stable な periodic gait を、**single-stage optimization** で直接求めようとする論文。
- monodromy matrix の固有値制約をいくつか比較し、**Schur decomposition** が一番扱いやすいと示している。
- open-loop stability を明示制約に入れる発想がかなり良い。

## Task

* Legged Locomotion
* Trajectory Optimization
* Periodic Gaits
* Stability Analysis

## Keywords

* Limit Cycle / Direct Collocation / Monodromy Matrix / Schur Decomposition / Open-Loop Stability

## AI依存度

* Non-AI

## 何を解決？

* legged gait design では feedback stabilization が主役になりがちで、open-loop stability 自体は後回しにされやすい。
* しかし inherent に安定な limit cycle を作れれば、feedback の負担を減らせる。
* その一方で、**安定性を最適化制約に直接入れる**のは数値的に難しい。

## 何が新しい？

* periodicity だけでなく、monodromy matrix の spectral radius を explicit に制約する single-stage optimization。
* 固有値制約の書き方を複数比較し、Schur decomposition が最も robust と示した点。
* hybrid hopping system でも実用的に解けることを見せた点。

## どうやってる？

* Direct Collocation で周期運動の最適化問題を立てる。
* periodic boundary condition に加え、monodromy matrix の固有値が単位円内へ入るよう制約する。
* Frobenius norm, power iteration, eigendecomposition, Schur などの定式化を比較する。
* その結果、Schur ベースが数値的に安定で、収束性も良かったと報告している。

## どこが強い？

* stability を後付け評価でなく、**最適化の本体に入れている**のが本質的に強い。
* limit cycle design の数値実装で何が効くかを丁寧に比較している。
* 高速に stable hopping gait を出せる可能性が見えている。

## 弱そうなところ

* 固有値制約の書き方によって、得られる gait が結構変わる。
* hybrid dynamics と接触不連続のせいで、最適化は依然として繊細。
* model uncertainty や online adaptation までは直接扱っていない。

## 関連研究との違い

* two-stage gait optimization より、**1 回の最適化で stability まで入れる**。
* post-impact state を間接的に置く手法より、固有値を直接見にいく。
* shooting 系より、Direct Collocation ベースで underactuated/hybrid 系へ使いやすい。

## non-AIとして見る価値

* locomotion stability を、経験的 tuning でなく **固有値と limit cycle 理論**で詰める classical ど真ん中の論文。
* gait optimization に stability をどう入れるかの教材としてかなり良い。

## 難易度

★★★★☆

## 自分の理解/感想

* 数値的には繊細だけど、やろうとしていることはとても正しい。
* Schur を推す結論も実務的で、limit-cycle optimization を触る人にはかなりありがたい。
