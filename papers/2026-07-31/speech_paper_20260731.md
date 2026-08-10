# 2026-07-31 语音论文速递

**共收录**: 4 篇 | **语音大模型**: 3 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 4 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

---

## [1] WeSep: A Modular and Cue-Composable Framework for Target Speaker Extraction

**arXiv ID** 2607.27436 | **方向** 语音大模型

**作者：** Ke Zhang, Xiaoyang Yu, Haoyu Li, Shuai Wang, Shuhan Zhang, Haizhou Li

**机构：** SAI, The Chinese University of Hong Kong, Shenzhen; Nanjing University, China; Shenzhen Loop Area Institute

**发布日期:** 2026-07-29 | **论文** https://arxiv.org/abs/2607.27436 | **PDF** https://arxiv.org/pdf/2607.27436.pdf | **代码** https://github.com/wenet-e2e/WeSep | **Demo** 暂无

### 📌 简介
目标说话人提取(TSE)旨在给定辅助线索的情况下，从混合语音中分离出目标说话人。现有系统通常针对特定线索类型设计，限制了场景变化时的灵活性。本文提出WeSep统一框架，将TSE重新表述为异构线索条件学习问题。

### 🔧 技术方案

**模型架构：** 模块化架构，包含数据抽象、线索前端、分离器骨干网和顶层组合四个部分。通过标准化接口解耦线索模块和分离器骨干网，支持可配置的线索注入和灵活的多模态集成。

**核心创新：** 1) 将TSE重新表述为异构线索条件学习问题，统一单线索和多线索设置；2) 结构化模内线索建模，支持对不同线索实例及其组合进行可控研究；3) 可组合多线索集成，在单一可配置架构中即插即用组合多个线索；4) 样本级异构训练管道，支持统一数据和优化管道下的异构线索配置。

**训练策略：** 支持异构线索配置的联合优化框架，动态模拟真实世界中线索可用性变化。

### 📊 实验结果

**数据集：** 在enrollment、spatial、visual、textual四种线索类型上进行了广泛实验。

**主要指标：** 实验揭示了模态依赖特性，证明了在异构线索可用性下稳定优化的能力。框架支持 enrollment cue (说话人注册)、spatial cue (空间信息)、visual cue (视觉信号)、textual cue (文本描述) 四种线索的灵活组合。

**是否开源：** 代码将公开发布于 https://github.com/wenet-e2e/WeSep

### ⭐ 评分：8/10
模块化设计思路新颖，解决了实际场景中线索可用性动态变化的难题，对语音分离和说话人提取领域有重要参考价值。

---

## [2] Enhancing Law-Enforcement Audio Transcription: A LoRA-Based Adaptation of Whisper for BWC Footage

**arXiv ID** 2607.27245 | **方向** 语音大模型

**作者：** Vivek Senthil, Zhiqiang Tao, Ernest Fokoué

**机构：** Rochester Institute of Technology (RIT), USA

**发布日期:** 2026-07-27 | **论文** https://arxiv.org/abs/2607.27245 | **PDF** https://arxiv.org/pdf/2607.27245.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
执法机构拥有大量随身摄像头(BWC) footage，但人工转录成本高昂。本文提出使用Low-Rank Adaptation (LoRA)对OpenAI Whisper模型进行参数高效微调，以适应执法环境的声学和语言挑战。

### 🔧 技术方案

**模型架构：** 基于Transformer的Encoder-Decoder架构，采用Whisper-base模型。输入原始音频转换为log-Mel频谱图，输出对应文本token。

**核心创新：** 1) 使用LoRA进行参数高效微调，仅训练0.3%的模型参数；2) 针对执法环境特有的词汇（如"10-52"、"Mirandize"等）进行领域适配；3) 在消费级硬件(NVIDIA 4GB GTX GPU)上使用8-bit量化和梯度检查点实现训练。

**训练策略：** LoRA rank设置为r=8, 16, 32，scaling factor α=32，dropout率0.05。使用RIT Research Computing的NVIDIA A100 20GB GPU进行训练。

### 📊 实验结果

**数据集：** 53个执法随身摄像头视频，42个训练样本，5个验证样本，6个测试样本。

**主要指标：** 
- 相对WER降低：39.7%
- LoRA rank r=8 为最优配置，在捕获领域特定声学模式的同时避免过拟合

**与基线对比：**
- Zero-shot Whisper-base: 基线性能
- Fully Fine-tuned Whisper-base: 全参数微调
- LoRA-adapted (r=8): 最佳性能，39.7%相对WER降低

**是否开源：** 暂未开源

### ⭐ 评分：8/10
针对特定领域(执法)的ASR微调工作，实战价值明显，LoRA参数高效微调方法具有普适性。

---

## [3] Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments with Turn Action GRPO

**arXiv ID** 2607.27756 | **方向** 语音大模型

