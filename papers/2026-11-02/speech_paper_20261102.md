# 2026-11-02 语音论文速递

**共收录**: 9 篇 | **语音大模型**: 6 篇 | **语音前端**: 3 篇

> 目标日期 2026-11-02（北京时间）arXiv 语音相关论文共命中 9 篇。
> 以下是按评分排序的结果。

---

## [1] VoxLock: Target-Speaker Extraction for Voice Agents Without an Enrollment Step

**arXiv ID**：2610.40727 | **方向**：语音前端

**作者**：Arbaz Siddiqui

**机构**：独立研究者（无机构挂靠）

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.40727 | **PDF**：https://arxiv.org/pdf/2610.40727.pdf | **代码**：https://github.com/arbazsiddiqui/voxlock | **Demo**：暂无（权重 https://huggingface.co/arbazsiddiqui/voxlock）

### 📌 简介
语音电话 agent 的 ASR 会把麦克风旁所有说话人转写进文本，降噪器天生保留语音而无济于事，Krisp/ai-coustics/Sanas 等商用"语音隔离"又闭源且按分钟/设备收费。本文在单张 NVIDIA L4 上微调公开因果 TSE 基线 REAL-TSE（27M 参数 BSRNN），改为直接使用通话自身截取的 3 秒语音作说话人线索，免注册，发布为 VoxLock。在 Krisp 265 条真实录音上 WER 达 4.95%（未处理 23.21%），冻结盲测 AMI 400 窗口将 WER 从 42.95% 压到 10.63%，8-bit 模型单 CPU 线程 77% 负载可跑实时通话。

### 🔧 技术方案

**问题背景：** 传统 TSE 依赖预录 enrollment 音频，而通话 agent 只有通话流本身；且 TSE 论文多在仿真混合上报告信号级指标，agent 真正关心的是识别器在真实音频上写出什么。商用隔离滤波器性能不公开、许可昂贵，缺少"开源 TSE 与商用产品按下游识别指标在真实录音上对比"的工作。

**模型架构：** 基于 WeSep/REAL-TSE 的因果 tfmap_context BSRNN：16 kHz、512 点 STFT、128 帧移、六段 band-split 块、单向序列建模，27M 参数，算法延迟 24 ms。语音样本以两条路径注入：通话谱帧对样本谱帧做 cross-attention 产生额外输入通道；分离带特征对样本的 ECAPA-TDNN 帧级特征做注意力后逐带相乘。

**核心创新：** (1) 免注册的通话内取样本：离线取前 15 s 中最响 3 s；流式先直通音频，累计够 3 s"高于近 2 s 最静帧 10 dB 的 10 ms 帧"即立样本并开启隔离，agent 只需输入一路音频。(2) 四阶段课程微调：S1 仿真通话、S2 引入 AMI 头带真实串扰、S3 30 s 长样本解决连续说话 40 s 内衰减 20 dB 问题、S4 随机距离+真实房间音纠正"保近端"捷径，逐阶段修正具体失效模式。(3) 以 ASR 端到端指标评测并工程化部署：双 ONNX 图（enroll 图每通话一次算出各带注意力 K/V，chunk 图携递归状态流式推理），int8 量化后单线程实时。

**训练策略：** 各阶段均最小化负 SI-SDR，AdamW（wd 0.01、梯度裁剪 5），训练含 ECAPA 分支全部权重；S1/S2 lr 1e-4（S2 末 1000 步退至 1e-5），S3/S4 为 3e-5。S1 4000 步：LibriSpeech 近场主说话人混 0–15 dB 较弱的 1–2 名背景，半数等距、否则 1.5–5 m 仿真房间，25% 过电话信道；S2 4000 步混入 40 场 AMI；S3 800 步、S4 400 步。单卡 L4，一次训练运行。

### 📊 实验结果
**数据集**：Krisp Voice Isolation Benchmark（265 条真实录音，办公/呼叫中心/电话场景）；AMI 134 窗口（5 会 7 人）与 400 窗口盲测集（11 会 16 人，评分前按哈希冻结）；识别器为 Parakeet TDT 0.6B。

**主要指标**：
- WER：Krisp 集 4.95%（流式 live() 5.15%），未处理 23.21%，REAL-TSE 初始检查点 9.81%
- Leak：0.11 词/分钟，85.3 分钟纯背景语音仅漏 9 个背景词（未处理 5674 词、Krisp Default 130 词）
- 盲测 AMI：WER 42.95%→10.63%，leak 98.19→1.17 词/分钟；错误人样本时 WER 升至 23.23%
- 关键对比：与 Krisp Default（5.30%）WER 无显著差异，显著低于 Krisp Lite（+1.26）、ai-coustics VF 2.2（+1.89/+1.96）、Sanas SE 1.0（+4.43）及 Hush/DeepFilterNet3/TIGER/SAM Audio 全部开源系统
- 部署：int8 单线程 80/40/20 ms 块分别耗 61%/77%/110% CPU，算法延迟 24 ms

**是否开源**：代码、ONNX 模型与逐文件分数开源 @ https://github.com/arbazsiddiqui/voxlock 与 HuggingFace

### ⭐ 评分：7/10
评分理由：实用价值突出——免注册 TSE 直击 voice agent 痛点，首次在真实录音上以下游 ASR 指标系统对比三家商用与多个开源系统，盲测集与部署负载数字完整可信。不足：方法属既有基线的课程式微调，创新偏工程；单训练运行、各阶段看前果调参而非受控消融；仅英语、依赖"主叫是最早最响说话人"假设，电话纯净场景反而引入 1.5 点 WER 损失。

