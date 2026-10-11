# LLMskill-forChem

> 本仓库新增代码由 **GPT-6 Astra** 生成，人工部分仅为向 LLM 提出需求和指定 skill。引用的上游技能及代码保留原作者署名、来源与许可证。

> **Token 与耗时提示：** 技能目录、正文、工具结果与执行记录会占用上下文；整个任务的总 token 和耗时取决于实际执行路径。[首轮 Windows DSH 对照](docs/evaluations/2026-10-10-dsh/README.md)已记录 21 次运行，未证明普遍节省 token 或提升质量，部分任务开销显著。用量中含大量缓存读取，不能套用单一价格；“省搜集时间”不代表“省 token”。

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

[六问 Astra / DeepSeek 三组实测](docs/evaluations/2026-10-11-astra-deepseek/README.md)提供逐题 token、耗时、回答质量观察及原始最终回答。两种宿主下 router 的成本变化方向不同，尚无稳定省 token 的证据；模型版本标识与测试边界见报告。

[首轮 Windows DSH 对照](docs/evaluations/2026-10-10-dsh/README.md)记录同一论文的 7 道问题、三组 21 份回复、资源消耗和独立上下文模型盲审。部分任务受益，部分增加消耗或出现错误；没有证明普遍优势，也不是专家认证。该轮 router 优先指令未实际注入，不能把组间差异归因为 router；新版本效果尚待复测。

该测试只覆盖指定 Windows/headless DSH 配置下的部分技能，不认证桌面 UI、默认目录或 VASP/DFT 能力。[完整验证范围](docs/validation.md)

## 可选：图形选择面板

面板显示英文技能名、中文用途和来源，用于选择并插入请求。它独立安装，普通技能使用无需面板。[面板说明](docs/codex-plugin.md)

## 来源与许可

技能来自 [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills)、[Computational Chemistry Agent Skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills)、[Google DeepMind Science Skills](https://github.com/google-deepmind/science-skills)、[K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills)、[BootLoops Skills](https://github.com/BootLoops-ai/skills)。各技能目录保留固定来源、版本和许可证；`scientific-skill-router` 为本仓库新增的选择入口。

本仓库新增代码与说明采用 [MIT 许可证](LICENSE)。上游内容按各自许可证使用，详见 [第三方声明](THIRD_PARTY_NOTICES.md)。

版权与再分发检查见 [逐项许可审查](docs/license-audit/README.md)。授权或随附许可未核清的技能暂停收录，不代表认定上游侵权。
