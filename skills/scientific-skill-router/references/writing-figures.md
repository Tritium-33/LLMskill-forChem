# 写作与图表

区分真实数据图、概念示意图、文稿与幻灯片；外部图像服务不是真实数据绘图的必需工具。

表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。

| 技能及固定来源 | 用于什么任务 |
| --- | --- |
| [scientific-writing](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-writing/SKILL.md) | 有证据溯源的科研论文撰写与一致性检查 |
| [matplotlib](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/matplotlib/SKILL.md) | 精细控制科研图表并导出出版格式 |
| [seaborn](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/seaborn/SKILL.md) | 分布、分组比较与统计关系可视化 |
| [scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-visualization/SKILL.md) | 多面板科研图设计、单位与可读性检查 |
| [scientific-schematics](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-schematics/SKILL.md) | 通过外部图像模型生成科学示意图草稿 |
| [scientific-slides](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-slides/SKILL.md) | 科研汇报幻灯片结构、制作与视觉检查 |
| [venue-templates](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/venue-templates/SKILL.md) | 期刊会议模板选择与投稿格式检查 |
| [markitdown](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/markitdown/SKILL.md) | 将PDF、Office等文档转换为Markdown |

## 选择后再核对依赖

- **scientific-writing**：Requires Python 3.11+ only for optional dependency-free local CLIs; core guidance is platform-neutral. Bundled tools are offline and require no API keys.
- **matplotlib**：Requires Python 3.11+ and Matplotlib 3.11.2. Bundled examples also use NumPy and SciPy; pandas examples need pandas, and Jupyter widgets need ipympl. Installation needs network access; local plotting needs no credentials.
- **seaborn**：Requires Python 3.8+ with seaborn 0.13.2, NumPy, pandas, and Matplotlib; the tested current dependency stack requires Python 3.12+. Optional scipy/statsmodels for advanced regression or clustering, ipywidgets for notebook controls. Network only for installation or uncached example datasets.
- **scientific-visualization**：Requires Python 3.11+ and uv for pinned examples. Bundled CLIs are network-free and load Matplotlib, Pillow, or pypdf only when needed. Plotly static export with Kaleido v1 requires a compatible Chrome/Chromium installation.
- **scientific-schematics**：Requires Python 3.10+ with requests, network access, and an OpenRouter API key.
- **scientific-slides**：Python 3.12+; requests for OpenRouter generation, Pillow for image PDFs, PyMuPDF for rendering, pypdf and python-pptx for validation and template editing. Generation needs network and OPENROUTER_API_KEY. Beamer needs TeX Live/MiKTeX; programmatic PPTX needs Node.js and PptxGenJS; rendering PPTX for review needs LibreOffice.
- **venue-templates**：Requires Python 3.11+ for helper scripts; LaTeX and Poppler command-line tools are optional for compilation and PDF inspection. Needs network access to verify current venue instructions.
- **markitdown**：Python >=3.10,<3.15 and uv. Examples target MarkItDown 0.1.8. Core local conversion can run offline; URL, YouTube, audio transcription, LLM, Azure, and MCP workflows may use network or external services.
