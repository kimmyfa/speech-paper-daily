# 2026-08-10 语音论文速递

**共收录**: 5 篇 | **语音大模型**: 4 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 5 篇。

---

## 语音大模型

---

## [1] SemBridge: Semantic Token Anchoring for Continuous-Latent Autoregressive Speech Generation

**arXiv ID**：2608.07462 | **方向**：语音大模型

**作者**：Hanke Xie, Haopeng Lin, Jiale Qian, Dake Guo, Yuepeng Jiang, Zhichao Wang, Wenxiao Cao, Jingbin Hu, Guobin Ma, Wenhao Li, Huakang Chen, Chengyou Wang, Ming Tao, Zhonghua Fu, Lei Xie, Xinsheng Wang

**机构**：西北工业大学 ASLP Lab、Soul AI Lab

**发布日期**：2026-08-07 | **论文**：https://arxiv.org/abs/2608.07462 | **PDF**：https://arxiv.org/pdf/2608.07462.pdf | **代码**：https://github.com/ASLP-lab/SemBridge | **Demo**：https://tiamojames.github.io/SemBridge_demo/

### 📌 简介
连续潜向量自回归语音生成避免了离散 token 的量化损失，但连续声学目标不提供显式 token 级语言结构，导致 LM 需间接学习语言结构，损害内容保真度。SemBridge 提出训练阶段语义 token 锚定框架，使用离散语义 token（GLM-4-Voice, 12.5Hz, 16384 词表）直接监督 AR LM 状态，并引入语义对齐声学 VAE（SA-VAE）组织连续目标空间。语义监督仅用于训练，推理时完全保持连续生成。在零样本 TTS 和分数条件歌声合成上，SemBridge 在 Seed-TTS-Eval 上达到中文 CER 0.95%、英文 WER 1.81%，同时保持竞争性说话人相似度（SIM 0.758/0.699），显著优于 MELA-TTS 等连续 AR 基线。

### 🔧 技术方案

**问题背景：** 连续 AR 语音生成中，LM 需从声学预测中推断语言结构，缺乏显式 token 级语义目标。现有方法使用连续语义特征对齐（如 SemaVoice、MELA-TTS），但离散语义 token 提供更明确的分类目标且能抑制与语言无关的声学变化。

**模型架构：** 两阶段框架。Stage I 训练 SA-VAE（因果卷积高斯 VAE, 44.1kHz→64维连续潜变量@25Hz），通过轻量投影将连续声学 patch 与冻结 GLM-4 语义 tokenizer embedding 对齐。Stage II 训练连续 AR 生成器，包含 32 层因果 Transformer（hidden=1024, 16 heads）、PatchEnc（8 层）、LocDiT（8 层）和语义预测头。总参数量 800M（不含冻结 SA-VAE 的 86M）。

**核心创新：** (1) 语义 token 锚定机制——使用离散语义 token ID 直接监督选定 AR LM 层状态，同时保持连续潜变量作为唯一生成和递归变量；(2) SA-VAE 目标空间对齐——将连续声学 patch 与语义 tokenizer embedding 在 12.5Hz 帧率下建立一一对应；(3) 训练-推理解耦——语义预测头仅在训练时激活，推理时保持纯连续生成，不改变推理路径。

**训练策略：** SA-VAE 在 25K 小时音频（20K 语音+5K 歌声）上训练 300K 步，8×H20 GPU。SemBridge 在 100K 小时 VoxBox 双语语料上训练 300K 步，16×H20 GPU，全局 batch size 4096 patches。AdamW 优化器，bf16 精度，lr 1e-4，cosine 衰减。语义锚定权重 λ_sem=0.1，推理时 NFE=10，CFG scale=2.0，采样温度 1.0。

### 📊 实验结果
**数据集**：Seed-TTS-Eval（中文/英文/中文困难）、CV3-EVAL（中文/英文/中文困难/英文困难）、GMO-SVS（歌声合成）

**主要指标**：
- 中文 CER: 0.95%（最佳），SIM: 0.758
- 英文 WER: 1.81%（最佳），SIM: 0.699
- 中文困难集 CER: 9.79%，SIM: 0.717
- CV3-EVAL 中文 CER: 3.34%，英文 WER: 4.22%
- 歌声合成：中文 CER 8.32%，SIM 0.906；英文 WER 14.77%，SIM 0.926
- 消融实验：+Align +Anchor 相比无锚定基线 CER 从 1.51→1.01（中文），WER 2.43→1.87（英文）

