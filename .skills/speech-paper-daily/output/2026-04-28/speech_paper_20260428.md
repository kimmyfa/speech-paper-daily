# 2026-04-28 语音论文速递

**共收录**: 6 篇 | **语音大模型**: 3 篇 | **语音前端**: 3 篇

> 今日 arXiv 语音相关论文共命中 6 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

## [1] UniSonate: A Unified Model for Speech, Music, and Sound Effect Generation with Text Instructions

**arXiv ID** 2604.22209 | **方向** 语音大模型 / TTS

**作者** Chunyu Qiang, Xiaopeng Wang, Kang Yin, Yuzhe Liang, Yuxin Guo, Teng Ma, Ziyu Zhang, Tianrui Wang, Cheng Gong, Yushen Chen, Ruibo Fu, Chen Zhang, Longbiao Wang, Jianwu Dang 等

**机构** Tianjin University, Kuaishou Technology, Institute of Automation CAS

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22209 | **PDF** https://arxiv.org/pdf/2604.22209.pdf | **代码** https://github.com/qiangchunyu/UniSonate | **Demo** https://qiangchunyu.github.io/UniSonate/

### 📌 简介
UniSonate是首个统一语音、音乐和音效生成的flow-matching框架,通过标准化自然语言指令接口生成多种音频类型。提出动态token注入机制,将非结构化音效投影到结构化时序潜在空间,在音素驱动的多模态扩散Transformer中实现精确时长控制。结合多阶段课程学习策略有效缓解跨模态优化冲突。

### 🔧 技术方案

**模型架构** 基于条件flow matching的统一生成框架,双流MM-DiT架构:Instruction流控制高层属性,Content流控制时序结构。使用统一的reference-free自然语言指令接口,无需参考音频即可进行细粒度声学属性控制。

**核心创新**
动态token注入机制将非结构化环境声音符号化为可学习[SFX] token,使transformer能用相同的离散符号推理处理非语言音频,实现音效的时长和进度推断。首次在统一框架中观察到正迁移现象:联合训练多样化音频数据显著增强语音的结构一致性和韵律表现力。提出Instruction-Content Alignment范式,将自然语言指令的语义空间与多样化音频模态的声学流形对齐。

**训练策略** 多阶段课程学习:第一阶段仅训练结构化语音,第二阶段扩展到半结构化音乐,第三阶段加入非结构化音效,逐步缓解优化冲突和灾难性遗忘。使用flow matching训练目标,在音素对齐的MM-DiT中嵌入[SFX] token实现音效的符号化表示。

### 📊 实验结果
**数据集** SeedTTS-test(指令式TTS)、SongEval(TTM)、AudioCaps和Clotho(TTA)等

**主要指标** 指令式TTS达到WER 1.47%,在SeedTTS-WER和Control指标上取得SOTA;TTM在SongEval Coherence达到3.18,显著优于专门模型;TTA在FAD和Fréchet Distance上保持竞争力。消融实验验证动态token注入和多阶段课程学习的必要性。

**是否开源** 是,代码和模型权重已开源

### ⭐ 评分: 9/10
ACL 2026主会议oral论文,首次统一TTS/TTM/TTA三大任务,创新性的动态token注入机制突破结构与非结构声学表示的根本冲突,正迁移现象揭示了跨模态学习的深层规律。实验充分,在多个数据集和指标上取得SOTA,开源完整,具有重要理论意义和实用价值。

---

## [2] Listening with Time: Precise Temporal Awareness for Long-Form Audio Understanding

**arXiv ID** 2604.22245 | **方向** 音频语言模型 / 长音频理解

**作者** Mingchen Shao, Hang Su, Wenjie Tian, Bingshen Mu, Zhennan Lin, Lichun Fan, Zhenbo Luo, Jian Luan, Lei Xie

**机构** Northwestern Polytechnical University, Independent Researchers

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22245 | **PDF** https://arxiv.org/pdf/2604.22245.pdf | **代码** https://github.com/alanshaoTT/LAT-Audio-Repo | **Demo** 暂无

### 📌 简介
大音频语言模型(LALM)在短音频上表现优异,但在长音频输入上性能下降,特别是在时间感知任务中,时间对齐准确性随着音频时长增加而降低。为此构建LAT-Chronicle(1.2k小时长音频数据集)和LAT-Bench(首个支持30分钟音频的人类验证基准),涵盖密集音频描述、时间音频定位和目标音频描述三大核心任务。

### 🔧 技术方案

**模型架构** LAT-Audio模型,将时间感知表述为渐进式全局到局部推理范式。首先构建全局时间线作为对齐的时间-语义上下文,然后引入Think-With-Audio Chain-of-Thought(TWA-CoT)通过工具使用融合局部音频信息进行迭代推理。支持按需采样机制,灵活选择音频片段进行细粒度分析。

