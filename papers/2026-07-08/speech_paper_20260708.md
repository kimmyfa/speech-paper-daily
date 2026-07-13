# 2026-07-08 语音论文速递

**共收录**: 16 篇 | **语音大模型**: 16 篇 | **语音前端**: 0 篇

> 今日 arXiv 语音相关论文共命中 16 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs

**arXiv ID** 2607.06540v1 | **方向** 语音大模型

**作者** Zhenyu Liu, Yunxin Li, Xuanyu Zhang, Qixun Teng, Shenyuan Jiang, Haolan Chen, Minjun Zhao, Fanbo Meng

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06540v1 | **PDF** https://arxiv.org/pdf/2607.06540v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
开发无缝、高性能的全双工口语语言模型（SLM）仍是语音和NLP社区的关键挑战。本文通过细粒度分析模型优化动态，揭示性能下降的根本原因：声学和语义建模的梯度冲突导致模态干扰。提出Lychee-FD框架，采用分层参数分离策略，在深层解耦冲突模态，同时通过专用语义对齐通道保持跨模态一致性。在多个全双工基准上显著超越SOTA，语音问答提升7.4%，全双工交互流畅度提升28.5%。

### 🔧 技术方案

**模型架构** Lychee-FD：端到端全双工框架，分层参数分离策略解耦声学和语义模态，专用语义对齐通道保持跨模态一致性。

**核心创新** 首次揭示并阐明全双工SLM中模态干扰的根本原因：梯度冲突。提出优雅的分层模型和实用解决方案，实现无缝、高性能原生智能全双工SLM。

**训练策略** 深层参数分离减少梯度冲突，语义对齐通道增强跨模态一致性。

### 📊 实验结果
**数据集** 多个全双工基准测试集（Spoken QA, FullDuplexBench 1.5）

**主要指标** 语音问答提升7.4%，全双工交互流畅度提升28.5%，不牺牲推理效率。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
Lychee-FD深入分析并有效解决了全双工SLM的模态干扰问题，分层解耦策略有重要创新。实验覆盖多个基准且提升显著，首次实现性能与效率的平衡。

---

## [2] InsideSSL: Understanding Self-Supervised Speech Representations using a Model-Centric Perspective

**arXiv ID** 2607.06392v1 | **方向** 语音大模型

**作者** Samir Sadok, Xavier Alameda-Pineda

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06392v1 | **PDF** https://arxiv.org/pdf/2607.06392v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Wav2Vec2、HuBERT、WavLM等自监督学习模型已成为语音任务的基础，但其内部层间动态理解仍是挑战。提出InsideSSL框架，从三个固有层间视角分析：压缩（熵）、几何（曲率）和扰动鲁棒性。研究表明不同训练目标诱导不同的声学压缩和流形展开机制。引入跨层生成兼容性矩阵（GCM）评估功能可迁移性，揭示稳定音素核心、身份波动性和深层语义剪枝。线性探测连接模型中心视角与下游任务，展示层拓扑如何决定音素、音高和说话人编码。

### 🔧 技术方案

**模型架构** InsideSSL框架：任务无关的三视角分析（压缩、几何、鲁棒性）+ 跨层GCM评估。

**核心创新** 模型中心视角的系统分析，揭示SSL模型内部表示的层间动态规律，为理解和优化自监督语音模型提供理论基础。

**训练策略** 不同训练目标（对比、掩码预测等）的系统对比分析。

### 📊 实验结果
**数据集** 通用语音任务基准

**主要指标** 揭示层拓扑与音素、音高、说话人编码的关系，为下游任务提供理论指导。

**是否开源** 暂未明确。本文已被INTERSPEECH 2026接收（long paper track）。

### ⭐ 评分：8/10
InsideSSL对SSL语音表示的深层理解有重要理论贡献，揭示了训练目标与表示质量的关联。被INTERSPEECH 2026接收验证了工作质量，对SSL模型的理解和优化有重要参考价值。

---

## [3] From Sinhala to Dhivehi: Cross-Lingual Transfer Learning for Low-Resource Speech Recognition

