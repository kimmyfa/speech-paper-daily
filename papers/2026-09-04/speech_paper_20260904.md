# 2026-09-04 语音论文速递

**共收录**: 9 篇 | **语音大模型**: 6 篇 | **语音前端**: 3 篇

> 目标日期 2026-09-04（北京时间）arXiv 语音相关论文共命中 9 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] VibeVoice-ASR-Streaming Technical Report

**arXiv ID**：2609.02812 | **方向**：语音大模型

**作者**：Yujie Tu, Zhiliang Peng, Jianwei Yu, Li Dong, Songchen Xu, Yaoyao Chang, Wenhui Wang 等

**机构**：微软研究院（Microsoft Research）、中国科学院大学、上海交通大学

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.02812 | **PDF**：https://arxiv.org/pdf/2609.02812.pdf | **代码**：https://github.com/microsoft/VibeVoice | **Demo**：https://huggingface.co/spaces/microsoft/VibeVoice-ASR-Streaming

### 📌 简介
现有端到端说话人标注ASR（如VibeVoice-ASR）已统一ASR与说话人日志，但仅支持离线识别，难以满足实时语音助手的低延迟需求。本文提出 VibeVoice-ASR-Streaming，首批基于LLM的流式说话人标注ASR方案：将固定音频块、0.5秒前瞻与历史文本交错生成"谁说了什么"。7B模型在五个评测集上取得最低平均WER/CER（24.66），在13项说话人标注设置中12项取得最优或并列最优cpWER/cpCER，且2.00秒标注延迟远低于云服务的8.21/9.12秒，并开源1.5B与7B权重及推理代码。

### 🔧 技术方案

**问题背景：** 现有流式LLM-ASR仅支持单说话人转录，而流式多人识别需额外声纹/聚类等说话人组件；历史上下文对保持说话人身份一致至关重要，两个方向均未同时满足"流式+说话人标注"。

**模型架构：** 基于VibeVoice-ASR的双tokenizer（声学σ-VAE与语义tokenizer均3200倍下采样，24kHz下每帧133.3ms），特征拼接后投影至Qwen2.5 LLM主干兼容1.5B/7B参数。语音块Xk与标注文本块Yk交错为单自回归序列[X1,Y1,X2,Y2,...]，每块后接4帧（0.5秒）前瞻，经<|text_chunk_end|>结束符控制切换。

**核心创新：** (1) 首个LLM端到端流式说话人标注ASR：交错生成只需保留完整历史上下文，说话人身份由词法与对话证据确定，无需额外日志阶段，标签由首现序号在整段会话中复用。(2) 三段式训练路由（离线→流式预训练→流式微调），各阶段仅改变样本构造而非模型，达成约42万小时到1.3万小时的平滑迁移。(3) 详尽设计消融：chunk尺寸、前瞻深度、模型规模、标签前置/后置复杂度均被系统评估，并给出延迟RTF服务成本分析。

**训练策略：** 基于Qwen3-ForcedAligner词级对齐切分块目标；合成会议数据含领域术语、说话人重叠与RIR卷积增强（50,884段/4519.6小时）。AdamW（β1=0.9,β2=0.95,wd=0.1）梯度裁剪2.0，bfloat16，cosine调度峰值LR 5×10⁻⁵，序列8192 token；Stage 3为8卡500步、全局batch 64。

### 📊 实验结果
**数据集**：AISHELL-4、AliMeeting、AMI（IHM/SDM）、MLC-Challenge（9语种）、AISHELL-1、LibriSpeech test-clean/test-other、GigaSpeech

**主要指标**：
- 五集平均WER/CER：24.66（Gemini 3.5 Transcribe Live为25.23、GPT Realtime Whisper为39.31）
- 说话人标注13项中12项最优/并列最优cpWER/cpCER；MLC平均cpWER 22.75（Azure CT为27.06）
- 预期标注延迟2.00秒（vs Azure CT 8.21秒、Google STT 9.12秒）
- 流式化代价：WER/CER升0.75–3.53，cpWER/cpCER升5.13–6.67
- 单说话人：AISHELL-1 CER 4.01、LS test-clean 2.33、GigaSpeech 10.20
- 实时因子≤0.104（7B/15帧配置，vLLM+A100单卡）

**是否开源**：开源。1.5B与7B权重（microsoft/VibeVoice-Collection）及含vLLM支持的推理代码（github.com/microsoft/VibeVoice），并提供在线Demo。

### ⭐ 评分：9/10
评分理由：首次将LLM流式ASR与说话人标注深度融合，设计（声学/语义双tokenizer+前瞻+lookahead消融）严谨，实验覆盖多语种会议基准、三大云API实时对比、延迟/成本/消融全面，数据确凿且有RTF、12/13最佳标注等硬指标。局限为面向聚类的历史压缩未解决、长时重叠及八分钟时长上限，稍扣分。开源权重与vLLM推理代码，实用价值极高。

---

## [2] Auditory Illusion Benchmark for Large Audio Language Models

**arXiv ID**：2609.02277 | **方向**：语音大模型

**作者**：Hayoon Kim, Eunice Hong, Kyogu Lee

**机构**：首尔国立大学（音乐与音频研究组MARG、智能与信息系、AIIS、IPAI）

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.02277 | **PDF**：https://arxiv.org/pdf/2609.02277.pdf | **代码**：https://github.com/gillosae/aib | **Demo**：暂无

