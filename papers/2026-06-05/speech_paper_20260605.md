# 2026-06-05 语音论文速递

**共收录**: 19 篇 | **语音大模型**: 12 篇 | **语音前端**: 7 篇

> 今日 arXiv 语音相关论文共命中 19 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] UniVoice: A Unified Model for Speech and Singing Voice Generation

**arXiv ID** 2606.05852 | **方向** 语音大模型

**作者** Junjie Zheng, Huixin Xue, Shihong Ren, Chaofan Ding, Hao Liu, Zihao Chen

**机构** Giant Network, Shanghai Conservatory of Music

**发布日期** 2026-06-04 | **论文** https://arxiv.org/abs/2606.05852 | **PDF** https://arxiv.org/pdf/2606.05852.pdf | **代码** 暂无 | **Demo** https://nips-unvoice.netlify.app/

### 📌 简介
本文提出UniVoice，一个基于条件流匹配(CFM)的统一语音和歌唱生成框架。核心创新是将条件分解为内容、旋律和音色三个独立因素，使用共享的Diffusion Transformer (DiT)主干网络。对于语音，旋律条件替换为学习的null melody token，让模型从语言和声学上下文推断韵律。训练数据包括30k小时语音和35k小时歌唱数据。UniVoice在语音PER达到5.26%，与专用TTS系统相当；在歌唱生成上PER为16.22%，显著优于统一基线Vevo1.5 (24.72%)。

### 🔧 技术方案

**模型架构** 基于条件流匹配(CFM)和Diffusion Transformer (DiT)主干，24层Transformer，隐藏维度1024，16头注意力，约0.3B参数。使用FlashAttention-2和RoPE进行高效长上下文建模。在Song Bloom VAE潜在特征(25Hz，维度48)上操作。

**核心创新** 因子化条件机制将条件分解为内容(音素序列)、旋律(MIDI音符序列或null token)和音色(音频提示)，由模态适切的编码器编码后送给共享DiT主干。对于语音，旋律条件替换为学习的null melody token，近似于旋律边缘化。任务token通过AdaLN调制，使模型自适应不同模态而无需任务特定参数。

**训练策略** 损失函数为CFM损失 ||vθ(φt(x0,x1),t)-(x1-x0)||²。训练数据混合30k小时语音和35k小时歌唱数据。推理时使用32步ODE采样。

### 📊 实验结果
**数据集** 语音评估使用内部测试集，歌唱使用UniSinging-Eval benchmark(覆盖12种音乐风格)。

**主要指标** 语音PER 5.26% (vs F5-TTS 5.21%, CosyVoice3 5.30%)，歌唱PER 16.22% (vs Vevo1.5 24.72%)，参数量0.3B。

**是否开源** 将发布推理代码、模型权重和UniSinging-Eval测试集。

### ⭐ 评分：8/10
UniVoice通过因子化条件设计巧妙解决了语音和歌唱生成的冲突问题，null melody token的理论分析有深度，实验覆盖语音和歌唱两个模态且效果优异。发布代码和数据集利于复现。

---

## [2] GLASS: GRPO-Trained LoRA for Acoustic Style Steering in Zero-Shot Text-to-Speech

**arXiv ID** 2606.05889 | **方向** 语音大模型

**作者** Jaehoon Kang, Yejin Lee, Kyuhong Shim

**机构** Sungkyunkwan University

**发布日期** 2026-06-04 | **论文** https://arxiv.org/abs/2606.05889 | **PDF** https://arxiv.org/pdf/2606.05889.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
GLASS提出一种基于后生成奖励的声学风格控制框架，用于零样本TTS的风格控制。核心思想是将每个声学属性视为奖励定义的控制方向，使用GRPO(Group Relative Policy Optimization)训练轻量级LoRA适配器。奖励设计包括语音token长度(语速)、F0均值(音高)和WER( intelligibility anchor)。独立训练的适配器可通过LoRA算术进行交换、插值和组合。实验证明在保持自然度、说话人相似度和清晰度的同时实现目标风格迁移，并支持多轴组合。

### 🔧 技术方案

