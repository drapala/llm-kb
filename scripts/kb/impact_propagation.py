#!/usr/bin/env python3
"""
Impact propagation: given a trigger slug (just ingested), find affected promoted
articles and generate patch-queue.yaml entries.

Materiality scoring (0.0–1.0):
  base score by how the trigger is connected to the affected article:
    depends_on match         → 0.80  (explicit dependency)
    typed link (challenging) → 0.90  → impact_type: claim_contradiction
    typed link (derivedFrom) → 0.65  → impact_type: new_support
    typed link (other)       → 0.50  → impact_type: bridge_creation / scope_expansion
    untyped link             → 0.30  → impact_type: scope_expansion
  topic overlap bonus: +0.05 per shared topic, capped at +0.20

  Thresholds (from patch-queue.yaml spec):
    >= 0.85: high materiality, auto_apply_eligible (unless claim_contradiction)
    0.45–0.85: medium, queue for review
    < 0.45: skip (no patch generated)

Usage:
  python scripts/kb/impact_propagation.py --trigger <slug>
  python scripts/kb/impact_propagation.py --trigger <slug> --dry-run
  python scripts/kb/impact_propagation.py --trigger <slug> --min-materiality 0.3
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent.parent
GRAPH_PATH = ROOT / "outputs" / "state" / "link-graph.json"
HEALTH_PATH = ROOT / "outputs" / "state" / "article-health.yaml"
PATCHQ_PATH = ROOT / "outputs" / "state" / "patch-queue.yaml"
WIKI_DIR = ROOT / "wiki" / "concepts"

MATERIALITY_AUTO = 0.85
MATERIALITY_QUEUE = 0.45

RELATION_TO_IMPACT = {
    "challenges": "claim_contradiction",
    "contradicts": "claim_contradiction",
    "derivedfrom": "new_support",
    "supports": "new_support",
    "complementsat": "bridge_creation",
    "analogto": "bridge_creation",
    "instanciates": "new_support",
    "refines": "claim_refinement",
    "ispartof": "scope_expansion",
    "extends": "scope_expansion",
    "relaciona": "scope_expansion",
}


def load_graph() -> dict:
    if not GRAPH_PATH.exists():
        sys.exit(f"link-graph.json not found at {GRAPH_PATH}. Run link_graph.py first.")
    return json.loads(GRAPH_PATH.read_text())


def load_health() -> dict:
    if not HEALTH_PATH.exists():
        return {"articles": []}
    return yaml.safe_load(HEALTH_PATH.read_text()) or {"articles": []}


def load_patchq() -> dict:
    if not PATCHQ_PATH.exists():
        return {"patch_queue": []}
    return yaml.safe_load(PATCHQ_PATH.read_text()) or {"patch_queue": []}


def promoted_slugs(health: dict) -> set[str]:
    return {
        a["article_slug"]
        for a in health.get("articles", [])
        if a.get("promotion_status") == "promoted"
    }


def topics_for(slug: str, graph: dict) -> set[str]:
    node = graph["nodes"].get(slug, {})
    return set(node.get("topics", []))


def next_patch_id(patchq: dict) -> str:
    today = date.today().strftime("%Y-%m-%d")
    existing = [
        p["patch_id"]
        for p in patchq.get("patch_queue", [])
        if p["patch_id"].startswith(f"patch-{today}-")
    ]
    n = len(existing) + 1
    return f"patch-{today}-{n:03d}"


def impact_type_from_relation(relation: str) -> str:
    return RELATION_TO_IMPACT.get(relation.lower(), "scope_expansion")


def compute_materiality(
    trigger: str,
    affected: str,
    graph: dict,
    health_entry: dict,
) -> tuple[float, str, list[dict]]:
    """
    Returns (materiality_score, impact_type, matching_edges).
    """
    edges = graph.get("edges", [])
    depends_on = health_entry.get("depends_on", [])

    # 1. Check explicit depends_on
    wiki_dep = f"wiki/concepts/{trigger}.md"
    if wiki_dep in depends_on or trigger in depends_on:
        # Find edge type to refine impact_type
        typed = [
            e
            for e in edges
            if e["source"] == affected
            and e["target"] == trigger
            and e["type"] != "untyped"
        ]
        if typed:
            best = typed[0]
            impact = impact_type_from_relation(best["type"])
            base = (
                0.90
                if "contradict" in best["type"] or "challeng" in best["type"]
                else 0.80
            )
        else:
            impact = "scope_expansion"
            base = 0.80
        topic_bonus = _topic_bonus(trigger, affected, graph)
        return min(1.0, base + topic_bonus), impact, typed

    # 2. Find edges: trigger → affected (trigger points to affected)
    outgoing = [e for e in edges if e["source"] == trigger and e["target"] == affected]
    # 3. Find edges: affected → trigger (affected already cites trigger)
    incoming = [e for e in edges if e["source"] == affected and e["target"] == trigger]

    matching = outgoing + incoming
    if not matching:
        return 0.0, "scope_expansion", []

    # Pick highest-materiality edge
    best_score = 0.0
    best_impact = "scope_expansion"
    best_edges = []

    for e in matching:
        rel = e["type"]
        if rel == "untyped":
            score = 0.30
            impact = "scope_expansion"
        elif rel.lower() in ("challenges", "contradicts"):
            score = 0.90
            impact = "claim_contradiction"
        elif rel.lower() in ("derivedfrom", "supports", "instanciates"):
            score = 0.65
            impact = "new_support"
        elif rel.lower() in ("refines",):
            score = 0.60
            impact = "claim_refinement"
        elif rel.lower() in ("complementsat", "analogto"):
            score = 0.50
            impact = "bridge_creation"
        else:
            score = 0.45
            impact = "scope_expansion"

        if score > best_score:
            best_score = score
            best_impact = impact
            best_edges = [e]

    topic_bonus = _topic_bonus(trigger, affected, graph)
    return min(1.0, best_score + topic_bonus), best_impact, best_edges


def _topic_bonus(trigger: str, affected: str, graph: dict) -> float:
    t_topics = topics_for(trigger, graph)
    a_topics = topics_for(affected, graph)
    overlap = len(t_topics & a_topics)
    return min(0.20, overlap * 0.05)


def materiality_label(score: float) -> str:
    if score >= MATERIALITY_AUTO:
        return "high"
    if score >= MATERIALITY_QUEUE:
        return "medium"
    return "low"


def patch_summary(
    trigger: str, affected: str, impact_type: str, edges: list[dict]
) -> str:
    edge_desc = ""
    if edges:
        e = edges[0]
        edge_desc = f" via '{e['type']}' link"
        if e.get("label"):
            edge_desc += f" ({e['label'][:80]})"
    return (
        f"Novo artigo '{trigger}' conectado a '{affected}'{edge_desc}. "
        f"Impact type: {impact_type}. Revisar se há claims a incorporar ou refinar."
    )


def find_affected(
    trigger: str,
    graph: dict,
    health: dict,
    min_materiality: float,
) -> list[dict]:
    """
    Find promoted articles affected by trigger.
    Returns list of patch dicts ready for patch-queue.yaml.
    """
    promoted = promoted_slugs(health)
    health_by_slug = {a["article_slug"]: a for a in health.get("articles", [])}

    # Candidates: promoted articles that share any edge with trigger
    edge_neighbors = set()
    for e in graph.get("edges", []):
        if e["source"] == trigger:
            edge_neighbors.add(e["target"])
        if e["target"] == trigger:
            edge_neighbors.add(e["source"])

    # Also promoted articles with trigger in depends_on
    dep_matches = {
        a["article_slug"]
        for a in health.get("articles", [])
        if f"wiki/concepts/{trigger}.md" in a.get("depends_on", [])
        or trigger in a.get("depends_on", [])
    }

    candidates = (edge_neighbors | dep_matches) & promoted
    candidates.discard(trigger)

    patches = []
    patchq = load_patchq()

    # Skip already-queued (pending) patches for same trigger+affected pair
    already_queued = {
        (p["trigger_slug"], p["article_slug"])
        for p in patchq.get("patch_queue", [])
        if p.get("status") == "pending"
    }

    for affected in sorted(candidates):
        entry = health_by_slug.get(affected, {})
        score, impact_type, edges = compute_materiality(trigger, affected, graph, entry)

        if score < min_materiality:
            continue

        if (trigger, affected) in already_queued:
            continue

        mat_label = materiality_label(score)
        auto_eligible = (score >= MATERIALITY_AUTO) and (
            impact_type != "claim_contradiction"
        )

        patches.append(
            {
                "patch_id": None,  # filled by caller
                "article_slug": affected,
                "trigger_slug": trigger,
                "status": "pending",
                "impact_type": impact_type,
                "materiality": mat_label,
                "materiality_score": round(score, 3),
                "auto_apply_eligible": auto_eligible,
                "affected_claims": [],
                "summary": patch_summary(trigger, affected, impact_type, edges),
                "created_at": str(date.today()),
            }
        )

    return patches


def apply_patches(
    patches: list[dict],
    patchq: dict,
    health: dict,
    dry_run: bool,
) -> None:
    if not patches:
        print("  No patches to apply.")
        return

    health_by_slug = {a["article_slug"]: a for a in health.get("articles", [])}

    for patch in patches:
        patch_id = next_patch_id(patchq)
        patch["patch_id"] = patch_id
        patchq.setdefault("patch_queue", []).append(patch)

        # Update article-health.yaml
        affected = patch["article_slug"]
        if affected in health_by_slug:
            entry = health_by_slug[affected]
            if patch["impact_type"] == "claim_contradiction":
                entry["freshness_status"] = "under_review"
                entry["epistemic_risk"] = "high"
            else:
                if entry.get("freshness_status") == "current":
                    entry["freshness_status"] = "impacted"
            entry["pending_patch_count"] = entry.get("pending_patch_count", 0) + 1
            entry["last_impact_at"] = str(date.today())

        action = "AUTO-APPLY" if patch["auto_apply_eligible"] else "QUEUE"
        print(
            f"  [{action}] {patch['article_slug']} ← {patch['trigger_slug']}"
            f"  materiality={patch['materiality']} ({patch['materiality_score']:.2f})"
            f"  type={patch['impact_type']}"
        )

    if not dry_run:
        PATCHQ_PATH.write_text(
            yaml.dump(
                patchq, allow_unicode=True, sort_keys=False, default_flow_style=False
            )
        )
        HEALTH_PATH.write_text(
            yaml.dump(
                health, allow_unicode=True, sort_keys=False, default_flow_style=False
            )
        )
        print(f"  Wrote {PATCHQ_PATH.name} ({len(patches)} new patches)")
        print(f"  Wrote {HEALTH_PATH.name}")
    else:
        print(f"  [dry] {len(patches)} patches would be written")


def main():
    parser = argparse.ArgumentParser(description="KB impact propagation")
    parser.add_argument("--trigger", required=True, help="Slug of the ingested article")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--min-materiality",
        type=float,
        default=MATERIALITY_QUEUE,
        help=f"Minimum materiality score to generate a patch (default: {MATERIALITY_QUEUE})",
    )
    args = parser.parse_args()

    trigger = args.trigger.removesuffix(".md")

    graph = load_graph()
    if trigger not in graph["nodes"]:
        sys.exit(
            f"Trigger slug '{trigger}' not in link-graph.json. "
            "Run link_graph.py first, then retry."
        )

    health = load_health()
    patchq = load_patchq()

    print(f"Impact propagation for: {trigger}")
    patches = find_affected(trigger, graph, health, args.min_materiality)
    print(f"Candidates: {len(patches)} affected promoted articles")

    apply_patches(patches, patchq, health, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