### 📌 简介
该论文提出AIB，首个面向大型音频语言模型（LALM）的听觉错觉基准，覆盖音乐、声音、语音三领域的十种代表性错觉，共14829个刺激（10385个错觉+4444个匹配对照）。方法将错觉感知判断重构为二元/三元选择题，并配以受控人类听感研究（20名绝对音高听者）实现人与模型的直接对比。结果显示多数LALM在低层物理型错觉上保持信号忠实，部分模型（Audio Flamingo 3、Gemini 3.1 Pro等）在依赖语言/音乐先验的错觉上更接近人类，但无一匹配人类知觉轮廓，最优平均ISI仅0.455。

### 🔧 技术方案

**问题背景：** 现有音频基准（SUPERB、AudioBench、MMAU等）聚焦转录、分类、推理等含客观真值任务，无法评估模型是否复现人类的主观错误知觉；视觉领域已有错觉基准，听觉领域尚属空白，LALM是否能像人类一样受错觉影响完全未知。

**模型架构：** AIB为评测基准而非新模型。以Gregory因果框架将十种错觉按主导机制分为物理型（缺失基频、Zwicker音、Tartini音等）与物理+知识型（说话-歌曲、音素修复等），并覆盖音乐、声音、语音三领域；每类均生成匹配对照刺激，剔除依赖双耳生理（八度错觉）与空间听觉的错觉以保证可评测性。评测统一为二元/三元选择题形式，便于与人类听感结果直接比较。

**核心创新：** (1) 首次系统构建听觉错觉基准：涵盖十种经典错觉，大规模合成刺激并开源生成代码，弥补了听觉领域无错觉基准的空白。(2) 提出三项对比指标：人类相似准确率（HLA）、现实对齐率（RA）与错觉易感性指数（ISI=HLA-RA），将错觉作为认知对齐的诊断工具而非性能指标。(3) 引入Gregory自下而上/自上而下因果分类框架，并配合20名绝对音高听者的受控人类研究（多数投票聚合、无反馈、随机序列），发现提示词改写可使ISI偏移高达0.6，说明易感性是"模型-提示词"联合属性。

**训练策略：** 本工作无需训练模型。刺激经再现性验证筛选，客观题面设双选/三选，模型自由文本经解析映射到答案集，无法解析的响应被剔除；人类试验用头戴耳机在安静环境完成，响应按多数投票构造基准分布。

### 📊 实验结果
**数据集**：缺失基频、Risset节奏、Shepard音、Tartini音、时隙错觉、Zwicker音、节拍变化错觉、连续性错觉、说话-歌曲、音素修复

**主要指标**：
- 平均ISI最优：Audio Flamingo 3（8B）0.455（人类参照1.0）
- 物理+知识型最高ISI：Audio Flamingo 3（8B）0.505；最高HLA：Gemini 3.1 Pro 0.707
- 模型分三态：易感型（MuLLaMa、Audio Flamingo 3）、字面型（Qwen2-Audio-Instruct等）、领域依赖型（Gemini 3.1 Pro、Kimi-Audio-Instruct）
- 提示词精炼使ISI偏移最多0.6，Qwen2-Audio-Instruct重述后物理ISI降至-0.876

**是否开源**：基准数据集与错觉生成实现已开源至 GitHub（https://github.com/gillosae/aib）

### ⭐ 评分：9/10
评分理由：选题精准切入视觉有、听觉无的错觉评测空白，把认知科学概念系统性工程化为评测工具，创新性强。实验充分：含10个模型跨规模对比、受控人类听感基线、提示词敏感性分析，并给出直觉清晰的三态模型归因。指标设计（HLA/RA/ISI）兼顾了感知与响应偏差。扣分点在于人类样本量（20人）略小，对照刺激生成真实性有待大规模验证。整体为语音大模型认知对齐评测树立了高价值基准，实用性强。

---

## [3] SonicCaps: Large-Scale Diverse and Fine-Grained Captioning for Improved Audio-Retrieval

**arXiv ID**：2609.02343 | **方向**：语音大模型

**作者**：Zineb Lahrichi, Marc Ferras, Gaël Richard, Geoffroy Peeters

**机构**：Sony CTC（法国）/ LTCI, Telecom Paris, Institut polytechnique de Paris（法国）

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.02343 | **PDF**：https://arxiv.org/pdf/2609.02343.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有音频-语言数据集普遍存在语义多样性低、描述缺乏声学细节、单对单映射无法反映听觉感知歧义等问题。本文提出大规模音频标题数据集 SonicCaps，含约70万音频片段与约1500万条标题，由多模态大语言模型 Qwen3-Omni 以音频和文本为条件联合生成，并针对每个音频生成约24条多粒度标题。消融实验表明，标题多样性的提升显著优于质量提升，能使 CLAP 模型在检索与零样本分类上一致获益，并提升与人类主观评分（MOS）的相关性。作者已开源数据集及两个专用 CLAP 模型。

### 🔧 技术方案

**问题背景：** 音频感知天生具有一对多的语义歧义，而现有数据集通常每段音频只有一两条标题；LLM 生成的标题重复单调、缺乏细粒度声学细节，手工标注又难以规模化且存在主观偏差。

