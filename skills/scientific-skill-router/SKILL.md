---
name: scientific-skill-router
description: Select and coordinate chemistry and materials research skills for a natural-language request, including a single skill when appropriate. Use when the user needs help choosing skills, analyzing papers, or connecting research steps. Respect explicitly requested skills. Not for ordinary chat or repository maintenance.
---

# Scientific skill router

Choose the smallest sufficient route, execute it, and deliver the requested result.
This is instruction-based coordination, not a scheduler or a host-enforced policy.
Do not recursively invoke this router. Do not start agents merely to choose skills.

## 1. Match the deliverable before choosing a skill

Infer scope from the request and supplied material; do not add a menu or mandatory
planning/approval step. Respect explicit skills and constraints.

| Requested result | Default scope |
| --- | --- |
| A fact, a paper section, or an explanation | Focused reading/tool use; no comprehensive review |
| “Analyze this paper” | Explain question → method → evidence → limits; not automatically a referee report |
| A few related papers or “what is new here?” | Bounded search/comparison; state coverage; do not certify priority |
| Explicit exhaustive novelty audit, systematic review, or referee report | The matching deep protocol, including its evidence obligations |
| New simulation, data analysis, or artifact | Relevant domain route and its prerequisites |

A bounded comparison is not a shortened execution of `lit-review`. Select that
skill for a deep novelty audit or an explicitly requested use, then honor it in
full; if it cannot finish, report incomplete coverage instead of claiming the
audit passed. Similarly, do not use `peer-review` just because the input is a paper.
For systematic screening/synthesis consider `literature-review`; for manuscript
writing consider `scientific-writing` only when writing is requested.

## 2. Load one relevant index, then the actual skill

| Task | Index |
| --- | --- |
| Molecular/material structures, spectra, physical chemistry, units | [chemistry-materials](references/chemistry-materials.md) |
| Papers, evidence, hypotheses, experimental design, review | [research-evidence](references/research-evidence.md) |
| Data checks, statistics, prediction, optimization | [data-modeling](references/data-modeling.md) |
| Writing, figures, slides, document conversion | [writing-figures](references/writing-figures.md) |

Read [runtime-support](references/runtime-support.md) only for a needed runtime
step. Load another index only when crossing domains. Indexes describe this bundle,
not what the host has installed. Check available skills, read the selected real
`SKILL.md` and `PACKAGING.md` if present, and check dependencies before execution.
Use host-provided paths or the sibling `../<name>/SKILL.md`; report missing skills
honestly. Reading instructions is a valid skill use even without a dedicated API;
mentioning a name, attempting a failed load, or selecting it is not successful use.

Choose one primary skill by task/input/method fit, available dependencies, and
least unnecessary work. Add a complementary skill only for a concrete missing
capability. Reuse sources and intermediate results. Do not randomize, favor a
source brand, or infer a global quality weight from one test. Use applicable
validation evidence as a tie-breaker, not as proof of scientific correctness.

## 3. Execute with bounded handoffs

For a multi-step task, briefly state the scope and next step, then proceed.
Carry forward only inputs, source locations, findings, limitations, and status
needed by the next step; do not reload whole contexts or repeat completed searches.
Apply the [execution and delivery contract](references/execution-contract.md).
This contract is for routes managed here; it does not modify upstream skill bodies
or impose this bundle's reporting on directly invoked standalone skills.

Read only the matching internal route when needed:

- Paper reading, retrieval, or comparison: [paper route](references/doi-paper-analysis.md).
- Existing VASP outputs/failures: [VASP triage](references/vasp-triage.md).
- Scientific tables and requested follow-up: [table analysis](references/table-analysis.md).

The optional [machine-readable contracts](references/workflows.json) connect
skills, handoffs, stopping conditions, and cases; they are not an execution engine.

## 4. Preserve domain ownership

- VASP input preparation: `dft-vasp` owns static/relax/DOS/band selection. Resolve
  these subskills inside its directory, not by generic bare names. No return to
  this router within that stage. Continue other stages only after the handoff.
- An established compatible workflow may instead use `mat-dft-vasp`; its full
  backend is not bundled. For output parsing/diagnosis inspect actual capabilities
  and packaging. Do not create two competing input sets or merge conflicting
  scientific defaults. Only requested execution/submission uses `dpdisp-submit`.
- General molecule handling: `datamol`; detailed molecule operations: `rdkit`;
  periodic structures: `pymatgen`. OpenMM molecular dynamics is not periodic AIMD.
- Specific DOI/cross-source lookup: `paper-lookup`; specified backend: its lookup
  skill; bibliography generation: `citation-management`; strict metadata conflicts:
  `ref-check`. A real DOI does not establish support for the cited claim.
- Data exploration: `exploratory-data-analysis`; inference planning:
  `statistical-analysis`; prediction: `scikit-learn`. Do not add modeling to a
  request for data inspection. Use `independence-bookkeeping` when independence
  of evaluation is at issue, not as a default extra step.
- Data figures: `seaborn`/`scientific-visualization`; conceptual illustrations:
  `scientific-schematics`. The latter's service is not required for data plotting.

## 5. Report actual execution, not intended execution

For a single selected skill, briefly name it and its purpose. For a combination,
put `【本轮技能】` (actual English names and purposes) and `【执行步骤】` before the
answer. Number actual skill reads, tool operations, outputs, and states in order;
include failures, skipped and incomplete work. A concise prefix may link an
existing full log. Reuse one record across domain handoffs. Never fabricate logs,
report private reasoning, expose credentials, or add tools merely to fill a trace.

Deliver the answer in chat unless a different deliverable was requested. Files
and promises of future agent results cannot replace the requested answer. Report
only observed completion; scientific verification is separate from tool success.

## Maintenance

`catalog.json` is the source for generated functional indexes; rebuild with
`python tools/build_skill_index.py` in the repository. Preserve English upstream
names, upstream bodies, licenses, and provenance. Reinstall changed copies using
the installer; editing this source does not update an already installed copy.
