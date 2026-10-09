# 科研技能功能目录

按任务选择技能，来源仅用于追溯与许可说明。包含52项具体技能及独立的 `scientific-skill-router` 选择入口。技能文件已收录，不表示依赖已安装或科学效果已验证。

## 运行与作业支持（3项）

仅在所选科学技能确有需要时加载；安装软件、凭据配置和提交作业是独立操作，不因加载技能自动执行。

| 技能 | 中文用途 | 来源 |
| --- | --- | --- |
| [dpdisp-submit](../skills/dpdisp-submit/SKILL.md) | 通过 DPDispatcher 管理已获授权的本地或集群作业 | [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/5c19e75b256d49849574c999b1965d94024ee072/tools/dpdisp-submit/SKILL.md) |
| [uv](../skills/uv/SKILL.md) | 配置 uv 并运行带独立依赖的 Python 脚本 | [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills/blob/68832757cbbf941c620b71df5756cf6e5cc287b0/skills/uv/SKILL.md) |
| [credentials](../skills/credentials/SKILL.md) | 检查服务凭据是否就绪，避免在会话中暴露密钥 | [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills/blob/68832757cbbf941c620b71df5756cf6e5cc287b0/skills/credentials/SKILL.md) |

## 化学与材料（19项）

输入通常为结构、分子、光谱、热力学数据库或动力学机制；根据科学对象选择，不把分子工具套用于周期晶体。

| 技能 | 中文用途 | 来源 |
| --- | --- | --- |
| [analytical-method-validation](../skills/analytical-method-validation/SKILL.md) | 分析方法的准确度、精密度与检出限验证 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/analytical-method-validation/SKILL.md) |
| [cantera](../skills/cantera/SKILL.md) | 化学反应动力学、反应器与点火延迟 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/cantera/SKILL.md) |
| [datamol](../skills/datamol/SKILL.md) | 常用分子标准化、描述符和构象处理 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/datamol/SKILL.md) |
| [deepchem](../skills/deepchem/SKILL.md) | 分子性质预测、特征化与化学机器学习 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/deepchem/SKILL.md) |
| [matchms](../skills/matchms/SKILL.md) | 串联质谱清理、相似度与谱库匹配 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/matchms/SKILL.md) |
| [medchem](../skills/medchem/SKILL.md) | 药物化学结构警示与分子库筛选 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/medchem/SKILL.md) |
| [molecular-dynamics](../skills/molecular-dynamics/SKILL.md) | OpenMM分子动力学与轨迹分析 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/molecular-dynamics/SKILL.md) |
| [molfeat](../skills/molfeat/SKILL.md) | 分子指纹、描述符与预训练分子表征 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/molfeat/SKILL.md) |
| [nmrglue](../skills/nmrglue/SKILL.md) | 一维核磁原始数据处理、谱峰与积分 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/nmrglue/SKILL.md) |
| [pybamm](../skills/pybamm/SKILL.md) | 电池充放电建模与参数敏感性分析 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pybamm/SKILL.md) |
| [pycalphad](../skills/pycalphad/SKILL.md) | 基于热力学数据库的相平衡计算 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pycalphad/SKILL.md) |
| [pymatgen](../skills/pymatgen/SKILL.md) | 晶体结构、材料数据与电子结构文件分析 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymatgen/SKILL.md) |
| [pyopenms](../skills/pyopenms/SKILL.md) | 液相色谱质谱数据处理与特征检测 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pyopenms/SKILL.md) |
| [rdkit](../skills/rdkit/SKILL.md) | 分子结构、描述符、指纹与子结构检索 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/rdkit/SKILL.md) |
| [uncertainty-and-units](../skills/uncertainty-and-units/SKILL.md) | 物理单位检查、误差传播与不确定度预算 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/uncertainty-and-units/SKILL.md) |
| [mat-dft-vasp](../skills/mat-dft-vasp/SKILL.md) | VASP 输入准备与结果提取；需另配上游运行环境 | [learningmatter-mit/AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills/blob/62574443f2a772e23dd5951f3712b65133b06715/skills/mat-dft-vasp/SKILL.md) |
| [dft-vasp](../skills/dft-vasp/SKILL.md) | 准备 VASP 静态、优化、DOS 与能带输入，不自动提交 | [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/5c19e75b256d49849574c999b1965d94024ee072/quantum-chemistry/dft-vasp/SKILL.md) |
| [dft-qe](../skills/dft-qe/SKILL.md) | 根据结构与指定参数准备 Quantum ESPRESSO 输入 | [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/5c19e75b256d49849574c999b1965d94024ee072/quantum-chemistry/dft-qe/SKILL.md) |
| [dpdata-cli](../skills/dpdata-cli/SKILL.md) | 原子结构和计算数据格式转换 | [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/5c19e75b256d49849574c999b1965d94024ee072/tools/dpdata-cli/SKILL.md) |

