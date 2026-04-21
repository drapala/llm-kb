# Index — Debt Behind the AI Boom

<!-- Sub-índice criado: 2026-04-11 -->
<!-- Foco: dívida técnica gerada e amplificada por sistemas AI/LLM -->
<!-- Fontes: 10 (5 empíricos Tier 1, 5 revisões Tier 2) -->
<!-- Artigos wiki: 3 (1 promovido, 2 em quarentena aguardando fix) -->

## Artigos Wiki

- [AI-Generated Code Debt — Evidência Empírica](concepts/ai-generated-code-debt-empirical.md) — **PROMOTED** · 5 estudos (2025-26): survival 24.2%, GIST, Type-4 clones, 45.1% PRs requerem revisão
- [AI Productivity Paradox e Comprehension Debt](concepts/ai-productivity-paradox.md) — **QUARANTINED** · METR -19%→-4%, gap 39pp, Osmani comprehension debt -17% compreensão
- [AI Technical Debt — Taxonomia e Framework Conceitual](concepts/ai-technical-debt-taxonomy.md) — **QUARANTINED** · Sculley 2015 → Recupito 2024 → Moreschini 2026 · prompt debt, explainability debt
- [SafeKV — Selective KV-Cache Sharing + RDR](concepts/safekv-selective-kv-cache-isolation.md) — **QUARANTINED** · scout E39 · Chu 2025 · três-tier detection + radix-tree + Reuse Diversity Ratio; 40,58% TTFT reduction vs full isolation
- [SMTA + Burn-After-Use para LLM Empresarial](concepts/smta-burn-after-use-enterprise-llm.md) — **QUARANTINED** · scout E39 · Zhang 2026 · 127 iter, SMTA 92% / BAU 76,75%; 4 métricas LRPR/RRPR/IFER/BTPR
- [FedDCA — Cross-Client Domain Coverage é Pivotal](concepts/feddca-cross-client-domain-coverage.md) — **QUARANTINED** · scout E39 · Wang 2024 · coverage > heterogeneity; +29,19% perf, +4,82–21,36% coverage; 11 baselines
- [Uni-CTR — Seesaw Phenomenon em Multi-Domain LLM](concepts/uni-ctr-multidomain-seesaw.md) — **QUARANTINED** · deep-research E39 · Fu 2025 ACM TOIS · ladder + masked loss; AUC 0.7523/0.7569/0.7246; +6pts zero-shot; +10.26% industrial
- [LLM-RecG — Semantic Bias em Shared-Layer](concepts/llm-recg-semantic-bias-shared-layer.md) — **QUARANTINED** · deep-research E39 · Li 2025 RecSys · inter-domain compactness + intra-domain diversity; +28.9% NDCG@10; ablation VG R@10 35.81→28.26
- [Participation Gap — Generalization em FL](concepts/federated-learning-participation-gap.md) — **QUARANTINED** · deep-research E39 · Yuan 2022 ICLR · out-of-sample gap vs participation gap; 20% held-out clients; diversity sweep

## Fontes Raw — Tier 1 (Empírico)

- [Liu et al. 2026](../raw/papers/liu-2026-debt-behind-ai-boom.md) — arXiv:2603.28592 · 304K commits, 5 tools, taxa de sobrevivência de issues
- [Ox Security 2025](../raw/articles/ox-security-2025-army-of-juniors.md) — 300 repos, 10 anti-patterns, "insecure by dumbness"
- [Mujahid et al. 2026](../raw/papers/mujahid-2026-todo-fix-gemini.md) — arXiv:2601.07786 · GIST, 81/6540 comentários, 3 padrões de dívida admitida
- [Huang et al. 2026](../raw/papers/huang-2026-more-code-less-reuse.md) — arXiv:2601.21276 · Type-4 clones, Max Redundancy Score
- [Watanabe et al. 2025](../raw/papers/watanabe-2025-agentic-coding-prs.md) — arXiv:2509.14745 · 567 Claude Code PRs, 83.8% merge, 45.1% necessitam revisão

## Fontes Raw — Tier 2 (Revisões e Framework)

- [METR 2025](../raw/papers/metr-2025-ai-developer-productivity.md) — arXiv:2507.09089 · RCT -19%→-4%, gap percepção 39pp
- [Osmani 2026](../raw/articles/osmani-2026-comprehension-debt.md) — comprehension debt, Anthropic RCT N=52, inversão dinâmica de review
- [Moreschini et al. 2026](../raw/papers/moreschini-2026-evolution-tech-debt-genai.md) — JSS 2026 · 61 fontes, prompt debt, explainability debt
- [Recupito & Palomba 2024](../raw/papers/recupito-palomba-2024-ai-tech-debt.md) — JSS 2024 · 53 practitioners, paradoxo prevalência/severidade
- [Sculley et al. 2015](../raw/papers/sculley-2015-hidden-tech-debt-ml.md) — NeurIPS 2015 · fundacional · glue code, CACE, pipeline jungles
