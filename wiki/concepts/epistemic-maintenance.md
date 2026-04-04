---
title: "Epistemic Maintenance for LLM Wikis"
sources:
  - path: raw/articles/epistemic-maintenance.md
    type: article
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [meta-kb, epistemic-quality, protocols, curation, maintenance]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: source
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-04
quarantine: true
quarantine_created: 2026-04-04
quarantine_reason: "3 unsourced claims: (1) LLMs better at adversarial than neutral review, (2) temporal gap mechanism independent of duration, (3) CI/CD analogy applied to epistemic quality without empirical basis"
quarantine_promoted: null
quarantine_criteria_met:
  tempo: false
  review_frio: false
  adversarial_or_scout_or_prediction: false
---

## Resumo

Companion ao padrão LLM Wiki: descreve como preservar qualidade epistêmica à medida que o wiki cresce. Identifica três failure modes (viés de curadoria, over-synthesis, review auto-confirmatório) e seis protocolos correspondentes. Todos os seis protocolos descritos já estão implementados nesta KB — com uma exceção parcial: epistemic lint como operação computável não existe ainda.

## Conteúdo

### Os três failure modes

**Viés de curadoria**: o curador seleciona fontes que confirmam suas crenças porque são mais fáceis de encontrar e mais satisfatórias de ler. O wiki cresce mais detalhado e mais confiante numa direção determinada pelos priors iniciais.

**Over-synthesis**: o LLM conecta pontos que as fontes não conectam. Cada inferência individualmente plausível; nenhuma em nenhuma fonte específica; juntas constroem uma estrutura sem fundação. Claims over-synthesized leem como insights — são os mais prováveis de estar errados.

**Review auto-confirmatório**: o LLM revisando uma página que ele mesmo escreveu a encontra coerente, bem suportada, largamente precisa — porque está avaliando seu próprio output com o mesmo modelo interno que o produziu. Captura erros de superfície. Não captura os vieses sistemáticos que introduziu ao escrever.

Os três compõem: curadoria enviesada → claims over-synthesized → review confirma. Resultado: o wiki reflete o worldview do compilador de volta com a autoridade de uma referência bem mantida.

### Os seis protocolos

**1. Curadoria adversarial (1 in 5 sources challenging)**

Toda 5ª fonte ingerida deve challenger, contrariar, ou complicar os claims existentes do wiki. Threshold: 20% challenging.

**2. Proveniência de claims**

Cada claim no wiki é rastreável a uma fonte específica. Claims que são síntese cross-paper — e não estão em nenhuma fonte individual — são marcados explicitamente como tais.

**3. Separação temporal (review frio)**

O review de um artigo acontece em sessão diferente da que o escreveu. O LLM lendo seu próprio trabalho sem o material original disponível é um ato cognitivo diferente de revisar o que acabou de escrever.

**4. Quarentena na criação**

Artigos especulativos começam isolados — não podem ser linkados por outros artigos até critérios de promoção serem satisfeitos.

**5. Challenge passes**

Pedir ao LLM que argumente contra páginas específicas, não apenas que as revise. Forçar construção de contraargumento é estruturalmente diferente de revisar para consistência.

**6. Epistemic lint**

Varredura periódica que reporta: % de claims sem rastreabilidade a fonte, % de synthesis claims marcados vs. não marcados, ratio de fontes confirming/challenging/neutral ao longo do tempo.

### A metáfora CI/CD

O documento propõe: wiki = codebase, claims = functions, protocols = test suite.

⚠️ Analogia interpretativa — não equivalente à ontologia formal já implementada na KB.

A ontologia formal (`formal-ontology-for-kbs.md`) cobre ESTRUTURA: o que existe no wiki e como se relaciona (continuants, occurrents, typed wikilinks). A metáfora CI/CD cobre QUALIDADE: se o que está no wiki é epistemicamente confiável. São layers complementares, não sobrepostos. Ontologia = tipagem. Epistemic maintenance = validação.

## Instruções especiais: análise de implementação

### Protocolo a protocolo: o que já existe na KB

| Protocolo do documento | Equivalente na KB | Status |
|------------------------|------------------|--------|
| Curadoria adversarial (1 in 5) | Adversarial quota no /ingest; `stance` tracking em _registry.md | ✅ implementado |
| Claim provenance | ⚠️ marking convention; seções Conteúdo vs. Interpretação; campos `source_quality` + `interpretation_confidence` | ✅ implementado |
| Separação temporal | Critério 2 do /promote (`review_frio`: log em sessão diferente) | ✅ implementado |
| Quarentena na criação | Sistema de quarentena com 3 critérios de promoção | ✅ implementado |
| Challenge passes | Comando `/challenge` | ✅ implementado |
| Epistemic lint | _registry.md tem os dados (stances, datas). Nenhum comando computa as métricas como operação | ⚠️ parcial — dados existem, operação não |

### O que o documento propõe que a KB ainda não tem

