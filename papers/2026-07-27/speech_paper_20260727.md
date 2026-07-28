# 2026-07-27 语音论文速递

**共收录**: 9 篇 | **语音大模型**: 5 篇 | **语音前端**: 4 篇

> 今日 arXiv 语音相关论文共命中 9 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

## [1] Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning

**arXiv ID** 2607.22304 | **方向** 语音大模型

**作者** Roseline Polle, Owen Fairs, San Martin Fernandez, Looney Wu, Georgescu Goria 等

**机构** thymia, UK; The University of Edinburgh, UK; University of Southampton, UK

**发布日期** 2026-07-24 | **论文** https://arxiv.org/abs/2607.22304 | **PDF** https://arxiv.org/pdf/2607.22304.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音合成数据增强在语言任务（如ASR）中已有广泛探索，但在副语言学任务（如临床情感识别）中却鲜有研究。语音克隆是一种有前景的数据增强方法，但通常只评估语音可懂度（WER）或说话人相似度（SS），而非下游任务性能。本文评估了8个开源语音克隆模型在5个副语言学任务上的表现，包括情感、情感、讽刺、口音和抑郁/焦虑检测，证明了大多数模型能保留信号且性能下降较小。

### 🔧 技术方案

**模型架构** 评估了8种开源语音克隆模型，覆盖自回归、Flow-matching和混合架构，包括XTTS v2（GPT-2自回归+Perceiver）、Zonos（Mamba2 SSM+Transformer解码器）、E2-TTS和F5-TTS（Flow-matching）、OpenAudio S1-mini（Qwen3 LLM+在线RLHF）、CosyVoice 2/3（自回归+Flow-matching）、MaskGCT（Masked生成式编解码Transformer）。

**核心创新** 提出使用语音克隆进行跨语言数据增强的新方法，将英语临床语音克隆为日语，验证了在低资源语言中增强临床语音数据的可行性。设计了两种克隆条件：Repeat（克隆语音重现原始转录）和Standard（所有克隆说话人产生相同固定段落）。

**训练策略** 使用WavLM Large提取1024维说话人嵌入，采用标准Scaler和L2正则化Logistic Regression分类器（C=0.001，balanced class weights）。所有结果报告为AUC（one-vs-rest，macro-averaged）。

### 📊 实验结果
**数据集** IEMOCAP（情感4类）、MELD（情感7类/情感3类）、MUSTARD（讽刺二分类）、VCTK（口音3类）、专有英语临床语料库（抑郁/焦虑二分类）、专有日语临床语料库。

**主要指标** 在Repeat条件下，前5个模型保留了超过90%的信号（P≥0.90）。E2-TTS、OpenAudio、MaskGCT、CosyVoice3，F5-TTS的平均性能下降为-1.7pp到-4.9pp。在跨语言任务中，OpenAudio在抑郁检测上提升+3.3pp，CosyVoice3在焦虑检测上提升+4.0pp，均显著优于原始跨语言基线。

**是否开源** 部分模型开源

### ⭐ 评分：8/10
创新性地将语音克隆应用于副语言学任务和跨语言数据增强，实验充分，覆盖8个模型5个任务，验证了语音克隆在临床语音数据增强中的实用价值。唯一不足是未测试更多语言对。

---

## [2] Listen, Do Not Copy: Internalizing Audio-Grounded Scaffold Context for Robust Omni-Model Speech Understanding

**arXiv ID** 2607.21943 | **方向** 语音大模型

**作者** Pengfei Zhang, Biao Tian, Tianxin Xie, Minghao Yang, Xiangang Li, Li Liu

**机构** 暂未明确标注

**发布日期** 2026-07-24 | **论文** https://arxiv.org/abs/2607.21943 | **PDF** https://arxiv.org/pdf/2607.21943.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Omni模型在转录干净单speaker语音时表现良好，但在说话人重叠和场景嘈杂时准确率急剧下降，而这正是知道"谁说了什么"最关键的场景。本文发现提供完整转录作为上下文会让模型通过"复制"而非"聆听"来提高分数，这种失败模式被称为"感知绕过"。提出Audio-Grounded Scaffold Context (AGSC)方法，通过提供不完整的线索来引导聆听，同时限制直接复制。

### 🔧 技术方案

**模型架构** 基于Qwen3-Omni 30B、MiniCPM-o 4.5 (9B)和Ming-flash-omni 2.0（100B总参数，6.1B活跃per-token专家混合）进行实验。

**核心创新** 提出感知绕过（Perception Bypass）概念，将静音音频作为上下文质量的检验测试。AGSC提供三种线索：目标说话人活动、场景噪音水平、部分打乱的词汇。设计三个安全保护：音频优先指令、答案重叠筛查、静音音频控制。

