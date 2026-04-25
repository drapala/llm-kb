# Index — Domínios Laterais

<!-- ~21 artigos: ecologia, economia comportamental, neurociência, filosofia da ciência, finanças pessoais, platform engineering -->
<!-- Viveiro: artigos com ≤3 citações. Regra: ≥4 citações → graduar para sub-índice funcional -->
<!-- PAC-Bayes aqui por ser fundações matemáticas sem vínculo direto com KB/agents ainda -->
<!-- Cluster platform-eng (2026-04-25): DORA + CNCF + supply-chain — ingerido p/ challenge externo, candidato a sub-índice se crescer -->

## Platform Engineering / DevEx (cluster 2026-04)

- [DORA 2025 — AI as Platform Amplifier](concepts/dora-2025-ai-as-amplifier.md) — AI amplifica plataforma boa OU má; "shift down complexity into the platform"; 90% das orgs com IDP, 76% com platform team
- [DORA Metrics — Evolution 4→5](concepts/dora-metrics-history-evolution.md) — 5 métricas (2024): Throughput (lead time, freq, recovery time) vs Instability (change fail rate, deployment rework rate). MTTR renomeado em 2023
- [CNCF Platform Engineering Maturity Model](concepts/cncf-platform-engineering-maturity-model.md) — 5 aspectos (Investment/Adoption/Interfaces/Operations/Measurement) × 4 níveis (Provisional→Operational→Scalable→Optimizing). Auto-aware de Goodhart
- [GitHub Artifact Attestations + SLSA](concepts/github-artifact-attestations.md) — provenance assinada via Sigstore; SLSA L2 default, L3 com reusable workflows. Princípio: gerar ≠ verificar; só verify cria valor


