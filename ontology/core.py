"""
ontology/core.py — Schema Pydantic canônico do llm-kb

Implementa a upper ontology do sistema epistêmico:
  Entity → KnowledgeArtifact → Claim (eixo estrutural)
  DisturbanceEvent + AlgedonicPolicy  (eixo algedônico / VSM S5)
  ResolutionSignal + ResolutionPolicy (eixo stigmergic / subsidiarity)

Referências fundacionais:
  Beer (1972) — VSM, variety absorption, algedonic channel
  Ashby (1956) — requisite variety, law of requisite variety
  Maturana & Varela (1987) — autopoiese, acoplamento estrutural
  BFO (2020) — continuant vs occurrent
  Luong (2026) — neurosymbolic coupling, inverse parametric knowledge effect
"""

from __future__ import annotations

import uuid
from datetime import datetime, UTC
from enum import Enum

from pydantic import BaseModel, Field, field_validator, model_validator


# ── Enums ─────────────────────────────────────────────────────────────────────


class EpistemicStatus(str, Enum):
    """
    Pearl Level — grau de validação epistêmica de um claim ou artigo.

    Implementa o eixo de confiança do sistema, derivado de:
    - Kahneman: distinção entre heurística (L0) e raciocínio verificado (L1/L2)
    - Lakatos: claims L2 têm predições falsificáveis; L0 são hipóteses degenerativas

    L0: hipótese ou emergence sem validação externa
    L1: verificado contra fonte primária (raw/)
    L2: validado por adversário (Gate 3) ou predição falsificável confirmada
    """

    L0 = "l0"
    L1 = "l1"
    L2 = "l2"


class ProvenanceType(str, Enum):
    """
    Classificação de origem de um artigo wiki.

    Implementa o contrato de proveniência: o sistema deve saber *de onde* veio
    cada conceito. Artigos emergence requerem revisão humana obrigatória porque
    o conceito não existe em nenhuma fonte — é uma contribuição original do
    compilador, não uma síntese de fontes existentes.

    Referência: CLAUDE.md — "Emergence requer revisão humana".
    """

    SOURCE = "source"  # resume principalmente 1 fonte raw/
    SYNTHESIS = "synthesis"  # combina 2+ fontes raw/ sem gerar conceito novo
    EMERGENCE = "emergence"  # conceito ausente em qualquer fonte individual


class SourceQuality(str, Enum):
    """
    Qualidade objetiva das fontes que suportam um artigo.

    Eixo objetivo: baseia-se nas fontes, não na interpretação do compilador.
    Contrasta com interpretation_confidence (eixo subjetivo).

    high:   2+ fontes primárias concordam
    medium: 1 fonte primária ou 2+ secundárias
    low:    apenas fontes terciárias (resumo, opinião)
    """

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class StanceType(str, Enum):
    """
    Postura de uma fonte em relação às premissas existentes do wiki.

    Implementa a Bradford quota: 20-25% das fontes devem ser challenging para
    prevenir convergência semântica (Shumailov 2024 — model collapse).
    O sistema verifica automaticamente se a cota está sendo respeitada.

    confirming:  evidência que corrobora claims existentes
    challenging: evidência que contradiz ou implica revisão de claims
    neutral:     evidência que não tem relação de stance com o corpus atual
    """

    CONFIRMING = "confirming"
    CHALLENGING = "challenging"
    NEUTRAL = "neutral"


