# Q12 — Neurosymbolic compliance aplicado aos gates 12/13/14

**Query**: onde regra simbólica supera LLM judge no contexto de prompt injection, secret scanning, git hooks?

## Resposta

### Framing do padrão neurossimbólico

[[neurosymbolic-ai-compliance-applications]] arquitetura canônica (Ajithp 2024):
```
[Dados] → [Neural: flags/scores] → [Symbolic: regras + exceções] → [Veredicto auditável]
```

Invariantes do padrão:
- Neural captura padrões emergentes que regras não cobrem
- Symbolic fornece veredicto **auditável** (rastreável a "violou regra R3 cláusula C2")
- Gate 3 em quarentena dita: **módulos simbólicos adicionam capacidade genuinamente nova** — não apenas explicitam LLM implícito; fornecem **computação deterministicamente correta**

### Gate 13 — Secret scanning

**Já é tool-first com LLM opcional**:
- `secret_scan_gate.py` usa gitleaks + regex (symbolic)
- `secret_allowlist.yaml` com value_hash (symbolic)
- LLM não no loop principal

**Verdict**: symbolic **domina completamente**. LLM não tem vantagem — regexes detectam AWS keys, tokens, PKs com precision altíssima. LLM seria **pior** (latência + ruído + self-enhancement bias).

**Onde LLM poderia ajudar marginalmente**:
- Analisar **contexto** de um match allowlisted — "este placeholder está rodeado de código suspeito?"  
Mas isto é luxury, não necessidade. Atual design do prompt 13 está correto.

### Gate 14 — Git hooks enforcement

**Já é determinístico**:
- Bash tool wrapper com `BLOCKED_GIT_PATTERNS` (regex)
- Detecção de pre-commit/husky/native (file existence checks)
- Hash-based tampering detection

**Verdict**: symbolic **domina**. Nenhum papel para LLM.

Único caso-limite: `hook_overrides.yaml` com `expires_at`. Se LLM propõe override, **exige aprovação humana** — symbolic policy, não LLM decision. Prompt 14 já especifica isto.

### Gate 12 — Prompt injection defense

**Híbrido neural + symbolic**, e **aqui está a questão interessante**:
- `injection_scanner.py` (regex patterns + risk levels) — symbolic
- `_security_preamble.md` — neural (prompt LLM para cautela)
- `tool_call_reviewer.py` — neural (LLM gate)
- `injection_allowlist.yaml` — symbolic

Ajithp pattern exato: neural flagga, symbolic decide. Ordem correta:
1. Symbolic regex scan (zero-cost) captura padrões óbvios: `<system>ignore previous</system>`, `<|im_start|>` bleed, unicode lookalikes, template injection strings.
2. Se symbolic não sinaliza mas contexto é alto-risco (ticket de source externa, logs de produção), LLM layer (`tool_call_reviewer`) entra.
3. Symbolic allowlist tem decisão final em patterns legítimos.

**Crítica ao design atual**: parece que LLM layer roda **sempre**, não só após symbolic. Isso é custo desnecessário.

**Isto muda o prompt 12**: ordem estrita `regex → (pass|LLM_review) → (pass|allowlist|block)`; LLM só roda em casos onde symbolic é inconclusive. Economia estimada: 60-80% das LLM reviewer calls (maioria dos ticket é clean).

### Onde regra simbólica **claramente supera** LLM judge

Domínios com:
- **Enumerable patterns**: regex consegue listar. Secret formats (AWS/GCP/Azure keys têm prefixos conhecidos), SQL injection syntax, null bytes, unicode direction override.
- **Custo alto de falso-negativo** mas **baixo de falso-positivo**: bloquear pattern suspeito e humano revisa é barato.
- **Auditabilidade crítica**: "rejected because matched pattern P3 at line 42" é auditável; "rejected because LLM said so" não.

### Onde LLM judge **claramente supera** regex

- **Semantic invariants** que regex não captura: "este código deixa de validar input antes de eval()"
- **Cross-file reasoning**: "função X em module A assume garantia que module B não dá mais"
- **Intent inference**: "commit message diz 'fix security bug' mas diff remove validation"

Gates 12/13/14 são majoritariamente **primeiro tipo**. Por isso symbolic domina aí.

### Estendendo o padrão para gates novos

Aplicando Ajithp a gates **que ainda não existem no roadmap mas deveriam**:

1. **Supply chain gate** (Q-inicial): diff em `pyproject.toml`/`package.json`  
   - Symbolic: lista de deps conhecidas, tree de CVEs, hash de deps.  
   - Neural: typosquatting detection (difflib ratio contra popular packages).  
   - Symbolic decide: auto-block em typosquat suspeito + dep nova nunca vista.

2. **Type-check gate** (Q-inicial): erros de pyright/tsserver  
   - Puramente symbolic (pyright é symbolic já).  
   - LLM *não* deveria ser adicionado — pyright é ground truth em sua camada.

3. **Symbol-graph scope_precheck** (Q-inicial):  
   - Symbolic (tree-sitter AST).  
   - LLM só se AST inconclusive (ex: dynamic dispatch).

### Risco da mechanistic fallacy (do Gate 3 deste artigo wiki)

O artigo wiki sofreu **Gate 3 invalidation**: o argumento "LLM já faz neurosymbolic implicitamente, módulo symbolic apenas explicita" foi invalidado. **Módulos simbólicos fornecem computação genuinamente nova, determinística**.

