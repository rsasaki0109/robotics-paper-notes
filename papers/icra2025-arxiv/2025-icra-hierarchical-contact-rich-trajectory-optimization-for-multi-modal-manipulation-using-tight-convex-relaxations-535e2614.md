# Hierarchical Contact-Rich Trajectory Optimization for Multi-Modal Manipulation Using Tight Convex Relaxations

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Manipulation Planning |
| arXiv | [http://arxiv.org/abs/2503.07963](http://arxiv.org/abs/2503.07963) |
| Authors | Shirai, Yuki;Raghunathan, Arvind;Jha, Devesh |
| Source | ICRA 2025 / arXiv |

## TL;DR

- contact-rich manipulation を、**K-OPT -> C-OPT -> Q-OPT の階層最適化**に分けて現実的に解こうとしている。
- contact mode を固定せずに、MILP と tight convex relaxation を使って **接触位置・接触力・物体軌道**を同時に詰めるのが肝。
- quasi-static 前提ではあるが、pivoting / sliding / regrasping みたいな multi-modal manipulation をかなりうまく扱っている。

## Task

* Manipulation Planning
* Contact-Rich Manipulation
* Trajectory Optimization
* Convex Relaxation

## Keywords

* Contact Planning / MILP / McCormick Relaxation / Quasi-Static Manipulation / Multi-Modal

## AI依存度

* Non-AI

## 何を解決？

* contact-rich manipulation は、軌道だけでなく「どこで接触するか」「いつ接触を切り替えるか」まで同時に考える必要がある。
* これを全部一発で解こうとすると mixed-integer nonlinear problem になって重すぎる。
* 既存法は接触モード固定や緩い近似に寄りがちで、複雑な multi-step manipulation をきれいに扱いにくかった。

## 何が新しい？

* kinematic planning、contact selection、full nonlinear refinement を **3 段階に分ける階層構造**。
* contact wrench の bilinear 項に対して、**binary encoding 付きの tighter convex relaxation** を使って計算量を落としている点。
* 下流の refinement が infeasible だった contact plan を cutting-plane 的に弾き返すループを持たせている点。

## どうやってる？

* まず K-OPT で、物体がどう動くか・どの接触状態がありそうかを粗く決める。
* 次に C-OPT で、接触位置や接触力を mixed-integer に近い形で選びつつ、moment balance の bilinear 項を tight relaxation で近似する。
* 最後に Q-OPT で、選ばれた contact pattern を前提に full nonlinear な quasi-static trajectory optimization で磨く。
* 下流でダメなら、その接触組み合わせを上流で禁止して再探索するので、階層分割の弱点を少し補っている。

## どこが強い？

* contact mode を固定しないのに、完全一体最適化よりはかなり現実的な計算量に落としている。
* binary encoding で piecewise relaxation のサイズを減らしており、単なる「分けました」以上の工夫がある。
* bimanual hardware demo まであり、pivot / sliding のような複雑接触がちゃんと出ている。

## 弱そうなところ

* quasi-static かつ planar 寄りなので、高速で慣性が効く manipulation にはそのまま乗りにくい。
* 階層構造なので、上流の粗い解が悪いと下流で苦しくなる。
* 実機も open-loop 寄りで、model mismatch に対しては feedback 併用が前提になりそう。

## 関連研究との違い

* 固定 contact mode 前提の contact-implicit optimization より、**接触選択をもっと自由に残している**。
* ただの McCormick relaxation より、binary encoding による tighter / smaller な定式化が効いている。
* manipulation planning と contact force optimization を分業しつつ、最終的に nonlinear refinement まで戻すのが特徴。

## non-AIとして見る価値

* manipulation を learned policy で押し切らず、**接触の組合せ爆発をどう数理最適化で扱うか**が見える。
* contact-rich planning の教科書的な難しさと、その妥協点がかなり分かりやすい。

## 難易度

★★★★★

## 自分の理解/感想

* 発想としてはすごくまっとうで、「全部同時最適化は重すぎるから階層化し、でも緩みすぎないよう relaxation を締める」という流れが綺麗。
* real-time control ではないが、offline / receding-horizon manipulation planner の設計材料としてかなり良い。