## 科研检索与论证（15项）

按找资料、核书目、证据综合、形成假设、设计实验和评阅区分；检索获得记录不等于已读全文。

| 技能 | 中文用途 | 来源 |
| --- | --- | --- |
| [citation-management](../skills/citation-management/SKILL.md) | 书目信息获取、引用核对与BibTeX生成 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/citation-management/SKILL.md) |
| [experimental-design](../skills/experimental-design/SKILL.md) | 实验设计、随机化、分区组与因素组合 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/experimental-design/SKILL.md) |
| [hypothesis-generation](../skills/hypothesis-generation/SKILL.md) | 将观察转化为可检验假设与区分性预测 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/hypothesis-generation/SKILL.md) |
| [lit-review](../skills/lit-review/SKILL.md) | 围绕明确研究主张检索近邻工作，记录检索、阅读和证据缺口。 | [BootLoops-ai/skills](https://github.com/BootLoops-ai/skills/blob/ca892277dcf0468d995f0036f3bd6d753a8afe7d/skills/lit-review/SKILL.md) |
| [literature-review](../skills/literature-review/SKILL.md) | 系统、范围与叙述综述的检索筛选和综合 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/literature-review/SKILL.md) |
| [paper-lookup](../skills/paper-lookup/SKILL.md) | 跨学术数据库检索论文、引文与开放全文 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/paper-lookup/SKILL.md) |
| [peer-review](../skills/peer-review/SKILL.md) | 有证据支持的论文评阅与修订意见 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/peer-review/SKILL.md) |
| [reading-contract](../skills/reading-contract/SKILL.md) | 逐条核对论文或记录中的证据，区分事实、推断和未核实内容。 | [BootLoops-ai/skills](https://github.com/BootLoops-ai/skills/blob/ca892277dcf0468d995f0036f3bd6d753a8afe7d/skills/reading-contract/SKILL.md) |
| [ref-check](../skills/ref-check/SKILL.md) | 核对书目信息及引用是否支持正文，给出可追溯的修改建议。 | [BootLoops-ai/skills](https://github.com/BootLoops-ai/skills/blob/ca892277dcf0468d995f0036f3bd6d753a8afe7d/skills/ref-check/SKILL.md) |
| [research-lookup](../skills/research-lookup/SKILL.md) | 通过外部搜索服务汇集科研证据与背景 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/research-lookup/SKILL.md) |
| [scholar-evaluation](../skills/scholar-evaluation/SKILL.md) | 对科研作品进行可追溯的质量评估 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scholar-evaluation/SKILL.md) |
| [scientific-brainstorming](../skills/scientific-brainstorming/SKILL.md) | 生成和比较候选研究方向及其关键假设 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-brainstorming/SKILL.md) |
| [scientific-critical-thinking](../skills/scientific-critical-thinking/SKILL.md) | 审查科研主张、证据质量与混杂因素 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-critical-thinking/SKILL.md) |
| [literature-search-arxiv](../skills/literature-search-arxiv/SKILL.md) | 检索 arXiv 预印本、下载论文及源文件 | [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills/blob/68832757cbbf941c620b71df5756cf6e5cc287b0/skills/literature_search_arxiv/SKILL.md) |
| [literature-search-openalex](../skills/literature-search-openalex/SKILL.md) | 检索 OpenAlex 论文、作者、机构及引文元数据 | [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills/blob/68832757cbbf941c620b71df5756cf6e5cc287b0/skills/literature_search_openalex/SKILL.md) |

