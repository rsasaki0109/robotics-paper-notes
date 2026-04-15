# Equivariant IMU Preintegration with Biases: A Galilean Group Approach

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | State Estimation |
| arXiv | [http://arxiv.org/abs/2411.05548](http://arxiv.org/abs/2411.05548) |
| Authors | Delama, Giulio, Fornasier, Alessandro, Mahony, Robert, Weiss, Stephan |
| Source | ICRA 2025 / arXiv |

## TL;DR

- IMU preintegration を、bias を外付け state として扱う従来形ではなく、Galilean group の拡張空間で幾何的に定式化し直した論文。
- bias と navigation state をまとめた preintegration error を導き、線形化誤差と consistency を改善したい立場。
- EuRoC では NEES などの一貫性指標で既存 preintegration より良い結果を示しており、理論色の強い基盤論文。

## Task

* SLAM
* Localization
* Sensor Fusion
* State Estimation

## Keywords

* IMU Preintegration / Galilean Group / Equivariant Filtering / Consistency / Lie Theory

## AI依存度

* Non-AI

## 何を解決？

* 既存の IMU preintegration は bias を別空間に持つことが多く、幾何構造と linearization の噛み合いが悪くなりやすい。
* preintegration は VIO / INS の土台なので、ここにある一貫性のズレが上位推定器全体へ波及する。

## 何が新しい？

* bias と navigation state を幾何的に結合した新しい preintegration error を導いた点。
* Gal(3) の左自明化接群上で離散時間 preintegration を構成し、bias 付き INS を対称性込みで扱う点。
* closed-form の更新と Jacobian を与えて、理論だけでなく optimizer で使える形に落としている点。

## どうやってる？

* continuous-time biased INS を Galilean group に沿って書き換え、preintegrated increment を群の指数写像で更新する。
* 誤差は left-invariant な normal coordinates で表し、Adjoint 作用を使って linearization を整理する。
* bias correction を後付け近似で済ませるのでなく、preintegration そのものに組み込んでいる。
* 評価では EuRoC で consistency と estimator behavior を中心に比較している。

## どこが強い？

* preintegration を「便利な近似部品」ではなく、state geometry から組み直しているのが強い。
* 一貫性の議論が NEES まで含めて比較的明確で、理論の自己満足で終わっていない。
* Lie++ 実装公開までつながっていて、再利用可能性が高い。

## 弱そうなところ

* 数学的負荷がかなり高く、普通の VIO 実装者が追うには難しい。
* 一貫性向上がそのまま最終 ATE 改善へどれだけ効くかは、タスク依存で解釈が必要。
* closed-form は美しいが、実装複雑性と計算負荷のバランスはもう少し見たい。

## 関連研究との違い

* Forster 系の標準 preintegration は bias を別状態として補正する設計で、幾何的には分離が残る。
* SE(2,3) 系の invariant preintegration をさらに一歩進めて、bias を含む symmetry を Galilean 群で正面から扱っている。
* EqF 系の biased INS 理論を、preintegration という実用部品へ落とした位置づけ。

## non-AIとして見る価値

* VIO / INS の性能が「フロントエンド」以前に、IMU モデルの持ち方で変わることを学べる。
* preintegration をブラックボックスにせず、state estimation の設計原理として理解したい人に向いている。

## 難易度

★★★★★

## 自分の理解/感想

* かなり理論寄りだが、こういう基礎部品の改善は長い目で効く。Top 12 に入れる理由は十分ある。
* すぐ実装するには重いけれど、EqF や invariant estimation を追っているなら外せない一本。
