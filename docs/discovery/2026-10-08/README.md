# 化学科研 Skills 候选来源初筛

检索日期：2026-10-08（UTC+8）。本轮寻找已有技能和可借鉴的工作步骤，服务于精选整理库；不是新颖性审计、全面文献综述或安装验证。当前发行目录仍只有原有五项通用技能。

## 筛选口径

论文路线优先考察领域相关性、公开结果、后续引用与采用；中科院大类分区作为记录项，必须注明年度与来源。知名团队增加审阅优先级，但不代替对具体方法的检查。新论文的引用积累时间较短，单列观察，不直接与多年论文比较总引用。

项目路线考察代表性 SKILL.md、配套脚本、可检查的输入输出、维护和许可。Stars 表示关注度；作者 benchmark、第三方复用和独立效果验证分别记录。两条路线可分别入围，不要求实用的新技能先有高被引论文，也不把高水平论文当作开箱即用保证。

## 优先名单

下表是后续试用建议，不是已验证的质量排名。所有 Windows 原生执行与模型间效果均未实测。数字为检索当日页面/API 返回快照，可能有缓存。

| 来源 | 学术或使用依据 | 可借鉴内容 | 建议 |
|---|---|---|---|
| [Computational Chemistry Agent Skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills) | JCTC 2026 正式论文；148 stars；实际读到 rdkit-repr | 分子描述符/指纹、格式转换、任务输出验收 | 优先试小任务；新论文，不能称高被引成熟方案 |
| [Google DeepMind Science Skills](https://github.com/google-deepmind/science-skills) | 约 3.2k stars；技术报告与作者评测；读到 ChEMBL 技能 | 数据库查询、分页、单位处理、结果落盘 | 优先试 ChEMBL；技术报告未确认为正式一区论文 |
| [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills) | API 47,852 stars；RDKit review；第三方仓库复用 | RDKit 分子检查、描述符、指纹等 | 挑单项审阅；处理自动插入上游论文引用的指令 |
| [Paper2Agent](https://github.com/jmiao24/Paper2Agent) | Nature 2026；约 3.7k stars；当前有 paper2agent 技能 | 将论文/已有代码整理为技能及 MCP 工具 | 优先考察文档转换；生成物仍须核查，计算路线依赖更重 |
| [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) | 175 stars；公开 31 任务作者 benchmark | 原子结构、表面吸附工作流及验收组织 | 先链接推荐；环境和模型后端较重 |
| [ChemCrow](https://github.com/ur-whitelab/chemcrow-public) | Nature Machine Intelligence 2024；出版社显示 1,090 引用 | 用化学工具完成查询和计算、保留工具证据 | 学术依据与步骤借鉴；公开版不等同论文完整系统 |
| [OpenScholar](https://github.com/AkariAsai/OpenScholar) | Nature 2026；出版社显示 59 引用 | 检索、证据段落、回答与引用核查 | 补充文献流程；本轮没有确认原生 SKILL.md |
| [Coscientist](https://github.com/gomesgroup/coscientist) | Nature 2023；出版社显示 1,348 引用 | 文档指导工具操作、任务分解与执行反馈 | 仅方法参考优先；公开简化代码带 Commons Clause 限制 |

上述论文出版、引用计数与许可原始链接见 [论文路线报告](paper-scout.md)；原生技能、Stars、维护和依赖证据见 [GitHub 路线报告](github-scout.md)。各项均未完成年度中科院大类分区的权威表逐刊认证，不应将整表称为“已核实的一区清单”。

## 建议的首批试用顺序

这是整理库的实施建议，尚未执行或收录：

1. **分子输入检查与特征表**：比较 rdkit-repr 和 K-Dense RDKit，在正常/非法 SMILES、立体异构体、盐等公开小样例上检查 ID、异常记录和输出一致性，优先保留一个主实现。
2. **数据库证据查询**：选 DeepMind ChEMBL，检查记录标识、查询日期、原始值/单位、分页和可追溯结果文件。
3. **论文方法卡片或技能转换**：选 Paper2Agent 的论文输入路线，用许可允许的开放材料检查方法条件、证据定位和缺失输入；不得将自动生成结果直接视为有效科研协议。
4. **材料计算候选**：在明确计算后端后再检查 AtomisticSkills。小型结构任务先于昂贵计算，参考值不能由待测步骤自身提供。

每个候选应先形成“中文用途—依赖—公开输入—预期输出—失败情形—实际执行记录”。通过后再固定上游 commit、保留逐项许可、纳入安装目录。单独测试 Windows/WSL 与宿主实际调用；文本能被读取并不证明脚本能运行。

## 报告与局限

- [GitHub 路线：9 个来源及代表性技能](github-scout.md)
- [论文路线：6 项、发表与代码证据](paper-scout.md)
- [论文路线检索、阅读与缺口记录](search-ledger.md)
- [论文项目元数据抓取记录](paper-project-metadata.json)

本轮没有取得足够独立第三方任务记录，不能给某个整库贴“社区公认好用”的标签。计算化学、材料与文献任务覆盖较多，谱学、仪器数据及实验室日常工作流仍需补充。没有安装候选、复现论文、修改现有技能或执行远端发布。
