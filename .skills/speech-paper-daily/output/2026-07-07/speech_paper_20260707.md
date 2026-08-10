# 2026-07-07 语音论文速递

**共收录**: 6 篇 | **语音大模型**: 3 篇 | **语音前端**: 3 篇

> 今日 arXiv 语音相关论文共命中 6 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] Lychee-FD: Hierarchical Acoustic-Semantic Modeling for Full-Duplex Spoken Language Models

**arXiv ID** 2607.06540 | **方向** 语音大模型

**作者** Zhenyu Liu, Yunxin Li, Xuanyu Zhang, Qixun Teng, Shenyuan Jiang, Haolan Chen, Minjun Zhao, Fanbo Meng, Yu Xu, Yancheng He, Baotian Hu, Haizhou Li, Min Zhang

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06540 | **PDF** https://arxiv.org/pdf/2607.06540.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
开发高性能全双工口语语言模型(SLM)仍是语音和NLP领域的重要挑战。尽管已有进展，但现有方法受制于严重的模态干扰问题，导致知识退化、语义完整性受损，使全双工SLM显得不自然和不够智能。本文通过精细分析模型优化动态，揭示了性能退化的根本原因： acoustic和semantic建模在被迫共享深层参数空间时存在固有的梯度冲突。基于这一洞察，提出Lychee-FD，一个原生端到端全双工框架。核心是层次化参数分离策略，在深层解耦冲突模态，同时通过专用语义对齐通道保持跨模态一致性。在多个全双工基准上的实验表明，该方法显著推进了SOTA：在语音智能(Spoken QA上+7.4%)和全双工交互流畅性(FullDuplexBench 1.5上+28.5%)方面取得大幅提升，同时不损失推理效率。这是首个揭示并阐明全双工SLM模态干扰根本原因的工作，并设计了优雅的层次化模型和实用解决方案。

### 🔧 技术方案

**模型架构** Lychee-FD采用原生端到端全双工架构，包含两个核心组件：(1)层次化参数分离模块：在深层将acoustic和semantic建模解耦；(2)语义对齐通道：专门设计用于保持跨模态一致性。模型基于Transformer架构，针对全双工语音交互优化。

**核心创新** (1)揭示根因：通过优化动态分析，发现模态干扰源于共享深层参数空间导致的梯度冲突；(2)层次化参数分离：在深层解耦acoustic和semantic建模路径；(3)语义对齐通道：通过专用通道维持跨模态一致性而不损失效率。

**全双工特性** 支持同时听说的自然交互流，低延迟响应，保持语义连贯性。

### 📊 实验结果
**数据集** 多个全双工基准测试，包括FullDuplexBench 1.5和Spoken QA。

**主要指标** Spoken QA上+7.4%，FullDuplexBench 1.5上+28.5%的交互流畅性提升。推理效率与基线相当。

**对比基线** 显著优于先前的全双工SLM方法，解决模态干扰问题。

### ⭐ 评分：9/10
Lychee-FD通过深入分析揭示了全双工SLM的性能瓶颈根源，层次化参数分离策略设计优雅且有效。实验结果在语音智能和交互流畅性两方面均有显著提升。该工作对全双工语音交互系统的设计有重要指导意义。

---

## [2] WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for LLM-Based TTS

**arXiv ID** 2607.06461 | **方向** 语音大模型

**作者** Sihang Nie, Jinxin Ji, Xiaofen Xing, Deyi Tuo, Chengbin Jin, Jialong Mai, Xiangmin Xu

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06461 | **PDF** https://arxiv.org/pdf/2607.06461.pdf | **代码** https://xxh333.github.io/wordvoice-demo/ | **Demo** https://xxh333.github.io/wordvoice-demo/