## 数据、统计与机器学习（9项）

先明确解释、推断、预测还是优化目标；若任务只需基础统计，不强制建立机器学习模型。

| 技能 | 中文用途 | 来源 |
| --- | --- | --- |
| [exploratory-data-analysis](../skills/exploratory-data-analysis/SKILL.md) | 科学数据的结构、缺失值和异常值探索 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/exploratory-data-analysis/SKILL.md) |
| [independence-bookkeeping](../skills/independence-bookkeeping/SKILL.md) | 检查验证路线的共享依赖、数据使用历史与循环验证。 | [BootLoops-ai/skills](https://github.com/BootLoops-ai/skills/blob/ca892277dcf0468d995f0036f3bd6d753a8afe7d/skills/independence-bookkeeping/SKILL.md) |
| [pymc](../skills/pymc/SKILL.md) | 贝叶斯建模、后验检查与不确定度推断 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymc/SKILL.md) |
| [pymoo](../skills/pymoo/SKILL.md) | 多目标优化、约束与帕累托解分析 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymoo/SKILL.md) |
| [scikit-learn](../skills/scikit-learn/SKILL.md) | 机器学习预处理、建模与交叉验证 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scikit-learn/SKILL.md) |
| [shap](../skills/shap/SKILL.md) | 模型预测的特征归因、解释与诊断 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/shap/SKILL.md) |
| [statistical-analysis](../skills/statistical-analysis/SKILL.md) | 统计检验选择、假设检查与效应量报告 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-analysis/SKILL.md) |
| [statistical-power](../skills/statistical-power/SKILL.md) | 样本量、重复数和统计功效规划 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-power/SKILL.md) |
| [statsmodels](../skills/statsmodels/SKILL.md) | 回归、广义线性模型和时间序列诊断 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statsmodels/SKILL.md) |

## 写作与图表（6项）

区分真实数据图、概念示意图、文稿与幻灯片；外部图像服务不是真实数据绘图的必需工具。

| 技能 | 中文用途 | 来源 |
| --- | --- | --- |
| [markitdown](../skills/markitdown/SKILL.md) | 将PDF、Office等文档转换为Markdown | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/markitdown/SKILL.md) |
| [scientific-schematics](../skills/scientific-schematics/SKILL.md) | 通过外部图像模型生成科学示意图草稿 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-schematics/SKILL.md) |
| [scientific-slides](../skills/scientific-slides/SKILL.md) | 科研汇报幻灯片结构、制作与视觉检查 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-slides/SKILL.md) |
| [scientific-visualization](../skills/scientific-visualization/SKILL.md) | 多面板科研图设计、单位与可读性检查 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-visualization/SKILL.md) |
| [scientific-writing](../skills/scientific-writing/SKILL.md) | 有证据溯源的科研论文撰写与一致性检查 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-writing/SKILL.md) |
| [seaborn](../skills/seaborn/SKILL.md) | 分布、分组比较与统计关系可视化 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/seaborn/SKILL.md) |

## 如何选择

直接描述任务，或使用 `$scientific-skill-router`。同一板块可以包含不同来源的技能；根据具体任务、输入和依赖选择，不以来源决定优先级。

- 找论文：`paper-lookup`；组织综述：`literature-review`；深入审查创新性：`lit-review`。
- 生成/整理书目：`citation-management`；严格核验书目：`ref-check`；核对原文证据：`reading-contract`。
- 建模与交叉验证：`scikit-learn`；审查数据接触历史与验证独立性：`independence-bookkeeping`。

