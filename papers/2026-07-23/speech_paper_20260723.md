# 2026-07-23 语音论文速递

**共收录**: 19 篇 | **语音大模型**: 5 篇 | **语音前端**: 14 篇

> 今日 arXiv 语音相关论文共命中 19 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

## [1] SimulS2ST-Omni: Data-Efficient Streaming Speech-to-Speech Translation via Explicit Trajectory Supervision

**arXiv ID** 2607.19810 | **方向** 语音大模型 / S2ST

**作者** He Rongshen, Liang Xinyu, Chen Dekun, Li Jiaqi, Chen Mingjie, Wu Zhizheng

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.19810 | **PDF** https://arxiv.org/pdf/2607.19810.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出SimulS2ST-Omni，一种支持流式的语音到语音翻译系统。现有方法通常受限于句子级监督或需要大量成对S2ST数据。本文仅使用约2000小时成对跨语言S2ST数据结合辅助监督即可实现句子级和长音频流式S2ST。通过两阶段Thinker-Talker因子分解解耦语言推理与声学预测，在RealSI和ACL60数据集上达到与最新闭源S2ST系统（如LiveInterpret 2.0）相当的ASR-BLEU性能。

### 🔧 技术方案

**模型架构** 基于语音语言模型的两阶段架构，核心为Thinker-Talker因子分解。Thinker负责语言推理，Talker负责密集声学预测，有效缓解模态干扰。

**核心创新** 联合文本-代码轨迹监督是本文核心创新，将目标文本和声学语义码调度为统一的承诺路径，消除了独立不稳定的声学侧发射控制器需求。结合辅助多任务训练，即使成对S2ST预算减少90%仍保持鲁棒性。

**训练策略** 训练配方包含三个层次：基础语音翻译学习（高延迟）、流式推理优化（GRPO）、两阶段因子分解。使用约2000小时成对跨语言S2ST数据。

### 📊 实验结果
**数据集** RealSI, ACL60/60-dev

**主要指标** ASR-BLEU达到与LiveInterpret 2.0相当水平，支持流式翻译。

**是否开源** 暂未开源代码

### ⭐ 评分：8/10
创新性显著，提出联合轨迹监督和两阶段因子分解，在低数据量条件下实现高质量流式S2ST。实验验证充分，与业界领先系统对齐。

---

## [2] Audio-Zero: Label-Free Self-Evolution for Fine-Grained Audio Reasoning

**arXiv ID** 2607.20166 | **方向** 语音大模型 / LALM

**作者** Tong Siqian, Li Xuan, Li Chaozhuo, Bi Baolong, Wang Yiwei, Cai Yujun, Liu Shenghua, Hao Chengpeng

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.20166 | **PDF** https://arxiv.org/pdf/2607.20166.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
大型音频语言模型（LALM）在细粒度音频推理（如识别事件顺序、重复和持续时间）方面仍存在挑战。现有后训练方法依赖昂贵的外部标签或仅提供粗粒度语义信号。本文提出Audio-Zero首个无标签自演进框架，通过构建来自无标签音频对比对的听觉自博弈游戏，模型首先生成描述所听内容的线索，然后通过推理线索间的不一致性识别异常听众。

### 🔧 技术方案

**模型架构** 基于Qwen2-Audio-7B-Instruct和Qwen2.5-Omni-7B构建听觉自博弈框架。

**核心创新** 听觉自博弈游戏机制：多数玩家听参考音频，一个异常听众听到细微变体。模型生成线索描述所听内容，通过推理不一致性识别异常听众。由于异常听众由构建已知，游戏提供可验证奖励无需标注答案。

**训练策略** 自博弈驱动的无监督训练，课程压力下自然涌现细粒度听觉描述。

### 📊 实验结果
**数据集** TREA, MMAU Test-mini, MMAR

**主要指标** Audio-Zero在细粒度音频推理任务上显著提升，同时保持广泛音频理解能力。演化分析显示游戏压力自然催生细粒度描述。

**是否开源** 暂未公开

