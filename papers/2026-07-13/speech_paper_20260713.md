# 2026-07-13 语音论文速递

**共收录**: 11 篇 | **语音大模型**: 8 篇 | **语音前端**: 3 篇

> 今日 arXiv 语音相关论文共命中 11 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] BlueMagpie-TTS: A Token-Efficient Tokenizer, Language Model, and TTS for Taiwanese-Accent Code-Switching Speech

**arXiv ID** 2607.06054 | **方向** 语音大模型

**作者** Ho Lam Chung, Bo-Xuan Zheng, Cheng-Chieh Huang, Cheng-Han Chang, Jung-Ching Chen, Lok-Lam Ieong, Ting-Lin Hsiao, Yu-Cheng Lee, Yi-Hsin Chung, Yu-Kai Guo, Hung-yi Lee

**机构** National Taiwan University

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06054 | **PDF** https://arxiv.org/pdf/2607.06054.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文针对台湾口音混语语音合成问题，提出从文本端进行优化的方案。现有TTS系统对台湾国语的适配不佳，口音默认偏向其他普通话变体，分词器对台湾文本过度分割，且在中英文切换边界发音退化。核心解决方案包括：PangolinTokenizer（字节级BPE分词器， token率0.485为最低）、Barbet（传统中文语言模型，14项评测第一）、BlueMagpie-TTS（结合Barbet和VoxCPM2声学模型）。实验在1000句台湾本地化测试集上，CER从11.45%降至4.81%，WER从14.83%降至5.36%，相对降低58.0%和63.9%。盲听实验中65.6%投票偏好BlueMagpie-TTS。

### 🔧 技术方案

**模型架构** PangolinTokenizer为字节级BPE分词器，在台湾语境数据上训练，token率0.485为最低（9个分词器中最小）。Barbet是基于PangolinTokenizer的十亿参数传统中文语言模型，在14项评测中排名第一。BlueMagpie-TTS将Barbet通过学习桥接层连接到VoxCPM2预训练声学栈，保持声学栈固定。

**核心创新** 文本侧自底向上适配台湾语境：针对台湾文本特点重新训练分词器和语言模型，解决现有系统对台湾口音和混语场景的不适配问题。学习桥接层在冻结声学栈的同时实现文本-声学对齐。

**训练策略** PangolinTokenizer在台湾语境数据上训练字节级BPE。Barbet在PangolinTokenizer上训练传统中文LM。BlueMagpie-TTS通过学习桥接层连接Barbet和VoxCPM2声学模型，训练时保持声学栈固定。

### 📊 实验结果
**数据集** 1000句台湾本地化测试集

**主要指标** CER从11.45%降至4.81%（相对降低58.0%），WER从14.83%降至5.36%（相对降低63.9%）。盲听实验中10位听众500句句子，65.6%投票偏好BlueMagpie-TTS。

**是否开源** 暂未发布

### ⭐ 评分：8/10
针对台湾口音和混语场景的实用TTS系统创新，分词器和语言模型联合优化策略有效，实验设计合理且有实际应用价值。

---

## [2] Flow Matching-Based Speech Source Separation with Best-of-N Biometric Sampling

**arXiv ID** 2607.06088 | **方向** 语音大模型

**作者** Anastasia Zorkina, Alexandr Anikin, Nikita Khmelev, Anastasiya Korenevskaya, Sergey Novoselov, Vladimir Volokhov, Maxim Korenevsky, Yuriy Matveev

**机构** 论文未提供机构信息

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06088 | **PDF** https://arxiv.org/pdf/2607.06088.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出基于条件流匹配的单通道语音分离方法，通过生物特征最佳-N采样解决排列歧义和长录音分块推理难题。核心创新是使用冻结的说话人编码器定义训练时的源顺序，推理时复用于生物特征最佳-N候选选择和分块级通道对齐。模型在Libri2Mix基准上评估，使用SI-SDR、PESQ、ESTOI等指标衡量分离质量，并使用cpWER和EER衡量下游ASR和说话人验证影响。Transformer U-Net变体在分离指标上具有竞争力，且在所有评估设置中实现最低的下游ASR和说话人验证错误率。

