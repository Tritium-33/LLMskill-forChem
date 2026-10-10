# 维护与评估设施

普通使用只需要技能、选择指导和安装工具。这里的设施服务于维护与评估，不随 router 加载，不要求使用者准备日志或填写运行记录。

| 维护目标 | 入口 |
| --- | --- |
| 修改用途和选择说明 | 仓库 `catalog.json`：中文 `summary` 与英文 `routing_hint`；来源继续以各技能 `SOURCE.json` 为准 |
| 生成中文目录和简短英文模型索引 | `python tools/build_skill_index.py`；选中后的依赖说明留在技能正文、PACKAGING 及完整目录 |
| 检查安装、来源与路线引用 | `python tools/manage.py check`、`python tools/check_architecture.py` |
| 检查上游版本与候选差异 | `python tools/review_upstream.py`；见[已有实施记录](../architecture-progress.md#上游监测与候选比较) |
| 核验实验中的实载指令与委派记录 | `python tools/maintenance/check_run_evidence.py`；见[输入格式](run-evidence.md)，不自动连接 DSH |
| 查看真实问答证据 | [首轮 DSH 对照](../evaluations/2026-10-10-dsh/README.md)；与程序测试分开解读 |

`references/index.json` 保留完整生成数据供工具按需读取；普通 router 选择无需读它。`workflows.json` 保留路线与案例关联供维护检查，不作为通用执行引擎。已有能力描述暂保留，不要求给所有技能补齐抽象字段。

维护验证：

```text
python tools/build_skill_index.py
python tools/manage.py check
python tools/check_architecture.py
python -X warn_default_encoding -W error::EncodingWarning -m unittest discover -s tests -v
```

评估检查器不认证科学质量。默认不自动升级上游、不自动改写技能、不创建新 agent 框架。新增设施应指出它替实际使用者或重复维护工作节省了哪一步，并提供相应证据。
