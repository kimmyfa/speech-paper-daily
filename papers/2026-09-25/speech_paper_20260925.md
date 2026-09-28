# 2026-09-25 语音论文速递

**共收录**: 44 篇 | **语音大模型**: 37 篇 | **语音前端**: 7 篇

> 目标日期 2026-09-25（北京时间）arXiv 语音相关论文共命中 44 篇。
> 以下是按评分排序的结果（前 15 篇完整精读，其余仅列标题、arXiv ID、评分与链接）。

---

## 语音大模型

## [1] EditVoice: Variable-Length Non-Autoregressive Zero-Shot TTS and Speech Editing with Edit Flows

arXiv ID：2609.29889 | 方向：语音大模型 | 作者：Hongyao Deng、Wenhao Guan、Xuetao Lin、Peijie Chen、Weijie Wu、Lin Li、Qingyang Hong（通讯） | 机构：厦门大学信息学院、厦门大学电子科学与工程学院 | 发布日期：2026-09-25 | 论文 https://arxiv.org/abs/2609.29889 | PDF https://arxiv.org/pdf/2609.29889.pdf | 代码暂无 | Demo https://dhy02.github.io/editvoice-demo/

### 📌 简介
本文提出 EditVoice，据作者所知首个变长非自回归零样本 TTS 模型。它基于 Edit Flows 离散流匹配框架，通过插入、删除、替换操作在采样时联合更新语音内容与序列长度，摆脱了传统 NAR 模型需预先指定目标长度的限制。模型采用随机区间语音填充训练，统一了零样本 TTS 与文本驱动的语音编辑，并支持前缀/后缀两种 prompt 位置。作者进一步提出互补 prompt 采样（CPS）融合两种位置的预测，并利用模型对合理 token 序列的编辑泛化能力实现端到端编辑与生成后精修。仅用 10K 小时 GigaSpeech 训练，便在 Seed-TTS Eval EN 与 RealEdit 上取得有竞争力的结果。

### 🔧 技术方案
**问题背景：** 现有零样本 TTS 中，AR 解码天然变长但局部误差易传播；NAR 并行生成却需先生成或预测目标长度，迭代修正也受限于固定长度序列。语音填充虽统一了 TTS 与编辑，但前缀与后缀 prompt 位置的联合利用此前未被探索。
**模型架构：** 444.7M 参数 Edit Flow 模型，14 层双向 LLaMA 风格 Transformer（hidden 1024、FFN 4096）加 6 层 Conformer 文本编码器，建模冻结 S3Tokenizer2 语义 token；TTS 由冻结 CosyVoice 2 声码解码，编辑场景改用微调的 Kimi-Audio BigVGAN。两阶段推理：CPS 生成语义 token，再做生成后精修与去 token 化。
**核心创新：** (1) 首次将 Edit Flows 变长离散流引入零样本 TTS，固定初始长度 50 个随机 token 即可在采样中通过插删替换自适应目标长度；(2) CPS：每个编辑操作选速率更高的 prompt 位置及其 token 分布，并施加局部 prompt 一致性避免切换伪影；(3) 发现模型可编辑非训练来源的合理 token 序列，据此实现无需外部定位的端到端编辑和免训练生成后精修。
**训练策略：** 随机区间语音填充：原文中随机区间替换为 50 个 p0 采样 token，借助含 blank 的辅助对齐空间构造条件路径与 Edit Flow 目标；线性调度，条件以 0.1 概率丢弃供 CFG；GigaSpeech 10K 小时训练 230K 步。

### 📊 实验结果
**数据集**：GigaSpeech 10K 小时训练；评测 Seed-TTS Eval EN、LibriSpeech-PC、RealEdit。
主要指标：
- WER（Seed-TTS EN）：1.48（64 NFE），优于同 tokenizer 的 AR CosyVoice2 的 2.58，全表最低
- WER（LibriSpeech-PC）：1.63；SIM-o：0.663，UTMOS：4.37
- T2S RTF：0.0989（16 NFE），远快于 MaskGCT 0.2791 与 CosyVoice2 0.5313
- RealEdit 级联编辑：WER 4.40 全场最佳（优于 SSR-Speech 4.75），MOSNet 3.22
- 端到端编辑：SIM-o 0.975、UTMOS 3.50 最佳，WER 4.67 第二，保留 31.5% 源 Mel 帧
- 消融：CPS 加局部一致性使 WER 由 1.65 降至 1.54；8 步生成+2 步精修优于 16 步无精修
**是否开源**：提供 demo 音频页，代码与模型暂未开源。

### ⭐ 评分：7/10
首个变长 NAR 零样本 TTS，将 Edit Flows 成功落地语音生成，统一 TTS 与编辑任务；CPS 与生成后精修思路巧妙且消融充分，10K 小时数据即达 SOTA 级 WER 与 0.099 RTF，效率突出。不足：说话人相似度低于大规模 AR 系统，端到端编辑源保持率仅 31.5%，未开源代码且仅英文实验，泛化性待验证。
## [2] TS-OPD: Reconciling ASR and QA in Speech Language Models via Task-Specific On-Policy Distillation

arXiv ID：2609.29464
方向：语音大模型
作者：Yujie Guo、Hongjie Chen、Jian Kang、Jie Li、Yongxiang Li、Yong Qin
机构：南开大学计算机学院 | 中国电信人工智能研究院星宸AGI实验室
发布日期：2026-09-25 | 论文 https://arxiv.org/abs/2609.29464 |PDF https://arxiv.org/pdf/2609.29464.pdf |代码与Demo：暂无

### 📌 简介

语音大模型（SLM）继承自预训练LLM的指令跟随能力，但ASR专用微调往往导致其大幅退化：本文实测QA准确率从42.57%崩塌至2.86%。为此提出任务级在线蒸馏TS-OPD，将ASR特化前后的模型分别作为QA与ASR两个互补教师，学生在两种任务提示下独立生成on-policy轨迹，各轨迹仅由对应教师监督，从而缓解双监督信号冲突。实验表明该方法显著提升基础与上下文ASR性能的同时完整保留甚至略增QA能力，并对平衡系数与蒸馏数据量表现出良好鲁棒性与可扩展性。

### 🔧 技术方案

**问题背景：** SLM在ASR特化微调中出现灾难性能力遗忘，现有模型合并、权重平均、离线蒸馏等多靠参数约束或数据设计保留能力，未在轨迹层面化解ASR与QA两种监督分布的直接竞争。

**模型架构：** 采用encoder-adapter-LLM范式，Whisper-large-v3作语音编码器，卷积加线性adapter将输出4倍下采样并投影至Qwen3-4B嵌入空间。

**核心创新：** (1)双教师构造：仅训练adapter得到的QA能力模型作QA教师，再由其全参ASR微调得到ASR教师，学生从QA模型初始化，两教师冻结只更新学生adapter。(2)任务级路由：学生分别在ASR与QA提示下采样on-policy轨迹，ASR轨迹仅受ASR教师前向KL监督、QA轨迹仅受QA教师监督；并构造共享轨迹变体ST-OPD对照组，实证路由机制减轻教师间干扰。(3)损失λ·L_ASR+(1-λ)·L_QA，因两教师监督不同轨迹，λ取值极不敏感。

**训练策略：** 从Emilia取约8k小时英文语音，转写经Qwen3-4B生成CoT回答构成QA配对目标；蒸馏用500小时，ASR与QA实例1:1采样，top-128前向KL，学习率1e-5余弦调度，训练1个epoch，ASR与QA最大生成长度分别为256和2048 token。

### 📊 实验结果

**数据集**：LibriSpeech test-clean/test-other、GigaSpeech、ContextASR-Bench英文对话子集、TELEVAL（LlamaQA-en/TriviaQA-en/WebQ-en）
- 基础ASR整体WER：TS-OPD 10.03 对 基线adapter 14.19、ASR全参微调 9.16（后者QA崩塌），LS test-clean达3.55
- 上下文ASR：WER 6.19、NE-FNR 16.82，在转写准确率与实体召回间最均衡
- TELEVAL QA总分：45.07，为全部系统最高，且以500小时数据优于8k小时联合训练基线44.29
- λ鲁棒性：0.1~0.9间双能力稳定，仅λ=1时QA崩塌；ST-OPD中λ增至0.55即致QA跌至23.97
- 数据扩展：100→1000小时，整体ASR WER由11.32降至9.82，QA稳定在45左右
**是否开源**：训练评测均基于Emilia等公开数据集、方法可复现，但代码与模型权重暂未开源

### ⭐ 评分：7/10

将on-policy蒸馏改造为任务路由双教师形式，直击SLM特化中"增强ASR即毁QA"的真实痛点；消融（ST-OPD对照、λ敏感性、数据扩展）系统，仅更新adapter、用500小时即取得近优ASR与全场最高QA，性价比高。局限是仅英文、4B规模与单一编码器架构，QA标签依赖LLM自动标注，代码未开放，对更大模型与中文场景可迁移性待验证。
## [3] Reward-Tilted On-Policy Distillation for Acoustic Grounding in Audio-Language Models

arXiv ID：2609.28778|方向：语音大模型
作者：Kaiyang Li、Shaobo Han、Yue Tian、Shihao Ji
机构：NEC Laboratories America（美国）| 康涅狄格大学计算科学学院（美国）
发布日期：2026-09-25|论文 https://arxiv.org/abs/2609.28778 |PDF https://arxiv.org/pdf/2609.28778.pdf |代码与Demo https://github.com/KaiyangLi1992/RT-OPD

### 📌 简介
音频语言模型（ALM）常借助文本捷径答题而忽视声学证据，导致"伪接地"。本文提出奖励倾斜在线蒸馏 RT-OPD：在同一问题与学生自生成文本下，让冻结教师分别在有音频与无音频条件下预测下一 token，以两者对数概率之差定义全词表奖励，用指数倾斜重塑教师分布，得到突出声学证据的蒸馏目标，再沿学生在线轨迹做反向 KL 蒸馏。在 MMAU、MMAR、ADQA-clean 三个基准上稳定超越 Vanilla OPD；蒸馏出的 3B 模型 Mizar-3B 在 MMAU 达 72.72% 准确率，为对比 3B 模型中最高，并可与部分 7B/8B 模型竞争。代码与权重已开源。

