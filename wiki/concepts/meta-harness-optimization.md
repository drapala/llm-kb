---
title: "Meta-Harness: Otimização Automática de Harnesses"
sources:
  - path: raw/papers/meta-harness-lee-2026.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-06
updated: 2026-04-06
tags: [harness-engineering, meta-optimization, automated-engineering, agent-architecture]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
quarantine: false
quarantine_promoted: 2026-04-06
quarantine_criteria_met:
  auto_promote: false
  gates_passed: [1, 2, 3]
  gate3_run: 2026-04-06
  gate3_models: [gpt-5.4, gemini-3.1-pro-preview]
  challenge_verdict: PRECISA_CORREÇÃO
  corrections_applied: true
  promoted_by: manual_promote
---

## Resumo

Meta-Harness é um sistema de outer-loop que busca automaticamente harnesses otimizados para aplicações LLM usando um coding agent com acesso irrestrito ao histórico completo de candidatos (código + scores + traces de execução) via filesystem. Supera harnesses hand-engineered em classificação de texto (+7.7 pts), raciocínio matemático (+4.7 pts IMO-level) e coding agentico (#1 TerminalBench-2 com Haiku 4.5).

## Conteúdo

### Problema

A performance de sistemas LLM depende não só dos pesos do modelo, mas do harness: o código que determina o que armazenar, recuperar e apresentar ao modelo. Harness engineering permanece majoritariamente manual apesar de sua importância.

**Por que métodos de text optimization existentes falham para harness engineering:**

| Método | Limitação |
|--------|-----------|
| OPRO | Apenas pares (solução, score) — sem traces |
| TextGrad | Feedback textual só sobre candidato atual |
| AlphaEvolve | Program database + eval scores, sem traces |
| GEPA | Feedback reflexivo de traces, comprimido em summary |
| Feedback Descent | Comparação + feedback textual, summary |
| TTT-Discover | Fragment de solução anterior (window) |

A maioria condiciona em feedback comprimido — summaries, scalars ou fragmentos de solução. AlphaEvolve mantém um program database, mas sem traces de execução detalhados; métodos window retêm fragmentos crus mas sem histórico de scores cruzado com código. Um harness age em horizontes longos: uma decisão sobre o que armazenar pode afetar comportamento muitos steps depois. Feedback comprimido torna o rastreamento de falhas até decisões anteriores do harness mais difícil — não necessariamente impossível, mas estruturalmente desfavorável. (Lee et al., 2026)

**Escala de contexto por passo de otimização:**
- Prior methods: 100–30,000 tokens por passo de otimização (estimativas do paper, Tabela 1)
- Meta-Harness: até 10,000,000 tokens de informação diagnóstica disponível por avaliação — 2.5 a 5 ordens de magnitude a mais dependendo do baseline de comparação (comparação "per evaluation" vs "per optimization step" não é diretamente apples-to-apples)

### Design do Meta-Harness

**Loop principal (Algorithm 1):**
```
Input: tasks X, LLM M, proposer P, iterations N
Inicializa filesystem D ← ∅
Para cada harness H inicial: avalia e armazena em D
Para t = 1..N:
  Proposer P consulta filesystem D
  Proposer P propõe k harnesses novos
  Avalia harnesses válidos e armazena em D
Retorna Pareto frontier de harnesses em D
```

**Acesso via filesystem, não prompt monolítico:**
- Cada candidato avaliado contribui um diretório: source code + scores + execution traces
- O filesystem cresce além da context window do proposer
- Proposer consulta via terminal tools (grep, cat) — lê mediana de 82 arquivos por iteração, referencia 20+ candidatos anteriores por step
- Proposer decide O QUE inspecionar (emergente, não hard-coded)

**Por que código-espaço:** harnesses como programas proveem viés de regularização natural — coding models tendem a propor algoritmos coerentes em vez de soluções brittle hardcoded.

**Implementação prática:**
- Proposer: Claude Code (Opus 4.6)
- Cada harness: programa Python single-file que modifica prompting, retrieval, memory e orchestration logic
- Modelo base M: frozen (varia por domínio)
- Run típico: ~60 harnesses ao longo de 20 iterações
- Tornou-se prático "por volta do início de 2026" com melhorias em coding agents (Lee et al., 2026)

### Resultados

**Classificação de texto online** (GPT-OSS-120B como classificador, datasets USPTO, S2D, Law):

| Harness | Avg Accuracy | Context tokens adicionais |
|---------|-------------|--------------------------|
| Zero-shot | 36.7% | 0 |
| ACE (state-of-art hand-designed) | 40.9% | 50.8k |
| Meta-Harness | 48.6% | 11.4k |

Meta-Harness: +7.7 pontos vs. ACE usando 4× menos tokens de contexto.

**Raciocínio matemático** (retrieval-augmented, 200 problemas IMO-level, 5 modelos held-out):
- Um único harness descoberto: +4.7 pontos médios através de 5 modelos held-out — evidência inicial de transferabilidade (generalização cross-model dentro de domínio matemático; não testada cross-domain)

**Coding agêntico (TerminalBench-2):**

| Harness | Pass Rate |
|---------|-----------|
| Meta-Harness (ours) | **37.6%** |
| Goose | 35.5% |
| Terminus-KIRA | 33.7% |
| Mini-SWE-Agent | 29.8% |
| ClaudeCode baseline | 27.5% |

#1 entre todos os agentes Haiku 4.5 reportados.

**Matchup com text optimizers (classificação de texto):**
- Meta-Harness atinge performance do próximo melhor método após apenas 4 avaliações (vs. 60 de OpenEvolve/TTT-Discover)

### Relacionamento com meta-learning

(⚠️ nossa interpretação) Meta-Harness aplica ideias de credit assignment e meta-learning no nível do harness externo, não nos pesos do modelo. Em vez de atualizar pesos, atribui crédito a nível de harness: usa experiência de rollouts passados para raciocinar sobre quais steps e componentes são responsáveis por falhas, depois reescreve o código externo que governa comportamento futuro.

## Verificação adversarial

**Claim mais fraco:** cross-model generalization em math reasoning — "um único harness descoberto melhora 4.7 pontos médios em 5 modelos held-out." Atraente, mas baseado em 200 problemas IMO-level; sem evidência de generalização além de domínio matemático.

**O que o paper NÃO diz:**
- Não avalia Meta-Harness em tarefas onde o harness descoberto não generaliza para modelos diferentes
- Não analisa falhas do proposer: quando o sistema converge para harnesses subótimos
- Não discute custo computacional total de busca vs. ganho incremental por iteração

**Simplificações feitas:**
- "Tornou-se prático por volta do início de 2026" é observação do paper, não análise sistemática de quando coding agents atingiram capacidade necessária
- Pareto frontier como critério de seleção final é descrito mas não avaliado em termos de trade-offs práticos de deployment

**Prior work central:** Zhang et al. (ACE/TTT-Discover), OpenEvolve, TextGrad, OPRO como baselines diretos — todos superados em classificação de texto.

## Aplicação à KB

(⚠️ nossa interpretação) O loop Meta-Harness — propor, avaliar, armazenar histórico completo, usar filesystem como feedback channel — é estruturalmente análogo ao que esta KB faz com /challenge + /ask + log de sessões: cada ciclo produz traces que alimentam iteração futura. A diferença: Meta-Harness automatiza a proposta de novo harness; nossa KB mantém humano no loop para proposta.

## Quality Gate
- [x] Wikilinks tipados: 3 substituições realizadas
- [x] Instance→class: claims numéricos qualificados com modelo+dataset+condição
- [x] Meta-KB separado: referências a esta KB em ## Aplicação à KB
- [x] Resumo calibrado: mantido — inclui resultados específicos sem overgeneralizar

## Conexões

- complementsAt: [[natural-language-agent-harness]] — Pan formaliza O QUE é um harness; Lee automatiza COMO buscá-lo — dois papéis distintos, mesmo objeto
- emerge-para: [[prometheus-as-nlah-substrate]] ON "filesystem de histórico como canal de feedback para proposer"
- derivedFrom: [[self-improving-agents]] — Meta-Harness é instância de sistema self-improving, mas no nível de código externo, não pesos
- complementsAt: [[context-management]] — harness optimization decide o que armazenar/recuperar/apresentar — é meta-context-management
- validates: [[autoresearch-programme-vitality]] ON "ciclos de feedback com histórico completo produzem predições mais ricas que feedback comprimido"

## Fontes

- [Meta-Harness (Lee et al., 2026)](../../raw/papers/meta-harness-lee-2026.pdf) — sistema de outer-loop, design do proposer, resultados em classificação, math reasoning e agentic coding

