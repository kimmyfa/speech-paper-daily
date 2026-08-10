# 2026-08-05 语音论文速递

**共收录**: 2 篇 | **TTS**: 1 篇 | **语音编码**: 1 篇

> 今日 arXiv 语音相关论文共命中 2 篇。
> 以下是按评分排序的结果。

---

## 🤖 TTS

---

## [1] GROW: Group-Relative Advantage-Weighted On-Policy Reinforcement Learning of Autoregressive-Diffusion Text-to-Speech Model

**arXiv ID** 2608.03215 | **方向** TTS

**作者**：Guanrou Yang, Tian Tan, Qian Chen, Ziyang Ma, Yakun Song, Zhikang Niu, Qi Chen, Wenming Tu, Haitao Li, Shan Yang, Xie Chen

**机构**：Shanghai Jiao Tong University, Shanghai Innovation Institute, Tencent, Zhejiang University

**发布日期**：2026-08-05 | **论文** https://arxiv.org/abs/2608.03215 | **PDF** https://arxiv.org/pdf/2608.03215.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
流匹配文本转语音的强化学习因确定性ODE采样而复杂化：轨迹级策略梯度方法通常将ODE转换为SDE并跟踪每步似然比，比离散token LM或NAR扩散模型的对齐引入更多开销和成本。本文提出GROW，一种组相对优势加权on-policy RL方法，直接在标准流匹配目标上运作。

### 🔧 技术方案

**模型架构**：流匹配TTS模型 + on-policy RL优化。

**核心创新**：1）群组相对优势加权：对每个prompt采样一组on-policy utterances，在组内标准化可懂度和说话人相似度奖励；2）Wasserstein-2速度惩罚：将更新后的模型锚定到冻结的预训练参考模型；3）组均值奖励基线：将奖励加权转化为优势加权；4）零均值符号优势：保留有效的组内信用分配。

**训练策略**：两阶段训练：先进行ASR监督微调建立稳健的自回归识别器，然后通过GROW进行强化学习优化。

### 📊 实验结果
**数据集**：LibriSpeech, Seed-TTS EN/ZH

**主要指标**：
- 平均WER：从2.016降至1.558
- 说话人相似度：从0.676提升至0.715
- UTMOS：保持不变

**是否开源**：暂无

### ⭐ 评分：8/10
首个针对流匹配TTS的on-policy RL方法，解决了该领域的关键训练问题。方法创新性强，实验效果显著。

---

## 🔊 语音编码

---

## [2] MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation

**arXiv ID** 2608.03021 | **方向** 语音编码

**作者**：Yizhong Geng, Wenxin Fu, Kecan Mao, Qifei Li, Yingming Gao, Ruimin Wang, Chunfeng Wang, Hao Li, Ya Li, Wei Chen

**机构**：Beijing University of Posts and Telecommunications, Li Auto

**发布日期**：2026-08-05 | **论文** https://arxiv.org/abs/2608.03021 | **PDF** https://arxiv.org/pdf/2608.03021.pdf | **代码** 暂无 | **Demo** https://anonymous.4open.science/

### 📌 简介
神经音频编解码器是LLM音频生成的基础tokenizer。虽然语义先验广泛用于增强语言可懂度，但显式声学先验的整合仍缺乏探索，限制了频率敏感领域的合成保真度。MeloCodec是一个有效整合旋律先验——歌唱的关键声学信息——的新框架。

### 🔧 技术方案

**模型架构**：Tokenize-then-Fuse范式 + 两阶段训练策略。

**核心创新**：1）Tokenize-then-Fuse范式：预训练独立的离散旋律分支来锁定结构，再进行特征融合，解决直接融合导致的优化不稳定问题；2）两阶段训练策略：防止码本坍塌，确保稳定收敛；3）旋律先验整合：将关键的旋律信息（音高、节奏）融入音频编码器。

**训练策略**：两阶段：旋律分支预训练 + 融合微调。

### 📊 实验结果
**数据集**：内部歌唱数据集

**主要指标**：
- 歌唱声音表示优于基线
- 提升音高一致性
- 支持可控的音高操控
- 最小化音色退化

**是否开源**：音频样本已公开

### ⭐ 评分：8/10
首个将旋律先验显式整合到神经音频编码器的工作，对LLM音频生成有重要意义。方法创新，针对歌唱这一特定场景有独特优化。