**arXiv ID** 2607.06289v1 | **方向** 语音大模型

**作者** Lukmal Ilyas, Nevidu Jayatilleke

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06289v1 | **PDF** https://arxiv.org/pdf/2607.06289v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
马尔代夫语（Dhivehi）在ASR和其他NLP任务上资源匮乏。研究从语言相关的僧伽罗语（Sinhala）进行跨语言迁移学习是否能改善Dhivehi ASR。进行了17组实验，覆盖五种迁移学习范式：Dhivehi单独基线、顺序微调、多语言微调、持续预训练和对照组（土耳其语作为无关语言）。最强系统在Sinhala持续预训练后用KenLM微调Dhivehi，达到12.89% WER和2.70% CER，相比Dhivehi单独基线提升13.50% WER和3.02% CER。土耳其语对照实验证实提升源于语言相关性。

### 🔧 技术方案

**模型架构** ASR系统基于端到端Transformer，进行多种迁移学习范式对比。

**核心创新** 系统比较五种迁移学习范式在低资源跨语言ASR上的效果，揭示语言相关性是迁移成功的关键因素。

**训练策略** Sinhala持续预训练 + Dhivehi微调 + KenLM语言模型解码。

### 📊 实验结果
**数据集** Dhivehi ASR数据集

**主要指标** 最强系统：12.89% WER，2.70% CER，相对基线提升13.50% WER和3.02% CER。

**是否开源** 暂未明确。本文已被MERCon 2026接收。

### ⭐ 评分：7/10
低资源语言ASR的跨语言迁移学习有实际价值。17组对照实验设计严谨，揭示了语言相关性在迁移中的关键作用。实验结果对类似低资源语言ASR有参考意义。

---

## [4] Goodbye Equal Error Rate, Hello Local Information Disclosure: Evaluating Voice Anonymisation against 1-to-N Linkage Threats

**arXiv ID** 2607.06259v1 | **方向** 语音大模型

**作者** Dāvis Šterns, Konstantinos Drossos, Natasha Fernandes, Tom Bäckström, Catuscia Palamidessi

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06259v1 | **PDF** https://arxiv.org/pdf/2607.06259v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音匿名化旨在保护说话人身份。当前隐私评估主要依赖EER，但EER设计用于1-to-1验证，与真实1-to-N数据库链接攻击存在威胁模型不匹配。提出模块化信息论评估框架，核心指标Local Information Disclosure（LID）以比特量化单次试验 utterance 的精确隐私损失。在VoicePrivacy 2024 Challenge系统上评估，揭示即便EER接近完美的系统也可能存在最坏情况1比特/次的信息泄露，有效加倍攻击者成功率。

### 🔧 技术方案

**模型架构** 信息论评估框架：LID量化原始相似度分数到攻击者后验置信度的隐私损失。

**核心创新** LID指标替代EER，明确针对1-to-N链接威胁模型，捕捉最坏情况隐私风险，与严格隐私法规对齐。

**训练策略** 无需训练，纯粹的评估框架。

### 📊 实验结果
**数据集** VoicePrivacy 2024 Challenge系统

**主要指标** 揭示EER近乎完美的系统在1-to-N场景下最坏情况泄露可达1比特/次，有效加倍攻击成功率。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
隐私评估指标创新性强，揭示了EER在1-to-N场景下的局限性。LID指标更符合实际威胁模型，对语音隐私保护有重要指导意义。被顶会接收验证了工作质量。

---

## [5] TriA Pipeline: A Large-Scale Automatic Audio Annotation Pipeline For Audio Classification In Specific Scenarios

**arXiv ID** 2607.06179v1 | **方向** 语音大模型

**作者** Hong Lyu, Mingru Yang, Qianhua He, Yanxiong Li, Jinxin Huang, Zhengyu Pei

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06179v1 | **PDF** https://arxiv.org/pdf/2607.06179v1.pdf | **代码** https://github.com/huanxian/TriA | **Demo** 暂无