**核心创新**
渐进式全局到局部推理范式:先建立全局时间线概览,再通过TWA-CoT逐步深入局部细节,兼顾全局一致性和局部精度。首次构建长音频时间感知完整生态系统:包含数据集LAT-Chronicle(1.2k小时,真实场景)、基准LAT-Bench(30分钟音频,三大任务)、模型LAT-Audio。提出On-Demand Sampling机制,模型根据需要动态选择音频片段,无需滑动窗口暴力枚举。

**训练策略** 三阶段训练:第一阶段全局时间线生成监督微调,学习全局结构;第二阶段完整轨迹SFT,学习局部细节;第三阶段强化学习,优化时间对齐和推理质量。奖励函数设计考虑时间对齐精度、内容相关性和推理连贯性。

### 📊 实验结果
**数据集** LAT-Chronicle(自建,1.2k小时),LAT-Bench(自建,30分钟音频),AudioSet,SoundNet等

**主要指标** 在长音频时间感知任务上超越现有模型,包括密集音频描述(BLEU/ROUGE提升)、时间音频定位(mAP提升)、目标音频描述(CIDEr提升)。消融实验验证全局时间线和TWA-CoT的有效性。输入时长鲁棒性分析显示LAT-Audio在不同时长下保持稳定性能。

**是否开源** 是,数据集、基准和模型全部开源

### ⭐ 评分: 8/10
首次系统性地解决长音频时间感知问题,构建了完整的数据集-基准-模型生态系统。渐进式全局到局部推理范式兼具理论创新性和实用价值,TWA-CoT和On-Demand Sampling机制设计精巧。实验充分,涵盖多个基准和消融实验,开源完整,对推动长音频理解领域发展具有重要意义。

---

## [3] Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis

**arXiv ID** 2604.22133 | **方向** 语音前端 / 发音错误检测

**作者** Haopeng Geng, Longfei Yang, Xi Chen, Haitong Sun, Daisuke Saito, Nobuaki Minematsu

**机构** Graduate School of Engineering, The University of Tokyo, Japan

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22133 | **PDF** https://arxiv.org/pdf/2604.22133.pdf | **代码** https://github.com/Secondtonumb/IF-MDD | **Demo** 暂无

### 📌 简介
发音错误检测和诊断(MDD)需要建模细粒度声学偏差,但当前ASR衍生的MDD系统面临固有局限:CTC模型偏好序列级对齐,忽略瞬态发音错误线索;明确正则文本先验偏向预期目标。提出无提示框架CROTTC-IF解耦声学保真度和正则引导,首先引入CROTTC声学模型强制单调帧级对齐准确捕获发音偏差,其次通过IF策略基于知识转移原理隐式注入发音错误信息。

### 🔧 技术方案

**模型架构** CROTTC-IF框架,包含CROTTC声学模型和IF-MDD语言模型。CROTTC(Consistency-Regularized Optimal Temporal Transport Classification)是强制单调帧级对齐的声学模型,避免CTC的稀疏性和延迟发射问题,保留细粒度瞬态发音错误线索。IF(Indirect Fusion)策略基于特权信息学习(LUPI),将正则文本和发音错误模式作为训练时的特权数据,在推理时提供软语言引导。

**核心创新**
CROTTC使用最优传输实现帧级对齐,避免CTC的序列级全局优化擦除细粒度声学证据,通过一致性正则化确保对齐的单调性和准确性。IF策略隐式融合语言先验而非显式注入,防止推理时覆盖真实声学证据,通过知识转移将特权信息软编码到语言模型中。系统性分析正则文本先验对MDD的影响,发现过度依赖正则先验会降低检测敏感性,证明解耦声学显式先验的必要性。

