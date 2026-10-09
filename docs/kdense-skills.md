# K-Dense 化学与通用科研技能（42项）

固定版本：`92ace75ac21efe19a620434e0ca4e356081fe807`。英文名称与上游 SKILL.md 保持不变，中文仅说明用途。

技能与支持文件已收录，运行依赖按任务单独准备；安装不等于科学效果验证，也不等于所有脚本可立即执行。无需一次加载全部技能。

文献检索优先考虑 paper-lookup；research-lookup 涉及外部服务认证。scientific-schematics 需要 OpenRouter，scientific-slides 部分生成路径也需要它。未配置密钥时不得声称这些路径已可用。

现有 lit-review/ref-check 保留：分别用于深入文献审查与严格参考文献核验；本批 literature-review/citation-management 提供不同的综述和书目工作流程。

本批排除临床、基因组学、无关学科、云实验室集成与自动修改技能的元工具。molecular-dynamics 主要面向生物分子/小分子，不能据此声称支持周期性材料的第一性原理分子动力学。

## 化学与材料

| 英文名称及来源 | 中文用途 |
| --- | --- |
| [pymatgen](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymatgen/SKILL.md) | 晶体结构、材料数据与电子结构文件分析 |
| [rdkit](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/rdkit/SKILL.md) | 分子结构、描述符、指纹与子结构检索 |
| [datamol](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/datamol/SKILL.md) | 常用分子标准化、描述符和构象处理 |
| [deepchem](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/deepchem/SKILL.md) | 分子性质预测、特征化与化学机器学习 |
| [molfeat](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/molfeat/SKILL.md) | 分子指纹、描述符与预训练分子表征 |
| [medchem](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/medchem/SKILL.md) | 药物化学结构警示与分子库筛选 |
| [molecular-dynamics](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/molecular-dynamics/SKILL.md) | OpenMM分子动力学与轨迹分析 |
| [cantera](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/cantera/SKILL.md) | 化学反应动力学、反应器与点火延迟 |
| [pycalphad](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pycalphad/SKILL.md) | 基于热力学数据库的相平衡计算 |
| [pybamm](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pybamm/SKILL.md) | 电池充放电建模与参数敏感性分析 |
| [nmrglue](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/nmrglue/SKILL.md) | 一维核磁原始数据处理、谱峰与积分 |
| [matchms](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/matchms/SKILL.md) | 串联质谱清理、相似度与谱库匹配 |
| [pyopenms](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pyopenms/SKILL.md) | 液相色谱质谱数据处理与特征检测 |
| [analytical-method-validation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/analytical-method-validation/SKILL.md) | 分析方法的准确度、精密度与检出限验证 |
| [uncertainty-and-units](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/uncertainty-and-units/SKILL.md) | 物理单位检查、误差传播与不确定度预算 |

## 科研检索与论证

| 英文名称及来源 | 中文用途 |
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

## 数据统计与机器学习

| 英文名称及来源 | 中文用途 |
| --- | --- |
| [exploratory-data-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/exploratory-data-analysis/SKILL.md) | 科学数据的结构、缺失值和异常值探索 |
| [statistical-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-analysis/SKILL.md) | 统计检验选择、假设检查与效应量报告 |
| [statistical-power](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-power/SKILL.md) | 样本量、重复数和统计功效规划 |
| [statsmodels](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statsmodels/SKILL.md) | 回归、广义线性模型和时间序列诊断 |
| [scikit-learn](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scikit-learn/SKILL.md) | 机器学习预处理、建模与交叉验证 |
| [pymc](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymc/SKILL.md) | 贝叶斯建模、后验检查与不确定度推断 |
| [pymoo](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymoo/SKILL.md) | 多目标优化、约束与帕累托解分析 |
| [shap](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/shap/SKILL.md) | 模型预测的特征归因、解释与诊断 |
| [sympy](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/sympy/SKILL.md) | 符号代数、微积分与精确公式推导 |

## 写作与图表