**模型架构** 基于自回归TTS(AR TTS)，将语音token策略π(y|x)作为 speech-token policy。GLASS冻结TTS主干，为每个风格方向学习一个轻量级LoRA适配器。使用CosyVoice2-0.5B或Seed-TTS作为主干。

**核心创新** GRPO训练：给定相同文本和说话人提示的G个样本，使用语音token长度作为语速奖励、F0均值作为音高奖励、WER作为清晰度锚点。奖励函数 R_k(y,x) = ηR_WER(y,x) + (1-η)R^style_k(y)，通过组内相对奖励更新LoRA。LoRA算术支持离散交换、连续插值和多轴组合。

**训练策略** 每个风格方向训练独立LoRA适配器，冻结主干。使用GRPO优化，组内相对策略优化。推理时通过LoRA权重线性组合实现风格控制。

### 📊 实验结果
**数据集** Seed-TTS-eval test_en基准测试。

**主要指标** 语速控制：Fast LoRA实现5.59 SPS (vs 基线3.65)，Slow LoRA实现2.30 SPS；音高控制：High-pitch LoRA将F0提升至156.1Hz(男)/241.0Hz(女)，Low-pitch LoRA将F0降至108.9Hz(男)/164.6Hz(女)。Speaker similarity达0.61-0.65 (vs DSP方法0.16-0.50)。

**是否开源** 暂未发布。

### ⭐ 评分：8/10
GLASS创新性地将RL用于TTS风格控制，LoRA算术支持灵活的风格组合，实验设计完整。唯一缺憾是未发布代码。

---

## [3] CoSTA: Cognitive-State-Conditioned TTS Data Augmentation Using ASR Transcripts for Alzheimer's Disease Detection

**arXiv ID** 2606.06170 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-04 | **论文** https://arxiv.org/abs/2606.06170 | **PDF** https://arxiv.org/pdf/2606.06170.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
CoSTA提出一种基于TTS的数据增强框架用于阿尔茨海默病(AD)检测。通过构建Cognitive-State-Conditioned (CS-Cond) TTS模型，合成为AD和健康对照特征的语音。使用CosyVoice2和F5-TTS进行适配，并研究文本来源(MT vs ASR转录本)对TTS增强的影响。在ADReSS数据集上，CoSTA相比基线获得4.16%提升，达到85.83%的音频单独准确率。

### 🔧 技术方案

**模型架构** 基于CosyVoice2和F5-TTS构建Cognitive-State-Conditional TTS模型。转录本池包括人工转录(MT)和36个ASR自动转录。

**核心创新** 认知状态条件TTS：针对AD和健康对照两种认知状态分别训练TTS模型。ASR驱动增强优于MT驱动增强，表明合成数据的多样性对下游任务有利。

**训练策略** 扩充因子分析和测试时增强(TTA)策略。

### 📊 实验结果
**数据集** ADReSS数据集。

**主要指标** 音频单独准确率85.83%，相比基线提升4.16%，优于先前方法。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
将TTS应用于医疗辅助诊断的数据增强，有实际应用价值。实验验证了ASR转录本作为合成数据来源的有效性。

---

## [4] Beyond Generative Decoding: Discriminative Hidden-State Readout from a Native Omni-Modal LLM for Multimodal Sentiment Analysis

**arXiv ID** 2606.05713 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-03 | **论文** https://arxiv.org/abs/2606.05713 | **PDF** https://arxiv.org/pdf/2606.05713.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文重新审视多模态情感分析(MSA)中大型多模态模型的读出机制。传统方法使用生成式读出(将情感分数作为文本字符串输出)，存在连续回归依赖离散自回归解码的问题。提出判别式读出方法，基于原生全模态LLM (Qwen2.5-Omni-7B)的Thinker模块，将最后一层的隐藏状态直接映射到连续分数。使用4-bit量化和QLoRA，整个7B管道可在单卡GPU上训练。在CMU-MOSI和CMU-MOSEI上达到SOTA准确率。

### 🔧 技术方案

**模型架构** 基于Qwen2.5-Omni-7B，使用Thinker模块的最终层隐藏状态，通过轻量级回归头映射到连续分数。单次前向传播完成推理，避免自回归解码。