---

## [2] Apriel Voice 27B Preview: An Open Model for Speech, Reasoning, and Tool Use

**arXiv ID**：2610.40738 | **方向**：语音大模型

**作者**：Aman Tiwari, Akshay Kalkunte, Akintunde Oladipo, Jash Shah, Tara Bogavelli, Hoang Nguyen, Nishanth Madhusudhan, Vishal Juneja 等

**机构**：Apriel 团队（论文文本未明确标注机构归属）

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.40738 | **PDF**：https://arxiv.org/pdf/2610.40738.pdf | **代码**：暂无（声明开源、已上线 Apriel Live 演示） | **Demo**：暂无

### 📌 简介
语音系统惯用 ASR-LLM-TTS 级联，把语音感知与推理、工具调用割裂，带来误差传播与高延迟。本文提出 Apriel Voice 27B Preview：在 Gemma 4 26B-A4B 骨干上串联冻结 Whisper large-v3-turbo 编码器与 47.7M 参数投影器，同一骨干统一语音理解、推理、对话与工具调用，保留文本/图像能力且 TTS 外部可替换。经两阶段适配、按源 CE/FKL 在线蒸馏与自动构造的语音条件对话数据，thinking 模式下 BBA 98.90、BFCL 81.13、SpeechMMLU-Pro-Voice 成功率 65.51%（延迟1.91s），为最强开源两级语音模型。

### 🔧 技术方案

**问题背景：** 识别准确不代表能遵循约束、调用正确工具，文本侧强能力也不保证请求以音频到达时推理依旧可靠。三段式级联与委托式语音系统把理解、推理、合成、轮次控制拆给不同组件，跨接口误差与延迟累积。

**模型架构：** 以 Gemma 4 26B-A4B（约 26B 总参、每 token 约 4B 激活的 MoE）为共享骨干；冻结 Whisper large-v3-turbo 输出 1280 维声学特征，Ultravox 风格投影器（8 帧堆叠、bias-free Linear 10240→4096、SwiGLU、投至 2816 维嵌入空间，共 47,722,496 参数）替换序列预留音频位置并与文本/图像交错；视觉塔与 bridge 冻结；TTS 外部可替换（评测用 Cartesia Sonic 3.5）。

**核心创新：** (1) 两阶段适配：阶段一冻结骨干仅训投影器，用多语转录/翻译/续写建立语音接口；阶段二联训投影器+骨干+MoE router，覆盖语音任务、工具交互与文本回放。(2) 按源自选 CE/FKL：每源独立选纯 CE、纯前向 KL 或组合，教师为冻结初始 checkpoint，仅训练期供全词表分布；混合损失可证等价于软标签 CE（目标=α·教师+(1-α)·one-hot），兼顾任务习得与能力保留。(3) 数据与系统工程：文本对话按 5 种 span 策略语音化、逐对话固定参考音色并做保真校验；本地 teacher worker 加 1-batch lookahead 重叠师生计算，融合全词表 CE/FKL 核降显存。

**训练策略：** 阶段一 18.17M 样本、2 epochs×32,213h 音频；阶段二 3 epochs×61,540h、52.6B token 曝光（7.9B 带 loss）；8 节点 16+48 张 H100、约 3 天；BF16、fused AdamW、零权重衰减、grad clip 1.0、20% warmup+余弦衰减。

### 📊 实验结果
**数据集**：LibriSpeech/GigaSpeech/FLEURS/Earnings21、CoVoST 2、BBA、Speech-BFCL、口语 IFEval/MT-Bench、EVA-Bench（639 例）、SpeechMMLU-Pro-Voice/-Bench、EnterpriseOps-Gym 及文本/图像评测集

**主要指标**：
- 语音推理（thinking，0-100 分制）：BBA 98.90、BFCL 81.13、IFEval 86.47、MT-Bench 86.19，8 项均值 85.84 为开源两级最优
- ASR：LibriSpeech test-clean/other WER 2.23%/5.15%，8 个基准平均 WER 12.61%
- ST：CoVoST 2 德法西→英平均 BLEU 42.87，仅差 GPT-realtime-2.1（43.72）0.85
- 代理任务：EVA-A 51.27%、EVA-X 74.13%；Voice pass@1 65.51%、均延迟 1.91s，距 GPT-realtime-2.1（69.82%）差 4.31 分
- 能力保持：较初始 Gemma 4 26B-A4B，MMLU-Pro -0.85、GPQA Diamond +2.6、MathVision +2.96

**是否开源**：论文称开源并上线 Apriel Live 演示，正文未给代码 URL，暂无

### ⭐ 评分：7/10
评分理由：单一骨干统一语音+推理+工具调用且评测广度罕见，开源两级显著领先，两阶段 CE/FKL 在线蒸馏配方与本地 teacher、融合全词表损失系统具工程借鉴价值；不足是缺逐组件消融、合成数据与蒸馏效果归因不明、多语言仅偏英语、内部与公开 harness 不完全可比。

---

## [3] Incongruence-Aware Evaluation of Multimodal Speech Emotion Recognition in Audio Large Language Models

**arXiv ID**：2610.40883 | **方向**：语音大模型

**作者**：Fengji Jing, Guy Laban

