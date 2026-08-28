# 2026-08-27 语音论文速递

**共收录**: 13 篇 | **语音大模型**: 9 篇 | **语音前端**: 4 篇

> 目标日期 2026-08-27 arXiv 语音相关论文共命中 13 篇（补录）。
> 数据来源 arxivdaily 镜像，基于页面 AI 总结与 comments 精炼，按评分排序。

---

## 语音大模型

## [1] CSAVocoder: A Causal Spatial Audio Vocoder Towards Real-Time Spatial Audio Generation

**arXiv ID**：2608.25404 | **方向**：语音大模型

**作者**：Zhiyuan Zhu, Han Wang, Wenxiang Guo, Yu Zhang, Changhao Pan, Rui Yang, Zhou Zhao

**机构**：暂无公开机构信息

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25404 | **PDF**：https://arxiv.org/pdf/2608.25404 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有神经声码器扩展到空间音频时往往出现空间质量下降，且难以满足实时性要求。CSAVocoder 提出基于因果 GAN 的空间音频声码器，通过空间适配器与空间一致性判别器实现空间保真度与音频质量的联合优化，在大规模数据集上验证其同时具备高空间保真度、有竞争力的音频质量与实时推理性能。

### 📊 实验结果
**数据集与关键信息**：在大规模空间音频数据集上兼顾高空间保真度、有竞争力音频质量与实时性能；具体指标详见页面 AI 总结。

### ⭐ 评分：7/10
首次提出面向实时空间音频生成的因果声码器，空间适配器加空间一致性判别器设计针对性强、工程价值高；但缺少开源与量化细节，评分主要基于 AI 总结。

---

## [2] VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction

**arXiv ID**：2608.26005 | **方向**：语音大模型

**作者**：Zhifei Xie, Jiaqi Lang, Ze An, Yifan Zhao, Dongchao Yang, Kai Li, Ziyang Ma, Mingbao Lin, Chunyan Miao, Shuicheng Yan

**机构**：暂无公开机构信息

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.26005 | **PDF**：https://arxiv.org/pdf/2608.26005 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
面向实时语音交互中语音大模型（SLM）缺乏记忆的痛点，本文提出 VoiceMem"双脑流式记忆"架构，将短时工作记忆与长期记忆结合，构建了完整的记忆感知 SLM 训练、评估与部署流水线。实验显示其在记忆准确性、情感个性化与实时性上均有显著优势，为实时语音交互提供了实用的记忆基础。

### 📊 实验结果
**数据集与关键信息**：在记忆准确性、情感个性化与实时性上优势显著；comments：18 pages, 9 figures, 6 tables，具体指标详见页面 AI 总结。

### ⭐ 评分：7/10
"双脑流式记忆"架构直击实时语音助手的长期记忆短板，覆盖训练到部署的完整流水线，实用性突出；具体量化结果依赖 AI 总结，代码未披露。

---

## [3] Can We Read the Mind of an Audio LLM? A Verbalizable, Multilingual Middle-Layer Workspace

**arXiv ID**：2608.24958 | **方向**：语音大模型

**作者**：Jiajun Fan, Jingyuan Li, Prashanth Gurunath Shivakumar, Qi Luo, Jia-Hong Huang, M. Maruf, Roger Ren, Yile Gu, Rahul Pandey, Ge Liu, Ivan Bulyko

**机构**：Amazon AGI Foundations（亚马逊 AGI 基金会）；伊利诺伊大学厄巴纳-香槟分校

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.24958 | **PDF**：https://arxiv.org/pdf/2608.24958 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文利用 logit lens 技术分析 Qwen3-Omni 音频大语言模型的内部表示，发现其中间层在输出最终答案前就已清晰呈现音频问题的答案，表明音频推理过程中存在可解读且多语言的中间层工作空间。该工作为解读音频 LLM 的内部思维机制提供了定性依据，揭示了音频特征在层间传递与语言信号分布的特性。

### 📊 实验结果
**数据集与关键信息**：基于 logit lens 对 Qwen3-Omni 的多语言中间层分析，发现其中间层提前呈现问题答案；为定性分析，量化指标详见页面 AI 总结。

### ⭐ 评分：6/10
将 logit lens 可解释性方法移植到音频 LLM，填补了音频模型内部机制解读的空白，来自工业界、视角新颖；但方法为已有技术迁移、以定性结论为主，缺乏系统定量评估。