**核心创新** 判别式读出替代生成式读出：不再将情感分数作为文本字符串解码，而是直接映射隐藏状态。4-bit量化+QLoRA实现高效训练，单GPU(RTX 5090, 32GB)可训练，10-21GB峰值内存，1.14%可训练参数。

**训练策略** 控制变量对比实验，固定主干、数据和LoRA配置，隔离读出机制的影响。

### 📊 实验结果
**数据集** CMU-MOSI, CMU-MOSEI。

**主要指标** MOSI: MAE 0.551, Corr 0.888；MOSEI: MAE 0.506, Corr 0.790，达到SOTA。生成式读出即使经过同等监督训练，MAE也会翻倍，产生2.8%的无法解析或超出范围的输出(零样本)。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
揭示了LLM读出方式的重要性，判别式读出相比生成式在准确率、效率和可靠性上全面超越。实验设计严谨，消融充分。

---

## [5] FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition

**arXiv ID** 2606.06211 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-04 | **论文** https://arxiv.org/abs/2606.06211 | **PDF** https://arxiv.org/pdf/2606.06211.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
自动语音识别(ASR)在标准语音上取得显著进展，但病理性语音仍面临重大挑战。本文研究通过Feature-wise Linear Modulation (FiLM)进行说话人条件化，将x-vector衍生信息注入冻结ASR编码器的每个Transformer层，以适应个体病理性说话者而不修改基模型权重。在西班牙语和英语病理性语音上进行基准测试，并评估适配模型是否保留回答语音相关问题的能力。

### 🔧 技术方案

**模型架构** 使用FiLM进行说话人条件化：x-vector通过FiLM调制注入每个Transformer层，调节归一化层的scale和shift参数。冻结ASR编码器权重，只训练FiLM调制模块。

**核心创新** FiLM条件化实现参数高效适配，病理性说话者的x-vector信息注入预训练ASREncoder内部表示，保持基模型能力同时增强病理性语音识别。

**训练策略** 参数高效微调，与标准微调和后处理基准对比。

### 📊 实验结果
**数据集** 西班牙语和英语病理性语音数据集。

**主要指标** 说话人条件化ASR与 established adaptation strategies 相当，同时保留非条件语音的性能。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
FiLM用于病理性语音适配的方法实用，创新点在于参数高效且保留基模能力。实验覆盖两种语言。

---

## [6] Learning Emotion-discriminative Representations for Zero-Shot Cross-lingual Speech Emotion Recognition

**arXiv ID** 2606.06200 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-04 | **论文** https://arxiv.org/abs/2606.06200 | **PDF** https://arxiv.gov/abs/2606.06200.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
零样本跨语言语音情感识别(SER)面临挑战：跨语言分布不匹配且目标语言缺乏情感标注。本文提出情感判别表示学习方法，结合监督对比学习和说话人对抗学习。对比学习促进跨语言情感对齐，说话人对抗学习抑制说话人相关线索，鼓励说话人不变表示。零样本跨语言SER设定下的实验证明该方法显著优于传统训练策略。

### 🔧 技术方案

**模型架构** 结合监督对比学习和说话人对抗学习的联合框架。前者通过跨语言情感对齐提升泛化，后者通过对抗训练消除说话人信息。

**核心创新** 情感判别表示：学习对情感敏感而对说话人身份不变的表示。对比学习和对抗学习的联合训练。

### 📊 实验结果
**数据集** 零样本跨语言SER设定。

**主要指标** 显著提升跨语言SER性能，超越传统训练策略。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
针对零样本跨语言SER的具体问题提出有效解决方案，对比+对抗的组合训练思路合理。

---

## [7] xvector-emotion-arithmetic: Task-Vector Arithmetic for Emotional Expressivity Control in Language-Model-Based TTS

**arXiv ID** 2606.05367 | **方向** 语音大模型

**作者** Daniel O. Brito, Arnaldo Candido Junior

**机构** UNESP (Universidade Estadual Paulista)

**发布日期** 2026-06-03 | **论文** https://arxiv.org/abs/2606.05367 | **PDF** https://arxiv.org/pdf/2606.05367.pdf | **代码** https://github.com/danielbrito91/xvector-emotion-arithmetic | **Demo** 暂无