**机构**：Faculty of Science, The University of Hong Kong；Ben-Gurion University of the Negev

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.40883 | **PDF**：https://arxiv.org/pdf/2610.40883.pdf | **代码**：https://github.com/Guylaban/incongruence-aware-ser | **Demo**：暂无

### 📌 简介
语音交互大模型同时处理"说了什么"与"怎么说的"，但两类情感通道并不总是一致，这种跨模态不一致是否降低语音情感识别（SER）性能此前难以度量。本文将文本（NRC-VAD 词库）与音频（MSP-Podcast 微调的 wav2vec2-large VAD 回归器）映到共享 valence-arousal-dominance 空间，用两分量 GMM 把两模态距离转换为连续、无阈值的 incongruence 概率 p_incon，并经人工标注验证（Spearman 0.65）。在 eNTERFACE'05、MELD、CMU-MOSEI 上评测三个音频 LLM 发现：控制情感类别与特征空间几何后，不一致性在文本+音频条件下全面提高错误概率（调整 OR 1.15–1.25，FDR q≤0.022）；而相同 VAD 特征上的监督分类器反而在不一致样本上更准，说明代价源于模型对原始双通道证据的整合而非信号本身。

### 🔧 技术方案

**问题背景：** 多模态 SER 长期默认"加模态只会更好"，但心理语言学表明情绪声调与词义是可分离而自动交互的通道，冲突时人类观察者亦有系统性偏差。已有计算工作依赖人工构造的对抗性冲突或二值一致标签，缺少在共享情感空间中连续、经人类验证且被用作误差回归量的不一致度量；且常见做法用不同模型跑 text-only 与 multimodal 条件，悄悄混淆了模型与模态。

**模型架构：** 本文为评测框架而非新模型，流水线含：(1) 文本 VAD：NRC-VAD 词库取 [-1,1] 三元组按命中词均值；(2) 音频 VAD：wav2vec2-large 情感回归器输出 clip 至 [0,1] 后映射至 [-1,1]；(3) 评分模块：对训练集 Euclidean 距离拟合两分量 GMM，取大均值分量的后验责任为 p_incon；(4) 推理端：gpt-audio-1.5、Qwen2-Audio-7B-Instruct（扩展语料用 Qwen2.5-Omni）、GLM-4-Voice，两种提示（T1 零样本、T2 规则引导含冲突解决指令）与两种模态条件，输出 JSON 情感标签。

**核心创新：** (1) GMM 后验构造连续、无阈值的 incongruence 分数：不同于离散"标签冲突"判据，p_incon 不需要真值情感标签，仅凭公开词库即可在任意双模态语音数据集复现，且在三个语料上与人类主观判断单调相关（r_s=0.58–0.65）。(2) 范式分离（paradigm dissociation）：同一组六维 VAD 特征既作 LLM 误差预测因子，又训练 LR/SVM/MLP 判别基线；不一致对 LLM 有害、对监督分类器反而提升类别可分性，将失败定位到端到端原始多模态整合环节而非特征几何。(3) 模型-模态解耦协议：text-only 与 text+audio 均由同一 gpt-audio-1.5 完成以固定模型，再用纯文本模型 gpt-5.2 重跑 text-only 条件作受控消融，证明换"读稿模型"即可翻转效应符号。

**训练策略：** 框架本身不训练新模型：GMM 仅在训练划分距离上拟合防泄漏，对分量数、协方差形式、随机种子及 0.3–0.7 切分点均稳健；音频重采样 16 kHz，>30s 截断；推理贪心解码，失败样本按条件级有效性剔除，主要推断用聚类稳健逻辑回归并做 Benjamini-Hochberg FDR 校正。

### 📊 实验结果
**数据集**：eNTERFACE'05（1,287 条表演式语音，6 类）；MELD（老友记对话，7 类，test 2,610 条）；CMU-MOSEI（自发独白，6 类 Ekman argmax，4,211 条）

**主要指标**：
- GPT-audio 在 eNTERFACE text+audio（T2）accuracy 最高 0.907；pooled 调整后 OR 1.25 [1.04,1.49]，q=0.022
- 三语料 text+audio 调整 OR：eNTERFACE 1.25、MELD 1.15、MOSEI 1.20（q≤0.022）；text-only 方向跨语料不一致（eNTERFACE OR 0.85）
- 范式分离：同特征监督基线 LR/SVM/MLP accuracy 0.85/0.89/0.96，在不一致样本上更准（OR 0.80–0.82），与 LLM 受损方向相反
- 人类验证：eNTERFACE r_s=0.65、MELD 0.58、MOSEI 0.62；标注员间 κ=0.46
- 稳健性：p_incon 是六种候选分数中唯一免标签且三语料均显著者；换 WavLM 提取器、lexicon-free 重构均复现主结果（OR 1.26/1.11）

**是否开源**：代码 @ https://github.com/Guylaban/incongruence-aware-ser，发布逐样本 VAD 特征、p_incon 分数与 LLM 预测构成 benchmark

### ⭐ 评分：7/10
评分理由：贡献在评测方法学：统计设计成熟（聚类稳健回归、FDR、类内对照、双读者消融、第二提取器与词条无关重构），以自然发生的不一致性取代人工对抗冲突，三类语料上确立文本+音频误差惩罚，对语音智能体可靠性门控有直接价值。不足在于控制后效应量偏小（OR≈1.1–1.25），跨模型显著性主要由 GPT-audio 支撑，人类验证仅 2 名标注员，构念效度仍待加强。

---