**模型架构：** 使用 Qwen/Qwen3-Omni-30B-A3B-Instruct 构建三阶段流水线：先做 fidelity-focused 重标注生成 factually 且感知可溯源的 main 标题，再做 diversity-focused 重标注（含 rephrased、rephrased-short、tags 三类），最后后处理。解码采用温度0.6、top-p=0.95、top-k=20、最长30 token，音频重采样至16kHz并截断至10秒。

**核心创新：** (1) 提出两阶段多样性标题生成策略，利用结构化提示词工程与 few-shot 示例引导（如以"dog barking"的多种表达作为风格参照），联合采样一次前向生成约10条改写标题，每条音频共约24条标题，覆盖不同风格、详略与粒度。(2) 明确区分"标题保真度"与"标题多样性"两个维度，设计采样概率可调的多样本采样策略与"标题采样困惑度"指标，揭示多样度与检索性能间的正向关系。(3) 提出多维度的成对主观评测框架（完整性/正确性/合理性/描述性），收集结构化定性反馈与 MOS 评分，并基于保真标题训练出与人类感知相关性显著更高的 CLAP 模型。

**训练策略：** CLAP 采用 RoBERTa-Large 文本编码器与 PaSST 音频编码器，投影至1024维共享空间；对称对比损失（温度τ=0.2），4卡、batch 112（有效batch 448），音频重采样至32kHz取随机10秒片段，训练时以概率0.2随机去除标点。

### 📊 实验结果
**数据集**：AudioCaps 验证集（T2A/A2T）、内部商用音效验证集（Commercial-Val）、ESC-50、FoleyBench

**主要指标**：
- AudioCaps-Val T2A R@5：Ours(8) 78.9 / SonicCLAP_AR 79.5（LAION-CLAP 64.7）
- AudioCaps-Val A2T-any R@5：SonicCLAP_AR 71.3（LAION-CLAP 49.7）
- Commercial-Val T2A R@10：SonicCLAP_AR 43.2（LAION-CLAP 34.8）
- FoleyBench 零样本 R@5：Ours(9) 25.6（LAION-CLAP 9.14）
- ESC-50 零样本 R@1：Ours(8) 89.4（LAION-CLAP 82.1）
- MOS 与 CLAP 得分配对 Spearman ρ：SonicCLAP_MOS 0.32（LAION-CLAP -0.07）

**是否开源**：开源。数据集与两个模型（SonicCLAP_AR、SonicCLAP_MOS）已发布于 https://huggingface.co/datasets/Zineb/SonicCaps。

### ⭐ 评分：9/10
评分理由：将"标题多样度"与"标题质量"解耦并系统性验证，属方法论上的重要贡献，消融实验设计严密、覆盖检索与零样本分类两类任务；主观评测框架引入多维成对比较与定性反馈，为数据集质量评估提供新范式。唯一不足是约70万音频规模中仍有残余冗余，且检索任务限定在单一 CLAP 架构上验证。总体数据量大、开源完整、实用价值高。

---

## [4] Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction

**arXiv ID**：2609.02623 | **方向**：语音大模型

**作者**：Kenichi Fujita, Yusuke Ijima

**机构**：NTT（日本）

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.02623 | **PDF**：https://arxiv.org/pdf/2609.02623.pdf | **代码**：暂无 | **Demo**：https://ntt-hilab-gensp.github.io/IS2026pseudo/

### 📌 简介
本文提出 direction-following TTS 任务：给定脚本、参考语音（pre-mod）与自然语言表演指示，生成保持说话人身份和文本内容、且风格按指示方向改变的新语音（post-mod）。针对缺乏(参考语音、指示、修改语音)三元组训练数据的难题，提出基于印象可控TTS与LLM的可扩展伪三元组构建流水线，得到350,617个伪三元组（127.6小时）。风格精调器基于rectified flow在语音嵌入空间建模方向条件变换。实验表明伪数据保障说话人稳定性、录音数据提升方向对齐，Full条件在seen/unseen测试上UTMOS为2.96/2.97，LLM对齐评分3.79/3.24，SMOS 3.35/3.22。

### 🔧 技术方案

**问题背景：** 大规模零样本TTS语料每条脚本通常只有一次朗读，缺少对"相对风格修改"的刻画；即使有小规模重复朗读语料，也缺少描述修改意图的方向文本。这一稀缺性制约了扩散/流式生成模型及跨说话人鲁棒的说话人保持型风格变换。

**模型架构：** 三组件框架：①语音印象估计器，将语音映射到13维反义词印象向量（11维已验证轴+新增fluent–hesitant、emotional–neutral），RT无法使用，RMSE 0.40；②FastSpeech2+冻结HuBERT编码器的印象可控零样本TTS（27,000小时日语训练，HiFi-GAN V1声码器）；③方向条件风格精调器，基于ModernBERT-Ja-310M编码方向文本，用rectified flow匹配在嵌入空间预测修改量Δ，叠加到pre-mod嵌入上，背骨模型冻结。

**核心创新：** (1) 伪三元组构建流水线：用印象可控TTS生成风格变化的配对语音，经ECAPA-TDNN说话人相似度(0.80–0.95)与语速比(0.85–1.15)筛选，并剔除嵌入几乎相同、变异过小的配对。(2) LLM方向生成基于相对印象差ΔI=I_post−I_pre而非绝对标签，提示LLM扮演导演推断自然语言表演指示，支持组合式/语境化指令。(3) 用rectified flow建模方向条件下的多解嵌入变换：确定回归会坍缩为条件均值产生保守更新，流匹配以x_t=(1−t)x0+tΔ学习随机速度场v_θ，辅以方向一致性、幅度对齐辅助损失，缓解说话人差异导致的方向多义性。

