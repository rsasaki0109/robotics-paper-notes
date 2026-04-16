# No Plan but Everything under Control: Robustly Solving Sequential Tasks with Dynamically Composed Gradient Descent

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Motion Planning and Control |
| arXiv | [http://arxiv.org/abs/2503.01732](http://arxiv.org/abs/2503.01732) |
| Authors | Mengers, Vito;Brock, Oliver |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 明示的 planner を立てず、**dynamically composed gradient descent** で sequential task を解こうとする論文。
- AICON 的な相互接続された推定器群を使い、world regularity と現在の不確実性から **その場で有効な勾配経路**を選ぶ。
- Blocks World と drawer manipulation を例に、planning なしでもかなり robust に多段タスクを回せる、と主張している。

## Task

* Sequential Task Solving
* Reactive Manipulation
* Gradient-Based Control
* Uncertainty-Aware Decision Making

## Keywords

* Dynamically Composed Gradient Descent / AICON / EKF / Sequential Tasks / Reactive Control

## AI依存度

* Non-AI

## 何を解決？

* 長い sequential task は通常 planning に寄るが、不確実性や外乱があると先読みがすぐ壊れる。
* 単純な potential field / gradient descent は reactive だが、普通は多段の subgoal をうまく扱えない。
* 本論文は、**今この瞬間に意味のある勾配を動的に構成**すれば、計画なしでもかなり先まで仕事を進められるのでは、という問題意識。

## 何が新しい？

* 単一の固定ポテンシャルではなく、複数の勾配候補を world state と interconnection から動的に構成する点。
* AICON の枠組みを perception だけでなく **action selection** へ広げている。
* symbolic planning の代表例である Blocks World を、planning ではなく gradient composition で解く見せ方が象徴的。

## どうやってる？

* タスクを構成する状態量や関係を、それぞれ推定器・相互接続として表す。
* 各推定器は観測と他推定器からの情報で状態を更新し、不確実性も追う。
* その時点で有効な勾配経路の集合を作り、最も強く task progress を生む方向を選んで制御へ使う。
* drawer task では、見失ったら見直し、把持が怪しければ確認し直す、といった **epistemic action** が明示計画なしに出てくる。

## どこが強い？

* planning と reactive control の二者択一ではなく、その中間をかなり本気で掘っている。
* 不確実性が増えると自然に情報取得行動が出る、という説明がわかりやすい。
* Blocks World のような象徴タスクと、実ロボ manipulation の両方を見せているのでメッセージ性が強い。
* ニューラル policy に頼らず、挙動の理由をかなり追いやすい。

## 弱そうなところ

* 勾配候補や interconnection の設計は手作業寄りで、タスクが変わると人手がかかる。
* competing goals があると、global optimal な順序を選ぶ保証はなく、不可逆タスクでは限界が見えやすい。
* 「planner 不要」と言い切るには、設計側でかなり task structure を入れている印象もある。

## 関連研究との違い

* classical planner のように長期離散計画を明示しない。
* standard potential field のように固定ポテンシャルへ全部押し込まず、**状態依存で勾配を組み替える**。
* learned policy と違って、状態推定・相互接続・勾配がどこで効いたかを比較的説明しやすい。

## non-AIとして見る価値

* non-learning で sequential behavior をどこまで作れるか、という意味でかなり面白い。
* planning を諦めて reactive に落とすのではなく、task structure を gradient composition へ埋め込む発想が新鮮。
* manipulation の robustification を考えるとき、policy 学習以外の選択肢として覚えておきたい。

## 難易度

★★★★☆

## 自分の理解/感想

* 主張はやや挑発的だが、単なる「planner は要らない」ではなく、reactive system をどう賢く見せるかの設計が丁寧。
* 汎用自動化というより、設計者が task structure を与えたうえで強い reactive system を作る論文として読むと納得しやすい。