**训练策略** CROTTC使用最优传输损失和一致性正则化,强制帧级对齐。IF策略在训练时使用教师网络提供发音错误检测标签作为特权信息,通过蒸馏传递给语言模型。使用L2-ARCTIC、ERJ、speechocean762等数据集训练,支持从L2英语到阿拉伯语古兰经诵读(Iqra'Eval2)的广泛泛化。

### 📊 实验结果
**数据集** L2-ARCTIC(L2英语),Iqra'Eval2(阿拉伯语古兰经诵读),ERJ,SO762等

**主要指标** CROTTC-IF在L2-ARCTIC上达到71.77% F1-score,在Iqra'Eval2排行榜上达到71.70% F1-score。消融实验验证CROTTC相对于CTC的优势,以及IF策略相比显式正则先验的有效性。跨数据集泛化研究展示在ERJ和SO762上的强泛化能力。

**是否开源** 是,代码已开源

### ⭐ 评分: 8/10
MDD任务的新范式,打破ASR的声学陷阱和语言学陷阱。CROTTC创新性地使用最优传输替代CTC,保留细粒度声学信息;IF策略通过知识转移隐式融合语言先验,避免显式偏差。实验充分,在多个数据集上达到SOTA,跨领域泛化能力强(从L2英语到阿拉伯语)。代码开源,实用价值高,对CAPT等应用场景有重要推动作用。

---

## [4] DM-ASR: Diarization-aware Multi-speaker ASR with Large Language Models

**arXiv ID** 2604.22467 | **方向** 语音大模型 / 多说话人ASR

**作者** Li Li, Ming Cheng, Weixin Zhu, Yannan Wang, Juan Liu, Ming Li

**机构** Wuhan University, Tencent Ethereal Audio Lab, The Chinese University of Hong Kong

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22467 | **PDF** https://arxiv.org/pdf/2604.22467.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
多说话人自动语音识别(ASR)旨在转录涉及多个发言者的对话语音,不仅需要识别说了什么,还需要识别谁说的以及何时说的。近期Speech-LLM方法展示了统一建模的潜力,但联合学习说话人归属、时间结构和词汇识别仍然困难且数据密集。提出DM-ASR框架,将任务重新表述为多轮对话生成过程,利用可靠的说话人分离作为显式结构先验有效简化任务。

### 🔧 技术方案

**模型架构** DM-ASR(Diarization-aware Multi-speaker ASR)框架,基于大语言模型的多说话人ASR系统。给定音频块和专用分离系统的分离结果,DM-ASR将转录分解为一系列说话人和时间条件查询,每个对应一个说话人在一个时间片段。这种表述将多说话人识别转换为一系列结构化子任务,显式解耦说话人-时间结构(谁和何时)与语言内容(什么)。

**核心创新**
将多说话人ASR重新表述为多轮对话生成过程,每轮对应一个说话人在一个时间片段的转录,使LLM能够利用其强大的语言建模和推理能力。设计专用token和分离感知提示机制,将分离结果(说话人身份、时间片段)结构化编码为提示,引导LLM生成说话人归属转录。可选的词级时间戳预测机制,交错词和时间戳token,产生更丰富的结构化输出和更好的转录质量。

**训练策略** 使用多说话人转录数据训练,包括说话人分离标签和时间信息。训练时提供分离结果作为输入,模型学习生成说话人归属转录。支持在仅音频、仅分离、完整信息等多种设置下训练和推理,逐步学习从分离中受益并校正不完美的分离结果。

### 📊 实验结果
**数据集** Mandarin多说话人ASR(Meeting,Conversation等),English多说话人ASR(LibriSpeech-2Mix,AMI等)

**主要指标** 在中英文多说话人ASR基准上取得强性能,相对较小的模型和训练数据即可达到或超过现有统一方法。消融实验验证专用token、分离感知提示和词级时间戳预测的有效性。不同评估设置分析显示模型能有效利用可靠分离线索,并随着模型规模和训练数据增加逐渐学习校正不完美分离。

**是否开源** 否

### ⭐ 评分: 7/10
实用的多说话人ASR框架,巧妙地将说话人分离作为显式先验与LLM的语言建模能力结合,避免端到端模型的高数据需求。多轮对话生成表述新颖,专用token设计合理。实验充分,在中英文基准上表现良好。实用价值高,适用于会议转录、对话分析等场景。不足之处是未开源代码,限制了可复现性和进一步研究。

---

## [5] TTS-PRISM: A Perceptual Reasoning and Interpretable Speech Model for Fine-Grained Diagnosis

**arXiv ID** 2604.22225 | **方向** 语音大模型 / TTS评估

**作者** Xi Wang, Jie Wang, Xingchen Song, Baijun Song, Jingran Xie, Jiahe Shao, Zijian Lin, Di Wu, Meng Meng, Jian Luan, Zhiyong Wu

**机构** Tsinghua University, MiLM Plus (Xiaomi Inc.), The University of Tokyo

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22225 | **PDF** https://arxiv.org/pdf/2604.22225.pdf | **代码** https://github.com/xiaomi-research/tts-prism | **Demo** 暂无

### 📌 简介
生成式TTS模型已达到人类级别质量,但整体指标无法诊断细粒度声学伪影或解释感知崩溃。提出TTS-PRISM,面向中文的多维度诊断框架。首先建立12维度模式,涵盖稳定性到高级表现力;其次设计有针对性的合成管道,包含对抗性扰动和专家锚点构建高质量诊断数据集;第三,模式驱动指令微调将显式评分标准和推理嵌入高效端到端模型。

### 🔧 技术方案

**模型架构** TTS-PRISM诊断框架,包含12维度层次分类模式、针对性数据合成管道和诊断评分模型。模式分为基础能力层(8个子维度,分数1-5)和高级表现力层(4个子维度,分数0-2)。使用基于现有LLM的高效端到端模型,通过模式驱动指令微调将显式评分标准和推理嵌入模型,实现单次推理的多维度诊断。

**核心创新**
首个面向中文的细粒度多维度诊断基准,建立12维度显式量化标准,填补中文语音评估细粒度量化标准的空白。针对性数据合成管道,结合对抗性扰动和专家锚点,在长尾样本上强化判别能力,包含真实人类录音和多范式TTS合成的均衡正负样本分布。模式驱动指令微调策略,基于全面的评分标准,使模型能够在全局视角和精细声学缺陷敏锐检测之间取得平衡。

**训练策略** 使用200k样本的指令调优数据集,通过Gemini-2.5-Pro进行12个独立维度的标注,减轻长上下文指令漂移和幻觉。构建11k专家标注的"Pronunciation Gold Subset"注入语言知识,解决中文声调和多音字问题。在1600样本中文Gold Test Set上评估,与人类对齐。

### 📊 实验结果
**数据集** 自建200k样本诊断数据集,1600样本中文Gold Test Set,多范式TTS系统合成的语音

**主要指标** 在1600样本Gold Test Set上,TTS-PRISM在人类对齐方面优于通用模型。对六个TTS范式的诊断分析建立了直观的诊断标志,揭示细粒度能力差异。消融实验验证针对性数据合成和模式驱动指令微调的有效性。

**是否开源** 是,代码和模型权重已开源

### ⭐ 评分: 7/10
首个面向中文的细粒度TTS诊断框架,建立12维度显式量化标准,填补中文语音评估的空白。针对性数据合成管道设计巧妙,对抗性扰动和专家锚点强化判别能力。模式驱动指令微调策略实用,在保持效率的同时提升可解释性。实验充分,开源完整,对TTS系统开发和评估有重要实用价值。创新性相对中等,主要是评估方法的系统化。

---

## [6] Advancing Automatic Speech Recognition using Feature Fusion with Self-Supervised Learning Features: A case study on Fearless Steps Apollo Corpus

**arXiv ID** 2604.22203 | **方向** 语音前端 / ASR

**作者** Szu-Jui Chen, John H.L. Hansen

**机构** Center for Robust Speech Systems, University of Texas at Dallas

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22203 | **PDF** https://arxiv.org/pdf/2604.22203.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
自监督学习(SSL)模型显著提升了下游语音任务性能,超越了传统手工特征。本研究探索SSL模型的融合,旨在利用各自优势并细化提取的特征以改进自然主义场景的语音识别模型。研究大规模自然主义Fearless Steps (FS) APOLLO资源,重点关注FS Challenge (FSC) Phase-4语料库,首次对该数据集进行分析。同时纳入CHiME-6数据集以评估不同自然主义语音场景的性能。

### 🔧 技术方案

**模型架构** 深度交叉注意力(DCA)融合方法,基于SSL模型特征融合。探索先前提出的Feature Refinement Loss和融合方法,发现这些方法在FSC Phase-4语料库上效果较差。提出新颖的DCA融合方法,专门为提升FSC Phase-4语料库性能而设计。结合多种SSL模型(基于SUPERB基准的先进SSL模型)和传统谱特征,通过DCA进行特征融合。

**核心创新**
深度交叉注意力(DCA)融合方法,专门设计用于提升FSC Phase-4语料库性能,有效融合不同SSL模型的特征。首次对FSC Phase-4语料库进行高级ASR结果分析和逐通道分析,作为150,000小时FS APOLLO社区资源的一部分。详细的音素级错误分析、功能词与内容词分析、层选择实验,深入理解融合系统的核心优势和性能提升的本质。

**训练策略** 在FSC Phase-4和CHiME-6数据集上训练,使用多种SSL模型(HuBERT、Wav2Vec 2.0、WavLM等)提取特征。探索不同SSL模型的层选择策略,确定最优特征提取层。使用Feature Refinement Loss的替代参数设置和可视化工具分析损失函数效果。

### 📊 实验结果
**数据集** Fearless Steps Challenge Phase-4 corpus,FSC Phase-2 corpus,CHiME-6

**主要指标** DCA融合方法相对于基线实现WER绝对提升1.1%,为大规模FS APOLLO社区资源提供有效的元数据创建。在CHiME-6上也取得 competitive性能。音素级错误分析、功能词与内容词分析、层选择实验揭示融合系统的优势和性能提升的本质。

**是否开源** 否

### ⭐ 评分: 6/10
增量改进工作,探索SSL特征融合在自然主义语音识别中的应用。DCA融合方法在FSC Phase-4上取得1.1% WER提升,虽实用但创新性有限。首次对FSC Phase-4语料库的详细分析有价值,但整体贡献主要是工程优化而非理论突破。未开源代码,限制可复现性。适合对大规模自然主义语音识别和SSL特征融合感兴趣的研究者。

---

## 📋 其他论文（快速浏览）

本日语音论文全部6篇已展示完整内容。