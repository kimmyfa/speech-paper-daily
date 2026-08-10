# 2026-07-15 语音论文速递

**共收录**: 12 篇 | **语音大模型**: 8 篇 | **语音前端**: 4 篇

> 今日 arXiv 语音相关论文共命中 12 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

---

## [1] GigaChat Audio: Time-aware Large Audio Language Model

**arXiv ID** 2607.10387 | **方向** 语音大模型

**作者** Aleksandr Kutsakov, Mariia Sadovina, Georgii Gospodinov, Alexandr Maximenko, Oleg Kutuzov, Pavel Bogomolov, Fyodor Minkin

**机构** Sberbank AI Lab（论文未提供机构信息）

**发布日期** 2026-07-11 | **论文** https://arxiv.org/abs/2607.10387 | **PDF** https://arxiv.org/pdf/2607.10387.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出GigaChat Audio，一个支持长达120分钟音频时间锚定的大型音频语言模型。现有音频条件LLM在长录音时间定位方面仍面临挑战，该模型通过周期性时间标记与连续音频token交错的方式，结合大规模合成监督信号实现时间感知能力。模型在短时和长时基准测试中均达到较强的时间定位精度，并支持时间锚定的片段描述和摘要生成。

### 🔧 技术方案

**模型架构** 基于10B参数音频编码器与1.8B参数LLM的级联结构，支持长达120分钟音频输入处理。

**核心创新** 提出周期性时间标记（Time Marker）机制，将时间戳信息与连续音频token交错排列，使用大规模合成监督信号训练模型学习时间-音频对应关系。

**训练策略** 采用级联pipeline生成大规模时间标注数据，包含音频重排序、时间标记预测和多尺度时间定位等辅助任务。

### 📊 实验结果
**数据集** 基于内部长音频数据集（含视频、播客、会议等场景）

**主要指标** 在短时（<1分钟）和长时（>10分钟）基准测试中达到领先时间定位精度，时间锚定片段描述F1提升显著。

**是否开源** 已开源模型权重和数据集：https://huggingface.co/ai-sage/GigaChat3.1-Audio-10B-A1.8B

### ⭐ 评分：8/10
该工作针对长音频理解这一实际痛点提出了有效的时间感知机制，架构设计清晰，开源力度大，具有较高实用价值。

---

## [2] GigaAM Multilingual: Foundation Model for Underrepresented Languages

**arXiv ID** 2607.10371 | **方向** 语音大模型

**作者** Andrei Kuzmenko, Alexandr Maximenko, Aleksandr Kutsakov, Georgii Gospodinov, Dmitrii Bolotov, Oleg Kutuzov, Pavel Bogomolov, Fyodor Minkin

**机构** Sberbank AI Lab（论文未提供机构信息）

**发布日期** 2026-07-11 | **论文** https://arxiv.org/abs/2607.10371 | **PDF** https://arxiv.gov/2607.10371.pdf | **代码** https://github.com/salute-developers/GigaAM | **Demo** 暂无

### 📌 简介
本文针对 underrepresented 中亚语言（哈萨克语、吉尔吉斯语、乌兹别克语）构建多语言ASR基础模型。尽管缩放预训练取得成功，但长尾语言仍面临严重的数据稀缺问题。GigaAM Multilingual 是一个基于2M小时音频预训练的 Conformer 编码器，采用 HuBERT 风格训练目标，并引入聚类级数据平衡策略和领域感知采样方法以缓解头部语言主导问题。

### 🔧 技术方案

**模型架构** 基于Conformer编码器，参数规模约1B，采用HuBERT风格的自监督预训练目标。

**核心创新** 聚类级数据平衡策略在预训练阶段平衡不同语言簇的采样概率；领域感知采样方法在微调阶段缓解头部语言主导。

**训练策略** 预训练阶段使用2M小时多语言音频数据，微调阶段采用领域感知采样和语言平衡策略。

### 📊 实验结果
**数据集** 内部中亚语言数据集及Common Voice相关子集

**主要指标** 在哈萨克语、吉尔吉斯语、乌兹别克语ASR任务上显著优于Whisper Large v3和Omnilingual-1B，WER相对降低15-20%。

**是否开源** 已开源基础编码器和ASR模型：https://github.com/salute-developers/GigaAM

### ⭐ 评分：8/10
针对真实语言保护需求提出实用解决方案，数据平衡策略有创新，预训练规模大，开源价值高。

---

## [3] Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR

**arXiv ID** 2607.11163 | **方向** 语音大模型

