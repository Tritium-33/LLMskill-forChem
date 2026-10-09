# 化学科研技能面板：Windows Codex 插件原型

版本 0.1.0（简化版）。面板仅包含五项技能的原始英文名称、中文用途、来源链接、搜索和逐项按钮。**选择技能 → 插入当前输入框 → 在对话里补充任务并发送**。没有任务表单、示例填充或指令预览。

界面只帮助选择方法；实际研究由 Codex 及其可用工具完成。无需额外模型 API Key，插件没有外部服务账户、云端存储或遥测。材料请在对话附上。调研候选、个人课题和每日广播没有加入插件。

## 官方依据与支持边界

核查日期：2026-10-08。

- [OpenAI 插件打包文档](https://developers.openai.com/plugins/build/plugins)：支持技能、MCP、个人 marketplace；本原型采用官方 Plugin Creator 生成的 `.codex-plugin/plugin.json` 兼容格式。
- [OpenAI MCP UI 指南](https://developers.openai.com/plugins/build/chatgpt-ui)：使用 `_meta.ui.resourceUri`、`text/html;profile=mcp-app` 及 `ui/*` 通信；工具需在无 UI 时也可用。
- [官方 UI quickstart](https://developers.openai.com/plugins/build/app-quickstart)：界面初始化和工具调用通过 MCP Apps 的 `postMessage` JSON-RPC；前端不需要 React 或 Node 构建。
- [OpenAI MCP 扩展规范](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md)：`openai/modelContext` 将 `ui/update-model-context` 内容显示为可移除的输入框附件；`mentions/search` 提供桌面原生选择菜单。
- [插件使用说明](https://learn.chatgpt.com/docs/plugins)：安装后在新对话使用。

插入按钮要求宿主同时声明 `updateModelContext.text` 与 `experimental["openai/modelContext"]`。点击后传入带中文标题的技能引用，作为可移除附件；再次选择替换本面板此前的附件。不会调用发送消息接口。仅支持普通 MCP Apps 上下文、仅支持消息发送或普通浏览器时，都显示“复制”。复制失败则选中文本供 Ctrl+C 使用。

官方文档将 Composer mentions 标为桌面功能；本插件提供该入口，尚未保证所有 Windows Codex 版本可用。安装成功与模拟宿主测试不等于真实客户端已经通过验证。

## Windows 原生安装

需要 Python 3.10+（含 pip、venv），首次安装需联网下载 `mcp==1.30.0` 及其依赖。在仓库根目录的 PowerShell 中：

```powershell
py -3 tools/build_plugin.py --zip
py -3 dist/chem-skill-panel/install.py --dry-run
py -3 dist/chem-skill-panel/install.py
```

如果拿到的是插件 ZIP，解压后进入 `chem-skill-panel` 文件夹，执行 `py -3 install.py --dry-run`，检查路径后执行 `py -3 install.py`。

也可以双击 `Open-panel.cmd` 先看面板；已有 Python 的 Windows 用户可双击 `Install-plugin.cmd` 首次安装。安装过程结束时窗口会保留输出，便于检查错误。

若 `py -3 --version` 低于 3.10，而 `python --version` 或已有 Conda 环境满足要求，可将上述 `py -3` 换为该解释器。双击安装入口会依次检查 `py -3` 和 `python`，选择满足版本要求的命令。

安装脚本会建立当前 Windows 用户目录下的 `plugins/chem-skill-panel`、隔离 Python 环境 `plugins/.chem-skill-panel-runtime`，并在 `.agents/plugins/marketplace.json` 追加个人插件入口，保留其他插件和 marketplace 名称。遇到同名目录/入口会停止，不静默覆盖。MCP 启动命令在本机安装时生成，使用该环境的 Python 与绝对路径，不依赖 WSL 或 Bash。

打开或刷新 Codex 的 Plugins 页面，在 Personal 来源找到“化学科研技能面板”并安装。随后打开新对话，输入：

> 打开化学科研技能面板。

界面出现后，点击相应技能旁的“插入”，在当前对话输入框补充任务并发送。如果按钮显示“复制”，点击后粘贴到当前输入框即可。若宿主不渲染界面，打开插件 `assets/panel.html` 使用同一列表。

支持原生菜单的桌面客户端还可在输入框输入 `@`，选“化学科研技能面板”，再按英文名称、中文用途或来源选择技能；空搜索返回全部五项。它与 Codex 自带的 `$` 技能选择器是不同入口，不需要背英文名称。若没有出现此菜单，使用面板或复制入口。

浏览器入口本身不需要 Python、联网或后台服务。Windows 双击 `dist/chem-skill-panel/assets/panel.html` 即可；未安装插件时，也可以将复制的技能名称交给已安装相应通用技能的 Codex，并说明使用已有技能。

## Windows App 使用 WSL 项目

如果 Codex 在 WSL 内执行任务，先在同一 WSL 环境安装插件，使用 `python3` 替代 `py -3`。该 Python 需包含 venv/pip；也可使用已有 Conda 环境中的 Python。

Windows 原生与 WSL 的用户目录、解释器和插件目录不同。不要把 WSL 的绝对启动路径复制给 Windows 原生运行环境。安装器默认使用执行它的那个环境；真实宿主拾取情况仍需在新对话检查。

## 源码与更新

仓库根目录 `catalog.json` 和 `skills/` 是目录及五项技能的唯一编辑源；来源在构建时从各技能 `SOURCE.json` 读取，链接指向固定 commit 的原文；`plugins/chem-skill-panel/` 保存 UI、MCP 与入口技能。`tools/build_plugin.py` 生成 `dist/chem-skill-panel`，复制原文及第三方许可并嵌入目录。仅打包通用技能，不扫描用户目录。

构建包最初提供技能与浏览器面板；运行 `install.py` 后才生成本机 `.mcp.json` 并将它加入插件 manifest。不要直接导入尚未运行安装器的 ZIP 后期待 MCP 自动连接。

本安装器面向首次安装，不自动替换现有插件。后续更新先改仓库并重新构建，再按官方 Plugin Creator 更新流程更新已注册源目录、缓存版本及重新安装；保留或备份本机 `.mcp.json`，避免把构建包中的无 MCP manifest 直接覆盖到已安装源。原有 `tools/manage.py` 仍仅管理独立技能，不管理本插件。

在 Codex CLI 可用的环境，个人 marketplace 注册后可运行 `codex plugin add chem-skill-panel@personal`；如果原个人 marketplace 名称不同，以安装器打印的 `marketplace_name` 为准。不必对默认个人目录另执行 `marketplace add`。

## 数据流与工具

| 工具 | 返回内容 | 是否执行研究 |
|---|---|---|
| `open_skill_panel` | 中文目录与 UI resource，状态 `catalog_only` | 否 |
| `search_skill_mentions` | 原生菜单的英文技能名、中文用途与来源，可按名称和用途搜索 | 否 |
| `prepare_skill_task` | 旧版兼容工具；新界面不调用 | 否 |
| `get_skill_instructions` | 所选技能原文与资源所在目录，状态 `instructions_loaded` | 否；随后由 Codex 按用户任务执行 |

MCP 服务只接受目录中的技能名称，不提供任意文件读取或命令执行工具。原生菜单返回的 `chem-skill://skills/<name>` 资源解析为对应技能原文。服务通过标准 stdio 在本机运行，不监听公网端口。选择时仅传递技能引用到当前输入框；由用户发送任务后，Codex 才按所选技能工作。

上游技能分别保留原许可；原创 UI 与工具遵循仓库 LICENSE，不能将整个插件包统一声称为 MIT 内容。
