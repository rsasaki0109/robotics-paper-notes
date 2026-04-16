# Curb Your Attention: Causal Attention Gating for Robust Trajectory Prediction in Autonomous Driving

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Tracking and Prediction 1 |
| arXiv | [http://arxiv.org/abs/2410.07191](http://arxiv.org/abs/2410.07191) |
| Authors | Ahmadi, Ehsan, Mercurius, Ray Coden, Mohamad Alizadeh Shabestary, Soheil, Rezaee, Kasra, Rasouli, Amir |
| Source | ICRA 2025 / arXiv |

## TL;DR

- trajectory prediction が **非因果的エージェントへの注意**に引きずられて壊れる、という問題を正面から扱う論文。
- 提案する **CRiTIC** は causal discovery network で agent 間因果関係を推定し、Transformer の attention を **Causal Attention Gating** で制約する。
- Waymo 系評価と cross-domain 実験で、通常精度を大きく落とさずに robustness と generalization をかなり改善している。

## Task

* Multi-Agent Trajectory Prediction
* Autonomous Driving Forecasting
* Causal Representation Learning
* Robust Prediction under Distribution Shift

## Keywords

* Causal Discovery Network / Causal Attention Gating / Granger Causality / Waymo / Domain Generalization

## AI依存度

* AI-heavy

## 何を解決？

* 既存の trajectory predictor は、未来軌跡を当てても **本当に効いている相手** と **たまたま相関しているだけの相手** を区別しない。
* そのため、非因果な agent を消したり挙動を少し変えたりすると、予測が大きく崩れる。
* 自動運転では planning 前段の prediction がこういう spurious relation に依存すると危険なので、因果関係を明示的に入れたい。

## 何が新しい？

* **causal discovery network (CDN)** を入れて、過去軌跡から agent 間の causal graph を推定している。
* その graph を Transformer backbone に渡し、**Causal Attention Gating (CAG)** で因果 agent への注意を通し、非因果側にはノイズを入れる。
* さらに、CDN 側に DAE 的な補助タスクと sparsity regularization を入れ、graph を疎で解釈しやすい形に寄せている。

## どうやってる？

* まず AgentNet で各 agent の過去軌跡や map context を埋め込み表現へ変える。
* CDN は MPNN ベースで agent 間エッジを推定し、BinConcrete 的な連続緩和を介して学習可能な causal adjacency を作る。
* その adjacency を prediction backbone 側へ渡し、self-attention の重みを causal edge 上で強め、non-causal edge 側は抑制する。
* 学習時には causal graph の復元を助ける補助損失も入れ、最終的な trajectory prediction と一緒に end-to-end で最適化する。

## どこが強い？

* 「prediction が何を見ているか」を causal graph として切り出せるので、**ロバスト性の理由を説明しやすい**。
* RemoveNoncausal 的な摂動でかなり強く、分布シフト下での generalization 改善もきちんと出している。
* 予測精度だけでなく、**壊れにくさ** をメトリクスに入れているのが IV らしい。
* causality を latent に閉じず、明示 graph と gating に落としているのが設計として良い。

## 弱そうなところ

* map や signal の因果関係までは本格的に扱っておらず、agent-agent 関係にかなり寄っている。
* Granger 的な因果発見なので、未観測交絡や真の因果保証までは難しい。
* hyperparameter や graph sparsity の調整が効きそうで、実装の安定化には手間がかかりそう。

## 関連研究との違い

* 普通の Transformer predictor より、**どの相手を見てよいか** を explicit causal graph で制御する。
* latent causal representation 系より、object-centric graph なので解釈しやすい。
* data augmentation や heuristic robustification より、「そもそも non-causal relation を見ない」方向で根本対応しているのが違い。

## non-AIとして見る価値

* AI-heavy だが、課題設定はかなり本質的で、「prediction stack の何が危ないか」をうまく言語化している。
* 明示 graph にして attention を制御する発想は、学習系の中でも比較的エンジニアリングしやすい。
* 自動運転で explanation / safety case を意識するなら、こういう causal framing は重要。

## 難易度

★★★★☆

## 自分の理解/感想

* trajectory prediction 論文としてかなり筋が良くて、単なる精度競争より一歩深い。
* ただし「因果」と言っても統計的近似の域は出ないので、過信せず **robustness-oriented design** として読むのがよさそう。
