# 2026-07-02 语音论文速递

**共收录**: 11 篇 | **语音大模型**: 6 篇 | **语音前端**: 5 篇

> 今日 arXiv 语音相关论文共命中 11 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis

**arXiv ID** 2607.00363 | **方向** 语音大模型

**作者** Yu, Zuda, Xu, Qianhui, Chen, Ting, Zhang, Junhui, Fu, Tao, Yu, Hongjiang, Wang, Qiangqing, Song, Yang

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00363 | **PDF** https://arxiv.org/pdf/2607.00363.pdf | **代码** 暂无 | **Demo** demo

### 📌 简介
Flow Matching (FM) has emerged as a powerful paradigm for speech generation but remains constrained by high inference latency and timbre leakage. To address these bottlenecks, we propose a unified guidance framework that enhances generation efficiency and robustness through two complementary strategies. On the data front, we introduce Data-guidance via heterogeneous augmentation, encouraging the model to disentangle linguistic content from acoustic residue. In parallel, we propose an enhanced Mo

### 🔧 技术方案
**模型架构** 基于Flow Matching的语音合成框架，通过统一引导框架增强生成效率。

**核心创新** 提出Data-guidance和Model-guidance双重策略。Data-guidance通过异质增强 disentangle语言内容与声学残差。Model-guidance设计高效推理路径减少延迟。

**训练策略** 解决timbre leakage问题，通过引导框架实现鲁棒语音合成。

### 📊 实验结果
**数据集** 语音合成标准 benchmark。

**主要指标** 解决高推理延迟和 timbre leakage，在保持质量的同时显著提升效率。

**是否开源** 暂无代码发布。

### ⭐ 评分：9/10
突破性工作，在各自领域有显著创新，实验充分全面。

---

## [2] NPUsper: Eliminating Redundant Computation for Real-Time Whisper on Mobile NPUs

**arXiv ID** 2607.01108 | **方向** 语音大模型

**作者** Lee, Sihyeon, Lee, Hojeong, Woo, Sungwon, Yan, Chengpo, Banerjee, Suman, Kim, Seyeon

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.01108 | **PDF** https://arxiv.org/pdf/2607.01108.pdf | **代码** https://github.com/npusper/NPUsper | **Demo** https://github.com

### 📌 简介
We present NPUsper, a live transcription system that makes Whisper efficient on mobile NPUs by eliminating redundant computation. To avoid the heavy padding used by prior streaming systems, NPUsper detects hallucinated tokens online from temporal patterns in decoder cross-attention, allowing each inference round to process short audio inputs with minimal carryover. For efficient mobile-NPU execution, we propose controlled unrolling, which executes autoregressive decoding as K-step chunk graphs, 

### 🔧 技术方案
**模型架构** 基于Whisper的实时转录系统，针对移动NPU优化。

**核心创新** 幻觉token在线检测：从decoder cross-attention的时序模式检测幻觉token，实现短音频输入处理。Controlled Unrolling：将自回归解码执行为K-step chunk graphs，减少KV-cache计算和图调度开销。

**训练策略** 实时处理输入语音，每轮推理只需处理短音频和最小carryover。

### 📊 实验结果
**数据集** 实时语音转录测试。

**主要指标** 相比基线实现4.84x更低 per-word latency，33.2x更低 TTFT，88.64%更低平均功耗，同时保持相当转录精度。

**是否开源** 代码已发布：https://github.com/npusper/NPUsper

### ⭐ 评分：8/10
有实质贡献，方法创新性强，实验设计完整。

---

## [3] A Geometric Perspective on Composable Emotion Steering in Text-to-Speech Models

**arXiv ID** 2607.00946 | **方向** 语音大模型

**作者** Wang, Siyi, Bailey, James, Dang, Ting

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00946 | **PDF** https://arxiv.org/pdf/2607.00946.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
While prior work has explored emotion control in hybrid text-to-speech systems, the geometric properties of these modules, and their implications for steerability, remain poorly understood. We present the first comparative study of speech language model (SLM) and conditional flow-matching (CFM) modules as activation steering sites for mixed emotion speech synthesis. We first characterize emotion representations using linear probing and local intrinsic dimensionality (LID), and then evaluate sing

### 🔧 技术方案
**模型架构** 比较SLM（Speech Language Model）和CFM（Conditional Flow Matching）模块作为激活 steering sites。

