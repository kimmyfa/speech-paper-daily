# 2026-08-07 语音论文速递

**共收录**: 4 篇 | **TTS**: 1 篇 | **语音编码**: 1 篇 | **说话人**: 1 篇 | **语音检测**: 1 篇

> 今日 arXiv 语音相关论文共命中 4 篇。
> 以下是按评分排序的结果。

---

## 🤖 TTS

---

## [1] Pixel-TTS: Image based Text Rendering for Robust Text-to-Speech

**arXiv ID** 2606.14750 | **方向** TTS

**作者**：Adarsh Arigala, Arjun Gangwar, Srinivasan Umesh, Yova Kostedjhieva

**机构**：IIT Madras, MBZUAI

**发布日期**：2026-07-16 | **论文** https://arxiv.org/abs/2606.14750 | **PDF** https://arxiv.org/pdf/2606.14750.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Pixel-TTS是首个视觉 grounded 的语音合成框架，它将文本渲染为图像并利用2D卷积层生成嵌入，替代传统的字符级嵌入。近期基于像素的文本建模进展表明，将文本表示为图像可以使模型利用视觉线索进行语言理解。这种方法允许结构相似的字符（即使Unicode编码不同）产生相似的嵌入，从而受益于跨语言和零样本场景。传统文本方法独立处理每个字符，限制了未见字符的泛化，并在跨语言适配时需要扩展嵌入矩阵。

### 🔧 技术方案

**模型架构**：Pixel-TTS建立在ADMA架构之上，采用双模态对齐加速收敛。使用文本渲染器将文本转换为图像，然后通过2D卷积层投影生成嵌入。模型采用字符级Tokenizer和音频Codec处理语音信号。

**核心创新**：1）将文本渲染为图像，利用2D卷积提取视觉特征；2）消除跨语言微调时的嵌入矩阵扩展需求；3）改善对未见字符和正字法变化的鲁棒性。

**训练策略**：基于ADMA进行双模态对齐，使用文本-音频对进行训练。

### 📊 实验结果
**数据集**：LibriSpeech, LibriTTS-R, German Common Voice

**主要指标**：
- 零样本跨语言泛化：具有竞争力
- 收敛速度：比传统文本方法更快
- 对正字法噪声（Unicode和l33tspeak）的鲁棒性：优于文本方法

**是否开源**：暂无

### ⭐ 评分：7/10
将视觉信息引入TTS是一个有价值的探索方向，对解决跨语言泛化和未见字符问题有一定帮助。但该工作的创新幅度相对有限，更多是已有方法的组合应用。

---

## 🔊 语音编码

---

## [2] LILAC: An Idempotent Neural Speech Codec

**arXiv ID** 2608.05727 | **方向** 语音编码

**作者**：June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon

**机构**：Seoul National University

**发布日期**：2026-08-07 | **论文** https://arxiv.org/abs/2608.05727 | **PDF** https://arxiv.org/pdf/2608.05727.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
神经音频编解码器广泛用于语音生成和编辑，但现有的神经音频编解码器不是幂等的：在测试的12个基线系统中，每种配置在单次解码-重编码过程中平均重写至少15%的token。这对将神经音频编解码器用作token接口的流水线存在问题，因为重编码解码后的输出会发生token变化。本文提出LILAC，一个在9.375Hz和0.75 kbit/s下工作的全卷积24kHz语音编解码器，通过构造保证编解码幂等性：重编码任何有效token流的解码音频都返回完全相同的token流。LILAC在保持竞争力的质量的同时达到UTMOS 4.14（LibriSpeech）和4.24（LibriTTS-R），与SOTA sub-1 kbit/s神经音频编解码器相当。

### 🔧 技术方案

**模型架构**：全卷积神经语音编解码器，24kHz采样率，9.375Hz latent频率，码率0.75 kbit/s。采用有限标量量化（Finite Scalar Quantization, FSQ）进行量化。

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
解决了一个关键而实际的问题——编解码-重编码循环中的令牌重写。对LLM音频生成流水线有重要意义，因为可以在不损失质量的情况下进行多轮编解码。

---

## 🎯 说话人识别

---

## [3] Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust Speaker Representation Learning

**arXiv ID** 2608.05549 | **方向** 说话人识别

**作者**：Zezhong Jin, Xiaoyu Wang, Zhe Li, Chong-Xin Gan, Zilong Huang, Man-Wai Mak, Kong Aik Lee

**机构**：The Hong Kong Polytechnic University, Baidu Inc., The University of Hong Kong

**发布日期**：2026-08-07 | **论文** https://arxiv.org/abs/2608.05549 | **PDF** https://arxiv.org/pdf/2608.05549.pdf | **代码** 暂无 | **Demo** 暂无

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
从残差连接到超连接的范式转变，对说话人表示学习有实际提升。INTERSPEECH 2026接收表明其得到了学术认可。

---

## 🛡️ 语音检测

---

## [4] AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks

**arXiv ID** 2608.05507 | **方向** 语音检测

**作者**：Aurosweta Mahapatra, Xiutian Zhao, Shreeram Suresh Chandra, Zihan Zhang, Zongyang Du, Ismail Rasim Ulgen, Kong Aik Lee, Nicholas Andrews, Carlos Busso, Berrak Sisman

**机构**：Johns Hopkins University, Hong Kong Polytechnic University, Carnegie Mellon University

**发布日期**：2026-08-07 | **论文** https://arxiv.org/abs/2608.05507 | **PDF** https://arxiv.org/pdf/2608.05507.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音深度伪造检测（SDD）系统在传统基准上取得强劲性能，但现有数据集对情感表达和近期大型音频语言模型（LALM）攻击的覆盖有限。现有的情感欺骗数据集在规模和攻击多样性上也有限，通常仅覆盖语音转换（VC）或文本转语音（TTS）攻击。本文介绍AffectDF，这是迄今为止最全面的情感表达语音深度伪造基准，涵盖TTS、VC、情感VC和LALM欺骗攻击，跨越表演和自发情感语音。AffectDF包含约260小时语音，使用21种欺骗攻击生成，涵盖五种情感状态。

### 🔧 技术方案

**模型架构**：标准SDD系统架构，包括音频特征提取器和分类器。

**核心创新**：1）首个大规模情感语音deepfake基准；2）覆盖21种攻击类型；3）涵盖表演和自发情感语音。

**训练策略**：在AffectDF上进行基准测试，评估现有SDD系统在不同条件下的性能。

### 📊 实验结果
**数据集**：AffectDF（约260小时，21种攻击，5种情感状态）

**主要指标**：
- 现有SDD系统在情感条件评估时性能严重下降
- 大规模情感训练不能一致提升跨域鲁棒性
- 情感状态、攻击家族、表演vs自发条件间鲁棒性差异显著
- 多个系统在情感条件下接近随机性能

**是否开源**：AffectDF数据集将公开

### ⭐ 评分：8/10
揭示了当前SDD系统的fundamental limitation，为后续研究指明了方向。对语音安全领域有重要贡献。
