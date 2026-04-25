# SGCR: A Specification-Grounded Framework for Trustworthy LLM Code Review

**Autores:** Kai Wang, Bingcheng Mao, Shuai Jia, Yujie Ding, Dongming Han, Tianyi Ma, Bin Cao
**Instituição:** HiThink Research
**Publicação:** arXiv:2512.17540 [cs.SE]
**Ano:** 2025 (dezembro)
**URL:** https://arxiv.org/abs/2512.17540
**Tipo:** paper / primary

---

## Metodologia

- Deployment em produção em Java na HiThink Research
- **140 regras Java** curadas por developers experientes
- **200 participantes** no estudo comparativo
- Métrica principal: adoption rate (% de sugestões aceitas e implementadas)
- Modelo base: 32B-parameter LLM privado + embedding model para RAG

## Arquitetura

### Dual-pathway

**Path 1 — Explicit Specification Injection:**
- Regras humanas passadas explicitamente ao LLM
- Ensemble de N instâncias LLM em paralelo → cada uma revisa contra as specs
- Aggregator LLM sintetiza resultados divergentes
- Para specs longas: divide em chunks, processa em paralelo, sintetiza → resolve atenção diluída
- Output: `R_explicit`

**Path 2 — Implicit Specification Discovery:**
- LLM proposer revisa código SEM acesso às specs (unconstrained)
- Gera hipóteses de issues (`Q_hypo`)
- Para cada hipótese: embedding → busca semântica em vector DB de specs → recupera specs relevantes
- Verifier ensemble confirma/rejeita cada hipótese contra specs recuperadas
- Output: `R_implicit`

**Agregação final:**
- De-duplicação entre R_explicit e R_implicit
- Priorização por severidade (specs marcadas com metadado de severidade)
- Opcionalmente: gera code patches guiados pelas specs

### Inovação em atenção diluída

Quando spec set é muito longa: divide em chunks → processa em paralelo → sintetiza. Garante que cada regra receba atenção adequada.

## Achados principais

### Adoption rate

| Configuração | Adoption Rate |
|-------------|---------------|
| SGCR (Full) | **42%** |
| Explicit-Only | 37% |
| Implicit-Only | 29% |
| Baseline LLM | 22% |

**Melhoria relativa: +90.9% sobre baseline.**

### Contribuição de cada componente

- Explicit path é o mais impactante (22% → 37%)
- Implicit path adiciona "safety net" para issues não cobertas pelas specs (37% → 42%)
- Os dois caminhos são complementares: explicit = disciplined, implicit = discovery-oriented

### Qualitative developer feedback

- **Enhanced trust:** sugestões ligadas a regras humanas explícitas, não black-box
- **Reduced noise:** foco em issues relevantes ao projeto específico
- **Educational value:** aprendizado just-in-time de best practices para devs júniores

## Comparação com topologia de codebase

SGCR não usa topologia — usa specs. Specs são mais interpretáveis para developers, mais controláveis, mais determinísticas na path explícita. Tradeoff: manutenção da spec library (overhead apontado pelos developers).

## Limitações

- Apenas Java / HiThink Research (generalização incerta)
- Manutenção da spec library é overhead contínuo
- 140 regras pode ser insuficiente para projetos sem documentação de regras

## Ligação com outros papers

- Resolve diretamente os problemas de Cihan 2024 (faulty reviews, irrelevant comments)
- Alinha com SWE-PRBench 2026: evita atenção diluída via chunk-based processing
- Adoption rate 42% supera BitsAI-CR (26.7% outdated rate / 75% precision)
