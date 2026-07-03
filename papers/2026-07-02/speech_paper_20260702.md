# 2026-07-02 语音论文速递

**共收录**: 11 篇 | **语音大模型**: 6 篇 | **语音前端**: 5 篇

> 今日 arXiv 语音相关论文共命中 11 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis

**arXiv ID** 2607.00363 | **方向** 语音大模型

**作者** Yu Zuda, Xu Qianhui, Chen Ting, Zhang Junhui, Fu Tao, Yu Hongjiang, Wang Qiangqing, Song Yang

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00363 | **PDF** https://arxiv.org/pdf/2607.00363.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Flow Matching (FM) 作为语音生成的强大范式，但仍受高推理延迟和音色泄露问题困扰。针对这些瓶颈，本文提出统一引导框架，通过数据引导和模型引导两个互补策略提升生成效率和数据鲁棒性。数据引导通过异质增强解耦语言内容与声学残差，模型引导设计高效推理路径减少延迟。该框架在保持合成质量的同时显著提升效率。

### 🔧 技术方案

**模型架构** 基于Flow Matching的语音合成框架，通过统一引导框架增强生成效率。

**核心创新** Data-guidance（数据引导）：通过异质增强 disentangle 语言内容与声学残差，减少音色泄露。Model-guidance（模型引导）：设计高效推理路径减少延迟。

**训练策略** 双重引导策略协同训练，解决高推理延迟和音色泄露问题，实现鲁棒语音合成。

### 📊 实验结果
**数据集** 语音合成标准 benchmark。

**主要指标** 相比基线方法在保持质量的同时显著提升合成效率，有效解决音色泄露问题。

**是否开源** 暂无代码发布。

### ⭐ 评分：9/10
统一引导框架解决FM在语音合成的关键瓶颈，Data-guidance和Model-guidance双重策略创新性强，实验验证充分。

---

## [2] NPUsper: Eliminating Redundant Computation for Real-Time Whisper on Mobile NPUs

**arXiv ID** 2607.01108 | **方向** 语音大模型

**作者** Lee Sihyeon, Lee Hojeong, Woo Sungwon, Yan Chengpo, Banerjee Suman, Kim Seyeon

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.01108 | **PDF** https://arxiv.org/pdf/2607.01108.pdf | **代码** https://github.com/npusper/NPUsper | **Demo** 暂无

### 📌 简介
本文提出NPUsper，一个在移动NPU上实现Whisper高效实时转录的系统。为避免先前流式系统使用的大量padding，NPUsper通过decoder cross-attention的时序模式在线检测幻觉token，使每轮推理只需处理短音频输入和最小carryover。为高效执行移动NPU推理，提出controlled unrolling技术，将自回归解码执行为K-step chunk graphs，大幅减少KV-cache计算和图调度开销。

### 🔧 技术方案

**模型架构** 基于Whisper的实时转录系统，针对移动NPU优化。核心为幻觉token在线检测器。

**核心创新** 幻觉token在线检测：从decoder cross-attention时序模式检测幻觉token，实现短音频输入处理。Controlled Unrolling：将自回归解码执行为K-step chunk graphs，减少KV-cache计算和图调度开销。

**训练策略** 实时处理输入语音，每轮推理只需处理短音频和最小carryver，实现低延迟转录。

### 📊 实验结果
**数据集** 实时语音转录测试集。

**主要指标** 相比基线实现4.84x更低 per-word latency，33.2x更低 TTFT，88.64%更低平均功耗，同时保持相当转录精度。

**是否开源** 代码已发布：https://github.com/npusper/NPUsper

### ⭐ 评分：8/10
针对移动端Whisper实时转录的系统性优化工程，幻觉检测和controlled unrolling创新性强，实验数据详实。

---

## [3] A Geometric Perspective on Composable Emotion Steering in Text-to-Speech Models

**arXiv ID** 2607.00946 | **方向** 语音大模型

**作者** Wang Siyi, Bailey James, Dang Ting

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00946 | **PDF** https://arxiv.org/pdf/2607.00946.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
先前工作已探索混合TTS系统中的情感控制，但对这些模块的几何特性及其对可控性的影响尚缺乏理解。本文首次系统比较语音语言模型(SLM)和条件流匹配(CFM)模块作为激活steering位点用于混合情感语音合成的效果。使用线性探测和局部本征维度(LID)表征情感表示，评估单语和跨语言场景下的情感控制能力。

### 🔧 技术方案

**模型架构** 比较SLM和CFM模块作为激活steering sites用于混合情感语音合成。

