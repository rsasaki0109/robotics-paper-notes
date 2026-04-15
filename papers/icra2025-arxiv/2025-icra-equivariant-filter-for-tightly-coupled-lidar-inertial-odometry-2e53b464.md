# Equivariant Filter for Tightly Coupled LiDAR-Inertial Odometry

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Localization 1 |
| arXiv | [http://arxiv.org/abs/2409.06948](http://arxiv.org/abs/2409.06948) |
| Authors | Tao, Anbo, Luo, Yarong, Xia, Chunxi, Guo, Chi, Li, Xingxing |
| Source | ICRA 2025 / arXiv |

## TL;DR

- EKF 系 LIO の弱点である線形化誤差と不整合を減らすために、equivariant filter を使った tightly coupled LIO `Eq-LIO` を提案している。
- IMU bias と LiDAR extrinsic まで含めた半直積群の対称性を使い、常に固定された原点で線形化することで一貫性を改善する設計。
- 公開・私有データセットのベンチマークでは、計算コストを大きく増やさずに精度・堅牢性・consistency の改善を狙っている。

## Task

* SLAM
* Localization
* LiDAR
* State Estimation

## Keywords

* LIO / Equivariant Filter / IMU Bias / Extrinsic Calibration / Consistency

## AI依存度

* Non-AI

## 何を解決？

* EKF ベースの LIO は非線形性が強い場面で線形化誤差が大きく、covariance が過信気味になる不整合が出やすい。
* IEKF は改善策だが、IMU bias を別空間に置くと群アファイン性が壊れ、理論的なきれいさと実用性にズレが残る。

## 何が新しい？

* EqF を LIO に持ち込み、navigation state・IMU bias・LiDAR extrinsic を半直積群の対称性でまとめて扱った点。
* 重力を S2 多様体上で扱い、state representation 自体を幾何的に整理した点。
* 「固定原点で線形化する error dynamics」を使って、unexpected state change 時の挙動まで改善しようとしている点。

## どうやってる？

* state は navigation pose / velocity / position に加え、gyro・acc bias と LiDAR extrinsic を含む多様体上で定義する。
* LiDAR 側は scan-to-map matching で観測モデルを作り、IMU propagation と EqF update で tightly coupled に推定する。
* bias や extrinsic を別パラメータとして後付け補正するのでなく、対称性の中に埋め込んで誤差方程式を導いている。
* 論文全体は Lie theory と manifold の準備をかなり丁寧に置いていて、理論先行で組み立てた LIO という印象。

## どこが強い？

* 「なぜ一貫性が良くなるのか」の説明が、経験則ではなく群論ベースで通っている。
* IMU bias と extrinsic を含めた self-calibration まで一つの推定器で見ているのが強い。
* filter 系の軽さを保ちつつ、optimization 系に寄せた幾何的な設計を入れているのが面白い。

## 弱そうなところ

* 理論と実装の距離がかなりあり、実務で素早く組み込むには敷居が高い。
* scan matching が崩れたときの復帰性や極端な退化環境での耐性は、式の美しさだけでは保証し切れない。
* EqF のチューニング・初期化・デバッグは通常の EKF より確実に重そう。

## 関連研究との違い

* 標準 EKF は state 依存の線形化点を追い掛けるので不整合が出やすいが、EqF は固定点 linearization を保ちやすい。
* IEKF 系は群構造を使うものの、bias を外に出すと理論的な対称性が崩れる。Eq-LIO はそこを正面から解いている。
* optimization-based LIO と比べると、filter の実時間性を維持しつつ幾何学的整合性を高めたい立場にある。

## non-AIとして見る価値

* LiDAR-IMU 融合を「どの群で state を持つか」というレベルまで掘って考えられる論文。
* preintegration や IEKF の次の一段として、state estimation の設計原理を学ぶ教材になる。

## 難易度

★★★★★

## 自分の理解/感想

* かなり理論寄りだが、LIO の精度改善を数値テクニックではなく state の持ち方から攻めているのが良い。
* 実装コストは高そうなので、すぐ使うというより「推定器をどう設計すべきか」の視点を得るために読む一本だと思う。
