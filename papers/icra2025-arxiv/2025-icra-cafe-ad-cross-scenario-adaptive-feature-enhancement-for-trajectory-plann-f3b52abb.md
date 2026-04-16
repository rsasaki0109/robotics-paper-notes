# CAFE-AD: Cross-Scenario Adaptive Feature Enhancement for Trajectory Planning in Autonomous Driving

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Navigation 1 |
| arXiv | [http://arxiv.org/abs/2504.06584](http://arxiv.org/abs/2504.06584) |
| Authors | Zhang, Junrui, Wang, Chenjie, Peng, Jie, Li, Haoyu, Ji, Jianmin, Zhang, Yu, Zhang, Yanyong |
| Source | ICRA 2025 / arXiv |

## TL;DR

- imitation learning ベースの planning が抱える **causal confusion** と **long-tail scenario bias** を、feature 操作で緩和しようとする論文。
- 提案法 **CAFE-AD** は、Adaptive Pruning Transformer と Cross-Scenario Feature Interpolation の 2 本柱で、重要でない情報を削りつつ dominant scenario への過学習を抑える。
- nuPlan Test14-Hard の closed-loop 評価で、PLUTO 系より良い R-Score を出しており、学習ベース planner の open-loop / closed-loop gap をかなり意識した設計。

## Task

* Trajectory Planning
* Imitation Learning for Autonomous Driving
* Closed-Loop Evaluation
* Scenario Generalization

## Keywords

* nuPlan / PLUTO / Adaptive Pruning / Feature Interpolation / Causal Confusion / Long-Tail Distribution

## AI依存度

* Hybrid

## 何を解決？

* imitation learning で学習した planner は、open-loop ではよく見えても closed-loop にすると壊れやすい。
* 原因の 1 つは、関係の薄い agent に注意が向く **causal confusion**、もう 1 つは停止・低速などの **dominant scenario への偏り**。
* その結果、本来進むべき場面で止まったり、重要車両を見誤ったりする。

## 何が新しい？

* Transformer encoder 内で、ego の attention を使って **重要 token だけを残す adaptive pruning** を行う。
* scenario classifier を使って feature を scenario-relevant / generic に分け、**cross-scenario interpolation** で支配的シナリオの偏りを緩める。
* つまり architecture を全部変えるのではなく、**feature selection と feature augmentation** で planner を強くしている。

## どうやってる？

* scene token を Transformer へ入れ、ego vehicle の attention score から token importance を測る。
* importance の低い token や attention を pruning して、planning に効く情報へ計算資源を寄せる。
* さらに hidden feature を scenario-relevant / generic に分解し、dominant scenario 側の relevant feature を他シナリオと混ぜることで bias を崩す。
* 学習は warm-up の後に augmentation ありフェーズへ進み、最終軌跡は baseline planner と同様に decoder / post-processing へ渡す。

## どこが強い？

* 自動運転 planner が失敗する理由を、**causal confusion** と **long-tail bias** に切り分けて処理しているのが良い。
* nuPlan の closed-loop benchmark で改善しており、open-loop metric だけで終わっていない。
* baseline を丸ごと置き換えず、既存 imitation planner に差し込みやすい設計なのも実用的。
* attention pruning と feature interpolation という、比較的わかりやすい改良で効果を出している。

## 弱そうなところ

* feature 分解や補間の設計は経験的で、なぜこの設定が最適かはまだややブラックボックス。
* 改善は baseline 依存の可能性があり、別 planner でどこまで再現するかは限定的。
* 実車側の検証はあるが、純学習 planner 単独の安全性保証までは当然遠い。

## 関連研究との違い

* 単純 dropout や token masking より、**ego-attention を使った動的 pruning** にしている。
* 通常の mix-up 系 augmentation より、scenario-aware に **relevant feature だけ** を混ぜている。
* GameFormer 系の複雑な interaction modeling と比べると、より軽量で feature engineering 寄りの改善。

## non-AIとして見る価値

* 学習ベース論文だが、planner failure を **どの特徴が悪さしているか** で整理しているのが読みやすい。
* closed-loop で効くように feature を調整する発想は、他の learned planner でもかなり応用範囲が広い。
* imitation learning planner をそのまま信じず、distribution bias をどう補正するかの視点が得られる。

## 難易度

★★★★☆

## 自分の理解/感想

* かなり実務寄りの改善で、SOTA を大きく塗り替えるというより **壊れ方を減らすための feature surgery** という印象。
* nuPlan のような benchmark を相手にすると、こういう closed-loop 重視の設計はかなり価値が高い。
