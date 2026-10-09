# 架构优化实施与验证记录

日期：2026-10-09。依据：[优化基线](optimization-baseline.md)。

## 已落实的结构

- 保留 53 项技能、原有自然语言/单项调用和 UI。上游技能正文与支持文件未改动。
- 在 `catalog.json` 中为首批路线涉及的 16 项技能增加能力、输入输出、运行前提和关系。其余技能仍可使用，未补充的字段不被当作“不可用”。
- 通用 router 更新为 0.4.0，按需读取论文阅读、VASP 输出诊断、表格分析三条内部路线。领域 router 继续拥有子任务分派；不新增用户选择步骤或全局宿主规则。
- `references/workflows.json` 保存候选技能、交接字段、停止条件和案例关联；操作说明在各路线 Markdown 中。它不是调度器或自动强制执行引擎。
- 新增 11 个公开合成案例；实际执行表格 CLI，论文与 VASP 案例仅提供验收判据。
- 增加全量静态依赖扫描、能力/关系/案例引用检查、只读上游监测与候选三方比较。CI 检查生成索引是否漂移。

## 如何维护（不增加普通用户步骤）

```text
python tools/audit_dependencies.py --output dependency-report.json
python tools/check_architecture.py
python tools/build_skill_index.py
python tools/manage.py check
python -X warn_default_encoding -W error::EncodingWarning -m unittest discover -s tests -v
```

输出报告文件须不存在，防止误覆盖。运行器在 Linux 上若名为 `python3`，相应替换命令即可。

依赖审计覆盖全部 53 项技能和 168 个 Python 文件，发现的耦合及限制见 [依赖审计](dependency-audit.md)。静态审计不执行代码，也不能证明依赖完备或环境可用。

## 上游监测与候选比较

```text
python tools/review_upstream.py --check-remote --output upstream-heads.json
python tools/review_upstream.py --skill mat-dft-vasp --candidate /path/to/AtomisticSkills --output candidate-review.json
```

Windows 将示例候选路径替换为本机路径并按需加引号。`--candidate` 接收上游仓库根目录，按来源记录定位技能子目录；不执行候选脚本、不修改当前技能，也不自动合并。

- 远端模式按仓库去重查询公开 HEAD。GitHub API 限流时，如有 Git 则使用只读 `git ls-remote` 回退；不需要配置新密钥。
- 仓库 HEAD 与固定版本不同，只能说明仓库发生变化，不能说明该技能改变、版本更好或可直接升级。失败会明确报告并返回非零状态。
- 对具有完整 `upstream_files_sha256` 的技能，候选比较区分上游变化、本地变化、相同修改、冲突与删除。
- 旧来源记录只有 `SKILL.md` 哈希时，其他文件的基线标记为未知，不推断可以安全合并。
- 打包新增文件单独保留，候选与它们发生同名碰撞时列出。候选根目录许可文件仅记录哈希，仍需人工审阅；不自动判断许可兼容性。
- 报告关联已登记的路线与案例。未关联案例不等于无需测试；外部后端、共享规则和依赖仍须检查。
- 本地候选快照的来源和 commit 未自动认证；采用前必须核对来源与版本。本轮未升级任何上游。

没有新增定时后台任务、自动发布或用户广播。监测脚本支持以后按需要接入维护自动化。

## 验证范围

表格执行检验已涵盖：已知行列数与均值、两个缺失值、畸形表格拒绝、分组重叠正反对照，以及原始文件不被修改。详见 [公开案例](../examples/README.md) 和带输入/脚本哈希的 [执行记录](../examples/evidence/2026-10-09.json)。

| 检查 | 结果 |
| --- | --- |
| Linux/WSL，Python 3.12.3，显式编码检查开启 | 40 项 unittest 全部通过 |
| Windows 原生，Python 3.13.5，cp936、UTF-8 模式关闭 | 40 项中 39 项通过；符号链接权限不足跳过 1 项，包含表格实际执行与新增维护工具测试 |
| 包装、来源与必需文件 | 53 项通过 |
| 能力、技能关系、路线与案例引用 | 16 项能力、3 条路线、11 个案例通过结构检查 |
| Router 的 skill 格式检查 | 通过；仅证明格式 |
| 插件及 ZIP 构建 | 通过；未更改界面，未部署到已安装副本 |
| AtomisticSkills 固定版本候选比较 | 7 个上游文件哈希相同，无打包文件碰撞 |
| 实际远端版本监测 | API 限流后只读 Git 回退成功，5 个上游仓库的 HEAD 均与已记录固定版本一致 |

远端观察是当日快照，见 [版本记录](../examples/evidence/upstream-heads-2026-10-09.json)，不能替代未来的检查。网络错误和不完整基线另有回归测试，工具不会把失败写成“无更新”。GitHub Actions 的新检查配置尚待本轮推送后的远端运行。

论文/VASP 合成案例不算模型行为验证或科学计算证据。单项安装与打包回归不等于运行环境完整。未验证 DSH、真实 Codex 自动路由、科学模型性能或所有上游技能。

## 下一阶段应由证据驱动

1. 在实际宿主中隔离执行公开案例，记录路由与输出；不能把模型阅读验收答案后的自评算作独立验证。
2. 对需要支持的真实 VASP 解析路径，先补足兼容后端，再使用可公开的真实输出验证；不将私人历史计算放入公共仓库。
3. 根据失败记录补充能力关系、推荐取舍或候选技能。当前没有数据支撑全局权重、自动技能改写或自动引入新项目，因此未实现这些功能。
4. 上游升级候选通过许可、依赖、差异和相关案例检查后，再使用现有安装器的冲突保护与备份机制部署。
