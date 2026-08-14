# 2026-07-31 语音论文速递

**共收录**: 4 篇 | **语音大模型**: 3 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 4 篇。

---

## 语音大模型

---

## [1] WeSep: A Modular and Cue-Composable Framework for Target Speaker Extraction

**arXiv ID**：2607.27436 | **方向**：语音大模型

**作者**：Ke Zhang, Xiaoyang Yu, Haoyu Li, Shuai Wang, Shuhan Zhang, Haizhou Li

**机构**：SAI, The Chinese University of Hong Kong, Shenzhen; Nanjing University; Shenzhen Loop Area Institute

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.27436 | **PDF**：https://arxiv.org/pdf/2607.27436.pdf | **代码**：https://github.com/wenet-e2e/WeSep | **Demo**：暂无

### 📌 简介
目标说话人提取（TSE）在给定辅助线索（如说话人注册、空间方向、视频信号或文本描述）的情况下从混合语音中分离目标说话人。现有系统通常针对单一线索类型设计，当线索可用性随场景动态变化时缺乏灵活性。本文提出WeSep统一框架，将TSE重新表述为异构线索条件学习问题，通过标准化接口解耦线索模块与分离器骨干网，支持可配置的线索注入和灵活的多模态集成。在Libri2Mix上，文本关键词线索DAE-TSE达到SI-SDRi 16.45 dB和98.98%准确率，多线索联合（说话人+空间）达到SI-SDRi 14.67 dB和99.05%准确率，且因果模式可实现32ms理论延迟。

### 🔧 技术方案

**问题背景：** 目标说话人提取（TSE）依赖辅助线索指定目标说话人，但现有系统针对特定线索类型定制架构和训练流程，难以扩展到新线索或多线索组合。实际场景中线索可用性动态变化（注册语音可能不匹配当前状态、空间线索依赖稳定定位、视觉信号可能退化），但缺乏统一框架来系统研究异构图线索条件下的提取行为。

**模型架构：** 模块化四层架构：(1) 数据抽象层，定义mix-target对和基于ID的线索索引；(2) 线索前端（Cue Frontend），包含enrollment特征（speaker embedding, USEF, TF-Map, Contextual embedding）、空间特征（IPD, STFT, SDF, CDF）、视觉特征（MuSE风格viseme嵌入）、文本特征（DAE-TSE音素编码器）；(3) 可配置分离器骨干网，支持BSRNN（32子带，128维/子带，6层192维双向LSTM）、Conv-TasNet、TF-GridNet、NBC2等；(4) 顶层组合，通过标准化融合接口注入线索。BSRNN为默认分离器，150 epoch训练，Adam优化器，3秒片段。

**核心创新：** (1) 将TSE重新表述为异构线索条件学习问题，统一单线索和多线索设置，支持样本级线索可用性变化（如30%样本缺失enrollment，30%缺失空间线索）；(2) 结构化模内线索建模，在统一分离器下可控研究不同线索粒度和组合，揭示enrollment特征中频谱级（USEF+Contextual 16.56 dB，98.05%）优于话语级（Speaker Emb. 13.17 dB，92.08%）；(3) 可组合多线索集成，即插即用组合多个线索无需架构重设计，多线索（空间+说话人）优于单线索（空间14.24 dB vs 联合14.67 dB）；(4) 样本级异构训练管道，零填充策略处理缺失线索，确保训练稳定且无性能崩溃。

**训练策略：** 负尺度不变信噪比（SI-SNR）损失函数，所有实验使用相同学习率调度以确保公平比较。因果模式通过将分离器和特征提取器转为因果模式实现，可导出ONNX并在流式TSE管线中验证。

### 📊 实验结果
**数据集**：Libri2Mix-100 (min.)、LibriSpeech+100 Nonspeech Sounds多通道混响数据集、VoxCeleb2-mix

**主要指标**：
- 说话人注册（BSRNN，非因果）：USEF+Contextual达SI-SDRi 16.56 dB，准确率98.05%
- 说话人注册（BSRNN，因果）：USEF+Contextual达SI-SDRi 14.15 dB，准确率95.93%
- 空间线索（BSRNN）：手工特征（CDF+SDF+IPD+STFT）SI-SDRi 14.24 dB，准确率98.08%
- 空间线索（NBC2）：手工特征SI-SDRi 17.49 dB，准确率98.13%
- 文本关键词（BSRNN）：DAE-TSE SI-SDRi 16.45 dB，准确率98.98%
- 视觉线索（BSRNN）：SI-SDRi 12.81 dB，准确率99.10%
- 多线索联合（空间+说话人）：SI-SDRi 14.67 dB，准确率99.05%
- 异构训练（缺失线索）：空间+说话人同时可用时SI-SDRi 13.51 dB，仅空间时12.61 dB，仅说话人时10.01 dB

