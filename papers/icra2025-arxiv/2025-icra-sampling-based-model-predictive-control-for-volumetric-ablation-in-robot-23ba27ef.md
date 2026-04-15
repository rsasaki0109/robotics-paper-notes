# Sampling-Based Model Predictive Control for Volumetric Ablation in Robotic Laser Surgery

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Surgical Robotics: Planning |
| arXiv | [http://arxiv.org/abs/2410.03152](http://arxiv.org/abs/2410.03152) |
| Authors | Wang, Vincent, Prakash, Ravi, Oca, Siobhan, LoCicero, Ethan, Codd, Patrick, Bridgeman, Leila |
| Source | ICRA 2025 / arXiv |

## TL;DR

- robotic laser surgery の volumetric ablation を、**sampling-based MPC** で計画する論文。
- Gaussian point-ablation model を使い、角度付き・複数回照射を含む 3D resection planning をやっている。
- real surgery 直前にそのまま使うにはまだ重いが、**pre-op planning** としてはかなり筋が良い。

## Task

* Surgical Robotics
* Model Predictive Control
* Sampling-Based Planning
* Laser Ablation

## Keywords

* Volumetric Ablation / MPC / Graph Search / Gaussian Beam Model / Surgical Planning

## AI依存度

* Non-AI

## 何を解決？

* laser ablation で複雑形状の腫瘍を削るには、どこをどの角度・出力で何回照射するかを決める必要がある。
* raster 的な単純走査では形状適合が難しく、critical tissue を避ける制約も入れにくい。
* さらに tissue model の誤差があるので、**open-loop 一発計画**では危ない。

## 何が新しい？

* volumetric ablation を Gaussian beam model で近似し、sampling-based MPC に載せている点。
* angle を持つ cut と repeated cut を扱える planning formulation。
* 各 cut 後に再計画する feedback loop を入れ、不確かさに対処している点。

## どうやってる？

* 各 laser shot の ablation 量を、spot size と距離に基づく Gaussian model で表す。
* 目標 volume との差、critical region 侵害、レーザ位置・出力などをコスト化して探索木を広げる。
* weighted sampling / graph search で良さそうな ablation sequence を見つける。
* 1 回の cut ごとに tissue state を更新し、必要なら MPC 的に plan を引き直す。

## どこが強い？

* ただの path planning でなく、**切除 volume そのもの**を最適化対象にしている。
* critical anatomy を避ける制約を比較的自然に入れられる。
* uncertainty 下で feedback replan が効くことを見せており、臨床寄りの視点がある。

## 弱そうなところ

* 3D planning runtime はまだ重く、intra-op で気軽に回せる速度ではない。
* tissue parameter の不確かさや非一様性に強く依存する。
* 実機/臨床 validation はまだなく、現状は simulation ベース。

## 関連研究との違い

* raster / heuristic ablation より、**geometry-aware volumetric planning** に踏み込んでいる。
* 線形化した MPC より、sampling-based にして nonlinear tissue model を保っている。
* one-shot optimization より、feedback replan を入れて堅くしている。

## non-AIとして見る価値

* surgical planning を learned policy でなく、**物理モデル + constraint-aware planning** で解いているのが良い。
* robotics と medical treatment planning の接点としてかなり面白い。

## 難易度

★★★★☆

## 自分の理解/感想

* 応用は特殊だが、中身はかなり王道の model-based planning。
* 速度が出れば臨床的にも強そうで、今後の高速化が鍵になりそう。
