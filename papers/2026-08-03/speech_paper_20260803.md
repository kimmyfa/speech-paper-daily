# 2026-08-03 语音论文速递

**共收录**: 6 篇 | **语音大模型**: 5 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 6 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] ParaASR: Multi-Token Prediction for Fast and Long-Context LLM-Based Speech Recognition

**arXiv ID** 2607.29279 | **方向** 语音大模型

**作者**：Qingjian Lin, Yuxin Li, Haoyang Zhang, Jun Chen, Yechang Huang, Feng Tian, Xie Li, Xiangyu Tony Zhang, Daijiao Liu, Yuxin Zhang, Jinglan Gong, Bo Zhao, Fei Tian, Xuerui Yang, Gang Yu, Xiangyu Zhang, Daxin Jiang

**机构**：StepFun, NTU, PKU, UNSW, SJTU, USTC

**发布日期**：2026-07-31 | **论文** https://arxiv.org/abs/2607.29279 | **PDF** https://arxiv.org/pdf/2607.29279.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
ParaASR是一个基于LLM的ASR系统，利用多Token预测（MTP）技术让4B参数LLM解码器在每个前向步骤中输出多个token。不同于开放式文本生成，语音转录与音频信号紧密相关，这为高并行度解码提供了天然的归纳偏置。系统每步可接受6个token中的5个，证实了语音的确定性结构使ASR成为多token解码的自然场景。模型支持32K上下文窗口，可单次转录最长30分钟音频。

### 🔧 技术方案

**模型架构**：编码器-适配器-解码器架构，冻结的0.6B音频编码器来自多模态基础模型，8×时间下采样产生80ms间隔的声学嵌入。4B dense Transformer解码器支持原生32K上下文。MTP-5模块包含5个分支，每步并行预测未来1-5个token。

**核心创新**：1）将多token预测作为可验证的前瞻机制，保留自回归解码的安全性；2）分段训练策略：先进行ASR监督微调建立稳健的自回归识别器，然后通过冻结分支对齐和联合校准两阶段优化MTP分支；3）自回归验证确保最终转录与标准解码同样可靠。

**训练策略**：音频语言预训练建立 multimodal foundation（1.356T文本和音频token），包含语音-文本对齐、音频token扩展、统一多模态预训练和cooldown四个阶段。ASR SFT使用约100K小时短语音和50K小时长语音伪标签数据。MTP训练采用两阶段：冻结分支对齐（仅优化MTP块，学习率2e-4）和联合校准（解冻适配器和LLM解码器，学习率2e-5）。

### 📊 实验结果
**数据集**：AISHELL-1, AISHELL-2, WenetSpeech, FLEURS, LibriSpeech, Common Voice, VoxPopuli, Earnings22等

**主要指标**：
- 中文：平均CER 2.97%，AISHELL-1达0.71%
- 英文：平均WER 3.68%，LibriSpeech clean达1.38%
- 长音频：平均WER 3.70%
- RTF：0.0053（单GPU H800），远低于Qwen3-ASR-1.7B的0.0094
- MTP接受率：平均5.0/6 tokens

**是否开源**：暂无

### ⭐ 评分：9/10
该工作完美解决了LLM-based ASR中解码器规模与推理延迟的根本矛盾。核心洞见——利用语音信号的确定性结构实现多token并行解码——既有理论创新又有工程价值。实验覆盖中英长音频多个benchmark，RTF 0.0053达到实时级别，产品潜力显著。

---

## [2] Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens

**arXiv ID** 2607.29363 | **方向** 语音大模型

**作者**：Yi Luo, Rongzhi Gu, Jixun Yao

**机构**：Columbia University, ByteDance Seed

**发布日期**：2026-07-31 | **论文** https://arxiv.org/abs/2607.29363 | **PDF** https://arxiv.org/pdf/2607.29363.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文研究自回归语音生成中如何平衡序列长度、表示能力和长程稳定性的核心问题。高帧率或高容量的表示可以保留更多信号细节，但使流式生成更容易受到分布漂移和AR误差累积的影响；更短更压缩的表示简化AR建模，但有限带宽可能丢弃重要信息。本文提出低帧率、高维、高带宽连续表示与流式生成框架的协同设计，以支持稳健的高保真重建、强大的单token可预测性和卓越的长程稳定性。

### 🔧 技术方案

**模型架构**：
1. **Locodec**：局部编码的tokenizer，塑造表示空间以改善低维核心流形的可插值性和原生高维坐标的可辨识性。采用mid/side输入 formulation 和 MDCT前端，全局部编码器，堆叠因果卷积解码器。训练目标包括重建、均匀化和可辨识性。
2. **MP-ELD**：单token AR flow-matching框架，使用多路径信息路由和残差无分类器引导（residual CFG）来缓解误差累积。ELD框架通过encoder-LM-decoder结构建模，信息通过多个路径传递，正交残差条件化实现不同类型信息的解耦控制。