**是否开源**：https://github.com/wenet-e2e/WeSep

### ⭐ 评分：8/10
评分理由：模块化设计思路新颖，从架构层面解决了TSE中线索可用性动态变化的实际问题。实验覆盖四种线索类型及其组合，证据充分。因果模式验证了部署可行性。但核心创新在于框架而非新的分离架构，性能提升主要来自多线索组合而非单一模块突破。

---

## [2] Enhancing Law-Enforcement Audio Transcription: A LoRA-Based Adaptation of Whisper for BWC Footage

**arXiv ID**：2607.27245 | **方向**：语音大模型

**作者**：Vivek Senthil, Zhiqiang Tao, Ernest Fokoué

**机构**：Rochester Institute of Technology (RIT), USA

**发布日期**：2026-07-27 | **论文**：https://arxiv.org/abs/2607.27245 | **PDF**：https://arxiv.org/pdf/2607.27245.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
执法机构随身摄像头（BWC）的音频转录面临极端环境噪声和专业执法词汇（如"10-52"、"Mirandize"）的挑战。本文使用Low-Rank Adaptation（LoRA）对OpenAI Whisper-base模型进行参数高效微调，仅训练0.3%的参数（294,912个可训练参数），在53个BWC视频数据集上实现了39.7%的WER相对降低（从0.6194降至0.3733）。消融实验表明低秩配置（r=8）最优，更高秩（r=16, 32）因过拟合噪声分布导致性能下降。

### 🔧 技术方案

**问题背景：** 执法机构管理PB级BWC录像，人工转录成本高昂。标准ASR模型（如Whisper）在执法环境中失败率高，原因有二：(1) 极端环境噪声（交通、人群、风噪）；(2) 专业词汇（如"10-52"、"Mirandize"、"Signal 13"）不在训练语料中，导致零样本下严重语义漂移。

**模型架构：** 基于Whisper-base Transformer Encoder-Decoder架构（~99M参数），输入为log-Mel频谱图，输出为文本token。LoRA应用于query和value投影层（[q_proj, v_proj]），权重更新W = BA，A∈R^(r×k)，B∈R^(d×r)。初始化策略：B=0，A从高斯分布采样，确保训练开始时W=0（保持零样本性能）。

**核心创新：** (1) 将LoRA（参数高效微调）首次应用于执法BWC领域的ASR适配，仅训练0.3%参数（294,912 vs 全微调99,148,800）；(2) 揭示了低秩（r=8）优于高秩（r=32）的反直觉发现——高秩导致对严重噪声伪影的过拟合，低秩有效捕获领域特定声学模式；(3) 在消费级GPU（NVIDIA 4GB GTX）上使用8-bit量化和梯度检查点实现训练，但主要实验在A100 20GB上进行。

**训练策略：** LoRA rank r=8, 16, 32，缩放因子α=32，dropout率0.05。数据集：294个视频经筛选保留53个BWC视频，8:1:1分割（42训练，5验证，6测试）。WER（S+D+I）/N作为评估指标。训练在RIT Research Computing的A100 20GB GPU上进行。

### 📊 实验结果
**数据集**：53个BWC视频（42训练/5验证/6测试），来自公开广播内容

**主要指标**：
- Zero-shot Whisper-base：WER 0.6194
- 全参数微调：WER 0.5874
- LoRA r=8：WER 0.3733（39.7%相对降低，最优）
- LoRA r=16：WER 0.3793
- LoRA r=32：WER 0.3848
- 场景敏感性：简单交通拦截WER 0.378，复杂事故现场WER 0.789

**是否开源**：暂未开源

### ⭐ 评分：7/10
评分理由：工作聚焦特定领域，LoRA微调方案实用性强，39.7%相对WER降低具有实际应用价值。低秩最优的发现对噪声场景下的PEFT有参考意义。但数据集仅53个视频，规模较小；场景WER方差大（0.378-0.789），在复杂场景下性能仍不理想。

---

## [3] Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments with Turn Action GRPO

**arXiv ID**：2607.27756 | **方向**：语音大模型

**作者**：Xilin Jiang, Riki Shimizu, Sukru Samet Dindar, Junkai Wu, Zhongweiyang Xu, Nima Mesgarani

