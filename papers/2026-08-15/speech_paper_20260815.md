# 2026-08-15 语音论文速递

**共收录**: 9 篇 | **语音大模型**: 7 篇 | **语音前端**: 1 篇 | **其他**: 1 篇

> 今日 arXiv 语音相关论文共命中 9 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] CookVoice: Unified Framework for Style Controllable Multi-Modal Human Voice Generation

**arXiv ID：** 2608.11590 | **方向：** 语音生成/TTS

**作者：** Haowei Lou, Hye-Young Paik, Jia Dai, Kai Li, Lina Yao

**机构：** UNSW Sydney, Dolby Laboratories

**发布日期：** 2026-08-13 | **论文：** https://arxiv.org/abs/2608.11590 | **PDF：** https://arxiv.org/pdf/2608.11590 | **代码：** 暂无 | **Demo：** https://haoweilou.github.io/CookVoice/

### 📌 简介
CookVoice 提出一个统一的人声生成框架，将语音和歌声生成任务统一在单一非自回归模型中。该框架将人声分解为内容、韵律和风格三个关键因子，通过灵活的帧级对齐策略实现精细控制，支持 TTS、歌声合成、风格可控生成、声音模仿、语音转换和语音编辑等多种任务。仅 43.51M 参数即可在 4 步 ODE 求解下高效推理，风格相似度达 91.65%（TTS）和 95.00%（TTSV），F0 相关系数达 0.71 和 0.84，显著优于基线模型。

### 🔧 技术方案

**问题背景：** 现有语音生成系统多为特定任务设计，TTS、歌声合成、语音克隆等任务各自使用独立架构、数据集和训练目标，导致碎片化严重。自回归模型难以实现帧级精细控制，非自回归模型又受限于预定义的音素-时长假设，无法灵活组合多种控制信号。

**模型架构：** 基于 HiFi-GAN 自编码器将线性谱压缩为连续潜变量，以 DiT-S 为骨干网络结合最优传输流匹配进行生成。风格编码器支持文本描述（MPNet 提取语义）和参考语音（Transformer 编码器+注意力池化）两种模态，内容编码器使用 G2P 模块将文本转为音素序列并通过 FFT 块处理，韵律编码器支持离散信号（声调/重音/MIDI 音符）和连续 F0 轮廓两种控制。三者拼接后作为 DiT 的交叉注意力条件。

**核心创新：** (1) 统一因子分解框架，将人声解耦为内容、韵律和风格三个独立因子，通过条件开关实现多任务训练，无需任务特定目标函数。(2) 灵活帧级对齐策略，将不同控制信号均展至声学帧级别，语音使用预训练对齐器获取音素时长，歌声根据乐谱节拍比例计算帧级时长，实现统一的时序建模。(3) 相对音高解耦设计，将 F0 减去语音级均值转为相对音高轮廓，避免韵律与音色信息纠缠，使连续 F0 控制仅表达旋律变化。

**训练策略：** 使用约 12.3 万样本（168 小时，6361 个说话人）的中英双语语音和歌声数据集，歌声与语音比例 1:9。流匹配 MSE 损失，单张 RTX 5090 训练 80 万步，batch size 32。推理使用 4 步 ODE 求解。

### 📊 实验结果
**数据集：** 多源数据集（Baker, LJSpeech, ESD, CREMA-D, CommonPhone, Genshin Voice, GTSinger 等）

**主要指标：**
- TTS MOS：3.98（接近 GT 4.05）
- TTSV MOS：3.40（最优基线 Vevo2 为 3.42）
- 风格相似度 S-SIM：91.65%（TTS Voice+DISC），95.00%（TTSV Voice+CONT）
- F0-CORR：0.7102（TTS），0.8425（TTSV）
- 参数量：43.51M，RTF：0.04

**是否开源：** 未提供代码，有 Demo 页面

### ⭐ 评分：8/10
评分理由：统一的语音/歌声生成框架设计简洁优雅，帧级对齐策略带来卓越的风格和韵律可控性，在参数量极小的情况下实现 SOTA 级可控性。但感知质量 MOS 略低于部分基线，训练数据量相对较小，可扩展性有待验证。

---

## [2] HybridSB-MoE: Dual-Domain Schrödinger Bridges with Scene-Adaptive Expert Routing for Speech Enhancement