## [4] From Transcription to Reformulation: Defining and Benchmarking Grounded Generative Speech Recognition

**arXiv ID**：2610.41292 | **方向**：语音大模型

**作者**：Qing Wang, Qihan Hu, Hang Lv, Yan Yang, Boqing Liu, Xuechao Zhu, Zehan Li, Hongjie Chen, Jian Kang, Jie Li, Yongxiang Li, Lei Xie

**机构**：星瀚AGI实验室，中国电信人工智能科技有限公司；西北工业大学计算机学院语音语言处理组（ASLP@NPU）

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.41292 | **PDF**：https://arxiv.org/pdf/2610.41292.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出GSR（Grounded Generative Speech Recognition）范式，将语音识别从恢复唯一字面转写重新定义为生成受声学证据支撑、按指令组织的文本，形式化接地改写空间G(Y,S)≥γ并建立四级改写层阶（字面转写/规范改写/语义改写/语音接地结构化）。据此构建首个评测基准GSR-Bench，覆盖精细会议转写、跨方言翻译、上下文化听写、语音摘要及静音/噪声声学幻觉五类赛道，并开发UniGSR（TeleASR编码器+Qwen3-4B）验证统一接地生成可行性。实验揭示转写保真与改写能力的"指标悖论"，并量化声学幻觉、无据生成与指令漂移等失效模式。

### 🔧 技术方案

**问题背景：** 传统ASR以WER/CER在单一参考转写下评估，但Speech-LLM已能做去冗余、标点恢复、ITN、结构化摘要等合法改写：精确匹配会错误惩罚这类 desirable 输出，也无法度量生成内容是否真正被语音接地。

**模型架构：** 理论框架定义接地改写空间 R(S)={Y|G(Y,S)≥γ}，结合指令P与先验集合C={对话史,声学环境,元数据}约束任务子空间；层级空间R3⊂R2⊂R1⊂R0由五维人类可理解度H(Y)（忠实度/覆盖/关键信息/简洁性/可读性）的门限参数化。系统侧UniGSR为指令跟随端到端Speech LLM：TeleASR语音编码器接Qwen3-4B，单一架构内经指令切换完成转写、润色、方言转普通话与摘要。

**核心创新：** (1) 首次形式化GSR范式：优化目标从argmax P(Y|S)的字面转写改为接地空间内 Y*=argmax P(Y|S,P,C)，明确"上下文只提供证据、不授权改写"的接地边界，幻觉即G(Y,S)<γ。(2) 层级可控的基准设计：GSR-Refine固定同一会议音频仅改任务级指令，隔离改写自由度与语音内容；GSR-PACE经Planner-Generator-Injector-Validator四阶段注入同音/拼音/实体混淆；GSR-Dialect覆盖粤/吴/西南官话/河南四方言；GSR-Summary从ContextASR-Bench保留700条实体密集长语音。(3) 评测框架超越精确匹配：LLM-as-a-Judge多维打分并经人类偏好研究验证，另设520段静音/音乐/噪声/弱语音压力测试独立度量接地可靠性。

**训练策略：** UniGSR由TeleASR编码器与Qwen3-4B经指令条件化端到端训练；GSR-PACE样本经语音相似度、语义可分性、上下文可消解性、结构一致性四条校验；GSR-Dialect用方言感知TTS合成并经母语者语义自然度与口音地道性双项≥4.0过滤；弱语音子集由AISHELL-1衰减叠加轻噪构造。

### 📊 实验结果
**数据集**：GSR-Refine（WenetSpeech TestMeeting）、GSR-PACE、GSR-Dialect（粤/吴/西南官话/河南）、GSR-Summary（约700条）、幻觉压力集520段

**主要指标**：
- GSR-Refine：UniGSR-Post以CER 54.44%代价换得最高LLM均分4.52，TeleASR仅CER 3.46%但均分4.16，直观呈现"指标悖论"
- GSR-PACE：热词上下文使UniGSR CER从8.52%降至4.79%，而用户画像上下文反升至17.00%
- GSR-Dialect：吴语LLM评分4.25对级联3.89，西南官话BLEU 0.619对0.526
- 接地可靠性：StepAudio-R1幻觉率HTR 5.4%最优；UniGSR HTR 15.0%、AHL 17.28
- GSR-Summary：Gemini 3.1 Pro五维领先（忠实度4.41/覆盖4.85），UniGSR忠实度仅3.14
- 关键对比：端到端UniGSR比ASR+LLM级联在方言语义裁判上一致占优，且可直接利用声学证据

**是否开源**：正文与摘要未提供代码或数据发布链接，暂无

### ⭐ 评分：7/10
评分理由：以严谨形式化填补了Speech-LLM改写输出"如何评测"的方法论空白，固定音频改指令的层级评测设计与声学幻觉压力测试极具巧思，指标悖论失效模式分析对系统选型有实用价值。不足：基准以中文场景为主、通用性待验证；UniGSR训练细节不透明且摘要显著弱于通用音频大模型；未开源限制复现。接近顶会水准的基准/范式工作。

---

## [5] Hierarchical Dual-Graph Retrieval for Long-form Audio Reasoning

**arXiv ID**：2610.41390 | **方向**：语音大模型

**作者**：Eunsang Lee, Taein Ju, Jiyoung Lee

**机构**：梨花女子大学人工智能与软件系（Ewha Womans University）

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.41390 | **PDF**：https://arxiv.org/pdf/2610.41390.pdf | **代码**：https://github.com/ewha-mmai/audiohelix | **Demo**：http://mmai.ewha.ac.kr/audiohelix/