### 🔧 技术方案
**问题背景：** ALM 仅凭语言先验即可答对音频问题（如由"a dog is"补出"barking"），标准在线蒸馏只对齐教师的音频条件分布，未显式区分"音频增益的证据"与"纯语言可预测部分"，学生因此继承文本捷径。
**模型架构：** 学生（Ke-Omni-R-3B 或 Qwen2.5-Omni-3B）在线采样回复，冻结的 Ke-Omni-R-7B 教师对同一前缀同时输出"带音频"与"去音频仅留文本"两份下一 token 分布。
**核心创新：** (1) 以全词表奖励 r(v)=log p(音频)v − log p(无音频)v 度量每个候选 token 获得教师支持的音频增益幅度；(2) 用 exp(αr) 对教师分布倾斜重归一，得 q∝p^{1+α}/p_∅^α，α=0 退化为标准 OPD；(3) 反向 KL 损失分解为"标准蒸馏项+音频奖励最大化项+常数项"，相当于在蒸馏中显式加入对比奖励，并以教师答对为门控、叠加金标答案交叉熵。
**训练策略：** 仅更新学生 rank-64 LoRA，10k 条 AudioMCQ 多选数据训 2 epoch，全局 batch 32，α=1、λ=0.25；推理只需一次前向，无音频教师仅训练期使用。

### 📊 实验结果
**数据集**：MMAU 9k 测试集、MMAR、ADQA-clean(1577 题)，训练取 AudioMCQ-StrongAC-GeminiCoT 10k 子集，五种子均值。
- MMAU：Ke-3B 学生 RT-OPD 72.72% vs Vanilla OPD 72.21%、CE-only 71.32%
- MMAR：60.08% vs OPD 57.78%（增益最大 +2.3；Qwen 学生 +3.0）
- Macro-3：63.08±0.36 vs OPD 62.00，逼近 7B 教师 63.47 且 ADQA-clean 反超；Qwen-3B 为 62.26 vs 60.79
- 消融：优于不匹配参考音频、分布锐化、G-OPD 式模型参照、离策略变体
- 扰动分析：静音/替换音频后 RT-OPD 掉分更大（MMAR −22.46），印证更强声学依赖
**是否开源**：代码与模型 checkpoint 开源（GitHub）。

### ⭐ 评分：7/10
理由：用同一教师的音频有/无对比把"声觉接地"转成词表级奖励注入在线蒸馏，思路简洁、有损失分解的可解释性，消融与音频扰动分析直接支撑接地主张。不足：增益仅 1-3 分，教师与学生局限于两个家族且以选择题为主，生成式任务上的文本捷径消解待验证。
## [4] TEMA: Evidence-Grounded Temporal Question Answering in Multi-Turn Multi-Audio Dialogs

arXiv ID：2609.30029
方向：语音大模型
作者：Kaidi Yang、Hualei Wang、Zhaohui Wang、Chenxuan Wang、Hong Liu、Xiangdong Wang
机构：中国科学院计算技术研究所、中国科学院大学
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.30029
PDF：https://arxiv.org/pdf/2609.30029
代码：https://github.com/KadeeYoung/TEMA
Demo：暂无

### 📌 简介

多轮多音频时序问答要求模型在追问、录音切换与历史引用中持续追踪目标事件，恢复每条时间轴上的完整实例及其边界，才能完成时间计算与比较。本文提出TEMA框架：每轮依次生成Route（限定音频范围）、Span（把所有匹配区间描述为条件化音频字幕）、Reason与Answer，将事件感知与循证回答连接起来。配套构建40,704段对话的TEMA-Dialog语料与证据-答案联合评测的TEMA-Bench，训练采用时序定位初始化、全对话SFT与完整性优先的Span-only GRPO三阶段。在Qwen2.5-Omni与AF-Next上显著提升时序问答，事件定位与跨音频比较改善尤为明显，且仅对证据做强化学习即同时提升区间恢复与答案正确率。

### 🔧 技术方案

问题背景：现有音频时序定位（TimeAudio、TEMPO、TimePro-RL、TAG-Bench等）以单轮、单录音为主，AF-Chat与MUGEN虽涉及对话或多录音，却不要求恢复起止区间与显式时间计算；多轮多音频细粒度时序问答长期缺乏数据集、训练方法与基准。

基准与系统构建：整合AudioSet Strong、TACOS、AudioTime-frequency为统一事件表，人工筛选202个可数事件并用预测计数与标注IoU一致性核验；按事件标签Jaccard与CLAP相似度构建相似分组、辅以随机分组；由Qwen3.7-Plus"先规划后实例化"生成对话，规则引擎对照事件表核查Route/Span并用DeepSeek V4-flash审查事实性。TEMA-Dialog含40,704段对话、198,195轮、75,561条录音（多音频占78.8%，支持提前与增量上传）；TEMA-Bench Test253含253段对话、1,239问及逐轮金证据，任务分五大类18型（定位测量、识别验证、音频内结构、跨音频检索比较、多轮时序引用）。

核心创新：（1）查询条件化完整时序证据范式：Route界定待检音频范围，Span穷举范围内所有匹配区间、无匹配标[NONE]，把证据获取与计算选择解耦，缺一个实例即会改变计数与累计时长。（2）三阶段训练：先用TimeAudio FTAR的98,401条样本做查询-区间对齐初始化，再全对话SFT学会生成与使用证据，最后Span-only GRPO仅优化Route/Span，奖励联合核查音频范围、实例数、缺失状态与边界（0.1秒内一对一匈牙利匹配；完整候选≥0.9、不完整≤0.1，完整性优先），避免开放式答案难以用字符串匹配或LLM裁判可靠验证的问题。（3）证据-答案联合评测协议：DeepSeek V4-flash判非时序事实、确定性规则以0.1s容差验时序值，报QA、QA+T、Span micro F1@0.5与完整证据H@0.1。

评测协议：Test253上贪心解码、模型自生成历史构成自然多轮链路，对比Qwen2.5-Omni-7B、AF-Next-Instruct、TEMPO及闭源Qwen3.5-Omni-Plus、Gemini 3.5 Flash，并设供给金Route/Span的诊断实验。

### 📊 实验结果

数据集：TEMA-Bench Test253（253段对话、1,239问）
- 总体QA（Qwen2.5-Omni三阶段）：69.81%
- 总体QA（AF-Next三阶段）：58.84%
- 原始Qwen2.5-Omni-7B基线QA：46.09%
- QA+T（含自述时间声明核验）：58.76%
- Span micro F1@0.5：44.39%
- 完整证据H@0.1：58.65%
- F1定位测量类QA：62.03%（基线26.05%）
- F4跨音频比较QA：51.11%（基线22.67%）
- F5历史引用QA：69.44%
- 金证据诊断QA：96.45%（I+S模型）
是否开源：是，代码、数据细节与模型权重已发布于GitHub。

### ⭐ 评分：7/10

首次系统定义多轮多音频时序问答任务，并打通数据-训练-评测闭环；"仅对可验证证据做RL即可提升答案质量"的假设由消融与金证据诊断双重支撑，Span-only GRPO的完整性优先奖励设计规避了开放式AQA的裁判不可靠问题，工程贡献扎实。扣分在于：数据大量依赖闭源模型生成与审计，事实一致性风险未完全排除；Test253规模偏小、绝对性能仍低且GRPO后F4反而微降（53.33%→51.11%），跨音频操作收益不稳定的根因分析不足；骨干仅7B级，未验证更大模型上的天花板。
## [5] AdaptDuplex: from static to adaptive full-duplex spoken dialogue

arXiv ID：2609.29217|方向：语音大模型|作者：Zhiyang Zhou, Yingxin Shang, Zhou Wang, Hongwei Cai, Weixu Wang, Shuran Zhou(通讯), Shuofeng Zhao, Wenke Fan, Qingxiang Guo, Dawei Yang, Lin Yang, Yang Song|机构：作业帮教育科技(Zuoyebang Education Technology)|发布日期：2026-09-25|论文 https://arxiv.org/abs/2609.29217 |PDF https://arxiv.org/pdf/2609.29217.pdf |代码与Demo：暂无(仅公开附录语法页 https://adaptduplex.github.io/appendix)

### 📌 简介

现有全双工语音对话模型（如 DuplexOmni、MiniCPM-o 4.5）在设计与训练期就把窗口时长和可用动作集合写死，打断、附和、静默监听等行为沦为静态操作点，无法随对话节奏与认知负荷逐时刻调整。AdaptDuplex 以 Qwen3-Omni 为底座，围绕"每个行为决策都是一个显式 token"这一原则进行三层协同设计：紧凑的规范化 token 序列协议、动态预测短/中/长三档窗长并可叠加非阻塞记忆整合与至多 4 路并行外部推理的自适应机制、课程化渐进训练管线。推理期还可通过 logits bias 免训练调节听/说倾向。模型在 Full-Duplex-Bench v1/v1.5 与真人录音 HumDial-FDBench 上，交互决策与响应时序全面领先对比的全双工模型。

### 🔧 技术方案

**问题背景：** 全双工对话要求模型亚秒级延迟边听边说，而时序与认知需求瞬息万变；既有方法把时间粒度与动作空间硬编码进协议与训练设定，协议要么笨重难以随决策扩展，要么稀疏到无法承载复杂策略，缺乏系统性的自适应决策机制。**模型架构：** 继承 Qwen3-Omni 的 Thinker–Talker 架构，Thinker 从"每轮生成完整回复"改为逐窗口输出交互决策：每个窗口由 Unit 定界符包裹，按固定顺序编码 listen/speak 控制、动作 token 序列（memory 与索引化 launch:N/cancel:N）、可选回复文本、下一窗口 token 与边界 token；Talker 在 <|speak|> 时对历史一次性预填充，随后自回归生成 codec 音频，文本经轮内 FIFO 按声学位置弹出、空位以 tts_pad 填充。**核心创新：** (1) 紧凑规范化协议：相比 DuplexOmni 的 JSON 序列化削减约 78% 协议 token，消除结构非法输出并降低解码延迟，决策显式为 token 后可在推理期用 logits bias 免训练调节运行时操作点；(2) 双流对齐：受限 Text-ahead 文本前移策略配合交错 text/tts_pad 条件，不改 Talker 结构即实现有界文本超前的流式文本–语音对齐；(3) 自适应交互机制：仅凭因果上下文动态预测 0.48/0.64/0.96 秒三档窗长，并以 L1 记忆后端与 L2 至多 4 路异步外部推理对直接回复做非阻塞增强，失败与无返回均不阻塞当前响应。**训练策略：** 按数据难度对 Thinker 做三阶段课程 SFT（单轮协议→基础双工事件→完整动作编排），再 Talker-only SFT 与联合 SFT，最后 GRPO 精调交互策略；数据为自动多智能体管线合成的 765,424 段对话（17,259 小时，其中助手语音 10,857 小时），8 张 H100 完成训练。

