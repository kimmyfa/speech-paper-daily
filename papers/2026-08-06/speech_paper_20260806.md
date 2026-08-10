# 2026-08-06 语音论文速递

**共收录**: 6 篇 | **TTS**: 1 篇 | **语音编码**: 1 篇 | **说话人**: 1 篇 | **其他**: 3 篇

> 今日 arXiv 语音相关论文共命中 6 篇。
> 以下是按评分排序的结果。

---

## 🎯 说话人识别

---

## [1] Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust Speaker Representation Learning

**arXiv ID** 2608.05549 | **方向** 说话人识别

**作者**：Zezhong Jin, Xiaoyu Wang, Zhe Li, Chong-Xin Gan, Zilong Huang, Man-Wai Mak, Kong Aik Lee

**机构**：The Hong Kong Polytechnic University, Baidu Inc., The University of Hong Kong

**发布日期**：2026-08-06 | **论文** https://arxiv.org/abs/2608.05549 | **PDF** https://arxiv.org/pdf/2608.05549.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
残差连接是深度说话人识别模型（如ECAPA-TDNN和ResNet）的基础，但标准恒等映射限制信息流到单一路径，约束了表示能力。本文提出Manifold-Constrained Hyper-Connections (mHC)，将残差路径重新表述为多流演化，其中信息通过双随机矩阵混合。通过使用Sinkhorn-Knopp迭代，mHC通过保留信号强度和特征均值确保能量守恒，从而稳定梯度并缓解复杂网络中的信号退化。在VoxCeleb1上的广泛实验表明，mHC连接在所有架构上一致提升性能。

### 🔧 技术方案

**模型架构**：将标准残差连接替换为mHC，包含：1）多流演化机制；2）双随机矩阵混合；3）Sinkhorn-Knopp迭代用于能量守恒。

**核心创新**：1）将残差连接扩展为多流演化；2）使用Sinkhorn-Knopp确保能量守恒；3）保持恒等映射属性的同时增强信息流动。

**训练策略**：替换ECAPA-TDNN、ResNet-34、Res2Net、E-Res2Net中的标准残差连接进行训练。

### 📊 实验结果
**数据集**：VoxCeleb1

**主要指标**：
- 所有架构一致提升性能
- 梯度更稳定
- 信号退化减轻

**是否开源**：暂无

### ⭐ 评分：8/10
INTERSPEECH 2026接收。从残差连接到超连接的范式转变，对说话人表示学习有实际提升。

---

## 🔊 语音编码

---

## [2] LILAC: An Idempotent Neural Speech Codec

**arXiv ID** 2608.05727 | **方向** 语音编码

**作者**：June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon

**机构**：Seoul National University

**发布日期**：2026-08-06 | **论文** https://arxiv.org/abs/2608.05727 | **PDF** https://arxiv.org/pdf/2608.05727.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
神经音频编解码器广泛用于语音生成和编辑，但现有的神经音频编解码器不是幂等的：在测试的12个基线系统中，每种配置在单次解码-重编码过程中平均重写至少15%的token。这对将神经音频编解码器用作token接口的流水线存在问题，因为重编码解码后的输出会发生token变化。本文提出LILAC，一个在9.375Hz和0.75 kbit/s下工作的全卷积24kHz语音编解码器，通过构造保证编解码幂等性。

### 🔧 技术方案

**模型架构**：全卷积神经语音编解码器，24kHz采样率，9.375Hz latent频率，码率0.75 kbit/s。采用有限标量量化（FSQ）进行量化。

**核心创新**：1）引入FSQ保证编解码幂等性，重编码解码后的音频返回完全相同的token流；2）从数学上证明编解码器的幂等性保证；3）首次从构造上实现幂等性的神经语音编解码器。

**训练策略**：标准编解码器训练流程，优化重建质量和token一致性。

### 📊 实验结果
**数据集**：LibriSpeech, LibriTTS-R

**主要指标**：
- LibriSpeech：UTMOS 4.14
- LibriTTS-R：UTMOS 4.24
- Token重写率：从15%降至0%
- 码率：0.75 kbit/s

**是否开源**：代码和训练checkpoint将公开

### ⭐ 评分：9/10
解决了一个关键而实际的问题——编解码-重编码循环中的令牌重写。对LLM音频生成流水线有重要意义。

---

## 🤖 其他

---

## [3] Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming

**arXiv ID** 2608.05663 | **方向** 音视频生成

**作者**：Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang

**机构**：Shanghai AI Lab

**发布日期**：2026-08-06 | **论文** https://arxiv.org/abs/2608.05663 | **PDF** https://arxiv.org/pdf/2608.05663.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
实时长形式Avatar音视频生成需要因果、连续合成，同时保持音视频同步和视觉一致性。将预训练的双向模型适配到这一设置面临两个关键挑战：首先，自回归重用生成的块作为上下文会产生暴露偏差，导致错误和视觉漂移累积；其次，全局语音话语不能指示因果生成器在只有有限局部音视频上下文时应该生成哪部分。

### 🔧 技术方案

**模型架构**：Vorch-Streamer后训练框架。

**核心创新**：1）合成80K Avatar片段语料库；2）混合Teacher Forcing和Diffusion Forcing的因果生成器训练；3）DMD蒸馏的长视野Self Forcing；4）外部语言模型预测25Hz语音规划token。

**训练策略**：多阶段训练：因果生成器预训练 + Self Forcing + DMD蒸馏。

### 📊 实验结果
**数据集**：内部Avatar数据集

