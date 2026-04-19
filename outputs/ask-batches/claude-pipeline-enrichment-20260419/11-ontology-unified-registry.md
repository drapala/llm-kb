# Q11 — Formal ontology: core.py pode estruturar registry unificado skills+antipatterns+lessons?

**Query**: ontology/core.py do metaxon → registry cross-pipeline; que classes emprestar, o que criar.

## Resposta

### O que core.py do metaxon já tem (inventário)

Classes canônicas atuais:
- **Enums estruturais**: `EpistemicStatus` (L0/L1/L2), `ProvenanceType` (SOURCE/SYNTHESIS/EMERGENCE), `SourceQuality` (HIGH/MEDIUM/LOW), `StanceType` (SUPPORTING/CHALLENGING/NEUTRAL), `SeverityLevel`, `DisturbanceType`, `ResolutionLevel`
- **Entidades** (BFO continuant): `KnowledgeArtifact`, `Claim`
- **Eventos** (BFO occurrent): `DisturbanceEvent` (algedônico), `ResolutionSignal`, `SelfChallengeEvent`
- **Policies**: `DisturbancePolicy`, `AlgedonicPolicy` (único factory válido de DisturbanceEvent), `ResolutionPolicy`

### Reúso direto (classes emprestáveis sem mudança)

| Entidade do pipeline | Classe core.py | Adaptação |
|---|---|---|
| Antipattern (entry na registry) | `KnowledgeArtifact` | Adicionar subclasse `Antipattern(KnowledgeArtifact)` com campos `trigger_condition`, `failure_mode`, `counter_evidence` |
| Lesson (padrão positivo) | `KnowledgeArtifact` | Subclasse `Lesson(KnowledgeArtifact)` com `trigger_condition`, `recommended_action` |
| Skill (loadable, prompt 16) | `KnowledgeArtifact` | Subclasse `Skill(KnowledgeArtifact)` com `executable_content` (YAML), `role_scope` |
| Claim dentro de antipattern/lesson | `Claim` | Direto; rastreia evidence individualmente |
| Disagreement entre oracles | `DisturbanceEvent` | Tipo ORACLE_DIVERGENCE via `DisturbancePolicy` |
| Challenge pós-commit em antipattern | `SelfChallengeEvent` | Direto — antipattern disputado vira self-challenge |

Isto já cobre ~70% do que o pipeline precisa estruturar. **Economia real**: um único schema para os 3 stores elimina duplicação atual (`lesson_recorder.py`, `antipattern_miner.py`, rule persistence são hoje schemas divergentes em JSONL).

### Invariantes herdados

Vantagem de usar core.py: **invariantes que o pipeline ganha de graça**:
- `EpistemicStatus` derivado, não declarado — antipattern não pode se auto-classificar como L2 sem challenge_survived.
- `ProvenanceType.EMERGENCE` requer 0 raw sources ou 2+ wiki sources — força rigor.
- `severity` em DisturbanceEvent imutável por design (`mode='before'`) — [feedback-pydantic-derived-fields] memória cobre isto.
- `AlgedonicPolicy` é única factory de DisturbanceEvent — garante instrumentação consistente.

Pipeline atual não tem essas proteções; antipatterns podem ter `confidence: high` declarado sem evidência.

### Classes a criar (genuinamente novas)

Não existe em core.py mas precisa no pipeline:

1. **`StageExecution(BaseModel)`** (BFO occurrent) — representa execução de 1 stage com: ticket_id, stage_name, turns, exit_status, duration, tokens_consumed. Hoje disperso em `executive_timeline.jsonl`.

2. **`StageCheckpoint(BaseModel)`** — para prompt 18 turn-level checkpointing. Subcampo de StageExecution.

3. **`InjectionDetection(BaseModel)`** — subclasse de `DisturbanceEvent`? Provavelmente sim — injection é variety-disturbance detectada em boundary. `DisturbanceType` precisaria enum novo `INJECTION_DETECTED`.

