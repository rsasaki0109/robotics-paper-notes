# ICRA 2025 Non-AI Top 12

expanded 521 corpus を見直したうえで、**最初に読むべき 12 本** を優先順で並べたページです。

- 軸: **いま読む価値 / classical な学びの濃さ / 実装や設計に効くか / 分野の広がり**
- 前提: full paper 精読前。draft note と abstract ベースの暫定キュレーション
- 方針: localization / SLAM / GNSS / LiDAR を厚めにしつつ、planning / control も今回の corpus から入れ直した
- 縦スクロールで見たい場合は [Top 12 slide feed](../../index.html) を開く

## Recommended reading path

1. **Localization / estimation core**: 1-6
2. **SLAM / place recognition / mapping**: 7-8
3. **Planning / control expansion**: 9-12

## Top 12

| Rank | Paper | Why read now | Focus area |
| --- | --- | --- | --- |
| 1 | [GNSS/Multi-Sensor Fusion Using Continuous-Time Factor Graph Optimization for Robust Localization](./2025-icra-gnss-multi-sensor-fusion-using-continuous-time-factor-graph-optimization-9a389d82.md) | GNSS + LiDAR + continuous-time factor graph を一本で見られる。expanded corpus を見ても、現場ローカライゼーション直結度は依然として最上位。 | localization / gnss integration |
| 2 | [Equivariant Filter for Tightly Coupled LiDAR-Inertial Odometry](./2025-icra-equivariant-filter-for-tightly-coupled-lidar-inertial-odometry-2e53b464.md) | LiDAR-IMU の tightly coupled 推定を EqF でどう扱うかが明快。古典推定を追う材料として強い。 | localization / lidar odometry |
| 3 | [GenZ-ICP: Generalizable and Degeneracy-Robust LiDAR Odometry Using an Adaptive Weighting](./2025-icra-genz-icp-generalizable-and-degeneracy-robust-lidar-odometry-using-an-ada-ba370ba1.md) | 退化ケースに強い LiDAR odometry という、実運用で刺さる問題設定が良い。実装価値も高い。 | localization / lidar odometry |
| 4 | [DynaVINS++: Robust Visual-Inertial State Estimator in Dynamic Environments by Adaptive Truncated Least Squares and Stable State Recovery](./2025-icra-dynavins-robust-visual-inertial-state-estimator-in-dynamic-environments-a88daf2a.md) | 動的環境で壊れやすい VINS をロバスト推定で立て直している。学習に寄らない改善として見やすい。 | visual-inertial / robust estimation |
| 5 | [Universal Online Temporal Calibration for Optimization-Based Visual-Inertial Navigation Systems](./2025-icra-universal-online-temporal-calibration-for-optimization-based-visual-iner-ab7c16cf.md) | 時間ずれ補正は地味だが効く。オンライン temporal calibration をどう扱うかの価値が大きい。 | calibration / localization |
| 6 | [Equivariant IMU Preintegration with Biases: A Galilean Group Approach](./2025-icra-equivariant-imu-preintegration-with-biases-a-galilean-group-approach-1c90d227.md) | IMU preintegration は多くの推定器の基礎部品。bias を含む幾何的扱い方を押さえられる。 | state estimation / preintegration |
| 7 | [A Hessian for Gaussian Mixture Likelihoods in Nonlinear Least Squares](./2025-icra-a-hessian-for-gaussian-mixture-likelihoods-in-nonlinear-least-squares-6e9814a0.md) | 推定と最適化の地力を上げる一本。SLAM や sensor fusion の裏側の計算を深められる。 | estimation / optimization |
| 8 | [Narrowing Your FOV with SOLiD: Spatially Organized and Lightweight Global Descriptor for FOV-Constrained LiDAR Place Recognition](./2025-icra-narrowing-your-fov-with-solid-spatially-organized-and-lightweight-global-587da81c.md) | 狭視野 LiDAR の place recognition という実機制約に近いテーマ。再局在化の観点で学びやすい。 | place recognition / localization |
| 9 | [A Complete and Bounded-Suboptimal Algorithm for a Moving Target Traveling Salesman Problem with Obstacles in 3D](./2025-icra-a-complete-and-bounded-suboptimal-algorithm-for-a-moving-target-traveling-salesman-problem-with-obstacles-in-3d-918c2b36.md) | expanded corpus の planning 側でかなり強い一本。完全性と bounded-suboptimality を明示していて読み筋が良い。 | motion planning |
| 10 | [Endpoint-Explicit Differential Dynamic Programming Via Exact Resolution](./2025-icra-endpoint-explicit-differential-dynamic-programming-via-exact-resolution-b7c9c9f2.md) | DDP の見通しを良くするタイプで、optimal control の勘所を押さえるのに向いている。 | optimal control |
| 11 | [Variable Time-Step MPC for Agile Multi-Rotor UAV Interception of Dynamic Targets](./2025-icra-variable-time-step-mpc-for-agile-multi-rotor-uav-interception-of-dynamic-aa48ddef.md) | 可変 time-step と horizon 設計が面白い。MPC をより実践的に使う発想が取れる。 | planning / control |
| 12 | [Kinodynamic Model Predictive Control for Energy Efficient Locomotion of Legged Robots with Parallel Elasticity](./2025-icra-kinodynamic-model-predictive-control-for-energy-efficient-locomotion-of-legged-robots-with-parallel-elasticity-881862ea.md) | legged 制御側の広がりとして入れる価値が高い。運動学とエネルギー効率を MPC でどう扱うかを見られる。 | legged control / MPC |

## Why these 12

- **推定の芯が強い**: GNSS-FGO, Eq-LIO, DynaVINS++, temporal calibration, IMU preintegration, Hessian
- **SLAM 側の広がりがある**: GenZ-ICP, SOLiD
- **localization 以外も読める**: moving-target planning, DDP, aerial MPC, legged MPC

## Good next picks

- [SuperLoc: The Key to Robust LiDAR-Inertial Localization Lies in Predicting Alignment Risks](./2025-icra-superloc-the-key-to-robust-lidar-inertial-localization-lies-in-predicting-alignment-risks-450d6bdd.md)
- [Kinematic-ICP: Enhancing LiDAR Odometry with Kinematic Constraints for Wheeled Mobile Robots Moving on Planar Surfaces](./2025-icra-kinematic-icp-enhancing-lidar-odometry-with-kinematic-constraints-for-wheeled-mobile-robots-moving-on-planar-surfaces-c7ecb98b.md)
- [Introspective Loop Closure for SLAM with 4D Imaging Radar](./2025-icra-introspective-loop-closure-for-slam-with-4d-imaging-radar-2151239e.md)
- [PTZ-Calib: Robust Pan-Tilt-Zoom Camera Calibration](./2025-icra-ptz-calib-robust-pan-tilt-zoom-camera-calibration-b24578c8.md)