### 📌 简介
本文对LM-TTS中情感表达的控制进行系统消除研究。发现x-vector是情感韵律的主导载体，而非模型权重、连续codec嵌入或离散codec token。提出基于x-vector空间质心算术的跨说话人情感控制方法τ_emo = E[x(s_i, emo)] - E[x(s_i, neutral)]，无需微调即可实现情感风格迁移。在英语跨说话人场景获得+0.29 EECS提升，在英到葡萄牙语跨语言场景获得+0.09 EECS提升，同时保持SECS ≥ 0.88的说话人相似度。

### 🔧 技术方案

**模型架构** 基于Qwen3-TTS-12Hz-1.7B-Base，ECAPA-TDNN作为说话人编码器(可学习，与主干共同训练)。x-vector直接注入codec嵌入序列。

**核心创新** 系统消除研究揭示x-vector是情感韵律的主导载体。质心算术：计算源说话人多说话人平均情感向量τ_emo，应用于目标说话人时 x_new = x(target, neutral) + α * τ_emo。参数α控制情感强度。

**训练策略** 无需训练，纯粹推理时操作。多说话人平均(avg4spk)变体在身份保持上优于单说话人变体。

### 📊 实验结果
**数据集** 英语 held-out speakers, 葡萄牙语跨语言评估。

**主要指标** EN跨说话人：+0.29 EECS gain (avg4spk)，SECS_W ≥ 0.88；EN→PT-BR跨语言：+0.09 EECS gain。WER ≈ 0.006 (基本不变)。

**是否开源** GitHub仓库已发布：https://github.com/danielbrito91/xvector-emotion-arithmetic

### ⭐ 评分：8/10
系统性消融研究揭示LM-TTS中情感控制的关键载体，方法简洁有效。开源代码利于复现，跨语言验证展示泛化性。

---

## [8] Towards Truly Multilingual ASR: Generalizing Code-Switching ASR to Unseen Language Pairs

**arXiv ID** 2606.05846 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-03 | **论文** https://arxiv.org/abs/2606.05846 | **PDF** https://arxiv.org/pdf/2606.05846.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
代码切换ASR (CS-ASR)因多语言CS语音资源严重匮乏而具有挑战性。现有方法通过合成CS语音生成或针对特定语言对微调，面临可扩展性限制。本文研究CS能力是否能从有限数量的可见语言对泛化到未见语言对，通过模型融合和领域泛化方法。实验表明，融合的双语CS-ASR模型能适度泛化到未见语言对，但双语CS能力的跨语言对转移有限。

### 🔧 技术方案

**核心创新** 探索模型融合和领域泛化方法实现CS能力的跨语言泛化。研究从有限可见语言对学到的CS能力能否迁移到未见语言对。

### 📊 实验结果
**主要指标** 融合的双语CS-ASR模型能适度泛化到未见语言对，但泛化能力有限。

**是否开源** 暂未明确。

### ⭐ 评分：6/10
问题定义有价值，但实验结果表明跨语言泛化能力有限，方法的新颖性一般。

---

## [9] Multi-task Learning is Not Enough: Representational Entanglement in Dual-output Second Language Speech Recognition

**arXiv ID** 2606.06065 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-04 | **论文** https://arxiv.org/abs/2606.06065 | **PDF** https://arxiv.org/pdf/2606.06065.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
二语(L2)语音识别需要发音转录和意图含义。多任务学习(MTL)是自然的方法，因为它假设共享表示有益于两个输出。然而，本文发现这一假设在韩语和英语之间不成立。MTL改善含义但损害表面转录，尤其在英语中损害程度与表面-含义分歧规模成比例。分析将这些模式归因于编码器层面的纠缠，韩国语保持独立任务表示而英语产生几乎相同的表示。

### 🔧 技术方案

**核心创新** 揭示MTL在L2 ASR中的编码器层面纠缠问题。意义双重输出解码器用独特表示适应，而表面双重输出解码器仍受编码器约束。

### 📊 实验结果
**数据集** 韩语-英语L2 ASR。

**主要指标** MTL改善含义但损害表面转录，Levenshtein编辑距离分析与编码器层面纠缠相关。

**是否开源** 暂未明确。

### ⭐ 评分：6/10
分析深入揭示MTL的局限性，对L2 ASR研究有启发，但方法创新性一般。

