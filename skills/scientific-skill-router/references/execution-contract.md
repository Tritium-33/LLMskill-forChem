# Execution and delivery contract

Apply to work coordinated by this router. Use existing host tools, not a new
runtime. Higher-priority host/user restrictions remain in force. These are model
instructions, not guarantees that the host will enforce budgets or routing.

## Scope → evidence → result

Maintain a compact internal handoff (in context is sufficient): requested result,
explicit limits, available inputs, next action, evidence locations, unresolved
items, and status (`ready`, `in_progress`, `complete`, `partial`, or `blocked`).
Do not require users to fill a form or write a project directory for a question.
`complete` requires delivery checks below, not merely a successful tool call.

For focused and bounded literature work, work serially by default. Set a finite
search scope around the actual question; a requested maximum number of papers
limits the whole delivered answer, including backup lists. A small candidate
pool may be screened internally without presenting it as exhaustive coverage.
Stop when the requested deliverable is supported or available routes are exhausted.
For a failed retrieval, try a materially different legitimate route, then report
that source unavailable if it still fails. Do not repeatedly retry the same
blocked endpoint or add agents to evade an access failure.

For deep protocols, retain their full requirements. If delegation is authorized
and useful, assign disjoint questions, required evidence, a finite tool/iteration
or time allowance supported by the host, and a clear stopping condition. Default
to one generation of workers with no worker-to-worker spawning; do not start
replacement workers on a concurrency-limit error. If a selected protocol needs a
different arrangement, state the bounded arrangement before starting. Reuse
retrieved sources instead of independent duplicate searches unless independence
is the point of the task. Do not invent token counts or quotas unavailable to you.

## Close work before a final answer

Collect and inspect delegated results before depending on them. A worker's
completion notice is not verification of its sources. For every launched task,
observe completion/failure/cancellation or explicitly mark its status unknown.
If blocked or out of budget, cancel outstanding work where supported and report
the partial result; if cancellation is unavailable, disclose outstanding work
without implying it will arrive after the final answer. Do not claim completion
based on an intended file, a progress message, or a nonexistent artifact.

Before delivery, check:

1. The user question is answered directly, with explicit length/date/reference
   limits applied to the entire reply. No extra list outside a requested cap.
2. Each decisive claim has a matching source or an explicit inference/uncertainty
   label. Preserve qualifications that affect the conclusion.
3. Any cited output file exists and was inspected. Important results are readable
   in chat; use files as supporting detail unless the user requested files only.
4. Outstanding work, missing evidence, failed tools, and partial coverage are
   visible. Do not label an incomplete deep audit exhaustive or verified.

## Observation is separate from policy

An instruction file on disk is not evidence it reached the model. A skill exposed
in the catalog is not evidence it loaded. A successful skill read is not evidence
its scientific procedure was followed. Host integration tests must examine actual
initial messages and returned tool events; do not infer these from profile names.
This router cannot enforce its own invocation or intercept final answers. The
repository's optional run-evidence checker audits exported observations only;
it is not required for ordinary use or standalone skill installation.
