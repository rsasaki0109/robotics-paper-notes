# DynORecon: Dynamic Object Reconstruction for Navigation

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Robot Mapping 2 |
| arXiv | [http://arxiv.org/abs/2409.19928](http://arxiv.org/abs/2409.19928) |
| Authors | Wang, Yiduo;Morris, Jesse;Wu, Lan;Vidal-Calleja, Teresa A.;Ila, Viorela |
| Source | ICRA 2025 / arXiv |

## TL;DR

- moving object を navigation 向けに扱うため、**object-centric submap** で動的物体を体固定座標系に再構成する論文。
- occupied だけでなく free space も明示的に持つ ESDF ベースで、**動的物体の形と通れる空間**を両方扱っている。
- Dynamic SLAM の object motion estimate を前提にした設計なので、dense dynamic mapping をかなり実務寄りに組んでいる。

## Task

* Dynamic Mapping
* Reconstruction
* Navigation
* SLAM

## Keywords

* ESDF / Object Submaps / Dynamic SLAM / Free-Space Mapping / Rigid Motion

## AI依存度

* Non-AI

## 何を解決？

* static-world 前提の dense mapping では、動く物体が通った履歴が map に残って navigation を邪魔しやすい。
* 一方、動的物体を単なる point cluster として捨てるだけでは、実際の形状や占有を十分使えない。
* そこで、dynamic object を **再構成しつつ free space も壊さない map** を作りたい。

## 何が新しい？

* 各 dynamic object に **object-centric ESDF submap** を持たせ、物体座標系で再構成する点。
* occupied voxel は object submap に、free voxel は static map に入れる分離設計。
* motion estimate に基づいて submap を時刻間で運ぶことで、毎回 map を作り直さずに済ませる点。

## どうやってる？

* Dynamic SLAM から object ごとの SE(3) motion とラベル付き点群を受け取る。
* static 部分は world frame の ESDF に積み、dynamic object はそれぞれの local frame に変換して submap へ積む。
* object pose を時刻ごとに伝播させることで、物体が動いても local submap 自体は安定して使える。
* query 時には static map と relevant object submap をまとめて見て、距離場を返す。

## どこが強い？

* dynamic scene で **形状再構成と navigation 用 free-space** を両立しているのが強い。
* object-centric submap の発想がきれいで、moving object の voxel 再配置地獄を避けている。
* outdoor っぽい大規模シーンでも回る速度感を出している。

## 弱そうなところ

* rigid object 前提なので、人や柔らかい物体にはそのまま乗りにくい。
* upstream の Dynamic SLAM が崩れると、submap 側もそのまま壊れる。
* object 数が増えると query / 管理が重くなりやすい。

## 関連研究との違い

* Dynablox のように free-space 主体の方法より、**dynamic object 自体の volumetric reconstruction** も持つ。
* object TSDF / surfel 系より、navigation 向けに ESDF と free-space を前に出している。
* non-rigid warp field 系より、rigid-body assumption のぶん実用的で軽い。

## non-AIとして見る価値

* dynamic environment を学習で吸収せず、**SE(3) motion + ESDF + submap** で整理しているのが良い。
* navigation map をどう dynamic object と両立させるかの設計としてかなり参考になる。

## 難易度

★★★☆☆

## 自分の理解/感想

* 大発明というより、dynamic mapping のつらいところにかなりまっすぐ答えた論文。
* free space をきちんと意識しているので、「reconstruction for pretty meshes」ではなく navigation 寄りなのが好み。