Aplicado: não cair no erro "bem, LLM consegue reconhecer injection, então tool_call_reviewer (LLM) é suficiente". Não é. Regex fornece **garantia determinística** que LLM não dá. Symbolic e neural são complementares, não redundantes.

### Confidence score como UQ proxy (não calibrado)

Padrão NeSy: confidence scores propagam via fuzzy logic. Pipeline atual usa confidence em lesson_retriever/antipattern_retriever. Importante: **scores não são calibrados** (linha 81 do artigo wiki). 

Consequência: treatar scores como proxy de utilidade de retrieval, não como probabilidade. Gates 12/13/14 **não devem** usar confidence do scanner neural como se fosse probability of attack — é heurística.

### Auditabilidade full-pipeline

Caveat do artigo (linha 58): auditabilidade **depende de interpretability do componente neural upstream**. Se `tool_call_reviewer` LLM diz "injection detected" sem explicar, auditabilidade quebra.

**Isto muda o prompt 12**: LLM reviewer deve retornar `{verdict, rule_cited, context_quote}` estruturado, não apenas boolean. Caso contrário, auditabilidade é ilusão.

### Gate novo proposto — Compliance gate

Inspirado diretamente Ajithp. Pipeline rodando em repo corporativo tem:
- Regras específicas (licencing, GDPR data handling, PII masking)
- Variam por repo

Um **compliance gate** neurosymbolic:
- Rules: `.pipeline/compliance_rules.yaml` per-repo
- Neural: LLM flagga violations not in rules
- Symbolic: rules produzem veredicto

Prompt **novo (42)** proposto.

### Conexão com displacement (Q6)

Q6 propõe displacement de stages LLM por tool-first. Gates 12/13/14 são exemplares de **displacement bem-executado** — LLM como fallback, symbolic como backbone. Pode servir de template para outros stages.

## Fontes wiki
- `[L0]` [[neurosymbolic-ai-compliance-applications]] — Ajithp padrão, fuzzy/probabilistic logic, Fang 2024, Gate 3 correction sobre mechanistic fallacy
- `[L1]` [[neurosymbolic-ai-knowledge-graphs]] — aplicado a KG
- `[L1]` [[zelox-neurosymbolic-architecture-mapping]] — aplicação concreta

## Fontes raw
- `raw/articles/ajithp-2024-neurosymbolic-compliance.md` (stub, via wiki)
- `raw/papers/fang-2024-llms-neurosymbolic-reasoners.md` (via wiki)
- `raw/papers/arabian-2025-neurosymbolic-robustness-uq-stub.md` (stub)

## Confiança
**Alta.** Análise aterrada em artigo com Gate 3 correction (evita mechanistic fallacy). Claims sobre onde symbolic domina são derivados de características do domínio (enumerabilidade, auditabilidade), não paramétricos.

## Gaps
- Ajithp e Arabian são stubs — falta evidência quantitativa comparando neural-only vs hybrid em produção.
- Sem corpus sobre **type-system ground truth em agentic code generation** (pyright/tsserver como oracle).

## Mudanças no roadmap
- **Prompt 12**: (a) ordem estrita symbolic→(optional neural)→symbolic decide; LLM reviewer só se symbolic inconclusive; (b) LLM reviewer retorna veredicto estruturado `{verdict, rule, quote}` para auditabilidade.
- **Prompt 13**: **manter como está** — symbolic domina completamente.
- **Prompt 14**: **manter como está** — symbolic domina; único toque: override via symbolic policy, não LLM.
- **Prompt novo (42)** — Compliance gate: rules per-repo + neural flagging, estrutura Ajithp.
- **Adicionar aos prompts novos Q-inicial (supply chain, type-check, symbol-graph)**: explicit design decision "primary symbolic, neural fallback only if enumerated test inconclusive".
- **Princípio metadoc**: adicionar ao CLAUDE.md do claude-pipeline: "gates devem ser tool-first; LLM é fallback só onde semantic reasoning é necessário".

## Reflexão cross-query
Este Q12 confirma Q6 (task displacement): gates 12/13/14 já são exemplares de pipeline onde LLM foi bem-displaced. Template transferível para outros gates (test quality 10, scope precheck, ticket validator). Q11 (ontology) reforça: veredictos simbólicos são auditáveis por serem estruturados — `pipeline_core.py` deveria tipar resultado de cada gate como `SymbolicVerdict | NeuralVerdict | HybridVerdict` com campo de explanation.

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Política symbolic-first no Gate 12 reduz custo e mantém segurança, enquanto Gates 13/14 permanecem estáveis.

**Experiment**
- Habilitar no Gate 12:
  1. passagem regex determinística,
  2. chamada LLM apenas em casos inconclusivos,
  3. retorno estruturado `{verdict, rule, quote}`.
- Medir: `llm_reviewer_call_rate`, `injection_escape_rate`, `false_block_rate`.

**Success Metric**
- `llm_reviewer_call_rate` -60% ou melhor.
- `injection_escape_rate` sem piora vs baseline.
- `false_block_rate` <= baseline +1pp.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| Pattern NeSy (neural flag + symbolic decide) | Measured (architecture literature) | Bem estabelecido em compliance. |
| "economia 60-80% de chamadas LLM no Gate 12" | Projected | Hipótese operacional; medir em produção. |
| "13 e 14 devem ficar tool-first" | Measured (codebase fact) | Já implementados com backbone determinístico. |
