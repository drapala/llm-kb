---
title: "GitHub Artifact Attestations + SLSA"
sources:
  - path: raw/articles/github-artifact-attestations.md
    type: docs
    quality: primary
    stance: neutral
created: 2026-04-25
updated: 2026-04-25
tags: [supply-chain-security, slsa, sigstore, provenance, devex, lateral, audit]
source_quality: medium
interpretation_confidence: high
quarantine: true
quarantine_created: 2026-04-25
quarantine_reason: "Domínio lateral recém-ingerido — aguarda review frio"
resolved_patches: []
provenance: source
---

## Resumo

GitHub Artifact Attestations criam provenance criptograficamente assinada para builds: workflow, repo, commit SHA, OIDC token, SBOM. Atendem **SLSA v1.0 Build Level 2** out-of-the-box; Level 3 requer reusable workflows compartilhados. Signing via **Sigstore** — public repos usam transparency log público; private repos usam Sigstore instance do GitHub, sem transparency log. Princípio crítico: **gerar attestation não cria segurança — só verificar cria.** Pipeline que gera sem enforce de `gh attestation verify` adiciona metadata, não safety.

## Conteúdo

### Provenance capturada

Claims criptograficamente assinados encodando:
- Workflow associado ao artifact
- Repo, organization, environment
- Commit SHA + triggering event
- Data via OIDC token

Mais SBOM (software bill of materials) — transparência sobre dependências open source, suporta data protection compliance.

### SLSA alignment

> "Artifact attestations by itself provides SLSA v1.0 Build Level 2"

Estabelece "a link between your artifact and its build instructions."

**SLSA Build Level 3:** requer "reusable workflows that many repositories across your organization share" — provê "isolation between the build process and the calling workflow."

### Sigstore (signing)

- **Public repos:** Sigstore Public Good Instance — bundles em "an immutable transparency log that is publicly readable on the internet"
- **Private repos:** GitHub's Sigstore instance — mesmo código, sem transparency log, federa só com GitHub Actions

### Recommended targets

**Sign:**
- Released software esperado para `gh attestation verify`
- Binaries, downloadable packages, manifests com content hashes

**Don't sign:**
- Frequent automated test builds
- Source files individuais, docs, embedded images

### Verificação

`gh attestation verify ...`

### Caveats explícitos da própria documentação

> "[attestations are] a link to the source code and the build instructions that produced them, but [are] not a guarantee that an artifact is secure."

> "It is up to you to define your policy criteria, evaluate that policy by evaluating the content, and make an informed risk decision when you are consuming software."

> "Generating attestations alone doesn't provide any security benefit, the attestations must be verified for the benefit to be realized."

### Asymmetry princípio

A geração cria **artifact + metadata**. A verificação cria **valor de segurança**. Pipeline maduro: não é "emite attestation" — é "exige verify nos consumers". Sem enforcement de verify, é teatro de provenance.

## Interpretação

(vazia por design)

## Conexões

- relatedTo: [[dora-2025-ai-as-amplifier]] — provenance verificável é parte do "platform quality" que governa adoção de AI
- relatedTo: [[market-for-lemons]] — attestations são mecanismo de signaling credível para supply-chain (resolução de assimetria informacional sobre origem do código)

## Fontes

- [GitHub Artifact Attestations docs](../../raw/articles/github-artifact-attestations.md) — provenance, SLSA, Sigstore, asymmetry generation/verification

> ⚠️ QUARENTENA: artigo recém-ingerido em domínio lateral. Critérios pendentes: tempo (24h), review frio.