### ⭐ 评分：8/10
创新性强，首个无标签自演进框架，为LALM细粒度推理提供新范式。实验验证全面。

---

## [3] Schrödinger Bridge Mamba for One-Step Speech Enhancement

**arXiv ID** 2510.16834 | **方向** 语音大模型 / 语音增强

**作者** Yang Jing, Wang Sirui, Wu Chao, Guo Lei, Fan Fan

**机构** 暂无（需从PDF提取）

**发布日期** 2025-10-19 | **论文** https://arxiv.org/abs/2510.16834 | **PDF** https://arxiv.org/pdf/2510.16834.pdf | **代码** 暂无 | **Demo** https://sbmse.github.io

### 📌 简介
本文提出Schrödinger Bridge Mamba（SBM），一种新型高效语音增强模型，整合了Schrödinger Bridge（SB）训练范式和Mamba架构。实验证明SBM在联合去噪和去混响任务上仅用一步推理就优于强生成式和判别式方法，多项指标达到最优，同时具有竞争性的实时因子支持流式推理。消融实验表明SB范式在不同架构上一致提升性能，Mamba在SB范式下表现优于Multi-Head Self-Attention和LSTM。

### 🔧 技术方案

**模型架构** 核心为Mamba状态空间模型结合Schrödinger Bridge训练范式。

**核心创新** 首次将Schrödinger Bridge引入语音增强，SB基于轨迹的培训相比传统映射方法显著提升性能。Mamba架构在SB范式下展现更强的性能优势。

**训练策略** 基于SB的训练范式，一步推理实现高质量增强。

### 📊 实验结果
**数据集** 语音增强标准数据集

**主要指标** 联合去噪和去混响任务上多项指标达到最优，实时因子具有竞争力。

**是否开源** Demo页面已开放

### ⭐ 评分：8/10
创新性显著，SB+Mamba组合在语音增强任务上效果突出。实验验证充分，有Demo可演示。

---

## [4] Simultaneous Speech-to-Speech Translation Without Aligned Data

**arXiv ID** 2602.11072 | **方向** 语音大模型 / S2ST

**作者** Labiausse Tom, Fabre Romain, Estève Yannick, Défossez Alexandre, Zeghidour Neil

**机构** 暂无（需从PDF提取）

**发布日期** 2026-02-11 | **论文** https://arxiv.org/abs/2602.11072 | **PDF** https://arxiv.org/pdf/2602.11072.pdf | **代码** https://github.com/kyutai-labs/hibiki-zero | **Demo** 暂无

### 📌 简介
同声传译需要将源语言语音实时翻译成目标语言并处理非单调词依赖。传统方法依赖词级对齐数据监督，这些数据难以大规模收集。本文提出Hibiki-Zero完全消除对词级对齐的需求。首先在句子级对齐数据上学习高延迟语音翻译，然后应用新型强化学习策略使用GRPO优化延迟同时保持翻译质量。

### 🔧 技术方案

**模型架构** Hibiki-Zero无需词级对齐，简化训练流程支持多语言无缝扩展。

**核心创新** 完全消除词级对齐需求这一根本性简化，使用RL（GRPO）优化延迟-质量权衡，可适配新输入语言仅需少于1000小时语音。

**训练策略** 两阶段：句子级对齐数据预训练 + GRPO强化学习优化延迟。

### 📊 实验结果
**数据集** X-to-English 5个任务，45h多语言评估基准

**主要指标** 翻译准确率、延迟、声音迁移、自然度均达最优。少于1000小时即可适配新语言。

**是否开源** 代码、模型权重、推理代码、评估基准均已发布

### ⭐ 评分：8/10
突破性工作，革新同声传译训练范式。开源精神可嘉，性能达到SOTA。

---

## [5] Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models

**arXiv ID** 2607.19932 | **方向** 语音大模型 / SLM

