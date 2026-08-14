# 2026-08-03 语音论文速递

**共收录**: 6 篇 | **语音大模型**: 5 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 6 篇。

---

## 语音大模型

---

## [1] ParaASR: Multi-Token Prediction for Fast and Long-Context LLM-Based ASR

**arXiv ID**：2607.29279 | **方向**：语音大模型

**作者**：Qingjian Lin, Yuxin Li, Haoyang Zhang, Jun Chen, Yechang Huang, Feng Tian, Xie Li, Xiangyu Tony Zhang, Daijiao Liu, Yuxin Zhang, Jinglan Gong, Bo Zhao, Fei Tian, Xuerui Yang, Gang Yu, Xiangyu Zhang, Daxin Jiang

**机构**：StepFun; NTU; PKU; UNSW; SJTU; USTC

**发布日期**：2026-07-31 | **论文**：https://arxiv.org/abs/2607.29279 | **PDF**：https://arxiv.org/pdf/2607.29279.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
LLM-based ASR面临解码器规模与推理延迟的根本矛盾——更大的解码器提供更好的语言建模但每个token都需要计算。ParaASR利用语音转录的确定性结构（与开放文本生成不同，ASR输出紧密锚定输入音频信号），引入多Token预测（MTP）技术让4B参数LLM解码器每步并行输出6个token（平均接受5.0个）。系统原生支持32K上下文窗口，单次可转录最长30分钟音频。在中文benchmark上平均CER 2.97%，英文平均WER 3.68%，RTF低至0.0053（单GPU H800），显著优于Qwen3-ASR-1.7B（RTF 0.0094）。

### 🔧 技术方案

**问题背景：** 音频编码器-LLM解码器架构已成为现代ASR主流范式，但自回归解码的计算成本随解码器规模线性增长。语音转录与开放文本生成不同——给定音频信号和之前转录，局部未来主要是忠实延续而非开放选择，这为高并行度解码提供了天然归纳偏置。

**模型架构：** 编码器-适配器-解码器架构。音频编码器为0.6B Transformer（来自Qwen3-Omni，冻结），8×时间下采样产生80ms间隔的声学嵌入。线性适配器将声学嵌入映射到解码器隐藏空间。解码器为4B密集Transformer，原生32K上下文窗口（可处理30分钟音频）。MTP-5模块包含5个分支，每步并行预测未来1-5个token。每个MTP block接收前一个分支的隐藏状态和移位token嵌入，经归一化、拼接、投影后通过Transformer block处理。所有分支共享embedding层和LM head。

**核心创新：** (1) 识别语音转录的确定性结构为MTP的关键机遇——ASR中局部未来高度可预测，MTP接受率达5.0/6 token，远超开放文本生成场景；(2) 分段训练策略：先建立稳健的自回归识别器（ASR SFT，~100K小时短语音+50K小时长语音），再通过冻结分支对齐（仅优化MTP block，lr 2e-4）和联合校准（解冻适配器和解码器，lr 2e-5）两阶段优化MTP分支；(3) 自回归验证确保安全——一旦未来token与正常解码路径不一致，拒绝后续所有提议token，保证最终转录与标准解码同样可靠；(4) 原生32K上下文支持30分钟音频单次转录，无需chunk-and-stitch管线。

**训练策略：** 音频语言预训练（1.356T文本和音频token，4阶段：语音-文本对齐100B/音频token扩展256B/统一多模态800B/cooldown 200B）。ASR SFT：~100K小时短语音（多领域+方言+远场）+ 50K小时长语音（ROVER多系统融合+LLM精炼），10K步，lr 2e-5，global batch 32。MTP训练：两阶段，各10K步，指数衰减权重α=0.9。SpecAugment时间/频率掩码作为正则化。

### 📊 实验结果
**数据集**：AISHELL-1/2, WenetSpeech, FLEURS, LibriSpeech, Common Voice, VoxPopuli, Earnings22等

**主要指标**：
- 中文平均CER：2.97%（AISHELL-1 0.71%，FLEURS zh 2.63%）
- 英文平均WER：3.68%（LibriSpeech clean 1.38%，VoxPopuli 2.76%）
- 长音频平均WER：3.70%（LibriSpeech clean long 1.27%，Earnings22 6.52%）
- RTF：0.0053（vs Qwen3-ASR-1.7B 0.0094，快1.77倍）
- MTP接受率：MTP-5平均5.0/6，MTP-3平均3.6/4，MTP-7平均6.1/8
- MTP消融：添加MTP前后平均CER/WER波动<0.06，证明MTP是安全的加速原语