### 📌 简介
大型音频语言模型（LALM）直接处理完整长录音时，难以捕捉分散在远距离片段中的查询相关内容，且开销巨大（35分钟录音约占52.5K token）。本文提出AudioHelix，首个面向LALM检索增强生成的层次化DualGraph框架：离线将长音频分块，在chunk、unit、语义概念三层构建声学-文本双模态节点与层次包含边；查询时从最相似的种子概念节点逐步传播相关性分数并经Personalized PageRank全局排序，仅检索少量音频单元作答。在TraceAV-Bench、MMAU-Pro、AudioMarathon上搭配三个主流LALM均超越全音频输入与现有RAG方法，推理延迟降低11.1倍。

### 🔧 技术方案

**问题背景：** LALM全量处理长音频超出有效上下文与计算预算；纯文本RAG基于ASR转录丢失情绪、语气、停顿等副语言线索，且音频转文本描述易幻觉；纯音频RAG则受静音与冗余干扰，朴素跨模态检索还受modality gap拖累。

**模型架构：** 离线将音频切为固定chunk（TraceAV 45s，其余30s），用Qwen2.5-Omni抽取每块ASR与事件caption；chunk再切为声学单元（5s/6s），预训练音频-文本对比编码器得声学单元节点，句子嵌入构成语言单元节点；声学单元经谱聚成10簇，质心为声学概念节点，LALM抽取文本概念构成语言概念节点；边按层次包含关系加权，每个声学单元连向最近top-3概念质心（阈值γ=0.85）。每份录音仅需构图一次。

**核心创新：** (1) DualGraph三级层次（chunk-/unit-/概念级）双模态图：不训练统一跨模态嵌入，文本与声学各自保留特征、仅在概念层互联，既保留副语言细节又绕开modality gap。(2) 查询时相关性传播检索：以与查询最相似的双模态概念节点为种子，经共享单元节点按余弦相似度传播，chunk级用对数压缩与首获分步数归一聚合，再做Personalized PageRank全局排序，取Top-K_c=15/8个chunk、每chunk取K_u=2个声学单元。(3) 证据时序重组装：检索单元与chunk文本按原时间序拼为 [{A_u*;D_c*};Q]；对不支持多音频的Audio-Flamingo-3，用带原始时间戳位置嵌入的单条合成录音统一承载。

**训练策略：** 完全免训练，全部使用现成组件（Qwen2.5-Omni、对比编码器、谱聚类与PPR）。8×RTX Pro 6000 上对平均32.9分钟录音索引耗时391s；超参：簇数10、γ=0.85、W_c=0.05、Top-K_c=15/8、K_u=2。

### 📊 实验结果
**数据集**：TraceAV-Bench（audio-centric reasoning 子集）、MMAU-Pro（long与ultra-long）、AudioMarathon（除ASR外全部任务）

**主要指标**：
- Qwen3-Omni-30B+AudioHelix：TraceAV 71.6、MMAU-Pro 67.2、AM 66.1，对比全音频71.3/66.1/63.7
- Audio-Flamingo-3：59.4/52.3/58.5，对比56.9/50.7/57.3；Voxtral-3B：50.6/56.5/57.9，MMAU-Pro提升15.6点
- 关键对比：在所有LALM×基准上全面超越PlanRAG-Audio与LinearRAG（领先6.0至32.8点）；推理延迟1.58s对17.52s（11.1倍），TFLOPs降17.6倍；NaïveRAG反使Voxtral降10.6点
- 消融：去掉任一模态均一致降分（AF-3 TraceAV 59.4→58.8/55.3），验证双模态互补

**是否开源**：代码已开源 @ https://github.com/ewha-mmai/audiohelix，项目页含定性演示

### ⭐ 评分：7/10
评分理由：首个面向LALM的层次化双模态图RAG，概念层互联缓解modality gap思路清晰，传播+PPR检索设计合理；3基准×3 LALM全覆盖、消融与效率分析充分，一致正增益说明模型无关性。不足在于对强基座增益有限（Qwen3-Omni在TraceAV仅+0.3），超参敏感性未充分展开，391s/录音索引成本对海量语料仍可观。

---

## [6] JYVA at BeTraC: Audio-Based Medical Note Generation with SOAP Section-Specific Queries

**arXiv ID**：2610.40695 | **方向**：语音大模型

**作者**：Youness Dkhissi, Valentin Vielzeuf, Antoine Caubrière, Jean-Emile Dartois

**机构**：Orange Research（法国 Cesson-Sévigné）

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.40695 | **PDF**：https://arxiv.org/pdf/2610.40695.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对语音大模型直接生成医学 SOAP 病历笔记时幻觉严重、长对话音频 token 冗余导致内容失真的问题，本文提出基于 Qwen2.5-Omni-3B 的分节感知架构：用轻量 Q-Former 学习 Subjective、Objective、Assessment&Plan 三组各 32 个分节专用查询，将医患对话音频压缩为 96 个临床 token 再馈入 LLM 解码器。系统在 BeTraC 挑战赛轻量组排名第 4，官方测试集 Concept F1 达 0.5005，远超基线 0.245；启发式分析显示幻觉率从微调基线的 15.5% 降至 7.5%，在困难音频条件下也更稳定。

### 🔧 技术方案