### 🔧 技术方案

**模型架构** 基于条件流匹配的语音分离方法，输出为排列无关的两个源。冻结的说话人编码器定义训练时的源顺序，推理时用于生物特征最佳-N候选选择和分块级通道对齐。

**核心创新** 条件流匹配处理单通道语音分离的排列歧义问题。生物特征最佳-N采样通过说话人编码器选择最佳分离候选。分块级通道对齐解决长录音处理难题。

**训练策略** 使用冻结说话人编码器定义训练时的源顺序。推理时通过生物特征编码器进行最佳-N候选选择，实现排列无关的确定性输出。

### 📊 实验结果
**数据集** Libri2Mix基准

**主要指标** SI-SDR、PESQ、ESTOI等分离指标具有竞争力，cpWER（ASR）和EER（说话人验证）错误率在所有评估设置中最低。

**是否开源** 暂未发布

### ⭐ 评分：8/10
流匹配应用于语音分离的创新方法，生物特征采样策略解决排列歧义问题，下游任务联合评估设计完整。

---

## [3] Fréchet Distance Loss on Speech Representations for Text-to-Speech Synthesis

**arXiv ID** 2607.06027 | **方向** 语音大模型

**作者** Ho-Lam Chung, Kuan-Po Huang, Bo-Ru Lu, Hung-yi Lee

**机构** National Taiwan University

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06027 | **PDF** https://arxiv.org/pdf/2607.06027.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出Speech Representation Fréchet Distance loss (SR-FD)，一种用于少步扩散/流匹配TTS的训练时分布正则化器。核心思想是在微调时使用与部署相同的少步采样器合成语音，然后通过SR-FD将合成语音的Whisper和CTC特征均值和协方差与离线计算的三种互补内容目标的参考统计量匹配。该损失无需判别器，推理时无额外计算量。在Seed-TTS English上，四步SR-FD微调将WER从2.2279%降至1.4147%（相对降低36.5%），且超越原始十步基线的1.7366%。

### 🔧 技术方案

**模型架构** 基于Tokenizer-free流匹配自回归TTS，使用few-step sampler进行推理。SR-FD在训练时对合成语音提取Whisper和CTC特征，计算与参考统计量的Fréchet距离。

**核心创新** 训练时分布正则化：使用与推理相同的few-step sampler合成语音，计算语音表征的Fréchet距离。三种互补内容目标提供多角度参考。无需判别器，推理时无额外开销。

**训练策略** SR-FD作为辅助损失函数，与条件流匹配、重建和停止预测损失联合优化。参考统计量离线计算。推理时使用32步或4步ODE采样。

### 📊 实验结果
**数据集** Seed-TTS English评估

**主要指标** 四步WER从2.2279%降至1.4147%（相对降低36.5%），超越原始十步基线1.7366%。说话人相似度和质量代理保持十步水平。

**是否开源** 暂未发布

### ⭐ 评分：8/10
SR-FD损失函数设计巧妙，解决少步TTS的分布匹配问题，实验验证充分（bootstrap显著性检验），且无需推理开销。

---

## [4] Escaping the Procrustean Bed: Groupwise Orthogonal Connectors for Audio-Language Models

**arXiv ID** 2607.06014 | **方向** 语音大模型

**作者** Ho-Lam Chung, Ke-Han Lu, Yi-Cheng Lin, Guan-Ting Lin, Yiming Chen, Hung-yi Lee

**机构** National Taiwan University

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06014 | **PDF** https://arxiv.org/pdf/2607.06014.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文揭示音频-语言模型中Q-Former连接器的两个失效问题：输出向量向单一方向塌缩，不同说话人的输出几乎无法区分，韵律等副语言线索在压缩过程中丢失。提出ORCA方法，通过将查询分组并约束各组输出指向不同方向来逆转这种塌缩。在SAKURA多跳推理任务上，ORCA相比4B基线提升26.4点，达到75.2%（vs 8B Audio Flamingo-3的49.0%）。连接器层面，查询冗余度降低12倍，跨说话人方差提升75倍。

