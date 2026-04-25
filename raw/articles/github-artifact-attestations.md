---
source: https://docs.github.com/en/actions/concepts/security/artifact-attestations
fetched: 2026-04-25
type: docs
publisher: GitHub
---

# GitHub Artifact Attestations

## Core definition

Artifact attestations enable developers to:

> "create unfalsifiable provenance and integrity guarantees for the software you build."

Consumer-side: "people who consume your software can verify where and how your software was built."

## Provenance information captured

Cryptographically signed claims encoding:
- Workflow association linked to the artifact
- Repository, organization, and environment
- Commit SHA + triggering event
- Data derived from OIDC tokens

Plus SBOM (software bill of materials) integration — transparency on open source dependencies, supports data protection compliance.

## SLSA framework alignment

> "Artifact attestations by itself provides SLSA v1.0 Build Level 2"

Establishes "a link between your artifact and its build instructions."

To reach SLSA v1.0 Build Level 3: implement "reusable workflows that many repositories across your organization share" — provides "isolation between the build process and the calling workflow."

## Signing: Sigstore

> "an open source project that offers a comprehensive solution for signing and verifying software artifacts via attestations."

- **Public repos:** Sigstore Public Good Instance — bundles stored by GitHub, written to "an immutable transparency log that is publicly readable on the internet"
- **Private repos:** GitHub's Sigstore instance — same code, no transparency log, federates only with GitHub Actions

## Recommended use

**Sign:**
- Released software expected to undergo `gh attestation verify`
- Binaries, downloadable packages, manifests with detailed content hashes

**Don't sign:**
- Frequent automated testing builds
- Individual source files, docs, embedded images

## Verification

`gh attestation verify ...` validates attestations.

## Critical caveats

> "[attestations are] a link to the source code and the build instructions that produced them, but [are] not a guarantee that an artifact is secure."

> "It is up to you to define your policy criteria, evaluate that policy by evaluating the content, and make an informed risk decision when you are consuming software."

> "Generating attestations alone doesn't provide any security benefit, the attestations must be verified for the benefit to be realized."

The asymmetry: **generation creates the artifact; verification is what creates security value.** A pipeline that generates without enforcing verification adds metadata, not safety.