4. **`OracleDisagreement(BaseModel)`** — registro estruturado de oracle split. Hoje `oracle_disagreement.md` é markdown livre. Como `DisturbanceEvent` subtype.

5. **`CanaryResult(BaseModel)`** — para prompt 20 self-mod canary. Seria `KnowledgeArtifact` ou `ResolutionSignal`? Provavelmente ResolutionSignal (resolve "este mod é seguro?").

6. **`AntipatternMatch(BaseModel)`** (BFO occurrent) — instance de antipattern detectado em ticket. Rastreia `retrieval_score`, `match_context`, `was_useful` (para feedback loop do prompt 11).

### Princípio subsidiarity (do CLAUDE.md do metaxon)

> 1. usa classe existente se cobre o caso
> 2. herda de classe existente se precisa especializar
> 3. cria classe nova só se genuinamente novo conceito
> 4. nunca relaxa restrição de classe pai

Aplicado: 4 das 6 classes novas listadas são heranças. Apenas StageExecution e AntipatternMatch são conceitos genuinamente novos ao pipeline (BFO occurrents sem análogo em metaxon).

### Luong 2026 (já no artigo): inverse parametric knowledge effect

Observação chave do [[formal-ontology-for-kbs]]: **ontologia formal ganha mais onde cobertura paramétrica é menor**. Pipeline agent context:
- Domínio AI/ML/Python core → LLM fluent, ontologia ajuda pouco
- Domínio **procurement logic**, **DB migrations**, **infra specifics** do repo alvo → LLM menos confiante, ontologia **ajuda muito**

Implicação prática: o **schema do registry de skills por domínio de usuário** deveria ser mais rigoroso em skills de domínios específicos do que em skills técnicas genéricas. **Isto muda o prompt 16**: loadable skills devem ter campo `parametric_coverage_estimate` — skills com low coverage recebem schema mais estrito (mandatory fields, validation tighter).

### BFO continuant vs occurrent aplicado (crítica ao prompt 11 e 16)

[[formal-ontology-for-kbs]] ensina: KB hoje trata tudo como continuant. Pipeline faz o mesmo.

Antipattern é **continuant** (persiste entre tickets). Antipattern **match** é **occurrent** (evento de aplicação). Hoje o pipeline não separa — armazena apenas antipattern.jsonl, não matches.jsonl.

**Consequência**: pipeline não sabe **qual antipattern foi útil em qual ticket**. Feedback loop (prompt 11) é ciego. Separação continuant/occurrent é pré-requisito para feedback quantitativo.

**Isto muda o prompt 11**: (a) `antipatterns.jsonl` = continuants; (b) novo `antipattern_matches.jsonl` = occurrents com `was_useful` preenchido retroativamente no end do ticket. Decay rate (prompt 11 feedback) calculado sobre matches, não sobre antipatterns.

### Typed relations entre entidades (Relation Ontology)

KB metaxon usa wikilinks tipados (`partOf`, `contradicts`, `derivedFrom`). Pipeline pode adotar relações análogas:
- Antipattern **supersedes** antipattern velho (quando padrão refinado substitui genérico)
- Antipattern **instance-of** failure_category (hierarchy)
- Lesson **counter-evidence-for** antipattern (detecção de invalidação)
- Skill **composed-of** skills (Voyager compositionality, Q3)
- StageExecution **caused** DisturbanceEvent

Relações tipadas permitem queries estruturais:
- "todos os antipatterns superseded nos últimos 30 dias" (decay auditing)
- "qual skill quebra se skill X mudar" (dependency analysis)
- "cadeia causal completa de um failure" (debug)

Hoje essas queries não são possíveis — registries são flat JSONL.

### Moat-building dimension (liga a Q9)

Se pipeline adotar core.py como schema canônico:
- **Schema standardization**: pipelines terceiros que adotam tornam-se interoperáveis.
- **Metaxon ownership do schema** vira moat suave (governance).
- Com multi-tenant (Q9), **schema cross-compat é pré-requisito**.

Isto faz Q9 + Q11 serem **complementares, não ortogonais**. Não adotar ontology é também fechar caminho para moat.

