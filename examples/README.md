# 公开案例与验收依据

这里的输入全部为本项目编写的合成教学数据，不包含真实论文、私人计算或赝势。案例帮助复现边界条件，不代表科研基准成绩。

案例请求、允许的技能范围、预期结果及禁止误用统一记录在 [cases.json](cases.json)。允许不同的合理执行路径，不要求逐字匹配答案。模型若直接检查简单合成输入，也不应为凑技能清单加载不必要的技能。

| 路线 | 案例 | 当前证据 |
| --- | --- | --- |
| 论文阅读 | 已有全文、仅摘要、元数据冲突 | 提供合成材料和验收判据；未运行模型路由评测或在线文献检索 |
| VASP 诊断 | 声明收敛、未收敛、中断、证据不足 | 仅合成状态记录；没有伪造原始 VASP 输出，不证明真实解析器或收敛判定有效 |
| 表格检查 | 无缺失、有缺失、畸形行、分组跨数据集 | 实际运行收录的 EDA 核心 CLI；预期数值按合成输入独立列出，含正反对照 |

## 复现已经执行的表格检查

在仓库根目录，使用 Python 3.11+：

```text
python -m unittest discover -s tests -p test_workflows.py -v
```

测试调用原始 `tabular_profile.py` 与 `missingness_leakage_audit.py`，不改写上游算法，不安装第三方科学软件，不联网、不修改原始输入。Python 3.10 仍能使用安装器；这组实际 EDA 执行测试会按上游要求跳过。

独立列出的预期值：

- `clean.csv`：4 行、5 列、0 个缺失值，response 均值 1.05；按 group/split 检查时跨划分组数为 0。
- `missing.csv`：temperature_K 与 response 各缺失 1 个，response 有效值 3 个；不得静默填补。
- `malformed.csv`：存在多余字段，命令应失败，不能当作成功的完整 profile。
- `group-leakage.csv`：A、B 两组均跨 train/test，跨划分组数为 2。它是需要检查的重叠，不自动证明某个实际模型发生泄漏。

全部脚本成功不等于统计推断有效。这里的 response 未指定物理单位，不能据此作实际化学结论；上述合成案例未测试 LLM 自动选 skill、DSH、在线 API、付费服务或真实 VASP 计算；另行实施的真实问答评估见文末。

## 后续行为评测

给模型案例请求、原始输入及实际可用技能，不提供预期答案；执行完成后再按 `expected` 与 `must_not` 核验。记录模型、宿主、技能 commit、软件版本、调用记录、输出和失败。避免把预期答案置于模型执行工作区或会话上下文；仅在同一个会话中解释案例不算独立行为评测。

比较编排收益时保持工具和技能集合一致，并使用干净上下文及多次运行。没有独立评测前，`cases.json` 的 `model_execution` 保持 `not_run`。

首轮结果和限制见 [实施与验证记录](../docs/architecture-progress.md)。

## 真实模型问答案例（独立于上述合成案例）

2026-10-10 的 [Windows DSH 首轮对照](../docs/evaluations/2026-10-10-dsh/README.md)包含同一论文的 7 道问题、三组 21 份回复及独立盲审；可用于了解实际调用、质量和消耗。它不是本目录 11 个合成案例的执行记录，因此不改变 `cases.json` 中的 `model_execution` 状态，也不认证 VASP 或表格科学分析能力。

## 0.5.0 新增回归材料

合成案例现在共 14 个；前文首轮 11 个是历史范围。新增 `paper-figure-conflict`、`paper-bounded-comparison`、`paper-cutoff-cap`，使用虚构材料检查证据映射、问题范围和日期/数量约束。`model_execution` 仍为 `not_run`，不可作为新版本行为提升的证明。

运行记录检查的正反控制见 `tests/test_run_evidence.py`：模拟指令漏注入、失败/工作会话加载、未收尾与过晚返回，以及不完整日志。使用 `python -m unittest discover -s tests -p test_run_evidence.py -v` 可离线重跑；这些测试核验检查器逻辑，不生成或评判科研回答。[输入格式](../docs/maintenance/run-evidence.md)。

0.6.0 将具体证据核验清单归入 [评审参考](review-checks.md)，不再随 router 阅读路线加载。独立行为评测时，仅把题目和输入提供给回答模型，不提供这份清单及案例期望。
