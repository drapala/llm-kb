#!/usr/bin/env python3
"""
patch-metrics.py — Métricas operacionais do sistema de manutenção epistêmica.

Lê patch-queue.yaml e article-health.yaml e computa:
  - patch_precision_estimate: ratio applied / (applied + dismissed)
  - under_review_count: artigos com freshness_status: under_review
  - mean_time_to_resolution: média de dias entre created_at e applied_at
  - articles_with_repeated_impact: artigos com 2+ patches
  - top_sources_of_contradiction: triggers que mais geraram claim_contradiction

Uso:
    python scripts/patch-metrics.py              # output texto
    python scripts/patch-metrics.py --json       # output JSON
    python scripts/patch-metrics.py --save       # salva outputs/state/patch-metrics.yaml
"""

import argparse
import json
from collections import Counter
from datetime import date, datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
HEALTH_FILE = REPO_ROOT / "outputs/state/article-health.yaml"
QUEUE_FILE = REPO_ROOT / "outputs/state/patch-queue.yaml"
METRICS_FILE = REPO_ROOT / "outputs/state/patch-metrics.yaml"


def load_yaml(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f) or {}


def parse_date(s) -> date | None:
    if not s:
        return None
    if isinstance(s, date):
        return s
    try:
        return datetime.strptime(str(s), "%Y-%m-%d").date()
    except ValueError:
        return None


def compute_metrics(health: dict, queue_data: dict) -> dict:
    articles = health.get("articles", [])
    patches = queue_data.get("patch_queue", [])

    # ── freshness distribution ────────────────────────────────────────────────
    freshness_counts = Counter(a.get("freshness_status", "current") for a in articles)
    under_review_count = freshness_counts.get("under_review", 0)
    impacted_count = freshness_counts.get("impacted", 0)
    current_count = freshness_counts.get("current", 0)

    # ── patch counts by status ────────────────────────────────────────────────
    status_counts = Counter(p.get("status", "pending") for p in patches)
    applied = status_counts.get("applied", 0)
    dismissed = status_counts.get("dismissed", 0)
    pending = status_counts.get("pending", 0)
    escalated = status_counts.get("escalated", 0)

    # patch precision = applied / (applied + dismissed), null if no resolved patches
    resolved = applied + dismissed
    patch_precision_estimate = round(applied / resolved, 3) if resolved > 0 else None

    # ── mean time to resolution ───────────────────────────────────────────────
    resolution_days = []
    for p in patches:
        if p.get("status") == "applied":
            created = parse_date(p.get("created_at"))
            applied_at = parse_date(p.get("applied_at"))
            if created and applied_at:
                resolution_days.append((applied_at - created).days)

    mean_time_to_resolution = (
        round(sum(resolution_days) / len(resolution_days), 1)
        if resolution_days
        else None
    )

    # ── articles with repeated impact ────────────────────────────────────────
    impact_count_per_article: Counter = Counter()
    for p in patches:
        slug = p.get("article_slug")
        if slug and p.get("status") != "dismissed":
            impact_count_per_article[slug] += 1

    articles_with_repeated_impact = [
        {"article": slug, "impact_count": count}
        for slug, count in impact_count_per_article.most_common()
        if count >= 2
    ]

    # ── top sources of contradiction ─────────────────────────────────────────
    contradiction_triggers: Counter = Counter()
    for p in patches:
        if p.get("impact_type") == "claim_contradiction":
            trigger = p.get("trigger_slug", "unknown")
            contradiction_triggers[trigger] += 1

    top_sources_of_contradiction = [
        {"trigger": slug, "count": count}
        for slug, count in contradiction_triggers.most_common(5)
    ]

    # ── impact type distribution ──────────────────────────────────────────────
    impact_type_dist = Counter(p.get("impact_type", "unknown") for p in patches)

    # ── high-churn articles (epistemically unstable) ──────────────────────────
    # Articles that: (a) under_review OR (b) have 2+ patches OR (c) have epistemic_risk: high
    high_churn = []
    for a in articles:
        slug = a["article_slug"]
        risk_flags = []
        if a.get("freshness_status") == "under_review":
            risk_flags.append("under_review")
        if a.get("epistemic_risk") == "high":
            risk_flags.append("epistemic_risk:high")
        if impact_count_per_article.get(slug, 0) >= 2:
            risk_flags.append(f"repeated_impact:{impact_count_per_article[slug]}")
        if risk_flags:
            high_churn.append({"article": slug, "flags": risk_flags})

    # ── summary ───────────────────────────────────────────────────────────────
    total_promoted = len(articles)
    total_patches = len(patches)

    return {
        "computed_at": str(date.today()),
        "corpus": {
            "total_promoted": total_promoted,
            "freshness": {
                "current": current_count,
                "impacted": impacted_count,
                "under_review": under_review_count,
            },
        },
        "patches": {
            "total": total_patches,
            "by_status": dict(status_counts),
            "by_impact_type": dict(impact_type_dist),
        },
        "metrics": {
            "patch_precision_estimate": patch_precision_estimate,
            "under_review_count": under_review_count,
            "mean_time_to_resolution_days": mean_time_to_resolution,
            "articles_with_repeated_impact": articles_with_repeated_impact,
            "top_sources_of_contradiction": top_sources_of_contradiction,
        },
        "risk_flags": {
            "high_churn_articles": high_churn,
        },
    }