### 📌 简介
尽管近年基于LLM的TTS系统达到了显著的自然度，但它们主要依赖隐式端到端生成范式，导致粗粒度控制。在需要精确风格干预和严格时间对齐的场景(如有声书配音和视频配音)中，无法显式操控词级声学属性仍是关键瓶颈。这一限制主要由细粒度标注数据集的严重稀缺和多维控制信号融入离散自回归生成的架构挑战所加剧。提出WordVoice框架：首先构建WordVoice-5A，一个4.7k小时的双语数据集，具有五维词级标注(时长、边界、能量、音高和语调)，通过严格的语言学引导流程开发；其次引入WordVoice，将隐式生成过程转换为显式、高度可控的范式。具体而言，引入bound-token机制实现显式"声学规划"过程，支持自适应多任务韵律规划和灵活人工干预；在token-to-waveform阶段增添加细粒度声学调制模块，桥接高度压缩离散token与连续波形之间的分辨率差距。大量实验证明WordVoice在保持竞争力的零样本合成稳定性的同时，实现了对多声学维度的优越解耦控制。

### 🔧 技术方案

**模型架构** WordVoice基于LLM的TTS架构，包含两个核心创新：(1)bound-token机制：在LLM中引入边界token，实现显式声学规划；(2)细粒度声学调制模块：在token-to-waveform阶段桥接离散token与连续波形。

**核心创新** (1)WordVoice-5A数据集：4.7k小时双语数据，五维词级标注(时长、边界、能量、音高、语调)；(2)显式声学规划：通过bound-token实现可干预的韵律规划；(3)细粒度声学调制：解决离散token到连续波形之间的分辨率gap；(4)解耦控制：支持多维声学属性的独立控制。

**训练策略** 严格语言学引导的标注流程，确保五维标注的准确性和一致性。

### 📊 实验结果
**数据集** WordVoice-5A(4.7k小时)，以及标准TTS评估基准。

**主要指标** 多维声学属性的解耦控制精度，零样本合成稳定性保持。实验验证了WordVoice在word-level控制的优越性和解耦能力。

**代码开源** 代码和音频样本已公开：https://xxh333.github.io/wordvoice-demo/

### ⭐ 评分：9/10
WordVoice解决了LLM-based TTS的细粒度控制难题，五维词级标注数据集是重要贡献。bound-token机制和声学调制模块设计精巧。代码开源便于复现。强烈推荐关注。

---

## [3] BlueMagpie-TTS: A Token-Efficient Tokenizer, Language Model, and TTS for Taiwanese-Accent Code-Switching Speech

**arXiv ID** 2607.06054 | **方向** 语音大模型

**作者** Ho Lam Chung, Bo-Xuan Zheng, Cheng-Chieh Huang, Cheng-Han Chang, Jung-Ching Chen, Lok-Lam Ieong, Ting-Lin Hsiao, Yu-Cheng Lee, Yi-Hsin Chung, Yu-Kai Guo, Hung-yi Lee

**机构** National Taiwan University

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06054 | **PDF** https://arxiv.org/pdf/2607.06054.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
现有TTS系统对台湾口音的适配较差：口音默认使用其他普通话变体，分词器对常见台湾文本过度细分，且在中文英文交替的代码切换边界处发音退化。这些问题有一个共同根源：文本侧缺乏对台湾情境的适配。从底层解决文本侧问题。PangolinTokenizer，一个在台湾情境数据上训练的字节级BPE分词器，达到最低token率(0.485 tokens/字符)，在九个分词器中 vocabulary最小。Barbet，一个基于PangolinTokenizer的十亿参数繁体中文语言模型，作为文本语义前端，在14任务评估中位居同类公开模型第一。BlueMagpie-TTS将Barbet通过学习型bridge连接到VoxCPM2的预训练声学堆栈，保持声学堆栈固定。在1000句台湾本地化测试集上，BlueMagpie-TTS将CER从11.45%降至4.81%，WER从14.83%降至5.36%，相对减少58.0%和63.9%。在500句盲听测试中(10位听众)，65.6%的多数票偏好BlueMagpie-TTS。

### 🔧 技术方案

**模型架构** BlueMagpie-TTS包含三个核心组件：(1)PangolinTokenizer：字节级BPE分词器，0.485 tokens/字符的最低token率；(2)Barbet：十亿参数繁体中文LM，基于PangolinTokenizer，14任务评估第一；(3)声学堆栈：基于VoxCPM2，通过learned bridge连接。

**核心创新** (1)台湾情境适配：从文本侧底层解决口音适应问题；(2)高效分词器：PangolinTokenizer以最小vocabulary达到最低token率；(3)Learned bridge：连接文本语义前端和声学后端，保持声学堆栈固定实现稳定。

