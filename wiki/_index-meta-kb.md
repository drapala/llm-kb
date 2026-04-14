# Index — Meta-KB

<!-- ~29 artigos: failure modes, curation, variety, epistemics, ontology, protocols -->
<!-- Cluster mais denso — hub autonomous-kb-failure-modes promovido ✅ -->

- [LLM Knowledge Base](concepts/llm-knowledge-base.md) — Core loop: raw/→wiki/→ask. Practitioner-described. Risks: AI-compiled content degrades RAG, model collapse
- [KB Architecture Patterns](concepts/kb-architecture-patterns.md) — 4 patterns + cross-cutting retrieval constraint. Pattern 4 (GBrain): SQLite+FTS5+vector, "thin CLI + fat skills"
- [Epistemic KB Benchmark Protocol](concepts/epistemic-kb-benchmark-protocol.md) — ⏳QUARANTINED. 2 eixos: calibração (ECE/Brier) + degradação temporal (30 dias, Stage B). Falsificadores H1/H2/H3
- [Tension Resolution](concepts/tension-resolution.md) — 5 mechanisms from papers inform design: grounded verification, self-enhancement risk, heuristic resolution, dynamic criteria
- [Groupthink and Cascades](concepts/groupthink-and-cascades.md) — RE-DISCOVERIES: semantic convergence = groupthink (Janis 1972), authority cascade = information cascade (Banerjee 1992)
- [Autonomous KB Failure Modes](concepts/autonomous-kb-failure-modes.md) — 4 silent failures (convergence, authority cascade, bloat, tension). Stage B empiricamente confirmado. Layer 3 Circularity
- [Curse of Knowledge — LLM Judge Bias](concepts/curse-of-knowledge-llm-judge.md) — ComplexEval: richer eval context → reference-anchoring bias. Refines Layer 3 Circularity mechanism
- [Evaluation Order Independence](concepts/evaluation-order-independence.md) — ⚠️ EMERGIDO. Reference-anchoring = L3 Pearl impossibility → única solução: sequestrar referência até julgamento independente
- [Knowledge Collapse in LLMs](concepts/knowledge-collapse-llm.md) — Stage B: fluency intact, facts degrading, metrics green. Domain-specific raw/ delays collapse 15×
- [Raw/ Design Constraints](concepts/raw-design-constraints.md) — ⚠️ EMERGIDO. Dois constraints independentes: diversidade tópica (CLS) + primazia de fontes (KC). Failure mode composto
- [Curation Anti-Bias](concepts/curation-anti-bias.md) — HOW TO FIX IT: 3 bias layers + 5 improvements. Adversarial quota, split confidence, style check, multiagent spot-check
- [Question Taxonomy](concepts/question-taxonomy.md) — 7 frameworks (Miles, Socratic, Oblique, Popper, Lakatos, AHRQ, Simon). 10 question types + stopping rule
- [Fast-and-Frugal Heuristics (Gigerenzer)](concepts/fast-frugal-heuristics.md) — EXPLAINS "compression > raw": bias-variance trade-off. Less-is-more in small samples. PREDICTS reversal at scale (500+ articles)
- [Requisite Variety (Ashby)](concepts/requisite-variety.md) — "Only variety can destroy variety." V(compiler) < V(domain) → irreducible error floor. All 5 failure modes = 1 cause
- [Causal Reasoning (Pearl)](concepts/causal-reasoning-pearl.md) — CAUSAL LEVELS: association/intervention/contrafactual. KB has 8 L1, 5 L2, 0 L3 claims
- [Formal Ontology for KBs](concepts/formal-ontology-for-kbs.md) — STRUCTURAL GAPS: untyped wikilinks, no hierarchy, no competency questions. 5 typed relations, adoption path
- [Variety Gap Analysis](concepts/variety-gap-analysis.md) — ⚠️ ESPECULATIVO. Gap V(compiler)/V(domain) por dimensão. Gap Beer/VSM preenchido. Gap Shannon parcialmente preenchido
- [Bibliometrics](concepts/bibliometrics.md) — Pritchard 1969: "application of math/stats to books and media." Utility-tracker = bibliometrics da KB (⚠️ interpretação)
- [Bradford's Law of Scattering](concepts/bradford-law-scattering.md) — Bradford 1934: zonas 1:n:n², rendimento decrescente. Proxy para V gap por domínio (⚠️ interpretação)
- [Epistemic Maintenance](concepts/epistemic-maintenance.md) — ⏳QUARANTINED. 3 failure modes (curation bias, over-synthesis, self-confirming review) + 6 protocols. Gap: epistemic lint computável
- [Modular Escape Principle](concepts/modular-escape-principle.md) — ⚠️ EMERGIDO. May+JudgmentAggregation+Bradford compartilham escape: especialização com interface mínima. L2. Em quarentena
- [Autoresearch Reliability Triad](concepts/autoresearch-reliability-triad.md) — ⚠️ EMERGIDO. Três pilares: grounded test + anti-cascade structure + stopping criterion. Sem um dos três → confirmação > 80%
- [Autoresearch Programme Vitality](concepts/autoresearch-programme-vitality.md) — ⚠️ EMERGIDO. Triad (sessão) + Lakatos (programa): hard core vs protective belt. confirming_ratio > 0.8 = diagnóstico degenerativo
- [Sequential Hypothesis Testing (SPRT)](concepts/sequential-hypothesis-testing.md) — Wald (1945): stopping rule ótima. Sₙ ≥ b → confirma; Sₙ ≤ a → rejeita. Formaliza Pilar 3 do autoresearch-reliability-triad
- [Autonomous Emergence Pipeline Risks](concepts/autonomous-emergence-pipeline-risks.md) — ⏳QUARANTINED. EMERGIDO. /emerge→/ask→/challenge sem humano: oracle co-gerador viola Systematicity; falso positivo composto
- [Challenge Protocol — REFINA Sub-tipos](concepts/challenge-protocol.md) — ⏳QUARANTINED. Taxonomia REFINA: marginal/empírica/scope/causal. Gap: stopping criterion para chains incrementais
- [Anti-padrões Epistêmicos em Sistemas ML](concepts/anti-patterns-epistemic-ml.md) — EMERGIDO. Taxonomia de 5 anti-padrões: circular ground truth, Goodhart×fraude, proxy drift, audit trail selection bias, threshold gaming. #2 e #5 críticos para Zelox produto
- [Circularidade de Ground Truth em Sistemas ML](concepts/circular-ground-truth-ml-systems.md) — EMERGIDO. Anti-padrão #1 detalhado. Labels de A não são ground truth para B que substitui A. Teste: concordância >90% = circular
- [Neurosymbolic AI for KBs](concepts/neurosymbolic-ai-for-kbs.md) — ⏳QUARANTINED. Luong (2026): FAOS 3-layer ontology constrainge inputs do agente LLM. Inverse parametric knowledge effect
- [Upper Ontology for Epistemic KBs](concepts/upper-ontology-for-kbs.md) — ⏳QUARANTINED. Síntese: BFO/DOLCE × Hindsight 4 redes. Hierarquia Entity→KnowledgeArtifact→Claim→VerifiedClaim/EmergentClaim
- [Meta-Ontologia do metaxon](concepts/meta-ontology-metaxon.md) — ⏳QUARANTINED. BFO upper ontology + domain hierarchy (KnowledgeArtifact/Claim/DisturbanceEvent) + pipeline mapping. ontology/core.py como invariante
- [Espectro Ontológico e McOntology](concepts/mconto-ontology-spectrum.md) — Lista→Schema→Taxonomia→Ontologia: inferência como propriedade definidora. McOntology (Seale): nome errado → falha atribuída à ferramenta. core.py é schema+hierarquia, não ontologia inferencial
- [LLM Strategic Bias — Trendslop](concepts/llm-strategic-bias-trendslop.md) — HBR 2026: LLMs preferem diferenciação/augmentação/longo-prazo independente de contexto. <2% de melhoria com prompting. 7 modelos, 15k+ testes
