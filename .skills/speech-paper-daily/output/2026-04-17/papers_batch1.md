# 2026-04-17 语音论文速递

**共收录**: 9 篇 | **语音大模型**: 5 篇 | **语音前端**: 4 篇

> 今日 arXiv 语音相关论文共命中 9 篇。
> 以下是按评分排序的结果。

---

## [1] Disentangled Dual-Branch Graph Learning for Conversational Emotion Recognition

**arXiv ID** 2604.14204 | **方向** 语音大模型

**作者** Chengling Guo, Yuntao Shou, Tao Meng, Wei Ai, Yun Tan, Keqin Li

**机构** Central South University of Forestry and Technology, Changsha Hospital for Maternal and Child Health Care, State University of New York

**发布日期** 2026-04-17 | **论文** https://arxiv.org/abs/2604.14204 | **PDF** https://arxiv.org/pdf/2604.14204.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
本文提出双空间特征解耦与双分支图学习框架解决多模态对话情感识别中的冗余信息、语义对齐不足和高阶说话人交互建模挑战。通过共享编码器和模态特定编码器分离模态不变和模态特定表示,傅里叶图神经网络捕获全局一致性,超图神经网络建模高阶说话人交互,最终通过Transformer融合进行情感预测。

### 🔧 技术方案
**模型架构** 模型由多模态特征提取、双空间特征解耦、双分支图学习和Transformer融合四个模块组成。使用RoBERTa提取文本特征,openSMILE提取声学特征,3D-CNN提取视觉特征。特征解耦模块将特征投影到模态不变子空间和模态特定子空间,通过重建损失、循环一致性损失、边际损失和正交损失约束解耦质量。

**核心创新** 双空间特征解耦机制通过共享编码器和私有编码器分离模态不变情感语义和模态特定信息,有效减少跨模态冗余。傅里叶图学习模块在频率域捕获长距离依赖和全局一致性,通过低通和高通滤波器提取低频和高频表示,并引入对称InfoNCE对比损失增强区分性。说话人感知超图神经网络建模高阶说话人交互,通过双重超图变换将原始图边转换为超图节点,使用雅可比多项式构建谱超图滤波器捕获多尺度高阶结构。

**训练策略** 整体损失函数包括分类损失、解耦损失、对比损失和私有分支损失。解耦损失包括重建损失、循环一致性损失、边际损失和正交损失。私有分支损失包括私有空间重建损失和说话人一致性约束损失。训练在IEMOCAP和MELD数据集上进行,使用加权F1分数作为主要评估指标。

### 📊 实验结果
**数据集** IEMOCAP和MELD数据集,IEMOCAP包含5种情感类别,MELD包含更多复杂的多方对话交互。

**主要指标** 在IEMOCAP上达到70.81%加权F1分数,在MELD上达到65.70%加权F1分数,在happy和angry类别上取得最佳F1分数。消融实验显示去除解耦模块导致性能下降,去除傅里叶图分支导致最大退化,去除超图分支也导致性能下降,验证了双分支设计的有效性。

**是否开源** 暂无代码和模型开源

### ⭐ 评分:8/10
理由 创新性高(双空间解耦+双分支图学习),实验充分(IEMOCAP和MELD两个数据集),结果显著(超过多个强基线),实用价值中等(对话情感识别应用场景明确)。

---

## [2] ClariCodec: Optimising Neural Speech Codes for 200bps Communication using Reinforcement Learning

**arXiv ID** 2604.14654 | **方向** 语音前端

**作者** Junyi Wang, Chi Zhang, Jing Qian, Haifeng Luo, Hao Wang, Zengrui Jin, Chao Zhang

**机构** Tsinghua University, Huawei Technologies Co., Ltd

**发布日期** 2026-04-17 | **论文** https://arxiv.org/abs/2604.14654 | **PDF** https://arxiv.org/pdf/2604.14654.pdf | **代码** 暂无 | **Demo** https://demo941.github.io/ClariCodec/

### 📌 简介
本文提出ClariCodec神经语音编解码器,在200bps极端压缩率下通过强化学习优化语音可懂度。传统编解码器使用声学重建损失导致比特分配偏重感知细节,WER严重退化。ClariCodec将量化重新表述为随机策略,使用GRPO优化WER奖励,在冻结声学管道的情况下微调编码器,实现语义对齐而不牺牲感知质量。

### 🔧 技术方案
**模型架构** 基于ConvNeXt V2的编码器将输入压缩为离散编解码索引,通过改进FSQ和可逆层归一化(ILN)稳定量化。编码器通过三次2倍下采样实现8倍总时间下采样,潜在帧率10Hz。解码器对称上采样,Vocos声码器从log-mel频谱图重建波形。量化模块采用两层残差FSQ,每层配置维度级别[8,5,5,5],有效码本大小10比特每层。

**核心创新** 随机残差量化将确定性量化网格重新表述为随机策略,通过距离基概率映射使用Gumbel-Softmax采样量化级别,使编码器成为可训练策略。两阶段训练策略:第一阶段使用重建损失端到端预训练,第二阶段冻结量化器、解码器和声码器,仅微调编码器使用WER驱动奖励。GRPO框架采样16个编解码令牌序列,计算组级相对优势优化策略。

