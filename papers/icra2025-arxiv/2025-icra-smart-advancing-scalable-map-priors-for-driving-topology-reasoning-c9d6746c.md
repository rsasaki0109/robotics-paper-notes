# SMART: Advancing Scalable Map Priors for Driving Topology Reasoning

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Robot Mapping 2 |
| arXiv | [http://arxiv.org/abs/2502.04329](http://arxiv.org/abs/2502.04329) |
| Authors | Ye, Junjie;Paz, David;Zhang, Hengyuan;Guo, Yuliang;Huang, Xinyu;Christensen, Henrik Iskov;Wang, Yue;Ren, Liu |
| Source | ICRA 2025 / arXiv |

## TL;DR

- Topology reasoning is crucial for autonomous driving as it enables comprehensive understanding of connectivity and relationships between lanes and traffic elements.
- While recent approaches have shown success in perceiving driving topology using vehicle-mounted sensors, their scalability is hindered by the reliance on training data captured by consistent sensor configurations.
- We identify that the key factor in scalable lane perception and topology reasoning is the elimination of this sensor-dependent feature.

## Task

* Perception
* Software Tools

## Keywords

* Mapping
* Computer Vision for Transportation

## AI依存度

* Non-AI

## 何を解決？

* Topology reasoning is crucial for autonomous driving as it enables comprehensive understanding of connectivity and relationships between lanes and traffic elements.

## 何が新しい？

* To address this, we propose SMART, a scalable solution that leverages easily available standard-definition (SD) and satellite maps to learn a map prior model, supervised by large-scale geo-referenced high-definition (HD) maps independent of sensor settings.

## どうやってる？

* Extensive experiments further demonstrate that SMART can be seamlessly integrated into any online topology reasoning method, yielding significant improvements by up to 28% on the OpenLane-V2 benchmark.

## どこが強い？

* Extensive experiments further demonstrate that SMART can be seamlessly integrated into any online topology reasoning method, yielding significant improvements by up to 28% on the OpenLane-V2 benchmark.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* To address this, we propose SMART, a scalable solution that leverages easily available standard-definition (SD) and satellite maps to learn a map prior model, supervised by large-scale geo-referenced high-definition (HD) maps independent of sensor settings.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
