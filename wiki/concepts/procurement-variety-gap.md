---
title: "Procurement Variety Gap — Lei de Licitações como Regulação de Variedade (Ashby × Bajari-Tadelis)"
sources:
  - path: wiki/concepts/procurement-contract-design.md
    type: synthesis
    quality: primary
  - path: wiki/concepts/requisite-variety.md
    type: synthesis
    quality: primary
  - path: raw/lei/lei-14133-2021-artigos-chave.md
    type: article
    quality: primary
    stance: neutral
  - path: raw/lei/tcu-manual-licitacoes-contratos-5ed-2024.md
    type: article
    quality: primary
    stance: confirming
created: 2026-04-04
updated: 2026-04-05
tags: [procurement, ashby, variety, brasil, lei-14133, lei-8666, b2g, zelox, regulatory-design, contratacao-integrada]
source_quality: high
interpretation_confidence: medium
resolved_patches:
  - date: 2026-04-04
    fix: "Referências de artigos corrigidas: contratação integrada = Art. 46, inciso V (não §1,I); semi-integrada = inciso VI; matriz de risco = Art. 22 (não Art. 103)"
  - date: 2026-04-04
    fix: "Contrato de eficiência: escopo corrigido — especificamente 'proporcionar economia ao contratante' (Art. 6, LIII), não 'qualquer método para outcome'"
  - date: 2026-04-04
    fix: "Mecanismo de segunda ordem CONFIRMADO empiricamente: anteprojeto obrigatório de 10 elementos (TCU) codifica a superespecificação. 'Aditamentos ilegais quando baseados em erros do anteprojeto' (jurisprudência TCU) — confirma que error floor é estruturalmente menor sob contratação integrada"
reads: 1
retrievals_correct: 1
retrievals_gap: 0
last_read: 2026-04-04
quarantine: false
quarantine_created: 2026-04-04
quarantine_reason: "Artigo emergido de /ask cross-domain (b2g × sistemas). Gap crítico: Lei 14.133 e TCU Manual não estavam em raw/."
quarantine_promoted: 2026-04-04
quarantine_criteria_met:
  tempo: "override_by_user — ingestão de raw/ da Lei 14.133 substituiu espera de 24h"
  review_frio: "override_by_user — verificação via ingestão legal é equivalente"
  adversarial_or_scout_or_prediction: "Predição L2 falsificável formulada E verificação parcial de claims legais concluída (Arts. 6, 22, 46, 125 verificados em raw/lei/lei-14133-2021-artigos-chave.md). 3 patches aplicados — 0 refutações, 3 refinamentos."
provenance: emergence
emergence_trigger:
  pair: [procurement-contract-design, requisite-variety]
  ask_session: outputs/logs/sessions/2026-04-04/ask-18-33.md
  connection_type: INSTANCIA
  pearl_level: L2
emerged_on: 2026-04-04
---

## Resumo

Promovido de quarentena em 2026-04-04 após verificação parcial dos claims legais contra raw/lei/lei-14133-2021-artigos-chave.md. 3 patches de refinamento aplicados (0 refutações). Predição falsificável L2 ativa.

Lei de licitações é regulação de variedade de contrato: o tipo de contrato mandatado pela lei fixa V(R) do sistema, a complexidade do projeto determina V(D), e o gap V(R)/V(D) se manifesta como aditivos (error floor de Ashby). Lei 8.666/93 fixou V(R)=1 para todos os projetos — gap estrutural. Lei 14.133/2021 aumentou V(R) parcialmente para obras de engenharia, mas um mecanismo de segunda ordem — auditores que sinalizam especificações vagas como suspeita de corrupção — pressiona gestores a reduzir V(R) mesmo quando a lei permite flexibilidade. Este mecanismo de segunda ordem não é endereçado por nenhum dispositivo da Lei 14.133.

## Conteúdo

### O que procurement-contract-design contribui

Bajari & Tadelis (2001): contrato ótimo minimiza [perda de incentivo] + [custo de adaptação].
- Projetos simples (baixa incerteza de escopo) → FP domina
- Projetos complexos (alta incerteza de escopo) → C+ ou mix

Brasil: Lei 8.666/93 exige licitação competitiva por menor preço para novos contratos → força FP mesmo para projetos complexos. Cada mudança de escopo = aditivo (único mecanismo legal de adaptação).

**Mecanismo:** projeto complexo → design incompleto em t=0 (inevitável) → FP fixo → mudanças de escopo → aditivo. Inevitável dado o design legal.

### O que requisite-variety contribui

Ashby (1956): V(R) < V(D) → irreducible error floor.
- V(D) = variedade das perturbações do ambiente (complexidade do projeto, mudanças de escopo)
- V(R) = variedade do regulador (flexibilidade do contrato para absorver perturbações)
- Regulador passivo (filtro) = V(R) = número de estados fixos
- Regulador ativo (compensador) = V(R) variável, adapta-se ao estado do ambiente

Controle perfeito (V(O) = 1) requer V(R) ≥ V(D). Se V(R) < V(D): as perturbações que passam through o regulador insuficiente = error floor irreduível.

