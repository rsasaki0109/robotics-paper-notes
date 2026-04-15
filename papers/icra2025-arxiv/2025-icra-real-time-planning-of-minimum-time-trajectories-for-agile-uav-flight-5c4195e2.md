# Real-Time Planning of Minimum-Time Trajectories for Agile UAV Flight

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Aerial Robots: Planning and Control |
| arXiv | [http://arxiv.org/abs/2409.16074](http://arxiv.org/abs/2409.16074) |
| Authors | Teissing, Krystof, Novosad, Matej, Penicka, Robert, Saska, Martin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- agile UAV flight の time-optimal trajectory planning を、**point-mass model ベースでミリ秒級**まで落としている。
- 軸ごとの加速度制約でなく **acceleration norm** を使い切る設計と、drag を含む簡略モデルが効いている。
- full dynamics の厳密最適化ほど美しくはないが、**onboard replanning できる速度**を狙った実務寄りの論文。

## Task

* Aerial Robots
* Trajectory Planning
* Optimal Control
* UAV

## Keywords

* Minimum-Time Planning / Point-Mass Model / Bang-Bang / Drag Modeling / NMPC

## AI依存度

* Non-AI

## 何を解決？

* multi-waypoint の time-optimal trajectory は、full multirotor dynamics で真面目に解くと重すぎて onboard replanning が難しい。
* 一方で、軽い近似モデルは速いが、推力制約や drag を雑に扱うせいで高速飛行では性能が落ちやすい。
* この論文は「最適性を少し犠牲にしても、実機で高速に回せる minimum-time planner」を狙っている。

## 何が新しい？

* point-mass model で **axis-wise ではなく norm ベースの加速度制約**を使い、使える推力をより素直に使っている点。
* PMM に **linear drag** を入れて、高速区間での tracking error を減らそうとしている点。
* 中間 waypoint の速度を gradient-based に最適化し、sampling よりかなり速く multi-waypoint 軌道を出す点。

## どうやってる？

* まず単一区間では、Pontryagin 的な bang-bang / bang-singular-bang 構造を使って区間時間を解析的に近く解く。
* 複数 waypoint の場合は、中間点での速度を最適化変数として持ち、総飛行時間が小さくなるように gradient update する。
* その際、重力と drag を point-mass dynamics に織り込んで、単なる理想加速度モデルより実機追従しやすくしている。
* 最終的な追従は NMPC 側に任せ、planner は「十分速くて大筋 time-efficient な reference を作る」役割にしている。

## どこが強い？

* とにかく速い。**minimum-time を onboard で回したい**という要求に対して、かなり筋が良い。
* full dynamics を捨てすぎず、drag や thrust utilization を入れているので、ただの雑な近似 planner で終わっていない。
* waypoint ベースで扱えるので、上位 planner / mission planner とつなぎやすい。

## 弱そうなところ

* heading や詳細な姿勢軌道まで planner 側では直接面倒を見ていない。
* gradient-based 最適化なので、多峰性が強い問題では局所解依存がありそう。
* obstacle avoidance 自体を直接やるわけではなく、collision-free な waypoint 列は別途必要。

## 関連研究との違い

* full-order direct collocation 系より、最適性よりも **replanning speed** を明確に優先している。
* polynomial trajectory 系より、bang-bang 構造を使って minimum-time により寄せている。
* 既存の PMM 系より、drag と thrust utilization の扱いが丁寧で、高速 flight 向けに一段実機寄り。

## non-AIとして見る価値

* 「速い planner」が learned policy ではなく、**簡略化した力学と解析構造**から出てきているのが面白い。
* UAV planning の世界で、モデルをどこまで簡略化すると実用速度が出るかのよい教材。

## 難易度

★★★☆☆

## 自分の理解/感想

* 理論的に一番美しいというより、agile flight を回すための良い engineering という印象。
* real-time minimum-time planning をやりたいなら、こういう「PMM + 追従側 NMPC」という分業はかなり現実的だと思う。
