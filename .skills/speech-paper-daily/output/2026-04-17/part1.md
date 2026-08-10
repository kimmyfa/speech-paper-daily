# 2026-04-17 语音论文速递

**共收录**: 6 篇 | **语音大模型**: 3 篇 | **语音前端**: 3 篇

> 今日 arXiv 语音相关论文共命中 6 篇。
> 以下是按评分排序的结果。

---

## 🎙️ 语音前端

## [1] SpeakerRPL v2: Robust Open-set Speaker Identification through Enhanced Few-shot Foundation Tuning and Model Fusion

**arXiv ID**: 2604.13605
**方向**: 语音前端
**作者**: Zhiyong Chen, Shuhang Wu, Yingjie Duan, Xinkang Xu, Xinhui Hu
**机构**: 中国研究机构
**发布日期**: 2026-04-15
**论文链接**: https://arxiv.org/abs/2604.13605
**PDF 链接**: https://arxiv.org/pdf/2604.13605.pdf
**代码链接**: https://github.com/zhiyongchenGREAT/Few-shot-Robust-Speaker-TTS/tree/v2.1
**Demo 链接**: 暂无

### 📌 简介
本文提出了一种基于预训练说话人基础模型的开放集说话人识别改进方法。在之前SpeakerRPL框架基础上，引入LogitNorm与自适应锚点学习来增强目标说话人表征约束，并提出模型融合策略稳定Few-shot训练过程。该方法在VoxCeleb等数据集上表现优异，将EER从1.28%降至0.09%，相对改进约93%。

### 🔧 技术方案

**模型架构**：基于预训练说话人基础模型（Eres2netv2/CAM++），采用轻量级MLP适配器进行Few-shot调优。引入反向点（Reciprocal Points）和中心点（Center Points）建模说话人嵌入空间。

**核心创新**：
1. 将LogitNorm与反向点学习结合，增强开放集学习目标
2. 引入自适应锚点（Adaptive Anchors），为未知说话人提供灵活表征空间
3. 提出基于特征值方差分析（RP/CP similarity matrix eigenvalue variance）的模型选择策略，用于融合候选模型筛选

**训练策略**：
- 使用TTS合成数据增强目标说话人和未知说话人
- 融合策略：训练30个候选模型，基于特征值方差筛选最优候选进行分数级融合
- 损失函数：L_LogitNorm + L_RPL

### 📊 实验结果
**数据集**：VoxCeleb2、3D-Speaker、ESD、Vox1-O*（新构建测试集）
**主要指标**：
- Vox1-O* EER: 1.28% → 0.09%（相对改进93%）
- VoxCeleb2 EER: 0.44%，minDCF: 0.03，OSCR: 98.69%
- 3D-Speaker EER: 0.36%，OSCR: 98.86%
- ESD EER: 0.61%，OSCR: 96.63%

**是否开源**：代码已开源

### ⭐ 评分：9/10
**理由**：创新性高（LogitNorm+RPL+Adaptive Anchor融合设计）、实验充分（多数据集验证）、结果显著（EER相对改进93%）、实用价值高（Few-shot高效调优）

---

## [2] ProSDD: Learning Prosodic Representations for Speech Deepfake Detection against Expressive and Emotional Attacks

**arXiv ID**: 2604.13229
**方向**: 语音前端
**作者**: Aurosweta Mahapatra, Ismail Rasim Ulgen, Kong Aik Lee, Nicholas Andrews, Berrak Sisman
**机构**: Johns Hopkins University, Hong Kong Polytechnic University
**发布日期**: 2026-04-14
**论文链接**: https://arxiv.org/abs/2604.13229
**PDF 链接**: https://arxiv.org/pdf/2604.13229.pdf
**代码链接**: https://prosdd.github.io/ProSDD_website/
**Demo 链接**: 暂无

### 📌 简介
本文提出ProSDD，一个两阶段语音深度伪造检测框架。Stage I仅使用真实语音学习说话人条件化的韵律表征（基于pitch、voice activity、energy），Stage II将韵律监督作为辅助任务与伪造分类联合优化。该方法在ASVspoof 2024上将EER从39.62%降至7.38%，在EmoFake/EmoSpoof-TTS上实现约50%相对改进。