**arXiv ID：** 2608.12715 | **方向：** 语音增强

**作者：** Zhengyi Lu, Aswini Sivakumar, Jie Hu, Yao Qiang

**机构：** Oakland University

**发布日期：** 2026-08-13 | **论文：** https://arxiv.org/abs/2608.12715 | **PDF：** https://arxiv.org/pdf/2608.12715 | **代码：** 暂无 | **Demo：** 暂无

### 📌 简介
HybridSB-MoE 提出一种双域语音增强框架，结合频域混合专家（MoE）和时域薛定谔桥（SB）两种路径，通过非对称不确定性融合机制自适应选择置信度更高的增强结果。频域路径使用 5 种异构专家架构进行稀疏路由，时域路径使用路径一致性和轨迹正则化训练 SB 实现 8 步推理。在 VoiceBank+DEMAND 上 PESQ 达 3.88，COVL 达 4.82，全面超越扩散和 SB 基线。

### 🔧 技术方案

**问题背景：** 生成式语音增强面临三个结构性缺陷：频域模型善于捕捉谐波结构但破坏相位，时域模型保持相位连续性但难以处理谐波干扰，薛定谔桥缩短了噪声到干净的传输路径但推理步数与训练目标缺少形式化关联。单一域模型无法自适应不同噪声场景。

**模型架构：** 双路径并行架构。频域路径对 log-magnitude STFT 特征使用 5 种异构专家（对应家庭/自然/办公/交通/公共场景），采用两级门控（语级+帧级），top-k=2 稀疏路由。时域路径使用 1D U-Net 加 Transformer 瓶颈的 SB 模型，噪声调度采用余弦累积策略。非对称融合模块使用频域专家分歧度（认知不确定性）和时域桥方差（偶然不确定性）驱动 MLP 动态加权。

**核心创新：** (1) 异构 MoE 专家设计，每种专家对应不同的噪声处理先验（低秩去噪、宽感受野、信息瓶颈、谐波基、通用逼近），使专家分歧度反映归纳偏置失配而非容量扰动。(2) 路径一致性和轨迹正则化，理论证明二者联合最小化可在 2-Wasserstein 距离下以 K^{-α} 速率界定 K 步桥采样误差，使小步数推理具有理论保证。(3) 非对称不确定性融合，认知不确定性仅存在于频域 MoE（多个专家共存），偶然不确定性仅存在于时域 SB（随机桥过程），融合权重在两种误差模式间切换而非平均两个预测。

**训练策略：** 端到端联合训练，损失函数包括重建损失、SB 损失、负载均衡损失和校准损失。VoiceBank+DEMAND 训练集 11572 句，测试集 824 句。AdamW 优化器，lr=2e-4，余弦调度，200 epoch，batch size 32，2 张 RTX 5090。推理时 SB 使用 8 步。

### 📊 实验结果
**数据集：** VoiceBank+DEMAND

**主要指标：**
- PESQ：3.88（ROSE-CD 为 3.85，SGMSE+ 为 3.45）
- STOI：0.96
- CSIG：4.82，CBAK：3.85，COVL：4.82
- CBAK 提升最显著，超出 SB-SE 0.10，超出 ROSE-CD 0.48

**是否开源：** 未提供代码

### ⭐ 评分：8/10
评分理由：双域非对称融合设计具有理论创新性，异构 MoE+SB 的耦合思路新颖，离散化界限提供了理论保证。实验充分，VoiceBank+DEMAND 上全面超越现有方法。但仅在单一数据集上评估，泛化性和实际部署延迟有待验证。

---

## [3] VoxAudio: Vocalized Audio Synthesis via Multi-Reward Autoregressive Flow Matching

**arXiv ID：** 2608.12951 | **方向：** 语音合成/T2A

**作者：** Wenxiang Guo, Changhao Pan, Ziyue Jiang, Fei Wu, Zhou Zhao

**机构：** Zhejiang University

**发布日期：** 2026-08-13 | **论文：** https://arxiv.org/abs/2608.12951 | **PDF：** https://arxiv.org/pdf/2608.12951 | **代码：** https://voxaudio.github.io | **Demo：** https://voxaudio.github.io