**Epistemic lint como operação computável.** O documento descreve lint que surfaça: (a) % de claims sem trace a fonte, (b) % de synthesis claims marcados vs não marcados, (c) evolução do stance ratio ao longo do tempo.

A KB tem os dados para (c) — _registry.md tem stances por data. Não tem operação para (a) nem (b). Uma implementação mínima de (c) seria possível agora com o grep de stances por período.

**Calibração por contexto.** O documento propõe decidir explicitamente quais protocolos aplicar baseado nas stakes (pessoal vs. research vs. profissional). A KB aplica todos os protocolos uniformemente. Para um usuário que começa uma KB menor, saber que pode começar só com (1) e (2) antes de implementar quarentena reduz o custo de entrada.

### Stance ratio atual da KB (verificado em _registry.md)

| Stance | Fontes | % corpus |
|--------|--------|---------|
| confirming | 14 | 16% |
| challenging | 25 | 29% |
| neutral | 48 | 55% |
| **Total** | **87** | **100%** |

O threshold "1 in 5" do documento (20% challenging) está sendo superado: 29% > 20%. O threshold interno da KB (25% mínimo) também está sendo superado.

**Nota de distribuição**: a contagem é sobre o corpus total. Por sessão, a distribuição varia. Sessão 2026-04-03 (ingestão inicial AI/ML): alta proporção confirming. Sessão 2026-04-04 (ingestão lateral): 3/12 = 25% challenging. Um epistemic lint real calcularia o trailing ratio das últimas N fontes, não o acumulado.

### Relação com ontologia formal (formal-ontology-for-kbs.md)

A metáfora "wiki is a codebase, claims are functions, protocols are test suite" mapeia como:
- articles → continuants (entidades persistentes)
- claims → occurrents (eventos/processos, instâncias de assertar algo)
- protocols → constraints sobre occurrents (regras de quando um claim pode existir sem quarentena)

Mas a ontologia formal cobre TIPOS (o que as coisas são). A metáfora CI/CD cobre QUALIDADE (se o que existe é válido). São dimensões ortogonais. Ontologia bem-formada + claims epistemicamente ruins = possível. Claims epistemicamente sólidos sem ontologia tipada = também possível.

⚠️ A integração natural seria: usar os tipos ontológicos (claim como occurrent) como unit of testing na epistemic lint. Isso não está implementado e seria uma extensão não trivial.

## Verificação adversarial

**Claims não sourced no documento original:**
1. "The LLM is better at adversarial analysis than at neutral review" — assertado como fato; nenhuma fonte primária citada
2. "The temporal gap is the mechanism; the duration matters less than the break" — design claim sem validação empírica
3. A analogia CI/CD aplicada a epistemic quality — produtiva mas sem evidência de que "claims are like functions" operacionalmente

**O que o documento NÃO resolve:**
- Como medir "% de claims não rastreáveis" em wikis existentes sem auditoria manual
- Se o threshold "1 in 5" é empiricamente derivado ou arbitrário (o documento não cita fonte para o número)
- Como detectar over-synthesis automaticamente (sem comparar artigo com raw/ claim by claim)

**Prior work que o documento não menciona:** autonomous-kb-failure-modes.md (esta KB) documenta os mesmos failure modes com mais detalhe e evidência. O documento epistemic-maintenance é uma articulação pública mais limpa, não uma descoberta nova.

## Quality Gate

- [x] Wikilinks tipados: 4 (implementedBy ×5 implicados via seção de análise, contradicts, complements, partOf)
- [x] Conteúdo vs. Interpretação: failure modes e protocolos em Conteúdo; análise de metáfora em Interpretação
- [x] Meta-KB separado: análise de implementação em seção dedicada
- [x] Resumo calibrado: "todos os seis protocolos já implementados — com uma exceção parcial"

## Conexões

- implementedBy: [[curation-anti-bias]] ON "adversarial sourcing + claim provenance"
- implementedBy: [[autonomous-kb-failure-modes]] ON "os três failure modes documentados com evidência"
- implementedBy: [[requisite-variety]] ON "review auto-confirmatório = V(self-eval) = V(self), zero bits adicionais"
- complementsAt: [[formal-ontology-for-kbs]] ON "ontologia = tipagem estrutural; epistemic maintenance = validação de qualidade — dimensões ortogonais"
- partOf: [[kb-architecture-patterns]] ON "epistemic maintenance é a camada de qualidade que Pattern 1 não descreve"
- gaps: [[question-taxonomy]] ON "epistemic lint como operação não implementada — question taxonomy poderia guiar quais perguntas o lint faz"

## Fontes

- [Epistemic Maintenance for LLM Wikis](../../raw/articles/epistemic-maintenance.md) — três failure modes, seis protocolos, metáfora CI/CD. Fonte primária: este documento. Análise de implementação na KB = nosso trabalho.

> ⚠️ QUARENTENA: 3 unsourced claims no documento fonte. Critérios pendentes: tempo (24h), review frio, adversarial/scout/predição.