class SeverityLevel(str, Enum):
    """
    Severidade de um DisturbanceEvent no canal algedônico.

    Implementa os níveis de resposta do VSM (Beer 1972):
    - medium:   sinal S3 normal — registra, não escala
    - high:     sinal que escala para S4 — registra + inbox
    - critical: bypass S5 genuíno — registra + inbox + degrada system_state

    INVARIANTE: SeverityLevel nunca é passado como input.
    É sempre derivado pelo AlgedonicPolicy a partir do DisturbanceType.
    """

    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class DisturbanceType(str, Enum):
    """
    Tipo de distúrbio no canal algedônico.

    Implementa a taxonomia de eventos que ameaçam a viabilidade do sistema
    epistêmico. Cada tipo tem regras de derivação de severidade e bypass_s3
    fixas no AlgedonicPolicy — não configuráveis por callers externos.

    Referência: Beer (1972) — o canal algedônico bypass S3/S4 e chega
    diretamente a S5 quando o sistema detecta ameaça à sua própria viabilidade.
    """

    RETRIEVAL_FAILURE = "retrieval_failure"  # /ask falha em recuperar
    L1_CONTRADICTION = "l1_contradiction"  # wiki contradiz raw/
    QUARANTINE_REPEAT = "quarantine_repeat"  # quarantine_rate > 15%
    CROSS_SESSION_DRIFT = "cross_session_drift"  # KB diverge entre sessões
    GATE_FAILURE = "gate_failure"  # oracle_ratio > 0.5
    QUARANTINE_STALE = "quarantine_stale"  # artigo pronto > 24h não promovido


class ResolutionLevel(str, Enum):
    """
    Nível de resolução de uma query, derivado do ResolutionPolicy.

    Implementa subsidiarity (Beer/VSM): resolve no nível mais local possível,
    escala apenas quando o nível local não tem variety suficiente.

    stigmergic: corpus local tem variety suficiente — resolve com /ask
    subsidiary: escala para ferramenta externa (web search, oracle)
    algedonic:  bypass de emergência — contradições detectadas, escala para S5
    """

    STIGMERGIC = "stigmergic"
    SUBSIDIARY = "subsidiary"
    ALGEDONIC = "algedonic"


# ── Entidades do conhecimento (BFO: Continuant) ───────────────────────────────


class KnowledgeArtifact(BaseModel):
    """
    Artefato de conhecimento persistente — BFO Continuant.

    Implementa a upper ontology: a unidade atômica do grafo epistêmico.
    Cada artigo wiki é um KnowledgeArtifact com proveniência, status epistêmico
    e rastreabilidade de leitura.

    Invariante de emergence: artigos com provenance=EMERGENCE não podem ter
    exatamente 1 fonte — por definição, emergence é o conceito que não existe
    em nenhuma fonte individual. Uma fonte única significaria SOURCE, não EMERGENCE.
    """

    slug: str = Field(description="Identificador kebab-case único")
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
                "provenance=EMERGENCE requer 0 fontes (conceito novo) ou 2+ fontes wiki "
                "(conexão cross-domain). Uma fonte única indica SOURCE, não EMERGENCE."
            )
        return self


