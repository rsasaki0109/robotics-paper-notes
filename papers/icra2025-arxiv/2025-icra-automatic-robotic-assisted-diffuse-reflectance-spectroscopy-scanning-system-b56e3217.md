# Automatic Robotic-Assisted Diffuse Reflectance Spectroscopy Scanning System

> **Updated note**: arXiv PDF をざっと読んで、auto-generated draft を手で補強したメモ。まだ完全精読ではない。

| Item | Value |
| --- | --- |
| Session | Imaging, Scanning, Localization |
| arXiv | [http://arxiv.org/abs/2503.08470](http://arxiv.org/abs/2503.08470) |
| Authors | Deng, Kaizhong;Peters, Christopher;Mylonas, George;Elson, Daniel |
| Source | ICRA 2025 / arXiv |

## TL;DR

- DRS probe を tissue 上で安定走査するための、**robot-assisted spectroscopy scanning system**。
- image-based visual servoing と learned height estimation を組み合わせ、probe contact を安定させている。
- control の芯は classical だが、probe/light detection や height estimation に DNN を使っており **Hybrid** 色が強い。

## Task

* Medical Robotics
* Visual Servoing
* Spectroscopy Scanning
* Surgical Assistance

## Keywords

* DRS / Visual Servoing / Contact Height Estimation / KUKA iiwa / Surgical Scanning

## AI依存度

* Hybrid

## 何を解決？

* 手持ち DRS probe による tissue scanning は、接触圧や手ぶれでスペクトル品質がぶれやすい。
* 特に in-vivo / intra-operative では、対象表面が柔らかく不均一なので安定接触が難しい。
* そこで、**DRS probe の位置・高さ・接触状態をロボットで安定化**したい。

## 何が新しい？

* DRS scanning を in-situ tissue 上で行う robotic assistance system。
* image-based visual servoing に加えて、wrist camera 画像から **contact height を推定**して補償する点。
* analytical Jacobian でなく、学習済み GMM-LLS 的な Jacobian approximation を使って安定制御している点。

## どうやってる？

* KUKA iiwa に probe を載せ、third-person / wrist camera で probe と light area を観測する。
* approach stage では visual servoing で probe tip と target の画像誤差を減らす。
* 接触後は wrist camera 画像から推定した高さ誤差で補正し、走査中の contact pressure 変動を減らす。
* DNN は probe/light detection や高さ推定に使われるが、最終的な motion は PID/servoing で決めている。

## どこが強い？

* spectroscopy を「データを取るだけ」でなく、**安定に押し当てて走査するロボ制御問題**として扱っている。
* contact control を force sensor でなく image 側から補うのが面白い。
* phantom と生体っぽい sample の両方で、manual scan に近い一貫性を出している。

## 弱そうなところ

* tissue type ごとの tuning や generalization はまだ重そう。
* light-center 検出や接触後の視覚条件に依存する部分がある。
* fully non-AI ではなく、perception 側の DNN 依存は強い。

## 関連研究との違い

* 手持ち DRS より、**probe positioning の一貫性**をロボットで担保している。
* ex-vivo specimen scanning より、in-situ / intra-operative 寄り。
* pure visual servoing より、高さ推定ループを別に持って contact を安定化している。

## non-AIとして見る価値

* Hybrid だが、医療ロボで **perception は学習、制御は classical** という分担がよく見える。
* 画像ベース接触制御の設計例としてはかなり参考になる。

## 難易度

★★★★☆

## 自分の理解/感想

* 医療系システム論文としてかなりちゃんとしていて、見た目以上に control integration が大変そう。
* 腫瘍判別そのものより、まず一貫した DRS acquisition を実現することの重要さがよく分かる。