### 📊 实验结果

**数据集**：评测用 Full-Duplex-Bench v1/v1.5（合成轮次与重叠场景）与中英真人录音 HumDial-FDBench；训练用内部合成全双工语料。
- HumDial-FDBench Final：72.9，优于 MiniCPM-o 4.5 的 66.7、DuplexOmni 的 57.3、Qwen3-Omni+VAD 的 66.5，为全双工模型最高
- HumDial 延迟(ALL)：1.042 s（中 0.835/英 1.345），快于 MiniCPM-o 4.5(2.203) 与 DuplexOmni(4.459)；拒绝率 49.1%
- FDB-v1 打断：TOR 0.985 且响应延迟 0.131 s（DuplexOmni 0.746/0.158）；纯附和场景 TOR 0.334 对 0.491
- FDB-v1.5 重叠：背景语音行为得分 0.43 对 0.07、附和 0.55 对 0.28，四场景响应延迟均为全场最低(0.30–0.37 s)
- 协议效率：每窗口 5.87 token 对 JSON 式 26.44，解码 P50 从 789 ms 降至 419 ms，非法输出归零
- 对齐消融：随机前移使 UTMOSv2 从 2.90 升至 3.65，中英 CER/WER 近乎减半，ValidEnd 从 50% 升至 86.37%
- 训练消融课程 vs 混合单阶段：响应延迟 1.65→0.37 s，GRPO 再将 talking-to-others 从 0.35 提至 0.44
- 动作预测：L1 memory F1 80.66%，L2 动作 EM 76.84%、launch F1 68.63%，两路以上并发降至 65.17%
**是否开源**：模型、代码与合成语料均未开源，暂未提供在线 Demo，仅公开附录语法页。

### ⭐ 评分：7/10（协议-机制-训练三层协同设计系统性、决策即 token 支撑免训练运行时控制、三个基准消融充分、真人评测领先，工程价值突出；扣分在底座复用 Qwen3-Omni 的增量式改造、依赖内部合成数据且不开源不可复现，评测仅中英、窗长仅三档离散、并发上限 4，外部推理依赖后端质量。）
## [6] AEGIS: Audio Endogenous Guarding via Internal Signals Against Large Audio-Language Model Jailbreaks

arXiv ID：2609.29287
方向：语音大模型
作者：Yu-Ling Liao、Tzu-Chin Chiu、Zong-You Chen、Chi-Lei Tsai、Shao-Yuan Lo
机构：台湾大学（National Taiwan University）
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.29287
PDF：https://arxiv.org/pdf/2609.29287
代码：https://github.com/azzzzliao/aegis-audio-defense
Demo：暂无

### 📌 简介

本文针对大型音频语言模型（LALM）面临的异构音频越狱攻击（语义混淆、多语言、副语言风格、波形扰动等），提出一个关键问题：越狱成功究竟是模型没识别出有害意图，还是识别之后没能触发拒绝？作者通过逐层探针分析发现风险信息在中间层仍可解码，但深层拒绝倾向接近于零，将此解耦现象命名为"风险-拒绝鸿沟"。据此提出 AEGIS 端到端防御：用轻量 MLP 风险门读取中层隐藏状态得到连续风险分，据此选择性激活后置层的 LoRA 安全适配器，把模型内部本已保留的风险信号转化为可靠拒绝。在 6 个 LALM、3 个越狱基准上平均不安全率从 17.9% 降到 0.4%，且正常输入的过度拒绝仅小幅上升。论文投稿 ICASSP 2027。

### 🔧 技术方案

问题背景：现有音频越狱防御（输入侧过滤、安全训练、表示级引导）能降低不安全输出，但无法解释安全对齐在哪个环节失效。本文用两个逐层信号回答：其一为逐层风险可解码性，即在每个解码层取最后一个输入 token 的隐藏状态训练独立线性探针，以越狱成功有害输入与良性输入的二分类 AUROC 衡量风险信息在各层的留存程度；其二为逐层拒绝倾向，即把各层隐藏状态投影到词表空间，统计预定义拒绝句式首 token 的 softmax 概率质量并按生成步平均。观察到风险可解码曲线在中深层持续上升而拒绝概率恒接近零，即风险-拒绝鸿沟。

框架：AEGIS 冻结基座模型，仅联合训练两个轻量组件。中层风险门在探针选定的层 lg 提取末尾 prompt token 表征，经 MLP 加 sigmoid 得到连续风险分 g；后置层插入 LoRA 安全适配器，隐藏状态更新为 h 加上 α·g 倍低秩残差，即以 g 作为强度调制因子；推理时只有风险分超过阈值才激活适配器，激活后 α 通过闭环缩放逐步增大直至满足预定拒绝标准。

核心创新：(1) 首次以逐层探针在 6 个 LALM 上实证风险信息与拒绝行为的解耦，给出可诊断的"风险-拒绝鸿沟"机制解释；(2) 提出检测后干预范式，把模型内生风险信号直接复用为门控来源，而非外挂独立守卫模型，且门控稀疏激活降低对良性行为的扰动；(3) 风险分连续调制 LoRA 残差强度并配合闭环放大，实现按风险程度分级干预。

训练协议：损失为语言建模损失（仅response token）加 BCE(g,z) 监督风险估计（权重 1.0），加 0.01 稀疏惩罚抑制门控误激活，基座全程冻结。

### 📊 实验结果

数据集：攻击侧用 AJailBench-Origin（1490 条，信号级扰动）、JALMBench 的 SSJ+ADiv（946 条，语义混淆与多语言）、SACRED-Bench-MSD（1364 条，多说话人组合攻击）；良性评估用 Qwen3-TTS 合成的 XSTest 音频版，训练良性样本来自 JBB-Behavior TTS 转换与 LLM 生成指令。模型覆盖 Qwen2-Audio、VITA-1.5、Ultravox v0.5、Phi-4-MM、Voxtral-Small-24B、Gemma 4 E4B。指标：以 Llama-Guard-3-8B 判定不安全率（即攻击成功率 ASR）与过度拒绝率。域内训练下平均不安全率 17.9%→0.4%（18 个模型-基准对多数降至 0-1.6%），过度拒绝平均仅 +6.3 个百分点；留一基准（LOBO）迁移设定平均不安全率仍降至 2.6%。对比 RRS、OmniSteer、ALMGuard、SARSteer、ASR 预处理与提示防御，AEGIS 是唯一在三个基准全部低于 1% 的方法，SARSteer 虽强但在 SACRED 残留 26.9% 且过度拒绝 +41.6。消融显示去掉门控的 always-on 或全层 LoRA 均使过度拒绝升至 +22。代码已开源，Demo 暂无。

### ⭐ 评分：7/10

理由：机制发现清晰可验证，探针驱动的"内部信号自防御"思路优雅，6 模型 3 基准加 LOBO 泛化证据充分，安全-效用权衡显著优于现有基线，且开源。减分点：ICASSP 短文（5 页），线性探针 AUROC 与拒绝 token 概率均为代理指标，机制解释并非直接因果；仅单模型做基线对比；未评估针对该防御的自适应攻击（门控本身可被绕开风险分数）；Voxtral/Ultravox 在 AJail 的 LOBO 迁移仍残留 4-10.3% 不安全率；依赖模型内部访问，闭源 LALM 不可用。综合评价为扎实且有启发性的防御工作。
## [7] PTC-Bias: Phoneme-Level Temporal Competition for Bias Retrieval and Post-Decoding Correction in Speech LLMs

arXiv ID：2609.28727
方向：语音大模型
作者：Zhiqi Ai、Han Cheng、Shiyi Mu、Yongjin Zhou、Shugong Xu
机构：上海大学；西交利物浦大学
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.28727
PDF：https://arxiv.org/pdf/2609.28727
代码：https://github.com/aizhiqi-work/PTC-Bias
Demo：暂无

### 📌 简介
本文提出 PTC-Bias，一个面向 SpeechLLM 的音素级时序竞争两阶段上下文偏置框架。预填充阶段，PTC Retrieval 在帧同步音素解码基础上对候选发音做时序竞争，产出精简偏置词表及对应语音区间；解码后，PTC Correction 在区间内对检索词与不匹配转写片段做第二次局部竞争，选择性纠正近同音与词切分错误，同时保留正确转写。两阶段共享同一音素后验，无需额外 SpeechLLM 前向。LibriSpeech 上，2000 偏置词时相对 CTC-Filter 降低 B-WER 约 23.4%/23.9%，U-WER 几乎不变。

### 🔧 技术方案
问题背景：SpeechLLM 识别稀有词（人名、术语）仍需偏置列表，但把大列表直接塞进 prompt 会增加推理开销并引入词汇干扰；现有检索方法对候选独立打分，同一语音片段上的多个近同音词可同时入选而缺乏竞争建模；且即便正确偏置词进入 prompt，模型仍可能输出高频同音词或错误切分，单靠检索无法保证纠正。

方法：在冻结音频编码器上接轻量 phoneme-CTC 分支，对全部 Transformer 层输出做可学习权重求和，经两层 Transformer 与 CTC 头输出 71 类音素后验，词经 g2pE 转成带重音 ARPAbet。PTC Retrieval 将候选发音编成共享前缀字典树做帧同步搜索，每个词保留长度校准（βlogU）的最优 CTC 路径及区间 [a,b]；取前 M=100 个事件，把区间重叠者视为同一声学证据的竞争解释，对互斥兼容子集族用温度 softmax 加权并经区间前向-后向高效计算每个事件的包含边缘概率，超过阈值的按边际置信排序，最多 K=10 个词连同区间注入 prompt。PTC Correction 将初始转写与后验对齐，找到与检索区间重叠且音素相近的短片段，把候选词与转写片段分别拼接左右共享音素上下文，在局部窗口内计算两条序列 CTC log 前向概率之差作为声学边际；边际超过阈值 2.0 并通过词汇与边界检查才执行替换，完全同音词仅在罕见词或切分受限条件下处理，冲突编辑由边际与检索边际联合裁决。

