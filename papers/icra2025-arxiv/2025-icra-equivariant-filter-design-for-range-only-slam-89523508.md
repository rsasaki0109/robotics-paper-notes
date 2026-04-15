# Equivariant Filter Design for Range-Only SLAM

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | SLAM 3 |
| arXiv | [http://arxiv.org/abs/2503.03973](http://arxiv.org/abs/2503.03973) |
| Authors | Ge, Yixiao, Pearce, Arthur, van Goor, Pieter, Mahony, Robert |
| Source | ICRA 2025 / arXiv |

## TL;DR

- range-only SLAM に対して、距離観測と相性の良い Lie 群対称性を使った **equivariant filter** を設計した論文。
- landmark 初期化を前提にせず、no-prior 条件でも回りやすい filter を目指している。
- UWB / BLE / acoustic beacon 系の localization を、古典的だがかなり美しい形で再定式化している。

## Task

* SLAM
* Localization
* Range Sensing
* State Estimation

## Keywords

* Range-Only SLAM / Equivariant Filter / Lie Group / UWB / Beacon Localization

## AI依存度

* Non-AI

## 何を解決？

* range-only SLAM は landmark 初期化や観測の非線形性が厳しく、標準 EKF だと linearization error に苦しみやすい。
* beacon 系 localization は実用性が高い一方で、状態表現と filter 設計が難しい。

## 何が新しい？

* range-only measurement と整合する symmetry Lie group を明示し、その上で EqF を導いた点。
* landmark 初期化フェーズなしでも動けるように、state と誤差座標の持ち方を工夫した点。
* SOT(3) 系の normal coordinates を使って、ランドマーク不確かさを幾何的に扱う点。

## どうやってる？

* robot pose と landmark state を含む range-only SLAM を、多様体上の状態空間として書く。
* range measurements に対して等変性を持つ群作用を定義し、EqF の correction term を導く。
* landmark を単純な Cartesian 座標で持たず、range-only に相性の良い誤差表現を使う。
* 実験では UAV / ground robot 系データで、EKF 系との比較を行っている。

## どこが強い？

* range-only SLAM という難しい設定で、bootstrap なしを狙っているのが強い。
* UWB / BLE / acoustic beacon など応用先が広い。
* Lie 群ベースの filter 設計としてかなり一貫していて、理論的に筋が良い。

## 弱そうなところ

* 理論負荷がかなり高く、実装やデバッグの敷居は高い。
* IMU bias など実機で重要な誤差源は基本形ではまだ弱い可能性がある。
* 実験条件によっては range dropout や severe noise の影響がさらに見たい。

## 関連研究との違い

* 標準 EKF は Cartesian state で range 非線形性を受け止めるので、初期化や linearization が重い。
* polar / ROP-EKF 系は range に寄せた座標を使うが、EqF ほど幾何的に統一されていない。
* 本論文は RO-SLAM を symmetry-aware filter design の文脈に乗せたのが大きい。

## non-AIとして見る価値

* beacon localization や UWB SLAM を、state estimation の設計原理から理解できる。
* VIO/LIO と違う sensing modality でも、EqF 的発想が効くことを示していて面白い。

## 難易度

★★★★★

## 自分の理解/感想

* 数学はかなり重いが、range-only SLAM をここまできれいに書き直しているのが良い。
* すぐ実装に使うというより、sensor modality に合わせた filter design を学ぶための論文として価値が高い。
