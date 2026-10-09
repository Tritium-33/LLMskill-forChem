# 写作与图表

区分真实数据图、概念示意图、文稿与幻灯片；外部图像服务不是真实数据绘图的必需工具。

表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。

| 技能 | 用于什么任务 | 来源 |
| --- | --- | --- |
| `markitdown` | 将PDF、Office等文档转换为Markdown | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/markitdown/SKILL.md) |
| `scientific-schematics` | 通过外部图像模型生成科学示意图草稿 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-schematics/SKILL.md) |
| `scientific-slides` | 科研汇报幻灯片结构、制作与视觉检查 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-slides/SKILL.md) |
| `scientific-visualization` | 多面板科研图设计、单位与可读性检查 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-visualization/SKILL.md) |
| `scientific-writing` | 有证据溯源的科研论文撰写与一致性检查 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/scientific-writing/SKILL.md) |
| `seaborn` | 分布、分组比较与统计关系可视化 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/blob/92ace75ac21efe19a620434e0ca4e356081fe807/skills/seaborn/SKILL.md) |

## 选择后再核对依赖

- **markitdown**：Python >=3.10,<3.15 and uv. Examples target MarkItDown 0.1.8. Core local conversion can run offline; URL, YouTube, audio transcription, LLM, Azure, and MCP workflows may use network or external services.
- **scientific-schematics**：Requires Python 3.10+ with requests, network access, and an OpenRouter API key.
- **scientific-slides**：Python 3.12+; requests for OpenRouter generation, Pillow for image PDFs, PyMuPDF for rendering, pypdf and python-pptx for validation and template editing. Generation needs network and OPENROUTER_API_KEY. Beamer needs TeX Live/MiKTeX; programmatic PPTX needs Node.js and PptxGenJS; rendering PPTX for review needs LibreOffice.
- **scientific-visualization**：Requires Python 3.11+ and uv for pinned examples. Bundled CLIs are network-free and load Matplotlib, Pillow, or pypdf only when needed. Plotly static export with Kaleido v1 requires a compatible Chrome/Chromium installation.
- **scientific-writing**：Requires Python 3.11+ only for optional dependency-free local CLIs; core guidance is platform-neutral. Bundled tools are offline and require no API keys.
- **seaborn**：Requires Python 3.8+ with seaborn 0.13.2, NumPy, pandas, and Matplotlib; the tested current dependency stack requires Python 3.12+. Optional scipy/statsmodels for advanced regression or clustering, ipywidgets for notebook controls. Network only for installation or uncached example datasets.
