# 逐项许可审查（2026-10-09）

审查范围：本仓库原有 48 项技能及其随附脚本、参考资料、模板和数据。下载 SOURCE.json 固定提交的上游归档进行文件比对，检查许可证、文件头、上游 README 许可范围、署名和修改记录。此记录是分发依据审查，不保证上游拥有所有内容的权利，也不替代法律意见。

## 结果

保留 44 项：K-Dense 39 项（MIT 28、Apache-2.0 6、BSD-3-Clause 5），BootLoops 4 项，原有本地 router 1 项。暂停 4 项；索引与新构建不再包含其正文。Apache/BSD 不是禁止再分发的许可证；本次补齐它们的文本和通知，而不是将它们改成 MIT。

## 暂停项目

| 技能 | 原因 | 恢复条件 |
| --- | --- | --- |
| `research-direction-recovery` | project-local 的授权范围未明确；根目录许可仅称主体代码 Apache-2.0。 | 固定并核清适用许可、署名和分发条件后重新审查 |
| `matplotlib` | 技能许可指向软件项目的可变目录，尚未固定适用于本技能的完整许可及署名集合。 | 固定并核清适用许可、署名和分发条件后重新审查 |
| `sympy` | 技能许可指向软件项目的可变文件，尚未固定适用于本技能的完整许可及署名集合。 | 固定并核清适用许可、署名和分发条件后重新审查 |
| `venue-templates` | 附带 Elsevier 的 LPPL 文件，但当前包未附完整许可与其所述 manifest；暂停整项分发，避免残缺模板。 | 固定并核清适用许可、署名和分发条件后重新审查 |

## 所有原收录项的处理

| 技能 | 上游声明 | 处理 |
| --- | --- | --- |
| `analytical-method-validation` | MIT | 保留 |
| `cantera` | MIT | 保留 |
| `citation-management` | MIT | 保留 |
| `datamol` | Apache-2.0 | 保留 |
| `deepchem` | MIT | 保留 |
| `experimental-design` | MIT | 保留 |
| `exploratory-data-analysis` | MIT | 保留 |
| `hypothesis-generation` | MIT | 保留 |
| `independence-bookkeeping` | CC-BY-4.0 prose; MIT code/manifests | 保留 |
| `lit-review` | CC-BY-4.0 prose; MIT code/manifests | 保留 |
| `literature-review` | MIT | 保留 |
| `markitdown` | MIT | 保留 |
| `matchms` | Apache-2.0 | 保留 |
| `matplotlib` | https://github.com/matplotlib/matplotlib/tree/main/LICENSE | 暂停分发 |
| `medchem` | Apache-2.0 | 保留 |
| `molecular-dynamics` | MIT | 保留 |
| `molfeat` | Apache-2.0 | 保留 |
| `nmrglue` | MIT | 保留 |
| `paper-lookup` | MIT | 保留 |
| `peer-review` | MIT | 保留 |
| `pybamm` | MIT | 保留 |
| `pycalphad` | MIT | 保留 |
| `pymatgen` | MIT | 保留 |
| `pymc` | Apache-2.0 | 保留 |
| `pymoo` | Apache-2.0 | 保留 |
| `pyopenms` | BSD-3-Clause | 保留 |
| `rdkit` | BSD-3-Clause | 保留 |
| `reading-contract` | CC-BY-4.0 prose; MIT code/manifests | 保留 |
| `ref-check` | CC-BY-4.0 prose; MIT code/manifests | 保留 |
| `research-direction-recovery` | project-local | 暂停分发 |
| `research-lookup` | MIT | 保留 |
| `scholar-evaluation` | MIT | 保留 |
| `scientific-brainstorming` | MIT | 保留 |
| `scientific-critical-thinking` | MIT | 保留 |
| `scientific-schematics` | MIT | 保留 |
| `scientific-skill-router` | MIT original additions | 保留 |
| `scientific-slides` | MIT | 保留 |
| `scientific-visualization` | MIT | 保留 |
| `scientific-writing` | MIT | 保留 |
| `scikit-learn` | BSD-3-Clause | 保留 |
| `seaborn` | BSD-3-Clause | 保留 |
| `shap` | MIT | 保留 |
| `statistical-analysis` | MIT | 保留 |
| `statistical-power` | MIT | 保留 |
| `statsmodels` | BSD-3-Clause | 保留 |
| `sympy` | https://github.com/sympy/sympy/blob/master/LICENSE | 暂停分发 |
| `uncertainty-and-units` | MIT | 保留 |
| `venue-templates` | MIT license | 暂停分发 |

## 依据与边界

- K-Dense 固定版本 [README](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/README.md#-license) 明确要求以各技能 license 字段为准。此前把这些字段统一解释为依赖软件许可证，依据不足，已纠正。
- 42 项 K-Dense 原收录内容与固定上游版本逐文件一致；BootLoops 仅 ref-check 正文有已记录的修改。来源比对不能证明上游原创性。
- BootLoops 保留原始 NOTICE、MIT 与 CC BY 4.0 声明；未改变正文许可，不暗示背书。
- [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)、[BSD-3-Clause](https://opensource.org/license/bsd-3-clause)、[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 和 [LPPL](https://www.latex-project.org/lppl/lppl-1-3c/) 按各自条款处理。
- `analytical-method-validation` 的 ICH 改编资料保留来源和非背书说明；已核对 [Q2(R2)](https://database.ich.org/sites/default/files/ICH_Q2%28R2%29_Guideline_2023_1130.pdf)、[Q14](https://database.ich.org/sites/default/files/ICH_Q14_Guideline_2023_1116.pdf)、[M10](https://database.ich.org/sites/default/files/M10_Guideline_Step4_2022_0524.pdf) 第二页允许署名再使用及改编的法律声明；PDF 全文不随包分发。
- 不分发外部科学软件、POTCAR、论文全文或商业标准；本次对文件类型及声明的检查不能代替后续新增资料的逐项审查。
- Git 旧提交仍可能含已撤回内容；从当前分支删除不等于清理历史、旧 release、fork 或他人已有副本。本次不进行强制推送或历史重写。
- 逐项来源、比较结果及整改前文件 SHA-256 见 [机器可读记录](inventory-2026-10-09.json)。

## 后续收录规则

固定上游版本；读取根许可和单项覆盖声明；检查模板、数据等附带材料；保留版权、许可与修改说明。遇到未解释的自定义许可或无法确定适用范围的链接，先只提供上游链接，不收录正文。

## 2026-10-09 新增批次

另加入三个项目的 9 项顶层技能，总数为 53。新增批次的固定提交、上游路径、许可和逐文件哈希见 [新增清单](additions-2026-10-09.json)；运行限制见 [接入说明](../imported-skills.md)。上方原始审计快照保留为历史记录，不代表已覆盖新增文件。新增源文件保持原字节，独立添加来源、界面与许可附件。Computational Chemistry 的 LGPL 附上其引用的 GPL v3 全文；DeepMind 区分软件 Apache 2.0 与其他材料 CC BY 4.0。
