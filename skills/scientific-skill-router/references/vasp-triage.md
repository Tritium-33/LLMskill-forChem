# Existing VASP run: evidence before reuse

Use this route for inspecting existing results. It does not prepare inputs or
authorize new calculations. Reuse project settings and existing validated tools.

1. Establish the requested use (diagnosis, extraction, comparison, or training
   labels), run type, and available files. Preserve raw outputs. Inventory absent
   and incomplete files; a scheduler state alone does not prove convergence.
2. Read the selected skill and its packaging notes. `mat-dft-vasp` scripts import
   an external AtomisticSkills `src/` backend: having the skill directory and
   pymatgen installed is insufficient. Check the actual backend before running.
   If unavailable, use an already available, inspected pymatgen path when suitable,
   or report the missing capability. Do not pretend to have run the upstream parser.
3. Record termination/completeness, electronic convergence, and (for relaxation)
   ionic convergence separately, with file/section locations and parser version.
   Use `unknown` when evidence is insufficient. Static calculations do not require
   ionic relaxation convergence. An energy returned by a parser is not proof that
   any of these conditions passed.
4. Explain errors using the actual messages and relevant method settings. Separate
   observed faults from hypotheses. Do not combine conflicting upstream defaults,
   invent pseudopotentials, overwrite outputs, or automatically resubmit jobs.
   If the user requests new inputs, hand off once to `dft-vasp` or the explicitly
   selected preparation path. Submission remains a separately authorized action.
5. Deliver an inventory, evidence-backed status, extracted values with units,
   proposed remedies, and unresolved items. Keep diagnostic/partial values separate
   from results eligible for the requested downstream use. Numerical convergence
   alone does not establish physical validity or methodological comparability.

Suggested handoff fields are in `workflows.json` (`vasp-triage`). They are a compact
record, not a form the user must fill in. Dataset alignment belongs after extraction
and validation; keep user-specific directory rules outside public skill content.

Public regression cases: `examples/cases.json` in the source repository. They
include synthetic status records, not real VASP calculations. Their gate tests
cannot validate a VASP parser or convergence thresholds.
