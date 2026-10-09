# 检索与阅读记录

日期：2026-10-08（UTC+8）。范围：补充科学检索执行与周期体系 DFT 输入、调度、输出能力。继承上级目录三份初筛报告；不重做全面文献综述，不核发期刊分区、高被引或社区口碑标签。

## 实际查询

- `github "SKILL.md" "quantum espresso"`
- `github "SKILL.md" "literature" "search" "scientific"`
- `github "CatMaster" skills`
- `github "computational-chemistry-agent-skills" dft`
- `site:github.com/learningmatter-mit/AtomisticSkills "SKILL.md" "vasp"`
- `site:github.com/learningmatter-mit/AtomisticSkills "SKILL.md" "surface"`
- `site:github.com/learningmatter-mit/AtomisticSkills "SKILL.md" "atomate2"`

随后从官方仓库 README/目录追踪原始 SKILL.md、许可证、部分脚本和官方 API 文档。索引网站只用于发现路径，不作为质量证据。GitHub API 树请求访问失败或 403 限流，部分 raw 页面在网页工具中失败后通过只读 HTTPS 获取成功。未安装包、未执行上游脚本、未运行模型或科学计算。

## 已读记录与精确定位

以下为检索当日可变分支快照，不是已锁定的部署版本；安装时必须固定 commit。引号内为从原文复制的短句，各自仅支持紧邻主张。所有推荐优先级和试用设计均为本次判断。

