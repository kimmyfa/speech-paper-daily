# 2026-04-16 语音论文速递

**共收录** 5 篇 | **语音大模型** 1 篇 | **语音前端** 1 篇 | **语音安全** 3 篇

> 今日 arXiv 语音相关论文共命中 5 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

## [2] Towards Fine-grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt

**arXiv ID** 2604.13715
**方向** 语音大模型
**作者** Yanfeng Shi, Pengfei Cai, Jun Liu, Qing Gu, Nan Jiang, Lirong Dai, Ian McLoughlin, Yan Song
**机构** USTC (中国科学技术大学) + Singapore Institute of Technology
**发布日期** 2026-04-15
**论文链接** https://arxiv.org/abs/2604.13715
**PDF 链接** https://arxiv.org/pdf/2604.13715.pdf
**代码链接** 暂无
**Demo 链接** 暂无

### 📌 简介
当前大型音频-语言模型（LALM）在语义理解上表现优异，但在细粒度时间感知（如推断事件起止时间）上存在瓶颈。本文提出 TimePro-RL 框架，通过音频侧时间提示和强化学习后训练显著提升时间对齐性能，在音频定位、声音事件检测和密集音频描述任务上取得突破。

### 🔧 技术方案

**模型架构**：基于 Qwen2-Audio 和 Qwen2.5-Omni 构建框架。核心设计 Audio-Side Time Prompt (ASTP)，将时间戳编码为嵌入向量并交织到音频特征序列中作为时间坐标。时间戳嵌入采用语义初始化策略，使用对应数字字符串的子词嵌入平均值初始化，训练过程中冻结参数防止语义漂移。

**核心创新**：
- Audio-Side Time Prompt：在输入级别提供时间提示，减少推理难度并缓解幻觉
- 强化学习后训练：采用 Group Relative Policy Optimization (GRPO) 优化时间对齐
- 自适应时间奖励机制：当主奖励（Event-based F1）缺乏区分性时，动态融合辅助奖励（mIoU/METEOR），提升数据效率

**训练策略**：
- SFT 阶段：使用 LoRA 微调（r=8, α=32），训练 3 epoch，学习率 1×10^-5
- RL 阶段：仅 1 epoch，使用 10,200 样本子集，组大小 4，学习率 1×10^-6
- 时间戳 token 扩展：750 个 token，覆盖 0-30 秒，步长 0.04 秒

### 📊 实验结果
数据集：Audio Grounding (FTAR, 61,862 训练样本)、Sound Event Detection (DESED, 15,041 训练样本)、Dense Audio Captioning (FTAR, 92,443 训练样本)

主要指标：
- Audio Grounding：Qwen2.5-Omni R@0.9 从 34.1 提升至 39.8，mIoU 从 69.9 提升至 74.4
- Sound Event Detection：Eb-F1 从 48.9 提升至 57.6
- Dense Audio Captioning：METEOR 从 31.3 提升至 33.9，Eb-F1 从 35.2 提升至 40.7

消融实验验证：
- 随机初始化时间戳嵌入导致性能回退（SED Eb-F1 下降 2.9）
- 语义初始化策略带来 AG R@0.9 提升 1.7
- RL 训练使 AG R@0.9 从 35.8 提升至 39.8

是否开源：暂无代码和 demo

### ⭐ 评分 8/10
理由：创新性较强，提出了 Audio-Side Time Prompt 和强化学习后训练的组合方案。实验充分，在三个任务上验证有效性，高精度指标（R@0.9）显著提升。已提交 Interspeech 2026，有望被顶会接收。时间戳嵌入的语义初始化策略和自适应奖励机制是亮点。

---

## 🎙️ 语音前端

## [4] Few-Shot and Pseudo-Label Guided Speech Quality Evaluation with Large Language Models

**arXiv ID** 2604.13528
**方向** 语音前端
**作者** Ryandhimas E. Zezario, Dyah A. M. G. Wisnu, Szu-Wei Fu, Sabato Marco Siniscalchi, Hsin-Min Wang, Yu Tsao
**机构** 未明确（已被 IEEE ICASSP 2026 接收）
**发布日期** 2026-04-15
**论文链接** https://arxiv.org/abs/2604.13528
**PDF 链接** https://arxiv.org/pdf/2604.13528.pdf
**代码链接** 暂无
**Demo 链接** 暂无

### 📌 简介
语音质量评估通常需要大量标注数据训练深度学习模型。本文提出 GatherMOS 框架，将大型语言模型作为元评估器，聚合轻量级声学描述器和伪标签信号来推断感知 MOS，在零样本和少样本设置下超越现有方法。

