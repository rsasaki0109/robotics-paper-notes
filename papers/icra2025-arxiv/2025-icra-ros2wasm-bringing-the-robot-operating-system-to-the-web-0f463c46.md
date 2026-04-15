# ROS2WASM: Bringing the Robot Operating System to the Web

> **Draft note**: This page was auto-generated from the ICRA 2025 paper list abstract and public arXiv metadata. Human review is still needed.

| Item | Value |
| --- | --- |
| Session | Resiliency and Security 1 |
| arXiv | [http://arxiv.org/abs/2409.09941](http://arxiv.org/abs/2409.09941) |
| Authors | Fischer, Tobias;Paredes, Isabel;Batchelor, Michael;Beier, Thorsten;Haviland, Jesse;Traversaro, Silvio;Vollprecht, Wolf Kristian;Schmitz, Markus;Milford, Michael J |
| Source | ICRA 2025 / arXiv |

## TL;DR

- The Robot Operating System (ROS) has become the de facto standard middleware in robotics, widely adopted across domains ranging from education to industrial applications.
- The RoboStack distribution, a conda-based packaging system for ROS, has extended ROS's accessibility by facilitating installation across all major operating systems and architectures, integrating seamlessly with scientific tools such as PyTorch and Open3D.
- This paper presents ROS2WASM, a novel integration of RoboStack with WebAssembly, enabling the execution of ROS 2 and its associated software directly within web browsers, without requiring local installations.

## Task

* Visual-Inertial
* Software Tools

## Keywords

* Software Tools for Robot Programming
* Software Tools for Benchmarking and Reproducibility
* Engineering for Robotic Systems

## AI依存度

* Non-AI

## 何を解決？

* The Robot Operating System (ROS) has become the de facto standard middleware in robotics, widely adopted across domains ranging from education to industrial applications.

## 何が新しい？

* This paper presents ROS2WASM, a novel integration of RoboStack with WebAssembly, enabling the execution of ROS 2 and its associated software directly within web browsers, without requiring local installations.

## どうやってる？

* We detail our methodology for cross-compiling ROS 2 packages into WebAssembly, the development of a specialized middleware for ROS 2 communication within browsers, and the implementation of www.ros2wasm.dev, a web platform enabling users to interact with ROS 2 environments.

## どこが強い？

* The Robot Operating System (ROS) has become the de facto standard middleware in robotics, widely adopted across domains ranging from education to industrial applications.

## 弱そうなところ

* abstract ベースの初稿。前提モデル、計算量、失敗ケース、パラメータ感度は本文確認が必要。

## 関連研究との違い

* This paper presents ROS2WASM, a novel integration of RoboStack with WebAssembly, enabling the execution of ROS 2 and its associated software directly within web browsers, without requiring local installations.

## non-AIとして見る価値

* 幾何 / 最適化 / 推定 / 制御の設計をそのまま追いやすく、実装や再利用の観点で学びが大きい。

## 難易度

★★★☆☆（abstract 初見ベース）

## 自分の理解/感想

* 初見では、古典的な数理設計や推定器の構成を学ぶ材料としてかなり良さそう。
