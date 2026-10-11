# LLMskill-forChem

> 本仓库新增代码由 **GPT-6 Astra** 生成，人工部分仅为向 LLM 提出需求和指定 skill。引用的上游技能及代码保留原作者署名、来源与许可证。

> **效果与消耗提示：** [GPT-6 Astra Medium / DeepSeek v4.1 Flash 实测](docs/evaluations/2026-10-11-astra-deepseek/README.md)中，部分技能组在专业表达、证据说明和文献覆盖上表现出改善，同时增加了 token 消耗；事实准确性及整体质量的提升尚未经过全面独立评审。router 的资源开销随执行路径变化，未显示稳定的节省效果。“省搜集时间”不代表“省 token”；统计含缓存读取，不能按单一价格换算费用。

面向化学与材料研究者的开源技能集合，提供中文用途说明、按板块选择技能的入口，以及适用于 Windows 和 Linux/WSL 的安装工具。

这个项目起源于作者使用相关工具时的困扰：开源科研技能项目很多，化学与材料相关内容常常散落在大量其他领域的技能中；同时安装多个项目，又会增加配置、筛选和维护的负担。因此，本仓库将部分开源项目中的相关技能集中整理，提供一个方便起步、节省自行搜集时间的选择，也可以把它理解为一个“懒人包”。收录基于作者有限的使用需求与了解，尚未经过全面、多轮效果验证，不保证更高效，也不一定适合每个人。有经验的使用者更适合按自己的研究方向选择、调整和验证技能。

Skill 是供 AI 助手读取的任务指导和配套资源。安装后，你可以直接用中文描述任务，或指定技能名称，让助手按相应流程处理。

## 可以用来做什么

收录 **52 项具体技能和 1 项可选 router**。保留英文名称，用中文解释用途，按功能组织并注明来源。

| 任务 | 技能示例 |
| --- | --- |
| DFT 输入与结果处理 | `dft-vasp`、`mat-dft-vasp`、`dft-qe` |
| 分子、晶体、光谱与物理化学 | `rdkit`、`pymatgen`、`nmrglue`、`cantera` |
| 文献检索、阅读与论证 | `paper-lookup`、`reading-contract`、`lit-review` |
| 数据分析与建模 | `statistical-analysis`、`scikit-learn`、`pymc` |
| 写作、绘图与汇报 | `scientific-writing`、`scientific-visualization`、`scientific-slides` |

[完整技能目录、选择区别与依赖](docs/skills-catalog.md) · [使用示例](docs/usage.md)

**不想记技能名，可以让 `scientific-skill-router` 帮你选择。** 它支持单项和组合任务；是否自动触发取决于宿主与模型，项目不设置强制优先规则。

## 安装

需要 Python 3.10+ 和支持本地 Skills 的 AI 助手。先克隆仓库，或在 GitHub 点击 **Code → Download ZIP** 后解压并打开终端：

```text
git clone https://github.com/Tritium-33/LLMskill-forChem.git
cd LLMskill-forChem
```

Windows PowerShell：

```powershell
py -3 tools/manage.py list
py -3 tools/manage.py install --dry-run
py -3 tools/manage.py install
```

Linux / WSL：

```bash
python3 tools/manage.py list
python3 tools/manage.py install --dry-run
python3 tools/manage.py install
```

默认安装到当前环境用户的 `~/.agents/skills`。Windows 原生和 WSL 的用户目录不同，应在助手实际运行的环境中安装；宿主使用其他目录时加 `--target`。已有本地修改不会被静默覆盖。

不必全装。以下 `python` 在 Windows 可换为 `py -3`，Linux/WSL 可换为 `python3`：

```text
python tools/manage.py list --search 文献
python tools/manage.py install --skill paper-lookup
python tools/manage.py install --group research-evidence --skill scientific-skill-router
```

单项技能可独立安装；router 不自动补装技能或依赖。[安装、更新与卸载](docs/install.md) · [平台与宿主兼容性](docs/compatibility.md)

## 怎么调用

直接用中文描述任务，例如“分析这篇论文”或“检查这些 CIF，汇总晶胞参数并画图”，同时提供实际文件或链接。

需要明确让 router 帮忙选择时：

> 先用 scientific-skill-router 选择必要技能，再分析这篇论文。

知道技能名时也可以直接指定，例如：

> 用 paper-lookup 查找这个主题的论文。

