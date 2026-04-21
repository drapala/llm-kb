---
title: "OutputArtifact Institucional — Família de Artefatos Auditáveis para Investigação B2G"
sources:
  - path: raw/articles/tcu-referencial-combate-fraude.md
    type: article
    quality: primary
    stance: neutral
  - path: wiki/concepts/zelox-mvp-laudo-aditivos.md
    type: synthesis
    quality: primary
    stance: confirming
  - path: wiki/concepts/audit-risk-rent-extraction.md
    type: synthesis
    quality: primary
    stance: confirming
created: 2026-04-12
updated: 2026-04-12
tags: [output-artifact, laudo, memo, referral, decisao-auditavel, compliance, tcu, cgu, coaf, mpf, agu, proof-carrying, b2g, produto, institutional]
source_quality: medium
interpretation_confidence: medium
resolved_patches: []
provenance: synthesis
synthesis_sources:
  - wiki/concepts/zelox-mvp-laudo-aditivos.md
  - wiki/concepts/audit-risk-rent-extraction.md
  - wiki/concepts/audit-deterrence-corruption.md
status: promoted
promoted_date: 2026-04-12
freshness_status: current
---

## Resumo

Um sistema de investigação de fraude que produz apenas scores não é suficiente para uso institucional. Órgãos públicos, escritórios de advocacia, controladorias e o próprio TCU operam com **artefatos documentais formais** — laudo, memo técnico, referral e decisão auditável — que têm requisitos de estrutura, rastreabilidade e citação legal específicos. A família de `OutputArtifact` é o que transforma o output técnico do sistema (score, path explanation, evidências) em instrumento operável dentro do fluxo institucional do cliente. Sem ela, o produto permanece uma engine forte que exige outro produto à frente para virar ação.

## Conteúdo

### O Gap: Score vs. Instrumento Institucional

O fluxo institucional de combate a fraude e corrupção no Brasil segue um ciclo de 5 fases (TCU Referencial, 2ª ed.):

```
Prevenção → Detecção → Investigação → Responsabilização → Monitoramento
```

Um sistema de scoring cobre **Detecção** (geração do alerta). Para virar produto dentro da operação do cliente, o sistema precisa também cobrir **Investigação** (estruturação da evidência) e habilitar **Responsabilização** (produção do artefato formal que aciona instâncias superiores).

O artefato de output é a ponte entre detecção automatizada e responsabilização institucional.

### Tipologia de OutputArtifacts

**1. Laudo Técnico**

Documento que certifica um padrão detectado com base em dados verificáveis e metodologia explícita. Usado para:
- Subsidiar representações ao TCU (quem aciona: escritório de advocacia, auditor, cidadão)
- Embasar processos administrativos internos (quem usa: controladoria interna, CGU)
- Instruir inquéritos (quem usa: MPF, delegacias especializadas)

Estrutura mínima de um laudo defensável:
```
1. Identificação do objeto (CNPJ, contrato, período)
2. Metodologia (fonte de dados, cálculos, thresholds aplicados)
3. Achados (evidências com citação de fonte primária)
4. Referência legal (artigo violado ou indício de violação)
5. Conclusão (qual irregularidade foi identificada, com grau de certeza declarado)
6. Limitações (o que o laudo não cobre ou não pode afirmar)
```

**Critério de defensabilidade:** o laudo precisa ser reproduzível — terceiro com acesso às mesmas fontes chega ao mesmo resultado. Isso significa que cálculos derivados de dados públicos (ex: aditivo_teto via PNCP) são mais defensáveis que scores de ML com features proprietárias não explicáveis.

**2. Memo Técnico**

Documento de comunicação interna (ou entre instâncias) que sintetiza um achado e recomenda ação. Menos formal que o laudo — não precisa ter metodologia completa — mas mais acionável: tem destinatário específico, recomendação explícita e prazo esperado de resposta.

Usado para:
- Comunicação entre gestor público e controladoria interna
- Briefing para tomador de decisão que não leu o laudo completo
- Registro interno de decisão de arquivamento ou prosseguimento