---

## [10] M2S-AVSR: Modality-aware Multi-view Self-supervised Representation for Robust Audio-Visual Speech Recognition

**arXiv ID** 2606.05763 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-03 | **论文** https://arxiv.org/abs/2606.05763 | **PDF** https://arxiv.org/pdf/2606.05763.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
音视频语音识别(AVSR)通过利用视觉线索增强语音识别鲁棒性，但现实场景因视角变化、音频失真和视觉遮挡而具有挑战性。M2S-AVSR提出多视图表示学习编码器学习视角不变的视觉语音表示，使用模态感知模块显式建模模态质量和跨模态同步进行细粒度模态感知融合。引入AISHELL8-RealScene真实场景音视频数据集。在LRS3上实现视角扰动和视觉降级设置下29.4%相对提升，在MISP2021-AVSR上达到新SOTA。

### 🔧 技术方案

**模型架构** 多视图表示学习编码器 + 模态感知模块。多视图学习视角不变表示，模态感知模块建模质量和同步。

**核心创新** 细粒度模态感知融合：在解码时进行精细化视觉信息注入，处理视角变化、音频失真和视觉遮挡。

### 📊 实验结果
**数据集** LRS3, MISP2021-AVSR, AISHELL8-RealScene。

**主要指标** LRS3上29.4%相对提升(视角扰动和视觉降级)，MISP2021-AVSR新SOTA，AISHELL8-RealScene户外场景最佳。

**是否开源** 暂未明确，数据集AISHELL8-RealScene已公开。

### ⭐ 评分：7/10
多视图学习加模态感知融合有效提升AVSR鲁棒性，新数据集有助于现实场景研究。

---

## [11] Domain-Aware Mispronunciation Detection and Diagnosis Using Language-Specific Statistical Graphs

**arXiv ID** 2606.05569 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-02 | **论文** https://arxiv.org/abs/2606.05569 | **PDF** https://arxiv.org/pdf/2606.05569.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
发音错误检测与诊断(MDD)在计算机辅助语言学习和语音技术中日益重要。本文提出构建统计图的方法，使模型学习表示为有向图的音素混淆模式。引入语言特定策略捕捉不同母语背景的系统性发音差异。在L2-ARCTIC基准上实现59.52% F1分数，优于多个竞争基线。

### 🔧 技术方案

**核心创新** 统计图建模音素混淆模式，语言特定策略捕捉L1迁移差异。

### 📊 实验结果
**数据集** L2-ARCTIC。

**主要指标** F1分数59.52%，优于竞争基线。

**是否开源** 暂未明确。

### ⭐ 评分：6/10
领域感知方法有价值，但F1分数提升有限，创新性一般。

---

## [12] LLM-Enhanced Dialogue Management for Full-Duplex Spoken Dialogue Systems

**arXiv ID** 2502.14145 | **方向** 语音大模型

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2025-01-27 | **论文** https://arxiv.org/abs/2502.14145 | **PDF** https://arxiv.org/pdf/2502.14145.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
实现全双工通信需要实时协调倾听、说话和思考。本文提出语义VAD模块作为对话管理器管理全双工SDS中的话轮转换。语义VAD预测四个控制token调节话轮切换和话轮保持，区分有意和无意打断，检测查询完成以处理用户停顿和犹豫。通过短间隔处理输入语音实现实时决策，核心对话引擎只在需要响应生成时激活，降低计算开销。

### 🔧 技术方案

**模型架构** 语义VAD模块(0.5B LLM微调) + 核心对话引擎(CDE)。语义VAD预测4个控制token管理话轮。

**核心创新** 全双工SDS的实时协调：语义VAD在短间隔内处理语音，实时决策是否切换或保持话轮，无需每次激活完整对话引擎。

### 📊 实验结果
**数据集** 全双工会话数据。

**主要指标** 平衡交互准确性和推理效率，支持可扩展的全双工SDS。

**是否开源** 暂未明确。

### ⭐ 评分：6/10
全双工SDS的系统设计有价值，但方法创新性一般，主要贡献在系统层面。

---

## 🎙️ 语音前端

---