### 🔧 技术方案

**模型架构** 基于Q-Former的音频-语言模型连接器，将语音编码器输出压缩后送给大语言模型。ORCA将查询分组，各组输出被约束指向不同方向。

**核心创新** 分组正交约束：将查询分成多组，约束各组输出向量正交，指向不同方向。这防止输出塌缩到单一方向，保持不同说话人的差异性。

**训练策略** 通过正交性约束损失训练，使各组查询输出在空间中分散。保留语音编码器和LLM冻结，只训练连接器。

### 📊 实验结果
**数据集** SAKURA多跳推理benchmark

**主要指标** ORCA在SAKURA上达75.2%（vs 4B基线49.0%，8B Audio Flamingo-3 49.0%）。查询冗余降低12倍，跨说话人方差提升75倍。

**是否开源** 暂未发布

### ⭐ 评分：8/10
诊断问题深入，创新解法针对性强（正交约束），实验覆盖充分（单跳、多跳、说话人变化），对音频-语言模型有重要指导意义。

---

## [5] SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models

**arXiv ID** 2607.05365 | **方向** 语音大模型

**作者** Thomas Thebaud, Yuzhe Wang, Hao Zhang, Sathvik Manikantan Napa Ugandhar, Ashish Hallur, Georgi Tinchev, Venkatesh Ravichandran, Laureano Moro-Velazquez

**机构** 论文未提供机构信息（匿名提交）

**发布日期** 2026-07-06 | **论文** https://arxiv.org/abs/2607.05365 | **PDF** https://arxiv.org/pdf/2607.05365.pdf | **代码** https://anonymous.4open.science/r/SPEAR-benchmark-code-anon-F4F1 | **Demo** https://anonymous.4open.science/w/SPEAR-benchmark-website-anon-82FE

### 📌 简介
本文提出SPEARBench，用于评估流式语音到语音语言模型的自然度。现有语音和文本基准无法捕捉这些系统在对话中的自然行为（时序、轮换、韵律、立场、语言/方言一致性、关系适当性）。SPEARBench从Seamless Interaction语料库构建受控对话提示，通过多维协议评估响应延迟、打断、语音质量、ASR鲁棒性、语言/方言一致性、情感自然度、人际立场等维度。包含人类答案作为参考条件，报告多个当代模型结果。当前模型可达到高信号级质量和低ASR错误，但在延迟、重叠、方言保持、情感适应和人际立场动态上仍与人类对话行为有差距。

### 🔧 技术方案

**模型架构** 流式语音到语音语言模型评测框架，从Seamless Interaction语料库提取对话提示，控制变量构建评测集。

**核心创新** 多维自然度评测协议：覆盖响应延迟、打断、语音质量、ASR鲁棒性、语言/方言一致性、情感自然度、人际立场等多个维度。与仅关注信号质量的现有基准不同。

**评测策略** 运行多个模型推理，使用多维协议评估生成答案。包含人类原始答案作为参考对比。

### 📊 实验结果
**数据集** Seamless Interaction语料库

**主要指标** 当前模型在信号级质量和ASR错误率上表现良好，但在对话自然度维度（延迟、重叠、方言、情感、立场）上与人类仍有显著差距。

**是否开源** 代码已开源：https://anonymous.4open.science/r/SPEAR-benchmark-code-anon-F4F1

### ⭐ 评分：7/10
首个流式语音到语音模型自然度评测基准，多维评测设计全面，开源有利于社区发展。

---

## [6] Goodbye Equal Error Rate, Hello Local Information Disclosure: Evaluating Voice Anonymisation against 1-to-N Linkage Threats

**arXiv ID** 2607.06259 | **方向** 语音大模型

**作者** Dāvis Šterns, Konstantinos Drossos, Natasha Fernandes, Tom Bäckström, Catuscia Palamidessi

