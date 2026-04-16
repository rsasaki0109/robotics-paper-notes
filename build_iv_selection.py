#!/usr/bin/env python3

from __future__ import annotations

import json
from pathlib import Path


IV_GROUPS = [
    (
        "Localization / Re-localization",
        [
            "2025-icra-gnss-multi-sensor-fusion-using-continuous-time-factor-graph-optimization-9a389d82",
            "2025-icra-semantic-and-feature-guided-uncertainty-quantification-of-visual-localization-for-autonomous-vehicles-5366ee25",
            "2025-icra-superloc-the-key-to-robust-lidar-inertial-localization-lies-in-predicting-alignment-risks-450d6bdd",
            "2025-icra-radar-teach-and-repeat-architecture-and-initial-field-testing-ef4907cf",
            "2025-icra-tdfanet-encoding-sequential-4d-radar-point-clouds-using-trajectory-guided-deformable-feature-aggregation-for-place-recognition-c4987639",
            "2025-icra-evaluating-global-geo-alignment-for-precision-learned-autonomous-vehicle-localization-using-aerial-data-9b6053c2",
        ],
    ),
    (
        "Maps / Topology / Driving Structure",
        [
            "2025-icra-smart-advancing-scalable-map-priors-for-driving-topology-reasoning-c9d6746c",
            "2025-icra-chameleon-fast-slow-neuro-symbolic-lane-topology-extraction-71396389",
        ],
    ),
    (
        "Perception / Occupancy / Sensor Fusion / Adverse Conditions",
        [
            "2025-icra-h3o-hyper-efficient-3d-occupancy-prediction-with-heterogeneous-supervision-b029e3c3",
            "2025-icra-occuq-exploring-efficient-uncertainty-quantification-for-3d-occupancy-prediction-9899ebaa",
            "2025-icra-crab-camera-radar-fusion-for-reducing-depth-ambiguity-in-backward-projection-based-view-transformation-71aa85ea",
            "2025-icra-towards-latency-aware-3d-streaming-perception-for-autonomous-driving-830ea09e",
            "2025-icra-unveiling-the-black-box-independent-functional-module-evaluation-for-bir-d048c0fd",
            "2025-icra-savid-spectravista-aesthetic-vision-integration-for-robust-and-discerning-3d-object-detection-in-challenging-environments-5e1ff4ff",
            "2025-icra-enhancing-autonomous-navigation-by-imaging-hidden-objects-using-single-p-fdffe9ca",
            "2025-icra-low-rank-adaptation-based-all-weather-removal-for-autonomous-navigation-9a081112",
        ],
    ),
    (
        "Prediction / Planning / Control",
        [
            "2025-icra-curb-your-attention-causal-attention-gating-for-robust-trajectory-predic-c099c718",
            "2025-icra-cafe-ad-cross-scenario-adaptive-feature-enhancement-for-trajectory-plann-f3b52abb",
            "2025-icra-beyond-simulation-benchmarking-world-models-for-planning-and-causality-i-cfc5e0c1",
            "2025-icra-actor-critic-cooperative-compensation-to-model-predictive-control-for-of-2466ad7f",
            "2025-icra-decentralized-vehicle-coordination-the-berkeley-deepdrive-drone-dataset-8a6bf914",
        ],
    ),
    (
        "Safety / Security / Benchmarks",
        [
            "2025-icra-cadre-controllable-and-diverse-generation-of-safety-critical-driving-sce-ca41e39e",
            "2025-icra-betty-dataset-a-multi-modal-dataset-for-full-stack-autonomy-b5170da8",
            "2025-icra-slamspoof-practical-lidar-spoofing-attacks-on-localization-systems-guided-by-scan-matching-vulnerability-analysis-6aa8e745",
        ],
    ),
]

IV_TOP10_ORDER = [
    "2025-icra-gnss-multi-sensor-fusion-using-continuous-time-factor-graph-optimization-9a389d82",
    "2025-icra-semantic-and-feature-guided-uncertainty-quantification-of-visual-localization-for-autonomous-vehicles-5366ee25",
    "2025-icra-radar-teach-and-repeat-architecture-and-initial-field-testing-ef4907cf",
    "2025-icra-chameleon-fast-slow-neuro-symbolic-lane-topology-extraction-71396389",
    "2025-icra-h3o-hyper-efficient-3d-occupancy-prediction-with-heterogeneous-supervision-b029e3c3",
    "2025-icra-crab-camera-radar-fusion-for-reducing-depth-ambiguity-in-backward-projection-based-view-transformation-71aa85ea",
    "2025-icra-curb-your-attention-causal-attention-gating-for-robust-trajectory-predic-c099c718",
    "2025-icra-cafe-ad-cross-scenario-adaptive-feature-enhancement-for-trajectory-plann-f3b52abb",
    "2025-icra-beyond-simulation-benchmarking-world-models-for-planning-and-causality-i-cfc5e0c1",
    "2025-icra-slamspoof-practical-lidar-spoofing-attacks-on-localization-systems-guided-by-scan-matching-vulnerability-analysis-6aa8e745",
]