**机构**：Columbia University; University of Washington; University of Illinois Urbana-Champaign

**发布日期**：2026-07-30 | **论文**：https://arxiv.org/abs/2607.27756 | **PDF**：https://arxiv.org/pdf/2607.27756.pdf | **代码**：https://github.com/xi-j/Cocktail-Talker | **Demo**：暂无

### 📌 简介
现实社交环境中语音助手需在多人对话和背景噪音中决定是否响应、继续倾听还是忽略。本文提出Cocktail-Talker，基于Qwen2.5-Omni-7B的语音LLM框架，通过三种行动token（respond/listen/ignore）建模助手的对话行为。使用Cocktail-DialogGen数据管道模拟14,400个独特对话、72,000个带噪音频混合物（约1,280小时），涵盖18种seen和10种unseen环境。SFT+GRPO训练后，在seen环境上达到93.1%的宏F1（决策准确率），在unseen环境上达到93.3%，显著超越Kimi-Audio（47.6%）、Qwen3-Omni（49.1%）等基线。

### 🔧 技术方案

**问题背景：** 现有语音对话系统假设干净的双人交互环境，用户话语直接面向助手。但真实社交场景中多人同时说话、背景噪音存在，每个话语可能面向助手、其他说话人或完全无关。助手需要决定是否回应、继续倾听还是忽略。这是一个多说话人-单助手的口语对话建模问题，目前缺乏系统性解决方案。

**模型架构：** 基于Qwen2.5-Omni-7B的thinker-talker架构。thinker为Transformer语言模型处理音频输入和生成文本回复，talker为流式TTS解码器合成语音。输入包含文本prompt（说话人元数据：性别、名字、角色、对话风格）和音频输入（未分离的完整混合音频）。输出为三种action token之一：<|respond|>后跟回复文本，<|listen|>或<|ignore|>表示静默。LoRA rank=128, α=256，应用于所有28层Transformer的线性层。三个action token新增到词表，仅embedding和LM head对应行可训练。音频编码器和talker冻结。

**核心创新：** (1) 首次系统性地研究多说话人社交场景中语音助手的轮次决策问题，定义三种行动token（respond/listen/ignore）；(2) Cocktail-DialogGen数据管道基于环境描述驱动对话生成，使用Gemini 3 Pro生成带动作标注的对话日志，Qwen3-TTS合成语音，支持18种seen和10种unseen环境；(3) 使用GRPO（Group Relative Policy Optimization）强化学习优化轮次决策，奖励函数结合动作准确率（0-1）和格式完整性（0-1）；(4) 训练时以50%概率随机丢弃说话人属性，增强推理时元数据缺失的鲁棒性。

**训练策略：** SFT阶段：在580,100个turn上训练1 epoch，batch size 3×4 L40 GPUs，学习率4×10^-5，cosine调度+10% warmup，48,342步，~52小时。GRPO阶段：G=16个采样，学习率1×10^-5，2,000步，~4.5小时。使用ms-swift和vLLM加速推理。

### 📊 实验结果
**数据集**：Cocktail-DialogGen（18环境中seen，10种unseen），14,400对话/72,000音频混合物

**主要指标**：
- Seen环境决策准确率：SFT+GRPO宏F1 0.928（respond recall 87%，F1-R 0.914，F1-S 0.942）
- Unseen环境决策准确率：宏F1 0.930（F1-R 0.917，F1-S 0.943）
- 对比基线：Moshi宏F1 0.298，Kimi-Audio 0.476，Qwen3-Omni 0.491
- 回复质量（seen METEOR）：SFT+GRPO 0.194/0.225（惩罚/条件），对比Qwen3-Omni 0.021/0.128
- 噪声鲁棒性：0-6dB SNR下性能仅轻微下降
- 匿名条件（移除名字/角色）：性能显著下降，语义模糊性影响大于声学因素

**是否开源**：https://github.com/xi-j/Cocktail-Talker

### ⭐ 评分：9/10
评分理由：问题定义新颖且具有重要实际意义，系统性地解决了语音助手在复杂社交场景中的轮次决策问题。Cocktail-DialogGen数据管道设计精巧，GRPO训练策略有效。实验全面覆盖seen/unseen环境、噪声水平、匿名性等维度，消融充分。开源代码促进可复现性。局限在于目前非流式且假设固定轮次边界。

---

## 语音前端

---

## [4] Does EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding

**arXiv ID**：2607.27268 | **方向**：语音前端