**核心创新** 首次系统比较两种模块的混合情绪语音合成steerability。使用线性探测和局部本征维度(LID)表征情感表示，揭示几何属性对情绪控制的影响。

**训练策略** 通过激活steering实现混合情绪控制，无需重新训练模型，支持单语和跨语言场景。

### 📊 实验结果
**数据集** 混合情绪语音合成测试集。

**主要指标** 系统比较SLM和CFM模块的steerability，揭示几何属性对情绪控制的影响，为方法选择提供理论指导。

**是否开源** 暂无。

### ⭐ 评分：8/10
从几何视角理解情感控制的系统性研究，首次比较SLM和CFM模块的steerability，研究问题有启发性。

---

## [4] AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization

**arXiv ID** 2607.00726 | **方向** 语音大模型

**作者** Zhou Tianhong, Han Mingyang, Li Boyu, Jiang Yuxuan, Ye Jiaxin, Wang Dongxiao, Shi Haoxiang, Wang Kunpeng, Song Jun, Yu Cheng, Zheng Bo

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00726 | **PDF** https://arxiv.org/pdf/2607.00726.pdf | **代码** 暂无 | **Demo** https://fgt7t6g.github.io

### 📌 简介
音视频特征提取是多模态理解和生成任务的基础组件。然而现有评估协议存在维度偏差，通常只关注语义匹配或时间偏移检测其一。数据构建仍耦合，无法独立评估时间和语义一致性。本文提出AV-SyncBench，首个完全分离时间和语义评估的基准测试，实现独立评估时间一致性和语义一致性。

### 🔧 技术方案

**模型架构** 音视频同步评估框架，完全分离时间和语义评估维度。

**核心创新** 现有评估协议存在维度偏差，AV-SyncBench首次完全分离时间和语义评估，数据构建解耦，独立评估时间一致性和语义一致性。

**训练策略** 系统评估音视频特征提取模型的同步能力，揭示现有方法的维度偏差。

### 📊 实验结果
**数据集** AV-SyncBench benchmark。

**主要指标** 首次实现时间和语义评估完全分离，在多个音视频特征提取模型上验证维度偏差问题。

**是否开源** Demo: https://fgt7t6g.github.io

### ⭐ 评分：8/10
首个解耦的时间和语义音视频同步基准，问题定义清晰，揭示现有方法的系统性偏差。

---

## [5] Do Multimodal Large Language Models Need Reasoning to Classify Dementia from Speech?

**arXiv ID** 2607.00260 | **方向** 语音大模型

**作者** Wang Liming, Rezaii Neguine, Dickerson Bradford C., Glass James

**机构** (arXiv未提供机构信息)

**发布日期** 2026-06-30 | **论文** https://arxiv.org/abs/2607.00260 | **PDF** https://arxiv.org/pdf/2607.00260.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
多模态大语言模型(MLLMs)已成为从语音录音进行自动痴呆症分类(ADC)的有前景方法。但推理能力是否对ADC有益，以及如何利用这些能力尚不清楚。本文对推理MLLMs进行仔细评估，发现依赖基于文本推理的naive策略可能误导模型。通过蒸馏和GRPO阶段学习认知标签和可解释的推理理由，MLP adaptor阶段用小规模MLP分类器学习任务特定表示。

### 🔧 技术方案

**模型架构** 基于MLLM的痴呆症分类系统，包含MLP adaptor和推理模块。

**核心创新** 研究推理能力对ADC的效用，发现naive文本推理策略的局限性。提出蒸馏+GRPO阶段学习认知标签和推理理由。

**训练策略** MLP adaptor阶段用小规模MLP分类器学习任务特定表示，避免复杂推理带来的误导。

### 📊 实验结果
**数据集** 语音痴呆症分类数据集。

**主要指标** 展示推理MLLMs在ADC任务上的表现，分析推理理由的效用，为实际应用提供指导。

**是否开源** 暂无。

### ⭐ 评分：7/10
探索MLLM推理能力在医疗语音分析中的作用，问题设置实际，消融分析有价值。

---

## [6] Adaptive Perturbation Selection for Contrastive Audio Decoding

**arXiv ID** 2607.00247 | **方向** 语音大模型

**作者** Grace Aaron Isidore, Huo Zhouyuan, Wang Weiran

**机构** (arXiv未提供机构信息)

