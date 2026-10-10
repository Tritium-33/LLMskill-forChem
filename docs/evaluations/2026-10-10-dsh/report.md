# LLMskill-forChem：三组科研问答盲测对比报告

> 公开收录说明：本报告评估的是提交 `cf65781d4058cb6c0e9dfcab3842149450351e04`。与本地交付版相比，仅将一处机器专属实验根路径替换为 `<experiment-root>` 并添加本说明；21 份问答、评分和结论未改。原版哈希与公开版哈希见 [来源记录](provenance.json)。文内原始日志及评审中间文件路径用于说明审计依据，不表示这些文件已公开附带；公开内容和局限见 [评估说明](README.md)。


评估日期：2026-10-10。对象：7 道题 × 3 组 × 1 次运行，共 21 份最终回复。目标论文 DOI：10.1038/s41467-026-68735-3。

本报告先完整呈现原始输入、输出与实际调用/资源，再给出独立内容盲审和主代理的过程审计。原始问答以代码块逐字保存，包括原有错误、技能声明和未完成说明；未替回答者改写。每题三组输入完全相同，因此共同原文只展示一次。

A：不提供本项目技能；B：提供具体技能，不提供合集 router；C：提供同样具体技能及合集 router。**这只是实际暴露配置的名称，不预设技能已使用或 C 已执行 router。** 设计文件中的“C 强制先使用 router”与实际请求存在差异，详见后文。

资源口径：token 是日志中已返回的 provider usage，含主会话和委派会话；未缓存输入、缓存读取、输出分别列出，缓存写入均为 0。输出 token 含推理部分，不等于最终回答长度。耗时为启动至 harness 进程结束的墙钟秒数，不是所有子会话耗时相加，也不必等于首个可见回答延迟。不换算货币金额。

本报告审计实际使用 scientific-skill-router 选择核查技能、reading-contract 核对来源、independence-bookkeeping 区分内容盲审与已知组别的过程审计。执行顺序：核对原始输入输出与材料 → 匿名化并独立评阅 → 重算日志用量并查实际调用 → 评分冻结后关联组别、合并报告。该记录属于评估者，不计入被测三组消耗。

## 第一部分：原始问答、实际 skill 调用与资源

### T1

#### 三组共同的用户输入原文

````text
所需论文材料位于 materials；可以按需要读取，并使用现有检索工具。

帮我分析一下这篇论文：10.1038/s41467-026-68735-3。
````

| 组 | 主会话成功加载的 skill（实际顺序） | 耗时/s | 未缓存输入 | 缓存读取 | 输出（含推理） | 总 token | 请求数（含委派） |
|---|---|---:|---:|---:|---:|---:|---:|
| A | 无 | 260.4 | 77,914 | 3,633,407 | 32,317 | 3,743,638 | 54（委派 0） |
| B | `peer-review` | 353.5 | 93,010 | 4,348,928 | 57,401 | 4,499,339 | 50（委派 0） |
| C | `scientific-skill-router` → `reading-contract` → `scientific-critical-thinking` | 369.1 | 164,166 | 4,977,664 | 63,603 | 5,205,433 | 40（委派 0） |

#### T1-A 最终输出原文

````text
核查完成。分析报告已写入 `artifacts/paper-analysis.md`（含从 PDF/Excel 抽取的原始数据与核查脚本）。以下是要点。

# 论文分析：*Machine-learning-guided tungsten single atoms promote oxyhydroxides for noble-metal-free water electrolysis*

**Nature Communications 17, 2344 (2026)** · DOI 10.1038/s41467-026-68735-3 · 首尔大学 Ho Won Jang 等（KRISS / 高丽大学合作）· 2025-10-14 投稿，2026-01-29 在线 · 开放获取，含 Transparent Peer Review、15.6 MB SI、逐图 source data 与 Zenodo 代码/检查点。

## 1. 做了什么

用预训练等变图神经网络 **EquiformerV2（OC22）**，在 **3,976 个"单原子 M₁ 掺入 8 种 MᴬMᴮOOH"构型 × 4 个 OER 中间体（>15,000 个吸附结构）**中做高通量筛选，选出 **W₁–NiFeOOH**；用循环伏安电沉积（−0.1→−1.8 V vs. Ag/AgCl，30 圈）制备，再以原位 XAS/Raman + DFT(+U) 解析机理。

**主要结果**
- **结构**：W 占金属原子 2.62 at.%（ICP-AES），HAADF-STEM/EDS 证明原子级分散；W L₃ EXAFS 仅见 W–O 第一壳（1.92–1.99 Å，畸变 WO₆），无 W–W 峰。
- **半电池**（1 M KOH，阴极回扫 + 95% iR 补偿）：η₁₀ = **178 mV**（W₁）vs 185（Ir₁）、214（NiFeOOH）；Tafel 32 mV dec⁻¹；>200 h 稳定。
- **AEMWE 单电池**（80 ℃、1 M KOH、商业 PiperION 20 µm、PtRu/C 阴极、**未 iR 补偿**）：**1 A cm⁻² @ 1.56 V；2.0 V 时 13.19 A cm⁻²**（Ir₁ 10.46、NiFe 8.15）；60 ℃ 下 **531 h @ 1 A cm⁻²** 稳定（源数据可查）。
- **机理**：原位 XAS 显示 W 价态在 OCP→1.6 V 恒定（+5.07→+5.11）、Ir 则从 +2.17 氧化到 +4.17 → **W 是"促进剂"、Ir 才是直接的活性位**；W 使 Ni 更早（~1.40 V）/更深氧化（+3.6 vs γ 相 +3.75），γ 相 Raman 特征峰在 1.43 V 出现（对照 1.45 V）。DFT 给出 W 路径 η = 0.357 V（NiFeOOH 0.475 V），走 Mars-van-Krevelen 晶格氧机制。

## 2. 最有价值的地方

1. **闭环 + 反直觉对照**：用 Ir₁–NiFeOOH 作"直接活性位"参照，把"促进剂 vs 活性位"两种角色区分开，机理叙事有说服力。
2. **域外验证做得比同类工作认真**：自建 DFT 集横比 GemNet/PaiNN/DimeNet++、给 parity plot、微调超参网格、并对未见组分做迁移性测试；还诚实说明"最终筛选仍用未微调模型"。
3. **AEMWE 部分最硬**：1.56 V @ 1 A cm⁻²、>500 h、商业膜、源数据齐全，是全文最有分量的工程结论。
4. 细节自觉：XAS/XPS 换到碳纸以排除泡沫镍干扰；AEMWE 明确声明未做 iR 补偿。

## 3. 关键问题（按重要性）

1. **摘要与自己的 DFT 数据冲突**：摘要说"降低 **deprotonation** 步骤的 PCET 势垒"，但 Fig. 6c 的自由能图显示势决定步是 **\*O→\*OOH（0.536 eV，0.357 eV 的脱质子步不是最高点）**；正文也自认 limiting step 是 \*O→\*OOH。
2. **"ML 指导"的证据被自己的数据削弱**：ML 首选的 Ir（0.254 V）在 DFT 复算的同类取代位上 η = **0.581 V，比未掺杂的 NiFeOOH（0.475 V）还差**；作者靠另一类锚定位点（Ir₁-3O，0.310 V）才救回名次。同时预训练模型吸附能 MAE 0.408 eV 与候选间真实能量差（0.2–0.5 V 量级）同数量级，**未做误差传播/排名稳定性分析**。结论：目前只能说 ML"能快速产生候选"，不足以支撑"可靠识别最优"。
3. **ECSA 数值对不上**：图注/正文写 3.28/5.93/6.08 mF cm⁻²，但我用 `Figure S34` 源数据回归只得到 **≈0.024/0.024/0.013 mF cm⁻²**（差约两个数量级）。且按图注值 W₁ 的 Cdl 最低，正文却说 ECSA 证明"活性位更多"，方向相反——数据其实支持"面积更小、本征活性更高"。
4. **审稿人要求的两点未落实**：Transparent Peer Review 中 Reviewer #4 明确要求（i）说明 KOH 是否 Fe-free / 是否监测 Fe 污染、（ii）Hubbard U 敏感性；修订稿补了 U 值（Ni 5.20 / Fe 2.56 / W 6.20 eV），但**全文与 SI 没有任何 Fe 污染、Fe-free 相关表述，也没做 U 敏感性测试**（我逐文件检索确认）。
5. **机理证据链偏弱**：EXAFS 拟合表**未给配位数 N**；pH 12.5–14.0 的 LSV、非原位 TMAOH-Raman 只是"形状相似"的定性旁证，缺同位素标记或 dη/dpH 定量。
6. **口径需澄清的小问题**：半电池活性取自**阴极回扫**（测的是被预活化的 γ 相，会高估初始本征活性）；AEMWE 用 50 mV s⁻¹ LSV 且不 iR 补偿（但作者其实测了 0.5–5 A cm⁻² 的 EIS，有条件给稳态点）；Fig. 3e 源数据里 Ir₁/NiFe 在 1.55–1.60 V 附近取值不单调、n 值与图注 n=5 不一致；Methods 扫描速率 50 与 Fig. 3e 图注 10 mV s⁻¹ 冲突；AFM 把 ~4 nm 片层称"单层"；"55 N m⁻¹"膜压单位疑似有误。

## 4. 总体判断

- **高置信**：W 确实以原子级分散掺入 NiFeOOH；W₁–NiFeOOH 确实比 NiFeOOH 更快（半电池与单电池同向）；**AEMWE 1 A cm⁻² @ 1.56 V + >500 h** 是扎实且有竞争力的结果（13 A cm⁻² @ 2.0 V 量级领先，但需稳态验证）。
- **中等置信**："W 为促进剂、Ni–O–Fe 边缘位为活性位"逻辑自洽，但"晶格氧 MvK"仍是 suggest 级别。
- **应打折**：标题中的 "machine-learning-guided"——ML 的首选 Ir 未被 DFT 支持，且缺少误差棒与命中率统计；这是一篇**实验价值 > 计算筛选价值**的论文，摘要/标题的因果强度应下调。

**建议补做（优先级序）**：Fe 污染控制说明 → AEMWE 稳态恒电流点 + iR-corrected 曲线 + 长时衰减速率与前后 XAS/STEM → ML 不确定性/排名稳定性量化 → EXAFS 配位数与 W 团簇检测限 → U ±1 eV 敏感性 + 溶剂/pH/电位对 MvK vs AEM 竞争的讨论 → 修正摘要中 deprotonation 表述并统一各处口径。

报告全文（含逐条数据核对、源数据回归结果与核查脚本索引）：`artifacts/paper-analysis.md`。
````

#### T1-B 最终输出原文

````text
已完成分析。我通读了 PMC 全文、Nature PDF、61 页补充材料、透明同行评审文件，并用 openpyxl 逐表解析了 `source-data.xlsx` 的 42 个工作表做交叉核对。完整报告已存至 `artifacts/paper-analysis.md`，以下是要点。

# 论文分析