**是否开源**：暂无

### ⭐ 评分：9/10
评分理由：完美解决了LLM-based ASR中解码器规模与推理延迟的根本矛盾。核心洞见——利用语音信号确定性结构实现多token并行解码——既有理论创新又有工程价值。MTP接受率5.0/6验证了ASR作为MTP天然场景的猜想。实验覆盖中英长音频多个benchmark，RTF 0.0053达到实时级别，产品潜力显著。分阶段训练策略（SFT→MTP对齐→联合校准）设计精巧。

---

## [2] Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens

**arXiv ID**：2607.29363 | **方向**：语音大模型

**作者**：Yi Luo, Rongzhi Gu, Jixun Yao

**机构**：Columbia University; ByteDance Seed

**发布日期**：2026-07-31 | **论文**：https://arxiv.org/abs/2607.29363 | **PDF**：https://arxiv.org/pdf/2607.29363.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
自回归语音生成中，高帧率高容量表示保留更多信号细节但易受分布漂移和误差累积影响，低帧率压缩表示简化AR建模但可能丢弃重要信息。本文提出协同设计低帧率（8Hz）、高维（768维）、高带宽连续表示与流式生成框架。Locodec tokenizer通过局部编码和训练目标塑造表示空间几何——围绕低维核心流形组织高维空间以改善可插值性，同时保持高维坐标能量层次以改善可辨识性。MP-ELD生成框架使用多路径信息路由和残差无分类器引导（residual CFG）缓解误差累积。无需外部SSL/ASR模型或预训练文本语言模型即可达到有竞争力的WER和稳定的长形式合成。

### 🔧 技术方案

**问题背景：** 自回归语音生成面临信息容量与长程稳定性的权衡。高带宽表示保留更多信号细节但预测误差在AR系统中累积导致漂移（响度、音色、语速、频谱质量退化甚至崩溃）。现有方法依赖语义-声学解耦（如SSL/ASR模型提供语义空间）来降低建模难度，但外部模型引入偏置，限制了tokenizer编码非语义信息的能力。

**模型架构：** 双组件设计。(1) Locodec tokenizer：mid/side输入公式+MDCT前端，全局部编码器（无下采样/自注意力），堆叠因果卷积解码器。重建损失+均匀化损失+可辨识性损失。训练目标关注可插值性、可辨识性和重建质量。(2) MP-ELD生成框架：encoder-LM-decoder架构，多路径信息路由——不同路径通过正交残差条件化携带不同类型信息（如声学一致性和外部条件对齐）。残差CFG允许独立控制不同路径的引导强度。使用flow-matching目标训练，桥接时间采样。

**核心创新：** (1) 通过数学分析证明高维球面上直接构造密集可插值性不切实际（N=256时30°球冠覆盖需~10^78个区域），提出构建嵌入高维空间内的低维流形——核心流形保持可插值性，高维坐标保持能量层次提供可辨识性；(2) Locodec通过均匀化损失（encouraging low-dimensional manifold）和可辨识性损失（energy hierarchy）协同塑造表示空间，无需外部SSL/ASR模型；(3) MP-ELD通过显式信息路由和训练时路径dropout，鼓励不同方面的音频状态通过不同条件化路径表示，使CFG可以独立控制不同路径的引导强度，显著减少长程合成中的累积声学漂移。

**训练策略：** Tokenizer训练关注重建质量、可插值性和可辨识性。生成模型使用flow-matching目标，无需外部SSL/ASR模型或预训练文本语言模型，也无需后训练阶段。8Hz 768维连续token配置。

### 📊 实验结果
**数据集**：Seed-TTS-eval

**主要指标**：
- 8Hz 768维token：重建质量保持，单token可预测性显著改善
- WER：具有竞争力（与使用外部SSL/ASR模型的方法相比）
- 长形式合成：稳定（无累积漂移）
- 无需外部SSL/ASR模型、预训练文本语言模型或后训练阶段

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：理论贡献突出——关于高维表示几何性质的数学分析（球冠覆盖的指数增长）令人信服且具有指导意义。Locodec和MP-ELD的协同设计解决了自回归生成中长程稳定性这一核心难题。无需外部模型即可达到竞争力，体现了方法论的独立性。但实验仅在Seed-TTS-eval上评估，规模有限，且缺乏与现有codec方法的系统对比。