**作者** Feng Pengchao, Tan Chao-Hong, Chen Qian, Wang Wen, Li Xiangang, Chen Xie

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.19932 | **PDF** https://arxiv.org/pdf/2607.19932.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
口语语言模型（SLM）支持自然人机交互，但推理能力仍落后于文本大模型，尤其是在口语数学问答任务上。SLM基于纯语言化数学表达式进行推理，比符号文本更难理解。本文提出Efficient Chain-of-Modality Reasoning（ECoM Reasoning），首个将压缩推理引入SLM的框架。通过压缩文本组件使其同时作为语音引导和推理表示，ECoM在更少token预算下提升推理准确率。

### 🔧 技术方案

**模型架构** 基于压缩推理的SLM架构

**核心创新** 压缩推理机制：压缩文本组件同时作为语音引导和推理表示。渐进压缩课程策略从全形式推理逐步训练到压缩推理。

**训练策略** 渐进压缩课程学习，逐步从全形式推理过渡到压缩推理。

### 📊 实验结果
**数据集** 口语数学问答基准

**主要指标** 相比标准CoM无显式推理提升21%，相比CoM全推理轨迹提升3%，同时仅使用40%文本token。

**是否开源** 暂未公开

### ⭐ 评分：7/10
创新性好，压缩推理思路新颖，在口语数学推理任务上效果显著。实验验证较充分。

---

## 🎙️ 语音前端

## [6] StellarTTS: Sparse Temporal Embedding for Low-Latency and Robust Speech Synthesis

**arXiv ID** 2607.19859 | **方向** 语音前端 / TTS

**作者** Luo Kaicheng, Gong Xuefei, Sun Yutao, He Jinling, Hou Yujie, Xing Xiaoyang, Li Huiyan, Han Bing, Qian Yanmin

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.19859 | **PDF** https://arxiv.org/pdf/2607.19859.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文介绍StellarTTS，一种基于稀疏时间嵌入策略的新型移动端优化非自回归TTS框架。延迟、鲁棒性和韵律之间的权衡是TTS系统的关键挑战。自回归模型虽保真度高但慢且易出错；非自回归模型虽快但通常牺牲韵律自然性。StellarTTS支持对音素持续时间、发音和韵律的细粒度控制。83M参数的轻量级掩码生成式Transformer在稀疏时间嵌入条件下达到0.08的实时因子。

### 🔧 技术方案

**模型架构** 83M参数轻量级掩码生成式Transformer，稀疏时间嵌入策略。

**核心创新** 稀疏时间嵌入策略实现音素持续时间、发音和韵律的细粒度控制。语义感知codec促进高效单阶段解码。

**训练策略** 非自回归训练，优化RTF和韵律自然度平衡。

### 📊 实验结果
**数据集** 标准TTS评估基准

**主要指标** RTF=0.08，更低延迟和更强鲁棒性，音频质量、韵律自然度和说话人相似度保持竞争性能。

**是否开源** 暂未公开

### ⭐ 评分：7/10
工程性强，移动端优化TTS系统，稀疏嵌入策略有创新。实验验证较充分。

---

## [7] Layer-Wise Decision Fusion for Fake Audio Detection Using XLS-R

**arXiv ID** 2607.20023 | **方向** 语音前端 / 伪造音频检测

**作者** Xiao Yixuan, Vu Ngoc Thang

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.20023 | **PDF** https://arxiv.org/pdf/2607.20023.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
近期伪造音频检测方法利用大型语音模型获取稳健语音表示。这些模型通常非常深，提供多层表示。然而，现有工作通常仅依赖单层表示或特征融合提取 utterance 级表示进行决策，存在信息利用不足和特征崩溃风险。本文提出新型层-wise决策融合方法，在每层决策后进行融合，在In-the-Wild数据集上实现最佳跨数据集性能（EER 6.90%）。

### 🔧 技术方案

**模型架构** 基于XLS-R的深度模型，多层表示决策融合。

**核心创新** 层-wise决策融合：每层独立决策后进行融合，避免特征融合导致的信息丢失和特征崩溃。模型设计更透明，可进行详细分析揭示决策机制。