### 📌 简介
大多数场景（如家庭环境）缺乏标注数据。提出TriA Pipeline，自动将各种场景音频转换为带音频事件标注的高质量训练数据。构建了TriA数据集，涵盖431个音频类、超过2130小时。划分先验知识引导的TriA_GK子集进行家庭音频分类任务对比实验。手动标注数据结合TriA_GK相比仅用手动标注数据，平均相对提升准确率3.97%，Macro-F1 3.35%。

### 🔧 技术方案

**模型架构** TriA Pipeline：自动音频标注流程，将原始音频转换为带标注的训练数据。

**核心创新** 大规模自动标注流程解决特定场景标注数据匮乏问题，先验知识引导的子集划分提升标注质量。

**训练策略** 自动标注流程生成大量训练数据，先验知识过滤提升标注质量。

### 📊 实验结果
**数据集** TriA数据集（431类，2130+小时），家庭AC任务

**主要指标** TriA_GK带来平均3.97%准确率相对提升，3.35% Macro-F1相对提升。

**是否开源** GitHub已发布：https://github.com/huanxian/TriA

### ⭐ 评分：7/10
自动标注流程解决实际数据匮乏问题，标注质量验证充分。开源代码利于复现，对音频分类任务有实用价值。

---

## [6] Fréchet Distance Loss on Speech Representations for Text-to-Speech Synthesis

**arXiv ID** 2607.06027v1 | **方向** 语音大模型

**作者** Ho-Lam Chung, Kuan-Po Huang, Bo-Ru Lu, Hung-yi Lee

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06027v1 | **PDF** https://arxiv.org/pdf/2607.06027v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
少步扩散和flow-matching TTS模型通常使用局部目标训练（条件流匹配、重建、停止预测），这些损失无法判断合成语音是否符合高质量语音分布。提出Speech Representation Fréchet Distance loss（SR-FD），一种用于无tokenizer flow-matching自回归TTS的训练时分布正则化器。微调时，模型用与部署相同的少步采样器合成语音，SR-FD将Whisper和CTC特征的均值和协方差与离线计算的参考统计量匹配。Seed-TTS英语上，四步SR-FD微调将WER从2.2279%降至1.4147%（相对降低36.5%）。

### 🔧 技术方案

**模型架构** SR-FD分布正则化：匹配Whisper和CTC特征的Fréchet距离，无需判别器和推理时计算。

**核心创新** 分布正则化替代局部损失，评估合成语音是否符合真实分布，提升少步TTS的可懂度。

**训练策略** 微调时用少步采样器生成语音，计算合成语音与参考语音的Fréchet距离作为额外损失。

### 📊 实验结果
**数据集** Seed-TTS English

**主要指标** 四步SR-FD微调将WER从2.2279%降至1.4147%（相对降低36.5%），超过原十步基线1.7366%。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
SR-FD有效提升少步TTS的可懂度，36.5%的WER相对降低显著。方法简洁有效，无需额外推理开销。被INTERSPEECH接收（短文 track）。

---

## [7] Escaping the Procrustean Bed: Groupwise Orthogonal Connectors for Audio-Language Models

**arXiv ID** 2607.06014v1 | **方向** 语音大模型

**作者** Ho-Lam Chung, Ke-Han Lu, Yi-Cheng Lin, Guan-Ting Lin, Yiming Chen, Hung-yi Lee

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06014v1 | **PDF** https://arxiv.org/pdf/2607.06014v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
音频-语言模型通过Q-Former连接器压缩语音编码器输出后送给LLM。本文揭示这种压缩的两个失败：连接器输出向量坍缩到单一方向；不同说话人产生几乎无法区分的输出，副语言线索（说话人身份、性别、韵律）丢失。提出ORCA方法，通过将查询分组并约束各组输出指向不同方向来逆转这种坍缩。在SAKURA多跳推理上，ORCA相比相同训练的4B基线提升26.4点，达到75.2%（vs 8B Audio Flamingo-3的49.0%）。连接器层面，查询冗余减少12倍，跨说话人差异增加75倍。

### 🔧 技术方案

**模型架构** ORCA连接器：分组正交约束，查询分组输出到不同方向，保持副语言信息。