**Machine-learning-guided tungsten single atoms promote oxyhydroxides for noble-metal-free water electrolysis**
*Nat. Commun.* **17**, 2344 (2026). DOI: 10.1038/s41467-026-68735-3（[nature.com](https://www.nature.com/articles/s41467-026-68735-3)；PMID 41611674 / PMC12979610）

## 一、做了什么

用 OC22 预训练的等变 Transformer 图神经网络 **EquiformerV2** 当吸附能代理模型，在 **3,976** 个"单原子 M₁ + 金属羟基氧化物 M_A M_B OOH"构型（8 × 41 × 13 去重）里筛选，提名 **W₁–NiFeOOH**；循环 CV 电沉积制备；半电池 η₁₀ = **178 mV**，AEMWE（PiperION 20 µm、1 M KOH、80 °C）在 2.0 V 达 **13.2 A cm⁻²**，1 A cm⁻² 下测了 **531 h**；再用原位 XAS/Raman + DFT 论证机理：**W 是促进剂（自身不变价），真正被激活的是边缘 Ni–O–Fe 桥位；Ir 则自身即活性位**。

## 二、证据强度分级

**强**
- W 原子级分散且取代进入八面体晶格（HAADF-STEM + EDX + ICP-AES 2.62 at% + XANES/EXAFS + WT-EXAFS + 形成能）。
- 活性排序 W₁–NiFeOOH > Ir₁–NiFeOOH > NiFeOOH（半电池与 AEMWE 一致；AEMWE 源数据 13.197 / 10.457 / 8.149 A cm⁻²）。
- W 在 OER 中基本不变价（原位 W L₃），Ir 明显变价（原位 Ir L₃ 白线位移 +1.16 eV）——"促进剂 vs 活性位"的定性区分有直接谱学证据。

**中**
- W 促进 Ni 氧化/γ 相转变；晶格氧（Mars-van-Krevelen）机理（DFT 自洽，实验为定性）。

**弱/过度解读**
- "超越 universal theoretical limit"；DFT 支持的"W 本征优于 Ir"；"500 h 稳定"。

## 三、我核查出的具体问题（均给出处）

1. **稳定性"stable"未量化**：Fig. 3g 源数据显示槽压 1 h **1.602 V** → 500 h **1.780 V**（**+178 mV**，约 0.36 mV h⁻¹，前 100 h 就升了 ~129 mV）。正文只说 "stable"，无衰减率、无 post-mortem。
2. **ML 筛选用错模型**：高通量筛选用的是**未微调的预训练模型（MAE 0.408 eV）**，而非精度高一倍的微调模型（0.191 eV）。Fig. 1d 预测 W 0.268 V、Ir 0.254 V，"超越 ~0.37 V 理论极限"的结论落在模型误差棒内。
3. **筛选前列未说明取舍**：Fig. 1d 前六为 Ir 0.254、W 0.268、**Tl 0.271、Rh 0.301、Ba 0.308、Ta 0.334** V，正文完全不讨论 Tl/Ba/Rh/Ta 为何被排除。
4. **DFT 结论不稳健 + Fig. S52 自相矛盾**：Ir 的 η 随锚定构型在 **0.310 / 0.485 / 0.581 / 0.754 / 0.962 V** 间变动（跨度远大于 W 与 Ir 的 ~0.2 V 差）；且渲染 S52 后确认 b 图 Ir₁ 曲线 PDS = 0.754 V、NiFeOOH = 0.855 V，而 c 图与正文给 Ir₁–3O = 0.310 V、NiFeOOH = 0.754 V。
5. **"W 促进 γ 相转变"的实验证据偏弱**：原位 Ni K 边"Ni oxidation state"（Fig. 4e 源数据）W₁/NiFeOOH 差异几乎全程 **≤0.08**，且 **1.40 V 时 NiFeOOH 反而更氧化**（2.74 vs 2.60），与正文 "significantly larger … at all potentials" 不符；Raman 转变电位仅差 **20 mV**（1.43 vs 1.45 V），而步长是 10 mV 且无重复/误差棒。
6. **混淆因素未控**：Fe 杂质完全未提（同行评审里 Reviewer #4 明确要求，正文未落实）；ECSA 翻倍（C_dl 6.08 vs 3.28 mF cm⁻²）带来位点数量效应；Tafel 32 mV/dec 取自窄窗口（log j 1.16–1.63）阴极扫描，偏低于 OER 常见值。
7. **W 价态前后冲突**：原位 XANES 拟合 +5.07 → +5.11，但正文结构部分说"接近 **+6**"（对齐 WO₃），XPS 也解出 W⁵⁺/W⁶⁺。
8. **原位 XAS 电解液不统一**：W、Ir L₃ 边在 **0.1 M KOH**，Ni K 边在 **1 M KOH**。
9. **EXAFS 报告缺口**：Supp. Table 3/4 **无配位数 N**；正文称 W–Ni/Fe 第二壳层"与拟合吻合"，但 Table 3 只有 W–O₁/₂/₃ 三条路径。
10. **数值对不上**：Ir₁–NiFeOOH η₁₀ 源数据 **185 mV** vs 正文/Table 5 **183 mV**；AEMWE 1 A cm⁻² 正文 **1.56 V**，源数据插值 ≈**1.51 V**；AEMWE 扫速 Methods 写 **50 mV/s**、Fig. 3e 图注写 **10 mV/s**。
11. **成分与假设不符**：镀液 Ni:Fe = 4:1，ICP 实测 ≈**1.81:1**；成本模型却假设 Ni:Fe = 3:1、M = 1 at%（实测 W = 2.62 at%）。
12. **Source Data 标注错误（影响独立复核）**：Fig. 4c 里标 "W L₃ edge" 的列装的是 ~11217.8 eV（实为 **Ir** 边），标 "Ir L₃ edge" 的列装的是 ~10212.1 eV（实为 **W** 边）——照表读会把机理读反；另有工作表名与图号错位（"Figure S37" 装 Fig. S38 数据）。
13. **编辑性错误**：AFM 型号是占位符 "**AFM (model)**"；"applied pressure of **55 N m⁻¹**" 单位可疑；"Nickel paper (**0.5 t**, Bekaert)"；"onset overpotential … **at 10 mA cm⁻²**" 术语误用。

**已核实自洽的部分**：3,976 = 8×41×13 去重、>15,000 ≈ 3,976×4；DFT 自由能图在 U = 1.23 V 下四步之和为 0 且 η = max(step)（Fig. 6c 与 Fig. S52 的数值记账本身没问题）；Fig. 1e 成本结论即使按实测 2.6 at% W 也稳健（W 45 vs Ir 162,577 USD/kg）。

## 四、总体评价

工程完成度高，闭环完整（筛选→制备→器件→原位谱学→DFT），"W 作促进剂 / Ir 作活性位"的对照是有价值的机理结论；AEMWE 性能在无贵金属阳极中居前列。但三处核心主张的支撑强度与措辞不匹配：**ML 预测精度撑不起"超越理论极限"**；**"W 促进 γ 相转变"的实验差异太小且无统计**；**Ir 的 DFT 结果被构型选择支配且有面板间矛盾**。此外 Fe 杂质控制、稳定性衰减率、EXAFS 配位数、U 值敏感性这些领域内标准信息缺失，加上若干报告错误，会实质影响可复现性。

建议作者优先补：500 h 电压衰减率（mV h⁻¹）+ post-mortem、Fe-free/定量 Fe 的 KOH 对照、U 值敏感性、用微调模型+不确定度重做火山图、修正 Fig. S52 与 Source Data 标签、统一原位 XAS 电解液并调和 W 价态。

（本分析为 AI 辅助草稿，关键数字建议对照原文与 Source Data 人工复核；完整版见 `artifacts/paper-analysis.md`。）
````

#### T1-C 最终输出原文

````text
已完成分析。报告同时存为 `artifacts/paper-analysis.md`（含可重跑的复核脚本）。

【本轮技能】`scientific-skill-router`（路线选择）、`reading-contract`（带定位的证据读取）、`scientific-critical-thinking`（证据与论证评价）

【执行步骤】
1. [完成] 读 `scientific-skill-router`，按 DOI→论文分析路线：已有可信全文 → 复用材料，条件分支接证据评价技能。
2. [完成] 读 `reading-contract`、`scientific-critical-thinking`。
3. [完成] 清点 `materials/`；自行用 PyMuPDF/openpyxl 抽取（未用 markitdown）：SI 61 页、同行评议 2 页、Source Data 42 个工作表 → `artifacts/extract_materials.py`。
4. [完成] `web_search` 确认题名/DOI/出版页；未加载 `paper-lookup`（路线允许复用全文）。
5. [完成] 阅读 Nature 落地页全文与 PMC 全文（抽查关键句两版一致）、SI 表 S1–S6、审稿文件、全部 Source Data。
6. [完成] 编写 `check_numbers.py` 等做“原文数字 vs 自带 Source Data”一致性核验。
7. [未执行] `ref-check`（未要求）、`lit-review`（单篇不升级为综述）、DFT/ML 复算（无结构与权重）。
8. [受限] `Supplementary Data 1` 不可用 → 3,976 候选结构清单与 K⁺ 插层模型未核实。

---

# 论文分析：10.1038/s41467-026-68735-3

**Machine-learning-guided tungsten single atoms promote oxyhydroxides for noble-metal-free water electrolysis**，*Nat. Commun.* **17**, 2344 (2026)，PMID 41611674 / PMC12979610（收稿 2025-10-14，接收 2026-01-14）。

## 1. 设计与论证链（读到的内容）
问题：在“单原子 M₁ 掺入金属(羟基)氧化物”的 3,976 个候选空间中找非贵金属 OER 阳极并解释机制。链条：OC22 预训练 EquiformerV2 + 自建 DFT 微调 → 火山图提名 W₁–NiFeOOH → CV 电沉积制备 → 结构与谱学表征 → 半电池/AEMWE → 原位 XAS+Raman → DFT 机制（W 走 MvK 晶格氧机制，Ir 走吸附质演化机制）。

设计上的亮点：把“W 是助剂、Ir 是活性位”做成**可证伪对照**——原位 W L₃-edge 价态应不随电位变，Ir 应随电位变。

## 2. 主要结果（附定位，行号指 `materials/pmc-fulltext.txt`）
- 候选空间：3,976 模型 / 13 种位点 / 41 种 M₁ / >15,000 吸附结构（第 281 行；SI 图 S1）。
- ML：基线总 MAE **0.408 eV**、加速 1158×；微调后 **0.191 eV**（SI 图 S3/S4、表 S1）。
- 筛选排名（Source Data `Figure 1`，Fig 1d 区块）：**Ir 0.254 < W 0.268 < Tl 0.271 < Rh 0.301 < Ba 0.308 V**；成本 W₁-NiFe 0.013、Ir₁-NiFe 1.638、IrO₂/C 55.75 USD g⁻¹。
- 组成：W **2.62 at%**，Ni:Fe = 1.81:1（表 S2）；W–O 1.92–1.99 Å、无 W–W、畸变八面体 WO₆（图 2e–g、表 S3）。
- 半电池：**178 mV**@10 mA cm⁻²、Tafel 32、TOF 0.198 s⁻¹、FE 97–109%（图 3a–c；SI 图 S35/S36）；234 h 恒电位稳定（~110 mA cm⁻²）。
- AEMWE：80 °C、PiperION 20 µm，2.0 V 时 **13.19 A cm⁻²**；正文称 1 A cm⁻² 需 1.56 V；60 °C、1 A cm⁻² 运行 531 h（图 3e–g）。
- 原位：W 价态 +5.07→+5.11（不变，助剂）；Ir +2.17→+4.17（活性位）；Raman γ 相 1.43 V（W₁）vs 1.45 V（图 4、5）。
- DFT：Ni–O–Fe 桥位 η=0.357 V（W₁）vs 0.475（NiFe）vs 0.581（Ir₁）；Ir₁-3O = 0.310 V（图 6、SI 图 S52）。

## 3. 用作者自带 Source Data 复核（一致≠独立验证）

| 论断 | 原文 | 复核值 | 判定 |
|---|---|---|---|
| 筛选提名 W | W 最优 | W 第 2 名，落后 Ir **14 mV**，领先 Tl 仅 3 mV | 复现，但 W 非第一 |
| 基线/微调 MAE | 0.408 / 0.191 eV | 表 S3/S4 完全一致 | 复现 |
| η@10 mA cm⁻² | 178 / 183 / 214 | Fig 3b 表 178 / **185** / 214；由 Fig 3a 曲线插值 181.8 / 187.2 / **200.8** | 部分复现 |
| Tafel 32 | 32 | 重拟合 32.6（j 仅 14.5–42.9 mA cm⁻²） | 复现（窗口窄） |
| 1.56 V @1 A cm⁻² | 1.56 V | **1.506 V** 达 1 A cm⁻²；1.56 V 对应 1.84 A cm⁻² | **未复现** |
| 13.1 A cm⁻²@2.0 V | 13.1 | 13.197 | 复现 |
| >500 h 稳定 | stable | 1.602 V(1 h)→1.781 V(531 h)，**+180 mV** | 时长复现，“稳定”未量化 |
| W₁ Ni 位移“所有电位都更大” | — | 1.40 V：2.60 vs **2.74**；1.42 V：2.81 vs **2.93** | **低电位段相反** |
| Ir 1.6 V“显著正移→+4.17” | — | Ir 白线/空穴在 **1.4 V 最高**，1.5→1.6 V 下降 | **与自带数据相反** |
| Raman 1.43 vs 1.45 V | — | 强度比 1.376→0.808（1.43 V）；Ir/NiFe 1.45 V 才跌破 1 | 复现 |
| DFT W 0.357 < NiFe 0.475 | — | 数值一致；但 Ir₁-3O 0.310 < W 0.357 | 数值复现，排序问题 |
| ICP W 2.6% | 2.62 | 一致；但成本模型假设 Ni:Fe=3:1 与实测 1.81:1 不符 | 复现 |
| 扫描速率 | 图注 10 vs 方法 50 mV s⁻¹ | 两处并存 | 内部不一致 |
| 表 S3 | — | 逐词核验 p.56：**无配位数 N 列**（脚注却定义 N） | 报告缺项 |
| 审稿意见（U 敏感性 / Fe-free KOH） | — | SI 检索不到相关分析；方法只有防 CO₂ 措施 | 未见明确回应 |

## 4. 结论强度

**关键问题**
- **C1｜筛选的分辨率远低于模型误差。** W 与 Ir 只差 14 mV≈0.014 eV，与 Tl 差 3 mV；而基线模型 MAE 是 **0.408 eV**，且高通量筛选用的是**未微调**骨干（第 285 行），也无不确定性量化。模型误差比待区分的能差大 1–2 个数量级 → “W 是最优非贵金属候选”应降级为“W 是与 Ir 同档的候选之一”。
- **C2｜计算与实验排序相反且未正面处理。** ML（Ir 0.254<W 0.268）与 DFT（Ir₁-3O 0.310<W 0.357）都把 Ir 排在 W 前；SI 图 S52 的解释并未反转排序。合理说法是“W 与 Ir 本征活性同档，W 因成本/无贵金属入选”。

**重要问题**
- I1 图 4e 与正文矛盾（支撑“W 促进 γ 相”的核心证据），需澄清含列标是否互换。
- I2 图 4c 与正文相反，且 +2.17→+4.17 与 W 的标定斜率差约 2 个数量级 → 价态值“按未说明约定才成立”。
- I3 “1.56 V”不可复现（1.506 V；1.56 V 更接近对照 NiFeOOH 的 1.554 V）。
- I4 “500 h 稳定”缺判据（+180 mV，无衰减率比较）；且未在 13.1 A cm⁻² 下测稳定性。
- I5 审稿人要求的 **Fe 杂质控制**未见回应，直接影响 Ni(OH)₂/NiFeOOH 对照（论文自己引 Klaus 2015 说明 Fe 效应）。
- I6 AEMWE 阳极载量（mg cm⁻²）未报告，A cm⁻² 无法跨研究归一化。
- I7 半电池取阴极扫描（合理）但表 S5 横向比较多为阳极扫描，可比性需注明。
- I8 审稿文件只有意见、无作者答复 → 响应不可核。

**次要**：183 vs 185 mV 疑张冠李戴；Fig 3b 与 Fig 3a 取数约定不同（NiFe 214 vs ≈201）；图注/方法扫描速率不一致；表 S3 缺 N；“<0.01 eV atom⁻¹”单位与表不符；“55 N m⁻¹”单位可疑；成本模型输入与实际样品不符；Source Data 工作表名与图号错位（`Figure S37`↔S38）；γ 相电位差仅 20 mV；标题“noble-metal-free water electrolysis”与 PtRu/C 阴极不符（摘要/讨论措辞正确）；图 1c,d 只含 4 类基元而非 3,976 全空间；n=10 是同一 MEA 连续扫描、500 h 为单电池。

## 5. 值得肯定
真正的“ML 筛选→合成→原位表征→DFT”闭环；W/Ir 角色对照可证伪；数据与代码公开（Source Data 42 表、Zenodo 10.5281/zenodo.18205124）并附透明审稿文件；误差棒与原始 EIS/极化数据齐备，使本次复核成为可能；基线模型对比与超参记录完整。

## 6. 建议
给作者：补筛选不确定性量化与 top 候选 DFT 抽检，说明为何不用更准的微调模型筛选；澄清图 4c/4e 矛盾并公开价态标定；更正或说明 1.56 V；把稳定性量化为 mV h⁻¹ 并给 n；补 Fe-free KOH/电解液 Fe 含量与阳极载量；统一取数约定与扫描速率；表 S3 补 N 或说明为定性判定；标题限定为“非贵金属阳极/OER 催化剂”。
给读者可放心引用：单原子 W 的组成与局域结构定性结论、半电池 178 mV/32 mV dec⁻¹ 量级、2.0 V 下 ~13 A cm⁻²（该构型与载量下）、W 工况价态不变这一关键原位观察；引用时须加限定的：计算排序、γ 相促进幅度、1.56 V、500 h“稳定”、表 S5/S6 跨文献比较。

## 7. 未验证/局限
未复算 DFT/ML（无结构清单与权重，仅做表内一致性核对）；未复核原始 XAS/Raman 谱（只能用作者处理后的结果）；未做逐字段书目核验；`Supplementary Data 1`（候选结构、K⁺ 插层模型细节）未取得。本次只确认论文身份与两版全文关键句一致。
````

### T2

#### 三组共同的用户输入原文

````text
所需论文材料位于 materials；可以按需要读取，并使用现有检索工具。

这篇论文里，机器学习和 DFT 分别做了什么？作者怎么判断机器学习的预测靠不靠谱？
````

| 组 | 主会话成功加载的 skill（实际顺序） | 耗时/s | 未缓存输入 | 缓存读取 | 输出（含推理） | 总 token | 请求数（含委派） |
|---|---|---:|---:|---:|---:|---:|---:|
| A | 无 | 75.3 | 42,943 | 423,039 | 9,180 | 475,162 | 14（委派 0） |
| B | 无 | 82.0 | 45,860 | 876,288 | 9,584 | 931,732 | 24（委派 0） |
| C | `reading-contract` | 91.1 | 48,826 | 827,392 | 14,622 | 890,840 | 21（委派 0） |

#### T2-A 最终输出原文

````text
我已读完论文正文、补充材料（Supplementary Figs. 1–8、Table 1）、同行评审意见和 Source Data（Figures 1、6、S3、S4 的原始数值）。下面把这篇 *Nat Commun* 论文（*Machine-learning-guided tungsten single atoms promote oxyhydroxides for noble-metal-free water electrolysis*）里 ML 与 DFT 的分工、以及 ML 可信度验证的完整链条讲清楚。

---

## 一句话总览

**ML 负责"从巨大的候选空间里快速筛出/提名候选者"（预筛），DFT 负责"产生标准答案、最终判断机制与热力学"（标定 + 验证 + 解释）。** ML 从来不单独下结论，所有关键结论最后都由 DFT 重算、并被实验独立证实。

---

## 一、机器学习做了什么

**1）工具**：EquiformerV2（等变 transformer 图神经网络，121M 参数，在 OC22 数据集上预训练），把它当作**机器学习原子间势（MLIP）**用——直接由原子构型预测总能与原子受力，绕开 Kohn–Sham 方程。构造用 ASE，推理在 NVIDIA A6000 上。

**2）筛选规模**：构建了 8 种 Ni/Co 基 (oxy)hydroxide 宿主 × 41 种单原子元素 × 13 种吸附位点（edge 01–12 + basal 0001）→ **3,976 个构型模型**；每个构型考虑 \*V、\*OH、\*O、\*OOH 四种中间体 → **超过 15,000 个吸附结构**。

**3）具体计算**：用 MLIP 预测总能和力，配合 BFGS 迭代弛豫到残余最大受力 < 0.03 eV Å⁻¹；再按式 (8)–(11) 把 ML 总能转成吸附能、进而得到各 OER 基元步的能量差，绘制二维火山热图（图 1c）和一维火山图（图 1d）。

**4）产出结论**：从火山图顶点提名两个候选——**W₁–NiFeOOH（预测 η ≈ 0.268 V）和 Ir₁–NiFeOOH（η ≈ 0.254 V）**（Source Data, Figure 1d）；并"重新发现"了 \*OOH 与 \*OH 吸附能之间的线性标度关系，与文献 DFT 趋势吻合（Fig. S10）。GPU 相对 DFT 加速约 **1,158 倍**（CPU 44 倍），即正文所说的"约三个数量级"。

**5）微调（用于迁移性检验）**：只用 M₁–NiNiOOH 子集的 DFT 数据微调 backbone（12 epochs、batch 8、dropout 0.1、AdamW、lr 2×10⁻⁴，A100），用于检验向二元 NiFeOOH 的迁移能力。注意：**主筛选用的是未微调的原始预训练 backbone**。

---

## 二、DFT 做了什么

DFT 在这篇文章里承担三件事，缺一不可：

**1）当"标准答案"（训练/验证标签）**
自建了一个 custom DFT 数据集：从候选空间中挑选对应 4 类代表性活性位点的结构（来自一元 NiOOH 和二元 NiFeOOH，即 Fig. 1b 的四种 motif），既用于**基准测试 ML 模型**，也用于**微调 ML**，还用于**机制研究**。

**2）判定结构与热力学**
- 形成能计算：层内取代的八面体 WO₆ 比基底上锚定的 WO₄ 四面体能量更有利（Fig. S28）——为后面的机制模型定结构。
- Gibbs 自由能图 + 决速步 + 各活性位的 DFT 过电位（图 6c,d，Source Data Figure 6）：
  - Ni–O–Fe bridge（edge，W 为次表层取代）：W₁–NiFeOOH **0.357 V**，NiFeOOH 0.475 V，Ir₁–NiFeOOH 0.581 V；
  - M–O–Ni/Fe bridge（basal）：W 0.700 V、NiFeOOH 0.943 V、Ir 0.962 V。
  - 结论：**暴露的 W–O–Ni/Fe 位点或基底 W 取代位点势垒更高**，说明 W 本身不是活性位，而是"促进剂"；真正的活性位是 edge 面的 Ni–O–Fe bridge。Ir 则相反，锚定的 Ir–O motif 自身就是活性位。
- 自旋态/磁矩分析推断活性位氧化态；PDOS 分析显示 W 取代使 **Ni 3d 带中心上移、与 O 2p 重叠增强**，从而稳定 \*OH→\*O 去质子化步（图 6e,f）。
- 机制区分：W₁–NiFeOOH 走 **Mars-van-Krevelen 晶格氧机制**，Ir₁–NiFeOOH 走 **吸附质演化机制（AEM）**。

**3）解释 ML/实验之间的"不一致"**
ML 认为 Ir（0.254 V）略优于 W（0.268 V），但实验是 W₁–NiFeOOH 更好。作者用额外 DFT 构型（不同羟基化 Ir 锚定方式）来解释：**Ir₁–3O 为 0.310 V，Ir₁–3OH 却高达 0.485 V**（Fig. S52）——真实碱性环境下 Ir 位点构型多样，性能区间被拉宽，从而弥合了这个偏差。

方法学细节：VASP，PAW + PBE，**DFT+U（U_eff: Ni 5.20、Fe 2.56、W 6.20 eV）**，DFT-D3 色散校正，500 eV 截断，Monkhorst-Pack (1×6×4)，真空 ≥ 20 Å + 偶极校正，受力收敛 0.01 eV Å⁻¹。

---

## 三、作者怎么判断 ML 预测"靠不靠谱"

这是论文最讲究的部分，作者搭了**五层交叉验证**：

**① 先自我坦白适用域问题。** 作者明确指出这些吸附构型**不在 OC22 原始训练域内**（out-of-domain），所以不能想当然，必须专门验证。

**② 自建 DFT 数据集做"横向打擂"。** 在同一套 DFT 弛豫数据上对比多种主流 GNN（Source Data Figure S3）：

| 模型 | 加速比 | 吸附能 MAE |
|---|---|---|
| **EquiformerV2-121M-OC22 (GPU)** | **1,158×** | **0.408 eV** |
| GemNet-OC-OC22 (GPU) | 2,382× | 0.482 eV |
| GemNet-dT-OC22 | 3,628× | 0.487 eV |
| PaiNN | 5,369× | 0.833 eV |
| DimeNet++ | 2,701× | 0.865 eV |
| SchNet | 6,496× | 1.971 eV |

给出的判据是**精度–效率权衡**：EquiformerV2 精度最好，同时仍有千倍级加速，故选它作 backbone。

**③ 微调 + 超参搜索 + 定量误差指标。** 用验证集损失挑选超参（Table S1），报告训练/验证损失、验证集与 DFT 的能量 MAE；微调后**总能 MAE < 0.01 eV/atom**，**吸附能 MAE 从 0.408 eV 降到 0.191 eV**（Fig. S4–S7 为 DFT-vs-ML parity plot / 自由能 parity plot）。

**④ 迁移性测试（最关键的可靠性判据）。** 微调只在 M₁–NiNiOOH 上做，然后在**完全没见过的二元 M₁–NiFeOOH 体系**上检验：吸附能 MAE < 0.2 eV，OER 关键基元步能量差的 parity plot 也落在可接受范围（Fig. S8）。这直接回答了"换个组成还准不准"。

**⑤ 物理/化学一致性与独立复核。**
- ML 自己"重新发现"的 \*OOH–\*OH 线性标度关系与既有 DFT 文献一致（Fig. S10）；
- 预测出 NiFeOOH、CoFeOOH 系宿主势垒最低，与先前实验趋势一致（Fig. S9）；
- 最终**用 DFT 独立复算被提名候选的机制与能垒**，结论不依赖 ML；
- 实验闭环：W₁–NiFeOOH 确实提升明显，而 **W₁–Ni(OH)₂ 几乎没提升**（因为 Ni–O–Ni 位点活性低），与"W 只调制 Ni–O–Fe bridge"的位点级预测自洽。

**⑥ 诚实报告局限。** 作者主动承认 ML 给出的 Ir ≈ W 甚至 Ir 略优于 W，与实验排序不符，并用额外 DFT 构型给出解释，而不是回避。

---

## 四、如果要挑刺，值得注意的三点

1. **ML 只用于预筛，不是最终证据**：所有机制结论都建立在 DFT + in situ XAS/Raman 之上。
2. **主筛选用的是未微调 backbone**，而精度更高的微调模型（0.191 vs 0.408 eV）只用于验证迁移性——即"用于筛选的模型"和"证明准确的模型"并非同一个，这是论文自己留下的一个逻辑缝隙。
3. **式 (8)–(11) 是混合方案**：吸附中间体用 E_ML，而 H₂O、H₂ 参考能仍用 E_DFT。因此 ML 误差中混入了 DFT 参考值，纯粹端到端的 ML 误差评估并未给出。

**总结**：ML 干的是"3976 个构型、15000+ 结构的高通量快速弛豫与吸附能估算 → 画火山图提名 W/Ir"；DFT 干的是"造训练/验证标签、算形成能与决速步能垒、算 PDOS 解释电子结构、最终确认 W 是促进剂而非活性位"。ML 可信度则靠 **"自建 DFT 数据集横向基准 → 微调 + parity plot 定量误差 → 未见组成的迁移测试 → 与文献标度关系和实验趋势交叉印证 → DFT 终审"** 这条链条来保证。
````

#### T2-B 最终输出原文

````text
已读完 `materials` 里的正文（PMC/Nature 版）、补充信息 PDF（61 页）、透明同行评审文件和 Source Data 清单。下面按你问的两点回答。

**论文**：Kim et al., *Machine-learning-guided tungsten single atoms promote oxyhydroxides for noble-metal-free water electrolysis*, Nat. Commun. 17, 2344 (2026), doi:10.1038/s41467-026-68735-3。

---

## 一、机器学习做了什么

ML 在这篇论文里只承担一件事：**替代 DFT 做大规模"能量+力"推理，把不可行的组合空间筛成几个候选**。

- **模型**：EquiformerV2（等变 transformer 图神经网络，1.21 亿参数），直接预训练权重来自 OC22 数据集；输入原子构型，直接输出总能与原子受力，不解 Kohn–Sham 方程。
- **候选空间**：K⁺ 插层 γ 相氢氧化物骨架 + 8 种 M_A M_B OOH 载体 × 41 种单原子 M₁ × 13 种吸附位（edge 01–12 + basal 0001），去重后 **3,976 个构型**；每个构型再考虑 \*V、\*OH、\*O、\*OOH 四种中间体，共 **>15,000 个吸附结构**。
- **高通量流程**：用预训练骨干网络在 NVIDIA A6000 上做迭代弛豫（BFGS，收敛判据：残余最大力 < 0.03 eV Å⁻¹），得到吸附能 → 自由能 → 四步 OER 台阶能 → 火山图（Fig. 1c,d）。筛选结论是 **W₁–NiFeOOH 与 Ir₁–NiFeOOH 最有希望**，并结合原料成本分析（Fig. 1e）把含 Ir 的方案排除掉。
- **一次微调**：在自建 M₁–NiNiOOH 小数据集上微调（A100；batch 8、dropout 0.1、12 epochs；AdamW，lr 2e-4，cosine annealing，能量/力损失系数 4/100，梯度裁剪 50，EMA 0.999），目的是检验能否迁移到二元组分。
- 一个容易忽略的细节：**真正用于 3,976 个候选全量筛选的是"未微调的预训练骨干"**，微调模型是用来做精度/迁移性论证的。

## 二、DFT 做了什么

DFT 是"真值来源 + 机制解释"两条腿：

1. **提供 ML 的训练/验证真值**：用 VASP（PAW + PBE，DFT+U：Ni 5.20、Fe 2.56、W 6.20 eV；D3 校正；500 eV 截断；1×6×4 k 点；真空 ≥20 Å、偶极校正；能量 1×10⁻⁵ eV、力 0.01 eV Å⁻¹）弛豫并计算自建数据集，供基准对比。
2. **机制研究（Fig. 6、Supplementary Figs. 49/52）**：对 W₁–NiFeOOH、Ir₁–NiFeOOH、NiFeOOH 做自由能台阶图，定出各活性位点的电位决定步（PDS）与过电位；磁矩/自旋态分析；Ni 3d–O 2p 投影态密度（PDOS）与带中心位置关系；识别 Mars-van-Krevelen（晶格氧）机制。
3. **几何/稳定性判定**：形成能计算说明 W 更倾向于**层内取代的八面体 WO₆**，而不是基面上的 WO₄ 锚定（Supplementary Fig. 28）——这一点后来被 EXAFS/XANES 实验证实。
4. **明确 W 的角色**：W–O–Ni/Fe 暴露位点或基面取代 W 的势垒**高于**原有 Ni–O–Fe 位点，所以 W 不是活性位而是"促进剂"（promoter），真正活性位是 edge 面 Ni–O–Fe 桥位；Ir 则是直接活性位。

## 三、作者怎么判断 ML 靠不靠谱

他们的验证是分层的，可以概括为"**自建 out-of-domain DFT 数据集 + 横向基准 + parity 图 + 迁移性测试 + 物理/实验交叉检验**"：

1. **先承认域外问题**：明确说这 15,000 个几何"不在 OC22 原始训练域内"，所以专门从 NiOOH/NiFeOOH 中挑出四类代表性活性基元（Fig. 1b）构建自建 DFT 数据集。
2. **横向基准选模型**：把 GemNet、PaiNN、DimeNet++、SchNet 等在自建 DFT 弛豫数据集上比较吸附能 MAE 与相对 DFT 的加速比，EquiformerV2 精度最高、约快三个数量级，据此选定骨干（Supplementary Fig. 3）。
3. **parity 图 + MAE/R²**（Supplementary Figs. 5–8）：
   - 总能 parity：未微调基线在 M₁–NiNiOOH 上 Total MAE ≈ 9.28 eV、R² = 0.963；微调后 **Total MAE = 0.201 eV、R² = 1.000**（正文表述为 MAE < 0.01 eV atom⁻¹，是总误差摊到每原子）。
   - OER 台阶能量差 parity（图 b 组）：**微调 EquiformerV2 0.191 eV / R² 0.987**，而基线 EquiformerV2-OC22 0.408 eV / R² 0.950，GemNet 系 0.48–0.69 eV，SchNet 差到 1.971 eV。
   - 分步 MAE（Supplementary Fig. 8）：OH→O 从基线 0.288 降到 0.178 eV；O→OOH 从 0.308 降到 0.165 eV。
4. **迁移性测试**：微调只在 M₁–NiNiOOH 上做，然后直接预测**没见过的二元 M₁–NiFeOOH**，吸附能 MAE < 0.2 eV，用来说明跨组分可迁移。
5. **超参数敏感性**：Supplementary Table 1 系统扫了 dropout（0.0–0.5）、batch size（1/2/4/8）、epoch（1–40），按验证损失与验证能量 MAE 选 ep12_b8_dr0.1。
6. **物理一致性交叉检验**（这是比统计指标更有说服力的部分）：
   - 预测的 \*OOH–\*OH 线性标度关系"重发现"，并与既有 DFT 文献结果吻合（Supplementary Fig. 10）；
   - 筛出的最优载体 NiFeOOH/CoFeOOH 与既有实验趋势一致；
   - 自建 DFST 独立给出的趋势与 ML 火山图一致（W₁ 与 Ir₁ 都是最优）。
7. **实验闭环**：真正合成的 W₁–NiFeOOH 在 half-cell（10 mA cm⁻² 过电位 178 mV，优于 Ir₁–NiFeOOH 183 mV、NiFeOOH 214 mV）和 AEMWE（2.0 V 下 13.1 A cm⁻²，1 A cm⁻² 稳定运行 >500 h）中确实是性能最好的非贵金属阳极之一。

## 四、需要打折扣的地方（如果要复现或评估这套结论）

- **筛选用的是基线模型，而精度论证靠的是微调模型**。基线在 OER 台阶能上的 MAE 是 0.408 eV，与被比较候选之间的差距（如 W 0.26 V vs Ir 0.25 V）同量级；论文没有给出微调模型在整个 M₁–M_A M_B OOH 空间上的校验。
- **验证域较窄**：自建 DFT 集只覆盖 4 个代表性活性基元和 NiOOH/NiFeOOH 两种载体，而筛选空间含 Co–Fe、Ni–Mn、Co–Mn 等 8 种载体；微调训练集只有 M₁–NiNiOOH。
- **DFT 与实验存在一处未完全消解的张力**：DFT 给出 Ir₁–NiFeOOH 的过电位 0.310 V 低于 W₁（Ir 的 3OH 构型是 0.485 V），但实验上 W₁–NiFeOOH 更好；作者用"锚定位点配位环境敏感性"来解释，属于事后调和而非独立预测。
- **U 值敏感性没有做**：同行评审明确要求说明 Ni/Fe/W 的 U 值并讨论小幅变化是否影响结论；最终稿只在 Methods 报了 U 值（5.20 / 2.56 / 6.20 eV），我没在正文或补充信息中找到 U 值扰动测试。此外该评审文件显示稿件此前已在别的期刊审过、Nat. Commun. 未再送审，所以这些问题并非都被重新核验过。
- 一个小的一致性瑕疵：正文 Fig. 6 说明文字在描述 W 取代调控电子结构时误引了 "Fig. 6d"，实际对应的是 Fig. 6e 的 PDOS。属编辑性错误，不影响结论。

**一句话总结**：ML 负责在 ~4,000 个构型、>15,000 个吸附结构中快速算能量与力、搭出火山图挑出 W₁–NiFeOOH；DFT 负责造训练真值、独立算机制与过电位、判定 W 的取代构型和"促进剂而非活性位"的角色。ML 可信度主要靠在自建 out-of-domain DFT 数据上的 parity/MAE/R²、多模型横向基准、跨组分迁移测试，以及标度关系、载体趋势与最终电化学/原位谱学实验的多重交叉印证；但"顶筛仍用基线模型、验证域偏窄、~0.2–0.4 eV 误差与候选间 ~0.01–0.1 V 差距同量级"是它最主要的可信度边界。
````

#### T2-C 最终输出原文

````text
我把 `materials/` 里的正式版正文、SI、源数据和同行评审文件都过了一遍。下面按"读到的原文+定位"来答，凡是我不确定或材料里没写的，单独标出来。

**材料版本**：Kim et al., *Nat. Commun.* **17**, 2344 (2026), doi:10.1038/s41467-026-68735-3 —— `nature-article.pdf`（13 页正式版）、`pmc-fulltext.html`（PMCID PMC12979610）；SI 为 `supplementary-information.pdf`（61 页）；`peer-review-file.pdf` 注明该稿"previously reviewed at another journal… considered suitable for publication without further review at Nature Communications"（审稿文件 p.1）。

---

## 一、机器学习做了什么

**定位**：正文 p.2「Machine learning-guided catalyst screening」+ p.11 Methods「Machine learning processes」。

1. **建候选空间**：以已确立的 K⁺ 插层 γ 相羟基氧化物为基底，组合 8 种 M<sup>A</sup>M<sup>B</sup>OOH × 41 种单原子元素 × 13 种吸附位点（edge 01–12 与 basal 0001），去重后得 **3,976 个构型**；每个构型再考虑 *V、*OH、*O、*OOH 四种中间体，共 **>15,000 个吸附结构**。用 ASE 建模。
2. **用预训练 EquiformerV2（OC22）做高通量筛选**：直接由原子构型预测总能量与原子受力，**不解 Kohn–Sham 方程**（正文 p.2 原文：*"predicts total energies directly from atomic structures without solving computationally intensive Kohn–Sham equations"*）。用 BFGS 迭代弛豫到残余力 <0.03 eV Å⁻¹。注意：**实际跑全空间筛选用的是"原始预训练 backbone"**——原文 *"High-throughput screening of all M₁–MAMBOOH candidates was performed using the original pretrained EquiformerV2 backbone model"*（正文 p.2）。
3. **把能量换算成催化指标**：用式 (8)–(11) 把 ML 能量差换算成四步反应步能垒，其中 **H₂、H₂O 的参考能仍取 DFT 值**（p.11 式 8–11）。再画 ΔG<sub>O</sub>–ΔG<sub>OH</sub> 二维火山图、1D 火山图（Fig. 1c,d）、violin 分布（SI Fig. 9）、*OOH–*OH 线性标度关系（SI Fig. 10），并用千元素原料成本做筛选（Fig. 1e）。最终提名 **W₁–NiFeOOH** 与 Ir₁–NiFeOOH，其中 W₁–NiFeOOH 是唯一的非贵金属候选。
4. **微调**：只用 M₁–NiNiOOH 子集微调（batch 8、dropout 0.1、12 epochs、AdamW、lr 2e-4、能量/力权重 4/100；推理 A6000、训练 A100），目的是检验保真度与跨组分可迁移性（不是用于最终筛选）。

## 二、DFT 做了什么

**定位**：p.7–8「Mechanistic insights from DFT calculations」、Fig. 6、p.11 Methods「DFT calculations」、SI Fig. 28/49/52。

1. **造验证数据集（这是 DFT 在 ML 流程里的第一职责）**：因为候选空间是 OC22 训练域之外（*"not included in the original OC22 training domain"*），作者针对 Fig. 1b 中四类代表性活性位做 DFT 弛豫，构成 custom DFT 数据集，用于**基准测试 + 微调 + 机制研究**（p.2；SI Fig. 2）。
2. **基准/对标参考**：GemNet、PaiNN、DimeNet++ 等模型的吸附能 MAE 和相对 DFT 的加速比都以该 DFT 数据为真值（SI Fig. 3）。
3. **结构归属的独立计算**：形成能计算表明 W 更倾向**层内取代的八面体 WO₆** 而非基面锚定的 WO₄ 四面体（p.5；SI Fig. 28），支撑 EXAFS 的结论。
4. **机制计算**（这是 DFT 的主战场）：自旋极化 PAW-PBE-VASP，**DFT+U**（U<sub>eff</sub>：Ni 5.20、Fe 2.56、W 6.20 eV），DFT-D3，500 eV 截断，(1×6×4) k 点，偶极修正，力收敛 0.01 eV Å⁻¹。产出：
   - 磁矩/自旋态指认活性位氧化态（Fig. 6b）；
   - W₁–NiFeOOH 与 Ir₁–NiFeOOH 的 OER 路径（前者 Mars-van-Krevelen 晶格氧机制，后者 AEM 吸附质演化机制）；
   - ΔG 自由能图与各活性位过电位（Fig. 6c,d）；
   - PDOS：Ni 3d 带中心上移、与 O 2p 重叠增强（Fig. 6e,f）。
5. **和实验互证/修正**：TMAOH 处理与 pH 依赖动力学佐证晶格氧参与；对 Ir 补算多种羟基化锚定构型（Ir₁–3O：η=0.310 V；Ir₁–3OH：η=0.485 V），以解释"DFT 与实验中 W 优于 Ir"的表观矛盾（p.8；SI Fig. 52）。

## 三、作者怎么判断 ML 靠不靠谱

证据链分五层，从"模型对模型"到"模型对实验"：

| 层次 | 做法 | 关键数字（读自原文/SI） |
|---|---|---|
| ① 域外意识 | 承认候选空间超出 OC22 训练域，另建 DFT 数据集 | 3,976 构型 / >15,000 吸附结构，标注为 out-of-domain |
| ② 横向基准 | 在自建 DFT 弛豫数据上比 GemNet、PaiNN、DimeNet++、SCN、SchNet 等 | EqV2-121M-OC22 吸附能 MAE **0.408 eV**，GPU 加速 **1158×**（≈三个数量级）；CPU 44×（SI Fig. 3, p.4） |
| ③ 微调 + 超参验证 | 用 validation loss / DFT energy MAE 选超参 | 选中 ep12_b8_dr0.1：validation energy MAE **0.182 eV**、DFT energy MAE **0.201 eV**（SI Table 1, p.54） |
| ④ Parity（ML vs DFT） | 总自由能 parity：M₁–NiNiOOH（同域）与 M₁–NiFeOOH（异域） | 微调后 **0.201 eV, R²=1.000**（同域）；含 NiFeOOH 时 **1.442 eV, R²=0.999**；基线同图 9.3–12.5 eV（SI Figs. 5,6, p.6–7）。反应步能 ΔE parity：微调 **0.191 eV, R²=0.987**，基线 0.408–0.717 eV（SI Fig. 7, p.8） |
| ⑤ 可迁移性 | 只用 M₁–NiNiOOH 微调，在**未见过的** M₁–NiFeOOH 上测 | 关键步 MAE：OH→O **0.178 eV**（R²=0.755）、O→OOH **0.165 eV**（R²=0.833）；基线 0.288–0.327 eV（SI Fig. 8, p.9）。正文表述：*"achieved adsorption energy MAEs below 0.2 eV for unseen binary M₁–NiFeOOH systems"* |
| ⑥ 物理合理性交叉检验 | ML 是否重现已知规律 | *"A linear scaling relation for predicted \*OOH and \*OH adsorption energies was rediscovered, closely aligning with previous DFT-derived results"*；且 *"NiFeOOH and CoFeOOH-based systems consistently exhibited the lowest average energy barriers… in agreement with trends reported in previous experimental studies"*（p.2） |
| ⑦ 实验终检 | 合成被提名的 W₁–NiFeOOH 及 W₁–Ni(OH)₂、Ir₁–NiFeOOH 等对照，测 OER/AEMWE | W₁–NiFeOOH onset 178 mV @10 mA cm⁻²（W₁–Ni(OH)₂ 反而弱于 NiFeOOH），AEMWE 2.0 V 下 13.1 A cm⁻²、500 h 稳定；原位 XAS/Raman 支持"W 是促进剂而非活性位、Ir 是活性位"的分工 |

值得一提的还有 DFT 层面的独立复核：Fig. 6c,d 用 DFT 重新算了 PDS 能垒，结论 *"W atoms themselves are not the primary active sites but rather act as promoters"*，与 ML 火山图选出的 Ni–O–Fe 边缘位一致。

## 四、阅读备注（按"读到 / 推断 / 材料未说明"分层）

- **读到**：ML 与 DFT 都有实打实的验证环节，且审稿文件确认 *"the benchmark comparisons are appropriate, and validation against DFT is clearly shown in the updated Supplementary parity plots."*（审稿文件 p.1）
- **推断（我的判断，非原文结论）**：ML 的"可靠性"实质是**对 DFT 的保真度**——所有 MAE/parity 的参照物都是 DFT，而 DFT 本身的可靠性靠实验与文献趋势间接支撑；真正把 ML 从"自洽"推到"可用"的是第 ⑦ 层实验（而且实验验证的只有被提名的少数几个体系，不是全空间）。
- **推断**：主打筛选用的是**预训练 backbone（步能 MAE≈0.408 eV）**，而"<0.2 eV"的好数字来自**微调模型**；两者在论文里被并列陈述，但筛选用的是精度较低的那个。
- **材料未说明**：SI Figs. 5–8 的图题没有交代 parity plot 的点是否 held-out（Fig. 5 所在组分正是微调训练组分），也没有给出按组分拆分的 MAE；Fig. 8 的 0.178/0.165 eV 是把 M₁–NiNiOOH 与 M₁–NiFeOOH 点混在一起算的（图例同时列出两种载体），所以"unseen binary 的 MAE"严格说没有单独报数。这点我无法从现有材料确认。
- **单位对不上的一处**：正文说总能量 MAE *"less than 0.01 eV atom⁻¹"*（p.2），而 SI Table 1 与 parity 图给的是每个结构的"Total MAE"（0.201 eV / 1.442 eV，单位 eV）。用原子数换算数量级上说得通，但**论文没有给出换算所需的原子数**，所以我只能标为"与 per-atom 单位相容，未能直接核对"。
- 另外，Fig. 1d 把 W₁/Ir₁–NiFeOOH 的预测过电位描述为 *"surpassing the universal theoretical limit"*，正文对此没有额外讨论——对于"预测是否可靠"这个问题，这是一处值得追问的物理异常点。

如果你要把这段写进综述/笔记，我建议按"ML 负责排序、DFT 负责真值和机制、实验负责终检"这条主线来组织，并保留上面第 ④ 层的具体数字（0.408 eV vs 0.191 eV、R² 0.99→0.75 的落差）作为可靠性讨论的证据。
````

### T3

#### 三组共同的用户输入原文

````text
所需论文材料位于 materials；可以按需要读取，并使用现有检索工具。

文中最高电流密度和 500 小时稳定性分别是在什么条件下测的？能放在一起比较吗？
````

| 组 | 主会话成功加载的 skill（实际顺序） | 耗时/s | 未缓存输入 | 缓存读取 | 输出（含推理） | 总 token | 请求数（含委派） |
|---|---|---:|---:|---:|---:|---:|---:|
| A | 无 | 83.9 | 28,315 | 522,496 | 8,503 | 559,314 | 20（委派 0） |
| B | `reading-contract` | 107.7 | 34,950 | 642,816 | 14,757 | 692,523 | 19（委派 0） |
| C | `reading-contract` | 133.5 | 50,064 | 1,489,920 | 15,897 | 1,555,881 | 32（委派 0） |

#### T3-A 最终输出原文

````text
## 结论先说

**文中"最高电流密度"和"500 小时稳定性"是两套完全不同条件下的测试，不能直接放在一起当作"同一个工况下的性能"来比较。**把"13.1 A cm⁻² @ 2.0 V"和"稳定 500 h"并列（摘要、讨论中的写法）会给人"器件在 13.1 A cm⁻² 下跑了 500 小时"的错觉，但原文的稳定性测试只有 **1 A cm⁻²**、**60 °C**。

---

## 一、两个数据各自的测试条件

**① 最高电流密度：13.1 A cm⁻² @ 2.0 V**

- 体系：AEMWE 单电池（anode = 电沉积 W₁–NiFeOOH/Ni paper，4.4 cm²；cathode = PtRu/C 1.0 mg cm⁻²；商业 PiperION 20 µm 阴离子交换膜）（Methods "Electrochemical measurements"）
- 电解质/温度：**1 M KOH，80 °C**
- 测试方式：**LSV 极化曲线（扫描）**，**未做 iR 补偿**，电解液流量 10 mL min⁻¹（Fig. 3e 图注；正文"…at 80 °C in 1 M KOH…delivers 13.1 A cm⁻² at an applied cell voltage of 2.0 V"）
- Source data 中 Fig. 3e 该点实测为 13.197 A cm⁻² @ 2.00 V（同一曲线在 2.1 V 处为 16.34 A cm⁻²，但文中采用的标题值是 2.0 V 处的 13.1）
- 同温 60 °C 下同一电极在 2.0 V 只有 **9.55 A cm⁻²**（Supplementary Fig. 41 与 Supplementary Table 6）

**② 500 小时稳定性：1 A cm⁻² @ 60 °C**

- 体系：同一 AEMWE 单电池构型
- 电解质/温度：**1 M KOH，60 °C**
- 测试方式：**计时电位法（恒电流）**，恒流 **1 A cm⁻²**（Fig. 3g 图注："Chronopotentiometric stability test … measured at 1 A cm⁻² and 60 °C"；正文"…in 1 M KOH at 60 °C, achieving stable operation for over 500 h at 1 A cm⁻²"）
- Source data（Fig. 3g）实际记录到 **531 h**，槽压从约 **1.60 V 缓慢升到 1.78 V**

另外，文中还有一个 **200 h 的半电池稳定性**（Supplementary Fig. 37），条件是 1 M KOH、**25 °C**、恒电位 — 这又是第三个不同条件，不要和上面两个混用。

---

## 二、为什么不能放在一起比较

| 维度 | 13.1 A cm⁻² | 500 h 稳定性 |
|---|---|---|
| 温度 | 80 °C | **60 °C** |
| 电流密度 | 13.1 A cm⁻²（峰值，2.0 V） | **1 A cm⁻²**（约峰值的 1/13） |
| 测试类型 | 快速 LSV 扫描极化曲线 | 恒电流长时保持 |
| iR 补偿 | 无 | 无 |
| 时长 | 分钟级 | 531 h |

三点关键问题：

1. **温度不同（80 vs 60 °C）**：温度直接改变动力学、膜电导和传质，80 °C 的极化曲线本身是更"乐观"的条件；60 °C 的数据（9.55 A cm⁻² @ 2.0 V）才是与稳定性测试同温的参照。
2. **负载差一个数量级**：13.1 是扫描峰值，1 A cm⁻² 是稳态负载。稳定性结果**不能证明**该阳极/膜电极在 13.1 A cm⁻²（或 2.0 V、80 °C）下能长期运行。文中也没有给出高电流密度下的耐久性数据。
3. **"500 h 稳定"含有可测衰减**：Fig. 3g 源数据槽压从 1.602 V 升到 1.781 V（约 +0.18 V，≈11%），所以"stable for 500 h"应理解为"未失效"，而非"零衰减"。

**若要与文献横向比较**（Fig. 3f / Supplementary Table 6）：该表已按 **1 M KOH、80 °C、商业膜** 统一列出，13.19 A cm⁻² @ 2.0 V 只在同温条目间可比；把它和 60 °C 或低电流密度长期数据混谈是不成立的。

---

## 三、顺带发现的一处内部不一致（影响可比性）

- Fig. 3e 图注写 AEMWE 极化曲线扫描速率 **10 mV s⁻¹**
- 但 Methods 写的是 **LSV at 50 mV s⁻¹**

两处文字相互矛盾（除非是不同实验）。而快速扫描 + 不做 iR 补偿得到的"13.1 A cm⁻²"对扫描速率和电阻都很敏感，这使得该峰值电流密度在跨文献比较时更需要限定条件。

---

## 四、一句话总结

文中最高电流密度 **13.1 A cm⁻² @ 2.0 V** 是在 **80 °C、AEMWE 单电池、未 iR 补偿的 LSV 扫描**下得到的峰值；**500 h** 是在 **同一电池、60 °C、恒流 1 A cm⁻²** 下得到的耐久性结果。两者温度、电流密度、测试模式都不同，**不能直接比较，也不能据此宣称器件在 13.1 A cm⁻²/2.0 V 下稳定运行 500 h**；公平的对照是同温 60 °C 的 9.55 A cm⁻² @ 2.0 V，以及与稳定性同条件的 1 A cm⁻² 长期负载。
````

#### T3-B 最终输出原文

````text
## 结论先行

**不能。** 这两个数字出自同一套 AEMWE 单电池，但不是同一工况：13.1 A cm⁻² 是 **80 °C 极化曲线**上 2.0 V 处的一个取值点；500 h 稳定性是 **60 °C、恒流 1 A cm⁻²** 下的保持测试。把二者并列成"在 13.1 A cm⁻² 下稳定 500 h"是原文摘要/讨论的表述方式所暗示、但数据并不支持的结论。

---

## 1. 两个数字各自的测量条件（逐项对照）

| 项目 | 最高电流密度 13.1 A cm⁻² | 500 h 稳定性 |
|---|---|---|
| 出处 | 摘要；正文 Fig. 3e 段；Discussion | 摘要；正文 Fig. 3g 段；Discussion |
| 器件 | AEMWE 单电池：W₁–NiFeOOH/Ni paper 阳极（4.4 cm²）‖ 20 µm PiperION ‖ PtRu/C 阴极（1.0 mg cm⁻²） | 同一 AEMWE 单电池 |
| 电解液 | 1 M KOH，流速 10 mL min⁻¹ | 1 M KOH |
| **温度** | **80 °C** | **60 °C** |
| 测量模式 | LSV 极化扫描（1.3–2.1 V），"ten consecutive measurements (n = 10)" | 恒流 chronopotentiometry |
| **负载** | 2.0 V 时 13.1 A cm⁻² | **恒流 1 A cm⁻²** |
| iR | 图注/方法：AEMWE 极化曲线"without iR compensation" | 未说明（Methods 只对极化曲线说明不补偿） |
| 扫描速率 | 图注 10 mV s⁻¹，Methods 写 50 mV s⁻¹（二者不一致） | — |
| 源数据 | 'Figure 3' 表 AL/AM 列：2.0 V → 13.19716 A cm⁻²（SI Table 6 记 13.19） | 'Figure 3' 表 AY/AZ 列：t = 1–531 h，cell voltage 1.602 → 1.781 V |

**逐字引文（已核对原文/PDF）**

- Fig. 3e 图注：*"Polarization curves of the AEMWE electrolyzer in 1 M KOH electrolyte at 80 °C without iR compensation."*
- Fig. 3g 图注：*"Chronopotentiometric stability test of the AEMWE electrolyzer measured at 1 A cm−2 and 60 °C."*
- 正文：*"The long-term durability of the W1–NiFeOOH in AEMWE was further validated in 1 M KOH at 60 °C, achieving stable operation for over 500 h at 1 A cm−2 (Fig. 3g)"*
- 摘要：*"achieves a high current density of 13.1 A cm-2 at 2.0 V and remains stable for 500 hours in alkaline exchange-membrane water electrolysis with commercial membranes."*（摘要这一句**完全没有给温度和电流条件**）

---

## 2. 为什么不能"放在一起比较"

1. **温度不同**：80 °C vs 60 °C。OER/AEMWE 动力学对温度敏感，20 °C 的差别直接影响给定电压下的电流。
2. **负载差约 13 倍**：13.1 A cm⁻² vs 1 A cm⁻²。耐久性只证明了在约 1/13 峰值负载下的稳定性，**没有给出高电流密度下的寿命**。
3. **测试性质不同**：一个是扫描极化曲线上的瞬时取值点（且是 10 次连续测量的平均），另一个是 500+ h 的恒流保持。二者不能互相"背书"。
4. 因此可支持的表述边界是：
   - ✅ "在 80 °C、2.0 V 下达到 13.1 A cm⁻²"；
   - ✅ "在 60 °C、1 A cm⁻² 下稳定运行超过 500 h"；
   - ❌ "在 13.1 A cm⁻² 下稳定 500 h"（文中没有这个实验，80 °C 下也没有长期耐久数据）。
5. 原文 Discussion 的句子 *"achieved a high current density of 13.1 A cm−2 at 2.0 V (80 °C) … with robust operational stability exceeding 500 h"* 把两个不同工况并列在同一句，摘要更是连条件都省去，容易让读者把两者合并理解——这正是需要拆开的地方。

---

## 3. 同一篇中另外几个容易混用的条件（供参照）

- **半电池 200 h 稳定性**（SI Fig. 37）又是第三个工况：1 M KOH、**25 °C**、恒电位 0.54 V vs. Ag/AgCl、**非 iR 校正**。既不同于 500 h 的 AEMWE 条件，也不同于 13.1 A cm⁻² 的条件。
- **"稳定"的判据未给出**：Fig. 3g 源数据显示电压并非持平，而是由 1.602 V 升至 1.781 V（+179 mV）；其中前 ~100 h 上升约 129 mV，之后约 430 h 再升约 51 mV（本行为为我对源数据的计算/derived）。原文只说"stable operation"，未定义衰减判据。
- **扫描速率前后不一致**：Fig. 3e 图注 10 mV s⁻¹，Methods 写 50 mV s⁻¹。
- **"1.56 V 达到 1 A cm⁻²"与 80 °C 源数据不符**：按 'Figure 3' 表 80 °C 数据（1.50 V→0.917、1.55 V→1.646 A cm⁻²），1 A cm⁻² 约在 1.50 V；而 1.56 V 与 60 °C 数据吻合（1.55 V→0.962、1.60 V→1.603，1 A cm⁻² ≈ 1.55 V）。这提示正文该句可能混用了 60 °C 的读数（此插值由我计算，属 derived）。
- **13.1 vs 13.19**：源数据平均值 13.19716 A cm⁻²（±0.057），SI Table 6 记 13.19，正文写 13.1，取整偏低。
- 同一组 80 °C 极化数据在 2.1 V 处为 16.34 A cm⁻²（源数据），文中以 2.0 V 的 13.1 A cm⁻² 作为"最高电流密度"对外表述。

---

## 4. 如果一定要做比较，需要补什么

- 做**同温同负载**的配对：例如在 60 °C 下比较活性与耐久（60 °C、2.0 V 时为 9.55 A cm⁻²，SI Table 6），但研究负载仍是 9.55 vs 1 A cm⁻²，差距依然存在。
- 要主张"高电流密度下耐久"，需要补做接近 13 A cm⁻²（或至少数 A cm⁻² 级）的恒流稳定性测试，并给出衰减判据（如电压上升速率、终点电压或失效时间）。
- 在任何引用/比较中，必须同时写出**温度、电流密度/电压、电解液、膜与阳极基底**；仅引用"13.1 A cm⁻²"或仅引用"500 h"都会丢失使结论成立的条件。

---

**报告分层说明**：以上所有数字与引文均来自本会话打开的 `materials` 文件（pmc-fulltext.txt / nature-article.pdf / supplementary-information.pdf / source-data.xlsx），locator 已在表中标注；两处"由我计算"的插值与漂移量（1 A cm⁻² ≈ 1.50 V/1.55 V、+179 mV 分解）已标为 derived/inferred，非原文结论。原文未给出稳定性测试的衰减判据，也未在 80 °C 下报告长期耐久——这两条是"记录中不存在"，不是我的推断。
````

#### T3-C 最终输出原文

````text
已读取 materials 中的正文（`nature-article.pdf` / `pmc-fulltext.txt` / `nature-landing.txt`）、补充材料、源数据工作簿（`source-data.xlsx`）和同行评审文件，逐条核对如下。所有引文均来自本会话打开的源文件。

## 一句话结论

这两个数字来自**两次条件不同的测量**：13.1 A cm⁻² 是在 80 °C 下由 LSV 极化曲线读到的工作点，500 h 是在 60 °C、1 A cm⁻² 恒流下的耐久性测试。它们可以作为两个独立指标并列报道，但**不能合并成一个性能声明**（不能读成"13.1 A cm⁻² 下稳定 500 h"），也不能当作同一工况下的数据互相比较。

## 两个测量点的实际条件

| | 13.1 A cm⁻²（文中头条数字） | 500 h 稳定性 |
|---|---|---|
| 出处 | Fig. 3e；Results"…delivers 13.1 A cm⁻² at an applied cell voltage of 2.0 V"；源数据 Figure 3 表 AL–AO 列 | Fig. 3g；Results"…achieving stable operation for over 500 h at 1 A cm⁻²" |
| 装置 | AEMWE 单电池（阳极 W₁–NiFeOOH/镍纸，阴极 PtRu/C 1.0 mg cm⁻²，有效面积 4.4 cm²） | AEMWE 单电池（同类构型；**未说明是否为同一片 MEA/同一电池**） |
| 温度 | **80 °C** | **60 °C** |
| 电流/电压 | 施加 2.0 V（无 iR 补偿），读出 13.1 A cm⁻² | **恒流 1 A cm⁻²**（约为前者的 1/13），记录电压 |
| 电解液/膜 | 1 M KOH，10 mL min⁻¹，商用 PiperION 20 µm | 1 M KOH（膜同系列为商用膜） |
| 测量模式 | LSV 极化曲线（图注 10 mV s⁻¹；方法写 50 mV s⁻¹），n=10 连续扫描平均 | 恒电流计时电位（chronopotentiometry），n=1 |
| 源数据实际值 | 2.00 V → 13.19716 A cm⁻²（表中记为 13.19；正文取 13.1） | 1 h → 1.602 V；531 h → 1.781 V（源数据 Figure 3 表 AY/AZ 列，共 507 点） |

引文（published version, Nat Commun 17:2344, 2026）：

- Fig. 3e 图注："Polarization curves of the AEMWE electrolyzer in 1 M KOH electrolyte at 80 °C without iR compensation."
- Fig. 3g 图注："Chronopotentiometric stability test of the AEMWE electrolyzer measured at 1 A cm⁻² and 60 °C."

## 为什么不能放在一起比较

1. **温度差 20 °C，本身就会改变数字。** 同一篇的源数据显示：2.0 V 下 80 °C 为 13.19 A cm⁻²，60 °C 只有 9.55 A cm⁻²（Figure S41 表第 18 行；Supplementary Table 6 也并列列出 13.19/9.55）。也就是说仅温度一项就差约 38%，把 13.1（80 °C）与 500 h（60 °C）放在一起，读者会默认它们同温。
2. **电流密度差约 13 倍。** 耐久性只做到 1 A cm⁻²，文中没有任何接近 13 A cm⁻² 的恒流/恒压耐久数据。因此 500 h **不能**作为"高电流密度下稳定"的证据。
3. **测量模式不同，数字不可互读。** 极化曲线是快速 LSV（非稳态、无 iR 补偿），500 h 是稳态恒流。一个可核对的自洽性问题：60 °C 极化曲线在 1.602 V 时给出约 1.6 A cm⁻²（Figure S41 第 10 行），而恒流 1 A cm⁻² 的起始电压也是 1.602 V（Figure 3 源数据 AY/AZ 首行）——同一工况下两条测量路径相差数十 mV。这说明跨这两种测量方式取数是不可靠的（此为根据源数据的推断，作者未解释该差异；也不能排除是不同 MEA）。
4. **"稳定"没有给出衰减指标。** 源数据显示电压从 1.602 V 单调升到 1.781 V，530 h 内升高约 0.18 V（≈0.34 mV h⁻¹，相对约 11%）；文中只写"stable operation for over 500 h"，未报告衰减速率，也未说明判据。（源数据另有 112–137 h 的数据缺口，row 116→117。）
5. **摘要把两个数字直接并置而不带条件。** 摘要原文："achieves a high current density of 13.1 A cm⁻² at 2.0 V and remains stable for 500 hours…"——不写 80/60 °C，也不写 1 A cm⁻²；正文 Results/Discussion 反而分别写明了 "13.1 A cm⁻² at 2.0 V (80 °C)" 与 "over 500 h at 1 A cm⁻²"。若要引用，应以正文的条件为准，而不是摘要的并置句。
6. **同一电池与否未记录。** Methods 只说电池在 60 和 80 °C 下运行过，没有说 500 h 测试与 13.1 A cm⁻² 极化测试是否用同一片 MEA；因此连"同一器件在不同工况下的表现"这一较弱比较也无法从记录确认。

（另有一组第三个条件下的稳定性：半电池计时电流 200 h，1 M KOH、**25 °C**、0.54 V vs Ag/AgCl、非 iR 补偿，Supplementary Fig. 37。它同样不能与上面两个混用。）

## 补充：文中"最高电流密度"有歧义

- 正文头条是 **13.1 A cm⁻²（@2.0 V）**，这是"在 2.0 V 这一约定电压下"的读数；源数据中该极化曲线实际测到 2.1 V、**16.34 A cm⁻²**（Figure 3 表 AM 列第 20 行），所以"最高"若按测到的最大值应是 16.3 而非 13.1。
- 半电池中最高约 **640 mA cm⁻²**（Fig. 3a 源数据，W₁–NiFeOOH，1.805 V vs RHE）——比 AEMWE 低约 20 倍，也常被混引。
- 另外一处需要留意的记录不一致：Fig. 3e 图注写扫描速率 **10 mV s⁻¹**，而 Methods 的 AEMWE 部分写 **50 mV s⁻¹**。LSV 扫描速率会直接影响极化曲线的表观电流密度，这也是不该把该曲线数值与稳态耐久数据直接对照的原因之一。

## 要能"放在一起"需要什么

- 在同一温度（如 80 °C）、同一电流密度（如 1 或 13 A cm⁻²）下做恒流耐久，并报告电压衰减速率/终止判据；
- 或至少在引用时把 13.1 A cm⁻²（80 °C，2.0 V，LSV，无 iR）与 500 h（60 °C，1 A cm⁻²，恒流）**分别标注条件**，作为"峰值活性"和"某一温和工况下的耐久性"两条独立陈述；
- 与文献对比时（Supplementary Table 6）同样要对齐温度、膜、电解液和取数电压——该表把 80 °C 与 60 °C 的条目混列，本身就说明缺条件标注容易造成误比。

（核对状态：上表与引文均为本会话打开源文件后的读取结果；第 3、4 点中的差值/速率是按源数据做的算术推断，已在文中标注为推断。全文搜索范围内，作者未在任何位置报告 13 A cm⁻² 级别的耐久性数据。）
````

### T4

#### 三组共同的用户输入原文

````text
所需论文材料位于 materials；可以按需要读取，并使用现有检索工具。

帮我找几篇 2026 年 1 月 29 日以前，用钨改善 NiFe 氢氧化物或氧羟化物析氧性能的论文，最多五篇，给我 DOI 和每篇主要做了什么。
````

| 组 | 主会话成功加载的 skill（实际顺序） | 耗时/s | 未缓存输入 | 缓存读取 | 输出（含推理） | 总 token | 请求数（含委派） |
|---|---|---:|---:|---:|---:|---:|---:|
| A | 无 | 711.1 | 40,294 | 1,506,432 | 26,634 | 1,573,360 | 39（委派 0） |
| B | `paper-lookup` | 1386.1 | 82,037 | 4,831,744 | 51,461 | 4,965,242 | 64（委派 0） |
| C | `paper-lookup` → `literature-search-openalex` | 432.2 | 75,786 | 1,889,280 | 37,689 | 2,002,755 | 27（委派 0） |

#### T4-A 最终输出原文

````text
已核验完毕。说明一下：你给的材料里那篇 Nature Communications 论文（W₁–NiFeOOH，DOI 10.1038/s41467-026-68735-3）恰好发表于 **2026-01-29**，按"1月29日以前"的界限属于边界、不作为答案列出。下面 5 篇都是此前已在线发表、且主题就是"用 W 改性 NiFe 氢氧化物/氧(氢)氧化物以提升 OER"的工作（DOI 与在线日期已用 Crossref / OpenAlex / Unpaywall 交叉核验）。

---

**1. Constructing Ultrathin W-Doped NiFe Nanosheets via Facile Electrosynthesis as Bifunctional Electrocatalysts for Efficient Water Splitting**
*ACS Appl. Mater. Interfaces* 2021, 13(17), 20070–20080；在线 2021-04-26
DOI: **10.1021/acsami.1c01815**
主要工作：室温常压下一步电沉积制备超薄 W 掺杂 NiFe-LDH（NiFeW）纳米片，用作全解水双功能催化剂。W 掺杂既调形貌又调 NiFe 氢氧化物电子结构、加速电荷转移；OER 过电位 239 mV@10 mA·cm⁻²，HER 115 mV，双功能电解槽 1.59 V@10 mA·cm⁻²，优于 IrO₂/Pt。

**2. Efficient electrocatalysis for oxygen evolution: W-doped NiFe nanosheets with oxygen vacancies constructed by facile electrodeposition and corrosion**
*Chem. Eng. J.* 2023, 452, 139104；在线 2022-09-09
DOI: **10.1016/j.cej.2022.139104**
主要工作：电沉积 + 化学腐蚀在泡沫镍上直接生长含氧空位的 W 掺杂 NiFe-LDH 纳米多孔电极。适量 W 改变 Ni、Fe 局域环境并优化氧空位浓度，增加表面 OER 活性位；代表样品过电位 211 mV@10 mA·cm⁻²，Tafel 斜率 36.44 mV·dec⁻¹，稳定运行 120 h 以上。

**3. Tungsten-Doped NiFe-Layered Double Hydroxides as Efficient Oxygen Evolution Catalysts（钨掺杂镍铁水滑石高效电催化析氧反应）**
*Acta Phys.-Chim. Sin.* 2024, 40(1), 2303055；在线 2023-08-21
DOI: **10.3866/PKU.WHXB202303055**
主要工作：一步醇热法可控掺 W 制得 NiFeW-LDH，W 以 +6 价存在且无 W 基纳米颗粒杂相；XPS 显示 Fe 结合能正移、表面吸附 OH 增多，说明 Fe–W 间发生电子重分布。DFT 表明 W(VI) 促进 H₂O 与 O* 中间体吸附并活化 Fe 位点；1 M KOH 中过电位 199 mV@10 mA·cm⁻²、237 mV@100 mA·cm⁻²。

**4. Electronic and Interfacial Engineering via Tungsten Incorporation for Robust Overall Water Splitting and Seawater Electrolysis**
*ACS Appl. Mater. Interfaces* 2026, 18(3), 5263–5278；在线 2026-01-10（纸质 2026-01-28）
DOI: **10.1021/acsami.5c20762**
主要工作：一锅水热在泡沫镍上原位生长富氧空位的 W 掺 NiFe-LDH（NiFeW-LDH@NF）。W 引入调控电子结构、提高氧空位浓度、改善水分子吸附，从而同时提升 OER/HER 动力学；OER 325 mV、HER 356 mV@100 mA·cm⁻²，全解水槽压 1.646 V、海水电解 1.693 V，DFT 给出 d 带中心位移与中间体吸附能解释。

**5. W-induced reconstruction of NiFe (oxy)hydroxides with abundant O-vacancies as efficient electrocatalysts for water oxidation**
*Fuel* 2026, 406, 136945；在线 2025-09-27
DOI: **10.1016/j.fuel.2025.136945**
主要工作：在 WO₄²⁻/Cl⁻ 体系中对商用镍铁泡沫原位电化学刻蚀重构，生长出 NiFeW 复合(氧)氢氧化物纳米片组装微球（NiFeW/NFF）。W 引入调节内部电子结构；OER 过程中 W 自发牺牲性溶出，原位生成大量氧空位和 Ni/FeOOH 活性位，剩余 W 通过增强 Ni/Fe–O 共价性进一步优化电子结构。1 M KOH 中过电位 243 mV@10 mA·cm⁻²，优于商用 RuO₂-IrO₂，稳定 500 h。

---

**一点说明**
- 第 5 篇（Fuel）卷期标注为 2026 年 2 月，但 2025-09-27 已在线发表，故满足"2026-01-29 以前"；第 2、3 篇同理为"在线早于卷期"。
- 另外还有若干高度相关但被你"最多五篇"限制排除的候选，例如 W 掺杂绣球状 NiOOH/FeOOH（*Int. J. Hydrogen Energy* 2025, DOI 10.1016/j.ijhydene.2025.151465）和 P–W 双掺 NiFe-LDH 纳米球（*J. Alloys Compd.* 2025, DOI 10.1016/j.jallcom.2025.185348）；如果需要我可以再展开。
- 核验来源：[Acta Phys.-Chim. Sin. 原文页](https://www.whxb.pku.edu.cn/EN/Y2024/V40/I1/2303055)、[KIST 机构库 CEJ 记录](https://pubs.kist.re.kr/handle/201004/114188?mode=simple)、[Fuel 论文中文解读](https://www.ebiotrade.com/newsf/2025-9/20250928083223705.htm)、[ACS AMI 2026 论文记录](https://pubs.acs.org/doi/10.1021/acsami.5c20762)。
````

#### T4-B 最终输出原文

````text
## 结论：5 篇用 W 改善 NiFe 氢氧化物/氧羟化物 OER 的论文（均早于 2026-01-29）

先说锚点：`materials/` 里那篇是 **Nat. Commun. 2026-01-29**（W₁-NiFeOOH，DOI `10.1038/s41467-026-68735-3`），本身就是 1 月 29 日发表，按"早于 1 月 29 日"不入选。

| # | DOI | 期刊/年 | 主要做了什么 |
|---|---|---|---|
| 1 | **10.1039/d0ta00691b** | J. Mater. Chem. A, 2020, 8, 8096–8103 | 简便水浴法合成"纳米颗粒堆叠"的 **W 掺杂 NiFe-LDH**（Ni–Fe–W LDH）纳米片，作高效水氧化催化剂；最早把 W 掺入 NiFe-LDH 的工作之一，被引 120+ |
| 2 | **10.1021/acsami.1c01815** | ACS Appl. Mater. Interfaces, 2021（在线 04-26） | 室温常压一步电沉积制备**超薄 W 掺杂 NiFe-LDH 纳米片**；W 同时调形貌和电子结构。OER 239 mV@10 mA cm⁻²、HER 115 mV，全解池 1.59 V@10 mA cm⁻²（比 IrO₂‖Pt 低 110 mV） |
| 3 | **10.1016/j.cej.2022.139104** | Chem. Eng. J., 2023, 452, 139104（在线 2022-09-09） | "电沉积+化学腐蚀"在泡沫镍上直接生长**含氧空位的 W 掺杂 NiFe-LDH**；W 调控 Ni/Fe 电子结构并优化氧空位浓度。OER 211 mV@10 mA cm⁻²、Tafel 36.44 mV dec⁻¹、>120 h 稳定 |
| 4 | **10.1002/smll.202311431** | Small, 2024, 20, 2311431 | 将**钨酸根 WO₄²⁻ 插层**进 NiFe-LDH；提升动力学与抗 Cl⁻ 选择性，碱性海水 O₂ 效率≈100%，1000 mA cm⁻² 运行 350 h 仅痕量活性氯，OER 走晶格氧机制（LOM） |
| 5 | **10.1021/acsami.5c20762** | ACS Appl. Mater. Interfaces, 2026, 18, 5263–5278（在线 01-10，纸本 01-28） | 一锅水热把 **W 引入富氧空位 NiFe-LDH/泡沫镍**（NiFeW-LDH@NF）；OER 325 mV、HER 356 mV@100 mA cm⁻²，全解水 1.646 V、海水电解 1.693 V，DFT 给出 d 带中心位移 |

**简要补充（未计入这 5 篇）：** `10.1016/j.nanoen.2020.105540`（W 调控分级 FeNi-LDH 氧空位，Nano Energy 2021，被引 145+）、`10.3866/pku.whxb202303055`（一步醇热 W 掺杂 NiFeW-LDH + DFT，Acta Phys.-Chim. Sin. 2024）、`10.1021/acscatal.5c05106`（W/S 共掺 NiFe-LDH，AEMWE 5 A cm⁻²@2.06 V、600 h，2025-09-16）、`10.1016/j.mtchem.2022.101369`、`10.1039/d0se00205d`、`10.1016/j.mcat.2025.115239`、`10.1016/j.fuel.2025.136945`（在线 2025-09-27，但期卷 2026-02，日期口径敏感）。

**特意排除的对口"近失"工作：** `10.1021/acscatal.5c07061`（"Impact of Solid Solution of Tungsten on Nickel–Iron Hydroxide OER Catalysts"）主题完全对口，但 Crossref/OpenAlex 显示在线发表 **2026-02-06**，晚于 1 月 29 日。另排除 W 掺杂 NiFe-MOF（`10.1016/j.ijhydene.2024.04.355`）和 WO₃₋ₓ/NiFe-LDH 尿素氧化（`10.1007/s42864-024-00267-z`）。

**检索与核实出处（访问日期 2026-10-10）**：Crossref `/works?query.title=…&filter=until-pub-date:2026-01-28` 标题扫描（400+ 命中后按 W/NiFe/OER 词根本地过滤）→ OpenAlex `/works/doi:…` 与 Semantic Scholar `/paper/DOI:…` 核定标题/日期/引用 → Unpaywall 查 OA → OpenAIRE 与出版社页面补齐摘要。注意 OpenAlex 的列表/搜索接口返回 HTTP 429（当日额度），故筛选主要依赖 Crossref 标题检索。

完整清单、摘要依据与原始响应留存在 `artifacts/literature-findings.md` 和 `artifacts/*.json`（`sweep_titles.json`、`cr_meta.json`、`verify_dois.json` 等）。
````

#### T4-C 最终输出原文

````text
## 结论

在 2026-01-29 之前，用钨（W）提升 NiFe 氢氧化物/氧羟氧化物析氧（OER）性能的工作，我筛出下面 5 篇（按时间排序，均已核对 DOI、期刊、日期与摘要原文）。

> 你给的 `materials/` 里正是那篇边界论文本身：*Machine-learning-guided tungsten single atoms promote oxyhydroxides for noble-metal-free water electrolysis*, Nat. Commun. 17, 2344 (2026)，DOI [10.1038/s41467-026-68735-3](https://doi.org/10.1038/s41467-026-68735-3)，**2026-01-29 发表**。因为它不满足"1 月 29 日以前"，所以被排除在下面 5 篇之外。

---

### 1. 10.1021/acs.inorgchem.9b01953
**Self-Supported Porous Ni–Fe–W Hydroxide Nanosheets on Carbon Fiber: A Highly Efficient Electrode for Oxygen Evolution Reaction**
*Inorganic Chemistry*, 2019-09-11（被引约 34）

把 W 掺进 NiFe 层状双氢氧化物，在碳纤维上原位长出多孔自支撑 Ni–Fe–W 氢氧化物纳米片。最佳 Ni:Fe:W = 6:2:1；W 以 W⁶⁺ 存在，促进电荷转移、降低吸附 OH⁻ 转化为 O 自由基的势垒。最优电极在碱性电解液中 η₁₀ = 264 mV，10 h 后电位仅上升 1.6%。

### 2. 10.1039/d0ta00691b
**Facile synthesis of nanoparticle-stacked tungsten-doped nickel iron layered double hydroxide nanosheets for boosting oxygen evolution reaction**
*Journal of Materials Chemistry A*, 2020（被引约 121，是该方向引用最高的 W–NiFe LDH 工作之一）

用简便水浴反应合成"纳米颗粒堆叠"的 W 掺杂 Ni–Fe–W LDH 纳米片，作为高效水氧化催化剂。（注：RSC 在 Crossref/OpenAlex 只登记了一句话摘要，因此这里不虚构其具体过电位数值。）

### 3. 10.1002/cssc.202002544
**Electrodeposited Trimetallic NiFeW Hydroxide Electrocatalysts for Efficient Water Oxidation**
*ChemSusChem* 14, 1324–1335, 2021-01-21（被引约 57）

在三维泡沫镍上阴极电沉积 W 掺杂 Ni–Fe 氢氧化物。适量 W 改变 Ni、Fe 局域环境并制造氧空位，产生大量活性位。最优催化剂 η₁₀ = 224 mV、η₅₀ = 251 mV，Tafel 斜率很低，性能超过 20 wt% Ir/C；约 30 h 计时电位测试后 W 发生还原，起到稳定 Ni/Fe 活性位的作用。

### 4. 10.1002/smll.202311431
**Tungstate Intercalated NiFe Layered Double Hydroxide Enables Long-Term Alkaline Seawater Oxidation**
*Small* 20, e2311431, 2024-02-16（被引约 74）

换了一条"插层"路线：把 WO₄²⁻ 作为客体插进 NiFe LDH 层间。插层后反应动力学与选择性提升，碱性海水中 O₂ 生成效率接近 100%；在 1000 mA cm⁻² 下运行 350 h 后电解液中仅检出痕量活性氯。机理上 OER 遵循晶格氧机制（LOM）。

### 5. 10.1016/j.jcis.2025.01.012
**Phase regulation of Ni(OH)₂ nanosheets induced by W doping as self-supporting electrodes for boosted water electrolysis**
*Journal of Colloid and Interface Science* 684, 1–10, 2025（被引约 63）

用一步腐蚀工程在泡沫镍上制备 W 掺杂 NiFe LDH（NiFe-Wₓ/NF）。大原子半径的 W 改变 Ni(OH)₂ 晶面生长，促成像相 α-Ni(OH)₂，层间距变大；W⁶⁺ 从邻近 Ni 抽电子。结果是更易形成高价 γ-NiOOH，加速 OER 动力学：η₁₀₀ = 269 mV，全解水 1.90 V 下可达 780 mA cm⁻²，100 mA cm⁻² 稳定运行超过 70 h。

---

### 备选（不计入上面的 5 篇）
若想再扩展，以下几篇同样切题且都在 2026-01-29 之前：
- 10.1021/acsami.1c01815（2021，一步电沉积超薄 W 掺杂 NiFe LDH，双功能，η_OER = 239 mV）
- 10.1016/j.cej.2022.139104（2023，电沉积+腐蚀制 W 掺杂 NiFe LDH，富氧空位，η₁₀ = 211 mV）
- 10.3866/pku.whxb202303055（2024，一步醇热法 W 掺杂 NiFe-LDH，W⁶⁺ 与 Fe 间电子重分布）
- 10.1016/j.cej.2021.130768（2021，NiFeW LDH 的稳定性与活性）
- 10.1038/s41467-019-09845-z（2019，W 单原子掺杂 α-Ni(OH)₂——不含 Fe，但常被视为"W 单原子提升镍氢氧化物 OER"的经典前作）
- 10.1021/acsami.5c20762（2026-01-10，NiFeW-LDH，仍在截止日之前）

---

### 检索记录与局限
- **检索库**：[Crossref](https://api.crossref.org/works)（标题/文献检索 + 单条 DOI 元数据、被引数）、[Europe PMC](https://www.ebi.ac.uk/europepmc/webservices/rest/search)（题录+摘要+全文关键词）、OpenAlex（单条 work 查询；批量检索额度当日已耗尽）、[Unpaywall](https://api.unpaywall.org/v2/)（OA 状态）。
- **未能使用**：OpenAlex 批量检索（无 API key，共享免费额度为 0，返回 429）、Semantic Scholar（无 key，持续 429）；ScienceDirect 与 RSC 页面被反爬拦截（403），故部分摘要改由 Europe PMC、Crossref、机构库（如 [KIST](https://pubs.kist.re.kr/handle/201004/114188)）获取。
- **截止条件**：所有入选文献的 online/issued 日期均早于 2026-01-29；分别在 Crossref/Europe PMC 中逐条核对了刊名、卷页与日期。
- **检索词**覆盖了 `tungsten / W-doped / W doping / tungstate / NiFeW / Ni–Fe–W` 与 `NiFe (oxy)hydroxide / LDH / layered double hydroxide / oxygen evolution` 的组合，并做了交叉库补充，因此上面的清单应已覆盖该主题的主要工作；若你需要"只列 5 篇、不要备选"，或要我把这 5 篇的 PDF/OA 链接与关键电化学数据整理成表格，我可以继续。
````

### T5

#### 三组共同的用户输入原文

````text
所需论文材料位于 materials；可以按需要读取，并使用现有检索工具。

这篇论文的新意主要在哪里？和 2026 年 1 月 29 日以前的相关工作比，哪些是新的，哪些是已有思路？
````

| 组 | 主会话成功加载的 skill（实际顺序） | 耗时/s | 未缓存输入 | 缓存读取 | 输出（含推理） | 总 token | 请求数（含委派） |
|---|---|---:|---:|---:|---:|---:|---:|
| A | 无 | 363.9 | 188,945 | 6,978,560 | 109,265 | 7,276,770 | 141（委派 80） |
| B | `lit-review` | 1291.2 | 601,023 | 24,686,464 | 301,299 | 25,588,786 | 323（委派 252） |
| C | `lit-review` → `paper-lookup` | 1097.8 | 1,143,030 | 62,039,552 | 456,376 | 63,638,958 | 630（委派 531） |

T5 还需计入子会话加载：
- A：无已记录的 skill 加载。
- B：`lit-review` × 5、`reading-contract` × 2、`paper-lookup` × 1。
- C：`lit-review` × 8。

#### T5-A 最终输出原文

````text
# 《Machine-learning-guided tungsten single atoms promote oxyhydroxides…》(Nat Commun 17, 2344, 2026) 的新意分析

**材料依据**：Nature 正文/PMC 全文、Supplementary Information（含 Supplementary Table 5/6 的文献对比）、Transparent Peer Review、Source Data，以及 2026-01-29 之前的文献检索。检索环境中 `web_fetch` 对全部外部域名不可用（返回“non-public IP”），因此文献的“标题/期刊/年份/DOI”来自检索命中，个别数字在文中标注为未核实。

---

## 0. 先明确时间基准

论文信息：收稿 2025-10-14，接收 2026-01-14，**发表 2026-01-29**，DOI [10.1038/s41467-026-68735-3](https://www.nature.com/articles/s41467-026-68735-3)。按用户口径以 **2026-01-29** 为界；但严格说，论文的内容在 2025 年 10 月投稿时已定型，所以“新意”实质上应对比 **2025 年秋以前**的文献。

---

## 1. 一句话结论

**这篇论文的新意主要不是“新原理”，而是“新集成 + 新数据点 + 一次较完整的机理指认”。** 它把四个在 2026 年前都已成熟的思路（GNN 势函数高通量筛选、W 掺 NiFe 氢氧化物 OER、α→γ 相变/晶格氧机理、高价掺杂调制 Ni 氧化）拼成一个端到端工作流，得到一个具体的材料—器件数据点（2.0 V 下 13.1 A cm⁻²、500 h）。**真正在概念层面可能算新的，只有一条：用同一套原位谱学把“取代型 W = 促进剂（价态不随电位变化）”与“锚定 Ir = 直接活性位（价态随电位上升）”在同一体系里对照指认出来。** 其余基本是 2019–2025 已有思路的再组合、放大和工程化；论文对若干直接相关的 W 掺 NiFe 最新文献引用不足，其“benchmark”表述（尤其耐久性）偏强。

---

## 2. 把论文拆成四个可检验的“新意主张”

| 编号 | 主张 | 关键证据 |
|---|---|---|
| **C1 方法** | 用预训练 EquiformerV2（OC22）做 out-of-domain 吸附能预测，从 8 种 MAMB OOH × 41 种单原子 × 13 类吸附位 = **3,976 个构型**（>15,000 个吸附结构）中选出 W₁‑NiFeOOH（以及 Ir₁‑NiFeOOH） | Fig. 1；Supplementary Figs. 1–12 |
| **C2 材料** | CV 循环电沉积一步制备**原子分散、取代式八面体 WO₆** 的 W₁‑NiFeOOH（W 2.6 at.%，无 W–W 键） | Fig. 2；HAADF‑STEM/EXAFS/XANES |
| **C3 性能** | 半电池 178 mV@10 mA cm⁻²；AEMWE 80 °C：1.56 V@1 A cm⁻²、**2.0 V 下 13.1 A cm⁻²**；60 °C 下 **500 h@1 A cm⁻²** | Fig. 3；Supplementary Tables 5, 6 |
| **C4 机理** | 原位 XAS：W 价态几乎不变（+5.07→+5.11），而 Ni 更早/更深氧化；原位 Raman：α→γ 相变提前（1.43 V vs 1.45 V）；DFT：取代 W 是**促进剂**，活性位仍是 Ni–O–Fe 边面桥位，走 MvK 晶格氧路径；对照的锚定 Ir 才是直接活性位 | Figs. 4–6；Supplementary Figs. 43–52 |

---

## 3. 逐条对照 2026-01-29 前的文献

### C1（ML 筛选）：**方法学上属于已有思路的集成，不是新能力**

- OC20/OC22 本身就是**为氧化物电催化（含 OER 中间体）设计**的数据集（[Tran et al., ACS Catal. 2023](https://pubs.acs.org/doi/10.1021/acscatal.2c05426)）；EquiformerV2 是 2024 年现成的 SOTA 模型（[Liao et al., ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ab12e8f3443c1a789f595b18d8c597b4-Abstract-Conference.html)）；AdsorbML 2023 已把 GNN 当作吸附能计算加速器（[npj Comput. Mater. 9, 203](https://www.nature.com/articles/s41524-023-01121-5)）。
- “用 ML 预测单原子催化剂 OER 过电位”可追溯到 **iScience 2021**（[10.1016/j.isci.2021.102398](https://www.sciencedirect.com/science/article/pii/S2589004221003667)）；2024 年 *The Innovation (Materials)* 有“ML fast exploration of stable and active SACs for OER”（[链接](https://the-innovation.org/article/doi/10.59717/j.xinn-mater.2024.100072)）；2025 年 *Accounts of Materials Research* 筛了 261 个 metal-single-atom-on-oxide 候选并排出 η<0.5 V 的若干（[10.1021/accountsmr.5c00319](https://pubs.acs.org/doi/10.1021/accountsmr.5c00319)）；2024 年 *Nanoscale* 已专门“用 OC22 合理设计 OER 氧化物催化剂”（[10.1039/d4nr01390e](https://pubs.rsc.org/en/content/articlelanding/2024/nr/d4nr01390e)）。
- “预测→合成→电化学验证”闭环在 2024–2025 已常态化：Nat. Commun. 2024 的钙钛矿氧化物水氧化（[10.1038/s41467-024-50605-5](https://www.nature.com/articles/s41467-024-50605-5)）、Science Bulletin 2025 的主动学习酸性 OER、IJHE 2025 的 Cu‑Co₃O₄ 等。
- 2D volcano（ΔG_OH vs ΔG_O）源自 Man et al. 2011，与 ML 吸附能结合早已有之。
- **论文自己也承认筛选是“rediscovered”已知规律**：ML 预测的 scaling relation“closely aligning with previous DFT‑derived results”，NiFe/CoFe 最优“in agreement with trends reported in previous experimental studies”。也就是说 ML 主要起**高通量复现/筛选**作用。
- **一个实质软肋**：筛选用的是**未 fine-tune 的预训练模型**，其吸附能 MAE ≈ 0.41 eV（fine-tune 后 0.19 eV，见 Supplementary Fig. 3/4）；而 Fig. 1d 中 W（0.268 V）、Tl（0.271 V）、Rh（0.301 V）之间的过电位差只有 0.01–0.05 V，**远小于模型误差**。“ML 选中 W”的统计置信度并不高——论文始终没有做候选间距 vs 模型误差的论证。

> 判断：**C1 ≈ 90% 已有思路**，新意只在“具体落到单原子-羟基氧化物候选空间 + 规模（3,976/15,000）”。

### C2（W‑NiFeOOH 材料）：**“W 掺 NiFe 氢氧化物/羟基氧化物做 OER”已相当拥挤；新的只是具体实现形态**

在 2026-01-29 前：
- **单原子 W 掺 α‑Ni(OH)₂**，Yan et al., Nat. Commun. 10, 2149 (2019)（[s41467-019-09845-z](https://www.nature.com/articles/s41467-019-09845-z)）——注意：**本文只在 Supplementary Table 5 里把它当性能对照（237 mV），正文完全没有与它“W 是活性位”的结论做机理对照**，这是一个明显的定位缺口。
- **W + Fe 共掺 Ni(OH)₂ 纳米片**，Sustainable Energy & Fuels 2020（[d0se00205d](https://pubs.rsc.org/en/content/articlelanding/2020/se/d0se00205d)）。
- **W 掺杂 NiFe‑LDH 高效 OER**，Acta Phys.-Chim. Sinica 40, 2303055 (2024)（[链接](https://www.whxb.pku.edu.cn/EN/Y2024/V40/I1/2303055)）。
- **Mo、W 单原子共掺表面羟基化 NiFe 氧化物**做全解水，Appl. Catal. B 2024（[S0926337324006702](https://www.sciencedirect.com/science/article/abs/pii/S0926337324006702)）。
- **W 在 NiFe 氢氧化物中的固溶（solid solution）对 OER 的促进**，ACS Catal.（[10.1021/acscatal.5c07061](https://pubs.acs.org/doi/full/10.1021/acscatal.5c07061)），其结论片段明确写道“**W doping lowers the overpotential at the Fe active site**”——与本文“W 促进 Ni–O–Fe/Fe 位”高度重叠（**该文确切发表日期需核实是否早于 2026-01-29**，从 DOI 年份看很可能是 2025 年）。
- W 掺杂 NiFe 纳米片（电沉积+腐蚀，含氧空位，[KIST](https://pubs.kist.re.kr/handle/201004/114188)）；W 掺入用于全解水/海水电解（[ACS AMI 10.1021/acsami.5c20762](https://pubs.acs.org/doi/10.1021/acsami.5c20762)）。

> 判断：**组合本身不新**；可能新的只有“**原子级分散、取代式八面体 WO₆、无 W–W** 的 W₁‑NiFeOOH 这一具体结构 + CV 电沉积一步合成工艺”。这属于**材料实现/工艺层面的增量新意**。

### C3（性能/器件）：**记录性主张需要打折**

- 半电池 178 mV@10 mA cm⁻²：很好，但与已有最好水平相当而非超越——它**自己**的 Supplementary Table 5 里就有 Ir₁/NFS 170 mV、NiVIr‑LDH 180 mV。
- AEMWE 2.0 V 下 13.1 A cm⁻²：论文 Table 6 最强对照是 CAPist‑L1 的 7.35 A cm⁻²@2.0 V（Nat. Catal. 2024）；但**2025 年已有“非贵金属 NiFe 阳极 10 A cm⁻² 持续 800 h”**（Hu/Ma, Angew. Chem. Int. Ed. 64, e202413698，[PubMed](https://pubmed.ncbi.nlm.nih.gov/39363762/)、[Zenodo](https://zenodo.org/records/15287698)）以及“**8000 mA cm⁻² at 2.05 V**”（J. Mater. Chem. A 2025, [d5ta05065k](https://pubs.rsc.org/sq/content/articlelanding/2025/ta/d5ta05065k/unauth)）。因此 13.19 A cm⁻²@2.0 V **至多是一个 ~30% 的边际记录**，强依赖电压归一化、温度、膜和是否 iR 补偿；而且**本文没有引用这两条最接近的记录**。
- 耐久性：**500 h@1 A cm⁻² 远低于已有水平**——800 h@**10 A cm⁻²**（Hu/Ma 2025），以及非贵金属 NiFe 阳极的 **14,000 h** 级结果（Sun 组, Angew. Chem. Int. Ed. 64, e202505924，[PubMed](https://pubmed.ncbi.nlm.nih.gov/40501335/)；该结果的电流密度未核实）。所以摘要中“sets a benchmark for noble‑metal‑free anode catalysts under practical water electrolysis conditions”**在耐久性上是明显的过度陈述**。
- 另外需注意：**“无贵金属”仅指阳极**；阴极是 PtRu/C（含 PGM），对比样 Ir₁‑NiFeOOH 本身含 Ir。
- “surpassing the universal theoretical limit”：Source Data 显示预测 η_W = 0.268 V、η_Ir = 0.254 V，低于 ~0.37 V 的 scaling 极限。这来自**按构型选用的不同 scaling 线**（substituted/bridge 用 ΔG_OOH = ΔG_OH + 3.20），本质是“位点特异性 scaling 让表观 η 越限”，而非打破普适原理；实测 178 mV 低于理论极限也主要是表观（几何）活性与热力学极限不可直接比较所致。

> 判断：**C3 是“数据点/工程优化”层面的贡献，不是概念新意**，且“记录/基准”的措辞需要显著下调。

### C4（机理）：**四个组成要素都是已有思路，唯一可能的新点是其组合式“角色指认”**

- Fe 造 Ni–O–Fe 边面活性位、Fe 调制 Ni：[Friebel et al., JACS 137, 1305 (2015)](https://www.osti.gov/biblio/1571037)；[Dionigi et al., Nat. Commun. 11, 2522 (2020)](https://www.osti.gov/pages/biblio/1904487)。**已有**。
- α→γ 相变、K⁺ 插层、原位 Raman 474/553 vs 455/525、Ni K‑edge XANES 追踪：[Klaus et al., JPCC 2015](https://pubs.acs.org/doi/10.1021/acs.jpcc.5b00105)；Trześniewski JACS 2015；Görlin JACS 2017；[Bai et al., Nat. Commun. 13, 6094 (2022)](https://www.nature.com/articles/s41467-022-33846-0)。**本文自引的 20/34/37/48/49 正是这些**。
- 晶格氧/Mars‑van‑Krevelen + pH 依赖 + TMA⁺ 探针 + ¹⁸O：Huang et al., Nat. Energy 4, 329 (2019)；[Zhang et al., Nat. Commun. 11, 4066 (2020)](https://www.nature.com/articles/s41467-020-17934-7)；Angew 2019 ¹⁸O 标记研究。**方法论是标准工具**。
- 高价掺杂剂（Mo/W/Nb/Ta/V）调制 3d 金属氧化循环/能带中心：[Zhang B. et al., Nat. Catal. 3, 985 (2020)](https://www.osti.gov/biblio/1780685)（本文自引 17）几乎是**同一论点**；Wei et al., J. Mater. Chem. A 2022（Mo 掺 NiFeOOH，自引 19）；2025 年 Nb/V 掺 NiFe‑LDH 的 d‑band/PDOS 分析。**已有**。
- “单原子是电子促进剂、不是活性位”这一概念本身：[单原子 Au/NiFe‑LDH, JACS 140, 3876 (2018)](https://pubs.acs.org/doi/10.1021/jacs.8b00752)；Mo 单原子 + 氧空位 NiFe‑LDH（Adv. Sci. 2025）。**已有先声**。
- **最可能新的**：在**同一工作、同一体系**里，用同一套原位方法把“**取代型 W 价态不随电位变化 → 促进剂**”与“**锚定 Ir 价态随电位升高 → 直接活性位**”形成**对照式角色指认**，并把它与 α→γ 提前、MvK 路径、Ni–O–Fe 桥位连成一条证据链。这是“角色指认逻辑 + 完整证据链”的新，而不是现象本身的新。

> 判断：**C4 中约 80% 是已有思路**；“促进剂 vs 活性位”的对照指认是全文最可能立得住的新意（增量级）。

---

## 4. 汇总表：哪些新、哪些是已有思路

| 要素 | 2026-01-29 前状态 | 判定 |
|---|---|---|
| 预训练等变 GNN（EquiformerV2/OC22）预测吸附能 | OC20/OC22 本就为氧化物 OER 设计；2023–2024 已有 fine-tune 到新化学体系 | **已有** |
| ML 高通量筛选 SAC 的 OER 过电位 | iScience 2021、Innovation 2024、Accounts Mater. Res. 2025 | **已有** |
| 预测→合成→器件验证闭环 | Nat. Commun. 2024、Science Bulletin 2025 等 | **已有** |
| 2D volcano + scaling relation | Man 2011 起 | **已有** |
| W 掺 NiFe 氢氧化物/羟基氧化物做 OER | 2019/2020/2024/2025 多篇（含 W 固溶 NiFe 氢氧化物） | **已有（拥挤）** |
| 原子分散、取代型 WO₆ 的 W₁‑NiFeOOH + CV 电沉积 | 未见完全相同的实现 | **较可能新（实现层面）** |
| 半电池 178 mV@10 mA cm⁻² | 同类已 170–200 mV | **非新** |
| AEMWE 13.1 A cm⁻²@2.0 V | 已有 10 A cm⁻²/800 h、8 A cm⁻²@2.05 V | **边际记录，条件依赖** |
| 500 h@1 A cm⁻² | 已有 800 h@10 A cm⁻²、14,000 h 级 | **不构成记录** |
| Ni–O–Fe 边面活性位 / Fe 调制 Ni | Friebel 2015、Dionigi 2020 | **已有** |
| α→γ 相变 / Raman、XANES 指纹 / K⁺ 插层 | Klaus 2015、Bai 2022 等 | **已有** |
| MvK/晶格氧、pH 依赖、TMA⁺ 探针 | Huang 2019、Zhang 2020 | **已有** |
| 高价掺杂调制 Ni 3d / O 2p、促进 Ni 氧化 | Nat. Catal. 2020 等 | **已有** |
| 取代 W=促进剂 vs 锚定 Ir=活性位的对照指认 | 有 Au/NiFe‑LDH 等先声，但无完全相同的 W/Ir 对照 | **最可能的新意（增量）** |
| “ML 选中 W”的因果性 | 候选间距 < 模型误差（0.41 eV） | **论证薄弱** |
| “无贵金属”叙述 | 仅阳极无 PGM，阴极 PtRu/C | **表述偏强** |

---

## 5. 若要判定“真新”，建议补做的三件事

1. **核实 ACS Catal. [10.1021/acscatal.5c07061](https://pubs.acs.org/doi/full/10.1021/acscatal.5c07061) 的发表日期**是否早于 2026-01-29。若是，则“W 掺 NiFe 氢氧化物降低 Fe 活性位过电位”的机理新意几乎被完全覆盖，C4 只剩“原位 XAS 对照指认”。
2. **核实 Hu/Ma 2025（Angew. 64, e202413698）10 A cm⁻² 对应的电池电压**，以及 Li et al. Nat. Catal. 7, 944 (2024)、Klingenhof et al. Nat. Catal. (2024, [10.1038/s41929-024-01238-w](https://colab.ws/articles/10.1038%2fs41929-024-01238-w)) 在 2.0 V 的电流密度。这决定 13.19 A cm⁻² 是不是记录。
3. **要求作者给出候选间过电位差与模型误差的对比**（目前 0.01–0.05 V 的候选间隔 vs 0.41 eV 的吸附能 MAE），以判断“ML 指导”是否真的是因果性的。

> 附带一条文献定位观察：本文正文 57 条参考文献中**没有任何一篇 W 掺杂 NiFe‑LDH/氢氧化物的 OER 工作**（W 单原子 α‑Ni(OH)₂ 只在 Supplementary Table 5 出现，且只当性能基准）。对于一篇以“W 单原子 + NiFe 羟基氧化物”为卖点的工作，这是评价其新意时必须纳入考量的定位缺口。
````

#### T5-B 最终输出原文

````text
## 结论摘要

这篇论文把五条本来各自成熟的东西拼成了一个完整闭环，**真正的"新"是组合、实例化和器件数字；"已有思路"占了机制与材料类别的大头**。最需要补引用的是 **Ir 对照那条——它基本是 2021 年 PNAS 工作的复现**，而正文没有引用它。

（方法说明：本环境的 `web_fetch` 对所有域名失效，我改用 Python 直连 Crossref / Europe PMC / OpenAlex / Unpaywall 及开放获取全文。**付费墙后的条目只有摘要级证据，判级为上限**；OpenAlex 前向引文全程 429，未完成。下文"未找到先例"只在我实际检索到的范围内成立。）

---

## 一、论文自称的新意（拆成五条）

| 编号 | 主张 |
|---|---|
| C1 | EquiformerV2（OC22 预训练 + M₁-NiNiOOH 微调）作 MLIP，筛 3,976 个 M₁-MₐM_bOOH 构型 / >15,000 吸附结构，"域外"预测并提名 W₁-NiFeOOH |
| C2 | 原子分散、八面体取代的 W 嵌入 NiFeOOH 晶格（W 2.6 at%） |
| C3 | CV 共电沉积一步得到原子分散 W 的 NiFeOOH 纳米片（25 °C、数分钟、"可放大"） |
| C4 | 商用膜 AEMWE：1.56 V@1 A cm⁻²、13.1 A cm⁻²@2.0 V（80 °C）；500 h@1 A cm⁻²（60 °C） |
| C5 | W 是**氧化还原惰性促进剂**而**非活性位**（价态 +5.07→+5.11、W–O 键长不变）；促进 Ni 氧化与 α→γ 相变（1.43 vs 1.45 V）；降低 Ni–O–Fe 桥位 *OH→*O 脱质子能垒；MvK 晶格氧机制。对照 Ir₁-NiFeOOH 中 Ir 是直接活性位（+2.17→+4.17） |

---

## 二、逐条对照（2026-01-29 以前）

**C1 方法 —— 模板已有，属新实例化。** "等变 GNN 代理模型 + 主动学习探索单原子局域环境、面向 ORR/OER"2024 年已发表，且规模更大（>30,000 个单原子位点）：[npj Comput. Mater. 10 (2024)](https://doi.org/10.1038/s41524-024-01432-1)。"拿预训练 EquiformerV2 微调、在 out-of-domain 体系上预测 *OH/*O 吸附能"更是逐字已有的表述（[J. Phys. Chem. C 128 (2024)](https://doi.org/10.1021/acs.jpcc.4c01704)，针对高熵合金）；EquiformerV2 接进 AdsorbML 管线 + Sabatier volcano 筛选几千个表面：[ACS Catal. 15, 19461 (2025-11-07)](https://doi.org/10.1021/acscatal.5c04967)。ML 预测 SAC 的 OER 过电位可追到 [iScience 24, 102398 (2021)](https://doi.org/10.1016/j.isci.2021.102398)。**新的只是**把模板套到"单原子取代 (oxy)hydroxide"这一特定材料空间（8 宿主 × 41 元素 × 13 位点），以及 K⁺ 插层 γ 相宿主这一设定。GemNet/PaiNN/DimeNet++ 基准比较是 OC22 的标准做法，不算新意。

**C2 材料类别 —— 已有**（"W 作为 NiFeOOH 晶格中唯一原子分散取代物"这一组分细节可能新，但不是新问题）：
- 单原子 W⁶⁺ 掺 α-Ni(OH)₂，237 mV@10 mA cm⁻²，**明确把 W⁶⁺ 当活性位**：[Nat. Commun. 10, 2149 (2019)](https://doi.org/10.1038/s41467-019-09845-z)
- Mo、W 单原子共掺表面羟基化 NiFe 氧化物，196 mV@10 mA cm⁻²：[Appl. Catal. B 358, 124356 (2024)](https://doi.org/10.1016/j.apcatb.2024.124356)
- W 掺入富氧空位 NiFe-LDH：[ACS AMI 18, 5263（online 2026-01-10）](https://doi.org/10.1021/acsami.5c20762)；W 诱导 NiFe(oxy)hydroxide 重构：[Fuel 406, 136945（online 2025-09-27）](https://doi.org/10.1016/j.fuel.2025.136945)
- 电沉积三元 NiFeW 氢氧化物：[ChemSusChem 14, 1324 (2021)](https://doi.org/10.1002/cssc.202002544)；W 掺 NiFe-LDH 另有 [Acta Phys.-Chim. Sin. 40, 2303055 (2024)](https://doi.org/10.3866/pku.whxb202303055)、[JCIS 684, 1 (2025)](https://doi.org/10.1016/j.jcis.2025.01.012)、[Inorg. Chem. 58, 13037 (2019)](https://doi.org/10.1021/acs.inorgchem.9b01953)

**C3 合成 —— 已有思路。** 一步电沉积 W 掺杂 NiFe LDH（室温常压）是 2021 年：[ACS AMI 13 (2021)](https://doi.org/10.1021/acsami.1c01815)；**电沉积 30 min 制备原子分散单原子并锚定在 NiFe LDH 上**：[Small 21, e2504076 (2025-06-05)](https://doi.org/10.1002/smll.202504076)。NiFe(oxy)hydroxide 的阴极电沉积本身是常规方法。摘要写"Cyclic-electrodeposited W₁-NiFeOOH"是安全的；但方法里"optimized CV electrodeposition … scalable synthesis within minutes at 25 °C"读起来像未加引用的既有说法。

**C4 器件 —— 一条可能新，两条不是。**
- 1.56 V@1 A cm⁻² vs 早已有的 **1.57 V@1 A cm⁻²（80 °C，非贵金属，Sustainion X37-50 商用膜）**：[Adv. Energy Mater. 10, 2002285 (2020)](https://doi.org/10.1002/aenm.202002285) ——**这篇就列在论文自己的 SI Table 6 里**。差距 0.01 V。
- **500 h@1 A cm⁻² 远非记录**：同电流密度下已有 1,500 h@80 °C（[Nat. Catal. 7, 944 (2024)](https://doi.org/10.1038/s41929-024-01209-1)，该工作还给出 7,350 mA cm⁻²@2.0 V、半电池 15,200 h）、1,813 h（[Nat. Commun. 16, 65254 (2025-11-24)](https://doi.org/10.1038/s41467-025-65254-5)）、900 h（[Nat. Commun. 16, 65980 (2025-12-12)](https://doi.org/10.1038/s41467-025-65980-w)）、1,000 h（[Adv. Sci. 11, 2306988 (2023)](https://doi.org/10.1002/advs.202306988)）。摘要把"500 hours"当亮点，是全文最弱的一句。
- **13.1 A cm⁻²@2.0 V 很可能作为"商用膜 + 无贵金属阳极"的记录成立**：pre-cutoff 的 ≥10 A cm⁻²（10.7 与 14.17 A cm⁻²@2 V）全用自研膜（[Adv. Sci. 11, 2306988](https://doi.org/10.1002/advs.202306988)；[Angew. Chem. Int. Ed. 63, e202316697](https://doi.org/10.1002/anie.202316697)）；10 A cm⁻² 稳定 800 h 的也是自研膜（[Angew. Chem. Int. Ed. 64, e202413698](https://doi.org/10.1002/anie.202413698)）。但这条完全靠"商用膜"这个限定词撑着；且论文方法自己写明 AEMWE 极化曲线**未做 iR 补偿**，而对照文献多按 iR 补偿报，两者不可直接比较。

**C5 机理 —— 大部分是已有思路；Ir 对照最弱。**
- "高价态金属促进 3d 金属氧化循环、降低过电位"且**明确包含 W 掺入 NiFe 氧氢氧化物**：[Nat. Catal. 3, 985 (2020)](https://doi.org/10.1038/s41929-020-00525-6)——原文"reprogram the Fe, Co, and Ni oxidation cycles by incorporating high-valence transition-metal modulators X (X=W, Mo, Nb, Ta, Re, MoW)"。**论文把它列为 ref 17，却只在引言泛泛一句，Results/Discussion 下结论时没把它当作出发点。**
- 掺杂使 Ni²⁺(OH)₂→Ni³⁺ᵟOOH 转变电位负移（用 B）：[Nat. Commun. 13, 6094 (2022)](https://doi.org/10.1038/s41467-022-33846-0)（论文自己 ref 20）；W 促高价位 γ-NiOOH：[JCIS 684, 1 (2025)](https://doi.org/10.1016/j.jcis.2025.01.012)。
- MvK/晶格氧机制：[Nat. Commun. 11, 2522 (2020)](https://doi.org/10.1038/s41467-020-16237-1)、[Angew. Chem. Int. Ed. 60, 14981 (2021)](https://doi.org/10.1002/anie.202101698)（¹⁸O-DEMS 证实）、Mo 掺杂改变反应路径 [Nat. Commun. 13, 2191 (2022)](https://doi.org/10.1038/s41467-022-29875-4)、高价金属位活化晶格氧 [Nat. Commun. 11, 4066 (2020)](https://doi.org/10.1038/s41467-020-17934-7)（论文自己 ref 49）。
- "单原子是促进剂不是活性位"的一般概念 12 年前就有标题级表述：[Energy Environ. Sci. 7, 1382 (2014)](https://doi.org/10.1039/c3ee43811b)"promotion of activity by a redox-inert metal ion"；Au/NiFe LDH 单原子把活性归给邻近 Fe 的电荷重分布：[JACS 140, 3876 (2018)](https://doi.org/10.1021/jacs.8b00752)。
- Ni–O–Fe 桥羟基脱质子 → 高价 Ni 活性位：[Nat. Commun. 16 (2025)](https://doi.org/10.1038/s41467-025-56070-y)（2025-01 在线）；单原子+空位驱动 LDH 晶格氧活化：[Adv. Sci. (2025-12-05)](https://doi.org/10.1002/advs.202515407)。
- **Ir 对照几乎是 2021 年 PNAS 的复现**：Ir 单原子锚定 NiFe 氧氢氧化物、operando Ir L₃-edge 显示 OER 下 Ir 被氧化到高价（+4 @OCV → **+5.3** @1.45 V）、Ir 是直接活性位、**183 mV@10 mA cm⁻²**——而本文 Ir₁-NiFeOOH 也报 183 mV；PNAS 那篇甚至测过"subsurface doping by Ir next to the Fe-active site"，结论是 Ir 不改善 Fe 活性位。[PNAS 118, e2101817118 (2021)](https://doi.org/10.1073/pnas.2101817118)。**本文正文 57 条参考文献中没有它**（只在 SI Table 5 以 [14] 出现）。另有一篇 2025-09-22 的 ACS Catalysis 标题概念几乎相同：[10.1021/acscatal.5c05674](https://doi.org/10.1021/acscatal.5c05674)（本文未引）。

---

## 三、那到底什么是新的？

1. **一个具体的材料点**：把 ML 模板实例化到"单原子取代 (oxy)hydroxide"构型空间，得到 W₁-NiFeOOH 这一具体提名（C1+C2 的交集）。
2. **一个具体的谱学证据**：operando W L₃-edge 显示 W 在该体系中氧化还原惰性（+5.07→+5.11、W–O 键长不变），从而支持"W 不是活性位"。这是 PNAS 2021 的 Ir 情形所**不能**覆盖的新观测。
3. **一个限定条件下的器件水平**：商用膜 AEMWE 中 2.0 V 下 13.1 A cm⁻²。

其余（高价金属促 Ni 氧化/γ 相、MvK 晶格氧、单原子作促进剂、W 单原子用于 OER、W 掺 NiFe 氢氧化物、电沉积单原子、EquiformerV2 域外微调与 volcano 筛选、1.57 V@1 A cm⁻²、数百小时稳定性、Ir 直接活性位）**都是已有思路**，论文对其中多项没有给出应有的先行工作引用。

**几处需要改写的表述**：摘要"remains stable for 500 hours"不应作为耐久性亮点（已有 1,500–1,813 h）；"setting a benchmark"需限定为"商用膜 AEMWE 中 2.0 V 下的电流密度"；"W as promoter"应先承认 EES 2014 的 redox-inert promoter 概念与 Nat Catal 2020 的高价调节金属结论，delta 才是 W 的 operando 价态不变证据；Ir 对照必须引用 PNAS 2021。此外论文内部有一处不一致值得追问：其 W₁-Ni(OH)₂ 对照只比 Ni(OH)₂ 略好，这与 [Nat. Commun. 10, 2149 (2019)](https://doi.org/10.1038/s41467-019-09845-z) 把 W⁶⁺ 当作高活性位的结果相冲突，文中未讨论。

**评审边界**：付费墙后的若干个最接近条目（Appl. Catal. B 2024 的 Mo+W SA、Fuel 2026 的 W 诱导重构、ACS AMI 2026 的 W/NiFe-LDH、Small 2025 的电沉积 Pt 单原子、ACS AMI 2021 的电沉积 W-NiFe）只到摘要级；前向引文链与逐作者近期成果扫描未完成；Google Scholar、中文库、学位论文、专利未覆盖；检索未迭代到收敛。完整台账与引文清单见 `artifacts/novelty-review.md`。
````

#### T5-C 最终输出原文

````text
六位检索代理仍在运行；我的独立检索与验证已走完关键路径，先给出结论（引文均来自实际抓取，代理报告将在其完成后并入 `artifacts/lit/`）。

---

# 结论要点

## 1. 一句话判断

**这篇论文的"概念性新意"很弱，"集成度与器件级"贡献是真的。**

W 掺入镍基氢氧化物、W 作为"促进剂而非活性位"、单原子通过向邻近 Ni/Fe 电荷转移来降低相变/去质子化势垒、贵金属单原子发生价态变化而指示其为活性位——这些**在 2018–2019 年就已发表**；到 2025 年底/2026 年 1 月，连"W 掺杂 NiFe 氢氧化物中 W 不是活性位、而是调 Ni/Fe 并降低 \*OH→\*O 势垒+AEMWE 演示"这一整套结论都已有论文（2026-01-08 上线，早于本文 2026-01-29）。真正剩下的是：**同一样品上 W 与 Ir 的"促进剂 vs 活性位"对照 + operando 三谱联用 + 商用膜下的器件数据**。

**必须指出：本文最直接的三个先例只出现在补充参考文献里，主参考文献表完全删除了它们，正文也从不讨论**（详见第 5 节）。这是同时的引用诚信问题与新意问题。

## 2. 新 / 已有 对照表

| 论文的要素 | 判断 | 最近的先行工作 |
|---|---|---|
| 单原子 W 掺入 Ni 氢氧化物做 OER | **已有**（本文重发现） | Yan et al., *Nat. Commun.* **10**, 2149 (2019)，237 mV@10 mA cm⁻²，原位层内取代 W。**本文只在补充材料引用 [6]** |
| 层内取代式（非表面锚定）金属单原子 | **已有**（motif 层面） | Yan 2019 的 DFT 模型："an edge Ni atom was substituted by a W atom"；Zheng 2021 PNAS 已在 NiFeOOH 上比较"取代 vs 锚定"自由能 |
| W 调控 Ni/Fe 局域电子结构 | **已有** | *Inorg. Chem.* 2019；*ACS AMI* 2021；*Chem. Eng. J.* 2023；*ACS Catal.* 2026 |
| W 降低 \*OH→\*O 势垒 | **已有** | *Inorg. Chem.* 2019（W⁶⁺ 降低 OH⁻→O 自由基转化势垒）；*ACS Catal.* 2026 |
| "W 不直接参与，只调宿主" | **已有**（2026-01-08，早于本文） | Abbas et al., *ACS Catal.* (2026), DOI 10.1021/acscatal.5c07061："when W acts as the active site, the overpotential reaches as high as 1.96 V, suggesting that W does not directly participate in the OER"；且该文亦报 AEM-WE 2.12 A cm⁻²@2.0 V |
| **"单原子不是活性位，而是通过向邻近金属电荷转移加速活性相转变"** | **已有（这就是本文的核心机制，2018 年已写死）** | Lin et al., *Chem. Sci.* **9**, 6803 (2018)："rather than acting as an active site for the OER, monatomic Pt effectively increases the phase transformation rate by reducing the migration barrier of nearby Ni atoms" |
| 单原子引起宿主 Fe 及邻近原子电荷重分布 | **已有** | Zhang et al., *JACS* **140**, 3876 (2018)（Au/NiFe LDH） |
| **贵金属单原子在 LDH 上价态不变仍高活性（operando XAS）** | **已有** | Li et al., *Nat. Commun.* **10**, 1711 (2019)："the isolated single atom ruthenium was kept under the oxidation states of 4+ even at high overpotential"。**本文仅作补充引用 [9]** |
| **锚定 Ir 单原子是 NiFeOOH 的直接活性位、operando Ir L₃ 价态上升、η₁₀=183 mV** | **已有（本文属复现）** | Zheng et al., *PNAS* **118**, e2101817118 (2021)："the origin of water oxidation activity of IrNiFe SACs is the presence of highly oxidized Ir single atom (Ir⁵·³⁺)"；原文 +4 (OCV)→+5.3 (1.45 V)，183 mV。**本文仅作补充引用 [14]，且自己测出同样 183 mV** |
| 掺杂剂促进 α→γ 活性相转变 | **已有** | *ACS Catal.* **14** (2024), DOI 10.1021/acscatal.4c03974："Chromium Promotes Phase Transformation to Active Oxyhydroxide…"；以及 Lin 2018 |
| W 提高 O 2p 共价性/晶格氧机制 | **已有** | *J. Colloid Interface Sci.* 2026, DOI 10.1016/j.jcis.2026.140656（WO₄²⁻-NiFe₂O₄） |
| W+NiFe 室温电沉积 | **已有** | *ACS AMI* 2021, 10.1021/acsami.1c01815；*Chem. Eng. J.* 2023, 10.1016/j.cej.2022.139104（"cathodic electrodeposition… tungsten dopant undergoes reduction to stabilize the Ni and Fe active sites"） |
| 预训练 OC20/OC22 图神经网络算吸附能；"out-of-domain"框架 | **已有**（方法） | OC20(2021)、OC22(2023)、AdsorbML(2023)、EquiformerV2(ICLR 2024)，全部是本文自引 |
| "计算筛选→合成→验证"的 OER 工作流/"blueprint" | **已有** | Hari Kumar Sai Govind et al., *Chem. Sci.* **15**, 10556 (2024)："From computational screening to the synthesis of a promising OER catalyst" |
| 非贵金属阳极 AEMWE 高电流密度 | **已有，且更高** | *Adv. Sci.* **11**, 2306988 (2024)：非贵金属阳极 **10.7 A cm⁻²@2.0 V**，1 A cm⁻² 下 **1000 h**；IrO₂ 阳极 13.39 A cm⁻² |
| ≥10 A cm⁻² AEMWE 运行 | **已有** | *Angew. Chem. Int. Ed.* 2025, 10.1002/anie.202413698：**10 A cm⁻²@2.3 V 稳定 800 h** |
| 1.0 A cm⁻² 下的低电压 | **已有（几乎同值）** | Chen et al., *Adv. Energy Mater.* **10**, 2002285 (2020)：非贵金属、Sustainion X37-50、80 °C、1 M KOH 下 **1.0 A cm⁻²@1.57 V**（本文 SI 表 6 自己列了这一行，本文为 1.56 V） |
| PGM 成本论证 / 1 at.% 贵金属主导成本 | **已有**（标准技术经济论述） |

## 3. 那么，什么是**真新**的（诚实清单）

1. **同一样品上的"W vs Ir"双角色对照，配齐 operando W L₃ + Ni K + Raman。** 单个元素的结论各自早已有（W 是促进剂：Lin 2018 的 Pt、Abbas 2026 的 W；Ir 是活性位：Zheng 2021），但**在同一篇、同一宿主上把"价态不变的贱金属促进剂"与"价态跃迁的贵金属活性位"作为对照实验**，我在 2026-01-29 前没找到。这是本文最结实的贡献——应作为核心主张，而不是"首次发现 W 是促进剂"。
2. **位点级机制归因**：把被促进的位点具体定位到**棱面 Ni–O–Fe 桥位**，并用形成能/自由能排序证明基底面锚定 W 与暴露的 W–O–Ni/Fe 位点更差。Abbas 2026 只归因到 Fe 位点，未做棱面/基底面区分。
3. **ML 部分作为"工程实现"是新的**：3,976 个单原子-羟基氧化物构型 / >15,000 吸附结构的**构型空间**、对 OC22 预训练模型做域外基准（GemNet/PaiNN/DimeNet++）、以及 NiOOH→NiFeOOH 的迁移性检验。方法本身不新，但在这一体系上做出来、并给出可复现的基准与 Zenodo 权重，是有价值的工程贡献。**但不应写成"我们提出/加速了域外预测"**——那读起来像模型是本文造的。
4. **商用膜（PiperION 20 µm）子集内**的器件结果：约 13 A cm⁻²@2.0 V、1 A cm⁻² 下 >500 h。**注意：这不构成全领域记录**——13.39/10.7 A cm⁻²（2024）用的是自制膜，10 A cm⁻²/800 h（2025）用的也是优化膜，所以"商用膜"限定词站得住；但摘要里"setting a benchmark"必须改成限定表述。

## 4. 论文自述与文献/数据之间的三处张力（评审应追问）

1. **与 2019 年 Ni(OH)₂ 工作的结论直接冲突。** Yan 2019 的结论是 W *削弱* Ni 的氧化：*"single-atom W doping can promote carrier migration … and weaken the oxidation step of Ni²⁺"*、*"the doped W can assist in the migration of carriers from the catalyst to solution and weaken the oxidation effect of the electrocatalyst Ni(OH)₂"*。本文的结论是 W *促进* Ni 氧化与 γ 相转变。两者从未被放在一起讨论——而本文的 SI 恰恰引用了那篇论文。**要么宿主依赖（Ni(OH)₂ vs NiFeOOH）需要明确论证，要么需要重新检验。**
2. **做筛选的模型不是被验证的模型。** 论文称微调后精度更好（MAE < 0.2 eV），但**全部 3,976 个候选是用未微调的预训练骨干筛的**；该骨干在目标体系类上的吸附能精度从未报告。而且后续 DFT（Fig. 6d、SI Fig. 52）把筛选给出的 Ir>W 顺序反转了（ML 用的 Ir 基底面 3O 构型被 DFT 判为 0.485 V，与实验相反）。这个"筛选排序在后续 DFT 中被改写"的问题需要正面说明。
3. **AEMWE 对比不是同类比较。** 本文极化曲线**未做 iR 校正**且用 50 mV s⁻¹，而若干对照工作（如 2024 *Adv. Sci.*）协议不同；SI 表 6 又漏掉了 2024 *Adv. Sci.* 的非贵金属 10.7 A cm⁻²@2.0 V + 1000 h 和 2025 *Angew.* 的 10 A cm⁻²/800 h 这两个最强非贵金属对照。"among systems employing commercially available membranes"这一限定必须在摘要层面写明。

## 5. 引用层面的问题（这是最该改的）

**三个（或四个）最直接预示本文主张的工作，都只出现在补充参考文献，且主参考文献表里一个都没有，正文也从不讨论。** 我逐字检索过本文的参考文献表：`Yan`、`Zheng`、`Zhang, J. … Single-Atom Au`、`Li, P. … single-atomic ruthenium`、`Tian, B` 在主文献列表中**零命中**。

| 工作 | 在本文中的位置 | 后果 |
|---|---|---|
| Yan 2019 *Nat. Commun.* 10, 2149（单原子 W⁶⁺-α-Ni(OH)₂，237 mV，层内取代） | 仅 SI ref. [6]（SI 表 5 一行） | 否认了"W-in-Ni 氢氧化物""取代式 W"的新意 |
| Zheng 2021 *PNAS* 118, e2101817118（NiFeOOH 锚定 Ir、operando +4→+5.3、183 mV） | 仅 SI ref. [14] | 推翻 C8；并预告了 C5 的"取代 vs 锚定"比较；本文还把 183 mV 复现了一遍 |
| Li 2019 *Nat. Commun.* 10, 1711（CoFe-LDH 上 Ru 单原子价态恒为 +4） | 仅 SI ref. [9] | 预示了本文"价态不变=促进剂"的一半论断 |

这种"把最接近的先例放进补充材料"的做法，使得本文引文表看起来比实际更有新意。**建议在改稿时把 Yan 2019、Zheng 2021、Li 2019、Zhang 2018(JACS Au/NiFe LDH)、Lin 2018(Chem. Sci. Pt)、Abbas 2026(ACS Catal. W-NiFe) 全部移入主参考文献并在引言/机制讨论中正面区分。**

## 6. 建议的改写（标题级主张）

- 摘要"setting a benchmark for noble metal-free anode catalysts under practical water electrolysis conditions" → **"among the highest reported for a noble-metal-free anode with a commercially available membrane"**，并引用 2024 *Adv. Sci.*、2025 *Angew.*、2020 *Adv. Energy Mater.*。
- "An equivariant transformer-based machine-learning interatomic potential accelerates out-of-domain adsorption energy predictions and nominates…" → **"We applied a pretrained EquiformerV2/OC22 potential out of domain to a 3,976-configuration single-atom-oxyhydroxide space, benchmarked its accuracy, and nominate…"**（现措辞读起来像模型是本文提出的）。
- 机制主张改为：**"W 在镍基羟基氧化物中已被证明是促进剂而非活性位 [Yan 2019; Abbas 2026]；本文将其被促进的位点定位到棱面 Ni–O–Fe 桥位，并用 operando 证明 W 价态不变而 Ni 氧化被加速。"**
- 标题里的 "Machine-learning-guided" 建议保留但降级为方法学修饰；真正的卖点是 **同源对照 + 位点级 operando 机制 + 商用膜器件**。

---

## 检索方法与边界（可核查）

- **检索引擎**：Europe PMC（检索 + fullTextXML，主力）、Crossref、PubMed eutils、Unpaywall、OpenCitations（正/反向引文链）、web_search；**OpenAlex 与 Semantic Scholar 因共享 IP 日额度耗尽全程 HTTP 429，未能使用**（已计入 gap）。
- **全文读取**：Yan 2019 (*Nat. Commun.*, PMC6517434)、Zheng 2021 (*PNAS*, PMC8433498)、Li 2019 (*Nat. Commun.*, PMC6461613)、Lin 2018 (*Chem. Sci.*, PMC6114998)、Abbas 2026 (*ACS Catal.*, PMC12976961)、本文正文/SI/源数据——均按原文逐字引用（引文见上表）。
- **未能读取（标记 FULL-TEXT-UNREAD）**：Tian 2021 *Angew.*、Shin 2018 *JACS*、Dou 2022 *Adv. Mater.*、Wang 2024 *Adv. Mater.*、Guo 2024 *Small*、Chen 2020 *Adv. Energy Mater.* 等付费墙文献（Chen 2020 的 1.57 V 数字取自本文 SI 表 6 自身引文 + Crossref 摘要核验）。
- **迭代轮次**：主管线 4 轮 + 9 条并行谱系（每条 4–9 轮）。**尚未完全 dry**：`artifacts/lit/` 下 6 个并行谱系的完整报告仍在生成（ML 筛选、W-in-NiFe、AEMWE 基准、α→γ 相变、operando XAS、成本/工作流框架），它们完成后会补齐各自的检索账本、读账本与 gap statement；这 6 条线目前是**欠账而非已覆盖**。
- 详细证据、引文与账本见 `artifacts/novelty-synthesis-lead.md`、`artifacts/claims.md`、`artifacts/lit/sac-oxyhydroxide.md` 及 `artifacts/lit/raw/`。

**如果只能记一句话**：这篇论文真正新的不是"W 是促进剂"，而是"在同一宿主上把 W(促进剂/价态不变) 与 Ir(活性位/价态跃迁) 做成对照，并把被促进位点定位到棱面 Ni–O–Fe 桥位"；其余多为 2018–2026 年间已发表的思路，其中三项最接近的先例被放在了补充参考文献里。
````

### T6

#### 三组共同的用户输入原文

````text
所需论文材料位于 materials；可以按需要读取，并使用现有检索工具。

作者凭什么说 W 主要是在促进邻近活性位点，而不是自己直接参与反应？这些证据够有说服力吗？
````

| 组 | 主会话成功加载的 skill（实际顺序） | 耗时/s | 未缓存输入 | 缓存读取 | 输出（含推理） | 总 token | 请求数（含委派） |
|---|---|---:|---:|---:|---:|---:|---:|
| A | 无 | 127.4 | 68,582 | 549,888 | 20,254 | 638,724 | 15（委派 0） |
| B | `scientific-critical-thinking` | 294.2 | 108,088 | 2,998,656 | 41,900 | 3,148,644 | 31（委派 0） |
| C | `scientific-critical-thinking` → `reading-contract` | 362.6 | 94,897 | 2,893,440 | 58,213 | 3,046,550 | 34（委派 0） |

#### T6-A 最终输出原文

````text
我把正文、补充材料、源数据和透明同行评议都过了一遍。下面按“作者提出了哪些证据 → 这些证据各自能证明什么 → 是否够有说服力”来回答。

---

## 一、作者用来主张“W 是促进者、不是直接活性位点”的证据链

**1) 原位 W L₃ 边 XANES / EXAFS：W 在 OER 条件下“价态和局域结构都不变”（核心证据）**
- 在 0.1 M KOH 中从 OCP 到 1.6 V，W L₃ 边白线位置和强度基本不变，拟合价态 +5.07（OCP）→ +5.11（1.6 V）；第一壳 W–O 键长也不变（正文 Fig. 4b–d，补充 Fig. 43）。
- Source data 也印证：W L₃ 白线约 10212.09 → 10212.13 eV（+0.04 eV）。
- 对照的同批 Ir₁–NiFeOOH：白线约 11217.8 → 11219.0 eV（约 +1.16 eV），价态 +2.17 → +4.17，并伴随 Ir–O 收缩（补充 Fig. 44）。
- 作者的三段论是：**直接参与 OER 的金属位点必须随电位发生氧化还原/成键变化；W 没变，所以 W 不是直接活性位点。**

**2) DFT 位点分辨过电位：把 W “放到台前”反而更差（最直接的“反事实”证据）**
– 边缘 (01‑12) Ni–O–Fe 桥 + 次表层 W：η = 0.357 V；
– 边缘暴露的 W–O–Ni/Fe 桥：η = 0.964 V；基面 W 位点：η = 0.700 V；
– 原始 NiFeOOH 的 Ni–O–Fe 桥：η = 0.475 V（正文 Fig. 6c,d；源数据一致）。
→ 结论：W 自己做活性位时比 Ni–O–Fe 差得多，只有“藏在 Ni–O–Fe 桥下面/旁边”时才把 0.475 V 降到 0.357 V。

**3) W 改变了“邻居 Ni”的氧化行为（说明作用对象是 Ni 位点）**
- 原位 Ni K 边 XANES：W₁–NiFeOOH 在 ~1.40 V 就开始显著氧化，且各电位下位移都比 NiFeOOH 大，平均 Ni 价态约 +3.6（向 γ‑NiOOH 转变）；NiFeOOH 需要更高电位（Fig. 4e）。
- 原位 Raman：α→γ 转变在 W₁–NiFeOOH 为 1.43 V，而 Ir₁–NiFeOOH/NiFeOOH 为 1.45 V（Fig. 5b–d）。
- 外加 Ni 2p XPS 正移（补充 Fig. 46）、Ni K 边 EXAFS 重组（Fig. 47）。

**4) 载体依赖性：W 的增益依赖“好的 Ni–O–Fe 宿主”**
- W₁–Ni(OH)₂ 相对 Ni(OH)₂ 只有很小提升，且仍不如纯 NiFeOOH；而 W₁–NiFeOOH 同时超过 Ir₁–Ni(OH)₂ 和 Ir₁–NiFeOOH（Fig. 3b）。Co 体系里 Mo 也只在 CoFeOOH 中才明显起效（补充 Fig. 33）。
- 作者据此认为 W 需要 Ni–O–Fe 位点才能发挥作用，不像 Ir 那样“到哪里都提升”。

**5) 结构 + 电子结构证据**
- EXAFS 无 W–W、W 为畸变八面体 WO₆、弱 W–Ni/Fe 第二壳；形成能计算表明**层内取代**优于表面锚定（Fig. 2e–g、补充 Fig. 28）→ W 在晶格内部、邻近 Ni/Fe。
- PDOS：W 掺入使 Ni 3d 带中心上移（-2.83 → -2.25 eV），Ni 3d–O 2p 能量差从 0.54 eV 降到 0.03 eV，增强杂化（Fig. 6e,f）。
- TMAOH 处理和 pH 依赖动力学支持晶格氧参与（补充 Fig. 50、51），以此论证 MvK 型机制。

---

## 二、这些证据够有说服力吗？

**总体判断：方向上有说服力，但“证明”不闭环——足以说明“W 不是主要的氧化还原金属中心、其主要作用是调控 NiFe 羟基氧化物”，但不足以严格排除 W 直接参与，也不足以坐实“促进的是紧邻的 Ni–O–Fe 位点”。**

### 比较有力、站得住的部分
- **多手段相互印证**：结构（EXAFS/STEM）、操作态谱学（原位 XAS、Raman）、DFT、对照实验（Ir、Ni(OH)₂ 宿主）指向同一方向，不是单一证据硬撑。
- **Ir 是同批内对照**：同样载体、同样电沉积流程，Ir 明显变价、W 不变，对照设计合理。
- **DFT 确实直接回应了“W 自己当活性位”这一反事实**：把 W 暴露到桥位后 η 反而升高（0.964 V），这是比其他旁证更直接的一条。
- **载体依赖是真正的“证伪型”实验**：如果 W 自己是活性位，高 W 含量（3.49 at%）的 W₁–Ni(OH)₂ 应该更强，事实并非如此。

### 明显薄弱、经不起追问的部分
1. **最核心的“W 价态不变”是一个系综平均的负结果。**
   XANES 白线是所有 W 原子的平均信号。催化相关的可能只是边缘/表面的一小部分 W，其变化会被大量“旁观”W 稀释；文中没有给误差棒，也没有给“能检出多大比例 W 变化”的灵敏度/检出限分析，且数据本身非单调（+5.07→+5.11 与扫描间散布同量级）。再加上 W 负载不低（2.6 at%）、测量在 0.1 M KOH 而性能测试在 1 M KOH、电位只到 1.6 V，因此**“测不到变化”≠“不参与”**。
2. **逻辑上存在跳跃：他们自己主张 MvK（晶格氧）机制，而晶格氧机制中氧化还原当量可以主要落在氧上，不一定体现在金属价态上。** 所以“W 价态不变”最多排除“W 作为主要变价金属中心”，并不能排除 W 通过其 W–O 键参与吸附/质子转移（双功能或协同位点）。把“促进者”与“直接活性位”处理成非此即彼，本身偏二分法。
3. **DFT 结论依赖模型和参数，且是热力学而非动力学。**
   - 单一 U 值（U_W = 6.2 eV 取自 Materials Project，U_Ni = 5.2、U_Fe = 2.56），没有给出 U 扰动下的稳健性分析——而审稿人 #4 恰恰提了这一点。
   - 只在 U = 1.23 V 下单点算 ΔG，没有 NEB/显式动力学势垒。摘要和正文却写成“降低 PCET 势垒/去质子化能垒”，**这是措辞上的越界**：他们算的是 *OH→*O 的热力学自由能台阶，不是 PCET 动力学势垒。
   - 0.357 V vs 0.964 V 的对比是不同几何/配位环境之间的比较（W 做桥金属时键长、弛豫都不同），差异未必全部来自“W 本征活性差”。
4. **“邻近/紧邻”这一空间关系是模型假设，不是直接观测。**
   HAADF‑STEM 只证明 W 单原子分散，并没有把“某个 W”和“某条边缘 Ni–O–Fe 桥”在空间上对应起来；EXAFS 是平均信息；DFT 给的是“次表层取代 W + 边缘 Ni–O–Fe 桥”的理想模型。而且 2.6 at% 的 W 在统计上不可能让每个 Ni–O–Fe 位点都紧邻 W。“促进邻近位点”目前只是最合理的解释，而非被证实的图像。
5. **贡献归因存在混杂因素。**
   W 的掺入同时改变形貌、边缘密度和双电层电容（补充 Fig. 34 各样品的 C_dl 不同），部分活性增益可能来自几何/面积而非位点本征电子效应。他们的 TOF 是“假设全部金属原子都是活性位”的下限估计，并不能把几何贡献和电子促进作用分开。
6. **Ir 对照并非严格配匹。** Ir 是基面锚定的 Ir–O₆（1.77 at%），W 是层内取代的 WO₆（2.62 at%），元素与位点几何同时改变，因此 W/Ir 的对比把“元素差异”和“位置差异”混在了一起。
7. **透明同行评议显示该机制未被真正“对抗性”审查。** peer-review 文件里这篇是从其他期刊转投、在 Nature Communications “无需再送审”，审稿人只提了 Hubbard U（正是上述薄弱点）、KOH 中 Fe 杂质、数据可用性；关于 W 是不是直接活性位的核心机制并没有被深入质询。

---

## 三、结论

- 作者凭什么说：主要靠 **“W 在操作态不变价、不变 W–O 键”（原位 XAS）+ “W 自己当位点反而更差”（DFT 位点分辨 η）+ “W 促进 Ni 氧化/γ 相转变”（Ni K 边、Raman）+ “换掉 Ni–O–Fe 宿主 W 就失效”** 四条线。
- 这些证据**足以支撑一个合理且内部自洽的“W 是高价调控型促进剂、而非主要变价活性中心”的结论**，其中“载体依赖”和“DFT 反事实比较”最有分量。
- 但要说“主要是在促进邻近活性位点、而不是自己直接参与”，**证据尚不充分**：核心负结果受系综平均/灵敏度限制且有逻辑缺口，DFT 依赖 U 与几何模型且缺少动力学势垒，“邻近”没有空间分辨的直接证据，“MvK/PCET 势垒降低”属于过度表述。属于**“有说服力的假说，但未闭环证明”**。

要把它变成硬证据，至少还需要：更高灵敏度/时间分辨的操作态 W XAS（L₁ 边或 HERFD，并在 1 M KOH、更高过电位下做，并给出检出限）、¹⁸O 同位素标记 + DEMS 直接确认晶格氧参与、操作态 Raman/IR 捕捉 W–OH/W=O 中间体、STEM‑EELS 把 W 位置与边缘位点在空间上对应、以及 U/收敛性敏感性与含显式动力学的势垒计算。
````

#### T6-B 最终输出原文

````text
## 先给结论

论文是 Kim et al., *Nat. Commun.* **17**, 2344 (2026)（[原文](https://www.nature.com/articles/s41467-026-68735-3)）。作者的理由是**三条相互独立的线索 + 一条自洽性检查**，方向一致，所以"W 主要起促进/调制作用"这个**方向性判断是有依据的、可信度中等偏上**；但"W 自己不直接参与反应"是一个**排他性结论**，现有证据属于"一致但不排他"，撑不到 Discussion 里那句 "unambiguous catalytic mechanisms"。下面拆开说。

---

## 一、作者凭什么这么说（论证链）

1. **结构位置**：W 是取代进入晶格（八面体 WO₆、无 W–W、W–O 1.92/1.94/1.99 Å），形成能计算表明"层内取代"优于"基面锚定"（Fig. 2e–g、S28、Table S3）→ 位置上是"埋在里面"的调制器，不是表面锚定位点。
2. **原位 XAS 对照实验（最核心的一条）**：W L₃-edge 从 OCP 到 1.6 V，白线位置/强度几乎不动，价态 +5.07 → +5.11；W–O 峰位不变。同一实验里的 Ir 则 +2.17(正文)/**2.78**(Fig. 4c 标注) → +4.17，Ir–O 键收缩（Fig. 4b–d、S43、S44）。**同一载体、同一实验，一个不动一个剧烈变** → 判定 Ir 是直接活性位、W 不是。
3. **载体依赖性（最有说服力的实验级证据）**：W 只在含 Fe 的载体上有效（Fig. 3b：NiFeOOH 214→178 mV；Ni(OH)₂ 246→231 mV，W₁–Ni(OH)₂ 甚至比纯 NiFeOOH 还差），而 Ir 在两种载体上都提升（→183/185 mV）；Mo/Co 体系（S33）复现同一规律 → W 的收益必须"经过" Ni–O–Fe 位点。
4. **DFT 位点排序**（我从 Source Data `Figure 6` 核过数字）：边面 Ni–O–Fe 桥 + 次表层 W 的 η = **0.357 V** 最低；暴露的 W–O–Ni/Fe 边位点 **0.964 V**、W 取代基面位点 0.700 V 都高于纯 NiFeOOH 边面 Ni–O–Fe 的 0.475 V；同时 W 使 Ni 3d 带上移、与 O 2p 重叠增强（Fig. 6c–e）。
5. **宿主被促进的谱学证据**：Ni K-edge 提前氧化、γ 相在较低电位出现（1.43 vs 1.45 V，Raman）；配合 TMAOH 与 pH 依赖实验指向晶格氧（MvK）机制（Fig. 4e、5、S49–S51）。

**一个作者没说、但确实存在的加分项**：ML 筛选（Fig. 1c,d）在完全不含机理信息的条件下，给 W 选出的最优 motif 恰好是 config 4（边面 Ni–O–Fe 桥 + 次表层取代，0.268 V），给 Ir 选的是 config 1（基面锚定 M₁–O₆，0.254 V）。纯能学筛选和后来的机理归属自洽，这比论文自己写出来的更漂亮。

---

## 二、这些证据的软肋

**逻辑性质问题**：第 2 条本质是"没观察到变化"，只能排除"W 是一个像 Ir 那样循环变价的 AEM 型位点"，排除不了"W 自己吸附 \*OH/\*O/\*OOH"。XAS 是 2.6 at% W 的整体平均，少数表面/边面 W 参与反应完全测不出来；+5.07→+5.11 没有给误差棒。更微妙的是：作者为 W₁ 提出的是 **MvK（晶格氧）机制**，而 MvK 下金属价态本来就**不**必变——所以"价态不变"这条论证针对 MvK 参与恰恰是最弱的，两条论证互相削弱。

**定量强度问题**：DFT 里"促进"的增益只有 0.475→0.357 = **0.12 eV**，而"W 不是好位点"的差距是 0.964 vs 0.475 = **0.49 eV**。也就是说，反证"W 不是直接位点"的证据远比论证"W 如何促进"的证据硬。0.12 eV 落在 DFT+U/无显式溶剂/恒电荷近似的典型误差量级内，而且论文没有 η 的误差棒、没有 U 敏感性测试（审稿人第 4 位明确要求过，正文补了 U 值但没补敏感性），motif 集合是人挑的。

**实验条件不统一**：W/Ir L₃-edge 原位 XAS 在 **0.1 M KOH**，Ni K-edge 和所有电化学在 **1 M KOH**；Raman 明确"without iR correction"。

**审稿背景**：peer review file 显示这是从别的期刊转来、在 Nat. Commun. "considered suitable for publication without further review"，文件里只有最后一轮的几条小意见（U 值、Fe 杂质、数据存放），**没有一条真正质疑 W 的角色**；而且文件声称包含作者答复，实际并没有。所以"审过了"不能当作这条结论稳健的证据。

---

## 三、我核出的几处正文与源数据/图不符（这会实质削弱说服力）

1. **Fig. 4e**：正文写 W₁-NiFeOOH "significantly larger edge shifts than NiFeOOH **at all potentials**"。但 Source Data（sheet `Figure 4`，AI/AJ 列）和图上曲线都显示 **1.40 V 时 NiFeOOH 反而更高（2.74 vs 2.60）、1.42 V 也是（2.93 vs 2.81）**，两条线在 ~1.44 V 交叉，之后 W₁ 只领先 0.03。"earlier onset"也不成立（两者都在 1.3→1.4 V 之间起跳）。这是支撑"W 促进宿主氧化"的关键图，正文表述被推高了。
2. **Ir 的 OCP 价态**：正文 +2.17，Fig. 4c 标注是 **Ir²·⁷⁸⁺**，差 0.6。二者必有一错。
3. **Raman 的 1.43 vs 1.45 V**：只有 10 mV 一步的分辨率，且 Fig. 5b 在 1.43 V 存了 **2 min 和 8 min 两条谱**，说明该转变有时间/扫描历史依赖；而且 W₁ 的强度比基线（1.3 V 时 ≈1.70）与 Ir/NiFe（≈1.20）差很多，比的是不同基线。
4. **DFT 与实验排序相反**：DFT 给 Ir 锚定位点 0.310 V < W 促进位点 0.357 V，实验却是 W₁（178 mV）略优于 Ir₁（185 mV）。差 7 mV 在 n=3 的散差里，作者用"Ir 还有更宽的过电位分布"来调和，属于事后解释。
5. **ML 分辨率不足**：Fig. 1d 前几名 Ir 0.254 / W 0.268 / Tl 0.271，彼此差 ≤0.02 eV，而微调模型的吸附能 MAE 是 0.19–0.20 eV（baseline 0.408 eV）。仅凭能量无法把 W 和 Tl/Ba 区分开——W 的胜出主要靠后面的实验，不靠 ML。
6. **ECSA 那句说法与数据相反**：正文说 ECSA "confirmed enhanced charge transfer with increased active site availability"，但 W₁-NiFeOOH 的 C_dl 最低（3.28 vs 5.93/6.08 mF cm⁻²）。这个数字其实**有利于**作者（排除比表面效应），但表述是错的。

---

## 四、要把这条结论做实，还缺什么

- **位点计数**：现在 TOF 按全部金属原子归一（"minimum bulk limit"），根本无法把 turnover 分摊给 W 或 Ni/Fe；需要 W 负载量梯度 + 单位 W 的活性。
- **直接探针**：operando IR/Raman 看 W–O–O/W–OH，或 **¹⁸O 同位素标记**判断放出的 O 是否来自 W–O 键——这是唯一能真正区分"促进"与"参与"的实验，论文没做。
- **选择性中毒/掩蔽 W 位点**。
- **在 1 M KOH、高电流下**做 W 原位 XAS，给出误差并处理自吸收。
- DFT 侧：U 与溶剂化/恒电位敏感性、η 的误差棒、motif 覆盖率与暴露面的实验约束。

---

## 五、对"够不够有说服力"的判断

- **够支持一个工作假设**：W 主要作为调制器促进邻近 Ni–O–Fe 边面位点（原位 XAS 的 W/Ir 对照 + DFT motif 排序 + 载体依赖性三条独立线索同向，且与"高价金属调制 3d 金属氧化还原循环"的既有框架（[Zhang et al., Nat. Catal. 2020](https://www.osti.gov/pages/biblio/1780685-high-valence-metals-improve-oxygen-evolution-reaction-performance-modulating-metal-oxidation-cycle-energetics)）一致；ML 筛选与 DFT 的 motif 归属自洽）。在电催化机理类论文里，这算比较完整的一套。
- **不够支持原文的排他表述**："W atoms themselves are not the primary active sites"、"unambiguous catalytic mechanisms"。所有关键证据都是"与促进假说一致"，没有一条能判决性地否证"W 自己也参与"；而且支撑"促进"的关键定量差值（0.12 eV、20 mV、7 mV、15 mV）都贴着噪声/误差/分辨率。
- 一句话：**该结论应当降格为"在整体平均意义上主要不是 W 在反应"**，而不是"W 不直接参与反应"。论文 Results 部分用词（suggest / might）是恰当的，Abstract 也留了 "suggest"，问题出在 Discussion 的 "unambiguous"。

完整的核对记录（含具体数值、列名、页码）我保存在 `artifacts/W-role-appraisal.md`，从 PDF/XLSX 抽出的原文与源数据文本在 `artifacts/` 下。
````

#### T6-C 最终输出原文

````text
## 结论先说

作者的主张是：**W 不是活性位，而是"促进剂"（promoter），通过电子调控加速邻近 Ni–O–Fe 边面位点的脱质子/γ 相转变；Ir 才是自己当活性位**。他们给出的证据链是**方向一致、彼此自洽的**，其中"换载体"的对照实验（Fig 3b）最有说服力；但就"W 不直接参与反应"这一否定性结论而言，证据**还不够硬**——关键的几条都踩在方法分辨率的边缘上，而且有一条逻辑缺口（"价态不变⇒不是活性位"在作者自己主张的晶格氧机制下不成立）。

---

## 一、作者的原话与主张强度

| 位置 | 原文（逐字） | 语气 |
|---|---|---|
| Abstract | "subsurface W promoter induces synergistic electron redistribution at neighboring Ni-O-Fe edge active sites" | 确定 |
| Introduction | "Anchored Ir atoms directly act as active sites, while substituted W atoms function as modulators, promoting the original active sites in the NiFeOOH edge plane." | 确定 |
| Results（XAS 段） | "The observed constancy in valence state and local structural environment **suggest** that atomically dispersed W atoms are not direct active sites in the electrocatalytic process (Supplementary Fig. 43)." | 试探（suggest） |
| Results（DFT 段） | "The exposed W–O–Ni/Fe motifs on the edge plane or W substituted on the basal plane exhibited a higher barrier than the original Ni–O–Fe active sites (Fig. 6d), **suggesting** that W atoms themselves are not the primary active sites but rather act as promoters." | 试探 |
| Discussion | "experimental validation of its electrocatalytic performance with **unambiguous catalytic mechanisms**" | 确定（过度） |

注意：Results 里是 "suggest"，到摘要/引言/讨论就变成了既成事实——**主张在文中被逐级加码**。

---

## 二、他们到底拿什么来论证（五条证据）

**(1) 原位 W L₃-edge XAS：W 价态与 W–O 键长不随电位变化**（Fig 4b–d；Supplementary Fig. 43）
- "Average W valence states of +5.07 at OCP and +5.11 at 1.6 V were estimated with a negligible shift (Fig. 4c)."
- 原位 FT-EXAFS 第一壳 W–O 峰位置不变（Fig 4d）。

**(2) 与 Ir 的对照**：Ir L₃-edge 白线随电位上升，"At OCP … a valence state of +2.17 … As the applied voltage increased to 1.6 V … oxidized to a valence state of +4.17"，且 Ir–O 键收缩；由此断言 Ir 是直接活性位。

**(3) DFT 位点能量比较**（Fig 6c,d；Supplementary Fig. 52，我核对了 Source Data）
- W 自身位点更差：边面 W–O–Ni/Fe 桥 η = 0.964 V；基面 M–O–Ni/Fe 0.70 V；基面 M₁–3O 1.401 V。
- 但**同一个 Ni–O–Fe 桥位**在 W₁–NiFeOOH 中 η = 0.357 V，优于 pristine NiFeOOH 的 0.475 V —— 这才是"促进"的直接计算证据。

**(4) 宿主被"激活"**：原位 Ni K-edge 显示 W₁ 样品 Ni 氧化更早/更深（Fig 4e）；原位 Raman 显示 γ-NiOOOH 特征峰在 1.43 V 出现，而 NiFeOOH 与 Ir₁ 是 1.45 V（Fig 5）；PDOS 显示 Ni 3d 带中心上移、与 O 2p 重叠增强（Fig 6e,f）。

**(5) 载体依赖性**（Fig 3b，我核对了 Source Data 的毫伏数）：

| 样品 | η@10 mA cm⁻² | 样品 | η@10 mA cm⁻² |
|---|---|---|---|
| W₁–NiFeOOH | **178** | W₁–Ni(OH)₂ | **231** |
| Ir₁–NiFeOOH | 185 | Ir₁–Ni(OH)₂ | 183 |
| NiFeOOH | 214 | Ni(OH)₂ | 246 |

即：W 在 NiFeOOH 载体上提升 36 mV，在 Ni(OH)₂ 上只提升 15 mV；Ir 换载体几乎不变（185→183）。这是全文**最有信息量的一个对照设计**。

**(6) 机制归属**：TMAOH 处理与 pH 依赖动力学（Supplementary Fig. 50、51）被用来支持晶格氧（Mars-van-Krevelen）参与。

---

## 三、这些证据够不够？逐条挑

### A. 有分量的部分（先给作者记分）
- **W/Ir 对照方向一致、多手段互证**：光谱（价态、键长）+ 载体依赖 + DFT 位点排序，三条独立信息指向同一图景，不是单点证据。
- **DFT 确实把 W 自身的几种位点都算过**（边面暴露 W、基面取代、基面锚定 3O），且都更差——不是只挑了有利的算。
- **ECSA 对照对作者有利**：C_dl 为 W₁ 3.28、Ir₁ 5.93、NiFeOOH 6.08 mF cm⁻²（Supplementary Fig. 34），W₁ 的比表面最小却电流最高，说明不完全是被面积效应灌水。
- **载体依赖性实验**（Fig 3b）是真正能区分"自身是位点"与"依赖宿主位点"的设计：如果 W 自己就是活性位，它应当像 Ir 一样在 Ni(OH)₂ 上也灵。

### B. 站不住 / 不够硬的部分（按严重程度）

**① 逻辑缺口："价态不变⇒不是活性位"在作者自己的机制下不成立。**
他们主张 MvK/晶格氧机制（氧化还原中心是氧），却又用"金属 W 价态不变"来排除 W 直接参与。若氧是氧化还原中心，金属中心完全可以不改变形式价态而直接参与（结合 OH*/O*、参与 O–O 偶联、或本身就是被交换的晶格氧）；Lewis 酸性的 W(VI) 也能在不被还原的情况下结合 OH⁻/H₂O。**这两条论据互相削弱的正是最关键的推断。**

**② 定量分辨率：W 的"不变"是测在方法噪声尺度上的。**（以下数字是我从 Source Data 谱线算的，非原文数字）
- 对 Fig 4b 的 W L₃-edge 谱做峰位拟合：OCP 10212.09 eV → 1.6 V 10212.13 eV，全程摆动 ≤0.11 eV；Ir 则 11217.82 → 11218.98 eV（+1.16 eV）。方向的对比是可靠的。
- 但 Fig 4c 右轴的 "formal d-band hole counts" 对 W 而言就是"白线能量 − 10203.014"（各点常数一致到 ±0.002 eV），也就是说 **1 eV ↔ 1 电子**；报告的 +5.07→+5.11（Δ0.04）就等于能量位移 0.04 eV，**全文没有给任何误差棒、重复测量或校准线**。
- 更麻烦的是**绝对价态不可复现**：正文说 ex situ W "close to +6"（Supplementary Fig. 24），原位却给 +5.07；用他们自己提供的参考谱（W foil 10209.17、WO₃ 10212.84）做两点线性内插，W₁–NiFeOOH（10211.59）只对应 ≈+4.0。属于"只有在文中未说明的约定下才成立"。
- **正文与图自相矛盾**：Ir 在 OCP 的价态正文写 **+2.17**，Fig 4c 标注却是 **Ir²·⁷⁸⁺**（差 0.6 个价态单位）——而这正是用来做 W/Ir 对比的量。

**③ Ni K-edge 证据被正文夸大了。** 正文说 "significantly larger edge shifts than NiFeOOH **at all potentials**"；但 Source Data（Fig 4e 的 "Ni oxidation state (a.u.)"）显示 1.30–1.42 V 区间 W₁ 的数值**反而更低**（2.48 vs 2.55；2.60 vs 2.74；2.81 vs 2.93），1.50 V 最大差 0.08，1.60 V 为 3.61 vs 3.58，且无误差棒。Raman 的 γ 相提前量也只有 0.02 V（1.43 vs 1.45 V）。"W 促进 Ni 氧化"因此是**很小且非单调**的效应。

**④ DFT 的分辨率撑不起这个结论。**
- 他们自己承认要引入 Ir₁–3OH（η = 0.485 V）才能"reconcile the apparent discrepancy"——而同一套计算里 Ir 位点随羟基化可在 **0.310–0.485 V（0.175 V）**间摆动；相形之下"W 促进 Ni–O–Fe 桥位"的关键差值只有 **0.118 V**，"W 自身位点更差"的差值也在 0.1–0.6 V 量级。**W 位点却没有做同等的羟基化/配位敏感性测试**（只算了 3 个非羟基化构型）。
- ML 筛选本身把 **Ir（0.254 V）排在 W（0.268 V）前面**（Fig 1d Source Data），实验却反了；其吸附能 MAE 也 <0.2 eV。也就是说，整套计算在"顶级候选之间"已被证明分不清。
- 审稿人**明确要求**的 "whether small variations in U impact the main trends"（Hubbard U 敏感性）在正文与 61 页 SI 中**都找不到**（我全文检索过；U 值本身列在 Methods 里）。

**⑤ 结构前提（"W 替位嵌入、与 Ni/Fe 相邻"）的关键拟合并不成立。**
- Supplementary Table 3（W L₃-edge EXAFS 拟合）**只有 3 条 W–O 路径（1.92/1.94/1.99 Å），没有配位数 N 列，也没有任何 W–Ni/Fe 路径**——尽管表注写了 N，正文也说第二壳层"matching with model-based EXAFS fitting (Supplementary Fig. 25 and Supplementary Table 3)"。
- Supplementary Fig. 25 里按图看，拟合曲线过了第一壳层就归零，而测量谱在 2.5–3 Å 明显还有第二壳层强度：**拟合并没有描述第二壳层**。
- Supplementary Fig. 43 里的 1.53 Å 是 **FEFF 正向模拟**（对两个自己设定的模型），且 OH* 与 O* 两个模型给出同一峰位——它只能说明"我的模型也预测不变"，**不能用来判断 W 是否结合中间体**。
- 另外措辞有滑移：摘要/Fig 6 说 W 是 **"subsurface"**（次表层），表征部分只说 **"substitutional octahedral / in-layer substitution"**。真正证明"在第二层、因此不可能结合吸附物"的是 DFT 模型假设，不是实验。

**⑥ 缺决定性的判别实验。**
- 主张 MvK 却**没有 ¹⁸O 同位素标记 / DEMS**；TMAOH 与 pH 只给了定性曲线，**没有 dE/dpH 斜率或反应级数**（SI 里检索不到）。
- TOF 按 Methods 是"以 ICP 全部金属原子数为分母的下限"，**算不出 per-W 的转换频率**——无论 W 是否参与，这套数据都无法回答。
- 对照不匹配：ICP-AES（Supplementary Table 2）显示 Fe/(Ni+Fe) 为 W₁ 0.356 vs NiFeOOH 0.331（相对差 ~7.5%），且 W 取代了 Ni/Fe；Fe 含量对 NiFeOOH 活性极敏感。审稿人问的"Fe-free KOH / Fe 污染监测"在正文与 SI 中都没有交代。

**⑦ 补充一句审稿背景**：随文的透明同行评议文件只含最后一轮两位审稿人的意见（Reviewer #3 的原始意见不在其中），其中**没有任何人质疑 W/Ir 的位点归属**，唯一与机制相关的技术性要求（U 敏感性、Fe 污染控制）在最终版里只落实了一半。也就是说，这个机制主张**没有经过针对性的同行压力测试**。

---

## 四、总体判断

**说服力评级：方向可信，但"W 不直接参与反应"是过度断言。**
- 若把结论弱化为"**W 在 OER 条件下不是经典的氧化还原活性金属中心；其增益主要依赖于宿主 Ni–O–Fe 边面位点**"——现有证据（原位 XAS 的方向性对比 + 载体依赖 + DFT 位点排序）**是支持的**。
- 但论文实际写的是"W 只促进邻近位点"（摘要/引言/讨论的确定语气，甚至 "unambiguous catalytic mechanisms"）。要下这个结论，还缺三样东西：**(i) 一个能排除"W 直接参与"的正向判别实验；(ii) 不是量在噪声里的原位证据；(iii) 支撑结构前提的定量拟合。** 而且第 ① 条逻辑缺口是结构性的：**用金属价态不变去否认直接参与，与他们自己主张的晶格氧机制是冲突的。**

如果要我作为审稿人提修改意见，会要求：
1. 给出 XANES 价态校准线、参考物、误差（或重复测量的误差棒），并解释 Ir 的 +2.17 vs 圖中 2.78、以及 "close to +6" vs +5.07 的出入；
2. ¹⁸O 标记 + DEMS/operando Raman，直接看 W–O 与 Ni–O 的氧交换是否发生；
3. 变 W 含量系列，并把活性归一化到位点数（或给出 per-W/ per-Ni 的位点计数），而不是 ICP 总金属量的 TOF 下限；
4. operando W L₃-edge EXAFS 的**第二壳层/差分谱**（比白线位移敏感得多），看 W 配位是否随电位变化；
5. DFT 补 U 与羟基化/显式溶剂/电位的敏感性分析，并给出 W 位点与 Ni–O–Fe 位点能量差的误差范围；
6. 一个"W 被埋在体相 vs 暴露于表面"的对照，以检验"subsurface/promoter"的空间假设。

*核查范围说明：我读取了 PMC 全文、Nature 版 PDF 的图、61 页 Supplementary Information、Source Data 工作簿与透明同行评议文件；Supplementary Data 1（结构文件 .docx）在材料包中不可得，故未能核查 DFT 模型与坐标；未重跑 DFT、未重做 EXAFS 拟合。文中标注"我算的"数字均由 Source Data 数值直接计算得到。*

参考：[原文（Nature Communications）](https://www.nature.com/articles/s41467-026-68735-3)
````

### T7

#### 三组共同的用户输入原文

````text
所需论文材料位于 materials；可以按需要读取，并使用现有检索工具。

这篇论文用的是主动学习吗？和直接拿预训练模型做筛选有什么区别？
````

| 组 | 主会话成功加载的 skill（实际顺序） | 耗时/s | 未缓存输入 | 缓存读取 | 输出（含推理） | 总 token | 请求数（含委派） |
|---|---|---:|---:|---:|---:|---:|---:|
| A | 无 | 58.5 | 53,644 | 371,963 | 7,617 | 433,224 | 12（委派 0） |
| B | `reading-contract` | 60.5 | 29,219 | 257,536 | 8,854 | 295,609 | 11（委派 0） |
| C | 无 | 70.8 | 44,815 | 664,192 | 10,315 | 719,322 | 17（委派 0） |

#### T7-A 最终输出原文

````text
## 结论

**这篇论文不是主动学习（active learning）。** 它是一条"预训练模型 → 一次性离线微调 → 对全候选空间穷举式高通量筛选 → 挑出 1–2 个候选 → 实验验证/机理解释"的单向流水线，没有主动学习必需的迭代闭环。

标题里的 "active" 指的是**活性位点/活性 motif**（Ni–O–Fe bridge 等），不是 active learning。全文唯一出现 "active machine learning" 的地方是参考文献 29（Zhong et al., *Nature* 581, 178 (2020)，CO₂ 电催化剂主动学习），属于"高通量筛选"背景引用，不是本文方法。材料里（正文、Methods、Supplementary Information、Source Data、Peer Review File）都检索不到 "active learning / uncertainty / acquisition function / Bayesian / ensemble variance" 等方法学痕迹。

---

## 一、论文实际的 ML 流程（逐段对照证据）

| 步骤 | 做法 | 出处 |
|---|---|---|
| ① 构建候选空间 | K⁺ 插层 γ 相 oxyhydroxide 为基底，8 种 M_A M_B OOH × 41 种单原子 M₁ × 13 种吸附位点（edge 01–12 / basal 0001）→ **3,976 个构型**；每个构型考虑 \*V/\*OH/\*O/\*OOH → **>15,000 个吸附结构** | 正文 "Machine learning-guided catalyst screening"；Supplementary Fig. 1 |
| ② 选底座模型 | 用 GemNet / PaiNN / DimeNet++ 等在**自建 DFT 数据集**上做基准比较，选定 EquiformerV2（OC22 预训练，121M） | 正文；Supplementary Figs. 3–4 |
| ③ 一次性微调 | 仅在 **M₁–NiNiOOH 子集**上微调（12 epochs、batch 8、dropout 0.1、AdamW、lr 2e-4），证明可迁移到未见过的二元 M₁–NiFeOOH | Methods "Machine learning processes"；Supplementary Table 1；Figs. 5–8 |
| ④ 筛选 | **用"原始预训练 backbone"（注意：不是微调后的模型）** 对全部 3,976 个构型做 BFGS 迭代弛豫，算总能量与受力 | 正文第 209–217 行明确写 "using the original pretrained EquiformerV2 backbone model" |
| ⑤ 出候选 | 火山图/2D 活性图 → W₁–NiFeOOH 与 Ir₁–NiFeOOH | Fig. 1c–e |
| ⑥ 验证 | 电沉积合成 + HAADF-STEM/XAS/Raman + DFT 机理计算 | Figs. 2–6 |

关键点：**微调只用于"验证可迁移性"（Supplementary Figs. 5–8），筛选本身用的是未微调的预训练模型**。也就是说，连"用自己微调过的模型去筛"都没做，更谈不上多轮迭代。

## 二、为什么这不构成主动学习

主动学习的判据是三件事同时具备：
1. **有不确定度/多样性驱动的采集函数**（ensemble variance、evidential、Bayesian、farthest-point…）；
2. **有选择性地向"昂贵标签源"（这里是 DFT）请求新增标签**，而不是无差别全标注；
3. **带反馈的迭代循环**：代理模型 → 选批 → DFT 标注 → 重新训练 → 更新排序，直到收敛。

本文对照：

| 主动学习要素 | 本文实际情况 |
|---|---|
| 不确定度量化 | 无。只报告 MAE/parity plot（点估计） |
| 采集函数/批次选择 | 无。候选空间是**规则枚举**出来的，不是"选"出来的 |
| 迭代重训练 | 无。微调只发生一次，且发生在筛选之前；实验与 DFT 结果**不回灌**到模型 |
| 标签预算意识 | 无。自建 DFT 数据集是为了 benchmark + 机理，不是为了"省 DFT 调用" |
| 反馈闭环 | 只有"预测 → 实验/DFT 验证"的单向闭环（人/实验在环），**模型参数不更新** |

反过来，作者**有理由**不做主动学习：ML 推理比 DFT 快约 3 个数量级（Supplementary Fig. 3，最优点约 1158× 单点加速），因此对 1.5 万个结构**穷举枚举**反而比设计采集循环更省事。主动学习的核心价值（在标签昂贵时提高样本效率）在这里被廉价推理抵消了。

## 三、那它和"直接拿预训练模型做筛选"到底差在哪？

**严格说：论文的筛选这一步，本身就是"直接拿预训练模型做筛选"。** 它与"裸用预训练模型"的差别不在学习方式，而在**验证与解释的厚度**：

1. **多模型基准比较**：不是随手拿一个 pretrained 模型，而是在自建 out-of-domain DFT 数据集上比了 GemNet/PaiNN/DimeNet++ 等，说明为什么选 EquiformerV2（MAE 0.408 eV、~1158× 加速）。
2. **做了域适配探测**：一次性微调证明 OC22 → M₁–NiNiOOH 可迁移，且在**未见过的二元 M₁–NiFeOOH** 上吸附能 MAE < 0.2 eV。
3. **DFT 机理复核**：对 4 类代表性活性 motif 用 DFT 复核，并用于后续机理讨论。
4. **实验验证与端到端闭环**：真的合成、表征、测 OER/AEMWE（13.1 A cm⁻² @ 2.0 V、500 h）。

所以更准确的定位是：**"预训练 MLIP 高通量穷举筛选（one-shot transfer learning）+ 实验验证"**，属于"ML-guided screening / high-throughput screening"，不属于"active learning"，也不属于"closed-loop autonomous discovery"。

## 四、由此带来的可质疑点（如果按 AL 的标准审视）

- **外推风险**：候选体系（K⁺ 插层 γ 相 oxyhydroxide 板模型）明确在 OC22 训练域之外（正文自己承认 "not included in the original OC22 training domain"），而 3,976 个构型的排序几乎完全依赖该模型的点预测；DFT 校验只覆盖 4 个代表性 motif。
- **误差与信号同量级**：微调模型对未见二元体系的吸附能 MAE < 0.2 eV，而 OER 决速步能差常在同一量级，火山图顶部的"最优/次优"排序（W vs Ir）很容易被系统偏差翻转——论文后文也承认 Ir 的 DFT 值与实验趋势存在需要"reconcile"的偏差（Supplementary Fig. 52 及相关讨论）。
- **筛选模型 ≠ 验证模型**：正文强调微调提升了精度，但真正跑 3,976 个构型的是**未微调**的 backbone，这条逻辑链在论文中并未解释。
- 没有不确定度量化，因此无法知道"W₁–NiFeOOH 排第一"与"第 2–10 名"是否在模型误差内不可区分。

## 五、如果要做成主动学习，这里会长什么样

起点用一个小的 DFT 种子集（如 unary NiOOH）微调 → 用 ensemble 方差/证据回归或潜空间最远点，从 3,976 × 4 个中间体的池子里挑一批（比如每轮 20–50 个）做 DFT → 重训 → 看火山图排序是否稳定 → 重复 3–5 轮，最后才对前几名做实验。判别标准是"用了多少次 DFT 调用达到同样排序"，而本文用的是"一次性把 1.5 万个结构全部推理一遍"。这与本文的实际做法有本质区别。

---

**一句话回答**：不是主动学习；它本质上是"用 OC22 预训练的 EquiformerV2 对 3,976 个候选做一次穷举筛选"，加了一次离线的域适配微调和 DFT/实验验证——比裸用预训练模型多了验证环节，但模型只学了一次，既没有不确定度驱动的采样，也没有任何迭代重训练。
````

#### T7-B 最终输出原文

````text
## 结论

**不是主动学习（active learning）。** 这篇论文用的是**"预训练图神经网络 + 一次性高通量筛选"**（zero-shot / one-shot screening），微调只是用来**验证迁移性**，并没有进入"筛选—标注—重训"的闭环。

论文：Kim, Kwon, Lim et al., *Machine-learning-guided tungsten single atoms promote oxyhydroxides for noble-metal-free water electrolysis*, [Nat Commun 17:2344 (2026)](https://doi.org/10.1038/s41467-026-68735-3) / [PMC12979610](https://pmc.ncbi.nlm.nih.gov/articles/PMC12979610/)。下面行号指本目录 `materials/pmc-fulltext.txt`（PMC 已发表版转换文本）。

---

## 一、读到的证据（逐条带定位）

| 断言 | 原文（逐字） | 定位 |
|---|---|---|
| 骨干模型是**预训练**的 EquiformerV2(OC22) | "The ML framework was implemented using the EquiformerV2 model, pretrained on the OC22 dataset." | Methods "Machine learning processes"，L419 |
| 筛选是**固定候选库的一次性全枚举**，不是自适应采样 | "creating a combinatorial candidate space from 8 different metal oxyhydroxides … with 41 elements of single-atom (M1) and 13 types of possible adsorption sites …, resulting in 3976 configurational candidate models"；"over 15,000 adsorbed structures" | L281 |
| **正式筛选用的是原始预训练骨干**，不是微调后的模型 | "High-throughput screening of all M1–MAMB OOH candidates was performed using the original pretrained EquiformerV2 backbone model" | L285 |
| 微调的目的被限定为"验证迁移性" | "Fine-tuning of the pretrained model was conducted exclusively on the M1–NiNiOOH subset to assess transferability to binary compositions." | L445 |
| 微调数据是**一次性人工构造的 DFT 集**（对应四个代表性活性基元） | "we generated a custom DFT dataset by selecting structures corresponding to four representative active motifs illustrated in Fig. 1b, derived from unary NiOOH and binary NiFeOOH systems" | L281（另见 SI Supplementary Fig. 2） |
| 筛选依据是火山图排名 | "The OER volcano plot was employed to definitively identify W1–NiFeOOH and Ir1–NiFeOOH as the most promising candidates" | L285 |
| 摘要自述为"out-of-domain"零样本预测 | "An equivariant transformer-based machine-learning interatomic potential accelerates out-of-domain adsorption energy predictions and nominates W1-NiFeOOH from 3,976 … configurations." | 摘要 L249 |

**"active learning" 在本材料中只出现一次，且是引文**："Zhong, M. et al. Accelerated discovery of CO2 electrocatalysts using active machine learning. Nature 581, 178–183 (2020)."（参考文献 29，L577）——它出现在引言罗列"ML 使能高通量筛选"的那句话里（L265），是**背景引用**，不是本文方法。

**阴性断言的检索范围**（按 reading-contract 要求说明）：我在 `materials/pmc-fulltext.txt`、`materials/nature-landing.txt`、以及我用 pypdf 抽取的补充材料全文（`artifacts/supplementary.txt`）和同行评审文件（`artifacts/peer-review.txt`）中检索 `active learn / iterative learn / uncertainty / ensemble / acquisition / Bayesian optimi / closed-loop / autonomous`，除上述参考文献 29 外**无任何命中**。因此可断言：这些记录中没有出现采集函数、不确定性量化或模型重训闭环。这不等于"整个领域没有"，只等于"本文这些材料里没有"。

---

## 二、两个容易被误读成"主动学习"的地方

1. **有 fine-tuning**。微调常被误当主动学习，但两者正交：微调是"用一批**事先准备好的**标签把预训练权重适配到新域"，是离线、单向的一步；主动学习是"让模型**决定下一批问谁要标签**"的在线循环。
2. **Methods 里有 "iteratively" 一词**——但那是 BFGS 几何弛豫的迭代，不是学习循环："applying the pretrained EquiformerV2 model to rapidly evaluate the total energies and atomic forces of the model systems **iteratively towards the equilibrium geometry with the BFGS algorithm**"（L419）。这是我要特别提示的陷阱：该词与模型迭代训练无关。

---

## 三、主动学习 vs. 直接用预训练模型筛选：机制差别

| | 主动学习（AL） | 直接用预训练模型筛选（本文实际做法） |
|---|---|---|
| 循环结构 | 模型 → 采集函数 → 选批 → DFT 标注 → 重训 → 重复多轮 | 固定候选库 → 单次前向推理 → 排名 → 取 top 候选 |
| 谁来选点 | **模型**按不确定性/多样性选（需要 ensemble、方差、或贝叶斯采集函数） | **人**事先枚举（8 基质 × 41 单原子 × 13 吸附位） |
| 新标签的角色 | 每轮产生的新 DFT 标签**回流**改变模型，进而改变下一轮选择 | DFT 子集只用于**离线验证/微调检查**，不改变候选排序 |
| 什么时候停 | 预算/收敛准则 | 库枚举完即停 |
| 主要收益 | **标签效率**：把昂贵的 DFT 花在信息量最大的点上 | **零训练成本、即时**：但可信度完全依赖迁移性 |
| 主要风险 | 需要可靠的 oracle 与不确定性估计；轮次多、工程复杂 | **域偏移**导致的系统性偏差可能悄悄改变排名 |

按这个判据，本文属于右列。**不是"AL 的一种"，也不是"AL 的简化版"，而是另一种范式。**

---

## 四、那它和"直接拿预训练模型筛选"到底差在哪？（我的判读，标注为推断）

**推断 1：从机制上说，本文的筛选环节就是"直接拿预训练模型筛选"**——原文明确说筛选用的是 original pretrained backbone（L285），而不是那个 MAE 更低的微调模型。差别只在**论证结构**：作者补了三层可信度论证来支撑这次零样本筛选：

- 与 GemNet / PaiNN / DimeNet++ 等基线在自建 DFT 弛豫集上做基准，选出 EquiformerV2（L283）；
- 在 M1–NiNiOOH 子集上微调，再测**未见过的** M1–NiFeOOH：吸附能 MAE < 0.2 eV，用来界定适用域（L283、L445，SI Figs. 7–8）；
- 内部一致性检查：复现了 *OOH–*OH 线性标度关系，且与既往实验趋势（NiFeOOH、CoFeOOH 最低势垒）一致（L285）。

**推断 2：这里存在一处值得注意的张力。** 论文报告了微调带来的精度提升（L283："MAE less than 0.01 eV atom⁻¹"），但实际筛选用的是未微调的骨干（L285）。因此**微调的精度数字并不能直接为筛选预测背书**；换用微调模型后火山图顶点的排序是否会变，论文没有报告。这属于方法学上的一个可追问点，不是错误——原文对"筛选用哪个模型"是明确披露的。

**推断 3：对该体系而言，主动学习的边际收益有限。** AL 的核心卖点是省 DFT 标签；而这里候选空间约 3976 个构型 × 4 个中间体，单次 GPU 推理比 DFT 快约 3 个数量级（L283，SI Fig. 3），全量枚举本身就可承受。AL 真正可能补上的，是**用自适应采样去修正域偏移**、以及**跳出人工枚举的基元清单**去发现枚举之外的构型——这两点是"直接筛"的结构性短板，而不是靠"多跑几轮"就能自动解决的。

**一句话回答第二问**：如果问"主动学习 vs 直接预训练筛选"——差别在**谁决定下一批算哪个点、以及新标签是否回流改变模型**；如果问"这篇论文 vs 直接预训练筛选"——二者在机制上是同一件事，差别只在于前者额外做了基准比较、迁移性微调和标度关系复现来**为这次零样本筛选的可信度作证**。

---

## 五、分层说明

- **读到的（read）**：第一节表格中所有带行号的引文，均在本会话中打开 `materials/pmc-fulltext.txt` 核对过；补充材料/评审文件是我用 pypdf 抽取到 `artifacts/supplementary.txt`、`artifacts/peer-review.txt` 后检索的（抽取文本含排版噪声，涉及具体数值时我只引用了正文陈述）。
- **推断的（inferred）**：第四节全部内容，以及"AL 边际收益有限"的判断；均基于上文已列出的读到的原文。
- **未核验的背景（background，不用于承载结论）**：主动学习的一般范式描述来自我的领域记忆，未在本次材料中检索文献佐证；若需要"本文与 AL 工作流对比"的文献级论证，应另做一次针对 AL-for-catalysis 的检索。
````

#### T7-C 最终输出原文

````text
## 结论先说

**这篇论文没有用主动学习（active learning）。** 它做的是**"预训练模型零样本高通量筛选 + 一次性微调/迁移性验证"**，是一条开环（one-shot）流水线，不含"不确定性选样 → 补算 DFT → 重训"的迭代闭环。

我在正文、Methods、补充材料（61 页）和透明同行评审文件里全文检索过 `active learning / uncertainty / acquisition function / committee / retrain / loop` 等关键词：**除了 DFT 自洽场迭代和 BFGS 几何弛豫的 "iterative/loop"，没有任何主动学习相关表述**。同行评审意见也只提到 "ML screening + DFT validation"，没有人讨论过 AL。

---

## 一、论文实际的 ML 工作流（四步，全部为一次性）

| 步骤 | 具体做法 | 出处 |
|---|---|---|
| ① 复用预训练模型 | 直接用 OC22 上预训练的 **EquiformerV2**（18 层、8 头、128 sphere/hidden channels、max degree 6）作 backbone | 正文 §Machine learning-guided catalyst screening；Methods §Machine learning processes |
| ② 事前基准测试 | 自建一个 DFT 数据集（从 unary NiOOH / binary NiFeOOH 中选 **4 个代表性活性基元**），对比 GemNet、PaiNN、DimeNet++ 与 EquiformerV2，选出精度最高且比 DFT 快约 3 个数量级者 | 补充 Fig. 3、Fig. 2 caption |
| ③ 一次性微调 | 在 **M₁–NiNiOOH 子集**（预先挑好的固定数据集）上微调 12 epochs（A100，batch 8，dropout 0.1，AdamW lr 2e-4，energy/force loss 权重 4/100，grad clip 50，EMA 0.999），目的写明是 *"to assess transferability to binary compositions"* | Methods；补充 Table 1、Fig. 4–8 |
| ④ 高通量筛选 | **关键**：筛选明确用的是 **"the original pretrained EquiformerV2 backbone model"**，不是微调后的模型。对 8 种 M_A M_B OOH × 41 种单原子 × 13 个吸附位 → **3,976 个构型 / >15,000 个吸附结构**做 BFGS 弛豫（max force < 0.03 eV Å⁻¹，A6000），再用 volcano plot 挑出 W₁–NiFeOOH 与 Ir₁–NiFeOOH | 正文 §Machine learning-guided catalyst screening；Methods |

微调的效果：总能量 MAE < 0.01 eV atom⁻¹，对**未见过的** binary M₁–NiFeOOH 吸附能 MAE < 0.2 eV；补充 Fig. 4 给出 0.191 eV（微调）vs 0.408 eV（baseline）。但**这些数字只用于论证"可迁移"，没有回流到筛选结果里**。

**主动学习的四个必备要素，本文一个都没有：**
1. ❌ 迭代闭环（多轮 train → screen → label → retrain）
2. ❌ 不确定性量化 / 采集函数（ensemble variance、MC dropout、GP variance、expected improvement 等）
3. ❌ 由模型（而非研究者先验）决定"下一个该算哪个 DFT"
4. ❌ 用最终迭代模型去做筛选（本文筛选用的是原始预训练模型）

它的 DFT 样本是研究者按化学直觉选的"4 个代表性基元"，属于**先验设计**，不是**不确定性驱动**。所以这是 **transfer learning / foundation-model screening**，不是 AL。

---

## 二、和"直接拿预训练模型做筛选"有什么区别？

**就"筛选"这一步本身：几乎没有区别。** 论文自己写明了筛选用的是原始预训练 backbone，所以第 ④ 步就是教科书式的"直接拿预训练模型做筛选"。

区别在于它在这个核心步骤外面包了**两层可信度包装**：

- **事前**（步骤②）：横向 benchmark 4 个 GNN + 自建 DFT 集，回答"为什么选 EquiformerV2"；
- **事后**（步骤③）：在 M₁–NiNiOOH 上微调、再在没见过的 M₁–NiFeOOH 上算误差，回答"这个预训练模型在目标域大概能信到什么程度"。

这两层**不改变候选排名，也不改进筛选模型**，只是提供证据。所以更准确的描述是：

> 本文 = 直接预训练筛选（得到 W₁–NiFeOOH）+ 一次独立的迁移性/误差验证实验（不参与筛选）。

这也正是它与主动学习的本质差别——AL 会把"验证得到的误差信息"反过来用在"下一步该算哪个结构"上，形成闭环；本文是开环，误差信息只用于写 parity plot。

| 维度 | 本文做法 | 主动学习做法 |
|---|---|---|
| 训练标签来源 | 研究者先验挑的 4 个活性基元 | 采集函数按不确定性/多样性挑 |
| 流程结构 | 线性、单次 | 多轮闭环 |
| 重训次数 | 1 次（12 epochs） | 每轮重训 |
| 不确定性 | 完全不用 | 核心机制 |
| 最终用于筛选的模型 | **原始预训练 backbone** | 迭代精化后的模型 |
| 优势 | 简单、可完全并行、候选空间可枚举时足够 | 标签效率高、能自动暴露模型盲区 |
| 风险 | 域外误差与排序鲁棒性无量化保证 | 实现复杂、不确定性估计本身可能不可靠 |

---

## 三、为什么这里"不用 AL"在方法上是可以接受的（但仍有代价）

论文的候选空间只有 **3,976 个构型**，且筛选是**纯推理**（不需要为每个候选算 DFT 标签）。AL 的核心卖点是"在固定标签预算下用最少的 DFT 换最好的模型"；当候选空间可全枚举、推理又便宜时，**直接预训练筛选本来就是合理选择**，AL 的边际收益有限。

但要注意本文为这个选择付出的代价，有三点值得你在引用/评审时留意：

1. **筛选本身是零样本域外预测。** 论文自己承认这些几何结构 *"represent catalytically relevant systems not included in the original OC22 training domain"*。整篇论文的头号结论就建立在这次零样本预测上。
2. **3,976 个预测没有任何不确定性。** 因此"W₁ 优于其他候选""W₁ 优于 Ir₁"的排序稳健性无法量化。而互补证据（补充 Fig. 52）显示：Ir₁ 的 DFT 与实验趋势原本对不上，是靠**事后追加羟基化 Ir 构型**才调和的——这正是"单一固定模型 + 固定基元集"容易漏东西的典型症状，也正是 AL / 不确定性驱动采样想解决的问题。
3. **微调模型精度明显更好，却没用于筛选。** 论文报道微调后吸附能 MAE 0.191 eV 远优于 baseline 0.408 eV，但筛选仍用 baseline；作者的解释是微调只在 unary NiNiNiOOH 上做过，对其它 M_A M_B 组分推广性未知，所以只当作迁移性验证。逻辑上说得通，但读者会很自然地追问："那为什么不筛两遍、比对两套排名？"——这恰恰是本文没有做的事。

---

**一句话总结**：这是一篇标准的"**预训练基础模型 + 一次性微调验证 + 全域枚举高通量筛选 + 实验验证**"工作；ML 部分是开环的，不是主动学习。它和"直接拿预训练模型做筛选"在筛选结果上没有方法论差异，真正的增量是**选型基准测试 + 跨组分迁移性检验**这两层证据，以及后续完整的实验与机理表征。

（依据材料：`materials/pmc-fulltext.txt` = `nature-article.pdf` 全文；`supplementary-information.pdf`（已抽文本核对 Methods/Fig. 2–8/Table 1）；`peer-review-file.pdf`。）
````

## 第二部分：实际运行与资源审计

### 1. “调用成功”如何判定

本次分开记录四层：目录可见、成功返回技能正文、执行了可观察的相应步骤、最终答案是否可靠。前一层不自动证明后一层。以回答中的“我用了某技能”作为自述，不作为调用成功证据；以原始 skill 工具调用和对应成功返回的 `<skill_instructions>` 作为加载证据。通过 read/pwsh 直接读取 SKILL.md 也在检索范围内，没有发现可补足其他 router 调用的读取。

主会话共成功加载 17 次：A 0 次、B 6 次、C 11 次。B、C 各有 6/7 道题加载了至少一项技能；B 的 T2 和 C 的 T7 没有加载技能。委派会话另有 16 次成功加载（B 8 次、C 8 次），所以全体日志共 33 次。T5-B 子会话中包括 lit-review ×5、reading-contract ×2、paper-lookup ×1；T5-C 子会话中 lit-review ×8。重复加载体现上下文和执行开销，并不等于八份独立高质量证据。

A 也有外部检索、代码执行和子代理，因此 A 不是“裸聊天”，而是“有同类工具能力、没有项目 skill 目录/工具的 agent”。A/B 差异同时包括目录注入、skill 工具暴露及实际选用行为。不能把全部资源差异解释为 skill 正文本身的长度。

### 2. router 的关键配置缺口

计划文件称 C 组应先读 router，规则确实位于 `profiles/C/DSH_HOME/AGENTS.md`。但 `tools/run-experiment.ps1` 将运行的 `DSH_HOME` 设置为 `runs/<任务-组>/.harness-home`，没有把该规则复制或注入实际运行位置。逐一解码 21 个主会话的初始 system/user/request 记录，没有发现该规则原句，也没有发现三组配置文件共同的任务说明段落。所有 C 的初始技能目录均有 router，A/B 没有。

因此，这轮实际检验的是 **C 比 B 多暴露一个 router 条目时的行为**，不是“强制路由与不路由”的严格对照。原计划中“不能测自发触发”的描述与实际执行不相符；本轮可报告的只是 router 在这些题中被观察到加载 1/7 次，不能把这个小样本比例推广为宿主稳定触发率。

唯一成功加载 router 的是 T1-C。该运行还实际读取其 `references/doi-paper-analysis.md`，随后加载 reading-contract、scientific-critical-thinking，进行了论文/补充材料读取和数字核查。它给出了一个路由链确实可以运行的实例，但只有一个实例，不能单独证明路由提高质量或降低消耗。其余 6 个 C 运行没有 router 加载证据；例如 T5-C 的大消耗不能称为“router 运行开销”。

### 3. 委派完成状态：不能沿用汇总口头说明

| 运行 | 子会话数 | 主回复前正常结束 | 被中止 | 未记录 turn/end | 能确认什么 |
|---|---:|---:|---:|---:|---|
| T5-A | 4 | 3 | 1 | 0 | 不是全部仍在运行；1 个子会话记录 parent 原因中止 |
| T5-B | 5 | 5 | 0 | 0 | 均在主 turn/end 前正常结束；正常结束本身不认证内容正确 |
| T5-C | 8 | 1 | 0 | 7 | 7 个日志停在工具调用/step/投递事件，没有结束记录；不能推定之后完成 |

依据为每个持久化会话的 `turn/end` 类型、时间与主会话结束时间。T5-C 的最终文本自称“六位检索代理仍在运行”，而日志中缺少结束记录的是七个子会话；一个是生成时的自述，一个是记录结束时的可核查状态，不能将两者强行等同。未采集到的后续状态不填补为完成或永久失败。

T5-C 同时出现 workflow 脚本语法错误、两次触及 8 个活跃子代理上限。父子会话实际发起 630 次模型请求，记录 63,638,958 token。过程具有明显的扩展与收尾问题；不能因为运行进程 exitCode=0 或主 turn/end=completed 就把整个检索工作流认定为完成。

### 4. token 与耗时对比

| 组 | 全7题总 token | 全7题耗时/s | 排除T5的总 token | 排除T5的耗时/s | 单题总token中位数 | 单题耗时中位数/s |
|---|---:|---:|---:|---:|---:|---:|
| A | 14,700,192 | 1,680.5 | 7,423,422 | 1,316.6 | 638,724 | 127.4 |
| B | 40,121,875 | 3,575.2 | 14,533,089 | 2,284.0 | 3,148,644 | 294.2 |
| C | 77,059,739 | 2,557.1 | 13,420,781 | 1,459.3 | 2,002,755 | 362.6 |

全题总 token 比值 B/A=2.73、C/A=5.24、C/B=1.92。排除 T5 后 B/A=1.96、C/A=1.81、C/B=0.92。排除 T5 是敏感性展示，不是删除不利样本后宣布获胜；T5 属于真实目标任务，必须保留在主结果中。C 的总耗时低于 B，但单题耗时中位数更高，说明少数慢任务（特别 T4-B）会改变汇总印象。

| 任务 | B/A token比 | C/A token比 | C/B token比 | C/B耗时比 |
|---|---:|---:|---:|---:|
| T1 | 1.20 | 1.39 | 1.16 | 1.04 |
| T2 | 1.96 | 1.87 | 0.96 | 1.11 |
| T3 | 1.24 | 2.78 | 2.25 | 1.24 |
| T4 | 3.16 | 1.27 | 0.40 | 0.31 |
| T5 | 3.52 | 8.75 | 2.49 | 0.85 |
| T6 | 4.93 | 4.77 | 0.97 | 1.23 |
| T7 | 0.68 | 1.66 | 2.43 | 1.17 |

总计 131,881,806 token，其中缓存读取 127,409,657（96.6%）、未缓存输入 3,116,408、输出（含推理）1,355,741。缓存 token 仍代表重复上下文处理和通常不同的计费类别，不能当作零开销，也不能与新输入/输出套一个价格。T5 占 73.2% 总 token，全部 863 次委派请求集中于 T5；这一题的工作流扩张主导整体资源结果。

上述数字用独立脚本通过 libzstd 流式解压 38 份日志、逐条累加带 usage 的 assistant/message 重新得到，与交付报告逐运行一致。原组织方脚本会跳过不能解压的帧，本次核对没有依赖其跳过逻辑。这里认证的是已记录 usage 的一致性，不是账单最终结算；中断请求或没有返回 usage 的请求是否计费，仍需服务端账单验证。

T5 的主会话与委派用量进一步拆分如下，避免把子代理花费漏掉：

| 运行 | 主会话 token | 委派 token | 委派占本运行 |
|---|---:|---:|---:|
| T5-A | 5,515,522 | 1,761,248 | 24.2% |
| T5-B | 6,517,641 | 19,071,145 | 74.5% |
| T5-C | 13,885,218 | 49,753,740 | 78.2% |

### 4.1 目录注入成本与后续执行成本可以部分拆开

逐题比较首个模型请求的逻辑输入（未缓存 + 缓存读取 + 缓存写入），七题均得到相同差值：B 比 A 多 **4,049 token**；C 比 B 多 **78 token**。A 首请求范围 5,761–5,794，B 为 9,810–9,843，C 为 9,888–9,921。这个测量发生在任何技能正文加载之前，因此对应本轮初始暴露的目录/工具等上下文差异，不是全部技能正文已经加载。

这说明额外暴露 router 目录条目的初始开销很小，但不能据此认定完整 router 路线一定便宜；也不能把 T5 的数千万 token 差异归结为这 78 token。后续多轮历史重传、技能载入、检索正文、代码和委派才构成累计量。未逐请求做反事实重放，所以不将这些因素拆成相互独立的精确归因份额。

### 5. 调用后的可观察行为与依赖限制

- T1-C：router → DOI 路线 → reading-contract / scientific-critical-thinking 可观察，附引用定位及数值核查；成功执行这条链不保证每条科学判断正确，质量另由盲审处理。
- T4-B/C：paper-lookup 被加载；C 还加载 literature-search-openalex。可观察到数据库/文献查找和补救路径，但工具加载不是全文获取保证。多次 web_fetch 返回 non-public IP 错误，随后使用其他现有访问方法。
- T5-B/C：lit-review 成功加载并实际分派检索、形成账本/中间材料。该上游协议明确要求按谱系搜索、对严肃新意主张覆盖六至十二角度、迭代直到新检索不再增加证据。它能解释为什么这类任务容易扩展，但并不能量化该技能的净因果开销：A 未加载技能也启动了四个子会话；C 的并行数量与失败重试又不同。
- T3 的 B/C 都加载 reading-contract，但仍需独立核验最终事实。T6 的 B/C 均加载 scientific-critical-thinking，C 又加 reading-contract；要看这些额外操作是否对应更可靠的判断，不能用批评条数代替质量。
- T7-C 没有实际加载任何 skill；其性能不能作为“router 调用效果”的证据。T2-B 同样不能当作具体技能成功执行的例子。

以上记录只描述可见指令载入、工具动作、返回状态、产物与时间，不转载模型的隐藏思考，也不把内部自述当成过程证据。

### 6. 资料补记需要纠正的地方

原 group-io-report 的“外部文件未纳入本文件”成立，但运行树中保留了大量 artifacts，不能扩写为“本次实验没有任何产物可核对”。本次只用产物存在性和执行记录辅助过程核验，没有把附件加入最终回答质量评分，也没有全面认证附件内容。外部成果的正确性与可交付性仍是另一个评价范围。

limitations-index 的 29 条摘录位置均真实，但分类有误报、句子截断和漏报；例如数据库列表不是访问受限，期刊缩写处截断会丢失限定，原论文证据不足不是模型工作未完成。该索引未交给独立评审，以免标签引导判断。评审依据匿名回复全文自行识别限制。

### 7. 材料与运行条件复核

另行 SHA-256 检查了 21 个运行目录中的 10 份共同原始材料（210 个文件）及独立评审收到的 10 份副本，均与 materials-frozen 一致。各运行可能新增自用提取文件，但本次未发现共同原始文件被更改。原始持久化 request/header 也确认 21 次运行均为 deepseek-official / deepseek-flash、reasoningEffort=high、maxTokens=256000；A 暴露 23 项工具，B/C 为 24 项，差异包含 skill 工具。

### 8. 适用范围

这是一次探索性、每题每组单次的 agent 运行比较，不做显著性检验，也不宣称可重复的平均增益。论文共享、任务异质，七题不是七篇独立论文。实际外部检索的配额、付费墙、网络错误、缓存状态与随机输出都可能影响结果；顺序随机化有帮助，却不能消除这些差异。模型/宿主配置只能按保留的快照描述，不把本次结果推广至其他模型或前端。过程和内容审计已分离，但只有一个模型盲审者，不等同于化学专家组意见。


## 第三部分：独立盲审的回答质量

独立评审为不继承父会话历史的 GPT-6 Astra Medium 子代理。候选按题和回答分别随机编号、打乱；评审先建立论文事实基线，再按固定六维量表评阅。没有收到真实组别、token、耗时、配置、调用过程、旧评分或主代理发现。评审共享底层文件系统，因此是上下文和读取范围隔离，并非独立安全沙箱；单模型评审也不等同于专家组认证。

只评最终可见回答；没有把隐藏思考、工具轨迹、被引用的附件内容补给评审。保留原始论文与可联网核查能力，用于验证科学事实。仅对身份线索做了 12 处最小删改，科学结论、访问限制、未完成声明均保留，私有删改记录可追溯。原文仍完整列于第一部分。

### 六维评分总表

| 任务/组 | C1 指令 | C2 事实 | C3 引用 | C4 覆盖 | C5 判断 | C6 可用性 |
|---|---:|---:|---:|---:|---:|---:|
| T1-A | 3 | 1 | 1 | 3 | 1 | 2 |
| T1-B | 4 | 2 | 2 | 3 | 2 | 3 |
| T1-C | 4 | 2 | 2 | 4 | 2 | 3 |
| T2-A | 4 | 3 | 3 | 4 | 2 | 3 |
| T2-B | 4 | 3 | 3 | 4 | 3 | 3 |
| T2-C | 4 | 3 | 4 | 4 | 4 | 3 |
| T3-A | 4 | 3 | 3 | 3 | 3 | 3 |
| T3-B | 4 | 3 | 4 | 4 | 3 | 3 |
| T3-C | 4 | 3 | 4 | 4 | 3 | 3 |
| T4-A | 3 | 4 | 4 | 4 | 4 | 3 |
| T4-B | 2 | 4 | 4 | 4 | 3 | 3 |
| T4-C | 2 | 3 | 4 | 4 | 3 | 3 |
| T5-A | 3 | 2 | 2 | 3 | 2 | 3 |
| T5-B | 4 | 3 | 3 | 4 | 3 | 3 |
| T5-C | 2 | 1 | 1 | 3 | 1 | 2 |
| T6-A | 4 | 3 | 3 | 4 | 3 | 3 |
| T6-B | 4 | 2 | 3 | 4 | 2 | 3 |
| T6-C | 4 | 2 | 2 | 4 | 2 | 3 |
| T7-A | 4 | 2 | 3 | 4 | 2 | 3 |
| T7-B | 4 | 3 | 4 | 4 | 3 | 3 |
| T7-C | 4 | 2 | 3 | 4 | 2 | 3 |

评分用于本轮描述性比较，不是正确率，也不是重复实验的统计估计。完整量表与逐条证据如下。

# Frozen content-only rubric

Assess only each original simulated user input and visible final response, independently first, then compare within that question. Candidate IDs do not imply common identity across questions. No configuration/process/resource information is considered. No independent domain-expert certification.

Six dimensions, each0–4 (NA if truly unassessable): C1 answering question/constraints; C2 factual accuracy; C3 citation authenticity and support; C4 coverage of key content and qualifications; C5 reasoning and uncertainty; C6 expression and user utility. 0=fundamental failure/severe invention;1=major shortcomings;2=partial fulfillment with substantive shortcomings;3=generally reliable with minor problems;4=fully accurate and well matched. NA is not zero. No automatic preference for length, critical tone, citations count, or unconditional certainty.

Citation assessment distinguishes existence/identity/date from supporting the linked claim. Verify external citations where necessary, especially retrieval/novelty questions; label unavailable full texts/attachments unverified. A real DOI with wrong title or unrelated content is not correct support. No fixed right-answer percentage for open judgments.

Files mentioned but not provided: do not credit as verified completed work, do not presume nonexistent. Explicit bounded incompleteness is assessed as stated. Source inconsistencies are retained; quoting one published version is not automatically hallucination. Distinguish measured quantity, author interpretation, reviewer inference and unsupported extrapolation. Do not require exhaustive critical review for a brief explanatory question.

Each evaluation gives six scores, confidence, scope,2–5specific evidence items containing verbatim short answer quotes and precise original-source locators or external URLs, plus strengths/defects. Cross-question aggregation, if reported, is descriptive only and cannot connect anonymous IDs to identities. Freeze full quality-review.md and scores.json via SHA256 at completion.


# 匿名内容质量评审（21份完整冻结版）

量表已在候选阅读前冻结。仅评可见最终回复，未核查回答所称附件；不评过程，不知模型/配置身份。无独立领域专家认证。评分0–4，NA不计作错误。

完整基线和证据边界见 fact-baseline.md / reading-ledger.md / rubric.md。外部文献核验多数止于作者摘要、题录及部分原文片段，不能视为全文重读。


## T4（Q-69757e） / T4-B（盲审编号 R-32b0c7d5）

评分：C1=2；C2=4；C3=4；C4=4；C5=3；C6=3。置信度：中高

核查范围：逐条核对5篇主列表的题名/DOI/截止时间与可访问作者摘要；Fuel在线日期、CEJ精确在线日/部分数值未完全独立重现；额外备选未全量核验，动态被引次数及自述检索流程不据此判定。

优点：五篇主列表主题直接相关，2026边界论文排除恰当；多数方法与量化摘要准确

缺陷/限制：主表5篇后继续给7篇备选，违反最多五篇的明确约束；主表不列完整题名仅影响定位便利，用户未要求故不作覆盖扣分；早期性/引用量属非必要且未充分限定的加注。

逐维理由：

- C1（2）：主表切题，但另加7篇突破“最多5篇”（E4）。
- C2（4）：已核的材料/方法/核心数值吻合；动态引用量与部分旁支细节未知，不因无法核实推定错误（E1–3）。
- C3（4）：主列表DOI真实且摘要支撑对应工作；未核旁支加注另列未知，不降低已核引用评价（E1–3）。
- C4（4）：用户要求的DOI、主要工作与截止边界均覆盖；用户未要求完整题名，不因此扣覆盖分（E1–4）。
- C5（3）：时间边界合理；早期性及引用排名的信心略超过已呈证据（E1、E4）。
- C6（3）：主表易扫描，但额外列表稀释用户要求的精选结果（E4）。


- E1 回答短引：“均早于 2026-01-29”。依据：Main p1；PMC出版日；https://pubs.acs.org/doi/10.1021/acsami.5c20762。判断：2026AMI在线1月10日、刊期1月28日均满足，排除1月29日锚点合理。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“OER 239 mV@10 mA cm⁻²”。依据：https://pubmed.ncbi.nlm.nih.gov/33900730/ Abstract。判断：原作者摘要支持电沉积、239/115mV和1.59V。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“1000 mA cm⁻² 运行 350 h”。依据：https://pubmed.ncbi.nlm.nih.gov/38366284/ Abstract。判断：WO4插层、近100%产氧、350h和LOM均为作者摘要内容，非DOI套用。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“简要补充（未计入这 5 篇）”。依据：T4（Q-69757e）用户原文“最多五篇”；https://pubs.rsc.org/en/content/articlelanding/2020/ta/d0ta00691b。判断：主项RSC水浴NiFeW方法已证实，但将多篇叫备选不取消数量约束。 证据置信度：高（针对列明核查范围）。


## T4（Q-69757e） / T4-A（盲审编号 R-ca654fbb）

评分：C1=3；C2=4；C3=4；C4=4；C5=4；C6=3。置信度：中高

核查范围：逐条核对5篇主列表的题名/DOI/截止时间与可访问作者摘要；Fuel在线日期、CEJ精确在线日/部分数值未完全独立重现；额外备选未全量核验，动态被引次数及自述检索流程不据此判定。

优点：完整题名/DOI/在线与卷期区分清楚；5篇方法各有材料体系和内容摘要，直接实用

缺陷/限制：额外两篇候选仍超过最多五篇；Fuel依赖中文解读的复杂溶出机理，本次只核到出版社题名/亮点和局部摘要，准确程度保留未知；不因未核到全文判错

逐维理由：

- C1（3）：5篇主表满足意图，但额外两篇违反篇数上限（E4）。
- C2（4）：已核主要事实准确；Fuel细机制/精确日期无法核实部分记未知，不扣作错误（E1–3）。
- C3（4）：已核DOI/题名及对应摘要一致；Fuel另给二手解读来源，其未全文核到部分保留未知（E1–3）。
- C4（4）：题名、DOI、发表时点、材料及方法覆盖充分（E1–3）。
- C5（4）：线上与卷期边界区分清楚；本轮未能重现的Fuel细节不足以判其推理不可靠（E1–3）。
- C6（3）：按材料路线组织实用；多余候选增加不必要选择负担（E4）。


- E1 回答短引：“在线 2026-01-10（纸质 2026-01-28）”。依据：https://pubs.acs.org/doi/10.1021/acsami.5c20762 Article history/Abstract。判断：准确；该篇水热法与OER/HER数值也受作者摘要支持。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“一步醇热法可控掺 W”。依据：https://www.whxb.pku.edu.cn/EN/10.3866/PKU.WHXB202303055 Abstract/publication dates。判断：方法、W6+、Fe-W电子重分布、199/237mV与2023-08-21网上日期均匹配。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“W 自发牺牲性溶出”。依据：https://www.sciencedirect.com/science/article/pii/S0016236125026705。判断：题名/DOI、NiFeW刻蚀重构和243mV亮点可核；牺牲溶出、500h及2025-09-27在线日本次完整一级证据未获取，列未核实而非错误。 证据置信度：高（已核材料和明确关系）；部分外部细节未知见发现。


- E4 回答短引：“另外还有若干高度相关”。依据：T4（Q-69757e）用户原文“最多五篇”。判断：又列两项带DOI，轻度违背数量限制。 证据置信度：高（针对列明核查范围）。


## T4（Q-69757e） / T4-C（盲审编号 R-0642ee1c）

评分：C1=2；C2=3；C3=4；C4=4；C5=3；C6=3。置信度：高（主列表），中（附加评价）

核查范围：逐条核对5篇主列表的题名/DOI/截止时间与可访问作者摘要；Fuel在线日期、CEJ精确在线日/部分数值未完全独立重现；额外备选未全量核验，动态被引次数及自述检索流程不据此判定。

优点：5篇主列表全部可核对口、DOI与摘要匹配；明确区分纯Ni(OH)2非NiFe先例，没有将其冒充主列表匹配

缺陷/限制：备选6篇突破数量上限；“应已覆盖主要工作”缺少可验证覆盖证据，动态引用排名也不是用户所需；“像相”笔误

逐维理由：

- C1（2）：主5篇切题，追加6篇且让用户再要求“只列5篇”未遵约束（E4）。
- C2（3）：多项性能/方法准确；投料比略写成最佳成分比（E1–3）。
- C3（4）：主表DOI与摘要内容相符，日期可核；不因动态引用量未知判伪（E1–3）。
- C4（4）：DOI、主要工作、日期及非NiFe边界均清楚，覆盖用户要求（E1–4）。
- C5（3）：能排除非NiFe主匹配，但“覆盖主要工作”缺覆盖证据（E4及缺陷）。
- C6（3）：主体可用，过量备选和笔误降低精练性（E4）。


- E1 回答短引：“最佳 Ni:Fe:W = 6:2:1”。依据：https://pubs.acs.org/doi/abs/10.1021/acs.inorgchem.9b01953 Abstract。判断：6:2:1原文是投料摩尔比，答复略省略“sources”；264mV、10h1.6%及2019-09-11正确。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“约 30 h 计时电位测试后 W 发生还原”。依据：https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cssc.202002544 Abstract；review/external-metadata-Q69757e.json。判断：作者摘要明确支持，224/251mV匹配；2021-01-21为正式版本在线日，早期接受稿日期不同不构成答复错误。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“W 掺杂 NiFe LDH（NiFe-Wₓ/NF）”。依据：https://pubmed.ncbi.nlm.nih.gov/39764892/ Abstract。判断：虽题名写Ni(OH)2，摘要明确NiFe，选择切题；269mV@100、1.90V780mA、70h一致。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“若你需要"只列 5 篇、不要备选"”。依据：T4（Q-69757e）用户原文“最多五篇”。判断：用户已经提出该约束，不宜转成后续可选请求。 证据置信度：高（针对列明核查范围）。


## T3（Q-2e5cea） / T3-C（盲审编号 R-cdd913bb）

评分：C1=4；C2=3；C3=4；C4=4；C5=3；C6=3。置信度：高

核查范围：完整核对Main pp5–6、10，SI pp38–42、59，workbook Figure3/ S41，包括端点、缺口和最高半电池行；非附件或实验流程复现。

优点：核心工况区分正确，允许带条件并列而禁止合并寿命声明；源数据端点、531h、112→137h缺口和2.1V最大点均准确，明确器件身份未知

缺陷/限制：稳定性n=1只从单条公开曲线不能断言独立重复数；将1A/cm²概称不能证明“高电流密度下稳定”措辞过宽；应限定13A级；全局0.34mV/h已标算术推断但不应视为稳态衰减率，答复篇幅显著超过问题需要

逐维理由：

- C1（4）：直接回答两项结果能否合并，提供合规表述（E1）。
- C2（3）：主要工况/端点正确；独立重复n=1未明确报告（E2–4）。
- C3（4）：页图及源数据能支撑大部分关键事实（E1、E4）；n=1属推断非引用原话。
- C4（4）：极化/耐久、温度、电流、器件身份和缺口均覆盖（E1–4）。
- C5（3）：多数未知保留，但n=1及泛称高电流缺稳定证据过强（E3）。
- C6（3）：表格与改写便于使用；对简单问题的重复分析较多（E1与缺陷）。


- E1 回答短引：“不能读成"13.1 A cm⁻² 下稳定 500 h"”。依据：Main p5 Fig3e/g,p6。判断：正确，是关键回答。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“未说明是否为同一片 MEA/同一电池”。依据：Main p10 Electrochemical measurements。判断：保持记录边界，优于强称同一物理器件。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“恒电流计时电位（chronopotentiometry），n=1”。依据：Main p5 Fig3g；source Figure3 AY/AZ。判断：只公开一条曲线，未给稳定性独立重复数；n=1是未经声明的推断。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“源数据另有 112–137 h 的数据缺口”。依据：source Figure3 AY116:AZ117；AM20；A283:B283。判断：缺口和16.34143A/cm²@2.1V、639.675mA/cm²@1.805V确实存在；不能据此推断设备中断。 证据置信度：高（针对列明核查范围）。


## T3（Q-2e5cea） / T3-B（盲审编号 R-cee543cb）

评分：C1=4；C2=3；C3=4；C4=4；C5=3；C6=3。置信度：高

核查范围：完整核对Main pp5–6、10，SI pp38–42、59，workbook Figure3/ S41，包括端点、缺口和最高半电池行；非附件或实验流程复现。

优点：条件表和原句引用可追溯，iR耐久性未知保留恰当；正确指出扫描速率矛盾及电压漂移

缺陷/限制：多次断言同一物理电池没有原文依据；1.56V“可能混用60°C”是合理但未证实猜测，已标可能故不重罚；开头“不能”偏绝对，正文已给可并列陈述边界；重复内容较多

逐维理由：

- C1（4）：明确分开条件并给出可并列陈述方式（E2、E4）。
- C2（3）：条件和插值正确，物理同一电池未经确认（E1–3）。
- C3（4）：原句与数据定位可靠；器件身份额外推断单列C2/C5（E1–4）。
- C4（4）：温度、电流、扫描、iR与漂移等重要限定齐全（E2–4）。
- C5（3）：iR未知处理好，但同一器件说法缺证据；混温已标可能（E1、E3–4）。
- C6（3）：条件表与建议句可直接用；开头绝对“不能”需读后文才能理解（E2及缺陷）。


- E1 回答短引：“同一 AEMWE 单电池”。依据：Main p10；Fig3g。判断：来源说明同类构型但未确认同一MEA；实物身份推断过强。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“60 °C、恒流 1 A cm⁻²”。依据：Main p5 Fig3g,p6。判断：核心条件准确。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“1 A cm⁻² 约在 1.50 V”。依据：source Figure3 AL8:AM9；S41 A9:B10。判断：插值≈1.5057V、60°C≈1.553V，识别原文1.56V矛盾有依据；混温来源只能猜测。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“未说明（Methods 只对极化曲线说明不补偿）”。依据：Main p10 AEMWE最后一句。判断：正确限定耐久测试iR条件，不从极化设置自动推广。 证据置信度：高（针对列明核查范围）。


## T3（Q-2e5cea） / T3-A（盲审编号 R-9a48b94f）

评分：C1=4；C2=3；C3=3；C4=3；C5=3；C6=3。置信度：高

核查范围：完整核对Main pp5–6、10，SI pp38–42、59，workbook Figure3/ S41，包括端点、缺口和最高半电池行；非附件或实验流程复现。

优点：基本区分80°C极化与60°C恒流，531h及槽压上升准确；提醒13.1是约定2V点而非曲线终点

缺陷/限制：表称耐久性无iR及总结称同一电池，均超出明确记录；说SI Table6已统一1M/80°C不实：包含60°C、0.1M及24wt%KOH行；把500h释为未失效是读者解释，非作者定义

逐维理由：

- C1（4）：核心问题得到正确且直接的条件拆分（E1）。
- C2（3）：多数性能数字准确；耐久iR与同一物理电池越过材料记录（E2、E4）。
- C3（3）：主Fig3引用可靠，SITable6支撑关系有误（E3）。
- C4（3）：主要条件齐备，但比较表异质条件被误统一（E2–3）。
- C5（3）：识别测试类型差异；未说明条件被默认为已知（E2、E4）。
- C6（3）：结论和表格清楚，但统一条件的误导限制直接复用（E3）。


- E1 回答短引：“恒流 **1 A cm⁻²**”。依据：Main p5 Fig3g,p6。判断：关键事实准确，不支持13A级500h。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“iR 补偿 | 无 | 无”。依据：Main p10 Electrochemical measurements。判断：记录仅明确极化曲线无iR；耐久条件不可同等断言。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“该表已按 **1 M KOH、80 °C、商业膜** 统一列出”。依据：SI p59 TableS6。判断：表内有60°C、0.1M和24wt%KOH，误把标题当所有行一致条件。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“同一电池、60 °C”。依据：Main p10；source Figure3 AY4:AZ511。判断：同构型可核，是否同一物理器件未知；端点1.602→1.781准确。 证据置信度：高（已核材料和明确关系）；部分外部细节未知见发现。


## T1（Q-44eead） / T1-B（盲审编号 R-20f89805）

评分：C1=4；C2=2；C3=2；C4=3；C5=2；C6=3。置信度：高

核查范围：正文/SI及42sheet目录；重点复看SI p35 S34和p53 S52原图、主文p9 Fig6c、source Fig4列标签。仅评可见要点，所谓完整附件未提供，未给其隐含内容评分。

优点：覆盖研究链条与数据局限广，筛选/微调区分及原文数值不一致有实质核查；正确识别Fig4c标签互换、TableS3缺N和半电池/器件条件

缺陷/限制：S52图像结论错误：把源数据错行当作图像本身矛盾；“ML筛选用错模型”及“MAE误差棒”将方法选择/群体误差夸大成单候选结论；总述531h省60°C可能连读80°C；把ECSA的Ir6.08归W，遗漏W5.93；“无post-mortem”应仅限AEMWE，SI S42有半电池后表征

逐维理由：

- C1（4）：对全文作了与请求相符的实质分析（E1–5）。
- C2（2）：若干真实核查与S52/Cdl关键误读并存（E1、E3–4）。
- C3（2）：有精确源表定位，但对S52原图的引用不能支持批评（E1）。
- C4（3）：覆盖链条广；器件温度及post-mortem范围限定有遗漏（缺陷、E3–5）。
- C5（2）：把MAE当误差棒及模型选择当用错，且据错误图读作强结论（E1–2）。
- C6（3）：结构可扫描、改进意见具体；部分强断言需纠正后才能复用（E1–2）。


- E1 回答短引：“b 图 Ir₁ 曲线 PDS = 0.754 V、NiFeOOH = 0.855 V”。依据：SI p53 FigS52b原图；workbook S52 C6/D6。判断：原图Ir .171→.481，PDS=.310；NiFe0→.754→1.026→1.659，PDS=.754。源表C6/D6互换，答复明称渲染确认却读错图，核心批评失据。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“ML 筛选用错模型”。依据：Main p2筛选段；SI S3/S4。判断：原文透明说明原始预训练筛选，微调用于转移验证。可质疑精度与排名，但不能从后者更准推定前者“用错”；MAE不是误差棒。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“ECSA 翻倍（C_dl 6.08 vs 3.28 mF cm⁻²）”。依据：SI p35 FigS34图例。判断：W5.93、Ir6.08、bare3.28。数量级对比仍大致成立但W数值错配。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“标 "W L₃ edge" 的列装的是 ~11217.8 eV”。依据：source Figure4 P3:R8 / T3:V9；Main p6 Fig4c。判断：准确定位源表互换，避免将W非单调数据当Ir；这一核查成立。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“差异几乎全程 **≤0.08**”。依据：source Figure4 AI7:AJ8；Main p7。判断：多数高电位差≤.08，但1.40/1.42差.14/.12，答复已指出一项；“全程”不宜笼统。 证据置信度：高（针对列明核查范围）。


## T1（Q-44eead） / T1-A（盲审编号 R-267c85fe）

评分：C1=3；C2=1；C3=1；C4=3；C5=1；C6=2。置信度：高

核查范围：正文/SI及42sheet目录；重点复看SI p35 S34和p53 S52原图、主文p9 Fig6c、source Fig4列标签。仅评可见要点，所谓完整附件未提供，未给其隐含内容评分。

优点：涵盖实验/计算/器件多个环节，识别EXAFS配位数缺项与Fe污染控制不足；给出适当的后续验证方向

缺陷/限制：最重要批评把累计自由能高点当单步能差，直接误判PDS；Cdl单位错1000倍并错读图例，反向机理结论错误；混淆Ir筛选锚定位与边缘取代位，错误宣称同一候选未被DFT支持；高置信宣称1.56V扎实未处理源数据不一致，并无依据称源极化不单调/图注n5

逐维理由：

- C1（3）：完成广泛分析，但多项中心批评导致用户获得失真的总体解释（E1–5）。
- C2（1）：PDS、单位、图例、位型与统计事实均有重大错误（E1–5）。
- C3（1）：关键数字虽来自真实表格却错释，不能支持结论（E1–4）。
- C4（3）：覆盖计算/实验/器件和后续验证，但关键信息虽出现却缺正确限定（E1–5）。
- C5（1）：累计量当单步、跨位型直接比、面积效应反向推理均损坏论证（E1–4）。
- C6（2）：组织详细，但用户据此修改机理或复算会被误导（E1–3）。


- E1 回答短引：“势决定步是 **\*O→\*OOH（0.536 eV”。依据：Main p9 Fig6c；source Figure6 B5:B8。判断：0.536是累计G，单步.536−.357=.179eV；OH→O=.357才是最大正步。要求修正摘要deprotonation错误。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“≈0.024/0.024/0.013 mF cm⁻²”。依据：source S34 A5:D13，列单位mV/s和mA/cm²。判断：逐列OLS得到.023675/.0243225/.0131417 F/cm²，即23.675/24.3225/13.1417mF/cm²；答复单位误差1000倍。原图数值本身有约4倍不一致，但不挽救其计算。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“按图注值 W₁ 的 Cdl 最低”。依据：SI p35 FigS34原图。判断：W5.93、Ir6.08、bare3.28，W并非最低；面积更小、本征活性更高的反向推论失据。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“ML 首选的 Ir（0.254 V）在 DFT 复算的同类取代位上”。依据：Main p3 Fig1b/d；source Figure1 G4:J4；SI p53S52。判断：ML最优Ir是基面锚定motif1，并非边缘取代位；跨不同位型比较不能证明同候选DFT失败。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“取值不单调、n 值与图注 n=5 不一致”。依据：source Figure3 AL9:AT10；Main p5Fig3e caption。判断：Ir1.06707→1.7217、NiFe.95352→1.4918均单调；caption n10，只有源表Ni paper AW4为n5。该批评错误。 证据置信度：高（针对列明核查范围）。


## T1（Q-44eead） / T1-C（盲审编号 R-91110c60）

评分：C1=4；C2=2；C3=2；C4=4；C5=2；C6=3。置信度：高

核查范围：正文/SI及42sheet目录；重点复看SI p35 S34和p53 S52原图、主文p9 Fig6c、source Fig4列标签。仅评可见要点，所谓完整附件未提供，未给其隐含内容评分。

优点：明确同研究内部一致性不等于独立验证，并保留未取附件/结构/原始谱限制；大多数端点、数字与真实报告缺口准确，分析覆盖全面

缺陷/限制：没有发现Fig4c源表W/Ir标题互换，将W的变化误批评为Ir的反向证据；把未见每原子MAE归一化直接列单位不符，证据不足；“未正面处理”忽略正文pp7–8对羟基化Ir .485的条件解释；不等于该解释已充分证实

逐维理由：

- C1（4）：完整回应论文分析请求，保持部分材料访问边界（E1–5）。
- C2（2）：真实数值核查较多，但Ir源表标签混淆导致关键机制批评错（E1、E3）。
- C3（2）：对源表标题照收未核边能，错误引用W列支持Ir结论（E1）；另有正确定位。
- C4（4）：覆盖广且说明独立性/未知材料，重要内容齐备（E2–5）。
- C5（2）：有良好边界意识，但主要Ir批评及“未处理”超过证据（E1、E4–5）。
- C6（3）：结构清楚且建议可用；关键错误需在复用前纠正（E1）。


- E1 回答短引：“Ir 白线/空穴在 **1.4 V 最高**”。依据：source Figure4 P3:R8/T3:V9；Main p6Fig4c。判断：随1.4V达峰又回落的是约10212eV的W列，源表标题互换；真正Ir约11218eV随电位单调升高。答案核心I2批评错误。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“W 与 Ir 只差 14 mV≈0.014 eV”。依据：source Figure1 J4:J5；S3C11。判断：排序差与群体MAE比较可作为谨慎提示，但不能当每个候选已知置信区间；答复合理要求不确定度。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“1.506 V”。依据：source Figure3 AL8:AM9。判断：线性插值可重现，识别1.56V不一致成立。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“一致≠独立验证”。依据：source Figure3 AY4:AZ511；SI p56TableS3。判断：适当地限定内部对表；531h与无N列核查成立。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“计算与实验排序相反且未正面处理”。依据：Main pp7–8；SI p53FigS52。判断：正文已用Ir3OH .485相对3O .310讨论差异，不能称未处理；可以说解释尚无位型分布实证。 证据置信度：高（针对列明核查范围）。


## T6（Q-f22f18） / T6-B（盲审编号 R-8b5c3e47）

评分：C1=4；C2=2；C3=3；C4=4；C5=2；C6=3。置信度：高

核查范围：核对Main pp4–9、SI S28/S34/S43/S44/S50/S51、TablesS2–4、source Figures3/4/6；补看S43的实验与FEFF面板、S25拟合原图。未重做谱学拟合，未替代领域专家认证。 外链OSTI未成功打开；其高价金属概括与原论文参考17题名相合，但未给全文核验信用。

优点：准确区分主要促进假说与完全排除直接参与，主要DFT位型数值正确；识别Ir起始价态和Ni低电位矛盾，保留摘要suggest

缺陷/限制：Cdl排序错误使排除面积效应的论据反向；“W只在含Fe有效”、少数W完全测不出、同位素是唯一判别均过强；ML不含机理信息不实：候选位型与中间体/路径预设包含机理；多线索不自动统计独立

逐维理由：

- C1（4）：直接评估W促进与直接参与的证据强度（E1–5）。
- C2（2）：Cdl/宿主有效性等重要事实错误，核心方向仍合理（E1–2、E5）。
- C3（3）：DFT位型等引用可核，部分图例支撑关系错（E1、E5）。
- C4（4）：列出光谱、宿主、DFT、替代机制及验证方向（E1–5）。
- C5（2）：不排他结论恰当；“唯一”实验、无机理ML及宿主排他推理不成立（E2–4）。
- C6（3）：论证易读、有最终强度判断，但具体建议的唯一性易误导（E4–5）。


- E1 回答短引：“W₁-NiFeOOH 的 C_dl 最低（3.28 vs 5.93/6.08”。依据：SI p35FigS34原图。判断：W5.93、Ir6.08、bare3.28；称W最低并排除面积效应是实质误读。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“W 只在含 Fe 的载体上有效”。依据：source Figure3 T5:U10。判断：无Fe也从246降231mV；答复自己列数值却说只在含Fe有效。宿主依赖支持但不排除W直接活性依赖配位。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“在完全不含机理信息的条件下”。依据：Main p2，SI p2FigS1/p50FigS49。判断：筛选已经预设位型、中间体及模型路径，不能称无机理信息或独立确认。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“这是唯一能真正区分"促进"与"参与"的实验”。依据：SI pp51–52现有证据范围；Main Fig6a。判断：一般18O示踪判晶格氧来源，不自动区分W–O与Ni/Fe–O；唯一性并无来源或方法论证明。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“方向性判断是有依据的、可信度中等偏上”。依据：Main p7 XAS/DFT；Fig6d/source G6:G7。判断：中等信心与不排他限定合理；0.357/.964/.700数值匹配。 证据置信度：高（针对列明核查范围）。


## T6（Q-f22f18） / T6-A（盲审编号 R-2303f5d0）

评分：C1=4；C2=3；C3=3；C4=4；C5=3；C6=3。置信度：高

核查范围：核对Main pp4–9、SI S28/S34/S43/S44/S50/S51、TablesS2–4、source Figures3/4/6；补看S43的实验与FEFF面板、S25拟合原图。未重做谱学拟合，未替代领域专家认证。

优点：核心负结果、系综平均、模型与动力学边界解释清楚；区分元素与位型混杂及TOF归一限制，建议多方法验证

缺陷/限制：把“所有电位更氧化”照转未提醒源数据相反，虽属于作者证据段仍欠限定；宿主依赖不是单独证伪W位点的实验：直接位点也可能依赖载体；从仅公开末轮意见断言机制未被对抗审查超出记录；2.6%原子比不能单独证明不可能覆盖所有活性边位

逐维理由：

- C1（4）：聚焦证据能否支持W角色，回答充分（E1–5）。
- C2（3）：多数事实正确；照转所有电位Ni更氧化忽略低电位例外（E3）。
- C3（3）：谱学/DFT主要来源可追溯，少数正文主张未与源数据交叉限定（E2–3）。
- C4（4）：平均谱、动力学/热力学、载体混杂与TOF范围均覆盖（E1–4）。
- C5（3）：大多数区分谨慎；宿主反事实及无对抗审稿推断过强（E4–5）。
- C6（3）：核心结论及验证建议实用，少量断言需软化（E1、E4–5）。


- E1 回答短引：“测不到变化”≠“不参与”。依据：Main p7Fig4b/d；SI p44S43。判断：恰当逻辑限定，系综平均及缺检出限说明合理。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“热力学自由能台阶，不是 PCET 动力学势垒”。依据：Main p9Fig6c；Methods p11。判断：正确区分最大ΔG与过渡态能垒，无NEB报告；比直接宣布作者机理反了更可靠。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“且各电位下位移都比 NiFeOOH 大”。依据：source Figure4 AI7:AJ8；Main p7。判断：这是正文主张但源数据低电位不支持，未识别内在矛盾。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“如果 W 自己是活性位，高 W 含量（3.49 at%）的 W₁–Ni(OH)₂ 应该更强”。依据：SI p55TableS2；source Fig3 T8:U10。判断：金属含量不是实际可及W位点数，载体可改变W位点本征活性，反事实不具排他性。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“该机制未被真正“对抗性”审查”。依据：peer-review-file p1。判断：可说可见末轮意见未问此点；早轮未公开，不能推断未曾审查。 证据置信度：高（针对列明核查范围）。


## T6（Q-f22f18） / T6-C（盲审编号 R-5e53b7f8）

评分：C1=4；C2=2；C3=2；C4=4；C5=2；C6=3。置信度：高

核查范围：核对Main pp4–9、SI S28/S34/S43/S44/S50/S51、TablesS2–4、source Figures3/4/6；补看S43的实验与FEFF面板、S25拟合原图。未重做谱学拟合，未替代领域专家认证。

优点：位型数值及Ni低电位矛盾核查有用，提出可检验的证据边界；S43区分FEFF正向模型与实测、TableS3缺项基本准确

缺陷/限制：截断摘要前置suggest却标“确定”，引用强度判断失真；Cdl图例全错配，排除面积效应结论错误；把未公开早轮审稿推为未压力测试；用位型敏感性/MAE当已证明不能分辨亦过强；绝对价态替代插值结果方法细节未交付，只有提出校准缺口可采信

逐维理由：

- C1（4）：充分回答角色归属与证据问题（E1–5）。
- C2（2）：DFT/FEFF核查有效，但Cdl及摘要措辞有实质误读（E1–3、E5）。
- C3（2）：摘录删去suggest改变主张强度，图例误引削弱支撑（E1–2）。
- C4（4）：实验、DFT、替代解释和验证缺口覆盖充分（E1–5）。
- C5（2）：大量合理限定与不当强指控并存，不能由未见审稿推出未审查（E4）。
- C6（3）：组织有条理，部分引用需修正才能直接用于批评论文（E1–2）。


- E1 回答短引：“| Abstract | "subsurface W promoter induces synergistic electron redistribution at neighboring Ni-O-Fe edge active sites" | 确定 |”。依据：Main p1Abstract完整句。判断：所摘短句前面紧接“calculations suggest that”，不能裁掉suggest后认定摘要加码成确定。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“C_dl 为 W₁ 3.28、Ir₁ 5.93、NiFeOOH 6.08”。依据：SI p35FigS34原图。判断：实际W5.93/Ir6.08/NiFe3.28，反向归因面积贡献错误。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“Supplementary Fig. 43 里的 1.53 Å 是 **FEFF 正向模拟**”。依据：SI p44FigS43右侧Feff calculation面板。判断：此处成立，右侧两模型同峰位不能唯一判别结合；左侧仍包含实际原位EXAFS，不能把整图视为纯模拟。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“没有经过针对性的同行压力测试”。依据：peer-review-file p1。判断：仅缺早轮记录，不能由未见等同没发生。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“同一个 Ni–O–Fe 桥位”。依据：Main p9Fig6c/d；source Figure6 G6:I6。判断：位型限定与0.357/.475正确，确实支持模型内促进效应。 证据置信度：高（针对列明核查范围）。


## T7（Q-676d73） / T7-C（盲审编号 R-481e93fb）

评分：C1=4；C2=2；C3=3；C4=4；C5=2；C6=3。置信度：高

核查范围：Main p2,p11；SI pp2–9,p54TableS1；参考29；另读Settles Active Learning Literature Survey的定义和查询策略目录/第1节（https://burrsettles.com/pub/settles.activelearning.pdf PDF pp2,6–8；非整份综述精读）以检验一般概念。

优点：核心回答非主动学习且筛选用原始预训练骨干正确；清晰区分BFGS几何迭代与新增标签重训

缺陷/限制：四个“必备要素”含最终迭代模型做筛选，并非AL定义必需条件；把微调未用于筛选的可能原因冒充作者解释；廉价推理并不抵消昂贵标签的AL需求；断言完全无AL相关表述忽略参考29；所谓事前事后时间顺序未由论文确定

逐维理由：

- C1（4）：正确回答不是主动学习及何处易混淆（E1–2）。
- C2（2）：核心方法准确；杜撰作者解释及绝对全文表述属实质错误（E3–4）。
- C3（3）：原始模型原句可核；动机解释无法由所引段落支持（E1、E3）。
- C4（4）：训练、推理、几何迭代和AL循环区别都有覆盖（E1–4）。
- C5（2）：AL必要条件过窄、廉价推理解释缺逻辑保证（E2及缺陷）。
- C6（3）：表格帮助理解；错误动机和定义给用户不必要误导（E2–3）。


- E1 回答短引：“筛选明确用的是 **"the original pretrained EquiformerV2 backbone model"**”。依据：Main p2原句，p11Methods。判断：正确、直接支撑关键判断。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“主动学习的四个必备要素，本文一个都没有”。依据：Settles定义/查询策略§1–3 https://burrsettles.com/pub/settles.activelearning.pdf。判断：自适应查询标签是核心；特定不确定度方法或最终模型必须用于筛选不是所有AL必要条件。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“作者的解释是微调只在 unary NiNiNiOOH 上做过”。依据：Main p2,p11；SI TableS1。判断：原文只说验证迁移性，没有这条不用微调筛选的作者解释；NiNiNiOOH也是笔误。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“没有任何主动学习相关表述”。依据：Main p12 reference29。判断：有active machine learning参考题名；不影响方法非AL，但全文检索绝对说法不准。 证据置信度：高（针对列明核查范围）。


## T7（Q-676d73） / T7-B（盲审编号 R-0cdcf2c4）

评分：C1=4；C2=3；C3=4；C4=4；C5=3；C6=3。置信度：高

核查范围：Main p2,p11；SI pp2–9,p54TableS1；参考29；另读Settles Active Learning Literature Survey的定义和查询策略目录/第1节（https://burrsettles.com/pub/settles.activelearning.pdf PDF pp2,6–8；非整份综述精读）以检验一般概念。

优点：精确找到参考文献中AL词，阴性判断有明确范围；指出微调数字不能直接背书原筛选，且不把披露清楚的方法选择判错

缺陷/限制：把AL选样说必须ensemble/方差/贝叶斯过窄；所谓直接筛选单次前向推理忽略本文BFGS多次调用；其后文已正确解释故属表格简化；AL边际收益有限虽标推断，但推理便宜不自动说明追加DFT标签价值小

逐维理由：

- C1（4）：直接且充分回答AL判断，兼顾参考题名出现该词（E1–2）。
- C2（3）：论文具体流程可靠；AL选样方法被写成过窄必要条件（E3）。
- C3（4）：关键论文原句和方法定位支撑结论（E1–2、E4）。
- C4（4）：微调/筛选/BFGS区别以及不确定性均完整（E1–4）。
- C5（3）：不把方法选择当错误，较谨慎；泛化AL定义仍过窄（E3–4）。
- C6（3）：清楚易用；表中单次前向推理简化与后文多次迭代不完全一致（缺陷、E2）。


- E1 回答短引：“微调的精度数字并不能直接为筛选预测背书”。依据：Main p2筛选段；SI S3/S4。判断：准确且紧贴用户可靠性概念。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“该词与模型迭代训练无关”。依据：Main p11BFGS描述。判断：正确识别几何优化与学习回路。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“需要 ensemble、方差、或贝叶斯采集函数”。依据：Settles§3查询策略 https://burrsettles.com/pub/settles.activelearning.pdf。判断：存在其他选样策略，这些不是必需依赖；一般定义略窄。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“这属于方法学上的一个可追问点，不是错误”。依据：Main p2明确original pretrained；p11fine-tuning用途。判断：适当保留论证边界，没有伪造作者动机。 证据置信度：高（针对列明核查范围）。


## T7（Q-676d73） / T7-A（盲审编号 R-d3c0d43f）

评分：C1=4；C2=2；C3=3；C4=4；C5=2；C6=3。置信度：高

核查范围：Main p2,p11；SI pp2–9,p54TableS1；参考29；另读Settles Active Learning Literature Survey的定义和查询策略目录/第1节（https://burrsettles.com/pub/settles.activelearning.pdf PDF pp2,6–8；非整份综述精读）以检验一般概念。

优点：结论正确，表格详细区分真实筛选与微调验证；给出示例AL循环且示例预算清楚属建议

缺陷/限制：声称标题含active，实际标题没有该词；把AL价值被廉价推理抵消作为确定因果，混淆推理成本与标签价值；“模型只学一次”忽略多超参训练而一次性应指无自适应轮次；严格先后顺序/时间未证实；8×41×13省去去重，易使3976算术关系误导

逐维理由：

- C1（4）：清楚给出非AL结论和解释（E2、E4）。
- C2（2）：预训练身份正确，但标题出现active为虚设事实（E1–2）。
- C3（3）：主要论文引用准确；对标题和AL价值的来源支持不足（E1、E3）。
- C4（4）：方法步骤、微调用途与假想AL流程均覆盖（E2–4）。
- C5（2）：廉价推理抵消昂贵标签学习价值的因果不成立（E3）。
- C6（3）：表格和例子可用；虚设词义解释会制造用户混淆（E1）。


- E1 回答短引：“标题里的 "active" 指的是”。依据：Main p1标题。判断：题名根本无active，解释虚设的词。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“不是微调后的模型”。依据：Main p2；p11。判断：关键模型身份区分准确。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“主动学习的核心价值（在标签昂贵时提高样本效率）在这里被廉价推理抵消了。”。依据：Settles§1.1 https://burrsettles.com/pub/settles.activelearning.pdf；Main p2域外误差。判断：AL旨在节省标签/提高精度，低推理成本与该价值不互斥；无比较实验支持抵消。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“不确定度/多样性驱动的采集函数”。依据：Settles§3目录及定义；Main p2,p11。判断：作为常见范式示例可用，列成排他性必要条件略窄；论文确实没报告自适应标签回灌。 证据置信度：高（针对列明核查范围）。


## T2（Q-e95e13） / T2-A（盲审编号 R-5a433cbe）

评分：C1=4；C2=3；C3=3；C4=4；C5=2；C6=3。置信度：高

核查范围：Main p2,p7–11，SI S3–S8和TableS1原图；source Figures1/6/S3/S4。核对角色分工与MAE归一化，未重训ML或重算DFT。

优点：分工、BFGS与DFT参考分子能量、预训练/微调区别准确；模型基准数字、所选位型η和参数准确

缺陷/限制：“所有关键结论”被独立实验证实过度，少量候选实验不验证全空间排名；DFT称标准答案/终审且保证可信，淡化近似与模型依赖；共同DFT参考项不会自动混入ML-vs-DFT差值误差：相同参考项相减抵消，应区分绝对物理误差

逐维理由：

- C1（4）：ML/DFT分工及可靠性问题回答完整（E1–4）。
- C2（3）：参数/模型身份正确，全面独立证实过度且误差来源需区分（E1–3）。
- C3（3）：方法引用可核；“五层交叉验证”非原文统计设计（E4）。
- C4（4）：加速、基准、参考能与机理复算均覆盖（E1–4）。
- C5（2）：将DFT当终审和多线索当独立证实，置信程度明显偏高（E1、E4）。
- C6（3）：框架易理解；“交叉验证”术语会使用户误会验证强度（E4）。


- E1 回答短引：“所有关键结论最后都由 DFT 重算、并被实验独立证实”。依据：Main p2benchmark；pp7–8机理；SI S8。判断：只支持代表性DFT和少数候选实验，不能扩展所有排名和排他机理已证实。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“主筛选用的是未微调的原始预训练 backbone”。依据：Main p2原句；S3C11/S4C10。判断：准确，是解释ML可信度必需限定。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“H₂O、H₂ 参考能仍用 E_DFT”。依据：Main p11Eqs4–11。判断：混合计算方案正确；但同参考项在ML–DFT步能残差中抵消，不应说由此混入DFT参考误差。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“五层交叉验证”。依据：SI S3–8；TableS1。判断：属于多类型验证证据，未报告五折/交叉验证，不能当严格统计CV；正文六项并不独立。 证据置信度：高（针对列明核查范围）。


## T2（Q-e95e13） / T2-B（盲审编号 R-231058fa）

评分：C1=4；C2=3；C3=3；C4=4；C5=3；C6=3。置信度：高

核查范围：Main p2,p7–11，SI S3–S8和TableS1原图；source Figures1/6/S3/S4。核对角色分工与MAE归一化，未重训ML或重算DFT。

优点：具体分工、统计数字与验证域局限全面；明确筛选模型≠微调精度及Ir配位敏感性未完全解消

缺陷/限制：“把含Ir方案排除掉”不符Ir仍是提名、合成及完整实验对照；将DFT称真值和所有结构归属被实验证实略过强；未明确S8分步MAE是混合组分点；大多数数字正确

逐维理由：

- C1（4）：两种计算各自任务和验证限制交代充分（E1–4）。
- C2（3）：主要指标可核，Ir被排除属不实（E1–2）。
- C3（3）：图表数值定位准确；混合MAE作为外域指标欠限定（E2）。
- C4（4）：角色、参数、域外局限和Ir构型敏感性覆盖完整（E2–4）。
- C5（3）：对验证域与调和保持警觉；真实时间先后和DFT真值措辞稍过强（E3–4）。
- C6（3）：说明和表格适用，Ir排除措辞及混合数值栏目需修正（E1–2）。


- E1 回答短引：“把含 Ir 的方案排除掉”。依据：Main pp2–3候选提名，p5Fig3。判断：成本支持偏向W但Ir实际被保留研究，不能称方案被排除。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“Total MAE = 0.201 eV、R² = 1.000”。依据：SI p6FigS5；p8FigS7；p9FigS8。判断：.201/1.000、.191/.987及.178/.165逐图可核，统计报数准确。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“验证域较窄”。依据：Main p2；SI p2S1/p3S2。判断：4类代表位型和NiNi/NiFe不足覆盖8host全空间，适当说明外推边界。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“属于事后调和而非独立预测”。依据：Main pp7–8Ir羟基化讨论；S52。判断：作者用额外构型解释实验差异；提醒不是新盲预测合理，但确切时间流程未公开。 证据置信度：高（针对列明核查范围）。


## T2（Q-e95e13） / T2-C（盲审编号 R-d9584020）

评分：C1=4；C2=3；C3=4；C4=4；C5=4；C6=3。置信度：高

核查范围：Main p2,p7–11，SI S3–S8和TableS1原图；source Figures1/6/S3/S4。核对角色分工与MAE归一化，未重训ML或重算DFT。

优点：明确S8混合组分MAE、held-out不明和每原子归一所需原子数未知；区分DFT保真度与真实物理验证，少量候选不代表全空间；多数参数、页码与数值准确

缺陷/限制：上表将混合S8数值先放于未见NiFe栏，后文才澄清，阅读上易误会；摘要式器件数值并列省温度，虽非本题核心仍宜限定；“唯一非贵金属候选”仅对最终W/Ir二者成立，不宜理解为3976中唯一；“千元素”明显笔误

逐维理由：

- C1（4）：完整回答分工、证据与可靠性范围（E1–4）。
- C2（3）：关键数字与方法准确；少量摘要压缩和“唯一”范围措辞欠准（缺陷）。 参见E1–E4及本份缺陷列表。
- C3（4）：SI混合点、总能/原子归一化均按真实材料限定（E1–2、E4）。
- C4（4）：训练与筛选身份、held-out未知、DFT近似及有限候选验证均覆盖（E1–4）。
- C5（4）：明确保真度并保留未知，不把缺材料当反证（E2–3）。
- C6（3）：整体清楚；上表外域栏与后文混合MAE澄清有局部阅读冲突（E1）。


- E1 回答短引：“0.178/0.165 eV 是把 M₁–NiNiOOH 与 M₁–NiFeOOH 点混在一起算的”。依据：SI p9FigS8双组图例。判断：重要且正确的限定；不把混合MAE直接当纯外域指标。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“与 per-atom 单位相容，未能直接核对”。依据：Main p2；SI pp6–7/54。判断：合理处理结构总能与每原子MAE，避免无依据判单位错误。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“ML 的"可靠性"实质是**对 DFT 的保真度**”。依据：SI S3–8的DFT横轴；Main pp7–8。判断：准确解释量化验证的参照，保留DFT自身近似。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“实际跑全空间筛选用的是"原始预训练 backbone"”。依据：Main p2原句,p11。判断：准确且没有用微调<.2eV替代原始.408eV。 证据置信度：高（针对列明核查范围）。


## T5（Q-437494） / T5-A（盲审编号 R-577c25b9）

评分：C1=3；C2=2；C3=2；C4=3；C5=2；C6=3。置信度：中高

核查范围：原论文全文/SI/Source Data/公开末轮审稿；外部核验分层见 external-citation-audit.md。核心先例按出版社/PMC摘要与相关正文片段核对，不声称遍读全部引文全文；引用清单附件未提供。

优点：将方法、材料、器件、机理分开，具体实现与一般概念区别有用；正确指出W体系先例和商用膜/测试条件影响，主动声明外部访问和部分数字未核实

缺陷/限制：把用户明确截止日改成投稿前，且用DOI字符串猜日期，把2026-02-06论文列入先前工作；断言正文无W-NiFe先例与ref17及其本人上文相矛盾；将群体MAE当候选排序置信度、90%/80%旧思路及30%边际记录都没有相应统计定义或同条件比较；桥位scaling写错；AdsorbML文章号错、OC20范围误述；未完成引用核验的边界虽说明但结论仍太强

逐维理由：

- C1（3）：回答新旧区分，但擅改比较截止基准且夹入晚发文献（E1）。
- C2（2）：总体集成判断有依据，但缺引/scaling/定量记录判断实质不准（E2–5）。
- C3（2）：部分先例真实相关；晚发论文不能支持先前性，文章号亦有错（E1、E5）。
- C4（3）：四方面较完整；未覆盖PNAS2021等直接Ir先例，且比较条件不足（E4–5）。
- C5（2）：已承认访问限制，却继续给无定义百分比和记录上限（E1、E4–5）。
- C6（3）：分层表格有用，绝对断言和未经量化的百分比削弱可用性（E2、E4）。


- E1 回答短引：“从 DOI 年份看很可能是 2025 年”。依据：https://pubs.acs.org/doi/10.1021/acscatal.5c07061（出版社题录/Article history及结论片段）。判断：该文正式网上日2026-02-06，晚于用户截止；DOI中5c不等于发表年。回答虽标日期待核，却在已有思路表把它算入，不能支撑截止日前覆盖。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“没有任何一篇 W 掺杂 NiFe‑LDH/氢氧化物的 OER 工作”。依据：Main p12 ref17；https://light.northwestern.edu/wp-content/uploads/2023/01/Zhang_et_al-2020-Nature_Catalysis-2.pdf Fig3（作者存档原文图及段落）。判断：ref17 Nat Catal2020 DOI10.1038/s41929-020-00525-6包含NiFeW并研究高价调节；绝对缺引指控不成立，且回答自己的C4已承认该引用。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“substituted/bridge 用 ΔG_OOH = ΔG_OH + 3.20”。依据：SI p11 FigS10；Main p2 Fig1。判断：实际取代桥位拟合0.75x+3.42；x+3.20是传统参考线，关于越过scaling极限的具体解释失据。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“至多是一个 ~30% 的边际记录”。依据：https://onlinelibrary.wiley.com/doi/10.1002/anie.202413698（题录、摘要及可见器件段落）；Main p5Fig3e/g和p10。判断：10A长期运行与13.1A@2V极化点不是同一指标，未核电压时不能量化记录提升上限；其后承认条件依赖不能补足该上限。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“新集成 + 新数据点 + 一次较完整的机理指认”。依据：Main pp2–9；https://pubs.rsc.org/en/content/articlelanding/2018/sc/c8sc02015a（摘要/日期）；https://www.nature.com/articles/s41524-023-01121-5（题录/摘要）。判断：一般单原子促进相变与ML加速早有先例，组合/特定材料的增量判断有支持；AdsorbML真实且相关，但卷9文章号应172非203。新意百分比不是可复核测量。 证据置信度：高（针对列明核查范围）。


## T5（Q-437494） / T5-B（盲审编号 R-a4fcae2f）

评分：C1=4；C2=3；C3=3；C4=4；C5=3；C6=3。置信度：中高

核查范围：原论文全文/SI/Source Data/公开末轮审稿；外部核验分层见 external-citation-audit.md。核心先例按出版社/PMC摘要与相关正文片段核对，不声称遍读全部引文全文；引用清单附件未提供。

优点：先例细分且多数DOI真实、主题相关，清楚区分摘要级和未穷尽检索；商用膜限定、两种温度与只讨论阳极的设备比较较审慎；PNAS2021的Ir机制/位型先例核对有实质内容，并辨认NatCatal2020确含W-NiFe

缺陷/限制：开头表把微调与实际筛选连写，易误导；DFT自由能叫动力学势垒欠区分；两个NatCommun文章号误用DOI中数字；Fuel上线日未核实，不能视为已确证；Ir对照“基本复现”、不同宿主W结果“相冲突”比证据更强；概念相近不等于相同实验；大多数对比文献按iR补偿的广泛判断未逐条给出协议，商用膜记录只能限定检索范围

逐维理由：

- C1（4）：按用户截止和新旧类别逐项回答，给出具体增量（E1–5）。
- C2（3）：多数核心先例事实准确；筛选模型混写和文章号错为局部问题（E1、E3）。
- C3（3）：关键前作确实支持一般先例，部分题录错误及未逐条协议核查限制满分（E2–5）。
- C4（4）：方法、材料、合成、器件和机制并明确证据层级，覆盖充分（E1–5）。
- C5（3）：未检到不等于不存在处理好；“复现”及跨宿主冲突仍偏强（E2、E5）。
- C6（3）：结论与对照表可用于定位后续阅读，部分强措辞宜软化（E2–5）。


- E1 回答短引：“EquiformerV2（OC22 预训练 + M₁-NiNiOOH 微调）作 MLIP，筛”。依据：Main p2明确original pretrained；p11fine-tuning段。判断：实际筛选没有使用微调模型。虽不改变ML模板已有的创新性判断，首表仍混淆方法。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“Ir 对照几乎是 2021 年 PNAS 的复现”。依据：https://pmc.ncbi.nlm.nih.gov/articles/PMC8433498/ Results Fig1–4（相关正文核验）；目标Main pp3–8和SITable2/5。判断：PNAS确有锚定Ir、4→5.3价态、183mV及亚表层对照，先例相关性强；合成、NiFe比、工作价态及器件不同，宜说概念/机制先例，不能凭相同η称实验复现。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“Nat. Commun. 16, 65254”。依据：https://www.nature.com/articles/s41467-025-65254-5.pdf pp1,7–8；https://www.nature.com/articles/s41467-025-65980-w 摘要/题录。判断：两DOI真实，文章号分别10349/11090而非65254/65980。1813h@1A和900h@1A确有原文支撑，前者纯水80°C，应区分测试条件。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“且**明确包含 W 掺入 NiFe 氧氢氧化物**”。依据：https://light.northwestern.edu/wp-content/uploads/2023/01/Zhang_et_al-2020-Nature_Catalysis-2.pdf Fig3；Main p12 ref17。判断：正确识别直接先例；没有把所有前人材料混同具体W单原子结构，这一层次划分可靠。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“只在我实际检索到的范围内成立”。依据：https://www.nature.com/articles/s41524-024-01432-1（题录、AL方法及30180位点正文段）；https://pubs.acs.org/doi/10.1021/acscatal.5c04967（题录/方法）；目标SI Table6。判断：限制性声明适当。前文方法先例相关：30180单原子位点AL、EqV2/AdsorbML筛5991构型均可核；后者为HER，证明通用方法先例而非相同OER材料已实现。 证据置信度：高（针对列明核查范围）。


## T5（Q-437494） / T5-C（盲审编号 R-6afc7448）

评分：C1=2；C2=1；C3=1；C4=3；C5=1；C6=2。置信度：高（主要错误）；中（未核全引文）

核查范围：原论文全文/SI/Source Data/公开末轮审稿；外部核验分层见 external-citation-audit.md。核心先例按出版社/PMC摘要与相关正文片段核对，不声称遍读全部引文全文；引用清单附件未提供。

优点：找到Lin2018 Pt促进相变及PNAS2021 Ir锚定等高度相关先例；明确检索仍未收敛、附件报告仍在生成；不把该未完成声明认定为欺骗；提出同宿主元素角色对照、位点归因和商用膜器件的具体贡献

缺陷/限制：两篇截止后论文用作先例，直接污染核心创新性结论；称原始模型目标精度从未报告、Ir3O=.485均与SI相反；把Yan2019改写成W不是活性位与其摘要相反；Ru价态不变文献实为直接活性位例子，不能当促进剂论据；将更高贵金属电流与更低非贵金属电流混为非贵金属超越；仅SI引用不能推断主文曾删除或诚信问题；同一样品W/Ir说法不准，实际不同催化剂；CEJ引文片段实际属于ChemSusChem2021

逐维理由：

- C1（2）：覆盖新旧问题，但两篇截止后文献违反核心时间约束（E1）。
- C2（1）：模型精度、构型η、日期和性能比较等多项重大错误（E1–4）。
- C3（1）：存在真实重要先例，但把晚发文献/相反机制结论用作关键支撑（E1、E3）。
- C4（3）：要素广泛、未完成检索已披露；关键比较限定缺失（E1–5）。
- C5（1）：由错误日期与反向支撑下强结论，并无证据推出删除/诚信问题（E1、E3、E5）。
- C6（2）：表格便于看，但可复用结论/建议中夹入严重错误与指控（E3–5）。


- E1 回答短引：“2026-01-08 上线，早于本文 2026-01-29”。依据：https://pubs.acs.org/doi/10.1021/acscatal.5c07061（出版社Article history）；https://pubmed.ncbi.nlm.nih.gov/42105675/（JCIS题录）。判断：ACS实为2026-02-06网上发表；其另列JCIS2026.140656为2026-04-30网上日。没有给出可核的截止日前预印本，均不能作为用户要求的前作。 证据置信度：高（针对列明核查范围）。


- E2 回答短引：“该骨干在目标体系类上的吸附能精度从未报告”。依据：SI p4FigS3、p8FigS7；source S3C11；p53S52c。判断：原始模型.408eV已报告。该段又把Ir3O写.485，实际3O=.310、3OH=.485；因而筛选模型完全未验证/排序反转的具体论据失真。 证据置信度：高（针对列明核查范围）。


- E3 回答短引：“W 在镍基羟基氧化物中已被证明是促进剂而非活性位 [Yan 2019; Abbas 2026]”。依据：https://www.nature.com/articles/s41467-019-09845-z.pdf p1摘要（一级摘要核验）；https://pmc.ncbi.nlm.nih.gov/articles/PMC6461613/ Results/Theoretical calculations（正文片段）。判断：Yan摘要把O自由基与O–O生成归于W6+位点，不能支持此改写；Abbas又晚于截止。Ru2019明确Ru为活性位，价态稳定可反驳“稳定即促进”的简单判据，不能被当作其半个证明。 证据置信度：高（针对列明核查范围）。


- E4 回答短引：“非贵金属阳极 AEMWE 高电流密度 | **已有，且更高**”。依据：https://scholarworks.bwise.kr/hanyang/bitstream/2021.sw.hanyang/193251/1/High%20Free%20Volume%20Polyelectrolytes%20for%20Anion%20Exchange%20Membrane%20Water%20Electrolyzers%20with%20a%20Current%20Density%20of%2013.39%C2%A0A%C2%A0cm%E2%88%922%20and%20a%20Durability%20of%201000%C2%A0h.pdf 摘要；目标Main p5Fig3e。判断：非贵金属10.7小于13.1，13.39对应IrO2。回复自己列出两类却仍断言非贵金属更高，比较逻辑错误。 证据置信度：高（针对列明核查范围）。


- E5 回答短引：“主参考文献表完全删除了它们”。依据：目标Main pp12–13参考表、SI pp60–61 refs6/9/14；https://pubs.rsc.org/en/content/articlelanding/2018/sc/c8sc02015a（摘要及日期）；https://pmc.ncbi.nlm.nih.gov/articles/PMC8433498/（相关正文）。判断：SI确有相关先例，Lin促进概念和PNAS Ir机制也属真实有效先例。但材料只显示引用位置，没有删除历史或意图，不能据此指控引用诚信；合理建议是加强正文比较。 证据置信度：高（针对列明核查范围）。


## 完成逐份评估后的题内比较

以下只比较同题匿名可见回答；编号跨题不关联身份。分数不是事实正确率，不按总字数、批判强度或引用数量选优，也不据此认证领域专家水平。

- **T4（Q-69757e）（先前W-NiFe文献，最多5篇）**：三份主列表均有真实相关工作。T4-A（盲审编号 R-ca654fbb） 的题名/日期/方法信息最便于定位，但额外两条仍越过上限；T4-C（盲审编号 R-0642ee1c） 的主要引文支撑完整，却额外列6篇；T4-B（盲审编号 R-32b0c7d5） 额外列7篇且主表缺完整题名。主题检索正确性与遵守精选篇数约束应分别看待。Fuel部分信息未知不作为已确定错误。
- **T3（Q-2e5cea）（最高电流与500h）**：三份均正确否定“13.1 A cm⁻²连续500h”。T3-C（盲审编号 R-cdd913bb） 明确器件身份未知，并定位源数据缺口；T3-B（盲审编号 R-cee543cb） 对耐久iR未知处理更准确，但同一物理电池说法过强。T3-A（盲审编号 R-9a48b94f） 多出耐久iR和Table6统一条件的不实断言。前两份各有小问题，不必强分唯一最佳。
- **T1（Q-44eead）（全文分析）**：T1-B（盲审编号 R-20f89805） 正确发现Fig4源表标签交换，却误读S52原图；T1-C（盲审编号 R-91110c60） 的多项一致性检查成立，但没发现该交换，错误批评Ir趋势。T1-A（盲审编号 R-267c85fe） 在累计自由能、Cdl单位与图例、Ir位型上均犯关键错误，中心批评可靠性明显较低。批评数量多不能替代核查准确。
- **T6（Q-f22f18）（促进剂还是直接W位点）**：T6-A（盲审编号 R-2303f5d0） 对系综平均和热力学/动力学边界较可靠，也有宿主反事实和早轮审稿缺失的过度推断。另两份共同误读Cdl图例，T6-C（盲审编号 R-5e53b7f8） 还裁掉摘要suggest后指责确定性。三份都有保留W少数直接位点可能性的合理方向，不能因结论审慎就免除支撑错误。
- **T7（Q-676d73）（是否主动学习）**：三份核心答案都对。T7-B（盲审编号 R-0cdcf2c4） 区分方法选择与错误较好；T7-C（盲审编号 R-481e93fb） 伪托作者动机，T7-A（盲审编号 R-d3c0d43f） 虚设标题active，两者把廉价推理当AL无价值的解释也较强。普遍需要把“常见AL实现”与“所有AL必要条件”分开。
- **T2（Q-e95e13）（ML/DFT分工及可靠性）**：三份分工解释大体正确。T2-C（盲审编号 R-d9584020） 明确混合MAE、未知每原子归一化与DFT保真度边界，证据限定较完整；T2-B（盲审编号 R-231058fa） 仍有Ir排除和混合组分指标归属问题；T2-A（盲审编号 R-5a433cbe） “所有关键结论独立证实”与DFT终审表述削弱不确定性判断。
- **T5（Q-437494）（创新性）**：T5-B（盲审编号 R-a4fcae2f） 提供多数真实切近的先例并保留检索范围限定，虽有题录/模型混写与“复现”措辞过强。T5-A（盲审编号 R-577c25b9） 的总体集成观点有依据，但发表日推断、绝对缺引、scaling和定量记录上限失据。T5-C（盲审编号 R-6afc7448） 提供若干有效先例，但两篇截止后论文、Yan支撑反向、原模型验证遗漏及性能混比使核心结论可靠性受重大影响。这里没有可客观测量的“新意百分比”；没有把较负面的评价当更深入。

## 交付范围与限制

原始论文正文、SI、Source Data工作簿与公开末轮审稿先于候选阅读；基线未根据候选改写。阶段2追加核查见 post-baseline-checks.md。未重做DFT、训练或实验，未访问作者Zenodo/候选附件；没有独立领域专家认证。

外部文献题录批量核验结果和摘要/正文片段层级见 external-citation-audit.md 及两个 external-metadata JSON。未核到的全文与部分精确日期保留未知，未因访问失败推断虚构。此轮不是穷尽创新性综述，也不保证候选的每一条边缘引文均被全文核过。结论主要建立在已明确核到的、对答案有实质影响的事实和支撑关系上。

所有评分均针对可见最终回复；引用但未交付的附件未计为已完成正确，也未认定不存在。候选主动声明检索未完成按原文范围评价。匿名化造成的编号跳跃未扣分。过程与资源成本、模型或配置身份不在本评审范围；最终文件在揭示映射前冻结。


### 外部引用核验范围

# 外部引用核验台账

范围：只为核对匿名可见回复中的科学支撑与时间边界；不是穷尽文献综述。题录/摘要/原文相关段分开记录，未核全文不等于内容错误。Crossref批量结果来自作者/出版方登记元数据；注册日期不当作发表日期。少量429失败由已读出版社页面补充，余项列未知，不无限重试。

原始题录返回值保存在 external-metadata-Q69757e.json 与 external-metadata-Q437494.json。下面“仅题录”条目不代表其全部机理与数字已验证。

| DOI或标识 | 核到的题名 | 实际核验层级 | 判断/未知 |
|---|---|---|---|
| [10.1002/advs.202306988](https://doi.org/10.1002/advs.202306988) | High Free Volume Polyelectrolytes for Anion Exchange Membrane Water Electrolyzers with a Current Density of 13.39 A cm                     −2                     and a Durability of 1000 h | 作者机构存档PDF摘要；Crossref | 网上2023-12-03；13.39为IrO2，非贵金属10.7，不能称后者高于13.1。 |
| [10.1002/advs.202515407](https://doi.org/10.1002/advs.202515407) | Dual‐Site Synergistic Mechanism via Single‐Atom and Vacancy Drives Lattice Oxygen Activation in Layered Double Hydroxides | Crossref题录及登记摘要（未全文核对） | 日期字段 [[2025, 12, 5]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1002/aenm.202002285](https://doi.org/10.1002/aenm.202002285) | 未取得题名 | 本轮元数据请求失败 | 未知：HTTP Error 429: Too Many Requests；不以失败判虚构。 |
| [10.1002/anie.202101698](https://doi.org/10.1002/anie.202101698) | Evidence of Mars‐Van‐Krevelen Mechanism in the Electrochemical Oxygen Evolution on Ni‐Based Catalysts | Crossref题录及登记摘要（未全文核对） | 日期字段 [[2021, 5, 26]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1002/anie.202316697](https://doi.org/10.1002/anie.202316697) | Triptycene Branched Poly(aryl‐co‐aryl piperidinium) Electrolytes for Alkaline Anion Exchange Membrane Fuel Cells and Water Electrolyzers | Crossref题录及登记摘要（未全文核对） | 日期字段 [[2023, 12, 15]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1002/anie.202413698](https://doi.org/10.1002/anie.202413698) | 未取得题名 | 出版社题录/摘要及部分器件段 | 支持10A运行800h与自研膜；不以此单独断言同2V性能提升仅30%。 |
| [10.1002/cssc.202002544](https://doi.org/10.1002/cssc.202002544) | Electrodeposited Trimetallic NiFeW Hydroxide Electrocatalysts for Efficient Water Oxidation | 出版社摘要/题录及作者存档片段 | 正式网上2021-01-21；30h后W还原段支持，不能误归CEJ2023。 |
| [10.1002/smll.202311431](https://doi.org/10.1002/smll.202311431) | Tungstate Intercalated NiFe Layered Double Hydroxide Enables Long‐Term Alkaline Seawater Oxidation | PubMed作者摘要/题录 | 2024-02-16；WO4插层、350h@1000mA与LOM为摘要主张。 |
| [10.1002/smll.202504076](https://doi.org/10.1002/smll.202504076) | Tailoring Pt‐Ni/Fe Coordination in Single‐Atom Pt/NiFe LDH With Facile Synthesis for Efficient and Long‐Term Alkaline Water Electrolysis | Crossref题录及登记摘要（未全文核对） | 日期字段 [[2025, 6, 5]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1016/j.apcatb.2024.124356](https://doi.org/10.1016/j.apcatb.2024.124356) | Synergistic Mo and W single atoms co-doped surface hydroxylated NiFe oxide as bifunctional electrocatalysts for overall water splitting | Crossref题录 | 日期字段 [[2024, 12]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1016/j.cej.2022.139104](https://doi.org/10.1016/j.cej.2022.139104) | Efficient electrocatalysis for oxygen evolution: W-doped NiFe nanosheets with oxygen vacancies constructed by facile electrodeposition and corrosion | 出版社题录/摘要可见片段 | 题名/DOI/电沉积腐蚀一致；全部数值未逐项全文核验。 |
| [10.1016/j.fuel.2025.136945](https://doi.org/10.1016/j.fuel.2025.136945) | W-induced reconstruction of NiFe (oxy)hydroxides with abundant O-vacancies as efficient electrocatalysts for water oxidation | 出版社题录、亮点及局部摘要；Crossref题录 | 2026卷期和W诱导重构真实；候选称2025-09-27网上日期未独立核到，牺牲溶出/500h详细机理未知。 |
| [10.1016/j.isci.2021.102398](https://doi.org/10.1016/j.isci.2021.102398) | Machine learning-accelerated prediction of overpotential of oxygen evolution reaction of single-atom catalysts | Crossref题录 | 日期字段 [[2021, 5]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1016/j.jcis.2025.01.012](https://doi.org/10.1016/j.jcis.2025.01.012) | Phase regulation of Ni(OH)2 nanosheets induced by W doping as self-supporting electrodes for boosted water electrolysis | PubMed作者摘要/题录 | 网上2025-01-04；题名Ni(OH)2不排除正文摘要NiFeW体系；主要数字支持。 |
| [10.1016/j.jcis.2026.140656](https://doi.org/10.1016/j.jcis.2026.140656) | Modulating charge distribution to enhance lattice oxygen reactivity by incorporating tungstate into NiFe2O4 spinel for enhanced overall water splitting | PubMed题录；Crossref | Article date2026-04-30，晚于截止；未用其全文判机理。 |
| [10.1021/accountsmr.5c00319](https://doi.org/10.1021/accountsmr.5c00319) | 未取得题名 | 本轮元数据请求失败 | 未知：HTTP Error 429: Too Many Requests；不以失败判虚构。 |
| [10.1021/acs.inorgchem.9b01953](https://doi.org/10.1021/acs.inorgchem.9b01953) | Self-Supported Porous Ni–Fe–W Hydroxide Nanosheets on Carbon Fiber: A Highly Efficient Electrode for Oxygen Evolution Reaction | 出版社摘要/题录 | 2019-09-11；6:2:1为来源投料比；264mV/10h支持。 |
| [10.1021/acs.jpcc.4c01704](https://doi.org/10.1021/acs.jpcc.4c01704) | Adapting OC20-Trained EquiformerV2 Models for High-Entropy Materials | Crossref题录 | 日期字段 [[2024, 7, 2]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1021/acs.jpcc.5b00105](https://doi.org/10.1021/acs.jpcc.5b00105) | Effects of Fe Electrolyte Impurities on Ni(OH)                     2                     /NiOOH Structure and Oxygen Evolution Activity | Crossref题录 | 日期字段 [[2015, 3, 19]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1021/acsami.1c01815](https://doi.org/10.1021/acsami.1c01815) | Constructing Ultrathin W-Doped NiFe Nanosheets via Facile Electrosynthesis as Bifunctional Electrocatalysts for Efficient Water Splitting | PubMed/出版社摘要及题录 | 2021-04-26；电沉积、239/115mV及1.59V支持。 |
| [10.1021/acsami.5c20762](https://doi.org/10.1021/acsami.5c20762) | Electronic and Interfacial Engineering via Tungsten Incorporation for Robust Overall Water Splitting and Seawater Electrolysis | 出版社摘要/题录 | 网上2026-01-10，刊期01-28；满足截止；一锅水热和性能值支持。 |
| [10.1021/acscatal.2c05426](https://doi.org/10.1021/acscatal.2c05426) | The Open Catalyst 2022 (OC22) Dataset and Challenges for Oxide Electrocatalysts | Crossref题录 | 日期字段 [[2023, 2, 16]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1021/acscatal.4c03974](https://doi.org/10.1021/acscatal.4c03974) | Chromium Promotes Phase Transformation to Active Oxyhydroxide for Efficient Oxygen Evolution | Crossref题录 | 日期字段 [[2024, 8, 30]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1021/acscatal.5c04967](https://doi.org/10.1021/acscatal.5c04967) | Machine Learning–Accelerated Discovery of Earth-Abundant Bimetallic Electrocatalysts for the Hydrogen Evolution Reaction | 出版社方法/结果相关段及题录；Crossref | 2025-11-07；EqV2+AdsorbML、5991筛选构型真实，研究HER而非相同OER材料。 |
| [10.1021/acscatal.5c05674](https://doi.org/10.1021/acscatal.5c05674) | 未取得题名 | 出版社摘要及Article history | 2025-09-22；Ir单原子/LOM题名与摘要吻合。 |
| [10.1021/acscatal.5c07061](https://doi.org/10.1021/acscatal.5c07061) | Toward Efficient Hydrogen Production: Impact of Solid Solution of Tungsten on Nickel–Iron Hydroxide OER Catalysts | 出版社Article history、相关结论段；Crossref | 网上2026-02-06，晚于截止；W促进Fe位点方向相关，但时间不支持先例。非全文精读。 |
| [10.1021/jacs.8b00752](https://doi.org/10.1021/jacs.8b00752) | Single-Atom Au/NiFe Layered Double Hydroxide Electrocatalyst: Probing the Origin of Activity for Oxygen Evolution Reaction | Crossref题录及登记摘要（未全文核对） | 日期字段 [[2018, 3, 8]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1038/s41467-019-09845-z](https://doi.org/10.1038/s41467-019-09845-z) | 未取得题名 | 出版社PDF摘要/题录，PMC访问失败 | 2019；摘要明确W6+生成O自由基/O–O，不能支持W仅促进不参与；未声称遍读原文。 |
| [10.1038/s41467-020-16237-1](https://doi.org/10.1038/s41467-020-16237-1) | In-situ structure and catalytic mechanism of NiFe and CoFe layered double hydroxides during oxygen evolution | Crossref题录及登记摘要（未全文核对） | 日期字段 [[2020, 5, 20]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1038/s41467-020-17934-7](https://doi.org/10.1038/s41467-020-17934-7) | 未取得题名 | 本轮元数据请求失败 | 未知：HTTP Error 429: Too Many Requests；不以失败判虚构。 |
| [10.1038/s41467-022-29875-4](https://doi.org/10.1038/s41467-022-29875-4) | 未取得题名 | 本轮元数据请求失败 | 未知：HTTP Error 429: Too Many Requests；不以失败判虚构。 |
| [10.1038/s41467-022-33846-0](https://doi.org/10.1038/s41467-022-33846-0) | 未取得题名 | 本轮元数据请求失败 | 未知：HTTP Error 429: Too Many Requests；不以失败判虚构。 |
| [10.1038/s41467-024-50605-5](https://doi.org/10.1038/s41467-024-50605-5) | 未取得题名 | 本轮元数据请求失败 | 未知：HTTP Error 429: Too Many Requests；不以失败判虚构。 |
| [10.1038/s41467-025-56070-y](https://doi.org/10.1038/s41467-025-56070-y) | Time-resolved spectroscopy uncovers deprotonation-induced reconstruction in oxygen-evolution NiFe-based (oxy)hydroxides | Crossref题录 | 日期字段 [[2025, 1, 16]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1038/s41467-025-65254-5](https://doi.org/10.1038/s41467-025-65254-5) | Covalent catalyst immobilization in cross-linked ionomers for durable pure water anion exchange membrane electrolysis | 出版社PDF pp1,7–8/图6；Crossref | 2025-11-24；文章号10349；1813h@1A、80°C纯水。 |
| [10.1038/s41467-025-65980-w](https://doi.org/10.1038/s41467-025-65980-w) | 未取得题名 | 出版社摘要及题录 | 2025-12-12；文章号11090；900h@1A支持。 |
| [10.1038/s41467-026-68735-3](https://doi.org/10.1038/s41467-026-68735-3) | Machine-learning-guided tungsten single atoms promote oxyhydroxides for noble-metal-free water electrolysis | 本地全文、SI、源数据、公开末轮意见 | 完整基线先于候选；日期2026-01-29。 |
| [10.1038/s41524-024-01432-1](https://doi.org/10.1038/s41524-024-01432-1) | Active learning accelerated exploration of single-atom local environments in multimetallic systems for oxygen electrocatalysis | 出版社相关正文：AL方法、30180位点；题录 | 2024-10-19；支持大规模AL单原子环境先例，不等于相同NiFeOOH材料。 |
| [10.1038/s41929-020-00525-6](https://doi.org/10.1038/s41929-020-00525-6) | High-valence metals improve oxygen evolution reaction performance by modulating 3d metal oxidation cycle energetics | 作者机构存档PDF Fig3及相关段；Crossref | 2020-10-19；包括NiFeW；目标Main ref17已引用。 |
| [10.1038/s41929-024-01209-1](https://doi.org/10.1038/s41929-024-01209-1) | Seed-assisted formation of NiFe anode catalysts for anion exchange membrane water electrolysis at industrial-scale current density | Crossref题录 | 日期字段 [[2024, 8, 13]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1038/s41929-024-01238-w](https://doi.org/10.1038/s41929-024-01238-w) | High-performance anion-exchange membrane water electrolysers using NiX (X = Fe,Co,Mn) catalyst-coated membranes with redox-active Ni–O ligands | Crossref题录 | 日期字段 [[2024, 10, 28]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1039/c3ee43811b](https://doi.org/10.1039/c3ee43811b) | Inverse spinel NiFeAlO4 as a highly active oxygen evolution electrocatalyst: promotion of activity by a redox-inert metal ion | Crossref题录 | 日期字段 [[2014]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1039/d0ta00691b](https://doi.org/10.1039/d0ta00691b) | 未取得题名 | 出版社摘要/题录 | 2020-04-07；水浴、纳米粒堆积NiFeW及247/320mV支持。 |
| [10.1039/d4nr01390e](https://doi.org/10.1039/d4nr01390e) | Rational design of nanoscale stabilized oxide catalysts for OER with OC22 | Crossref题录及登记摘要（未全文核对） | 日期字段 [[2024]]；主题与候选基本相符，细节支持未逐条确证。 |
| [10.1073/pnas.2101817118](https://doi.org/10.1073/pnas.2101817118) | Origin of enhanced water oxidation activity in an iridium single atom anchored on NiFe oxyhydroxide catalyst | PMC原文相关章节Fig1–4；Crossref | 2021-08-31；锚定Ir、+4→+5.3、183mV与亚表层比较支持；并非相同合成/配比重复。 |
| [10.3866/pku.whxb202303055](https://doi.org/10.3866/pku.whxb202303055) | Tungsten-Doped NiFe-Layered Double Hydroxides as Efficient Oxygen Evolution Catalysts | 出版社摘要/题录 | 网上2023-08-21；醇热、Fe-W电荷调节、199/237mV支持。 |
| [10.59717/j.xinn-mater.2024.100072](https://doi.org/10.59717/j.xinn-mater.2024.100072) | 未取得题名 | 本轮元数据请求失败 | 未知：HTTP Error 429: Too Many Requests；不以失败判虚构。 |
| [10.1038/s41524-023-01121-5](https://doi.org/10.1038/s41524-023-01121-5) | AdsorbML: a leap in efficiency for adsorption energy calculations using generalizable machine learning potentials | 出版社题录/摘要 | 2023-09-22；9:172而非9:203。 |
| [10.1039/c8sc02015a](https://doi.org/10.1039/c8sc02015a) | Accelerated active phase transformation of NiO powered by Pt single atoms for enhanced oxygen evolution reaction | 出版社摘要/题录 | 2018-07-16；支持Pt促进NiO→NiOOH而不是直接OER位点。 |
| [PMC6461613](https://pmc.ncbi.nlm.nih.gov/articles/PMC6461613/) | Boosting oxygen evolution of single-atomic ruthenium through electronic coupling with cobalt-iron layered double hydroxides | PMC正文相关结果/计算段 https://pmc.ncbi.nlm.nih.gov/articles/PMC6461613/ | 2019；明确Ru为活性位，价态稳定并不推出仅促进。 |



## 额外边界

EquiformerV2在目标原文引文和2024工作中可识别，但候选给的ICLR长哈希URL未单独成功解析，不据此认定不存在。若引用只有作者/年份或模糊期刊而无可唯一定位信息，本轮不以猜测补全。R-577c25b9若干旁支条目（例如Accounts Mater. Res.5c00319、Innovation100072及未给完整书目信息的Science Bulletin/IJHE）未完成支撑核验；其新意90%/80%旧的量化依然没有操作定义。

Settles Active Learning Literature Survey只阅读定义/策略目录及第一节，https://burrsettles.com/pub/settles.activelearning.pdf ，PDF pp2,6–8；用于核对AL概念边界，不声称全文综述。

以上外部访问只获取一级文献、作者存档或出版方登记题录。没有访问任何候选附件、过程日志、配置、资源统计或身份映射。

## 第四部分：质量、skill 与 router 的综合判断

以下为主代理在独立评分冻结后，结合真实组别和运行日志作出的解释；不是独立盲审者在知道配置后重新打分。冻结评分不变，不用综合结论反向修改分数，也不把六个序数分数硬换算成正确率或“每百万 token 科研价值”。

### 1. 逐题看质量是否值得额外消耗

| 任务 | 独立内容评审的主要差异 | 对应实际调用和资源 | 本轮能支持的判断 |
|---|---|---|---|
| T1 整篇分析 | B/C 比 A 的中心批评更可靠，但仍各有实质错误：B 误读 S52 原图；C 漏掉 Fig4c 源表 W/Ir 标题互换。C 覆盖更完整，不能称全面优于 B。 | A 无技能；B peer-review；C 是唯一实际 router 链。C 比 B 多 15.7% token、耗时多 4.4%。 | 路由链能运行；没有显示它在这道题上相对具体技能有明确质量/资源优势。不能由一次混合路径判断 router 净效应。 |
| T2 ML/DFT 分工 | C 对 DFT 保真度、混合 MAE、未知归一化的限定较好；B 有“排除 Ir”的错误；A 对独立验证和 DFT 权威性说得过强。 | B 没有实际加载技能；C 加载 reading-contract，未加载 router。C 总 token 比 B 少 4.4%，耗时多 11.1%；相对 A 则仍明显多用 token。 | 本题出现更好的证据限定，但它关联的是 reading-contract 及本次生成行为，不能归为 router 执行成功。 |
| T3 工况核对 | 三组都识别 80°C 极化与 60°C 恒流的区别。B/C 六维评分相同，各有小缺陷；A 多出耐久 iR 和比较表条件的不实断言。 | B/C 都只加载 reading-contract；C 用量是 B 的 2.25 倍、耗时 1.24 倍。 | 同一个技能也可能走出成本差异很大的路径。本题 C 更多核查细节没有转化为明确的整体质量优势。 |
| T4 最多五篇文献 | A 的题名/日期/方法组织更实用；三组都给出主表之外的额外论文，均违反数量上限。 | A 无技能；B paper-lookup；C paper-lookup + literature-search-openalex。B/C token 分别是 A 的 3.16/1.27 倍；C 耗时却比 A 短。 | 具体检索技能没有在本题稳定超越通用工具路径。不能只看速度或文献数量；数量约束是显式任务要求。 |
| T5 创新性 | B 的相关先例、限定与器件对比整体最好；A 有截止日、缺引和量化新意问题；C 有两篇截止后文献、反向引用、漏看原模型验证和不公平性能比较，核心判断可靠性最低。 | A/B/C 均委派；B/C 加载 lit-review，C 还加载 paper-lookup，但未加载 router。B token 是 A 的 3.52 倍；C 是 B 的 2.49 倍。C 7 个子会话缺结束记录。 | B 的额外工作对应较好的回答，但是否值得该成本取决于用途；C 展示高消耗与低质量并存。不能将 C 的失败或开销归因于没实际运行的 router，也不能把未完成检索较早返回说成完成更快。 |
| T6 W 机理证据 | A 整体更可靠；B/C 共同误读 Cdl 图例并据此作反向论证，C 还截掉摘要 suggest 后指责结论过强。 | B 加载 scientific-critical-thinking；C 再加 reading-contract；B/C token 为 A 的 4.93/4.77 倍。 | “多做批评、写更多审慎措辞”不是事实准确的替代。此题加载审查技能未带来质量提升，反而扩大了错误批评的篇幅和成本。 |
| T7 是否主动学习 | 三组核心结论都正确，B 的检索范围和方法界定更可靠；A 虚设标题 active，C 伪托作者动机，均存在概念过度简化。 | B 加载 reading-contract，A/C 无实际技能。B token 为 A 的 0.68 倍，C 为 B 的 2.43 倍；B 也比 C 更快。 | 本题是适配的单项技能对应更好质量与更低消耗的正例；仍是单次实例，不证明总是如此。 |

### 2. skill 是否有效：分别回答三个层次

**能否接入和实际加载？能，且有原始日志证据。** 在该 Windows DSH、deepseek-flash 配置下，具体技能成功通过 skill 工具返回正文，并出现相应读取、检索、核查与委派动作。不是仅仅“文件下载了”或“回答提到了技能”。但这不意味着仓库全部 53 个目录均被功能验证；本轮只覆盖实际加载的这些技能和七种文献任务，没有认证 VASP、DFT 计算执行或其他科学软件。

**能否提升某些任务的回答？本轮有正例，也有反例。** T7-B 的概念辨析、T2-C 的证据限定和 T5-B 的先例对比是正例；T6 的错误批评、T4 的过量输出及 T5-C 的严重过度扩展是反例。技能作为指导可以改变执行习惯，但不是事实校验器，也不是质量保证。当前合理定位仍是“提供省时入口和可复用做法”，不能宣传成已证明提高科研准确率。

**能否节省 token 和耗时？不能给全局肯定答案。** 本轮 A 的总 token 和总耗时最低；B/C 质量并非全局优于 A，且多数任务消耗增加。T7-B 是局部节省且质量较好的案例；C 相对 B 在部分题更省 token，但其他题大幅增加。总 token、实际费用、墙钟耗时与答案质量不是同一个指标，不能用其中一个替代另外三个。

### 3. router 是否有效：当前证据主要说明接入缺口

router 正文加载在 T1-C 成功；其余六次并未加载。更重要的是，“优先使用 router”的指令没有进入实际初始上下文。所以本轮不能回答“正确启用强制 router 后，是否提高质量/降低消耗”。C/B 的比较仅能作为多一个可选入口时的实际系统行为观察，不能将差异因果归给路由执行。

T1-C 没有出现相对 T1-B 的清晰全面优势；同时也不能据此判断 router 无价值，因为它还更换了具体技能组合、核查步骤和回答覆盖度。只有这些配置一起变化的单次例子，不能隔离路由本身的作用。七题不足以建立可靠的自动权重排序，更不能用本轮分数自动淘汰或改写某一上游技能。

### 4. 当前最值得做的优化，按轻量优先

1. **先修测试接入，再讨论 router 规则优化。** 将优先路由指令放进每次运行真正使用的指令位置，或由宿主明确注入；预检直接检查实际请求中是否出现规则、目录是否正确。正式运行照实记录是否加载，不把计划文件当作生效证明。保留自然语言提问，不增加用户选择面板或额外操作。
2. **把普通问答和深度创新性审查分清。** 不应让每个“新意在哪里”都不受控地扩展到大量并行综述。可以提供限定范围的初查路径；若选择严格 lit-review，则遵守其完成标准并明确资源边界，做不完就如实交付“未完成的初查”，不能静默删掉上游要求却自称已完整执行。预算在执行层管理，不直接篡改上游正文。
3. **为否定性结论加一条小而具体的检查。** 在写“论文算错/数据相反/证据缺失”前，核对原图图例、轴单位、源表列标题、累计自由能与相邻差分、以及来源中的 suggest 等限定词。本轮多处失误发生在这些环节，增加这类有目标的复核比继续堆更多审查技能更贴近问题。它仍需真实案例验证，不能宣称加一句规则就已解决。
4. **把完成条件和可见交付收紧。** 回复前确认仍相关的委派已收集、取消或明确列为未完成；主进程正常退出不等于研究工作完成。用户要最多五篇，整个回复（包括备选）就不超过五篇；核心结论和必要证据应放在可见回复里，不依赖未交付附件补齐。这里主要需要执行收尾检查，不需要大系统。
5. **保留案例证据，不急于做自动排名。** 将任务、实际加载、关键错误、资源和适用限制形成可追溯的小型回归案例。优先采用与任务匹配、依赖可用的最小技能组合；本轮不能给所有 skill 设科学可靠的数值权重，也不支持自动抓取上游新版本后立即替换已测版本。

后续若要验证改进，先修复规则注入，再对 T1（路由链）、T5（复杂检索）、T6（图表批评）和 T7（单项问答）做小规模重复对照；提前固定资源上限、完成条件、外部材料和评价规则，并继续让生成者与评审者分离。需要推广到整个化学领域时，还应换论文复核。本次没有重跑模型、修改公共仓库或替你扩展测试规模。

### 5. 如何使用这份结果

这份报告可作为工具改进和下一轮验收的依据，而不是公开宣称“skill/router 显著优于无 skill”的证据。最明确的成果是：实际接入情况已可核查、失效的优先路由配置已定位、失控委派与未完成状态已揭示，以及一组需要优先防止的错误批评案例。质量结论保留为一个上下文独立模型的盲审意见；涉及发表、否定作者结果或指导真实计算的判断，仍应由领域人员核对关键证据。


## 审计出处与复核边界

原始实验根目录：`<experiment-root>`。本次未改动源仓库、问答或运行日志。

- 问答与汇总：`group-io-report.json`；已与逐次 `runs/<任务-组>/answer.md` 及持久化会话中的最终可见 text 核对 21/21 一致；原始 user/message 也与报告输入 21/21 一致。
- 实际主会话 skill 加载：`runs/<任务-组>/.harness-logs/events.jsonl` 的 tool_call 与对应 tool_result，要求成功返回技能正文。
- 初始上下文、子会话完成状态和 provider usage：`runs/<任务-组>/.harness-home/sessions/**/session.v4.jsonl.zstd`，使用独立 libzstd 流式解码器检查帧完整性并逐条重算；38 份会话均解析完成，用量与原报告 21/21 一致。
- 规则位置与启动方式：`profiles/C/DSH_HOME/AGENTS.md`、`tools/run-experiment.ps1`，结合实际 system/user/request 记录核对，未仅凭计划文件推断。
- 盲审证据、评分和冻结哈希：本地 `blind-review-20261010/review/`；匿名映射、删改日志与过程复核脚本：`blind-review-audit-20261010/`。