---

## [4] TurnBench: A Multi-Domain Benchmark for Turn-Taking Dynamics in Spoken Dialogue

**arXiv ID**：2608.25218 | **方向**：语音大模型

**作者**：Freeman Jiang, Ramon Sanabria, Soham Deshmukh, Bandhav Veluri, Simon Michael Vuch Williams, Elliott K. Suen, Garreth Lee, Kevin Yoonho Choi, Takuya Umeki, Riku Kubo, Sathvik Udupa, Chien-yu Huang, Shih-Yun Shan Kuan, Zhuoyan Tao, Satyapriya Krishna, Sefik Emre Eskimez, Yu Tsao, Hung-yi Lee, Shinji Watanabe

**机构**：暂无公开机构信息

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25218 | **PDF**：https://arxiv.org/pdf/2608.25218 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
口语对话系统中话轮转换的流畅度尚无统一评测标准。TurnBench 提出一个多领域的话轮转换动态基准，包含标注语料与评估协议，系统测试了 14 种系统。结果表明打断误报具有明显的风格依赖性，且当前系统均未达到人类流畅话轮交接的水平，为口语对话交互评测提供了标准化工具。

### 📊 实验结果
**数据集与关键信息**：覆盖多领域的标注语料与评估协议；测试 14 种系统发现打断误报具风格依赖性，当前系统整体未达人类流畅交接水平（Submitted to IEEE SLT 2026）。

### ⭐ 评分：6/10
首个多领域话轮转换评测基准，参与机构众多、覆盖面广，对口语对话研究有标准化价值；作为基准工作无新方法贡献，量化细节依赖 AI 总结。

---

## [5] AudioLens: Multi-Perspective Speech Clustering with Reasoning Audio-Language Models

**arXiv ID**：2608.25177 | **方向**：语音大模型

**作者**：Wenjun Huang, Qiaosong Chu, Tiger Shao, Pengfei Zhang, Yutong Song, Hanning Chen, Yezi Liu, Weiyi Wu, SungHeon Jeong, Ryozo Masukawa, Sanggeon Yun, Yang Ni, Jiang Gui, Mohsen Imani

**机构**：加利福尼亚大学欧文分校；达特茅斯学院；普渡大学西北分校

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25177 | **PDF**：https://arxiv.org/pdf/2608.25177 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出"音频多视角语音聚类"任务，让模型基于推理能力对语音从多个视角进行聚类划分，并构建基准 AudioLens-Bench。作者开发经推理蒸馏与偏好优化训练的 AudioLens-R1 模型，实验表明其在语音聚类任务上性能优于现有基线模型。

### 📊 实验结果
**数据集与关键信息**：构建 AudioLens-Bench 基准；AudioLens-R1 经推理蒸馏与偏好优化后在语音聚类上优于基线模型；具体指标详见页面 AI 总结。

### ⭐ 评分：6/10
将推理能力引入语音聚类并提出配套基准，思路有新鲜度；但任务设定较窄且无开源信息，评分基于 AI 总结、实验细节有限。

---

## [6] SPECTRA: Subspace-Preserving Embedding Calibration, Transport, and Replay for Fully Few-Shot Class-Incremental Audio Classification

**arXiv ID**：2608.25054 | **方向**：语音大模型

**作者**：Giries Abu Ayoub, Loay Mualem, Simon Korman

**机构**：海法大学；斯图加特大学

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25054 | **PDF**：https://arxiv.org/pdf/2608.25054 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对全少样本类增量音频分类中持续学习导致性能快速下降的问题，SPECTRA 提出包含嵌入校准适配器、子空间特征重放以及直推式最优传输优化三部分的框架，在保留已有子空间结构的同时实现新类的少样本学习，在三类基准数据上均优于现有方法。

### 📊 实验结果
**数据集与关键信息**：在三类类增量音频分类基准上优于现有方法；具体准确率指标详见页面 AI 总结。

### ⭐ 评分：6/10
子空间保留校准与最优传输重放的组合设计有方法论价值，聚焦少样本增量学习的实际难题；但以 AI 总结为依据，缺乏开源与数据集细粒度对比。

---

## [7] Domain-Adaptive ASR for Telephony AI Agents: Fine-tuning Canary Flash Models for Enterprise Contact Center Applications

