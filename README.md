# LLMskill-forChem

> 本仓库新增代码由 **GPT-6 Astra** 生成，人工部分仅为向 LLM 提出需求和指定 skill。引用的上游技能及代码保留原作者署名、来源与许可证。

面向化学与材料研究者的开源技能集合，提供中文用途说明、按板块选择技能的入口，以及适用于 Windows 和 Linux/WSL 的安装工具。

Skill 是供 AI 助手读取的任务指导和配套资源。安装后，你可以直接用中文描述任务，或指定技能名称，让助手按相应流程处理。

## 可以用来做什么

本仓库收录 **48 项技能**：42 项 K-Dense 化学与通用科研技能、5 项科研审查与研究规划技能，以及1项技能选择入口。

| 任务 | 技能示例 |
| --- | --- |
| 晶体、分子与化学数据处理 | `pymatgen`、`rdkit`、`datamol` |
| 光谱、反应动力学与相平衡 | `nmrglue`、`matchms`、`cantera`、`pycalphad` |
| 文献检索与引用管理 | `paper-lookup`、`literature-review`、`citation-management` |
| 科研论证与实验设计 | `hypothesis-generation`、`experimental-design`、`scientific-critical-thinking` |
| 数据分析、统计与机器学习 | `statistical-analysis`、`scikit-learn`、`pymc`、`shap` |
| 科研写作、绘图与汇报 | `scientific-writing`、`matplotlib`、`scientific-visualization`、`scientific-slides` |
| 原文、文献与参考文献核验 | `reading-contract`、`lit-review`、`ref-check` |
| 验证独立性与研究方向梳理 | `independence-bookkeeping`、`research-direction-recovery` |

[K-Dense 技能分类、用途与依赖](docs/kdense-skills.md) · [使用指南](docs/usage.md)

## 安装

需要 **Python 3.10 或更新版本**，以及支持本地 Skills 的 AI 助手。安装工具仅使用 Python 标准库；具体技能所需的科学软件、Python 版本和外部服务另有要求。

先克隆仓库，或在 GitHub 点击 **Code → Download ZIP** 并解压：

```bash
git clone https://github.com/Tritium-33/LLMskill-forChem.git
cd LLMskill-forChem
```

使用 ZIP 时，在解压后的仓库目录打开终端即可，不需要运行上面的克隆命令。

### Windows

在仓库目录打开 PowerShell：

```powershell
py -3 tools/manage.py list
py -3 tools/manage.py install --dry-run
py -3 tools/manage.py install
```

默认安装到当前 Windows 用户的 `.agents\skills`。如果你的 Python 命令是 `python`，将 `py -3` 替换为 `python`。

### Linux / WSL / macOS

在仓库目录运行：

```bash
python3 tools/manage.py list
python3 tools/manage.py install --dry-run
python3 tools/manage.py install
```

默认安装到 `~/.agents/skills`。Windows 原生助手和 WSL 中的助手使用不同的用户目录，请在助手实际运行的环境中安装。

### 只安装需要的技能

例如只安装 `paper-lookup`：

```bash
python3 tools/manage.py install --skill paper-lookup
```

Windows 将 `python3` 换成 `py -3`。可重复传入 `--skill` 选择多项，用 `--target` 指定宿主读取的技能目录。选择入口不会自动补装其他技能；希望使用完整板块选择功能时，可按上面的默认方式安装全部技能。

更多选项见 [安装、更新与卸载](docs/install.md)；Codex、DeepSeek Harness（DSH）及不同平台的说明见 [兼容性说明](docs/compatibility.md)。

## 怎么调用

安装后，在 AI 助手对话中直接描述任务，例如：

- “查找这个主题的论文，保留 DOI 和来源，说明哪些读到了全文。”
- “检查这个 CIF 的元素、晶胞和周期性结构。”
- “分析这份数据的缺失值，并绘制带单位和误差条的图。”
- “核验这份参考文献的作者、题名、年份和 DOI。”

也可以指定英文技能名：

> 请使用 `paper-lookup` 检索这个主题的论文。

在 Codex 中可以显式调用：

```text
$paper-lookup 检索这个主题的论文，并保留 DOI 和来源。
```

这里的 `$技能名` 是对话中的调用方式，不是在终端运行的命令。自然语言自动匹配取决于宿主和模型。

## 不知道该选哪个技能？

直接说：

> 帮我选择合适的科研技能，检查这批数据并生成图。

或明确指定：

```text
$scientific-skill-router 根据我的目标选择必要技能并完成任务。
```

该入口为已收录的42项 K-Dense 技能提供四个板块索引：

| 板块 | 覆盖内容 |
| --- | --- |
| 化学与材料 | 分子、晶体、光谱、动力学、相平衡、电池与单位误差 |
| 科研检索与论证 | 文献、引用、证据、假设、实验设计与评阅 |
| 数据、统计与机器学习 | 数据检查、统计推断、预测、模型解释与优化 |
| 写作与图表 | 论文、数据图、示意图、幻灯片、格式与文档转换 |

助手按任务读取相关索引，再读取所需技能；不必一次加载全部技能。任务已明确对应某个技能时，可直接使用它。

## 可选：图形选择面板

[化学科研技能面板](docs/codex-plugin.md) 显示英文技能名称、中文用途和来源，方便浏览与选择。兼容宿主支持插入当前输入框；浏览器入口提供复制功能。

面板是可选插件，普通技能安装不会同时安装面板。安装方式与宿主支持范围见 [面板使用说明](docs/codex-plugin.md)。

## 使用前需要了解

- **技能文件与运行环境分别安装。** 科学计算可能需要额外软件；部分检索或图像生成路径需要网络、账号或 API 密钥，具体要求见各技能说明。
- **按任务选择工具。** 例如，真实数据绘图可使用 `matplotlib`，不需要为了画数据图调用外部图像生成服务。
- **核对结果。** 技能被成功加载不等于计算收敛、引用正确或科学结论成立。文件安装的跨平台支持也不代表所有科学依赖都支持同一平台。

## 来源与许可

技能主要来自 [K-Dense Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills)、[BootLoops Skills](https://github.com/BootLoops-ai/skills) 和 [CatMaster](https://github.com/q734738781/CatMaster)。各技能目录保留固定来源、版本和许可证；`scientific-skill-router` 为本仓库新增的选择入口。

本仓库新增代码与说明采用 [MIT 许可证](LICENSE)。上游内容按各自许可证使用，详见 [第三方声明](THIRD_PARTY_NOTICES.md)。