**核心创新** 分组正交连接器设计，有效解决Q-Former的向量坍缩和说话人信息丢失问题。

**训练策略** 正交约束损失让不同组的查询输出指向不同方向。

### 📊 实验结果
**数据集** SAKURA多跳推理基准

**主要指标** ORCA提升26.4点达75.2%，查询冗余减少12倍，跨说话人差异增加75倍。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
ORCA有效解决了音频-语言模型中连接器的信息丢失问题，方法创新且效果显著。多跳推理性能大幅提升证明了方法有效性。

---

## [8] Flow Matching-Based Speech Source Separation with Best-of-N Biometric Sampling

**arXiv ID** 2607.06088v1 | **方向** 语音大模型

**作者** Anastasia Zorkina, Alexandr Anikin, Nikita Khmelev, Anastasiya Korenevskaya, Sergey Novoselov, Vladimir Volokhov, Maxim Korenevsky, Yuriy Matveev

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06088v1 | **PDF** https://arxiv.org/pdf/2607.06088v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
单通道语音分离在实际部署中面临源排列模糊、生成模型采样可变性和长录音分块推理等挑战。提出基于条件流匹配的方法，给定混合语音产生有序双源输出。冻结的说话人编码器在训练时定义源顺序，推理时用于生物特征最佳-N候选选择和分块级通道对齐。在Libri2Mix基准评估分离质量（SI-SDR、PESQ、ESTOI）和下游影响（cpWER、EER）。Transformer U-Net变体在客观分离指标上与强基线竞争，下游ASR和说话人验证错误率最低。

### 🔧 技术方案

**模型架构** 条件流匹配分离模型 + 冻结说话人编码器 + 最佳-N生物特征采样。

**核心创新** 条件流匹配框架结合生物特征最佳-N采样，解决排列歧义和采样变异问题。

**训练策略** 说话人编码器定义源顺序，最佳-N候选选择确保稳定输出。

### 📊 实验结果
**数据集** Libri2Mix

**主要指标** Transformer U-Net在SI-SDR、PESQ、ESTOI上与强基线竞争，下游cpWER和EER最低。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
流匹配用于语音分离有新意，生物特征采样策略有效解决排列问题。下游任务指标验证了分离质量的有效性。

---

## [9] BlueMagpie-TTS: A Token-Efficient Tokenizer, Language Model, and TTS for Taiwanese-Accent Code-Switching Speech

**arXiv ID** 2607.06054v1 | **方向** 语音大模型

**作者** Ho Lam Chung, Bo-Xuan Zheng, Cheng-Chieh Huang, Cheng-Han Chang, Jung-Ching Chen, Lok-Lam Ieong, Ting-Lin Hsiao, Yu-Cheng Lee

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06054v1 | **PDF** https://arxiv.org/pdf/2607.06054v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
现有TTS系统对台湾口音适应差：口音默认其他普通话变体，tokenizer过度分割常见台湾文本，中英混语边界发音退化。提出从底层解决文本侧问题：PangolinTokenizer（字节级BPE，训练于台湾语境数据）达到最低token率（0.485 tokens/字符）；Barbet（基于PangolinTokenizer的传统中文语言模型）在14任务评估中排名第一；BlueMagpie-TTS将Barbet连接到VoxCPM2预训练声学栈。在1000句台湾本地化测试集上，CER从11.45%降至4.81%（相对降低58.0%），WER从14.83%降至5.36%（相对降低63.9%）。盲听实验中65.6%受试者偏好BlueMagpie-TTS。

### 🔧 技术方案

**模型架构** BlueMagpie-TTS：PangolinTokenizer + Barbet（传统中文LM）+ VoxCPM2声学栈。

**核心创新** 从底层适配台湾语境：字节级BPE tokenizer解决文本处理问题，分层设计（tokenizer→LM→声学）实现高效TTS。

**训练策略** 台湾语境数据训练tokenizer和LM，声学栈固定只训练桥接模块。

### 📊 实验结果
**数据集** 1000句台湾本地化测试集

