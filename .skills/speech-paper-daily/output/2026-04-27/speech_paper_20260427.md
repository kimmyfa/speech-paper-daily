# 2026-04-27 语音论文速递

**共收录**: 7 篇 | **语音大模型**: 4 篇 | **语音前端**: 3 篇

> 今日 arXiv 语音相关论文共命中 7 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

## [1] UniSonate: A Unified Model for Speech, Music, and Sound Effect Generation with Text Instructions

**arXiv ID** 2604.22209 | **方向** 语音大模型

**作者** Chunyu Qiang, Xiaopeng Wang, Kang Yin 等

**机构** 天津大学, 快手科技, 中科院自动化所

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22209 | **PDF** https://arxiv.org/pdf/2604.22209.pdf | **代码** 暂无 | **Demo** https://qiangchunyu.github.io/UniSonate/

### 📌 简介
UniSonate是一个基于条件流匹配的统一音频生成框架，能够通过标准化的自然语言指令接口合成语音、音乐和音效。该工作首次实现了TTS、TTM和TTA三个任务的真正统一，在指令型TTS和TTM任务上达到了SOTA性能，同时在TTA任务上保持竞争力。

### 🔧 技术方案

**模型架构** 采用双流多模态扩散Transformer（MM-DiT）架构，包含文本流和音频流，通过联合注意力层交互。使用Mel-VAE将44.1kHz波形压缩到连续潜空间，采用Qwen2.5-7B作为指令编码器。

**核心创新**
提出动态令牌注入机制，通过可学习的[SFX]特殊令牌将非结构化环境声音投射到结构化时序潜空间，实现音效的精确时长控制。创新性提出指令-内容对齐范式，将输入标准化为自然语言指令和内容序列两部分。使用多阶段课程学习策略，从结构化语音逐步扩展到半结构化音乐和非结构化音效，有效缓解跨模态优化冲突。

**训练策略**
采用三阶段课程学习：第一阶段仅训练语音数据，第二阶段加入音乐数据，第三阶段加入音效数据。训练使用32块NVIDIA A800 80GB GPU，批次大小16，初始学习率1e-4，优化器为Adam。

### 📊 实验结果
**数据集** 使用50小时语音、20小时音乐和150万音效片段。

**主要指标** 指令型TTS：WER 1.47%（英文）、1.25%（中文），SOTA；TTM：SongEval Coherence 3.18、Musicality 3.01，SOTA；TTA：FAD 4.21，与AudioLDM-L相当。消融实验显示联合训练显著提升语音可懂性（WER从2.24%降至1.47%）和音乐结构（Coherence从3.11提升至3.18）。

**是否开源** 是，提供Demo和代码链接

### ⭐ 评分：9/10
理由 ACL 2026 oral录用，创新性强（首次真正统一TTS/TTM/TTA），实验充分（多任务SOTA），提供完整Demo和代码，具有重大实用价值。

---

## [2] Listening with Time: Precise Temporal Awareness for Long-Form Audio Understanding

**arXiv ID** 2604.22245 | **方向** 语音大模型

**作者** Mingchen Shao, Hang Su, Wenjie Tian 等

**机构** 西北工业大学, 独立研究员

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22245 | **PDF** https://arxiv.org/pdf/2604.22245.pdf | **代码** https://github.com/alanshaoTT/LAT-Audio-Repo | **Demo** 暂无

### 📌 简介
针对长音频时间感知问题，构建了1.2小时长音频数据集LAT-Chronicle和首个支持30分钟音频的基准LAT-Bench，覆盖密集音频字幕、时序音频定位和目标音频字幕三个核心任务。提出LAT-Audio框架，将时间感知表述为渐进式全局到局部推理范式。

### 🔧 技术方案

**模型架构** 基于Qwen3-Omni-30B-A3B-Instruct，采用渐进式全局到局部推理范式。首先构建全局时间轴作为对齐的时序-语义上下文，然后引入Think-With-Audio Chain-of-Thought（TWA-CoT）通过工具使用迭代推理，结合局部音频信息。