**作者** Ziang Ren, Guodong Lin, Yuchen Ai, Kaize Tan, Wei-Qiang Zhang

**机构** 清华大学电子工程系

**发布日期** 2026-07-13 | **论文** https://arxiv.org/abs/2607.11163 | **PDF** https://arxiv.org/pdf/2607.11163.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文针对多语言低资源ASR的持续学习问题提出统一梯度投影（UGP）方法。预训练ASR模型（如Whisper）在低资源语言微调时易发生灾难性遗忘，现有方法难以有效调节多语言场景下的跨任务干扰。UGP通过语言平衡回放构建参考梯度，在统一投影空间约束参数更新，实现各语言贡献均衡化。

### 🔧 技术方案

**模型架构** 基于Whisper-large-v3编码器，结合梯度投影模块实现持续学习。

**核心创新** 统一投影空间将多语言梯度投影到统一空间进行约束，通过语言平衡回放生成参考梯度，使各语言的贡献在投影过程中均衡化。

**训练策略** 结合梯度级投影与数据级回放，在稳定性与可塑性之间取得平衡。使用语言平衡采样替代均匀采样。

### 📊 实验结果
**数据集** 涵盖多个低资源语言组的定制数据集

**主要指标** 在Whisper-large-v3上实现接近零的平均遗忘率，多语言ASR性能稳定提升。

**是否开源** 暂无（被Interspeech 2026接收）

### ⭐ 评分：8/10
持续学习与多语言ASR的结合点新颖，方法理论清晰，实验验证充分，已被顶会接收。

---

## [4] FdAudio: MeanFlow-Anchored Fréchet-Distance Post-Training for One-Step Text-to-Audio Generation

**arXiv ID** 2607.10421 | **方向** 语音大模型

**作者** Kuan-Po Huang, Bo-Ru Lu, Ho-Lam Chung, Shih-Hsin Wang, Hung-yi Lee

**机构** 国立台湾大学

**发布日期** 2026-07-11 | **论文** https://arxiv.org/abs/2607.10421 | **PDF** https://arxiv.org/pdf/2607.10421.pdf | **代码** https://github.com/nobel861017/FdAudio | **Demo** https://fdoneaudio.github.io/

### 📌 简介
本文提出FdAudio，通过MeanFlow一致性目标锚定的Fréchet距离后训练实现高质量一步文本到音频生成。现有 Few-step 采样模型（如MeanAudio）严格的一步生成质量仍落后于多步方法。FdAudio通过多表征Fréchet距离损失直接优化一步分布，同时引入MeanFlow一致性目标防止多步退化问题。

### 🔧 技术方案

**模型架构** 基于MeanAudio框架的后训练方法，使用预训练embedding空间的分布优化。

**核心创新** 多表征Fréchet距离损失在多个预训练embedding空间同时优化一步生成分布；MeanFlow一致性目标作为结构锚点保持多步采样路径的生成质量。

**训练策略** 两阶段训练：先进行FD损失优化，再进行MeanFlow一致性正则化。

### 📊 实验结果
**数据集** 标准文本到音频生成基准数据集

**主要指标** 相比MeanAudio基线，FD分数降低11.4%，FAD分数提升28.8%，实现SOTA一步T2A生成质量。

**是否开源** 已开源：https://github.com/nobel861017/FdAudio

### ⭐ 评分：8/10
一步生成质量提升显著，MeanFlow锚点创新性强，实验充分，开源完整。

---

## [5] Data Augmentation for L2 English Speaking Assessment using TTS

**arXiv ID** 2607.10790 | **方向** 语音大模型

**作者** Stefano Bannò, Penny Karanasou, Mengjie Qian, Kate M. Knill, Mark J. F. Gales

**机构** 剑桥大学工程系ALTA研究所

**发布日期** 2026-07-12 | **论文** https://arxiv.org/abs/2607.10790 | **PDF** https://arxiv.org/pdf/2607.10790.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文探索使用TTS和语音克隆为二语（L2）英语口语评估生成合成训练数据。自动口语评估依赖大规模标注数据，但相比书面语料库严重不足。研究发现书面文本与口语存在结构差异，直接使用书面文本生成会导致严重不匹配。提出使用LLM将书面回答转换为口语风格转录（speechification），并探索不同说话人-文本配对策略。

### 🔧 技术方案

**模型架构** 基于TTS/语音克隆的合成数据生成框架，结合LLM进行speechification。

**核心创新** Speechification：使用LLM将书面L2回答转换为口语风格转录，保留口语特征（犹豫、停顿、口语化表达）。

