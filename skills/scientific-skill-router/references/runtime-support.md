# 运行与作业支持

仅在所选科学技能确有需要时加载；安装软件、凭据配置和提交作业是独立操作，不因加载技能自动执行。

表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。

| 技能 | 用于什么任务 | 来源 |
| --- | --- | --- |
| `dpdisp-submit` | 通过 DPDispatcher 管理已获授权的本地或集群作业 | [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/5c19e75b256d49849574c999b1965d94024ee072/tools/dpdisp-submit/SKILL.md) |
| `uv` | 配置 uv 并运行带独立依赖的 Python 脚本 | [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills/blob/68832757cbbf941c620b71df5756cf6e5cc287b0/skills/uv/SKILL.md) |
| `credentials` | 检查服务凭据是否就绪，避免在会话中暴露密钥 | [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills/blob/68832757cbbf941c620b71df5756cf6e5cc287b0/skills/credentials/SKILL.md) |

## 选择后再核对依赖

- **dpdisp-submit**：Read the skill for runtime requirements.
- **uv**：Read the skill for runtime requirements.
- **credentials**：Read the skill for runtime requirements.

## 首批路线的能力与交接

以下为合集维护的适配说明，不是性能排名；未列出的技能仍可使用，需读取原文判断。

### dpdisp-submit

Tasks: compute-job-submission
Inputs: Prepared task, target environment and execution authorization
Outputs: submission identifier and observed status
Requires: Configured target scheduler, executable and credentials
Evidence: See referenced cases; no general task-performance claim.