**是否开源**：已开源

### ⭐ 评分：9/10
评分理由：首次证明离散语义 token 监督对连续 AR 语音生成的有效性，设计优雅且实用——训练时引入额外监督，推理时零开销。在 Seed-TTS-Eval 上达到最优内容准确率，消融实验证实语义对齐和状态锚定互补增益。歌声合成跨任务迁移验证了方法的泛化性。唯一不足是 0.8B 参数量相比 VoxCPM2（2B）仍有差距，但以更少数据（120K vs 2M 小时）达到可比较性能。

---

## [2] LILAC: An Idempotent Neural Speech Codec

**arXiv ID**：2608.05727 | **方向**：语音大模型

**作者**：June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon

**机构**：Seoul National University（首尔大学）

**发布日期**：2026-08-06 | **论文**：https://arxiv.org/abs/2608.05727 | **PDF**：https://arxiv.org/pdf/2608.05727.pdf | **代码**：https://github.com/Rick-McCoy/lilac-codec | **Demo**：https://rick-mccoy.github.io/lilac-demo

### 📌 简介
现有神经音频编解码器不是幂等的——12 个基线系统在单次解码-重编码周期中平均至少重写 15% 的 token，多次循环后质量严重退化。LILAC 是首个在设计上保证幂等的全卷积 24kHz 语音编解码器（0.75 kbit/s, 9.375Hz），利用可逆分析变换（可逆 1×1 卷积 + 加性耦合块）和有限标量量化（FSQ）实现结构级幂等性保证。在 LibriSpeech 和 LibriTTS-R 上分别达到 UTMOS 4.14 和 4.24，与 SOTA 亚 1 kbit/s 编解码器相当，且任意次重编码后 token 100% 一致。

### 🔧 技术方案

**问题背景：** 神经编解码器作为 token 接口在语音生成管线中广泛使用，但重编码解码输出会导致 token 漂移：EnCodec 一次循环后仅 80.5% token 一致，Mimi 32.9%，FocalCodec 10.9%，DAC 1.7%。现有方法（Code Drift, ICASSP 2025）通过辅助损失缓解但无法消除。

**模型架构：** 全卷积可逆架构。分析变换由可逆 1×1 卷积（正交核初始化，转置即逆）和加性耦合块（ConvNext1D 块）组成，4 级 squeeze-and-mix 阶段将 5 通道扩展至 80 通道，逐级丢弃坐标（80,80,80,80,140）最终得到 [20, T/2560] 张量。FSQ 每通道 4 比特（范围[-1,1]，16 级量化），共 80 bits/帧。填充网络（15.4M）用卷积上下文网络重建丢弃坐标。

**核心创新：** (1) 结构级幂等性保证——使用可逆分析变换，编码器丢弃部分坐标，解码器仅从传输的量化坐标重建丢弃信息，数学证明任意权重下幂等性成立；(2) 编码器-解码器权重共享——分析变换权重同时用于编码和解码，减少参数 43.1M；(3) 支持随机解码器——幂等性证明不要求填充网络确定性，可扩展为随机填充实现多样输出。

**训练策略：** 在 HiFiTTS-2 数据集（31700 小时, 4629 说话人, 24kHz）上训练。损失函数：多分辨率 mel 损失（权重 15）、多分辨率 STFT 损失（1）、对抗铰链损失（1）、特征匹配损失（2）。AdamW 优化器，生成器 lr 2e-4，判别器 lr 1e-4，batch size 256，TPU v6e-8 训练，fp32 精度（可逆卷积保持全精度）。SWA 平均最后 10 个 checkpoint。

### 📊 实验结果
**数据集**：LibriSpeech test-clean, LibriTTS-R test, VCTK, HiFiTTS-2 test

**主要指标**：
- LibriSpeech: UTMOS 4.14, dWER 0.101, PESQ 2.60, STOI 0.935, SI-SNR +2.2 dB
- LibriTTS-R: UTMOS 4.24, dWER 0.086, PESQ 2.60, STOI 0.944, SI-SNR +6.0 dB
- 幂等性：100% token 一致（所有 7457 个测试样本，100 次循环验证）
- 下游任务：100 次重编码后 speaker EER 保持 4.00%（FocalCodec 从 3% 退化至 41%）
- 人类评价：MUSHRA 51.4（与 FocalCodec 48.5 无显著差异，p=0.077）