IV_TOP10_META = {
    "2025-icra-gnss-multi-sensor-fusion-using-continuous-time-factor-graph-optimization-9a389d82": {
        "why": "full-stack autonomy の土台として、GNSS + multi-sensor fusion を continuous-time factor graph でどう整理するかを見られる。",
        "focus": "localization / sensor fusion",
    },
    "2025-icra-semantic-and-feature-guided-uncertainty-quantification-of-visual-localization-for-autonomous-vehicles-5366ee25": {
        "why": "AV localization で『当たるか』だけでなく『どれだけ危ないか』を評価する視点が明確で、実運用に近い。",
        "focus": "visual localization / uncertainty",
    },
    "2025-icra-radar-teach-and-repeat-architecture-and-initial-field-testing-ef4907cf": {
        "why": "urban / adverse weather を意識した radar-based relocalization の入口としてわかりやすい。",
        "focus": "radar localization",
    },
    "2025-icra-chameleon-fast-slow-neuro-symbolic-lane-topology-extraction-71396389": {
        "why": "lane topology を fast-slow 構成で扱う設計が IV らしく、HD map / topology reasoning 側の流れを掴みやすい。",
        "focus": "lane topology / map perception",
    },
    "2025-icra-h3o-hyper-efficient-3d-occupancy-prediction-with-heterogeneous-supervision-b029e3c3": {
        "why": "occupancy 系の軽量化と supervision 設計を押さえられ、近年の BEV / occupancy stack を俯瞰しやすい。",
        "focus": "occupancy prediction",
    },
    "2025-icra-crab-camera-radar-fusion-for-reducing-depth-ambiguity-in-backward-projection-based-view-transformation-71aa85ea": {
        "why": "camera-radar fusion を depth ambiguity 解消という形で扱っていて、センサ融合の勘所が見やすい。",
        "focus": "camera-radar fusion",
    },
    "2025-icra-curb-your-attention-causal-attention-gating-for-robust-trajectory-predic-c099c718": {
        "why": "trajectory prediction 側で causal robustness をどう作るかを見られ、planning 前段の代表例としてちょうど良い。",
        "focus": "trajectory prediction",
    },
    "2025-icra-cafe-ad-cross-scenario-adaptive-feature-enhancement-for-trajectory-plann-f3b52abb": {
        "why": "trajectory planning を scenario adaptation の観点で読む入口として使いやすい。",
        "focus": "trajectory planning",
    },
    "2025-icra-beyond-simulation-benchmarking-world-models-for-planning-and-causality-i-cfc5e0c1": {
        "why": "world model を planning / causality の評価軸で比較しており、最近の end-to-end 流れの見取り図になる。",
        "focus": "world models / evaluation",
    },
    "2025-icra-slamspoof-practical-lidar-spoofing-attacks-on-localization-systems-guided-by-scan-matching-vulnerability-analysis-6aa8e745": {
        "why": "IV stack の安全性を考えるうえで、localization spoofing を具体的に読む価値が大きい。",
        "focus": "security / localization robustness",
    },
}

GOOD_NEXT_PICKS = [
    "2025-icra-smart-advancing-scalable-map-priors-for-driving-topology-reasoning-c9d6746c",
    "2025-icra-occuq-exploring-efficient-uncertainty-quantification-for-3d-occupancy-prediction-9899ebaa",
    "2025-icra-unveiling-the-black-box-independent-functional-module-evaluation-for-bir-d048c0fd",
    "2025-icra-cadre-controllable-and-diverse-generation-of-safety-critical-driving-sce-ca41e39e",
]


def load_records(root: Path) -> dict[str, dict[str, str]]:
    records = json.loads((root / "data" / "icra2025" / "icra2025_arxiv_matches.json").read_text(encoding="utf-8"))
    by_id = {}
    for record in records:
        item = dict(record)
        item["id"] = Path(record["note_path"]).stem
        by_id[item["id"]] = item
    return by_id