### 🔧 技术方案

**模型架构**：GatherMOS 使用 GPT-5 作为核心推理引擎，将声学特征和伪标签序列化为结构化文本提示。输入包括：
- 轻量级声学描述器：RMS（能量）、ZCR（噪声程度）、clipping ratio、duration、13 维 MFCC、mel-spectrogram 统计
- 伪标签：DNSMOS（1-5 分）和 VQScore（0-1 分）

**核心创新**：
- LLM 作为元评估器：利用推理能力整合异构信号，而非依赖粗粒度音频信息或文本代理
- Zero-shot GatherMOS：仅使用基本声学特征 + 伪标签
- Few-shot GatherMOS：引入代表性样本提供上下文指导（低、中、高 MOS 各一个）

**训练策略**：
- 不训练 LLM 参数，仅通过 in-context learning 提供指导
- GatherMOS-ZS* 版本增加 MFCC 和 spectrogram 特征，进一步提升性能
- 测试时使用 minibatch（10 样本）评估，批次间重置 LLM session 防止交叉影响

### 📊 实验结果
数据集：VoiceBank-DEMAND（200 utterances，包括干净语音、4 种噪声类型下的 0 dB 嘈杂语音、5 种增强系统输出）

主要指标（SRCC 和 LCC）：
- Few-shot subset：GatherMOS-FS SRCC 0.8473，超越 DNSMOS (0.5231)、VQScore (0.6359)
- Full test set：GatherMOS-ZS* LCC 0.6495，SRCC 0.6069，超越 CNN-BLSTM (0.3192)、MOS-SSL (0.4888)
- Scatter plot 分析：GatherMOS-ZS* 预测分布更广，与 ground truth 对齐更好

关键发现：
- Few-shot 样本与测试域匹配时带来大幅增益，不匹配时可能降低性能
- Richer acoustic features（MFCC + spectrogram）持续提升性能

是否开源：暂无代码和 demo

### ⭐ 评分 7/10
理由：创新性不错，将 LLM 作为元评估器的思路新颖。实验充分，已被 ICASSP 2026 接收。GatherMOS-ZS* 在 limited labeled-data 条件下超越训练模型，实用价值高。但在 few-shot 设置下存在 domain bias 问题，整体属于增量式创新。

---

## 🔒 语音安全

## [1] ProSDD: Learning Prosodic Representations for Speech Deepfake Detection against Expressive and Emotional Attacks

**arXiv ID** 2604.13229
**方向** 语音安全
**作者** Aurosweta Mahapatra, Ismail Rasim Ulgen, Kong Aik Lee, Nicholas Andrews, Berrak Sisman
**机构** Johns Hopkins University + Hong Kong Polytechnic University
**发布日期** 2026-04-14
**论文链接** https://arxiv.org/abs/2604.13229
**PDF 链接** https://arxiv.org/pdf/2604.13229.pdf
**代码链接** https://prosdd.github.io/ProSDD_website/
**Demo 链接** 暂无

### 📌 简介
现有语音深度伪造检测系统在情感和表达性语音攻击上泛化能力不足。本文提出 ProSDD 两阶段框架，通过监督掩码预测学习说话人条件的韵律变异性（基于 pitch、voice activity、energy），使模型内化自然语音的韵律结构，显著提升在标准 benchmark 和情感数据集上的检测性能。

### 🔧 技术方案

**模型架构**：基于 XLS-R SSL backbone 构建。两阶段训练框架：
- Stage I：仅使用真实语音，通过监督掩码预测学习韵律表示
- Stage II：联合优化韵律预测和欺骗分类

**核心创新**：
- 说话人条件韵律目标：组合 speaker embedding（ECAPA-TDNN, 192 维）和 frame-level prosodic embedding（256 维，集成 pitch、voice activity、energy）
- 监督掩码预测目标：使用 InfoNCE 损失区分正确和错误的 speaker-prosody pairs，采用 intra-speaker 和 inter-speaker negatives
- 两阶段策略：Stage I 学习自然韵律变异性，Stage II 保持韵律监督作为辅助任务

**训练策略**：
- Stage I：span masking（长度 8，掩码概率 0.25，温度 τ=0.07），仅真实语音
- Stage II：掩码概率降至 0.15，温度 τ=0.1，联合损失 α=1、β=0.2（前 4 epoch）→ 0.05
- Lightweight classifier：线性层 + dropout + ReLU + 线性层，避免复杂架构

