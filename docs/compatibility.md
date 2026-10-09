# 兼容性

2026-10-08 补充：Windows 原生 Python 3.13.5 已运行打包/安装器测试（18 项通过、1 项符号链接测试因权限跳过），新图形插件的本地 MCP 通信亦已在 Windows 和 WSL 验证。此结果不代表 Windows Codex 内嵌 UI 或完整科研任务已验证，详见 [验证记录](validation.md) 与 [插件说明](codex-plugin.md)。

本仓库采用一份技能源码，按实际运行环境安装。安装工具需要 Python 3.10+，仅使用标准库；无需 Bash、systemd、管理员权限或符号链接。

| 环境 | 安装入口 | 技能目录 | 当前验证边界 |
| --- | --- | --- | --- |
| Windows 原生 | `py -3 tools/manage.py install` | 当前用户的 `.agents\skills` | 已运行原生安装器测试；宿主科研任务仍待验证 |
| WSL / Linux | `python3 tools/manage.py install` | `~/.agents/skills` | 本地安装器检查已运行 |
| macOS | `python3 tools/manage.py install` | `~/.agents/skills` | 按同一接口设计，未实测 |

Windows 窗口承载的智能体也可能在 WSL 中执行。目录由智能体和安装命令的实际运行环境决定；Windows 与 WSL 的用户主目录不是同一个目录。

## Codex

根据 [官方技能文档](https://learn.chatgpt.com/docs/build-skills)，支持用户级 `~/.agents/skills` 和项目级 `.agents/skills`，显式调用及根据描述自动选择。相同名字的多份技能不会合并，应避免无意重复安装。

包内 `agents/openai.yaml` 保留英文技能名称，并提供中文用途简介，不修改默认隐式调用策略。本仓库本身不是带 UI 的 Codex 插件。

## DeepSeek Harness

**目前暂未实测 DSH 兼容性。** 以下内容依据文档整理，仅作配置参考；尚未验证技能发现、自然语言选择、脚本执行或完整任务效果。

根据 [官方技能子系统文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md)，默认本地提供器发现 `.dsh/skills`、`.agents/skills` 和配置的目录，项目级条目优先于用户级条目。

用户级共享目录默认位于用户主目录的 `.agents/skills`；DSH 可通过 `agentsHome` 或 `DSH_AGENTS_HOME` 改写位置，见 [实现](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/src/index.ts)。有自定义配置时用安装器的 `--target` 指向实际技能目录。

本仓库依赖 DSH 已启用技能发现与调用能力，不替用户修改 DSH 插件组成。能解析 `SKILL.md` 不表示一定读取 `agents/openai.yaml`，也不保证展示 Codex 的中文技能菜单。

## 模型和科研工具

宿主发现技能、模型遵循技能、外部工具完成任务是三层不同能力。模型切换后应使用一个真实但小规模的任务复查；本仓库没有验证所有模型组合。文献全文访问、联网检索和科学软件需要由用户所在环境提供。

## 验收方法

安装后运行 `status`，确认文件已部署；在宿主的新会话中检查能发现稳定英文技能名及正确路径，再给出一个小任务，核对是否实际读取了技能与资料。只有完成这些步骤才记录该宿主组合“实际验证通过”。

GitHub Actions 检查安装工具在 Windows/Ubuntu 下的文件操作，不验证模型行为或科学正确性。官方发现机制核对日期：2026-10-08。
