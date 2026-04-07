"""
ontology/core.py — Schema Pydantic canônico do llm-kb

Implementa a upper ontology do sistema epistêmico:
  Entity → KnowledgeArtifact → Claim (eixo estrutural — BFO Continuant)
  DisturbancePolicy + DisturbanceEvent + AlgedonicPolicy (canal algedônico VSM S5)
  ResolutionSignal + ResolutionPolicy (subsidiarity / Ashby requisite variety)

Referências fundacionais:
  Beer (1972)          — VSM, variety absorption, algedonic channel
  Ashby (1956)         — requisite variety, law of requisite variety
  Maturana & Varela (1987) — autopoiese, acoplamento estrutural
  BFO (2020)           — continuant vs occurrent
  Luong (2026)         — neurosymbolic coupling, inverse parametric knowledge effect
"""

from __future__ import annotations

import uuid
from datetime import datetime, UTC
from enum import Enum
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


# ── Enums ─────────────────────────────────────────────────────────────────────


class EpistemicStatus(Enum):
    """
    Pearl Level — grau de validação epistêmica de um claim ou artigo.

    Implementa o eixo de confiança do sistema:
    - Kahneman: distinção entre heurística rápida (L0) e raciocínio verificado (L1/L2)
    - Lakatos: claims L2 têm predições falsificáveis; L0 sem predição = hipótese degenerativa

    Invariante: nenhum claim de interpretação (⚠️) pode ser L2 sem challenge_survived=True.

    Correto:   EpistemicStatus.L2  (via Claim.epistemic_status)
    Incorreto: EpistemicStatus("l2")  — preferir acesso por atributo
    """

    L0 = "l0"  # hipótese ou emergence sem validação externa
    L1 = "l1"  # verificado contra fonte primária (raw/)
    L2 = "l2"  # validado por adversário (Gate 3) ou predição falsificável confirmada


class ProvenanceType(Enum):
    """
    Classificação de origem de um artigo wiki.

    Implementa o contrato de proveniência: o sistema deve saber de onde veio
    cada conceito. Artigos EMERGENCE requerem revisão humana obrigatória —
    o conceito não existe em nenhuma fonte individual.

    Invariante: EMERGENCE com exatamente 1 fonte é impossível pelo schema
    (seria SOURCE). EMERGENCE requer 0 fontes raw/ ou 2+ fontes wiki.

    Referência: CLAUDE.md — "Emergence requer revisão humana".
    """

    SOURCE = "source"  # resume principalmente 1 fonte raw/
    SYNTHESIS = "synthesis"  # combina 2+ fontes raw/ sem gerar conceito novo
    EMERGENCE = "emergence"  # conceito ausente em qualquer fonte individual


