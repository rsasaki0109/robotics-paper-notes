# Enhancing Feature Tracking Reliability for Visual Navigation Using Real-Time Safety Filter

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Localization 6 |
| arXiv | [http://arxiv.org/abs/2502.01092](http://arxiv.org/abs/2502.01092) |
| Authors | Kim, Dabin;Jang, Inkyu;Han, Youngsoo;Hwang, Sunwoo;Kim, H. Jin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- visual navigation で十分な feature を見失わないよう、**visibility を制御制約として扱う safety filter** を提案している。
- 参照入力をなるべく崩さずに、QP ベースの filter でロボット速度を修正し、**必要な visual information score を下回らない**ようにする。
- belief-space planning のような重い手法ではなく、**リアルタイムな制御層で feature tracking reliability を守る**発想が面白い。

## Task

* Visual Navigation
* Feature Tracking
* Safety Filter
* Control for Perception

## Keywords

* Quadratic Programming / Control Barrier Function / Visibility Constraint / Real-Time Filtering

## AI依存度

* Non-AI

## 何を解決？

* visual odometry / V-SLAM は、追跡できる feature 数が落ちるとすぐ不安定になる。
* 既存の navigation は目標追従や障害物回避は見ても、**「特徴点が見え続けるか」**までは制御で守らないことが多い。
* その結果、texture が薄い場所や視野条件が悪い姿勢に入ると、state estimation 側にしわ寄せが出る。

## 何が新しい？

* 可視 landmark の重み付き総量を **safety condition** として定義し、forward invariance を保つ filter に落としている。
* 離散的で扱いにくい visibility 条件を、そのままではなく **補助変数を入れて滑らかに扱える制約系**へ変形している。
* planning ではなく、**reference controller の上に被せる QP filter** として実装しているので実時間性が高い。

## どうやってる？

* ロボット運動学と landmark の見え方を関係づけ、現在の状態でどれだけ feature visibility を確保できているかを score 化する。
* その score が閾値を割らないよう、Nagumo 的な前進不変条件に基づく不等式制約を作る。
* 実際の制御入力は、「元の reference input にできるだけ近い」という目的関数つきの **QP** で毎ステップ解く。
* landmark の出入りや visibility 変化を、補助状態を介して連続的に扱えるようにし、制約系をリアルタイムに更新する。

## どこが強い？

* 視覚情報を「nice to have」ではなく、**守るべき制約**として明示しているのが強い。
* pose estimation 側の内部に手を入れなくても、上位の navigation / tracking controller に載せやすい。
* 参照入力からの逸脱を最小化する形なので、過度に保守的な挙動になりにくい。
* 数学的保証と実装の軽さのバランスが良く、classical control の使いどころがきれい。

## 弱そうなところ

* 「停止可能な入力が常にある」など、理論保証のための仮定は実機では強め。
* landmark 位置や visibility 判定が大きくずれると、filter の前提そのものが崩れる。
* 実験は説得力があるが、超大規模 SLAM や激しい occlusion を含む場面まで見ているわけではない。

## 関連研究との違い

* belief-space planning や perception-aware trajectory optimization より、**局所・即応的な制御補正**に寄せている。
* 一般的な CBF / safety filter は衝突回避を扱うことが多いが、この論文は **feature visibility** を安全性の対象にしている。
* 視覚サーボのように特定ターゲットを見る話ではなく、navigation 用 feature set を維持する点が違う。

## non-AIとして見る価値

* perception と control をつなぐ古典的アプローチの好例で、learned active perception と違って挙動理由を説明しやすい。
* QP filter と invariance condition の組み合わせは、そのまま他の sensing constraints にも横展開しやすい。
* feature が消える前に制御で守る、という考え方自体が実務上かなり有用。

## 難易度

★★★★☆

## 自分の理解/感想

* 「見えるように計画する」ではなく「見えなくならないように制御で守る」という切り方がうまい。
* VIO / SLAM の failure mode を control 側で減らしたい人にはかなり刺さる論文で、理論も実装もわりと筋が良い。
