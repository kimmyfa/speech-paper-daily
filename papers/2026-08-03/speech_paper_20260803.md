# 2026-08-03 语音论文速递

**共收录**: 7 篇 | **语音大模型**: 4 篇 | **语音前端**: 3 篇

> 今日 arXiv 语音相关论文共命中 13 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] ParaASR: Multi-Token Prediction for Fast and Long-Context LLM-Based Speech Recognition

**arXiv ID** 2607.29279v1 | **方向** 语音大模型

**作者**：Lin, Qingjian, Li, Yuxin, Zhang, Haoyang, Chen, Jun, Huang, Yechang

**机构**：待确认

**发布日期**：2026-07-31 | **论文** https://arxiv.org/abs/2607.29279v1 | **PDF** https://arxiv.org/pdf/2607.29279v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
ParaASR针对音频编码器-LLM解码器架构中的推理效率问题提出了多token预测方法。当前的ASR系统采用自回归解码，但解码成本随decoder规模线性增长，在长上下文场景下尤为严重。ParaASR通过多token预测实现并行解码，显著降低推理延迟同时保持识别准确率。

### 🔧 技术方案

**模型架构**：基于音频编码器-LLM解码器架构，引入多token预测模块实现并行解码。模型从公开的音频-语言基础模型出发进行微调。

**核心创新**：提出多token预测机制，在单次前向传播中预测多个输出token，实现并行解码。与传统自回归解码相比，可大幅降低长音频的识别延迟。

**训练策略**：基于大规模音频-语言基础模型进行微调，使用多token预测目标函数进行训练。

### 📊 实验结果
**数据集**：实验在标准ASR基准数据集上进行评估

**主要指标**：在保持识别准确率的前提下，推理延迟相比传统自回归解码显著降低。具体数值待补充。

**是否开源**：待确认

### ⭐ 评分：8/10
多token预测是提升LLM-based ASR推理效率的重要方向，方法创新性强，具有实际应用价值。

---

## [2] Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens

**arXiv ID** 2607.29363v1 | **方向** 语音大模型

**作者**：Luo, Yi, Gu, Rongzhi, Yao, Jixun

**机构**：待确认

**发布日期**：2026-07-31 | **论文** https://arxiv.org/abs/2607.29363v1 | **PDF** https://arxiv.org/pdf/2607.29363v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
自回归语音生成面临序列长度、表示能力和长期稳定性的三重权衡问题。高帧率或高维度的表示能保留更多信号细节，但会使流式生成更容易出现错误传播导致的性能下降。本文提出低帧率高维连续token的稳定自回归语音生成方法。

### 🔧 技术方案

**模型架构**：采用低帧率高维连续token表示的自回归语音生成模型，平衡序列长度与表示能力。

**核心创新**：提出低帧率高维连续token表示方法，在保证生成质量的同时提高长期稳定性。通过特殊的tokenization策略减少错误传播。

**训练策略**：采用课程学习策略，从短音频逐步过渡到长音频训练，提升模型的长上下文生成能力。

### 📊 实验结果
**数据集**：在标准语音生成数据集上评估

**主要指标**：相比高帧率表示，生成稳定性显著提升；相比低维表示，语音质量保持良好。具体数值待补充。

**是否开源**：待确认

### ⭐ 评分：7/10
针对自回归语音生成的核心挑战提出解决方案，技术思路清晰，有一定创新性。

---

## [3] DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual Speech Recognition with LLMs

**arXiv ID** 2607.29112v1 | **方向** 语音大模型

**作者**：Cheng, Ziwei, Tan, Zhenhua, Zhu, Zhuomin

**机构**：东北大学软件学院

**发布日期**：2026-07-30 | **论文** https://arxiv.org/abs/2607.29112v1 | **PDF** https://arxiv.org/pdf/2607.29112v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
视听语音识别(AVSR)需要有效融合音频和视觉模态，但现有方法将跨模态交互视为单步操作，缺乏结构化的迭代优化。DoubleHelix提出双螺旋结构的多模态融合框架，将融合重新表述为迭代细化过程。