### 📌 简介
VoxAudio 提出一种因果自回归流匹配模型，用于在环境音景中嵌入可理解语音的有声音频合成。通过分块因果分解、随机分块边界预训练、滑动窗口流式推理实现可变时长流式生成。引入多奖励负感知微调（NFT）联合优化语义保真度、语言准确率（WER）、感知美学和时序对齐。在 AudioCaps 等四个基准上验证了有效性，234M 参数，RTF 0.32，语音 WER 仅 1.61%。

### 🔧 技术方案

**问题背景：** 现有 Text-to-Audio 系统无法生成嵌入场景中的可理解语音，引用的对话通常退化为不可识别的语音咕哝。解耦管线（TTS + T2A + 后混音）无法控制语音与场景的时序交互。此外，非自回归模型无法流式输出，监督式训练无法直接优化人类偏好。

**模型架构：** 基于 Universe Audio VAE 的潜空间，使用因果 Diffusion Transformer 骨干。核心设计为分块因果自回归流匹配：将潜序列划分为因果块，每块独立噪声水平，训练时随机化分块边界（pb=0.15）使模型对任意推理分块大小鲁棒。推理时采用滑动窗口流式策略，相邻块间保持固定步长差 Δ=5，结合 KV 缓存实现连续音频输出。

**核心创新：** (1) 分块感知因果自回归流匹配，训练时随机分块边界使模型学习对任意分块粒度的鲁棒去噪动力学，推理时可自由选择流式分块大小。(2) 多奖励负感知微调（NFT），在因果流匹配框架中引入语义（CLAP/PEAV）、语言（WER）、美学（Audiobox Aesthetics）和时序（TG-IoU）四维奖励，通过组内优势归一化和 KL 正则化进行偏好对齐。(3) VoxCorpus 数据集构建，包含带逐字转录和时间戳的语音标注的大规模音频场景数据集，以及带时序定位指标的 VoxBench 基准。

**训练策略：** 两阶段训练。第一阶段：模拟语料库从头训练，随机分块边界，约 195k 步，batch 384，lr=1e-4；然后在混合语料（70% 模拟+30% 真实叙事）上继续 60k 步，lr=5e-5。第二阶段：多奖励 NFT 偏好对齐，lr=1e-5，每组 6 个 rollout。推理使用 25 步求解器，text-CFG 5.0。

### 📊 实验结果
**数据集：** AudioCaps, VoxBench-10s, MECAT-en, seed-tts-eval

**主要指标：**
- AudioCaps CLAP：0.657（TangoFlux 为 0.728）
- VoxBench 语音 WER：3.8%（优于 Dasheng-AudioGen 的 26.4%）
- seed-tts-eval WER：1.61%（TTS 专用模型 F5-TTS 为 1.20%）
- 参数量 234M，RTF 0.32

**是否开源：** 代码和 Demo 可用

### ⭐ 评分：7/10
评分理由：VoxAudio 首次将因果自回归流匹配用于有声音频合成，解决了 T2A 系统中语音不可理解的关键问题。多奖励 NFT 对齐和 VoxCorpus 数据集是实质贡献。但通用音频质量（CLAP 等指标）低于专用 T2A 模型，270 步推理延迟较高。

---

## [4] SraVaani 1.0: Scaling Inclusive Speech Recognition for Indic Languages

**arXiv ID：** 2608.08235 | **方向：** ASR

**作者：** Sujith Pulikodan, Agneedh Basu, Pavan Kumar J, Pranav D Bhat, Suryansh Shukla, Nihar Desai, Prasanta Kumar Ghosh

**机构：** Indian Institute of Science (IISc), Bangalore; ARTPARK@IISc

**发布日期：** 2026-08-12 | **论文：** https://arxiv.org/abs/2608.08235 | **PDF：** https://arxiv.org/pdf/2608.08235 | **代码：** https://huggingface.co/ARTPARK-IISc/SraVaani-1.0 | **Demo：** 暂无

### 📌 简介
SraVaani-1.0 是一个覆盖 65 种印度语言和方言的多语言 ASR 模型，基于 FastConformer 架构，采用三阶段训练：自监督对比学习预训练（31,255 小时无标签语音）、音频-图像表示对齐（利用 VAANI 语料库的图片-语音对）、混合 TDT-CTC 监督微调（31,263 小时标注语音）。在 8 个基准测试中，SraVaani-1.0 在 17 种可比较语言上平均 WER 28.4%，为 44 种低资源语言和部落语言提供了首个公开 ASR 能力。

