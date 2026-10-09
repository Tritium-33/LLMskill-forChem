# LLMskill-forChem

为化学与材料研究者筛选、归类和说明实用的开源 LLM skills，提供中文使用示例与便捷的安装方式。

当前收录48项技能：原有5项通用科研协议、42项 K-Dense 化学与通用科研技能，以及1项本地技能选择入口。[K-Dense 分类目录、用途和依赖](docs/kdense-skills.md)。技能可安装，不代表配套软件已安装或科学效果已验证。

技能是交给智能体的操作指导，不是模型训练权重，也不自带文献数据库、计算软件或模型账号。原文多为英文，可以用中文提出任务。

## 定位与收录原则

本项目以筛选、使用说明和实践记录为主要工作。安装工具是使用配套，后续根据真实需求维护。

- **按科研任务组织。** 说明技能适合解决什么问题，需要哪些输入，预期交付什么，以及何时不适用。
- **跨来源精选。** 可收录来自不同项目、许可允许分发的技能，也可仅提供上游链接与使用说明；列入推荐与纳入安装包分别标明。
- **保留上游关系。** 优先复用原始技能，记录固定版本、许可和必要修改。适用于化学的通用技能不需要为了领域名称而强行改写。
- **用实例判断实用性。** 后续为推荐项补充可公开的小型化学任务、执行记录、表现与局限。目录或安装检查通过，只代表能打包部署。
- **分别评价学术依据与使用证据。** 论文优先考察领域相关性、实际结果与后续引用/采用，记录分区年度；项目考察代表技能、维护、许可与可检查产物。期刊分区、作者名气和 GitHub stars 都不能单独作为收录依据。
- **明确验证程度。** 区分候选、已检查内容与依赖、已完成任务示例、已有重复使用反馈。原有五项完成了内容与来源检查、格式及安装器测试；新增项保留固定版本及依赖声明，尚未完成化学任务的系统效果验证。

[2026-10-08 候选来源初筛](docs/discovery/2026-10-08/README.md) 汇总论文与 GitHub 两条路线、优先试用项及证据缺口；其中本次收录的 K-Dense 项已加入安装包，其余仍按候选标记。

## 按板块自动选择技能

`scientific-skill-router` 提供四个板块索引：化学与材料、科研检索与论证、数据统计与机器学习、写作与图表。任务明确时直接使用具体技能；需要选择或组合时，入口先读取相关索引，再读取必要的技能原文。

可以直接说：“帮我选择合适的科研技能，分析这批数据并生成图。”也可明确使用 `$scientific-skill-router`。自动选择由宿主和模型依据描述完成，索引不是确定性调度程序，不保证每次路由最优。它不会把所有技能正文加载到上下文，也不会自动安装软件或启动付费服务。这里仅索引已收录的42项，不声称覆盖 K-Dense 整库。

修改 `catalog.json` 的 `routing_group` 或上游技能后，运行 `python tools/build_skill_index.py` 更新索引，再重新部署 `scientific-skill-router`。分类缺失会报错，不会静默遗漏新增 K-Dense 技能。

## 与 BootLoops Skills 的关系

