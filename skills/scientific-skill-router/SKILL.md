---
name: scientific-skill-router
description: 按科研任务选择已收录的化学、材料、文献、统计、写作和绘图技能。用于用户要求自动选技能、询问该用哪个技能，或任务需要跨板块组合时；任务已明确对应单个技能时直接使用该技能。
---

# Scientific skill router

本技能只负责选择与串联，不代替领域技能，不启动子代理。

## 按任务读取一个板块

| 用户希望得到什么 | 读取索引 |
| --- | --- |
| 分子/晶体处理，光谱分析，化学动力学、相平衡、电池或单位误差计算 | [chemistry-materials](references/chemistry-materials.md) |
| 找论文、核对引用、梳理证据、形成假设、设计实验或评阅稿件 | [research-evidence](references/research-evidence.md) |
| 检查数据、统计推断、建立预测模型、解释模型或做优化 | [data-modeling](references/data-modeling.md) |
| 写论文、制作数据图/示意图/幻灯片、匹配格式或转换文档 | [writing-figures](references/writing-figures.md) |

这些索引覆盖此分发包选择的42项 K-Dense 技能，并非上游全部技能。只在下一步确实跨板块时再读第二个索引；不要为简单任务加载所有索引或所有 SKILL.md。

## 选择和执行

1. 优先尊重用户指定的技能、工具与任务范围。从目标交付物、输入格式和方法需求选主要技能，只有实际需要时才加入辅助技能。证据核验不等于每次启动全面文献审查。
2. 检查当前会话的可用技能列表，再读取选中技能的真实 `SKILL.md`。索引表表示本分发包有该技能，不保证用户安装了全部技能。用会话给出的路径；缺失时可检查本分发包同级 `../<name>/SKILL.md`，仍不存在就说明缺失并用已有能力继续，不假装已经调用。
3. 按所选 SKILL.md 执行；宿主没有通用的“调用技能”API时，读取指导并执行其步骤即可。不要凭记忆重写技能，也不要把技能再路由回本入口。
4. 在实际运行脚本前核对软件版本、输入数据、凭据和服务可用性。需要的依赖未就绪时标明限制，优先采用能完成目标的现有本地路径；不能把认证/付费服务的缺失伪装成已检索或已生成。
5. 简短告知“本次使用 X 处理 Y”；然后完成任务，说明结果与未验证项。选择或读取技能并不证明其脚本已成功运行。组合任务按数据依赖顺序串联，不把所有领域的检查堆到每次任务中。

## 容易混淆的入口

- 找具体论文/DOI先看 `paper-lookup`；生成书目用 `citation-management`；需要系统筛选综合才用 `literature-review`。既有 `lit-review`、`ref-check` 可用于更严格的创新性与参考文献审查，仅在当前可用且任务需要时组合。
- 通用分子处理选 `datamol`，精细分子操作选 `rdkit`；周期性材料结构选 `pymatgen`。`molecular-dynamics` 面向 OpenMM 生物分子/小分子，不自动等同周期性材料 AIMD。
- VASP 输入、提交或报错任务不能仅凭 `pymatgen` 当作完整工作流。若当前环境已有 `mat-dft-vasp`，读取其本地适配说明和项目约束；该技能不属于本42项索引，也不保证在其他用户环境中存在。
- 数据探索 → `exploratory-data-analysis`；选择统计检验 → `statistical-analysis`；样本量 → `statistical-power`；预测模型 → `scikit-learn`。只有任务明确需要时才扩展到 PyMC/SHAP/多目标优化。
- 真实数据图选 `matplotlib`、`seaborn` 或 `scientific-visualization`；概念示意图才考虑 `scientific-schematics`。后者的外部图像服务不是数据绘图的必需依赖。

## 维护

索引由仓库 `catalog.json` 中的板块信息及各技能的来源/依赖元数据生成；在仓库运行 `python tools/build_skill_index.py`。上游正文不合并、不删除，英文技能名称不改。索引更新后重新部署本技能。原始来源与运行限制保留在各板块中。