核心创新：（1）首次将音素级"时序竞争"引入偏置检索：重叠区间事件互为竞争解释，用区间前向-后向算包含边缘，一次性解决检索与定位并抑制近同音干扰。（2）解码前检索与解码后纠错共享同一份缓存音素后验，低成本补上"检索命中不等于生成正确"的缺口。（3）完全免训练 backbone、不改 prompt 接口的即插即用设计，纯 CPU 毫秒级检索，可扩展到 5 万词表。

解码协议：SpeechLLM 全程冻结；偏置 prompt 至多 10 词；检索与纠错复用同一份音素后验缓存，无任何额外编码或 LLM 前向。

### 📊 实验结果
数据集：LibriSpeech（460h/960h 训练音素前端，test-clean/test-other 评测，Rare5k 协议，干扰词 N=100~2000）；骨干为 Prompt-SLAM-ASR-7B 与 Qwen3-ASR-0.6B，前端对比 DS-KWS、AuT、WavLM。
主要指标（N=2000，clean/other）：
- B-WER（Prompt-SLAM-ASR-7B）：3.38%/7.63%，对比 CTC-Filter 的 4.41%/10.02% 相对降低 23.4%/23.9%
- WER：1.30%/2.93%；U-WER：1.06%/2.43%（基本无损）
- B-WER（Qwen3-ASR-0.6B+AuT）：4.45%/8.61%（基线 5.08%/9.24%）
- Recall@99：16.9 个候选达 99% 召回（BR-ASR 声学版 42.2）；top50 内近同音干扰召回 22.0%（原 69.3%）
- 音素 PER：WavLM 1.13%/2.27%，AuT 2.06%/5.13%，DS-KWS 4.45%/11.80%
- 检索延迟：7.61ms@2000 词（4 worker），34.74ms@5万词（16 worker）
是否开源：代码已开源（GitHub: aizhiqi-work/PTC-Bias）；论文 5 页，处于 under-review。

### ⭐ 评分：7/10
理由：动机精准（独立打分的检索缺竞争建模、检索命中仍可能生成同音错词），时序竞争+两阶段共享后验的设计优雅、零侵入、可工程落地，结果一致且代码开源。扣分：仅英语 LibriSpeech 与 Rare5k 合成协议，缺少真实业务热词与中文等高同音密度场景验证；纠错阈值与边际判定的消融不够充分；严格同音词仍依赖受限规则兜底；5 页篇幅使定性分析偏浅。属扎实高效的即插即用型改进。
## [8] A Harness for Synthesizing Diverse Naturalistic Full-Duplex Conversations

arXiv ID：2609.28806 | 方向：语音大模型 | 发布日期：2026-09-25 | 论文 https://arxiv.org/abs/2609.28806 | PDF https://arxiv.org/pdf/2609.28806.pdf | 代码与Demo：暂无

作者：Matthew Sun、Vinay Kothapally、Meng Yu、Chao Huang、Hao Zhang、Yixuan Zhang、Steve Yves

机构：Tencent Americas（Palo Alto/Bellevue）| 西北工业大学电子信息学院

### 📌 简介
本文提出一个可编程控制的语音数据合成harness（管线），用于批量生成带意图标注的英/中双语两通道全双工对话语音，直指真实语料对打断、附和、旁聊等事件缺乏可控性与意图标签的痛点。LLM仅编写含说话人、文本、对话行为与依附关系的关系事件列表，不预测绝对时间戳；随后经TTS独立渲染、强制对齐测词界、按锚点与偏移装配到共享时钟上，覆盖8大家族42种现象。论文以生成消融、语义VAD标注恢复和Moshi微调迁移三级评测证明：受控合成能为全双工轮次管理提供可学习且可迁移的监督信号。

### 🔧 技术方案
**问题背景：** 全双工系统需边说边听：沉默可能是轮内停顿或轮次完成；重叠语音可能是抢话、附和或旁聊，声学模式相似而正确响应截然不同。真实语料不标注意图且现象不均衡；为说话人分离设计的音频混合把不同意图的重叠赋予相同活动标签；文本对话合成则无法控制声学时间轴，形成监督缺口。
**架构与数据管线：** 将"创作"与"声学实现"解耦。8大场景家族42个scenarioID下，DeepSeek按关系事件图生成JSON对话（事件含说话人、文本、行为及参照更早事件的cue，仅backward引用构成DAG），经静态校验、时间线预检、文本过滤与可选LLM评审后，用Qwen3-TTS逐事件独立合成，Qwen3-ForcedAligner测词/字级边界，再按引用锚点、插入静默与带符号偏移在80ms网格双通道时钟上以样本精度装配；成功抢话截断被话者尾部。轮间间隙、轮内停顿、抢话反应时分别从未指定时的文献先验分布回退采样，且停顿与转轮分布刻意重叠，杜绝时长阈值捷径。帧级标签（取floor/保持/放floor/监听及13类细粒度态）由创作意图+声学活动推导，改标签体系或帧率无需重合成。另支持音色库采样与RIR/MUSAN噪声扰动，保持事件结构与标签不变。
**核心创新：** (1)关系事件表示：把时间戳预测从LLM与TTS中剥离，语音地标从渲染信号实测，静默由规格或分布给出；(2)少样本双多样性hub：结构hub用27维地板特征向量与act序列距离（加权0.75/0.25）混合表征，语义hub用BGE-M3 1024维嵌入，二者以在线max-min coreset维护32容量内的负记忆提示防模式坍缩；(3)概率言语化批量创作：单次调用要求5个完整对话及自报概率，显式激发低频备选，与hub跨调用记忆正交组合。
**评测协议：** 三层递进：固定场景的单项消融以EAD、Vendi、ROUGE-L与NN距离验证各机制针对性目标；中英内建因果semantic VAD仅用当前与历史音频在4-token核心与13-token合并标签空间上预测地板动作，分clean与用户通道加噪两条件；最后在Moshi（Moshiko检查点）上微调，以自由生成与teacher forcing评测轮次接管、地板精度与SS/SL地标F1。

### 📊 实验结果
**数据集**：自合成英/中双语两通道语料（42现象）；VAD实验同split为19,575训练/2,756验证段，验证集91万帧80ms标签；Moshi实验英文子集5,906训练/890验证段，2000步微调。
- 生成消融：结构hub使特征空间Vendi +64.2%、NN均距 +95.0%、act序列EAD-2 +185.7%（无hub时抢话/截断完全坍缩）；语义hub语义Vendi +3.6%；概率言语化使语义Vendi +68.7%、词汇EAD-2 +37.6%，但结构作用混合
- Semantic VAD（4-token核心）：clean准确率0.9932，start-speaking F1 0.8186、start-listening F1 0.8019；加噪仅降0.0003，主要地板转换稳定，退化集中于静默敏感类
- 13-token合并空间：clean准确率0.9613；合并用户/同伴来源使hold-backchannel F1由0.7120升至0.9061、yield由0.7211升至0.7853；稀类barge-in仅0.4325
- Moshi迁移：自由生成参考轮接管率0.44→0.85、地板精度0.46→0.88；teacher forcing地板F1 0.893→0.962；3帧容差SS F1 0.066→0.145、SL F1 0.037→0.122
**是否开源**：文中称已有released corpus质量标准但正文未给下载/代码链接，代码与Demo暂无。

### ⭐ 评分：7/10
创作与渲染解耦、意图派生标签直指全双工训练的真实痛点，管线工程扎实，三层评测与Moshi迁移证据链完整；但全部实验基于自建语料与内建基准，缺乏与真实语料训练及外部系统的对照，自由生成地标分数仍低，语料规模与开源地址交代不清，可复现性打折。
## [9] ReaFlow-TTS: Realization-Conditioned Flow Matching for High-Quality and Controllable Speech Synthesis
arXiv ID：2609.28906
方向：语音大模型
作者：Junyi Zhao、Changsheng Ma、Yihao Qin、Yongfeng Tao、Minqiang Yang（通讯）、Hu Bin（通讯）
机构：兰州大学信息科学与工程学院
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.28906 | PDF：https://arxiv.org/pdf/2609.28906 | 代码：暂无 | Demo：暂无

### 📌 简介
针对流匹配TTS中同文本不同语音实现（realization）导致目标速度不一致、确定性网络只学到条件均值而抹平实现变化的问题，本文提出ReaFlow-TTS：引入话语级随机实现潜变量z并在整条流轨迹上条件化速度预测，同时用VAD（效价-唤醒-支配）语义结构化潜空间。推理时可直接从先验采样、无需目标语音，并沿VAD轴做分级属性操控。实验在音质上超越F5-TTS基线，且潜变量跨初始噪声可复现地影响音高、能量与时长。

### 🔧 技术方案
问题背景：同一段文本可有不同音色、韵律与情绪的实现。借鉴变分修正流匹配（VRFM）的速度歧义分析，不同源-目标对在同一状态与流时间下目标速度不同，平方误差损失使确定性速度网络预测条件均值，实现级变化被边缘化；且单纯建模变化并不天然提供可语义解释的操控接口。
模型架构：基于DiT的条件流匹配框架，24kHz音频、100维对数梅尔谱，推理模型约158M参数，配Vocos声码器。新增256维话语级实现潜变量z，由9层DiT后验编码器从目标梅尔谱推断并按AdaLN调制各DiT块；z在帧间共享、在ODE积分全程固定，为轨迹级一致条件。
核心创新：(1) 实现条件化速度建模：将网络扩展为v(x_t,t,c,z)，用KL项将后验对齐标准高斯先验，推理时可从先验直接采样z，摆脱对目标语音的依赖。(2) 潜空间VAD语义结构化：冻结audEERING的Wav2Vec2（MSP-Podcast微调）作为教师，用后验均值经线性映射W预测VAD三属性，并以同文本异实现的成对数据构造绝对对齐损失与相对距离保持损失联合监督。(3) 分级操控接口：推理丢弃编码器与教师，通过W的正则化右逆把目标VAD变化量映射为潜变量偏移Delta z，强度eta连续可调，eta为零时还原基底实现。
训练策略：两阶段。第一阶段在过滤后LibriTTS上用基础损失（KL权重3e-4）训练50万步；第二阶段在ESD英文子集加入属性与距离损失（KL权重1e-3，两项系数0.05）续训10万步；AdamW，学习率7.5e-5。