## [1] Absorbing Discrete Diffusion for Speech Enhancement

**arXiv ID** 2602.22417 | **方向** 语音前端

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-02-26 | **论文** https://arxiv.org/abs/2602.22417 | **PDF** https://arxiv.org/pdf/2602.22417.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出ADDSE，使用吸收离散扩散(ADD)进行语音增强，通过建模干净语音码给定噪声语音码的条件分布。方法利用神经音频 codec 的表达潜在空间和扩散模型的非自回归采样过程。为高效建模RVQ码的分层结构，提出RQDiT，结合RQ-Transformer和扩散Transformer技术。在两个数据集上的非侵入式客观指标表现具有竞争力，尤其在低信噪比和少采样步数条件下。

### 🔧 技术方案

**模型架构** 使用神经音频 codec (NAC)将干净和噪声语音编码为离散码(RVQ，4个codebook，K=1024)，RQDiT进行非自回归建模。RQDiT包含沿帧维度的Frame-DiT和沿深度维度的Depth-DiT。

**核心创新** 吸收离散扩散(ADD)替代连续扩散，避免连续空间的量化伪影。RQDiT处理RVQ的分层结构，两阶段Transformer分别处理帧和深度维度。

**训练策略** 训练R=10步均匀采样，Euler或Tweedie τ-leaping采样。NAC使用多周期判别器(MPD)和多尺度STFT判别器(MS-STFT)训练。

### 📊 实验结果
**数据集** Libri-TUT (跨语料库噪声泛化)，Clarity-FSD50K (跨语料库语音泛化)。

**主要指标** ADDSE在低SNR和少采样步数下表现竞争力。在Libri-TUT和Clarity-FSD50K上进行评估，对比Conv-TasNet、BSRNN、SGMSE+、EDM-SE等基线。

**是否开源** 暂未明确，论文提到代码可用。

### ⭐ 评分：8/10
离散扩散用于语音增强有理论创新，RQDiT设计巧妙处理RVQ分层结构。实验覆盖多种条件和基线。

---

## [2] P2PSynCodec: An Ultra-Low-Bitrate Neural Speech Codec with Plain-to-Pseudo Synergistic Vector Quantization

**arXiv ID** 2606.05876 | **方向** 语音前端

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-03 | **论文** https://arxiv.org/abs/2606.05876 | **PDF** https://arxiv.org/pdf/2606.05876.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
大多数神经语音codec使用残差向量量化(RVQ)，后续VQ贡献更少但消耗相同比特率，效率低下。提出P2PSynCodec，使用Plain-to-Pseudo协同向量量化器(P2PSVQ)的超低比特率神经语音codec。P2PSVQ包含一个plain VQ和多个pseudo VQ。Plain VQ通过量化产生基本token，pseudo VQ通过神经预测生成辅助token且不消耗传输比特率。语音从plain-VQ token和预测的pseudo-VQ token联合解码。在0.5 kbps下实现与2.0 kbps竞品相当的重构质量。

### 🔧 技术方案

**模型架构** P2PSVQ包含plain VQ(产生基本token)和多个pseudo VQ(神经预测，不消耗比特率)。语音从plain-VQ token + 预测的pseudo-VQ token联合解码。

**核心创新** Pseudo VQ概念：通过神经预测生成辅助token，实现零比特率开销。Plain VQ和pseudo VQ协同工作，在超低比特率下保持质量。

### 📊 实验结果
**数据集** 标准语音codec评估数据集。

**主要指标** 0.5 kbps下达到与2.0 kbps竞品相当的质量，实现超低比特率语音编码。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
Pseudo VQ概念有创新性，超低比特率表现有价值。方法简洁有效。

---

## [3] SB-RF: Schrodinger Bridge Rectified Flow for One-Step Robust Speech Enhancement

**arXiv ID** 2606.05575 | **方向** 语音前端

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-02 | **论文** https://arxiv.org/abs/2606.05575 | **PDF** https://arxiv.org/pdf/2606.05575.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
生成模型在语音增强上取得优异结果但通常面临多步推理问题。提出SB-RF，将Rectified Flow (RF)与Schrodinger Bridge (SB)理论结合的单步生成框架。SB-RF通过熵正则最优传输在干净和噪声语音分布之间构建条件桥。通过RF的速度匹配目标对齐SB轨迹与最优传输测地线，实现高质量一步增强。在VoiceBank-DEMAND基准上达到生成方法的领先性能，并验证了低SNR真实场景的鲁棒性。