**是否开源**：已开源

### ⭐ 评分：9/10
评分理由：LILAC 是首个从结构上保证编解码幂等性的神经语音编解码器，解决了语音生成管线中重编码 drift 的关键问题。数学证明严谨，实验验证充分（12 个基线对比、100 次循环验证、下游任务稳定性）。音质在 0.75 kbit/s 下具有竞争力，但 dWER 和 SCOREQ 并非最优，且 GPU RTF 实现效率低于其他编解码器。幂等性的实际收益（下游模型稳定性）仍需经验验证。

---

## [3] Multi Codec Discrete Diffusion Model for Text Guided Speech Inpainting and Editing

**arXiv ID**：2608.06424 | **方向**：语音大模型

**作者**：Iftach Shoham, Tali Dror, Oren Gal, Haim Permuter, Gilad Katz, Eliya Nachmani

**机构**：Ben-Gurion University of the Negev（本-古里安大学）、University of Haifa（海法大学）

**发布日期**：2026-08-05 | **论文**：https://arxiv.org/abs/2608.06424 | **PDF**：https://arxiv.org/pdf/2608.06424.pdf | **代码**：https://github.com/iftachShoham/SIEDD | **Demo**：暂无

### 📌 简介
语音修复（inpainting）和编辑（editing）需要在不完全重新合成整个语音的情况下重建或修改缺失/错误区域。离散扩散天然适合该任务，因为它能迭代精炼 mask token 同时联合条件于左右声学上下文。SIEDD 提出分层多码本离散扩散框架 HiCoDD，遵循 RVQ 粗到细生成顺序，将先前生成的 codebook 表示为干净承诺声学上下文，仅对当前精炼 codebook 应用扩散。在 RealEdit 基准上，SIEDD 达到最佳整体语音编辑性能（WER 0.121, SIM 0.98, MCD 270.0），且在所有语音修复设置中优于自回归基线。

### 🔧 技术方案

**问题背景：** 语音编辑中，自回归编解码器语言模型按固定因果顺序生成，无法同时利用左右上下文，早期错误会传播。离散扩散可同时条件于双边上下文并反复精炼，但简单将所有 RVQ codebook 扁平化处理会忽略粗到细的层次依赖。

**模型架构：** HiCoDD（Hierarchical Codebook Discrete Diffusion）基于 DiT 作为 score 网络。包含承诺上下文编码器（编码干净低位 codebook）和解噪解码器。使用 XPhoneBERT 编码器进行音素级条件化。EnCodec 16kHz tokenizer 在 GigaSpeech XL 上训练，K 个 RVQ codebook 以粗到细顺序生成。

**核心创新：** (1) 层次感知 codec 扩散——在每个 codebook 内联合去噪时间位置，同时按 RVQ 固有粗到细顺序生成 codebook，干净低位 codebook 编码为承诺上下文条件化高位去噪；(2) 对比引导（span-localized CFG）——在 log-score 空间组合条件和负条件分数，负分支仅随机化编辑区间音素，不改变边界音素，实现精确的局部引导；(3) 泄漏防止训练——训练时始终使用真实低位 codebook 作为条件，避免推理时条件不匹配。

**训练策略：** 在 GigaSpeech XL 上训练 550K 步，2×RTX A6000 GPU，约 1 周。AdamW 优化器，lr 1e-4。Duration predictor 在 LibriTTS train-clean 上训练。推理使用 512 去噪步。

### 📊 实验结果
**数据集**：RealEdit benchmark（LibriTTS + GigaSpeech YouTube 录音）

**主要指标**：
- 语音编辑：WER 0.121（最佳），SIM 0.98（最佳），MCD 270.0（最佳），F0 Dist. 8.57，Energy Dist. 0.005
- 对比 VoiceCraft（WER 0.124, SIM 0.97, MCD 392.25）和 SSR-Speech（WER 0.146, SIM 0.97, MCD 308.3）
- 语音修复：单 250ms gap：MCD 21.1（VoiceCraft 191.5, SSR-Speech 91.3）
- 多重 gap 设置：SIEDD 保持稳定，AR 基线 WER 急剧上升

