# GS-EVT: Cross-Modal Event Camera Tracking Based on Gaussian Splatting

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv/OpenAlex metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Localization 2 |
| arXiv | [http://arxiv.org/abs/2409.19228](http://arxiv.org/abs/2409.19228) |
| Authors | Liu, Tao, Yuan, Runze, Ju, Yiang, Xu, Xun, Yang, Jiaqi, Meng, Xiangting, Lagorce, Xavier, Kneip, Laurent |
| Source | ICRA 2025 / arXiv |

## TL;DR

- This paper explores the use of event cameras for motion tracking thereby providing a solution with inherent robustness under difficult dynamics and illumination.
- Reliable self-localization is a foundational skill for many intelligent mobile platforms.
- As demonstrated by our results, the realistic view rendering ability of gaussian splatting leads to stable and accurate tracking across a variety of both publicly available and newly recorded data sequences.

## Task

* SLAM
* Localization
* Mapping
* Perception

## Keywords

* Localization / SLAM / Deep Learning for Visual Perception

## AI依存度

* AI-heavy

## 何を解決？

* In order to circumvent the challenge of event camera-based mapping, the solution is framed in a cross-modal way.

## 何が新しい？

* Specifically, the proposed method operates on top of gaussian splatting, a state-of-the-art representation that permits highly efficient and realistic novel view synthesis.

## どうやってる？

* This paper explores the use of event cameras for motion tracking thereby providing a solution with inherent robustness under difficult dynamics and illumination.

## どこが強い？

* As demonstrated by our results, the realistic view rendering ability of gaussian splatting leads to stable and accurate tracking across a variety of both publicly available and newly recorded data sequences.

## 弱そうなところ

* 学習パイプライン、データ要件、推論コスト、ドメインシフト耐性は要確認。

## 関連研究との違い

* The latter is then compared against images of integrated events in a staggered coarse-to-fine optimization scheme.

## non-AIとして見る価値

* 直接の non-AI 論文ではないが、比較対象として「何を学習で置き換えているか」を把握する価値がある。

## 難易度

★★★★（abstract 初見ベース）

## Autoware視点

* 使えるか: そのまま導入するより、比較対象や将来候補として見るのが良さそう。
* どのモジュールに効くか: localization / mapping, localization, map / localization
* 実用性: 実用性はありそうだが、評価環境の詳細を本文で確認したい。

## 自分の理解/感想

* 初見では、比較対象として保持しつつ、非学習部分の設計だけでも回収したい。