### O que emerge da combinação

⚠️ Tese central é interpretação do compilador. Claims legais específicos verificados em raw/lei/lei-14133-2021-artigos-chave.md.

**Tese central:** Tipo de contrato = tipo de regulador de Ashby. Lei de licitações = meta-regulação de V(R).

| Tipo de contrato | Tipo de regulador Ashby | V(R) |
|-----------------|------------------------|------|
| FP (preço fixo) | Passivo (filtro) | Baixo — 1 estado (preço) |
| C+ (custo + margem) | Ativo (compensador) | Alto — adapta-se ao custo real |
| Contratação integrada (Lei 14.133) | Ativo parcial | Médio-alto — contratante redesenha projeto básico e executivo |
| Contrato de eficiência (Lei 14.133) | Ativo por economia | Médio — qualquer método que gere economia ao contratante (Art. 6, LIII) |

**Lei 8.666/93 = mandato de V(R) = 1 para todos os contratos.** Projeto simples com V(D) baixo → V(R) ≥ V(D) → sistema controlado. Projeto complexo com V(D) alto → V(R) << V(D) → error floor = aditivos.

**Aditivos não são corrupção primária — são o error floor de Ashby manifestado como instrumento jurídico.** A corrupção ocorre quando o error floor é explorado estrategicamente (underbidding + aditivo próximo de 25%), não quando o error floor simplesmente existe.

#### Análise da Lei 14.133/2021 por mecanismo

| Mecanismo | Artigo | Tipo de mudança | V(R) resultante |
|-----------|--------|----------------|-----------------|
| Contratação integrada | Art. 46, inciso V | Genuína | Alto — contratante elabora projeto básico + executivo + executa |
| Contratação semi-integrada | Art. 46, inciso VI | Genuína | Médio — contratante elabora projeto executivo + executa |
| Contrato de eficiência | Art. 6, inciso LIII | Genuína (escopo estreito) | Médio — qualquer método que gere economia ao contratante |
| Matriz de risco | Art. 22, §3 | Gestão de V(D) — obrigatória apenas >R$200M e regimes integrado/semi-integrado | V(R) inalterado — redistribui perturbações |
| Limite de aditivo 25% | Art. 125 | Não alterado | Error floor preservado (idêntico à Lei 8.666) |
| Cobertura de TI/compras/serviços não-engenharia | Sem dispositivo | Não alcançado | V(R) = 1 (regime 8.666 preservado) |

**Conclusão estrutural:** Lei 14.133 é melhoria genuína, não renomeação — mas parcial. Resolve o gap V(R)/V(D) para obras de infraestrutura que usam contratação integrada. Para a maioria dos contratos públicos brasileiros, o gap persiste.

#### O mecanismo de segunda ordem: auditores como supressor de V(R)

⚠️ Este é o insight que emerge da combinação e não está em nenhuma das fontes individuais.

TCU (Tribunal de Contas da União) historicamente penaliza especificações "vagas" como indicador de corrupção em licitações. Gestores que usam contratação integrada com Anteprojeto funcional (alto V(R)) são vulneráveis a questionamentos se o projeto executivo difere substancialmente do anteprojeto — mesmo que a diferença seja tecnicamente justificada e esperada.

**Confirmação formal (TCU Manual 5ª Ed., 2024):** O anteprojeto obrigatório exige 10 elementos (Art. 6º, XXIV, Lei 14.133/2021), incluindo "levantamento topográfico e cadastral, pareceres de sondagem, memorial descritivo dos elementos construtivos" — nível de detalhe que codifica a superespecificação. Acórdãos 2.591/2017, 622/2018 e 544/2021 (Plenário) consolidam que "aditamentos são ilegais quando baseados em erros do anteprojeto" — o que paradoxalmente incentiva gestores a superespecificar o anteprojeto para eliminar a possibilidade de "erros" que gerem aditivos questionáveis. O mecanismo de segunda ordem é, portanto, parcialmente gerado pela própria jurisprudência do TCU que deveria prevenir corrupção.

**Jurisprudência paralela — superespecificação em licitações gerais:** O TCU penaliza igualmente a superespecificação em sentido contrário (especificações excessivamente onerosas que restringem competitividade). Acórdão 898/2021-Plenário: "o que não se admite é o estabelecimento de condições que restrinjam o caráter competitivo das licitações em razão de circunstância impertinente ou irrelevante para o específico objeto do contrato." Acórdão 2129/2021-Plenário: exigência de certificações sem "demonstração da essencialidade" é irregular. Acórdão 1496/2015-Plenário (TI): tanto especificações excessivas quanto insuficientes são irregulares. **Princípio TCU:** restrição é inerente à especificação; o ilegal é restringir por razão impertinente ao objeto.

**Resultado:** Incentivo burocrático é superespecificar o Anteprojeto para reduzir risco de auditoria → o Anteprojeto se torna equivalente ao projeto básico da 8.666 → ganho de V(R) da lei é anulado na prática.

Este mecanismo de segunda ordem cria um **equilíbrio de Nash perverso:**
- Gestor que usa V(R) alto → auditável e vulnerável
- Gestor que superespecifica → protegido de auditoria + aditivos são esperados

