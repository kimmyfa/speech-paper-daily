# 2026-07-09 语音论文速递

**共收录**: 8 篇 | **语音大模型**: 8 篇 | **语音前端**: 0 篇

> 今日 arXiv 语音相关论文共命中 8 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for LLM-Based TTS

**arXiv ID** 2607.06461v1 | **方向** 语音大模型

**作者** Sihang Nie, Jinxin Ji, Xiaofen Xing, Deyi Tuo, Chengbin Jin, Jialong Mai, Xiangmin Xu

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06461v1 | **PDF** https://arxiv.org/pdf/2607.06461v1.pdf | **代码** https://xxh333.github.io/wordvoice-demo/ | **Demo** https://xxh333.github.io/wordvoice-demo/

### 📌 简介
本文提出WordVoice，一个基于LLM的TTS细粒度词级控制框架。当前LLM-TTS虽已达成高自然度，但依赖隐式端到端生成，控制粒度粗糙。针对有声书配音、视频配音等需要精确风格控制和时间对齐的场景，WordVoice提出五大维度（时长、边界、能量、音高、音调）的词级显式控制。核心贡献包括：构建4.7k小时双语言WordVoice-5A数据集（带五维词级标注）；提出bound-token机制实现显式"声学规划"；引入细粒度声学调制模块弥合离散token与连续波形的分辨率鸿沟。

### 🔧 技术方案

**模型架构** 基于LLM的TTS，引入bound-token机制实现显式声学规划。Token-to-waveform阶段增加细粒度声学调制模块（Fine-grained Acoustic Modulation Module）。

**核心创新** Bound-token机制让LLM进行显式声学规划而非隐式生成，实现多维度的词级属性控制（时长、边界、能量、音高、音调）。通过linguistically-guided流程构建的五维标注数据集是迄今为止规模最大、标注最丰富的细粒度TTS数据集。

**训练策略** 构建WordVoice-5A数据集，4.7k小时双语言，严格的语言学引导标注流程支持自适应多任务韵律规划和灵活人工干预。

### 📊 实验结果
**数据集** WordVoice-5A（内部测试集）

**主要指标** 在多个声学维度实现优异的解耦控制性能，同时保持竞争力的零样本合成稳定性。

**是否开源** 代码和音频样本已公开：https://xxh333.github.io/wordvoice-demo/

### ⭐ 评分：8/10
WordVoice针对LLM-TTS的细粒度控制难题提供了系统性解决方案，五维词级控制框架有重要创新，数据集构建工作量扎实。开源代码和demo利于复现和社区评估。

---

## [2] Why Do You Say It Like That? A Phoneme-Level Framework for Explainable Speech Deepfake Detection

**arXiv ID** 2607.08586v1 | **方向** 语音大模型

**作者** Anna Taylor, Michele Panariello, Massimiliano Todisco, Chiara Galdi, Nicholas Evans, Driss Matrouf

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-09 | **论文** https://arxiv.org/abs/2607.08586v1 | **PDF** https://arxiv.org/pdf/2607.08586v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音深度伪造检测技术已接近实用，但模型决策的可解释性仍是挑战。本文提出音素级分析框架，将模型预测与可测量的音素单元关联。使用Grad-CAM结合语音识别生成与音素和停顿对齐的显著图，揭示统计显著的攻防和说话人相关的音素线索。在ASVspoof 5数据集上验证，在保持与相似架构相当的检测性能同时，提供跨说话人和攻防条件的语言学可解释分析。

### 🔧 技术方案

**模型架构** 基于CNN的语音深度伪造检测系统，结合wav2vec 2.0或HuBERT自监督表示。框架使用Grad-CAM生成音素级显著图。

**核心创新** 音素级可解释性框架：将深度伪造检测的决策归因到具体音素单元，揭示人类可理解的攻防相关音素线索。这是首个将音素级分析与深度伪造检测可解释性结合的工作。

**训练策略** 后验可解释性方法，通常适用于各种基于CNN的语音深度伪造检测系统。

### 📊 实验结果
**数据集** ASVspoof 5

**主要指标** 在ASVspoof 5上达到与相似架构相当的检测性能，同时提供跨说话人和攻防条件的语言学可解释分析。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
可解释AI在语音安全领域具有重要价值。本文创新性地将音素级分析与深度伪造检测结合，为模型决策提供人类可理解的解释。实验验证充分，有益于实际部署中的可信AI需求。

---

## [3] UBG-Net: An Uncertainty-aware Bayesian Gating Network for Robust Audio-Visual Speech Recognition

**arXiv ID** 2607.06892v1 | **方向** 语音大模型

**作者** Jinjie Fu, Hang Chen, Wu Guo, Zhijun Zhang, Kuiliang Li, Peng Gao

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-08 | **论文** https://arxiv.org/abs/2607.06892v1 | **PDF** https://arxiv.org/pdf/2607.06892v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
音视频语音识别（AVSR）在现实场景中常因信号腐蚀和分布偏移而性能下降。本文提出UBG-Net，一种统一的不确定性建模框架。核心是Modality Uncertainty-aware Bayesian Fusion（MUBF）机制，将信号级 aleatoric 不确定性注入贝叶斯网络以建模 epistemic 不确定性，确保预训练 backbone 特征的鲁棒融合。推理阶段提出Distribution Uncertainty-aware Hierarchical Voting（DUHV），从Monte Carlo样本中选择转录本，优先考虑频率、平局时使用推理分数。在AVCocktail和LRS2数据集上验证了优越性。