### 🔧 技术方案

**模型架构** 基于Schrodinger Bridge和Rectified Flow的条件生成模型。通过熵正则最优传输构建干净-噪声条件桥。

**核心创新** 一步生成：通过SB-RF对齐实现单步高质量增强，避免多步迭代的推理开销。兼顾生成质量和效率。

### 📊 实验结果
**数据集** VoiceBank-DEMAND，扩展低SNR测试集。

**主要指标** 在VoiceBank-DEMAND上达到生成方法领先性能，低SNR条件下强鲁棒性。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
SB理论结合RF实现一步生成有理论深度，在保持质量的同时大幅加速推理。

---

## [4] DBHN-Net: Dual-Branch Hybrid Neural Network For Low-Complexity Monaural Speech Enhancement

**arXiv ID** 2606.05911 | **方向** 语音前端

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-03 | **论文** https://arxiv.org/abs/2606.05911 | **PDF** https://arxiv.org/pdf/2606.05911.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
基于人工神经网络(ANN)的语音增强方法性能优异但高计算复杂度和高能耗阻碍实际部署。尖峰神经网络(SNN)有降低功耗的潜力，但离散二元激活和复杂时空动力学导致信息丢失。提出双分支混合神经(DBHN)网络：SNN分支降低功耗，ANN分支解决信息丢失。BandSplit和TF-Mamba模块压缩能耗同时增强性能。结果显示模型在三个公共数据集上保持优越性能，同时相比基线模型实现平均7.5倍计算复杂度降低。

### 🔧 技术方案

**模型架构** 双分支网络整合ANN和SNN：SNN分支降低功耗，ANN分支处理信息丢失。BandSplit和TF-Mamba模块用于压缩能耗和增强性能。交互模块和TF-Cross Attention-Fusion模块促进分支间信息融合。

**核心创新** ANN-SNN混合架构兼顾能效和性能。TF-Mamba引入选择性状态空间机制处理时频信息。

### 📊 实验结果
**数据集** 三个公共语音增强数据集。

**主要指标** 保持优越性能同时实现平均7.5倍计算复杂度降低。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
ANN-SNN混合设计有效平衡性能和能效，7.5倍复杂度降低有实用价值。

---

## [5] Age-Aware Adapter Tuning for Children's Speech Recognition

**arXiv ID** 2606.05440 | **方向** 语音前端

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-02 | **论文** https://arxiv.org/abs/2606.05440 | **PDF** https://arxiv.org/pdf/2606.05440.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
儿童自动语音识别(ASR)具有挑战性，因为儿童语音与成人不同且在不同发育阶段差异显著。适配器调优是适应大预训练ASR模型的有前景方法，但单一共享儿童适配器可能无法完全捕捉年龄依赖性变异。提出年龄感知适配器调优的系统研究，比较按年龄分组训练的专用适配器与统一FiLM适配器。真实年龄路由下，专用适配器将整体WER从12.6%降至12.3%，宏WER从18.4%降至17.6%。

### 🔧 技术方案

**模型架构** 年龄专用适配器：不同年龄组分别训练独立适配器。统一FiLM适配器：年龄条件FiLM调制。

**核心创新** 年龄感知适配vs统一适配的首次系统研究。发现专用适配器优于统一FiLM条件化。

### 📊 实验结果
**数据集** 3-12岁及以上儿童语音。

**主要指标** 整体WER 12.3% (vs 基线12.6%)，宏WER 17.6% (vs 基线18.4%)，所有年龄组一致改善。预测年龄路由接近真实年龄路由。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
首个年龄感知适配器系统研究，问题设置实际有价值，实验设计完整。

---

## [6] VoCodec: A Low-bitrate Streamable Neural Speech Codec with Voicing-driven Quantization

