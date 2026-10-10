# Paper reading, retrieval, and comparison

Select scope from the user's actual request, not the number of available skills.
Read the [evidence checks](evidence-checks.md) before making evaluative claims.
Use the shared [execution contract](execution-contract.md) for handoff and delivery.

| Need | Action | Handoff / limit |
| --- | --- | --- |
| Identify or obtain a paper | `paper-lookup` only when identity/material is missing; reuse supplied reliable text | DOI/title/version, retrieved sources, actual coverage |
| Resolve metadata conflict or explicitly verify bibliography | `ref-check` | Verified fields plus unresolved discrepancies |
| Explain a paper or one dimension | `reading-contract`; read relevant full text, figures and accessible SI | Claims with locations, conditions and limitations; no automatic referee report |
| Evaluate method/evidence | Add `scientific-critical-thinking` only if needed | Evidence-based appraisal, distinguishing inference from author claims |
| Find a requested number of related papers | `paper-lookup`, then inspect sources relevant to the requested relation | Deduplicated selected records with verified dates/identities and support locations |
| Compare novelty briefly | Bounded lookup + source-bound reading; reuse existing evidence | What differs from the examined works; coverage limits; no exhaustive priority claim |
| Deep novelty audit explicitly required | `lit-review`, follow its full protocol | Read/search receipts, coverage gaps, no completion claim if requirements unmet |
| Systematic/scoping synthesis | `literature-review`, follow its protocol | Search/screening/synthesis appropriate to requested review |

Plain “analyze this paper” means explain the question, method, key evidence,
conclusion and limitations. Plain “what is new?” calls for distinguishing the
paper's own novelty claim from what a bounded comparison establishes; it does
not license a percentage novelty score, a definitive first-ever claim, or an
unbounded parallel literature review.

Carry identity, material/version coverage, claims with exact locations, conditions,
and unresolved items between steps. Do not copy entire sources into every stage.
Reuse a source while checking each new claim against its relevant passage.

For cutoff-date tasks, decide which date the question requires (e.g. first public
availability or journal publication), check the actual record, and separate
post-cutoff context from eligible evidence. An unverified date cannot establish
eligibility. When the user requests at most N papers, present at most N unique
works across the full answer, not N main works plus a backup bibliography.

If only an abstract is available, restrict the answer to that coverage. If a
figure or SI is inaccessible, state what cannot be checked. Do not silently
convert missing access into evidence of a flaw in the research.