def selected_items(by_id: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    seen: set[str] = set()
    for group, ids in IV_GROUPS:
        for item_id in ids:
            if item_id in seen:
                raise RuntimeError(f"Duplicate IV selection ID: {item_id}")
            if item_id not in by_id:
                raise RuntimeError(f"Unknown IV selection ID: {item_id}")
            item = dict(by_id[item_id])
            item["group"] = group
            items.append(item)
            seen.add(item_id)
    return items


def write_iv_md(items: list[dict[str, str]], output_path: Path) -> None:
    lines = [
        "# ICRA 2025 IV 24",
        "",
        "ICRA 2025 の arXiv 公開済み 521 本の下書き群から、**Intelligent Vehicles / Autonomous Driving を掴む入口**として 24 本を curated したページです。",
        "",
        "- Base corpus: expanded arXiv drafts 521",
        "- Mix policy: IV 系は AI-heavy な論文も多いため、`Non-AI / Hybrid / AI-heavy` を混ぜて選定",
        "- Focus: localization / map understanding / occupancy / prediction / planning / safety / security",
        "- figure 付きで流し見したい場合は [IV 24 feed](./iv-feed.html) を開く",
        "- まず読む順番が欲しい場合は [IV Top 10](./iv-top.md) から入る",
        "",
    ]
    current_group = None
    for item in items:
        if item["group"] != current_group:
            current_group = item["group"]
            lines.append(f"## {current_group}")
            lines.append("")
        note_name = Path(item["note_path"]).name
        lines.append(f"- [{item['title']}](./{note_name}) — {item['ai_dependency']} — [arXiv]({item['arxiv_url']})")
    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_iv_top_md(by_id: dict[str, dict[str, str]], output_path: Path) -> None:
    lines = [
        "# ICRA 2025 IV Top 10",
        "",
        "expanded 521 corpus を見直したうえで、**まず読むべき Intelligent Vehicles / Autonomous Driving 10 本** を優先順で並べたページです。",
        "",
        "- 軸: **いま読む価値 / IV stack 全体の見取り図になるか / 実運用に近い論点があるか / 分野の広がり**",
        "- 前提: curated entry のため、updated note と draft-first note が混在する",
        "- 方針: localization / relocalization を厚めにしつつ、perception / prediction / planning / security まで含めて選んだ",
        "- 縦スクロールで見たい場合は [IV Top 10 feed](./iv-top-feed.html) を開く",
        "",
        "## Recommended reading path",
        "",
        "1. **Localization / relocalization**: 1-3",
        "2. **Perception / occupancy / sensor fusion**: 4-6",
        "3. **Prediction / planning / evaluation**: 7-9",
        "4. **Security / robustness**: 10",
        "",
        "## Top 10",
        "",
        "| Rank | Paper | AI dependency | Why read now | Focus area |",
        "| --- | --- | --- | --- | --- |",
    ]
    for rank, item_id in enumerate(IV_TOP10_ORDER, start=1):
        item = by_id[item_id]
        meta = IV_TOP10_META[item_id]
        note_name = Path(item["note_path"]).name
        lines.append(
            f"| {rank} | [{item['title']}](./{note_name}) | {item['ai_dependency']} | {meta['why']} | {meta['focus']} |"
        )
    lines.extend(
        [
            "",
            "## Why these 10",
            "",
            "- **Localization を起点に入れる**: GNSS-FGO, visual localization UQ, radar teach-and-repeat",
            "- **Perception 側の今っぽさも押さえる**: lane topology, occupancy, camera-radar fusion",
            "- **Planning までの橋渡し**: trajectory prediction, planning adaptation, world-model evaluation",
            "- **安全性も外さない**: LiDAR spoofing を 1 本入れて IV stack の脆弱性を見る",
            "",
            "## Good next picks",
            "",
        ]
    )
    for item_id in GOOD_NEXT_PICKS:
        item = by_id[item_id]
        note_name = Path(item["note_path"]).name
        lines.append(f"- [{item['title']}](./{note_name})")
    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_selection_json(items: list[dict[str, str]], output_path: Path) -> None:
    minimal = []
    for item in items:
        minimal.append(
            {
                "id": item["id"],
                "group": item["group"],
                "session": item["session"],
                "title": item["title"],
                "note_path": item["note_path"],
                "arxiv_url": item["arxiv_url"],
                "ai_dependency": item["ai_dependency"],
            }
        )
    output_path.write_text(json.dumps(minimal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parent
    by_id = load_records(root)
    items = selected_items(by_id)

    missing_top = [item_id for item_id in IV_TOP10_ORDER if item_id not in by_id]
    if missing_top:
        raise RuntimeError(f"Top10 IDs missing from records: {missing_top}")

    write_iv_md(items, root / "papers" / "icra2025-arxiv" / "iv.md")
    write_iv_top_md(by_id, root / "papers" / "icra2025-arxiv" / "iv-top.md")
    write_selection_json(items, root / "data" / "icra2025" / "icra2025_iv24_selection.json")

    print(
        json.dumps(
            {
                "selected": len(items),
                "top10": len(IV_TOP10_ORDER),
                "groups": len(IV_GROUPS),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