**核心创新**：1）通过几何分析证明高维球面直接构造密集可插值性在数学上不切实际，提出构建嵌入高维空间内的低维流形；2）Locodec的token空间围绕低维核心流形组织，同时保持高维坐标的能量层次以提高可辨识性；3）MP-ELD通过显式信息路由和训练时路径dropout，鼓励不同方面的音频状态通过不同条件化路径表示。

**训练策略**：tokenizer训练关注可插值性、可辨识性和重建质量。生成模型使用flow-matching目标训练，无需外部SSL/ASR模型或预训练文本语言模型。

### 📊 实验结果
**数据集**：Seed-TTS-eval

**主要指标**：8Hz 768维token：
- 重建质量：保留重建质量
- 单token可预测性：显著改善
- WER：具有竞争力
- 长形式合成：稳定

**是否开源**：暂无

### ⭐ 评分：8/10
理论贡献突出：关于高维表示几何性质的数学分析令人信服。Locodec和MP-ELD的协同设计解决了自回归生成中长程稳定性这一核心难题。无需外部SSL/ASR模型即可达到竞争力，体现了方法论的独立性。

---

## [3] DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual Speech Recognition with LLMs

**arXiv ID** 2607.29112 | **方向** 语音大模型

**作者**：Ziwei Cheng, Zhenhua Tan, Zhuomin Zhu

**机构**：东北大学 (Northeastern University, China)

**发布日期**：2026-07-31 | **论文** https://arxiv.org/abs/2607.29112 | **PDF** https://arxiv.org/pdf/2607.29112.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
视听语音识别（AVSR）依赖音频和视觉模态的有效融合，但现有方法将跨模态交互视为单步操作，缺乏结构化的迭代细化。本文提出DoubleHelix，将融合重新表述为具有自适应退化感知增强的迭代跨模态交互过程。框架包含三个组件：ReverseParallelHelix实现多轮结构化交互与学习对齐约束，QualitySensor学习退化感知门控信号，HelixReplication实现一致性引导的条件特征增强。

### 🔧 技术方案

**模型架构**：
- ReverseParallelHelix：多轮结构化交互模块，使用学习到的对齐约束进行双向跨模态信息交换
- QualitySensor：自适应门控机制，根据音频质量动态调整模态融合权重
- HelixReplication：一致性引导的特征增强，保持视听特征的一致性

**核心创新**：1）将融合从单步操作转变为迭代过程，模拟生物视觉和听觉信息的协同处理机制；2）引入退化感知门控，根据环境噪声水平动态调整模态权重；3）非对称路径权重设计优化视听信息流。

**训练策略**：待补充

### 📊 实验结果
**数据集**：LRS3

**主要指标**：
- Clean音频：0.68% WER，比之前最佳结果提升5.6%（相同backbone设置）
- Babble噪声 SNR -5dB：11.6% WER

**是否开源**：暂无

### ⭐ 评分：8/10
ACM MM2026接收。迭代跨模态交互的设计思路新颖，退化感知门控在噪声条件下的鲁棒性提升显著（5.6%相对提升）。在LRS3上达到0.68% WER的clean性能处于领先水平。

---

## [4] Leveraging Beam Search Information for Confidence Estimation in E2E ASR

**arXiv ID** 2607.29299 | **方向** 语音大模型

**作者**：Yichen Jia, Hugo Van hamme

**机构**：KU Leuven (鲁汶大学, 比利时)

**发布日期**：2026-07-31 | **论文** https://arxiv.org/abs/2607.29299 | **PDF** https://arxiv.org/pdf/2607.29299.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
端到端ASR系统的置信度估计是可靠应用的关键。现有的置信度估计模块通常依赖于ASR模型主干的特征，但大多数方法与特定架构绑定。本文提出Score-Rank置信度估计模块（SR-CEM），这是一个轻量级模块，利用beam search信息生成token级和word级置信度分数。SR-CEM通过结合hypothesis内token的分数和排名来构建特征。

### 🔧 技术方案

**模型架构**：轻量级置信度估计模块SR-CEM：
- Score特征：利用beam search中每个token的分数
- Rank特征：token在beam中的排名信息
- 结合方式：分数与排名的融合表示

**核心创新**：1）利用beam search过程中自然产生的分数和排名信息，无需额外训练参数；2）架构无关设计，可应用于各种E2E ASR架构（hybrid、transducer等）；3）同时生成token级和word级置信度。

**训练策略**：待补充

### 📊 实验结果
**数据集**：英语域内和域外测试集，荷兰语、噪声和对话语音

**主要指标**：
- 域内测试集 token级：MCE 4.50%, ECE 0.30%（vs softmax置信度20.04%和1.75%）
- 域内测试集 word级：MCE 8.17%, ECE 0.35%（vs softmax 17.91%和1.67%）
- 跨架构鲁棒性：适用于hybrid和transducer架构，不同解码策略

**是否开源**：暂无

### ⭐ 评分：7/10
ICASSP 2026发表。SR-CEM在降低最大校准误差（MCE）方面表现突出，这对可靠的下游应用至关重要。架构无关的设计增强了通用性。但在域外泛化方面仍有提升空间。

---

## [5] Cloned Voices, Real Consequences: Evaluating Bias in Political Deepfake Detection for Electoral Integrity in Brazil