### 🔧 技术方案

**问题背景：** 印度有 700 多种语言和数千种方言，但现有 ASR 系统仅覆盖少数高资源语言。Whisper、Google USM 等对印度低资源语言支持有限，IndicConformer 和 Sarvam Saaras 仅覆盖 22 种宪法认可语言，大量部落语言和方言完全没有 ASR 支持。

**模型架构：** FastConformer 编码器（17 层 Transformer，dmodel=1024，8 头注意力，8× 深度可分离卷积降采样），采用混合 TDT-CTC 解码器（Token-and-Duration Transducer + CTC 联合优化，λCTC=0.3）。BPE 分词器，5000 个子词单元，统一覆盖所有印度文字。

**核心创新：** (1) 三阶段训练策略，自监督预训练后插入音频-图像对齐阶段，利用 VAANI 语料库中图片提示语音对，通过 SigLIP 对比损失将语音表示与冻结视觉编码器的图像嵌入对齐，无需任何转录即可注入语义信息。(2) FastConformer 高效架构，深度可分离卷积降采样 8 倍，在保持建模能力的同时大幅降低注意力计算成本。(3) 极广泛的语言覆盖，65 种语言包括 44 种无任何公开 ASR 的部落语言（如 Garo、Mizo、Nyishi 等），基于 24 个公开数据集的 31,263 小时标注语音。

**训练策略：** 第一阶段：VAANI 语料 28,418 小时无标签语音，wav2vec2.0 对比损失，70 epoch，Noam 调度，lr 峰值 3.5e-6。第二阶段：1184 万音频-图像对，SigLIP 对比损失，200K 步，SigLIP2-Large 视觉编码器冻结。第三阶段：24 个数据集 30,565 小时标注语音，lr=1e-5，最多 50 epoch。

### 📊 实验结果
**数据集：** CommonVoice, FLEURS, IndicTTS, Kathbath, RESPIN, GramVaani, MUCS, VAANI

**主要指标：**
- 17 种可比较语言平均 WER：28.4%（低于 Gemini 39.4%、Sarvam 33.9%、IndicConformer 30.2%）
- 44 种唯一语言平均 WER：50.2%（Garo 9.5%，Mizo 25.3%，Nyishi 93.9%）
- 在 10/17 种可比语言上取得最佳 WER
- 28/68 个语言-数据集对上取得最佳 WER

**是否开源：** 模型权重在 Hugging Face 开源

### ⭐ 评分：7/10
评分理由：SraVaani-1.0 在语言覆盖广度上具有独特价值，首次为 44 种低资源语言提供 ASR 能力。音频-图像对齐的创新设计有效利用多模态信号。但低资源语言 WER 偏高（均值 50%），且训练和评估数据同源，域外泛化能力待验证。

---

## [5] Optimal Transport-based Semantic Alignment for LLM-based Audio-Visual Speech Recognition

**arXiv ID：** 2607.09001 | **方向：** AVSR

**作者：** Xugang Lu, Peng Shen, Yu Tsao, Hisashi Kawai

**机构：** National Institute of Information and Communications Technology, Japan; Academia Sinica, Taiwan

**发布日期：** 2026-08-13（更新版） | **论文：** https://arxiv.org/abs/2607.09001 | **PDF：** https://arxiv.org/pdf/2607.09001 | **代码：** 暂无 | **Demo：** 暂无

### 📌 简介
本文提出基于最优传输（OT）的语义对齐框架用于 LLM 视听语音识别（AVSR）。在融合前，通过 OT 将 Whisper 声学编码器和 AV-HuBERT 视觉编码器的表示对齐到 LLaMA3.2-3B 的语言嵌入空间，利用 OT 耦合矩阵作为软伪标签监督对比学习，促使多模态特征在语义上更一致。在 LRS3-TED 上，信噪比 -5dB 条件下 WER 从 8.34% 降至 7.16%，干净条件下 WER 从 0.89% 降至 0.71%。

### 🔧 技术方案

