# Radar Teach and Repeat: Architecture and Initial Field Testing

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | RADAR-Based Navigation |
| arXiv | [http://arxiv.org/abs/2409.10491](http://arxiv.org/abs/2409.10491) |
| Authors | Qiao, Xinyuan;Krawciw, Alec;Lilge, Sven;Barfoot, Timothy |
| Source | ICRA 2025 / arXiv |

## TL;DR

- FMCW radar だけで **teach and repeat** を閉ループ実証した off-road navigation 論文。
- continuous-time ICP と高レート gyro 補間で、4 Hz radar でも path tracking を成立させている。
- LiDAR より精度は落ちるが、**dust / fog / darkness に強い sensor choice** として radar を現実的に評価しているのが良い。

## Task

* Radar Navigation
* Teach and Repeat
* Off-Road Autonomy
* Localization

## Keywords

* FMCW Radar / ICP / Teach-and-Repeat / Gyro Fusion / Path Tracking

## AI依存度

* Non-AI

## 何を解決？

* LiDAR や camera は悪天候・粉塵・暗所でつらく、GPS も当てにできない環境がある。
* radar odometry の研究は増えているが、**実際に teach-and-repeat を閉ループで回した例** は少なかった。
* そこで、radar-only でも off-road autonomy がどこまでいけるかを実証したい。

## 何が新しい？

* FMCW radar を使った **closed-loop teach and repeat** の一式アーキテクチャ。
* 低レート radar scan の間を 100 Hz gyro で埋める高レート odometry レイヤ。
* LiDAR baseline と比較しつつ、radar の強みと弱みをかなり率直に示している点。

## どうやってる？

* teach phase では人が運転しながら radar scan から local submap を作り、odometry でつなぐ。
* odometry / localization は radar point cloud に対する ICP を continuous-time state 表現で解く。
* repeat phase では保存 submap に live radar を合わせ、gyro で高レート補間した pose を controller に渡す。
* その pose を使って path tracking を閉ループで回し、ルートを再走する。

## どこが強い？

* 「radar が使えるか」を demo でなく **実際の自律走行距離**で見せている。
* 悪条件での sensor robustness をちゃんと autonomy stack まで落としている。
* VT&R 系の枠組みに radar を載せ替える形なので、teach-and-repeat の理解にも良い。

## 弱そうなところ

* 精度はやはり LiDAR に負け、sparse scene や radial artifact にかなり苦しむ。
* 今回の実験は radar の強みである snow/fog/dust の極限条件までは十分踏み込んでいない。
* point extraction や artifact handling の tuning 余地がまだ大きい。

## 関連研究との違い

* CFEAR などの radar odometry 研究より、**closed-loop navigation 実証**まで持っていっている。
* LiDAR teach-and-repeat に比べ、精度より robustness を重視した sensor swap の色が強い。
* graph-SLAM で global consistency を追うより、local submap chaining の実務的構成。

## non-AIとして見る価値

* radar autonomy を learned perception ではなく、**ICP / gyro fusion / controller** で堅く組んでいる。
* センサ選定の trade-off を理解するうえでもかなり実用的。

## 難易度

★★★☆☆

## 自分の理解/感想

* method novelty は大きくないが、「radar だけで本当に走れるのか」にちゃんと答えているのが価値。
* LiDAR ほど綺麗ではないが、悪条件での fallback/autonomy sensor としての radar を考える入口になる。