**问题背景：** LLM 语音摘要易产生无依据内容，医患对话不流利、结构松散且极长，全量音频 token 直入 decoder 加剧幻觉与重复；现有自由格式摘要方法忽略 SOAP 笔记固有的分节结构及各节所需证据类型的差异。

**模型架构：** 保留 Qwen2.5-Omni-3B 的语音塔、音频投影与 thinker LLM，移除视觉与 TTS 模块。核心是 2 层 Q-Former 适配器（96 个可学习查询、8 注意力头、dropout 0.1），经 cross-attention 从冻结语音塔嵌入中抽取三组紧凑临床表示；thinker 上加 LoRA（rank 16、α=32）。Stage 2 冻结 Q-Former、恢复原生音频投影，将 96 个 Q-Former token 作为前缀拼接原生音频 token 之后输入 thinker。

**核心创新：** (1) SOAP 分节专用查询：32 个查询分别绑定 S/O/AP 节，配合分节辅助损失，为信息抽取注入结构归纳偏置。(2) 两阶段解冻策略：Stage 1 用 Q-Former 替换原生投影并联合 LoRA 训练（全笔记损失+医学概念列表损失+分节损失），Stage 2 冻结 Q-Former、恢复原生投影、仅训新 LoRA，兼顾压缩表示与原生声学细节。(3) 端到端无说话人分离：不依赖 diarization 或角色掩码，辅以 beam search、重复惩罚、5-gram 阻断及确定性后处理抑制幻觉。

**训练策略：** BeTraC 官方训练子集，单张 H100，batch size 1×梯度累积 8、6 epochs，余弦学习率衰减、5% warmup；LoRA lr 5e-5，Q-Former lr 1e-4；按验证损失选模型。推理 16 beam、最长 512 token、长度惩罚 1.0、重复惩罚 1.2。

### 📊 实验结果
**数据集**：BeTraC 官方 SynthDoPaCo 合成医患对话，含 Mock、Realistic 及聚合评测集

**主要指标**：
- Concept F1（官方集）：0.5005（基线 0.245，冠军 0.543）；聚合 0.486
- 幻觉率 Hallu：7.5%（微调基线 15.5%），无依据 claim 0.4%、无依据数字 7.5%
- 关键对比：较微调基线 Concept F1 +0.04；困难语音子集上 0.51→0.48，基线 0.47→0.31；77.5% 验证对话优于微调基线，轻量组排名第 4

**是否开源**：暂无（医学概念抽取复用组织方开源 matcher）

### ⭐ 评分：6/10
评分理由：将 Q-Former 查询与 SOAP 分节结构显式对齐是简洁有效的归纳偏置设计，两阶段训练与分节辅助损失有工程价值；幻觉启发式诊断比单一 Concept F1 更能说明可靠性收益。不足是挑战赛系统级增量工作，仅在单一合成基准验证，Realistic 子集明显掉点，未开源，可复现性与通用性受限。

---

## [7] From prediction error to sparse events: Biologically inspired signed-dyadic coding for Mandarin keyword spotting

**arXiv ID**：2610.41381 | **方向**：语音前端

**作者**：Zijian Zhou, Rui Liu, Rongxiang Nie, Rui Ma, Ziyao Zhang, Xin Du

**机构**：Sivy Limited（中国杭州）；英国剑桥大学卡文迪许实验室（Xin Du，通讯作者）

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.41381 | **PDF**：https://arxiv.org/pdf/2610.41381.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对脉冲神经网络关键词唤醒中稠密声学接口对时间相关帧反复触发访存与计算的问题，论文受预测处理与感觉适应启发，提出可学习的预测符号二进制事件编码（PG）：每个输入通道维护本地泄漏预测，仅当残差超过学习阈值时发出携带符号与2的幂幅值的事件，接收端用移位加法免乘法重建。在自建中文关键词集（4545条、5类）上，整数推理下仅输入端放置PG的INPUT-PG达90.00%准确率，平均SRAM读取降33.87%、推理周期降32.77%，Sky130HD布线实测评得增量推理能耗降39.49%，为低功耗连续语音处理提供了硬件事件接口。

### 🔧 技术方案

**问题背景：** 连续KWS逐帧处理log-mel特征，相邻帧高度相关，但稠密输入接口仍传输每一帧并重复触发存储访问与下游计算，即使隐层活动稀疏也产生额外功耗。现有事件编码（rate、TTFS、delta类）各有取舍，且对已阈值化的隐层脉冲再做编码会同时为上升/下降沿新增事件，故编码放置位置与编码本身同等重要。

**模型架构：** 前端为PG事件编码器加Deep-SNN/LIF-TCN分类器。PG对40维log-mel输入按地址维护共享预测状态，超阈残差以"地址+有效位+符号+指数"报文发出，指数取自6个二进制槽位；解码器做符号扩展、移位选择与累加并更新预测状态，全程定点、无乘法器与查找表。主干为Deep-SNN（线性层+3层streaming LIF，109,841参数）与LIF-TCN（4个因果残差Conv1d/LIF块，膨胀1/2/4/8，99,284参数）。三种部署：DIRECT、INPUT-PG（仅声学输入）、ALL-PG。

