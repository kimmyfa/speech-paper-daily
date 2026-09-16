# 2026-09-15 语音论文速递

**共收录**: 35 篇 | **语音大模型**: 23 篇 | **语音前端**: 12 篇

> 目标日期 2026-09-15（北京时间）arXiv 语音相关论文共命中 35 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

### 📖 完整精读（按评分降序）

## [1] Realtime-Venus：A full-duplex interaction system with asynchronous delegation

**arXiv ID**：2609.13814 | **方向**：语音大模型（全双工语音交互系统）

**作者**：Ruixiang Zhao, Hualei Wang, Renhe Sun, Enzhi Zhou, Jincenzi Wu 等

**机构**：蚂蚁集团（Ant Group）、清华大学（Tsinghua University）

**发布日期**：2026-09-12 | **论文**：https://arxiv.org/abs/2609.13814 | **PDF**：https://arxiv.org/pdf/2609.13814v1 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有全双工语音模型（如 MiniCPM-o 4.5、Moshi）能连续感知与流式输出，但背景推理与工具执行通常阻塞交互或依赖外部 ASR/TTS 拼装。本文提出 Realtime-Venus，一个将全双工交互与异步委派（asynchronous delegation）结合的主动式交互系统，含两个独立训练的 9B 前端模型 Realtime-Venus-Omni（音视频）与 Realtime-Venus-Audio（纯语音），并配共享执行框架 Realtime-Venus-Harness。在 8 个视频基准上 Omni 于在线模型中 6 项领先，StreamingBench 达 70.2%、OVO-Bench 64.7%、Daily-Omni 81.3%；Audio 在 MMAU（78.0%）、MMAU-Pro（63.2%）等 4 项音频基准领先，并在 Full-Duplex-Bench v1.5 上以 97%/88%/86% 的延续率全面超过 Gemini 3.1 Live 与 GPT-4o。

### 🔧 技术方案

**问题背景：** 连续交互与外部计算处于不同时间尺度，后台任务需要请求时刻的证据快照，但其结果必须在已演进的对话中重新解读。现有系统要么无法在播放中感知变化，要么将工具有效性限制在暂停式回合，任务捕获与结果回投缺乏统一时序。

**模型架构：** 基于开源 MiniCPM-o 4.5 的 Omni-Flow 架构：SigLIP2 视觉编码器与 Whisper-Medium 音频编码器接入 Qwen3-8B 语言骨干（仅更新 Thinker，声学解码器冻结），LLM 隐藏状态经流式 flow-matching 解码器以约 25 token/秒的 S3 语音 token 生成 24 kHz 波形。流按 1 秒 chunk 组织，每 chunk 预测 <|listen|>/<|speak|> 控制 token，以 <|chunk_eos|>、<|turn_eos|> 管理轮次；新增 <delegate>/</delegate> 私有委派跨度与 <backend>/</backend> 后台结果跨度。三股流（用户感知流、助手输出流、后台文本流）在同一因果时间轴序列化，前端在后端执行期间保持感知与播报。

**核心创新：** (1) 双环运行时与统一流抽象：延迟敏感的交互环持续执行，能力环通过证据边界固定的任务包异步调用注册能力，快照 X_i=Snap(B^σ;κ_i,Δ) 限定请求时刻可观测证据，结果经新鲜度检查与播放感知投递回原会话。(2) 训练免长视频记忆模块：基于 AdaCodec 的像素运动补偿预测代价做帧门控存档（含局部变化保护与最大连续丢弃约束），检索用 MaxSim 逐 query token 余弦匹配加 MAD 加权、MMR 融合相关性与新颖性，(60,90] 分钟子集上 LVOmniBench 提升 5.88 个百分点。(3) 耦合全双工与委派的统一数据管线：场景规划、副语言声学实现与时间对齐三步构造轨迹，区分反馈语（继续播报）、他人/背景语音（保持）与打断（stop/repair/redirect），duplex 目标与 delegation 目标共享事件时间线联合监督。

**训练策略：** 2.8M+ 样本、9 类数据构成统一后训练语料：视频组约占 70%（其中通用音视频理解 936k、视觉主动双工 454k、Omni 主动 201k、语音入流双工 315k、委派 95k）仅供 Omni 使用，音频组约占 30%（通用音频 470k、口语问答 205k、纯语音双工 100k、委派 90k）两模型共享；离线理解约 56%、主动双工约 37%、委派约 6%。损失仅监督响应跨度与每秒控制 token，按样本归一化，仅更新 Thinker。

### 📊 实验结果
**数据集**：StreamingBench、OVO-Bench、ProactiveVideoQA、OmniPro、WorldSense、Daily-Omni、OmniVideoBench、LVOmniBench、LongVideoBench、CGBench、MMAU、MMAU-Pro、MMAR、MMSU、VoiceBench AlpacaEval、Llama Questions、Speech TriviaQA、Speech CMMLU、Full-Duplex-Bench v1.5/v3、自建 Delegate Benchmark

**主要指标**：
- StreamingBench：70.2%（在线模型最高）
- OVO-Bench：64.7% | Daily-Omni：81.3% | OmniPro：29.0%
- MMAU：78.0% | MMAU-Pro：63.2% | Speech CMMLU：67.8% | Llama Questions：83.8% | AlpacaEval：4.81
- FDB v1.5：打断响应率 75%；反馈语/他人语音/背景语音延续率 97%/88%/86%，均超 Gemini 3.1 Live 与 GPT-4o
- FDB-v3 工具调用：工具选择 F1 86.0%（Omni）、85.0%（Audio），Pass@1 43.0%/48.0%
- 自建委派基准：Omni 总路由准确率 75.93%，Audio 68.89%

**是否开源**：未提供代码与模型权重；基座为开源 MiniCPM-o 4.5，论文以 CC BY-NC-SA 4.0 发布。

### ⭐ 评分：8/10
评分理由：创新性较强，首次将异步委派协议内嵌于原生全双流式策略，双环运行时、证据边界固定与播放感知投递的工程设计完整且可复现性高；训练免长视频记忆结合预测编码门控与 MMR 检索亦有实用价值。实验充分，覆盖理解、连续性、工具调用与委派决策四类评测且与主流闭源模型对比，但打断响应率落后 Joy-Duplex、GPT-4o、Gemini 3.1 Live，委派基准为自建且无消融实验拆分离各设计贡献，故未达顶会突破水准。

---

## [2] CVSS-X: A Multilingual Speech-to-Speech Translation Corpus for 28 Languages

**arXiv ID**：2609.13413 | **方向**：语音大模型（语音到语音翻译语料）

**作者**：Lucas Rafael Stefanel Gris, Alef Iury Siqueira Ferreira, Frederico Santos de Oliveira, Augusto Seben da Rosa 等

**机构**：巴西戈亚斯联邦大学（UFG）、马托格罗索联邦大学（UFMT）、圣保罗州立大学（UNESP）

**发布日期**：2026-09-11 | **论文**：https://arxiv.org/abs/2609.13413 | **PDF**：https://arxiv.org/pdf/2609.13413v1 | **代码**：https://github.com/ErmisAI/XVSS-X | **Demo**：暂无

### 📌 简介
CVSS 语料仅支持 21 种语言到英语的多对一语音翻译，缺乏从英语出发的一对多训练数据。本文提出 CVSS-X，反向扩展 CVSS，构建从英语到 28 种目标语言（覆盖 12 个语系）的大规模合成语音到语音翻译语料，含 CVSS-X-C（每语言两个固定嗓音）与 CVSS-X-T（跨语言音色克隆）两个变体。语料约 24 万句对/语言，总量超 16,000 小时，为 CVSS 的 8 倍；质量评测中 CVSS-X-C 平均 UTMOS 3.55、ASR-BLEU 82.4，CVSS-X-T 说话人相似度达 0.607，与 CVSS 翻译质量可比。

### 🔧 技术方案

**问题背景：** 真实并行的语音到语音翻译语料因跨语言对齐录制成本极高而稀缺；SpeechMatrix（41.8 万小时）为挖掘式对齐且仅覆盖 17 种欧洲语言，SeamlessAlign（37 语言）仅公开元数据需自行重建。现有最大规模开源语料 CVSS 仅支持 X→EN 单一方向，阻碍了从英语翻译及非英语语言对间的研究。

**模型架构：** 沿袭 CVSS 设计，CVSS-X-C 使用每语言一男一女两个 ElevenLabs 设计的规范中性嗓音（按源说话人性别元数据分配，男性 81.4%、女性 18.6%），CVSS-X-T 以源英语语音为参考进行 OmniVoice 零样本跨语言音色克隆；源语音为 Common Voice v17 英语录音。训练/验证/测试划分为 222,349/10,000/7,843 句。