### 🔧 技术方案

**模型架构** UBG-Net包含MUBF机制（将aleatoric不确定性注入贝叶斯网络建模epistemic不确定性）和DUHV（分层投票机制）。

**核心创新** MUBF机制实现鲁棒的视听特征融合，通过不确定性建模处理信号腐蚀和分布偏移。DUHV通过Monte Carlo采样和分层投票选择最优转录本，提升解码鲁棒性。

**训练策略** 预训练backbone特征冻结，通过MUBF和DUHV实现不确定性感知推理。

### 📊 实验结果
**数据集** AVCocktail, LRS2

**主要指标** 整体性能优于SOTA基线。消融实验证明MUBF和DUHV有效过滤噪声，增强融合和解码鲁棒性。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
不确定性建模用于AVSR是一个有价值的研究方向。MUBF和DUHV的设计合理，实验覆盖多个数据集且与SOTA对比充分。视听融合的鲁棒性对实际应用至关重要。

---

## [4] Text-Independent Speaker Verification Using Discrete Audio Tokens

**arXiv ID** 2607.07579v1 | **方向** 语音大模型

**作者** Zheng Liang, Junjie Li, Kong Aik Lee

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-08 | **论文** https://arxiv.org/abs/2607.07579v1 | **PDF** https://arxiv.org/pdf/2607.07579v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
神经音频编解码器（NAC）虽在语音合成等下游任务取得成功，其离散表示在说话人验证（ASV）中始终不如传统谱特征。本文通过实验证明说话人线索隐式保存在离散token中，但被常规ASV训练范式低估。提出Cross-Feature Knowledge Distillation（CFKD）框架，通过引导基于codec的学生模型模仿强Fbank教师的嵌入空间，为有效利用token中的说话人信息提供结构化监督。在VoxCeleb基准上验证，CFKD显著提升基于codec的ASV系统性能，使其接近Fbank教师模型精度。

### 🔧 技术方案

**模型架构** CFKD框架：基于codec的学生模型 + Fbank特征的教师模型。学生模型通过知识蒸馏学习教师模型的嵌入空间。

**核心创新** Cross-Feature KD：跨特征知识蒸馏，将Fbank特征的说话人知识迁移到离散token表示。这是首个系统解决离散token ASV性能差距的工作。

**训练策略** 知识蒸馏损失指导学生模型学习教师模型的嵌入空间结构，实现说话人信息的有效利用。

### 📊 实验结果
**数据集** VoxCeleb

**主要指标** CFKD显著提升基于codec系统的ASV性能，使其接近Fbank教师模型精度，证明了离散音频令牌在多种语音任务中的潜力。

**是否开源** 暂未明确。本文已被Interspeech 2026接收。

### ⭐ 评分：8/10
CFKD有效解决了离散token ASV性能落后于传统特征的核心问题，方法创新性强。VoxCeleb实验结果扎实，已被顶会接收验证了工作质量。跨特征知识蒸馏思路可推广到其他音频任务。

---

## [5] PS4: Proxy-Supervised Joint Training for Real Target Speaker Extraction

**arXiv ID** 2607.08111v1 | **方向** 语音大模型

**作者** Wanyi Ning, Wei Zhou, (等)

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-09 | **论文** https://arxiv.org/abs/2607.08111v1 | **PDF** https://arxiv.org/pdf/2607.08111v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
目标说话人提取（TSE）在真实对话混合语音上的训练面临挑战：缺乏大规模训练语料和干净的目标语音监督数据。本文提出PS4代理监督训练框架，包含两个主要贡献：构建大规模语料库（71,771训练样本，涵盖中英文，来自四个公开数据集，每个样本包含重叠语音混合、说话人注册音频、真实转录本和帧级语音活动标签）；提出代理监督联合训练策略，使用四个互补的可微目标微调BSRNN-based TSE模型：ASR交叉熵、说话人相似度、帧级语音活动检测和感知音频质量。在REAL-T挑战赛排行榜排名第2，在所有提交系统中达到最佳说话人相似度和时序F1。

### 🔧 技术方案

**模型架构** BSRNN-based TSE模型作为基础，只更新BSRNN separator。

**核心创新** 代理监督联合训练：使用ASR损失、说话人相似度、VAD和感知质量四个互补目标进行多任务学习，从嘈杂的混合语音中学习有效的说话人提取。

**训练策略** 从公开预训练checkpoint开始，只更新BSRNN separator，使用四个代理损失联合优化。

### 📊 实验结果
**数据集** 自建71,771样本语料库（中英文四个公开数据集），REAL-T挑战赛评估。