**核心创新：** (1) PG是可端到端训练有损事件编码：尺度、归一化阈值、预测泄漏系数均为可学习参数，硬门控与指数选择采用直通估计回传梯度，部署时冻结为定点常数。(2) 符号二进制载荷：事件仅含符号与有限2的幂幅值，保留变化方向与粗粒度幅值层级，解码仅需移位与加减，指数槽数/尺度/阈值/泄漏构成精度-活动-能耗可调旋钮。(3) 选择性放置原则："预期收益超过分组、状态与解码器开销才在该边界放PG"；预测只应放在尚有时间冗余的声学输入端，隐层LIF已是二值稀疏事件，ALL-PG反而增加流量。

**训练策略：** 语料4545条/101说话人/5关键词，3150/675/720划分且跨集无说话人重叠；48kHz→16kHz，40通道log-mel。三种部署各自从零训练50轮，种子7/17/27，batch 128，AdamW lr 0.001。整数推理冻结seed-17权重（特征/状态15位、权重9位、膜累积24位）；布线评估在Sky130HD、25°C、1.8V、10MHz下对固定clip做门级活动仿真与OpenROAD功耗标注。

### 📊 实验结果
**数据集**：自建中文关键词语音集（4545条/101人/5类，16kHz、40维log-mel，测试720条）

**主要指标**：
- 整数推理准确率：INPUT-PG 90.00% vs DIRECT 89.58%、ALL-PG 89.58%；输入活动-71.67%，SRAM读取-33.87%，推理周期-32.77%
- 布线能耗：INPUT-PG增量resident能耗20,122.6μJ vs DIRECT 33,253.0μJ（-39.49%）；瞬时动态功耗+1.23%、面积+1.00%
- 从零训练（3种子均值）：Deep-SNN INPUT-PG 88.47%（DIRECT 88.84%），输入事件降71.74%、全通信代理降20.07%；LIF-TCN 88.10%对88.75%
- 关键对比：RATE-T8全代理能耗+33.42%、TTFS-T8降14.69%；INPUT-PG全通信负载与resident能耗均最低

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由：把预测编码落地为免乘法定点事件接口的思路有新意，"选择性放置"结论对SNN加速器前端设计有实用价值，软件指标、整数推理、Sky130HD布线三轨测量口径清晰，RTL-软件一致性校验严谨。局限在仅自建5类关键词小语料，布线能耗仅一条固定clip，精度差不显著，未与真实神经形态硬件对比，代码未开源。

---

## [8] Scalable Audio-LLM System for Speech MOS Evaluation: A Diagnostic Case Study and Adaptation Roadmap

**arXiv ID**：2610.41539 | **方向**：语音前端

**作者**：Dimitrios Kokkinis, Panagiotis Kakoulidis, Nikolaos Ellinas, Chrysovalanti Lymperi, Alexandra Vioni, Georgios Vardaxoglou, Iakovi Alexiou, Myrsini Christidou, Jeasung Lee, Gunu Jho, Inchul Hwang, Pirros Tsiakoulis, Aimilios Chalamandaris

**机构**：Innoetics, Samsung Electronics（希腊）；Mobile eXperience Business, Samsung Electronics（韩国）

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.41539 | **PDF**：https://arxiv.org/pdf/2610.41539.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对企业级TTS持续集成中人工MOS评测成本高、周转慢、难扩展的问题，本文提出基于Qwen2-Audio-7B-Instruct的可扩展离线语音质量评估路线。先以直接打分、few-shot、成对比较、CoT四种零样本提示策略做系统审计，暴露分数压缩与位置偏置；再从SOMOS提取语流与音高变化两个低层声学维度构造诊断基准，定位模型感知盲区；最终经4-bit量化+LoRA微调仅0.53%参数，与人类MOS的Pearson相关达0.6506、SRCC 0.6582，超过基线UTMOSv2（0.4310/0.4193）。

### 🔧 技术方案

**问题背景：** 人耳MOS金标准开销大、需数天周转，无法覆盖CI/CD中数千条离线合成音频；UTMOS/NISQA等传统回归模型只输出单一分数、诊断价值有限；Audio-LLM能否开箱即用作为质量门禁尚未验证。

**模型架构：** 系统分零样本探测、诊断评估、参数高效对齐三阶段。推理时输入候选TTS音频批次与固定指令prompt，直接返回标量MOS。主干为Qwen2-Audio-7B-Instruct，4-bit量化加载并外挂LoRA权重压低显存；两阶段缓解方案则由音频LLM生成分维度定性描述，再由Llama-3-8B映射为数值分。

**核心创新：** (1) 零样本审计：四种提示下模型均在评转写准确性而非声学保真，分数恒>4.5；25条few-shot下复述上下文分值，成对比较确定性偏向样本A，证明Audio-LLM不可直接作为发布门禁。(2) SOMOS驱动诊断基准：以字数/时长比划分语速档，网格搜索优化权重合成expressivity指标=0.46·音高标准差+0.05·基频过零率+0.49·音高速度并离散为三档，据此建三项各600样本的3类选择题基准，暴露低层感知盲区。(3) 参数高效LoRA对齐：直接数值标量目标取代文本模板，不做类别平衡的全量训练优于平衡采样，仅训0.53%参数即把相关性从近零提升至0.65并超UTMOS。

**训练策略：** SOMOS训练集构造指令三元组{音频,prompt,目标分}，目标MOS取两位小数；LoRA r=16、α分别为16/32；4-bit量化、单GPU、batch size 2、lr 1e-4、1 epoch；基准评测temperature 0.7。

### 📊 实验结果
**数据集**：SOMOS（20K条LJ Speech声音、200个TTS系统生成的合成语音，AMT众包1-5分MOS，英文）；诊断基准三项各600样本。