**核心创新**
提出TWA-CoT多轮推理框架，每轮包含Think、Tool call和Tool response三个步骤，通过crop_audio工具引入局部音频信息进行迭代验证和修正。设计按需采样策略，对长音频采用2倍时间下采样生成全局时间轴，推理时使用全分辨率音频帧以保留足够的局部细节。

**训练策略** 三阶段训练：第一阶段全局时间轴生成SFT，第二阶段完整轨迹SFT，第三阶段使用GRPO强化学习进一步改善推理质量。训练数据来自LAT-Chronicle，包括7K全局时间轴样本和30K完整CoT轨迹。

### 📊 实验结果
**数据集** LAT-Chronicle（1.2k小时，覆盖中英文，六种场景），LAT-Bench（40小时，人工验证）。

**主要指标** 在TAG、DAC和TAC任务上超越现有方法，输入时长增加时鲁棒性提升。在LAT-Bench上达到SOTA性能，有效缓解时间幻觉和时间戳漂移问题。多种评估设置表明模型能有效利用可靠的说话人区分信息。

**是否开源** 是，提供GitHub代码仓库

### ⭐ 评分：8/10
理由 首次系统研究长音频时间感知，构建大规模数据集和基准，方法创新（渐进式全局到局部推理），实验充分，开源完整代码，具有重要研究价值。

---

## [3] DM-ASR: Diarization-aware Multi-speaker ASR with Large Language Models

**arXiv ID** 2604.22467 | **方向** 语音大模型

**作者** Li Li, Ming Cheng, Weixin Zhu 等

**机构** 武汉大学, 腾讯

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22467 | **PDF** https://arxiv.org/pdf/2604.22467.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
提出DM-ASR，一个说话人区分感知的多说话人ASR框架，将任务重新表述为多轮对话生成过程。给定音频块和区分系统结果，将转录分解为一系列说话人和时间条件查询，明确解耦说话人-时间结构（谁和何时）与语言内容（什么）。

### 🔧 技术方案

**模型架构** 包含语音编码器、映射器、大语言模型解码器和特殊令牌离散化机制。使用Whisper-large-v3-turbo作为语音编码器，Gemma3 270m/Qwen3 0.6B/Qwen3 1.7B作为LLM解码器，采用LoRA进行参数高效微调。

**核心创新**
引入三类特殊令牌：说话人令牌（基于出现顺序的局部索引）、时间戳令牌（以0.1秒为分辨率离散化）和控制令牌。设计说话人区分感知提示构造，将区分输出转换为LLM可理解的说话人和时间戳令牌。创新性支持词级时间戳预测，通过交织单词和时间戳令牌产生更丰富的结构化输出和更好的转录质量。

**训练策略** 采用教师强制将多轮对话连接为单个序列，仅在响应令牌上计算交叉熵损失。引入标签扰动策略，以10%概率随机扰动说话人标签和时间戳，防止模型过度依赖完美正确的区分提示，鼓励使用声学证据和对话上下文从不完美提示中恢复。

### 📊 实验结果
**数据集** 中文：AISHELL-4、AliMeeting、MISP2025、HKUST等；英文：AMI、ICSI、Fisher等。中英文训练数据最多2900小时。

**主要指标** 在AliMeeting和AISHELL-4上，0.6B模型达到tcpCER 19.67%（AliMeeting）和20.40%（AISHELL-4），1.7B模型进一步优化至19.79%和19.94%。在英文数据集上达到与SOTA competitive性能。多评估设置分析显示模型能有效利用可靠区分信息并逐步学习纠正不完美信息。

**是否开源** 暂无

### ⭐ 评分：8/10
理由 创新方法（说话人区分感知的多说话人ASR），支持词级时间戳预测，双语实验充分，多种评估设置深入分析，实用性强。