**问题背景：** 现有 LLM-AVSR 系统直接将音频和视觉特征投影融合，未解决模态间的表示差异问题。声学编码器和视觉编码器使用不同目标和数据分布独立预训练，其潜空间存在结构性失配。此外，时间同步不一定等于语义同步，音视频对语言内容的贡献可能发生在不同时间位置。

**模型架构：** Whisper 声学编码器（medium，冻结）+ AV-HuBERT 视觉编码器（large，冻结）+ LLaMA3.2-3B 解码器（LoRA 微调）。OT 对齐模块插入在编码器和投影层之间，将声学/视觉特征序列与目标文本嵌入分布之间的 OT 耦合矩阵作为软标签监督对比学习。

**核心创新：** (1) OT 语义对齐，将音频和视觉特征分布与 LLM 文本嵌入分布之间的 OT 耦合作为软伪标签，显式桥接模态间隙而非简单拼接。(2) 虚拟桶机制，引入虚拟桶吸收非信息帧（噪声/静音/背景），避免不相关帧强制对齐到语言标记。(3) 对比学习对齐损失，OT 耦合矩阵作为软标签监督交叉熵对比学习，促使提取语义一致且跨模态一致的特征表示。

**训练策略：** 联合优化 AR 交叉熵损失和对齐损失（α=0.1-0.5）。LoRA rank=16，缩放因子 32，Adam 优化器，初始 lr=1e-4，5k warmup，总计 30k 步。噪声训练使用 babble 噪声，SNR [-5,0,5,10,15,20] dB。

### 📊 实验结果
**数据集：** LRS3-TED

**主要指标：**
- SNR-5dB WER：7.16%（基线 C_Concat 8.34%，MMS-LLaMA 7.44%）
- SNR0dB WER：2.26%（基线 2.82%）
- 干净条件 WER：0.71%（基线 0.89%）
- 虚拟桶带来额外提升（SNR-5 从 8.06% 降至 7.98%）

**是否开源：** 未提供代码

### ⭐ 评分：7/10
评分理由：OT 语义对齐思路新颖，有效解决了多模态表示融合前的语义对齐问题。在 LRS3-TED 上一致改进，-5dB 条件下提升显著。但超参数多且交互复杂，调优依赖经验，缺少对更多低 SNR 条件的评估。

---

## [6] CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model

**arXiv ID：** 2608.13101 | **方向：** 口语评估/ASA

**作者：** Nhan Phan, Ilona Lähteenmäki, Anna von Zansen, Olli-Pekka Pauna, Yaroslav Getman, Tamás Grósz, Mikko Kurimo

**机构：** Aalto University, University of Helsinki, Walton Institute

**发布日期：** 2026-08-13 | **论文：** https://arxiv.org/abs/2608.13101 | **PDF：** https://arxiv.org/pdf/2608.13101 | **代码：** https://github.com/aalto-speech/casa | **Demo：** 暂无

### 📌 简介
CASA 提出一种内容-声学双分支口语自动评估架构，显式分离语音表达（声学分支）和内容（文本分支）。使用 Whisper-medium 编码器（LoRA 适配）提取声学特征，Qwen3.5-2B（LoRA 适配）处理 ASR 转录文本，仅使用三个手工流畅度特征。在 Speak & Improve Corpus 2025 上 RMSE 达 0.358，略优于 SOTA 0.360，同时参数量减半（3.13B vs 6.24B）。代码已开源。

### 🔧 技术方案

**问题背景：** 口语自动评估需要同时考虑语音表达（怎么说）和内容（说什么）。现有 speech LLM 方法依赖大型多模态骨干网络，推理开销大，且对声学和文本信息各自贡献的分析不足。多评估器组合系统管线复杂，可迁移性受限。

**模型架构：** 双分支架构。声学分支：Whisper-medium 编码器（冻结，LoRA 适配），输出帧级特征经 Transformer 聚合后生成 4 个声学软 token 和辅助 CEFR 估计。文本分支：ASR 转录文本与任务提示、评分标准、3 个流畅度统计（时长、静音比、语速）拼接后输入 Qwen3.5-2B（LoRA 适配）。线性回归头从最后 token 表示预测分数。

**核心创新：** (1) 显式声学-内容分离，通过双分支架构实现声学信息和文本信息的独立建模和可解释融合，辅助损失（容忍度 τ=1）仅在偏差超过容忍度时惩罚。(2) 声学软 token 设计，将声学汇总表示为 4 个软 token 输入 LLM，配合辅助损失头提供互补监督信号。(3) 训练无关内容验证，利用 LLM 在推理时零样本判断回答是否切题，检测率 99.9%，单条响应耗时 <0.1s。