**主要指标** CER相对降低58.0%，WER相对降低63.9%，盲听65.6%偏好BlueMagpie-TTS。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
台湾口音TTS的系统性解决方案，从tokenizer到LM再到声学的完整适配。实验验证充分（自动指标+盲听），实际应用价值高。

---

## [10] Determinantal point process sampling for bioacoustic active learning

**arXiv ID** 2607.06063v1 | **方向** 语音大模型

**作者** Hugo Magaldi, Gabriel Dubus

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06063v1 | **PDF** https://arxiv.org/pdf/2607.06063v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
生态声学监测产生大量音频数据，主动学习可减少标注工作量同时高效训练可靠生物多样性分类器。提出CARE-DPP，一种批主动学习获取方法，结合类别平衡的预测不确定性与嵌入空间新颖性，DPP目标选择高质量非冗余获取批次。不确定性-新颖性平衡随标注预算退火：早期强调几何覆盖，后期越来越多利用分类器不确定性。评估在BirdSet HSN、POW、UHH和ATBFL上，Macro mAP的AULC达0.50 vs 基线0.46。

### 🔧 技术方案

**模型架构** CARE-DPP：类别平衡不确定性 + 嵌入空间新颖性 + DPP批次选择。

**核心创新** DPP用于生物声学主动学习的选择性，确保批次多样性和非冗余性。

**训练策略** 早期DPP池混合高质量候选与随机探索，后期批次逐步增大。

### 📊 实验结果
**数据集** BirdSet HSN, POW, UHH, ATBFL

**主要指标** Macro mAP的AULC达0.50 vs CoreSet基线0.46。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
DPP用于主动学习有创新性，解决生物声学数据标注效率问题。实验设计完整，AULC提升验证有效性。

---

## [11] Few-Shot Class-Incremental Audio Classification Using Pseudo-Incrementally Trained Embedding Learner and Continually Updated Stochastic Classifier

**arXiv ID** 2607.05953v1 | **方向** 语音大模型

**作者** Yanxiong Li, Wenchang Cao, Jiaxin Tan, Qianqian Li, Guoqing Chen

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.05953v1 | **PDF** https://arxiv.org/pdf/2607.05953v1.pdf | **代码** https://github.com/vinceasvp/PITEL-CUSC | **Demo** 暂无

### 📌 简介
少样本类别增量音频分类（FCAC）需要逐步识别增量类（少标签样本）同时记忆基类。模型需兼具高稳定性（记忆基类）和强可塑性（适应增量类）。设计解耦为两个独立模块：嵌入学习器（残差卷积网络骨干）和随机分类器（每类由均值和方差向量组成的分布）。基会话训练后，嵌入学习器不再更新以记忆基类知识，通过伪增量训练策略保持增量类表示能力；随机分类器在每个增量会话更新以适应新类。在FSC-89、NSynth-100、LS-100三个数据集验证。

### 🔧 技术方案

**模型架构** 嵌入学习器（冻结）+ 随机分类器（持续更新）。伪增量训练策略保持嵌入学习器的表示能力。

**核心创新** 解耦设计：冻结嵌入学习器记忆基类，持续更新分类器适应新类，避免灾难性遗忘。

**训练策略** 基会话伪增量训练嵌入学习器，增量会话只更新随机分类器。

### 📊 实验结果
**数据集** FSC-89, NSynth-100, LS-100

**主要指标** 准确率超越比较方法，计算复杂度低于大多数比较方法。

**是否开源** GitHub已发布：https://github.com/vinceasvp/PITEL-CUSC

### ⭐ 评分：7/10
FCAC问题的解耦设计方案合理，有效避免灾难性遗忘。三个数据集验证泛化性，开源代码利于复现。

---

## [12] PluraMath: Extending Mathematical Reasoning Evaluation Beyond High-Resource Languages

**arXiv ID** 2607.05992v1 | **方向** 语音大模型

