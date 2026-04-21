---
title: "File-as-Bus Workspace"
sources:
  - path: raw/papers/chen-2026-aiscientist-long-horizon-ml-engineering.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-14
updated: 2026-04-14
tags: [multi-agent, coordination, state-management, long-horizon, autonomous-agents]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
freshness_status: current
pending_patch_count: 0
topics: [multi-agent-coordination, durable-state, workspace-design, thin-control, orchestration]
---

## Resumo

File-as-Bus (Chen et al., 2026) é um protocolo de coordenação multi-agente onde o workspace de arquivos é o substrato de estado — não handoffs conversacionais. Agentes se re-ancoram em artefatos duráveis (análises, código, logs de experimentos) em vez de herdar contexto de predecessores. Princípio: **thin control over thick state**. Ablação empírica: remover File-as-Bus custa −31.82 Any Medal% (MLE-Bench Lite) e −6.41 pts (PaperBench).

## Conteúdo

### Problema que resolve

Em sistemas multi-agente de longa duração, o estado do projeto tipicamente é transmitido via handoffs conversacionais: o agente B recebe um resumo do que o agente A fez, comprimido em tokens. Esse mecanismo tem dois problemas:

1. **Perda de fidelidade:** compressão em resumo elimina detalhes técnicos (falhas de execução, configurações exatas, resultados parciais) que podem ser críticos para decisões futuras
2. **Dependência de contexto acumulado:** conforme o projeto avança, o contexto crescente necessário para raciocinar coerentemente supera o contexto ativo disponível

File-as-Bus resolve substituindo handoffs conversacionais por **artefatos duráveis em disco**: cada agente re-entra no estado atual do workspace, lê artefatos relevantes sob demanda, e escreve de volta seus outputs.

### Princípio: Thin Control over Thick State

```
Thin = interface de controle
  - Orchestrator carrega: stage-level summaries + workspace map (índice compacto)
  - Decisões de controle operam sobre m_t = M(W_t), não sobre W_t inteiro

Thick = estado externalizado
  - Análises de paper, planos, código, logs, resultados
  - Persistem em disco independente de qual agente está ativo
  - Qualquer agente pode re-ancorar lendo artefatos relevantes
```

O orchestrator *pode* ler artefatos específicos quando necessário, mas não precisa carregar o workspace inteiro no contexto ativo para decisões rotineiras de controle.

### Estrutura do Workspace

Três regiões por responsabilidade:

| Região | Conteúdo |
|--------|----------|
| `paper_analysis/` | Compreensão estruturada do paper, métricas alvo, ambiguidades, detalhes de implementação |
| `submission/` | Repositório executável: código, config, setup scripts, `reproduce.sh` |
| `agent/` | Artefatos de planejamento e execução: `prioritized_task.md`, `plan.md`, `impl_log.md`, `exp_log.md` |
| `agent/experiments/` | Outputs detalhados de cada execução |

**Permission-scoped:** cada Tier-1 especialista tem write access apenas às regiões de sua responsabilidade. Logs compartilhados são append-only e estruturados por iteração.

### Progressive Disclosure

O orchestrator não lê o workspace inteiro — usa o **workspace map** como interface de navegação:

```
m_t = M(W_t)   # índice textual leve das regiões e seus papéis
```

Agentes começam pelo map, leem artefatos relevantes à tarefa sob demanda, e escrevem de volta outputs duráveis. Isso desacopla temporalmente o progresso de qualquer instância de agente específica.

### Ciclo Evidência-Driven

Padrão dominante: implement → run → diagnose → patch → re-validate

```
exp_log.md  →  diagnóstico de falha  →  impl_log.md  →  novo run
```

Cada rodada deixa artefatos que rodadas futuras podem inspecionar, verificar e construir. Progresso é **cumulativo**, não episódico.

### Resultados Empíricos (AiScientist, Chen et al. 2026)

**PaperBench** (replicação from-scratch de papers ML):
- AiScientist: 33.73 avg score vs baseline humano ~41%
- Ganho sobre melhor baseline (IterativeAgent): +11.15 pts
- Custo: $12.20/tarefa vs $54.90 (IterativeAgent)

**MLE-Bench Lite** (otimização competition-style):
- AiScientist: 81.82% Any Medal% (Gemini-3-Flash e GLM-5)
- Exemplo: "Detecting Insults" — 74 ciclos de experimento em 23h, AUC 0.903→0.982

**Ablação File-as-Bus:**

| Benchmark | Sem File-as-Bus | Com File-as-Bus | Δ |
|-----------|----------------|----------------|---|
| PaperBench avg score | ~27 | 33.73 | **−6.41** |
| MLE-Bench Lite Any Medal% | ~50 | 81.82 | **−31.82** |

