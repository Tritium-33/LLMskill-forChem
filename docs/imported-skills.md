# 新增技能与运行边界

保留上游英文名称、原始正文和附属文件，按功能归类。不是三个完整计算平台的安装，也未验证这些技能能改善收敛或科研结果。

| 来源 | 收录技能 | 用法与限制 |
| --- | --- | --- |
| [AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills) | `mat-dft-vasp` | VASP 输入准备与结果提取；另需 pymatgen 等依赖。上游 `venv/run`、`src/` 和 atomate2 MCP 未打包，原文命令不可直接假定可运行。 |
| [Computational Chemistry Agent Skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills) | `dft-vasp`、`dft-qe`、`dpdata-cli`、`dpdisp-submit` | 前两项准备输入；结构转换和作业提交按需另用后两项。VASP 的四个子流程完整保留在父目录中，不另列为四个顶层技能。 |
| [Google DeepMind Science Skills](https://github.com/google-deepmind/science-skills) | `literature-search-arxiv`、`literature-search-openalex`、`uv`、`credentials` | 指定数据库的脚本检索，另附运行与凭据指导。先确认 API 当前访问条件；检索到元数据不代表已读全文。 |

默认按目标、已有依赖和输入选择一个主要技能，不随机选择或叠加所有同用途技能。`mat-dft-vasp` 与 `dft-vasp` 不合并参数；用户给定的赝势、磁性、计算设置和项目约束优先。解析器成功退出不能证明电子/离子收敛，应另核对被中断和未完成计算。

## 安装与调用

全部安装沿用 README 中的命令。只装部分技能可以重复 `--skill`：

```bash
python tools/manage.py install --skill dft-qe --skill dpdata-cli --skill uv
python tools/manage.py install --skill literature-search-openalex --skill uv --skill credentials
```

依赖技能不会由安装器自动补齐；上例列出了相应配套项。提交作业时另外选择 `dpdisp-submit`，并配置自己的软件和调度环境。安装技能不会启动计算、安装科学软件或索取密钥。

自然语言示例：“为这个结构准备 QE 输入，暂不提交。”“使用 arXiv 检索这个主题，并区分预印本与正式发表记录。”也可以先用 `$scientific-skill-router` 选择所需技能。router 支持单项和组合任务；单项只需简短说明所用技能，组合任务按 README 附执行记录。

技能目录中的 `PACKAGING.md` 记录打包边界，`SOURCE.json` 记录固定提交、路径及原文件 SHA-256。DeepMind 的目录按原始 frontmatter 名称改为连字符形式，文件正文未改。安装工具支持 Windows；上游 Bash、envsubst、tmux、集群及凭据示例可能需要 WSL/Linux 或适配，新增科学流程没有完成原生 Windows 验证，DSH 仍未实测。

## 验证范围

这次检查覆盖源文件一致性、许可附件、目录索引、Python 语法、安装器回归和插件打包。没有运行 VASP/QE、提交集群作业、调用收费 API 或证明科学有效性。Paper2Agent 仅参考；CatMaster 仍未收录。