**作者：** Xilin Jiang, Riki Shimizu, Sukru Samet Dindar, Junkai Wu, Zhongweiyang Xu, Nima Mesgarani

**机构：** Columbia University, USA

**发布日期:** 2026-07-30 | **论文** https://arxiv.org/abs/2607.27756 | **PDF** https://arxiv.org/pdf/2607.27756.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
现实社交环境中的对话通常是多人参与且伴有噪音，语音助手需要决定是否响应、继续倾听还是忽略。本文提出Cocktail-Talker框架，通过三种turn action tokens (respond, listen, ignore) 让语音LLM在复杂社交场景中自然地选择行为。

### 🔧 技术方案

**模型架构：** 语音LLM框架，使用三个action token：`<|respond|>`、`<|listen|>`、`<|ignore|>`，放在响应或静音之前。

**核心创新：** 1) 提出多说话人单助手口语对话建模问题；2) 设计三种turn action tokens决定是否响应；3) 开发Cocktail-DialogGen数据管道，模拟真实多说话人对话场景；4) 使用GRPO (Group Relative Policy Optimization) 进行强化学习训练。

**数据管道：** 模拟环境包括18种seen和10种unseen环境，涵盖室内、室外、交通场景。每个对话有3-4名说话人，支持ASSISTING和CASUAL两种对话风格，支持Named和Anonymous两种命名策略。

**训练策略：** 监督微调 + GRPO强化学习。生成14,400个独特对话，72,000个带噪音频混合物。

### 📊 实验结果

**数据集：** 
- 训练：18环境 × 2风格 × 2命名策略 × 2说话人数 × 100对话 = 14,400对话
- 5种噪声水平混合 = 72,000个带噪音频混合物 (约1,280小时)
- 测试：seen环境1,440对话/7,200混合物，unseen环境800对话/4,000混合物

**主要指标：** 
- 环境SNR范围：0-3dB, 3-6dB, 6-9dB, 9-12dB, clean
- 对话能量：助手-20dB RMS，其他人-20±5dB RMS

**是否开源：** 暂未开源

### ⭐ 评分：8/10
创新性地提出语音助手在鸡尾酒会场景下的行为决策问题，数据模拟和训练方法具有参考价值。

---

## 语音前端

---

## [4] Does EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding

**arXiv ID** 2607.27268 | **方向** 语音前端

**作者：** Owais Mujtaba Khanday, Mohamed Baha Ben Ticha, Sanae Belfrouh, Marc Ouellet, Jose A. Gonzalez-Lopez

**机构：** University of Granada, Spain; Research Centre for Information and Communication Technologies (CITIC-UGR), Spain; University of Chouaib Doukkali, Morocco; Brain, Mind, and Behavior Research Center (CIMCYC), University of Granada, Spain

**发布日期:** 2026-07-29 | **论文** https://arxiv.org/abs/2607.27268 | **PDF** https://arxiv.org/pdf/2607.27268.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
EEG基础模型在数千小时数据上预训练，在运动 imagery、癫痫检测、睡眠分期、情绪识别等任务上取得进展，但其向语音解码的迁移效果尚未被系统验证。本文首次系统性地对EEG基础模型与CNN基线在语音解码任务上进行基准测试。

### 🔧 技术方案

**模型架构：** 
- 基础模型：EEGNet (16K参数), ShallowFBCSPNet (162K参数), EEGConformer (406K参数)
- 基础模型：LaBraM (~5.8M参数，2500小时EEG预训练), EEGMamba (~16,000小时EEG预训练)

**核心创新：** 1) 首次系统性地对EEG基础模型vs卷积基线进行语音/语言解码基准测试；2) 评估覆盖overt、covert、imagined speech三种模式；3) 使用统一预处理和微调协议确保公平比较。

**数据集：**
- UGR-MINDVOICE: 64通道EEG，15名说西班牙语者，22个sessions，包含overt和covert speech
- BCI Competition 2020 Track 3: 64通道EEG，15名受试者，5个imagined speech词汇

**预处理：** 使用MNE-Python和MNE-BIDS进行数据处理，应用0.1-75Hz带通滤波和50Hz陷波，ICA去除眼动伪迹，公共平均参考，重采样到200Hz。

### 📊 实验结果

**主要发现：** 大规模EEG预训练并没有一致性地优于16K参数的CNN，揭示当前通用EEG预训练尚未迁移到语音生产任务。

**UGR-MINDVOICE结果（LOSO协议）：**
- Speech Mode (3类): EEGNet Acc 61.3%, W-F1 0.607
- Semantic Category (6类): EEGNet Acc 19.9%, W-F1 0.186
- Word (60类): EEGNet Acc 2.8%, W-F1 0.019

**结论：** 当前通用EEG预训练不能迁移到语音解码任务，需要专门针对语音的基础模型。

### ⭐ 评分：7/10
首个EEG基础模型语音解码基准测试，结论具有启发性，为BCI和语音解码领域指明方向。

---

今日语音论文速递
