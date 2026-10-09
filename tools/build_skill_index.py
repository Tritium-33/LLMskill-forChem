#!/usr/bin/env python3
"""Generate cross-source functional routing indexes from the canonical package catalog."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
 'runtime-support': ('运行与作业支持', '仅在所选科学技能确有需要时加载；安装软件、凭据配置和提交作业是独立操作，不因加载技能自动执行。'),
 'chemistry-materials': ('化学与材料', '输入通常为结构、分子、光谱、热力学数据库或动力学机制；根据科学对象选择，不把分子工具套用于周期晶体。'),
 'research-evidence': ('科研检索与论证', '按找资料、核书目、证据综合、形成假设、设计实验和评阅区分；检索获得记录不等于已读全文。'),
 'data-modeling': ('数据、统计与机器学习', '先明确解释、推断、预测还是优化目标；若任务只需基础统计，不强制建立机器学习模型。'),
 'writing-figures': ('写作与图表', '区分真实数据图、概念示意图、文稿与幻灯片；外部图像服务不是真实数据绘图的必需工具。'),
}

def build(root=ROOT):
 catalog=json.loads((root/'catalog.json').read_text(encoding='utf-8'))['skills']
 rows=[]
 for entry in catalog:
  source=json.loads((root/'skills'/entry['name']/'SOURCE.json').read_text(encoding='utf-8'))
  if entry['name']=='scientific-skill-router':continue
  group=entry.get('routing_group')
  if group not in GROUPS:raise ValueError('Missing/unknown routing group: '+entry['name'])
  text=(root/'skills'/entry['name']/'SKILL.md').read_text(encoding='utf-8')
  front=text.split('---',2)[1]
  compatibility=next((line.split(':',1)[1].strip() for line in front.splitlines() if line.startswith('compatibility:')), 'Read the skill for runtime requirements.')
  rows.append(dict(name=entry['name'],group=group,purpose=entry['summary'],example=entry['example_prompt'],compatibility=compatibility,source_name=source.get('repository',source.get('project','Local')).removeprefix('https://github.com/'),source_url=(f"{source['repository']}/blob/{source['commit']}/{source['path']}/SKILL.md" if source.get('repository') else None),bundled=True,runtime_ready='not established by installation'))
 out=root/'skills/scientific-skill-router/references';out.mkdir(parents=True,exist_ok=True)
 for group,(title,guidance) in GROUPS.items():
  members=[r for r in rows if r['group']==group]
  lines=['# '+title,'',guidance,'','表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。','','| 技能 | 用于什么任务 | 来源 |','| --- | --- | --- |']
  lines += [f"| `{r['name']}` | {r['purpose']} | "+(f"[{r['source_name']}]({r['source_url']})" if r['source_url'] else r['source_name'])+" |" for r in members]
  lines+=['','## 选择后再核对依赖','']
  lines += [f"- **{r['name']}**：{r['compatibility']}" for r in members]
  (out/(group+'.md')).write_text('\n'.join(lines)+'\n',encoding='utf-8')
 (out/'index.json').write_text(json.dumps({'schema_version':1,'scope':'All bundled task skills grouped by function across sources; router excluded','skills':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 docs=root/'docs';docs.mkdir(exist_ok=True)
 lines=['# 科研技能功能目录','',f'按任务选择技能，来源仅用于追溯与许可说明。包含{len(rows)}项具体技能及独立的 `scientific-skill-router` 选择入口。技能文件已收录，不表示依赖已安装或科学效果已验证。','']
 for group,(title,guidance) in GROUPS.items():
  members=[r for r in rows if r['group']==group]
  lines += ['## '+title+'（'+str(len(members))+'项）','',guidance,'','| 技能 | 中文用途 | 来源 |','| --- | --- | --- |']
  lines += [f"| [{r['name']}](../skills/{r['name']}/SKILL.md) | {r['purpose']} | "+(f"[{r['source_name']}]({r['source_url']})" if r['source_url'] else r['source_name'])+" |" for r in members]
  lines += ['']
 lines += ['## 如何选择','','直接描述任务，或使用 `$scientific-skill-router`。同一板块可以包含不同来源的技能；根据具体任务、输入和依赖选择，不以来源决定优先级。','','- 找论文：`paper-lookup`；组织综述：`literature-review`；深入审查创新性：`lit-review`。','- 生成/整理书目：`citation-management`；严格核验书目：`ref-check`；核对原文证据：`reading-contract`。','- 建模与交叉验证：`scikit-learn`；审查数据接触历史与验证独立性：`independence-bookkeeping`。','','## 依赖与使用限制','','以下是上游声明或原文指引，安装时没有逐项运行全部科学任务。外部API和科学软件需按任务确认。','']
 lines += [f"- **{r['name']}**：{r['compatibility']}" for r in rows]
 (docs/'skills-catalog.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print(f'Indexed {len(rows)} skills across {len(GROUPS)} groups.')
 return rows

if __name__=='__main__':build()