**核心创新：** (1) 首次提供 EN→28 语言的一对多大规模 S2ST 语料，与 CVSS 互补，使借助英语为枢轴实现任意语言对及双向翻译成为可能，总配对句数达 6,725,376。(2) 提出可复现的全自动生成流水线：先用 NLLB-200-distilled-600M 做文本翻译（经 7 模型基准测试，LLM-as-judge 得 8.0/10、17ms/句，单 GPU 约 11 小时完成 28 语言），再用 OmniVoice 合成目标语音，保证句级完美对齐。(3) 通过与 CVSS 相同的归一化文本匹配，恢复 Common Voice v17 中与 v4 对齐的 240,192/264,037 句源音频（91.0%），实现与 CVSS 数据集级别的直接对称。

**训练策略：** 数据集构建类工作，文本翻译选用 NLLB-200-distilled-600M（对比 TranslateGemma 质量 9.0-9.3/10 但耗时 377-548ms/句需超 10 天）；质量评测从 dev 集每语言分层抽样 200 句（共 5,600×2），经功效分析确定（σ≈0.5 时 95% 置信区间 ±0.07），使用 Whisper large-v3 计算 WER/CER 与 ASR-BLEU，UTMOS 评测自然度、ECAPA-TDNN 评测说话人相似度。

### 📊 实验结果
**数据集**：CVSS-X-C/T、CVSS（重新评测对照）、Common Voice

**主要指标**：
- CVSS-X-C：UTMOS 3.55 | ASR-BLEU 82.4 | WER/CER 12.1%
- CVSS-X-T：UTMOS 3.21 | ASR-BLEU 79.4 | WER/CER 14.1% | 说话人相似度 0.607
- CVSS-C 对照：UTMOS 4.43 | ASR-BLEU 94.2 | WER 3.5%
- 最优语系组（罗曼语族）：WER 5.8%（C）/8.2%（T），ASR-BLEU 90.3/88.0
- 最难语系（印伊语族/其它）：ASR-BLEU 约 60-65，希伯来 BLEU 46.1、泰语 WER 77.0%

**是否开源**：代码开源（MIT 仓库），数据集托管于 HuggingFace（CC-BY-NC 4.0 协议，含 CVSS-X-C/T 完整音频）

### ⭐ 评分：8/10
评分理由：数据规模与语言覆盖度显著超越现有开源 S2ST 语料，首次打通与 CVSS 的反向对称，且提供两种变体覆盖嗓音多样性需求，实用价值高。评测方法论严谨，含功效分析抽样、重新评测 CVSS 对照及无分词语言特化评估。但语料为纯合成数据、未训练任何 S2ST 基线模型验证其有效性，且 CC-BY-NC 协议限制商业应用，创新点集中于语料构建而非方法层面。

---

## [3] StepAudio 3 Realtime Technical Report

**arXiv ID**：2609.14005 | **方向**：语音大模型（语音生成/实时语音模型）

**作者**：StepFun-Audio Team（Bin Lin, Bo Zhao, Boyang Zhang 等 90 余人）

**机构**：阶跃星辰（StepFun）

**发布日期**：2026-09-12 | **论文**：https://arxiv.org/abs/2609.14005 | **PDF**：https://arxiv.org/pdf/2609.14005v1 | **代码**：暂无 | **Demo**：https://stepaudiollm.github.io/step-audio-3-realtime/

### 📌 简介
实时语音交互需要在深度推理、快速应答与自然的轮换控制之间取得平衡。论文提出 StepAudio 3 Realtime，一个约 196B 总参数（11B 激活）的端到端语音-语言基础模型，围绕"监听-对话-思考-行动"连续循环组织 Deep Perception、Seamless Duplex、Think-While-Speaking 与流式 Voice Agent 四大能力。实验表明其在 StepAudioChat 推理模式下达 73.0 宏平均；借助 Think-While-Speaking 可实现与专用推理模型相近的对话推理质量同时实时说话，并在 MMSU 上取得 90.6、Artificial Analysis Full-Duplex Bench Overall 98.9、τ-Voice 宏任务成功率 56.0%，位居全线顶尖。

### 🔧 技术方案

**问题背景：** 全双工语音对话需在未说完的句内停顿与话轮结束之间、简短应和与实质打断之间做出区分，复杂请求还需在响应延迟与深思熟虑间权衡，工具调用又要求外部任务与对话并行推进。现有多数系统分别优化识别、理解或流式生成，缺乏对感知-推理-行动的统一协调。

**模型架构：** 采用 MoE 架构，总参数约 196B、每 token 激活 11B；语言主干为 Step 3.7 Flash，音频前端使用 Qwen3-Omni 的 Audio Transformer 编码器，经适配器接入 LLM 解码器。全双工输入包含用户音频与模型音频双音频流，语音生成器输出流式返回模型音频流。交互由 320ms 音频块与交互状态 token 在共享时间线上交错表示。

**核心创新：** (1) Seamless Duplex 会话管理：以时间交错的双音频流加对话历史为上下文，联合推断句内停顿、应和、实质打断与背景语音，仅在句义完整时启动应答，实现听、说、让的平衡。(2) Think-While-Speaking：同一模型并行调用两次构成 Formulation Brain（生成私有推理轨迹）与 Articulation Brain（基于当前推理产出短时语音片段），按播放进度调度发音，默认 Speak-First 无需等待推理前缀，推理完成后可追加补正。(3) Adaptive Thinking 与 MTP 加速：以盲审对比有/无思考轨迹决定每轮是否使用显式推理，思考率控制在 51.5%-82.0%；MTP3 三预测头配合 Medusa 熵自适应典型接受与 1.05 重复惩罚加速私有推理，墙钟加速最高 2.05 倍。

**训练策略：** 预训练分模态对齐、多模态混合、cooldown 三阶段，固定序列 32K、共处理 1.2T token；midtraining 扩展上下文至 128K，融合超 1 万小时合成全双工交互数据。ASR 分支用 SpecAugment 掩蔽、ROVER 多系统融合与长尾术语合成增强微调；音频理解 SFT 采用约 10 万条高质量样本（消融显示 200 万随机样本 MMSU 78.78 仅得 89.70 的近反）。

### 📊 实验结果
**数据集**：LibriSpeech、AISHELL-1、WenetSpeech、ContextASR-Bench、MMSU、MMAU、MMAR、AudioMultiChallenge、WildSpeech、Big Bench Audio、Step-Caption、MTalk-Bench、StepAudioChat、Full Duplex Bench、τ-Voice、HMMT、GPQA Diamond

**主要指标**：
- ASR Max：LibriSpeech test-clean WER 1.18｜test-other 2.28｜AISHELL-1 CER 0.49｜ContextASR-Bench 英/中宏平均误差 5.67%/1.23%（均第一）
- 音频理解宏平均：81.3（MMSU 90.6 领先 7.0 分，MMAR 86.5 领先 4.8 分）
- AA Full-Duplex Bench Overall：98.9（Turn Taking 100.0、User Interruption 99.0、Pause Handling 98.9）领先 Qwen Realtime Plus 98.4
- StepAudioChat 宏平均：推理模式 73.0｜实时模式 70.4
- τ-Voice 宏任务成功率：56.0（Telecom 70.2 最高，Retail 37.7 明显短板）

**是否开源**：未开源，仅提供项目主页。

### ⭐ 评分：8/10
评分理由：以统一循环框架同时整合感知、全双工轮换管理、并行推理与工具代理，Think-While-Speaking 的"边想边说"机制与 MTP 加速组合在工程上具有明显实用价值，并在全双工与 ASR 多个权威榜上取得最优或并列最优。实验覆盖面广且含 "less is more" 数据消融与模型合并分析，诚实披露了多轮约束跟随、零售工具任务等短板。不足在于作为技术报告缺乏可复现细节与开源，推理模式对话能力仍落后于顶尖文本推理模型。

---

## [4] Inherited Heads: Audio language models track speakers with their text backbone's attention, and an attention-mass ranking retrieves a different set

**arXiv ID**：2609.14174 | **方向**：语音大模型（音频语言模型可解释性/说话人追踪）

**作者**：Bojro Das

**机构**：Cornell University

