---
title: "SHACL vs OWL — Validação vs Inferência em Knowledge Graphs"
sources:
  - path: raw/papers/ruckhaus-2025-shacl-owl-kcap.md
    type: paper
    quality: primary
    stance: confirming
created: 2026-04-11
updated: 2026-04-11
tags: [SHACL, OWL, knowledge-graphs, validation, inference, open-world-assumption, closed-world-assumption, compliance]
source_quality: medium
interpretation_confidence: high
resolved_patches: []
provenance: source
status: quarantined
quarantine_date: 2026-04-11
quarantine_reason: "Gate 3 invalidou: 'SHACL não deriva novo conhecimento' — SHACL Advanced Features / SHACL Rules permitem derivar novos triplos (W3C spec, unanimidade). Fixes aplicados: SHACL Core vs SHACL-AF distinguidos; OWL 'tecnicamente incorreto' → 'não recomendado'; OWL detecta inconsistências (não só infere)."
---

## Resumo
Ruckhaus et al. (KCap 2025) estabelece a distinção operacional entre OWL e SHACL: toda validação de dados em knowledge graphs deve ser implementada em SHACL (Closed World Assumption), enquanto modelagem de domínio e inferência pertencem a OWL (Open World Assumption). A incompatibilidade semântica entre os dois é fundamental — não uma limitação de implementação.

## Conteúdo

### A Distinção Fundamental

**OWL — Open World Assumption (OWA):**
- Modela domínio: classes, propriedades, axiomas de subsunção
- Inferências: raciocinar sobre novo conhecimento implícito
- Constraint OWL → produz **novas inferências** ou detecta inconsistências lógicas (não "violações" no sentido SHACL)
- Exemplo: `domain(hasSupplier, Company)` em OWL inferirá que qualquer entidade com `hasSupplier` é uma `Company` — mesmo que você quisesse dizer "isso é inválido"

**SHACL — primariamente validação (com extensões de inferência):**
- Valida dados: shapes, constraints, regras de negócio
- SHACL Core: constraint SHACL → produz **violações** (erros de validação)
- Na validação, opera contra o grafo fornecido (comportamento de mundo fechado para presença de dados)
- Nota: SHACL Advanced Features (SHACL Rules) permitem derivar novos triplos — SHACL Core e SHACL-AF têm propósitos distintos
- Exemplo: `sh:minCount 1` em SHACL Core flaggará entidades sem o campo

**Incompatibilidade semântica (SHACL Core vs OWL):**
A mesma constraint tem comportamentos diferentes nos dois formalismos. OWL não tem semântica nativa de "isso é uma violação" — quando uma constraint OWL é "violada", o reasoner infere novo conhecimento ou detecta inconsistência lógica. Para a maioria dos casos de validação de dados, SHACL Core é a tecnologia recomendada (não OWL). Nota: OWL pode ser usado para verificação de qualidade via consistência lógica, mas não reporta violações no estilo SHACL.

### Shape Templates Identificados (Ruckhaus 2025)

Padrões reutilizáveis para desenvolvimento combinado:
- Validação de propriedades datatype/object
- Validação de taxonomias (class membership)
- Grupos de regras de negócio reutilizáveis como shapes

### Aplicação em Domínios Regulatórios

O paper foi aplicado em **RINF (Register of Infrastructure)** da Agência Ferroviária da UE — um domínio com requirements formais de conformidade. Padrão de uso:
1. OWL define a ontologia do domínio (o que os conceitos são, como se relacionam)
2. SHACL valida se os dados reais satisfazem os constraints do domínio
3. Reasoner OWL infere novo conhecimento; validator SHACL detecta violações

### Quando Usar Cada Um

| Necessidade | Tecnologia Correta |
|---|---|
| "Entidade X deve ter campo Y" | SHACL (`sh:minCount`, `sh:datatype`) |
| "Todo Z que tem W implica que Z é subclasse de V" | OWL (class restrictions) |
| "Valor de Y deve ser > 10000" | SHACL (`sh:minExclusive`) |
| "hasSupplier é transitivo" | OWL (transitive property) |
| "Contrato do tipo A deve ter campo auditoria" | SHACL (shape por tipo) |
| "Contratação Integrada é subclasse de Modalidade" | OWL (class hierarchy) |

### Limitações do Desenvolvimento Combinado

- Ferramentas de conversão OWL→SHACL geram artefatos difíceis de manter
- Diferentes engines SHACL têm suporte heterogêneo para componentes avançados
- Propagação de mudanças entre os dois artefatos é custosa sem tooling adequado

## Verificação adversarial

**Claim mais fraco:** STUB baseado em abstract — os shape templates específicos e os detalhes de implementação do RINF não foram verificados.

**O que o paper não diz:** (1) benchmark de performance SHACL vs. reasoner OWL; (2) como lidar com casos onde você precisa das duas semânticas simultaneamente no mesmo domínio.

**Prior work:** OWL e SHACL têm literaturas extensas separadas; este paper é relevante por endereçar o desenvolvimento *combinado* — que é o caso real na maioria dos sistemas.

## Quality Gate
- [x] Wikilinks tipados: sem wikilinks externos — artigo novo
- [x] Instance→class: OWA/CWA distinção atribuída a Ruckhaus 2025; sem estatísticas a qualificar
- [x] Meta-KB separado: sem referências ao KB no Conteúdo
- [x] Resumo calibrado: source_quality medium (1 primary, STUB)

## Conexões
- neurosymbolic-ai-knowledge-graphs partOf shacl-owl-knowledge-graphs (OWL como camada de governança — distinção SHACL faltava no artigo base)

## Fontes
- [Ruckhaus et al. 2025](../../raw/papers/ruckhaus-2025-shacl-owl-kcap.md) — distinção OWL/SHACL, shape templates, aplicação em domínio regulatório (STUB — KCap 2025)