### 📊 实验结果
数据集：训练用LibriTTS（554h）与ESD英文子集（10说话人5情绪平行语料）；音质评测用F5-TTS的LibriSpeech-PC test-clean同说话人跨句1127对；30名英语母语者主观评测。
- WER：2.09%，优于F5-TTS 2.27%、全掩码基线2.32%、ZipVoice 2.24%，与真值2.28%相当
- UTMOS：4.19，高于真值4.10及所有基线（3.83至3.91）
- NMOS：3.91（500k版3.93），达真值3.93水平，基线为3.63至3.72
- 分级VAD操控：eta取0/0.5/1时唤醒3.38/4.76/5.23、支配3.71/4.98/5.36，排序准确率最高92%；效价敏感度较弱；NMOS仅小幅波动
- 潜变量复用性：3个z与9组匹配初始噪声交叉，F0、能量、时长倾向跨噪声稳定复现
是否开源：暂无公开代码与Demo。

### ⭐ 评分：7/10
理由：动机精准，把VRFM的速度均值问题引入TTS实现建模，方法简洁（一个先验潜变量加一个线性VAD映射即同时换来音质与可控性提升），跨噪声复现实验为"z确被速度场使用"提供了难得的行为证据；全掩码下仍超F5-TTS，质量指标达真值水平。不足在于仅限英文小语料、未与前沿LLM-TTS系统对比，效价方向操控偏弱，且未开源，可复现性与影响力受限。
## [10] Depth through recurrence: Looped transformers for flow-matching TTS

arXiv ID：2609.29768
方向：语音大模型
作者：Jiabao Ai、Peng Han、Yuchen Song、Zhengjun Yue
机构：Shenzhen Loop Area Institute（深圳）、香港中文大学（深圳）
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.29768 ｜ PDF：https://arxiv.org/pdf/2609.29768 ｜ 代码：暂无 ｜ Demo：https://jiabaoai67.github.io/loop-f5/

### 📌 简介
本文系统研究在 flow-matching TTS 的 velocity 网络中如何用"循环深度"（权重跨层复用、迭代加深）组织 Transformer，即以参数共享的若干 block 在同一网络前向内被多次执行，用更少独特参数保留等效执行深度。作者在统一目标、采样器与宽度下比较七种复用布局（全共享环、相邻序列重复、部分共享的前/中/后段），在 Seed-TTS 与 LibriSpeech-PC 上考察参数量、采样步数与可懂度、说话人相似度、预测音质之间的权衡，为按推理预算与质量维度选择布局提供依据。

### 🔧 技术方案
问题背景：Voicebox、E2 TTS、F5-TTS 等 flow-matching TTS 在数值积分中反复调用 velocity 网络，计算量由网络深度与采样步数两个维度决定；通用 Transformer 与 ALBERT 已证明跨层共享可行，但复用次序与共享位置在流匹配生成中如何与采样预算交互尚不清楚。模型架构：基于修改版 F5-TTS Small（宽度 768），速度网络 v(x_t,t,c) 以隐状态 h 条件于流时 t 与文本/参考语音上下文；共享段 F 在各次访问间权重不变、隐状态不重置，访问间无 index embedding 与辅助监督；所有布局固定每次网络评估执行 18 个 block。核心创新（1）固定执行深度 D=18 构造七种布局，严格分离共享量、复用次序、共享位置三因素：Baseline 18 独立 block（158.0M）、CYCLE 9x2 整栈环绕与 SEQUENCE 9x2 相邻重复（均 83.6M）、CYCLE 6x3（58.8M）、以及仅共享段位置不同的 Prefix/Middle/Suffix（108.4M）；（2）将布局与采样步数 N 耦合，block 调用预算 B=2ND（CFG 双分支分计），在 32 步与 4 步及中间步追踪排序变化；（3）机理诊断每次调用相对更新幅度、共享 block 两次访问更新余弦与调用移除敏感度。训练策略：LibriTTS 从零训练；AdamW 峰值 7.5e-5，20k warmup 线性衰减，bf16，每次更新最多 307,200 mel 帧（8 GPU），CFG dropout；各布局单次训练，统一用 500k 步 EMA 评测。

### 📊 实验结果
数据集：训练 LibriTTS；评测 Seed-TTS test-en（1088 句）与 LibriSpeech-PC（1127 句、39 人）。统一 Euler 采样、CFG 2.0、fp32、Vocos 声码；WER 用 Whisper large-v3，SIM-o 用 WavLM/ECAPA，UTMOS 预测音质；主表跨 4/3 个推理种子并做 bootstrap 区间。主要指标（32 步，Seed-TTS）：
- WER：SEQUENCE 2.03% 对比 Baseline 2.23%，参数 83.6M 对 158.0M 减 47.1%
- SIM-o：0.573 vs 0.567；UTMOS：3.75 vs 3.68，CYCLE 9x2 最高 3.90
- 同参数对比：均 83.6M 均 18 次调用下 SEQUENCE 的 WER 显著优于 CYCLE 9x2（2.03% 对 2.60%，-0.57pp），但后者音质略高；CYCLE 6x3（58.8M）WER 升至 2.96%，可懂度受损
- 预算交互：4 步时 Suffix 比 Prefix 差 3.44pp（Seed-TTS）/5.97pp（LibriSpeech-PC），32 步仅差 0.17/0.14pp；仅 Middle 在两数据集两 budget 平均 WER 均列前二（32 步 2.04/2.07%）
- 资源：SEQUENCE/CYCLE 峰值显存较 Baseline 降 34.5%（877 对 574MB），七布局 RTF 相当（约 0.143）
开源：Demo 页面公开，训练代码暂无。

### ⭐ 评分：7/10
优点：首个在 flow-matching TTS 中把共享量/次序/位置与采样步数解耦的系统对照；控制严格、多 seed bootstrap、调用移除与访问余弦诊断提供机理解释；SEQUENCE 同执行深度减参 47.1% 且 WER 略优，对端侧低步数部署有直接参考价值。不足：仅一个规模、单次训练 run、仅英文客观指标、无听测；Baseline 2.23% 弱于原版 F5-TTS，绝对水位存疑；Middle"全预算领先"仅在 WER 成立。属扎实实证短文，创新在实验设计与分析而非新方法。
## [11] STAM-ASR: Speaker-Temporal Anchoring with Memory for Multi-Speaker ASR

arXiv ID：2609.29805
方向：语音大模型
作者：Victor Tolulope Olufemi、Syeda Faiza Ahmed Sara（同等贡献）、Shammur Absar Chowdhury
机构：Qatar Computing Research Institute（QCRI），卡塔尔多哈
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.29805
PDF：https://arxiv.org/pdf/2609.29805
代码：暂无
Demo：暂无

### 📌 简介

多说话人会议转写需同时回答"说了什么、谁说、何时说"。本文提出STAM-ASR，一个在预训练AudioLLM（Qwen2.5-Omni-7B，编码器冻结）之上的轻量扩展框架：不依赖外部日志系统、不做显式语音分离，直接从AudioLLM中间层特征学习说话人活动与说话人表征，以残差FiLM方式把"谁、何时"线索注入语义表征；并用共享Q-Former维护固定长度的说话人记忆与会话记忆，跨轮次携带互补上下文。在AMI、ICSI、LibriCSS、NOTSOFAR-1的近讲、远场、重叠与跨域条件下评测，自动分段下多数场景取得最优cpWER，分析表明说话人活动预测仍是主要瓶颈。

### 🔧 技术方案

问题背景：传统说话人归属ASR需级联外部日志或目标说话人条件化，重叠语音依赖分离或序列化输出训练，而长音频的说话人跟踪与上下文记忆常被分开处理，难以同时保留说话人特定与会话级信息。

模型架构：四组件流水线。其一，冻结音频编码器提取中间表征H_mid（第15层，层内说话人探针准确率94.3%）与语义表征H_sem；其二，基于Transformer的轻量内部日志模块直接作用于H_mid，输出多标签说话人活动（显式支持重叠）与说话人感知隐状态，再经活动加权池化得到各说话人表征；其三，说话人-时间调制：由说话人表征与活动预测特征缩放偏移参数，对H_sem做残差FiLM变换，不改变序列长度与维度，重叠段各活跃说话人共享混合表征但分别条件化；其四，记忆条件化ASR：固定token数的说话人记忆按同人轮次递推、会话记忆按时间顺序递推，以边界token包裹后拼入当前轮表征，由AudioLLM生成说话人归属转录。

核心创新：(1)内部日志复用预训练编码器特征，免除外部说话人编码器与独立声学前端；(2)残差FiLM把"谁-何时"线索无侵入注入语义表征，天然支持重叠多说话人并行解码；(3)说话人/会话双固定长度记忆互补保留跨轮上下文，推理期可选择性启用各组件而无需重训。

训练策略：训练数据约143小时（AMI、ICSI、Mixer6），日志预训练另用约200小时（AMI加NeMo_simulator仿真的LibriSpeech多人会话）。先1轮日志预热，再联合优化日志头、FiLM、Q-Former与LoRA(r=8)，编码器与LLM基座冻结；损失为语言建模交叉熵加Sortformer混合日志目标(α=0.25)；参考活动时间概率从1渐进退火到0以弥合训练-推理失配；分块≤20秒，前2轮仅预热记忆。

### 📊 实验结果

数据集：AMI-IHM/SDM、ICSI、LibriCSS、NOTSOFAR-1；基线为Qwen2.5-Omni-7B、Whisper-large-v3+pyannote级联、TagSpeech-AMI。

主要指标（cpWER/tcpWER@5，参考分段）：
- STAM(参考活动)：AMI-IHM 25.3、ICSI 20.4、LibriCSS 18.5、NOTSOFAR-1 52.6
- STAM(预测活动)：AMI-IHM 51.5、ICSI 47.7、LibriCSS 53.3、NOTSOFAR-1 76.6
- 对比TagSpeech：AMI-IHM 54.3、LibriCSS 63.2；对比Qwen-Omni：AMI-IHM 58.5

VAD自动分段下STAM在AMI-IHM 61.8、ICSI 58.2、LibriCSS 69.0、NOTSOFAR-1 78.1均为最优，仅AMI-SDM略逊TagSpeech(73.3对71.7)。全会议gDI-cpWER显著领先：AMI-IHM 37.6对52.1、LibriCSS 41.5对48.9。消融显示：近讲会议场景全组件最优，远场/跨域单用说话人-时间条件化更好。内部日志模块AMI-IHM DER 36.6%，明显差于pyannote的12.3%，印证跨长录音的说话人跟踪是残余瓶颈。