**训练策略：** 单张 H100 80GB，batch size 16，梯度累积 2 步。声学 LoRA lr=2e-4，LLM LoRA lr=1e-4，其他模块 lr=5e-5，训练约 2 小时。主损失 MSE + 辅助损失 0.1×MSEτ。

### 📊 实验结果
**数据集：** Speak & Improve Corpus 2025

**主要指标：**
- RMSE：0.358（NTNU 0.360，Perezoso 0.364）
- PCC：0.829
- 参数量 3.13B（NTNU 6.24B 的一半）
- 10 次重复运行平均 RMSE 0.363，95% CI [0.359, 0.367]
- 不同 CEFR 等级：A2 0.553，B1 0.351，B2 0.290，C1 0.554

**是否开源：** 代码在 GitHub 开源

### ⭐ 评分：7/10
评分理由：CASA 以更小的模型达到 SOTA 级性能，双分支设计清晰可解释，LLM 零样本内容验证功能实用。但 RMSE 提升幅度小（0.358 vs 0.360），低分（A2）和高分（C1）的评估误差较大，且声学 Transformer 聚合器的任务嵌入效果不理想。

---

## [7] Alignment Drift in Single-Model Speculative Decoding for ASR: Mechanism, Correction, and Cost

**arXiv ID：** 2608.12703 | **方向：** ASR 加速

**作者：** Xinyu Wang, Huapeng Zhou, Ziyu Zhao, Silin Meng, Ke Bai, Dongming Shen, Xiao-Wen Chang, Alex Smola

**机构：** Boson AI

**发布日期：** 2026-08-13 | **论文：** https://arxiv.org/abs/2608.12703 | **PDF：** https://arxiv.org/pdf/2608.12703 | **代码：** 暂无 | **Demo：** 暂无

### 📌 简介
本文研究了单模型推测解码在 ASR 中的应用，发现轻量级 draft 模块在目标模型验证之间运行时会出现"对齐漂移"问题——draft 的音频注意力逐渐偏离正确的音频位置。在 Qwen 1.7B 和 Voxtral 3B 上，带音频交叉注意力的 draft 相比无音频版本将续行接受率提升约一倍（从 0.25-0.32 到 0.54-0.58），端到端加速达 1.41-1.69 倍。提出 AnchorDraft 训练方法在训练时加入位置监督，无需改变推理图即可提升加速效果。

### 🔧 技术方案

**问题背景：** 推测解码通过轻量 draft 提出多个候选 token 由目标模型一次性验证来加速生成。在 ASR 中，draft 每一步都能读取完整的编码音频，但自回归运行 draft 时其注意力逐渐偏离正确音频帧（对齐漂移），导致后续提案接受率下降。晚期 draft 中位误差在困难条件下达 21 帧，而验证阶段目标注意力中位误差仅 2 帧。

**模型架构：** 基于 EAGLE-3 的 draft 设计（直接 token 预测+多层特征），加入从每个 draft 步到冻结音频编码器的交叉注意力。训练了 Qwen3-ASR 两个规模（1.7B 和 0.6B）和 Voxtral-Mini 的 draft，Whisper 作为跨架构对比。

**核心创新：** (1) 对齐漂移的定量刻画，首次系统分析 ASR 推测解码中 draft 的音频位置跟踪问题，通过 MMS 强制对齐器验证注意力峰值作为位置度量。(2) 验证注意力校正方法，在运行时从验证注意力读取音频位置指导下一轮 draft，仅在额外接受 token 抵消费用时有效。(3) AnchorDraft 训练方法，在不改变推理图的情况下，通过训练目标加入位置监督，使 draft 学会跟踪音频位置，在两个测试规模上均提升端到端速度。

**训练策略：** LibriSpeech train-clean-100 训练可行性 draft，官方数据训练主要因果实验。A100-80GB 单卡，batch size 1，bfloat16。评估使用 LibriSpeech clean/other、TED-LIUM、GigaSpeech、FLEURS。

### 📊 实验结果
**数据集：** LibriSpeech, TED-LIUM, GigaSpeech, FLEURS

