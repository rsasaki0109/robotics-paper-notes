# Enhancing Robotic System Robustness Via Lyapunov Exponent-Based Optimization

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Optimization and Optimal Control |
| arXiv | [http://arxiv.org/abs/2412.06776](http://arxiv.org/abs/2412.06776) |
| Authors | Fadini, Gabriele, Coros, Stelian |
| Source | ICRA 2025 / arXiv |

## TL;DR

- ロボットの robustness を、**Lyapunov exponent** を直接最適化することで高めようとする論文。
- differentiable simulation 上で hardware / control parameter を一緒に調整し、trajectory sensitivity を下げる。
- equilibrium だけでなく limit cycle にも自然に使える robustness metric なのが良い。

## Task

* Optimization
* Robustness Analysis
* Co-Design
* Differentiable Simulation

## Keywords

* Lyapunov Exponents / Robustness Metric / Co-Optimization / JAX / Contact Dynamics

## AI依存度

* Non-AI

## 何を解決？

* ロボット最適化は task performance を主に見がちで、頑健性は後付けになりやすい。
* stochastic stress test だけでは高 DoF / contact-rich robot の robustness を設計へうまく戻しにくい。
* そこで、**trajectory が摂動にどれだけ敏感か**を、もっと根本的な dynamical metric で最適化したい。

## 何が新しい？

* Lyapunov exponent を differentiable に計算し、gradient-based co-design に使う点。
* floating-base / contact system に対して、SVD ベースで非正方 Jacobian も扱える実装。
* manipulator, spider, quadruped など複数系で、hardware/control co-optimization まで見せている点。

## どうやってる？

* differentiable simulator 上で trajectory rollout を行う。
* 各 time step の state transition Jacobian から singular value を求め、Lyapunov spectrum を近似する。
* その総和や代表値を robustness objective として、design/control parameter に勾配を返す。
* ADAM などで link parameter や gain を更新し、より収束的なダイナミクスを目指す。

## どこが強い？

* robustness を ad-hoc metric でなく、**非線形力学の本流の量**で見ているのが強い。
* limit cycle を自然に扱えるので locomotion 系にも相性が良い。
* differentiable simulation とかなり相性が良く、co-design 指標として綺麗。

## 弱そうなところ

* 長い rollout が必要で、gradient quality と計算量が厳しい。
* contact smoothing を入れた simulator の artifact に引っ張られる可能性がある。
* 現状は simulation 中心で、real hardware transfer はまだ未知数。

## 関連研究との違い

* 単なる robustness proxy や stress test より、**Lyapunov exponent を直接見る**。
* region-of-attraction 系より、limit cycle を自然に扱える。
* data-driven robustness metric より、完全に mechanics / dynamics ベース。

## non-AIとして見る価値

* robustness を「たくさん試して壊れなかった」ではなく、**力学系の性質として最適化**する発想が面白い。
* differentiable robotics の中でもかなり classical theory 寄り。

## 難易度

★★★☆☆

## 自分の理解/感想

* 発想はとても良く、co-design に一本芯を通す metric として魅力がある。
* 一方で、実務投入には simulator artifact と rollout 長さの問題がまだ重そう。