调用过程是 **自然语言任务 → 选择必要技能 → 读取指导并检查依赖 → 操作工具 → 返回结果**。已有材料会复用，只有需要跨技能交接才使用组合路线；不会要求你选择 workflow 或填写任务表单。个人是否优先使用 router 由你决定，见[调用与记录说明](docs/usage.md#调用与执行记录)。

组合任务经 router 组织时，答复前应列出 `【本轮技能】` 和 `【执行步骤】`，记录实际操作、结果和未完成项。单项直接调用不强制加此前缀。记录由模型依据实际操作整理，并非后台监控或正确性保证。

## 装载技能不等于运行科学软件

安装器只复制技能文件和配套资源。装载技能不会因此自动下载或运行 VASP、Quantum ESPRESSO 等科学软件，也不会自动提交计算。执行具体任务可能另需软件、网络、账号、API 密钥及计算资源，按所选技能检查。

技能文件能安装，不代表相关科学软件支持该平台；技能读取成功，也不代表计算收敛或结论正确。

## 已有测试与使用限制

最近一次对照使用同一篇论文、六个连续问题，分别测试 **A 无技能、B 要求使用合适技能、C 指定 router**。GPT-6 Astra Medium 与 DeepSeek v4.1 Flash 各完成18份回答。

| 模型与宿主 | A 无技能：token / 秒 | B 自选技能：token / 秒 | C 指定 router：token / 秒 |
| --- | ---: | ---: | ---: |
| GPT-6 Astra Medium / Codex | 1,099,535 / 355.8 | 1,761,676 / 395.2 | 2,699,391 / 485.2 |
| DeepSeek v4.1 Flash / DSH | 847,183 / 218 | 12,042,457 / 716 | 4,612,317 / 499 |

实际读取情况如下，仅统计主会话；两边A组均为0。单项技能次数不含router，补读另计一次：

| 模型 | 组 | 单项技能读取/调用 | router读取/调用 | 不同技能数（含router） | 发生读取的轮次 |
|---|---|---:|---:|---:|---:|
| GPT-6 Astra Medium | B | 2 | 0 | 2 | 2/6 |
| GPT-6 Astra Medium | C | 5 | 1 | 5 | 3/6 |
| DeepSeek v4.1 Flash | B | 4 | 0 | 4 | 2/6 |
| DeepSeek v4.1 Flash | C | 5 | 1 | 6 | 4/6 |

Astra C包含一次对同一技能的补读；DSH C依据原始事件流更正为6次总调用（原回执为7次）。连续会话可沿用已读技能，表中轮次不是技能作用覆盖率。[逐技能次数、逐题顺序与分析](docs/evaluations/2026-10-11-astra-deepseek/README.md#技能与-router-调用的定量分析)

以上为六轮合计，DSH B 包含子代理消耗。技能与 router 均有实际读取记录。**初步审计观察到，部分技能组在专业表达、证据说明和文献覆盖上有所改善：**例如 Astra B 的前作选择覆盖 Fe 位点、协同理论和 CoFe，C 在创新性题进一步扩展了相关研究，并明确说明阅读范围和证据限制。

这些改善具有实际参考价值，但收益随任务而异：Astra 前四题的核心回答较接近，无技能组也能完成较好的分析；DSH 部分回答仍有延迟交付、文献归属错误或过强批评。**专业性与可核查性的改善，不等于事实准确性已全面提高；后者及整体质量仍需独立评审。**两种模型的技能组均增加了 token 消耗，router 相比自选技能的消耗变化方向不同。

两边的工具、网络、缓存及委派条件不同，不能据此归因于纯模型差异或换算费用。质量评价是知晓组别的初步审计，不是专家认证或准确率排名。测试固定于提交 `cf65781`，不代表后续版本效果。

[简要统计、逐题消耗与效果分析](docs/evaluations/2026-10-11-astra-deepseek/README.md) · [36份原始问题与最终回答](docs/evaluations/2026-10-11-astra-deepseek/answers.json)

另有[首轮 Windows DSH 对照](docs/evaluations/2026-10-10-dsh/README.md)，包含七题、三组21份回复及独立上下文模型盲审。该轮未实际注入 router 优先指令，应与上述明确要求使用技能/router 的测试分开理解。

现有测试只覆盖特定 Codex 与 Windows/headless DSH 环境下的部分文献任务，不认证 DSH 全面兼容、桌面 UI、默认目录或 VASP/DFT 计算能力。[完整验证范围](docs/validation.md)

## 可选：图形选择面板

面板显示英文技能名、中文用途和来源，用于选择并插入请求。它独立安装，普通技能使用无需面板。[面板说明](docs/codex-plugin.md)

## 来源与许可

技能来自 [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills)、[Computational Chemistry Agent Skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills)、[Google DeepMind Science Skills](https://github.com/google-deepmind/science-skills)、[K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills)、[BootLoops Skills](https://github.com/BootLoops-ai/skills)。各技能目录保留固定来源、版本和许可证；`scientific-skill-router` 为本仓库新增的选择入口。

本仓库新增代码与说明采用 [MIT 许可证](LICENSE)。上游内容按各自许可证使用，详见 [第三方声明](THIRD_PARTY_NOTICES.md)。

版权与再分发检查见 [逐项许可审查](docs/license-audit/README.md)。授权或随附许可未核清的技能暂停收录，不代表认定上游侵权。
