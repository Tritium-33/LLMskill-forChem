# 科研检索与论证

按找资料、核书目、证据综合、形成假设、设计实验和评阅区分；检索获得记录不等于已读全文。

表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。

| 技能及固定来源 | 用于什么任务 |
| --- | --- |
| [paper-lookup](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/paper-lookup/SKILL.md) | 跨学术数据库检索论文、引文与开放全文 |
| [research-lookup](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/research-lookup/SKILL.md) | 通过外部搜索服务汇集科研证据与背景 |
| [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/literature-review/SKILL.md) | 系统、范围与叙述综述的检索筛选和综合 |
| [citation-management](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/citation-management/SKILL.md) | 书目信息获取、引用核对与BibTeX生成 |
| [scientific-critical-thinking](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-critical-thinking/SKILL.md) | 审查科研主张、证据质量与混杂因素 |
| [scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-brainstorming/SKILL.md) | 生成和比较候选研究方向及其关键假设 |
| [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/hypothesis-generation/SKILL.md) | 将观察转化为可检验假设与区分性预测 |
| [experimental-design](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/experimental-design/SKILL.md) | 实验设计、随机化、分区组与因素组合 |
| [peer-review](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/peer-review/SKILL.md) | 有证据支持的论文评阅与修订意见 |
| [scholar-evaluation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scholar-evaluation/SKILL.md) | 对科研作品进行可追溯的质量评估 |

## 选择后再核对依赖

- **paper-lookup**：Needs network access and curl. The bundled scripts require Python 3.11+ and use only the standard library. No credentials are required; NCBI_API_KEY, S2_API_KEY, CORE_API_KEY, and OPENALEX_API_KEY raise rate limits or unlock full text where noted.
- **research-lookup**：Requires Python 3.10+ and network access; targets parallel-web-tools CLI 0.9.3 for Search, Extract, and Research. Explicit Chat requires requests and PARALLEL_API_KEY; optional Perplexity through openrouter.ai requires requests and OPENROUTER_API_KEY.
- **literature-review**：Python 3.10+ with requests; network for DOI checks and searches. Optional parallel-cli requires Parallel authentication. PDF export needs Pandoc and XeLaTeX; AI schematics need OPENROUTER_API_KEY.
- **citation-management**：Requires Python 3.9+ with requests. Google Scholar search additionally needs scholarly. Needs network access to api.openalex.org, api.crossref.org, eutils.ncbi.nlm.nih.gov, pmc.ncbi.nlm.nih.gov, doi.org, export.arxiv.org, and api.datacite.org.
- **scientific-critical-thinking**：Analytical guidance needs no network. Optional figures via the scientific-schematics skill require OPENROUTER_API_KEY and outbound API access to OpenRouter.
- **scientific-brainstorming**：Core guidance works in any Agent Skills-compatible host. Optional bundled CLIs require Python 3.11+ and use only the standard library; they make no network or LLM calls and require no credentials.
- **hypothesis-generation**：Python 3.11+ standard library. Bundled CLIs are deterministic and local-only; they accept bounded JSON, CSV, or Markdown and require no network, credentials, models, image services, or external packages.
- **experimental-design**：Requires Python >=3.12 with numpy, pandas, and pydoe 1.5.0 (DOE matrices). Network access is needed only to install packages; no credentials are required.
- **peer-review**：Python 3.11+ standard library. Bundled CLIs are deterministic and local-only; they accept bounded JSON, CSV, or Markdown and make no network, model, image, or external-service calls.
- **scholar-evaluation**：Requires Python 3.11+ for optional bundled standard-library CLIs. All tooling is local JSON/CSV processing with no network, credentials, external models, or subprocesses.