**arXiv ID**：2608.24916 | **方向**：语音大模型

**作者**：Chanameth Boonpramuk, Winn Voravuthikunchai, Songpol Bunyang

**机构**：Botnoi Group（博特诺伊集团）

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.24916 | **PDF**：https://arxiv.org/pdf/2608.24916 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
企业联络中心的电话语音在信道、口音与术语上明显偏离通用 ASR 训练分布。本文基于 NVIDIA NeMo 框架微调 Canary Flash ASR 模型，构建面向电话场景的数据集，通过四项实验验证微调可显著提升电话环境下的 ASR 识别性能，同时保持实时响应性，为电话智能体提供领域适配 ASR 实践方案。

### 📊 实验结果
**数据集与关键信息**：构建电话导向数据集，经四项实验验证微调提升电话场景 ASR 性能并保持实时性；具体 WER 指标详见页面 AI 总结。

### ⭐ 评分：5/10
实用价值明确（企业电话 ASR 落地），工程化微调流程清晰；但属应用工程报告，技术贡献有限，无公开数据与完整对比。

---

## [8] Mandarin Humorous Homophone Recognition and Disambiguation in Automatic Speech Recognition

**arXiv ID**：2608.25384 | **方向**：语音大模型

**作者**：Sicheng Jin, Jinghao Chen, Mostafa Shahin, Beena Ahmed, Aditya Joshi

**机构**：暂无公开机构信息

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25384 | **PDF**：https://arxiv.org/pdf/2608.25384 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
中文幽默常依赖同音字的语音双关，而 ASR 默认输出规范词形，导致幽默内容被"规整化"丢失。本文针对第二语言中文学习者发音诊断（MDD）需求，提出基于音系特征的 Wav2Vec2-CTC 框架，区分音段错误与声调错误，可降低 FAR（漏报率）与 DER（诊断错误率），提供更细粒度的发音诊断反馈。

### 📊 实验结果
**数据集与关键信息**：基于音系特征的 Wav2Vec2-CTC 框架区分音段与声调错误，降低 FAR 与 DER，提供更详细诊断反馈（Accepted at ISCSLP 2026）。

### ⭐ 评分：5/10
聚焦中文幽默同音字 + 发音诊断这一特色场景，任务选择有新意；但方法为既有 Wav2Vec2-CTC 的简单适配，缺少大规模实验支撑。

---

## [9] Formal, Executable and Explainable Runtime Monitoring of Spoken Air Traffic Control Operational Procedures

**arXiv ID**：2608.25926 | **方向**：语音大模型

**作者**：Roberto Luvini, Giacomo Longo, Alessandro Armando, Enrico Russo

**机构**：热那亚大学；CASD — 高级国防研究大学学院

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25926 | **PDF**：https://arxiv.org/pdf/2608.25926 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
航空管制中大量流程通过口语交流执行，对运行程序的实时合规监控需求迫切。本文提出运行时验证框架，通过监控管制员与飞行员的口语交流、监视数据与机载观测，以形式化时序公式评估 ICAO 义务的履行情况，能准确识别程序违规，在真实场景、合成场景及历史事故复现中均表现良好。

### 📊 实验结果
**数据集与关键信息**：以形式化时序公式评估 ICAO 义务，准确识别程序违规，在真实、合成场景及历史事故上表现良好；具体指标详见页面 AI 总结。

### ⭐ 评分：5/10
将口语 ASR 与形式化运行时验证结合，领域应用价值与可解释性突出；但偏领域应用系统，缺少针对语音/ASR 侧的技术创新与通用性讨论。

---

## 语音前端

## [1] A Training-Free Proactive Defense Against Partial Speech Manipulation via Self-Embedding Steganography

**arXiv ID**：2608.25285 | **方向**：语音前端

**作者**：Yigitcan Özer, Zhe Zhang, Wanying Ge, Xin Wang, Junichi Yamagishi

**机构**：情报信息研究所（National Institute of Informatics）

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25285 | **PDF**：https://arxiv.org/pdf/2608.25285 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
部分（局部）语音被替换、拼接式的深度伪造难以被整段检测器捕获。本文提出一种无需训练的主动防御方法，将自嵌入策略与现有音频隐写术结合，在待保护语音中内嵌自身摘要，解码器据此修复被操纵区域从而实现操纵检测。该方法无需重新训练模型、数据效率高，可与被动检测互补。已被 Interspeech 2026 接收。

