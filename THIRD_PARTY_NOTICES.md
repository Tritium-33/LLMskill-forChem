# Third-party sources and modifications

LLMskill-forChem is a redistribution bundle with original installation tooling and
Chinese usage documentation. It does not claim authorship of the upstream methods.
Each skill carries a `SOURCE.json` with the pinned repository, commit, path, source
hash and modification summary. Chinese UI metadata was added during packaging.

## BootLoops Skills

- Repository: https://github.com/BootLoops-ai/skills
- Commit: `ca892277dcf0468d995f0036f3bd6d753a8afe7d`
- Bundled: `reading-contract`, `lit-review`, `ref-check`, `independence-bookkeeping`
- Attribution: BootLoops 1.0, Anthropic, PBC and Matthew D. Schwartz (2026),
  https://www.bootloops.ai
- Upstream prose: CC BY 4.0, documented in each bundle's `LICENSE-CONTENT`.
- Upstream code/manifests: MIT, with the upstream `LICENSE` retained.
- Upstream `NOTICE` is retained verbatim, including its authorship and affiliation
  statements. It describes the upstream project, not the entirety of this repository.
- Modifications: added Chinese `agents/openai.yaml`; `ref-check` replaces two
  shell-pipeline examples with platform-neutral instructions. Other upstream skill
  text is retained unchanged. See individual `SOURCE.json` files.

## Withdrawn content

CatMaster `research-direction-recovery`, and K-Dense `matplotlib`, `sympy` and
`venue-templates` are no longer bundled pending clarification of skill-specific
licensing or completion of attached third-party notices. See docs/license-audit/README.md.
This is a conservative distribution decision, not an allegation against upstream.

## Original additions

Original installation tooling, tests, documentation and packaging metadata are
provided under the root MIT license. That license does not replace third-party
licenses. No affiliation or endorsement by upstream authors or model vendors is
implied.

## K-Dense Scientific Agent Skills

- Repository: https://github.com/K-Dense-AI/scientific-agent-skills
- Commit: `92ace75ac21efe19a620434e0ca4e356081fe807`
- 39 bundled skills: see docs/skills-catalog.md and each SOURCE.json.
- The upstream README explicitly says individual SKILL.md license fields apply:
  28 skills declare MIT, six Apache-2.0, and five BSD-3-Clause.
- The upstream root MIT copyright notice, Copyright (c) 2025 K-Dense Inc., is
  retained in each LICENSE. It does not override individual skill licensing.
- Apache/BSD skills additionally carry LICENSE-Apache-2.0 or LICENSE-BSD-3-Clause
  and a NOTICE recording the declared license, source and known attribution.
- English display names, Chinese purpose/source metadata and provenance were added.
  Retained upstream SKILL.md and support files are unchanged.
- No affiliation, scientific validation, installed dependencies or configured services is claimed.

## Local routing skill

`scientific-skill-router` is original LLMskill-forChem content under the root MIT license. Its indexes link to individually attributed skills across sources. SOURCE.json uses kind=original and a local version; there is no invented upstream repository or commit.
