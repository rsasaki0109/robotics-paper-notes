# RenderWorld: World Model with Self-Supervised 3D Label

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Autonomous Vehicle Perception 3 |
| arXiv | [http://arxiv.org/abs/2409.11356](http://arxiv.org/abs/2409.11356) |
| Authors | Yan, Ziyang, Dong, Wenzhen, Shao, Yihua, Lu, Yuhang, Liu, Haiyang, Liu, Jingwen, Wang, Haozhe, Wang, Zhe, Wang, Yan, Remondino, Fabio, Ma, Yuexin |
| Source | ICRA 2025 / arXiv |

## TL;DR

- End-to-end autonomous driving with vision-only is not only more cost-effective compared to LiDAR-vision fusion but also more reliable than traditional methods.
- To achieve a economical and robust purely visual autonomous driving system, we propose RenderWorld, a vision-only end-to-end autonomous driving framework, which generates 3D occupancy labels using a self-supervised gaussian-based Img2Occ Module, then encodes the labels by AM-VAE, and use world model for forecasting and planning.
- By applying AM-VAE to encode air and non-air separately, RenderWorld achieves more fine-grained scene element representation, lead- ing to state-of-the-art performance in both 4D occupancy forecasting and motion planning from autoregressive world model.

## Task

* LiDAR
* Perception
* Sensor Fusion
* Motion Planning

## Keywords

* Computer Vision for Automation / Planning / Scheduling and Coordination / Object Detection / Segmentation and Categorization

## AI依存度

* AI-heavy

## 何を解決？

* End-to-end autonomous driving with vision-only is not only more cost-effective compared to LiDAR-vision fusion but also more reliable than traditional methods.

## 何が新しい？

* To achieve a economical and robust purely visual autonomous driving system, we propose RenderWorld, a vision-only end-to-end autonomous driving framework, which generates 3D occupancy labels using a self-supervised gaussian-based Img2Occ Module, then encodes the labels by AM-VAE, and use world model for forecasting and planning.

## どうやってる？

* To achieve a economical and robust purely visual autonomous driving system, we propose RenderWorld, a vision-only end-to-end autonomous driving framework, which generates 3D occupancy labels using a self-supervised gaussian-based Img2Occ Module, then encodes the labels by AM-VAE, and use world model for forecasting and planning.

## どこが強い？

* To achieve a economical and robust purely visual autonomous driving system, we propose RenderWorld, a vision-only end-to-end autonomous driving framework, which generates 3D occupancy labels using a self-supervised gaussian-based Img2Occ Module, then encodes the labels by AM-VAE, and use world model for forecasting and planning.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* End-to-end autonomous driving with vision-only is not only more cost-effective compared to LiDAR-vision fusion but also more reliable than traditional methods.

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: sensing / localization / perception, perception, perception / localization fusion
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
