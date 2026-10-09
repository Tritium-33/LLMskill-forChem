# 已发表论文支持的候选来源

日期：2026-10-08（UTC+8）。本报告为来源初筛：发表信息、已读部分、代码开放范围和建议用途分别记录。没有完成所有论文及补充材料的全文精读，也没有复现。阅读深度与检索缺口见 [记录](search-ledger.md)。

引用数均为当日出版社页面的 Citations 计数，可能存在缓存，不是统一 Google Scholar/WoS 口径，也不是 ESI 高被引认定。Stars 来自当日 GitHub 首页快照。论文发表与当前代码版本、当前技能的科学验证是不同事实。

## 1. Computational Chemistry Agent Skills：领域贴近，已有真实技能

**已读事实。** Mingwei Ding 等，*Automating Computational Chemistry Workflows via OpenClaw and Domain-Specific Skills*，JCTC **22(12), 5919–5929 (2026)**，DOI [10.1021/acs.jctc.6c00622](https://pubs.acs.org/doi/abs/10.1021/acs.jctc.6c00622)。ACS 的 Article history 记录 6 月 9 日上线、6 月 23 日卷期发表；[官方卷期目录](https://pubs.acs.org/jctcce/issue/22/12)也列出该文。出版社部分直接打开返回 403，本轮通过搜索工具取得官方摘要页和卷期目录的正文记录，未取得期刊全文。

摘要区分规划、领域操作与 HPC 调度，并报告甲烷氧化反应 MD 案例。公开 [arXiv v2](https://arxiv.org/html/2603.25522v2) 的案例段（图 3 附近）说明由通用软件接口技能组合流程；结论仍将更广泛任务列为后续方向。预印本内容不能自动当作期刊终版的逐字记录。

**代码。** [官方仓库](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills)，148 stars，LGPL-3.0。已读 `molecular-representation/rdkit-repr/SKILL.md`，具体入口、输出和依赖见 [GitHub 分报告 D](github-scout.md#d-computational-chemistry-agent-skills)。

**整理建议（推断）。** 这是“正式计算化学论文 + 原生技能”较贴近目标的候选，优先试描述符、指纹、格式转换。尚未核到可靠引用数或独立第三方复现，不称高被引或成熟通用方案；作者案例不证明任意任务与宿主均有效。

## 2. Paper2Agent：论文、代码转为可调用能力

**已读事实。** Jiacheng Miao、Joe R. Davis、Yaohui Zhang、Jonathan K. Pritchard、James Zou，*Reimagining research papers as interactive and reliable AI agents*，Nature，**2026-09-16**，[DOI 10.1038/s41586-026-11044-y](https://www.nature.com/articles/s41586-026-11044-y)。出版社显示 **6 引用**。正文 Methods、Discussion、Code availability 与摘要支持论文/代码生成 MCP 工具并检查执行的设计；主要已读案例涉及 AlphaGenome、Scanpy、TISSUE，不能当作普遍化学有效性证明。

**代码。** [Paper2Agent](https://github.com/jmiao24/Paper2Agent)，约 **3.7k stars**；[代码 LICENSE](https://raw.githubusercontent.com/jmiao24/Paper2Agent/main/LICENSE) 为 MIT。实际打开的 [paper2agent/SKILL.md](https://raw.githubusercontent.com/jmiao24/Paper2Agent/main/skills/paper2agent/SKILL.md) 第 8–11 行按论文 PDF / 代码 / 两者分流；关键短引：“Every MCP tool must bind to existing repository code.” 配套 paper2skill/paper2mcp 文件已打开，但所有脚本、验证器和资源尚未逐项审阅。论文材料本身与代码许可证不同，不能依代码 MIT 任意再分发第三方全文/图表。

**整理建议（推断）。** 优先考察把开放论文整理为带证据定位的方法技能。代码转换还需要目标软件环境、执行权限和实际测试。Nature 论文不自动认证当前分支新增的所有技能；作者/刊物可以提高审阅优先级，6 次引用不足以称为高被引。

## 3. ChemCrow：化学工具使用的高关注研究依据

**已读事实。** Andres M. Bran、Sam Cox、Oliver Schilter、Carlo Baldassari、Andrew D. White、Philippe Schwaller，*Augmenting large language models with chemistry tools*，Nature Machine Intelligence **6, 525–535 (2024)**，2024-05-08，[DOI 10.1038/s42256-024-00832-8](https://www.nature.com/articles/s42256-024-00832-8)。出版社显示 **1,090 引用**。摘要描述整合 18 个工具及实验案例；Code availability 明确公开实现仅包括 **12 个工具子集**，短引：“a subset of 12 tools used in the original implementation”。

**代码。** [chemcrow-public](https://github.com/ur-whitelab/chemcrow-public)，**957 stars**，[LICENSE](https://raw.githubusercontent.com/ur-whitelab/chemcrow-public/main/LICENSE) 为 MIT。[README](https://raw.githubusercontent.com/ur-whitelab/chemcrow-public/main/README.md) 的 Note 写明 API 限制导致工具不全：“This repo will not give the same results as that paper.” 依赖 LangChain、RDKit、数据库/API；示例仍使用旧模型标识。论文链接到实验记录仓库，但本轮未逐项核实验日志。

**整理建议（推断）。** 适合作为结构核验、数据库查询、外部工具证据的学术来源。不能直接称为可加载 SKILL.md，也不能承诺按旧 README 即可复现。引用量体现较强关注度，不等同正确性或用户群口碑。

## 4. Coscientist：高关注论文，公开范围和许可均有限制

**已读事实。** Daniil A. Boiko、Robert MacKnight、Ben Kline、Gabe Gomes，*Autonomous chemical research with large language models*，Nature **624, 570–578 (2023)**，2023-12-20，[DOI 10.1038/s41586-023-06792-0](https://www.nature.com/articles/s41586-023-06792-0)。出版社显示 **1,348 引用**。摘要支持搜索文档、代码与实验工具结合的系统设计；Data/Code availability 明确公开简化实现，并说它“may not produce the same results”。

**代码。** [coscientist](https://github.com/gomesgroup/coscientist)，**211 stars**。实际打开的 [LICENSE](https://raw.githubusercontent.com/gomesgroup/coscientist/main/LICENSE) 顶部为 **Apache 2.0 + Commons Clause**，附有 Sell 限制。不可省略附加条件而标成普通 Apache-2.0 开源包。

**整理建议（推断）。** 优先作为文档指导工具操作、分步执行与反馈记录的思想来源。首批仅链接和原创步骤说明；本轮不打包其代码，也不将公开简化版本视为论文完整系统。

## 5. OpenScholar：文献检索与证据核验的可借鉴流程

**已读事实。** Akari Asai 等，*Synthesizing scientific literature with retrieval-augmented language models*，Nature **650, 857–863 (2026)**，2026-02-04，[DOI 10.1038/s41586-025-10072-4](https://www.nature.com/articles/s41586-025-10072-4)。注意 DOI 中的 2025 不等于正式发表年份。出版社显示 **59 引用**。Methods 的 Overview / Citation verification 描述检索、生成、自反馈、引用核查；摘要明确评测涉及计算机、物理、神经科学和生物医学，不能直接扩展为化学验证。

**代码。** [OpenScholar](https://github.com/AkariAsai/OpenScholar)，约 **1.7k stars**；[LICENSE](https://raw.githubusercontent.com/AkariAsai/OpenScholar/main/LICENSE) 为 Apache-2.0。本轮未确认原生 SKILL.md；模型、检索数据与推理管线不是复制一段提示词即可获得的能力。

**整理建议（推断）。** 为已有阅读/文献技能补充“检索段落—对应主张—核引用—记录缺口”的流程和评价维度；初版不必部署完整检索基础设施。将流程改写成技能后的效果仍需另测。

## 6. SciToolAgent：补充观察项

**元数据核查，期刊全文未读。** *SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration*，Nature Computational Science **5, 962–972 (2025)**，2025-08-20，[DOI 10.1038/s43588-025-00849-y](https://www.nature.com/articles/s43588-025-00849-y)。取得出版社搜索记录中的题名、发表与 Code availability，正文直接访问失败。不能据此评价完整实验设计。

**代码。** 正式项目为 [HICAI-ZJU/SciToolAgent](https://github.com/HICAI-ZJU/SciToolAgent)，**428 stars**；[LICENSE](https://raw.githubusercontent.com/HICAI-ZJU/SciToolAgent/main/LICENSE) 为 MIT。README 的 Planning/Executor/Summarizer 与依赖说明已查看，属于整套工具调度平台。

**整理建议（推断）。** 工具目录、输入输出约束可作参考；因正文阅读缺口和平台依赖，本轮不列首批试用。未核引用数或独立采用效果。

## 年度分区与声誉的边界

本轮已核上述论文的出版记录（SciToolAgent 为官方搜索元数据），**未完成逐刊的年度中科院大类分区权威表核对**；不能把这六项整体标为“已认证大类一区”。没有用 JCR Q1 替代中科院分区。

检索找到 [深圳大学图书馆分区表服务说明](https://www.lib.szu.edu.cn/er/fenqubiao)，公告提到 2026 年不再更新及平台服务调整；另找到 [乐山师范学院公开的 2025 年表附件页面](https://kejc.lsnu.edu.cn/info/1045/7011.htm)，但附件未成功读取。因此这里保留年度核验缺口，没有编造“2026 中科院分区”。

这里的实际优先级来自任务贴近程度、可读代码/技能和可核产物。ChemCrow/Coscientist 的千次级引用提供比单一期刊标签更多的影响证据；Paper2Agent/JCTC 技能项目较新，应通过后续实用性试验判断，不因低引用直接淘汰。知名作者与机构仅作阅读线索，不作为无条件采纳依据。