**训练策略** 使用LoRA进行监督微调（rank=16，α=32），然后进行GDPO（Group Reward-Decoupled Policy Optimization）训练，单独归一化格式、门控和转录奖励。

### 📊 实验结果
**数据集** Context-Speech Bench (CSB)：13255训练样本和1525评估样本，涵盖重叠、噪音、会议，流式线索和门控。

**主要指标** 在重叠+噪音条件下，无线索的capped mean mpWER从25%-71%降至9%-15%。最难1/3样本上，从50%-96%降至13%-17%。门控GDPO达到timeline F1 0.753-0.803，延迟约0.2s。

**是否开源** 承诺开源AGSC代码和基准清单

### ⭐ 评分：8/10
创新性地提出感知绕过问题并设计了系统性解决方案，实验在3个异构Omni模型上进行，验证了内部化假设。方法创新性强，实验规模大。

---

## [3] Music-JEPA: Learning a World Model of Sound from Action

**arXiv ID** 2607.22000 | **方向** 语音大模型

**作者** 暂未从摘要提取到

**机构** 暂未从摘要提取到

**发布日期** 2026-07-24 | **论文** https://arxiv.org/abs/2607.22000 | **PDF** https://arxiv.org/pdf/2607.22000.pdf | **代码** 即将发布 | **Demo** https://zzwaang.github.io/music-jepa-demo/

### 📌 简介
联合嵌入预测架构（JEPA）已成为通过预测潜在表示来学习世界模型的新范式。本文提出Music-JEPA，将音乐建模为动作条件系统：音频作为状态，钢琴卷作为乐器动作。给定当前音频状态和动作，模型预测未来音频状态，模拟人类通过交互学习音乐声音的方式。

### 🔧 技术方案

**模型架构** 使用Vision Transformer (ViT) backbone编码状态和动作表示。状态编码器使用12层Transformer，动作编码器使用8层。状态和动作预测器均为6层Transformer。模型参数量约19M。

**核心创新** 将JEPA框架应用于音乐领域，将音乐建模为动作条件系统。引入动作预测器建模动作的时间结构。采用指数移动平均（EMA）训练策略防止表示崩溃。

**训练策略** 在MAESTRO v3.0数据集上训练，该数据集包含约200小时钢琴录音及时间对齐的MIDI。使用Adam优化器，学习率6e-4，权重衰减1e-4，batch size 128，训练15-25个epoch。

### 📊 实验结果
**数据集** MAESTRO v3.0（古典钢琴曲目，17-20世纪初作曲家）

**主要指标** 在beat tracking任务上，Music-JEPA的F1为0.6208（70ms容差）和0.6599（100ms容差），优于AO-JEPA和MERT。在composer identification上，Top-3准确率70.45%，Top-5准确率87.34%。在key recognition上，wF1为76.17%。在持续踏板估计上达到最佳性能（MAE最低）。

**是否开源** 代码和预训练模型即将发布

### ⭐ 评分：7/10
将JEPA范式创新性地应用于音乐世界模型，证明了动作条件动态建模的有效性。在下游MIR任务上表现竞争力强。不足是仅在钢琴数据集上验证。

---

## [4] SoundscapeAgent: Agentic Soundscape Construction for Controllable Synthesis and Scalable Audio-Language Supervision

**arXiv ID** 2607.21857 | **方向** 语音大模型

**作者** Hao Zhang, Yiwen Zhao, Yixuan Zhang, Yiwen Shao, Steve Yves

**机构** 暂未从摘要提取到（腾讯实习期间完成）

**发布日期** 2026-07-23 | **论文** https://arxiv.org/abs/2607.21857 | **PDF** https://arxiv.org/pdf/2607.21857.pdf | **代码** 即将发布 | **Demo** https://haozhang6720.github.io/SoundscapeAgentDemoPage/

### 📌 简介
本文提出智能音景构建框架，用于可控的组合音频生成。该框架使场景规划、源选择，时间布局和渲染步骤显式化，而不是像单shot文本到音频模型那样隐式处理。LLM代理将用户意图转换为可执行场景计划，通过检索和按需生成获取资产，渲染可控多事件混合，并导出对齐的场景元数据。

### 🔧 技术方案

**模型架构** LLM代理层+渲染层双耦合架构。代理层解释用户意图并生成场景计划，渲染层执行确定性时间线调度，波形的Post-processing和导出。

**核心创新** 提出智能音景构建框架，将组合音景生成作为智能体引导的构建问题，而非从文本到波形的单shot映射。支持离线先验模式进行大规模语料库构建。

**训练策略** 使用EzAudio和TangoFlux作为文本到音频后端进行按需生成。使用Qwen2.5-Omni音频编码器+Qwen2.5-7B-Instruct进行下游音频推理。

### 📊 实验结果
**数据集** AudioCaps测试集、DCASE 2024任务7、MMAU test-mini

