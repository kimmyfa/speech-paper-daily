# 2026-08-05 语音论文速递

**共收录**: 2 篇 | **语音大模型**: 1 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 2 篇。

---

## 语音大模型

---

## [1] GROW: Group-Relative Advantage-Weighted On-Policy RL of Autoregressive-Diffusion TTS

**arXiv ID**: 2608.03215 | **方向**: 语音大模型

**作者**: Guanrou Yang, Tian Tan, Qian Chen, Ziyang Ma, Yakun Song, Zhikang Niu, Qi Chen, Wenming Tu, Haitao Li, Shan Yang, Xie Chen

**机构**: 上海交通大学 (SJTU), 上海创新研究院, 腾讯 (Tencent), 浙江大学 (Zhejiang University)

**发布日期**: 2026-08-05 | **论文**: https://arxiv.org/abs/2608.03215 | **PDF**: https://arxiv.org/pdf/2608.03215.pdf | **代码**: https://github.com/yanghaha0908/GROW | **Demo**: 暂无

### 📌 简介
流匹配TTS的强化学习因确定性ODE采样而复杂化：轨迹级策略梯度方法需将ODE转换为SDE并跟踪每步似然比，引入随机扰动和大量开销。本文提出GROW，一种组相对优势加权的on-policy RL方法，直接在标准流匹配目标上运作。对每个prompt采样一组on-policy utterances，在组内标准化可懂度和说话人相似度奖励，结合Wasserstein-2速度惩罚锚定到预训练参考模型。在DiTAR上实例化，平均WER从2.016降至1.558，说话人相似度从0.676提升至0.715，训练速度比32-NFE DiTAR-GRPO快2.9倍。代码和模型检查点将开源。

### 🔧 技术方案

**问题背景：** 流匹配（Flow Matching）TTS模型（如DiTAR）使用确定性ODE从噪声到数据采样，不涉及随机性。传统RL方法（如策略梯度）需要估计策略的似然比，但确定性ODE的似然比计算需要轨迹级展开，将ODE转换为SDE引入随机扰动，计算开销大且不稳定。GRPO（Group Relative Policy Optimization）虽然不需要隐式奖励模型，但需要每个token的log概率，而流匹配模型在连续空间中的log概率难以直接获得。

**模型架构：** GROW基于DiTAR（自回归-扩散TTS模型）实例化。DiTAR结合自回归声学token预测和扩散模型，自回归部分建模文本-声学对齐，扩散部分建模声学细粒度生成。GROW作为RL微调框架，在DiTAR预训练模型基础上进行on-policy优化。

**核心创新：** (1) 组相对优势加权（Group-Relative Advantage Weighting）：对每个prompt采样一组on-policy utterances，在组内分别标准化可懂度（WER）和说话人相似度奖励，然后组合成统一优势函数。这种方法不需要值函数估计，避免了流匹配模型的似然比计算。(2) 零均值符号优势（Zero-Mean Signed Advantage）：对于强预训练模型，指数正加权可能被奖励无关的自模仿主导，零均值符号优势保留有效的组内信用分配。(3) Wasserstein-2速度惩罚：将更新后的模型的速度场锚定到冻结的预训练参考模型的速度场，防止RL训练中模型偏离预训练能力（如自然度退化）。(4) 组均值奖励基线：将奖励加权转化为优势加权，无需额外的critic网络。

**训练策略：** 两阶段：(1) 预训练阶段：使用标准流匹配目标训练DiTAR模型。(2) GROW RL微调：对每个prompt，采样N个on-policy utterances（10-NFErollout），计算WER（ASR模型）和说话人相似度（说话人验证模型），在组内标准化后计算优势，用优势加权流匹配目标优化模型。使用W2速度惩罚锚定到参考模型。32-NFE评估时保持性能，训练速度比32-NFE GRPO快2.9倍。

### 📊 实验结果
**数据集**: LibriSpeech, Seed-TTS EN/ZH

**主要指标**:
- 平均WER: 从2.016降至1.558（相对降低22.7%）
- 说话人相似度: 从0.676提升至0.715
- UTMOS: 保持不变（未退化）
- 训练效率: 10-NFE rollout + 32-NFE evaluation，比32-NFE DiTAR-GRPO快2.9倍
- 线性优势加权优于指数加权：在强预训练模型上更有效
- 消融实验验证了W2锚定、组均值和符号优势各组件的必要性

**是否开源**: 代码和模型检查点将开源 (github.com/yanghaha0908/GROW)

