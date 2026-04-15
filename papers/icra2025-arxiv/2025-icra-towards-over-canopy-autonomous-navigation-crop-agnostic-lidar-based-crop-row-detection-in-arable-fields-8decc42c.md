# Towards Over-Canopy Autonomous Navigation: Crop-Agnostic LiDAR-Based Crop-Row Detection in Arable Fields

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Agricultural Automation 4 |
| arXiv | [http://arxiv.org/abs/2403.17774](http://arxiv.org/abs/2403.17774) |
| Authors | Liu, Ruiji;Yandun, Francisco;Kantor, George |
| Source | ICRA 2025 / arXiv |

## TL;DR

- crop row detection を **over-canopy LiDAR** でやり、RTK-GPS なしでも field navigation できるようにしている。
- ground filtering + K-means + RANSAC というかなり classical な構成で、**crop-agnostic** に row を抜くのがポイント。
- detection だけで終わらず、nonlinear MPC による row following と lane switching まで入れた実システム論文。

## Task

* Agricultural Robotics
* Navigation
* LiDAR Perception
* Model Predictive Control

## Keywords

* Crop Row Detection / Over-Canopy / K-Means / RANSAC / EKF / MPC

## AI依存度

* Non-AI

## 何を解決？

* 農業ロボットは RTK-GPS に強く依存しがちだが、環境やコストの制約で使いにくいことがある。
* vision ベースの row detection は canopy が閉じたり照明条件が悪いと崩れやすい。
* そこで、上から見た 3D LiDAR 幾何を使って **作物種類に依存しにくい row navigation** を実現したい。

## 何が新しい？

* crop-specific な特徴設計に寄らず、**高さ差と row 幾何**で検出する crop-agnostic な over-canopy LiDAR pipeline。
* local relative localization と row centroid 蓄積を組み合わせ、row を安定して追う実装。
* detection / following / lane switching まで含めた full-field navigation 系としてまとめている点。

## どうやってる？

* 傾けて載せた LiDAR から点群を取り、virtual ground plane で地面や低い不要点を落とす。
* 残った点を depth bin ごとに K-means でまとめ、row centroid 候補を出す。
* EKF で統合した相対位置推定を使って centroid を時間方向に蓄積し、RANSAC で row line を当てる。
* 制御側では nonlinear MPC で row center を追い、row end に来たら PID ベースの lane switching で次の畝へ移る。

## どこが強い？

* アルゴリズムがかなり素朴で、**field robot に載せやすい**。
* vision がつらい成熟 crop でも、LiDAR の高さ情報で押し切れるのが強い。
* 1 論文で perception から control までつないでおり、実装イメージが掴みやすい。

## 弱そうなところ

* 平行 row 構造をかなり前提としているので、複雑な植生配置には弱い。
* relative localization の drift が長距離でどこまで効くかはもっと見たい。
*比較対象は広くなく、最先端 LiDAR row detection 全体との比較までは踏み込んでいない。

## 関連研究との違い

* camera-based crop row detection より、**illumination や canopy 閉塞に強い幾何ベース**。
* under-canopy navigation より、上から見る over-canopy 構成に振っているのが特徴。
* detection 単体論文でなく、MPC row following まで含めた agricultural navigation system としてまとまっている。

## non-AIとして見る価値

* 農業ロボでも、派手な学習器なしで **幾何・フィルタ・MPC** を積めばかなり戦えると分かる。
* 3D LiDAR を使った row navigation の実務的な入口として良い。

## 難易度

★★★☆☆

## 自分の理解/感想

* 新規アルゴリズムが尖っているというより、field deployment を強く意識した堅いシステム論文。
* 農業ロボで「GPS なしでも最低限走らせたい」という現実的なニーズにかなり素直に刺さる。
