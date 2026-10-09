# 科学检索与 DFT 技能：优先试用清单

检索日期：2026-10-08（UTC+8）。本轮继承同日初筛，细读技能正文和部分代码；没有安装技能、调用模型、运行检索脚本或提交计算。以下排序是**试用优先级判断**，不是效果排名。现有 reading-contract、lit-review、ref-check 继续负责证据纪律，不重复计作新能力。来源定位与缺口见 [阅读记录](search-ledger.md)。

## 科学检索：前三项

### 1. K-Dense：paper-lookup——首选新增检索入口

[仓库](https://github.com/K-Dense-AI/scientific-agent-skills) · [skills/paper-lookup/SKILL.md](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/paper-lookup/SKILL.md)

**类型：原生 skill + 脚本。** `Core Workflow`、`Bundled Scripts` 规定按任务选数据库、记录端点和参数、核对分页数量；支持 DOI、引文邻域、OA 位置和全文。四个主脚本负责分页、JATS 分节、arXiv XML 和 OpenAlex 摘要重建。抽查分页与 JATS 代码，能看到缺失正文、提前截断等处理；这比再加一份“认真读论文”提示词更能补当前能力。

**条件：** 单项 MIT，保留署名和许可；Python 3.11+，脚本使用标准库，指令仍依赖 Bash/curl。WSL 路线较直接；Windows 要改 shell 示例并实测。API 密钥、邮箱和全文权限按具体来源配置。上游末尾要求在实际贡献时引用其论文，收录时应说明这一行为。

**证据/试用：** 有作者维护的 [tests/paper-lookup](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/tests/paper-lookup)，未执行、未取得独立效果验证。先用两个已知 DOI、一个不存在的 DOI、一个只有摘要的记录，验收原始响应、标识去重、正文状态和来源日志。

### 2. DeepMind Science Skills：OpenAlex + arXiv——范围明确的检索组件

[仓库](https://github.com/google-deepmind/science-skills) · [OpenAlex skill](https://github.com/google-deepmind/science-skills/blob/main/skills/literature_search_openalex/SKILL.md) · [arXiv skill](https://github.com/google-deepmind/science-skills/blob/main/skills/literature_search_arxiv/SKILL.md)

**类型：原生 skills + CLI。** 前者的 `resolve/get/filter/download-pdf` 支持作者消歧、DOI 查询及 OA 获取；后者提供查询、分页、PDF/HTML 和 LaTeX 源文件下载。生物化学方向可补 [Europe PMC skill](https://github.com/google-deepmind/science-skills/blob/main/skills/literature_search_europepmc/SKILL.md)，但其强制 OA 筛选会限制覆盖面。

**条件：** uv、附带 Python 脚本，OpenAlex 还引用 credentials 技能；Bash/jq/临时路径需 Windows 改写。README 将软件列 Apache-2.0、其他材料列 CC BY 4.0，数据源另有条款，不能标“全仓 Apache”。OpenAlex 基础查询可无 key；归档全文下载需 key，当前配额应查官方文档，不复制技能里的旧称谓。

**证据/试用：** 继承初筛的作者技术报告线索，不据此认证单项检索效果。用同一篇有 arXiv 与期刊版本的论文核对版本、DOI、下载正文及错误记录；与 paper-lookup 比较后选主入口，避免功能重复。

### 3. PaperQA2——本地论文集的证据检索工具

[仓库及 README 工作流](https://github.com/Future-House/paper-qa#paperqa2-algorithm)

**类型：Python/CLI 工具，可借鉴工作流；本轮未确认主分支原生 skill。** README `PaperQA2 Algorithm` 描述检索、分块取证、回答三阶段；可对已有 PDF 目录建索引并返回带位置的引用。新增技能的 [PR #1341](https://github.com/Future-House/paper-qa/pull/1341) 仍显示 Open，不能按已合并插件推荐。

**条件：** Apache-2.0；Python 3.11+、PDF 解析、索引、模型及 embedding 服务，API 或本地模型需另配。元数据写 OS Independent，不等于 Windows 实测通过。作者有[研究论文](https://arxiv.org/abs/2409.13740)和示例，本轮仅核身份/摘要与代码文档，未复现。

**试用：** 只导入三篇许可允许的论文，人工预先指定一个有答案和一个无答案的问题，检查引用页段、条件限定与拒答；适合第二阶段接入。

## DFT：前三项

### 1. Computational Chemistry Agent Skills——先复用输入准备

[仓库](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills) · [dft-qe](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/master/quantum-chemistry/dft-qe/SKILL.md) · [dft-vasp/relax](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/master/quantum-chemistry/dft-vasp/relax/SKILL.md) · [ASE 路由](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/master/atomistic-workflows/ase/SKILL.md) · [dpdisp-submit](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/master/tools/dpdisp-submit/SKILL.md)

**类型：原生技能树，计算与调度依赖外部工具。** QE 条目明确只准备输入；VASP relax 要先区分离子、晶胞和 slab 弛豫，再确定 ISIF。提交单列，避免把“输入已生成”写成“计算完成”。这是首批最容易限定边界的 DFT 入口。

**条件：** DFT 条目 LGPL-3.0-or-later，分发须保留上游许可；VASP/POTCAR 另有授权。结构处理可能需 ASE、pymatgen、dpdata；执行需 QE/VASP 和 DPDispatcher/集群配置。Windows 可考察准备环节，实际计算优先 WSL/Linux/HPC，均未测试。既有初筛核过 JCTC 项目论文，但不证明当前每个新增 DFT 子技能已验证。

**试用：** 给一份公开 Si 结构和明确参数，仅生成输入；再故意移除晶胞或赝势映射，检查是否指出缺口。随后才安排小规模截断能/k 点收敛计算。

### 2. CatMaster——最值得借鉴的催化计算操作链

[仓库](https://github.com/q734738781/CatMaster) · [VASP 输入准备](https://github.com/q734738781/CatMaster/blob/main/skills/materials_worker/vasp-input-preparation/SKILL.md) · [批量执行](https://github.com/q734738781/CatMaster/blob/main/skills/materials_worker/vasp-batch-execution/SKILL.md) · [失败回执恢复](https://github.com/q734738781/CatMaster/blob/main/skills/execution/dpdispatcher-remote-receipts/SKILL.md)

**类型：有原生 SKILL.md，但当前更适合作工作流参考。** 前两项按 bulk/slab/gas 和计算阶段准备输入、收回产物；恢复条目避免网络错误后重复提交。正文依赖 `vasp_prepare`、`remote_submission` 等 CatMaster 工具，单拷 Markdown 不能运行。

**条件：** 根项目 Apache-2.0，但回执条目标 `project-local`，再分发前需澄清其适用许可。还需 ASE/pymatgen、DPDispatcher、VASP 与远程资源；部署示例面向 Linux，Windows 建议仅作客户端。其默认 k 点/展宽等属于项目起点，不能当收敛证明。公开预印本、demo 和 benchmark 均是作者产出，本轮未复核数值。

**试用：** 先借鉴“准备—执行—科学验收”目录和状态规则；用脱敏失败日志做恢复演练，确认不会重复发作业，再考虑工具适配。

### 3. AtomisticSkills：mat-dft-vasp——完整但需先修审

[仓库](https://github.com/learningmatter-mit/AtomisticSkills) · [skills/mat-dft-vasp/SKILL.md](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/skills/mat-dft-vasp/SKILL.md)

**类型：原生 skill + 脚本 + 可选 atomate2 MCP。** 提供批量输入、能量/力/应力/结构解析及远程工具入口。依赖整库 `src/`、`venv/run cpu`、ASE/pymatgen、POTCAR；远程执行还需 jobflow-remote 配置。MIT；README 明确 Linux 环境，Windows 应先用 WSL/远程 Linux。其 [mat-surface-adsorption](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/skills/mat-surface-adsorption/SKILL.md) 使用 MLIP，不能冒充 DFT。

**发现/试用：** `KPOINTS pitfall` 中的 `gamma_automatic(lattice, kpts=0.22)` 与 [pymatgen 当前签名](https://pymatgen.org/pymatgen.io.vasp.html#pymatgen.io.vasp.inputs.Kpoints.gamma_automatic) 不符，须修审后试用。公开 [31 项 benchmark](https://github.com/learningmatter-mit/AtomisticSkillsBenchmark) 是作者评测且绑定旧 commit，不自动认证当前 VASP 条目。先解析一份公开完成记录和一份截断记录，再测试输入生成，最后接集群。

## 当前取舍

建议先试 **paper-lookup + 一个 QE/VASP 输入准备技能**；PaperQA2、CatMaster、AtomisticSkills 排在后续。补充观察：K-Dense 的 [pymatgen skill](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/pymatgen/SKILL.md) 可用于结构与结果检查，不能等同 DFT 引擎；[qe-analysis](https://github.com/chatmaterials/qe-analysis) 有独立后处理技能和 fixtures，但本轮未核验解析正确性。没有足够独立任务记录给上述整库贴“已验证好用”标签。
