# Semantic and Feature Guided Uncertainty Quantification of Visual Localization for Autonomous Vehicles

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Localization 4 |
| arXiv | [http://arxiv.org/abs/2506.15851](http://arxiv.org/abs/2506.15851) |
| Authors | Wu, Qiyuan;Campbell, Mark |
| Source | ICRA 2025 / arXiv |

## TL;DR

- visual localization の推定値そのものより、**その測定誤差分布を学習して Bayesian filter に渡す**ことを主題にした論文。
- keypoint / matching score / semantic class を入力にして、各フレームごとの **2D error distribution** を KSE-Net で予測する。
- 単一 Gaussian でなく **Gaussian mixture** を使うことで、夜間や雪で出やすい長い裾の誤差を吸収し、Ithaca365 で gating と localization を安定化している。

## Task

* Visual Localization
* Uncertainty Quantification
* Bayesian Filtering
* Autonomous Driving Localization

## Keywords

* Gaussian Mixture Model / KSE-Net / Sensor Error Model / Gating / Ithaca365

## AI依存度

* Hybrid

## 何を解決？

* 自動運転の visual localization は、推定位置が出ても **その信頼度をどれだけ正しく見積もれるか** が安全側の挙動に直結する。
* 既存の sensor error model は run ごとに固定の分布を置くことが多く、夜間・雪・見え方の変化で誤差分布が歪むと gating が壊れやすい。
* 本論文は、画像ペアごとに誤差分布を出して、Bayesian localization filter 側で使える uncertainty model を作りたい、という問題設定。

## 何が新しい？

* localization result の後段に、**フレーム単位の uncertainty predictor** を外付けしている。
* keypoint の位置や matching score に加え、**semantic information を一緒に使う**ことで、どの対応が危ないかをより細かく見ている。
* さらに誤差分布を単一 Gaussian でなく **Gaussian mixture (K=3)** で表現し、悪条件下の非ガウス的な tail を扱っている。
* mixture に対応した gating を組んで、SPF / GSF の両方で localization へ統合している。

## どうやってる？

* ベースの localization pipeline は NetVLAD + SuperPoint / SuperGlue 系で query-reference 対応を作る。
* 各マッチについて、query / reference の keypoint 座標、matching score、semantic class を並べた入力行列を作り、**KSE-Net** に入れる。
* KSE-Net は各フレームの誤差分布パラメータを出力し、最終的に 2D の Gaussian mixture measurement model を構成する。
* その分布を Bayesian filter に食わせ、通常のカイ二乗ゲートや mixture-aware gating で measurement update の採否と重みづけを決める。

## どこが強い？

* 不確実性を「あとで calibration する」のではなく、**localization module の出力条件に応じて変える**点が実務的。
* 晴天だけでなく夜間・雪まで含む Ithaca365 で見ていて、単純な固定分布より悪条件での改善幅が大きい。
* localization network 本体を作り変えずに、measurement model 側を賢くする設計なので既存系へ差し込みやすい。
* 自動運転らしく、精度向上そのものより **危ない測定をどれだけ正しく弾けるか** に重心がある。

## 弱そうなところ

* 評価は Ithaca365 中心で、都市やセンサ条件が変わったときの外挿性能はまだわからない。
* semantic segmentation の質に依存するので、そこで崩れると uncertainty model 側にも影響が出る。
* K や gating threshold の感度、推論時間など、実運用で気になる設計パラメータの詰めはやや薄い。

## 関連研究との違い

* 単純な Bayesian NN 的 uncertainty estimation より、**visual localization の measurement model** へ直接つなぐ作り。
* run 単位の固定誤差モデルより、**frame-conditioned sensor error model** にしているのが本質的な差。
* localization network を end-to-end に作り直す路線ではなく、古典的 filter の前に learned uncertainty block を挟む折衷案。

## non-AIとして見る価値

* 学習は使っているが、主眼は「deep output をどう filter に接続するか」という **system integration** にある。
* uncertainty を mixture で持って gating に落とす発想は、他の learned sensor module を classic estimator に入れるときにも応用しやすい。
* 自動運転で learned perception を使うなら、こういう downstream-safe な設計はかなり重要。

## 難易度

★★★★☆

## 自分の理解/感想

* かなり良い折衷案で、network を増やして accuracy を盛るというより、**filter が壊れにくい learned localization** を作ろうとしているのが好印象。
* 自動運転文脈では「当たるか」より「どれだけ危ない外れ方をするか」が大事なので、その意味でかなり IV らしい論文だと思う。