**主要指标** 人类对齐评分上，SoundscapeAgent在整体align得分3.63，优于TangoFlux (3.41)、EzAudio (2.98)、AudioLDM2 (2.91)。在下游音频推理任务上，使用100k合成示例后，MMAU整体准确率从51.05%提升至56.50%，最大提升出现在Hard问题(+8.90点)。

**是否开源** 代码、演示和听力测试结果将发布

### ⭐ 评分：7/10
提出智能体框架进行音景构建的思路新颖，实验验证了可控生成和大规模音频语言监督两条路径。人类评估和客观指标结合较好。

---

## [5] Reflector: Arrangement-Aware Harmonic Retrieval for Sample-Based Composition

**arXiv ID** 2607.22413 | **方向** 语音大模型

**作者** Austin Rockman

**机构** Independent Researcher

**发布日期** 2026-07-24 | **论文** https://arxiv.org/abs/2607.22413 | **PDF** https://arxiv.org/pdf/2607.22413.pdf | **代码** https://github.com/austinrockman/reflector | **Demo** 暂无

### 📌 简介
样本检索工具可以帮助作曲者找到和谐兼容的材料，但随着编曲演进和每个音乐决定的谐波上下文变化，从固定参考样本查询变得不那么有效。本文提出Reflector，一个交互式音频工作站，跟踪谐波组合随着作曲者时间线上的积累而变化，并随着编曲发展调整检索。

### 🔧 技术方案

**模型架构** 核心是手工设计的12×12间隔类权重表，作为固定间隔类oracle。一个完全在合成音频上训练的编码器学习在128维嵌入空间中近似oracle，其中点积代替交互速度下的兼容性评分。

**核心创新** 提出排列感知检索系统，跟踪多轨道时间线上的谐波组合。将oracle蒸馏到编码器中，通过InfoNCE优化点积几何。使用sweep-line分析发现共响区域，计算oracle加权质心。

**训练策略** 两阶段训练：Stage A生成基于音阶集合的轨迹，Stage B将每个轨迹渲染成音频（加法合成、域随机化），然后用CQT重新提取色度。编码器在合成数据上训练，无需版权录音。

### 📊 实验结果
**数据集** 631个样本的工作语料库（电子、原声、实地录音等）

**主要指标** 学习到的嵌入保留oracle的成对判断，同时覆盖整个库。NDCG@10达到0.85。直接内核评分覆盖率仅64个样本（崩溃到通用donor），但学习嵌入覆盖625个样本。相似度和兼容性几乎相反——相似回答"什么相似"，兼容性回答"什么组合"。

**是否开源** 免费macOS应用，训练pipeline开源

### ⭐ 评分：7/10
系统性强，设计决策有详细说明。实验揭示了oracle蒸馏作为多样性控制的作用。无需版权训练数据是重要优点。

---

## 🎙️ 语音前端

## [6] Probing Speaker Identity Sensitivity in Audio Deepfake Detectors

**arXiv ID** 2607.21820 | **方向** 语音前端

**作者** Daniyal Kabir Dar, Arun Ross

**机构** Michigan State University, USA

**发布日期** 2026-07-23 | **论文** https://arxiv.org/abs/2607.21820 | **PDF** https://arxiv.org/pdf/2607.21820.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
音频深度伪造检测器用于区分真实语音和合成语音，在标准基准上表现良好，但在跨数据集评估时错误率可能增加20倍。本文认为一个原因是检测器依赖说话人身份：标准训练语料库中说话人身份与真实/合成标签相关联，允许检测器部分依赖说话人相关线索而非仅依赖合成伪影。本文提出Identity Sensitivity Score (ISS)，一种无需标签的per-utterance诊断指标。

### 🔧 技术方案

**模型架构** 使用AASIST（图注意力网络）和RawNet2（端到端CNN）两种架构不同的检测器进行评估。

**核心创新** 提出Identity Sensitivity Score (ISS)，通过在logit空间扰动来测量检测器输出在不同说话人身份上下文下的变化程度。使用ECAPA-TDNN提取说话人嵌入，使用FreeVC进行语音转换验证。

**训练策略** 预训练ECAPA-TDNN用于说话人嵌入提取，检测器使用官方预训练checkpoint或ASVspoof 2021基线训练。

### 📊 实验结果
**数据集** ASVspoof 2019 LA和ASVspoof 2021 LA

**主要指标** 在2019 LA上，AASIST错误预测的ISS比正确预测高29倍，RawNet2高52倍。ISS单独预测错误分类的AUC达0.954。语音转换验证显示，高ISS utterances对身份manipulation的响应比低ISS utterances强19.2-30.7倍。

**是否开源** 暂无

### ⭐ 评分：7/10
提出新视角分析深度伪造检测器的失败模式，ISS作为诊断工具具有实际价值。实验规模大，但仅在两个检测器上验证。