**arXiv ID** 2607.28770 | **方向** 语音大模型

**作者**：Lucas Rafael Stefanel Gris, Daniel Casanova, Frederico Santos De Oliveira, Alef Iury Ferreira, Beatriz Almeida Felício, Raul César Reis Mata, Anderson da Silva Soares

**机构**：巴西研究机构（具体信息待补充）

**发布日期**：2026-07-30 | **论文** https://arxiv.org/abs/2607.28770 | **PDF** https://arxiv.org/pdf/2607.28770.pdf | **代码** https://huggingface.co/datasets/freds0/ParlaSpoof-BR | **Demo** https://ermisai.github.io/parlaspoof-br-demo

### 📌 简介
生成式AI的进展使制作假音频更容易，并在选举期间放大政治虚假信息。本文引入ParlaSpoof-BR，一个来自巴西众议院记录并通过多种TTS和语音转换模型扩展的音频deepfake数据集。使用该数据集对先进的音频deepfake检测器进行基准测试，检验其对巴西葡萄牙语政治语音的泛化能力，并分析预测中的潜在偏见。

### 🔧 技术方案

**数据集构建**：
- 来源：巴西众议院官方音频档案
- 规模：40名说话人（性别和地区平衡），2000个真实样本
- 攻击类型：TTS（5种系统）、语音转换（5种系统）、部分操控（音频填充）

**评估维度**：
- 检测系统：AASIST、AASIST-L、DF-Arena-1B
- 鲁棒性条件：语音增强、有损压缩、 babble噪声

**核心发现**：1）方法论因素（合成模型选择、操控程度）主导性能差异，超越人口统计差异；2）部分操控比完全合成更难检测（25%修改的召回率仅29.2%）；3）合成模型偏见最大（68.5pp差距），性别偏见最小（0.7pp）。

### 📊 实验结果
**数据集**：ParlaSpoof-BR（134,400文件：11,200真实，123,200伪造）

**主要指标**：
- 总体EER：AASIST 50.98%, AASIST-L 53.70%, DF-Arena-1B 32.30%
- 合成模型偏见：recall从31.2%（Qwen3-TTS）到99.7%（OpenVoice-v2），68.5pp差距
- 部分操控检测：25%修改召回29.2%，75%修改召回73.5%
- 噪声鲁棒性：SNR 10dB时22.2% previously detected deepfakes逃避检测

**是否开源**：数据集已开源

### ⭐ 评分：7/10
首个葡萄牙语政治语音deepfake基准数据集，社会意义重大。揭示了当前检测器在域迁移和实际场景中的严重局限性。方法论偏见超过人口统计偏见的发现对公平性研究有重要启示。

---

## [6] Model-Agnostic Meta-Learning Initialization for Distributed Multichannel Active Noise Control

**arXiv ID** 2607.29117 | **方向** 语音前端

**作者**：Xiaoyi Shen, Junwei Ji, Woon-Seng Gan, Dongyuan Shi, Jun Yang

**机构**：中国科学院声学研究所, 南洋理工大学, 西北工业大学

**发布日期**：2026-07-31 | **论文** https://arxiv.org/abs/2607.29117 | **PDF** https://arxiv.org/pdf/2607.29117.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
分布式多通道主动噪声控制（DMCANC）已成为大规模噪声衰减的可扩展框架，其中多个节点运行本地单通道ANC控制器并交换信息以实现全局控制。现有DMCANC实现的关键限制在于依赖零或随机初始化，导致自适应滤波器收敛缓慢，限制节点间协作效率。本文提出基于模型无关元学习（MAML）的DMCANC初始化策略。

### 🔧 技术方案

**模型架构**：MAML初始化框架：
- 任务定义：每个DMCANC节点的不同声学配置作为一个任务
- 元学习：跨节点聚合异构声学特征（包括主通道和次通道）
- 初始化部署：将学习到的初始化部署到所有节点

**核心创新**：1）利用MAML学习可泛化的初始化，使新场景下的快速适应成为可能；2）通过间歇通信（IC）策略减少通信负担；3）补偿滤波器补偿自次通道和互次通道之间的差异。

**训练策略**：
- MAML训练：使用宽带噪声（100-1200Hz, 800-1500Hz, 1200-2000Hz）训练最优初始系数
- 数据划分：70%训练，30%验证
- 在线部署：MAML初始化作为每个节点的初始控制滤波器

### 📊 实验结果
**数据集**：6节点DMCANC系统，实测声学环境

**主要指标**：
-  tonal噪声（315Hz, 500Hz）：所有节点最快收敛
- 宽带噪声（200-800Hz）：最快收敛
- 真实录音噪声（压缩机噪声）：从控制开始即抑制噪声，其他方法约10秒后开始明显衰减

**是否开源**：暂无

### ⭐ 评分：7/10
MAML应用于ANC初始化的创新尝试，解决了分布式ANC中自适应滤波器收敛慢的实际问题。在多种噪声条件下的收敛加速效果显著，工程价值明确。理论创新相对有限，但问题定义清晰，实验充分。

---

## 附录：今日论文速递