A lei aumenta V(R) formal. A estrutura de incentivos de auditoria reduz V(R) efetivo de volta ao nível da 8.666. **Este mecanismo não é endereçado por nenhum dispositivo da Lei 14.133.**

#### Critério ANSP — teste operacional para especificações

Derivado jurisprudencial do TCU (Acórdão 1417/2008-Plenário), aplicável a qualquer exigência editalícia:

| Predicado | Pergunta operacional |
|-----------|---------------------|
| **Adequado** | A exigência é tecnicamente compatível com o objeto? |
| **Necessário** | Sem essa exigência, o objeto não seria entregue com qualidade? |
| **Suficiente** | A exigência captura o que precisa, sem ir além? |
| **Pertinente** | Tem relação direta com o objeto específico (não genérica)? |

Falha em qualquer predicado → irregularidade potencial = fundamento para impugnação.

⚠️ Interpretação do compilador: O critério ANSP pode ser usado como test operacional para distinguir anteprojeto funcional legítimo (alto V(R), todos os predicados satisfeitos) de superespecificação burocrática (V(R) artificial baixo, Suficiência e Pertinência violadas).

## Especulação

- O equilíbrio de Nash perverso (superespecificação como proteção) deveria ser observável como correlação entre densidade de especificações técnicas no Anteprojeto e taxa de aditivos nos contratos — se a especulação é correta, mais especificação → mais aditivos, não menos.
- O efeito do segundo-order de auditores deveria ser menor em municípios com corpo técnico mais qualificado (que entende a distinção entre Anteprojeto funcional e superespecificação).
- Reformas de sucesso deveriam incluir guidelines do TCU explicitamente aceitando Anteprojetos funcionais — sem isso, Lei 14.133 permanece parcialmente inerte.

## Verificação adversarial

**Pergunta falsificável (L2):** Contratos de contratação integrada têm taxa de aditivo_teto significativamente menor que contratos tradicionais de igual complexidade?

**Evidência que confirmaria:** Dados PNCP filtrados por modalidade (contratação integrada vs tradicional), mesma categoria de objeto, mesmo intervalo de valor — contratação integrada com taxa de aditivo_teto < tradicional × 0.7.

**Evidência que refutaria:** Taxa de aditivo_teto similar entre modalidades → o mecanismo de segundo-order (superespecificação do Anteprojeto) está anulando o ganho teórico de V(R).

**Dados necessários:** PNCP com campo de modalidade de contratação. Disponível? Verificar antes de testar.

**Implicação para Zelox Risk Score:** O sinal `aditivo_teto` (aditivo próximo de 25%) deveria ter peso **diferente** para contratos de contratação integrada vs regime tradicional. Sob contratação integrada, o error floor de Ashby é estruturalmente menor → aditivo_teto é mais anômalo → peso maior. Sob regime tradicional, aditivo_teto é parcialmente esperado → peso relativo menor.

## Conexões

- emerge-de: [[procurement-contract-design]] ON "FP vs C+ = reguladores com V(R) baixo vs alto; Lei 8.666 = mandato de V(R)=1"
- emerge-de: [[requisite-variety]] ON "V(R) < V(D) → error floor irreduível; regulador passivo vs ativo"
- relates: [[procurement-renegotiation]] ON "aditivos como error floor vs aditivos como hold-up — Tirole modela o segundo; Ashby explica por que o primeiro é estruturalmente inevitável"
- relates: [[incentive-theory-procurement]] ON "Laffont-Tirole: menu de contratos para revelation — complementa Ashby: o menu ótimo precisa incluir contratos de V(R) adequado ao V(D) do projeto"
- relates: [[audit-deterrence-corruption]] ON "auditores que suprimem V(R) criam o equilíbrio perverso que Lei 14.133 não resolve — mecanismo de segunda ordem"

## Fontes

- [[procurement-contract-design]] — FP vs C+ de Bajari-Tadelis; Lei 8.666 como mandato de FP; aditivos estruturalmente inevitáveis
- [[requisite-variety]] — V(R)/V(D); error floor; regulador passivo vs ativo; "only variety can destroy variety"
- [Lei 14.133/2021 — Artigos-chave](../../raw/lei/lei-14133-2021-artigos-chave.md) — Arts. 6 (definições), 22 (matriz de risco), 46 (regimes de execução), 125 (limite 25%). Fonte: TCE-SP + licitacoesecontratos.tcu.gov.br
- [TCU Manual de Licitações 5ª Ed. (2024)](../../raw/lei/tcu-manual-licitacoes-contratos-5ed-2024.md) — Jurisprudência sobre superespecificação (Acórdãos 898/2021, 2129/2021, 1496/2015, 1417/2008); seção 4.4.2 anteprojeto funcional; Critério ANSP; confirmação dos Acórdãos 2.591/2017, 622/2018, 544/2021 sobre rigidez de aditivos
- [Log /ask](../../outputs/logs/sessions/2026-04-04/ask-18-33.md) — sessão que descobriu a conexão e gerou a análise mecanismo-a-mecanismo da Lei 14.133