**发布日期**：2026-09-12 | **论文**：https://arxiv.org/abs/2609.14174 | **PDF**：https://arxiv.org/pdf/2609.14174 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对音频语言模型（ALM）在说话人归属上表现差的问题（让模型描述六个轮流说话者之一的内容，仅6%–16%试次答对，低于随机猜测的16.7%），本文提出：向约100个注意力头（不足模型头数十分之一）的注意力logits加恒定偏置，无需任何训练即可把输出导向指定说话者，成功率90.7%–99.0%。进一步发现这些头大部分继承自文本骨干：仅按纯文本模型选出前100头号并原样迁移，即可在80.8%–95.0%试次上完成定向（随机控制仅12.5%–45.0%）。同时发现注意力质量排序（mass ranking）与逐头归一化后的选择性排序（selectivity ranking）在前100头上仅共享4–69个。

### 🔧 技术方案

**问题背景：** 现有多模态模型通过注意力质量（mass）排序挑选"注视头"（Gaze Heads）来定位查询区域，但未区分"头部本来就关注该区域"与"注意力随问题变化"。ALM 的说话人追踪机制来源不明，且现成方法在部分模型上失效。本文用因果干预（steering）在音频模态中检验两种排序，首次对照文本骨干做头级比较。

**模型架构：** 三个模型跨度从文本骨干"几乎不改"到"大幅改造"：Qwen2-Audio-7B（语言模型与音频编码器联合训练，32层×32头=1024头）；Ultravox-v0.6-8B（冻结Llama-3.1-8B骨干，1024头）；SALMONN-13B（冻结Vicuna-13B+LoRA+Q-Former，40×40=1600头）。干预方法为：对所选头在目标段token跨度内所有key的softmax前logits加+B、其余五段加−B；B=10^4用于与已发表工作可比，B=5时效果已饱和。数据为500条33.5秒音频条（6段×5秒LibriSpeech）。

**核心创新：** (1) 继承性证据：仅在纯文本骨干上排序取前100头，直接迁移即能在95.0%/85.0%/80.8%试次定向，音视频头集合共享66/71/74个（随机重叠约20），但共享性即因果在三个模型上均无法区分。(2) 双排序对比：mass与selectivity仅弱相关（Spearman ρ=0.168/0.258/0.025），在Ultravox上mass排序的头集中于浅层，两个集合失败方式不同。(3) 方法学自检：偏置在饱和强度下目标段新增注意力仅0.173来自其他段，0.416来自提示、0.412来自attention sink；layer-matched随机控制5次抽样跨度达0.642，主张控制应作为分布而非单点报告。

**训练策略：** 全程无需训练、无标注、无梯度；每头读取最终提示token对各段的注意力，每次任务仅需少量前向传播。模型以4-bit NF4+bf16计算加载，作者明确承认4-bit量化威胁头排序保真度。

### 📊 实验结果
**数据集**：LibriSpeech（500条6说话人拼接音条）、openai-comic-strips（视觉布局控制臂）

**主要指标**：
- 无干预说话人归属正确率：6%–16%（低于1/6随机）
- 零训练注意力偏置定向成功率（3模型）：90.7%–99.0%
- 文本骨干头迁移定向成功率 vs 随机控制：95.0% vs 12.5%（Qwen2-Audio）| 85.0% vs 45.0%（Ultravox）| 80.8% vs 15.0%（SALMONN）
- 音/文本发现集合共享量 vs 随机期望：66/71/74 vs 约20
- mass排序 vs selectivity排序定向（Ultravox）：0.017 vs 0.990；不可归因率69.7% vs 1.0%

**是否开源**：论文未提供代码或模型链接，使用预注册并由"结果台账"自动生成图表。

### ⭐ 评分：8/10
评分理由：首次以因果干预证明ALM说话人追踪机制继承自文本骨干，并严格区分共享性是否因果（坦诚报告"无法区分"），方法学贡献突出——对random-control分布稳定性的测量具普遍价值。实验覆盖3个音频模型+2个视觉模型族。扣分点：样本规模小、4-bit量化威胁、且作者自认不提出更优打分工具，实用价值偏解释性。

---

## [5] Grounded in Sound: Reinforcement Learning with a Frozen Acoustic Judge to Curb ASR Insertion Hallucinations

**arXiv ID**：2609.14455 | **方向**：语音大模型（ASR幻觉抑制/强化学习）

**作者**：Tingzhen Xiong, Rilin Chen, Weiwei Li, Wentao Zhang, Qicong Xie

**机构**：腾讯（Tencent），深圳，中国

**发布日期**：2026-09-13 | **论文**：https://arxiv.org/abs/2609.14455 | **PDF**：https://arxiv.org/pdf/2609.14455v1 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对ASR的RL后训练中奖励几乎全部位于文本空间、模型可借助LLM强语言先验在弱声学证据下"猜测"而非"听"，导致插入型幻觉激增（插入率由干净语音0.37%单调升至AMI-SDM 5.75%）的问题，本文提出声学保真度奖励：将GRPO奖励与一个独立预训练且永久冻结的字符级wav2vec2-CTC声学裁判（约0.3B）结合，裁判仅训练时提供奖励、推理时移除。以Qwen2-Audio-7B（LoRA）为策略，插入错误在AMI-IHM/SDM上分别降低28.3%、22.3%，同时AMI-SDM WER从35.89%显著降至34.71%。

### 🔧 技术方案

**问题背景：** 现行语音LLM的后训练RL（GRPO等多采用-WER或文本规则奖励）只比较假设与参考文本，从不核对转录是否被音频支撑。干净语音下依赖先验解析成本极低，于是-WER奖励默许该捷径；一旦声学退化，模型持续凭先验补全，产生流畅但无依据的词语。

**模型架构：** 系统含两个模型：策略为Qwen2-Audio-7B（LoRA rank16/α32）；裁判为永久冻结的字符级wav2vec2-large-960h CTC（0.3B，32符号字符词表）。训练时策略为每条音频采样G=8个候选，裁判与-WER文本评分器共同打分，组内稳健Z归一化后经GRPO更新LoRA；推理时裁判彻底移除，策略单次贪心解码。

**核心创新：** (1) 声学保真度奖励：总奖励R_i=Z_grp(-min(WER,2.0))+μ·Z_grp(S_ctc(y,X))，S_ctc为冻结裁判对候选字符序列的CTC对齐损失并按目标长度归一化；μ=0即还原纯WER-GRPO基线，全部实验无KL惩罚（β=0）。(2) 裁判门控（judge gate）：训练前以成对排序准确率筛选裁判有效区，clean/10dB/5dB全部通过，而AMI仅0.843/0.775被否决，故远近场条件被排除出训练混合。(3) 推理无裁判约束：将抑制能力内化为策略权重，单模型贪心解码即可获得增益，并对比证明推理期CTC重打分在该配置下反而增加插入。

**训练策略：** GRPO组大小G=8，学习率1×10⁻⁶，有效批大小32，1000步余弦调度（warmup 30），三随机种子，8×H20。训练数据为LibriSpeech train-clean-100（28,539句）四桶各25%：clean、噪声10dB、7.5dB、5dB。

### 📊 实验结果
**数据集**：LibriSpeech test（四档渲染）与AMI-IHM（近讲）、AMI-SDM（远场），合计33,282条样本

**主要指标**：
- 插入相对降低：AMI-IHM 28.3%（1598→1145）；AMI-SDM 22.3%（4502→3498）
- 净WER：AMI-SDM 35.89%→34.71%（显著）；AMI-IHM 16.70%→16.28%（n.s.）
- 三种子复现：插入降低+28.6±0.7%（IHM）、+24.3±4.9%（SDM）
- 不可懂音频：输出长度塌缩85-90%，特异度0.85-0.90
- CTC重打分：插入率反升（1.78%/7.64%）；μ=0.6贪心达1.50%/5.39%

**是否开源**：未提供代码或模型权重

### ⭐ 评分：8/10
评分理由：思路新颖且直击痛点——首次在ASR GRPO中引入独立冻结声学裁判的音频一致性奖励，训练时施教、推理零开销，机制设计严谨（裁判门控、反事实探针、聚类bootstrap、三种子）。虽非顶会级大尺度突破，但实验充分、因果论证规范；局限为单策略单裁判单OOD语料、μ>0.6未测、无KL对照，作者对局限性有坦诚披露。

---

## [6] Reducing the Output-Mode Gap in Speech Language Models via Joint-Output On-Policy Distillation

**arXiv ID**：2609.15313 | **方向**：语音大模型（语音语言模型/蒸馏）

**作者**：Daxin Tan, Dehua Tao, Chengxi Deng, Hanlin Zhang, Xiao Chen

**机构**：华为AI Lab、香港中文大学、香港城市大学

