# 化学与材料

输入通常为结构、分子、光谱、热力学数据库或动力学机制；根据科学对象选择，不把分子工具套用于周期晶体。

表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。

| 技能及固定来源 | 用于什么任务 |
| --- | --- |
| [pymatgen](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymatgen/SKILL.md) | 晶体结构、材料数据与电子结构文件分析 |
| [rdkit](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/rdkit/SKILL.md) | 分子结构、描述符、指纹与子结构检索 |
| [datamol](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/datamol/SKILL.md) | 常用分子标准化、描述符和构象处理 |
| [deepchem](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/deepchem/SKILL.md) | 分子性质预测、特征化与化学机器学习 |
| [molfeat](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/molfeat/SKILL.md) | 分子指纹、描述符与预训练分子表征 |
| [medchem](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/medchem/SKILL.md) | 药物化学结构警示与分子库筛选 |
| [molecular-dynamics](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/molecular-dynamics/SKILL.md) | OpenMM分子动力学与轨迹分析 |
| [cantera](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/cantera/SKILL.md) | 化学反应动力学、反应器与点火延迟 |
| [pycalphad](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pycalphad/SKILL.md) | 基于热力学数据库的相平衡计算 |
| [pybamm](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pybamm/SKILL.md) | 电池充放电建模与参数敏感性分析 |
| [nmrglue](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/nmrglue/SKILL.md) | 一维核磁原始数据处理、谱峰与积分 |
| [matchms](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/matchms/SKILL.md) | 串联质谱清理、相似度与谱库匹配 |
| [pyopenms](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pyopenms/SKILL.md) | 液相色谱质谱数据处理与特征检测 |
| [analytical-method-validation](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/analytical-method-validation/SKILL.md) | 分析方法的准确度、精密度与检出限验证 |
| [uncertainty-and-units](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/uncertainty-and-units/SKILL.md) | 物理单位检查、误差传播与不确定度预算 |

## 选择后再核对依赖

- **pymatgen**：Python 3.11+ with uv. The verified snapshot uses pymatgen 2026.9.24, pymatgen-core 2026.9.23, and mp-api 0.46.5. Bundled help and planning CLIs use only the standard library; local scientific execution lazily requires the pinned pymatgen packages. Materials Project access additionally requires explicit network approval and the single named secret MP_API_KEY.
- **rdkit**：Tested with RDKit 2026.03.6 on Python 3.13; bundled scripts require the rdkit package. No credentials or network are needed after installation. Use conda-forge for the broadest binary support or PyPI package `rdkit` for supported platform wheels; `rdkit-pypi` is the legacy PyPI name.
- **datamol**：Requires Python 3.11+ and datamol 0.13.0 with RDKit 2024.09+. Installation needs network access; local molecular workflows need no credentials. Remote I/O needs the selected provider credentials.
- **deepchem**：Requires Python 3.11 for the tested DeepChem 2.8.0 stack. Molecular workflows need RDKit. Torch, Transformers, torch-geometric or DGL/DGL-LifeSci depend on the chosen model. Network is needed only for package, benchmark or model downloads.
- **molfeat**：Requires Python 3.11+ and molfeat 1.0.0 (RDKit, datamol, PyTorch). macOS Intel needs Python 3.11–3.12 and upstream platform-specific dependency pins. Optional extras and network access are needed for pretrained models; core fingerprints run offline.
- **medchem**：Requires Python 3.11+ with medchem, datamol, and RDKit. Optional Lilly demerits require native tools built with medchem install-lilly, a C++ compiler, make, zlib, and Ruby; installation needs network access. Other filters run locally without credentials.
- **molecular-dynamics**：Requires Python 3.11+ with OpenMM and MDAnalysis; matplotlib for plots. Optional PDBFixer and OpenFF need separate installation. Network access for installation; local simulation and analysis run offline.
- **cantera**：Requires Python 3.12-3.14, Cantera 3.2.0, and NumPy. Installation needs network access; simulations run locally without credentials. Custom mechanisms must be available as Cantera YAML files.
- **pycalphad**：Requires Python 3.12+, pycalphad 0.11.2, and NumPy. Installation needs network access; calculations run locally without credentials. Real-material predictions require a suitable licensed thermodynamic database.
- **pybamm**：Requires Python 3.12 with PyBaMM 26.9.0.0 and pybammsolvers 0.10.0 (IDAKLU). NumPy and CasADi are supplied by PyBaMM. Network is needed for installation and optional upstream dataset retrieval; bundled simulations and CSV comparisons run locally without credentials.
- **nmrglue**：Requires Python 3.12+, nmrglue, NumPy 2+, and SciPy. Installation needs network access; processing is local and needs no credentials.
- **matchms**：Requires Python >=3.10,<3.15, uv, and matchms 0.33.1. Local file workflows need no credentials; metabolomics-USI loading requires network access.
- **pyopenms**：Requires CPython 3.11+ and pyOpenMS 3.6.0; pandas and NumPy for tables, Matplotlib for plots. Wheels support macOS 15+ arm64, Linux glibc 2.34+ x86-64/arm64, and Windows x86-64. Search-engine executables are separate.
- **analytical-method-validation**：Requires Python 3.11+. Scripts use only the standard library - no numpy, scipy, or network access. Statistical distributions are computed from first principles so results are reproducible in any conforming interpreter.
- **uncertainty-and-units**：Requires Python 3.12+. The numeric CLIs need pint, uncertainties, NumPy, and SciPy; the static auditor is standard-library only. All bundled tooling runs locally with no network access.
