# Repository maintenance

This repository distributes general skills and practical guidance for chemistry
researchers. Keep individual projects, researcher biographies, machine-specific
paths, credentials, chat identifiers and personal automations outside it.

The primary work is curating useful skills across sources, explaining task fit,
and accumulating public usage examples and evidence of usefulness. Installation
tooling supports that work. Prefer upstream reuse and narrow adaptations over
new framework development. Separate linked recommendations from bundled skills,
and packaging validation from observed task performance. The current distribution contains four BootLoops protocols, 39 K-Dense skills and one local router. Check docs/license-audit before adding or restoring third-party content. Packaging checks do not establish scientific effectiveness.

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

## 输出前缀：技能与执行记录

每次向用户返回结果时，先列出本轮实际使用的技能及完整的操作步骤，再给出正文。阶段性更新列出截至当前的状态；最终答复覆盖本轮从开始到结束的步骤。

- 技能保留英文名，说明本轮用途；没有使用时写“无”。仅计划使用、目录中可见或仅被提及的技能不能列为已使用。读取指导与实际执行脚本应分别标明。
- 步骤按实际顺序编号，记录读取了什么、调用了哪个工具或脚本、产生了什么结果及完成状态。包含失败、重试、跳过和未完成项；计划另列，不能伪装成已执行。
- 这里的步骤是可核查的操作记录，不要求公开内部推理。无需逐字复制工具输出；不显示密钥、隐私数据或无关环境信息。
- 记录很长时，前缀给出步骤概览并链接完整操作日志；只有实际生成了日志才提供链接。不能为凑记录而额外调用技能。

格式：

```text
【本轮技能】英文名称 — 实际用途；或“无”
【执行步骤】
1. [完成/失败/跳过/未执行] 操作 → 结果或产物。

正文……
```