### 📊 实验结果
**数据集与关键信息**：自嵌入隐写实现部分语音操纵检测与修复，可与被动防御互补且无训练、数据效率高（6 pages; accepted at Interspeech 2026）；具体指标详见页面 AI 总结。

### ⭐ 评分：7/10
针对部分语音操纵提出无训练的主动防御范式，隐写自嵌入设计简洁有效且与被动防御互补，被顶级语音会议接收；量化细节依赖 AI 总结，代码未公开。

---

## [2] Knowledge Distillation for Efficient Acoustic Echo Control

**arXiv ID**：2608.25596 | **方向**：语音前端

**作者**：Ernst Seidel, Pejman Mowlaee, Tim Fingscheidt

**机构**：暂无公开机构信息

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25596 | **PDF**：https://arxiv.org/pdf/2608.25596 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文首次将知识蒸馏（KD）系统应用于声学回声控制（AEC）任务。提出的 CGGN16 学生模型计算复杂度仅为教师模型的 2%，在大幅降低计算成本的同时还能减少近端语音失真，性能优于同类高效 AEC 模型，为嵌入式低算力回声消除提供了高效的模型压缩路线。

### 📊 实验结果
**数据集与关键信息**：CGGN16 学生模型计算复杂度为教师的 2%，降低计算成本并减少近端语音失真，优于同类高效模型（5 pages, accepted to EUSIPCO 2026）。

### ⭐ 评分：6/10
首次把知识蒸馏用于 AEC，2% 计算量下维持并改善近端语音质量，工程压缩价值明确；但技术上是成熟 KD 技术在新任务上的迁移，创新幅度有限。

---

## [3] Combining Self-Embedding Audio Watermarking with Ultra-Low-Bitrate Neural Codecs

**arXiv ID**：2608.25289 | **方向**：语音前端

**作者**：Yigitcan Özer, Xin Wang, Zhe Zhang, Junichi Yamagishi

**机构**：情报信息研究所（National Institute of Informatics）

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25289 | **PDF**：https://arxiv.org/pdf/2608.25289 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文进一步将自嵌入音频水印与超低比特率神经编解码器结合，实现无训练的音频操纵检测与定位，并支持对被操纵区域的恢复。研究发现神经编解码器的选择是影响整体性能的主导因素，为深伪取证与水印联合方案提供了关键设计指导。

### 📊 实验结果
**数据集与关键信息**：自嵌入水印与超低比特率神经编解码器结合实现无训练操纵检测、定位与恢复；神经编解码器选择是性能主导因素（6 pages; submitted to WIFS 2026）。

### ⭐ 评分：6/10
与同组 2608.25285 互补，明确揭示编解码器选择的主导影响，对系统设计有直接指导意义；为延伸性工作，前瞻实验为主，具体指标依赖 AI 总结。

---

## [4] Acoustic Echo Control Based on Sound Object Identification for Suppressing Howling Caused by Complicated Acoustic Paths

**arXiv ID**：2608.25413 | **方向**：语音前端

**作者**：Osamu Hoshuyama

**机构**：暂无公开机构信息

**发布日期**：2026-08-27 | **论文**：https://arxiv.org/abs/2608.25413 | **PDF**：https://arxiv.org/pdf/2608.25413 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
多免提终端会议环境中，复杂声学路径会导致传统 AEC 失效并引发啸叫。本文提出基于声音对象识别的声学回声控制方法，采用默认静音、仅放行非重复声音的策略抑制啸叫，通过声音对象识别区分自身环境声音与远端重放声音。仿真验证了其啸叫抑制效果以及与语音质量之间的权衡。

### 📊 实验结果
**数据集与关键信息**：基于声音对象识别的回声控制抑制复杂路径啸叫，仿真验证效果及与语音质量的权衡（5 pages, 3 figures; Submitted to IEEE Signal Processing Letters）。

### ⭐ 评分：5/10
问题场景特殊（多终端复杂声路啸叫），声音对象识别加默认静音策略思路朴素直接；仅仿真验证、方法深度有限，属短文级工作。

---

*Generated on 2026-08-28 (补录)*