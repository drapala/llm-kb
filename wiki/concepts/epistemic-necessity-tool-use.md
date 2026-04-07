---
title: "Epistemic Necessity como Critério para Uso de Ferramentas em Agentes"
sources:
  - path: raw/papers/epistemic-necessity-tool-use.md
    type: paper
    quality: secondary
    stance: confirming
created: 2026-04-07
updated: 2026-04-07
tags: [tool-use, epistemic-calibration, agent-design, uncertainty, metacognition]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
quarantine: true
quarantine_reason: "Fonte secundária (síntese paramétrica + PDF real, 13 páginas, Edinburgh/CUHK/UIUC/Northwestern/Princeton). Claims verificados via texto completo. Aguarda challenge protocol."
---

## Resumo

Wang et al. (2026, ICML submetido) propõem epistemic necessity como critério normativo para decisão de uso de ferramentas externas por agentes LLM. Introduzem a Theory of Agent (ToA): ferramenta externa é justificada se e somente se a incerteza restante não pode ser resolvida via raciocínio interno. Failure modes comuns (overthinking e overacting) são reinterpretados como falhas de decisão sob incerteza epistêmica, não falhas de raciocínio ou execução isoladas.

## Conteúdo

### Definição central

**Epistemic necessity**: uma tarefa não pode ser completada de forma confiável via raciocínio interno do agente sobre seu contexto atual, sem qualquer interação externa.

Corolário: uso de ferramenta é justificado **se e somente se** a incerteza restante para completar a tarefa não pode ser resolvida internamente.

### Theory of Agent (ToA)

Framework que modela agentes como tomadores de decisões sequenciais sobre como alocar esforço epistêmico:
- **Raciocinar** (resolver incerteza internamente)
- **Agir** (delegar resolução a ferramenta/ambiente externo)

Ambos são tratados como formas de uso de ferramenta para aquisição de conhecimento — unificando reasoning e acting sob o mesmo framework de decisão.

### Failure modes reinterpretados

- **Overthinking**: raciocínio interno excessivo quando interação externa seria mais eficiente — decisão miscalibrada sob incerteza
- **Overacting**: delegação externa excessiva quando raciocínio interno seria suficiente — decisão miscalibrada sob incerteza

Ambos emergem de calibração epistêmica incorreta, não de déficits de raciocínio ou execução.

### Long-term consequence: trajetória da inteligência

O argumento mais forte do paper (Figure 1): dois agentes podem atingir task success comparável via alocações diferentes de esforço epistêmico.

- Agente A (over-delegating): invoca ferramentas mesmo quando raciocínio interno é suficiente → raciocínio interno não é exercitado → capacidade estagna
- Agente B (epistemically calibrated): invoca ferramentas apenas quando necessário → raciocínio interno é exercitado → capacidade se expande com a experiência

"Unnecessary delegation reshapes not just efficiency, but the trajectory of agent intelligence itself."

### Contra o paradigma dominante

Frameworks existentes (ReAct, Toolformer) otimizam para task success ou reward, tratando tool use como ação ordinária e "shortcut gratuito". Isso permite overuse de ferramentas enquanto as respostas são corretas, sem penalizar a degradação de capacidade interna.

### Implicações para design e treinamento

- Agentes precisam de mecanismos de self-assessment epistêmico antes de decidir invocar ferramentas
- Custo de invocação não é apenas latência/tokens — é custo epistêmico de não exercitar raciocínio interno
- Avaliação de agentes deve medir calibração epistêmica, não apenas task success

## Interpretação

(⚠️ nossa interpretação) O critério de epistemic necessity é análogo ao ResolutionPolicy em `ontology/core.py`: antes de emitir um DisturbanceEvent (invocar intervenção externa), o sistema deve verificar se a incerteza é genuinamente irresolvível internamente. O ToA formaliza essa intuição como critério normativo derivado de fundamentos epistêmicos, não apenas como heurística de custo.

(⚠️ nossa interpretação) O argumento de "trajetória da inteligência" tem implicação para o design da KB: o /ask deve ser exercitado sobre o corpus interno antes de recorrer a oracle externo — não como otimização de custo, mas porque bypassing o raciocínio interno impede que a KB desenvolva connections que só emergem do processamento interno (como as conexões de /emerge).

(⚠️ nossa interpretação) O reframing de overthinking/overacting como falhas de calibração epistêmica é relevante para o canal algedônico: sinais de dor não devem disparar por custo de tokens, mas por miscalibração epistêmica — o agente invocar /ask quando já tem a resposta, ou não invocar quando genuinamente não sabe.

## Conexões

- [[meta-ontology-llm-kb]] — ResolutionPolicy em ontology/core.py é instância do critério de epistemic necessity
- [[autonomous-kb-failure-modes]] — overacting como failure mode se mapeia para authority cascade; overthinking para bloat
- [[self-improving-agents]] — trajetória da inteligência via exercício interno ressoa com Reflexion (raciocínio verbal) vs. delegação prematura
- [[epistemic-maintenance]] — calibração epistêmica contínua é o mecanismo subjacente ao critério
- [[llm-as-judge]] — juízes LLM que delegam internamente sem verificação = overthinking institucionalizado

## Fontes

- [Wang et al. 2026](../../raw/papers/epistemic-necessity-tool-use.md) — Theory of Agent (ToA); epistemic necessity; overthinking/overacting como miscalibração; trajetória da inteligência