### 🔧 技术方案

**模型架构**：双螺旋结构的多模态融合框架，包含音频分支和视觉分支，通过多层迭代实现跨模态信息交互。

**核心创新**：提出结构化迭代融合机制，而非传统单步融合。每一层迭代中，音频和视觉特征相互增强，逐步提升表示质量。

**训练策略**：采用多阶段训练策略，先分别预训练单模态编码器，再联合训练融合模块。

### 📊 实验结果
**数据集**：在主流视听语音识别数据集上评估

**主要指标**：相比单步融合方法，识别准确率显著提升，特别是在噪声环境下提升明显。

**是否开源**：待确认

### ⭐ 评分：8/10
双螺旋结构创新性强，针对AVSR的核心问题提出有效解决方案。

---

## [4] Cloned Voices, Real Consequences: Evaluating Bias in Political Deepfake Detection for Electoral Integrity in Brazil

**arXiv ID** 2607.28770v1 | **方向** 语音大模型

**作者**：Gris, Lucas Rafael Stefanel, Casanova, Daniel, De Oliveira, Frederico Santos, Ferreira, Alef Iury, Felício, Beatriz Almeida

**机构**：Federal University of Goiás / Ermis, Federal University of Technology – Paraná

**发布日期**：2026-07-29 | **论文** https://arxiv.org/abs/2607.28770v1 | **PDF** https://arxiv.org/pdf/2607.28770v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
生成式AI的最新进展使得伪造言论和放大政治假信息变得更加容易。本文提出ParlaSpoof-BR，一个基于巴西众议院录音构建的音频deepfake数据集，并评估政治deepfake检测中的偏见问题。

### 🔧 技术方案

**模型架构**：基于深度学习的音频deepfake检测系统，使用预训练的音频编码器提取特征，后接分类头进行二分类。

**核心创新**：构建了针对巴西政治场景的专项deepfake数据集ParlaSpoof-BR，该数据集基于真实的众议院发言录制并扩展了合成样本。系统性地评估了检测模型在不同说话人、口音和音频条件下的偏见。

**训练策略**：使用开源数据训练deepfake检测器，在ParlaSpoof-BR数据集上进行评估。

### 📊 实验结果
**数据集**：ParlaSpoof-BR数据集（巴西众议院音频+合成deepfake）

**主要指标**：Pooled EER达到1.454%，在14个测试集上优于当前公开系统。在5个单独测试集上获得最低EER。

**是否开源**：代码和数据集将开源

### ⭐ 评分：8/10
针对政治选举场景的语音deepfake检测具有重要社会意义，数据集构建和偏见评估工作扎实。

---

## 语音前端

## [5] RIPPLE: Generating Multi-Channel Phase, Not Recovering It

**arXiv ID** 2607.27775v1 | **方向** 语音前端

**作者**：Lee, Jaehyuk, Lee, Yeajin, Shin, Dayeon, Lee, Donghun

**机构**：Korea University, Department of Mathematics; Korea University, Program in Actuarial Science and Financial Engineering

**发布日期**：2026-07-29 | **论文** https://arxiv.org/abs/2607.27775v1 | **PDF** https://arxiv.org/pdf/2607.27775v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
生成模型可以高保真合成幅度谱，而相位则交给独立应用于每个通道的恢复模块（如Griffin-Lim、声码器或潜在解码器）。对于多通道波形，这种分离代价高昂：空间音频和三分量地震图的物理内容存在于通道间的相位关系中，而这正是通道独立恢复无法产生的。本文提出RIPPLE，将Griffin-Lim重新解释为相位先验而非最终估计器。

### 🔧 技术方案

**模型架构**：基于修正流(Rectified Flow)的相位生成模型，包含源相位初始化模块和相位细化网络。

**核心创新**：将Griffin-Lim重新解释为相位先验，从源相位初始化，携带待保留的通道间结构。使用显式的通道间相位损失通过修正流将先验精炼到目标。

