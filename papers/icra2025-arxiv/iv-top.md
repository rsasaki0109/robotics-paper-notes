# ICRA 2025 IV Top 10

expanded 521 corpus を見直したうえで、**まず読むべき Intelligent Vehicles / Autonomous Driving 10 本** を優先順で並べたページです。

- 軸: **いま読む価値 / IV stack 全体の見取り図になるか / 実運用に近い論点があるか / 分野の広がり**
- 前提: curated entry のため、updated note と draft-first note が混在する
- 方針: localization / relocalization を厚めにしつつ、perception / prediction / planning / security まで含めて選んだ
- 縦スクロールで見たい場合は [IV Top 10 feed](./iv-top-feed.html) を開く

## Recommended reading path

1. **Localization / relocalization**: 1-3
2. **Perception / occupancy / sensor fusion**: 4-6
3. **Prediction / planning / evaluation**: 7-9
4. **Security / robustness**: 10

## Top 10

| Rank | Paper | AI dependency | Why read now | Focus area |
| --- | --- | --- | --- | --- |
| 1 | [GNSS/Multi-Sensor Fusion Using Continuous-Time Factor Graph Optimization for Robust Localization](./2025-icra-gnss-multi-sensor-fusion-using-continuous-time-factor-graph-optimization-9a389d82.md) | Non-AI | full-stack autonomy の土台として、GNSS + multi-sensor fusion を continuous-time factor graph でどう整理するかを見られる。 | localization / sensor fusion |
| 2 | [Semantic and Feature Guided Uncertainty Quantification of Visual Localization for Autonomous Vehicles](./2025-icra-semantic-and-feature-guided-uncertainty-quantification-of-visual-localization-for-autonomous-vehicles-5366ee25.md) | Hybrid | AV localization で『当たるか』だけでなく『どれだけ危ないか』を評価する視点が明確で、実運用に近い。 | visual localization / uncertainty |
| 3 | [Radar Teach and Repeat: Architecture and Initial Field Testing](./2025-icra-radar-teach-and-repeat-architecture-and-initial-field-testing-ef4907cf.md) | Non-AI | urban / adverse weather を意識した radar-based relocalization の入口としてわかりやすい。 | radar localization |
| 4 | [Chameleon: Fast-Slow Neuro-Symbolic Lane Topology Extraction](./2025-icra-chameleon-fast-slow-neuro-symbolic-lane-topology-extraction-71396389.md) | AI-heavy | lane topology を fast-slow 構成で扱う設計が IV らしく、HD map / topology reasoning 側の流れを掴みやすい。 | lane topology / map perception |
| 5 | [H3O: Hyper-Efficient 3D Occupancy Prediction with Heterogeneous Supervision](./2025-icra-h3o-hyper-efficient-3d-occupancy-prediction-with-heterogeneous-supervision-b029e3c3.md) | Hybrid | occupancy 系の軽量化と supervision 設計を押さえられ、近年の BEV / occupancy stack を俯瞰しやすい。 | occupancy prediction |
| 6 | [CRAB: Camera-Radar Fusion for Reducing Depth Ambiguity in Backward Projection Based View Transformation](./2025-icra-crab-camera-radar-fusion-for-reducing-depth-ambiguity-in-backward-projection-based-view-transformation-71aa85ea.md) | Hybrid | camera-radar fusion を depth ambiguity 解消という形で扱っていて、センサ融合の勘所が見やすい。 | camera-radar fusion |
| 7 | [Curb Your Attention: Causal Attention Gating for Robust Trajectory Prediction in Autonomous Driving](./2025-icra-curb-your-attention-causal-attention-gating-for-robust-trajectory-predic-c099c718.md) | AI-heavy | trajectory prediction 側で causal robustness をどう作るかを見られ、planning 前段の代表例としてちょうど良い。 | trajectory prediction |
| 8 | [CAFE-AD: Cross-Scenario Adaptive Feature Enhancement for Trajectory Planning in Autonomous Driving](./2025-icra-cafe-ad-cross-scenario-adaptive-feature-enhancement-for-trajectory-plann-f3b52abb.md) | Hybrid | trajectory planning を scenario adaptation の観点で読む入口として使いやすい。 | trajectory planning |
| 9 | [Beyond Simulation: Benchmarking World Models for Planning and Causality in Autonomous Driving](./2025-icra-beyond-simulation-benchmarking-world-models-for-planning-and-causality-i-cfc5e0c1.md) | Hybrid | world model を planning / causality の評価軸で比較しており、最近の end-to-end 流れの見取り図になる。 | world models / evaluation |
| 10 | [SLAMSpoof: Practical LiDAR Spoofing Attacks on Localization Systems Guided by Scan Matching Vulnerability Analysis](./2025-icra-slamspoof-practical-lidar-spoofing-attacks-on-localization-systems-guided-by-scan-matching-vulnerability-analysis-6aa8e745.md) | Non-AI | IV stack の安全性を考えるうえで、localization spoofing を具体的に読む価値が大きい。 | security / localization robustness |

## Why these 10

- **Localization を起点に入れる**: GNSS-FGO, visual localization UQ, radar teach-and-repeat
- **Perception 側の今っぽさも押さえる**: lane topology, occupancy, camera-radar fusion
- **Planning までの橋渡し**: trajectory prediction, planning adaptation, world-model evaluation
- **安全性も外さない**: LiDAR spoofing を 1 本入れて IV stack の脆弱性を見る

## Good next picks

- [SMART: Advancing Scalable Map Priors for Driving Topology Reasoning](./2025-icra-smart-advancing-scalable-map-priors-for-driving-topology-reasoning-c9d6746c.md)
- [OCCUQ: Exploring Efficient Uncertainty Quantification for 3D Occupancy Prediction](./2025-icra-occuq-exploring-efficient-uncertainty-quantification-for-3d-occupancy-prediction-9899ebaa.md)
- [Unveiling the Black Box: Independent Functional Module Evaluation for Bird's-Eye-View Perception Model](./2025-icra-unveiling-the-black-box-independent-functional-module-evaluation-for-bir-d048c0fd.md)
- [CaDRE: Controllable and Diverse Generation of Safety-Critical Driving Scenarios Using Real-World Trajectories](./2025-icra-cadre-controllable-and-diverse-generation-of-safety-critical-driving-sce-ca41e39e.md)