**发布日期**：2026-09-14 | **论文**：https://arxiv.org/abs/2609.15313 | **PDF**：https://arxiv.org/pdf/2609.15313v1 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
交错生成文本与声学token的语音大语言模型在流式口语应答时，已生成的声学token会进入后续文本预测的上下文，使相同语音输入下语音转文本及语音（S2TS）模式内部文本的答题准确率显著低于纯S2T模式，作者将此差异命名为「输出模式差距」（OMG）。Step-Audio-2-mini在Spoken-MQA和语音渲染GSM8K上的OMG分别高达42.87与29.72个百分点。本文提出联合输出在线蒸馏（JO-OPD），利用模型自身更强的S2T策略作为教师，沿学生自生成的S2TS轨迹蒸馏文本预测，并加入非文本预测保持正则。JO-OPD将两个基准的OMG分别降至16.26与13.04个百分点，S2T准确率几乎不变。

### 🔧 技术方案

**问题背景：** 交错式文本-声学token自回归生成（如Step-Audio 2、Baichuan-Audio）支持流式口语输出，但声学token进入上下文后干扰后续文本预测，造成OMG。现有研究多聚焦输入侧模态差距，输出侧差异未被系统量化。

**模型架构：** JO-OPD不引入新模块，复用基础模型同时充当学生、教师与非文本参考。学生以S2TS模式采样联合轨迹z；在文本位置i构造学生上下文（语音输入、原生联合历史）与教师上下文（语音输入、文本投影历史），教师与参考分支全程冻结，仅更新学生。

**核心创新：** (1) 首次正式定义并量化输出模式差距，实证启用语音输出对文本推理能力的损害，且显式推理指令（CoT）会进一步扩大差距。(2) 联合输出在线蒸馏：教师基于学生前缀的文本投影历史做S2T预测，学生基于完整交错历史做S2TS预测，蒸馏损失仅在文本词表内计算，保留教师对候选文本token的相对偏好而不改变文本与非文本的概率分配。(3) 非文本预测保持正则：对共享输出头的声学与控制token预测与冻结参考的S2TS分布做匹配，防止破坏语音生成能力。

**训练策略：** 训练集为27,847条prompt（Tulu 3与NaturalReasoning，剔除评测重叠），用flite的SLT音色合成训练语音。固定初始学生S2TS轨迹训练一个epoch；优化器AdamW，batch size 32，学习率2e-6。

### 📊 实验结果
**数据集**：Spoken-MQA（1,402题）、语音渲染GSM8K（1,319题）、VoiceBench-BBH（1,000条真人录音，Short与CoT两种条件）

**主要指标**：
- Step-Audio-2 Spoken-MQA：S2TS(T) 32.45→58.92，OMG 42.87→16.26 pp，S2T 维持75左右
- Step-Audio-2 GSM8K：S2TS(T) 39.50→56.86，OMG 29.72→13.04 pp
- Baichuan-Audio：MQA的OMG 12.41→9.49 pp，GSM8K的OMG 10.39→9.78 pp
- 消融：Soft较Hard的S2TS(T)高17.97（MQA）；去保持正则跌至29.74
- 数据规模：2k/8k/27,847条prompt对应S2TS(T) 36.95/49.71/58.92

**是否开源**：暂无（未提供代码或模型权重）

### ⭐ 评分：8/10
评分理由：创新性上首次系统定义并量化输出侧模式差距，现象发现清晰、切中交错生成架构的核心痛点；JO-OPD方法简洁有效，在两个代表性开源模型上均取得可复现的定量改进，消融设计完整。不足在于训练规模较小、口语评估依赖ASR间接度量，且未在Thinker-Talker等其他架构上验证。

---

## [7] Cross-Lingual F5-TTS 2: A Simplified Framework for Language-Agnostic Voice Cloning

**arXiv ID**：2609.15184 | **方向**：语音大模型（跨语言语音克隆TTS）

**作者**：Qingyu Liu, Rixi Xu, Yushen Chen, Zhikang Niu, Haitao Li, Pengcheng Zhu 等

**机构**：约翰霍普金斯大学、上海交通大学X-LANCE实验室、上海创新研究院、吉利、浙江大学

**发布日期**：2026-09-14 | **论文**：https://arxiv.org/abs/2609.15184 | **PDF**：https://arxiv.org/pdf/2609.15184 | **代码**：暂无 | **Demo**：https://qingyuliu0521.github.io/Cross-Lingual_F5-TTS_2_demo/

### 📌 简介
零样本TTS推理时通常依赖音频提示的文本转写，跨语言克隆场景下该转写常不可得。本文提出Cross-Lingual F5-TTS 2，用预训练F5-TTS合成同说话人提示音，与真实语音构成配对进行有监督微调，无需强制对齐即去除转写依赖。实验在LibriSpeech-PC与Seed-TTS上取得最高说话人相似度SIM-o 0.687/0.683/0.768，可懂度不降（WER低至2.014%），并泛化至8种训练未见语言的提示音。

### 🔧 技术方案

**问题背景：** F5-TTS依赖提示音转写承担双重角色：文本条件与时长估计参考。Cross-Lingual F5-TTS用MMS强制对齐分割训练对并训练音节级语速预测器（SRP）来消除该依赖，但对齐对边界错误敏感、随语言扩展成本上升，且提示音带头尾静音时SRP会低估语速、高估时长导致语音被拉伸。

**模型架构：** 沿用F5-TTS-Base的DiT主干（22层、16头、1024维）。训练时将合成提示音与真实目标按时间轴拼接x1=[x_syn; x_target]，用掩码m令提示区可见、目标区被预测。文本序列为N个可学习提示token⟨P⟩加EOS标记'. '再拼接目标文本与填充token⟨F⟩。SRP为Transformer（6层、8头、512维），输出离散语速类别。

**核心创新：** (1) 合成提示有监督微调：以真实语音为参考、从文本池采样目标文本，用预训练F5-TTS合成同说话人提示音，构造不依赖外部对齐器的同说话人配对。(2) 提示token文本条件：用比例驱动的可学习⟨P⟩加EOS替换缺失转写，保留预训练文本-音频布局，EOS标记提示区与目标区分界，加速WER收敛。(3) 静音鲁棒SRP：以70%/10%/10%/10%概率在提示音前、后、两侧插入原时长30%-70%的静音做增强，使语速预测对首尾静音免疫。

**训练策略：** 主模型在Emilia约9.5万小时中英文真实语音上配对生成2.9万小时合成提示，100K步、8卡A100、每卡38400帧、AdamW、学习率先20K线性升至7.5e-5再线性衰减。SRP在中英各500小时上30K步训练，学习率升至2.5e-4。推理用Euler求解器NFE=32、CFG=2.0、Vocos声码器。

### 📊 实验结果
**数据集**：LibriSpeech-PC test-clean, Seed-TTS test-en/test-zh, 及自建8语种OOD跨语测试集

**主要指标**：
- LIBRISPEECH-PC WER：2.014%（三个系统中最低）
- SIM-o：0.687（LibriSpeech-PC）、0.683（test-en）、0.768（test-zh），均最高
- UTMOS：3.704（LibriSpeech-PC）、3.544（test-en）、2.761（test-zh）
- 跨语SIM-o：16对中14对优于Cross-Lingual F5-TTS
- 填充静音后SRP的MRE：原版>70%，本文13.15%-18.93%

**是否开源**：资源公开，含演示页面；代码仓库暂未公布

### ⭐ 评分：8/10
评分理由：以合成提示微调替代强制对齐，数据管线显著简化且保留完整上下文音色，思路简洁有效；新增prompt token+EOS条件化与静音鲁棒SRP两个针对性改进，消融完整。实验覆盖8语种OOD跨语克隆、静音健壮性及数据规模消融，但自然度略逊于基线，仅中英两训练语言，且缺正式代码仓库。

---

## [8] Building a Production Greek-English Speech Recognizer

**arXiv ID**：2609.13498 | **方向**：语音大模型（ASR）

**作者**：Christos Petrocheilos, Cleopatra Papadopoulou, Chris Porikis 等

**机构**：Sophea AI Lab, KIEFER SA（希腊雅典）

**发布日期**：2026-09-11 | **论文**：https://arxiv.org/abs/2609.13498 | **PDF**：https://arxiv.org/pdf/2609.13498v1 | **代码**：暂无 | **Demo**：https://huggingface.co/spaces/KIEFERSA/sophea-asr-k1-docs