### 🔧 技术方案

**模型架构**：基于XLS-R SSL backbone，采用两阶段训练框架：
- Stage I：仅使用真实语音，通过supervised masked prediction学习说话人条件化韵律表征
- Stage II：联合优化伪造分类与韵律masked prediction（辅助任务）

**核心创新**：
1. 韵律驱动表征学习：构建说话人嵌入（ECAPA-TDNN 192维）+ 帧级韵律嵌入（pitch/VAD/energy 256维）的联合目标
2. 说话人条件化masked prediction：使用InfoNCE损失区分正确/错误的speaker-prosody配对（intra-speaker和inter-speaker negatives）
3. Two-pass训练策略：每步包含masked pass（韵律监督）和classification pass（伪造检测）

**训练策略**：
- Stage I：span masking (length=8, prob=0.25), temperature τ=0.07
- Stage II：masking prob=0.15, τ=0.1, joint loss α=1, β=0.2→0.05
- 辅助任务权重逐渐降低，使韵律监督转为regularizer

### 📊 实验结果
**数据集**：ASVspoof 2019/2021/2024 LA、EmoFake、EmoSpoof-TTS
**主要指标（2019-trained）**：
- ASVspoof 2019: 0.42% EER
- ASVspoof 2024: 16.14% EER（vs baseline 25.43%）
- EmoFake: 3.70% EER（vs baseline 8.84%）
- EmoSpoof-TTS: 9.54% EER（vs baseline 18.92%）

**主要指标（2024-trained）**：
- ASVspoof 2024: 7.38% EER（vs baseline 39.62%，相对改进81%）
- EmoFake: 25.06% EER
- EmoSpoof-TTS: 11.96% EER

**是否开源**：代码已开源

### ⭐ 评分：9/10
**理由**：创新性高（韵律表征+SSL融合设计）、实验非常充分（多数据集、跨攻击类型验证）、结果显著（ASVspoof 2024 EER从39.62%→7.38%）、实用价值高（解决情感伪造检测难题）

---

## [3] Classical Machine Learning Baselines for Deepfake Audio Detection on the Fake-or-Real Dataset

**arXiv ID**: 2604.13400
**方向**: 语音前端
**作者**: Faheem Ahmad, Ajan Ahmed, Masudul Imtiaz
**机构**: 未明确
**发布日期**: 2026-04-15
**论文链接**: https://arxiv.org/abs/2604.13400
**PDF 链接**: https://arxiv.org/pdf/2604.13400.pdf
**代码链接**: 暂无
**Demo 链接**: 暂无

### 📌 简介
本文为深度伪造音频检测提供可解释的经典机器学习基线。从Fake-or-Real (FoR)数据集提取韵律、语音质量和谱特征，训练多种分类器（LR、LDA、QDA、NB、SVM、GMM），在44.1kHz和16kHz采样率下评估。最佳模型RBF SVM达到约93%准确率和7% EER，特征分析揭示pitch variability和谱丰富度（spectral centroid、bandwidth）是关键区分线索。

### 🔧 技术方案

**模型架构**：采用经典机器学习分类器：Logistic Regression、LDA、QDA、Gaussian Naive Bayes、SVM（RBF kernel）、GMM

**核心创新**：
1. 可解释性基线：使用ANOVA和相关性热图分析特征差异显著性
2. 多采样率验证：在44.1kHz（高保真）和16kHz（电话质量）下评估
3. 统计显著性检验：McNemar测试验证模型间差异

**训练策略**：
- 特征提取：prosodic features、voice-quality features、spectral features
- 评估指标：Accuracy、ROC-AUC、EER、DET curves

### 📊 实验结果
**数据集**：Fake-or-Real (FoR) dataset
**主要指标**：
- RBF SVM: ~93% test accuracy, ~7% EER（两种采样率）
- Linear models: ~75% accuracy
- 关键特征：pitch variability、spectral centroid、bandwidth

**是否开源**：暂无代码

### ⭐ 评分：5/10
**理由**：创新性一般（经典ML基线）、实验较充分（多分类器对比）、实用价值中等（可解释性有参考价值）