**主要指标**：
- 27.12 FPS生成速度
- 超过24 FPS实时播放速率
- 保持音唇同步和身份保持

**是否开源**：项目页面将公开

### ⭐ 评分：8/10
首个实时长形式Avatar音视频生成框架，对虚拟数字人应用有重要价值。

---

## [4] KVAE: Family of Tokenizers for Multimodal Generative Models

**arXiv ID** 2608.05798 | **方向** 多模态tokenizer

**作者**：Andrey Shutkin, Denis Parkhomenko, Ivan Kirillov, Kirill Chernyshev, Kirill Malakhov, Ilia Vasiliev, Ilia Trushkin, Valeriya Kobenko, David Chikovani, Alexander Ivanov, Azat Saginbaev, Egor Silvestrov, Ivan Mikheev, Konstantin Zakharov

**机构**：KLEIN

**发布日期**：2026-08-06 | **论文** https://arxiv.org/abs/2608.05798 | **PDF** https://arxiv.org/pdf/2608.05798.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
潜在扩散建模（LDM）使用tokenizer将输入信号映射到压缩表示。这种依赖使tokenizer成为生成过程本身的重要组成部分，因为它影响合成质量、学习速度，并为后续应用奠定基础。本文提出一系列用于音频、图像和视频的KVAE tokenizer，用于后续文本条件生成。

### 🔧 技术方案

**模型架构**：KVAE-Audio：连续全频段48kHz tokenizer，50Hz latent，64通道；KVAE-3D：两个因果视频tokenizer，4x16x16和4x8x8压缩；KVAE-2D：图像模型，8倍压缩，32通道。

**核心创新**：1）统一的多模态tokenizer系列；2）针对重建和生成的多维度优化；3）与Wan-2.2、HunyuanVideo、FLUX等前沿开源tokenizer对标。

**训练策略**：标准VAE训练流程，针对不同模态定制。

### 📊 实验结果
**数据集**：内部评估集

**主要指标**：
- PSNR、LPIPS、PESQ等重建指标
- Frechet Distance、CLAP Score等生成指标
- 与SOTA开源tokenizer相当或更优

**是否开源**：代码将公开

### ⭐ 评分：7/10
提供了一套完整的多模态tokenizer解决方案，对社区有参考价值。

---

## [5] Explicit and Stable Pseudospectral Time-Domain Method for the Föppl-von Kármán Equations

**arXiv ID** 2608.06139 | **方向** 声学模拟

**作者**：Victor Zheleznov, Stefan Bilbao

**机构**：University of Edinburgh, IRCAM, CNRS, Sorbonne Université

**发布日期**：2026-08-06 | **论文** https://arxiv.org/abs/2608.06139 | **PDF** https://arxiv.org/pdf/2608.06139.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
模态合成是模拟乐器动力学的广泛使用技术。在线性情况下，模态分解导致非耦合的阻尼和受迫谐振子系统，可以用标准时间步进方法高效求解。然而，扩展到非线性问题具有挑战性，因为存在模态展开的乘积项。

### 🔧 技术方案

**模型架构**：伪谱方法，时域求解器。

**核心创新**：1）在空域网格上评估乘积项；2）精确计算模态域中的空间导数；3）使用离散正弦和余弦变换施加边界条件；4）标量辅助变量技术实现显式稳定时间积分。

**训练策略**：无需训练，纯数值方法。

### 📊 实验结果
**数据集**：数值实验

**主要指标**：
- 计算成本降低
- 保持精确的频率范围控制
- 声音示例将提供

**是否开源**：将在Forum Acusticum 2026展示

### ⭐ 评分：7/10
对声学模拟领域有贡献，但更偏重于传统信号处理而非深度学习。

---

## [6] Audio-to-Score Transcription using Pre-trained Features, Data Augmentation, and the New SheetSage-A2S Dataset

**arXiv ID** 2608.06165 | **方向** 音乐 transcription

**作者**：Eoin Cummins, Zhongyi Huang, Alexandre D'Hooge, Zhuoro Mo, Yaolong Ju

**机构**：University College Dublin, Guangxi Normal University, Great Bay University, Shenzhen University

**发布日期**：2026-08-06 | **论文** https://arxiv.org/abs/2608.06165 | **PDF** https://arxiv.org/pdf/2608.06165.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
现有的音频到乐谱（A2S）系统主要关注古典音乐，对流行音乐的应用仍然缺乏探索。本文首先提出新的SheetSage-A2S数据集，包含61小时音频和9468个片段的**kern乐谱编码，来源于6066首独特歌曲，是首个促进流行音乐A2S研究的数据集。此外，我们使用数据增强和MuQ（音乐音频预训练特征提取模型）来改进现有A2S方法。

### 🔧 技术方案

**模型架构**：MuQ特征提取 + A2S解码器。

**核心创新**：1）SheetSage-A2S数据集：首个流行音乐A2S数据集；2）数据增强策略；3）MuQ预训练特征提取。

**训练策略**：端到端训练，使用数据增强和预训练特征。

### 📊 实验结果
**数据集**：Quartets收藏（古典音乐）, SheetSage-A2S（流行音乐）

**主要指标**：
- 古典音乐：4.98% SER
- 流行音乐：20.92% SER
- 显著优于现有SOTA（15.3% SER）

**是否开源**：数据集、模型和代码将公开

### ⭐ 评分：8/10
ACM MM 2026接收。首个流行音乐A2S数据集，对音乐信息检索领域有重要贡献。