**作者** Daryna Dementieva, Nikolay Babakov, Kathy Hämmerl, Ilseyar Alimova, Jindřich Libovický, Shu Okabe, Miras Baisbay, Lukas Edman

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.05992v1 | **PDF** https://arxiv.org/pdf/2607.05992v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
数学推理已成为评估LLM的核心任务，但现有基准严重偏向高资源语言。PolyMath数据集仅覆盖18种高资源语言。提出PluraMath，将PolyMath扩展到18种额外低资源语言（涵盖6个语系，从中等资源到极低资源）。通过人工审核流程构建，本地发言者彻底验证预计算翻译。评测27个推理LLM，揭示高资源和低资源语言间持续存在的数学推理性能差距，强结果与更好指令遵循能力高度相关。

### 🔧 技术方案

**模型架构** PluraMath基准：18种低资源语言的数学推理评估集。

**核心创新** 将数学推理评估扩展到低资源语言，揭示性能差距与指令遵循能力的关联。

**训练策略** 人工审核确保翻译质量，本地发言者验证。

### 📊 实验结果
**数据集** PluraMath（18种低资源语言）

**主要指标** 揭示高资源和低资源语言间持续性能差距，强结果与指令遵循能力相关。

**是否开源** 数据集、数据获取流程和评估框架全部开源。

### ⭐ 评分：7/10
低资源语言数学推理基准填补空白，揭示了性能差距的根源。开源利于促进低资源语言NLP研究。

---

## [13] Pitwall: Faithful Natural-Language Race-Strategy Briefings from a Calibrated Real-Time Monte Carlo Engine

**arXiv ID** 2607.06495v1 | **方向** 语音大模型

**作者** Juan S. Santillana (Independent Researcher)

**机构** Independent Researcher

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06495v1 | **PDF** https://arxiv.org/pdf/2607.06495v1.pdf | **代码** 暂无 | **Demo** https://pitwall.jsantillana.com

### 📌 简介
实时体育解说是在截止日期下的接地生成：陈述涉及真实命名运动员，接地状态每几秒变化，生成时无参考文本。提出Pitwall系统生成英语、西班牙语、葡萄牙语的F1策略简报，将忠实性作为架构属性而非追求目标：每个发布的句子分解为类型化事实声明，每个声明根据促使它的概率状态验证。验证器同样门控微调数据：3045个模型撰写目标中，只保留81.9%所有声明都有状态支持的，其余回退到可证明忠实的模板。验证基于126场2018-2024比赛的校准向量化Monte Carlo引擎（每圈N=2000）实现。在两场现场大奖赛确认端到端运行。

### 🔧 技术方案

**模型架构** Pitwall：Monte Carlo引擎（每圈2000次续篇）+ 事实验证器 + 三语生成模型。

**核心创新** 忠实性作为架构属性，事实验证门控训练数据和生成，确保每句陈述都有状态支持。

**训练策略** 验证器过滤微调数据，只保留事实支持的目标。

### 📊 实验结果
**数据集** 126场比赛校准，2025-2026完全留出赛季验证

**主要指标** Winner-in-top-3准确率90.3%（155次回测），留出Brier 0.0745。现场验证在奥地利和英国大奖赛成功。

**是否开源** Demo已上线：https://pitwall.jsantillana.com

### ⭐ 评分：8/10
将忠实性作为架构属性的设计理念创新，事实验证机制有效防止幻觉。实战验证（在真实大奖赛上确认）证明了系统可靠性。

---

## [14] InfluMatch: Frontier-Quality KOL Search at 4B-Model Cost

**arXiv ID** 2607.05968v1 | **方向** 语音大模型

**作者** Krittanon Kaewtawee, Petmongkon Pornpichitsuwan, Natchaya Temyingyong, Nutnicha Laplamoon, Wachiravit Modecrua, Krittin Pachtrachai, Touchapon Kraisingkorn

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.05968v1 | **PDF** https://arxiv.org/pdf/2607.05968v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
KOL（关键意见领袖）匹配当前依赖关键词搜索（丢失语义）或提示前沿LLM处理每个候选（准确但慢且贵）。提出InfluMatch，低成本三阶段级联——检索→重排→推理——完全基于小规模开源模型：密集检索返回50候选，4B逐点评分重排器对每个候选打分取前10，4B推理器按 rubric 评估短名单。端到端在11-query、50-KOL标签集上达94.1% P@5，匹配前沿模型Kimi-K2.6（91.8%）同时发出约35倍更少输出token，单A100上约20秒处理50-KOL查询。

