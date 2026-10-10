---
name: scientific-skill-router
description: Choose relevant chemistry and materials research skills for a natural-language request, including one skill or a small combination. Use when the user needs help choosing skills or connecting research steps. Respect explicitly requested skills. Not for ordinary chat or repository maintenance.
---

# Scientific skill router

Help the user choose and use skills without learning their names. This is a guide,
not a scheduler, quality judge, or host-enforced policy.

## Select

Respect the requested result, supplied material, explicit skills and constraints.
If the user specifies an appropriate skill, read it directly; no index is needed.
Otherwise read one relevant selection index, then the selected skill:

- [Chemistry and materials](references/chemistry-materials.md)
- [Papers and research evidence](references/research-evidence.md)
- [Data and modeling](references/data-modeling.md)
- [Writing and figures](references/writing-figures.md)
- [Runtime support](references/runtime-support.md), only if a chosen task needs it

Choose one primary skill by task fit and available dependencies. Add another only
for a needed complementary step. Do not load all indexes, rank by source brand,
randomize, or invoke this router recursively. A short question does not imply an
exhaustive review, new simulation, model, or multi-agent project.

Check the host's available skills, then read the actual `SKILL.md` and any
`PACKAGING.md`. Use the host path or sibling `../<name>/SKILL.md`. An index entry
is not proof of installation or runtime readiness. Follow the chosen protocol;
do not silently simplify its requirements. Report missing prerequisites honestly.

## Connect only when needed

For a multi-step request, use only its relevant guide:
[paper analysis](references/doi-paper-analysis.md),
[VASP output triage](references/vasp-triage.md), or
[table analysis](references/table-analysis.md).
Otherwise follow the selected skill directly. Reuse existing inputs and sources;
pass the needed results, evidence locations, conditions and unresolved items.

Domain routers own their substeps: `dft-vasp` resolves static/relax/DOS/band inside
its own directory, without routing back here. Do not run competing input workflows
or combine conflicting scientific defaults. Execution/submission needs the user's
request. Budgets, worker lifecycle and hard enforcement belong to the host;
do not start agents merely to select skills or present unfinished work as complete.

## Return the result

For one selected skill, briefly state its name and purpose. For combinations,
place `【本轮技能】` (actual English names and purposes) and `【执行步骤】` before
the answer. Record actual reads, tool operations, outputs and states in order,
including failures, retries, skipped and incomplete steps. Use one shared record;
a concise prefix may link an existing full log. Never invent logs or disclose
private reasoning or credentials. A successful read is not scientific validation.

Answer the question directly within the user's limits. State evidence gaps and
unfinished work; files or promises do not replace the requested result. Directly
invoked standalone skills keep their own output rules without this extra prefix.
