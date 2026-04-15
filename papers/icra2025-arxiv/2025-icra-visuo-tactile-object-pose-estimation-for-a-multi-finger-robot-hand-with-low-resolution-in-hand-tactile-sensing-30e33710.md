# Visuo-Tactile Object Pose Estimation for a Multi-Finger Robot Hand with Low-Resolution In-Hand Tactile Sensing

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Perception for Manipulation 1 |
| arXiv | [http://arxiv.org/abs/2503.19893](http://arxiv.org/abs/2503.19893) |
| Authors | Mack, Lukas;Grüninger, Felix;Richardson, Benjamin A.;Lendway, Regine;Kuchenbecker, Katherine J.;Stueckler, Joerg |
| Source | ICRA 2025 / arXiv |

## TL;DR

- multi-finger hand の in-hand pose estimation を、**vision + binary tactile + proprioception** の factor graph で解く論文。
- tactile は高解像でなくても、**SDF residual** として幾何的に入れるだけで occlusion 下の pose tracking をかなり助ける。
- vision の初期値には FoundationPose を使っており、全体としては **Hybrid** だが、コアは古典的最適化。

## Task

* Manipulation Perception
* Pose Estimation
* Tactile Sensing
* Factor Graph Optimization

## Keywords

* Visuo-Tactile Fusion / SDF / Factor Graph / In-Hand Manipulation / FoundationPose

## AI依存度

* Hybrid

## 何を解決？

* multi-finger grasp 中は hand が object を大きく隠すため、vision-only pose estimation が崩れやすい。
* 高解像 tactile を使う方法もあるが、センサ実装が重く高価になりやすい。
* そこで、低解像・binary tactile でも **幾何制約として十分効かせられるか**を見ている。

## 何が新しい？

* low-resolution binary tactile を multi-finger hand に多数載せ、factor graph に自然に統合している点。
* tactile contact を object SDF への signed-distance residual として書く点。
* non-penetration prior も入れ、vision が見えないときに pose を geometry で支える点。

## どうやってる？

* vision 側は FoundationPose から初期 pose を得る。
* tactile pad の接触有無と hand kinematics から、pad 周辺の点が object SDF 上でどうあるべきかを residual にする。
* visual factor、tactile factor、penetration factor をまとめて factor graph で最適化する。
* LM 最適化を数回回し、occlusion 時でも pose を安定化させる。

## どこが強い？

* tactile を高解像画像化せず、**安い binary contact でも効く**ことを示したのが良い。
* factor graph で各センサの役割が明快で、解釈しやすい。
* in-hand manipulation での occlusion 問題にかなり素直に効いている。

## 弱そうなところ

* object CAD / SDF が既知である前提が強い。
* vision 初期値に学習系を使っているため、完全な non-AI とは言えない。
* リアルタイム性は十分だが、vision-only よりは当然重い。

## 関連研究との違い

* 高解像 tactile ベースより、**低解像 tactile を幾何最適化で活かす**方向。
* particle filter や learned tactile fusion より、SDF と factor graph でかなり明示的。
* 単一 modality より、occlusion 時の頑健性が明確に強い。

## non-AIとして見る価値

* Hybrid ではあるが、中核は **SE(3) 最適化・SDF・factor graph** という classical pose estimation。
* manipulation で tactile をどう geometry に変えるかの教材として面白い。

## 難易度

★★★☆☆

## 自分の理解/感想

* tactile を増やしただけでなく、「どう residual に書くか」がきれい。
* learned front-end を使いつつ、最後は幾何で詰めるバランスが実務的。