---

## [3] DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual Speech Recognition with LLMs

**arXiv ID**：2607.29112 | **方向**：语音大模型

**作者**：Ziwei Cheng, Zhenhua Tan, Zhuomin Zhu

**机构**：Northeastern University (东北大学), China

**发布日期**：2026-07-31 | **论文**：https://arxiv.org/abs/2607.29112 | **PDF**：https://arxiv.org/pdf/2607.29112.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
视听语音识别（AVSR）依赖音频和视觉模态的有效融合，但现有方法将跨模态交互视为单步操作，缺乏结构化的迭代细化。本文提出DoubleHelix，将融合重新表述为具有自适应退化感知增强的迭代跨模态交互过程，包含三个核心组件：ReverseParallelHelix实现多轮结构化交互与学习对齐约束，QualitySensor学习退化感知门控信号，HelixReplication实现一致性引导的条件特征增强。在LRS3数据集上，clean音频WER达0.68%（相对改善5.6%），babble噪声SNR -5dB条件下WER为11.6%。被ACM MM 2026接收。

### 🔧 技术方案

**问题背景：** AVSR融合音频和视觉模态提升噪声鲁棒性，但现有方法将跨模态交互视为单步操作，缺乏迭代细化。此外，音频质量动态变化（从clean到高噪声），固定融合策略无法适应。需要一种结构化迭代融合机制，能够根据音频质量动态调整跨模态交互强度。

**模型架构：** 三组件架构：(1) ReverseParallelHelix——多轮结构化跨模态交互模块，使用学习到的对齐约束进行双向信息交换，模拟生物视觉和听觉信息的协同处理机制；(2) QualitySensor——自适应门控机制，学习退化感知门控信号，根据环境噪声水平动态调整模态融合权重；(3) HelixReplication——一致性引导的条件特征增强，保持视听特征的一致性。非对称路径权重设计优化视听信息流。

**核心创新：** (1) 将AVSR融合从单步操作转变为迭代跨模态交互过程（ReverseParallelHelix），模拟生物视觉和听觉信息的协同处理机制，这在AVSR领域是首次；(2) 引入QualitySensor退化感知门控，根据环境噪声水平动态调整模态权重——在clean条件下侧重音频，在有噪条件下增加视觉权重；(3) 非对称路径权重设计，优化视听信息流，避免对称融合带来的信息冗余。

**训练策略：** 被ACM MM 2026接收，具体训练细节在论文中。

### 📊 实验结果
**数据集**：LRS3

**主要指标**：
- Clean音频：0.68% WER（相对改善5.6%，相同backbone设置）
- Babble噪声 SNR -5dB：11.6% WER

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：ACM MM 2026接收论文。迭代跨模态交互的设计思路新颖，受到生物视觉听觉协同处理的启发。QualitySensor退化感知门控在噪声条件下的鲁棒性提升显著。LRS3上0.68% WER的clean性能处于领先水平。但缺乏更详细的实验数据（如多噪声类型、多信噪比下的详细结果），代码未开源影响可复现性。

---

## [4] Leveraging Beam Search Information for Confidence Estimation in E2E ASR

**arXiv ID**：2607.29299 | **方向**：语音大模型

**作者**：Yichen Jia, Hugo Van hamme

**机构**：KU Leuven (鲁汶大学, 比利时)

**发布日期**：2026-07-31 | **论文**：https://arxiv.org/abs/2607.29299 | **PDF**：https://arxiv.org/pdf/2607.29299.pdf | **代码**：https://github.com/windskylionheart1023/Score_Rank_Confidence_Estimation_Module | **Demo**：暂无

### 📌 简介
端到端ASR系统的置信度估计对可靠应用至关重要，但现有方法大多依赖ASR模型内部特征（隐藏状态、注意力权重等），与特定架构绑定。本文提出SR-CEM（Score-Rank Confidence Estimation Module），一个仅依赖beam search信息的轻量级置信度估计模块（0.6K参数），利用token分数和排名生成token级和word级置信度分数。在LibriSpeech test-clean上，token级最大校准误差（MCE）从softmax的20.04%降至4.50%，期望校准误差（ECE）从1.75%降至0.30%。SR-CEM架构无关，可应用于hybrid CTC/Attention、attention-only、CTC-only和RNN-T等多种架构。ICASSP 2026发表。