**性能指标** CER相对减少58.0%，WER相对减少63.9%，65.6%盲听偏好率。

### 📊 实验结果
**数据集** 1000句台湾本地化测试集。

**主要指标** CER: 11.45%→4.81% (58.0%相对减少)，WER: 14.83%→5.36% (63.9%相对减少)，盲听偏好65.6%。

**盲听实验** 10位听众，500句，65.6%多数票偏好BlueMagpie-TTS。

### ⭐ 评分：8/10
BlueMagpie-TTS针对台湾口音code-switching场景进行了全面优化，从分词器到语言模型到TTS的系统性适配。实验数据充分，盲听结果有说服力。Hung-yi Lee团队的工作一贯高质量。

---

## 🤖 语音前端

---

## [4] Flowley: Precise Video-to-Audio Generation with Cross-Modal Alignment in Latent Space

**arXiv ID** 2607.06405 | **方向** 语音前端

**作者** Thanh V. T. Tran, Ngoc-Son Nguyen, Luong Tran, Long-Khanh Pham, Paarth Neekhara, Shezheen Hussain, Van Nguyen

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06405 | **PDF** https://arxiv.org/pdf/2607.06405.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
视频到音频(V2A)生成旨在为无声视频合成语义一致且时间同步的真实音频。尽管已有进展，许多方法仍依赖多阶段训练，导致高计算成本和长推理时间；或先将视觉输入转换为文本以利用预训练的文本到音频模型，这牺牲了细粒度时间线索。提出Flowley，一个端到端单阶段训练架构，通过结合视觉特征和文本提示生成配乐。核心创新是渐进式软掩码交叉注意力(Progressive Soft-masked Cross-Attention)，将音视频同步直接嵌入注意力机制，相比标准注意力层零额外计算成本。进一步观察到现有V2A基准缺乏面向声音的描述性caption，这可能降低合成音频质量。因此提出SoundCap，一个即插即用的pipeline，用于创建详细的、声音感知的caption来指导模型。值得注意的是，Flowley无需集成任何预训练音视频对齐模块，即在VGGSound上实现SOTA性能。此外，通过集成SoundCap，在零样本设置下进一步超越了最强闭源方法的音频质量。

### 🔧 技术方案

**模型架构** Flowley基于端到端单阶段架构，结合视觉特征和文本提示生成音频。核心是Progressive Soft-masked Cross-Attention机制。

**核心创新** (1)端到端单阶段：无需多阶段训练，降低计算成本；(2)渐进式软掩码交叉注意力：将音视频同步直接嵌入注意力机制，零额外计算成本；(3)SoundCap：面向声音的caption生成pipeline，弥补现有基准的不足。

**技术细节** 在注意力机制中引入soft-mask，逐步增强音视频对齐，渐进式提升同步精度。

### 📊 实验结果
**数据集** VGGSound等V2A基准。

**主要指标** 在VGGSound上实现SOTA，集成SoundCap后零样本设置下超越最强闭源方法的音频质量。

**对比基线** 优于现有V2A方法，无需预训练音视频对齐模块。

### ⭐ 评分：8/10
Flowley通过创新的注意力机制解决了V2A的时序同步问题，单阶段训练提高效率。SoundCap弥补了数据集的空白。ECCV 2026接收表明其创新性获得认可。

---

## [5] InsideSSL: Understanding Self-Supervised Speech Representations using a Model-Centric Perspective

**arXiv ID** 2607.06392 | **方向** 语音前端

**作者** Samir Sadok, Xavier Alameda-Pineda

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06392 | **PDF** https://arxiv.org/pdf/2607.06392.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
自监督学习(SSL)模型(如Wav2Vec2、HuBERT和WavLM)已成为各种语音和音频任务的基础。尽管取得成功，理解其内部层间动态仍是持续挑战。提出InsideSSL，一个两部分的模型中心框架。第一部分：从三个内在的逐层视角建立任务无关分析：压缩率(entropy)、几何学(curvature)和扰动鲁棒性。结果表明不同训练目标诱导不同的声学压缩和流形展开机制。第二部分：引入跨层生成兼容性矩阵(GCM)来评估功能可迁移性，揭示稳定的音素核心、身份不稳定性和深层语义剪枝。除这些评估外，线性探测将模型中心视角与下游任务连接，展示了层拓扑如何决定音素、音高和说话人编码。该论文被INTERSPEECH 2026接受为long paper。

