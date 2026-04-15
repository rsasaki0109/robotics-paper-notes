# Robust and Accurate Multi-View 2D/3D Image Registration with Differentiable X-Ray Rendering and Dual Cross-View Constraints

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Imaging, Scanning, Localization |
| arXiv | [http://arxiv.org/abs/2506.22191](http://arxiv.org/abs/2506.22191) |
| Authors | Cui, Yuxin;Min, Zhe;Song, Rui;Li, Yibin;Meng, Max Q.-H. |
| Source | ICRA 2025 / arXiv |

## TL;DR

- preoperative CT と intraoperative X-ray を合わせる 2D/3D registration を、**multi-view 化**して安定化した論文。
- differentiable DRR rendering と cross-view consistency が核で、単一 view より registration を崩れにくくしている。
- ただし中には ResNet ベースの pose regressor も入っていて、幾何主体ではあるが **pure non-AI ではない**。

## Task

* Medical Imaging
* 2D/3D Registration
* Surgical Navigation
* Multi-View Pose Estimation

## Keywords

* DRR / X-Ray Rendering / SE(3) / Cross-View Constraint / Registration / Surgical Guidance

## AI依存度

* Hybrid

## 何を解決？

* 単一 X-ray から CT を rigid registration する 2D/3D alignment は、投影情報が少なく不安定になりやすい。
* 従来の最適化ベース手法は初期値に敏感で、単一画像だけだと local minimum に落ちやすい。
* そこで、複数 view をまとめて使って **pose consistency を強めた registration** をしたい。

## 何が新しい？

* single-view DiffPose 系を拡張し、**multi-view registration** として明示的に定式化した点。
* pose cross-loss と image cross-loss により、各 view の推定が互いに矛盾しないよう縛る点。
* SE(3) / se(3) の Lie algebra パラメータ化を使い、differentiable rendering と pose optimization をきれいにつないでいる点。

## どうやってる？

* CT から differentiable DRR renderer で各 view の合成 X-ray を作る。
* pose regressor が coarse な pose update を出し、それを multi-view loss で学習する。
* loss は各 view 個別の registration 誤差だけでなく、view 間で姿勢や画像整合が一致するよう cross-view 項も入れる。
* test 時には network 出力を初期値にして、NCC ベースの fine registration でさらに詰める。

## どこが強い？

* 2D/3D registration を multi-view consistency で補強する発想が素直で、single-view の不安定さに効いている。
* rendering physics と pose geometry がしっかりしていて、単なる black-box ではない。
* surgical navigation に直結するので、応用先がかなり明確。

## 弱そうなところ

* patient-specific な training / synthetic data 依存が強く、運用コストは軽くない。
* improvement は安定に出ているが、劇的に世界が変わるほどではない。
* 学習ベース regressor を使うため、repo の pure non-AI 軸からは少し外れる。

## 関連研究との違い

* single-view DiffPose より、**cross-view constraint** を明示的に入れている。
* landmark 対応や point-based registration より、dense image / rendering ベースで押している。
* 従来の pure iterative optimization より、coarse-to-fine で初期値問題を和らげている。

## non-AIとして見る価値

* fully non-AI ではないが、**DRR rendering / SE(3) geometry / NCC fine-tuning** など classical 要素が主役。
* medical registration で幾何拘束がどれだけ効くかを学ぶにはかなり良い。

## 難易度

★★★★☆

## 自分の理解/感想

* 中身は hybrid だが、「学習だけ」ではなく幾何とレンダリングで支えている点が面白い。
* repo の幅を広げる意味では、robotics 周辺の medical imaging を押さえる入口として価値がある。