class SourceQuality(Enum):
    """
    Qualidade objetiva das fontes que suportam um artigo.

    Eixo objetivo: baseia-se nas fontes, não na interpretação do compilador.
    Contrasta com interpretation_confidence (eixo subjetivo do agente).

    high:   2+ fontes primárias independentes concordam
    medium: 1 fonte primária OU 2+ fontes secundárias
    low:    apenas fontes terciárias (resumo, opinião, sem dado original)
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class StanceType(Enum):
    """
    Postura de uma fonte em relação às premissas existentes do wiki.

    Implementa a Bradford quota: 20-25% das fontes devem ser CHALLENGING
    para prevenir convergência semântica (Shumailov 2024 — model collapse).
    O /lint-epistemic verifica automaticamente se a cota está sendo respeitada.

    supporting:  evidência que corrobora claims existentes
    challenging: evidência que contradiz ou implica revisão de claims
    neutral:     sem relação de stance com o corpus atual
    """

    SUPPORTING = "supporting"
    CHALLENGING = "challenging"
    NEUTRAL = "neutral"


class SeverityLevel(Enum):
    """
    Severidade de um DisturbanceEvent no canal algedônico.

    Implementa os 3 níveis de resposta do VSM (Beer 1972):
    - MEDIUM:   sinal S3 normal — registra em algedonic_events, nada mais
    - HIGH:     escala para S4 — registra + cria outputs/inbox/algedonic-*.md
    - CRITICAL: bypass S5 genuíno — registra + inbox + system_state: degraded

    INVARIANTE ABSOLUTA: SeverityLevel é sempre derivado pelo DisturbancePolicy
    a partir do DisturbanceType. Nunca é aceito como input externo.
    O model_validator(mode='before') em DisturbanceEvent sobrescreve qualquer
    valor passado diretamente — tornando a injeção estruturalmente impossível.

    Correto:   AlgedonicPolicy().emit(DisturbanceType.GATE_FAILURE, ...)
    Impossível: DisturbanceEvent(severity=SeverityLevel.MEDIUM, type=GATE_FAILURE, ...)
                → validator sobrescreve severity para CRITICAL
    """

    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class DisturbanceType(Enum):
    """
    Tipo de distúrbio no canal algedônico — taxonomia de ameaças à viabilidade.

    Cada tipo tem regras de derivação de severity e bypass_s3 fixas em
    DisturbancePolicy.rules — não configuráveis por callers externos.

    Referência: Beer (1972) — o canal algedônico bypassa S3/S4 e chega
    diretamente a S5 quando o sistema detecta ameaça à própria viabilidade.
    O mecanismo é *automático*: não passa por camadas que têm interesse
    em suprimir o sinal.
    """

    RETRIEVAL_FAILURE = "retrieval_failure"  # /ask falha em recuperar artigos
    L1_CONTRADICTION = "l1_contradiction"  # wiki contradiz raw/ (raw/ vence)
    QUARANTINE_REPEAT = "quarantine_repeat"  # quarantine_rate > 15%
    CROSS_SESSION_DRIFT = (
        "cross_session_drift"  # KB diverge semanticamente entre sessões
    )
    GATE_FAILURE = "gate_failure"  # oracle_ratio > 0.5 (metabolismo defensivo)
    QUARANTINE_STALE = "quarantine_stale"  # artigo pronto há > 24h sem /promote


class ResolutionLevel(Enum):
    """
    Nível de resolução de uma query, derivado pelo ResolutionPolicy.decide().

    Implementa subsidiarity (Beer/VSM): resolve no nível mais local possível,
    escala apenas quando o nível local genuinamente não tem variety suficiente
    para absorver a perturbação (Ashby: V(regulator) ≥ V(disturbance)).

    stigmergic: corpus local tem variety suficiente — /ask resolve internamente
    subsidiary: escala para ferramenta externa (web search, oracle LLM)
    algedonic:  contradições detectadas — bypassa S3/S4, escala para S5
    """

    STIGMERGIC = "stigmergic"
    SUBSIDIARY = "subsidiary"
    ALGEDONIC = "algedonic"


# ── Entidades do conhecimento (BFO: Continuant) ───────────────────────────────


class KnowledgeArtifact(BaseModel):
    """
    Artefato de conhecimento persistente — BFO Continuant.

    Unidade atômica do grafo epistêmico. Persiste como um todo em qualquer
    instante (diferente de Session, que é BFO Occurrent com partes temporais).

    Invariante de emergence: artigos com provenance=EMERGENCE não podem ter
    exatamente 1 fonte. Por definição, emergence é o conceito ausente em qualquer
    fonte individual. Uma fonte única → SOURCE. Zero fontes ou 2+ fontes wiki → EMERGENCE.

    Correto:
        KnowledgeArtifact(slug="x", provenance=EMERGENCE, sources=[])
        KnowledgeArtifact(slug="x", provenance=EMERGENCE, sources=["wiki/a.md", "wiki/b.md"])
    Incorreto (ValidationError):
        KnowledgeArtifact(slug="x", provenance=EMERGENCE, sources=["raw/one.md"])
    """

    model_config = ConfigDict(use_enum_values=False)

    slug: str = Field(description="Identificador kebab-case único no wiki")
    title: str
    epistemic_status: EpistemicStatus
    provenance: ProvenanceType
    source_quality: SourceQuality = SourceQuality.MEDIUM
    sources: list[str] = Field(default_factory=list)
    reads: int = Field(default=0, ge=0)
    quarantine: bool = False

    @model_validator(mode="after")
    def emergence_requires_no_single_source(self) -> KnowledgeArtifact:
        if self.provenance == ProvenanceType.EMERGENCE and len(self.sources) == 1:
            raise ValueError(
                "provenance=EMERGENCE requer 0 fontes (conceito inteiramente novo) "
                "ou 2+ fontes wiki (conexão cross-domain). "
                "Uma fonte única indica provenance=SOURCE, não EMERGENCE."
            )
        return self


class Claim(BaseModel):
    """
    Afirmação rastreável a um KnowledgeArtifact — grão atômico de conhecimento.

    Implementa o princípio: 'conhecimento sem epistemologia é ruído'.
    Todo claim tem origem (source_artifact), grau de validação (epistemic_status),
    e flag de sobrevivência adversarial (challenge_survived).

    Invariante: claims de interpretação (⚠️ nossa interpretação) não podem ser L2
    sem challenge_survived=True. L2 requer validação adversarial externa.

    Correto:
        Claim(content="X", epistemic_status=L1, is_interpretation=False)
        Claim(content="X", epistemic_status=L2, is_interpretation=True, challenge_survived=True)
    Incorreto (ValidationError):
        Claim(content="X", epistemic_status=L2, is_interpretation=True, challenge_survived=False)
    """

    content: str
    source_artifact: str = Field(description="slug do KnowledgeArtifact de origem")
    epistemic_status: EpistemicStatus
    challenge_survived: bool = False
    is_interpretation: bool = Field(
        default=False,
        description="True para claims marcados (⚠️ nossa interpretação) no wiki",
    )

    @model_validator(mode="after")
    def interpretation_requires_challenge_for_l2(self) -> Claim:
        if (
            self.is_interpretation
            and not self.challenge_survived
            and self.epistemic_status == EpistemicStatus.L2
        ):
            raise ValueError(
                "Claim de interpretação (is_interpretation=True) não pode ser L2 "
                "sem challenge_survived=True. L2 requer validação adversarial."
            )
        return self


# ── Canal Algedônico (VSM S5 bypass) ──────────────────────────────────────────


class DisturbancePolicy(BaseModel):
    """
    Tabela de derivação canônica para severity e bypass_s3.

    Implementa o princípio de que o canal algedônico é automático (Beer 1972):
    a severity não pode ser configurada por quem reporta o distúrbio —
    seria como deixar o paciente calibrar o termômetro.

    ClassVar rules: imutável em tempo de execução; Pydantic não valida
    nem serializa ClassVar, garantindo que a tabela não pode ser sobrescrita
    por um caller via construtor de instância.

    Correto:   DisturbancePolicy().derive(DisturbanceType.GATE_FAILURE, 1)
               → (SeverityLevel.CRITICAL, True)
    Impossível: DisturbancePolicy(rules={...})  ← ClassVar não é campo de instância
    """

    # ClassVar: Pydantic não trata como campo — não pode ser sobrescrito via construtor
    rules: ClassVar[dict[DisturbanceType, dict[str, Any]]] = {
        DisturbanceType.RETRIEVAL_FAILURE: {
            "threshold": 1,
            "severity_single": SeverityLevel.MEDIUM,
            "severity_multiple": SeverityLevel.HIGH,
            "bypass_s3_single": False,
            "bypass_s3_multiple": True,
        },
        DisturbanceType.L1_CONTRADICTION: {
            "severity": SeverityLevel.HIGH,
            "bypass_s3": True,
        },
        DisturbanceType.QUARANTINE_REPEAT: {
            "severity": SeverityLevel.HIGH,
            "bypass_s3": True,
        },
        DisturbanceType.CROSS_SESSION_DRIFT: {
            "severity": SeverityLevel.CRITICAL,
            "bypass_s3": True,
        },
        DisturbanceType.GATE_FAILURE: {
            "severity": SeverityLevel.CRITICAL,
            "bypass_s3": True,
        },
        DisturbanceType.QUARANTINE_STALE: {
            "severity": SeverityLevel.MEDIUM,
            "bypass_s3": False,
        },
    }

    def derive(
        self,
        type: DisturbanceType,
        evidence_count: int = 1,
    ) -> tuple[SeverityLevel, bool]:
        """
        Deriva severity e bypass_s3 a partir do type e contagem de evidências.

        Para RETRIEVAL_FAILURE: 1-2 artigos → MEDIUM; 3+ artigos → HIGH.
        Para todos os outros tipos: regra fixa independente de evidence_count.

        Args:
            type:           tipo do distúrbio
            evidence_count: len(evidence) — usado apenas para RETRIEVAL_FAILURE

        Returns:
            (SeverityLevel, bypass_s3: bool)
        """
        rule = self.rules[type]
        if "threshold" in rule:
            # RETRIEVAL_FAILURE: threshold=1, threshold+2=3 → multi threshold
            if evidence_count >= rule["threshold"] + 2:
                return rule["severity_multiple"], rule["bypass_s3_multiple"]
            return rule["severity_single"], rule["bypass_s3_single"]
        return rule["severity"], rule["bypass_s3"]


class DisturbanceEvent(BaseModel):
    """
    Evento de distúrbio no canal algedônico — BFO Occurrent.

    Implementa o sinal de dor/prazer do VSM (Beer 1972) que bypassa S3/S4
    e chega diretamente a S5 quando o sistema detecta ameaça à viabilidade.

    INVARIANTE ABSOLUTA: severity e bypass_s3 são SEMPRE derivados do type
    via DisturbancePolicy. O model_validator(mode='before') sobrescreve qualquer
    valor passado antes da validação dos campos — tornando a injeção impossível.

    Correto — via AlgedonicPolicy.emit() (única interface autorizada):
        policy = AlgedonicPolicy()
        e = policy.emit(DisturbanceType.L1_CONTRADICTION, "/challenge", ["art-a"])
        # e.severity == SeverityLevel.HIGH  (derivado automaticamente)
        # e.bypass_s3 == True               (derivado automaticamente)

    "Impossível" — severity é sobrescrita pelo validator, não respeitada:
        DisturbanceEvent(type=GATE_FAILURE, severity=MEDIUM, ...)
        # severity será sobrescrita para CRITICAL pelo mode='before' validator
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    ts: str = Field(
        default_factory=lambda: datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    origin: str = Field(description="command ou hook que detectou o distúrbio")
    type: DisturbanceType
    severity: SeverityLevel  # derivado — nunca confiar no valor passado externamente
    bypass_s3: bool  # derivado — nunca confiar no valor passado externamente
    evidence: list[str] = Field(default_factory=list)
    resolved: bool = False
    resolved_at: str | None = None

    @model_validator(mode="before")
    @classmethod
    def derive_severity_and_bypass(cls, data: Any) -> Any:
        """
        Deriva e SOBRESCREVE severity+bypass_s3 antes de qualquer validação de campo.

        mode='before' garante que mesmo valores explicitamente passados pelo caller
        sejam ignorados e substituídos pelos valores corretos derivados do type.
        Isso torna a injeção de severity incorreta estruturalmente impossível.
        """
        if not isinstance(data, dict):
            return data
        raw_type = data.get("type")
        if raw_type is None:
            return data  # deixa Pydantic reportar "field required: type"
        # normaliza str → Enum se necessário (para compatibilidade com desserialização)
        ev_type = DisturbanceType(raw_type) if isinstance(raw_type, str) else raw_type
        evidence_count = len(data.get("evidence", []))
        severity, bypass_s3 = DisturbancePolicy().derive(ev_type, evidence_count)
        data["severity"] = severity
        data["bypass_s3"] = bypass_s3
        return data

    @property
    def is_s5_bypass(self) -> bool:
        """True se o evento bypassa S3/S4 e escala direto para S5."""
        return self.bypass_s3


class AlgedonicPolicy(BaseModel):
    """
    Única interface autorizada para criar DisturbanceEvents.

    Implementa o princípio de Beer (1972): o canal algedônico é automático.
    Severity nunca é escolhida pelo caller — é computada por DisturbancePolicy.

    Como BaseModel, AlgedonicPolicy pode ser serializada, versionada, e
    injetada com uma DisturbancePolicy customizada para testes.

    Correto:
        policy = AlgedonicPolicy()
        e = policy.emit(DisturbanceType.L1_CONTRADICTION, "/challenge", ["art-a", "sess-b"])
        assert e.severity == SeverityLevel.HIGH
        assert e.bypass_s3 == True

    Incorreto (não use diretamente):
        DisturbanceEvent(type=..., severity=..., ...)  ← severity será sobrescrita
    """

    policy: DisturbancePolicy = Field(default_factory=DisturbancePolicy)

    def emit(
        self,
        type: DisturbanceType,
        origin: str,
        evidence: list[str],
    ) -> DisturbanceEvent:
        """
        Cria um DisturbanceEvent com severity e bypass_s3 derivados do type.

        O model_validator(mode='before') em DisturbanceEvent garante a derivação
        mesmo que este método não passasse os valores — mas passamos explicitamente
        para clareza e para evitar a chamada dupla ao DisturbancePolicy.

        Args:
            type:     tipo do distúrbio (DisturbanceType)
            origin:   command ou hook que detectou o distúrbio (string livre)
            evidence: slugs de artigos ou paths de sessões que evidenciam o distúrbio
        """
        severity, bypass_s3 = self.policy.derive(type, len(evidence))
        return DisturbanceEvent(
            origin=origin,
            type=type,
            severity=severity,
            bypass_s3=bypass_s3,
            evidence=evidence,
        )

    def can_auto_resolve(self, event: DisturbanceEvent) -> bool:
        """
        CRITICAL events nunca auto-resolvem — exigem resolved=True explícito do humano.
        MEDIUM e HIGH podem ser auto-resolvidos após ação corretiva verificada.

        Referência: invariante do canal algedônico — sinais que bypassam S5
        requerem resposta de S5 para fechar o loop.
        """
        return event.severity != SeverityLevel.CRITICAL


# ── Sinais de Resolução (subsidiarity / Ashby variety) ────────────────────────


class ResolutionSignal(BaseModel):
    """
    Sinal de entrada para ResolutionPolicy.decide() — diagnóstico de variety local.

    Implementa a lei de Ashby: antes de escalar, o sistema verifica se tem
    variety suficiente para absorver a perturbação localmente.

    source_diversity: número de fontes distintas que cobrem o domínio da query
    confidence_by_domain: confiança média [0.0, 1.0] nas fontes do domínio
    has_contradictions: True se o corpus local tem claims contraditórios sobre a query

    Correto:
        ResolutionSignal(query="X", source_diversity=4, confidence_by_domain=0.9)
    Incorreto (ValidationError):
        ResolutionSignal(query="X", source_diversity=-1, confidence_by_domain=1.5)
    """

    query: str
    domain: str | None = None
    source_diversity: int
    confidence_by_domain: float
    has_contradictions: bool = False

    @field_validator("confidence_by_domain")
    @classmethod
    def confidence_must_be_valid(cls, v: float) -> float:
        if not 0.0 <= v <= 1.0:
            raise ValueError(f"confidence_by_domain {v!r} fora do range [0.0, 1.0]")
        return v

    @field_validator("source_diversity")
    @classmethod
    def diversity_must_be_positive(cls, v: int) -> int:
        if v < 0:
            raise ValueError(f"source_diversity {v!r} não pode ser negativo")
        return v


class ResolutionPolicy(BaseModel):
    """
    Política de subsidiarity: decide o nível de resolução a partir do sinal.

    Implementa a lei de Ashby: V(regulator) ≥ V(disturbance) é condição
    necessária para absorção local. Se source_diversity < min_source_diversity,
    o regulador não tem variety suficiente — deve escalar.

    O threshold assimétrico (stigmergic_threshold=0.8) reflte que sub-resolução
    é mais cara que sobre-escalamento: melhor consultar oracle do que alocar
    claims sem evidência suficiente.

    Correto:
        policy = ResolutionPolicy()
        level = policy.decide(ResolutionSignal(query="X", source_diversity=4,
                                               confidence_by_domain=0.9))
        assert level == ResolutionLevel.STIGMERGIC
    """

    stigmergic_threshold: float = Field(default=0.8, ge=0.0, le=1.0)
    min_source_diversity: int = Field(default=3, ge=1)

    def decide(self, signal: ResolutionSignal) -> ResolutionLevel:
        """
        Deriva o nível de resolução.

        Prioridade (em ordem):
        1. Contradições detectadas → ALGEDONIC (bypassa S3/S4, escala para S5)
        2. Confiança ≥ threshold E diversidade ≥ mínimo → STIGMERGIC (resolve local)
        3. Caso contrário → SUBSIDIARY (escala para ferramenta externa)
        """
        if signal.has_contradictions:
            return ResolutionLevel.ALGEDONIC
        if (
            signal.confidence_by_domain >= self.stigmergic_threshold
            and signal.source_diversity >= self.min_source_diversity
        ):
            return ResolutionLevel.STIGMERGIC
        return ResolutionLevel.SUBSIDIARY
