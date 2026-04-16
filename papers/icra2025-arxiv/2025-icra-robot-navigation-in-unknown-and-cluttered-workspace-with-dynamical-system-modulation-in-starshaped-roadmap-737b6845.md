# Robot Navigation in Unknown and Cluttered Workspace with Dynamical System Modulation in Starshaped Roadmap

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Motion Planning and Control |
| arXiv | [http://arxiv.org/abs/2403.11484](http://arxiv.org/abs/2403.11484) |
| Authors | Chen, Kai;Liu, Haichao;Li, Yulin;Duan, Jianghua;Zhu, Lei;Ma, Jun |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 未知・混雑環境に対して、LiDAR 点群から **starshaped free-space roadmap** を逐次作り、DSM ベースで反応的に走る手法。
- 楕円や凸 corridor より広い自由空間を取りやすく、**未知環境でも star-shaped region を直接つくる**のが売り。
- frontier 管理と stuck 判定も入っていて、reactive control だけでは詰まりやすい場面に少し deliberative 要素を足している。

## Task

* Robot Navigation
* Unknown Environment Exploration
* Reactive Planning and Control
* LiDAR-Based Navigation

## Keywords

* Starshaped Region / Dynamical System Modulation / Frontier Point / Roadmap / Reactive Control

## AI依存度

* Non-AI

## 何を解決？

* cluttered unknown environment では、free space を保守的に切る corridor 型手法だと通れる空間を狭めすぎる。
* 一方で purely reactive な避障だけでは dead end や局所最小に弱い。
* 本論文は、**環境をその場で starshaped region として記述しつつ、reactive control と roadmap を結ぶ**ことでこの中間を狙っている。

## 何が新しい？

* LiDAR 点群から区分多項式で境界を近似し、**starshaped free-space region** をその場で構成する。
* 複数の starshaped region を roadmap 化し、frontier point を使って未知空間へ伸ばしていく。
* 実際の制御は DSM で行い、重なり領域の扱いや stuck 判定を含めてオンラインで更新する。

## どうやってる？

* センサ点群を極座標で扱い、角度方向に piecewise polynomial を当てて free-space boundary を近似する。
* その boundary から、中心点に対して star-shaped な領域を作り、局所 roadmap node とみなす。
* frontier candidate を見つけて次の node を伸ばし、goal へ向かう系列を作る。
* ロボットは DSM controller で短期目標へ向かうが、行き詰まりやすい node は捨てて別 frontier を使う。

## どこが強い？

* star-shaped 表現のおかげで、凸 corridor より **空間を無駄なく使える**。
* 完全な global planner ではないが、frontier / roadmap を足すことで reactive method の弱さをかなり補っている。
* 点群処理から制御までが軽量で、実時間動作をかなり意識している。
* 未知環境 navigation の論文として、幾何表現と controller の接続が素直。

## 弱そうなところ

* point cloud が疎だったり occlusion が強いと、starshaped fit 自体が不安定になりそう。
* 2D LiDAR ベースの話なので、3D 複雑環境や高低差つき空間へはそのままでは行きにくい。
* stuck 判定や frontier 更新は heuristic な部分もあり、難しい迷路では詰め切れていない可能性がある。

## 関連研究との違い

* convex safe corridor より、**空間形状に沿いやすい free-space representation** を使っている。
* 既存 DSM 系のように障害物形状既知前提ではなく、未知環境から online に region を作る点が違う。
* potential field のみで抜けるのでなく、roadmap 的な離散構造を少し持ち込んでいるのが特徴。

## non-AIとして見る価値

* point cloud から自由空間表現を作って、そのまま controller へ食わせる classical pipeline として非常に読みやすい。
* unknown navigation を learned policy でなく、幾何 + reactive control でどこまで押せるかが見える。
* 安全 corridor の表現設計そのものを見直すヒントになる。

## 難易度

★★★☆☆

## 自分の理解/感想

* 反応型と roadmap の中間を狙った実装で、派手ではないが実機寄りの工夫が多い。
* starshaped region を前面に出しているぶん、free-space modeling の視点で読むと面白い論文。
