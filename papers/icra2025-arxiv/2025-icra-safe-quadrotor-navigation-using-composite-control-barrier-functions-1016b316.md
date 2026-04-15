# Safe Quadrotor Navigation Using Composite Control Barrier Functions

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Mechanics and Control 1 |
| arXiv | [http://arxiv.org/abs/2502.04101](http://arxiv.org/abs/2502.04101) |
| Authors | Harms, Marvin Chayton;Jacquet, Martin;Alexis, Kostas |
| Source | ICRA 2025 / arXiv |

## TL;DR

- cluttered environment で多数の障害物制約をそのまま扱うと重い、という CBF の弱点に対して、**composite CBF** で 1 つの滑らかな安全制約にまとめている。
- quadrotor の姿勢を直接ひっくり返さず、**3次系っぽい thrust dynamics** を入れた定式化で high-order CBF を扱いやすくしている。
- LiDAR ベースの実機実験まで出しており、**安全フィルタを最後段で被せる classical safety shield** としてかなり実用寄り。

## Task

* Aerial Robots
* Safe Navigation
* Control Barrier Functions
* Motion Control

## Keywords

* Composite CBF / High-Order CBF / Safety Filter / Quadrotor / Obstacle Avoidance

## AI依存度

* Non-AI

## 何を解決？

* CBF 系の安全制御は、障害物が増えると制約本数が増えすぎて計算が重くなりやすい。
* quadrotor では入力が推力・姿勢経由になるため、位置安全制約の relative degree も高くなり、そのままだと設計が面倒。
* つまり「安全性は欲しいが、dense obstacle でリアルタイムに回すのがしんどい」という問題を狙っている。

## 何が新しい？

* 各障害物の安全制約を soft-min 的にまとめた **composite CBF** で、多数制約を 1 本の滑らかな制約として扱う点。
* quadrotor の平動側を high-order CBF で扱いやすくするために、**artificial thrust dynamics** を入れた 3 次系表現を使っている点。
* nominal controller が多少雑でも、その上に safety filter を被せて衝突回避を担保する構成を実機で見せている点。

## どうやってる？

* 障害物との距離に基づく安全関数を各障害物について作り、それを exponential / high-order CBF の形で微分して扱う。
* 個別制約をそのまま QP に全部入れる代わりに、soft-min でまとめた **composite barrier** を作って単一制約化する。
* 制御入力は QP で補正し、nominal tracking controller の出力を「危ないときだけ」安全側に押し戻す。
* 実装上は、姿勢を全面的に最適化するのではなく、推力方向と平動安全性をつなぐ形で整理しているので、MPC より軽い safety layer として使いやすい。

## どこが強い？

* 障害物数が多い場面でもスケールしやすく、**CBF の現場実装しづらさ**に真正面から答えている。
* 「planner を全部置き換える」のではなく、既存 controller の上に安全層を足す設計なので導入しやすい。
* 論文としても theory だけでなく LiDAR 実機まで出しており、絵に描いた餅感が薄い。

## 弱そうなところ

* soft-min 系は smoothing parameter のチューニングが必要で、鋭くしすぎると数値的に不安定になりやすい。
* composite によって制約本数は減るが、個々の障害物の意味が薄れるので、場面によっては保守的/鈍感になる可能性がある。
* 位置安全には強いが、heading や高次の mission-level behavior まで面倒を見るものではない。

## 関連研究との違い

* 1 障害物 1 CBF の素直なやり方より、**多数制約をまとめる**ところが明確に違う。
* cascaded QP や backstepping っぽい構成に比べると、最後段 safety filter としての見通しが良い。
* MPC ベースの衝突回避よりも軽量で、安全集合の forward invariance を前面に出した classical control 論文。

## non-AIとして見る価値

* 安全性を「policy が賢くなること」に期待せず、**安全制約を明示的に設計する**立場がはっきりしていて良い。
* aerial robot の安全制御を学ぶ入口として、CBF の実装上の痛点と工夫がまとまっている。

## 難易度

★★★★☆

## 自分の理解/感想

* CBF を実機に持っていくときの「障害物が多いとつらい」をかなり素直に解いた論文に見える。
* 飛行体の安全制御としては地味に見えるが、既存 stack に足しやすい safety shield という意味で実務価値が高い。
