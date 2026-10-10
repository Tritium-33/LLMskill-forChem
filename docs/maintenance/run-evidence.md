# 可选的运行证据检查

这是维护者/测试运行器使用的离线检查工具，普通用户无需运行，独立安装 skill 也不依赖它。只需要 Python 3.10+ 标准库，输出到标准输出，不修改输入，不调用模型、联网或安装软件。

它解决三个可机械检查的问题：预期指令有没有出现在**实际初始上下文**；主会话有没有成功读取指定技能；返回最终答案时有没有尚无终态记录的委派。它不判定科学质量，不证明模型遵循了指令，也不是 DSH 日志的自动适配器。

## 输入由哪里来

由宿主日志导出器或审计人员从真实记录整理以下 JSON；不能从计划/profile 文件生成“已观察”记录。`source` 保存原始记录的相对路径及事件号/JSON 指针，供独立复核。源日志不必公开，也不要导出内部思考、凭据或无关个人信息。

```json
{
  "schema_version": 1,
  "initial_context": {
    "complete": true,
    "source": "request.json#/messages",
    "messages": [
      {"role": "user", "content": "先读取 scientific-skill-router，再选择必要技能。"}
    ]
  },
  "events_complete": true,
  "events": [
    {"seq": 1, "kind": "skill_load", "session": "main", "skill": "scientific-skill-router", "status": "success", "source": "events.jsonl:12"},
    {"seq": 2, "kind": "job_start", "session": "main", "job": "worker-1", "source": "events.jsonl:18"},
    {"seq": 3, "kind": "job_end", "session": "worker-1", "job": "worker-1", "status": "completed", "source": "worker.jsonl:41"},
    {"seq": 4, "kind": "final_answer", "session": "main", "source": "events.jsonl:27"}
  ]
}
```

这是格式示例，不是真实运行证明。每个记录对应一个用户任务回合，`seq` 是跨会话按发生顺序整理的严格递增序号，不是各原始文件自行重复的行号。无法确定先后关系或缺日志时，不能宣称事件完整。

- `initial_context.complete`：实际首个请求的全部 system/developer/user 文本是否完整捕获。不能用磁盘上的 AGENTS.md 替代。`messages` 是整理后的文本块，非直接兼容任意厂商请求格式。
- `events_complete`：本回合全部技能加载、所有层级委派的开始/终态和主会话最终答复是否完整覆盖；只有部分日志时设为 `false`。`session: main` 表示主会话，其余值表示工作会话。
- `skill_load.status: success`：已观察到内容成功返回，而非调用发出或回答自述使用。普通文件读取也可导出为技能加载，但必须确实返回对应正文。失败用 `failure`。
- `job_end.status`：只能为有回执的 `completed` / `failed` / `cancelled`。推断超时不是已取消；没有终态时保留未结束状态。
- 一个技能被 worker 读取不证明主会话读取；终态发生在最终答复之后不能倒算为答复前已收齐。

完整性和 source 真实性由导出者负责，工具无法认证。伪造 JSON 会使检查失去意义；它检查的是记录内部的可观察条件，不是安全隔离或完成状态强制器。

## 执行方式

在仓库根目录，先将想验证的原始指令文字保存到 UTF-8 的 `expected-instruction.txt`。匹配是**精确子串**，不是语义判断；即便文字出现，也可能只是引用，并不能证明其指令优先级或实际被遵循。

```text
python tools/maintenance/check_run_evidence.py observed-run.json --instruction-file expected-instruction.txt --preflight
python tools/maintenance/check_run_evidence.py observed-run.json --instruction-file expected-instruction.txt --required-skill scientific-skill-router
```

Windows 路径含空格时加引号；在只有 `python3` 的系统上替换命令名。

预检只检查真实初始上下文。可在宿主已组装请求、尚未大规模执行前导出快照；若宿主只能事后提供，则先运行最小试验再检查，不能声称有实时拦截。正式实验的 runner 可在非零退出码时停止后续批次；本工具本身不控制 runner。

| 输出 | 含义 | 退出码 |
| --- | --- | --- |
| `pass` | 请求检查的观察条件满足 | 0 |
| `fail` | 有缺失证据，例如完整上下文没有所需指令，或最终答复前存在未结束任务 | 1 |
| `inconclusive` | 记录不足，或没有请求任何可判定检查 | 2 |
| `invalid` | 输入格式或事件顺序矛盾 | 2 |

子任务失败或取消也属于已收尾，因此可能通过收尾检查；**不代表任务成功或内容已核验**。部分结果是否合理、回答是否诚实披露限制，交由内容评审。token、缓存、耗时和质量仍需单独计量，不从这些状态推算成本或归因 router。