Estrutura mínima:
```
1. Para: [destinatário com cargo]
2. Assunto: [identificação do caso]
3. Síntese do achado (1 parágrafo)
4. Recomendação (arquivar / aprofundar / acionar instância X)
5. Prazo sugerido para resposta
6. Referência ao laudo completo (se existir)
```

**3. Referral / Encaminhamento Institucional**

Documento que aciona formalmente uma instância superior ou especializada. É o artefato que materializa a escalada do caso:

| Origem | Destino | Instrumento legal |
|--------|---------|------------------|
| Órgão público | CGU | Comunicação de irregularidade (Lei 12.527/2011) |
| Qualquer cidadão / empresa | TCU | Representação (Art. 113, Lei 8.666; Art. 169, Lei 14.133) |
| Órgão público / cidadão | MPF/PGR | Notícia-crime (CPP Art. 27) |
| Banco / fintech | COAF | Comunicação de operação suspeita (Resolução COAF) |
| Agente público | CGU | Denúncia (Lei 12.846/2013 + Portaria CGU 1.089/2018) |

O referral precisa conter: identificação do denunciante/comunicante, identificação do investigado, descrição do fato com evidências, base legal, e — quando aplicável — solicitação de medida cautelar (ex: suspensão de pagamento).

**4. Decisão Auditável**

Registro estruturado de decisão tomada por analista humano dentro do sistema, com todos os elementos que a tornam contestável e reversível:

```
- Decisão: [arquivar / aprofundar / emitir laudo / acionar instância]
- Analista: [id + cargo]
- Timestamp: [ISO 8601]
- Evidências consideradas: [lista de fontes com versão/data]
- Justificativa: [texto livre, min. 50 palavras]
- Score do modelo no momento: [valor + versão do modelo]
- Override?: [sim/não — se decisão diverge do score do modelo]
- Revisão programada: [data ou condição]
```

A decisão auditável é o primitivo que viabiliza accountability interna: se o órgão for questionado por ter arquivado um caso que depois se revelou fraude, o registro da decisão mostra quem decidiu, com base em quê, e se havia alerta do sistema sendo ignorado (override com justificativa).

### Proof-Carrying Risk: Estrutura de Evidência Rastreável

O conceito de proof-carrying risk descreve um score ou alerta que carrega consigo a cadeia de evidências que o gerou — não apenas o número final, mas o caminho de inferência verificável. Isso é crítico para uso institucional porque:

1. **Contestabilidade:** o fornecedor investigado tem direito ao contraditório. Sem o caminho de inferência, a defesa pode questionar a origem do score.
2. **Admissibilidade:** o TCU exige que representações sejam instruídas com evidências verificáveis. Score opaco não é evidência; laudo com citação de fonte primária (PNCP, Diário Oficial) é.
3. **Responsabilização do analista:** a decisão auditável precisa referenciar as evidências consideradas — impossível sem o path de inferência registrado.

Estrutura do proof-carrying risk para um alerta B2G:
```
alerta_id: ZLX-2026-00123
entidade: CNPJ 12.345.678/0001-99
score: 0.84 (modelo v1.1)
features_top3:
  - aditivo_teto: 0.23 (fonte: PNCP contrato_id=X, aditivo_id=Y)
  - co_participacao_watchlist: true (fonte: CEIS item_id=Z)
  - socios_em_comum_cnpj_bloqueado: 2 (fonte: RFB consulta 2026-04-10)
base_legal_indicada: Art. 125 Lei 14.133/2021; Art. 7º Lei 12.846/2013
```

### Mapeamento para Fluxo Institucional Brasileiro

```
Zelox detecta padrão (score + features)
       ↓
Analista investiga (Case + Task no sistema)
       ↓
Analista decide (Decisão Auditável registrada)
       ↓
   ┌───────────────────────────────────────┐
   │ Se irregularidade confirmada:         │
   │   → Gerar Laudo Técnico               │
   │   → Gerar Memo para gestor interno   │
   │   → Acionar Referral para TCU/CGU/MPF│
   └───────────────────────────────────────┘
       ↓
Instância receptora processa (outcome externo)
       ↓
Zelox registra Outcome (fecha loop de aprendizado)
```

### Por que o Laudo Precisa Ser Visível ao Fornecedor

