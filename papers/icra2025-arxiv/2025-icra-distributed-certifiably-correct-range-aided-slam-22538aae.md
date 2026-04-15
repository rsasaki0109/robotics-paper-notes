# Distributed Certifiably Correct Range-Aided SLAM

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | SLAM 4 |
| arXiv | [http://arxiv.org/abs/2503.03192](http://arxiv.org/abs/2503.03192) |
| Authors | Thoms, Alexander, Papalia, Alan, Velasquez, Jared, Rosen, David, Narasimhan, Sriram |
| Source | ICRA 2025 / arXiv |

## TL;DR

- range-aided SLAM を multi-agent / distributed setting で、しかも **certifiably correct** に解こうとする `DCORA` の論文。
- RA-SLAM を QCQP → SDP → rank-restricted problem と整理し、Riemannian Staircase で globally optimality certificate まで見に行く。
- centralized CORA に近い精度を分散で狙っており、通信制約下の multi-robot SLAM としてかなり筋が良い。

## Task

* Multi-Robot SLAM
* Localization
* Range Sensing
* State Estimation

## Keywords

* Range-Aided SLAM / Certifiable Optimization / Riemannian Staircase / Distributed SLAM / Global Optimality

## AI依存度

* Non-AI

## 何を解決？

* 複数ロボットが UWB などの range 観測を持つとき、RA-SLAM は自然だが、非凸性と分散計算の両方が難しい。
* local method だけでは bad local minimum にはまりやすく、centralized solver は通信前提が重い。

## 何が新しい？

* RA-SLAM に対して **distributed certifiably correct** なアルゴリズムを与えた点。
* CORA 系の certifiable optimization を distributed setting へ拡張した点。
* dual certificate と staircase を組み合わせ、単なる良い近似解でなく最適性認証まで狙う点。

## どうやってる？

* RA-SLAM の最尤問題を QCQP として書き、そこから SDP 緩和へ落とす。
* rank-restricted SDP を Stiefel manifold 上の問題へ変え、Riemannian Staircase で解く。
* 各 agent は variable ownership に従って局所ブロック更新し、必要な情報だけ通信する。
* 解が得られたら dual certificate を計算して、global optimality を満たすか確認する。

## どこが強い？

* distributed SLAM でここまで理論保証を押し出しているのが強い。
* range 観測を含む multi-agent localization を、ちゃんと certifiable optimization の文脈へ乗せている。
* centralized 法の精度に近づけつつ、分散化の道筋を示している。

## 弱そうなところ

* 実装はかなり重く、Riemannian Staircase と certificate 計算の負担は小さくない。
* エージェント数や通信遅延が増えたときの scaling はシビアそう。
* 実データ評価はあるが、非常に大規模な swarm まで見たわけではない。

## 関連研究との違い

* 一般的な distributed SLAM は local convergence ベースで、global optimality certificate までは出さない。
* SE-Sync / CORA 系の certifiable PGO を、range-aided multi-agent setting に広げた位置づけ。
* back-end の安全性を上げる方向で、front-end robustness と違う価値を持つ。

## non-AIとして見る価値

* multi-robot SLAM を「なんとなく解く」のではなく、最適性認証つきで解く世界観が学べる。
* UWB / BLE / ranging を使う cooperative localization の back-end 設計としてかなり重要。

## 難易度

★★★★★

## 自分の理解/感想

* 数学は重いが、certifiable SLAM の流れを distributed まで伸ばしているのが良い。
* 実装難度は高いものの、multi-robot localization を本気でやるなら押さえておきたい一本。
