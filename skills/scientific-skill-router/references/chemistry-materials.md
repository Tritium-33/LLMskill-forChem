# 化学与材料

输入通常为结构、分子、光谱、热力学数据库或动力学机制；根据科学对象选择，不把分子工具套用于周期晶体。

表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。

| 技能 | 用于什么任务 | 来源 |
| --- | --- | --- |
| `analytical-method-validation` | 分析方法的准确度、精密度与检出限验证 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/analytical-method-validation/SKILL.md) |
| `cantera` | 化学反应动力学、反应器与点火延迟 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/cantera/SKILL.md) |
| `datamol` | 常用分子标准化、描述符和构象处理 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/datamol/SKILL.md) |
| `deepchem` | 分子性质预测、特征化与化学机器学习 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/deepchem/SKILL.md) |
| `matchms` | 串联质谱清理、相似度与谱库匹配 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/matchms/SKILL.md) |
| `medchem` | 药物化学结构警示与分子库筛选 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/medchem/SKILL.md) |
| `molecular-dynamics` | OpenMM分子动力学与轨迹分析 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/molecular-dynamics/SKILL.md) |
| `molfeat` | 分子指纹、描述符与预训练分子表征 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/molfeat/SKILL.md) |
| `nmrglue` | 一维核磁原始数据处理、谱峰与积分 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/nmrglue/SKILL.md) |
| `pybamm` | 电池充放电建模与参数敏感性分析 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pybamm/SKILL.md) |
| `pycalphad` | 基于热力学数据库的相平衡计算 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pycalphad/SKILL.md) |
| `pymatgen` | 晶体结构、材料数据与电子结构文件分析 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymatgen/SKILL.md) |
| `pyopenms` | 液相色谱质谱数据处理与特征检测 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pyopenms/SKILL.md) |
| `rdkit` | 分子结构、描述符、指纹与子结构检索 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/rdkit/SKILL.md) |
| `uncertainty-and-units` | 物理单位检查、误差传播与不确定度预算 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/uncertainty-and-units/SKILL.md) |
| `mat-dft-vasp` | VASP 输入准备与结果提取；需另配上游运行环境 | [learningmatter-mit/AtomisticSkills](https://github.com/learningmatter-mit/AtomisticSkills/blob/62574443f2a772e23dd5951f3712b65133b06715/skills/mat-dft-vasp/SKILL.md) |
| `dft-vasp` | 准备 VASP 静态、优化、DOS 与能带输入，不自动提交 | [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/5c19e75b256d49849574c999b1965d94024ee072/quantum-chemistry/dft-vasp/SKILL.md) |
| `dft-qe` | 根据结构与指定参数准备 Quantum ESPRESSO 输入 | [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/5c19e75b256d49849574c999b1965d94024ee072/quantum-chemistry/dft-qe/SKILL.md) |
| `dpdata-cli` | 原子结构和计算数据格式转换 | [jinzhezenggroup/computational-chemistry-agent-skills](https://github.com/jinzhezenggroup/computational-chemistry-agent-skills/blob/5c19e75b256d49849574c999b1965d94024ee072/tools/dpdata-cli/SKILL.md) |

## 选择后再核对依赖

- **analytical-method-validation**：Requires Python 3.11+. Scripts use only the standard library - no numpy, scipy, or network access. Statistical distributions are computed from first principles so results are reproducible in any conforming interpreter.
- **cantera**：Requires Python 3.12-3.14, Cantera 3.2.0, and NumPy. Installation needs network access; simulations run locally without credentials. Custom mechanisms must be available as Cantera YAML files.
- **datamol**：Requires Python 3.11+ and datamol 0.13.0 with RDKit 2024.09+. Installation needs network access; local molecular workflows need no credentials. Remote I/O needs the selected provider credentials.
- **deepchem**：Requires Python 3.11 for the tested DeepChem 2.8.0 stack. Molecular workflows need RDKit. Torch, Transformers, torch-geometric or DGL/DGL-LifeSci depend on the chosen model. Network is needed only for package, benchmark or model downloads.
- **matchms**：Requires Python >=3.10,<3.15, uv, and matchms 0.33.1. Local file workflows need no credentials; metabolomics-USI loading requires network access.
- **medchem**：Requires Python 3.11+ with medchem, datamol, and RDKit. Optional Lilly demerits require native tools built with medchem install-lilly, a C++ compiler, make, zlib, and Ruby; installation needs network access. Other filters run locally without credentials.
- **molecular-dynamics**：Requires Python 3.11+ with OpenMM and MDAnalysis; matplotlib for plots. Optional PDBFixer and OpenFF need separate installation. Network access for installation; local simulation and analysis run offline.
- **molfeat**：Requires Python 3.11+ and molfeat 1.0.0 (RDKit, datamol, PyTorch). macOS Intel needs Python 3.11–3.12 and upstream platform-specific dependency pins. Optional extras and network access are needed for pretrained models; core fingerprints run offline.
- **nmrglue**：Requires Python 3.12+, nmrglue, NumPy 2+, and SciPy. Installation needs network access; processing is local and needs no credentials.
- **pybamm**：Requires Python 3.12 with PyBaMM 26.9.0.0 and pybammsolvers 0.10.0 (IDAKLU). NumPy and CasADi are supplied by PyBaMM. Network is needed for installation and optional upstream dataset retrieval; bundled simulations and CSV comparisons run locally without credentials.
- **pycalphad**：Requires Python 3.12+, pycalphad 0.11.2, and NumPy. Installation needs network access; calculations run locally without credentials. Real-material predictions require a suitable licensed thermodynamic database.
- **pymatgen**：Python 3.11+ with uv. The verified snapshot uses pymatgen 2026.9.24, pymatgen-core 2026.9.23, and mp-api 0.46.5. Bundled help and planning CLIs use only the standard library; local scientific execution lazily requires the pinned pymatgen packages. Materials Project access additionally requires explicit network approval and the single named secret MP_API_KEY.
- **pyopenms**：Requires CPython 3.11+ and pyOpenMS 3.6.0; pandas and NumPy for tables, Matplotlib for plots. Wheels support macOS 15+ arm64, Linux glibc 2.34+ x86-64/arm64, and Windows x86-64. Search-engine executables are separate.
- **rdkit**：Tested with RDKit 2026.03.6 on Python 3.13; bundled scripts require the rdkit package. No credentials or network are needed after installation. Use conda-forge for the broadest binary support or PyPI package `rdkit` for supported platform wheels; `rdkit-pypi` is the legacy PyPI name.
- **uncertainty-and-units**：Requires Python 3.12+. The numeric CLIs need pint, uncertainties, NumPy, and SciPy; the static auditor is standard-library only. All bundled tooling runs locally with no network access.
- **mat-dft-vasp**：Read the skill for runtime requirements.
- **dft-vasp**：Requires a user-provided structure and valid VASP pseudopotential resources/license in the target environment.
- **dft-qe**：Requires a user-provided initial structure and enough DFT parameters to build a scientifically meaningful QE input.
- **dpdata-cli**：Requires uvx (uv) for running dpdata

## 首批路线的能力与交接

以下为合集维护的适配说明，不是性能排名；未列出的技能仍可使用，需读取原文判断。

### pymatgen

Tasks: materials-structure-analysis, vasp-output-inspection
Inputs: Structures or supported materials output files
Outputs: analysis with units, parser version and limitations
Requires: Compatible pymatgen environment; remote services only when requested
Evidence: See referenced cases; no general task-performance claim.

### mat-dft-vasp

Tasks: vasp-input-preparation, vasp-output-extraction
Inputs: Structures/settings or VASP output directory
Outputs: prepared inputs or parsed results; convergence needs separate checking
Requires: AtomisticSkills src/ backend and compatible environment are external; Upstream venv/run and atomate2 MCP are not bundled; VASP/pseudopotentials and scheduler configuration when executing
alternatives: dft-vasp
Evidence: See referenced cases; no general task-performance claim.

### dft-vasp

Tasks: vasp-input-preparation
Inputs: Structure or prerequisite SCF artifacts and explicit method constraints
Outputs: task-specific inputs and unresolved choices
Requires: Task-specific VASP prerequisites; pseudopotentials supplied separately
feeds_into: dpdisp-submit
alternatives: mat-dft-vasp
delegates_to: dft-vasp/static, dft-vasp/relax, dft-vasp/dos, dft-vasp/band
Evidence: See referenced cases; no general task-performance claim.