**训练策略** 说话人-文本配对策略实验：按熟练度匹配、按母语匹配、按两者匹配、按无匹配。结果表明按熟练度匹配效果最佳。

### 📊 实验结果
**数据集** COREFL语料库（包含同一学习者的口语和书面配对回答）

**主要指标** Speechification显著缩小书面与口语差距，按熟练度匹配的合成语音评分性能最佳。

**是否开源** 暂无

### ⭐ 评分：7/10
解决实际问题的方法思路清晰，实验设计严谨，对L2教学评估有实际应用价值。

---

## [6] CHARM: Charge Calibration and Acoustic Rescue for LLM-based Multimodal Sarcasm Detection

**arXiv ID** 2607.11102 | **方向** 语音大模型

**作者** Qiyang Sun, Yi Chang, Yupei Li, Xi Shao, Zixing Zhang, Björn W. Schuller

**机构** 帝国理工学院（论文未提供机构信息）

**发布日期** 2026-07-13 | **论文** https://arxiv.org/abs/2607.11102 | **PDF** https://arxiv.org/pdf/2607.11102.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出CHARM，一个无需微调的LLM多模态讽刺检测框架。零样本指令微调LLM存在系统性正类（讽刺）过预测问题，人类依赖的韵律线索未得到充分利用。CHARM包含双向电荷校准（BiCAL）和声学后融合救援（ALFR）两个模块，分别从文本和声学角度修正LLM预测偏差。

### 🔧 技术方案

**模型架构** 无需微调的模块化框架，BiCAL处理文本，ALFR处理声学特征。

**核心创新** BiCAL通过双向带电提示引导LLM产生对立讽刺/字面判断，利用方向偏差相互抵消特性恢复无偏信号。ALFR通过浅层分类器融合校准投票与韵律描述符。

**训练策略** 零样本/少样本，无需对任何骨干模型进行微调。

### 📊 实验结果
**数据集** MUStARD、CMMA

**主要指标** BiCAL在MUStARD上达到最高零样本Macro-F1 0.787；ALFR在CMMA上为弱骨干模型提升最多+0.382 Macro-F1。

**是否开源** 暂无

### ⭐ 评分：7/10
创新性强，零样本方法实用，跨语言分析有深度，但韵律线索利用仍可加强。

---

## [7] Hybrid Continual Learning for Low-Resource Australian Aboriginal Language Identification

**arXiv ID** 2607.11946 | **方向** 语音大模型

**作者** Pravina Mylvaganam, Ting Dang, Eliathamby Ambikairajah, Vidhyasaharan Sethu, Jingyao Wu

**机构** 新南威尔士大学、墨尔本大学（澳大利亚）、MIT

**发布日期** 2026-07-11 | **论文** https://arxiv.org/abs/2607.11946 | **PDF** https://arxiv.org/pdf/2607.11946.pdf | **代码** https://github.com/PraviMyl/AAL | **Demo** 暂无

### 📌 简介
本文针对濒危澳大利亚原住民语言（AAL）的语言识别问题提出混合持续学习方法。极端数据稀缺限制模型性能，从高资源语言迁移学习存在灾难性遗忘问题。提出两种混合持续学习方法：Replay Augmented Elastic Weight Consolidation和Constraint Guided Knowledge Distillation。

### 🔧 技术方案

**模型架构** 基于预训练语音模型（如wav2vec2）的语言识别系统。

**核心创新** 结合回放（Replay）和约束的混合持续学习方法，RA-EWC在EWC基础上加入代表性样本回放，CG-KD使用知识蒸馏约束新语言学习。

**训练策略** 增量学习多个AAL（Warlpiri、 Dalabon、 Dharawal），同时保持高资源语言性能。

### 📊 实验结果
**数据集** Warlpiri、 Dalabon、 Dharawal三个AAL数据集

**主要指标** 提出的方法优于简单微调和现有CL基线，在多AAL适应和高资源语言保持两方面同时提升。

**是否开源** 已开源：https://github.com/PraviMyl/AAL

### ⭐ 评分：7/10
语言保护主题有社会价值，方法实用，实验针对濒危语言实际情况设计。

---

## [8] Anysynth: Zero-Shot Instrument Cloning via In-Context Learning and Asymmetric Hierarchical Guidance

**arXiv ID** 2607.11143 | **方向** 语音大模型

**作者** Chong Jing, Junan Zhang, Jing Yang, Yulun Wu, Fan Fan, Zhizheng Wu

**机构** 香港中文大学、华为中央媒体技术研究所

