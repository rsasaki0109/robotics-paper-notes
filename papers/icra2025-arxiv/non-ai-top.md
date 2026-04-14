# ICRA 2025 Non-AI Top 12

ICRA 2025 の arXiv 公開済み Non-AI 論文 60 本のうち、**最初に読むべき 12 本** を優先順で並べたページです。

- 軸: **Autoware との近さ / classical な学びの濃さ / 実装に効くか / いま読む価値**
- 前提: まだ full paper 精読前で、既存の draft note と abstract ベースの暫定キュレーション
- 方針: まずは **Localization / SLAM / GNSS / LiDAR** を厚めにし、Planning / Control も最低限押さえる

## Recommended reading path

1. **Localization core**: 1-6
2. **SLAM / place recognition / mapping**: 7-9
3. **Planning / control expansion**: 10-12

## Top 12

| Rank | Paper | Why read now | Autoware area |
| --- | --- | --- | --- |
| 1 | [GNSS/Multi-Sensor Fusion Using Continuous-Time Factor Graph Optimization for Robust Localization](./2025-icra-gnss-multi-sensor-fusion-using-continuous-time-factor-graph-optimization-9a389d82.md) | GNSS + LiDAR + factor graph で、都市部ローカライゼーションに直結。テーマのど真ん中。 | localization / gnss integration |
| 2 | [Equivariant Filter for Tightly Coupled LiDAR-Inertial Odometry](./2025-icra-equivariant-filter-for-tightly-coupled-lidar-inertial-odometry-2e53b464.md) | LiDAR-IMU の tightly coupled 推定を EqF でどう安定化するかが見える。数理も実装価値も高い。 | localization / lidar odometry |
| 3 | [GenZ-ICP: Generalizable and Degeneracy-Robust LiDAR Odometry Using an Adaptive Weighting](./2025-icra-genz-icp-generalizable-and-degeneracy-robust-lidar-odometry-using-an-ada-ba370ba1.md) | corridor など退化ケースに強い LiDAR odometry。現場で困る典型問題に真正面から効く。 | localization / lidar odometry |
| 4 | [DynaVINS++: Robust Visual-Inertial State Estimator in Dynamic Environments by Adaptive Truncated Least Squares and Stable State Recovery](./2025-icra-dynavins-robust-visual-inertial-state-estimator-in-dynamic-environments-a88daf2a.md) | 動的物体で壊れやすい VINS を、学習ではなくロバスト推定で立て直しているのが良い。 | localization / sensor fusion |
| 5 | [Universal Online Temporal Calibration for Optimization-Based Visual-Inertial Navigation Systems](./2025-icra-universal-online-temporal-calibration-for-optimization-based-visual-iner-ab7c16cf.md) | 実機では地味に効く時間ずれ補正。オンライン temporal calibration は運用面の価値が大きい。 | sensor calibration / localization |
| 6 | [Equivariant IMU Preintegration with Biases: A Galilean Group Approach](./2025-icra-equivariant-imu-preintegration-with-biases-a-galilean-group-approach-1c90d227.md) | IMU preintegration は基礎ブロック。bias を含めた幾何的な扱い方を押さえる価値が高い。 | state estimation / localization |
| 7 | [A Hessian for Gaussian Mixture Likelihoods in Nonlinear Least Squares](./2025-icra-a-hessian-for-gaussian-mixture-likelihoods-in-nonlinear-least-squares-6e9814a0.md) | 推定・最適化の基礎体力を上げる論文。SLAM や sensor fusion の裏側に効く。 | estimation / optimization |
| 8 | [Narrowing Your FOV with SOLiD: Spatially Organized and Lightweight Global Descriptor for FOV-Constrained LiDAR Place Recognition](./2025-icra-narrowing-your-fov-with-solid-spatially-organized-and-lightweight-global-587da81c.md) | 狭視野 LiDAR の place recognition は実機制約に近い。loop closure や再局在化の勘所を学びやすい。 | localization / place recognition |
| 9 | [CoVoxSLAM: GPU Accelerated Globally Consistent Dense SLAM](./2025-icra-covoxslam-gpu-accelerated-globally-consistent-dense-slam-6599ffd4.md) | dense SLAM を GPU で現実的に回す話。精度だけでなく実行性能も意識していて実装寄り。 | mapping / localization |
| 10 | [Exact Wavefront Propagation for Globally Optimal One-To-All Path Planning on 2D Cartesian Grids](./2025-icra-exact-wavefront-propagation-for-globally-optimal-one-to-all-path-plannin-50b72344.md) | 幾何ベースで path planning の基礎を鍛える一本。global optimality をどう出すかが明快。 | planning |
| 11 | [Variable Time-Step MPC for Agile Multi-Rotor UAV Interception of Dynamic Targets](./2025-icra-variable-time-step-mpc-for-agile-multi-rotor-uav-interception-of-dynamic-aa48ddef.md) | 可変 time-step と horizon 設計が面白い。MPC をどう実用寄りにするかの発想が取れる。 | planning / control |
| 12 | [Distributed Certifiably Correct Range-Aided SLAM](./2025-icra-distributed-certifiably-correct-range-aided-slam-22538aae.md) | すぐ実装するタイプではないが、certifiable / distributed SLAM の整理に価値がある。 | multi-robot localization / SLAM |

## Why these 12

- **すぐ効く**: GNSS-FGO, Eq-LIO, GenZ-ICP, DynaVINS++, temporal calibration
- **基礎体力が付く**: IMU preintegration, Hessian, certifiably correct SLAM
- **周辺を広げる**: place recognition, dense SLAM, planning, MPC

## Good next picks

- [Equivariant Filter Design for Range-Only SLAM](./2025-icra-equivariant-filter-design-for-range-only-slam-89523508.md)
- [PTZ-Calib: Robust Pan-Tilt-Zoom Camera Calibration](./2025-icra-ptz-calib-robust-pan-tilt-zoom-camera-calibration-b24578c8.md)
- [From Instantaneous to Predictive Control: A More Intuitive and Tunable MPC Formulation for Robot Manipulators](./2025-icra-from-instantaneous-to-predictive-control-a-more-intuitive-and-tunable-mp-10d09420.md)
