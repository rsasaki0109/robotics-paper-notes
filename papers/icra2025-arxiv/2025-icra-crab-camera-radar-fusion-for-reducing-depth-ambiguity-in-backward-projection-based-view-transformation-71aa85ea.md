# CRAB: Camera-Radar Fusion for Reducing Depth Ambiguity in Backward Projection Based View Transformation

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 6 |
| arXiv | [http://arxiv.org/abs/2509.05785](http://arxiv.org/abs/2509.05785) |
| Authors | Lee, In-Jae;Hwang, Sihwan;Kim, Youngseok;Kim, Wonjune;Kim, Sanmin;Kum, Dongsuk |
| Source | ICRA 2025 / arXiv |

## TL;DR

- camera-radar BEV perception で、backward projection の **depth ambiguity** を正面から潰しにいく論文。
- 中心は **ROSCA** と **RCSCA** の 2 モジュールで、レーダ占有とレーダコンテキストを使って BEV query の深度対応を改善する。
- nuScenes で backward projection 系の camera-radar fusion 手法としてかなり強く、悪天候や夜間も意識した評価が入っている。

## Task

* Camera-Radar Fusion
* 3D Object Detection
* BEV Perception
* Autonomous Driving Perception

## Keywords

* Backward Projection / Depth Ambiguity / ROSCA / RCSCA / nuScenes / BEV Detection

## AI依存度

* Hybrid

## 何を解決？

* camera-only の backward projection BEV は、同じ視線上の別深度点が画像上で潰れてしまい、**同一 ray 上の物体を区別しづらい**。
* その結果、遠近での false positive や depth confusion が出やすい。
* radar は距離に強いが sparse なので、単純に足すだけでは camera 側の depth ambiguity をうまく解消できない。

## 何が新しい？

* backward projection 系で見落とされがちな **same-ray depth ambiguity** を問題の中心に据えている。
* **ROSCA** で camera depth distribution と radar occupancy を組み合わせ、深度方向に意味のある attention を作る。
* **RCSCA** では radar の RCS や velocity を frustum-view の文脈特徴として扱い、BEV へ渡す。
* つまり radar を単なる sparse point 補助でなく、**深度対応を決める信号**として使っている。

## どうやってる？

* カメラ側は通常の BEV pipeline で image feature と depth-related feature を作る。
* レーダ側は frustum-view 的な形に整形し、occupancy と context feature を保持する。
* ROSCA では camera depth distribution と radar occupancy を掛け合わせて、どの depth bin を重く見るべきかを補正する。
* RCSCA ではさらに radar の反射強度や速度情報を attention に入れ、最終的な BEV feature を detection / segmentation head に渡す。

## どこが強い？

* 問題設定がかなりクリアで、「camera-radar fusion の何が本当に難しいか」を depth ambiguity に絞っている。
* backward projection 系で SOTA クラスの性能を出しており、単なる fusion の足し算ではない。
* 昼夜や雨のような条件別評価があり、レーダを使う意味が定量的に見えやすい。
* detection だけでなく segmentation にも使える BEV feature として整理しているのが良い。

## 弱そうなところ

* 計算量やレイテンシの議論が薄く、実運用でどこまで載るかはまだ見えづらい。
* radar-camera calibration のズレや radar noise にどれだけ強いかはあまり詰めていない。
* nuScenes 以外での汎化や、別レーダ設定での安定性は未確認。

## 関連研究との違い

* forward projection 系の camera-radar fusion より、**backward projection の弱点を局所的に補う**設計。
* 単なる feature-level fusion ではなく、depth distribution そのものへ radar occupancy を効かせるのが違い。
* TransCAR や他の backward projection 系に対して、「same-ray 問題を本当に解くには radar をこう使うべき」という主張が明確。

## non-AIとして見る価値

* 学習ベースではあるが、核は **センサ幾何と表現設計** にある。
* camera と radar のどこが補完関係になるのかを、depth ambiguity という形で整理しているのは IV の設計論として価値が高い。
* multi-sensor fusion を考えるとき、ただ fusion するのでなく「何の曖昧さを消すためか」をはっきりさせる重要性が見える。

## 難易度

★★★★☆

## 自分の理解/感想

* camera-radar fusion 論文としてかなり読みやすく、問題設定がきれい。
* LiDAR なしでどこまで詰められるかを考えると、こういう **depth ambiguity に絞った改善** は実際かなり効きそうだと感じる。