def print_report(metrics: dict) -> None:
    c = metrics["corpus"]
    p = metrics["patches"]
    m = metrics["metrics"]
    r = metrics["risk_flags"]

    print(f"\n{'=' * 55}")
    print(f"  PATCH METRICS — {metrics['computed_at']}")
    print(f"{'=' * 55}")

    print(f"\nCorpus: {c['total_promoted']} promovidos")
    f = c["freshness"]
    print(
        f"  current: {f['current']}  |  impacted: {f['impacted']}  |  under_review: {f['under_review']}"
    )

    print(f"\nPatches: {p['total']} total")
    bs = p["by_status"]
    print(
        f"  pending: {bs.get('pending', 0)}  applied: {bs.get('applied', 0)}  "
        f"dismissed: {bs.get('dismissed', 0)}  escalated: {bs.get('escalated', 0)}"
    )
    if p["by_impact_type"]:
        print(
            "  por tipo:",
            ", ".join(f"{k}:{v}" for k, v in sorted(p["by_impact_type"].items())),
        )

    print("\nMétricas operacionais:")
    prec = m["patch_precision_estimate"]
    print(
        f"  patch_precision_estimate : {f'{prec:.1%}' if prec is not None else 'n/a (sem patches resolvidos)'}"
    )
    print(f"  under_review_count       : {m['under_review_count']}")
    mtr = m["mean_time_to_resolution_days"]
    print(
        f"  mean_time_to_resolution  : {f'{mtr} dias' if mtr is not None else 'n/a (sem patches aplicados)'}"
    )

    if m["articles_with_repeated_impact"]:
        print(
            f"\nArtigos com impacto repetido ({len(m['articles_with_repeated_impact'])}):"
        )
        for item in m["articles_with_repeated_impact"]:
            print(f"  {item['article']} — {item['impact_count']}x")

    if m["top_sources_of_contradiction"]:
        print("\nPrincipais fontes de contradição:")
        for item in m["top_sources_of_contradiction"]:
            print(f"  {item['trigger']} — {item['count']}x")

    if r["high_churn_articles"]:
        print(f"\nArtigos de alto risco epistêmico ({len(r['high_churn_articles'])}):")
        for item in r["high_churn_articles"]:
            print(f"  {item['article']}: {', '.join(item['flags'])}")
    else:
        print("\nNenhum artigo em estado de alto risco.")

    print(f"{'=' * 55}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Métricas do sistema de manutenção epistêmica"
    )
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument(
        "--save", action="store_true", help="Salva em outputs/state/patch-metrics.yaml"
    )
    args = parser.parse_args()

    health = load_yaml(HEALTH_FILE)
    queue_data = load_yaml(QUEUE_FILE)

    metrics = compute_metrics(health, queue_data)

    if args.json:
        print(json.dumps(metrics, indent=2, ensure_ascii=False))
    else:
        print_report(metrics)

    if args.save:
        with open(METRICS_FILE, "w") as f:
            yaml.dump(metrics, f, allow_unicode=True, sort_keys=False)
        print(f"Salvo: {METRICS_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
