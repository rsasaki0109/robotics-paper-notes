# Benchmarking Different QP Formulations and Solvers for Dynamic Quadrupedal Walking

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Legged Robots |
| arXiv | [http://arxiv.org/abs/2502.01329](http://arxiv.org/abs/2502.01329) |
| Authors | Stark, Franek;Middelberg, Jakob;Mronga, Dennis;Vyas, Shubham;Kirchner, Frank |
| Source | ICRA 2025 / arXiv |

## TL;DR

- quadruped walking で使う QP について、**formulation / solver / hardware** をまとめて比べた実務寄りベンチマーク。
- MPC では **sparse + HPIPM** が強く、WBC では problem size が小さいため formulation 差のほうが効く、というかなり役立つ結論が出ている。
- 論文の芯は新アルゴリズムではなく、**Solve Frequency per Watt (SFPW)** という省電力込み指標を含めた比較にある。

## Task

* Legged Robots
* Model Predictive Control
* Whole-Body Control
* Benchmarking

## Keywords

* QP Solver / Sparse MPC / Condensing / Whole-Body Control / SFPW

## AI依存度

* Non-AI

## 何を解決？

* legged control では MPC でも WBC でも QP を解くが、どの solver・定式化・計算機を選ぶべきかは経験則に寄りがち。
* solve time だけ見ると見誤ることがあり、embedded robot では消費電力まで含めた効率も重要。
* つまり「controller の中身」以前に、**何で解くのが最適か**を整理したいという論文。

## 何が新しい？

* sparse / partially condensed / dense の各 QP formulation を、複数 solver と複数 hardware 上で系統比較している点。
* solve frequency を消費電力で割った **SFPW** を持ち込んで、embedded 向け比較をやっている点。
* quadruped MPC と WBC の両方で、どこに formulation の差が効くかを切り分けている点。

## どうやってる？

* 単一剛体近似ベースの MPC と、TSID 系の WBC 問題を benchmark 問題として用意する。
* それぞれについて、sparse / condensed などの定式化と、HPIPM・OSQP・qpOASES などの solver を組み合わせて比較する。
* desktop x86 だけでなく ARM 系も含めて測り、solve rate と power の両方を見る。
* 結果として、MPC は疎構造を活かせる solver が強く、WBC 側は問題規模がそこまで大きくないため solver 差が小さい、と整理している。

## どこが強い？

* 実装者にそのまま役立つ。「どれを使うべきか」にかなり直接答えている。
* 新手法の宣伝でなく、比較論文としてフラットに見えるのが良い。
* ARM が電力効率で有利、という現場的な結論もちゃんと出している。

## 弱そうなところ

* solver の hyperparameter tuning を深くやっていないので、順位は設定次第で少し動きうる。
* horizon や problem size の範囲は限られており、もっと大きい MPC でどうなるかは追加で見たい。
* そもそものダイナミクスモデルは簡略化されているので、実機の複雑さすべてを代表しているわけではない。

## 関連研究との違い

* generic QP benchmark と違って、**quadruped locomotion の MPC / WBC** に特化している。
* controller 提案論文の一部で軽く比較するのではなく、solver / formulation / hardware を主題にしている。
* performance だけでなく energy efficiency を前に出しているのが特徴。

## non-AIとして見る価値

* classical control の世界では、アルゴリズムだけでなく **数値最適化の実装選択** が性能を決めることがよく分かる。
* legged MPC / WBC をこれから触る人にとって、かなり実務的な地図になる。

## 難易度

★★★☆☆

## 自分の理解/感想

* 新規性は控えめでも、こういう benchmark は実際かなりありがたい。
* 論文としては派手ではないが、`どの solver を使うか問題` に答えてくれるので手元に置きたいタイプ。