**是否开源**：已开源

### ⭐ 评分：8/10
评分理由：SIEDD 首次将离散扩散成功应用于分层 RVQ 语音编辑，层次感知 codec 扩散设计合理。在 RealEdit 上实现最佳 WER、SIM 和 MCD，多 gap 修复展示了对 AR 基线的显著优势。消融实验验证了多 CB 优于单 CB、层次分解优于联合建模。但 UTMOS 得分（3.44）与 TTS 基线（4.11）有差距，且推理速度可能较慢（512 步）。

---

## [4] Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement

**arXiv ID**：2608.07423 | **方向**：语音前端

**作者**：Xulin Fan, Juan Azcarreta, Ashutosh Pandey, Jesus Alvarez, Ke Tan, Jacob Donley, Ritwik Giri, Buye Xu

**机构**：University of Illinois Urbana-Champaign、Meta Reality Labs Research

**发布日期**：2026-08-07 | **论文**：https://arxiv.org/abs/2608.07423 | **PDF**：https://arxiv.org/pdf/2608.07423.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
低延迟、低计算量的语音增强对可穿戴设备至关重要，但严格计算约束严重限制设备端性能。该工作提出云边协作框架，包含三种技术：(1) 延迟服务器输出作为额外输入，(2) 层特征增强（FiLM 调制）传输中间服务器表示指导边缘推理，(3) 协作多通道 Wiener 滤波（MCWF）融合服务器和边缘估计的加权协方差矩阵。在 DNS-Challenge 模拟数据上，完整框架相比仅边缘基线在标准条件下 SI-SDR 提升 3.77 dB（从 1.97 到 5.74 dB），挑战条件下提升 3.49 dB（从 -1.16 到 2.33 dB），仅增加 1.5% 参数和 2.4% 计算量。被 Interspeech 2026 接收。

### 🔧 技术方案

**问题背景：** 可穿戴设备实时通信需要低延迟语音增强，但边缘模型容量受限。知识增强（Knowledge Boosting）已被提出，但语音增强性能提升有限，因为非平稳噪声的快速谱变化在通信延迟存在时难以处理。

**模型架构：** 服务器端为因果 SpatialNet（高容量多通道增强模型），边缘端基于 TinyGRU（空间卷积 + 3 层 SplitGRU, 145K 参数, 32.9 MMACs）。服务器模型预训练 100 轮后冻结。协作 MCWF 使用自适应融合权重 α(t) 平衡服务器延迟估计和边缘实时估计。

**核心创新：** (1) 延迟输入级联——服务器增强音频（延迟 64ms）作为辅助参考通道，提供干净但延迟的估计；(2) 层特征增强——从 SpatialNet 4 层提取中间表示（输入编码层, layer 4, 8, 12），经 1×1 卷积压缩后通过 FiLM 注入 TinyGRU 各层；(3) 协作 MCWF——融合服务器和边缘的交叉协方差向量，自适应权重 α(t) 由 TinyGRU 最后一层预测，在平稳环境偏向服务器，快速变化时偏向边缘。

**训练策略：** DNS-Challenge 数据集，8 通道圆形麦克风阵列，RIR 用 Pyroomacoustics 生成。标准条件 SNR [-5,10] dB，挑战条件 SNR [-10,-5] dB。80K 训练样本。Adam 优化器，lr 1e-3，梯度裁剪 0.03，100 轮训练，SNR 损失函数。

### 📊 实验结果
**数据集**：DNS-Challenge 模拟数据集

**主要指标**：
- 标准条件：SI-SDR 5.74 dB（+3.77 vs 基线），PESQ 2.33，STOI 85.48%
- 挑战条件：SI-SDR 2.33 dB（+3.49 vs 基线），STOI 73.73%
- 延迟敏感性：64ms 最优，96ms 降至 4.39 dB，128ms 降至 4.26 dB，仍显著优于基线
- 与 TinyGRU-Large（432K 参数, +198%）对比：SI-SDR 仅 2.75 dB，验证架构优势而非参数优势

**是否开源**：暂无

### ⭐ 评分：8/10
评分理由：该工作提出实用的云边协作语音增强框架，三种技术互补增益显著。在极小额外开销（+1.5% 参数, +2.4% 计算）下 SI-SDR 提升 ~3.5 dB，远超简单缩放边缘模型。自适应 MCWF 融合权重设计精巧，理论合理。延迟敏感性分析验证了 64ms 实际可行性。但仅在模拟数据上评估，真实场景表现待验证，且依赖稳定网络连接。

