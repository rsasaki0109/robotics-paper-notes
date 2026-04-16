# Efficient Trajectory Generation Based on Traversable Planes in 3D Complex Architectural Spaces

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Model Predictive Control |
| arXiv | [http://arxiv.org/abs/2503.08076](http://arxiv.org/abs/2503.08076) |
| Authors | Zhang, Mengke;Tian, Zhihao;Xia, Yaoguang;Xu, Chao;Gao, Fei;Cao, Yanjun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 建築空間の floor / ramp / stairs を点群から **traversable plane graph** として抽出し、その上で ground robot の軌道を最適化する。
- 単に path をつなぐだけでなく、**斜面の速度制限や階段上の姿勢制約**を明示的に入れているのが肝。
- 平面抽出、graph search、trajectory optimization の流れがきれいで、複雑な屋内構造を classical に扱う実装論文という印象。

## Task

* Motion Planning
* Ground Robot Navigation
* Trajectory Optimization
* 3D Architectural Spaces

## Keywords

* Traversable Plane / Plane Graph / ESDF / Trajectory Optimization / Stair Traversal

## AI依存度

* Non-AI

## 何を解決？

* 一般的な ground robot planner は 2.5D map や単層の floor を前提にしがちで、階段・斜面・多層空間では扱いにくい。
* 点群ベースで直接 planning すると表現が重く、走行制約まで入れるとさらに扱いづらい。
* 本論文は、3D 建築空間を robot にとって意味のある **走行可能平面の集合**に落として、効率よく軌道生成したい、という問題設定。

## 何が新しい？

* 点群から region growing などで **走行可能平面を抽出し、交差関係つき graph** を自動構築する。
* 各平面内の局所座標系で軌道を表現し、複数平面をまたぐ軌道を 1 つの問題として扱う。
* ramp と stair に対して、単なる collision avoidance ではなく **速度・姿勢の安全制約**を陽に入れている。
* 実機で階段や複雑な屋内構造を通す評価までやっており、概念実証で終わっていない。

## どうやってる？

* LiDAR point cloud から法線推定と領域成長で平面候補を作り、統合・分類して traversable planes を得る。
* 平面の境界や隣接関係を graph にし、start / goal を最寄り平面に射影して graph search で平面列を決める。
* 軌道は各平面のローカル座標で多項式的に記述し、滑らかさや時間コストを目的関数に入れて最適化する。
* さらに、ESDF による障害物安全距離、斜面での進行方向依存の速度制限、階段での姿勢制限を加える。

## どこが強い？

* 建築空間の複雑さを、点群丸ごとではなく **robot 可走行な平面構造**に落とすので見通しが良い。
* 「階段を通れる path がある」だけでなく、実際に危険姿勢を避ける軌道最適化まで踏み込んでいる。
* 実機での stair traversal を含むので、fieldable な planner として説得力がある。
* 空間表現と軌道最適化の結びつきが自然で、拡張もしやすい。

## 弱そうなところ

* 平面近似に強く依存するので、曲面や荒れた地形では一気に扱いづらくなる。
* point cloud 品質が悪いと、平面抽出や graph 接続の時点で不安定になりそう。
* 動的障害物や大規模再計画を主眼にした手法ではなく、静的・幾何中心の設計。

## 関連研究との違い

* elevation map 系より、**多層構造をまたぐ幾何表現**が豊か。
* 通路 graph を作るだけの手法より、平面ごとの走行制約を軌道生成へきちんと渡している。
* 階段走破を機械学習で吸収する路線ではなく、**環境幾何と robot 制約を数式で入れる** classical な方向。

## non-AIとして見る価値

* センサ点群から構造を抽出し、それをそのまま optimization に食わせる流れがきれい。
* path planning と locomotion feasibility の間にあるギャップを、学習ではなく制約設計で埋めている。
* 屋内 service / inspection robot を考えるなら、かなり実務寄りの読み物。

## 難易度

★★★★☆

## 自分の理解/感想

* 建築空間を plane graph にするアイデア自体は素直だが、そこに stair / ramp の constraint を丁寧に入れているので論文として締まっている。
* 「3D 複雑環境 planning」と言っても空中ロボット向けではなく、ground robot が本当に困る場所へ焦点を当てていて実用感が強い。