---

## [4] TTS-PRISM: A Perceptual Reasoning and Interpretable Speech Model for Fine-Grained Diagnosis

**arXiv ID** 2604.22225 | **方向** 语音大模型

**作者** Xi Wang, Jie Wang, Xingchen Song 等

**机构** 清华大学, 小米, 东京大学

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22225 | **PDF** https://arxiv.org/pdf/2604.22225.pdf | **代码** https://github.com/xiaomi-research/tts-prism | **Demo** 暂无

### 📌 简介
提出TTS-PRISM，一个针对中文的多维度诊断框架。建立12维度评估模式，涵盖从稳定性到高级表达力的能力。设计目标化合成流水线，通过对抗扰动和专家锚点构建高质量诊断数据集。通过模式驱动的指令调优将明确评分准则和推理嵌入到高效端到端模型中。

### 🔧 技术方案

**模型架构** 基于MiMo-Audio（100M小时无监督预训练），采用模式驱动的指令调优策略。构造交错目标序列Y=[R1,S1,...,R12,S12]实例化可解释推理机制，强制模型在分配分数前生成基于明确评分准则的客观锚点Ri。

**核心创新**
建立12维度分层分类法：基础能力层（8个子维度，1-5分）评估正确性和稳定性；高级表达力层（4个子维度，0-2分加分）捕捉类人表达细微差别。每个分数级别都有明确的容差阈值（如定义4分允许的具体伪影类型）。设计目标化数据构建策略，融合对抗扰动和专家锚点以增强对长尾伪影的鉴别能力。

**训练策略** 构建200k对齐样本，包括真实人声录音和多范式TTS合成。使用全参数SFT训练MiMo-Audio，优化器AdamW（批次大小1，固定lr=1e-6）。三个消融变体验证核心模块：无指令调优、无CoT、无负样本。

### 📊 实验结果
**数据集** 构建200k指令调优样本，包含800k真实人声录音和多范式TTS合成。建立1600样本中文金测试集（20% OOD）。

**主要指标** 在金测试集上，TTS-PRISM在12个维度上超越Step-Audio-R1（33B）、Qwen3-Omni（30B）和Gemini-2.5-Pro。实现高LCC和SRCC，LCC平均0.717（基础能力层）和0.716（高级表达力层）。在高级表达力层，TTS-PRISM展现出明显优势，特别是在Emotion Expression和Paralinguistics维度。对六个主流TTS范式进行诊断画像，揭示细粒度能力差异和架构倾向。

**是否开源** 是，提供GitHub代码仓库和模型checkpoint

### ⭐ 评分：7/10
理由 创新评估框架（12维度诊断），构建高质量数据集，实验充分，开源完整代码，对TTS社区具有重要价值。

---

## 🎙️ 语音前端

## [5] Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis

**arXiv ID** 2604.22133 | **方向** 语音前端

**作者** Haopeng Geng, Longfei Yang, Xi Chen 等

**机构** 东京大学

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22133 | **PDF** https://arxiv.org/pdf/2604.22133.pdf | **代码** https://github.com/Secondtonumb/IF-MDD | **Demo** 暂无

### 📌 简介
MDD需要建模细粒度声学偏差，但当前ASR衍生的MDD系统存在固有限制。CTC模型倾向于序列级对齐而忽略瞬时发音偏差线索，显式标准先验倾向于将预测偏向预期目标。提出CROTTC-IF，一个无提示框架，解耦声学保真度与标准指导。

### 🔧 技术方案

**模型架构** CROTTC-IF包含三部分：CROTTC声学模型（蓝色）、轻量IF-MDD语言模型（橙色）和详细的IF组件。基于WavLM Large和2层Conformer构建AM，使用2层Transformer decoder作为LM。