**主要指标：**
- Qwen 1.7B + 音频 draft：加速 1.41-1.55×（无音频 1.14-1.30×）
- Voxtral 3B + 音频 draft：加速 1.42-1.69×（无音频 0.95-1.08×）
- 续行接受率 a2c：0.54-0.58（有音频）vs 0.25-0.32（无音频）
- 正确位置窗口 vs 偏移窗口的接受率差异：+0.254（95% CI [+0.241,+0.268]）

**是否开源：** 未提供代码

### ⭐ 评分：7/10
评分理由：对齐漂移问题的发现和分析深入，对 ASR 推测解码社区有指导意义。AnchorDraft 校正方法简洁有效。但实验主要在特定模型架构上进行，泛化性有待验证，AnchorDraft 端到端加速增益有限。

---

## [8] Evaluating Pre-trained Speech Encoders for Spontaneous Speech Detection and Out of Domain Synthetic Speech Generalisation in Indic Languages

**arXiv ID：** 2608.12536 | **方向：** 语音检测/说话人识别

**作者：** Varun Rai, Pavan Kumar J, Sujith Pulikodan, Nihar Desai

**机构：** IIT Guwahati, ARTPARK@IISc

**发布日期：** 2026-08-12 | **论文：** https://arxiv.org/abs/2608.12536 | **PDF：** https://arxiv.org/pdf/2608.12536 | **代码：** 暂无 | **Demo：** 暂无

### 📌 简介
本文系统评估了 5 种冻结预训练语音编码器（AST、Vaani-FastConformer、Wav2vec2、Whisper、BEATs）在 22 种印度语言上的自发语音检测和合成语音泛化能力。发现编码器选择至关重要：Wav2vec2 存在语言可区分性与自发性检测之间的权衡，Whisper 和 Vaani 则保持高准确率且与语言结构无关。在合成语音泛化中，训练多样性将 OOD 召回率从 7% 提升至 51%，泛化能力由训练系统与未见 TTS 嵌入的邻近度决定。

### 🔧 技术方案

**问题背景：** 基于 Transformer 的语音编码器在自发/脚本语音分类和自然/合成语音分类上表现优异，但结果主要建立在英语等高资源语言上，对印度语言的泛化性未知。嵌入几何分析来解释编码器行为和深度伪造泛化失败的研究也缺乏。

**模型架构：** 5 种冻结 Transformer 编码器（AST、Vaani-FastConformer、Wav2vec2、Whisper、BEATs），每种提取帧级嵌入后时间平均池化，通过轻量 3 层全连接 DNN 分类器（约 28-32 万参数）进行线性探测。

**核心创新：** (1) 语言隔离探测分析，通过训练多分类逻辑回归探针预测嵌入的语言来源，发现 Wav2vec2 存在显著负相关（Pearson R=-0.62，p=0.0015），即语言可区分性越高的语言，自发性检测准确率越低，而 Whisper 和 Vaani 无此权衡。(2) 质心邻近度分析，发现 OOD 泛化由训练系统与未见 TTS 嵌入的邻近度预测，而非与自然语音的距离，这对训练数据选择有直接指导意义。(3) 多系统 TTS 泛化实验，训练池从 1 个扩展到 4 个 TTS 系统时，OOD 合成语音召回率从 7% 提升至 51%。

**训练策略：** 使用 IndicVoices 语料库的 22 种印度语言，IEMOCAP 作为英语参考。自发性分类使用 IndicVoices 的场景标签（Read/Extempore/Conversation）作为二值标签。合成语音分类使用 4 个 TTS 系统（F5、OmniVoice、Indic VITS、M4）生成音频，2 个外部系统（freevc24、xttsv2）用于 OOD 评估。

### 📊 实验结果
**数据集：** IndicVoices, IEMOCAP, IndicSynth

**主要指标：**
- 自发性分类：Whisper 和 Vaani 在所有 22 种语言上均保持高准确率（约 85%+）
- OOD 合成语音召回率：4 系统训练 51%（单系统训练仅 7%）
- F5 嵌入最接近自然语音（欧氏距离 1.12），但 OOD 泛化最差
- Omni 嵌入最接近 OOD 系统（xttsv2 距离 1.27），OOD 泛化最好