**发布日期** 2026-06-30 | **论文** https://arxiv.org/abs/2607.00247 | **PDF** https://arxiv.org/pdf/2607.00247.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
大音频语言模型(LALMs)常通过语言先验覆盖声学证据产生幻觉。虽然对比解码(CD)提供无需训练的缓解方法，但现有方法依赖mask或noise等粗粒度扰动，结构化音频转换未被探索。本文通过评估多样化针对性音频扰动库并自适应为每个任务和样本选择最优negative branch来探索这一设计空间。首先改进先前VCD等方法，然后提出自适应扰动选择策略。

### 🔧 技术方案

**模型架构** 对比音频解码框架，包含扰动库和自适应选择器。

**核心创新** VCD等方法用mask或noise等粗粒度扰动，提出评估多样化针对性音频扰动库，自适应为每个任务和样本选择最优negative branch。

**训练策略** 无需训练的对比解码方法，探索结构化音频转换设计空间，提升选择效率。

### 📊 实验结果
**数据集** AH benchmark等音频语言模型任务。

**主要指标** 在多种音频语言模型任务上减少语言先验覆盖声学证据的问题，提升生成质量。

**是否开源** 暂无。

### ⭐ 评分：7/10
自适应扰动选择扩展了对比解码的设计空间，方法有一定创新，实验覆盖多种任务。

---

## 🎙️ 语音前端

---

## [1] From Objectives to Applications: Aligning Architectural Biases in Audio Self-Supervised Learning

**arXiv ID** 2607.00387 | **方向** 语音前端

**作者** Xu Kele, Fang Yulu, Zhou Boda, Sun Yulin, Xu Qisheng, Song Qiya, Zhang Jin, Yang Cheng, Wang Huaimin

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00387 | **PDF** https://arxiv.org/pdf/2607.00387.pdf | **代码** https://github.com/colaudiolab/Awesome-Self-Supervised-Audio-Learning | **Demo** 暂无

### 📌 简介
本文从预训练目标、架构归纳偏置和下游应用的对齐角度审视音频自监督学习(SSL)。不同于将SSL方法视为时间顺序的代理任务或模型家族序列，本文探讨不同监督信号如何塑造模型预期学习的表示。讨论围绕五个范式组织：辅助任务、对比学习、生成重建、离散token化和掩码预测，为SSL方法选择提供理论指导。

### 🔧 技术方案

**模型架构** 审视音频SSL的预训练目标与架构归纳偏置对齐的统一框架。

**核心创新** 从表示学习和模型需求角度审视SSL，而非按时间顺序回顾。围绕五个范式系统分析：辅助任务、对比学习、生成重建、离散token化、掩码预测。

**训练策略** 探索不同监督信号如何塑造模型学习表示，揭示目标与架构的匹配关系。

### 📊 实验结果
**数据集** 多种音频下游任务。

**主要指标** 揭示预训练目标与架构偏置如何影响表示学习，为SSL方法选择提供系统性指导。

**是否开源** GitHub: https://github.com/colaudiolab/Awesome-Self-Supervised-Audio-Learning

### ⭐ 评分：8/10
系统性审视音频SSL的综述性工作，五个范式的分类框架有启发性，为方法选择提供理论依据。

---

## [2] Positive-Incentive Noise Predictor for Adversarial Purification in Speaker Verification

**arXiv ID** 2607.00899 | **方向** 语音前端

**作者** Bai Yibo, Chen Sizhou, Panariello Michele, Ma Hao, Zhang Xiao-Lei, Li Xuelong, Todisco Massimiliano, Evan Nicholas

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00899 | **PDF** https://arxiv.org/pdf/2607.00899.pdf | **代码** 暂无 | **Demo** https://eurecom-asp.github.io

### 📌 简介
现代自动说话人验证(ASV)系统易受对抗扰动攻击。基于扩散的净化方法已显示对这类扰动的强有效性，但反向去噪过程需要迭代采样导致高推理延迟。本文发现前向noising过程提供大部分鲁棒性增益。基于此观察，将对抗净化重新表述为可学习的noising问题，提出Positive-Incentive Noise Predictor，避免迭代采样的高推理延迟。

### 🔧 技术方案

**模型架构** 基于扩散的说话人验证对抗净化框架，核心为Positive-Incentive Noise Predictor。

**核心创新** 发现前向noising过程提供大部分鲁棒性增益。将对抗净化重新表述为可学习的noising问题，替代需要迭代采样的扩散净化。

**训练策略** 学习性noising替代传统扩散净化，大幅降低推理延迟同时保持净化效果。

### 📊 实验结果
**数据集** 说话人验证对抗攻击测试数据集。

**主要指标** 保持净化效果的同时显著降低推理延迟，实现效率和鲁棒性的平衡。

**是否开源** Demo: https://eurecom-asp.github.io

