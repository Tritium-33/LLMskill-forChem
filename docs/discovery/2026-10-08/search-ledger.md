# 论文路线检索与阅读记录

检索日：2026-10-08，UTC+8。通道：会话内网页搜索、出版社/arXiv 页面、官方 GitHub/原始文件；GitHub API 抓取失败记录见 `paper-project-metadata.json`。不是全领域系统综述，没有进行新颖性结论判定。

## 实际查询

没有设置统一起止年过滤；以下查询显式覆盖到 2026，返回候选的主要发表时间为 2023–2026。GitHub 路线的独立查询记录位于 `github-scout.md`。

1. `chemistry large language model agents open source skills Nature 2026 Coscientist ChemCrow`
2. `scientific literature research agent PaperQA2 published Nature 2025 2026`
3. `El Agente autonomous quantum chemistry agent Nature computational science published GitHub 2025 2026`
4. `Nature Nature Machine Intelligence Nature Computational Science 2025 中科院 大类 分区 1区 site:edu.cn`
5. `中科院期刊分区表 2026 2025 自然科学 大类 官网`
6. `"SciToolAgent" "github.com"`
7. `"Nature" "中科院" "综合性期刊" "1区" site:edu.cn`
8. `"Nature Computational Science" "2025" "分区" site:edu.cn`
9. `"Automating Computational Chemistry Workflows via OpenClaw" 2026`
10. `"Journal of Chemical Theory and Computation" "2025" "中科院"`
11. `site:pubs.acs.org "10.1021/acs.jctc.6c00622" "5919"`
12. `site:pubs.acs.org/jctcce/issue/22/12 "Automating Computational Chemistry"`

## 轮次与实际阅读

首轮广搜化学智能体和文献工作流，核 ChemCrow、Coscientist、OpenScholar、Paper2Agent；第二轮追项目仓库与分区来源；第三轮由原生技能仓库线索发现 JCTC 论文，并核 ACS 出版记录。仍有新候选加入，**没有达到系统综述的检索饱和**。

| 来源 | 实际读取范围 | 没有完成的部分 |
|---|---|---|
| ChemCrow 期刊版 | 出版信息、摘要、部分工具方法、Data/Code availability、计数 | 全文连续精读、SI 和实验仓库逐项审查 |
| Coscientist 期刊版 | 出版信息、摘要、Data/Code availability、计数；仓库 LICENSE 全文 | 全文/SI 精读、实验复现 |
| Paper2Agent 期刊版 | 出版信息、摘要、方法/讨论/代码段、部分案例、计数 | 完整 SI、所有评价与结果的独立复核 |
| Paper2Agent 仓库 | README/许可、顶层 paper2agent SKILL 全文、打开子 SKILL | 所有资源和脚本、运行验证 |
| OpenScholar 期刊版 | 出版信息、摘要、方法中检索/引用核查、部分评测段、计数 | 全文/SI 精读、模型或检索复现 |
| JCTC 技能论文 | ACS 官方搜索返回的摘要页正文、历史与卷期元数据；arXiv v2 框架、案例、结论段 | 期刊付费全文、预印本全文连续精读、SI trace 逐项核查 |
| SciToolAgent | 出版社搜索元数据/摘要与代码入口、仓库 README 部分与 LICENSE | 期刊正文访问失败，标记 FULL-TEXT-UNREAD |

所有文章均为**初筛/部分阅读**，不借用“全文已读”标签。具体结论只归属于已读段落；未读内容保留为缺口。

## 访问与范围缺口

- 出版社题名、历史、期刊字段优先于仓库 BibTeX；例如 ChemCrow 仓库仍列 2023 预印本，报告采用期刊 2024 信息。
- GitHub API 四个主项目返回 403 rate limit exceeded；没有继续请求规避限流，改用公开网页。API 错误不说明项目不存在。页面 stars 可能是缓存近似数。
- ACS DOI/卷期直接打开有 403，官方搜索返回可见正文；正式发表可据此核实，期刊全文仍未读取。arXiv v2 单列，未冒充期刊终版。
- SciToolAgent 出版社正文未打开；分区表附件未下载成功；没有绕过登录、订阅或访问限制。
- 未完成 Web of Science/Scopus/Google Scholar 的统一被引检索、作者去重或 ESI 高被引认定。出版社计数只作粗略影响线索。
- 没有完成每篇论文双向引文链和每位作者到当月的完整作品追踪，没有逐题审查所有 benchmark；不能用于证明“没有其他同类项目”或科研创新性。
- El Agente/Quntur 等搜索线索未完成正式发表与代码核验，未混入已发表推荐名单；尚未核验不等于不存在或质量低。
- 原生技能多数还很新；未取得足够独立社区成效记录。仓库署名复用证明发生了复用，不证明科学效果。
- 本轮没有安装、调用付费 API、访问计算集群或运行 Windows 测试；可移植性建议是基于依赖与脚本入口的判断。

下一轮若用于实际收录，应固定少量候选版本并完成公开小样例；若用于文章相关工作或创新性论证，则需要另做全文和引文链审计。
