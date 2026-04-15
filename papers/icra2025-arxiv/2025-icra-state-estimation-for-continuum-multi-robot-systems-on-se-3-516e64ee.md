# State Estimation for Continuum Multi-Robot Systems on SE(3)

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | State Estimation |
| arXiv | [http://arxiv.org/abs/2401.13540](http://arxiv.org/abs/2401.13540) |
| Authors | Lilge, Sven, Barfoot, Timothy, Burgner-Kahrs, Jessica |
| Source | ICRA 2025 / arXiv |

## TL;DR

- continuum multi-robot system の shape / strain estimation を、**SE(3) 上の Gaussian process + factor graph** で解く論文。
- 並列・協調・混合トポロジまで含む **任意結合 topology** を扱えるのが大きい。
- force/moment を直接知らなくても、Cosserat rod ベース prior と sensor fusion で実時間推定している。

## Task

* State Estimation
* Continuum Robotics
* Sensor Fusion
* Factor Graph Optimization

## Keywords

* SE(3) / Gaussian Process / Cosserat Rod / FBG / EM Tracking / Sparse Cholesky

## AI依存度

* Non-AI

## 何を解決？

* continuum robot は変形自由度が大きく、単体でも状態推定が難しい。
* それが複数本結合された parallel / collaborative system になると、serial robot 用 estimator では対応しにくい。
* material parameter や外力が不確かでも、**形状とひずみを連続体として推定**したい。

## 何が新しい？

* coupled continuum multi-robot system 全般を扱える一般的な state estimator。
* SE(3) 上の GP prior と factor graph を組み合わせ、shape と strain を arclength 上で推定する点。
* FBG / EM tracking を含む測定モデルと coupling constraint を、疎構造を壊しすぎず入れている点。

## どうやってる？

* 各 continuum robot を Cosserat rod 系の簡略 prior で表し、arclength 離散点上に pose / strain state を置く。
* pose は SE(3) 上、strain は Euclidean 量として factor graph に載せる。
* prior factor、measurement factor、robot 間 coupling factor をまとめて MAP 推定する。
* Hessian の疎構造を使って sparse Cholesky で解き、連続位置への補間は GP で行う。

## どこが強い？

* continuum multi-robot という難しい設定に対して、**かなり一般的な枠組み**を出している。
* topology 依存の特殊解法に寄らず、parallel / collaborative を同じ考えで扱える。
* 実時間級の計算時間と実機検証があり、理論だけで終わっていない。

## 弱そうなところ

* quasi-static 色が強く、高速ダイナミクスまでは直接見ていない。
* calibration と hyperparameter tuning の負担は小さくなさそう。
* constant-strain 寄りの prior は、強い外力や複雑変形で限界がありうる。

## 関連研究との違い

* 単一 continuum robot 用 estimator より、**coupled system topology** を明示的に扱える。
* learned basis / data-driven approach より、完全に mechanics と probabilistic estimation ベース。
* shooting method や特殊 parallel robot 向け方法より、より一般的で factor graph 的。

## non-AIとして見る価値

* continuum robotics で state estimation をどう立てるかが、**SE(3)・GP・Cosserat rod** の接続としてきれいに見える。
* soft/continuum robot の classical estimation を学ぶ入口としてかなり良い。

## 難易度

★★★★☆

## 自分の理解/感想

* 数学的には重いが、かなり良い classical robotics 論文。
* continuum robot を複数本つないだ時点で一気に難しくなるので、その一般枠組みを出している価値は高い。
