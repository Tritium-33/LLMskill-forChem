# Third-party sources and modifications

LLMskill-forChem is a curated distribution with original installation tooling and
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

## CatMaster

- Repository: https://github.com/q734738781/CatMaster
- Commit: `06b856814f980ca35f97fb01d7b970b5b18fd230`
- Path: `skills/research_reasoning/research-direction-recovery`
- The repository-root Apache-2.0 license is included in the skill directory.
- The upstream skill's `license: project-local` metadata is preserved verbatim;
  it is an upstream label, not an SPDX license identifier invented by this package.
  Consult the retained license and the linked upstream version for its terms.
- Modifications: Chinese UI metadata added; skill text retained unchanged.

## Original additions

Original installation tooling, tests, documentation and packaging metadata are
provided under the root MIT license. That license does not replace third-party
licenses. No affiliation or endorsement by upstream authors or model vendors is
implied.

## K-Dense Scientific Agent Skills

- Repository: https://github.com/K-Dense-AI/scientific-agent-skills
- Commit: `92ace75ac21efe19a620434e0ca4e356081fe807`
- 42 selected skills: see docs/kdense-skills.md and each SOURCE.json.
- Repository MIT license, copyright (c) 2025 K-Dense Inc., retained in each directory. Original frontmatter library-license labels and bundled notices are preserved; these do not replace dependency licenses.
- Added English display names, Chinese purpose/source metadata and provenance. Upstream SKILL.md and support files remain byte-identical.
- No claim of affiliation, scientific validation, installed dependencies or configured external services.

## Local routing skill

`scientific-skill-router` is original LLMskill-forChem content under the root MIT license. Its indexes link to individually attributed K-Dense skills. SOURCE.json uses kind=original and a local version; there is no invented upstream repository or commit.