**作者**：Owais Mujtaba Khanday, Mohamed Baha Ben Ticha, Sanae Belfrouh, Marc Ouellet, Jose A. Gonzalez-Lopez

**机构**：University of Granada, Spain; CITIC-UGR; University of Chouaib Doukkali, Morocco; CIMCYC, University of Granada, Spain

**发布日期**：2026-07-29 | **论文**：https://arxiv.org/abs/2607.27268 | **PDF**：https://arxiv.org/pdf/2607.27268.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
EEG基础模型（LaBraM在~2,500小时EEG上预训练，EEGMamba在~16,000小时上预训练）在运动imagery、癫痫检测、睡眠分期等任务上显著超越CNN基线，但其向语音解码的迁移效果尚未被系统验证。本文首次对EEG基础模型与卷积基线在语音解码任务上进行系统基准测试，覆盖overt、covert和imagined speech三种模式。在UGR-MINDVOICE数据集上，16K参数的EEGNet（61.3%准确率，语音模式三分类）反而超越5.8M参数的LaBraM（57.3%）和8.3M参数的EEGMamba（56.6%），表明当前通用EEG预训练尚未迁移到语音生产任务。

### 🔧 技术方案

**问题背景：** EEG基础模型在运动imagery、癫痫检测等任务上表现优异，但语音解码涉及腹侧感觉运动皮层和颞上回的皮层动态，与基础模型预训练语料（静息态、运动imagery、临床事件）主导的范式有本质差异。现有研究仅在EEGMamba中将BCI Competition 2020 Track 3作为6个下游任务之一进行了评估，缺乏针对语音解码的受控比较。

**模型架构：** 对比5个模型：
- CNN基线：EEGNet（16.6K参数，深度可分离卷积）、ShallowFBCSPNet（161.6K参数）、EEGConformer（405.9K参数，卷积前端+Transformer编码器）
- 基础模型：LaBraM-Base（~5.8M参数，VQ神经频谱预测，~2,500小时预训练）、EEGMamba（8.3M参数，双向Mamba2状态空间模型，~16,000小时预训练）
所有模型接收EEG epoch张量，通过线性头输出分类logits。使用braindecode实现基线，公开检查点初始化基础模型。

**核心创新：** (1) 首次系统性地对EEG基础模型vs卷积基线进行语音/语言解码基准测试，覆盖overt、covert和imagined speech三种模式；(2) 使用统一预处理和微调协议（MNE-Python，0.1-75Hz带通滤波，50Hz陷波，ICA去除眼动伪迹，公共平均参考，重采样到200Hz，LOSO交叉验证）确保公平比较；(3) 揭示反直觉发现：大规模EEG预训练（~16,000小时）不优于16K参数CNN，表明需要专门针对语音的EEG基础模型。

**训练策略：** Adam优化器（η=10^-3，权重衰减10^-4），batch size 128，交叉熵损失，最多100 epoch，早停patience 10。基础模型从预训练检查点微调，基线从随机初始化训练。UGR-MINDVOICE使用LOSO协议（14折），BCIC2020-T3使用within-subject和LOSO两种协议。

### 📊 实验结果
**数据集**：UGR-MINDVOICE（64通道，15名西班牙语者，overt/covert speech，3/6/60类）；BCIC2020-T3（64通道，15名受试者，5类imagined speech）

**主要指标**：
- UGR-MINDVOICE语音模式（3类）：EEGNet 61.3% Acc / 0.607 W-F1，LaBraM 57.3% / 0.562，EEGMamba 56.6% / 0.553
- 语义类别（6类）：EEGNet 19.9% / 0.186，EEGMamba 19.3% / 0.150，LaBraM 17.0% / 0.056（接近随机16.7%）
- 词汇（60类）：EEGNet 2.8% / 0.019，EEGMamba 2.9% / 0.023，均接近随机1.7%
- BCIC2020-T3 within-subject：EEGConformer 30.2% Bal.Acc最优，LaBraM 27.7%，EEGMamba 25.7%
- BCIC2020-T3 LOSO：所有模型均接近随机20%水平（p>0.18）

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：首个EEG基础模型语音解码基准测试，结论具有重要启示意义——当前通用EEG预训练不能迁移到语音生产任务，指明了speech-specific预训练的必要方向。实验设计严谨，LOSO协议和统一预处理确保公平比较。但词汇级解码全部接近随机，表明任务本身极难，基础模型和基线均有巨大提升空间。

---

*Generated on 2026-08-14*