### 🔧 技术方案

**模型架构** InsideSSL提出两部分分析框架：(1)任务无关分析：从压缩率、几何学和扰动鲁棒性三个视角分析各层；(2)GCM：跨层生成兼容性矩阵，评估功能可迁移性。

**核心创新** (1)模型中心视角：不同于数据驱动，从模型内部特性理解SSL；(2)三层分析维度：压缩(entropy)、几何(curvature)、鲁棒性；(3)GCM矩阵：揭示稳定的音素核心、身份不稳定性和深层语义剪枝；(4)线性探测验证：将模型特性与下游任务连接。

**关键发现** 不同训练目标导致不同的声学压缩和流形展开机制；深层具有语义剪枝特性。

### 📊 实验结果
**数据集** 多种语音基准，包括音素识别、音高检测、说话人识别等下游任务。

**主要指标** 通过线性探测验证层拓扑与下游任务性能的关联，揭示了SSL模型的层级特化规律。

**论文接收** INTERSPEECH 2026 long paper。

### ⭐ 评分：8/10
InsideSSL提供了理解SSL语音模型的系统方法论，三层分析框架和GCM矩阵是创新性工具。INTERSPEECH接收验证了其学术价值。对SSL模型的设计和理解有重要贡献。

---

## [6] SR-FD: Fréchet Distance Loss on Speech Representations for Text-to-Speech Synthesis

**arXiv ID** 2607.06027 | **方向** 语音前端

**作者** Ho-Lam Chung, Kuan-Po Huang, Bo-Ru Lu, Hung-yi Lee

**机构** National Taiwan University

**发布日期** 2026-07-07 | **论文** https://arxiv.org/abs/2607.06027 | **PDF** https://arxiv.org/pdf/2607.06027.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
少步扩散和flow-matching TTS模型通常使用局部目标训练，如条件flow matching、重建和停止预测。这些损失提供稳定优化，但从未问询采样语音是否符合高质量语音的分布。提出Speech Representation Fréchet Distance loss (SR-FD)，一种用于无分词器flow-matching自回归TTS的训练时分布正则化器。在微调期间，模型使用与部署相同的少步采样器合成语音，SR-FD将冻结的Whisper和CTC特征的均值和协方差与离线从三个互补内容目标计算的参考统计量匹配。该损失无需判别器，也无需推理时计算。在Seed-TTS English上，四步SR-FD微调将原始四步VoxCPM2基线的WER从2.2279%降至1.4147%，相对减少36.5%，并且超越了原始十步基线的1.7366%。说话人相似度和客观质量代理保持在十步水平，错误分析显示增益来自所有提示长度下的内容替换。SR-FD因此成为少步TTS的 intelligibility-improving分布正则化器。

### 🔧 技术方案

**模型架构** SR-FD应用于无分词器flow-matching自回归TTS，结合Whisper和CTC特征计算分布损失。

**核心创新** (1)SR-FD损失：训练时分布正则化器，匹配Whisper和CTC特征的均值和协方差；(2)无需判别器：不同于GAN-based方法，SR-FD是纯重建目标；(3)推理时零计算成本：仅在训练时使用，不增加推理负担。

**技术细节** 离线计算三个互补内容目标的参考统计量，微调时匹配这些分布。

### 📊 实验结果
**数据集** Seed-TTS English基准。

**主要指标** 四步WER: 2.2279%→1.4147% (36.5%相对减少)，超越十步基线(1.7366%)。说话人相似度和质量保持十步水平。

**消融分析** 错误分析显示增益来自所有提示长度下的内容替换，证明SR-FD改进了内容准确性。

### ⭐ 评分：8/10
SR-FD巧妙地将Fréchet距离引入TTS训练，提供了一种无需判别器的分布正则化方法。实验结果显著，四步超越十步基线。Hung-yi Lee团队持续输出高质量工作。

---