Olken (2007) e Zamboni & Litschig (2018): o mecanismo de deterrência opera ex-ante — fornecedores que sabem que estão sendo monitorados reduzem irregularidades *antes* de serem auditados. Isso implica que laudos e alertas que chegam ao conhecimento do fornecedor têm efeito dissuasório além do caso investigado.

Implicação de design: o sistema que produz laudos formais e os usa em representações ao TCU cria sinal público de que o monitoring está ativo. Isso amplifica o impacto além dos casos diretamente processados.

## Interpretação

⚠️ Interpretação do compilador.

**Implicação direta para Zelox:** O sistema hoje expõe `packet` (evidência factual) mas não tem uma família de OutputArtifact. O próximo passo não é mais evidência — é a interface de produção de laudo, memo, referral e decisão auditável. Essas quatro peças fecham o gap entre "engine que detecta" e "sistema encaixado no dia a dia do órgão/equipe".

**Prioridade de implementação:**
1. Decisão Auditável — primeiro porque habilita o loop de aprendizado (override registry)
2. Laudo Técnico — segundo porque é o MVP pagável (escritório de advocacia, controladoria)
3. Referral — terceiro porque depende do laudo como instrução
4. Memo — pode ser gerado automaticamente como resumo do laudo

**Relação com proof-carrying risk:** o `packet` atual já tem parte das features necessárias para o laudo. O que falta é o template de estrutura legal + a interface de geração que respeita os requisitos de forma do TCU/CGU.

**Caveat de mercado:** os requisitos de forma do TCU evoluem. O laudo que é suficiente hoje para admissão de representação pode não ser suficiente amanhã. O sistema precisa ter o template de laudo como configuração versionada, não hardcoded.

## Verificação adversarial

**Claim mais fraco:** "o referral precisa conter X" — os requisitos formais de cada tipo de encaminhamento variam por instrumento legal e por instruções normativas específicas de cada órgão. A estrutura aqui é derivada de práticas comuns, não de uma norma única unificada. Cada tipo de referral pode ter requisitos adicionais não cobertos.

**O que não está aqui:** como o sistema lida com sigilo — laudos em casos sigilosos (inquéritos policiais, investigações em andamento) têm restrições de divulgação que limitam o proof-carrying público. Não há referência primária sobre como NICE Actimize ou Palantir resolvem isso em contexto B2G brasileiro.

## Quality Gate
- [x] Instance→class: estruturas de laudo/memo/referral são padrões derivados, não normas únicas citáveis
- [x] Meta-KB separado: implicações para Zelox em Interpretação
- [x] Resumo calibrado: source_quality medium (síntese de documentação institucional + corpus existente)

## Conexões
- output-artifact-institutional relates-to fraud-case-management-lifecycle ON "OutputArtifact é o output da fase Decision+Action do ciclo case management"
- output-artifact-institutional relates-to zelox-mvp-laudo-aditivos ON "laudo de aditivos é instância específica do tipo Laudo Técnico desta família"
- output-artifact-institutional relates-to audit-deterrence-corruption ON "laudo visível ao fornecedor = mecanismo de deterrência ex-ante de Olken"
- output-artifact-institutional relates-to audit-risk-rent-extraction ON "laudo instrui representação TCU = aumenta audit risk percebido = reduz irregularidades (Zamboni & Litschig)"
- output-artifact-institutional relates-to fraud-system-operational-telemetry ON "decisão auditável = primitivo do override_registry que viabiliza o flywheel de dados"

## Fontes
- TCU — Referencial de Combate a Fraude e Corrupção, 2ª edição (portal.tcu.gov.br, 2024)
- CGU — Portaria 1.089/2018: estruturação de programas de integridade
- Lei 12.846/2013 — Lei Anticorrupção brasileira (acordos de leniência, responsabilização administrativa)
- Lei 14.133/2021 — Nova Lei de Licitações (Art. 125: thresholds de aditivo)
- [[zelox-mvp-laudo-aditivos]] — laudo de aditivos como MVP pagável
- [[audit-deterrence-corruption]] — deterrência ex-ante via monitoramento visível
- [[audit-risk-rent-extraction]] — Zamboni & Litschig: impacto de audit risk em procurement municipal