### 📌 简介
本文报告为希腊语与英语混合语音构建商业级双语ASR系统Sophea的多月工程实践。系统需同时通过九项生产门禁：四个希腊语和三英语WER上限、95%语种识别下限、非语音零幻觉。在23次训练迭代后发现关键负结果：希腊噪音门禁需约1500步密集噪音暴露，而英语LID门禁最多容忍250步，两区间相差约6倍且永不重叠，单一模型无法全部通过。最终交付模型家族加路由服务层与解码端修复，集成系统Sophea ASR K1登上Open ASR Leaderboard（4.26平均WER）。

### 🔧 技术方案

**问题背景：** 希腊语音频多来自电话线、嘈杂会议室而非录音棚，且单句内希腊英混合切换，数据稀缺。固定容量双语模型面临"多语言诅咒"，其竞争本质是声学邻域而非语言数据量：加835小时纯净英语保护无济于事，而577小时噪声重叠会议英语即保住指标。

**模型架构：** (1) 紧凑1.7B双语模型（Qwen-Audio谱系内部改造）C1-C7七轮；(2) 大模型（Whisper内部微调）L1-L7七轮，面向会议；(3) Turbo层用四解码器层Whisper变体。ROVER混淆网络逐词投票按置信度破平，K1系统改用梯度提升分类器做整片段仲裁。

**核心创新：** (1) 量化为两语言训练步数预算前沿（s≥1500 vs s≤250），证明组合变化只沿前沿移动，只有容量/辅助目标/架构才能平移前沿。(2) UTMOS锚定校准：绝对阈值3.0会丢弃98.7%希腊语料，改以域内干净参考校准后仅丢10.6%。(3) 双解码端修复胜于重训策略：VAD加双阈值把静音幻觉压到2%以下；剔除"ok/okay"使boilerplate从26降至0；自动LID+beam=5+重复惩罚1.1使Turbo码转换WER从10.78降到9.79。

**训练策略：** 六阶段数据管线：音频质量分、词速合理性、转写置信度、多教师交叉校验、强制对齐、语言均衡组装。最终希腊1073294/英语1079148行，均衡差0.55%。

### 📊 实验结果
**数据集**：FLEURS、Common Voice、LibriSpeech、AMI、Open ASR Leaderboard八套英语集、专有希腊语料

**主要指标**：
- 希腊语脏环境WER：K1单模型25.88（首次单served模型破≤26门禁）
- 希腊码转换WER：三模型投票23.84 vs 单模型59.74
- 重叠语音WER：53.35降到37.87（相对降29%）
- K1七清洗集平均WER：4.35；LibriSpeech test-clean 1.18

**是否开源**：未开源。模型权重、训练数据、评测集均不发布。

### ⭐ 评分：7/10
评分理由：首次定量给出ASR双语言训练步数预算不可能性前沿，UTMOS锚定校准与"解码端先于重训"策略具可复用工程价值；23次迭代、预注册消融、完整负结果清单披露极为诚实充分。但核心结果偏工程经验报告，评测多依赖专有不可复现语料，无开源，学术增量有限。

---

## [9] DiTAR+: Dual Optimization for Robust Autoregressive Diffusion Speech Synthesis

**arXiv ID**：2609.13909 | **方向**：语音大模型（语音合成/扩散TTS）

**作者**：Ziyu Zhang, Tianlun Zuo, Hanzhao Li, Haoyu Zhang, Lei Xie

**机构**：西北工业大学 ASLP@NPU

**发布日期**：2026-09-12 | **论文**：https://arxiv.org/abs/2609.13909 | **PDF**：https://arxiv.org/pdf/2609.13909 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
连续隐空间自回归扩散Transformer（AR-DiT）在零样本语音合成中展现巨大潜力，但在长句或复杂语言结构下解码稳定性不足。本文提出DiTAR+双优化框架：膨胀上下文采样（DCS）扩大历史感受野，分层声学掩码（HAM）抑制扩散解码器浅层的声学惯性捷径。在ZH-Hard硬句集上WER从12.478%降至9.893%，在25至35秒长句上SIM从0.741升至0.759且WER从2.778%降至2.173%。

### 🔧 技术方案

**问题背景：** 连续latent AR-DiT保留更丰富的音色、韵律与频谱细节，但存在两大瓶颈：LocDiT感受野窄，长句生成时历史信息逐渐不可达引发累计误差与说话人漂移；迭代去噪中浅层网络过度依赖历史声学走"复制延续"捷径而弱化LM语义条件。

**模型架构：** DiTAR+以DiTAR为骨干：VAE将波形压缩为连续latent，非重叠patch化并映射为聚合嵌入；因果自回归Transformer在patch间预测语义条件向量h_i，LocDiT在patch内重建细粒度连续token。DCS保留c个连续局部patch（c=3）保证边界平滑，同时以固定步长j稀疏采样远端patch。HAM引入逐层可变注意力掩码，浅层对历史声学注意力置-∞，深层恢复访问。

**核心创新：** (1) DCS以近零计算开销扩大宏观感受野：与朴素Skip-patchify重排不同，DCS保证绝对物理时序完整，消融显示朴素重排使ZH-Hard WER恶化至16.231%。(2) HAM按深度渐进暴露条件，从结构上切断声学惯性捷径；频谱分析显示基线陷入25.5秒循环退化（WER高达52%），HAM后按时于14.0秒终止且WER降至6%。(3) 两个机制均参数免费且效应正交：DCS主导时序一致性与长句说话人保持，HAM主导语义鲁棒性。

**训练策略：** 在Emilia大规模多语种语音数据集上从零训练，4节点32块H20 GPU集群，每卡batch size为8；推理使用Euler ODE采样器10步，CFG尺度α=2.0，最大prompt长度截断为75。

### 📊 实验结果
**数据集**：Seed-EN、Seed-ZH、ZH-Hard（400条中文硬句）、ZH-Long（400条约25-35秒中文长句）

**主要指标**：
- Seed-EN WER/SIM：1.672%/0.735（WER最低）
- Seed-ZH WER/SIM：0.985%/0.762（全场最优）
- ZH-Hard WER/SIM：9.893%/0.695（比DiTAR的12.478%大幅降低）
- ZH-Long WER/SIM：2.173%/0.759（双项全场最优）
- 主观N-MOS/Q-MOS/S-MOS：3.71/3.82/3.58

**是否开源**：未提供代码、模型权重及Demo链接

### ⭐ 评分：7/10
评分理由：对AR-DiT两类核心失效模式的诊断精准，DCS与HAM机制简单优雅且参数免费，具备直接嵌入现有模型的工程价值；实验充分，涵盖双语标准集、硬句与长句压力测试、完整消融、主观MOS与频谱定性分析。但本质上是对现有DiTAR框架的针对性增补改进，缺乏范式层面突破，且未开源、缺少训练细节。

---

## [10] Modeling, Scaling, and Decoding: Optimizing Controllable Speech Generation with Nonverbal Vocalizations

**arXiv ID**：2609.14231 | **方向**：语音大模型（可控语音生成/非语言发声）

**作者**：Ziyu Zhang, Yun Chen, Taihui Wang, Hanzhao Li, Qicong Xie, Rilin Chen, Zhixian Zhao, Lei Xie 等

**机构**：腾讯海燕语音团队（Tencent HY Speech Team）

**发布日期**：2026-09-13 | **论文**：https://arxiv.org/abs/2609.14231 | **PDF**：https://arxiv.org/pdf/2609.14231v1 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
可控地合成非语言发声（NVV）对自然且富有表现力的语音至关重要，但因其声学形态多样、语料分布极不均衡，仍是难题。本文提出NVV感知的DiTAR系统：以连续语音潜在表示建模，将16个NVV类别注册为专用特殊token，并改造停止预测以区分句中发声与真实句尾。系统先在10万小时双语语音上预训练，再在经定向合成增强与频率感知再均衡的数据上继续SFT。最终官方加权双语得分62.786，夺得ISCSLP 2026 NVVSpeech挑战赛Track 2中文第一、英文第二、总榜第一。

### 🔧 技术方案

**问题背景：** 传统TTS主要优化词法流畅性，NVV事件常在数据清洗中被滤除；现有零样本TTS仍无法在指定位置以令人信服的声学表现生成指定NVV。

**模型架构：** 基于自研15亿参数DiTAR，将连续VAE潜在变量分组成声学patch并聚合成embedding，用因果LM提供patch级条件给LocDiT生成下一连续语音patch。将16个NVV标签注册为文本词汇表中的专用特殊token，与普通文本token共享嵌介入空间与自注意力。