**训练策略：** 精调器用Adam（lr 0.01，batch 32）训练至100万步；流匹配目标+方向一致性/幅度对齐辅助损失。伪数据160,000对筛选后74,619对，每对Qi使用Qwen3-Next-80B-A3B-Instruct生成至多5条方向，去畸形后得350,617三元组（训练346,488/验证4,129，30个held-out说话人）；另采集2名专业配音演员录音数据（8.9小时、6,899对）。

### 📊 实验结果
**数据集**：自建日语伪三元组（1600说话人）、专业演员录音（2人8.9小时）、HiFi-CAPTAIN测试集（unseen说话人）

**主要指标**：
- UTMOS自然度：Full条件 seen 2.96±0.01 / unseen 2.97±0.01，与pre-mod基线(2.95/2.97)相当，无明显退化
- LLM方向对齐评分（1-5）：Full seen 3.79±0.01 / unseen 3.24±0.02；Recorded 3.78/3.37；Pseudo-all 3.67/3.12
- SMOS说话人相似度：Pseudo-all seen 3.54±0.08最佳、Full 3.35±0.08、Recorded仅2.67±0.08
- AlignMOS方向对齐：Recorded最佳seen 3.50±0.07，Full 3.22±0.07
- 说话人嵌入余弦：Recorded条件unseen出现大量低于第5百分位0.57的漂移，Pseudo条件更稳健
- F0分析：Recorded的mean lnF0绝对变化0.14±0.15高于Pseudo的0.05±0.08

**是否开源**：暂无（代码未开源，仅提供Demo音频页 https://ntt-hilab-gensp.github.io/IS2026pseudo/）

### ⭐ 评分：8/10
评分理由：创新点明确——将TTS风格控制从绝对标签转为相对方向建模，伪三元组流水线数据规模大（35万+三元组）且筛选、LLM生成、F0分析等设计严谨，缓解了数据稀缺这一核心痛点。实验充分：客观+主观+LLM评估三路证据，并做了数据规模消融与F0诊断。扣分点：依赖大量自研内部数据与组件无法复现；未见与现有指令TTS同数据条件下的公开基线对比。

---

## [5] Choosing a PEFT Variant for Per-Patient Dysarthric ASR: A Single-Speaker Case Study on Two ASR Bases

**arXiv ID**：2609.02735 | **方向**：语音大模型

**作者**：Bernard Muller, László Tóth, LaVonne Roberts

**机构**：Scott-Morgan Foundation（英国Torquay）；Institute of Informatics, University of Szeged（匈牙利Szeged）

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.02735 | **PDF**：https://arxiv.org/pdf/2609.02735.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
面向重症卒中后构音障碍（dysarthria）患者的单人ASR生产场景，本工作首次系统对比7种LoRA家族PEFT变体（LoRA、QLoRA、AdaLoRA、DoRA、LoHA、VeRA、VB-LoRA）在Whisper-large-v3+匈牙利微调与Qwen3-ASR-1.7B两个生产基座上的效果。注意力投影适配显著降低CER，三种子配对bootstrap证明LoRA与DoRA统计无差异（13.86/13.90%），故选用更简单便宜的LoRA作为生产默认；真实4bit QLoRA在所有种子均更差（14.56%）且不省显存。50-80步小数据预算下其他变体未能追赶LoRA家族，注册数据网格显示约5分钟音频即可获得30min全程CER降幅的45.6%。

### 🔧 技术方案

**问题背景：** per-patient adapter是临床构音障碍ASR的生产架构（单个患者独立训练小适配器、基座不动），但说话人相关小数据端PEFT变体选型从未被系统研究；既有工作（Wagner等AdaLoRA、Ankita等LoHA）均为说话人无关条件，speaker重叠正是per-patient场景的定义属性。

**模型架构：** 两个基座：Whisper-large-v3（1.55B encoder-decoder，含38K段匈牙利语FT合并）与Qwen3-ASR-1.7B（AuT音频编码器+Qwen LLM解码器，多语生产checkpoint）。7种变体经HF PEFT实现，适配目标为编码器与解码器注意力投影模块（Whisper选择encoder self-attn与decoder self/cross-attn的q/k/v/out_proj共384模块，不含FFN；Qwen3选LLM-decoder attention及audio encoder投影/卷积输出）。

**核心创新：** (1) 首次进行七变体在speaker-dependent per-patient条件下的对比，通过"控制变量设计"（基座+数据+配方完全固定、仅变PEFT）使比较可解释，并给出每变体可训练参数、适配器大小与模块清单。(2) 首个跨架构构音障碍PEFT对比（encoder-decoder vs LLM-decoder ASR），并披露Qwen3"warm-base回归"：匈牙利语FT使S1失语CER恶化23.55pp，经dys-only池消融定位为预训练语料窄而非健康对照成分，得出"干净语言微调不可跨架构复用"的结论。(3) 6点注册时间网格（1/3/5/10/15/30min）量化临床采集需求，约5min音频捕获45.6%的CER降幅；并给出目标集归因阶梯与NeMo基座（Parakeet/Canary）LoRA回归或崩溃的负结果。