**核心创新**
提出CROTTC（Consistency-Regularized Optimal Temporal Transport Classification），通过单调帧级对齐强制执行，准确捕获发音偏差。不同于标准CTC最大化所有有效对齐路径的边际概率，CROTTC通过最优传输理论构建单调映射governing frame-to-label correspondence，产生密集帧级对齐而没有空白令牌主导。引入一致性正则化（CR），通过对称KL散度最小化两个增强视图的后验分布距离。

提出间接融合（IF）策略，基于使用特权信息学习（LUPI）范式。将标准音素和发音偏差信息作为仅在训练阶段可用的特权信息，通过反向传播引导模型的潜表示。IF-MDD包含编码器-解码器backbone和辅助发音检测教师网络，教师网络提供强鉴别梯度信号帮助深层backbone收敛。

**训练策略** CROTTC训练准则：LAM = LCR + η(LOTTC(Za,Y) + LOTTC(Zb,Y))，超参数η设置为1.0。IF-MDD通过多目标优化：Ltotal = ω1LAM + (1-ω1)LLM + ω2(Lpos + Ltype) + ω3Lga，超参数ω1、ω2、ω3分别设置为0.3、1.0和10.0。

### 📊 实验结果
**数据集** L2-ARCTIC（6个说话者）、SO762（5.58小时）、ERJ（0.99小时）、Iqra'Eval2挑战。

**主要指标** CROTTC-IF在L2-ARCTIC上达到71.77% F1-score，在Iqra'Eval2排行榜上达到71.70% F1-score。消融实验显示CROTTC优于CTC（F1-score从66.54%提升至71.77%），IF策略优于无辅助（F1-score从68.03%提升至71.77%）。在SO762和ERJ上显示出强泛化能力。

**是否开源** 是，提供GitHub代码仓库

### ⭐ 评分：7/10
理由 创新方法（无提示MDD框架），Iqra'Eval2 SOTA，实验充分，开源代码，对语音教育领域有重要应用价值。

---

## [6] Audio Effect Estimation with DNN-Based Prediction and Search Algorithm

**arXiv ID** 2604.22276 | **方向** 语音前端

**作者** Youichi Okita, Haruhiro Katayose

**机构** 未明确

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22276 | **PDF** https://arxiv.org/pdf/2604.22276.pdf | **代码** 暂无 | **Demo** https://okitayouichi.github.io/afx-pred-sch-demo/

### 📌 简介
音频效果估计旨在从湿信号估计应用效果的配置。现有方法可分为预测方法（数据驱动预训练模型）和基于搜索的方法（基于湿信号重建）。提出新方法整合这两种方法：首先DNN预测干信号和效果配置，然后基于这些预测进行基于湿信号重建的搜索。

### 🔧 技术方案

**模型架构** 遵循SunAFXiNet架构，包括使用基于时频域U-Net网络的effect remover和从cross-domain encoder瓶颈分支的effect configuration estimator。cross-domain encoder包含归一化和位置编码，交替五层自注意力和交叉注意力编码器。

**核心创新**
提出三种预测阶段设置：Dry-Type-Direct（DNN直接预测整个链的无序效果类型组合和干信号）、Bypass-Type-Iter（DNN迭代预测最后一个单效果的类型和旁路信号）、Bypass-Config-Iter（DNN迭代预测最后一个单效果的配置和旁路信号）。实验发现预测效果类型组合然后基于搜索估计顺序和参数的任务划分在所有指标上最有效。

搜索阶段优化目标为最大化重建湿信号和给定湿信号之间的相似度，使用SI-SDR作为相似度度量。主要使用CMA-ES作为优化算法，当搜索参数数量为1时使用TPE。

**训练策略** 两阶段训练：第一阶段仅训练effect remover，损失函数为Lmae + αLmrstft（α=0.01）；第二阶段冻结effect remover参数，仅训练effect configuration estimator。优化器AdamW，学习率1×10^-4和1×10^-5，批次大小64，epoch分别为170和50。