**核心创新：** (1) NVV专用token条件建模：每类NVV仅占一个token，避免子词切分破坏标签完整性，连续表示较量化codec更保真NVV精细声学细节。(2) NVV感知停止预测：仅监督最后一个有效patch为停止，含NVV的中间patch一律标为继续，并配合固定正类权重、标签平滑与不detach的LM隐状态，从而区分句中打断性NVV与真实句尾。(3) 长尾感知训练与两阶段推理优化：用合成数据增强弱类，按标签频率感知重采样，推理端搜寻v/τ组合并对每句生成N=5候选按加权多指标评分择优。

**训练策略：** 预训练用10万小时双语语音，NVV部分含NVSpeech-170K、NonVerbalSpeech-38K等公开语料并全部归一化为16类；Adam优化器、学习率5e-5、32块H20 GPU、per-GPU batch为4、patch大小P=10；继续SFT在再均衡混合数据上进行。

### 📊 实验结果
**数据集**：NVSpeech-170K、NonVerbalSpeech-38K（预训练），NVVSpeech挑战赛Track 2开发/测试集

**主要指标**：
- 官方最终分数（ZH/EN/双语）：61.775 / 63.797 / 62.786（总榜第一）
- 相比官方基线（双语61.431）提升1.355分，中文提升2.075分
- 中文CER：5.012%（基线6.267%）| 英文WER：2.194%（基线3.159%）
- DNSMOS：3.221（基线3.026）| NVV检测CA-F1：0.589（基线0.569）

**是否开源**：未提供代码或模型权重，为挑战赛参赛系统技术报告。

### ⭐ 评分：7/10
评分理由：创新性属于对DiTAR的针对性改造，NVV专用token、感知停止预测与长尾训练组合合理但均为工程化增量；实验充分，含渐进式系统对比、逐标签长尾分析与解码配置双消融，证据链完整；实用价值高，以总榜第一的成绩验证了整套方案在可控NVV合成上的有效性。

---

### 📋 其余论文（仅列出标题、链接与评分）

- **The Limits of Reference-Free Speech Quality Metrics as Evaluators and Rewards on Modern Text-to-Speech**（arXiv:2609.13150 | ⭐ 7/10）https://arxiv.org/abs/2609.13150
- **The VoiceMOS Challenge 2026: Evaluating Speech Enhancement, Emotional TTS and Accented TTS Systems**（arXiv:2609.13792 | ⭐ 7/10）https://arxiv.org/abs/2609.13792
- **Machine Unlearning for Speech Question Answering in Large Audio-Language Models**（arXiv:2609.13195 | ⭐ 6/10）https://arxiv.org/abs/2609.13195
- **Neyshekar: An Open Persian Read-Speech Corpus for Automatic Speech Recognition**（arXiv:2609.14542 | ⭐ 7/10）https://arxiv.org/abs/2609.14542
- **Bridging the Modality Gap in Long-Form Clinical Audio: End-to-End SOAP Generation**（arXiv:2609.14467 | ⭐ 7/10）https://arxiv.org/abs/2609.14467
- **Bridging Data, Reasoning, and Alignment: A Unified Framework for Context-Aware Instruction-Following TTS**（arXiv:2609.14740 | ⭐ 7/10）https://arxiv.org/abs/2609.14740
- **Exploring Multimodal Turn-Taking Cues in Face-to-Face Conversation using Voice Activity Projection**（arXiv:2609.14666 | ⭐ 7/10）https://arxiv.org/abs/2609.14666
- **HARP: Agentic Hybrid Retrieval and Analysis for Long-Form Audio**（arXiv:2609.14116 | ⭐ 7/10）https://arxiv.org/abs/2609.14116
- **Word Timestamps and Speaker Attribution with a Non-Autoregressive LLM**（arXiv:2609.15218 | ⭐ 7/10）https://arxiv.org/abs/2609.15218
- **CAL-MOS: Bridging Layers with Adapters for Robust MOS Prediction Across Speech Foundation Models**（arXiv:2609.14956 | ⭐ 7/10）https://arxiv.org/abs/2609.14956
- **Augmenting Large Audio-Language Models with Frame-Level Grounding for Fine-Grained Temporal Perception**（arXiv:2609.15215 | ⭐ 7/10）https://arxiv.org/abs/2609.15215
- **Typhoon ASR Streaming: Steerable Low-Latency Thai Speech Recognition**（arXiv:2609.14991 | ⭐ 7/10）https://arxiv.org/abs/2609.14991
- **OpenEnded: An Open-Response Speech Corpus for Speaking Proficiency Assessment**（arXiv:2609.15666 | ⭐ 7/10）https://arxiv.org/abs/2609.15666

---

## 语音前端

### 📖 完整精读（按评分降序）

## [1] CCMAN: Cognitive Instability-Aware Cross-Modal Attention Network for Interpretable Temporal Biomarkers of Verbal Fluency Speech

**arXiv ID**：2609.14764 | **方向**：语音前端（语音医学检测/言语流畅度）

**作者**：Madhurananda Pahar, Caitlin Illingworth, Dorota Braun, Daniel Blackburn, Heidi Christensen

**机构**：英国谢菲尔德大学计算机科学学院；谢菲尔德转化神经科学研究所（SITraN）

**发布日期**：2026-09-13 | **论文**：https://arxiv.org/abs/2609.14764 | **PDF**：https://arxiv.org/pdf/2609.14764v1 | **代码**：https://github.com/Madhurananda/CCMAN | **Demo**：暂无

### 📌 简介
现有基于语音的认知衰退自动检测多在整段录音上聚合特征，忽略言语流畅度任务中的词级时序动态与生成不稳定性。本文提出认知不稳定性感知的跨模态注意力网络（CCMAN）：先在12个记忆探测任务上预训练任务无关的多模态认知语音表征，再在60秒语义与语音流畅度任务上微调。在843名受试者共165.44小时语音上，语义流畅度二分类Macro-F1达0.81、多分类0.59，语音流畅度达0.77与0.53；独立PROCESS-2基准上最多提升9%。统计发现语义漂移方差与停顿方差在MCI和痴呆组显著升高，验证了时序语音不稳定性作为可解释动态生物标志物。

### 🔧 技术方案

**问题背景：** 传统语义/语音流畅度评分是粗粒度的静态指标；多数深度学习模型对录音级特征平均池化，丢失会话内的检索不稳定性信息，且缺乏跨数据集泛化与临床可解释性。

**模型架构：** 每个60秒录音由ASR时间戳对齐为T个词级token，每token拼接五类特征：语义嵌入s_t、声学表征a_t、spaCy语言描述l_t、停顿特征p_t与语义漂移d_t。各模态经线性投影到共享256维空间，双向交叉注意力MHA(S,A,A)与MHA(A,S,S)捕捉语义-声学交互并计算注意力熵；sigmoid门控融合后送入Transformer编码器，掩码均值池化得到序列表示，拼接全局漂移均值/方差与停顿方差后由投影头生成64维l2归一化嵌入。

**核心创新：** (1) 多模态词级时序表征：首次将语义漂移差分、停顿动态与声学-语义双向交叉注意力整合进认知衰退检测。(2) 认知任务间迁移学习：先在137.30小时12类记忆探测语音上预训练，微调时冻结表征层仅更新约15%参数，学习率由1e-4降至1e-5。(3) 不稳定性感知可解释输出：基于注意力熵正则与全局不稳定性统计构建动态语音生物标志物框架，实现分类性能与临床解释的统一。

**训练策略：** AdamW优化器，5折受试者级交叉验证；复合损失为类别加权Focal Loss（γ=2）、监督对比损失（温度0.07，权重0.3）与交叉注意力熵正则（权重0.01）。ASR使用Whisper、Wav2Vec 2.0、NeMo三系统（WER约20%）。

### 📊 实验结果
**数据集**：CognoMemory平台自建语料（843人、165.44小时）；独立外部基准PROCESS-2

**主要指标**：
- 语义流畅度二分类Macro-F1：0.81（LLM静态基线0.75）
- 语义多分类Macro-F1：0.59（静态基线0.50）
- 语音流畅度二分类/多分类：0.77 / 0.53（+5% / +7%）
- 消融：Base 0.50→+Drift 0.52→+CrossAttn 0.54→+Entropy 0.56→+TF 0.59
- 语义漂移方差：Kruskal H=18.65，MCI/痴呆显著高于HC；停顿方差H=17.00

**是否开源**：已开源完整框架（GitHub: Madhurananda/CCMAN）并发布数据子集

### ⭐ 评分：8/10
评分理由：创新性突出，将词级时序不稳定性作为可解释动态生物标志物并融入端到端跨模态架构，属领域内少见且有临床导向的贡献；实验充分，843人最大规模流畅度语料、双任务双设定结合消融与独立外部验证，统计严谨。扣分在于非公开基准下与SOTA横向对比有限、架构多为已有组件组合，且MCI与痴呆分组区分度不足。

