# H3O: Hyper-Efficient 3D Occupancy Prediction with Heterogeneous Supervision

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 2 |
| arXiv | [http://arxiv.org/abs/2503.04059](http://arxiv.org/abs/2503.04059) |
| Authors | Shi, Yunxiao;Cai, Hong;Ansari, Amin;Porikli, Fatih |
| Source | ICRA 2025 / arXiv |

## TL;DR

- 3D occupancy prediction を、**cross-attention を減らした軽量 view transformation** と heterogeneous supervision で効率化した論文。
- camera feature を 3D grid へ投影して平均化するかなり素朴な構成だが、深度・セマンティック・法線の **2D teacher** を volume rendering で入れることで精度を戻している。
- Occ3D-nuScenes / SemanticKITTI で、計算量をかなり落としつつ occupancy 精度を維持・改善する、という方向性が明快。

## Task

* 3D Occupancy Prediction
* Autonomous Driving Perception
* Multi-Camera Scene Understanding
* Efficient 3D Representation Learning

## Keywords

* Occupancy Grid / Volume Rendering / Heterogeneous Supervision / Occ3D-nuScenes / SemanticKITTI

## AI依存度

* Hybrid

## 何を解決？

* 3D occupancy は planning に使いやすい表現だが、既存法は 2D-3D cross-attention や heavy 3D processing でかなり重い。
* さらに LiDAR 由来の 3D occupancy label だけでは supervision が粗く、遠距離や遮蔽で曖昧さが残る。
* 本論文は、**occupancy を実用速度に近づけつつ精度も落としすぎない**ことを狙っている。

## 何が新しい？

* 画像特徴から 3D voxel feature を作る段で、重い attention ではなく **projection + bilinear sampling + averaging** を使っている。
* その単純化で失う情報を、深度・セマンティック・表面法線という **heterogeneous 2D supervision** で補っている。
* この 2D supervision は differentiable volume rendering を通して occupancy volume に戻す設計になっている。
* 要するに「network を重くして勝つ」のではなく、**architecture は軽く、teacher は賢く** の方向。

## どうやってる？

* multi-camera image から 2D backbone feature を取り、各 3D grid point を各カメラへ投影して特徴をサンプルする。
* 複数カメラの対応特徴は単純平均して 3D volume を作り、そこから 3D occupancy / semantics を予測する。
* 学習時には ray casting 的に volume rendering を行い、各画素方向の深度・semantic・normal を再投影して 2D teacher と合わせる。
* これにより、3D occupancy label だけでは弱い supervision を補強する。

## どこが強い？

* メッセージが明快で、**効率と精度のトレードオフ改善**に集中している。
* heavy transformer 系よりかなり軽く、occupancy prediction の deployability を意識しているのが良い。
* 2D teacher を複数使う設計が自然で、3D GT 不足を補う実装パターンとして参考になる。
* Occ3D-nuScenes だけでなく SemanticKITTI でも見ていて、camera-centric occupancy の広がりを押さえやすい。

## 弱そうなところ

* 中身はかなり learning-heavy で、teacher の質や backbone に依存する。
* 時系列情報はあまり使わず単時刻寄りなので、動的シーンへの強さは別問題。
* occupancy の絶対精度は still hard で、特に難クラスや遠距離では限界が残る。

## 関連研究との違い

* BEVFormer / TPVFormer 系より、**view transformation をかなり軽く**している。
* RenderOcc 系と比べると、volume rendering を auxiliary supervision に使うが、構造はもっとシンプル。
* self-supervised occupancy より、複数種の teacher を整理して強い supervised signal にしている点が特徴。

## non-AIとして見る価値

* AI 依存は強いが、「どこを重くし、どこを教師信号で補うか」という **system design** が非常にわかりやすい。
* 3D task を全部大型 attention に寄せず、投影幾何と rendering supervision で詰める発想は他の perception stack にも効く。
* occupancy を下流 planning 向け表現としてどう育てるか、という論点整理にもなる。

## 難易度

★★★★☆

## 自分の理解/感想

* 派手な新モジュールより、**軽くして教師を増やす**方向で勝っているのが実務寄りで面白い。
* occupancy 系は重くなりがちなので、この論文は「何を削ってもまだ戦えるか」を考える材料としてかなり良い。