**训练策略** 多层决策联合训练，融合层优化。

### 📊 实验结果
**数据集** In-the-Wild

**主要指标** EER 6.90%，跨数据集性能最佳。

**是否开源** 暂未公开

### ⭐ 评分：7/10
伪造音频检测有新意，层-wise融合思路合理。实验验证跨数据集泛化性能。

---

## [8] Schrödinger Bridge Mamba for One-Step Speech Enhancement (重复， 见上)

---

## [9] LoRA-Tuned Large Language Models for Dementia Detection via Multi-View Speech-Derived Features

**arXiv ID** 2606.28445 | **方向** 语音前端 / 医疗语音

**作者** Park Jonghyeon, Jung Olivier Jiyoun, Oh Myungwoo

**机构** 暂无（需从PDF提取）

**发布日期** 2026-06-26 | **论文** https://arxiv.org/abs/2606.28445 | **PDF** https://arxiv.org/pdf/2606.28445.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
老年痴呆早期检测可实现及时干预。自发性语音反映认知障碍，提供非侵入性筛查。传统方法通常聚焦单一表示维度——如声学描述符、停顿建模、ASR转录或多模态融合——限制了对异构认知症状的综合推理。本文提出LoRA调优的大语言模型，对四个互补的语音衍生信号进行结构化多视角推理：带停顿标记的ASR转录、话语级主题线索、时间流利度统计和语音序列。

### 🔧 技术方案

**模型架构** LoRA调优的LLM，四视角语音特征统一提示编码。

**核心创新** 结构化多视角推理：四类语音衍生信号编码于统一提示中，单个LLM学习连贯决策函数无需模态特定编码器或后期融合。

**训练策略** LoRA参数高效调优，冻结主干网络。

### 📊 实验结果
**数据集** ADReSSo

**主要指标** 最佳模型F1=90.14%，消融确认每个视角的互补贡献。

**是否开源** 暂未公开

### ⭐ 评分：7/10
医疗语音应用价值高，多视角融合思路合理。F1达90%以上性能较好。

---

## [10] UtterTune: LoRA-Based Target-Language Pronunciation Edit and Control in Multilingual Text-to-Speech

**arXiv ID** 2508.09767 | **方向** 语音前端 / TTS

**作者** Kato Shuhei

**机构** 暂无（需从PDF提取）

**发布日期** 2025-08-13 | **论文** https://arxiv.org/abs/2508.09767 | **PDF** https://arxiv.org/pdf/2508.09767.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出UtterTune，一种基于大语言模型的轻量级多语言TTS系统目标语言发音控制方法。提高目标语言发音控制能力同时保持其他语言性能。LLM架构使TTS模型达到显著自然度，但准确建模字素到音素映射和韵律仍具挑战，尤其是当模型省略显式G2P模块直接处理最小编码文本时。UtterTune利用低秩适配在音素级别实现日语发音和音调重音控制，同时在零样本设置下保持自然度和说话人相似度。

### 🔧 技术方案

**模型架构** 基于LLM的多语言TTS + LoRA发音控制适配器

**核心创新** 轻量级LoRA适配实现音素级别发音和音调控制，无需微调整个模型。

**训练策略** LoRA参数高效训练，保持零样本能力。

### 📊 实验结果
**数据集** 日语TTS评估

**主要指标** 客观和主观评估确认有效性。

**是否开源** 暂未公开

### ⭐ 评分：7/10
LoRA应用于发音控制有创新性，针对日语的实验验证有效。

---

## [11] Scalable Keyword Spotting via Modular Network Expansion

**arXiv ID** 2607.19918 | **方向** 语音前端 / KWS

**作者** Khaymonenko Viktor, Saladukha Dzmitry, Rak Aliaksei, Rostov Alexander

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.19918 | **PDF** https://arxiv.org/pdf/2607.19918.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
嵌入式设备上的关键词检测（KWS）模型常需在部署后添加新关键词，但原始训练数据不可用且需避免现有触发器退化。本文方法在固定操作点下相比参数匹配的独立模型基线将平均新关键词误拒率从6.46降至4.37，优于参数高效调优基线（adapters, LoRA），同时在相同添加参数预算（≤10k）下使用更少MAC：16.34M vs 18.45M/20.52M。