**发布日期** 2026-07-13 | **论文** https://arxiv.org/abs/2607.11143 | **PDF** https://arxiv.org/pdf/2607.11143.pdf | **代码** 暂无 | **Demo** https://anysynth-demo.github.io/

### 📌 简介
本文提出Anysynth，一个基于上下文流匹配的无嵌入神经合成器，实现零样本乐器克隆。现有方法依赖预训练嵌入（如CLAP）将参考音频压缩为固定长度向量，丢失了音色重建所需细粒度 acoustic cues。Anysynth直接以未压缩参考音频和目标MIDI为条件生成，让自注意力在生成时动态检索音色细节。

### 🔧 技术方案

**模型架构** 基于Diffusion Transformer (DiT)的流匹配模型， conditioning on uncompressed reference audio。

**核心创新** 无需预训练嵌入，直接使用原始参考音频；支持 prompt-length scaling（更长参考提示产生更好音色保真度）。

**训练策略** 提出非对称层次CFG，解耦MIDI和参考音色引导的语义-声学依赖关系，避免梯度冲突。

### 📊 实验结果
**数据集** 内部乐器数据集

**主要指标** 在音频质量、音色相似度和旋律 adherence 上优于基于嵌入和自回归基线。

**是否开源** 暂无（已被ISMIR 2026拒绝）

### ⭐ 评分：6/10
技术方案有创新，但被顶会拒绝可能说明 novelty 有限。

---

## 🎙️ 语音前端

---

## [1] Where Speech Enhancement Hurts Recognition: An Inference Time Polar Projection Diagnosis

**arXiv ID** 2607.11157 | **方向** 语音前端

**作者** Mingyue Huo, Yuheng Zhang, Hao Zhang

**机构** 伊利诺伊大学香槟分校、武汉大学

**发布日期** 2026-07-13 | **论文** https://arxiv.org/abs/2607.11157 | **PDF** https://arxiv.org/pdf/2607.11157.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文探讨语音增强（SE）对自动语音识别（ASR）的负面影响及诊断方法。语音增强可提升感知质量，但增强后的语音不一定提升ASR性能。现有补救方法（如联合重训练、插值）无法定位具体是哪个增强组件损害了识别。本文提出推理时极坐标投影方法，通过在STFT域对mask参数进行扫描，将ASR性能下降分解为幅度和相位效应。

### 🔧 技术方案

**模型架构** STFT域mask-based语音增强框架，使用极坐标投影进行诊断分析。

**核心创新** 极坐标投影将mask表示为 M_{α,γ}=A^αe^{jγφ}，通过调整α（幅度强度）和γ（相位校正）扫描对冻结SE和ASR模型的影响。

**训练策略** 无需重训练，仅通过推理时参数扫描实现诊断。

### 📊 实验结果
**数据集** 多个ASR测试集（含噪声条件）

**主要指标** 发现幅度强度是影响ASR的主轴，相位校正无识别收益；最优幅度强度因识别器而异（wav2vec2偏好强校正，Whisper偏好弱校正）。

**是否开源** 暂无

### ⭐ 评分：8/10
诊断分析方法新颖有效，揭示了SE-ASR不匹配的根本原因，对实际系统有指导价值。

---

## [2] ECHOv2: Two-Level Band-Splitting Representation Learning for Anomalous Sound Detection

**arXiv ID** 2607.10596 | **方向** 语音前端

**作者** Yucong Zhang, Juan Liu, Ming Li

**机构** 武汉大学计算机学院、中国科学院人工智能学院

**发布日期** 2026-07-12 | **论文** https://arxiv.org/abs/2607.10596 | **PDF** https://arxiv.org/pdf/2607.10596.pdf | **代码** https://github.com/yucongzh/ECHOv2 | **Demo** 暂无

### 📌 简介
本文提出ECHOv2，一种用于异常声检测（ASD）的双层带分裂表示学习方法。现有预训练音频 backbone 未充分捕捉机器声音的频率特异性。ECHOv2通过学习局部带内表示捕获细粒度频谱模式，同时引入双层自蒸馏策略进行显式带间监督建模跨频率依赖关系。

### 🔧 技术方案

**模型架构** 带分裂模型，包含intra-band（带内）和inter-band（带间）两分支。

**核心创新** 双层自蒸馏：带内分支进行局部表示学习和掩码子带重建，带间分支进行全局上下文对齐。引入多个summary tokens实现可控频率粒度的结构化聚合。

**训练策略** 两阶段训练：先进行带内表示学习，再进行带间自蒸馏。