**训练策略**：使用修正流训练，通道间相位损失作为主要优化目标。

### 📊 实验结果
**数据集**：一阶声学环境传输(First-Order Ambisonics)、跨台站地震数据转换

**主要指标**：在下游分析使用的相干性指标上优于基于恢复的管道。地震案例具有决定性：跨架构不同的生成器，每通道恢复使S波偏振误差接近57.3°的随机期望，而学习相位将其降至33.8°。

**是否开源**：待确认

### ⭐ 评分：9/10
相位生成思路新颖，解决了多通道音频处理中的核心问题，方法创新性强。

---

## [6] Model-Agnostic Meta-Learning Initialization for Distributed Multichannel Active Noise Control

**arXiv ID** 2607.29117v1 | **方向** 语音前端

**作者**：Shen, Xiaoyi, Ji, Junwei, Gan, Woon-Seng, Shi, Dongyuan, Yang, Jun

**机构**：State Key Laboratory of Acoustics and Marine Information, Institute of Acoustics, Chinese Academy of Sciences; Nanyang Technological University; Northwestern Polytechnical University; University of Chinese Academy of Sciences

**发布日期**：2026-07-30 | **论文** https://arxiv.org/abs/2607.29117v1 | **PDF** https://arxiv.org/pdf/2607.29117v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
分布式多通道主动噪声控制(DMCANC)已成为大面积降噪的可扩展框架，多个节点运行本地单通道ANC控制器并交换信息以实现全局控制。现有DMCANC实现的关键局限是每个节点从随机初始化开始，需要大量通信才能收敛。

### 🔧 技术方案

**模型架构**：基于模型无关元学习(MAML)的分布式ANC初始化框架，每个节点通过元学习获得良好的初始化参数。

**核心创新**：利用MAML为DMCANC系统提供快速收敛的初始化，使各节点仅需少量通信即可达到良好性能。提出基于任务分布的元训练策略。

**训练策略**：采用MAML两阶段训练：元训练阶段学习泛化初始化，元适应阶段快速适应具体噪声场景。

### 📊 实验结果
**数据集**：模拟大规模室内噪声环境

**主要指标**：相比随机初始化，收敛速度提升明显，通信开销显著降低。在大面积场景下仍保持良好的降噪性能。

**是否开源**：待确认

### ⭐ 评分：7/10
将MAML应用于DMCANC的思路有创新性，实际工程价值较高。

---

## [7] Leveraging Beam Search Information for Confidence Estimation in E2E ASR

**arXiv ID** 2607.29299v1 | **方向** 语音前端

**作者**：Jia, Yichen, Van hamme, Hugo

**机构**：Department Electrical Engineering ESAT-PSI, KU Leuven, Belgium

**发布日期**：2026-07-31 | **论文** https://arxiv.org/abs/2607.29299v1 | **PDF** https://arxiv.org/pdf/2607.29299v1.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
为端到端ASR系统估计置信度，现有研究提出置信度估计模块(CEM)来整合ASR模型 backbone 的特征。然而大多数现有方法依赖于特定架构。本文提出Score-Rank方法，不依赖具体模型架构，利用beam search信息进行置信度估计。

### 🔧 技术方案

**模型架构**：基于Score-Rank的置信度估计框架，使用beam search的评分和排名信息。

**核心创新**：提出架构无关的置信度估计方法，不依赖特定ASR模型内部特征。利用beam search过程中产生的多个候选的评分和排名模式来估计识别结果的可靠性。

**训练策略**：使用带置信度标注的ASR数据训练Score-Rank模型，学习评分模式与真实置信度之间的映射。

### 📊 实验结果
**数据集**：在标准ASR置信度估计基准数据集上评估

**主要指标**：相比现有架构依赖的方法，在多个ASR模型上取得相当或更好的置信度估计性能。

**是否开源**：待确认

### ⭐ 评分：7/10
置信度估计是ASR实用化的关键问题，架构无关的方法具有更广泛的适用性。

---

今日语音论文速递