### 🔧 技术方案

**模型架构** 参数封顶模块化扩展架构，冻结主干网络包括batch-normalization统计和核心分类器。

**核心创新** 参数封顶模块化扩展：仅训练轻量级扩展分支和新关键词头，保留核心logits、已发货输出和阈值。

**训练策略** 冻结基础网络，扩展分支独立训练。

### 📊 实验结果
**数据集** 嵌入式KWS评估

**主要指标** 新关键词FRR从6.46降至4.37，MAC 16.34M vs 18.45M。

**是否开源** 暂未公开

### ⭐ 评分：7/10
嵌入式KWS扩展性问题解决方案，参数和计算效率优化有效。

---

## [12] Cumsum-Composable Phase Transport for Low-Cost Streaming Keyword Spotting

**arXiv ID** 2607.20086 | **方向** 语音前端 / KWS

**作者** Godavarti Mahesh

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.20086 | **PDF** https://arxiv.org/pdf/2607.20086.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
状态空间序列模型因保持紧凑递归状态而吸引用于流式语音，但扫描式训练内核对短音频任务常数不利。本文研究cumsum可组合相位传输，一种用于KWS的流式原生时间层。每层将声学帧投影到复数通道，通过学习酉旋转传输，用前缀差分累积有限窗口，然后应用门控残差更新。相同前缀表示使普通cumsum精确批量训练和逐帧精确在线推理。

### 🔧 技术方案

**模型架构** 状态空间+ cumsum组合的流式KWS架构

**核心创新** cumsum可组合相位传输：酉旋转传输是关键约束，逆旋转范数为一，保持前缀项良好条件。

**训练策略** 前缀表示精确批量训练 + 逐帧在线推理。

### 📊 实验结果
**数据集** Google Speech Commands v2 (12标签)

**主要指标** 最佳单种子97.3%测试准确率，51.6K参数绑定模型同样97.3%，24.8K模型96.8%。

**是否开源** 暂未公开

### ⭐ 评分：7/10
流式KWS创新方案，cumsum技术路线新颖，性能和效率平衡好。

---

## [13] Multimodal Speaker Verification as a Threat to Speaker Anonymization

**arXiv ID** 2607.19636 | **方向** 语音前端 / 说话人验证

**作者** Garg Ashi, Aggazzotti Cristina, García-Perera Leibny Paola, Andrews Nicholas

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-22 | **论文** https://arxiv.org/abs/2607.19636 | **PDF** https://arxiv.org/pdf/2607.19636.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
大多数自动说话人验证（ASV）系统对单个话语操作，尽管现实世界交互通常由多个话语组成。随着语音积累，通过声学、韵律和语言线索可获得更丰富的说话人信息，可能挑战主要针对声音特征的说话人匿名化方法。本文研究多话语、多模态设置中的ASV，检查跨匿名化语音聚合信息是否影响隐私。

### 🔧 技术方案

**模型架构** 多话语多模态ASV系统

**核心创新** 研究多话语聚合对说话人匿名化的威胁，引入韵律和语言信息的多模态系统。

**训练策略** 多话语音频聚合 + 帧级聚合策略。

### 📊 实验结果
**数据集** 说话人匿名化评估

**主要指标** 5个匿名化话语下，音频+文本组合相比音频单独EER降低15%以上。

**是否开源** 暂未公开

### ⭐ 评分：7/10
隐私安全角度新颖，多模态聚合威胁分析有价值。实验验证充分。

---

## [14] A Novel Hybrid Deep Learning Technique for Speech Emotion Detection using Feature Engineering

**arXiv ID** 2507.07046 | **方向** 语音前端 / SER

**作者** Chowdhury Shahana Yasmin, Banik Bithi, Hoque Md Tamjidul, Banerjee Shreya

