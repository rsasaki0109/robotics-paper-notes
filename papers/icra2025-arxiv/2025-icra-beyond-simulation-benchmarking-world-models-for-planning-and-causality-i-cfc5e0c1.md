# Beyond Simulation: Benchmarking World Models for Planning and Causality in Autonomous Driving

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Navigation 1 |
| arXiv | [http://arxiv.org/abs/2508.01922](http://arxiv.org/abs/2508.01922) |
| Authors | Schofield, Hunter, Elmahgiubi, Mohammed, Rezaee, Kasra, Shan, Jinjun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- learned world model を「traffic prediction 精度」でなく、**planning の訓練環境として本当に使えるか** で評価し直す論文。
- WOSAC 的な標準評価だけでは見えない問題として、ego を replay 固定した partial-control 条件での性能崩れを測る **新しい評価指標** を提案している。
- さらに **Control Dropout** を導入し、autoregressive world model が uncontrollable object に過敏になる問題を和らげている。

## Task

* World Model Evaluation
* Autonomous Driving Simulation
* Planning-Oriented Benchmarking
* Causality-Aware Traffic Modeling

## Keywords

* WOSAC / WOMD / Partial Control / Control Dropout / Learned Simulator / Causal Agents

## AI依存度

* Hybrid

## 何を解決？

* 最近の world model は learned traffic simulator として使われ始めているが、標準ベンチで高スコアでも **policy training environment として健全か** は別問題。
* 特に ego や一部 agent が外部 policy で制御される partial-control 条件では、モデルが uncontrollable object に引きずられて挙動を崩しやすい。
* 本論文は、「良い simulator」に見えても planning 用には危ない world model を見抜く評価軸が必要、という問題意識。

## 何が新しい？

* ego replay あり / なしを比較する **ΔM, ΔMsim** 系のメトリクスを作り、partial-control 感度を測る。
* さらに、シミュレータ側の混乱と policy 側の混乱を分けてみる **confusion rate** を導入している。
* 訓練面では、一定確率で agent を ground-truth control に置き換える **Control Dropout** で、world model を partial-control に慣らしている。

## どうやってる？

* Waymo Open Motion Dataset / WOSAC 系 world model を対象に、通常 rollout と ego replay 固定 rollout の両方を回す。
* その差分から、標準評価では見えない「ego を自分で決められないときの崩れ」を計算する。
* さらに causal agent subset を含めた拡張評価域を使って、真に planning に効く相手への感度を見る。
* Control Dropout では、autoregressive rollout 中の一部 agent を GT policy で置き換え、partial replay に近い条件で学習する。

## どこが強い？

* world model を prediction benchmark から切り離し、**planner の学習環境として再評価する**観点が非常に良い。
* 指標設計が実務的で、simulator failure と policy failure を分けて見ようとしている。
* Control Dropout は単純だが効いていて、既存 autoregressive world model の弱点をかなりうまく突いている。
* learned simulator を本気で使いたい人には、かなり重要な benchmark 論文。

## 弱そうなところ

* 新メトリクスの閾値や causal set 定義には、ある程度恣意性がある。
* 実際にその world model 上で policy を学習したとき、どこまで下流性能に相関するかはまだ間接的。
* 評価と 2 パス rollout が増えるので、計算コストや運用負荷は小さくない。

## 関連研究との違い

* WOSAC のような標準 benchmark は **full-control に近い評価**が中心で、本論文は partial-control へ踏み込んでいる。
* 通常の motion forecasting benchmark と違い、目的が prediction 精度ではなく **simulator suitability**。
* 改善案も world model architecture の大型化ではなく、訓練条件と評価指標の見直しにある。

## non-AIとして見る価値

* 学習ベースの論文だが、価値の中心は **benchmark design** と **evaluation methodology** にある。
* 「何を良い simulator と呼ぶべきか」を問い直しており、これは AI 以外の simulation / control 研究にも通じる。
* learned world model を使う前に、どう壊れるかを見抜く指標を用意すべき、という教訓が強い。

## 難易度

★★★☆☆

## 自分の理解/感想

* かなり好きなタイプの評価論文で、world model の hype に対してちゃんとブレーキをかけている。
* architecture 提案より地味だが、IV ではこういう **何を測るべきか** を定義する論文の価値が大きい。