**是否开源：** 未提供代码

### ⭐ 评分：6/10
评分理由：在印度语言语音检测上的系统评估填补了空白，质心分析结果为训练数据选择提供了新视角。但编码器仅使用冻结版本，方法较为常规，缺乏细粒度分析或新方法提出。

---

## 其他

## [9] Motor, Cognitive, or Corpus? What Survives Cross-Lingual Transfer in Speech-Based Parkinson's Disease Detection

**arXiv ID：** 2608.13425 | **方向：** 语音医学/帕金森检测

**作者：** Serli Kopar, Sam Gijsen, Abner Hernandez, Paula Andrea Perez-Toro, Kerstin Ritter

**机构：** University of Tübingen, Charité–Universitätsmedizin Berlin, FAU Erlangen-Nürnberg

**发布日期：** 2026-08-13 | **论文：** https://arxiv.org/abs/2608.13425 | **PDF：** https://arxiv.org/pdf/2608.13425 | **代码：** 暂无 | **Demo：** 暂无

### 📌 简介
本文系统评估了 9 种自监督学习语音表征在跨语言帕金森病（PD）检测中的迁移能力。通过 5 种渐进式分布偏移场景分析发现：最优层选择高度依赖语料库而非模型架构，跨语言迁移的判别信号缺乏病理特异性——PD 分类器对痴呆症语音也赋予高概率。在严重偏移下（跨语言+跨任务），平衡准确率下降至 64%，表明当前语音 PD 检测更多反映语料库特定因素而非疾病特异性特征。

### 🔧 技术方案

**问题背景：** 自监督语音表征在单一语料库内的 PD 检测表现优异，但跨语言、跨语料库的泛化能力未知。模型是否真正捕获了疾病相关特征，还是利用了语料库特定的混杂因素？SSL 模型几乎仅在健康语音上预训练，能否编码 PD 相关语音特征？此外，大多数研究仅与健康对照比较，未评估与痴呆等其他神经退行性疾病的区分能力。

**模型架构：** 9 种 SSL 语音骨干（HuBERT-B/L、WavLM-B/L、W2V2-B、W2V2-B-FT、HuBERT-L-FT、XLS-R、MMS）+ 手工 eGeMAPS 特征（88 维），提取每层帧级表示后时间平均池化，使用低容量逻辑回归探针分类。

**核心创新：** (1) 五场景渐进式评估框架，从无偏移（REF）到重测（S1）、录音条件（S2）、语言（S3）、任务（S4）、语言+任务（S5）逐步引入分布偏移，系统性量化 PD 检测的鲁棒性。(2) 跨病理特异性分析，将 PD 训练分类器迁移到 TREND 队列，发现其对 PD 和痴呆症语音的区分能力为随机水平（AUC 0.50-0.55），表明捕获的是"患者-健康对照"一般性差异而非 PD 特异性特征。(3) 层选择语料库依赖性发现，大模型最优层跨语料库标准差高达 0.43（WavLM-L 在 DDK 任务上），说明层选择由语料库而非架构主导。

**训练策略：** 3 种 PD 语料库（西班牙语 ES、德语 DE、捷克语 CZ），每种包含 DDK/READ/VOWEL 三种任务。REF 设定下 5 折交叉验证选择最优层，10 个随机种子。TREND 队列用于跨病理评估（36 痴呆+18 PD，各匹配对照组）。

### 📊 实验结果
**数据集：** ES/DE/CZ 三种 PD 语料库，TREND 队列（痴呆+PD+对照）

**主要指标：**
- REF 准确率：READ 任务最优（约 80-90% BA）
- S1（重测）平均变化：-1.9±4.5 BA 点
- S2（录音条件）平均变化：-12.5±14.3 BA 点
- S3（跨语言）平均变化：-16.3±10.6 BA 点
- S4/S5（跨病理）：PD vs 痴呆 AUC 0.50-0.55（随机水平）

**是否开源：** 未提供代码

### ⭐ 评分：6/10
评分理由：严格的五场景评估框架和跨病理特异性分析具有重要临床意义，揭示了语音 PD 检测的泛化瓶颈。但样本量有限（DE 176 人，痴呆 36 人），结论的统计效力有限，且仅使用线性探针，未探索更复杂的迁移方法。

---

*Generated on 2026-08-15*