| 英文名称及来源 | 中文用途 |
| --- | --- |
| [scientific-writing](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-writing/SKILL.md) | 有证据溯源的科研论文撰写与一致性检查 |
| [matplotlib](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/matplotlib/SKILL.md) | 精细控制科研图表并导出出版格式 |
| [seaborn](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/seaborn/SKILL.md) | 分布、分组比较与统计关系可视化 |
| [scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-visualization/SKILL.md) | 多面板科研图设计、单位与可读性检查 |
| [scientific-schematics](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-schematics/SKILL.md) | 通过外部图像模型生成科学示意图草稿 |
| [scientific-slides](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-slides/SKILL.md) | 科研汇报幻灯片结构、制作与视觉检查 |
| [venue-templates](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/venue-templates/SKILL.md) | 期刊会议模板选择与投稿格式检查 |
| [markitdown](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/markitdown/SKILL.md) | 将PDF、Office等文档转换为Markdown |

## 运行依赖（上游声明，未逐项实测）

- **pymatgen**：Python 3.11+ with uv. The verified snapshot uses pymatgen 2026.9.24, pymatgen-core 2026.9.23, and mp-api 0.46.5. Bundled help and planning CLIs use only the standard library; local scientific execution lazily requires the pinned pymatgen packages. Materials Project access additionally requires explicit network approval and the single named secret MP_API_KEY.
- **rdkit**：Tested with RDKit 2026.03.6 on Python 3.13; bundled scripts require the rdkit package. No credentials or network are needed after installation. Use conda-forge for the broadest binary support or PyPI package `rdkit` for supported platform wheels; `rdkit-pypi` is the legacy PyPI name.
- **datamol**：Requires Python 3.11+ and datamol 0.13.0 with RDKit 2024.09+. Installation needs network access; local molecular workflows need no credentials. Remote I/O needs the selected provider credentials.
- **deepchem**：Requires Python 3.11 for the tested DeepChem 2.8.0 stack. Molecular workflows need RDKit. Torch, Transformers, torch-geometric or DGL/DGL-LifeSci depend on the chosen model. Network is needed only for package, benchmark or model downloads.
- **molfeat**：Requires Python 3.11+ and molfeat 1.0.0 (RDKit, datamol, PyTorch). macOS Intel needs Python 3.11–3.12 and upstream platform-specific dependency pins. Optional extras and network access are needed for pretrained models; core fingerprints run offline.
- **medchem**：Requires Python 3.11+ with medchem, datamol, and RDKit. Optional Lilly demerits require native tools built with medchem install-lilly, a C++ compiler, make, zlib, and Ruby; installation needs network access. Other filters run locally without credentials.
- **molecular-dynamics**：Requires Python 3.11+ with OpenMM and MDAnalysis; matplotlib for plots. Optional PDBFixer and OpenFF need separate installation. Network access for installation; local simulation and analysis run offline.
- **cantera**：Requires Python 3.12-3.14, Cantera 3.2.0, and NumPy. Installation needs network access; simulations run locally without credentials. Custom mechanisms must be available as Cantera YAML files.
- **pycalphad**：Requires Python 3.12+, pycalphad 0.11.2, and NumPy. Installation needs network access; calculations run locally without credentials. Real-material predictions require a suitable licensed thermodynamic database.
- **pybamm**：Requires Python 3.12 with PyBaMM 26.9.0.0 and pybammsolvers 0.10.0 (IDAKLU). NumPy and CasADi are supplied by PyBaMM. Network is needed for installation and optional upstream dataset retrieval; bundled simulations and CSV comparisons run locally without credentials.
- **nmrglue**：Requires Python 3.12+, nmrglue, NumPy 2+, and SciPy. Installation needs network access; processing is local and needs no credentials.
- **matchms**：Requires Python >=3.10,<3.15, uv, and matchms 0.33.1. Local file workflows need no credentials; metabolomics-USI loading requires network access.
- **pyopenms**：Requires CPython 3.11+ and pyOpenMS 3.6.0; pandas and NumPy for tables, Matplotlib for plots. Wheels support macOS 15+ arm64, Linux glibc 2.34+ x86-64/arm64, and Windows x86-64. Search-engine executables are separate.
- **analytical-method-validation**：Requires Python 3.11+. Scripts use only the standard library - no numpy, scipy, or network access. Statistical distributions are computed from first principles so results are reproducible in any conforming interpreter.
- **uncertainty-and-units**：Requires Python 3.12+. The numeric CLIs need pint, uncertainties, NumPy, and SciPy; the static auditor is standard-library only. All bundled tooling runs locally with no network access.
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
- **exploratory-data-analysis**：Bundled core CLIs require Python 3.11+ and are local/network-free; the complete pinned optional snapshot requires Python 3.12+, uv, and format-specific libraries listed below.
- **statistical-analysis**：Requires Python 3.12+ and the documented isolated scientific Python environment; network access only for installation and documentation.
- **statistical-power**：Requires Python >=3.12 with statsmodels, scipy, numpy, pandas, and matplotlib. Optional comparison uses pingouin; survival extensions use lifelines (requires pandas<3). Installation needs network access unless packages are cached. Calculations run locally without credentials.
- **statsmodels**：Requires Python 3.10+ and statsmodels 0.15.0; the tested NumPy 2.5.3/SciPy 1.18.1 stack needs Python 3.12+. Plotting needs matplotlib; predictive metrics need scikit-learn. Network access is needed only for installation or documentation; no credentials.
- **scikit-learn**：Requires Python 3.11+ and scikit-learn 1.9.1. NumPy, SciPy, and joblib are dependencies; bundled scripts also require pandas and matplotlib. Installation needs network access; bundled examples use local datasets without credentials.
- **pymc**：Requires Python 3.12+ with PyMC 6.3.2, PyTensor 3.3.2 and ArviZ 1.3-compatible dependencies; NumPy, pandas, Matplotlib, h5netcdf and h5py for bundled helpers/artifacts. Network access for installation only. Optional nutpie, NumPyro and BlackJAX samplers need separate dependencies.
- **pymoo**：Requires Python 3.10+ and pymoo 0.6.2 with its NumPy, SciPy, matplotlib and autograd dependencies. Optional joblib for parallel runners, optuna for its algorithm wrapper, and dill for checkpoints. Network needed for installation only.
- **shap**：Requires Python 3.12+ and uv for SHAP 0.52.0; model-specific libraries are optional.
- **sympy**：Requires Python 3.9+ and SymPy 1.14.0. Optional NumPy/SciPy/Matplotlib, IPython/ipywidgets, or ANTLR 4.11 parser runtime for relevant examples. Compiled wrappers need a C/Fortran compiler and backend packages; emitting source needs no compiler. Network only for installation/docs.
- **scientific-writing**：Requires Python 3.11+ only for optional dependency-free local CLIs; core guidance is platform-neutral. Bundled tools are offline and require no API keys.
- **matplotlib**：Requires Python 3.11+ and Matplotlib 3.11.2. Bundled examples also use NumPy and SciPy; pandas examples need pandas, and Jupyter widgets need ipympl. Installation needs network access; local plotting needs no credentials.
- **seaborn**：Requires Python 3.8+ with seaborn 0.13.2, NumPy, pandas, and Matplotlib; the tested current dependency stack requires Python 3.12+. Optional scipy/statsmodels for advanced regression or clustering, ipywidgets for notebook controls. Network only for installation or uncached example datasets.
- **scientific-visualization**：Requires Python 3.11+ and uv for pinned examples. Bundled CLIs are network-free and load Matplotlib, Pillow, or pypdf only when needed. Plotly static export with Kaleido v1 requires a compatible Chrome/Chromium installation.
- **scientific-schematics**：Requires Python 3.10+ with requests, network access, and an OpenRouter API key.
- **scientific-slides**：Python 3.12+; requests for OpenRouter generation, Pillow for image PDFs, PyMuPDF for rendering, pypdf and python-pptx for validation and template editing. Generation needs network and OPENROUTER_API_KEY. Beamer needs TeX Live/MiKTeX; programmatic PPTX needs Node.js and PptxGenJS; rendering PPTX for review needs LibreOffice.
- **venue-templates**：Requires Python 3.11+ for helper scripts; LaTeX and Poppler command-line tools are optional for compilation and PDF inspection. Needs network access to verify current venue instructions.
- **markitdown**：Python >=3.10,<3.15 and uv. Examples target MarkItDown 0.1.8. Core local conversion can run offline; URL, YouTube, audio transcription, LLM, Azure, and MCP workflows may use network or external services.

## 调用

`$pymatgen 检查这个结构的元素顺序、晶胞和周期性边界。`

也可直接描述任务，例如“检索这个主题的论文并保留 DOI 和来源”“检查这组测量值的单位与误差传播”。自动选择取决于任务与技能描述的匹配，不保证每次选中预期技能。

仓库维护源为 skills/；安装器仍只需要 Python 3.10+，但技能内部软件有各自的 Python/系统要求。Windows 能复制安装技能不等于所有科学依赖均兼容 Windows。