### 🔧 技术方案

**模型架构** 三阶段级联：密集检索 + 4B逐点重排 + 4B推理评分。

**核心创新** 小模型级联匹配前沿模型性能，成本大幅降低，推理高效。

**训练策略** SimPO微调重排器有效，按点标签微调推理器反而降低端到端性能。

### 📊 实验结果
**数据集** 泰语营销KOL搜索

**主要指标** 94.1% P@5匹配Kimi-K2.6（91.8%），约35倍更少输出token，约20秒/A100。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
小模型级联有效降低成本提升效率，工程实用性强。揭示了按点微调与端到端性能的差异有研究价值。

---

## [15] Umm... With Transformers? Insights from Filled Pause Use across Four Slavic Parliaments

**arXiv ID** 2607.05964v1 | **方向** 语音大模型

**作者** Ivan Porupski, Branimir Dropuljić, Nikola Ljubešić

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.05964v1 | **PDF** https://arxiv.org/pdf/2607.05964v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
填充停顿（FP）是自发语音的普遍特征，但大多数研究依赖小型单语语料库。分析四种相关斯拉夫语言（克罗地亚语、捷克语、波兰语、塞尔维亚语）约4000小时议会演讲。FP检测使用Transformer自动检测，FP率使用Mundlak校正的GEE建模以区分说话人内和说话人间效应。复制了年龄和语速与FP率的负相关，发现性别效应是语言特定的且与大多数先前文献方向相反。情感、政治倾向和权力状态的新分析揭示情感与FP率一致正相关，倾向和权力状态有议会特定调节。

### 🔧 技术方案

**模型架构** Transformer-based FP检测 + GEE统计建模。

**核心创新** 四种斯拉夫语言的大规模跨语言FP分析，揭示先前未报告的语言特定性别效应。

**训练策略** Mundlak校正区分说话人内/间效应。

### 📊 实验结果
**数据集** 四种斯拉夫语议会演讲（约4000小时）

**主要指标** 复制年龄-语速负相关，发现语言特定性别效应，情感正相关于FP率。

**是否开源** 暂未明确。

### ⭐ 评分：6/10
大规模跨语言FP分析有语言学价值，但语音技术直接贡献有限。发现语言特定的性别效应是新颖的，但应用场景有限。

---

## [16] When Does Tool Use Increase the Expressive Power of Finite-Precision Recurrent Models?

**arXiv ID** 2607.06155v1 | **方向** 语音大模型

**作者** Nikola Zubić, Qian Li, Yuyi Wang, Davide Scaramuzza

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06155v1 | **PDF** https://arxiv.org/pdf/2607.06155v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
现代序列模型作为代理部署时将token生成与外部工具调用交错。本文给出工具访问何时增加计算表达性的精确架构级描述。将任何固定有限精度循环序列模型（包括B位内部状态的有限精度SSM）建模为通过有限命令/观察接口与oracle交互的确定性有限状态控制器。结果形成尖锐二分法：有限状态工具本质上不增加表达能力；单个最小无限状态工具（图灵机磁带）使系统图灵完备；一阶层有限精度选择性仿射SSM控制器（含二元one-hot隐藏状态）恰好实现此构造。

### 🔧 技术方案

**模型架构** 有限精度循环序列模型 + 工具oracle接口。

**核心创新** 精确描述工具访问何时增加计算表达性，揭示SSM与图灵机的等价条件。

**训练策略** 理论分析，无需实验训练。

### 📊 实验结果
**数据集** 理论工作，无具体数据集

**主要指标** 揭示EQ_n需要2^n状态但带工具的单常规模控制器可模拟，指数级分离。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
理论贡献扎实，揭示了有限精度模型与图灵机的精确表达能力边界。构造性证明清晰，对理解序列模型的计算能力有重要价值。

---

今日语音论文速递