### 🔧 技术方案

**问题背景：** E2E ASR系统输出的softmax概率存在系统性偏差——模型通常过度自信。现有置信度估计方法（CEM）依赖ASR模型内部特征（隐藏状态、注意力权重、编码器输出），这些特征在不同架构间差异大，需要特定适配。此外，beam search中局部概率与全局累积分数之间存在不匹配，导致非rank-1 token系统性不自信。

**模型架构：** 轻量级MLP模块（1隐藏层64维+ReLU+Sigmoid输出）。Token级特征向量（8维）：token分数s(yt)、token排名r(yt)、前序累积分数S<t、后序累积分数S>t、top-4分数Topk(t)。Word级特征向量（5维）：词分数、最大token排名、前序/后序累积分数、token数量。训练使用BCE损失，batch size 128，Adam优化器，lr 0.001，权重衰减1e-4，早停patience。

**核心创新：** (1) 识别并分析了beam search中局部-全局不匹配导致的置信度系统性偏差——非rank-1 token由于局部概率低但被全局累积分数选中而系统性不自信；(2) 提出SR-CEM，仅依赖beam search中自然产生的分数和排名信息，无需任何ASR模型内部特征，实现架构无关性；(3) 仅0.6K参数（token级）/ 0.4K参数（word级），比基线小100-250倍，推理延迟<0.1ms。

**训练策略：** 使用Levenshtein对齐标注token/word正确性（插入和替换标记为错误），BCE损失训练。训练数据可来自任何ASR解码的输出。在hybrid CTC/Attention（12 Conformer encoder + 6 Transformer decoder，4.6% WER）上训练和评估，同时验证在attention-only、CTC-only和RNN-T架构上的泛化性。

### 📊 实验结果
**数据集**：LibriSpeech, Common Voice, Libri-Adapt, CGN (荷兰语), CHiME-6

**主要指标**：
- LibriSpeech test-clean token级：MCE 4.50%, ECE 0.30%（vs softmax 20.04%, 1.75%）
- LibriSpeech test-clean word级：MCE 8.17%, ECE 0.35%（vs softmax 17.91%, 1.67%）
- CTC-only token级：MCE 3.27%（vs softmax 15.65%）
- RNN-T token级：MCE 4.20%（vs softmax 21.45%）
- 域外（Common Voice）：MCE 19.59%（vs softmax 34.77%）
- 荷兰语（CGN）：MCE 4.41%（token）/ 6.26%（word）
- 噪声（Libri-Adapt）：MCE 5.99%（token）/ 5.58%（word）
- 对话语音（CHiME-6）：MCE 7.51%（token）/ 7.46%（word）

**是否开源**：https://github.com/windskylionheart1023/Score_Rank_Confidence_Estimation_Module

### ⭐ 评分：8/10
评分理由：ICASSP 2026发表。SR-CEM在降低最大校准误差（MCE）方面表现突出，这对可靠的下游应用至关重要。架构无关的设计增强了通用性，跨hybrid、CTC、RNN-T架构验证了鲁棒性。0.6K参数的极端轻量级设计具有实际部署价值。开源代码可复现。局限在于需要beam search解码（greedy decoding不适用），且域外泛化仍有提升空间。

---

## [5] Cloned Voices, Real Consequences: Evaluating Bias in Political Deepfake Detection for Electoral Integrity in Brazil

**arXiv ID**：2607.28770 | **方向**：语音大模型

**作者**：Lucas Rafael Stefanel Gris, Daniel Casanova, Frederico Santos De Oliveira, Alef Iury Ferreira, Beatriz Almeida Felício, Raul César Reis Mata, Anderson da Silva Soares

**机构**：Federal University of Goiás; Federal University of Technology – Paraná; Ermis, Brazil

**发布日期**：2026-07-30 | **论文**：https://arxiv.org/abs/2607.28770 | **PDF**：https://arxiv.org/pdf/2607.28770.pdf | **代码**：https://huggingface.co/datasets/freds0/ParlaSpoof-BR | **Demo**：https://ermisai.github.io/parlaspoof-br-demo