| 来源与版本 | 实际阅读位置/深度 | 可核事实与短引 | 未核项目 |
|---|---|---|---|
| [K-Dense paper-lookup/SKILL.md](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/paper-lookup/SKILL.md)，main，frontmatter v2.4、reviewed 2026-09-30 | 全部技能正文；重点 Core Workflow、Bundled Scripts、Completeness、Citing Scientific Agent Skills | “Never present metadata as full text.” 四个主脚本及标准库/Python 3.11 依赖明确；MIT | 18 个接口逐个可用性、认证全文、脚本完整测试未执行 |
| [paginate.py](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/paper-lookup/scripts/paginate.py)，main | 模块说明，`fetch`、API parser、`walk`、`main` 中计数/截断/脱敏相关行，非逐行完整审计 | 源码包含 `stopped_at_limit`、计数对账、redact_url；上限截断保留 partial 状态 | 重试正确性、所有分页边界与真实 API 运行未核 |
| [jats_to_text.py](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/paper-lookup/scripts/jats_to_text.py)，main | 模块说明、章节提取、`main` 中 `body is None` 与章节筛选分支 | 缺少正文时有专门状态/错误处理；分节文本有明确数据结构 | 未喂测试 XML；表格/公式保真未核 |
| [K-Dense pymatgen/SKILL.md](https://raw.githubusercontent.com/K-Dense-AI/scientific-agent-skills/main/skills/pymatgen/SKILL.md)，main | frontmatter 与能力说明，非全部 413 行精读 | Python 3.11+、uv；固定 pymatgen/mp-api 快照；局部结构/材料数据分析 | 配套脚本、科学检查、Windows 安装未核；只列辅助 |
| [DeepMind OpenAlex SKILL](https://raw.githubusercontent.com/google-deepmind/science-skills/main/skills/literature_search_openalex/SKILL.md)，main | 全文，Core Rules/CLI/Rate Limits | “Resolve before filter.” CLI 支持 resolve/get/filter/download-pdf | 配额文字和 polite pool 旧表述不能代替当前官方说明；脚本未审 |
| [DeepMind arXiv SKILL](https://raw.githubusercontent.com/google-deepmind/science-skills/main/skills/literature_search_arxiv/SKILL.md)，main | 全文，Utility Scripts/Workflow | 搜索 JSON、PDF/HTML、源文件下载三条入口；要求验证下载文件 | 下载、解包、重试与 Windows 路径未执行 |
| [DeepMind Europe PMC SKILL](https://raw.githubusercontent.com/google-deepmind/science-skills/main/skills/literature_search_europepmc/SKILL.md)，main | 全文，Core Rules/Search/Get Full Text/Citations/References | “This skill exclusively searches open-access content.” 限定 OPEN_ACCESS:y | 不可描述为涵盖全部学术论文；脚本未审 |
| [DeepMind README](https://github.com/google-deepmind/science-skills#licensing--disclaimer) 与 [SKILL_LICENSES](https://github.com/google-deepmind/science-skills/blob/main/SKILL_LICENSES.md)，main | Licensing & Disclaimer、文学数据库对应行 | 软件 Apache-2.0、其他材料 CC BY 4.0；数据来源另有条款 | 未逐项解释数据库法律条款；本轮仅记录分发声明 |
| [PaperQA README](https://github.com/Future-House/paper-qa#paperqa2-algorithm)、[pyproject](https://github.com/Future-House/paper-qa/blob/main/pyproject.toml)、[LICENSE](https://github.com/Future-House/paper-qa/blob/main/LICENSE)，main | Algorithm、Installation、CLI Usage、依赖与许可 | “Python 3.11+”；分块证据及引用回答；软件 Apache-2.0 | 未读完全部源码，不认定任一宿主或模型已兼容 |
| [PaperQA2 论文](https://arxiv.org/abs/2409.13740) | 题名、作者元数据和摘要页 | 题名 Language agents achieve superhuman synthesis of scientific knowledge；只作作者研究产出线索 | 未读全文/补充材料，不引用“超人”作本次性能判断 |
| [dft-qe/SKILL.md](https://raw.githubusercontent.com/jinzhezenggroup/computational-chemistry-agent-skills/master/quantum-chemistry/dft-qe/SKILL.md)，master | 全文，Scope/Hard requirement/DFT parameters/Expected output | “This skill prepares the QE task only”；须给结构、明确关键设置；LGPL-3.0-or-later | 没有执行生成任务；不是收敛自动验收实现 |
| [dft-vasp/SKILL.md](https://raw.githubusercontent.com/jinzhezenggroup/computational-chemistry-agent-skills/master/quantum-chemistry/dft-vasp/SKILL.md)、[relax 子技能](https://raw.githubusercontent.com/jinzhezenggroup/computational-chemistry-agent-skills/master/quantum-chemistry/dft-vasp/relax/SKILL.md)，master | 全文，Routing/Relaxation intent/Must provide | 顶层只路由；relax 将离子/晶胞/slab 意图区分，POTCAR 映射明确 | 非 VASP 参数普适正确性证明；子技能嵌套布局需保留 |
| [ASE 路由](https://raw.githubusercontent.com/jinzhezenggroup/computational-chemistry-agent-skills/master/atomistic-workflows/ase/SKILL.md)、[dpdisp-submit](https://raw.githubusercontent.com/jinzhezenggroup/computational-chemistry-agent-skills/master/tools/dpdisp-submit/SKILL.md)，master | 打开正文；核路由/准备与提交边界、调度范围 | 前者准备 workflow/backend，后者处理 shell/远程调度 | 未审所有 adapter、远程配置、恢复实现 |
| [CatMaster VASP 准备](https://raw.githubusercontent.com/q734738781/CatMaster/main/skills/materials_worker/vasp-input-preparation/SKILL.md)，main | 全文，regime/preset、Method-critical defaults、Output Contract | “Treat these as explicit starting recipes, not convergence proofs.” 依赖 vasp_prepare 等专用工具 | 未逐条验证参数和 VASPsol 方法；不照搬 house defaults |
| [CatMaster 批量执行](https://raw.githubusercontent.com/q734738781/CatMaster/main/skills/materials_worker/vasp-batch-execution/SKILL.md)，main | 全文，Triage failures、structured analysis、Output Contract | “dispatch success is not the same as usable scientific output.” 先确认旧作业再重试 | 未查远端任务配置和实际防重复实现 |
| [CatMaster 回执](https://raw.githubusercontent.com/q734738781/CatMaster/main/skills/execution/dpdispatcher-remote-receipts/SKILL.md)，main | 全文，frontmatter/trigger/Inspect and recover once | `license: project-local`；“Do not assume network exceptions cancel remote jobs.” | 根 Apache-2.0 与单项 project-local 的具体适用关系未澄清，暂只链接参考 |
| [CatMaster README](https://github.com/q734738781/CatMaster)、[LICENSE](https://github.com/q734738781/CatMaster/blob/main/LICENSE)、[部署手册](https://github.com/q734738781/CatMaster/blob/main/docs/user-guide/10-deployment-operations.en.md) | 依赖/部署/Benchmark archives、许可证正文 | 主体 Apache-2.0、conda + shell + 工具平台；README 自述有公开 benchmark 报告 | 未逐份读 benchmark 报告；不算独立用户证据 |
| [CatMaster arXiv](https://arxiv.org/abs/2601.13508v4) | 元数据、摘要、版本记录 | 当前 v4 题名已为 Autonomous computational catalysis through an agentic research system；页面注明 SI 不在此 | 未读正文、未确认期刊终版；不沿用旧标题宣称当前版本 |
| [AtomisticSkills VASP skill](https://raw.githubusercontent.com/learningmatter-mit/AtomisticSkills/main/skills/mat-dft-vasp/SKILL.md)，main | 全文，Step 1/2、Constraints | “The scripts require the `cpu` environment.” 提供 prepare、parse、atomate2 工具衔接 | KPOINTS 示例与当前 API 不匹配，见下；未运行 |
| [parse_vasp_results.py](https://raw.githubusercontent.com/learningmatter-mit/AtomisticSkills/main/skills/mat-dft-vasp/scripts/parse_vasp_results.py)，main | 全文约 80 行 | 引用整库 VASPParser；单目录/批目录分支，JSON 输出 | 未审 VASPParser 内部；不能据此认证收敛判断完整 |
| [AtomisticSkills surface adsorption](https://raw.githubusercontent.com/learningmatter-mit/AtomisticSkills/main/skills/mat-surface-adsorption/SKILL.md)，main | 全文 | 描述明确写 “using MLIPs.”；使用 matcalc、ASE、pymatgen 与模型 wrapper | 不能作为直接 DFT 技能；模型优先级、训练集陈述与默认厚度未验证 |
| [AtomisticSkills README](https://github.com/learningmatter-mit/AtomisticSkills#system-requirements--runtime)、[LICENSE](https://github.com/learningmatter-mit/AtomisticSkills/blob/main/LICENSE) | System Requirements、2.0 migration 提示、MIT 文本 | Linux、cpu glibc≥2.28；uv 环境与旧 conda 布局不兼容 | Windows/WSL、容器回退未执行 |
| [AtomisticSkillsBenchmark](https://github.com/learningmatter-mit/AtomisticSkillsBenchmark) | README Tasks/With-skill mode/Scoring/License | 31 任务、作者评估；with-skill 绑定 `10048cca1b5e34da182e02fded5cd622151001bc` 等旧 commit；benchmark Apache-2.0 | 未读所有 verifier/reference，未跑 benchmark，非当前分支 DFT 认证 |
| [qe-analysis/SKILL.md](https://raw.githubusercontent.com/chatmaterials/qe-analysis/main/SKILL.md)、[README](https://github.com/chatmaterials/qe-analysis) | 技能全文、README Local Validation | 后处理、比较、能带/DOS/projwfc 脚本路径、fixtures；首页标 MIT | LICENSE/分析脚本经网页工具获取失败，未核内部数值提取；只列观察 |

## 重要交叉检查

1. **OpenAlex 鉴权。** 主线程独立核查后，本轮再次打开 [Authentication](https://help.openalex.org/api/authentication/) 与 [Fulltext / Download options](https://help.openalex.org/access/fulltext/)。基础查询无 key 仍可用；免费 key 提升预算；`content.openalex.org` 归档下载需 key，出版社 OA 链接与此不同。当前每页上限 100。未发送真实 API 请求，不把文档规则当本机连通性证明。
2. **PaperQA skill 状态。** [PR #1341](https://github.com/Future-House/paper-qa/pull/1341) 页面为 Open；Summary 指向拟新增 `docs/skills/paper-qa/SKILL.md` 和 Claude 插件。本轮按工具推荐，不把 PR 文件当主分支已发行能力。
3. **AtomisticSkills KPOINTS 示例。** `mat-dft-vasp/SKILL.md` 的 `Constraints / KPOINTS pitfall` 写 `gamma_automatic(lattice, kpts=0.22)`；[pymatgen 官方 API](https://pymatgen.org/pymatgen.io.vasp.html#pymatgen.io.vasp.inputs.Kpoints.gamma_automatic) 签名为 `gamma_automatic(kpts: tuple[int,int,int], shift, comment)`。这是静态接口不一致，不是本轮运行报错；应先修审再执行，不用该示例自动“修复”输入。
4. **许可缺失候选。** 新发现 [scholarly-deep-research](https://github.com/Tw6249/scholarly-deep-research#license) 有真实 SKILL.md 与多源检索脚本，但 README 明说尚未选择许可证。先链接观察，不纳入本库分发。
5. **还未展开的线索。** 搜索命中 MatClaw、qe-scf-slim、Deep-Matter-Chem-Skills、four-state-vasp、FCP-VASP-ASE；尚未完成代表技能/许可/运行证据核查，不列优先推荐。没有检索到并核实足够独立第三方任务成功记录；这不是不存在独立证据的全局断言。

## 验证边界

已做：读取公开来源、静态比对部分实现与官方接口、检查候选分类和许可声明、生成本地报告。未做：安装、实网检索 CLI、模型调用、Windows/WSL 运行、DFT/MLIP 作业、独立科学复现、期刊年度分区认证。低成本试用方案见 [报告](scout-report.md)，执行前固定上游版本并单列实际输入、产物和失败记录。