**机构** Aalto University, Finland; Inria, France; Nokia, Finland; Macquarie University, Australia

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06259 | **PDF** https://arxiv.org/pdf/2607.06259.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文针对语音匿名化的隐私评估框架提出根本性改进。现有隐私评估主要依赖EER（等错误率），但EER设计用于二值验证（1-to-1比对），与现实世界的N选一数据库链接攻击存在威胁模型不匹配。本文提出Local Information Disclosure (LID)框架，核心指标LID以比特为单位量化单次试验的话语隐私损失。在VoicePrivacy 2024 Challenge系统上评估，发现看似EER达48%的系统仍存在最坏情况下1比特的局部泄露（相当于随机猜测成功率翻倍）。

### 🔧 技术方案

**模型架构** 信息论评估框架，针对1-to-N链接攻击威胁模型设计。将原始相似度分数校准为攻击者对每个注册身份的后验置信度。

**核心创新** LID指标：量化单次试验话语的精确隐私损失，以比特为单位。相比EER的全局聚合，LID能捕捉局部隐私失效。支持模块化设计，可组合不同系统评估。

**评测策略** 在VoicePrivacy 2024 Challenge系统上验证，分析全局EER与局部LID的差异。揭示看似良好的全局指标可能掩盖局部失效。

### 📊 实验结果
**数据集** VoicePrivacy 2024 Challenge评测系统

**主要指标** 看似EER达48%的系统在局部最坏情况下仍有1比特LID泄露，有效使攻击成功率翻倍。

**是否开源** 暂未发布

### ⭐ 评分：7/10
隐私评测框架的实质性改进，LID指标设计合理，揭示了全局指标的局限性，对语音隐私研究有重要指导意义。

---

## [7] Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts

**arXiv ID** 2607.06611 | **方向** 语音大模型

**作者** Andrei-George Durdun, Victor Constantinescu, Radu Tudor Ionescu

**机构** 论文未提供机构信息

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06611 | **PDF** https://arxiv.org/pdf/2607.06611.pdf | **代码** https://github.com/andreidurdun/cross-modal-audio-sentiment | **Demo** 暂无

### 📌 简介
本文提出基于蒸馏和多语言转录本跨模态融合的音频情感分析方法。核心方案是通过ASR自动生成转录本，并将其翻译成多种语言创建多文本模态。音频和多语言文本特征通过级联架构的跨模态Transformer块逐个整合。多模态模型（教师）的知识蒸馏到单模态（音频仅）学生模型。实验证明自动生成的文本信息能显著提升多模态情感分类性能，消融实验确认自动转录和自动翻译都有帮助，蒸馏可增强音频仅模型性能且推理时无额外计算开销。

### 🔧 技术方案

**模型架构** 多模态融合框架：音频特征提取、ASR转录、多语言机器翻译、跨模态Transformer融合。教师-学生蒸馏架构。

**核心创新** 多语言文本生成：自动转录 + 多语言翻译，创建多文本模态补充音频信息。跨模态Transformer级联整合各模态。蒸馏将多模态知识迁移到单模态学生模型。

**训练策略** 两阶段训练：先训练多模态教师模型，再蒸馏到音频仅学生模型。推理时学生模型仅需音频输入，无计算开销。

### 📊 实验结果
**数据集** 大规模情感分类数据集（具体名称未披露）

**主要指标** 自动文本信息显著提升多模态分类性能，消融实验验证转录和翻译的贡献。蒸馏后音频仅模型性能提升。

**是否开源** 代码已开源：https://github.com/andreidurdun/cross-modal-audio-sentiment

### ⭐ 评分：7/10
跨模态融合和蒸馏策略设计合理，实验验证充分，开源代码利于复现。

---

## [8] Revisiting the Relation Between Language Model Perplexity and ASR Word Error Rate for Modern End-to-End Speech Recognition

**arXiv ID** 2607.05612 | **方向** 语音大模型