**核心创新** 首次系统比较两种模块的混合情绪语音合成steerability。使用线性探测和局部本征维度（LID）表征情绪表示。评估单语和跨语言场景下的情绪控制能力。

**训练策略** 通过激活steering实现混合情绪控制，无需重新训练模型。

### 📊 实验结果
**数据集** 混合情绪语音合成测试。

**主要指标** 系统比较SLM和CFM模块的steerability，揭示几何属性对情绪控制的影响。

**是否开源** 暂无。

### ⭐ 评分：8/10
有实质贡献，方法创新性强，实验设计完整。

---

## [4] AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization

**arXiv ID** 2607.00726 | **方向** 语音大模型

**作者** Zhou, Tianhong, Han, Mingyang, Li, Boyu, Jiang, Yuxuan, Ye, Jiaxin, Wang, Dongxiao, Shi, Haoxiang, Wang, Kunpeng, Song, Jun, Yu, Cheng, Zheng, Bo

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00726 | **PDF** https://arxiv.org/pdf/2607.00726.pdf | **代码** 暂无 | **Demo** https://fgt7t6g.github.io

### 📌 简介
Audio-visual feature extraction is a fundamental component of multimodal understanding and generation tasks. However, existing evaluation protocols for feature extraction models exhibit dimensional bias, typically focusing on either semantic matching or temporal offset detection. Moreover, their data construction remains coupled, preventing independent assessment of temporal and semantic consistency. We propose AV-SyncBench, the first benchmark to fully separate temporal and semantic evaluation 

### 🔧 技术方案
**模型架构** 音视频特征提取评估框架，完全分离时间和语义评估。

**核心创新** 现有评估协议存在维度偏差，聚焦语义匹配或时间偏移检测其一。AV-SyncBench首次完全分离时间和语义评估，数据构建解耦，独立评估时间一致性和语义一致性。

**训练策略** 系统评估音视频特征提取模型的同步能力。

### 📊 实验结果
**数据集** AV-SyncBench benchmark。

**主要指标** 首次实现时间和语义评估完全分离，揭示现有方法的维度偏差。

**是否开源** Demo: https://fgt7t6g.github.io

### ⭐ 评分：8/10
有实质贡献，方法创新性强，实验设计完整。

---

## [5] Do Multimodal Large Language Models Need Reasoning to Classify Dementia from Speech?

**arXiv ID** 2607.00260 | **方向** 语音大模型

**作者** Wang, Liming, Rezaii, Neguine, Dickerson, Bradford C., Glass, James

**机构** (arXiv未提供机构信息)

**发布日期** 2026-06-30 | **论文** https://arxiv.org/abs/2607.00260 | **PDF** https://arxiv.org/pdf/2607.00260.pdf | **代码** 暂无 | **Demo** demo

### 📌 简介
Multimodal large language models (MLLMs) have emerged as a promising approach for improving the accuracy, transferability, and explainability of automatic dementia classification (ADC) systems from voice recordings. Yet it remains unclear whether their reasoning capabilities are beneficial for ADC, and how such capabilities should be leveraged. In this paper, we conduct a careful evaluation of reasoning MLLMs for ADC and show that naive strategies, such as relying on text-based rationales, can l

### 🔧 技术方案
**模型架构** 基于多模态大语言模型（MLLM）的痴呆症分类系统。

**核心创新** 研究推理能力是否对ADC有益，以及如何利用。发现基于文本推理的naive策略可能误导模型。提出蒸馏和GRPO阶段学习认知标签和解释性rationale。

**训练策略** MLP adaptor阶段用小规模MLP分类器学习任务特定表示。

### 📊 实验结果
**数据集** 语音痴呆症分类数据集。

**主要指标** 展示推理MLLMs在ADC任务上的表现，分析rationale的效用。

**是否开源** Demo available.

### ⭐ 评分：7/10
有价值的工作，方法有一定创新，实验较充分。

---

## [6] Adaptive Perturbation Selection for Contrastive Audio Decoding

**arXiv ID** 2607.00247 | **方向** 语音大模型

**作者** Grace, Aaron Isidore, Huo, Zhouyuan, Wang, Weiran

**机构** (arXiv未提供机构信息)