### ⭐ 评分：8/10
将对抗净化重新诠释为可学习noising问题的理论创新，避免迭代采样延迟，方法简洁有效。

---

## [3] AmbiDrop: Ambisonics-Based Array-Agnostic Neural Speech Enhancement

**arXiv ID** 2607.00548 | **方向** 语音前端

**作者** Tatarjitzky Michael, Tourbabin Vladimir, Rafaely Boaz

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00548 | **PDF** https://arxiv.org/pdf/2607.00548.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
多通道深度神经网络(DNNs)显著提升了语音增强性能，但通常受限于固定麦克风阵列几何，导致在不可见或不规则配置上泛化差。现有阵列无关方法依赖高复杂度架构或大规模多样化数据集，仍难以泛化到分布外布局。本文深入分析AmbiDrop方法，通过球面谐波域处理实现任意麦克风阵列配置的泛化。

### 🔧 技术方案

**模型架构** 基于Ambisonics的阵列无关神经语音增强，通过球面谐波域处理实现泛化。

**核心创新** 深度分析Ambisonics编码和语音增强任务的数学框架，实现对任意麦克风阵列配置的泛化能力。

**训练策略** 在实际麦克风设备（如Aria眼镜）上评估真实数据，验证阵列无关泛化能力。

### 📊 实验结果
**数据集** Aria眼镜等实际设备采集的真实数据，多种阵列配置测试。

**主要指标** 在不可见阵列配置上表现鲁棒，实现真正的阵列无关语音增强。

**是否开源** 暂无。

### ⭐ 评分：8/10
基于Ambisonics的阵列无关方法有理论深度，在实际设备上的验证增强了实用性。

---

## [4] Disentangling Speaker and Language Effects in Cross-Lingual Speaker Verification for Iberian Languages

**arXiv ID** 2607.01161 | **方向** 语音前端

**作者** Buitrago Pol, Hernando Javier

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.01161 | **PDF** https://arxiv.org/pdf/2607.01161.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
跨语言说话人验证(SV)系统在注册和测试语音语言不同时通常表现下降。然而标准评估协议混淆了语言不匹配与说话人间变异性，因为评估通常在不同语言的不同说话人之间进行。本文引入五种Iberian语言的双语同说话人评估集，在固定说话人身份下进行跨语言SV分析，使用跨语言迁移矩阵(CLTM)量化donor language训练数据对目标语言性能的影响。

### 🔧 技术方案

**模型架构** 跨语言说话人验证框架，分析语言和说话人效应的解耦。

**核心创新** 标准评估协议混淆语言不匹配与说话人间变性。使用双语同说话人评估集，五种Iberian语言，固定说话人身份下的跨语言SV分析。

**训练策略** 使用Cross-Lingual Transfer Matrix (CLTM)量化donor language训练数据对目标语言性能的影响，分离语言和说话人效应。

### 📊 实验结果
**数据集** 五种Iberian语言的双语同说话人评估集。

**主要指标** 固定说话人ID下跨语言性能分析，分离语言和说话人效应，揭示语言迁移的真实模式。

**是否开源** 暂无。

### ⭐ 评分：7/10
双语同说话人评估集设计有创新，分离语言和说话人效应的方法论有参考价值。

---

## [5] Speech Playground: An Interactive Tool for Speech Analysis and Comparison

**arXiv ID** 2607.00418 | **方向** 语音前端

**作者** McIntosh Stephen, Saito Daisuke, Minematsu Nobuaki

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00418 | **PDF** https://arxiv.org/pdf/2607.00418.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出Speech Playground，一个交互式语音可视化和比较工具。现有工具如Praat虽然优秀，但与现代深度学习表示集成和用于比较时仍繁琐。Speech Playground通过结合Python后端和基于Web的前端，支持多种特征类型（连续、离散、变长）的交互探索，集成TextGrid和forced alignment，面向语音研究、表示验证和CAPT实验。

### 🔧 技术方案

**模型架构** 交互式语音可视化和比较工具，Python后端+Web前端架构。

**核心创新** 支持多种特征类型的交互探索（连续、离散、变长），集成TextGrid和forced alignment，提升研究效率。

**训练策略** 面向语音研究、表示验证和CAPT实验的工具设计。

### 📊 实验结果
**数据集** 多种语音特征类型测试。

**主要指标** 支持灵活的特征可视化和比较，提升语音研究效率。

**是否开源** 暂无。

### ⭐ 评分：6/10
有参考价值的工具工作，将现代深度学习表示与传统语音分析工具结合，但方法创新性一般。

---

今日语音论文速递