**主要指标**：
- 零样本两阶段映射最优Pearson r=0.2467，原始直接打分仅-0.0312
- 诊断基准宏平均F1：Qwen2-Audio语流21.9%、表达力26.5%、内容对齐29.5%；Audio Flamingo 3为16.9%/27.4%/36.5%
- LoRA微调最优配置：Pearson 0.6506、SRCC 0.6582（utterance级）
- 关键对比：base model相关0.0028，UTMOSv2为0.4310/0.4193，微调后SRCC相对UTMOSv2提升+0.239

**是否开源**：正文未提供代码或模型发布链接，暂无。

### ⭐ 评分：6/10
评分理由：企业语音QA工程case study，"零样本审计→归因到低层感知盲区→LoRA对齐"链条完整，"数值目标优于文本模板、数据量优于类别平衡"等消融结论实操指导性强；但仅英文SOMOS域内评测、单一7B主干，0.65相关性距生产门禁尚远，诊断基准依赖手工声学特征，创新性与实验广度有限。

---

## [9] Nedimo: An Evidence-Grounded Multilingual Pipeline for AI-Generated Sleep Stories

**arXiv ID**：2610.40970 | **方向**：语音大模型

**作者**：Georgios Makridis, Stefanos Kampouris

**机构**：皮赖乌斯大学（University of Piraeus）数字系统系

**发布日期**：2026-11-02 | **论文**：https://arxiv.org/abs/2610.40970 | **PDF**：https://arxiv.org/pdf/2610.40970.pdf | **代码**：暂无 | **Demo**：https://nedimo.com

### 📌 简介
本文提出 Nedimo——证据导向的多语种 AI 助眠故事生成与语音合成管线，针对普通媒体目标（完播、留存、新颖性）与助眠"入睡脱离注意力"目标相悖、且睡前故事临床证据参差（USleep RCT n=495 对主动对照无 superiority，g=0.12）的问题。系统把证据转化为保守工程约束：确定性规划、四阶段注意力递减、结构化与词法校验、限定重试加隔离，以及 provider 无关 TTS 与 EBU R128 母带发布门。试点单次运行 5 种语言故事全部通过阻断校验与响度门（-22 LUFS±0.3 LU），但非英语渲染时长偏差达 -13%~-38%。论文明确不声称临床疗效。

### 🔧 技术方案

**问题背景：** 生成式音频可量产个性化睡前内容，但娱乐式优化目标与助眠意图冲突——听完并续播恰恰说明用户未入睡；同时睡前旁白对成人睡眠的直接证据矛盾。现有约束生成与 TTS 系统无法同时保证低唤醒叙事、时长预算与声学合规。

**模型架构：** 端到端流程：确定性规划器按"日期-语言"解析 slot 记录（目标时长、参与度档位、故事域、视角、语音配置等，幂等可复现）→ 组合提示契约（机读front matter+叙述正文+合成注记）→ LLM 生成 → 分层校验器 → 失败一次定向重试后隔离 → provider 适配器（SSML/locale/发音替换，按段落缓存拼接）→ 重采样 44.1kHz，FFmpeg loudnorm 两遍（-22 LUFS、-3 dBTP、LRA 4）+150s淡出 → AAC 96kb/s → 对编码文件复测发布门。时长规划为 W* = T·r_s/s̄。

**核心创新：** (1) 证据到需求映射：将 6 项临床研究逐条转成可验证控制（无后果性剧情、禁用睡眠指令词、关自动连播、无连续打卡激励），并把"不承诺疗效"写入提示、界面文案与校验规则。(2) 四阶段注意力递减合同：Arrival/Exploration/Settling/Fade 按 10%/55%/20%/15% 切分词索引，服务端按实际字数重算边界。(3) 纵深防御护栏：阻断项（时长偏差>8%、问号感叹号、高唤醒词、悬念、听众自称）与顾问项分层，叠加编码后文件响度复测门，底层失败不可被上层流畅文本补偿。

**训练策略：** 无模型训练，属管线/系统工程。关键固定阈值：音节估计时长 ±8% 阻断、±7% 警告、目标 20 min/夜/语言；已部署 en/de/fr/hi/ja 五语生产目录；试点用同一 ElevenLabs 音色；日语 mora 级时长校验为已知未实现缺口。

### 📊 实验结果
**数据集**：单次夜间运行（2026-10-12）发布的 5 篇故事，en/de/fr/hi/ja 各一 20 分钟槽；属 pilot。

**主要指标**：
- 阻断校验通过率：5/5 无警告通过脚本与母带门
- 综合响度：全部在 -22 LUFS 目标 0.3 LU 内（-22.17~-22.28）
- 真峰值 -2.68~-2.98 dBTP、LRA 3.0–4.4 LU（4/5 超 4 LU 目标但≤4.5 门限）
- 渲染时长误差：en +2.0%、de +2.9%、fr -13.0%、ja -24.1%、hi -38.2%

**是否开源**：代码未开源；产品（Web+Android/iOS）已上线，论文自报无固定语料一致性结果与临床数据。

### ⭐ 评分：5/10
评分理由：作为系统论文，证据映射与纵深护栏设计严谨、诚实标注实现边界；但仅 5 篇 pilot，无任何临床或感知对比结果，多语时长估计器最大偏差 -38% 的核心缺陷仅被承认而未解决。对睡眠音频工程化有参考价值，学术贡献增量有限。

*Subagents used for reading: 9* | Generated on 2026-11-02 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