**发布日期** 2026-06-30 | **论文** https://arxiv.org/abs/2607.00247 | **PDF** https://arxiv.org/pdf/2607.00247.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Large audio-language models (LALMs) frequently hallucinate by overriding acoustic evidence with language priors. While contrastive decoding (CD) offers training-free mitigation, existing methods rely on blunt perturbations like masking or noise, leaving structured audio transformations unexplored. We explore this design space by evaluating a diverse library of targeted audio perturbations and adaptively selecting the optimal negative branch for each task and example. First, we improve upon earli

### 🔧 技术方案
**模型架构** 对比音频解码框架，改进LALMs的幻觉问题。

**核心创新** VCD等方法用mask或noise等粗粒度扰动，提出评估多样化针对性音频扰动库，自适应为每个任务和样本选择最优negative branch。

**训练策略** 无需训练的对比解码方法，探索结构化音频转换设计空间。

### 📊 实验结果
**数据集** AH benchmark等音频基础任务。

**主要指标** 在多种音频语言模型任务上提升性能，减少语言先验覆盖声学证据的问题。

**是否开源** 暂无。

### ⭐ 评分：7/10
有价值的工作，方法有一定创新，实验较充分。


## 🎙️ 语音前端

---

## [1] From Objectives to Applications: Aligning Architectural Biases in Audio Self-Supervised Learning

**arXiv ID** 2607.00387 | **方向** 语音前端

**作者** Xu, Kele, Fang, Yulu, Zhou, Boda, Sun, Yulin, Xu, Qisheng, Song, Qiya, Zhang, Jin, Yang, Cheng, Wang, Huaimin

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00387 | **PDF** https://arxiv.org/pdf/2607.00387.pdf | **代码** https://github.com/colaudiolab/Awesome-Self-Supervised-Audio-Learning | **Demo** https://github.com

### 📌 简介
This paper examines audio self-supervised learning (SSL) through the alignment between pretraining objectives, architectural inductive biases, and downstream applications. Rather than treating SSL methods as a chronological sequence of pretext tasks or model families, we ask how different supervisory signals shape the representations that models are expected to learn. The discussion is organized around five paradigms: auxiliary tasks, contrastive learning, generative reconstruction, discrete tok

### 🔧 技术方案
**模型架构** 审视音频自监督学习（SSL）的预训练目标与架构归纳偏置对齐。

**核心创新** 从表示学习和模型需求角度审视SSL，而非按时间顺序回顾loss函数。围绕五个范式组织讨论：辅助任务、对比学习、生成重建、离散token化和掩码预测。

**训练策略** 探索不同监督信号如何塑造模型学习表示。

### 📊 实验结果
**数据集** 多种音频下游任务。

**主要指标** 揭示预训练目标与架构偏置如何影响表示学习，为SSL方法选择提供指导。

**是否开源** GitHub: https://github.com/colaudiolab/Awesome-Self-Supervised-Audio-Learning

### ⭐ 评分：10/10
突破性工作，在各自领域有显著创新，实验充分全面。

---

## [2] Positive-Incentive Noise Predictor for Adversarial Purification in Speaker Verification

**arXiv ID** 2607.00899 | **方向** 语音前端

**作者** Bai, Yibo, Chen, Sizhou, Panariello, Michele, Ma, Hao, Zhang, Xiao-Lei, Li, Xuelong, Todisco, Massimiliano, Evan, Nicholas

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00899 | **PDF** https://arxiv.org/pdf/2607.00899.pdf | **代码** 暂无 | **Demo** https://eurecom-asp.github.io

### 📌 简介
Modern automatic speaker verification (ASV) systems are vulnerable to adversarial perturbations. Diffusion-based purification has recently shown strong effectiveness against such perturbations, but its reverse denoising process requires iterative sampling and leads to high inference latency. We find that the forward noising process provides most of the robustness gain. Motivated by this observation, we reformulate adversarial purification as a learnable noising problem, and propose the Positive-

### 🔧 技术方案
**模型架构** 基于扩散的说话人验证对抗净化框架。

**核心创新** 发现前向noising过程提供大部分鲁棒性增益。将对抗净化重新表述为可学习的noising问题，提出Positive-Incentive Noise Predictor。避免迭代采样的高推理延迟。

**训练策略** 学习性noising替代传统扩散净化。

### 📊 实验结果
**数据集** 说话人验证对抗攻击测试。

**主要指标** 保持净化效果的同时显著降低推理延迟。

**是否开源** Demo: https://eurecom-asp.github.io

### ⭐ 评分：8/10
有实质贡献，方法创新性强，实验设计完整。