---

## [2] DualSpecSE: A Dual-Path Speech Enhancement Network Integrating Mel and Complex Spectrograms

**arXiv ID**：2609.13911 | **方向**：语音前端（语音增强）

**作者**：Xingchen Li, Ziqian Wang, Zikai Liu, Yike Zhu, Zihan Zhang, Longshuai Xiao, Lei Xie 等

**机构**：西北工业大学（ASLP@NPU）；华为技术有限公司

**发布日期**：2026-09-12 | **论文**：https://arxiv.org/abs/2609.13911 | **PDF**：https://arxiv.org/pdf/2609.13911 | **代码**：https://github.com/StellanLi/SenSE-demo | **Demo**：https://github.com/StellanLi/SenSE-demo

### 📌 简介
Mel域增强方法虽可提升ASR性能，但必须级联预训练声码器才能重构波形，引入级联误差且丢失细粒度相位与幅度细节。本文提出DualSpecSE双路径框架，在不依赖外部声码器的前提下同时输出增强Mel谱与复数谱：Mel分支学习粗粒度ASR友好表征，复数分支精修细粒度谱细节。在DNS Challenge 2020测试集上，仅1.85M参数即达WB-PESQ 3.25、NB-PESQ 3.68、ESTOI 0.936，全面超过CleanMel与TF-GridNet等基线；CHiME-4上波形输出WER降至14.76%（simu）。

### 🔧 技术方案

**问题背景：** Mel谱紧凑且感知动机强，但现有Mel域增强方法重构波形需接入外部声码器，带来级联误差与相位/幅度信息丢失；而纯线性域复数谱方法缺失ASR友好的粗粒度语义约束。两域优势难以兼得。

**模型架构：** 16kHz语音经STFT（Hann窗512、跳128）得复数谱，经幂律压缩后拼接幅度与实虚部为T×F×3输入共享编码器。Mel分支经Mel滤波器组将频率降至80维，以N=7组交替跨带/窄带块输出增强Mel谱；复数分支同构建模线性频域细节。跨带块由频域分组卷积和跨频线性层组成，窄带块采用分组数G=2的双向GroupMamba降低计算量。

**核心创新：** (1) 双路径联合建模：共享编码器下Mel分支与复数分支并行，同时输出可直接喂给ASR的增强Mel谱与用于高保真重构的增强复数谱，无需预训练声码器，以1.85M参数实现端到端双域增强。(2) 交互模块：将Mel分支表征与复数分支融合生成门控掩码，把Mel幅度线索注入复数分支。(3) 融合模块：基于FreeV对增强Mel谱施加伪逆变换得近似幅度谱，用ConvNeXtV2残差模块细化后结合带噪相位重建复数谱，构成联合重构。

**训练策略：** 总损失由五项加权组成（log-Mel域L1、Mel源自幅度L2、复数域实虚部L2、增强复数谱对应Mel域与幅度损失），权重λ依次取0.05、1、0.5、0.01、0.5。AdamW优化器，初始学习率0.001按0.99^epoch指数衰减，batch size 16，每轮50000样本，动态仿真混合数据，共训练200轮。

### 📊 实验结果
**数据集**：DNS3/EARS/Emilia（387小时纯净语音）+噪声376小时；Interspeech 2020 DNS测试集、CHiME-4 simu/real

**主要指标**：
- WB-PESQ：3.25（CleanMel 2.91、TF-GridNet 3.12）
- ESTOI：0.936（TF-GridNet 0.935）
- CHiME-4 WER（波形输出，simu/real）：14.76% / 13.21%（CleanMel 15.95% / 14.03%）
- 参数量/FLOPs：1.85M / 30.0 G/s
- 消融：去除Mel分支后WB-PESQ降至3.12、WER升至19.05%

**是否开源**：是，代码与音频示例见 GitHub

### ⭐ 评分：7/10
评分理由：将Mel与复数谱双路径联合建模，交互、融合模块设计合理且消融实验干净完备，以仅1.85M参数在DNS与CHiME-4上全面超越CleanMel、TF-GridNet等强基线，实用价值高。但本质上是对CleanMel的增量扩展，核心组件多为既有技术的组合，缺乏突破性创新；评测场景与泛化性分析有限。

---

## [3] CRAF: Cross-View Residual-Aware Fusion for Deepfake Speech Detection

**arXiv ID**：2609.13842 | **方向**：语音前端（深度伪造语音检测）

**作者**：Minh-Xuan Phan, Khalid Zaman, Candy Olivia Mawalim, Masashi Unoki

**机构**：日本北陆先端科学技术大学院大学（JAIST）

**发布日期**：2026-09-12 | **论文**：https://arxiv.org/abs/2609.13842 | **PDF**：https://arxiv.org/pdf/2609.13842 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对深度伪造语音检测对未知新型欺骗攻击泛化不足的问题，本文提出跨视角残差感知融合框架 CRAF，以自监督（SSL）表示为主、听觉大语言模型（ALLM）为高层次指导，通过交叉注意力、残差学习与 SSL 优先融合联合建模互补信息。在 ASVspoof 5 开放条件下，CRAF（Kimi-Audio）取得 Eval EER 5.96%、minDCF 0.1192，优于 XLS-R+AASIST 的 9.78% 与 Kimi-Audio+AASIST 的 7.35%，为对比单系统方法中性能最优。

### 🔧 技术方案

**问题背景：** SSL 预训练模型捕获细粒度声学特征，ALLM 提供高层语义上下文，两者互补；但直接拼接式融合对两视角共享信息与各自特有互补信息不加区分，引入冗余并削弱检测关键的 SSL 细粒度信息。

**模型架构：** 冻结的 XLS-R 300M 为 SSL 编码器，可选 Step-Audio、Qwen2-Audio-7B 或 Kimi-Audio-7B 为 ALLM 编码器，经投影层映射至共享 256 维空间。ALLM 引导交叉注意力以 SSL 为查询、ALLM 为键值生成 S^g；参考估计器估计 ALLM 可解释部分 Ŝ，残差 D=LayerNorm(S−Ŝ)；特征级门控选择性精炼残差；最后 SSL 优先融合 Z=S+Dropout(G_f⊙(R+λS^g))。

**核心创新：** (1) 非对称 SSL-ALLM 公式：以 SSL 为主、ALLM 为引导，避免对两视角平等对待造成细粒度声学信息稀释。(2) 跨视角残差学习：用独立交叉注意力估计 ALLM 条件参考，经 S−Ŝ 显式分离互补 SSL 残差，去除门控使 Eval EER 升至 6.69%。(3) SSL 优先自适应融合：tanh 融合权重逐特征加权，以残差路径保留原始 SSL 表示。

**训练策略：** 加权交叉熵加 0.05 标签平滑，投影、交叉注意力、参考估计、残差门控与分类器联合优化而双编码器冻结；AdamW（lr 2e-5，wd 1e-3），梯度累积 4，梯度裁剪 5.0；音频 16kHz，ASVspoof 5 训练集 182,357 条。

### 📊 实验结果
**数据集**：ASVspoof 5 Track 1（开放条件）

**主要指标**：
- CRAF (Kimi-Audio)：Eval EER 5.96% | minDCF 0.1192 | Dev EER 2.41%
- 基线 XLS-R+AASIST：Eval EER 9.78%
- 基线 Kimi-Audio+AASIST：Eval EER 7.35%
- 近期单系统 ASTDT 6.94%、ProSDD 7.38%，CRAF 最优且无集成
- 攻击级分析：较 XLS-R+AASIST 在 16 个攻击中 13 个提升

**是否开源**：论文未提及代码与模型，暂无

### ⭐ 评分：7/10
评分理由：以 SSL-ALLM 残差解耦融合解决跨视角冗余问题，思路清晰，系统消融证明三组件互补及门控必要性，在 ASVspoof 5 开放条件取得单系统最优 EER；但仅在单一数据集验证、未跨数据集评测，机制本质属特征交互改进，创新性中等偏上。

---

## [4] Directivity-Conditioned Low-Latency Neural Filtering for Speech Enhancement in Hearing Aids

**arXiv ID**：2609.15760 | **方向**：语音前端（助听器神经定向滤波）

**作者**：Lennart Uphaus, André Merboldt, Markus Hofbauer, Timo Gerkmann 等

**机构**：德国汉堡大学信号处理组、Audatic GmbH、Sonova