### 📊 实验结果
数据集：LibriSpeech (Stage I)、ASVspoof 2019/2024 (Stage II)、ASVspoof 2019/2021/2024 (测试)、EmoFake、EmoSpoof-TTS (测试)

主要指标（EER %）：
- ASVspoof 2019 trained：ProSDD 在 ASVspoof 2019 达到 0.42%（超越 XLSR-SLS 0.56%），ASVspoof 2024 EER 从 25.43% 降至 16.14%，EmoFake 从 8.84% 降至 3.70%，EmoSpoof-TTS 从 18.92% 降至 9.54%
- ASVspoof 2024 trained：ProSDD 在 ASVspoof 2024 EER 从 39.62% 降至 7.38%，EmoFake 25.06%，EmoSpoof-TTS 11.96%

消融实验：
- 移除 MP 和 Stage I：ASVspoof 2019 EER 从 0.42% 升至 6.78%
- 仅保留 Stage II MP：ASVspoof 2019 EER 5.14%，泛化性不足
- 完整 ProSDD：最稳定的跨数据集性能

是否开源：代码已开源（https://prosdd.github.io/ProSDD_website/）

### ⭐ 评分 9/10
理由：创新性强，从人类感知角度出发建模韵律变异性，提出新颖的两阶段框架。实验非常充分，在多个 benchmark 上取得突破性进展（ASVspoof 2024 EER 从 39.62% 降至 7.38%，相对减少 81%）。EmoFake 和 EmoSpoof-TTS 上相对减少约 50%。已提交 Interspeech 2026，顶会水准，有实质贡献。

---

## [3] SpeakerRPL v2: Robust Open-set Speaker Identification through Enhanced Few-shot Foundation Tuning and Model Fusion

**arXiv ID** 2604.13605
**方向** 语音安全
**作者** Zhiyong Chen, Shuhang Wu, Yingjie Duan, Xinkang Xu, Xinhui Hu
**机构** 未明确
**发布日期** 2026-04-15
**论文链接** https://arxiv.org/abs/2604.13605
**PDF 链接** https://arxiv.org/pdf/2604.13605.pdf
**代码链接** https://github.com/zhiyongchenGREAT/Few-shot-Robust-Speaker-TTS/tree/v2.1
**Demo 链接** 暂无

### 📌 简介
开放集说话人识别需要在识别已注册目标说话人的同时可靠检测未知说话人。本文改进 SpeakerRPL V1 框架，集成 LogitNorm + 互惠点学习 + 自适应锚点学习提升说话人表示，并提出模型融合策略和选择机制减少少样本调优的随机性，在 Vox1-O* 上 EER 从 1.28% 降至 0.09%（相对减少 93%）。

### 🔧 技术方案

**模型架构**：基于预训练说话人基座模型构建。核心设计：
- Reciprocal Points Loss (LRPL)：结合判别性和 margin 约束
- LogitNorm：归一化 logits 稳定开放集分类
- 自适应锚点：扩展类别集合 K = Ktarget ∪ Ksynthetic ∪ Kadaptive，仅扩展 RP 而非 CP

**核心创新**：
- 改进的开放集学习目标：联合优化 LRPL 和 LLogitNorm
- 自适应锚点学习：动态学习 reciprocal points，无需显式注册数据，为未知说话人提供更灵活的表示空间
- 模型融合策略：score-level averaging 多个 adapter 模型
- 模型选择策略：基于 CP 和 RP 的相似矩阵特征值方差选择最佳候选模型

**训练策略**：
- 少样本调优：轻量级 MLP adapter，几分钟完成 GPU 训练
- 目标说话人增强：使用 GPT-SoVITSv2 生成合成数据
- 未知说话人增强：从 LibriTTS 和 AiShell 选择音色
- 融合训练：30 个 adapter 候选，丢弃底部 33% 模型（基于 RP 和 CP 特征值方差），保留交集

### 📊 实验结果
数据集：VoxCeleb2（118 speakers, 10 splits）、3D-Speaker（73 speakers, 10 splits）、ESD（20 speakers, 5 splits）、Vox1-O*（40 target speakers）

主要指标（VoxCeleb2, 5 splits）：
- SpeakerRPL V2 (w/ fusion)：EER 0.44%，minDCF 0.03%，OSCR 98.69%，ACC 99.47%
- 对比 Direct Enrollment：EER 3.74%，OSCR 97.31%
- 对比 Softmax：EER 0.69%，OSCR 97.47%

Vox1-O*（40 target speakers）：
- Close-set：EER 从 1.28% 降至 0.09%（相对减少 93%）
- Open-set：EER 从 1.72% 降至 0.24%

