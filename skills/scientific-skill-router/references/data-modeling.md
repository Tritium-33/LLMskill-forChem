# 数据、统计与机器学习

先明确解释、推断、预测还是优化目标；若任务只需基础统计，不强制建立机器学习模型。

表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。

| 技能及固定来源 | 用于什么任务 |
| --- | --- |
| [exploratory-data-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/exploratory-data-analysis/SKILL.md) | 科学数据的结构、缺失值和异常值探索 |
| [statistical-analysis](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-analysis/SKILL.md) | 统计检验选择、假设检查与效应量报告 |
| [statistical-power](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statistical-power/SKILL.md) | 样本量、重复数和统计功效规划 |
| [statsmodels](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/statsmodels/SKILL.md) | 回归、广义线性模型和时间序列诊断 |
| [scikit-learn](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scikit-learn/SKILL.md) | 机器学习预处理、建模与交叉验证 |
| [pymc](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymc/SKILL.md) | 贝叶斯建模、后验检查与不确定度推断 |
| [pymoo](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/pymoo/SKILL.md) | 多目标优化、约束与帕累托解分析 |
| [shap](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/shap/SKILL.md) | 模型预测的特征归因、解释与诊断 |
| [sympy](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/sympy/SKILL.md) | 符号代数、微积分与精确公式推导 |

## 选择后再核对依赖

- **exploratory-data-analysis**：Bundled core CLIs require Python 3.11+ and are local/network-free; the complete pinned optional snapshot requires Python 3.12+, uv, and format-specific libraries listed below.
- **statistical-analysis**：Requires Python 3.12+ and the documented isolated scientific Python environment; network access only for installation and documentation.
- **statistical-power**：Requires Python >=3.12 with statsmodels, scipy, numpy, pandas, and matplotlib. Optional comparison uses pingouin; survival extensions use lifelines (requires pandas<3). Installation needs network access unless packages are cached. Calculations run locally without credentials.
- **statsmodels**：Requires Python 3.10+ and statsmodels 0.15.0; the tested NumPy 2.5.3/SciPy 1.18.1 stack needs Python 3.12+. Plotting needs matplotlib; predictive metrics need scikit-learn. Network access is needed only for installation or documentation; no credentials.
- **scikit-learn**：Requires Python 3.11+ and scikit-learn 1.9.1. NumPy, SciPy, and joblib are dependencies; bundled scripts also require pandas and matplotlib. Installation needs network access; bundled examples use local datasets without credentials.
- **pymc**：Requires Python 3.12+ with PyMC 6.3.2, PyTensor 3.3.2 and ArviZ 1.3-compatible dependencies; NumPy, pandas, Matplotlib, h5netcdf and h5py for bundled helpers/artifacts. Network access for installation only. Optional nutpie, NumPyro and BlackJAX samplers need separate dependencies.
- **pymoo**：Requires Python 3.10+ and pymoo 0.6.2 with its NumPy, SciPy, matplotlib and autograd dependencies. Optional joblib for parallel runners, optuna for its algorithm wrapper, and dill for checkpoints. Network needed for installation only.
- **shap**：Requires Python 3.12+ and uv for SHAP 0.52.0; model-specific libraries are optional.
- **sympy**：Requires Python 3.9+ and SymPy 1.14.0. Optional NumPy/SciPy/Matplotlib, IPython/ipywidgets, or ANTLR 4.11 parser runtime for relevant examples. Compiled wrappers need a C/Fortran compiler and backend packages; emitting source needs no compiler. Network only for installation/docs.