### 📊 实验结果
**数据集** 从IDMT-SMT-Guitar、GuitarSet、EGDB、Guitar-TECHS提取2231个10秒吉他片段，应用3种效果类型（Chorus、Distortion、Reverb）形成33种效果链组合，总时长205小时。

**主要指标** Dry-Type-Direct + Search在整体效果链类型分类上达到最佳性能（Macro F1 0.958，LD 0.313，EMA 0.774）。在湿信号重建上，Dry-Type-Direct + Search达到SI-SDR 23.07，显著优于仅预测方法的18.18。在音频效果移除上，Bypass-Type-Iter达到最佳SI-SDR 14.95。

**是否开源** 提供Demo链接

### ⭐ 评分：6/10
理由 创新方法（预测+搜索结合），ICASSP 2026录用，实验充分，有Demo，对音频制作领域有实用价值。

---

## [7] Advancing automatic speech recognition using feature fusion with self-supervised learning features: A case study on Fearless Steps Apollo corpus

**arXiv ID** 2604.22203 | **方向** 语音前端

**作者** Szu-Jui Chen, John H.L. Hansen

**机构** 德克萨斯大学达拉斯分校

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.22203 | **PDF** https://arxiv.org/pdf/2604.22203.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
研究SSL模型的融合，旨在利用它们的个体优势并精炼提取特征以改善自然主义场景的语音识别模型。研究大规模自然主义Fearless Steps（FS）APOLLO资源，特别关注FS Challenge（FSC）Phase-4语料库，提供该数据集的首次分析。同时结合CHiME-6数据集评估在多样化自然主义语音场景中的性能。

### 🔧 技术方案

**模型架构** 主要考虑Wav2Vec 2.0、HuBERT和WavLM的大版本。前端模型在训练期间保持冻结，仅作为特征提取器。后端ASR模型采用混合CTC/Attention架构，使用12层Conformer编码器或12层E-Branchformer编码器，配对6层Transformer解码器。

**核心创新**
提出深度交叉注意力（DCA）融合方法，针对偶数层SSL模型应用每层两个交叉注意力模块（A2B和B2A），每个使用单头缩放点积注意力。查询、键、值向量维度dat设置为100。通过加权和在所有层上提取特征，得到交叉注意力表示FA2B和FB2A。最终特征为四个提取特征的组合：FASR = [Norm(X; FA2B); Norm(Y; FB2A)]。

探索Feature Refinement Loss（FRL），通过最小化提取SSL特征之间的互相关来减少冗余。FRL定义：Lrefine = Σi=1D Σj=1D {(Cij)^2 if |Cij| > ε; 0 otherwise}，其中C = MVN(X̃)⊤ · MVN(Ỹ)，ε控制特征间最大相关值。

**训练策略** Conformer编码器使用Adam优化器，学习率在25k步内线性预热至0.001后指数衰减。E-Branchformer使用AdamW，FSC数据集学习率在25k步内预热至0.001，DCA融合实验使用0.002和15k步预热。CHiME-6学习率在20k步内预热至0.001，DCA融合实验相同。使用8块NVIDIA 2080Ti GPU。

### 📊 实验结果
**数据集** FSC Phase-4（29.8小时训练、8.6小时开发、19.2小时评估），CHiME-6。

**主要指标** 在FSC Phase-4 Eval上，WavLM + E-Branchformer baseline达到WER 27.7%。使用DCA融合（HuBERT + WavLM）达到最佳WER 25.1%，绝对提升+1.1%（相比WavLM baseline的27.7%）和+2.6%（相比HuBERT baseline的37.0%）。在CHiME-6上，DCA融合达到WER 13.7%，与最佳方法competitive。

**是否开源** 暂无

### ⭐ 评分：6/10
理由 Speech Communication 2026录用，创新方法（DCA融合），首个FSC Phase-4分析，实验充分，对自然主义ASR有参考价值。