### ⭐ 评分：9/10
评分理由：首个针对流匹配TTS的on-policy RL方法，巧妙绕过ODE似然比计算的难题。组相对优势加权设计简洁有效，W2速度惩罚防止了RL训练中的能力退化。实验效果显著（WER降低22.7%），训练效率高（2.9倍加速）。代码将开源，实用价值高。对流匹配模型的RL优化有重要推动意义。

---

## 语音前端

---

## [2] MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation

**arXiv ID**: 2608.03021 | **方向**: 语音前端

**作者**: Yizhong Geng, Wenxin Fu, Kecan Mao, Qifei Li, Yingming Gao, Ruimin Wang, Chunfeng Wang, Hao Li, Ya Li, Wei Chen

**机构**: 北京邮电大学 (BUPT), 理想汽车 (Li Auto)

**发布日期**: 2026-08-05 | **论文**: https://arxiv.org/abs/2608.03021 | **PDF**: https://arxiv.org/pdf/2608.03021.pdf | **代码**: 暂无 | **Demo**: https://anonymous.4open.science/api/repo/melocodec_demo-60EC/file/demo.html

### 📌 简介
神经音频编解码器是LLM音频生成的基础tokenizer。现有工作广泛使用语义先验增强语言可懂度，但显式声学先验的整合仍缺乏探索。MeloCodec提出"Tokenize-then-Fuse"范式，预训练独立的离散旋律分支锁定旋律结构（音高、节奏），再进行特征融合，解决直接融合导致的优化不稳定问题。两阶段训练策略防止码本坍塌。在歌唱声音表示上优于基线，提升音高一致性，支持可控音高操控，最小化音色退化。

### 🔧 技术方案

**问题背景：** 神经音频编解码器（如EnCodec、DAC、SoundStream）将音频编码为离散token，作为LLM音频生成（如TTS、音乐生成）的输入。现有工作主要引入语义先验（如HuBERT、WavLM特征）提升可懂度，但显式声学先验（如旋律、音高、节奏）的整合尚未被充分探索。直接融合声学先验可能导致优化不稳定（如码本坍塌、收敛困难），特别是对于歌唱这类对音高敏感的领域。

**模型架构：** MeloCodec采用"Tokenize-then-Fuse"范式：(1) Tokenize分支：独立的离散旋律分支，使用残差向量量化（RVQ）将旋律信息（音高轮廓、节奏结构）编码为离散token序列，预训练时锁定旋律结构。(2) Fuse分支：异构特征融合模块，将旋律token与音频编码器的主干特征融合，通过交叉注意力机制实现信息交互。(3) 整体架构遵循标准encoder-RVQ-decoder结构，但旋律分支作为并行路径提供显式声学先验。

**核心创新：** (1) "Tokenize-then-Fuse"范式：先预训练独立的离散旋律分支锁定结构，再与主分支特征融合，避免直接融合导致的优化不稳定性。这类似于"先训练一个好的初始化，再联合微调"的策略。(2) 两阶段训练策略：第一阶段仅训练旋律分支（冻结主分支），学习离散旋律表示；第二阶段将旋律分支与主分支联合微调，实现特征融合。这种策略有效防止了码本坍塌。(3) 旋律先验的显式建模：首次将旋律（音高、节奏）作为显式离散先验引入神经音频编解码器，而非仅依赖隐式学习。

**训练策略：** 两阶段训练：(1) 旋律分支预训练阶段：训练旋律分支的RVQ码本，优化旋律重建损失（音高一致性、节奏准确性），冻结主编码器。(2) 融合微调阶段：解冻主编码器，联合训练主分支和旋律分支，优化重建损失（Mel频谱L1损失、对抗损失、多尺度STFT损失）和旋律一致性损失。

### 📊 实验结果
**数据集**: 内部歌唱数据集

**主要指标**:
- 重建质量：MeloCodec显著优于基线（EnCodec、DAC），特别是在高音区域
- 音高一致性：PCC（Pearson相关系数）提说明显高于基线
- 可控音高操控：在编码空间中进行音高偏移后，解码器能保持音色一致性
- 音色退化最小化：在MOS评估中，音色自然度接近原始录音
- 消融实验验证了两阶段训练策略和旋律分支的必要性

**是否开源**: 音频样本已公开；代码暂无

### ⭐ 评分：8/10
评分理由：首个将旋律先验显式整合到神经音频编码器的工作，对LLM音频生成（特别是歌唱合成）有重要意义。"Tokenize-then-Fuse"范式解决了直接融合声学先验的优化问题。两阶段训练策略实用有效。但仅在内部数据集上验证，且未在端到端LLM生成任务中测试（如使用MeloCodec token的TTS或歌唱合成）。

---

*Generated on 2026-08-14*