是否开源：论文未提供代码仓库，暂无。

### ⭐ 评分：7/10

理由：思路务实且完成度高——在冻结AudioLLM内部长出日志与记忆，免前端、免分离、免扩维，评测覆盖四类条件并给出诚实的组件消融与瓶颈分析，工程启发强。扣分在于：预测活动下性能大幅回落，内部日志DER远逊商用系统，核心收益高度依赖参考日记；TagSpeech对比协议非严格复现；数据规模小且未开源，可复现性受限。创新为组合式而非范式级突破，故评7分。
## [12] To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech

arXiv ID：2609.30227
方向：语音大模型
作者：Debajyoti Mazumder、Mamta、Abhirama Subramanyam Penamakuri
机构：IISER Bhopal、King's College London、MBZUAI
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.30227v1 | PDF：https://arxiv.org/pdf/2609.30227v1 | 代码：暂无 | Demo：暂无（数据集 Hugging Face: abhiram4572/VeriSpeak）

### 📌 简介
本文提出 VeriSpeak：面向大音频语言模型（LALM）的语音事实核查探针基准，含 3879 条时间、地理、关系三类语音声明，标签真假平衡，声学与文本证据跨模态。论文系统检验核查能力能否从文本迁移到语音，以及检索与显式推理能否弥合模态差。核心发现是该迁移并不自动发生：语音输入平均准确率骤降约 5 个点到 86.1% 之间波动，单纯检索收益有限，模型常把检索文本误当作待核查声明，而"检索加推理"可让思考微调模型反超纯文本基线。

### 🔧 技术方案
问题背景：新闻、播客与视频里的虚假声明多以语音形态传播，语音核查与图-文核查不同——声明本身是声学信号，可用证据主要为文本，模型须在把语音声明作为核查对象的同时对检索证据推理。
方法：以 KVQA 名人传记为知识库、抓取维基补全出生国与性别并做审计修正，再用正则、spaCy NER 与关系关键词标注年份、地点、关系三类事实；用 Llama-3.2-3B 抽取原子化无代词单句声明，并用确定性扰动生成负例（年份偏移、国家同类替换、关系词或人名实体替换），Coqui tacotron2-DDC 单说话人 TTS 合成音频，附 wav2vec2 自动转录标签。评测设 C0 文本 LLM、C1 文本 LALM、C2 语音 LALM、C3 语音加 CoT、C4 Transcript-RAG（多 e5 取证据）、C5 检索加 CoT 六条件，另测 CLAP 音频查询 RAG，覆盖 Qwen-Audio-Chat、Qwen2-Audio、Audio-Flamingo-3、AF-next-think、Phi-4-multimodal 及其纯文本基座。
核心创新：(1) 将"文本-语音落差"分解为多模态适配造成的文本退化与语音接口造成的推理退化两个分量，定位瓶颈位置；(2) 提出并量化声明-证据混淆失败模式，指出检索收益受限的根因不是召回质量而是核查对象错位；(3) 分离推理时 CoT 提示与思考微调两种推理路径，证明推理只在证据在手时才有价值。
评测协议：报告每类及平均准确率，相对文本基座的落差 Delta 越低越好，相对语音基线的提升 Lift 越高越好；CoT 输出缺少可解析答案字段记为错误。

### 📊 实验结果
数据集：VeriSpeak（HF 公开）。主要指标为准确率。能力不传递明显：Qwen2-Audio 语音仅 49.2% 而基座文本 76.4%，AF-3 语音 58.5% 文本 65.0%；落差主要来自语音接口而非适配。检索增益有限：Transcript-RAG 平均 Lift 仅 2.3，AudioQuery-RAG 平均 -0.3（CLAP Recall@1 约 0.3%）；混淆诊断显示仅 31% 例子正确定位原声明、65% 把检索段当声明。CoT 单独有害（Phi-4 跌至 16.7% 因格式不可解析），RAG 加 CoT 平均提升 4.9。AF-next-think 用 RAG 与 CoT 达 86.1%，虽超文本基座 14.3 点，仍距文本 RAG 上限 92.4% 差 6.3 点。语音识别误差整体可控，WER 0.13 到 0.23，AF-3 约 74% 错误集中在专名。开源：数据集与提示词均已公开。

### ⭐ 评分 : 7/10
理由：首次把语音事实核查做成可控探针，模态差分解与声明-证据混淆诊断具有可复用的分析价值，实验覆盖多模型多检索器且结论明确。扣分在于数据完全依赖单说话人 TTS 合成，缺乏真实噪声、口音与多轮语境，三类事实偏名人传记域窄，仅二分类且无开放检索库评估，结论向真人语音场景外推需谨慎。
## [13] Spooftral: Can Voxtral Audio-Language Model Detect Speech Spoofing?

arXiv ID：2609.28713
方向：语音大模型
作者：Avishai Weizman、Yehuda Ben-Shimol、Itshak Lapidot
机构：内盖夫本-古里安大学电气与计算机工程学院（以色列）、Afeka工程学院电气工程系（以色列）、阿维尼翁大学LIA实验室（法国）
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.28713 ｜ PDF：https://arxiv.org/pdf/2609.28713 ｜ 代码：https://github.com/avishai111/Spooftral ｜ Demo：暂无

### 📌 简介
本文以Voxtral-mini-3B音频语言模型（ALM）为对象，系统评估其微调后用于语音反欺诈（spoofing detection）的能力，是将反攻击/反欺骗（CM）能力并入统一ALM框架的第一步。研究发现：冻结的LLM层偏重语义表征，会削弱可分的反欺诈声学线索，其表征 separability 不及前置的Whisper音频编码器；而经指令引导的生成式标签似然判决与DoRA轻量微调构成的Spooftral，在ASVspoof5评测集取得4.25% EER，在不到1.2%可训练参数条件下展现了ALM兼顾语音理解与反欺诈的可行性。

### 🔧 技术方案
问题背景：基于SSL（WavLM、HuBERT等）的CM近年性能强劲，但面对未见攻击与失配条件泛化退化明显；ASVspoof5还存在bonafide语音分布漂移的新挑战。ALM拥有多模态大规模预训练与统一框架潜力，但其是否适合反欺诈这类细粒度声学辨别任务此前未被验证。

方法：将spoofing detection重构为指令引导的生成式标签似然分类。给定固定prompt与两个标签token序列（bonafide、spoof），从模型原始logits计算长度归一化对数似然，以两者差值作为检测分数，推理时不采样、不做温度缩放，保证判决可控可复现；训练用类加权交叉熵。同时用冻结表征的线性探测与PaCMAP可视化，剖析反欺诈线索在音频适配器与LLM解码器各阶段的分布与衰减。

核心创新：（1）首批在ASVspoof系列上系统评测Voxtral内Whisper编码器及其LLM前后的表征，以实证说明spoofing detection必须做任务特定适配，冻结LLM层反而稀释声学线索；（2）提出生成式标签似然框架，有意采用有语义的标签词而非0/1符号，便于复用预训练语义先验，并兼容问答等自由生成任务共存于同一模型；（3）引入基于两假设似然差的margin正则项，拉开bonafide与spoof的间隔，在ASVspoof5上稳定带来约0.2个百分点的EER改善。

训练策略：以DoRA（在LoRA基础上对权重做幅值与方向分解）仅适配注意力Q/K/V/O投影层，ASVspoof5采用rank 32、α=64；音频适配器全量可训练，LLM可选接入。数据增广含加性噪声与MP3/OPUS编解码扰动，每条语音最多并行3次增广以避免把bonafide伪造成类spoof特征。AdamW优化器、余弦调度、学习率1e-4、batch 32、梯度累积8、最多20 epoch，bfloat16精度；类权重按逆频率平方根归一（约1.5/0.5）。全量Spooftral与仅编码器变体Spooftral-Enc分别对应生成式似然与交叉熵目标。

### 📊 实验结果
数据集：ASVspoof2019 LA、ASVspoof2021 LA/DF、ASVspoof5；主指标EER，附1000次bootstrap置信区间。结论一：冻结线性探测中音频适配器Eval EER（ASVspoof5为9.75%）显著优于LLM输出（19.09%）。结论二：微调后Spooftral各集Eval EER为2019 LA 0.41%、2021 LA 6.46%、2021 DF 3.88%、ASVspoof5 4.25%；对比SSL基线，优于WavLM融合系统7.01%、SSL-IVSPT 5.99%、SLIM 5.50%，但逊于ASVspoof5最佳公开条件参赛系统2.59%（后者使用融合与额外训练数据）。指令界面消融显示bonafide/spoof优于real/fake。开源：代码已公开于GitHub。

### ⭐ 评分：6/10
理由：选题切中ALM统一框架与反欺诈交叉的空白，"LLM层稀释spoof声学线索"是有参考价值的实证发现；4.25% EER仅需1.17%可训练参数，轻量高效有说服力。扣分在于方法论以评估与成熟适配技术（DoRA）组合为主、原创性有限，未达SOTA，且仅验证单一3B模型，指令-似然接口的机理讨论尚浅。
## [14] Voice Agents under Acoustic Stress: From Signal Degradation to Interaction and Action

arXiv ID：2609.29452
方向：语音大模型
作者：Amir Ivry、Kai-Wei Chang、Lin Zhang、Sharon Gannot、Carlos Busso
机构：Technion（以色列理工学院）、MIT、独立研究者、Bar-Ilan 大学、Carnegie Mellon 大学
发布日期：2026-09-25
论文/PDF/代码/Demo：论文与 PDF 见 arXiv 2609.29452v1；样例音频与代码见 https://amir-ivry.github.io/trace/

### 📌 简介

本篇是关于任务型语音智能体声学鲁棒性评测的综述兼方法学短文。作者主张：噪声、混响与竞争说话人对智能体的影响不应只用 ASR 错误率衡量，而要沿"信号退化→对话交互→行动后果"三层压力链条追踪到底。论文给出 TRACE 评测工作流：同一智能体分别在原始录音与声学退化副本上执行同一任务，对两段对话按任务完成、错误动作、恢复行为与用户负担打分，并据此指导智能体改进，防止错误动作、提升纠错恢复能力。

### 🔧 技术方案

