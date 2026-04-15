# No Plan but Everything under Control: Robustly Solving Sequential Tasks with Dynamically Composed Gradient Descent

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Motion Planning and Control |
| arXiv | [http://arxiv.org/abs/2503.01732](http://arxiv.org/abs/2503.01732) |
| Authors | Mengers, Vito;Brock, Oliver |
| Source | ICRA 2025 / arXiv |

## TL;DR

- We introduce a novel gradient-based approach for solving sequential tasks by dynamically adjusting the underlying myopic potential field in response to feedback and the world's regularities.
- This adjustment implicitly considers subgoals encoded in these regularities, enabling the solution of long sequential tasks, as demonstrated by solving the traditional planning domain of Blocks Worldwithout any planning.
- Unlike conventional planning methods, our feedback-driven approach adapts to uncertain and dynamic environments, as demonstrated by one hundred real-world trials involving drawer manipulation.

## Task

* Control
* Manipulation
* Perception

## Keywords

* Integrated Planning and Control
* Reactive and Sensor-Based Planning
* Optimization and Optimal Control

## AI依存度

* Non-AI

## 何を解決？

* We introduce a novel gradient-based approach for solving sequential tasks by dynamically adjusting the underlying myopic potential field in response to feedback and the world's regularities.

## 何が新しい？

* We introduce a novel gradient-based approach for solving sequential tasks by dynamically adjusting the underlying myopic potential field in response to feedback and the world's regularities.

## どうやってる？

* Unlike conventional planning methods, our feedback-driven approach adapts to uncertain and dynamic environments, as demonstrated by one hundred real-world trials involving drawer manipulation.

## どこが強い？

* These experiments highlight the robustness of our method compared to planning and show how interactive perception and error recovery naturally emerge from gradient descent without explicitly implementing them.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* We introduce a novel gradient-based approach for solving sequential tasks by dynamically adjusting the underlying myopic potential field in response to feedback and the world's regularities.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★★★（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