---

## [5] LSEAD: A Privacy-Preserving LLM-Based Speech Analysis Framework for Early Alzheimer's Disease Screening

**arXiv ID**：2608.07378 | **方向**：语音大模型

**作者**：Xin Wang, Yingchao Huang, Yuhan Su, Shanshan Yao, Wei Peng

**机构**：Saskatchewan Polytechnic（萨斯喀彻温理工学院）、河北大学、阿尔伯塔大学、里贾纳大学

**发布日期**：2026-08-07 | **论文**：https://arxiv.org/abs/2608.07378 | **PDF**：https://arxiv.org/pdf/2608.07378.pdf | **代码**：https://github.com/kelci2017/AD_Text_LLMs | **Demo**：暂无

### 📌 简介
阿尔茨海默病（AD）早期诊断对及时干预至关重要。基于语音的筛查使用自然语音采集，无需专业设备。LSEAD 提出使用本地部署的开源 LLM（Zephyr-7B-β）提取语音转录文本 embedding，经 PCA 降维后使用逻辑回归分类。在 ADReSS20 和 ADReSSo2021 基准上，LLM embedding 跨数据集泛化良好，分类准确率提升高达 5%（达到 90.0%），尤其对早期阶段检测表现优异。隐私保护特性——所有数据处理在本地完成，无需外部数据交换。

### 🔧 技术方案

**问题背景：** 传统 AD 诊断依赖 MRI/PET 等资源密集型方法。基于语音的检测面临隐私挑战——商用 LLM（如 GPT-4）需要云端处理，不符合 HIPAA 合规要求。现有方法使用手工特征或浅层模型，泛化能力有限。

**模型架构：** 五阶段流水线：(1) 语音预处理（重采样、幅度归一化、VAD 静音去除、分帧）；(2) ASR 转录（自动语音识别）；(3) LLM embedding 提取（Zephyr-7B-β 最后一层隐藏状态，attention-mask 加权均值池化到 4096 维）；(4) PCA 降维（保留 90%-99.9% 方差）；(5) 二分类（逻辑回归/支持向量机/XGBoost/神经网络）。

**核心创新：** (1) 隐私保护设计——仅使用本地部署开源 LLM，所有数据处理在医疗机构内部完成，无需外部数据传输；(2) Zephyr-7B-β 应用于 AD 检测——首次证明该轻量级开源模型在语音 AD 筛查中优于 GPT-3.5/GPT-4；(3) PCA+LR 的简单高效组合——在高维 LLM embedding 上 PCA 降维 + 逻辑回归达到 90% 准确率，超越复杂深度学习方案。

**训练策略：** 在 ADReSS20（54 AD + 54 CN 训练, 24+24 测试）和 ADReSSo2021（87+79 训练, 35+36 测试）上评估。5 折交叉验证，PCA 方差保留率通过网格搜索选择。ASR 质量影响分析：使用不同 ASR 系统评估转录误差对下游分类的影响。

### 📊 实验结果
**数据集**：ADReSS20、ADReSSo2021

**主要指标**：
- 测试准确率：LR 90.0%, F1 89.7%, 精确率 91.2%, 召回率 88.1%
- 对比：Mortensen et al. 84.9%, Bang et al. 83.1%, Agbavor et al. 80.3%
- 早期检测：正确分类 AD 的 MMSE 均值 19.4±7.3，覆盖轻度认知障碍范围
- 消融：无 PCA 时所有分类器性能下降；NNs 仅 78.2%

**是否开源**：已开源

### ⭐ 评分：7/10
评分理由：LSEAD 提供了实用、隐私保护、可扩展的早期 AD 语音筛查方案。Zephyr-7B-β embedding 跨数据集泛化良好，PCA+LR 的简洁设计在有限样本下达到 90% 准确率。隐私保护特性具有实际临床价值。但框架相对简单——仅使用文本级特征，未利用声学/韵律信息；数据集规模较小（<400 样本）；ASR 误差对性能的影响分析不够深入；且 Zephyr-7B-β 作为 beta 模型存在输出不稳定性风险。

---

## 语音前端

---

*Generated on 2026-08-14*