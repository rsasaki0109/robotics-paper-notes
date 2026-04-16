# Chameleon: Fast-Slow Neuro-Symbolic Lane Topology Extraction

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 1 |
| arXiv | [http://arxiv.org/abs/2503.07485](http://arxiv.org/abs/2503.07485) |
| Authors | Zhang, Zongzheng;Li, Xinrun;Zou, Sizhe;Chi, Guoxuan;Li, Siqi;Qiu, Xuchong;Wang, Guoliang;Zheng, Guantian;Wang, LeiChen;Zhao, Hang;Zhao, Hao |
| Source | ICRA 2025 / arXiv |

## TL;DR

- lane topology extraction を、**fast symbolic path と slow VLM reasoning path** に分けて解く neuro-symbolic 論文。
- 単純ケースは合成プログラムで高速に処理し、交差点などの corner case だけを **VLM + chain-of-thought** に回す。
- 全部を dense visual prompting で解くより現実的で、OpenLane-V2 で few-shot ベースでもかなり戦える構成にしている。

## Task

* Lane Topology Extraction
* Mapless Autonomous Driving Perception
* Neuro-Symbolic Reasoning
* Vision-Language Reasoning

## Keywords

* OpenLane-V2 / VLM / Program Synthesis / Chain-of-Thought / Lane-Element Relations

## AI依存度

* AI-heavy

## 何を解決？

* lane topology extraction は、lane や traffic element を検出するだけでなく、**どの lane がどこへつながるか** まで推論しないといけない。
* 完全監督学習で dense relation matrix を出す方法はデータ依存が大きく、逆に VLM へ全部投げるとクエリ数も計算コストも重い。
* 本論文は、mapless autonomous driving で必要な topology reasoning を、**VLM を使いつつも全部は使わない**形で実用寄りに組みたい、という立場。

## 何が新しい？

* simple case を処理する **fast system** と、corner case を処理する **slow system** を分離している。
* fast system では、few-shot の visual / textual prompt から **実行可能なプログラムを合成**して topology を推論する。
* slow system では、VQA 的な API 呼び出しと chain-of-thought を組み合わせて、交差点や複雑関係だけを精査する。
* つまり「VLM で全部 reasoning」ではなく、**symbolic execution と selective VLM reasoning の役割分担**が新規性。

## どうやってる？

* まず lane / traffic element detector でインスタンスを取る。
* 次に VLM へ example、API 説明、expert rule などを与えて、単純な topology 判定用の Python コードを合成させる。
* この fast symbolic program で大半の関係を処理し、曖昧なケースだけを slow path に送る。
* slow path では、left-or-right や adjacency のような小さい VQA サブタスクを chain-of-thought 的に積み上げて、最終的な lane topology relation を確定する。

## どこが強い？

* VLM を使うが、**全部を expensive reasoning にしない**ので、計算コストのバランスが良い。
* program synthesis を挟むことで、推論の中身をある程度追える。
* OpenLane-V2 で few-shot でも supervised baseline と近い性能を出しており、「VLM は使いたいが full prompting は重い」という現実的な答えになっている。
* lane topology という、普通の detection より reasoning 色の濃い IV タスクに対して、かなり素直な分解。

## 弱そうなところ

* GPT-4 系への依存が強く、VLM が変わると安定性もかなり変わりそう。
* code generation の不安定さや corner-case selector の失敗率が、実運用ではボトルネックになりうる。
* 評価は OpenLane-V2 中心で、別データや別 topology setting への汎化はまだ見えにくい。

## 関連研究との違い

* dense visual prompting に全部頼る方式より、**必要なところだけ VLM** を使う。
* 通常の supervised topology network より、明示的な rules / program / VQA decomposition を持つので reasoning 経路が見える。
* 既存の neuro-symbolic 系より、**画像文脈を踏まえた program synthesis** を前に持ってきているのが特徴。

## non-AIとして見る価値

* AI-heavy な論文だが、「どの部分を symbolic に残し、どの部分だけ foundation model に任せるか」という設計が面白い。
* lane topology をどういう小問題へ分けるかのタスク設計は、純粋に IV problem formulation として参考になる。
* VLM 活用論文の中では、かなり工学的で雑ではない。

## 難易度

★★★★☆

## 自分の理解/感想

* VLM を使った IV 論文の中では、わりと筋が良い部類で、「全部を end-to-end にしない」判断に好感が持てる。
* ただし真価は OpenLane-V2 以外でどこまで安定するかで、今はまだ面白い設計論文寄りという印象。