**作者** Mohammad Zeineldeen, Albert Zeyer, Haoran Zhang, Robin Schmitt, Ralf Schlüter, Hermann Ney

**机构** RWTH Aachen University, Germany

**发布日期** 2026-07-06 | **论文** https://arxiv.org/abs/2607.05612 | **PDF** https://arxiv.org/pdf/2607.05612.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文重新审视语言模型困惑度（PPL）与ASR词错误率（WER）之间的关系。传统观点认为PPL与WER在对数-对数空间呈近似线性关系，但现代端到端ASR系统挑战了这一假设：它们已内置语言建模能力，通常在没有外部LM的情况下评估，可通过不同识别策略与神经LM或LLM结合。本文研究外部LM是否仍能改进当前端到端ASR系统、PPL-WER关系是否仍保持线性、编码器上下文长度如何影响该关系、LLM困惑度是否符合神经LM趋势等。研究发现ILM（内部语言建模）减法改变了PPL-WER关系，解码器内部LM必须纳入考量。

### 🔧 技术方案

**模型架构** 现代端到端ASR系统（具体架构未详述），可结合外部神经LM或LLM，使用不同识别策略。

**核心创新** 系统性重新评估PPL-WER关系的多方面问题。引入ILM减法分析，揭示解码器内部LM对PPL-WER关系的影响。

**评测策略** 在多个ASR系统上实验，系统性分析外部LM贡献、关系线性假设、编码器上下文影响、LLM困惑度趋势等。

### 📊 实验结果
**数据集** 标准ASR评估基准（具体名称未披露）

**主要指标** ILM减法改变PPL-WER关系，表明解码器内部LM需纳入考量。外部LM在某些场景仍有贡献。

**是否开源** 暂未发布

### ⭐ 评分：7/10
系统性重新评估经典问题，设计严谨，对理解现代ASR系统中LM的作用有重要价值。

---

## 🎙️ 语音前端

---

## [9] InsideSSL: Understanding Self-Supervised Speech Representations using a Model-Centric Perspective

**arXiv ID** 2607.06392 | **方向** 语音前端

**作者** Samir Sadok, Xavier Alameda-Pineda

**机构** Inria, Université Grenoble Alpes CNRS, LJK, France

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06392 | **PDF** https://arxiv.org/pdf/2607.06392.pdf | **代码** https://insideSSL.github.io/ | **Demo** https://samsad35.github.io/audio-ssl-dynamics-site/

### 📌 简介
本文提出InsideSSL框架，从模型中心视角理解自监督语音表示的层级动态。框架分两部分：建立任务无关分析，从压缩（熵）、几何（曲率）、扰动鲁棒性三个固有层级视角分析；提出跨层生成兼容性矩阵（GCM）评估功能可迁移性，揭示稳定音素核心、身份可变性和深层语义剪枝。此外线性探测将模型中心视角与下游任务连接，展示了层级拓扑如何决定音素、音高和说话人编码。

### 🔧 技术方案

**模型架构** Wav2Vec2、HuBERT、WavLM等SSL模型的分析框架。GCM矩阵评估跨层功能可迁移性。

**核心创新** 三维模型中心分析：压缩（entropy）、几何（curvature）、扰动鲁棒性。GCM揭示稳定音素核心、身份波动性、深层语义剪枝现象。

**训练策略** 预训练SSL模型分析。线性探测连接模型层拓扑与下游任务（音素、音高、说话人编码）。

### 📊 实验结果
**数据集** 多种下游任务评估

**主要指标** 揭示不同训练目标诱导不同的声学压缩和流形展开机制。层级拓扑决定音素、音高、说话人编码。实验验证框架有效性。

**是否开源** 代码和项目页已开源：https://insideSSL.github.io/

### ⭐ 评分：7/10
自监督语音表示分析的创新框架，三维分析视角全面，GCM矩阵设计巧妙，有助于理解SSL模型的内部工作机制。

---

## [10] Distributed Multichannel Wiener Filtering for Topology-Unconstrained Wireless Acoustic Sensor Networks