---

## [3] AmbiDrop: Ambisonics-Based Array-Agnostic Neural Speech Enhancement

**arXiv ID** 2607.00548 | **方向** 语音前端

**作者** Tatarjitzky, Michael, Tourbabin, Vladimir, Rafaely, Boaz

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00548 | **PDF** https://arxiv.org/pdf/2607.00548.pdf | **代码** 暂无 | **Demo** demo

### 📌 简介
Multichannel Deep Neural Networks (DNNs) have significantly improved speech enhancement performance; however, they typically remain constrained by reliance on fixed microphone array geometries, leading to poor generalization on unseen or irregular configurations. Current array-agnostic approaches often rely on high-complexity architectures or massive, diverse datasets, yet they still struggle to generalize to out-of-distribution layouts. In this paper, we present an in-depth analysis of AmbiDrop

### 🔧 技术方案
**模型架构** 基于Ambisonics的阵列无关神经语音增强。

**核心创新** 分析AmbiDrop方法，通过球面谐波域处理实现任意麦克风阵列配置的泛化。深度分析Ambisonics编码和语音增强任务的数学框架。

**训练策略** 在实际麦克风设备（如Aria眼镜）上评估真实数据。

### 📊 实验结果
**数据集** Aria眼镜等实际设备采集的真实数据。

**主要指标** 阵列无关泛化能力验证，在不可见阵列配置上表现鲁棒。

**是否开源** 暂无。

### ⭐ 评分：8/10
有实质贡献，方法创新性强，实验设计完整。

---

## [4] Disentangling Speaker and Language Effects in Cross-Lingual Speaker Verification for Iberian Languages

**arXiv ID** 2607.01161 | **方向** 语音前端

**作者** Buitrago, Pol, Hernando, Javier

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.01161 | **PDF** https://arxiv.org/pdf/2607.01161.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Cross-lingual speaker verification (SV) systems typically exhibit performance degradation when enrollment and test utterances are spoken in different languages. However, standard evaluation protocols confound language mismatch with inter-speaker variability, as evaluation is generally performed with different speakers across languages. In this work, we introduce a bilingual same-speaker evaluation set for five Iberian languages, enabling analysis of cross-lingual SV under constant speaker identi

### 🔧 技术方案
**模型架构** 跨语言说话人验证框架，分析语言和说话人效应。

**核心创新** 标准评估协议混淆语言不匹配与说话人间变性。使用双语同说话人评估集，五种Iberian语言，固定说话人身份下的跨语言SV分析。

**训练策略** 使用Cross-Lingual Transfer Matrix (CLTM)量化 donor language训练数据对目标语言性能的影响。

### 📊 实验结果
**数据集** 五种Iberian语言的双语同说话人评估集。

**主要指标** 固定说话人ID下跨语言性能分析，分离语言和说话人效应。

**是否开源** 暂无。

### ⭐ 评分：7/10
有价值的工作，方法有一定创新，实验较充分。

---

## [5] Speech Playground: An Interactive Tool for Speech Analysis and Comparison

**arXiv ID** 2607.00418 | **方向** 语音前端

**作者** McIntosh, Stephen, Saito, Daisuke, Minematsu, Nobuaki

**机构** (arXiv未提供机构信息)

**发布日期** 2026-07-01 | **论文** https://arxiv.org/abs/2607.00418 | **PDF** https://arxiv.org/pdf/2607.00418.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
This paper presents Speech Playground, an interactive speech visualization and comparison tool. While existing tools such as Praat are excellent, it can be cumbersome to integrate them with modern deep learning representations and use them for comparison. Speech Playground addresses this by combining a Python backend with a web-based frontend for interactive exploration of multiple feature types, including continuous, discrete, and variable-length representations. It includes TextGrid and forced

### 🔧 技术方案
**模型架构** 交互式语音可视化和比较工具。

**核心创新** 结合Python后端和Web前端，支持多种特征类型（连续、离散、变长）的交互探索。集成TextGrid和forced alignment。

**训练策略** 面向语音研究、表示验证和CAPT实验的工具。

### 📊 实验结果
**数据集** 多种语音特征类型测试。

**主要指标** 支持灵活的特征可视化和比较，便利于语音研究。

**是否开源** 暂无。

### ⭐ 评分：6/10
增量工作，有参考价值但创新性一般。


---

今日语音论文速递