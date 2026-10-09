# Local scientific table: inspect, then analyze within scope

1. Establish the requested question, authorized file/root, known units, groups,
   replicates, and intended use. Start with `exploratory-data-analysis` for a
   supported local format. Its core CLI declares Python 3.11+ independently of
   this collection's Python 3.10+ installer. Additional formats need their own
   dependencies; do not infer support from an extension alone.
2. Use the smallest suitable upstream inspector. Preserve raw data and record
   full versus bounded coverage, missingness, malformed rows and group/split
   information. Do not silently impute, delete outliers, or execute cell contents.
3. Reuse the profile. Choose `statistical-analysis` only when inference is requested
   and its design assumptions can be checked. Choose `scientific-visualization`
   or `seaborn` for a requested plot. Use `scikit-learn` only for a prediction task;
   add `independence-bookkeeping` when validation provenance needs inspection.
   Do not run both plotting skills or build a model merely because available.
4. Missing units/design can permit a descriptive profile while blocking particular
   scientific interpretations. Group overlap or reuse of held-out data blocks an
   independent predictive-validation claim until resolved. Record limitations
   without converting them into fabricated measurements or causal conclusions.
5. Deliver the profile, chosen analysis and relevant diagnostics/figure, plus
   units, coverage, transformations and unresolved issues. Suggested handoff
   fields are in `workflows.json` (`table-analysis`); use ordinary natural language
   and existing artifacts rather than asking the user to complete a new template.

Public fixtures and runnable upstream CLI checks live under `examples/` and
`tests/test_workflows.py` in the source repository. These test table handling,
not the validity of arbitrary statistical methods or model selection.
