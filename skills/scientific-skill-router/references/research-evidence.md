# 科研检索与论证

按找资料、核书目、证据综合、形成假设、设计实验和评阅区分；检索获得记录不等于已读全文。

表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。

| 技能 | 用于什么任务 | 来源 |
| --- | --- | --- |
| `citation-management` | 书目信息获取、引用核对与BibTeX生成 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/citation-management/SKILL.md) |
| `experimental-design` | 实验设计、随机化、分区组与因素组合 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/experimental-design/SKILL.md) |
| `hypothesis-generation` | 将观察转化为可检验假设与区分性预测 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/hypothesis-generation/SKILL.md) |
| `lit-review` | 围绕明确研究主张检索近邻工作，记录检索、阅读和证据缺口。 | [BootLoops-ai/skills](https://github.com/BootLoops-ai/skills/blob/ca892277dcf0468d995f0036f3bd6d753a8afe7d/skills/lit-review/SKILL.md) |
| `literature-review` | 系统、范围与叙述综述的检索筛选和综合 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/literature-review/SKILL.md) |
| `paper-lookup` | 跨学术数据库检索论文、引文与开放全文 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/paper-lookup/SKILL.md) |
| `peer-review` | 有证据支持的论文评阅与修订意见 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/peer-review/SKILL.md) |
| `reading-contract` | 逐条核对论文或记录中的证据，区分事实、推断和未核实内容。 | [BootLoops-ai/skills](https://github.com/BootLoops-ai/skills/blob/ca892277dcf0468d995f0036f3bd6d753a8afe7d/skills/reading-contract/SKILL.md) |
| `ref-check` | 核对书目信息及引用是否支持正文，给出可追溯的修改建议。 | [BootLoops-ai/skills](https://github.com/BootLoops-ai/skills/blob/ca892277dcf0468d995f0036f3bd6d753a8afe7d/skills/ref-check/SKILL.md) |
| `research-lookup` | 通过外部搜索服务汇集科研证据与背景 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/research-lookup/SKILL.md) |
| `scholar-evaluation` | 对科研作品进行可追溯的质量评估 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scholar-evaluation/SKILL.md) |
| `scientific-brainstorming` | 生成和比较候选研究方向及其关键假设 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-brainstorming/SKILL.md) |
| `scientific-critical-thinking` | 审查科研主张、证据质量与混杂因素 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-critical-thinking/SKILL.md) |

## 选择后再核对依赖

- **citation-management**：Requires Python 3.9+ with requests. Google Scholar search additionally needs scholarly. Needs network access to api.openalex.org, api.crossref.org, eutils.ncbi.nlm.nih.gov, pmc.ncbi.nlm.nih.gov, doi.org, export.arxiv.org, and api.datacite.org.
- **experimental-design**：Requires Python >=3.12 with numpy, pandas, and pydoe 1.5.0 (DOE matrices). Network access is needed only to install packages; no credentials are required.
- **hypothesis-generation**：Python 3.11+ standard library. Bundled CLIs are deterministic and local-only; they accept bounded JSON, CSV, or Markdown and require no network, credentials, models, image services, or external packages.
- **lit-review**：Read the skill for runtime requirements.
- **literature-review**：Python 3.10+ with requests; network for DOI checks and searches. Optional parallel-cli requires Parallel authentication. PDF export needs Pandoc and XeLaTeX; AI schematics need OPENROUTER_API_KEY.
- **paper-lookup**：Needs network access and curl. The bundled scripts require Python 3.11+ and use only the standard library. No credentials are required; NCBI_API_KEY, S2_API_KEY, CORE_API_KEY, and OPENALEX_API_KEY raise rate limits or unlock full text where noted.
- **peer-review**：Python 3.11+ standard library. Bundled CLIs are deterministic and local-only; they accept bounded JSON, CSV, or Markdown and make no network, model, image, or external-service calls.
- **reading-contract**：Read the skill for runtime requirements.
- **ref-check**：Read the skill for runtime requirements.
- **research-lookup**：Requires Python 3.10+ and network access; targets parallel-web-tools CLI 0.9.3 for Search, Extract, and Research. Explicit Chat requires requests and PARALLEL_API_KEY; optional Perplexity through openrouter.ai requires requests and OPENROUTER_API_KEY.
- **scholar-evaluation**：Requires Python 3.11+ for optional bundled standard-library CLIs. All tooling is local JSON/CSV processing with no network, credentials, external models, or subprocesses.
- **scientific-brainstorming**：Core guidance works in any Agent Skills-compatible host. Optional bundled CLIs require Python 3.11+ and use only the standard library; they make no network or LLM calls and require no credentials.
- **scientific-critical-thinking**：Analytical guidance needs no network. Optional figures via the scientific-schematics skill require OPENROUTER_API_KEY and outbound API access to OpenRouter.
