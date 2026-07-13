# 2026-07-13 语音论文速递

**共收录**: 6 篇 | **语音大模型**: 4 篇 | **语音前端**: 2 篇

> 今日 arXiv 语音相关论文共命中 6 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] Optimal Transport-based Semantic Alignment for LLM-based Audio-Visual Speech Recognition

**arXiv ID** 2607.08863v1 | **方向** 语音大模型

**作者** (需从PDF提取)

**机构** School of Electronic Engineering & Computer Science, Queen Mary University of London, UK

**发布日期** 2026-07-10 | **论文** https://arxiv.org/abs/2607.08863v1 | **PDF** https://arxiv.org/pdf/2607.08863v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文针对LLM-AVSR中多模态融合的表示差异问题，提出基于最优传输（OT）的语义对齐框架。现有方法使用独立预训练的声学和视觉编码器，但融合时未显式处理模态间表示差异。本文通过OT估计概率耦合矩阵，将音频和视觉表示对齐到LLM的语言嵌入空间，再用于对比学习监督，实现语义一致且跨模态一致的表示学习。在LRS3-TED基准上验证，在干净和噪声条件各SNR下均达到SOTA。

### 🔧 技术方案

**模型架构** 基于Whisper的声学编码器 + AV-HuBERT视觉编码器 + LLaMA3.2-3B解码器。OT对齐模块在融合前对齐模态表示。

**核心创新** OT语义对齐：使用OT估计模态特定特征与语言嵌入之间的结构对应关系，用OT耦合作为软伪标签监督对比学习，将多模态特征锚定到LLM语言空间。

**训练策略** 两阶段：先通过OT对齐学习语义一致的跨模态表示，再用对齐后的表示进行多模态融合和解码。

### 📊 实验结果
**数据集** LRS3-TED基准

**主要指标** 在干净和噪声条件各SNR下均达到SOTA，超越强基线方法。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
OT对齐框架有效解决LLM-AVSR的模态差异问题，方法创新性强。LRS3-TED多条件验证证明有效性，达到SOTA性能值得肯定。

---

## [2] Why Do You Say It Like That? A Phoneme-Level Framework for Explainable Speech Deepfake Detection

**arXiv ID** 2607.08586v1 | **方向** 语音大模型

**作者** Anna Taylor, Michele Panariello, Massimiliano Todisco, Chiara Galdi, Nicholas Evans, Driss Matrouf

**机构** Laboratoire Informatique d'Avignon, Avignon Université, France

**发布日期** 2026-07-09 | **论文** https://arxiv.org/abs/2607.08586v1 | **PDF** https://arxiv.org/pdf/2607.08586v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音深度伪造检测准确率随wav2vec 2.0、HuBERT等自监督表示的使用而提升，但模型决策的可解释性仍是挑战。本文提出音素级分析框架，将模型预测与可测量的音素单元关联。使用Grad-CAM结合语音识别生成与音素和停顿对齐的显著图，揭示统计显著的攻防和说话人相关音素线索。在ASVspoof 5数据集验证，在保持与相似架构相当检测性能的同时提供语言学可解释分析。

### 🔧 技术方案

**模型架构** 基于CNN的语音深度伪造检测系统，结合wav2vec 2.0或HuBERT自监督表示。框架使用Grad-CAM生成音素级显著图。

**核心创新** 音素级可解释性框架：将深度伪造检测决策归因到具体音素单元，揭示人类可理解的攻防相关音素线索。

**训练策略** 后验可解释性方法，通常适用于各种基于CNN的语音深度伪造检测系统。

### 📊 实验结果
**数据集** ASVspoof 5

**主要指标** ASVspoof 5上达到与相似架构相当的检测性能，同时提供跨说话人和攻防条件的语言学可解释分析。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
可解释AI在语音安全领域具有重要价值。音素级分析与深度伪造检测的结合是创新工作，实验验证充分，有利于实际部署中的可信AI需求。

---

## [3] On the Role of Conversational Timing in Synthetic Training Data for ASR

**arXiv ID** 2607.09001v1 | **方向** 语音大模型

**作者** (需从PDF提取)

**机构** National Institute of Information and Communications Technology, Kyoto, Japan; Research Center for Information Technology Innovation, Academia Sinica, Taiwan

**发布日期** 2026-07-10 | **论文** https://arxiv.org/abs/2607.09001v1 | **PDF** https://arxiv.org/pdf/2607.09001v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
合成多说话人对话广泛用于训练对话ASR系统，但何种时序特性使模拟数据最有效仍不清晰。本文将对话时序作为可控训练变量而非仅是语料库统计量来研究。用指数倾斜族参数化停顿和重叠时序分布，通过拉丁超立方采样和多目标贝叶斯优化探索四维参数空间。每种采样时序配置生成模拟训练对话，训练ASR系统并在匈牙利语对话语料库上评估cpWER和cpCER。结果表明下游ASR行为与诱导时序统计更直接相关：高重叠暴露关联更低cpWER，更长更可变间隙关联更高cpWER。

### 🔧 技术方案

**模型架构** 合成对话生成系统 + ASR系统。参数化停顿和重叠时序分布。

**核心创新** 时序作为可控训练变量：系统研究对话时序对ASR训练的影响，揭示重叠-间隙权衡。

**训练策略** 拉丁超立方采样 + 多目标贝叶斯优化探索时序参数空间。

### 📊 实验结果
**数据集** 匈牙利语对话语料库