## 依赖与使用限制

以下是上游声明或原文指引，安装时没有逐项运行全部科学任务。外部API和科学软件需按任务确认。

- **analytical-method-validation**：Requires Python 3.11+. Scripts use only the standard library - no numpy, scipy, or network access. Statistical distributions are computed from first principles so results are reproducible in any conforming interpreter.
- **cantera**：Requires Python 3.12-3.14, Cantera 3.2.0, and NumPy. Installation needs network access; simulations run locally without credentials. Custom mechanisms must be available as Cantera YAML files.
- **datamol**：Requires Python 3.11+ and datamol 0.13.0 with RDKit 2024.09+. Installation needs network access; local molecular workflows need no credentials. Remote I/O needs the selected provider credentials.
- **deepchem**：Requires Python 3.11 for the tested DeepChem 2.8.0 stack. Molecular workflows need RDKit. Torch, Transformers, torch-geometric or DGL/DGL-LifeSci depend on the chosen model. Network is needed only for package, benchmark or model downloads.
- **matchms**：Requires Python >=3.10,<3.15, uv, and matchms 0.33.1. Local file workflows need no credentials; metabolomics-USI loading requires network access.
- **medchem**：Requires Python 3.11+ with medchem, datamol, and RDKit. Optional Lilly demerits require native tools built with medchem install-lilly, a C++ compiler, make, zlib, and Ruby; installation needs network access. Other filters run locally without credentials.
- **molecular-dynamics**：Requires Python 3.11+ with OpenMM and MDAnalysis; matplotlib for plots. Optional PDBFixer and OpenFF need separate installation. Network access for installation; local simulation and analysis run offline.
- **molfeat**：Requires Python 3.11+ and molfeat 1.0.0 (RDKit, datamol, PyTorch). macOS Intel needs Python 3.11–3.12 and upstream platform-specific dependency pins. Optional extras and network access are needed for pretrained models; core fingerprints run offline.
- **nmrglue**：Requires Python 3.12+, nmrglue, NumPy 2+, and SciPy. Installation needs network access; processing is local and needs no credentials.
- **pybamm**：Requires Python 3.12 with PyBaMM 26.9.0.0 and pybammsolvers 0.10.0 (IDAKLU). NumPy and CasADi are supplied by PyBaMM. Network is needed for installation and optional upstream dataset retrieval; bundled simulations and CSV comparisons run locally without credentials.
- **pycalphad**：Requires Python 3.12+, pycalphad 0.11.2, and NumPy. Installation needs network access; calculations run locally without credentials. Real-material predictions require a suitable licensed thermodynamic database.
- **pymatgen**：Python 3.11+ with uv. The verified snapshot uses pymatgen 2026.9.24, pymatgen-core 2026.9.23, and mp-api 0.46.5. Bundled help and planning CLIs use only the standard library; local scientific execution lazily requires the pinned pymatgen packages. Materials Project access additionally requires explicit network approval and the single named secret MP_API_KEY.
- **pyopenms**：Requires CPython 3.11+ and pyOpenMS 3.6.0; pandas and NumPy for tables, Matplotlib for plots. Wheels support macOS 15+ arm64, Linux glibc 2.34+ x86-64/arm64, and Windows x86-64. Search-engine executables are separate.
- **rdkit**：Tested with RDKit 2026.03.6 on Python 3.13; bundled scripts require the rdkit package. No credentials or network are needed after installation. Use conda-forge for the broadest binary support or PyPI package `rdkit` for supported platform wheels; `rdkit-pypi` is the legacy PyPI name.
- **uncertainty-and-units**：Requires Python 3.12+. The numeric CLIs need pint, uncertainties, NumPy, and SciPy; the static auditor is standard-library only. All bundled tooling runs locally with no network access.
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
- **exploratory-data-analysis**：Bundled core CLIs require Python 3.11+ and are local/network-free; the complete pinned optional snapshot requires Python 3.12+, uv, and format-specific libraries listed below.
- **independence-bookkeeping**：Read the skill for runtime requirements.
- **pymc**：Requires Python 3.12+ with PyMC 6.3.2, PyTensor 3.3.2 and ArviZ 1.3-compatible dependencies; NumPy, pandas, Matplotlib, h5netcdf and h5py for bundled helpers/artifacts. Network access for installation only. Optional nutpie, NumPyro and BlackJAX samplers need separate dependencies.
- **pymoo**：Requires Python 3.10+ and pymoo 0.6.2 with its NumPy, SciPy, matplotlib and autograd dependencies. Optional joblib for parallel runners, optuna for its algorithm wrapper, and dill for checkpoints. Network needed for installation only.
- **scikit-learn**：Requires Python 3.11+ and scikit-learn 1.9.1. NumPy, SciPy, and joblib are dependencies; bundled scripts also require pandas and matplotlib. Installation needs network access; bundled examples use local datasets without credentials.
- **shap**：Requires Python 3.12+ and uv for SHAP 0.52.0; model-specific libraries are optional.
- **statistical-analysis**：Requires Python 3.12+ and the documented isolated scientific Python environment; network access only for installation and documentation.
- **statistical-power**：Requires Python >=3.12 with statsmodels, scipy, numpy, pandas, and matplotlib. Optional comparison uses pingouin; survival extensions use lifelines (requires pandas<3). Installation needs network access unless packages are cached. Calculations run locally without credentials.
- **statsmodels**：Requires Python 3.10+ and statsmodels 0.15.0; the tested NumPy 2.5.3/SciPy 1.18.1 stack needs Python 3.12+. Plotting needs matplotlib; predictive metrics need scikit-learn. Network access is needed only for installation or documentation; no credentials.
- **markitdown**：Python >=3.10,<3.15 and uv. Examples target MarkItDown 0.1.8. Core local conversion can run offline; URL, YouTube, audio transcription, LLM, Azure, and MCP workflows may use network or external services.
- **scientific-schematics**：Requires Python 3.10+ with requests, network access, and an OpenRouter API key.
- **scientific-slides**：Python 3.12+; requests for OpenRouter generation, Pillow for image PDFs, PyMuPDF for rendering, pypdf and python-pptx for validation and template editing. Generation needs network and OPENROUTER_API_KEY. Beamer needs TeX Live/MiKTeX; programmatic PPTX needs Node.js and PptxGenJS; rendering PPTX for review needs LibreOffice.
- **scientific-visualization**：Requires Python 3.11+ and uv for pinned examples. Bundled CLIs are network-free and load Matplotlib, Pillow, or pypdf only when needed. Plotly static export with Kaleido v1 requires a compatible Chrome/Chromium installation.
- **scientific-writing**：Requires Python 3.11+ only for optional dependency-free local CLIs; core guidance is platform-neutral. Bundled tools are offline and require no API keys.
- **seaborn**：Requires Python 3.8+ with seaborn 0.13.2, NumPy, pandas, and Matplotlib; the tested current dependency stack requires Python 3.12+. Optional scipy/statsmodels for advanced regression or clustering, ipywidgets for notebook controls. Network only for installation or uncached example datasets.
- **mat-dft-vasp**：Read the skill for runtime requirements.
- **dft-vasp**：Requires a user-provided structure and valid VASP pseudopotential resources/license in the target environment.
- **dft-qe**：Requires a user-provided initial structure and enough DFT parameters to build a scientifically meaningful QE input.
- **dpdata-cli**：Requires uvx (uv) for running dpdata
- **dpdisp-submit**：Read the skill for runtime requirements.
- **literature-search-arxiv**：Read the skill for runtime requirements.
- **literature-search-openalex**：Read the skill for runtime requirements.
- **uv**：Read the skill for runtime requirements.
- **credentials**：Read the skill for runtime requirements.