### 📌 简介
生成式AI使制作假音频更容易，在选举期间放大政治虚假信息。本文引入ParlaSpoof-BR，一个基于巴西众议院官方录音构建的葡萄牙语政治语音deepfake数据集，包含40名说话人（性别和地区平衡）、2,000个真实样本，通过5种TTS、5种语音转换和部分操控（音频infilling）扩展至134,400个文件（11,200真实/123,200伪造）。评估发现：AASIST和AASIST-L在ParlaSpoof-BR上EER达50.98%和53.70%（vs ASVspoof 2019的0.83%和0.99%），DF-Arena-1B也仅达32.30% EER。方法学因素（合成模型选择68.5pp差距，操控程度44.3pp）主导性能差异，远超人口统计差异（性别0.7pp，地区3.7pp）。

### 🔧 技术方案

**问题背景：** 政治虚假信息对民主进程构成持续威胁。音频deepfake可伪造政治人物言论，在事实核查前影响选民。巴西2022年选举已出现协调性虚假信息活动，2026年总统选举中零样本语音克隆技术已广泛可用。现有检测器在ASVspoof上接近完美，但在真实场景中性能下降一个数量级，且葡萄牙语资源稀缺。

**数据集构建：** ParlaSpoof-BR来自巴西众议院官方音频档案（2024.01-2026.07），40名说话人（20男20女，5个地理区域平衡），每人50个话语（共2,000真实样本）。攻击类型：(1) TTS——5种零样本系统（OmniVoice, XTTS-v2, Chatterbox, VoxCPM2, Qwen3-TTS），每系统2,000样本，共10,000个；(2) VC——5种系统（Seed-VC, kNN-VC, OpenVoice-v2, X-VC, EZ-VC），共10,000个；(3) 音频Infilling——OmniVoice掩码填充，4种条件（LLM语义攻击+25%/50%/75%连续填充），共8,000个。鲁棒性变体：语音增强（3系统×6,000）、有损压缩（MP3/OGG，38,400）、babble噪声（3个SNR，60,000）。总计134,400文件。

**检测系统：** AASIST（RawNet2+图注意力，ASVspoof 2019 LA训练）、AASIST-L（85K参数轻量版）、DF-Arena-1B（1B参数Transformer，多语种deepfake语料训练）。

**核心发现：** (1) 方法学因素主导性能差异——合成模型选择（68.5pp差距，Qwen3-TTS召回31.2% vs OpenVoice-v2 99.7%）、操控程度（44.3pp，25%修改召回29.2% vs 75%修改73.5%），远超性别（0.7pp）和地区（3.7pp）；(2) 部分操控比完全合成更难检测——25%修改召回仅29.2%，意味着仅替换几个政治关键词即可以~70%概率规避最佳检测器；(3) babble噪声SNR 10dB时22.2%已检测deepfake逃逸；(4) OGG压缩导致94.8%真实音频被误标为假；(5) 语音增强（Resemble Enhance）导致98.9%真实音频被误标为假。

**评估协议：** 核心评估集30,000文件（2,000真实+28,000未扰动造假），鲁棒性评估集104,400文件分开报告。EER、AUC、Macro-F1、准确率、精确率/召回率。

### 📊 实验结果
**数据集**：ParlaSpoof-BR（134,400文件：11,200真实，123,200伪造）

**主要指标**：
- 总体EER：AASIST 50.98%, AASIST-L 53.70%, DF-Arena-1B 32.30%
- TTS检测（DF-Arena-1B）：平均EER 39.3%，Qwen3-TTS最差（EER 58.0%, 召回31.2%）
- VC检测（DF-Arena-1B）：平均EER 26.8%，OpenVoice-v2最佳（EER 19.6%, 召回99.7%）
- 部分操控（DF-Arena-1B）：25%修改召回29.2%，50%召回45.2%，75%召回73.5%
- 噪声鲁棒性：SNR 10dB时22.2%已检测deepfake逃逸
- 性别偏差：0.7pp EER差距
- 地区偏差：3.7pp EER差距（Norte 30.0% vs Sul 33.7%）

**是否开源**：数据集开源（HuggingFace, CC BY license）