**Padrão crítico:** a perda se concentra em métricas de refinamento tardio (Silver, Gold, Any Medal), não em estabelecer submissões iniciais válidas (Bronze/Valid Submission quase inalterados). File-as-Bus habilita progresso *cumulativo* em múltiplas rodadas, não setup inicial.

Takeaway dos autores: "More interaction alone is not enough; additional rounds help only when they build on prior progress."

### Comparação com Abordagens Anteriores

| Sistema | Mecanismo de estado | Horizon |
|---------|-------------------|---------|
| BasicAgent | Contexto conversacional | Curta |
| IterativeAgent | Contexto conversacional + iteração | Média |
| **AiScientist** | **File-as-Bus (artefatos duráveis)** | **Longa** |

IterativeAgent adiciona mais rodadas que BasicAgent mas permanece significativamente abaixo do AiScientist — validando que o mecanismo (estado durável) importa, não apenas a quantidade de iterações.

## Interpretação

(⚠️ nossa interpretação) O princípio File-as-Bus é estruturalmente análogo ao design desta KB: `raw/` é estado durável (thick state), os comandos `/ingest`, `/ask`, `/challenge` são thin control. A diferença é que no AiScientist o estado é atualizado por agentes especializados; nesta KB o estado é atualizado pelo compilador humano-assistido. O princípio de coordenação é o mesmo: o agente seguinte não herda o raciocínio do agente anterior — herda os artefatos.

(⚠️ nossa interpretação) "Permission-scoped workspace" tem análogo nos sub-índices desta KB (`_index-agents.md`, `_index-econ-poli.md`): cada domínio tem escopo de escrita separado, reduzindo interferência cross-domínio. Não é idêntico mas o princípio de isolamento de regiões é compartilhado.

(⚠️ nossa interpretação) O padrão ablação (File-as-Bus importa mais para refinamento tardio do que para setup inicial) tem implicação para KB: fontes simples de lookup (um artigo, um conceito direto) podem funcionar sem estado durável; sínteses cross-paper e emergências requerem acesso a artefatos de sessões anteriores. Sugere que `/dream` (consolidação de memória entre sessões) é o análogo funcional do File-as-Bus neste sistema.

## Verificação adversarial

**Claim mais fraco:** "81.82 Any Medal% exceeds all leaderboard results" — comparison is not fully controlled. Leaderboard results use different models, budgets, and evaluation dates. The controlled comparison (AIDE, ML-Master 2.0, LoongFlow) shows +4.55 pts, which is more defensible than the leaderboard comparison.

**O que o paper NÃO diz:**
1. Não mede o custo de manter o workspace de artefatos (disco, tempo de leitura) como parte do orçamento de tempo de 24h
2. Não testa ablação de hierarquia isolada de File-as-Bus — os dois mecanismos são testados separadamente mas a interação entre eles não é isolada
3. Não avalia degradação do File-as-Bus em tarefas onde os artefatos são muito grandes para serem lidos eficientemente (ex: repos com milhões de linhas)

**Simplificações:** o paper não discute como o workspace map (índice compacto) é mantido atualizado. Se o map ficar desatualizado em relação ao estado real do workspace, o thin control opera sobre informação incorreta — failure mode não abordado.

**Prior work:** o paper cita CAMEL, MetaGPT, ChatDev como trabalhos anteriores em coordenação multi-agente, mas não cita trabalhos específicos em file-based state management para agentes (ex: MemGPT). File-as-Bus parece contribuição de design nova neste contexto de ML research engineering.

## Conexões

- instancia: [[kb-architecture-patterns]] — "thin CLI + fat skills" é instância do princípio "thin control over thick state" de File-as-Bus
- validates: [[autoresearch-reliability-triad]] — durable artifact state = Pilar 1 (grounded oracle) aplicado a nível de workspace, não apenas a experimentos individuais
- partOf: [[ai-scientist-autonomous-research]] — File-as-Bus é o mecanismo central do AiScientist 2026
- contradicts: [[agent-memory-architectures]] — "artefatos em disco como memória primária" diverge de abordagens baseadas em memória vetorial ou episódica como mecanismo principal de continuidade

## Fontes

- [Chen et al. 2026 — AiScientist](../../raw/papers/chen-2026-aiscientist-long-horizon-ml-engineering.md) — File-as-Bus protocol, ablações, benchmarks PaperBench/MLE-Bench Lite

## Quality Gate

- [x] Wikilinks tipados: 4 relações (instanceOf ×1, confirms ×1, partOf ×1, contradicts ×1)
- [x] Instance→class: percentuais qualificados por benchmark e condição (Gemini-3-Flash/GLM-5, controlled eval)
- [x] Meta-KB separado: referências ao design desta KB em ## Interpretação com ⚠️
- [x] Resumo calibrado: limita claim a "AiScientist, Chen et al. 2026, dois benchmarks"