问题背景：语音智能体会直接代用户执行动作（如下单、改地址）。文中用典型例子说明压力传导：用户说"寄到十五 Oak 街"，噪声吞掉数字后智能体听成"五十 Oak 街"，若立即下单即铸成不可逆错误；若先追问用户则能纠错，但增加了用户负担。可见鲁棒性取决于智能体对退化语音的响应策略，传统信号级指标无法刻画这一后果。

基准梳理：作者综述 2026 年一批相关工作。VoiceBench 考察口语请求与听觉条件对回答质量的影响；tau-Voice 与 EVA-Bench 在模拟交互中追踪任务完成与会话行为；Pardon? 发现模型能答对问题却不会在关键信息缺失时主动追问；LALM-as-a-Judge 表明用自动评判检测有害语音内容高度依赖评判模型及其输入模态。这些基准各有任务、条件与评分规则，实践者难以把它们合并成针对自己应用的可复现测试。

核心创新：
（1）TRACE 工作流：将评测的设计、运行、解读整合为一套可操作的流程，明确对智能体行为的预期与判定标准；
（2）配对扰动评测：控制变量式对比，同一智能体、同一任务，只在"原始录音"与"声学应力副本"之间切换，以差分量化声学压力的端到端影响；
（3）四维结局打分：任务完成、错误动作、恢复行为、用户努力，把"何时该追问、何时可直接执行"的交互策略显式纳入评分。

评测协议：构造带应力副本的任务型对话集，运行同一智能体两次得到可对比的对话记录，按上述四维打分并解读差异；评测结果进一步用于指导智能体侧修改（如调整追问阈值、加入确认环节），目标是既阻断错误行动又控制纠错成本。

### 📊 实验结果

本文为方法学综述，未发布大规模新数据集或跨模型量化排行榜；主要贡献是评测协议与配套的样例音频、代码页面（amir-ivry.github.io/trace），可视为部分开源。评估指标即 TRACE 四维度：任务正确完成率、错误动作率、恢复成功率与用户交互负担。引用的 VoiceBench、tau-Voice、EVA-Bench、Pardon? 等构成其实验设计的证据基础，说明"答得对不等于知道何时需要更多信息"是当前 LALM 语音智能体的普遍短板。

### ⭐ 评分：6/10

理由：选题切中要害，把语音智能体评测从信号层推进到行动后果层，配对扰动设计简单有效、可操作性强，对做车载/客服等落地语音 Agent 的团队有直接参考价值；作者阵容（Gannot、Busso 等）可信。但作为短文其创新性偏流程整合而非新方法，缺乏跨模型的实证数值与公开基准数据集，TRACE 的打分细则与统计效度也未展开，故中等偏上。

---

## 语音前端

## [15] Exploring a Single Autoregressive LLM for Unified Target Speech Extraction across Synchronous and Asynchronous Inference

arXiv ID：2609.29238
方向：语音前端
作者：Wenxuan Wu、Shuhan Zhang、Shuai Wang、Haizhou Li
机构：论文未标注单位；资深作者 Haizhou Li 属新加坡国立大学（NUS）
发布日期：2026-09-25
论文：https://arxiv.org/abs/2609.29238 ｜ PDF：https://arxiv.org/pdf/2609.29238 ｜ 代码：暂无（无 repo 与权重） ｜ Demo：https://alexwxwu.github.io/tseomni-main/

### 📌 简介
本文提出 TSE-Omni，用单一自回归 LLM 主干统一目标语音提取的两类线索：时间同步线索（唇动、协同手势）与时间异步线索（注册语音、文本）。传统范式按线索单独训练部署提取器，视觉体系还需损坏匹配训练才鲁棒。TSE-Omni 利用 next-token prediction 的天然属性：每一步都以自身已预测的目标语音语义 token 为条件，形成连续刷新的"自注册"上下文，初值来自异步音频或文本线索、或前 2 秒视觉片段。视觉完好时融合同步视觉 token，视觉清零或缺失时改用 token 历史跟踪目标，实现跨模态补偿并支持流式推理。

### 🔧 技术方案
问题背景：音频线索提取器（SpEx、USEF、SoloSpeech）与视觉线索提取器（TDSE、USEV、AV-Mamba）独立训练部署，参数不共享、推理无法互补；已有 AR-LLM 方案仅接单一音频线索，解缠不彻底易生内容与声学幻觉，视觉帧损坏时无退路。
模型架构：AR 阶段：混合语音 mel 经 6 层 Conformer 得混合嵌入 m，线索编码器按模态产出统一 128 维嵌入 c，以 25Hz 语义 token（预测 32 层 RVQ 前 2 层）自回归解码；视觉线索时上一步语音 token 与同步视觉 token 拼接送残差模块，其加权和作下一步条件。NAR 阶段用 6 层 Conformer 预测其余声学 token 并由 codec 还原波形。线索编码器族含音频（共享混合编码器）、唇动（LRS3 预训练 ResNet VSR）、手势（BLSTM 15Hz 插值至 25Hz）、文本（RoBERTa），多线索拼接、缺失置零。
核心创新：（1）单一 AR-LLM 同吃同步与异步线索，把线索职责拆为识别与跟踪：异步线索仅做冷启动识别，跟踪完全依赖语音 token 历史。（2）自注册补偿：把 AR 累积的语音语义 token 当零成本持续刷新的注册线索，视觉断供时仅靠残差语音通路维持提取，无需损坏匹配训练与恢复模块。（3）残差式音视频 token 融合与 25Hz 低帧率语义空间，缓解语音为主骨干的模态失衡并使语音与视觉语义帧级对齐，天然支持流式推理。
训练策略：Omni 训练前先用 MSE 对齐音频与视觉线索编码器，跳过则视觉线索性能明显下降；每批次各半音频与唇动线索，文本与手势随后单独训练；损失为语义 token 交叉熵加目标语音全嵌入 MSE 以训练 NAR，默认不用视觉头损失；学习率 1e-3，验证损失 3 轮不降折半、6 轮不降早停。

### 📊 实验结果
数据集：自建 VoxCeleb2 双人混合核心集 40 万/2000/2000 句约 400h，SIR 取自 -5 至 5dB，片段 3 至 6s；零样本迁移 LRS3 与 Libri2mix；另建视觉损坏测试集（全缺失、部分遮挡、低分辨率）、LRS3 说话人切换微调集、VoxCeleb2 三说话人零样本集、IEMOCAP 稀疏重叠集与 YGD 手势集。
主要指标：SpeechBERTScore、WavLM 说话人相似度、NISQA、DNSMOS 三项、RTF。VoxCeleb2 上 TSE-Omni 视觉线索 SBS 0.81 与最优视觉基线持平，NISQA 3.24 明显高于基线 2.55/2.08/2.50；LRS3 零样本 SBS 0.89 追平 AV-Mamba，NISQA 3.84 为全场最高；Libri2mix 零样本 SBS 0.83 低于域内 LauraTSE 0.90，从 LauraTSE 初始化后微调可达 0.88。2 秒后视觉帧全清零时 SBS 仍为 0.81、SIM 0.95，而 USEV 与 AV-Sepformer 跌至 0.71/0.70 且 NISQA 崩坏；稀疏重叠、三说话人干扰、视觉引导说话人切换、流式推理均可用。
是否开源：仅项目主页与音频演示，代码、权重与混合数据均未开源，复现门槛高。

### ⭐ 评分：7/10
理由：把 AR 解码累积的 token 历史改造成免费且持续刷新的注册线索，以 77M AR-LLM 统一同步与异步线索，并在无损坏匹配训练下让 SBS 在视觉完全断供时保持 0.81，该结论有对照与消融支撑，感知质量提升显著，25Hz 对齐与流式能力具备落地价值。扣分在于全部结果来自仿真混合、缺少真实录制与主观听感评价；工作在语义 token 层，声学细节还原与强干扰抑制存在上限；Libri2mix 零样本与域内 SOTA 差距明显，需要借用 LauraTSE 初始化才能补齐；说话人切换与稀疏重叠仍需微调；代码权重未发布，第三方验证受阻。整体属于统一架构加免损坏训练补偿的扎实增量工作。

---

## 其余论文（仅列标题、arXiv ID、评分与链接）

### [16] Transcript-Supervised Post-Training of Generative Speech Enhancement on Real Recordings via Reinforce Adjoint Matching
- **arXiv ID**：2609.29405 | **方向**：语音前端 | **评分**：6/10（未精读，按标题与主题评分）
- Richter/Le Roux 组：转录监督在真实录音上后训练生成式增强，免配对精炼流模型
- **论文**：https://arxiv.org/abs/2609.29405 | **PDF**：https://arxiv.org/pdf/2609.29405.pdf | **代码**：暂无 | **Demo**：暂无

### [17] The Vulnerability of Neural Audio Watermarks under Speech Enhancement
- **arXiv ID**：2609.29040 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 系统评估语音增强对神经音频水印的破坏，揭示水印-增强安全权衡盲区
- **论文**：https://arxiv.org/abs/2609.29040 | **PDF**：https://arxiv.org/pdf/2609.29040.pdf | **代码**：暂无 | **Demo**：暂无

### [18] No Time to Collapse: Unlocking Robustness and Multiplexed Capacity in Frozen Audio Watermarkers
- **arXiv ID**：2609.29737 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 冻结水印器上的时间特征崩塌防御与多路复用容量
- **论文**：https://arxiv.org/abs/2609.29737 | **PDF**：https://arxiv.org/pdf/2609.29737.pdf | **代码**：暂无 | **Demo**：暂无

### [19] Configurable-Bandwidth Time-Frequency Modeling for Efficient Full-Band Speech Enhancement Across Sampling Rates
- **arXiv ID**：2609.29463 | **方向**：语音前端 | **评分**：6/10（未精读，按标题与主题评分）
- 可配置带宽时频建模，单模型跨采样率全带语音增强
- **论文**：https://arxiv.org/abs/2609.29463 | **PDF**：https://arxiv.org/pdf/2609.29463.pdf | **代码**：暂无 | **Demo**：暂无

### [20] Beyond Model Size: Redesigning LiSenNet for Embedded Speech Enhancement
- **arXiv ID**：2609.29866 | **方向**：语音前端 | **评分**：6/10（未精读，按标题与主题评分）
- 嵌入式语音增强 LiSenNet 的架构重构（Microsoft）
- **论文**：https://arxiv.org/abs/2609.29866 | **PDF**：https://arxiv.org/pdf/2609.29866.pdf | **代码**：暂无 | **Demo**：暂无

