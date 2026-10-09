# 化学科研 Skills 来源初筛：GitHub 路线

检索日期：2026-10-08（UTC+8）。这是候选初筛，不是全面文献综述、安装认证或科学正确性审计。未安装、执行或修改所列技能；Windows 原生环境均未实测。本报告只使用公开资料。

结论：优先细读 **K-Dense 的单项化学技能、Google DeepMind 的数据库技能、Computational Chemistry Agent Skills、AtomisticSkills**。它们分别提供轻量分子操作、可追溯数据库查询、计算化学 CLI 工作流和带公开任务的原子模拟方案。小型分子可视化技能可以作为低成本试用候选。**高 star 是关注度；作者报告、第三方复用、独立效果验证分别记录，不能相互替代。**

## 1. 候选总表

Star 是当日查询时工具返回的 GitHub 页面/API 快照，可能有缓存，不是保证即时的计数。多数 API 访问失败，因此没有把页面约数伪装成精确 API 数据。提交数仅说明可见历史，不表示近期活跃程度。

| 项目（正式仓库） | Star 快照 | 维护线索 | 入选依据 | 当前建议 |
|---|---:|---|---|---|
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 47,852（API）；页面约 47.9k | API `pushed_at=2026-10-05T09:39:11Z`；页面 759 commits；RDKit review 更新到 2026-10-01 | 高关注度、真实单项技能、具体测试记录、第三方复用痕迹 | 优先筛单项，不整库搬入 |
| [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills) | 约 3.2k | 页面 10 commits；有公开技术报告与许可证清单 | 高关注度、数据库脚本、作者对照评估 | 优先选 ChEMBL/PubChem 一类小任务 |
| [learningmatter-mit/AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) | 175（页面） | 页面 722 commits；公开 benchmark 仓库 | 领域直接相关、真实技能和可检查的评测任务 | 先链接推荐，再按任务适配 |
| [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills) | 148（页面） | 页面 138 commits、8 个开放 PR | 领域直接相关、CLI 技能；README 列出 JCTC DOI，发表状态另核 | 优先 RDKit/数据转换等小任务 |
| [ghutchis/chem-skill](https://github.com/ghutchis/chem-skill) | 4（页面） | 页面 5 commits；没有据此认定持续维护 | 输出明确、范围小，非高 star 项目 | 候补：轻度修整后试用 |
| [lamm-mit/scienceclaw](https://github.com/lamm-mit/scienceclaw) | 244（页面） | 页面 138 commits；有 tests/、benchmarks/ | 原生技能集合、可核第三方复用关系 | 借鉴单项和产物记录，不引入整个平台 |
| [Hongyu-yu/matsci-ai-skills](https://github.com/Hongyu-yu/matsci-ai-skills) | 19（页面） | 页面 3 commits；中文 README | 接近“按材料学任务分类”的整理库 | 目录组织参考，证据仍弱 |
| [jskherman/engg-skills](https://github.com/jskherman/engg-skills) | 9（页面；较旧搜索缓存为 8） | 页面 53 commits；tests/ 与验证工具 | 补充化工方向，原生技能与计算后端说明 | 观察候选，先检查工程方法假设 |
| [BootLoops-ai/skills](https://github.com/BootLoops-ai/skills) | 23（页面） | 页面 1 commit | 研究质量协议；作为已有来源的比较基线 | 保留方法类价值，不能当化学能力全集 |

K-Dense 的精确计数来源：[GitHub API](https://api.github.com/repos/K-Dense-AI/scientific-agent-skills)，字段 `stargazers_count`、`pushed_at`。其他计数与提交数均来自上表仓库首页的 Stars/History；最近提交日期未核实，不作“近期活跃”结论。

## 2. 逐项核查

### A. K-Dense Scientific Agent Skills

- **实际打开**：[README](https://github.com/K-Dense-AI/scientific-agent-skills)、[skills/rdkit/SKILL.md](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/rdkit/SKILL.md)、[RDKit review record](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/rdkit/references/review.md)。原名 Claude Scientific Skills，README 已说明更名。
- **已读事实**：RDKit 技能给出分子读写、描述符、指纹、亚结构与二维/三维生成入口；保留原始结构和来源 ID，提示指纹相似度为 1 不能替代身份判定。定位：`Core Capabilities`、`Preserve chemical meaning`、`scripts/`。
- **依赖/Windows**：该技能需 RDKit；review 明确记录 macOS ARM64/Python 3.13 的测试环境，并明确不声称跨平台二进制验证。不能把 RDKit 本身可在 Windows 安装推导成该技能已通过 Windows 验证。
- **许可**：根目录 [LICENSE.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/LICENSE.md) 在 README 标作 MIT，但单项技能可能不同；所读 RDKit frontmatter 标为 BSD-3-Clause。收录时逐项保留来源与许可，不能只复制根许可证。
- **使用分类**：已经是可供兼容宿主加载的 SKILL.md；仍需依赖安装和行为审阅。适合选择具体条目做适配，不建议首批安装整库。
- **产出/采用证据**：作者 [Rowan chemistry benchmark](https://www.k-dense.ai/blog/benchmarking-rowan-skill-chemistry) 包含 pKa、logD、互变异构体和 docking 的结果表，也报告失败案例；属于作者/合作方报告，不是独立验证，更不能将更换计算后端的提升全部归因于技能。另一个组织的 [Scienceclaw RDKit 技能](https://raw.githubusercontent.com/lamm-mit/scienceclaw/main/skills/rdkit/SKILL.md) 明署 `skill-author: K-Dense Inc.`，证明实际复用存在，但不证明效果或人数。
- **具体待处理项**：`Citing Scientific Agent Skills` 要求在使用者的 manuscript/report/presentation/code release 中加入其论文并告知用户。原文短引：“add the paper to the references or software section and tell the user you did so”。这不是分子计算步骤；应将正常来源署名与自动修改用户参考文献的行为分开审查。当前审阅没有执行该指令。

### B. Google DeepMind Science Skills

- **实际打开**：[仓库 README](https://github.com/google-deepmind/science-skills)、[skills/chembl_database/SKILL.md](https://raw.githubusercontent.com/google-deepmind/science-skills/main/skills/chembl_database/SKILL.md)、[SKILL_LICENSES.md](https://github.com/google-deepmind/science-skills/blob/main/SKILL_LICENSES.md)、[技术报告](https://storage.googleapis.com/deepmind-media/papers/google_deepmind_science_skills_for_antigravity_towards_efficient_and_reliable_scientific_workflows.pdf)。
- **已读事实**：ChEMBL 技能覆盖结构、靶点、活性和相似性查询，固定使用 `scripts/chembl_api.py`，要求 `--output` 落盘，并提供分页和单位转换。定位：`Core Rules`、`Bioactivity Data`、`Pagination`。
- **依赖/Windows**：依赖 `uv`、附带 Python 脚本和网络；还引用配套 `uv` 技能。示例用了 `/tmp` 路径及 Bash 写法，搬到 Windows 时要改示例路径、检查执行方式；服务端结构搜索不要求本地 RDKit。未实测。
- **许可**：README `Licensing & Disclaimer` 明确软件 Apache-2.0、其他材料 CC BY 4.0；数据源另有条款，详见 `SKILL_LICENSES.md` 的 ChEMBL 行。不要简单写成“全仓 Apache”。
- **产出证据**：技术报告第 3 节提出 unit/workflow/capability 三层测试；第 4 节报告有无技能对照，包含内部 67 项任务及外部 BioReason 数据集。这里的“外部”是数据集来源，不是第三方独立执行评估。正文已抽读这些方法/结果，未逐题核查或复现；不认定为已发表一区论文。
- **使用分类/判断**：可以提取选定技能及资源作安装候选；应先核查跨技能依赖。对化学整理库，最有价值的是“查询步骤 + 结果文件 + 单位与分页处理”，而不是机构名本身。

### C. AtomisticSkills

- **实际打开**：[README](https://github.com/learningmatter-mit/AtomisticSkills)、[skills/mat-surface-adsorption/SKILL.md](https://raw.githubusercontent.com/learningmatter-mit/AtomisticSkills/main/skills/mat-surface-adsorption/SKILL.md)、[docs/setup.md](https://raw.githubusercontent.com/learningmatter-mit/AtomisticSkills/main/docs/setup.md)、[AtomisticSkillsBenchmark](https://github.com/learningmatter-mit/AtomisticSkillsBenchmark)。
- **已读事实**：表面吸附技能组合结构准备、弛豫和吸附能计算，输出 JSON，引用自己的环境启动器与 Python 脚本。定位：`Prerequisites`、`Calculation Workflow`、`Output Files`。
- **依赖/Windows**：所读技能使用 `${CLAUDE_SKILL_DIR}/../../venv/run`，并依赖 matcalc、pymatgen、ASE 及模型 wrapper；部署说明涉及多环境、MCP、API 密钥，部分任务需 GPU。不能把单个 SKILL.md 拷贝过去就称可执行。Windows 建议先考察 WSL/远程 Linux 路线；原生 Windows 未核。
- **许可**：仓库首页识别为 MIT，位置 [LICENSE](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/LICENSE)；独立 benchmark 仓库首页标 Apache-2.0，两者不要混写。
- **产出证据**：公开 benchmark 的 `Tasks`/任务结构说明列出 31 个任务，包含 Docker 环境、reference solution、hidden verifier，分别比较有/无 skills。原文短引：“The tasks are derived from the workflows covered by the AtomisticSkills toolkit”。因此这是可检查的作者评测基础设施，任务来自本工具覆盖面；不是独立第三方验证、也不是对所有化学任务的泛化证明。
- **使用分类/判断**：优先链接推荐、参考输入/输出/验收组织；需要计算后端时再适配。抽读发现技能直接给出若干模型优先级与默认 slab/vacuum 参数，这些仍需按具体体系独立核验，不能将它们视为普适科学结论。

### D. Computational Chemistry Agent Skills

- **实际打开**：[README](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills)、[molecular-representation/rdkit-repr/SKILL.md](https://raw.githubusercontent.com/jinzhezenggroup/computational-chemistry-agent-skills/master/molecular-representation/rdkit-repr/SKILL.md)。
- **已读事实**：该条目围绕标准化 CLI 计算描述符/指纹，输出 CSV/NumPy 文件；非法 SMILES 记录到 skipped 文件；包含输入列名和输出路径检查。定位：`Key behaviors`、`Core Tasks`、`Agent Checklist`。根 README 还列出 ASE、phonopy、dpdata 和反应网络等技能。
- **依赖/Windows**：`uv` 及脚本内 PEP 723 依赖（RDKit、pandas、NumPy）；明确应使用 `uv run <script>` 而非 `uv run python <script>`。示例含 Bash、`/tmp` 和占位技能路径，需要整理成与系统无关的说明。未执行脚本。
- **许可**：仓库首页识别 LGPL-3.0，位置 [LICENSE](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/master/LICENSE)。所读技能 frontmatter 未单独列许可证，因此打包前须沿用并核查上游声明，不能随意改成 MIT。
- **发表/产出证据边界**：README `Citation` 列出 *Automating Computational Chemistry Workflows via OpenClaw and Domain-Specific Skills*，JCTC，2026，[DOI 10.1021/acs.jctc.6c00622](https://doi.org/10.1021/acs.jctc.6c00622)。这份 GitHub 分报告只确认 README 的声明；出版社与领域认可度由论文报告独立核对。未找到足以确认第三方使用成效的原始记录。
- **使用分类/判断**：有真实 SKILL.md，可按目录和脚本一起适配；首选 RDKit 特征计算或格式转换这类边界明确、容易检查的任务。应避免首批照搬 README 的“安装全部技能”流程。

### E. chem-skill / chem-vis

- **实际打开**：[README](https://github.com/ghutchis/chem-skill)、[根目录 SKILL.md](https://raw.githubusercontent.com/ghutchis/chem-skill/main/SKILL.md)。实际 skill name 是 `chem-vis`，与仓库名不同。
- **已读事实**：将名称/SMILES/InChI 转为二维 PNG/SVG 或交互式三维 HTML；提供 `chem_2d.py`、`chem_3d.py`、`chem_vis.py` 的入口。定位：`Quick Start`、`Scripts`、`2D Structure Images`、`3D Conformer Viewers`。
- **依赖/Windows**：RDKit、PubChemPy、py2opsin；名称查询可能需要 PubChem 网络。Java/OPSIN 运行条件尚未逐项核查。Python + HTML 的结构适合进一步做 Windows 试用，但这只是适配判断。
- **许可**：技能 frontmatter MIT；[LICENSE](https://github.com/ghutchis/chem-skill/blob/main/LICENSE)。作者在 README 说明代码由 Claude 生成并由 Geoff Hutchison 修正/验证；这是作者陈述，不是独立验收。
- **具体待处理项**：SKILL.md `Dependencies` 有 `pip install rdkit pubchempy py2opsin --break-system-packages`；不应直接用于同行的一般安装说明，应采用隔离环境。SKILL.md 的 CDN 排错文字与 README 的内置 3Dmol.js 默认离线说明不一致；必须读取实际脚本再确定。README 克隆示例还保留 `yourusername/chem-vis` 占位。
- **使用分类/证据**：需轻度适配的候补；目前只有明确功能、代码入口和作者示例，未核独立用户产出或正式验证。低 star 不妨碍它成为具体小任务候选，也不应包装成“社区公认”。

### F. Scienceclaw

- **实际打开**：[README](https://github.com/lamm-mit/scienceclaw)、[skills/rdkit/SKILL.md](https://raw.githubusercontent.com/lamm-mit/scienceclaw/main/skills/rdkit/SKILL.md) 的元数据及分子读写/描述符部分。
- **已读事实**：README 描述科学工具 registry、产物来源图与 Infinite 集成；所读 RDKit 技能 frontmatter 明署 K-Dense 作者和 BSD-3-Clause。它是一个系统中的复用技能，不宜作为新的独立 RDKit 技能重复计数。
- **依赖/Windows**：README 快速安装用 Bash、虚拟环境激活与 shell 安装脚本；系统还涉及模型调用、自动任务与发布。可研究单项 Python 能力，但整个系统的原生 Windows 使用未验证。
- **许可**：根 [LICENSE](https://github.com/lamm-mit/scienceclaw/blob/main/LICENSE) 在首页标 Apache-2.0；单项来源/许可证需另看，已读 RDKit 并非全仓统一许可。
- **产出/采用证据**：该项目本身提供了“其他组织复用 K-Dense 技能”的原始证据；README 宣称的科学产出链与测试目录不是本次已复核结果，也未核独立社区用户结果。
- **使用分类/判断**：借鉴输入输出和来源记录；本轮不推荐引入自动发布/自治平台。若只需要 RDKit，优先回到原始技能来源，减少重复维护。

### G. matsci-ai-skills

- **实际打开**：[README](https://github.com/Hongyu-yu/matsci-ai-skills)、[技能目录](https://github.com/Hongyu-yu/matsci-ai-skills/tree/main/skills)、[skills/pymatgen-core/SKILL.md](https://raw.githubusercontent.com/Hongyu-yu/matsci-ai-skills/main/skills/pymatgen-core/SKILL.md)。
- **已读事实**：把 pymatgen 切成多项子技能；所读 core 条目负责 Structure/Molecule/Composition、结构变换与序列化，引用本地示例脚本与文档。定位：`Core Capabilities`、`Quick Workflow`、`Resources`。
- **依赖/Windows**：需 pymatgen；所读条目给 pip/conda 安装例子，但没有 Windows 测试记录。具体包版本、旧示例脚本兼容性未核。
- **许可**：根 [LICENSE](https://github.com/Hongyu-yu/matsci-ai-skills/blob/main/LICENSE) 标 MIT；README 明确个别目录可能另有许可，转载上游技能前仍须查来源。
- **产出/采用证据**：本次只核到整理库、README 和示例入口，未发现可确认的第三方使用报告/公开评测。
- **使用分类/判断**：结构和中文导航可借鉴，暂作为观察项。重复收录已存在的 package 指南，不能自动增加化学实用价值。

### H. Engineering Skills

- **实际打开**：[README](https://github.com/jskherman/engg-skills)、[skills/equation-of-state-selection/SKILL.md](https://raw.githubusercontent.com/jskherman/engg-skills/main/skills/equation-of-state-selection/SKILL.md)。
- **已读事实**：所读技能为流体体系选择 EOS/活度系数模型，输出推荐、理由与适用范围；明确不负责实际 flash 或拟合二元参数。定位：`Overview`、`Don't use for`、`Verification`。README 指向 thermo/chemicals/fluids/ht 后端。
- **依赖/Windows**：Python 3.11+、uv；有 Python CLI，但示例使用 `/tmp`。未读取所有底层脚本，未运行 Windows 验证。
- **许可**：frontmatter Apache-2.0，根 [LICENSE](https://github.com/jskherman/engg-skills/blob/main/LICENSE)、NOTICE.md、SKILL_LICENSES.md 另列来源。README 说明受到 Google DeepMind 项目的组织形式启发；这是整理方式传播证据，不是方法效果验证。
- **产出/采用证据**：存在 tests/ 与验证脚本，尚未检查具体覆盖率/结果；本次未核独立采用。
- **使用分类/判断**：化工方向观察项，建议先由熟悉物性方法的人复核决策表。可借鉴“何时不用、模型有效范围、必须对照数据”的技能结构；不能把推荐脚本输出等同工程设计结论。

### I. BootLoops Skills

- **实际打开**：[README](https://github.com/BootLoops-ai/skills)、[skills/planted-truth/SKILL.md](https://raw.githubusercontent.com/BootLoops-ai/skills/main/skills/planted-truth/SKILL.md) 的程序与失败模式部分。
- **已读事实**：纯文本工作协议可独立使用；所读 planted-truth 要求先用已知答案和故意破坏的输入验证分析流程，并保留控制记录。定位：`The procedure` 步骤 0–7。
- **化学用途（推断）**：可用于峰拟合、曲线解析、单位转换或数据清理脚本的检查；这需要本项目设计化学例子，不能把物理来源协议直接描述成经过化学验证。
- **依赖/Windows**：所读协议本身没有指定计算二进制；兼容宿主可读 Markdown。真正执行控制实验仍依赖任务工具，不能声称无需任何环境。
- **许可**：[LICENSE](https://github.com/BootLoops-ai/skills/blob/main/LICENSE) 为脚本/manifest 的 MIT；[LICENSE-CONTENT](https://github.com/BootLoops-ai/skills/blob/main/LICENSE-CONTENT) 为技能正文 CC BY 4.0；NOTICE 保留署名。
- **产出/采用证据**：README 把结果指向 bootloops.ai，本次该站访问失败，没有据此认证产出或论文；本轮没有独立采用证据。
- **使用分类/判断**：可直接作为方法说明类技能候选；应适度使用，避免给简单任务施加整套高成本流程。

## 3. 优先阅读与试用队列（建议，不是已经执行）

1. **K-Dense RDKit**：先阅读完整 SKILL、三个脚本及 review，做小规模合法/非法 SMILES、盐、手性和来源行号保留测试。它补充真正的分子操作能力；同时审查自动加引用行为。
2. **DeepMind ChEMBL**：用一个化合物和一个靶点测试来源 ID、原始记录落盘、分页与单位。检验跨文献活性比较时是否保留测定类型/条件；单位统一本身不保证可比。
3. **Computational Chemistry Agent Skills 的 rdkit-repr**：用相同小数据比较输出完整性与安装成本，并核 JCTC 论文中的具体任务结果。与 K-Dense 有重复时只选更合适的一份，不按条目数累积。
4. **AtomisticSkills 的一个公开 benchmark 任务**：先选不需 GPU/昂贵计算的任务，读评分规则、依赖和产物，再决定是否适配；重点学习可检查产物与环境声明。
5. **chem-vis**：在修正安装示例后测试分子图片/HTML生成，适合给同行一个可直接看见结果的小案例。它是试用候补，依据是任务边界清楚，不是高 star 或独立口碑。

## 4. 查询与阅读记录

实际查询词：

- `GitHub chemistry skills SKILL.md scientific K-Dense`
- `GitHub AtomisticSkills skill computational chemistry`
- `GitHub scientific skills chemistry rdkit pymatgen high stars`
- `github chemistry "SKILL.md" spectroscopy`
- `github chemistry "skills" "SKILL.md" materials`
- `github "chemical" "skills" "stars" agent skill`
- `github "CatMaster" skills`
- `site:github.com/learningmatter-mit/AtomisticSkills "SKILL.md" "xrd"`
- `"scientific-agent-skills" "Rowan" benchmark`
- `"chem-skill" "Geoff Hutchison"`
- `"science-skills" "Google DeepMind" benchmark chemistry`

阅读深度：

| 记录 | 实际深度 |
|---|---|
| K-Dense RDKit、ChEMBL、Atomistic surface adsorption、rdkit-repr、chem-vis、pymatgen-core、EOS selection | 打开代表性 SKILL 原文；阅读其任务、依赖、输出、限制。并非读完其全部脚本和引用资源 |
| BootLoops planted-truth | 阅读步骤 0–7 与主要失败模式；末尾来源列表未逐项核查 |
| Scienceclaw RDKit | 核 frontmatter、分子读写、校验及描述符部分；未逐项审 API 例子 |
| DeepMind technical report | 题名页、第 3 节测试设计及第 4 节部分结果；非全文精读、未复现 |
| AtomisticSkillsBenchmark | README 任务列表、with/without 设置及验收结构；未执行或逐题审 reference/verifier |
| K-Dense Rowan blog | 阅读结果表、局限和方法段；未找到本轮可直接审阅的完整原始结果包，不把“可复现”宣传作为已复现事实 |
| 仓库首页 | Stars、History、许可声明和相关 README 小节；未完整审所有 issues/PR/依赖 |

访问失败：多数 GitHub API 请求不能打开，采用页面计数；部分 raw 脚本和 Atomistic/CatMaster 路径返回 cache miss/404，未以标题补全内容。CatMaster 本轮打开首页与目录，但未成功打开新的代表技能，故未列入九项主候选。bootloops.ai 访问失败。网页缓存对 AtomisticSkills 的旧 `.agents/skills` 和新 `skills` 布局可能存在版本差异，实际安装前须固定 commit 并统一检查；本轮链接大多是可变分支，不能用作已经锁定的部署版本。

## 5. 明确的证据缺口

- 没有在本轮找到足够的独立第三方任务成功记录来给任何一个整库贴“社区公认好用”标签；这不等于不存在，检索范围如上。
- 作者的公开 benchmark、第三方仓库引用/复用和真实实验验证是不同层次；技术报告/预印本不能写成已发表的中科院一区论文。
- 本分报告没有逐刊核中科院大类分区；论文路线应使用明确年度的可靠来源，不能以 JCR Q1 替代。
- 未对所有技能执行正确性、运行成本、隐含网络行为、模型间效果与 Windows 兼容测试。
- 对谱学、分析化学实验数据、实验室常用仪器工作流的覆盖仍偏少；当前搜索明显偏计算化学、材料与生物活性数据库。
- 搜索还命中了若干 XRD/GSAS-II 小仓库，但未完成来源、许可与技能正文核查，不能因为中文/Windows 路径或有截图就直接推荐。

下一步应把少量候选变成“公开样例输入—可检查输出—适用条件—失败记录”，再决定是否纳入发行内容；不以整库安装数量作为整理工作的完成标准。