消融实验：
- Adaptive anchor 数量增加提升性能（10→50 anchors，EER 从 0.60% 降至 0.42%）
- 模型融合 + 选择策略优于 naive fusion（OSCR 从 98.60% 提升至 98.69%）
- 特征值方差与 OSCR 强相关，验证选择策略有效性

是否开源：代码已开源（https://github.com/zhiyongchenGREAT/Few-shot-Robust-Speaker-TTS/tree/v2.1）

### ⭐ 评分 8/10
理由：创新性强，提出多项改进（LogitNorm集成、自适应锚点、模型融合 + 选择）。实验充分，在多个数据集上验证，EER 从 1.28% 降至 0.09% 是显著突破。已被 ICASSP 2026 接收。模型融合策略有效解决少样本调优的随机性问题，有实质贡献。

---

## [5] Classical Machine Learning Baselines for Deepfake Audio Detection on the Fake-or-Real Dataset

**arXiv ID** 2604.13400
**方向** 语音安全
**作者** Faheem Ahmad, Ajan Ahmed, Masudul Imtiaz
**机构** 未明确
**发布日期** 2026-04-15
**论文链接** https://arxiv.org/abs/2604.13400
**PDF 链接** https://arxiv.org/pdf/2604.13400.pdf
**代码链接** 暂无
**Demo 链接** 暂无

### 📌 简介
深度学习推动了高度逼真的合成语音，引发欺诈、冒充和虚假信息担忧。尽管神经检测器进展迅速，仍需要透明基线揭示可靠分离真实和合成语音的声学线索。本文提出可解释的经典机器学习基线，提取韵律、语音质量和频谱特征，统计分析识别关键判别特征，最佳模型（RBF SVM）在两种采样率下均达到 ~93% 准确率和 ~7% EER。

### 🔧 技术方案

**模型架构**：使用多种经典分类器：
- Logistic Regression、LDA、QDA、Gaussian Naive Bayes
- SVM（RBF kernel）
- GMM

**核心创新**：
- 可解释性：通过统计分析（ANOVA、correlation heatmaps）识别显著差异特征
- 多维度特征：韵律（pitch variability）、语音质量（spectral centroid、bandwidth）、频谱（spectral richness）
- 两种采样率对比：44.1 kHz（高保真）和 16 kHz（电话质量）

**训练策略**：
- 特征提取：从 2 秒片段提取韵律、语音质量、频谱特征
- 统计分析：ANOVA 确认特征显著性，correlation heatmaps 可视化特征关系
- McNemar's tests：确认模型间统计显著性差异

### 📊 实验结果
数据集：Fake-or-Real (FoR) dataset

主要指标：
- 最佳模型（RBF SVM）：~93% 测试准确率，~7% EER（两种采样率）
- 线性模型：~75% 准确率

关键发现：
- Pitch variability 和 spectral richness（spectral centroid、bandwidth）是关键判别线索
- McNemar's tests 确认模型间统计显著性差异
- 可解释性分析揭示了可靠分离真实和合成语音的声学特征

是否开源：暂无代码和 demo

### ⭐ 评分 5/10
理由：方法相对传统（经典机器学习），创新性有限。但提供了有价值的可解释基线，实验较充分（两种采样率、多种分类器对比、统计分析）。已被 The 35th IEEE Microelectronics Design and Test Symposium 接收（Oral Presentation）。属于增量工作，有参考价值。

---

## 📋 其他论文（快速浏览）

无（论文总数 5 篇，全部已完整展示）

---

## 总结

今日语音领域共发布 5 篇相关论文，涵盖多个方向：

**最推荐** ProSDD 提出了创新的两阶段框架，通过监督掩码预测学习说话人条件韵律变异性，在 ASVspoof 2024 上 EER 从 39.62% 降至 7.38%，EmoFake 和 EmoSpoof-TTS 上相对减少约 50%，突破性进展（9 分）。

**值得关注** TimePro-RL 和 SpeakerRPL v2 获得高分（8 分），分别在音频大语言模型时间感知和开放集说话人识别方向上有创新性贡献。TimePro-RL 的 Audio-Side Time Prompt 和 RL 后训练组合有效提升细粒度时间感知；SpeakerRPL v2 的 LogitNorm 集成和模型融合策略解决少样本调优随机性问题，EER 相对减少 93%。

---

生成时间 2026-04-16 10:14 (Asia/Shanghai)

数据来源 arXiv cs.SD & eess.AS

---

*由开心果 🍀 自动生成 · 数据来源：arXiv*