**发布日期**：2026-09-14 | **论文**：https://arxiv.org/abs/2609.15760 | **PDF**：https://arxiv.org/pdf/2609.15760 | **代码**：暂无 | **Demo**：https://sp-uhh.github.io/film-osn/

### 📌 简介
现有神经定向滤波（NDF）方法虽能在推理时自适应调节指向性方向与形状，但总时延高达40-50 ms，且忽略麦克风位置随头径变化、头影效应等听力设备真实约束。本文针对耳背式（BTE）助听器提出10 ms低时延双耳神经滤波框架 FiLM-OnlineSpatialNet（FiLM-OSN），将 FiLM 条件机制注入 OnlineSpatialNet 架构并引入余弦型可配置主瓣宽度。实验表明在 PESQ 2.06、ESTOI 0.77、SI-SDR 5.72 dB 下，10 ms 时延模型达到与放宽时延基线 FiLM-JNF 相当甚至更优的性能。

### 🔧 技术方案

**问题背景：** 助听器场景要求总时延≤10 ms，但现有 NDF 工作时延过高；降低 STFT 窗长虽可降时延，却因谱分辨率下降使宽频带 LSTM 序列变短而显著损伤性能。同时传统 DMA 指向性模式无法精确指定主瓣角宽，且完全抑制来向噪声不利于空间态势感知。

**模型架构：** FiLM-OSN 输入为 Q=4 通道（每只 BTE 设备取双麦克风）STFT 复数实虚部拼接张量。核心为 L=4 个交错的跨频带块、FiLM 层与窄频带块，通道数 C=96。窄频带块用 Mamba 状态空间模型替代 LSTM 建模长时依赖。采用8 ms STFT窗、2 ms跳帧，总时延10 ms，参数量700 k，输出双耳两通道。

**核心创新：** (1) 将 FiLM 条件机制引入 OnlineSpatialNet 构建 FiLM-OSN，用 Mamba 替换 LSTM，在低谱分辨率下保持长程时域建模能力。(2) 提出余弦指向性模式 Λ(θ)=|cos(π/W·∠e^{j(θ-θ_d)})|，可精确指定主瓣宽 W 与最大衰减 M。(3) 设计 IPD 相位保持损失，以参考通道能量加权并用余弦规避相位歧义，使网络在保留 ITD 的同时保持跨通道谱相干。

**训练策略：** 采用 WSJ0 语音与19个 HARTF 模拟 P=5 说话人房间场景，共模拟6000/1200/600条 BRIR；每样本5种指向性模式形成30000/6000/3000个训练/验证/测试样本。训练100轮，早停；批量大小6，学习率1e-3，指数衰减调度器γ=0.99。

### 📊 实验结果
**数据集**：自建仿真双耳数据集（WSJ0+HARTF BTE 房间脉冲响应模拟）

**主要指标**：
- FiLM-OSN_{8ms,L1+IPD}：PESQ 2.06±0.46 | ESTOI 0.77±0.08 | SI-SDR 5.72±2.73 dB
- FiLM-JNF（32 ms/40-50 ms）：PESQ 2.10±0.46
- FiLM-JNF（8 ms）：PESQ 1.72±0.36 | ESTOI 0.66 | SI-SDR 2.98 dB
- 参数对比：700 k vs FiLM-JNF 950 k
- IPD 损失使波束图与目标模式高度吻合

**是否开源**：未提供代码与模型，仅提供音频示例网页

### ⭐ 评分：7/10
评分理由：将动静态结合的低时延神经定向滤波落地于助听器场景，方法简洁有效，以更小参数量在10 ms时延下追平甚至超越40-50 ms基线，实用性突出。但数据集均为自建仿真、缺乏公认基准与真实设备评估，竞争者仅 FiLM-JNF 一个基线，创新性与验证深度属于扎实的增量工作。

---

## [5] Subphonetic Acoustic Modeling via Optimal Transport for Pronunciation Assessment

**arXiv ID**：2609.13694 | **方向**：语音前端（发音评测/次音素声学建模）

**作者**：Haopeng Geng, Jiun-Ting Li, Daisuke Saito, Nobuaki Minematsu 等

**机构**：东京大学工学研究科；中华电信先进技术实验室

**发布日期**：2026-09-12 | **论文**：https://arxiv.org/abs/2609.13694 | **PDF**：https://arxiv.org/pdf/2609.13694v1 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
发音评测需要时间精确、诊断上可解释且忠实于学习者实际发声的声学证据，但现有模型在识别与分割间存在根本权衡。作者提出拓扑感知的逐帧声学模型，将每个音素展开为有序次音素状态，并用最优时序传输分类（OTTC）学习稠密单调的帧到状态指派。在TIMIT、Buckeye、L2-ARCTIC上分割精度超过Charsiu等神经基线，并在SO762上取得0.084音素MSE、0.617 PCC的最佳音素级APA性能。

### 🔧 技术方案

**问题背景：** HMM强制对齐依赖多状态拓扑获得音素内部结构，但解码受转录约束不灵活；CTC可免transcript识别但blank主导、后验尖峰，且次音素线索被忽略。

**模型架构：** 以可训练WavLM-large做SSL编码器（10/20毫秒分辨率），后接两个输出头：CTC头预测单音素序列，SP头用OTTC预测展开后的次音素状态序列。CTC后验先经过FiLM式线性调制条件化SP头。两个预测头均为两层MLP（隐藏层384、ReLU）。

**核心创新：** (1) 在神经声学模型中重建HMM式有序次音素拓扑SxTy，将音素内状态转化为显式输出单元。(2) 用OTTC作为稠密单调状态传输训练：将对齐定义为一维最优传输问题，以-Σγ_ij·log p(z_j|x_i)监督。(3) 耦合CTC损失维持识别能力，并设计拓扑感知解码。

**训练策略：** 仅在LibriSpeech train+dev（971.6小时）训练；联合训练两头上至50轮、批大小32，总损失L=0.5·L_CTC+0.5·L_OTTC，之后做1000步帧级CE监督稳定静音帧。

### 📊 实验结果
**数据集**：LibriSpeech（训练）、TIMIT、Buckeye、L2-ARCTIC、speechocean762

**主要指标**：
- TDFA分割：Ours–10ms在TIMIT dev/test的TSE为36.37/38.12毫秒
- 消融：同拓扑下CTC换OTTC使TD F1 38.61→62.91、TSE 78.14→40.64ms
- 下游APA（SO762）：音素MSE 0.084、PCC 0.617
- MDD F1：Ours–10ms在L2-ARCTIC达0.486

**是否开源**：论文未提供代码链接；解码依赖开源工具K2-FSA

### ⭐ 评分：7/10
评分理由：将HMM式有序次音素拓扑与OTTC结合用于发音评测，动机清晰且有理论框架支撑，属实质贡献。实验覆盖阅读语、自发语与L2语，同时验证分割、识别、MDD和APA下游任务。但拓扑CTC与OTTC均为已有概念，组合创新有限，且仅用LibriSpeech训练、未开源，实用推广受限。

---

### 📋 其余论文（仅列出标题、链接与评分）

- **Robust Cross-Domain Speech-Based Alzheimer's Disease Detection via Iterative Adversarial Self-Training**（arXiv:2609.14139 | ⭐ 7/10）https://arxiv.org/abs/2609.14139
- **Exploiting Speech LLM Representations for Multilingual and Cross-Lingual Parkinson's Disease Detection**（arXiv:2609.14431 | ⭐ 7/10）https://arxiv.org/abs/2609.14431
- **A New Transformer-Based Approach for Audio-Based Kinship Verification and a New Uncontrolled Mandarin Kinship Speech Dataset**（arXiv:2609.14145 | ⭐ 7/10）https://arxiv.org/abs/2609.14145
- **Interpreting hierarchical organisation of speaker embeddings**（arXiv:2609.15203 | ⭐ 6/10）https://arxiv.org/abs/2609.15203
- **OLAC: An Overlapped Lossless Audio Codec in the Time-Domain with MDCT Compatibility**（arXiv:2609.15616 | ⭐ 7/10）https://arxiv.org/abs/2609.15616
- **Listening for Airway Stenosis: A Foundation Model-Based Method for Rapid and Accessible Detection**（arXiv:2609.15453 | ⭐ 7/10）https://arxiv.org/abs/2609.15453
- **Graph Attention Design Choices Matter: A Controlled Study of LoRA-Adapted Audio Anti-Spoofing**（arXiv:2609.15650 | ⭐ 7/10）https://arxiv.org/abs/2609.15650

---

*Generated on 2026-09-15*