**机构** 暂无（需从PDF提取）

**发布日期** 2025-07-09 | **论文** https://arxiv.org/abs/2507.07046 | **PDF** https://arxiv.org/pdf/2507.07046.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音情感识别（SER）在人机交互和AI演进中扮演重要角色。本文提出的DCRF-BiLSTM模型识别七种情感：中性、快乐、悲伤、愤怒、恐惧、厌恶、惊讶，在五个数据集上训练：RAVDESS、TESS、SAVEE、EmoDB、Crema-D。模型在各数据集上达到高准确率，包括RAVDESS 97.83%、SAVEE 97.02%、CREMA-D 95.10%、TESS和EMO-DB均为100%。

### 🔧 技术方案

**模型架构** DCRF-BiLSTM混合深度学习模型

**核心创新** 特征工程结合BiLSTM，跨五个基准数据集评估。

**训练策略** 多数据集联合训练和单独训练策略。

### 📊 实验结果
**数据集** RAVDESS, TESS, SAVEE, EmoDB, Crema-D

**主要指标** RAVDESS 97.83%, SAVEE 97.02%, CREMA-D 95.10%, TESS 100%, EMO-DB 100%, 组合(R+T+S) 98.82%, 五数据集组合93.76%。

**是否开源** 暂未公开

### ⭐ 评分：6/10
SER任务实验充分，多数据集评估有价值。但创新性一般。

---

## [15] CAPS: A Cascaded Reconstruction Model to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension

**arXiv ID** 2607.19434 | **方向** 语音前端 / 语音增强

**作者** Tamiti Tarikul Islam, Dipto Sajid Fardin, Baja-Ricketts Luke, Vergano David, Barua Anomadarshi

**机构** 暂无（需从PDF提取）

**发布日期** 2026-07-21 | **论文** https://arxiv.org/abs/2607.19434 | **PDF** https://arxiv.org/pdf/2607.19434.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
可穿戴电脑戴在耳朵上。骨传导麦克风与气传导麦克风结合用于噪声条件下的多模态语音增强。现有模型未能探索联合降低ADC采样位分辨率和采样频率对功耗和音频质量的影响。CAPS在ADC中故意使用欠奈奎斯特采样和低分辨率，实现3.3x功耗降低。支持移动平台流式运行，推理时间1.36ms，内存占用11.04MB。

### 🔧 技术方案

**模型架构** 级联重建模型 + 欠奈奎斯特采样 + 带宽扩展

**核心创新** 子采样和低分辨率ADC实现3.3x功耗降低，带宽扩展重建宽频信号。

**训练策略** 级联重建优化功耗-质量权衡。

### 📊 实验结果
**数据集** 真实可穿戴设备评估

**主要指标** 3.3x功耗降低，推理时间1.36ms，内存11.04MB，实时语音清晰度保持。

**是否开源** 暂未公开

### ⭐ 评分：6/10
可穿戴设备功耗优化方案，实际应用价值明显。创新性中等。

---

## 📋 其他论文（快速浏览）

### 语音前端

## [16] The False Resonance: Emotion Embedding Similarity for Speech Generation Evaluation
**arXiv ID**: 2604.26347 | **评分**: 6/10
**链接**: https://arxiv.org/abs/2604.26347

## [17] Black-Box Optimization for Identifying and Inverting Audio Dynamic Range Control Effects
**arXiv ID**: 2607.19645 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.19645

## [18] Acoustic-to-Articulatory Inversion of Clean Speech Using an MRI-Trained Model
**arXiv ID**: 2603.11845 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2603.11845

## [19] Nonlinear Bias-Compensated Adaptive Filter and Its Application for Time-Series Prediction
**arXiv ID**: 2607.19902 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.19902

## [20] Improved Monitoring of Honey bee Colony Strength via Audio IoT Sensors
**arXiv ID**: 2607.20386 | **评分**: 4/10
**链接**: https://arxiv.org/abs/2607.20386

---

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*
