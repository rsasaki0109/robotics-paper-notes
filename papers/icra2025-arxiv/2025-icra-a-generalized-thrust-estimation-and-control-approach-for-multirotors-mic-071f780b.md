# A Generalized Thrust Estimation and Control Approach for Multirotors Micro Aerial Vehicles

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Mechanics and Control 1 |
| arXiv | [http://arxiv.org/abs/2412.02874](http://arxiv.org/abs/2412.02874) |
| Authors | Santos, Davi Henrique dos, Saska, Martin, Nascimento, Tiago |
| Source | ICRA 2025 / arXiv |

## TL;DR

- rotor thrust を単純な二次式でなく、**BEMT ベースの一般化 thrust estimator** で推定して制御に入れる論文。
- platform ごとに大量キャリブレーションする代わりに、**1点キャリブレーション + 物理モデル** で済ませようとしているのが実務的。
- 省電力性は少し悪化するが、wind gust を含む実環境では tracking robustness が上がっている。

## Task

* Aerial Robots
* Low-Level Control
* Thrust Estimation
* Flight Dynamics

## Keywords

* BEMT / Thrust Mapping / PX4 / Feedforward PID / Aerodynamic Modeling

## AI依存度

* Non-AI

## 何を解決？

* multirotor の下層制御では、推力とロータ速度の関係を単純な二次式で近似することが多い。
* しかし forward flight や風のある状況では、その近似が崩れて tracking error が上位制御へ波及しやすい。
* つまり、**hover 前提の雑な thrust map** をもう少し物理寄りに置き換えたい。

## 何が新しい？

* BEMT をベースにした thrust / power 推定を、ESC telemetry だけで real-time に回している点。
* 多数の係数同定でなく、既知の空力係数をベースに **最小限の platform fitting** へ落としている点。
* PX4 に統合できる軽さで、feedforward thrust control として実装している点。

## どうやってる？

* 電流・電圧・回転数から mechanical / aerodynamic power を見積もる。
* induced inflow や stream inflow を含む BEMT モデルを立て、Newton-Secant 的な反復で thrust を解く。
* その推定 thrust を使って、attitude controller の下で thrust tracking 用の feedforward PID を回す。
* 既存 PX4 の simple thrust map を差し替える形なので、stack に入れやすい。

## どこが強い？

* モデルベースなのに重すぎず、**autopilot に現実的に入る**。
* 1点キャリブレーションで platform 間へ展開しやすい。
* outdoor 風外乱下での改善をちゃんと見せていて、机上モデルで終わっていない。

## 弱そうなところ

* power consumption は増えており、電費重視 mission では単純には喜べない。
* decoupling や小角近似に依るので、極端な flight regime では破綻しうる。
* thrust map は改善しても、他の空力/姿勢誤差まですべて救えるわけではない。

## 関連研究との違い

* 純粋な empirical polynomial thrust model より、**空力の物理構造を残している**。
* full BEMT の重い identification 系より、autopilot 実装に乗るよう簡略化している。
* learning ベースの rotor model より、訓練データなしで解釈可能。

## non-AIとして見る価値

* drone control の性能は policy だけでなく、**最下層の thrust estimation** でもかなり変わることが分かる。
* BEMT を flight stack にどう埋めるかの良い実例。

## 難易度

★★★☆☆

## 自分の理解/感想

* 派手さはないが、PX4 周辺の実務にはかなり効きそうな改善。
* 「上位 controller を賢くする前に、まず thrust map を真面目にしよう」という姿勢がとても健全。
