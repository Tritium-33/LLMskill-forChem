# Repository maintenance

This repository distributes general skills and practical guidance for chemistry
researchers. Keep individual projects, researcher biographies, machine-specific
paths, credentials, chat identifiers and personal automations outside it.

The agreed positioning is “省时的化学科研技能合集”: help chemistry and
materials researchers spend less effort finding, choosing and configuring skills.
Prioritize clear task guidance, straightforward installation, source attribution
and useful examples. Evaluate additions by the user problem they address and
maintenance cost, rather than catalog size. Keep public-facing documentation
focused on users; record maintenance guidance here. Treat time savings as an aim
unless supported by measured usage evidence.

The primary work is curating useful skills across sources, explaining task fit,
and accumulating public usage examples and evidence of usefulness. Installation
tooling supports that work. Prefer upstream reuse and narrow adaptations over
new framework development. Separate linked recommendations from bundled skills,
and packaging validation from observed task performance. The current distribution contains 53 entries across five upstream projects and one local router. Check docs/license-audit before adding or restoring third-party content. Packaging checks do not establish scientific effectiveness.

- Edit `skills/` here as the source of truth. Installed skill folders are copies.
- Keep stable skill names and preserve upstream licenses, notices and provenance.
- Record changes to upstream text in that skill's `SOURCE.json`.
- Keep the installation tool compatible with Python 3.10+ on Windows and Linux,
  using the standard library. Do not require Bash, symlinks or administrator rights.
- Never overwrite untracked or locally edited skills silently. Back up replacements.
- Keep documentation clear about what was tested versus intended compatibility.
- For installer changes run `python -m unittest discover -s tests -v` and
  `python tools/manage.py check`. Documentation-only edits need relevant review.
- Do not add a UI, model API, scheduler or project-specific scientific workflow
  without a concrete request. No account credentials belong in this repository.

## Skill usage reporting

For collection tasks combining skills, use scientific-skill-router to plan the
sequence and report actual skill usage and execution steps before the final result.
Do not impose this format on standalone direct skill calls, ordinary conversation
or repository maintenance. Keep reporting rules in the local router rather than
inserting them into upstream skills. Preserve existing provenance and license notices.
