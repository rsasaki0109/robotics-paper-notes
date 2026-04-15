# Bayesian Optimal Experimental Design for Robot Kinematic Calibration

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Calibration 1 |
| arXiv | [http://arxiv.org/abs/2409.10802](http://arxiv.org/abs/2409.10802) |
| Authors | Das, Ersin;Touma, Thomas;Burdick, Joel |
| Source | ICRA 2025 / arXiv |

## TL;DR

- robot kinematic calibration で「どの姿勢を次に測ると一番うまく較正できるか」を、**Bayesian optimal experimental design** として解いている。
- SE(3) を雑に Euclidean 扱いせず、**S^3 x R^3 上の geometry-aware kernel** を使うところが技術的な芯。
- 地味だがかなり classical で、少ない計測回数で calibration を詰めたい人には刺さるタイプ。

## Task

* Calibration
* Manipulator
* Experimental Design
* Bayesian Optimization

## Keywords

* Kinematic Calibration / Gaussian Process / Experimental Design / Quaternion Geometry / DH Parameters

## AI依存度

* Non-AI

## 何を解決？

* kinematic calibration は、良い計測姿勢を少数選べるかで効率が大きく変わる。
* 既存法は候補姿勢を固定で用意したり、SE(3) の誤差構造を雑に Euclidean に押し込んだりしがちだった。
* その結果、測定回数が増えたり、姿勢誤差の扱いが幾何的に不自然になる。

## 何が新しい？

* end-effector pose 空間上で calibration 実験を設計する **Bayesian experimental design** を前面に出している点。
* 回転を quaternion / S^3 として扱い、**Riemannian Matérn kernel** を使う geometry-aware GP を組んでいる点。
* joint space ではなく task space 側で次の測定姿勢を選ぶので、encoder 誤差の影響を受けにくい設計にしている点。

## どうやってる？

* 現在の calibration 誤差を、end-effector pose 上の関数として GP で近似する。
* acquisition function に従って、次に測ると情報が増えそうな pose を選ぶ。
* 実機では vision-guided にその pose へ持っていき、観測した pose 誤差から identification Jacobian を更新し、DH parameter を補正する。
* 要するに「適当にたくさん測る」のではなく、**不確かさが一番減る姿勢を順番に打つ**設計。

## どこが強い？

* calibration を単なる最小二乗でなく、**測定設計問題**としてきちんと扱っている。
* geometry-aware kernel によって、回転を Euclidean ベクトルとして無理やり扱う違和感が減る。
* 計測回数が高価な場面では、少数ショットで収束させたい要求にかなり合う。

## 弱そうなところ

* GP の hyperparameter や acquisition の設計に依存する部分があり、完全に気楽ではない。
* 実験系としては vision-guided 計測や fiducial が必要で、アルゴリズム単体では完結しない。
* 基本は rigid / time-invariant な kinematic calibration なので、温度変化や摩耗のような長期変動までは直接扱っていない。

## 関連研究との違い

* 固定の calibration pose セットを使う方法より、**online に次の測定姿勢を選ぶ**ところが違う。
* SE(3) を平坦空間っぽく扱う GP より、回転幾何を真面目に入れている。
* joint-space ベースの較正より、task-space measurement planning という見方が鮮明。

## non-AIとして見る価値

* calibration で大事なのは「たくさん測る」より「どこを測るか」だとよく分かる。
* learning で誤差補正する方向とは違って、**幾何と実験計画で詰める classical calibration** の良い例。

## 難易度

★★★★☆

## 自分の理解/感想

* 派手さはないが、姿勢空間の幾何をちゃんと守る calibration 論文として好感が持てる。
* 惑星探査のように計測回数が貴重な場面とも相性がよく、応用先まで含めて筋が通っている。