**主要指标** 重叠暴露降低cpWER，间隙增大和可变性与cpWER正相关。贝叶斯优化产生受控时序干预揭示重叠-间隙权衡。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
时序对ASR训练的影响研究有实际价值，揭示了合成对话数据中时序特性的重要性。多目标优化方法设计合理。

---

## [4] Phone Segmentation and Recognition through Phonological Activation Mapping

**arXiv ID** 2607.09020v1 | **方向** 语音大模型

**作者** (需从PDF提取)

**机构** Japan Advanced Institute of Science and Technology, Japan

**发布日期** 2026-07-10 | **论文** https://arxiv.org/abs/2607.09020v1 | **PDF** https://arxiv.org/pdf/2607.09020v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
音素切分和识别是内在相关的任务，但现代方法通常分别建模。本文认为音素结构已潜伏在自监督语音模型（S3M）的表示中，只需引导它们同时解决两个任务。利用S3M的音韵激活映射（SPAM），将每个S3M表示帧映射到音韵特征激活向量（如清浊音、鼻音）。在SPAM之上引入两个轻量级、无梯度下降的预测头：识别头和切回头。方法只需不到一分钟的音素转录即可生效，并可泛化到训练时未见音素。在多个数据集上达到强切分和识别性能。

### 🔧 技术方案

**模型架构** S3M (Self-Supervised Speech Models) + SPAM (Phonological Activation Mapping) + 轻量级预测头。

**核心创新** 音韵激活映射：利用S3M表示中已潜伏的音素结构，无需复杂训练即可同时完成音素切分和识别。

**训练策略** 不到一分钟音素转录即可训练，可泛化到未见音素。

### 📊 实验结果
**数据集** 多个语音数据集

**主要指标** 在多个数据集上达到强音素切分和识别性能，泛化能力得到验证。

**是否开源** 暂未明确。

### ⭐ 评分：7/10
利用自监督表示中已潜伏的音素结构是巧妙的方法，设计简洁有效。泛化能力和低训练成本是亮点。

---

## 🎙️ 语音前端

---

## [1] Technical Report for MERL's Real-TSE Challenge Submission

**arXiv ID** 2607.09043v1 | **方向** 语音前端

**作者** (需从PDF提取)

**机构** Mitsubishi Electric Research Laboratories (MERL), Cambridge, USA

**发布日期** 2026-07-10 | **论文** https://arxiv.org/abs/2607.09043v1 | **PDF** https://arxiv.org/pdf/2607.09043v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
目标语音提取（TSE）主要由在合成完全重叠数据上训练和评估的神经网络方法主导。Real-TSE Challenge旨在推进真实世界远场噪声和混响录音的性能。本文描述MERL对该挑战的提交。未提出新颖模型架构，而是在基线模型基础上主要关注数据准备和清洗。系统分四阶段训练：从完全重叠混合物的预训练，到带噪声和混响的模拟多说话人对话，再到使用来自处理过的近讲麦克风信号的伪目标的真实世界条件适应。提交在第二赛道获得第一名，证明了高质量数据准备的关键重要性。

### 🔧 技术方案

**模型架构** 基于基线TSE模型，四阶段训练流程。

**核心创新** 数据准备和清洗优先于模型架构改进。四阶段训练：合成预训练→模拟对话微调→真实远场适应。

**训练策略** 高质量数据准备和清洗是关键。DNSMOS和说话人相似度易被过度优化。

### 📊 实验结果
**数据集** Real-TSE Challenge

**主要指标** 第二赛道第一名。DNSMOS和说话人相似度可被驱动到极端值而不降低TER或VAD F1。

**是否开源** 暂未明确。

### ⭐ 评分：8/10
证明数据准备比模型架构改进更重要的实证研究有重要参考价值。Real-TSE Challenge第一名验证了方法有效性。

---

## [2] Clean2FX: Label-conditioned modeling for clean-to-effect guitar audio transformations

**arXiv ID** 2607.08952v1 | **方向** 语音前端

**作者** (需从PDF提取)

**机构** Queen Mary University of London, UK

**发布日期** 2026-07-09 | **论文** https://arxiv.org/abs/2607.08952v1 | **PDF** https://arxiv.org/pdf/2607.08952v1.pdf | **代码** 暂无 | **Demo** https://clean2fx.github.io/

### 📌 简介
本文提出Clean2FX，研究标签条件的清音到效果音转换的吉他音频变换。给定清音吉他输入和目标效果标签，任务是合成相应效果信号同时保留音乐内容。训练和评估对从EGFxSet真实单音录音构建，组装匹配清/效果音和弦、旋律和混音时间线。评估四种神经方法：两个VAE和两个U-Net（在线性或对数量幅度表示上操作）。U-Net模型优于VAE变体。失真效果最容易改进，而延迟和混响效果FAD增益较弱。条件敏感性诊断证明最佳模型响应目标标签而非崩溃到单一变换。

### 🔧 技术方案

**模型架构** 频谱图变换框架：两个VAE和两个U-Net（线性/对数幅度表示）。

**核心创新** 标签条件吉他音频效果变换，清音到效果音的受控转换。

**训练策略** EGFxSet数据集构建匹配清/效果音对，实现受控效果比较。

### 📊 实验结果
**数据集** EGFxSet

**主要指标** U-Net优于VAE。失真效果最易改进，延迟和混响效果FAD增益较弱。

**是否开源** Demo已上线：https://clean2fx.github.io/

### ⭐ 评分：6/10
吉他音频效果变换的研究有音乐应用价值，但属于特定领域音频处理，创新性一般。

---

今日语音论文速递