[BootLoops Skills](https://github.com/BootLoops-ai/skills) 已将其定量科研工作协议整理成可供智能体加载的技能，并提供插件和安装方式。本项目首批四项直接来自它，因此在内容与分发功能上存在明确重叠。

本项目计划提供的额外便利是面向化学同行的跨来源选择、中文任务说明、实际使用记录与安装指导；这些需要在持续使用中积累。现阶段应将本仓库看作注明来源的精选整理版，不能把转载、翻译或安装封装表述为新的科研方法。

## 原有五项科研协议

| 中文名称 | 技能标识 | 用途与自然语言示例 |
| --- | --- | --- |
| 原文证据核查 | `reading-contract` | “核对论文中支持结论的原文、页码和图表，区分事实与推断。” |
| 文献深审与创新性审查 | `lit-review` | “审查这个研究主张与已有工作的重叠，记录检索范围与未读全文。” |
| 参考文献核验 | `ref-check` | “核验参考文献的作者、题名、年份和 DOI，并检查关键引用。” |
| 验证独立性与数据泄漏检查 | `independence-bookkeeping` | “检查分子性质模型的训练、调参、测试数据及验证路线是否独立。” |
| 研究方向纠偏 | `research-direction-recovery` | “根据目标与现有结果，提出能改变研究决策的下一步验证。” |

日常读一篇论文通常先用原文证据核查；只有需要系统审查研究主张时才使用文献深审。无需每个任务加载全部技能。更多组合步骤见 [使用指南](docs/usage.md)。

## 可选图形面板

新增42项已进入仓库构建目录；先前安装的面板不会自动更新，需要重新构建和安装插件。

[化学科研技能面板](docs/codex-plugin.md) 显示原始英文技能名、中文用途、来源链接与选择按钮。兼容宿主可将技能插入当前输入框，也可通过原生 `@` 搜索选择；浏览器入口提供一键复制。选好后在对话里写任务，无需在面板填写表单。真实 Windows Codex 的插入与原生菜单显示仍需客户端验证。

在仓库根目录运行 `py -3 tools/build_plugin.py --zip`（Linux/WSL 使用 `python3`），生成 `dist/chem-skill-panel` 和 ZIP。面板从现有 `catalog.json`、`skills/` 构建，不增加需单独维护的技能原文副本。首次安装及支持边界见上面的面板说明。

## Windows 快速开始

需要 Python 3.10 或更新版本，以及能读取本地技能的 Codex 或 DeepSeek Harness（DSH）。从 [Python 官方网站](https://www.python.org/downloads/windows/)安装 Python 后，打开 PowerShell 验证 `py -3 --version`。若使用的发行版只有 `python` 命令，将下文 `py -3` 替换为 `python`。

获得仓库文件后，在包含本 README 的文件夹中打开 PowerShell。可以通过 Git 克隆；仓库公开后，也可以在 GitHub 点击 **Code → Download ZIP** 并解压，首次安装不要求会用 Git。

```powershell
py -3 tools/manage.py list
py -3 tools/manage.py install --dry-run
py -3 tools/manage.py install
py -3 tools/manage.py status
```

默认安装到当前 Windows 用户的 `.agents\skills`。程序会打印实际目标目录；无需管理员权限。它会复制技能，不依赖 WSL、Bash 或符号链接。

## WSL / Linux / macOS 快速开始

同样需要 Python 3.10+；在仓库根目录运行：

```bash
python3 tools/manage.py list
python3 tools/manage.py install --dry-run
python3 tools/manage.py install
python3 tools/manage.py status
```

默认安装到运行该命令的用户目录 `~/.agents/skills`。Windows 原生智能体与 WSL 智能体使用的用户目录不同，请在智能体实际运行的环境安装。完整说明见 [安装、更新与卸载](docs/install.md)。

## 调用与宿主支持

安装后向智能体直接描述任务即可。需要明确指定时，可以说：“请使用 `reading-contract` 核查这篇论文。”Codex 还支持 `$reading-contract` 等显式调用。自动选择由宿主和模型决定，中文显示名不是固定的关键词路由。

Codex 和 DSH 的默认本地发现机制都支持用户级 `.agents/skills`；项目级安装与自定义目录见 [兼容性说明](docs/compatibility.md)。本仓库不会修改模型、API 密钥或宿主的工具权限。文献检索与全文阅读需要宿主提供相应工具和可访问的资料。

## 修改与同步

只在本仓库的 `skills/` 修改技能，再执行安装命令更新部署副本。不要同时维护安装目录与源码目录。

从 GitHub 拉取更新后，再安装一次：

```bash
git pull --ff-only
python3 tools/manage.py install
```

Windows 将最后一行替换为 `py -3 tools/manage.py install`。如果在已安装副本中发现手动修改，工具会停止并报告冲突。ZIP 下载用户重新解压完整新版，审查后运行安装命令即可。

GitHub 账号、无图形界面登录、首次上传与日常同步步骤见 [GitHub 入门](docs/github.md)。GitHub 用于版本保存与分发；上传本身不会自动安装技能。

## 验证范围

- 安装器仅依赖 Python 标准库，包含预览、选装、冲突保护、备份、状态检查与卸载。
- Linux/WSL 本地验证记录见 [验证记录](docs/validation.md)。
- 已配置 Ubuntu / Windows、Python 3.10 / 3.13 的 GitHub Actions；配置存在不表示远端检查已经运行。
- Windows 原生、macOS 和 DSH 中的实际发现与任务执行仍须分别验证。安装器测试不证明模型给出的科学结论正确。

## 来源与许可

前四项源自 [BootLoops Skills](https://github.com/BootLoops-ai/skills)，研究方向纠偏源自 [CatMaster](https://github.com/q734738781/CatMaster)。版本固定在各技能的 `SOURCE.json`，保留上游许可与声明。本仓库的整理、中文元数据和工具不代表这些科研方法由本项目首创。

本仓库原创说明与工具采用 [MIT](LICENSE)，上游技能分别保留自己的许可，具体见 [第三方声明](THIRD_PARTY_NOTICES.md)。
