# 上游依赖与架构审计（首轮）

日期：2026-10-09。范围：53 项技能、168 个 Python 文件。审计的是本仓库固定版本，未执行科学依赖安装。

## 方法与限制

运行 `python tools/audit_dependencies.py` 对所有技能做只读静态扫描，提取 Python AST 的导入候选、正文中的项目运行器/MCP 线索及已有打包说明。没有导入或执行被扫描代码。168 个文件均可被当前 Python 解析。

导入候选不是完整依赖清单：可能包含可选模块，动态导入、非 Python 脚本与纯文字要求可能遗漏。本机标准库分类随 Python 版本变化。没有发现线索不等于无外部依赖，运行状态统一为 `not_checked`。

## 人工核对的关键交接

| 范围 | 已收录 | 外部或未继承部分 | 处理 |
| --- | --- | --- | --- |
| AtomisticSkills / mat-dft-vasp | 原文、技能目录脚本和资料 | `src.utils.dft.vasp_parser` 等后端、`venv/run`、atomate2 MCP、研究规则与完整 workflow | 保留原文；在能力目录和 VASP 路线显式检查后端，缺失时报告受限或使用已验证的其他路径 |
| Computational / dft-vasp | 父 router 及 static/relax/dos/band 子目录 | VASP、赝势、调度环境；独立 taskboard 编排技能未收录 | 保留领域分派，合集只做跨任务衔接；不默默引入完整 taskboard |
| DeepMind / arXiv、OpenAlex | 技能脚本、uv 与 credentials 技能 | uv 程序、服务访问条件、密钥；安装目录不等于执行环境 | 按实际任务检查，不自动安装或创建凭据；Windows 下单独检查 Bash 示例 |
| K-Dense / EDA | 标准库核心 CLI 与可选格式脚本 | 核心声明 Python 3.11+，可选格式有更高版本及第三方依赖 | 与 Python 3.10+ 安装器要求分开；真实表格回归只运行标准库核心路径 |
| K-Dense / 其他技能 | 各自指导、支持资源和声明 | 第三方库、服务以及完整宿主集成 | 不从目录完整性推断科学任务可运行 |
| BootLoops | 本仓库四项协议/研究技能 | BootLoops 计算工具、其他未收录协议与宿主配置 | 使用已收录指导，不声称继承完整 harness 或独立验证效果 |

## 全量静态清单

完整细节可重新生成 JSON 报告；下表仅汇总文件数和发现的导入候选数，不是风险评分或可用性排名。

| 技能 | Python 文件 | 外部导入候选 | 有打包说明 | 项目耦合线索 |
| --- | ---: | ---: | --- | --- |
| `analytical-method-validation` | 8 | 0 | 否 | 静态扫描未发现 |
| `cantera` | 1 | 2 | 否 | 静态扫描未发现 |
| `datamol` | 0 | 0 | 否 | 静态扫描未发现 |
| `deepchem` | 4 | 7 | 否 | 静态扫描未发现 |
| `matchms` | 1 | 4 | 否 | 静态扫描未发现 |
| `medchem` | 1 | 5 | 否 | 静态扫描未发现 |
| `molecular-dynamics` | 0 | 0 | 否 | 静态扫描未发现 |
| `molfeat` | 0 | 0 | 否 | 静态扫描未发现 |
| `nmrglue` | 1 | 4 | 否 | 静态扫描未发现 |
| `pybamm` | 1 | 2 | 否 | 静态扫描未发现 |
| `pycalphad` | 1 | 3 | 否 | 静态扫描未发现 |
| `pymatgen` | 9 | 10 | 否 | 静态扫描未发现 |
| `pyopenms` | 17 | 5 | 否 | 静态扫描未发现 |
| `rdkit` | 4 | 2 | 否 | 静态扫描未发现 |
| `uncertainty-and-units` | 7 | 6 | 否 | 静态扫描未发现 |
| `citation-management` | 8 | 2 | 否 | 静态扫描未发现 |
| `experimental-design` | 2 | 3 | 否 | 静态扫描未发现 |
| `hypothesis-generation` | 8 | 0 | 否 | 静态扫描未发现 |
| `lit-review` | 0 | 0 | 否 | 静态扫描未发现 |
| `literature-review` | 5 | 1 | 否 | 静态扫描未发现 |
| `paper-lookup` | 5 | 0 | 否 | 静态扫描未发现 |
| `peer-review` | 8 | 0 | 否 | 静态扫描未发现 |
| `reading-contract` | 0 | 0 | 否 | 静态扫描未发现 |
| `ref-check` | 0 | 0 | 否 | 静态扫描未发现 |
| `research-lookup` | 2 | 1 | 否 | 静态扫描未发现 |
| `scholar-evaluation` | 8 | 0 | 否 | 静态扫描未发现 |
| `scientific-brainstorming` | 4 | 0 | 否 | 静态扫描未发现 |
| `scientific-critical-thinking` | 0 | 0 | 否 | 静态扫描未发现 |
| `exploratory-data-analysis` | 13 | 6 | 否 | 静态扫描未发现 |
| `independence-bookkeeping` | 0 | 0 | 否 | 静态扫描未发现 |
| `pymc` | 4 | 5 | 否 | 静态扫描未发现 |
| `pymoo` | 5 | 18 | 否 | 静态扫描未发现 |
| `scikit-learn` | 2 | 17 | 否 | 静态扫描未发现 |
| `shap` | 1 | 9 | 否 | 静态扫描未发现 |
| `statistical-analysis` | 1 | 8 | 否 | 静态扫描未发现 |
| `statistical-power` | 2 | 11 | 否 | 静态扫描未发现 |
| `statsmodels` | 0 | 0 | 否 | 静态扫描未发现 |
| `markitdown` | 3 | 1 | 否 | Mentions MCP; connection/tool availability needs task-specific inspection. |
| `scientific-schematics` | 2 | 1 | 否 | 静态扫描未发现 |
| `scientific-slides` | 7 | 6 | 否 | 静态扫描未发现 |
| `scientific-visualization` | 8 | 4 | 否 | 静态扫描未发现 |
| `scientific-writing` | 9 | 0 | 否 | 静态扫描未发现 |
| `seaborn` | 0 | 0 | 否 | 静态扫描未发现 |
| `scientific-skill-router` | 0 | 0 | 否 | 静态扫描未发现 |
| `mat-dft-vasp` | 2 | 6 | 是 | References upstream venv/run; not provided by the skill installer.; Imports project-level src backend outside this skill directory.; Mentions MCP; connection/tool availability needs task-specific inspection. |
| `dft-vasp` | 0 | 0 | 是 | 静态扫描未发现 |
| `dft-qe` | 0 | 0 | 是 | 静态扫描未发现 |
| `dpdata-cli` | 0 | 0 | 是 | 静态扫描未发现 |
| `dpdisp-submit` | 0 | 0 | 是 | 静态扫描未发现 |
| `literature-search-arxiv` | 3 | 1 | 是 | 静态扫描未发现 |
| `literature-search-openalex` | 1 | 2 | 是 | 静态扫描未发现 |
| `uv` | 0 | 0 | 是 | 静态扫描未发现 |
| `credentials` | 0 | 0 | 是 | 静态扫描未发现 |

## 后续验收

- 原文中提及的科学 API 与参数需在具体任务中核验；本轮没有重写或背书这些示例。
- 三条内部路线优先填补交接与验收缺口；未新建运行环境或计算引擎。
- 单项技能仍可独立安装；独立安装不自动获得其他 skill、MCP 或上游根目录资源。