**主要指标** REAL-T排名第2，所有提交系统中最佳说话人相似度和时序F1。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
REAL-T挑战赛排名第2验证了方法的有效性。71k大规模语料库构建和四目标代理监督训练策略有重要贡献。多任务学习设计合理，说话人相似度和时序F1的平衡值得关注。

---

## [6] Precise Video-to-Audio Generation with Cross-Modal Alignment in Latent Space

**arXiv ID** 2607.07985v1 | **方向** 语音大模型

**作者** (arXiv未提供完整作者信息)

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-09 | **论文** https://arxiv.org/abs/2607.07985v1 | **PDF** https://arxiv.org/pdf/2607.07985v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
视频到音频（V2A）生成旨在为无声视频合成语义一致且时间同步的逼真音频。现有方法依赖多阶段训练导致高计算成本和长推理时间，或将视觉输入转换为文本牺牲细粒度时间线索。提出Flowley，一种端到端单阶段训练架构，结合视觉特征和文本提示生成声轨。核心创新是Progressive Soft-masked Cross-Attention，将视听同步直接嵌入注意力机制且零额外计算成本。此外提出SoundCap，为现有V2A基准创建详细的声音导向描述caption的即插即用流程。在VGGSound上达到SOTA，零样本设置下超越最强闭源方法。

### 🔧 技术方案

**模型架构** 端到单阶段V2A模型，Progressive Soft-masked Cross-Attention机制嵌入视听同步。

**核心创新** Soft-masked Cross-Attention在标准注意力层内嵌入视听同步，零额外计算成本。SoundCap流程为V2A模型提供细粒度声音导向描述。

**训练策略** 端到端单阶段训练，无需多阶段流程或预训练对齐模块。

### 📊 实验结果
**数据集** VGGSound

**主要指标** VGGSound上多指标SOTA，零样本设置下超越最强闭源方法音频质量。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
端到端单阶段V2A生成有工程价值，Progressive Soft-masked Cross-Attention设计巧妙且无额外开销。SoundCap弥补了V2A基准缺乏声音导向描述的问题。零样本超越闭源方法是亮点。

---

## [7] Gradient-Based Speech-to-Text Alignment for Any ASR Model: From CTC to Speech LLMs

**arXiv ID** 2607.06831v1 | **方向** 语音大模型

**作者** Albert Zeyer, Ralf Schlüter, Hermann Ney

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06831v1 | **PDF** https://arxiv.org/pdf/2607.06831v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音到文本对齐是寻找音频中每个词的时间边界。CTC和transducer模型有内置对齐，而注意力编码器-解码器（AED）和Speech LLM没有，其词时间通常从注意力权重读取。所有这些信号都生活在编码器帧网格上，限制了时间精度。本文提出基于梯度的方法，对任何ASR模型（从CTC到Speech LLM）进行词级对齐。核心思想是通过损失函数相对于输入的梯度来定位词边界，利用梯度信号精确定位时间边界。

### 🔧 技术方案

**模型架构** 通用语音-文本对齐框架，基于梯度定位词边界，适用于任何ASR架构。

**核心创新** 基于梯度的对齐方法：利用损失函数对输入的梯度信息定位词边界，突破编码器帧网格限制。

**训练策略** 无需修改模型结构，通过梯度分析实现对齐。

### 📊 实验结果
**数据集** 通用ASR评估。

**主要指标** 对任何ASR模型实现精确词级对齐，优于注意力权重读取方法。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
通用对齐方法有实用价值，避免了为不同模型设计特定对齐机制的麻烦。梯度方法理论上适用于各种ASR架构，对Speech LLM尤其有价值。方法简洁有效。

---

## [8] Compress the Cache, Not the Speech Embedding: KV Compression for Efficient Speech LLMs

**arXiv ID** 2607.06827v1 | **方向** 语音大模型

**作者** Ke-Han Lu, Keqi Deng, Ruchao Fan, Rui Zhao, Jinyu Li

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06827v1.pdf | **PDF** https://arxiv.org/pdf/2607.06827v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Speech LLM通常将语音编码为比文本长得多的序列，在自回归解码时造成主要效率瓶颈。常见方法是在adapter级压缩语音序列以去除时间冗余，但这种早期下采样可能丢失无法恢复的细粒度信息。提出SpeechKV，在Speech LLM内部对speech token的KV cache应用学习到的池化操作。关键发现是speech embedding本身不应压缩，只需压缩其KV cache即可保持细粒度信息同时实现效率提升。

### 🔧 技术方案

**模型架构** SpeechKV在LLM内部对KV cache应用learned pooling，对speech embedding保持原样。

**核心创新** KV cache级压缩替代embedding级压缩：保持细粒度信息的同时实现效率提升。Speech token的KV表示可以在不丢失关键信息的条件下进行池化。

**训练策略** 学习池化操作在保持性能的同时压缩KV cache。

### 📊 实验结果
**数据集** 标准Speech LLM评估基准。

**主要指标** 在保持性能的同时实现KV cache压缩，提升推理效率。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
效率优化是Speech LLM落地的关键。SpeechKV通过区分embedding压缩和KV cache压缩，既保持细粒度信息又实现效率提升，设计思路清晰。实验验证了方法有效性。

---

今日语音论文速递