### Risco honesto

Core.py foi desenhado para **knowledge base sobre texto**. Pipeline é sobre **execução de código**. Alguns conceitos podem não transferir bem:
- `KnowledgeArtifact` assume conteúdo textual sintetizável. StageExecution tem mais binary fields (pass/fail, diff hash).
- `StanceType` (SUPPORTING/CHALLENGING/NEUTRAL) é epistemológico — aplicação a skill é forçada.

**Solução**: não forçar 1:1. Adotar **core.py como ancestral**, criar `pipeline_core.py` que herda e especializa. Metaxon core.py evolui separadamente; pipeline_core.py herda deltas.

### Esforço estimado

Avaliação Pareto:
- Migrar antipatterns para `Antipattern(KnowledgeArtifact)`: 2 dias
- Migrar lessons para `Lesson(KnowledgeArtifact)`: 2 dias
- Criar StageExecution/AntipatternMatch: 3 dias
- Adotar typed relations em links internos: 3 dias
- Testes de invariantes (mode='before' etc.): 2 dias

**Total**: ~12 dias — equivalente a Fase 1 ou 6 do roadmap. Não trivial mas trackable.

## Fontes wiki
- `[L0]` [[formal-ontology-for-kbs]] — Noy 101, BFO, DOLCE, OWL, RO; Luong 2026 inverse parametric effect
- `[L1]` [[meta-ontology-metaxon]] — meta-ontology do sistema (verificar se artigo existe)
- Source code: `ontology/core.py` — classes, enums, invariantes

## Confiança
**Alta.** Análise é baseada em classes reais, não aspiracional. Esforço é estimativa cauta.

## Gaps
- Falta artigo específico sobre **ontology for software process** (BFO aplicado a CI/CD).
- Meta-ontology-metaxon referenciado mas não lido nesta sessão.

## Mudanças no roadmap
- **Prompt 11 + 04 + 19 + 16 (todos os registries)**: migrar para `pipeline_core.py` baseado em `metaxon/ontology/core.py`.
- **Prompt 16**: schema per-skill com `parametric_coverage_estimate`; skills low-coverage têm validation stricter (Luong 2026).
- **Prompt 11**: separar `antipatterns.jsonl` (continuant) de `antipattern_matches.jsonl` (occurrent); feedback loop sobre matches.
- **Prompt novo 41 (proposto)**: Ontology alignment — define `pipeline_core.py` herdando de core.py; governance do schema.
- **Ligação explícita com Q9**: ontology é pré-requisito para cross-tenant moat.

## Sugestão de leitura futura
- Ingerir literatura sobre **upper ontologies em software** (BFO 2.0 application to software engineering).
- Cross-check com skills loadable format de agent ecosystems (Anthropic Agent SDK, Claude Skills) — para evitar divergência com padrões emergentes.

## Execution Block (Hypothesis / Experiment / Success Metric)

**Hypothesis**
- Registry unificado em `pipeline_core.py` melhora consistência semântica e feedback quantitativo de uso.

**Experiment**
- Migrar primeiro `antipatterns` + `antipattern_matches` para modelo continuant/occurrent.
- Rodar 1 ciclo de release mantendo dual-write (JSONL antigo + schema novo).
- Medir: `schema_validation_failures`, `feedback_loop_completeness`, `retrieval_precision`.

**Success Metric**
- `schema_validation_failures` < 1%.
- `feedback_loop_completeness` >= 95% dos matches com resultado útil/inútil registrado.
- `retrieval_precision` +10% ou melhor vs baseline.

## Estimate Classification (Measured vs Projected)

| Claim | Classification | Note |
|---|---|---|
| Reuso de core.py cobre ~70% das entidades | Projected (architecture estimate) | Validar durante migração real. |
| Esforço ~12 dias para alignment | Projected | Estimativa de implementação local. |
| Benefício de separar continuant/occurrent | Projected (but strongly grounded) | Mecanismo lógico sólido; impacto precisa medição. |
