# 安装、更新与卸载

所有命令在仓库根目录运行。本文使用 `python` 表示 Python 3.10+；Windows 常用 `py -3`，Linux/WSL 常用 `python3`。首次运行先检查版本。

## 选择安装范围

默认安装到当前用户的 `~/.agents/skills`；请确认宿主实际读取此目录。DSH 尚未实测：

```text
python tools/manage.py install --dry-run
python tools/manage.py install
```

只装一项，用稳定英文标识；可重复 `--skill`：

```text
python tools/manage.py install --skill reading-contract --skill ref-check
```

如需项目级安装，将 `--target` 指向目标项目下的 `.agents/skills`，并在该项目中启动智能体。例如 Windows：

```powershell
py -3 tools/manage.py install --target "C:\Research\my-project\.agents\skills"
```

项目应当是独立于本技能源码仓库的目录。DSH 的项目目录发现行为需以实际版本验证。不要在用户级和项目级重复安装同名技能，除非确实需要分别维护版本。

自定义安装目标时，后续 `status`、更新、卸载都要传入同一个 `--target`。程序不会扫描或更改其他用户、Windows/WSL 的另一侧或其他智能体配置。

## 按用途查找与按板块安装

```text
python tools/manage.py list --search 文献
python tools/manage.py list --group chemistry-materials
python tools/manage.py install --group chemistry-materials --skill scientific-skill-router --dry-run
```

`--search` 只用于 `list`，匹配英文名称或中文用途，不会自动安装搜索结果。没有匹配项时返回状态码 `1`。

`--group` 使用以下标识，可重复传入，也可和 `--skill` 合用；选择范围取并集。适用于 `list`、`install`、`status` 和 `uninstall`。卸载板块前先用 `--dry-run` 查看范围。

| 标识 | 板块 |
| --- | --- |
| `chemistry-materials` | 化学与材料 |
| `research-evidence` | 科研检索与论证 |
| `data-modeling` | 数据、统计与机器学习 |
| `writing-figures` | 写作与图表 |
| `runtime-support` | 运行与作业支持 |

router 是独立入口，不归入上述板块，需要时用 `--skill scientific-skill-router` 添加。板块选择不自动解析配套技能或安装软件。状态输出仅反映指定目录中的文件与清单，不证明宿主已加载技能或科学环境可运行。

## 更新和冲突

先更新源码，再更新安装副本：

```text
git pull --ff-only
python tools/manage.py install --dry-run
python tools/manage.py install
python tools/manage.py status
```

这是显式更新，不会自动联网或定期拉取。运行中的长任务建议完成后再更新。Codex 按官方机制发现变更；若未显示，重新打开会话或重启应用，并确认实际安装目录。

对于已存在的目录：

- 与本仓库逐文件一致：记录为本工具管理，不重写技能正文。
- 由本工具安装且未改动：允许从源码更新，旧版本先备份。
- 来自其他安装方式或已被手动修改：停止，要求先检查差异。
- 只有明确使用 `--replace` 才会备份并替换冲突副本。该选项只适用于安装，不用于强制卸载。

明确决定替换某一项后，例如：

```text
python tools/manage.py install --skill ref-check --replace --dry-run
python tools/manage.py install --skill ref-check --replace
```

不要把需要保留的研究笔记放进已安装的技能目录。将有价值的技能修改合并回源码，再部署。

## 状态、卸载与恢复

```text
python tools/manage.py status
python tools/manage.py uninstall --skill reading-contract --dry-run
python tools/manage.py uninstall --skill reading-contract
```

不指定 `--skill` 时卸载本仓库列出的全部技能。工具不会卸载未接管的同名目录，也不会删除其他个人技能。存在本地修改时会拒绝卸载。

状态码：`0` 表示命令成功；`status` 的 `1` 表示有缺失、更新或冲突，逐项看输出；`2` 表示输入或操作错误。

安装清单位于目标目录中的 `.llmskill-forchem.json`。它记录文件哈希，用于判断哪些文件由本工具安装、之后是否被修改；不是个人账号配置。

每次有变更的操作会打印备份目录，位于目标目录的父目录下 `.llmskill-forchem-backups/<操作编号>/`。备份保留旧技能和旧安装清单，不会自动清理。

恢复时先停止安装/更新操作，将当前副本另存，再从对应备份复制需要的技能目录。只有完整恢复同一次操作涉及的全部技能时，才整体恢复该次旧清单；只恢复一项时保留当前清单，`status` 会标记差异，之后审查并重新安装。不要把备份整体复制成新的技能发现目录。

安装过程中常规文件操作失败会尝试回滚。进程被强制终止或断电时不保证自动回滚，先检查备份与目标目录。如果遗留 `.llmskill-forchem.lock` 文件夹，确认没有安装进程运行后再移除该空锁目录。

## 迁移旧安装

已经通过其他工具安装过这些技能的用户，先运行 `install --dry-run`。若来源元数据或技能正文不同，出现冲突是正常保护。对照源码检查后，用 `--skill 名称 --replace` 逐项接管；旧版本留在备份中。

从此只编辑本仓库，不编辑用户目录中的部署副本。公开仓库之外的个人技能可以继续保留；安装器只管理目录清单中选定的技能。

## 已验证的安装工具范围

2026-10-09：本轮 28 项安装、更新保护、回滚、搜索、板块选择、插件打包与索引检查在 Linux/WSL 下全部通过；Windows 原生 Python 3.13.5、默认文本编码 `cp936`、关闭 UTF-8 模式下，27 项通过，1 项因无符号链接创建权限跳过。测试使用独立临时目录，不覆盖个人已安装技能。

CI 使用以下命令，将遗漏文本编码产生的警告视为错误，即使运行器本身使用 UTF-8 也能发现这类遗漏：

```text
python -X warn_default_encoding -W error::EncodingWarning -m unittest discover -s tests -v
```

这些结果验证的是安装与打包工具，不代表宿主发现行为、DSH 兼容性或各项科学计算已验证。
