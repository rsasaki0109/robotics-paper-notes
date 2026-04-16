# Non-Conservative Obstacle Avoidance for Multi-Body Systems Leveraging Convex Hulls and Predicted Closest Points

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Motion Planning 3 |
| arXiv | [http://arxiv.org/abs/2410.12659](http://arxiv.org/abs/2410.12659) |
| Authors | Rassaerts, Lotte, Suichies, Eke Janke, van de Vrande, Bram, Alonso, Marco, Meere, Bastiaan Guillermo Lorenzo, Chong, Michelle S., Torta, Elena |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 凸包で表した multi-body robot に対し、**現在の closest point だけでなく予測された closest point** も MPC 制約へ入れる obstacle avoidance 手法。
- closest point が急に切り替わると距離予測が壊れやすい、という凸包ベース回避の実務的な弱点をかなり真っ当に潰している。
- 医療系 IGT robot で検証しており、保守的すぎる近似を避けつつ滑らかさと安全性を上げる、という狙いがはっきりしている。

## Task

* Obstacle Avoidance
* Model Predictive Control
* Convex Hull Geometry
* Multi-Body Robot Control

## Keywords

* Closest Point Prediction / Convex Hull / GJK / MPC / Shared Control

## AI依存度

* Non-AI

## 何を解決？

* 複雑形状ロボットの collision avoidance では、球近似は保守的すぎ、厳密形状をそのまま扱うと重い。
* 凸包ベースで closest point distance を使う路線は有力だが、回転や姿勢変化で **closest point が不連続に飛ぶ**と予測が不安定になる。
* そのせいで controller が振動したり、必要以上に離れたり、逆に危険な接近を見逃したりする。

## 何が新しい？

* 現在の closest point だけを見るのではなく、**予測 horizon 内の closest point 候補**を制約に入れている。
* closest point が近傍で切り替わるときのノイズを抑えるため、**point smoothing / selection の工夫**を入れている。
* これを shared-control 系の MPC に載せ、医療ロボットで「安全だが過剰には逃げない」挙動を狙っている。

## どうやってる？

* ロボットと障害物を convex hull 群で表し、各時刻で距離と勾配を計算する。
* MPC は通常どおり future state を予測するが、距離制約は単一の現在 closest point 線形化だけでなく、**将来予測された closest point**にも基づいて作る。
* 予測中に衝突や point switching が起きそうな場合は、平滑化や hull 縮小の工夫で constraint を安定化させる。
* これにより、必要以上に conservative な近似を避けつつ、制御入力の滑らかさも確保する。

## どこが強い？

* closest point switching という、幾何ベース回避で本当に困るところを正面から扱っている。
* sphere approximation より空間を有効に使え、**non-conservative** の看板にそれなりの中身がある。
* 医療ロボットの shared control という応用先が具体的で、評価も単なる simulation で終わっていない。
* geometry と MPC のつなぎ方がわかりやすく、他の複雑形状ロボットにも発想を移植しやすい。

## 弱そうなところ

* 複数 closest point 候補をどう間引くか、平滑化閾値をどう取るかに設計依存がある。
* 非凸や極端に多リンクな系では、凸包分解と距離計算の負担が効いてきそう。
* 理論保証よりも実務改善寄りで、最適性や収束性の話はそこまで強くない。

## 関連研究との違い

* 単純な球近似ベース回避より、**形状忠実度を保ったまま保守性を減らす**方向。
* closest point を 1 本だけ固定して線形化する既存 MPC より、future switching を見越している点が違う。
* swept volume や厳密衝突判定寄りの手法より、MPC に素直に入る近似として扱いやすい。

## non-AIとして見る価値

* collision avoidance で learned policy を使わず、幾何計算と MPC だけでかなり詰められることがわかる。
* closest point / hull / linearized distance constraints の設計は、実ロボに落とすときに非常に参考になる。
* 「保守的すぎる安全」と「危ない最適化」の間を classical に埋める良い例。

## 難易度

★★★☆☆

## 自分の理解/感想

* 派手ではないが、実機 MPC をやる人が本当に欲しい改善という感じで好印象。
* 予測 closest point を入れる発想は自然だが、closest point switching を丁寧に扱っているぶん、実装論文として価値がある。