**训练策略：** AdamW（weight decay 0）、lr 1e-4、bf16、batch 4×grad-acc 4、固定5 epoch（约80优化步）、cosine调度10% warmup、种子42（多因子42/43/44）；262训练/40验证/107测试段，固定预算无早停。硬件DGX Spark。

### 📊 实验结果
**数据集**：S1个人匈牙利语语料（409段、55min，重度卒中构音障碍；训练池32.68min）；38K段匈牙利语池（Common Voice+FLEURS+匈牙利语失语+命名失败+VoxPopuli_hu）；Qwen3内部多语言评估集（131,849段）

**主要指标**：
- Whisper-large-v3+HUFT零样本 CER 29.46%，LoRA r=16 三种子平均 13.86±0.07%（相对降低52.8%）
- DoRA r=16 13.90±0.07%，配对bootstrap无显著差异（Δ+0.03pp，CI[-0.17,+0.25]，p=0.79）
- 真实4bit QLoRA在Whisper/Qwen3上 14.56%/30.09%，落后且峰值显存16.9 vs 14.8GiB无节省
- Qwen3-ASR零样本 49.46%，LoRA 28.10±0.60%
- LoHA在Whisper上 23.99%；VeRA/VB-LoRA/AdaLoRA未达LoRA家族
- 全参数FT 11.43±0.50%；LoRA扩展到FFN后 12.09%（28.8M参数/115MB）
- 注册网格：5min 22.49%，10min 18.87%，30min 14.17%
- Qwen3 HU-FT回归 +23.55pp（S1），dys-only池更差（+28.75pp）

**是否开源**：训练脚本、各变体配置与Pareto/注册网格运行器将以source-available形式发布（research-use许可、商用保留）；S1语料与训练适配器受数据共享协议（DSA）限制不公开。

### ⭐ 评分：8/10
评分理由：该工作填补了构音障碍ASR领域per-patient PEFT变体对比的空白，控制变量设计与多因子统计检验（配对bootstrap）提高了结论可信度；汇报多个负结果（NeMo回归、Qwen3 warm-base回归、QLoRA劣势）体现方法论严谨性，且注册时间网格对临床落地有直接实用价值。局限在于单说话人单语言轻病例，结论外推性有限，且公开代码尚无实际URL，复现性受折扣。

---

## [6] Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models

**arXiv ID**：2609.01723 | **方向**：语音大模型

**作者**：Kunlin Cai, Kaiyuan Zhang, Zihang Xiang, Jinghuai Zhang, Abeer Alwan, Fnu Suya, Yuan Tian

**机构**：University of California, Los Angeles (UCLA); University of Tennessee, Knoxville

**发布日期**：2026-09-01 | **论文**：https://arxiv.org/abs/2609.01723 | **PDF**：https://arxiv.org/pdf/2609.01723.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
该论文首次针对现代生成式 TTS 模型提出黑盒成员推断攻击（MIA）框架，在说话人级和记录级两个粒度上审计隐私泄露。方法上，作者刻画了 TTS 双条件输入（文本+参考语音）的查询空间并提出两条评估准则，发现"复述查询"（Recitation）最有效；在表征工程中，采用 WavLM 多层级特征结合改进的 DTW 时序对齐和 LSTM 评分器。在 CosyVoice2、F5-TTS、XTTS-v2 三个模型和 VCTK、British Dialect 两个数据集上，说话人级 AUC 始终高于 0.80（最强设置接近 1.0），记录级 AUC 达 0.80–0.90。DP-SGD（ε=4,10）可将攻击降至接近随机水平。

### 🔧 技术方案

**问题背景：** 现有黑盒 MIA 对生成模型采用"查询生成+表征工程"两阶段流水线，但 TTS 的双条件输入（文本+参考语音）产生了巨大的未探索查询空间，且语音的多层级特性与时序变异性导致低层声学特征（Mel谱、MFCC）无法捕捉成员推断信号。

**模型架构：** 整体框架包含三个模块：查询生成器 G_Q（基于 Recitation 策略，用目标记录的完整文本和音频作为查询）、表征提取器 ϕ（说话人级使用 WavLM+ECAPA-TDNN 声纹编码器，输出 192 维嵌入；记录级使用 WavLM Base 24 层 Transformer，每层 d=1024）、时序对齐与评分模块（说话人级用余弦相似度直接比较拼接后的固定维度向量；记录级用改进 DTW 将生成特征对齐到目标时间轴，再由 LSTM 聚合为标量成员分数）。

**核心创新：** (1) 提出首个 TTS 黑盒 MIA 框架，在说话人级和记录级两个粒度审计隐私泄露，后者即使在非成员来自同说话人的困难设定下仍有效（AUC 0.80–0.90）。(2) 系统刻画 TTS 双条件查询空间，凝练出 5 种代表查询，并建立"可评分范围"（C1）和"记忆诱发"（C2）两条准则，理论预测结合实验验证 Recitation 是最强查询（说话人级 AUC 0.980，记录级 0.896）。(3) 针对语音的变长连续波形特性，设计多层级 WavLM 表征+改进 DTW（将生成特征扭曲到目标帧轴而非提取可变长度路径）+ LSTM 时序聚合器，实现了帧级细粒度比较。