- [Stigmergic Coordination (Grassé)](concepts/stigmergic-coordination.md) — KB = stigmergic system: wiki is environment, wikilinks are pheromones. Observado: /ingest sem conexões → /ask descobriu espontaneamente
- [Complexity and Emergence (Waldrop)](concepts/complexity-emergence.md) — VOCABULARY: emergence, edge of chaos, fitness landscape, path dependence. May (1972) âncora os claims. KB drifting toward order-death
- [Predictive Processing (Friston)](concepts/predictive-processing.md) — Supersedes "LLM as amplifier": prediction error minimizer. Self-assessment = convergence to minimum surprise. Suportado por Tulving+McClelland
- [Complexity-Stability Tradeoff](concepts/complexity-stability-tradeoff.md) — May (1972): σ√(nC) < 1 para estabilidade. Complexidade aleatória → instabilidade. Contra-intuitivo; modularidade necessária
- [Resource Competition and Coexistence](concepts/resource-competition-coexistence.md) — Tilman (1994): modelos espaciais com trade-off colonização-competição permitem coexistência ilimitada. Resolve paradoxo de exclusão competitiva
- [Heuristics and Biases](concepts/heuristics-and-biases.md) — K&T (1974): 3 heurísticas (representatividade, disponibilidade, ancoragem) → vieses sistemáticos previsíveis. Atalhos adaptativos com zonas de falha
- [Prospect Theory](concepts/prospect-theory.md) — K&T (1979): valor sobre ganhos/perdas, não riqueza final. Loss aversion (λ≈2). Certainty effect, reflection effect. ~80k citações
- [Zipf's Law and Power Laws in Language](concepts/zipf-law-power-laws.md) — Ferrer-i-Cancho (2003): Zipf emerge na transição de fase λ*≈0.41. Piantadosi (2014): nenhuma teoria explica tudo ainda
- [Falsificationism and Demarcation](concepts/falsificationism-demarcation.md) — Popper (1963): ciência = falsificável, não verificável. Einstein > Freud/Adler: risco epistêmico. Confirmações fáceis valem pouco
- [Scientific Research Programmes](concepts/scientific-research-programmes.md) — Lakatos (1970): hard core + protective belt + heurísticas. Progressivo (novas predições) vs. degenerativo (só acomoda)
- [Episodic and Semantic Memory](concepts/episodic-semantic-memory.md) — Tulving (2002): episódica = autonoética, temporal, 1ª pessoa; semântica = noética, atemporal. Hipocampo crítico. Mental time travel
- [Complementary Learning Systems](concepts/complementary-learning-systems.md) — McClelland (1995): catastrophic interference → dois sistemas. Hipocampo (rápido/esparso) + neocórtex (lento/distribuído). Replay = consolidação sistêmica
- [PAC-Bayes Bounds](concepts/pac-bayes-bounds.md) — E[R(θ)]≤E[r(θ)]+√(KL(ρ||π)/n). Prior/posterior on predictors. First non-vacuous bounds on NNs (Dziugaite 2017). Ensemble generalization framework
- [Acoplamento Estrutural — Maturana](concepts/structural-coupling-maturana.md) — ⚠️ EMERGIDO L0 (sem raw/). Perturbação recíproca sem controle. Critério de saúde: remove KB, pensa melhor? Candidato para ingest de Tree of Knowledge
- [Lem — Summa Technologiae](concepts/lem-summa-technologiae.md) — ⏳QUARANTINED. Autoevolução, fantomática, ariadnologia, intellectrônica. Ariadnologia = instintos artificiais. Lem como linhagem filosófica da KB
- [Two-Sigma Problem](concepts/two-sigma-problem.md) — ⏳QUARANTINED. Bloom 1984: tutoria 1:1 = +2σ vs sala de aula. Meta-análises: efeito real (d≈0.79) mas 2σ não replicado em condições gerais. Mecanismo: feedback+teste+remediação
- [Aristocratic Tutoring — History](concepts/aristocratic-tutoring-history.md) — Oxford/Cambridge = tutoria pura no século XVII (Newton). 8 ingredientes de Hoel. Mass education substituiu por escala, não por superioridade pedagógica. O'Malley: infância moderna = construção burguesa sec. XVIII
- [Parenting as Environment Design](concepts/parenting-as-environment-design.md) — ⏳QUARANTINED. Gopnik: carpenter vs. gardener. Overimitation: crianças copiam métodos ineficientes de adultos (aprendizado social > eficiência). Infância longa = R&D evolutivo
- [Play — Neuroscience](concepts/play-neuroscience.md) — ⏳QUARANTINED. Brown: jogo é necessidade biológica análoga ao sono. 6.000 histórias de vida. Ratos privados de jogo → rigidez comportamental. Rebound de jogo como homeostase
- [Adverse Childhood Experiences](concepts/adverse-childhood-experiences.md) — ⏳QUARANTINED. Felitti 1998 (N=9.508): ACE score dose-response. Score 4+: até 12x suicídio, 46x drogas injetáveis. Mecanismo: toxic stress → HPA → neurotoxicidade cortisol → epigenética intergeracional
- [Self-Directed Learning](concepts/self-directed-learning.md) — ⏳QUARANTINED. Gray: instinto evolutivo para aprender via jogo. Sudbury Valley: 75% ensino superior, viés de seleção reconhecido. Hunter-gatherer: menos formal, não sem instrução. two-sigma contradicts
- [Statistical Arbitrage & Pairs Trading](concepts/statistical-arbitrage-pairs-trading.md) — Cointegração + RL/DRL. DQN: 18.39% anual Sharpe 2.43. Copula supera cointegração pura. RL pairs: 9.94–31.53% anual dependendo do agente
- [Copula Dependency Modeling](concepts/copula-dependency-modeling.md) — Modela dependência não-linear entre pares cointegrados. Outperforms correlação linear em crypto pairs trading. 3 famílias: Gaussian, Clayton, Gumbel
- [Cryptocurrency Perpetual Futures & Funding Rate Arbitrage](concepts/cryptocurrency-perpetual-futures-funding-rate.md) — Delta-neutral arb: até 115.9% em 6 meses, risco -1.92%. Apenas 40% das oportunidades positivas após custos. CEX domina price discovery 61% sobre DEX
- [Deep Learning Statistical Arbitrage](concepts/deep-learning-statistical-arbitrage.md) — DL supera PCA/PLS em 1.4–4.1% Sharpe anual. Redes LSTM + transformer para latent factor extraction. Generalization gap: overfitting em regimes voláteis
- [Robust Stat-Arb DNN (Regime-Robust)](concepts/robust-stat-arb-dnn-regime.md) — ⚠️ CHALLENGING. DNN model-free lucrativa em crises e quando cointegração colapsa. 50 dimensões. Não requer pares cointegrados estáveis. Contraria premissa de fragilidade de stat-arb em regime change
- [HMM Stat-Arb Regime-Switching (Crude Oil)](concepts/hmm-stat-arb-regime-switching.md) — ⚠️ CHALLENGING. HMM + estimador online adaptativo. Cobre COVID 2020 e crise energética Rússia-Ucrânia 2022. Lucrativo em crises quando cointegração estática falha
- [Market-Neutral Pairs Trading Crypto (Bull/Bear)](concepts/market-neutral-pairs-crypto-bull-bear.md) — ⚠️ CHALLENGING. OTT + otimização bi-objetivo. Testado jan 2021 – jan 2023: bull run + colapso LUNA + bear market 2022. 15.49% anual market-neutral. 3x menos trades em bear vs. bull
- [Epistemic Dependency Copula](concepts/epistemic-dependency-copula.md) — ⚠️ EMERGIDO. Wikilinks tipados = cointegração epistêmica (declarada). Co-ativações sem wikilink = fat tails invisíveis. CMI como proxy de staleness de pares antes do sinal individual
- [Safe Withdrawal Rate (Regra dos 4%)](concepts/safe-withdrawal-rate.md) — Bengen 1994: 4% derivada de dados EUA 1926–1992. Pfau 2010: segura em apenas 4/17 países desenvolvidos. Metodologia: rolling histórico + Monte Carlo
- [Taxa de Retirada Segura no Brasil](concepts/taxa-retirada-segura-brasil.md) — Perlin & Pereira 2023 (FGV): 5% sustentável para renda fixa. AA40: SafeMax 8.48% (30 anos), Monte Carlo 95% → 3.7–4.5%. Juros reais altos invertem lógica de renda variável
