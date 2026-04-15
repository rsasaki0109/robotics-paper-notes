# GNSS/Multi-Sensor Fusion Using Continuous-Time Factor Graph Optimization for Robust Localization

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Localization 1 |
| arXiv | [http://arxiv.org/abs/2309.11134](http://arxiv.org/abs/2309.11134) |
| Authors | Zhang, Haoming, Chen, Chih-Chun, Vallery, Heike, Barfoot, Timothy |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 都市峡谷やトンネルで GNSS が壊れても動くように、連続時間の因子グラフで GNSS・IMU・速度・LiDAR odometry をまとめて融合する `gnssFGO` を提案している。
- Gaussian process による連続時間軌跡表現を使うので、非同期センサを無理に同期させず、任意時刻の状態を補間して因子を張れる。
- Aachen の 17 km シーケンスでは、tight coupling で平均 2D 誤差 0.48 m を出しており、GNSS 劣化区間で LiDAR 中心の従来法よりかなり粘る。

## Task

* Localization
* GNSS Fusion
* LiDAR
* Sensor Fusion

## Keywords

* Continuous-Time FGO / Gaussian Process / Tight Coupling / GNSS Pseudorange / Doppler

## AI依存度

* Non-AI

## 何を解決？

* 都市環境では GNSS が multipath や NLOS で壊れやすく、LiDAR 側もトンネルや退化区間で外すので、単一センサ主導の localization だと破綻しやすい。
* 既存の factor graph 系も「主センサの時刻に他センサを合わせる」設計が多く、非同期観測をそのまま活かしにくい。

## 何が新しい？

* センサ周波数に依存しない **time-centric** な因子グラフ構築にして、推定時刻を任意に選べるようにした点。
* Gaussian process で連続時間軌跡を表し、補間状態に対して GNSS / IMU / speed / LiDAR odometry の因子を張れる点。
* loose coupling と tight coupling の両方を同じ枠組みで実装し、raw GNSS 観測まで graph に直接入れられる点。

## どうやってる？

* 軌跡は GP prior 付きの連続時間状態列として表現し、測定時刻に厳密な state がなくても補間して残差評価する。
* motion prior は WNOA / WNOJ smoother を比較し、特に WNOJ を含めて補間精度と滑らかさを検討している。
* loose coupling では GNSS 解を因子に使い、tight coupling では pseudorange / Doppler をそのまま因子化する。
* 外れ値や GNSS 劣化には頑健誤差と multi-sensor smoothing を組み合わせ、LiDAR map の破綻も含めて全体で吸収する構成。

## どこが強い？

* 非同期センサ融合をかなり自然に扱えていて、実ロボットの現実的な timestamp ずれ・周波数差に強い。
* GNSS が壊れる区間で、LiDAR-centric な従来手法が scan registration 由来で崩れるケースにも粘れる。
* framework 自体が modular なので、他のセンサ追加やロボットへの横展開をしやすい。

## 弱そうなところ

* GP smoother 系なので、EKF 系より計算資源と実装の重さが出そう。online といってもレイテンシ管理は要注意。
* GP hyperparameter や robust cost の設計に依存する部分があり、環境をまたいだチューニング負荷は残りそう。
* tight coupling の恩恵は大きいが、raw GNSS 観測品質や受信機モデルへの依存も増える。

## 関連研究との違い

* 従来の multi-sensor FGO は primary sensor 主導で graph を伸ばすものが多く、非同期観測を合わせる都合で情報を捨てがちだった。
* LiDAR-centric SLAM + GNSS の後付け融合より、GNSS 生観測まで含めた統一 graph のほうが劣化区間で一貫した設計になっている。
* 以前の著者らの offline smoother 仕事より、今回は online multi-sensor localization に寄せている。

## non-AIとして見る価値

* localization を「どのセンサを何時刻の状態に結び付けるか」という因子設計の問題として学べる。
* continuous-time trajectory と GNSS tight coupling の両方を一緒に追えるので、Autoware 周辺の localization 設計にもかなり近い。

## 難易度

★★★★☆

## 自分の理解/感想

* GNSS + LiDAR の論文の中でも、単に精度が良いだけでなく「非同期センサをどう graph に入れるか」が主題になっていて学びやすい。
* 実運用では計算量とチューニングが気になるが、GNSS 劣化区間での粘り方を設計レベルで見たいならかなり読む価値が高い。
