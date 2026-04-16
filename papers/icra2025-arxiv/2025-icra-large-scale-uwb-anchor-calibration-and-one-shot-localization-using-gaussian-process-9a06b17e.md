# Large-Scale UWB Anchor Calibration and One-Shot Localization Using Gaussian Process

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Calibration 3 |
| arXiv | [http://arxiv.org/abs/2412.16880](http://arxiv.org/abs/2412.16880) |
| Authors | Yuan, Shenghai;Lou, Boyang;Nguyen, Thien-Minh;Yin, Pengyu;Li, Jianping;Xu, Xinhang;Cao, Muqing;Xu, Jie;Chen, Siyu;Xie, Lihua |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 広い warehouse / seaport 環境で、**UWB anchor calibration を one-shot でやる**ために GP を使った論文。
- continuous-time LIO で作った軌跡と UWB range を合わせ、GPS なしでも anchor 位置を較正している。
- その較正済み UWB を loop-closure / one-shot localization の search-space 削減に使う構成が実務的。

## Task

* Calibration
* Localization
* UWB
* Sensor Fusion

## Keywords

* UWB Calibration / Gaussian Process / CT-LIO / One-Shot Localization / Descriptor Filtering

## AI依存度

* Non-AI

## 何を解決？

* 大規模屋外・半屋内では GPS が不安定で、UWB anchor の配置較正も簡単ではない。
* UWB 単独の one-shot localization は NLoS や range bias で壊れやすく、LiDAR descriptor だけでも repetitive scene では false positive が多い。
* そこで、**anchor calibration と one-shot localization を現場スケールで現実的に回したい**。

## 何が新しい？

* CT-LIO 軌跡と UWB range を使い、**Gaussian Process で大規模 anchor calibration** を行う点。
* calibration 結果を、STD など descriptor-based localization の検索範囲フィルタとして使う点。
* 600x450 m 級の環境で、UWB を trilateration の主役でなく **search-space reduction の補助情報**として使っている点。

## どうやってる？

* 車体に LiDAR / IMU / UWB を積んで 1 回走行し、CT-LIO で連続時間軌跡を作る。
* その軌跡と UWB 測距の誤差構造を GP で吸収しつつ、anchor 位置を推定する。
* localization 時は、各 anchor からの距離に応じて候補領域を絞り、その領域内だけで STD descriptor matching を行う。
* つまり、UWB は粗い global cue、LiDAR descriptor は幾何照合、という役割分担。

## どこが強い？

* かなり広い現場スケールを意識していて、実環境での deployability が高い。
* UWB を無理に単独定位へ使わず、**LiDAR localization の前段フィルタ**として使うのがうまい。
* GP によって NLoS を含む range error を雑に捨てず、統計的に扱っている。

## 弱そうなところ

* UWB 環境依存 bias や湿度依存など、現場ごと tuning/再較正が必要そう。
* LiDAR odometry / descriptor 側が崩れると、全体もそのまま苦しくなる。
* 低コストセンサ構成へそのまま落とすには、まだ LiDAR 側の要求が高い。

## 関連研究との違い

* GPS 依存の UWB calibration より、**現場内自己較正**に寄せている。
* UWB-only localization より、LiDAR descriptor と組み合わせて使うのが特徴。
* iterative least squares 的 calibration より、GP で spatial error structure を吸う方向。

## non-AIとして見る価値

* UWB と LiDAR を learning なしで、**統計モデルと幾何照合**でうまく役割分担させている。
* 大規模現場の hybrid localization を考える上でかなり実用的。

## 難易度

★★★☆☆

## 自分の理解/感想

* 地味だけど現場ではかなり効きそうな論文。
* UWB を「全部解く主役」にせず、LiDAR sidekick として使う割り切りが良い。