class Claim(BaseModel):
    """
    Afirmação factual ou interpretativa rastreável a um KnowledgeArtifact.

    Implementa o princípio fundamental: 'conhecimento sem epistemologia é ruído'.
    Todo claim tem origem (source_artifact), status de validação (epistemic_status),
    e flag de sobrevivência adversarial (challenge_survived).

    Claims marcados como interpretação (⚠️) têm epistemic_status L0 por padrão
    até sobreviverem a um challenge adversarial (Gate 3 ou /challenge humano).
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
    def interpretation_implies_l0_or_l1(self) -> Claim:
        """Interpretações não validadas por adversário não podem ser L2."""
        if self.is_interpretation and not self.challenge_survived:
            if self.epistemic_status == EpistemicStatus.L2:
                raise ValueError(
                    "Claim de interpretação não pode ser L2 sem challenge_survived=True. "
                    "L2 requer validação adversarial."
                )
        return self


# ── Canal Algedônico (VSM S5 bypass) ──────────────────────────────────────────

# Tabela de derivação: DisturbanceType → (SeverityLevel, bypass_s3)
# Invariante: imutável. Severity nunca é aceita como input externo.
_SEVERITY_RULES: dict[DisturbanceType, tuple[SeverityLevel, bool]] = {
    DisturbanceType.RETRIEVAL_FAILURE: (SeverityLevel.MEDIUM, False),
    DisturbanceType.L1_CONTRADICTION: (SeverityLevel.HIGH, True),
    DisturbanceType.QUARANTINE_REPEAT: (SeverityLevel.HIGH, True),
    DisturbanceType.CROSS_SESSION_DRIFT: (SeverityLevel.CRITICAL, True),
    DisturbanceType.GATE_FAILURE: (SeverityLevel.CRITICAL, True),
    DisturbanceType.QUARANTINE_STALE: (SeverityLevel.MEDIUM, False),
}

# retrieval_failure com 3+ artigos escala para HIGH
_RETRIEVAL_MULTI_THRESHOLD = 3


class DisturbanceEvent(BaseModel):
    """
    Evento de distúrbio no canal algedônico — BFO Occurrent.

    Implementa o canal algedônico de Beer (1972): sinais que bypassam S3/S4
    e chegam diretamente a S5 quando o sistema detecta ameaça à viabilidade.

    INVARIANTE CRÍTICA: severity e bypass_s3 são campos somente-leitura derivados.
    Nunca construa DisturbanceEvent diretamente — use AlgedonicPolicy.emit().
    O model_validator rejeita qualquer severity inconsistente com o type.

    bypass_s3=True: sinal escala direto para S5 sem passar por S3/S4 normal.
    bypass_s3=False: sinal S3 normal — registra mas não escala.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    ts: str = Field(
        default_factory=lambda: datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    origin: str = Field(description="command que detectou o distúrbio")
    type: DisturbanceType
    severity: SeverityLevel
    bypass_s3: bool
    evidence: list[str] = Field(default_factory=list)
    resolved: bool = False
    resolved_at: str | None = None

    @model_validator(mode="after")
    def severity_consistent_with_type(self) -> DisturbanceEvent:
        """
        Verifica que severity e bypass_s3 são consistentes com as regras de
        derivação canônicas. Rejeita eventos com severity incorreta para o type.

        Nota: para retrieval_failure, aceita MEDIUM (1 artigo) ou HIGH (3+).
        A variante HIGH é derivada pelo AlgedonicPolicy com base no len(evidence).
        """
        expected_severity, expected_bypass = _SEVERITY_RULES[self.type]

        # retrieval_failure HIGH é válido se evidence tiver múltiplos artigos
        if self.type == DisturbanceType.RETRIEVAL_FAILURE:
            if len(self.evidence) >= _RETRIEVAL_MULTI_THRESHOLD:
                expected_severity = SeverityLevel.HIGH
                expected_bypass = True

        if self.severity != expected_severity:
            raise ValueError(
                f"severity={self.severity!r} é inconsistente com type={self.type!r}. "
                f"Esperado: severity={expected_severity!r}. "
                "Use AlgedonicPolicy.emit() para construir DisturbanceEvent."
            )
        if self.bypass_s3 != expected_bypass:
            raise ValueError(
                f"bypass_s3={self.bypass_s3!r} é inconsistente com type={self.type!r}. "
                f"Esperado: bypass_s3={expected_bypass!r}."
            )
        return self

    @property
    def is_s5_bypass(self) -> bool:
        """True se o evento bypassa S3/S4 e escala direto para S5."""
        return self.bypass_s3


class AlgedonicPolicy:
    """
    Única interface autorizada para emitir DisturbanceEvents.

    Implementa o princípio de derivação obrigatória de severity: callers externos
    nunca escolhem a severity — ela é sempre computada a partir do type e do
    tamanho da evidence list.

    Referência: Beer (1972) — o canal algedônico é um mecanismo *automático*
    de detecção de ameaça. Se severity fosse configurável, o canal poderia ser
    silenciado por quem tem interesse em esconder o distúrbio.

    critical events nunca auto-resolvem — exigem resolved=True explícito do humano.
    """

    def emit(
        self,
        type: DisturbanceType,
        origin: str,
        evidence: list[str],
        event_id: str | None = None,
    ) -> DisturbanceEvent:
        """
        Cria um DisturbanceEvent com severity e bypass_s3 derivados do type.

        Args:
            type:     tipo do distúrbio (DisturbanceType enum)
            origin:   command que detectou o distúrbio
            evidence: lista de slugs de artigos ou paths de sessões
            event_id: UUID opcional (gerado automaticamente se None)
        """
        severity, bypass_s3 = _SEVERITY_RULES[type]

        # retrieval_failure com 3+ artigos escala para HIGH
        if (
            type == DisturbanceType.RETRIEVAL_FAILURE
            and len(evidence) >= _RETRIEVAL_MULTI_THRESHOLD
        ):
            severity = SeverityLevel.HIGH
            bypass_s3 = True

        return DisturbanceEvent(
            id=event_id or str(uuid.uuid4()),
            origin=origin,
            type=type,
            severity=severity,
            bypass_s3=bypass_s3,
            evidence=evidence,
        )

    def can_auto_resolve(self, event: DisturbanceEvent) -> bool:
        """
        critical events nunca auto-resolvem — exigem intervenção humana explícita.
        medium e high podem ser auto-resolvidos após ação corretiva verificada.
        """
        return event.severity != SeverityLevel.CRITICAL


# ── Sinais de Resolução (subsidiarity) ────────────────────────────────────────


class ResolutionSignal(BaseModel):
    """
    Sinal de entrada para o ResolutionPolicy decidir nível de resolução.

    Implementa o diagnóstico de variety de Ashby: o sistema avalia se tem
    variety local suficiente para absorver a perturbação (query) antes de
    escalar para ferramentas externas.

    source_diversity: número de fontes distintas que cobrem o domínio
    confidence_by_domain: confiança média [0.0, 1.0] nas fontes do domínio
    has_contradictions: True se o corpus local tem claims contraditórios sobre a query
    """

    query: str
    domain: str | None = None
    source_diversity: int = Field(ge=0)
    confidence_by_domain: float = Field(ge=0.0, le=1.0)
    has_contradictions: bool = False

    @field_validator("confidence_by_domain")
    @classmethod
    def confidence_in_range(cls, v: float) -> float:
        if not 0.0 <= v <= 1.0:
            raise ValueError(
                f"confidence_by_domain deve estar em [0.0, 1.0], recebido: {v}"
            )
        return v


class ResolutionPolicy(BaseModel):
    """
    Política de resolução que implementa subsidiarity.

    Subsidiarity (Beer/VSM): cada nível do sistema resolve o que pode com
    a variety disponível. Escala apenas quando genuinamente não sabe —
    não por conveniência ou por falta de tentativa local.

    O threshold assimétrico reflete a lei de Ashby: V(regulator) ≥ V(disturbance)
    é condição necessária para absorção. Se source_diversity < min_source_diversity,
    o regulador local não tem variety suficiente para absorver a query.

    stigmergic_threshold: confiança mínima para resolução local (default 0.8)
    min_source_diversity: diversidade mínima de fontes para confiança válida (default 3)
    """

    stigmergic_threshold: float = Field(default=0.8, ge=0.0, le=1.0)
    min_source_diversity: int = Field(default=3, ge=1)

    def decide(self, signal: ResolutionSignal) -> ResolutionLevel:
        """
        Deriva o nível de resolução a partir do sinal.

        Prioridade:
        1. Contradições → algedônico (escala imediatamente para S5)
        2. Confiança e diversidade suficientes → stigmergic (resolve local)
        3. Caso contrário → subsidiary (escala para ferramenta externa)
        """
        if signal.has_contradictions:
            return ResolutionLevel.ALGEDONIC
        if (
            signal.confidence_by_domain >= self.stigmergic_threshold
            and signal.source_diversity >= self.min_source_diversity
        ):
            return ResolutionLevel.STIGMERGIC
        return ResolutionLevel.SUBSIDIARY