### [21] Does Per-Frame Early Exit Pay? A Compute-Matched Study of Dynamic Depth for On-Device Speech Enhancement
- **arXiv ID**：2609.29867 | **方向**：语音前端 | **评分**：6/10（未精读，按标题与主题评分）
- 算力对齐对照：逐帧动态深度早退在端侧增强是否值得
- **论文**：https://arxiv.org/abs/2609.29867 | **PDF**：https://arxiv.org/pdf/2609.29867.pdf | **代码**：暂无 | **Demo**：暂无

### [22] Is Broader Better? A Controlled Study of Multilingual Coverage and Pretraining Objective in Frozen SSL Encoders for Speech Deepfake Detection
- **arXiv ID**：2609.29138 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 冻结 SSL 编码器多语覆盖与预训练目标对深伪检测的受控因果分析
- **论文**：https://arxiv.org/abs/2609.29138 | **PDF**：https://arxiv.org/pdf/2609.29138.pdf | **代码**：暂无 | **Demo**：暂无

### [23] Joint Analysis of Latent Dimensionality and Frame Rate in Continuous Audio Encoders
- **arXiv ID**：2609.29780 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 连续音频编码器潜维与帧率联合分析，指导 ALM 前端容量分配
- **论文**：https://arxiv.org/abs/2609.29780 | **PDF**：https://arxiv.org/pdf/2609.29780.pdf | **代码**：暂无 | **Demo**：暂无

### [24] Same Bit Width, Different Outcomes: Post-Training Quantization of Text-to-Speech Across Architectures
- **arXiv ID**：2609.28974 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 跨架构 TTS 训练后量化系统评测：同位宽不同结局
- **论文**：https://arxiv.org/abs/2609.28974 | **PDF**：https://arxiv.org/pdf/2609.28974.pdf | **代码**：暂无 | **Demo**：暂无

### [25] Temporal Taxation Compounds Under Post-Training Compression of Whisper Models
- **arXiv ID**：2609.28739 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- PTQ 压缩下 Whisper 时序失真复合脆弱性研究
- **论文**：https://arxiv.org/abs/2609.28739 | **PDF**：https://arxiv.org/pdf/2609.28739.pdf | **代码**：暂无 | **Demo**：暂无

### [26] Learning New Words from Unlabeled Test Data in Automatic Speech Recognition
- **arXiv ID**：2609.28877 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- ASR 测试时从无标注数据学习新词
- **论文**：https://arxiv.org/abs/2609.28877 | **PDF**：https://arxiv.org/pdf/2609.28877.pdf | **代码**：暂无 | **Demo**：暂无

### [27] Accent Analogy Guidance: More Speaker Similarity at Equal Accent in Cross-Lingual Voice Cloning
- **arXiv ID**：2609.29123 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 跨语言克隆中口音类比引导，同口音下提高音色相似度
- **论文**：https://arxiv.org/abs/2609.29123 | **PDF**：https://arxiv.org/pdf/2609.29123.pdf | **代码**：暂无 | **Demo**：暂无

### [28] Towards Clinical Adoption of Voice and Speech as Measures of Health: The Need for Harmonization
- **arXiv ID**：2609.28894 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 立场论文：语音健康度量临床采纳亟需数据与方法标准化
- **论文**：https://arxiv.org/abs/2609.28894 | **PDF**：https://arxiv.org/pdf/2609.28894.pdf | **代码**：暂无 | **Demo**：暂无

### [29] COSED: Setting the Bar for Open-Vocabulary Sound Event Detection
- **arXiv ID**：2609.30083 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 开放词汇声学事件检测基准与强基线
- **论文**：https://arxiv.org/abs/2609.30083 | **PDF**：https://arxiv.org/pdf/2609.30083.pdf | **代码**：暂无 | **Demo**：暂无

### [30] VietPrism: A Large-Scale Vietnamese Speech and Deepfake Corpus with Diverse Dialects and Code-Switching
- **arXiv ID**：2609.30005 | **方向**：语音大模型 | **评分**：6/10（未精读，按标题与主题评分）
- 越南语方言+语码转换大规模语音与深伪语料
- **论文**：https://arxiv.org/abs/2609.30005 | **PDF**：https://arxiv.org/pdf/2609.30005.pdf | **代码**：暂无 | **Demo**：暂无

### [31] Broadening Uncertainty Estimation for Audio Question Answering Across Methods, Formats, and Inputs
- **arXiv ID**：2609.28879 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- 音频问答不确定性估计跨方法/格式/输入横向评测
- **论文**：https://arxiv.org/abs/2609.28879 | **PDF**：https://arxiv.org/pdf/2609.28879.pdf | **代码**：暂无 | **Demo**：暂无

### [32] Personalized Korean Lipreading as Visual Speech Recognition: Transfer, Census and Adaptation on OLKAVS
- **arXiv ID**：2609.28988 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- OLKAVS 韩语唇读数据集与 VSR 个性化适配
- **论文**：https://arxiv.org/abs/2609.28988 | **PDF**：https://arxiv.org/pdf/2609.28988.pdf | **代码**：暂无 | **Demo**：暂无

### [33] Few-Shot Calibration for Sim-to-Real Single-Channel Speaker Distance Estimation
- **arXiv ID**：2609.29203 | **方向**：语音前端 | **评分**：5/10（未精读，按标题与主题评分）
- 单通道说话人距离估计 sim-to-real 少样本校准
- **论文**：https://arxiv.org/abs/2609.29203 | **PDF**：https://arxiv.org/pdf/2609.29203.pdf | **代码**：暂无 | **Demo**：暂无

### [34] DAMSEP: Distance-Aware Monaural Source Separation Using Multi-RIR Estimation
- **arXiv ID**：2609.29749 | **方向**：语音前端 | **评分**：5/10（未精读，按标题与主题评分）
- 多 RIR 估计实现距离感知单声道源分离
- **论文**：https://arxiv.org/abs/2609.29749 | **PDF**：https://arxiv.org/pdf/2609.29749.pdf | **代码**：暂无 | **Demo**：暂无

### [35] ASR Ensembling for Phoneme Intelligibility Evaluation of Speech Anonymizers
- **arXiv ID**：2609.28577 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- ASR 集成评估语音匿名化器音素可懂度
- **论文**：https://arxiv.org/abs/2609.28577 | **PDF**：https://arxiv.org/pdf/2609.28577.pdf | **代码**：暂无 | **Demo**：暂无

### [36] Speech Block Influence: Component-Specific Layer Scoring for Pruning Speech LLMs
- **arXiv ID**：2609.29343 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- 组件级层打分的语音 LLM 剪枝
- **论文**：https://arxiv.org/abs/2609.29343 | **PDF**：https://arxiv.org/pdf/2609.29343.pdf | **代码**：暂无 | **Demo**：暂无

### [37] WST-Graph: Topology-Preserving Wavelet Scattering Front-End for Speech Deepfake Detection
- **arXiv ID**：2609.29372 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- 拓扑保持小波散射前端用于深伪检测
- **论文**：https://arxiv.org/abs/2609.29372 | **PDF**：https://arxiv.org/pdf/2609.29372.pdf | **代码**：暂无 | **Demo**：暂无

### [38] BiMamba2 Masked Discrete-Unit Prediction for Multilingual Speech Representation (UIW Challenge)
- **arXiv ID**：2609.28758 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- 掩码离散单元预测多语表征，无监督 ASR 挑战赛方案
- **论文**：https://arxiv.org/abs/2609.28758 | **PDF**：https://arxiv.org/pdf/2609.28758.pdf | **代码**：暂无 | **Demo**：暂无

### [39] Exemplar-Free Analytic Learning for Multi-Label Audio Class-Incremental Learning
- **arXiv ID**：2609.29777 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- 免样本解析学习多标签音频类增量学习
- **论文**：https://arxiv.org/abs/2609.29777 | **PDF**：https://arxiv.org/pdf/2609.29777.pdf | **代码**：暂无 | **Demo**：暂无

### [40] A Native-Reference Phone-Class Geometry for Second-Language Pronunciation Analysis
- **arXiv ID**：2609.30075 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- 母语参照的音类几何空间度量二语发音偏误
- **论文**：https://arxiv.org/abs/2609.30075 | **PDF**：https://arxiv.org/pdf/2609.30075.pdf | **代码**：暂无 | **Demo**：暂无

### [41] A Training Criterion with Token-Level Tolerance to Transcription Ambiguity for ASR
- **arXiv ID**：2609.30160 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- 转写歧义 token 级容忍的 ASR 训练准则
- **论文**：https://arxiv.org/abs/2609.30160 | **PDF**：https://arxiv.org/pdf/2609.30160.pdf | **代码**：暂无 | **Demo**：暂无

### [42] Do Audio Language Models Hear and Read Distinctive Features Alike?
- **arXiv ID**：2609.30167 | **方向**：语音大模型 | **评分**：5/10（未精读，按标题与主题评分）
- 音频语言模型'听'与'读'音位特征一致性研究
- **论文**：https://arxiv.org/abs/2609.30167 | **PDF**：https://arxiv.org/pdf/2609.30167.pdf | **代码**：暂无 | **Demo**：暂无

### [43] Anatomy-Aware Cross-Speaker Adaptation of Complete Vocal-Tract Acoustic-to-Articulatory Inversion
- **arXiv ID**：2609.29766 | **方向**：语音大模型 | **评分**：4/10（未精读，按标题与主题评分）
- 解剖感知跨说话人全声道声学-构音反演适配
- **论文**：https://arxiv.org/abs/2609.29766 | **PDF**：https://arxiv.org/pdf/2609.29766.pdf | **代码**：暂无 | **Demo**：暂无

### [44] ARIS: Low-Resource Glass-Box Neural Source-Filter Synthesis for Phonetic Stimulus Manipulation
- **arXiv ID**：2609.29923 | **方向**：语音大模型 | **评分**：4/10（未精读，按标题与主题评分）
- 低资源玻璃盒源-滤波合成用于语音心理实验刺激操纵
- **论文**：https://arxiv.org/abs/2609.29923 | **PDF**：https://arxiv.org/pdf/2609.29923.pdf | **代码**：暂无 | **Demo**：暂无

---

*Generated on 2026-09-25*