---

## [7] CODA: Cascaded Online Discontinuity-Aware Alignment for Real-Time Image-Based Score Following

**arXiv ID** 2607.21899 | **方向** 语音前端

**作者** 暂未从摘要提取到

**机构** 暂未从摘要提取到

**发布日期** 2026-07-24 | **论文** https://arxiv.org/abs/2607.21899 | **PDF** https://arxiv.org/pdf/2607.21899.pdf | **代码** https://github.com/ValleyC/CODA | **Demo** 暂无

### 📌 简介
实时乐谱跟踪从乐谱图像仍然具有挑战性，因为模型必须在严格延迟约束下处理流式音频同时解决高度重复的视觉模式。本文提出CODA，据我们所知是第一个解决这两个缺口的实时乐谱跟踪系统。CODA明确利用乐谱的级联结构：首先选择活动系统，然后选择活动系统内的活动小节，最后选择所选小节内的活动音符。

### 🔧 技术方案

**模型架构** 因果Mamba音频编码器+共享CNN视觉主干+三个级联阶段（系统选择，小节选择、音符定位）+带学习时间先验的Beam Search。

**核心创新** 级联选择-回归公式强制几何一致性。静音驱动的跳转检测和恢复机制处理乐谱不连续性（重复、Da Capo、coda跳转）。

**训练策略** 两阶段课程训练：第一阶段使用真实系统标签训练，第二阶段使用调度采样逐渐混入模型自预测系统。

### 📊 实验结果
**数据集** MSMD数据集（354训练、19验证、94测试曲目）

**主要指标** 在Setting I上，CODA在≤0.10s阈值下达0.914，而CYOLO-SB为0.837。小节准确率从0.890提升至0.975。在Setting II上，达0.743 vs 0.630。跳转恢复上，重复子集1s系统恢复率0.78，随机子集0.64。

**是否开源** 开源代码：https://github.com/ValleyC/CODA

### ⭐ 评分：7/10
方法创新性强，级联结构设计合理，实验全面（跳转恢复 benchmark是重要贡献）。在实时图像乐谱跟踪领域有显著推进。

---

## [8] Kutti AI: A Voice-First, Offline-Capable Learning Companion with Real-Time Struggle Detection for Visually-Impaired Children

**arXiv ID** 2607.22377 | **方向** 语音前端

**作者** Kadharmoideen Fadurudeen

**机构** Independent Researcher

**发布日期** 2026-07-24 | **论文** https://arxiv.org/abs/2607.22377 | **PDF** https://arxiv.org/pdf/2607.22377.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
大多数面向儿童的教育技术都围绕视觉界面构建，这让全球数百万视力障碍儿童被排斥在外。本文提出Kutti AI，一个语音优先的学习伴侣，设计上让音频成为主要且足够的界面：孩子通过口语对话学习课程内容，通过说话回应，并获得口语反馈，不依赖视觉元素。

### 🔧 技术方案

**模型架构** 跨平台移动应用，使用React Native (Expo)和TypeScript构建。语音识别使用设备端Whisper ASR模型实现离线转录。语音合成使用平台TTS引擎。

**核心创新** 多信号挣扎检测引擎，融合三个独立信号：响应延迟分析、错误尝试跟踪、基于关键词的犹豫检测。跨语言答案匹配管道，结合语言感知翻译/音译、Levenshtein模糊匹配和文本规范化。

**训练策略** 设备端运行的 Whisper 模型用于语音识别，无需网络连接。课程内容本地缓存，离线优先设计。

### 📊 实验结果
**数据集** 支持英语和泰米尔语，原型在Half Baked hackathon演示

**主要指标** 响应延迟阈值2.5秒触发提示；错误尝试阈值2次触发简化问题；模糊匹配相似度阈值0.6；跨语言匹配容忍code-switching和发音变化。

**是否开源** 暂无

### ⭐ 评分：6/10
面向视障儿童的教育技术创新性强，实用价值高。离线优先设计对欠发达地区有重要意义。但目前只有hackathon原型演示，定量评估不足。

---

## [9] Optimising Neural Speech Codecs for 300bps Communication using Reinforcement Learning

**arXiv ID** 2607.10023 | **方向** 语音前端

**作者** 暂未获取到详细信息

**机构** 暂未获取到详细信息

**发布日期** 2026-07-24 | **论文** https://arxiv.org/abs/2607.10023 | **PDF** https://arxiv.org/pdf/2607.10023.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
暂未获取到详细信息

### 🔧 技术方案
暂未获取到详细信息

### 📊 实验结果
暂未获取到详细信息

### ⭐ 评分：5/10
信息不足，无法完整评估

---

## 📋 其他论文（快速浏览）

### 语音大模型

### 语音前端

---

*SpeechResearchTool 🍀 自动生成 · 数据来源：arXiv*