**arXiv ID** 2607.05561 | **方向** 语音前端

**作者** Paul Didier, Pourya Behmandpoor, Henri Gode, Toon van Waterschoot, Simon Doclo, Jörg Bitzer, Marc Moonen

**机构** 论文未提供机构信息

**发布日期** 2026-07-06 | **论文** https://arxiv.org/abs/2607.05561 | **PDF** https://arxiv.org/pdf/2607.05561.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出拓扑无关的分布式多通道Wiener滤波器（TI-dMWF），用于无约束拓扑的无线声学传感器网络（WASNs）分布式节点特定信号估计。TI-dMWF使每个节点仅通过交换低维融合信号即可计算集中式多通道Wiener滤波器解，无需迭代估计（不同于TI-DANSE算法）。当每个源被所有节点或仅一个节点观测时，TI-dMWF是最优的。理论分析和数值仿真确认其在单次运行中达到集中式估计性能。

### 🔧 技术方案

**模型架构** 分布式多通道Wiener滤波框架，网络中各节点通过交换低维融合信号计算滤波器。

**核心创新** 拓扑无关设计：无需网络拓扑信息，无需迭代，单次运行达到集中式性能。与TI-DANSE的迭代估计形成对比。

**训练策略** 理论证明最优性：在每个源被所有节点或仅一个节点观测的假设下。分析延迟和计算复杂度。

### 📊 实验结果
**数据集** 仿真实验（混响房间）

**主要指标** 在理论最优条件下达到集中式估计性能。分析延迟（与修剪树深度相关）和计算复杂度。鲁棒性评估通过仿真验证。

**是否开源** 暂未发布

### ⭐ 评分：6/10
分布式语音增强的理论贡献，单次运行达到最优性能有重要意义，但实验主要基于仿真。

---

## [11] Few-Shot Class-Incremental Audio Classification Using Pseudo-Incrementally Trained Embedding Learner and Continually Updated Stochastic Classifier

**arXiv ID** 2607.05953 | **方向** 语音前端

**作者** Yanxiong Li, Wenchang Cao, Jiaxin Tan, Qianqian Li, Guoqing Chen

**机构** 论文未提供机构信息

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.05953 | **PDF** https://arxiv.org/pdf/2607.05953.pdf | **代码** https://github.com/vinceasvp/PITEL-CUSC | **Demo** 暂无

### 📌 简介
本文研究少样本增量音频分类（FCAC），目标是用少量标注样本逐步识别增量类，同时记忆基础类。模型需要高稳定性（记忆基础类）和强可塑性（适应增量类）。设计模型由两个独立模块组成：嵌入学习器（残差卷积网络骨干）和随机分类器（每类由均值向量和方差向量组成的分布）。基础会话训练后，嵌入学习器在各增量会话中不更新以记忆基础类知识，而随机分类器持续更新以适应增量类。通过伪增量训练策略和数据增强提升嵌入学习器对增量类的表示能力。实验在FSC-89、NSynth-100和LS-100三个数据集上验证。

### 🔧 技术方案

**模型架构** 解耦设计：嵌入学习器（残差卷积网络骨干）+ 随机分类器（均值和方差向量分布）。

**核心创新** 伪增量训练策略：嵌入学习器在基础会话中通过数据增强伪增量训练，增强对增量类的表示能力。随机分类器持续更新适应新类。

**训练策略** 基础会话：联合训练嵌入学习器和随机分类器。增量会话：冻结嵌入学习器，更新随机分类器。

### 📊 实验结果
**数据集** FSC-89、NSynth-100、LS-100

**主要指标** 准确率超过对比方法，计算复杂度低于大多数对比方法。

**是否开源** 代码已开源：https://github.com/vinceasvp/PITEL-CUSC

### ⭐ 评分：6/10
少样本增量学习的有效方法，解耦设计和伪增量训练策略合理，开源有利于复现。

---

## 📋 其他论文（快速浏览）

### 语音大模型

### 语音前端

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*