**训练策略：** 攻击分类器（LSTM）在影子模型上训练，影子模型与被攻击模型同架构，在不相交的说话人集上微调。数据集划分：从各数据集随机选 100 说话人，等分 50 人用于受害模型和影子模型；受害模型微调数据量 N=5000（VCTK）/N=3000（British Dialect）。说话人级攻击使用 n=3 条攻击者录音、m=5 个随机种子；记录级使用 m=10 个种子。评分使用多查询均值和方差的组合。

### 📊 实验结果
**数据集**：VCTK（44 小时/110 说话人/约 400 句每人）、British Dialect（31 小时/120 说话人/6 种方言）

**主要指标**：
- 说话人级 MIA AUC（CosyVoice2 on VCTK）：0.980
- 说话人级 MIA AUC（CosyVoice2 on British Dialect）：接近 1.0
- 说话人级 MIA AUC（XTTS-v2 on VCTK）：0.841 / British Dialect：0.949
- 记录级 MIA AUC（CosyVoice2 on VCTK）：0.896；F5-TTS on VCTK：0.800 / British Dialect：0.844
- 记录级 TPR@1%FPR（CosyVoice2 Recitation）：0.281
- DP-SGD 防御后 AUC（ε=4）：~0.52–0.53

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：首次系统性地构建了 TTS 的黑盒成员推断攻击框架，创新性地解决了双条件查询空间刻画和多层级表征+时序对齐两大核心难题。实验覆盖 3 种代表性架构（flow-matching/AR/混合）和 2 个数据集，消融研究充分，对数据特征与脆弱性关系的分析深入。但未开源代码，且对 DP-SGD 防御的评估仅限 CosyVoice2 单模型。

---

## 语音前端

## [7] Sensing Bone-Conducted Speech with Earbuds

**arXiv ID**：2609.02165 | **方向**：语音前端

**作者**：Christoph Weyer, Peter Jax

**机构**：德国亚琛工业大学通信系统研究所（RWTH Aachen University, IKS）

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.02165 | **PDF**：https://arxiv.org/pdf/2609.02165.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对无线入耳式耳机在噪声环境下自身语音（OV）采集困难的问题，本文系统分析了佩戴者语音诱发的耳机壳振动（骨导语音）的频谱与空间特性。基于 Anker P3i 与 A20i 两款耳机、17 名受试者的实测数据，发现该振动呈显著低通特性：400 Hz 以上以约 -93 dB/decade 滚降，100-400 Hz 为高功率频段（平均约 530 µg）。空间分析表明耳机主要沿耳道口进出方向振动，且个体间与佩戴间高度一致。仿真证实单轴加速度计按最优方向安装时，400 Hz 以下高功率分量平均衰减小于 1.5 dB，验证了低成本单轴方案的可行性。

### 🔧 技术方案

**问题背景：** 骨导语音可提升 TWS 在噪声下的自语音采集，但耳机壳振动的带宽与空间特性缺乏系统测量，致使加速度计轴数选择、安装方向以及单轴/三轴方案缺乏设计依据，现有多项研究用法不一、未达共识。

**模型架构：** 属测量分析研究而非学习模型。实验以 ST LIS25BA 三轴加速度计记录耳机壳振动，Knowles 头戴式麦克风作气导参考，HTC Vive Tracker 估计头部姿态；利用校准与前倾两次录制中的重力向量配对，经 Kabsch 算法求解 Wahba 问题获得耳机在世界系中的朝向，将振动变换至统一头相关坐标系。后续以 Welch 谱估计、传递函数、PCA 及方向投影仿真为分析手段。

**核心创新：** (1) 首次定量刻画骨导壳振动的频谱特性：100-400 Hz 恒幅约 530 µg，400 Hz 以上 -93 dB/decade 陡降，1 kHz 以上降至约 5 µg，并据此推导达 20 dB SNR 所需的噪声底（100-400 Hz 约 50 µg、1-2 kHz 仅约 0.5 µg）。(2) 提出基于重力向量与头部追踪的双姿态姿态估计算法，在统一头相关坐标系中可视化并跨受试者比较振动主轴方向。(3) 系统评估单轴拾取的可行性：仿真表明按第一主分量方向投影，P3i/A20i 在 400 Hz 以下仅引入平均 0.7/1.5 dB 衰减，而按第三主分量方向达 11-15 dB；并证明偏离最优安装方向 ±45° 内额外衰减小于 3 dB。

**训练策略：** 无需训练。数据采集含 5 s 静默校准、约 37 s rainbow passage 诵读与 5 s 前倾录制，48 kHz 同步采样；采用 Welch 法（4096 点 Hann 窗、50% 重叠）估计 PSD 与麦克风-加速度计传递函数，PCA 前经 100 Hz-1.5 kHz 的 FIR 带通预滤波。

### 📊 实验结果
**数据集**：自采实测数据（Anker P3i 带硅胶羽翼、Anker A20i 豆状），各 17 名受试者（14 男 3 女，23-61 岁），每人两次佩戴、左右耳共 68 路加速度信号

**主要指标**：
- 振动带宽：400 Hz 以上约 -93 dB/decade 滚降；截止频率 P3i 约 360 Hz、A20i 约 280 Hz
- 第一主分量方差占比：P3i 89%（77-96%）、A20i 79%（49-92%）
- 主方向角度离散度：P3i 6.5°、A20i 14.7°
- 单轴投影平均衰减（100-400 Hz，最优方向）：P3i 0.7 dB、A20i 1.5 dB
- 最差方向投影衰减：P3i 15 dB、A20i 11 dB