**训练策略** 第一阶段使用复合损失函数包括L1 mel重建损失、对抗损失和特征匹配损失,训练200k步。第二阶段使用RL损失和mel重建损失平衡可懂度优化和声学质量保持,训练50k步。WER奖励使用预训练ASR系统计算重建波形和真实波形的WER负值。使用Libriheavy大规模子集(50,000小时)训练。

### 📊 实验结果
**数据集** Libriheavy训练集(50,000小时),LibriSpeech test-clean和test-other测试集。使用STOI、PESQ、UTMOS、SIM评估声学质量,使用WER评估可懂度。

**主要指标** 在test-clean上达到3.20% WER(无RL时3.68%),在test-other上达到8.93% WER(无RL时9.97%),13%相对WER减少。声学质量指标:STOI 0.88,PESQ 1.98,UTMOS 4.03,SIM 0.56。与更高比特率的编解码器比较,ClariCodec在200bps达到StableCodec-400在400bps的WER性能。消融实验显示ILN对性能至关重要,去除ILN导致WER从3.68%增加到10.5%。

**是否开源** 代码暂无,Demo页面可用

### ⭐ 评分:9/10
理由 创新性极高(首次将RL应用于神经语音编解码器),实验充分(LibriSpeech多个测试集和详细消融),结果显著(200bps超越400bps编解码器),实用价值高(卫星和水下通信等带宽受限场景)。

---

## [3] Listen, Pause, and Reason: Toward Perception-Grounded Hybrid Reasoning for Audio Understanding

**arXiv ID** 2604.14806 | **方向** 语音大模型

**作者** Jieyi Wang, Yazhe Niu, Dexuan Xu, Zhongyu Wei

**机构** Shanghai AI Laboratory, Peking University, CUHK MMLab, Fudan University

**发布日期** 2026-04-17 | **论文** https://arxiv.org/abs/2604.14806 | **PDF** https://arxiv.org/pdf/2604.14806.pdf | **代码** https://github.com/JOY-SWang/HyPeR | **Demo** 暂无

### 📌 简介
本文提出HyPeR混合感知推理框架,通过显式感知反射和隐式潜在推理增强大型音频语言模型的音频理解能力。引入PAQA数据集实现听觉场景分层解耦,分离语音和环境声音、区分多说话人。第一阶段通过SFT教授模型模仿类人听觉分解,第二阶段使用GRPO优化内部推理,引入PAUSE令牌促进声学模糊阶段的潜在计算。

### 🔧 技术方案
**模型架构** 基于Qwen2-Audio-7B-Instruct构建两阶段混合框架。第一阶段通过SFT在PAQA数据集上训练显式感知反射,生成包含规划、字幕、推理、总结和反射的结构化推理链。第二阶段使用GRPO优化隐式推理,当置信度低时模型自主调用PAUSE令牌进行潜在推理。PAQA数据集包含7,470多选音频QA对,每个包含结构化注释。

**核心创新** ASA启发的分层解耦策略将复杂听觉场景分解为两层:Level 1分离语音与环境声音,Level 2区分说话人与说话人。PAUSE令牌表示推理步骤,模型在声学模糊阶段发出PAUSE令牌并进行潜在推理,不产生可见输出令牌。最低组置信度(LGC)指标检测推理轨迹中的局部不确定段,当LGC落入中间模糊范围时触发PAUSE,低于阈值时中止轨迹防止幻觉。

**训练策略** 第一阶段使用交叉熵损失在PAQA训练集上进行SFT。第二阶段使用GRPO框架采样组级rollouts,计算组相对优势更新策略。奖励函数包括准确性奖励、格式奖励、感知一致性奖励和长度奖励。感知一致性奖励沿三个声学-逻辑轴正则化推理链:背景声鲁棒性、说话人-ASR保真度、推理-答案对齐。使用关键词集作为冷启动先验校准声学敏感性。

### 📊 实验结果
**数据集** PAQA训练集用于SFT,AQVA增强数据集(30,000样本)用于RL训练。评估数据集包括PAQA Test(MSQA-hard和ENVQA-hard),MMAU Test-mini和Test,MMAR和MMSU。

**主要指标** 在MMAU Test-mini上达到67.40%平均准确率,在MMAU-Test上达到67.15%,在MMAR上达到55.50%,在MMSU上达到56.38%。PAQA Test上WER达到0.78%,CER达到0.62%,FSD50K上mAP达到43.6%。与大型模型比较,HyPeR达到与Audio-Flamingo-3和OmniVinci相当的性能。PAUSE机制在复杂音频环境(特别是MMAR +25.5)上最有效。

**是否开源** 代码和数据开源在GitHub

### ⭐ 评分:8/10
理由 创新性高(PAUSE令牌+分层解耦+混合推理),实验充分(多个基准数据集和详细消融),结果显著(达到大型模型性能),实用价值高(复杂音频理解场景)。