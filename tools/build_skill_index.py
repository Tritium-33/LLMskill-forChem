#!/usr/bin/env python3
"""Generate bounded K-Dense routing indexes from the canonical package catalog."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
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
  if source.get('repository')!='https://github.com/K-Dense-AI/scientific-agent-skills':continue
  group=entry.get('routing_group')
  if group not in GROUPS:raise ValueError('Missing/unknown routing group: '+entry['name'])
  text=(root/'skills'/entry['name']/'SKILL.md').read_text(encoding='utf-8')
  front=text.split('---',2)[1]
  compatibility=next((line.split(':',1)[1].strip() for line in front.splitlines() if line.startswith('compatibility:')), 'Read the skill for runtime requirements.')
  rows.append(dict(name=entry['name'],group=group,purpose=entry['summary'],example=entry['example_prompt'],compatibility=compatibility,source_url=f"{source['repository']}/blob/{source['commit']}/{source['path']}/SKILL.md",bundled=True,runtime_ready='not established by installation'))
 out=root/'skills/scientific-skill-router/references';out.mkdir(parents=True,exist_ok=True)
 for group,(title,guidance) in GROUPS.items():
  members=[r for r in rows if r['group']==group]
  lines=['# '+title,'',guidance,'','表中英文标识对应独立技能；先核对当前会话可用性，再读取其 SKILL.md。支持软件/账号是否可用需在任务中检查。','','| 技能及固定来源 | 用于什么任务 |','| --- | --- |']
  lines += [f"| [{r['name']}]({r['source_url']}) | {r['purpose']} |" for r in members]
  lines+=['','## 选择后再核对依赖','']
  lines += [f"- **{r['name']}**：{r['compatibility']}" for r in members]
  (out/(group+'.md')).write_text('\n'.join(lines)+'\n',encoding='utf-8')
 (out/'index.json').write_text(json.dumps({'schema_version':1,'scope':'Selected K-Dense skills in this distribution, not the complete upstream catalog','skills':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(f'Indexed {len(rows)} skills across {len(GROUPS)} groups.')
 return rows

if __name__=='__main__':build()