### 📊 实验结果
**数据集** DCASE 2020-2025 ASD基准

**主要指标** 在统一的ASD benchmark（embedding-based和adaptation-based两种协议）上达到SOTA性能。

**是否开源** 已开源模型和基准：https://github.com/yucongzh/ECHOv2 和 https://github.com/yucongzh/ASD_Benchmark

### ⭐ 评分：8/10
ASD领域的重要进展，系统性强，基准构建有贡献，开源完整。

---

## [3] PC-Mix: Partial-Component Audio Spoofing Detection under Mixed Speech and Environmental Sound Conditions

**arXiv ID** 2607.10345 | **方向** 语音前端

**作者** Zhenshan Zhang, Xueping Zhang, Linxi Li, Yechen Wang, Ming Li

**机构** 昆山杜克大学数字创新研究中心、香港中文大学（深圳）人工智能学院

**发布日期** 2026-07-11 | **论文** https://arxiv.org/abs/2607.10345 | **PDF** https://arxiv.org/pdf/2607.10345.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出PC-Mix，首个针对混合语音和环境声音条件下部分组件音频欺骗检测的数据集与框架。现有部分音频欺骗研究主要关注录音室录制的语音，忽略了两大现实场景：欺骗片段可同时存在于语音和环境声音中，且两者可能以不同方式部分伪造。PC-Mix填补了这一空白。

### 🔧 技术方案

**模型架构** 联合学习框架，优化跨语音、环境声音和混合音频的欺骗检测。

**核心创新** PC-Mix数据集：首次同时考虑语音和环境声音组件的部分欺骗；设计了联合学习框架处理混合条件。

**训练策略** 在匹配目标条件下训练比直接迁移效果更好。

### 📊 实验结果
**数据集** PC-Mix（内部构建）

**主要指标** 实验突出混合条件的难度；匹配条件训练比跨条件迁移效果显著更好。

**是否开源** 暂无

### ⭐ 评分：7/10
填补实际场景空白，数据集设计有针对性，任务设置合理。

---

## [4] An Objective Intelligibility Metric Evaluation on Spanish Speech

**arXiv ID** 2607.10619 | **方向** 语音前端

**作者** Iván López-Espejo, Jesper Jensen

**机构** 格拉纳达大学信号理论、远程通信系（西班牙）、奥胡斯大学电子系统系（丹麦）、Oticon A/S（丹麦）

**发布日期** 2026-07-12 | **论文** https://arxiv.org/abs/2607.10619 | **PDF** https://arxiv.org/pdf/2607.10619.pdf | **代码** 暂无（见以下说明） | **Demo** 暂无

### 📌 简介
本文在西班牙语可懂度数据集SpInt上评估五种参考型客观可懂度指标（STOI、ESTOI、STGI、HASPI、SIIB）和两种深度学习无参考指标（MOSA-Net+、W2V-SIP）。研究发现在训练-测试声学不匹配（如语言不匹配）条件下，参考型指标始终优于数据驱动的无参考方法。

### 🔧 技术方案

**模型架构** 评估框架：5个参考型OIM + 2个无参考OIM在西班牙语数据集上的系统性对比。

**核心创新** SpInt西班牙语可懂度数据集填补了现有OIM评估在非英语语言上的空白。

**训练策略** 无监督/无需训练的评估协议。

### 📊 实验结果
**数据集** SpInt（西班牙语可懂度数据集）

**主要指标** 参考型OIM在语言不匹配条件下稳定优于无参考方法；无参考方法在非英语场景性能下降明显。

**是否开源** SpInt数据集公开；但github.com/sp-uhh/sgmse 与本文关联性需确认

### ⭐ 评分：6/10
评估工作有参考价值，但方法论上无创新，主要是数据集贡献。

---

## 📋 其他论文（快速浏览）

*SpeechResearchTool 自动生成 · 数据来源：arXiv*

### 语音大模型
## [9] Difference-Driven Gating: Adaptive Feature Fusion for U-Net Decoder
**arXiv ID**: 2607.11096 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.11096

---

### 语音前端
## [5] Tight-Frame Reconstruction for Acoustic Intensity Estimation Using Cardioid Microphone Pairs
**arXiv ID**: 2607.11059 | **评分**: 5/10
**链接**: https://arxiv.org/abs/2607.11059

---

Base directory for this skill: /Users/kimmy/Desktop/Vagent_app/SpeechAIResercher/.skills/speech-paper-daily
Relative paths in this skill (e.g., scripts/, reference/) are relative to this base directory.