**arXiv ID** 2606.05892 | **方向** 语音前端

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-03 | **论文** https://arxiv.org/abs/2606.05892 | **PDF** https://arxiv.org/pdf/2606.05892.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
神经语音codec是语音传输和存储的关键，但大多数在帧间使用均匀量化，分配相同比特率而不考虑内容，造成浪费。提出VoCodec，具有发声驱动量化的低比特率可流式神经语音codec，根据感知敏感性为发声帧分配更高比特率、为非发声帧分配更低比特率。VoCodec在完全因果编码器-量化器-解码器框架中嵌入发声检测器，对发声帧使用残差标量-向量量化，对非发声帧使用简单标量量化。实验显示在16kHz LibriTTS上，即使比特率低至1.1 kbps也优于基线神经codec，且可降低约27%比特率。

### 🔧 技术方案

**模型架构** 完全因果编码器-量化器-解码器框架。发声检测器决定量化策略：发声帧用残差标量-向量量化，非发声帧用标量量化。

**核心创新** 发声驱动量化：感知导向的比特率分配，根据帧类型自适应调整量化精度。

### 📊 实验结果
**数据集** LibriTTS (16kHz)。

**主要指标** 1.1 kbps下优于基线，相比均匀量化策略降低约27%比特率。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
发声驱动量化策略合理，低比特率表现优异，工程实用性强。

---

## [7] To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval via Active Modality Detection

**arXiv ID** 2606.05931 | **方向** 语音前端

**作者** (论文未完整获取)

**机构** (论文未完整获取)

**发布日期** 2026-06-03 | **论文** https://arxiv.org/abs/2606.05931 | **PDF** https://arxiv.org/pdf/2606.05931.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
从视频档案中通过声音和人脸检索人员时，系统是否应该多模态？在真实世界广播档案中，目标可能只闻其声不见其人，或只见其人不闻其声。融合缺席模态的分数会注入噪声，将精度降至最佳单模态系统以下。提出查询自适应框架，通过跨模态分数一致性检测活动模态：当两个模态都活动时，一个模态检索的文件在另一个模态上评分也高；当模态缺席时一致性打破。在BBC Rewind语料库(12000+视频)上，自适应系统达到94.2% P@1，优于仅说话人(82.9%)、仅人脸(93.4%)和固定融合(90.0%)。

### 🔧 技术方案

**模型架构** 查询自适应框架：跨模态分数一致性驱动活动模态检测。分类器基于跨模态特征检测模态是否活动。

**核心创新** 自适应决定多模态vs单模态：在真实场景中灵活切换，避免错误融合降低精度。跨模态一致性作为模态检测信号。

### 📊 实验结果
**数据集** BBC Rewind (12000+广播视频)。

**主要指标** P@1 94.2% (vs 说话人82.9%、人脸93.4%、固定融合90.0%)，恢复64%的oracle差距(96.6%)。模态检测准确率89%。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
问题设置实际且有意义，自适应多模态策略有效提升检索精度。

---

## 📋 其他论文（快速浏览）

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*

### 语音大模型
## [13] The Silent Thought: Modeling Internal Cognition in Full-Duplex Spoken Dialogue Models via Latent Reasoning
**arXiv ID**: 2603.17837 | **评分**: 6/10
**链接**: https://arxiv.org/abs/2603.17837

## [14] RAS: a Reliability Oriented Metric for Automatic Speech Recognition
**arXiv ID**: 2604.24278 | **评分**: 6/10
**链接**: https://arxiv.org/abs/2604.24278

## [15] DuoGesture: Neuro-Inspired and Biomechanically Informed Dual-Stream Co-Speech Gesture Generation
**arXiv ID**: 2605.26236 | **评分**: 6/10
**链接**: https://arxiv.org/abs/2605.26236

## [16] MCBench: A Multicontext Safety Assessment Benchmark for Omni Large Language Models
**arXiv ID**: 2606.05177 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2606.05177

## [17] nnAudio 2: Overcoming Dynamic Compilation Barriers and Transform Inconsistencies
**arXiv ID**: 2606.05394 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2606.05394

## [18] Exploring LLMs for South Asian Music Understanding and Generation
**arXiv ID**: 2606.05522 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2606.05522

### 语音前端
## [19] Sound Effects Dataset Unification With the Universal Category System
**arXiv ID**: 2606.05571 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2606.05571

---

今日语音论文速递