### ⭐ 评分：8/10
评分理由：首个葡萄牙语政治语音deepfake基准数据集，社会意义重大。数据集构建质量高（40说话人性别/地区平衡，5种TTS+5种VC+部分操控，鲁棒性变体覆盖全面）。核心发现——方法学偏见超过人口统计偏见——对公平性研究和检测器设计有重要启示。部分操控检测的薄弱性揭示了实际部署中的严重漏洞。但DF-Arena-1B的32.30% EER表明当前最佳检测器仍远未达到实用水平。

---

## 语音前端

---

## [6] Model-Agnostic Meta-Learning Initialization for Distributed Multichannel Active Noise Control

**arXiv ID**：2607.29117 | **方向**：语音前端

**作者**：Xiaoyi Shen, Junwei Ji, Woon-Seng Gan, Dongyuan Shi, Jun Yang

**机构**：中国科学院声学研究所; 南洋理工大学; 西北工业大学; 中国科学院大学

**发布日期**：2026-07-31 | **论文**：https://arxiv.org/abs/2607.29117 | **PDF**：https://arxiv.org/pdf/2607.29117.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
分布式多通道主动噪声控制（DMCANC）是大面积降噪的可扩展框架，但现有方法依赖零或随机初始化，导致自适应滤波器收敛缓慢，限制了节点间协作效率。本文提出基于模型无关元学习（MAML）的初始化策略，通过聚合不同节点和声学环境的异构声学特征（主通道和次通道脉冲响应），学习可泛化的初始控制滤波器系数。在6节点DMCANC系统上验证，使用宽带噪声（100-2000Hz多种范围）进行MAML训练。结果表明该方法在单频噪声、宽带噪声和真实压缩机噪声下均实现最快收敛，真实噪声场景下从控制开始即抑制噪声，而其他方法约10秒后才开始明显衰减。

### 🔧 技术方案

**问题背景：** DMCANC系统中多个节点独立运行本地单通道ANC控制器并通过间歇通信交换信息实现全局控制。现有DMCANC实现依赖零或随机初始化，在时变噪声和大规模系统中收敛缓慢。自适应滤波器初始化对ANC系统收敛行为至关重要，但DMCANC领域此前未系统研究。

**模型架构：** MAML初始化框架，每个DMCANC节点的不同声学配置作为一个任务。MAML训练阶段：使用宽带噪声（100-1200Hz, 800-1500Hz, 1200-2000Hz三种范围）训练最优初始系数。数据集70%训练/30%验证。元学习跨节点聚合异构声学特征（主通道和次通道脉冲响应）。学习到的初始化部署到所有节点作为初始控制滤波器。补偿滤波器补偿自次通道和互次通道之间的差异。间歇通信（IC）策略减少通信负担。

**核心创新：** (1) 首次将MAML应用于分布式ANC初始化，从异构声学环境中提取共享知识，学习可泛化的初始滤波器系数；(2) 通过间歇通信（IC）策略减少通信负担，同时保持性能接近集中式系统；(3) 补偿滤波器设计，补偿自次通道和互次通道之间的差异，确保混合梯度更新的一致性。

**训练策略：** 6节点DMCANC系统，次通道长度256 taps，补偿滤波器33 taps，控制滤波器512 taps。采样率16 kHz。MAML使用宽带噪声（100-1200Hz, 800-1500Hz, 1200-2000Hz）训练，70%训练/30%验证。在线部署时MAML初始化作为初始控制滤波器，自适应算法继续更新。

### 📊 实验结果
**数据集**：实测声学环境（消声室），6节点DMCANC系统

**主要指标**：
- 单频噪声（315Hz, 500Hz）：所有节点最快收敛，稳态衰减与其他方法相当
- 宽带噪声（200-800Hz）：最快收敛，稳态性能一致
- 真实压缩机噪声：从控制开始即抑制噪声，其他方法（IC-DMCANC, MGDFxLMS, 集中式）约10秒后开始明显衰减
- 步长设置：单频1e-8，宽带3e-7

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：MAML应用于ANC初始化的创新尝试，解决了分布式ANC中自适应滤波器收敛慢的实际问题。在多种噪声条件下收敛加速效果显著，尤其是真实压缩机噪声从一开始就产生降噪效果，工程价值明确。理论创新相对有限（MAML为成熟技术），但问题定义清晰、实验充分。6节点系统规模较小，更大规模系统下的泛化性有待验证。

---

*Generated on 2026-08-14*