**是否开源**：未提供代码与数据；前期并列工作已发表于 IWAENC 2024

### ⭐ 评分：8/10
评分理由：创新性较高，首次系统量化骨导耳机壳振动的频谱与空间特性，为加速度计选型、轴数与安装方位提供定量依据，弥补了该方向基础数据空白。实验设计严谨，17 名受试者、双模型、双佩戴并辅以头相关坐标系可视化，充分性良好。局限在于仅两款耳机且受限于参考传感器噪声底，无法可靠评估 1 kHz 以上频段。实用价值明确，可直接支撑低成本单轴骨导拾音方案的设计决策。

---

## [8] VAANI Noise Event Dataset: A curated spontaneous speech dataset annotated with timestamps for noise events

**arXiv ID**：2609.02474 | **方向**：语音前端

**作者**：Pavan Kumar J, Agneedh Basu, Pranav Bhat, Sujith Pulikodan, Suryansh Shukla, Nihar Desai, Prasanta K. Ghosh

**机构**：AI & Robotics Technology Park（ARTPARK），I-Hub @ IISc；印度科学研究院（IISc）电气工程系

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.02474 | **PDF**：https://arxiv.org/pdf/2609.02474.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有音效语料要么面向通用音频标记，要么面向纯净语音分离，缺少叠加在自发性真实语音上、带时间戳的强噪声标注。VAANI Noise Event Dataset 基于 Project VAANI 在印度自发性语音现场录音，为背景噪声事件添加精确起止时间戳，构成七类语义分类法（动物、交通、婴儿/儿童、音乐、信号/报警、家电、非言语人声）。数据集含 72,756 段语音（122.17 小时、38,541 位说话人），覆盖 58 门语言、30 个邦、162 个地区，共 106,892 个时间戳事件，分 verified/unverified 两个质检层级，服务于抗噪 ASR、声音事件检测与语音增强。

### 🔧 技术方案

**问题背景：** 真实印度场景中语音与车辆、动物、婴儿等非平稳背景噪声共存，噪声起止与语音的重叠关系直接决定识别误差与增强质量。现有语料要么合成混合（WHAM!、DESED 合成子集）、仅帧/片段级弱标签（AVA-Speech、FSD50K、AudioSet）、或无噪声标注（CHiME-6）；iNoise 与 Kathbath-Noisy 虽面向印度，却分别缺少语音与噪声事件标注。

**模型架构：** 数据集采用双层级注释。片段级记录噪声类别多标签列表（NoiseCategory）；事件级对每个噪声出现记录 `{category, tag, start, end}` 四元组（NoiseSubCategoryTimeStamp），时间戳以逐字精确精度字符串存储、原标签同步保留。七大类中非言语人声覆盖 37.8% 片段，动物与交通贡献主要噪声时长，事件可相互重叠并与语音共现，全部标注叠加于单麦克风移动设备录制的自发性多语种印地语音之上。

**核心创新：** (1) 首个将真实同场景语音-噪声共现、跨层重叠时间戳与自发性多语种语音三大属性集于一体的资源——语音与噪声在同一单通道现场录音中自然共存而非事后合成，并保留事件级精确起止。(2) 面向 ASR 的紧凑七类语义分类与双层级标注格式，支持按噪声类型与时间位置的结构化查询，相比 AudioSet 等弱标签语料提供精确时间监督。(3) 分级质检流水线：外部自由职业者标注经结构合法性检查后拆分，约 100 小时直接发布为 unverified，≥20 小时子集经内部复核重标注加 10% 独立随机审计（任一事件不一致即整批重做）后发布为 verified_timestamps，给出可审计的双层质量区分。

**训练策略：** 标注协议与 QC 流程：约 150 小时以上片段自 VAANI 语料采样，训练有素的自由职业者逐段听音标注每个可闻噪声事件的起止时间戳与类别标签；输出先经完整性检查，失败整批返回重做；通过后约 20 小时子集再经内部重标注与 10% 独立审计方进入 verified 层。数据集不含语音类模型训练配置。

### 📊 实验结果
**数据集**：VAANI Noise Event Timestamp Dataset（对比语料：WHAM!、AVA-Speech、MUSAN、FSD50K、AudioSet、DESED、CHiME-6、iNoise、Kathbath-Noisy）

**主要指标**：
- 总规模：72,756 段 / 122.17 小时 / 38,541 位说话人
- 覆盖率：58 门语言、30 个邦、162 个地区（Hindi 占 83.9 小时为主）
- 噪声事件：106,892 个时间戳事件，72,746 段含事件标注
- 质量层级：verified 11,111 段/21.85 小时；unverified 61,645 段/100.32 小时
- 片段时长：0.79～23.49 秒（均值 6.05 秒）
- 类别分布：非言语人声 37.8%、动物 31.3%、交通 24.9%、婴儿/儿童 16.1%

**是否开源**：数据集以 CC BY 4.0 协议公开提供，论文未发布代码仓库，无 Demo 页面；下载入口与检索信息需通过论文及 Project VAANI 相关资源获取。

### ⭐ 评分：7/10
评分理由：作为数据集论文缺乏模型基准对比实验，创新主要体现在既有缺口属性的整合与严谨分级质检流水线，而非全新标注方法；但针对印度真实声学环境、语音与噪声自然共现且带跨层时间戳的数据在公开资源中确属空白，细粒度类别统计与 58 语言覆盖使其对噪声鲁棒 ASR、SED 与语音增强研究具有直接实用价值，尤其 verify/unverify 双层设计便于下游按需选用质量等级。

---

## [9] Removing Speech, Keeping Activities: A Privacy Firewall for Acoustic Sensing in Assisted Living

**arXiv ID**：2609.02376 | **方向**：语音前端

**作者**：Pavlos Nicolaou, Christos Efstratiou

**机构**：塞浦路斯大学 KIOS 研究与创新卓越中心; 英国肯特大学计算学院

**发布日期**：2026-09-02 | **论文**：https://arxiv.org/abs/2609.02376 | **PDF**：https://arxiv.org/pdf/2609.02376.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
为解决辅助生活环境中声学感知系统采集日常活动声时泄露居民言语内容的隐私问题，本文提出"隐私防火墙"流水线：卷积 U-Net 编解码器在 log-mel 频谱域去除语音分量、保留环境活动声，全程仅用合成数据训练；下游活动识别采用 VGGish+SVM 迁移学习。在 ESC-50 和 SINS 上所有语音电平下残言语音均降为 0% VAD 可检测（Silero），ESC-50 40% 语音电平下精确率/召回率恢复至 85%/85%，显著优于 Facebook Denoiser(残余 6.55%)、SepFormer(36.34%)、ConvTasNet(47.21%)；真实 AudioHive 家居录音处理后 VAD 语音为 0%，仍保持 76% 精确率与召回率。

### 🔧 技术方案

**问题背景：** 声学感知能非侵入监测老人日常活动，但居民与护理人员最担忧系统录制私人对话。ADAPTIVE 养老院部署中采用 VAD 触发静音捕获，遇广播语音频繁误触发导致大量活动信号丢失；且真实部署数据标注昂贵、收集窗口短，需契合实际工业部署约束（ADAPTIVE 项目经验启发）。

**模型架构：** 隐私防火墙为五层编码器-解码器的 U-Net 卷积自动编码器：编码端 5 个卷积块（每块两个 3×3 卷积+LeakyReLU+2×2 最大池化），首层 112 滤波器逐层翻倍，无 dropout；解码端镜像上采样并带对称跳连；输出 1×1 卷积+Tanh。输入 96×64 log-mel 语谱（25ms 窗/10ms hop/64 bins，约 1 秒），直接回归背景语谱，无需波形重建。活动识别用 VGGish 预训练提取 128 维嵌入（0.96s 滑窗、10 个聚合），SVM 多项式核（C=10, gamma=1, degree=5）。

**核心创新：** (1) 反向任务设定：将 DEMUCS 式语音增强 U-Net 倒置为"去除言语、保留背景"，直接回归背景分量 n̂；活动识别路径直接消费输出语谱，仅在 VAD 隐私评估时用 Griffin-Lim 重建波形，正常流程零波形重建。(2) 全合成训练：用 ESC-50/SINS 背景声叠加 LibriSpeech 语音，在 100%/80%/60%/40% 四种相对幅度电平下生成 8 个合成数据集（40% 对应衰减约 8dB），从根本上避免采集隐私敏感的居家语音标签。(3) 隐私-效用双指标评估框架：以 Silero VAD 检测语音占比为操作性隐私代理，以 AAC 精确率/召回率为效用指标，并通过 AudioHive 双阶段真实采集做分布外泛化验证。

**训练策略：** 复合损失 L1 谱重建 + 多分辨率 STFT 谱损失（谱收敛+对数幅度差）；网格搜索超参，最终选用首层 112 滤波器、无 dropout、LeakyReLU、batch 32、学习率 2.95×10⁻⁵、SGD 优化器、早停于 20 轮；70/30 分层划分，特征 L2 归一化。

### 📊 实验结果
**数据集**：ESC-50、SINS、LibriSpeech、AudioHive（自采集两阶段，10/12 名参与者）

**主要指标**：
- ESC-50 40% 语音电平去去除后精确率/召回率：85%/85%（无语音基线 84%/83%，语音污染时 81%/75%）
- VAD 可检测语音：ESC-50 100% 语音电平由 67.5% 降至 0%；SINS 各电平均为 0%
- 现成模型对比（ESC-50 100% 语音，残余 VAD）：Facebook Denoiser 6.55%、SepFormer 36.34%、ConvTasNet 47.21%
- SINS 40% 语音电平去除后：71%/77%（语音污染时 59%/58%）
- AudioHive 第二采集（含自然语音）：处理后 VAD 0%、精确率/召回率 76%/76%

**是否开源**：未开源。AudioHive 采集数据因含隐私敏感音频不可共享；模型代码未见公开发布。

### ⭐ 评分：7/10
评分理由：问题定义源于真实养老院部署痛点，动机扎实；全合成训练"去言语留背景"的反向 U-Net 设定规避了敏感家居语音采集，工程实用性强，且与三个现成基线做了系统性对比。不足之处：仅单次 70/30 划分无交叉验证与置信区间；VAD 仅作为操作性隐私代理，未以 ASR 词错误率或主观听测证明不可懂性；真实测试集仅含 6.8% 语音，重语音压力场景验证不足。综合创新性与实验充分度中等偏上，价值体现在复用性强（可嵌入现有声学感知系统前端）。

---

*Generated on 2026-09-04*