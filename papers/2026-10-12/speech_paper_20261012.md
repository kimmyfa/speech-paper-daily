# 2026-10-12 语音论文速递

**共收录**: 26 篇 | **语音大模型**: 21 篇 | **语音前端**: 5 篇

> 目标日期 2026-10-12（北京时间）arXiv 语音相关论文共命中 26 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] Lossless Inference Acceleration for ASR via EAGLE-Style Speculative Decoding

**arXiv ID**：2610.13506 | **方向**：语音大模型

**作者**：Sen Zhang, Xianghu Yue, Yiming Chen, Wenhuan Lu, Jianguo Wei, Haizhou Li

**机构**：天津大学智能与计算学部、ASUS Intelligent Cloud Services（新加坡）、香港中文大学（深圳）、新加坡国立大学

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13506 | **PDF**：https://arxiv.org/pdf/2610.13506.pdf | **代码**：https://github.com/ssss-sen/eagle-asr | **Demo**：暂无

### 📌 简介
针对自回归 ASR 逐 token 解码延迟高，而现有推测解码要么草稿质量差、要么依赖外部分布对齐草稿模型的问题，本文提出 EAGLE-ASR 框架。核心是轻量自回归 Speech-Draft 模块（仅 1 层 Transformer decoder 块，复用目标模型 embedding 与 LM head），联合编码器的声学特征与解码器低/中/高层级表示生成草稿，并配合自蒸馏训练数据和多步生成训练策略。在 Whisper-large-v3 和 Conformer AED（220M）上分别实现 1.91× 和 2.43× 无损加速（ΔWER=0.00），多语种 ASR 平均 2.09×、语音翻译平均 1.62×，全面超越 SpD 与 Medusa 基线。

### 🔧 技术方案

**问题背景：** 自回归 Transformer/Conformer ASR 顺序生成 token 形成解码瓶颈；模型压缩与非AR解码会牺牲精度；已有 ASR 推测解码要么需与目标同族的外部草稿模型（跨架构时接受率骤降），要么如 Whisper-Medusa 独立多头预测忽略时序依赖且需微调目标层导致 WER 退化，无法同时做到高质量草稿、通用性与无损。

**模型架构：** 冻结目标 ASR 模型（Encoder+AR Decoder）外挂 Speech-Draft：含 2 个 FC 层、embedding 层、1 个 Transformer decoder 块和 LM head（embedding/LM head 直接复用目标模型参数）。FC1 仅在首步融合解码器 low/middle/high 三层表示为 f_mixed；FC2 将 f_mixed（或上一步隐状态）与已生成 token 嵌入拼接；f_encoder 通过交叉注意力注入，保持声学与解码器上下文耦合。推理时递归生成 K 个草稿 token，目标解码器并行验证（min(1,p/p̂) 接受、残差分布重采样），输出分布与原模型严格一致。

**核心创新：** (1) 首个 EAGLE 式 ASR 通用草稿模块：不依赖外部同族小模型，直接利用目标内部表示，跨 Whisper/Conformer 无缝集成，任意 Transformer 解码器 AED 均可即插即用。(2) 自蒸馏训练数据：用目标模型转写全部训练音频作为草稿学习目标，消除"理想标注"与"模型真实分布"在标点、大小写、特殊 token 前缀上的差异，显著提升接受率。(3) 多步生成+指数衰减加权损失：训练时递归 K 步以自身隐状态条件预测后续 token，缓解与推理的训练-推理失配误差累积；按 α_k=β^(k-1)/Σβ^(j-1) 加权交叉熵优先保证近端 token 精度。

**训练策略：** 仅训练 FC 层与 decoder 块，其余冻结。LibriSpeech 960h 训练 Speech-Draft：Whisper 200K 步、Conformer 150K 步；VoxPopuli 上分别 400K/300K 步。AdamW（β1,β2=0.9,0.95），梯度裁剪 0.5，余弦学习率峰值 5×10⁻⁵、warmup 比 0.05，batch size 2×梯度累积 4（有效 8）；衰减因子 β=0.8、预测深度 K=7。评测在单张 RTX 4090 上完成。

### 📊 实验结果
**数据集**：LibriSpeech（960h 训练，test-clean/test-other）；VoxPopuli（英/德/西/法/意 ASR 及德西法意→英翻译）

**主要指标**：
- Whisper-large-v3 加速比：1.91×（clean）/1.79×（other），τ=3.79/3.55，ΔWER=0.00
- Conformer AED 加速比：2.43×/2.30×，τ=4.98/4.50，ΔWER=0.00
- 多语种 ASR 平均加速 2.09×（τ≈4.4，ΔWER=0.00）；语音翻译平均 1.62×（top-k=2，ΔBLEU=0）
- 最强基线对比：优于 SpD+Distil-large-v3（1.72×/1.52×）与 Whisper-Medusa（1.67×/1.65× 且 ΔWER+1.17~+3.61 非无损）；SpD 在 Conformer 上反而减速（0.88~0.90×）
- 消融：去编码器特征致 0.89× 减速（τ=0.08）；去多步生成降至 1.17×；去自蒸馏降至 1.43×
- 超参：K=5、top-k=1 为最优，ASR 上线性验证优于树形验证

**是否开源**：代码已开源 @ https://github.com/ssss-sen/eagle-asr

### ⭐ 评分：8/10
评分理由：首次将 EAGLE 式推测解码成功移植到跨模态 ASR，Speech-Draft 的声学交叉注意力和自蒸馏设计直击草稿-目标分布失配痛点，消融完整、无损性全程严格成立，且对异构目标模型通用性强。实验限于离线 AED 模型、单卡评测，加速比约 2× 量级，流式与端侧部署未涉及，稍抵影响力。

---

## [2] From 2.1M Hours of Raw Broadcast Audio to Finnish Speech SSL: Confidence Filtering and Architectural Analysis at Scale

**arXiv ID**：2610.13102 | **方向**：语音大模型

**作者**：Yaroslav Getman, Tamás Grósz, Tommi Lehtonen, Mikko Kurimo

**机构**：阿尔托大学（芬兰）、SETU Walton研究所（爱尔兰）、芬兰国家视听研究所（KAVI）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13102 | **PDF**：https://arxiv.org/pdf/2610.13102.pdf | **代码**：https://github.com/aalto-speech/large-scale-monolingual-speech-foundation-models （模型开源，语料因广播版权不可再分发） | **Demo**：暂无

### 📌 简介
针对广播档案用于低资源语言语音自监督预训练时含大量噪声、非语音与多语内容、"存在语音"不等于"高质量"的问题，本文提出以ASR的CTC置信度作为数据质量代理：从芬兰RTVA 210万小时广播出发，经pyannote VAD得120万小时、ASR转写去重得89万小时，再以置信度阈值τ=-0.1筛出47.1万小时（99%芬兰语）。在wav2vec 2.0框架下对Transformer、Macaron-Net、Conformer、E-Branchformer做95M/317M/965M参数量对齐对比。置信度过滤较LID过滤带来3-7%相对WER下降，卷积增强编码器在Base规模较Transformer最高37%相对WERR，X-Large在KAVI广播测试集达19.54%，全面超越既有芬兰SSL基线。

### 🔧 技术方案

**问题背景：** 广播档案规模大、多样但质量混杂，既有工作仅用VAD或LID保证"提取到语音"，从未按质量系统性筛选无标注预训练数据；同时先前SSL架构对比同时变动结构与参数量（如618M Conformer vs 317M Transformer），无法区分收益来自架构还是容量。

**模型架构：** wav2vec 2.0框架（CNN特征前端+编码器），三档规模Base(95M)/Large(317M)/X-Large(965M)。四种编码器后端：标准Transformer（MHSA+FFN）、Macaron-Net（MHSA前后各半阶FFN、内维减半保持参数量）、Conformer（Macaron结构中间插入Convolution模块）、E-Branchformer（MHSA与卷积门控MLP并行分支，经depthwise卷积Merge融合）。每档在固定参数预算下扫描多个层数/宽度配置（如Base含6/12/18/24层）。

**核心创新：** (1) 首次将ASR置信度用于SSL预训练数据选择：定义C_char为剔除blank token后逐帧字符预测的平均log概率（用自有芬兰w2v2 Large模型转录），保留C_char≥τ样本；τ=-0.1为不退化的最严阈值，保留53%数据且天然滤除非目标语言（终集99%芬兰语），可替代显式LID。(2) 首次参数量对齐的四种编码器SSL受控对比（95M–965M），并将Macaron-Net作为独立后端以隔离双FFN效应；发现卷积增强架构优势在容量受限的Base规模最大（CV上31.0-36.7%相对WERR），接近1B参数时收窄、Transformer scaling最稳。(3) 构建"VAD→转写去重→置信度过滤"三段流水线，得到迄今最大规模单语学术SSL语料471K小时并公开发布模型。

**训练策略：** 预训练512张AMD MI250X、Fairseq实现，wav2vec 2.0标准目标（掩码预测+对比损失）：Base lr 6e-4、动态batch 3分钟/GPU、125K steps；Large lr 4e-4、2分钟/GPU、167K steps；X-Large lr 1e-4、1分钟/GPU、400K steps。ASR微调128卡、CTC损失、冻结CNN前端，标注数据4.6K小时（FP+LP转录），lr从1e-5~1e-4选优：Base batch 2.5分钟/GPU/16K updates，Large 2分钟/GPU/25K steps，X-Large约1分钟/GPU/40-45K steps。

### 📊 实验结果
**数据集**：预训练471K小时（RTVA 2.1M小时广播经流水线筛选，并入VoxPopuli芬兰语14.3K、FP 3.1K、LP 3.2K小时）；评测含FP'16/FP'20、LP、Common Voice 16.1、FLEURS及自建KAVI真实广播测试集（Nova、Basso各1小时）。

**主要指标**（WER）：
- 置信度过滤 vs LID过滤：同等~72%保留率下4个验证集中3个更低，最终带来3-7%相对WER下降
- Base Conformer(17/512/1536)：CV 5.69、FLEURS 10.56，较同参数Transformer（9.74/13.02）相对下降41.6%/18.9%
- Base E-Branchformer：KAVI 22.44，较Transformer 24.85相对下降9.7%；卷积编码器Base规模最高37%相对WERR
- X-Large Transformer：KAVI 19.54、CV 3.85，较前芬兰基线（22.42/5.42）分别相对下降12.8%/29.0%

**是否开源**：模型已开源 @ https://github.com/aalto-speech/large-scale-monolingual-speech-foundation-models，语料未开源（版权限制）（已被 SLT 2026 接收）

### ⭐ 评分：8/10
评分理由：实验设计严谨是本文最大价值——参数量对齐的多深宽配置、六测试集域内外评测、保留率受控的过滤消融，得出"质量优先于数量""架构优势随规模衰减"等可直接指导低资源语言SSL实践的工程结论。局限是仅涉及芬兰语与wav2vec 2.0框架、置信度代理依赖单一既有ASR、对基线绝对改进有限，属扎实的大规模实证研究而非方法突破。

---

## [3] Emo-BPO: Emotion Bidirectional Preference Optimization for Diffusion-based Emotional TTS

**arXiv ID**：2610.12958 | **方向**：语音大模型

**作者**：Jiacheng Shi, Hongfei Du, Xinyuan Song, Y. Alicia Hong, Yanfu Zhang, Ye Gao

**机构**：College of William & Mary（美国）| Emory University（美国）| George Mason University（美国）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.12958 | **PDF**：https://arxiv.org/pdf/2610.12958.pdf | **代码**：暂无 | **Demo**：https://jiachengqaq.github.io/emo-bpo/

### 📌 简介
针对扩散情感TTS的偏好对齐只强化目标情绪、忽略竞争情绪建模，且在分类器自由引导（CFG）下形成非对称优化的缺陷，提出 Emo-BPO：把同一文本、不同情绪的音频样本重排序构造为偏好对，并行训练情绪对齐（EA）与情绪对比（EC）两个得分分支，推理时以 (1+ω)ε_EA − ω ε_EC 的对比引导配合后期步调度 ω(t)=1−t/T 联合控制。在 ESD 与 EmoVoiceDB 上，情绪相似度 99.23、韵律相似度 3.85、UTMOS 4.52、情绪识别平均准确率 0.87，主观 MOS/Emo MOS 达 3.93/4.25，全面优于 EmoVoice 与 CosyVoice2，且无需奖励模型或额外标注。

### 🔧 技术方案

**问题背景：** 现有情感TTS偏好方法（Emo-DPO、EMORL-TTS、EASPO）只将条件轨迹推向"偏好"方向，未显式建模与非偏好情绪模式的分离；而扩散生成本质依赖 CFG 的对数似然比对比机制，这一对比通道被闲置，导致多情绪轨迹共存时情绪间判别力弱化、细粒度可控性受限。

**模型架构：** 骨干为 Grad-TTS，在 80 维 mel 频谱上运行；文本编码器与时长预测器全部冻结，仅更新扩散去噪解码器（ε 预测 score network），波形由预训练 HiFi-GAN 声码器重建。EA 分支拟合目标情绪条件得分场，EC 分支拟合备选情绪条件得分场，两者共享架构但参数独立。数据流为：同文本多情绪样本 → 构造有序对 (c,a1,a2) 与其反转 (c,a2,a1) → 双分支去噪训练 → 推理阶段合成噪声估计。模型规模沿用 Grad-TTS 预训练配置，论文未额外披露参数量。

**核心创新：** (1) 从分数模型视角揭示 CFG 是在对数似然比上做梯度上升，据此把 CFG 参考条件由"无条件"替换为"情绪对比条件"，显式建模情绪间梯度差、扩大情绪间隔，这是与所有单方向偏好方法的关键区别。(2) 双向偏好优化：对齐分支损失 ℒ_align 与对比分支损失 ℒ_ctr 均为标准去噪 MSE，分别形成吸引能量谷与排斥梯度，使情绪监督从现有情绪标注语料中自然涌现，不需辅助奖励模型与新数据。(3) 后期步引导调度：早期弱引导保留粗粒度声学结构、后期逐步增强引导细化情感韵律，实验证明优于固定值与早期调度（ω(t)=t/T 会在高噪阶段引发韵律退化与 WER 瞬时尖峰）。

**训练策略：** 训练数据为 ESD 英文子集（10 说话人 × 5 情绪 × 350 句 = 17,500 句，约 12 小时，按"说话人-情绪"8:1:1 划分）与 EmoVoiceDB（约 22,100 句，约 40 小时，用官方划分）；偏好对按 Emo-DPO 的文本匹配策略构造，目标情绪为首选、其他情绪为拒选。优化器 Adam，学习率 1e-4，batch size 16，输入随机裁剪 2 秒 mel 片段，属对预训练骨干的部分微调；论文未给出训练轮数与早停配置。

### 📊 实验结果
**数据集**：ESD 英文子集与 EmoVoiceDB 测试集（客观指标 3 次独立运行平均，主观评测 30 人，情绪类别均衡）

**主要指标**：
- 情绪相似度 Emo SIM：99.23（最强基线 EmoVoice 98.59，提升 0.64）
- 韵律相似度 Prosody SIM：3.85（CosyVoice2 3.78，提升 0.07）
- 可懂度 WER：3.84（CosyVoice2 3.77，劣化 0.07，仍具竞争力）
- 自然度 UTMOS：4.52（CosyVoice2 4.43，提升 0.09）
- 情绪识别准确率：Happy 0.82、Sad 0.87、Surprise 0.84，均值 0.87（CosyVoice2 0.82，提升 0.05）
- 主观 MOS / Emo MOS / MOS EC：3.93 / 4.25 / 3.92（CosyVoice2 为 3.61 / 3.93 / 3.75，分别高 0.32 / 0.32 / 0.17），AB 偏好测试明显胜出 EmoSpeech 与 CosyVoice2
- 消融：去对比分支 Emo SIM 降到 97.41、WER 升到 4.48；去后期调度 Emo SIM 98.76、WER 4.29；微调 Grad-TTS 基线仅 96.68 / 6.71

**是否开源**：论文仅提供 Demo 音频页 https://jiachengqaq.github.io/emo-bpo/，代码暂无；工作已被 Interspeech 2026 接收。

### ⭐ 评分：7/10
评分理由：把 CFG 的对比机制转化为可训练的情绪对比分支，视角清晰、方法简洁且零额外标注，工程上可即插即用注入现有扩散TTS。评测覆盖客观、主观、AB 偏好与双重消融，主要指标一致领先且与消融结论互证。不足是骨干限于 Grad-TTS 与两个英语中小规模语料，未在 LLM-TTS 或跨语种大数据验证泛化，且代码未开源、缺乏情绪强度连续旋钮与推理开销分析。

---

## [4] E3-System: Expressive EmoData, Explicitly Controllable, Easy-to-Use TTS

**arXiv ID**：2610.12993 | **方向**：语音大模型

**作者**：Yiqiao Huang, Xiaolong Lin, Zhenpeng Zhan, Zhizheng Wu

**机构**：Baidu Inc. 百度、Harvard University、The Chinese University of Hong Kong, Shenzhen

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.12993 | **PDF**：https://arxiv.org/pdf/2610.12993.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有零样本 TTS 中，文本描述缺乏声学锚定、语音风格提示词又把音色与风格耦合，导致语义意图到声学表现之间的鸿沟，无法兼顾表现力与可控性。论文提出 E3-System：用 EmoData（1012 小时、5681 说话人、6 语言 6 情感）、Style-RAG 检索、Dual-TTS 解耦合成形成完整控制环，双参考输入实现任意音色×风格迁移。零样本单参考下 WER 低至 2.33、SIM 74.82；双参考解耦下 SIM-Spk 达 70.15、SIM-Style 89.22，均超最强基线。

### 🔧 技术方案

**问题背景：** 零样本 TTS 复刻单参考时音色与韵律天然绑定，缺乏"任意音色×风格"的显式控制能力；GRL 类解耦方法存在音色/风格/内容泄漏，可控性与音质互相妥协。文本指令无声学锚定、语音提示需人工选样本，易用性与质量难两全。

**模型架构：** Dual-TTS 两阶段合成。Text-to-Semantic 采用 Dual-AR 解码器（Contextual-AR 12 层 + Fast-AR 12 层、hidden 4096、16 头、Fast-AR 做 2×下采样），说话人提示编码为全局嵌入控音色、风格提示编码为风格向量注入参考语义 token；Semantic-to-Acoustic 沿用 SoundStorm 式 mask 扩散，将语义 token 映射为声学 token 后解码；配合 disentangled codec 与解耦训练范式。Style-RAG 利用对比打分（CLAP 类）从 caption–wav 库检索最匹配风格参考。EmoData 经响度归一、重采样、商用级音源分离、说话人日志聚类、多 SER 模型（emotion2vec/OSUM/FunAudioLLM）置信度集成、语义-韵律双检过滤，覆盖 6 情感。

**核心创新：** (1) EmoData 千小时野外情感基准，自动化管线在规模上超 IEMOCAP/ESD 录音棚库同时保留棚级表现力，并实现语义-声学一致。(2) VC-augmented 解耦训练，构造伪 GT 时三重防泄漏——说话人提示用不同人避免音色泄漏、VC 目标换同说话人不同句避免内容泄漏、VC 音色参考用同人异风格避免风格泄漏；伪 GT SIM-Style 由 71.20 升至 92.85。(3) Style-RAG 用跨模态相似度把自然语言意图落地为高质量声学参考，免人工选样且不损失质量。

**训练策略：** 所有模型先在企业合规数据预训练、再在 EmoData 上微调；用 VC 扩生成伪 GT 并按 WER 与说话人相似度过滤。消融显示 2×下采样比单 AR 提速约 1.8×并略升质量，更大下采样率反而退化。正文未披露总轮数与 LR/优化器/batch 等具体超参，仅给出上述结构与阈值性约束。

### 📊 实验结果
**数据集**：EmoData（1012 h、5681 说话人、EN/ZH/JA/KO/DE/FR、44.1 kHz、6 情感）；评测 LibriTTS 采样 300 组说话人×风格提示。

**主要指标**：
- WER：双参考 Ours 2.51（无 RAG）／2.93（带 RAG），单参考 2.33
- SIM-Spk：70.15，超 Vevo-TTS 65.16、IndexTTS2 69.85、DisCo 63.68
- SIM-Style：89.22，优于 DisCo 87.25、IndexTTS2 86.73（GRL 版仅 72.50）
- SM-MOS 4.08、SN-MOS 3.98（双参考无 RAG 口径）
- EmoData 微调基线 CosyVoice 后 SIM-Style +6.12、SIM-Spk +2.36、WER −0.07；风格匹配率中性 95.20/愤怒 92.30/快乐 91.75

**是否开源**：正文未给出代码与 Demo 仓库，暂无。

### ⭐ 评分：7/10
评分理由：数据、检索、解耦合成三者闭环设计完整，VC 伪 GT + 三重防泄漏思路清晰且消融充分，双参考 SIM-Style 89.22 相对 SOTA 有实质提升。不足是模型规模/超参披露有限、EmoData 与权重均不开源且无 Demo，复现门槛高；野外版权与情感标注可靠性仍有隐忧。

---

## [5] AudioTETRIS: Token Elimination via Transitional Importance Signals for Efficient Audio LLMs

**arXiv ID**：2610.13600 | **方向**：语音大模型

**作者**：Shreya Sajid, Anna Vettoruzzo, Joaquin Vanschoren

**机构**：埃因霍温理工大学（Eindhoven University of Technology）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13600 | **PDF**：https://arxiv.org/pdf/2610.13600.pdf | **代码**：https://github.com/ShreyaSajid/AudioTETRIS | **Demo**：暂无

### 📌 简介
大音频语言模型（LALM）的编码器为几秒语音生成数百个token，自注意力二次方开销推高推理成本；现有免训练压缩仅凭粗粒度注意力或特征相似度剪枝，抹平了承载关键信息的音素过渡区。AudioTETRIS提出两阶段免训练框架：先从编码器中间层隐状态相邻帧平方L2距离导数构建音素过渡声学先验，再在LLM解码器内与深度自适应注意力分数相乘融合，于两个剪枝层做渐进式top-k选择。在Qwen2-Audio-7B上压缩率0.36时WER 4.52优于未压缩4.61；4×压缩（0.75）下WER 8.50、延迟1.31s降至0.62s，全面超越SpeechPrune等基线。

### 🔧 技术方案

**问题背景：** 语音信息密度集中于快速声学过渡而非稳态段，均匀token化本身冗余；但SpeechPrune依赖早期层注意力、LTBM依赖局部特征相似度，均将音频token视作各向同性特征，破坏音素级过渡细节，导致ASR等需精确词法恢复的任务在强压缩下急剧退化。

**模型架构：** 基座为Qwen2-Audio-7B（约8.4B，Whisper编码器）、Phi-4-Multimodal（5.6B，Conformer编码器）、Audio Flamingo 3（约8.3B）。编码器隐状态{h_t}∈R^{T×d}投影进LLM嵌入空间与query拼接；Stage 1在编码器中层（按峰度选层：Qwen2第16层、Phi-4第14层、AF3第15层）计算过渡先验w_t；Stage 2在解码器第1层与交叉层ℓ†两级剪枝，注意力矩阵A^(ℓ)按头数H聚合。

**核心创新：** (1) 音素过渡声学先验：d_t=‖h_t−h_{t−1}‖²归一化为单位均值权重w_t，作者用强制对齐验证其与真实音素边界Pearson相关r_soft达0.68，且峰度κ≈24–26.5可在无标注下选出最优先验层。(2) 深度自适应注意力打分：实测音频token占输入84.98%但早层注意力76.91%集中于音频内部、中晚层转向跨模态，故ℒ_early用intra-audio、ℒ_later用text-to-audio注意力，交叉层ℓ†由校准前向自动发现。(3) 乘性融合s_t=p̃_t·w_t使token存活同时受声学结构与任务语义约束，全免训练、可跨三种编码器架构迁移。

**训练策略：** 免训练，推理配置：压缩率0.36/0.51/0.64/0.75对应两阶段保留率r∈{0.8,0.7,0.6,0.5}（总保留1−r²）；诊断先验b_t对d_t做σ=2高斯平滑后裁剪[0,1]；每基座仅需一次校准前向定位ℓ†；注意力后端用可输出权重的SDPA并处理RoPE重索引与KV-cache裁剪；单卡A100；基线复用公开超参并在同一剪枝调度下匹配压缩率。

### 📊 实验结果
**数据集**：LibriSpeech test-other（ASR）、IEMOCAP（情感识别）、MMAU-mini（音频QA）、CoVoST 2英中语音翻译

**主要指标**（Qwen2-Audio-7B）：
- WER：压缩0.36时4.52，优于未压缩4.61；0.75时8.50，最低（SpeechPrune 9.75，差值−1.25；随机剪枝31.59）
- 准确率：0.36时IEMOCAP 58.04（未压缩55.11，+2.93）、MMAU-mini 42.36；0.75时CoVoST2 BLEU 31.33，SpeechPrune跌至25.77（差值+5.56）
- 效率：0.75压缩下延迟1.31s→0.62s，总TFLOPs 7.89→4.32
- 消融：0.75时仅用Stage 2的WER为15.56，两级融合8.50；L2距离优于余弦（5.77 vs 9.04 WER）
- 泛化：Phi-4-Multimodal与AF3上0.51压缩时WER与未压缩差距均在1点内

**是否开源**：代码将于 https://github.com/ShreyaSajid/AudioTETRIS 发布（论文承诺release）

### ⭐ 评分：7/10
评分理由：将编码器表示几何作为声学前验传播进解码器的思路新颖且动机充分，强制对齐相关性与峰度双重验证、三基座四任务的实验较扎实，并给出训练-free方法中少见的效率量化。不足在于ASR在4×压缩下WER近乎翻倍，跨英语外与噪声条件未验证，且ℓ†仍需每基座一次校准，非完全零样本，整体属高质量增量贡献。

---

## [6] Does Location Matter? A Black-Box Causal Audit Reveals Model-Dependent Audio Grounding in LALM Hallucination

**arXiv ID**：2610.13112 | **方向**：语音大模型

**作者**：Mohammad Khalooei, Mohammad Sabokrou

**机构**：Sharif University of Technology、Amirkabir University of Technology（伊朗）；New Uzbekistan University（乌兹别克斯坦）；Okinawa Institute of Science and Technology（日本）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13112 | **PDF**：https://arxiv.org/pdf/2610.13112.pdf | **代码**：https://github.com/khalooei/causa | **Demo**：暂无

### 📌 简介
LALM 常幻觉出不存在的声音事件，现有 AAD 方法用全零"blank"波形做对比，但 blank 分布外，混淆了"证据缺失"与"输入畸形"。本文提出 CAUSA 黑盒因果审计：用滑窗 CLAP 定位 claim 依赖的时频谱区，STFT 频谱门控仅剔除该区域，与等尺寸随机窗口、blank、纯语言先验对照，在 Qwen2-Audio-7B、Audio Flamingo 3、Qwen2.5-Omni-7B 上验证。关键结果：blank 的检测优势（AUROC 0.721 vs 0.613）实为时长混淆，固定时长后局部剔除全面胜出；组合对比解码将 Qwen2-Audio 准确率从 57.1% 提升至 71.9%。

### 🔧 技术方案

**问题背景：** AAD 等推理期缓解方法以全零波形为对比基线，该输入对音频编码器分布外，其 logit 差同时反映"证据不存在"和"输入损坏"两种效应，无法判断模型是否真在依赖局部声音证据；已有白盒因果工作需梯度或内部激活访问，闭源模型不可用。

**模型架构：** 免训练黑盒管线，被测模型为 Qwen2-Audio-7B-Instruct（主）、Audio Flamingo 3（Whisper 式编码器 + Qwen2.5-7B 解码器）、Qwen2.5-Omni-7B。定位模块用 LAION-CLAP 对 2s/4s 滑窗（0.5s hop）与目标声学文本算相似度取峰值区间 R(o)；干预模块为 STFT 掩码频谱门控，在 R(o) 内衰减 −40/−100 dB，边缘 50 ms 升余弦淡入淡出，其余波形不动。评分单次前向取 "yes/no" 下一 token 对数概率重归一化为 P(yes)，确定性无采样。

**核心创新：** (1) 必要性局部剔除加严格对照：等尺寸随机窗、blank、无音频的语言先验、真实无关音频替换四组对照，并用"充分性测试"（向负样本混入真实例证验证翻转）保证管线灵敏度。(2) 将 Pearl 的 PN/PS 从二值推广为分级曲线：嵌套删除前 ⌈rK⌉ 个窗，定义最小必要删除比例 R*、NAUC 与配对定位效率 Δloc=E[R*_rand−R*_clap]，并诊断出 blank 优势是时长混淆——仅用随机窗拟合"删除时长占比→P(yes) 下降"的线性回归即可几乎精确预测 blank 效应（预测 0.067 vs 实际 0.071）。(3) 合成 oracle 定位对照与解码期修正：把已知插入位置的例证混入负样本后删 oracle/CLAP/随机三窗，分离"模型不依赖局部"与"CLAP 定不准"两种零结果；解码端复用已算 logit，将 AAD 的 blank 对比与语言先验对比加权组合并按置信度门控、先验取 5 条改述平均。

**实验配置：** 数据为 AudioCaps/ESC-50/VocalSound 组成的 object-existence 判别式 QA，10,800 行、53 类；Qwen2-Audio 抽 n=5000（seed 42）得 4355 条肯定 claim（2488 正确/1867 幻觉，43% 过度断言率），AF3 用全量 n=10,800 得 1192 条，Qwen2.5-Omni n=2000 得 1774 条。R* 估计用 6 个检查点（累积 1/2/4/7/11/17 窗，约 6%→全覆盖 10s clip）、−100 dB、首次翻转为止。解码对比扫 α∈[0,3]，报告 α=1 文献标准值；显著性用 Wilcoxon、2000 次重采样 95% CI、5 折交叉验证。

### 📊 实验结果
**数据集**：AudioCaps/ESC-50/VocalSound object-existence 幻觉基准（10,800 行、53 类，音频中位 10s）

**主要指标**：
- 检测 AUROC（n=4355）：CAUSA 5 特征 ensemble 0.743，高于 AAD blank 基线 0.721（+0.022）；单格局部剔除 0.613 vs 随机窗 0.577
- 固定时长配对：P(yes) 均值下降 0.041 vs 0.016（Qwen2-Audio，p=4.8×10⁻⁴⁶）、0.393 vs 0.233（AF3）；Δloc=0.028（CI [0.023,0.033]）
- Oracle 控制：翻转率 oracle 16.8% / CLAP 10.5% / 随机 3.1%，CLAP 与真实位置 IoU 仅 0.45
- 解码准确率：Qwen2-Audio 57.1%→LangPrior-CD 68.2%（+11.1）、AAD-CD 64.7%（+7.5）、组合+门控+ensemble 先验 71.9%（+14.8）；AF3 各法均停滞于 93.0% 上限，CAUSA-CD 反降 3.4pp；跨模型 profile 迁移为负（Qwen→AF3 −1.4pp，AF3→Qwen −13.1pp）

**是否开源**：代码已开源 @ https://github.com/khalooei/causa

### ⭐ 评分：7/10
评分理由：时长混淆诊断与 oracle 定位控制方法学扎实，把因果可解释性检验做成了纯黑盒并给出诚实的负结果（profile 不跨模型迁移），解码端免训练提升显著且带交叉验证。局限是仅三个 7B 级模型、限于二值存在性问答、定位强烈依赖 CLAP 质量、AF3 小样本功效不足，属增量但可靠的实质贡献。

---

## [7] OpenSVBench: Diagnosing Speaker Verification Generalization Across Deployment Scenarios

**arXiv ID**：2610.13760 | **方向**：语音大模型

**作者**：Qituan Shangguan, Bosen Xu, Shuai Wang

**机构**：南京大学智能科学与技术学院（苏州）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13760 | **PDF**：https://arxiv.org/pdf/2610.13760.pdf | **代码**：https://github.com/shangguanqituan/opensvbench-submission-kit | **Demo**：https://opensvbench.xyz/

### 📌 简介
说话人验证（SV）系统在VoxCeleb等标准协议上错误率已极低，但单一聚合分无法刻画多场景部署泛化。本文提出OpenSVBench跨场景SV诊断基准：以16个公开语料构建固定核心，含26个trial集、11个场景组、共915万验证对，冻结目标/非目标密钥与元数据，并配套提交套件与在线榜单输出trial集分解、场景画像与宏EER/minDCF。评测18个公开checkpoint：最优W2V-BERT2宏EER 9.96%，但最强模型在genre-shift与口音/方言场景EER仍达26–27%与20–22%，证明宏分数会掩盖不同失败模式。

### 🔧 技术方案

**问题背景：** SV进展主要用VoxCeleb1-O/E/H锚点评测（如w2v-BERT 2.0报0.14% EER），而真实部署存在短语音、远场、声道/设备、噪声混响、重叠、口音、耳语、老化时长间隔等注册-测试失配；CN-Celeb、3D-Speaker、SVeritas等评估偏场景特定，缺少统一的跨场景泛化视图。

**基准设计：** 16个公开源（VoxCeleb、CN-Celeb、3D-Speaker、FFSVC、TidyVoiceX2、GLOBE、HI-MIA、VOiCES、AliMeeting、CHiME-6、Whisper40、Lombard、ESD、VoxKnesset、VoxPopuli、GSC）组织为26个trial集、11个场景组（跨语言、短时长、体裁偏移、口音/方言、in-the-wild媒体、声道/设备、说话风格、距离、噪声/混响、重叠、老化），含110.5万目标对与804.6万非目标对，共9,150,366 trials；采用官方/过滤/构造三种协议并以校验和冻结。

**核心创新：** (1) trial集+场景组两级报告框架，把常见锚点协议与条件化trial集统一到同一场景结构下，宏分与逐场景画像同时可见。(2) 提交套件+在线诊断榜单：新系统提交分数包，用冻结密钥与统一评分协议评测，输出场景组指标、宏EER/minDCF、模型画像与跨场景对比，使基准成为可持续诊断平台。(3) 条件元数据诊断：按时长/重叠严重度分箱定位失败驱动，并用同场景trial对间Spearman秩相关量化组内源/协议鸿沟（如in-the-wild组CN-Celeb vs VoxCeleb1-E仅ρ=0.13）。

**评测协议：** 音频16kHz单声道，长语音切非重叠块后embedding平均+L2归一化，余弦打分，不用PLDA/评分归一化/校准；EER阈值扫描，minDCF取P_tar=0.05、Cfa=Cmiss=1；场景分先按源内trial集平均、再跨源、再对11组宏平均的源平衡聚合，避免大trial集主导。

### 📊 实验结果
**数据集**：OpenSVBench固定核心（9,150,366 trials）；评测对象为18个公开SV checkpoint（x-vector、ECAPA-TDNN、CAMPPlus、ResNet/ERes系、ReDimNet2、SAM-ResNet、W2V-BERT2/WavLM/UniSpeech系）。

**主要指标**：
- 宏EER：W2V-BERT2 9.96%居首，ReDimNet2 10.53%、SAM-R100 10.58%
- 宏minDCF：W2V-BERT2 0.361、SAM-R100 0.390
- 最弱基线：x-vector 23.35%、UniSAT-SV 25.67%，比最优差13.39–15.71个百分点
- 最难场景：genre-shift均值27.36%、口音/方言24.76%；声道设备/短时长/重叠/距离为15.49–17.58%次高簇
- 条件诊断：CN-Celeb Short从0.5s的36.1%降至3s的15.6%；CHiME-6重重叠EER 30.0%
- 稳定性：1万次场景bootstrap下W2V-BERT2 84.3%保持第一、99.4%居前三

**是否开源**：提交套件代码已开源（github.com/shangguanqituan/opensvbench-submission-kit），榜单@opensvbench.xyz；不重新分发源音频，提供各语料下载脚本；已被NCMMSC 2026接收。

### ⭐ 评分：7/10
评分理由：以冻结核心加可提交诊断榜单为SV部署泛化提供统一评测框架，"模型在genre-shift仍~27% EER""同场景组内秩相关低至0.13"等发现具实用诊断价值，bootstrap与去源检验较严谨；但仅评测成品checkpoint、无受控训练对比，部分场景组依赖单一源覆盖不均，属扎实增量基准工作而非方法突破。

---

## [8] OpenPA: Forced-Alignment-free Multi-granular Pronunciation Assessment with Mixed-transcript Adaptation

**arXiv ID**：2610.13826 | **方向**：语音大模型

**作者**：Fu-An Chao, Bi-Cheng Yan, Berlin Chen

**机构**：台湾师范大学（National Taiwan Normal University，台北）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13826 | **PDF**：https://arxiv.org/pdf/2610.13826.pdf | **代码**：https://github.com/fuann/open-apa | **Demo**：https://fuann.github.io/open-apa/audios/（定性音频样例）

### 📌 简介
本文提出OpenPA：一个基于Whisper-medium的统一词级/句级双粒度发音评估框架，通过在每个词后插入<score>token并利用cross-attention直接检索声学证据，彻底摆脱强制对齐；再借混合转录适配与自适应替换加权，使单一模型同时鲁棒于真值转录与含ASR错误的转录。仅用speechocean762训练，域内模拟开放作答下取得最高词级M+S PCC 0.544与句均PCC 0.787，MultiPA零样本韵律PCC达0.644（较最强对齐基线+0.171），口腔癌语音跨任务零样本说话人级PCC 0.82。

### 🔧 技术方案

**问题背景：** 传统自动发音评估面向有参考答案的朗读封闭作答，依赖"强制对齐+异构特征提取器+独立打分组件"的多级级联；开放作答场景没有人工转录、只能用ASR假设，对齐误差会沿级联传播，阻碍端到端联合优化与跨场景部署，且细粒度标注数据极度稀缺。

**模型架构：** 以Whisper-medium为骨干。将增强token序列teacher-force进解码器，每个词最后一个BPE token后插入特殊<score>token（类比BERT的[CLS]），其解码器隐状态经cross-attention汇聚完整声学encoder状态、经因果self-attention汇聚词表前缀，构成词级表示，由方面特定回归头g_k输出各发音维度词级分；句级用一个轻量双向Transformer encoder层上下文化词表示，再按HiPAMA式方面特定attention pooling聚合为u_k，经回归头f_k给出句级分。双粒度共享同一骨干，句级预测建立在词级证据之上。

**核心创新：** (1) 免对齐打分：score token直接attend整个encoder序列定位发音证据，无需外部词级时间戳；定性分析显示即便ASR把person替换成pizza，先前词的注意力模式与分数仍保持稳定。(2) 混合转录适配：训练时按(0.5,0.3,0.2)概率采样真值、S&I语料微调的L2-ASR（训练集WER 18.5%）、Whisper medium.en（WER 21.6%）三种转录做teacher forcing，单模型覆盖闭合与开放作答。(3) 自适应替换加权：Levenshtein映射仅用于构造目标——替换词继承参考词分数、插入词屏蔽；对ASR替换词按人工词准确度a_i赋权ω=0.5+0.5·(1−a_i/10)，放大真实发音偏差损失、抑制疑似识别错误的贡献。

**训练策略：** 仅用speechocean762（250名中文母语非英语者多粒度标注朗读语料）；整个Whisper加rank-16 LoRA适配器联合任务打分模块微调，5 epochs，batch size 64，学习率8×10⁻⁴；损失为λ_ASR·token级CE（保留ASR生成能力与预训练表示）+ λ_word·加权MSE + λ_utt·MSE的联合目标。

### 📊 实验结果
**数据集**：speechocean762（域内闭合+模拟开放）、MultiPA（50条真实开放应答，零样本跨数据集）、YouTube口腔癌语料PathBench子集（98条/21人，零样本跨任务）

**主要指标**：
- 域内（Qwen3-ASR-0.6B转录）：词M+S PCC 0.544，句均PCC 0.787，总体平均PCC为所有对比系统最高
- 替换词鲁棒性：GT-only训练S条件PCC仅0.076–0.152，混合适配+自适应权重提升至0.333（medium.en 0.118→0.295）
- MultiPA零样本：句级韵律PCC 0.644，较最强基线MultiPA*（0.473）提升0.171，词/句两粒度均优于多PA*与LLM方案TextPA
- 跨任务：说话人级PCC 0.82，高于ASRIC、DArtP、ArtP等参考基线

**是否开源**：评测代码已开源 @ https://github.com/fuann/open-apa，附音频demo页

### ⭐ 评分：7/10
评分理由：首个免强制对齐的词级+句级联合发音评估框架，用Whisper cross-attention做"软对齐"思路简洁且经跨任务证据支撑；混合转录与自适应替换加权直击开放作答下ASR错误迁移痛点，消融充分。不足：仅在小规模speechocean762上训练，句级流畅度/韵律仍略逊带专用超音段特征的HiPPO，跨数据集测试集规模偏小。

---

## [9] Input Representation, Not Model Size or Pretraining Scale, Shapes Speaker Verification Robustness to Temporal Degradation

**arXiv ID**：2610.12539 | **方向**：语音大模型

**作者**：Erdem Baha Topbas, Srikanth Madikeri, Elisa Pellegrino, Volker Dellwo

**机构**：苏黎世大学计算语言学系（University of Zurich）；NTT（日）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.12539 | **PDF**：https://arxiv.org/pdf/2610.12539.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语音在重度过渡性退化（如无限峰值削波）下人耳仍可听懂，但说话人身份能否存续此前几乎未被研究。本文构造PER、PER+ENV、PER+TFS三种时域分解退化条件，在卷积/Transformer/Conformer三架构族中配对6个音频大模型ASV系统（波形输入对mel滤波器组输入），训练仅用时域完整语音。结果显示鲁棒性跟输入表征走而非模型规模或预训练量：9/9家族×条件对比中filterbank输入组退化更少，8/9的95%CI不含零；受控卷积对中ResNet34 EER由1.1%升至17.1%，ResNet1D为2.9%升至29.7%；恢复TFS平均找回10.94个百分点EER，而恢复包络只有1.32。

### 🔧 技术方案

**问题背景：** 心理声学研究证明听者可在缺失慢调制或精细结构的语音中保持理解力与部分说话人识别能力，但ASV系统能否在同类重度退化条件下守住说话人身份未知；且既有鲁棒性研究中模型规模、预训练量与输入表征三个因素相互纠缠，无法归因。

**模型架构：** 六模型按架构族组成三对：卷积ResNet1D（6.20M，波形）与ResNet34（6.63M，filterbank）；Transformer WavLM-large（319.1M，94k小时预训练）与Speech2Text（158.9M，1k小时）；Conformer Wav2Vec2-Conformer（617.6M，960小时）与w2v-BERT 2.0（581.8M，4.5M小时）。全部经时序统计池化（TSTP）输出256维说话人嵌入。

**核心创新：** (1) 三条件时域成分隔离：PER用IPC逐样本取符号仅留周期性；PER+ENV将Hilbert包络经四阶Butterworth 30Hz零相位前后向滤波后按0.01×最大值下限截断并与IPC相乘；PER+TFS用x[n]/ENV[n]除尽幅度包络仅留振荡，三对条件互补对照。(2) 跨规模/预训练的配对对照框架：每对内波形与filterbank模型严格对比，卷积对训练数据与日程完全相同仅差输入表征，且各对中filterbank侧参数更少（预训练对差100至96000倍）仍更鲁棒，直接证伪规模假说。(3) 头部空间归一化退化指标D=(EER_cond−EER_base)/(50−EER_base)×100，解决基线EER差异导致的绝对变化不可比；说话人级配对bootstrap（2000次重采样）判显著，明确拒绝trial级伪重复。

**训练策略：** VoxCeleb2上2秒随机裁剪训练，MUSAN加性噪声与RIR卷积混响以60%概率增强、噪声SNR随机0~20dB。卷积族按WeSpeaker配方从头训练150轮；四个预训练模型用LoRA适配（rank 16、alpha 32）。统一AAM-Softmax损失（scale 32.0，margin 0.2），margin仅在训练准确率过80%阈值后启用（卷积两模型与w2v-BERT 2.0达标）。

### 📊 实验结果
**数据集**：VoxCeleb2训练，VoxCeleb1-O试次对评测（condition-matched）

**主要指标**：
- EER：受控卷积对PER条件 ResNet34 1.06%→17.09% vs ResNet1D 2.90%→29.74%
- ΔEER（PER）：w2v-BERT 2.0仅8.28（归一化17.0）vs Wav2Vec2-Conformer 34.90（归一化76.5），同为581M/618M参数、预训练反而多4700倍
- 恢复TFS平均找回10.94个百分点EER，恢复ENV仅1.32，六模型全部TFS>ENV
- 9/9家族×对比中filterbank侧退化更少，8/9的95%CI不含零
- PER条件波形侧5次评测minDCF超0.95接近随机判决
- 方法学：说话人级CI宽度中位数为trial级的5.97倍，trial级重采样会大幅高估精度

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：首次将时域成分分解与ASV鲁棒性结合并用严格配对设计归因输入表征，挑战"规模与预训练决定鲁棒性"的直觉，统计分析克制（拒绝伪重复、头部空间归一化）是亮点，对语音大模型前端表征选择有直接工程警示。不足在于仅VoxCeleb1-O一个评测集、机制解释停留在定性论证，属扎实的增量分析型工作（投稿 ICASSP 2027）。

---

## [10] Oído: Open-Vocabulary Speech Recognition on a $5 Microcontroller without a Neural Accelerator

**arXiv ID**：2610.13447 | **方向**：语音大模型

**作者**：Daniel Varela Sánchez, Guillermo Martín-Coello Juárez

**机构**：Lokutor（Hashing Works, S.L.L.），西班牙马德里

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13447 | **PDF**：https://arxiv.org/pdf/2610.13447.pdf | **代码**：https://github.com/lokutor-ai/oido | **Demo**：暂无

### 📌 简介
低成本单片机ASR长期只能做关键词唤醒或固定命令表。本文的Oído推理引擎在无神经加速器的ESP32-S3（240MHz双核Xtensa LX7、512KB SRAM、8MB PSRAM）上以int8运行13M参数Conformer-CTC，实现端到端开放词汇英语识别。LibriSpeech test-clean/other机载WER 3.70%/8.23%，与全精度差仅0.12点；叠加片上1.3M语言模型降至3.33%/7.15%，误差比同芯片厂商识别器少2.3-2.8倍，也低于笔记本上全精度Whisper tiny与Moonshine tiny。真机单核RTF 1.97尚非实时，代码与模型全部开源。

### 🔧 技术方案

**问题背景：** 单片机只有KB级SRAM与低速PSRAM/flash，无矩阵加速单元，主流方案要么缩小到命令词表，要么把音频传云端；开放词汇端到端识别的算力与内存需求被认为不切实际。难点不在模型规模而在Xtensa SIMD指令上的int8算术吞吐与flash/PSRAM带宽调度。

**模型架构：** 13M参数Conformer-CTC，int8权重、逐帧动态int8激活、int8注意力，全部算子围绕40/80/160MHz flash与PSRAM带宽设计调度；另有1.3M参数片上AR语言模型做浅融合 rescoring，以及transducer(RNNT)头替代CTC解码；int4权重变体可压缩到8.3MB flash。

**核心创新：** (1) 首个在无NPU商用$5 MCU上的完整开放词汇ASR引擎，逐算子手工量化与内存调度使int8与全精度误差差仅0.12 WER点。(2) 双核调度实证失败并诚实报告：两核版本在真实芯片上产出错误结果而被禁用，固件输出与指令精确模拟器逐条一致。(3) 流式变体边说边出部分文本，3.6-10.6s音频在4.1-11.1s后交付最终文本（WER 4.86%/11.03%）；另训练西班牙语模型，较同尺寸多语Whisper tiny错误少34-60%。

**训练策略与推理细节：** 英语模型基于LibriSpeech 960h训练；量化以逐帧动态激活标定，评测含真实噪声与混响条件；固件在物理开发板实测，与模拟器输出做instruction-exact一致性校验；代码、模型与原始板级测量数据均公开。

### 📊 实验结果
**数据集**：LibriSpeech test-clean/test-other（含真实噪声/混响实测），西班牙语子实验

**主要指标**：
- 机载int8 WER：3.70%/8.23%，与全精度差0.12点；+1.3M片上LM 3.33%/7.15%；transducer头2.99%/6.67%
- 对比同芯片厂商识别器：错误少2.3-2.8倍；优于全精度Whisper tiny.en与Moonshine tiny（笔记本）
- 实时性：单核RTF 1.97（4s命令约8.7s后出文本，尚未实时）；int4变体占用8.3MB flash
- 流式：4.86%/11.03% WER，最终文本延迟4.1-11.1s
- 西班牙语：比多语Whisper tiny错误少34-60%

**是否开源**：代码与模型已开源 @ https://github.com/lokutor-ai/oido

### ⭐ 评分：6/10
评分理由：在无加速器商业MCU上落地开放词汇ASR是罕见且可复验的系统工程贡献，实测纪律（模拟器逐指令一致、双核失败如实披露）与全开源提升可信度与实用价值。不足是RTF 1.97尚未达标称实时、仅英语为主、精度对比基线偏弱，属端侧部署方向的增量但扎实的工作。

---

## [11] Frontend-Assisted Large Audio-Language Models for SLT2026 SmartGlasses Challenge

**arXiv ID**：2610.13282 | **方向**：语音大模型

**作者**：Yushi Wang, Zeyan Song, Xiaobin Rong, Chengwei Liu, Jun Gao, Jing Lu

**机构**：南京大学现代声学重点实验室、南大-地平线智能音频实验室（Horizon Robotics）、阿里巴巴Qwen业务单元

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13282 | **PDF**：https://arxiv.org/pdf/2610.13282.pdf | **代码**：暂无（基于开源 SoulX-Transcriber 构建） | **Demo**：暂无

### 📌 简介
针对智能眼镜四通道录音中双人对话的语音重叠、远场与背景干扰导致的带时间戳说话人归属ASR（TSA-ASR）难题，本文在开源多模态大模型 SoulX-Transcriber（Qwen3-Omni 底座）基础上搭建三套系统：直接使用、加装规则式引导源分离（GSS）前端、加装数据驱动多通道 DPRNN 分离前端。在官方验证集上，微调版 tcpCER 从原始 9.02 降至 7.82，GSS 与 DPRNN 前端进一步压到 6.97/7.04，明显优于组织方基线 VibeVoice-ASR 的 14.09；最终提交稳定性最好的微调系统，测试集 tcpCER 为 6.22。

### 🔧 技术方案

**问题背景：** 现有端到端 LLM 转录系统（MOSS、VibeVoice-ASR、SoulX-Transcriber 等）把整段混叠音频直接丢给后端大模型，未显式建模或分离重叠语音，且多为单通道设计，浪费了智能眼镜麦克风阵列的空间信息。

**模型架构：** 后端 SoulX-Transcriber 由 30B 参数 MoE Thinker 与 0.6B AuT 音频编码器组成，输入全长音频、自回归输出带时间戳与说话人标签的结构化转写。System 2 以 DiariZen+ChannelAttention 多通道说话人日志模型产出的说话人级 VAD 引导 GSS：STFT→WPE 去混响→CACGMM 掩码→MVDR 波束成形，轮流提取佩戴者与对话者两路单说话人音频独立解码再合并。System 3 的 DPRNN_mc（仅 4.7M 参数）对四通道 STFT 做 ERB 滤波降冗余、分通道编码后融合，经 Dual-Path RNN 块预测两路复数时频掩码，重建出两条单通道流送入后端。

**核心创新：** (1) 首次把规则式目标说话人提取（GSS）与神经多通道分离（DPRNN_mc）两条前端路线与长上下文音频大模型在同一 TSA-ASR 基准上系统对比，并揭示前端失真与零填充静音区会加剧 LLM 幻觉（重复 token、时间戳漂移），需配合微调与分段推理缓解。(2) DPRNN_mc 采用复数谱 MSE + 幅度谱 MSE + 时域 PMSQE 感知损失的加权组合，并对对话者流以 2 倍权重（L_total = L1 + 2·L2）抑制干扰泄漏，且用 VAD 将非活跃区置零。(3) 用约 33 小时赛题真实数据即可通过 LoRA 有效适配大模型，验证小样本域适应对 TSA-ASR 的性价比。

**训练策略：** 对 SoulX-Transcriber 做 LoRA 监督微调，rank=8、缩放因子 α=32；System 2/3 先用前端处理赛题训练集再微调后端。DPRNN_mc 用 CHiME-8 MMCSG 的 Aria 眼镜真实 RIR、MCAS 仿真 RIR 与按赛题麦克风布局生成的仿真 RIR 训练，语音与噪声取自 URGENT 挑战赛数据。推理配置 temperature=0.2、top-p=0.9、top-k=-1、repetition penalty=1.05；全部实验在 4 张 48GB NVIDIA 4090 上完成。

### 📊 实验结果
**数据集**：SmartGlasses Challenge Track 1 官方验证集与测试集（四通道智能眼镜双人对话，约 33 小时训练语料），另用 CHiME-8 MMCSG/MCAS/URGENT 数据做分离仿真。

**主要指标**：
- 基线 VibeVoice-ASR：tcpCER 14.09，cpCER 12.88，DER 17.24
- System1 原始 SoulX：tcpCER 9.02；微调后 7.82（DER 3.70→2.56）
- System2 GSS-SoulX（估计 VAD）：tcpCER 6.97，cpCER 6.12
- System3 DPRNN_mc-SoulX（oracle VAD）：tcpCER 7.04，DER 低至 0.15
- 最终提交（测试集）：tcpCER 6.22
- 对比最强公开基线：验证集 tcpCER 降低约 7.12（6.97 vs 14.09）；重叠率越高前端优势越明显（High 组重叠 12.0%-22.8%）

**是否开源**：暂无官方代码发布，依赖开源 SoulX-Transcriber 与 DiariZen 模型。

### ⭐ 评分：6/10
评分理由：作为 SLT 2026 挑战赛系统报告，三套系统独立评测、oracle/估计 VAD 双设定与重叠率分组分析使前端消融相当扎实，测试集 6.22 tcpCER 有竞争力；诚实披露了前端处理诱发 LLM 幻觉这一真实问题，具工程参考价值。但方法本身是 GSS/DPRNN/LoRA 等已有组件的装配，无新架构贡献，数据仅 33 小时、未在公开数据集交叉验证，且最终提交的恰恰是不用前端的最稳系统，削弱了核心论点的说服力，属增量型工作汇报。

---

## [12] TTS-Q: Perception-Guided Post-Training Quantization of Text-to-Speech Diffusion Transformers

**arXiv ID**：2610.12474 | **方向**：语音大模型

**作者**：Xiaoqin Feng, Yuqi Li, Weilun Feng, Yi-Cheng Lin, Kai Li, Xianglong Wang, Kuo Yang, Chuanguang Yang, Yingli Tian, Wei Li, Zhongwei Cheng, Lin Chen

**机构**：arXiv未提供

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.12474 | **PDF**：https://arxiv.org/pdf/2610.12474.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
十亿参数级零样本TTS扩散Transformer难以端侧部署，而现有PTQ方法面向语言与图像视频设计，4-bit权重激活联合量化（W4A4）在语音上呈现特失效模式：可懂度几乎不掉但说话人音色明显漂移。本文首次对1B/3.5B的LongCat-AudioDiT做系统W4A4研究，诊断出音色损伤集中于后期采样步FFN的激活侧，提出TTS-Q：任务镜像构造校准候选、损失引导选择最难量化样本、预算均衡的late-FFN混合精度（末5步FFN激活A9、其余A3、权重保持W4）。留出集上较同预算最强基线三子集合计SIM提升+0.0046/+0.0041且不增名义比特；部署用校准W4A4使GPU峰值内存降低2.1至3.6倍。

### 🔧 技术方案

**问题背景：** SmoothQuant、QuaRot、FlatQuant、ViDiT-Q等PTQ配方均在LLM或图像视频扩散上调优，从未在TTS DiT上验证；语音在W4A4下的损伤落在语音专有的音色轴上，且"对拟合最差块加强校准"或"直接优化说话人相似度"的直觉修复被本文实验证伪，因为受损位置并不承载说话人音色。

**模型架构：** 量化对象为LongCat-AudioDiT两尺度：1B（24层block）与3.5B（32层block），每block含self-attention、以文本为条件的cross-attention与FFN；推理走16个ODE节点（S=15步显式Euler）流匹配采样，配APG自适应投影引导，latent经VAE解码为音频；量化器采用FlatQuant块式重建，学习变换与激活裁剪参数，权重W4对称per-output-channel、激活A4动态per-token非对称，每块200次重建迭代。

**核心创新：** (1) 任务镜像校准池：仅用目标语向任务形态比例、prompt时长、文本长度等聚合描述子，从AISHELL-3与LibriTTS构造376条/158说话人的外部池，prompt与target跨说话人交叉配对，与评测集完全无交叠，再切成3组互斥、各32条的候选集。(2) 损失引导选择：在FlatQuant初始化态下按steps {0,14}计算各候选逐块量化输出与FP输出的平均MSE，保留最难量化的32条lossmax样本（两尺度独立排序），并取steps {13,14}的块输入与条件成64个快照拟合统一W4A4量化器。(3) 结构对齐精度分配：基于音色损伤集中于后期采样FFN激活的诊断，推理时权重固定W4，最后K=5步FFN激活升至A9、其余激活位降至A3，按参数量加权名义比特（1B为4.000、3.5B为3.947）匹配uniform A4预算，位置在开发集上冻结后再评测。

**训练策略：** 无需重训模型，仅离线学习每块重建变换/裁剪参数，重建MSE损失、200次迭代每块、64快照；以seed 20260718从基准抽样300/100/200（zh/hard/en）固定开发子集确定task-best、快照放置与分配放置，判据为跨尺度summed-SIM增益并拒绝文本退化方向，K=5为早窗对晚窗的方向性对照宽度而非扫参结果；同生成种子严格配对同一批音频评测。

### 📊 实验结果
**数据集**：Seed-TTS-eval留出余量：1,720条普通中文、300条困难中文、888条英文；CER用Paraformer-zh、WER用Whisper-large-v3，SIM取WavLM-large加ECAPA-TDNN头256维说话人嵌入余弦相似度。

**主要指标**：
- 1B全精度基线：SIM（zh/hard/en）0.8119/0.7901/0.7632，CER（zh/hard）1.193/6.888
- 崩溃性基线：RTN/GPTQ在1B直接崩溃（zh CER 104.6/102.1，GPTQ SIM en仅0.2001）
- 最强基线FlatQuant+lossmax（uniform W4A4）：1B SIM 0.8091/0.7873/0.7554；3.5B SIM 0.8175/0.7985/0.7796
- TTS-Q：1B SIM 0.8109/0.7884/0.7571、CER/WER 1.205/6.752/2.156；3.5B SIM 0.8189/0.7979/0.7829、CER/WER 1.157/6.009/1.918
- 与最强基线差值：合计SIM +0.0046（1B）/+0.0041（3.5B），六项对比五项提升，全部文本指标变化不超过0.105个百分点；已部署W4A4峰值内存降2.1至3.6倍，但INT4路径延迟并非全面更快

**是否开源**：暂无（论文未给出代码/Demo链接，评测复用开源Seed-TTS-eval工具链）

### ⭐ 评分：6/10
评分理由：首次系统研究TTS DiT的W4A4量化并给出"音色损伤集中于后期FFN激活"的可迁移诊断，对照实验设计严谨、结论表述克制。不足是恢复幅度小（合计SIM仅+0.004量级）、无主观MOS验证、混合精度未带来实测加速，工程收益有限，属有参考价值的增量工作。

---

## 语音前端

## [1] Phonology-Aware Speaker Extraction Frontend for Audio LLMs

**arXiv ID**：2610.13500 | **方向**：语音前端

**作者**：Yanxiang Chen, Haoyuan Deng, Jinyu Wang, Hongyi Chen, Dingshan Li, Runlin Huang, Weifeng Su

**机构**：中山大学（珠海）、复旦大学、北师港浸大（珠海）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.13500 | **PDF**：https://arxiv.org/pdf/2610.13500.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对固定深度目标说话人提取（TSE）在多语种混合语音上"难样本处理不足、易样本算力浪费"的矛盾，本文提出5.2M参数的音系感知自适应前端LATTE，由声学Difficulty Estimator、任务自适应phonology-informed prior（PDI）与共享多出口Adaptive Hourglass Extractor（2/4/6块三档出口）组成，推理无需语言标识。在自建PolyExtract上以0.30 GFLOPs取得15.07 dB宏SI-SNRi，较固定深度模型仅损失0.09 dB而算力降43.4%；接入冻结Qwen3-Omni后平均WER从TF-GridNet的16.8%降至14.6%。

### 🔧 技术方案

**问题背景：** 不同语言的声调、发声态、节奏差异显著改变混合语音的提取难度，固定深度系统对多语种条件只能"一刀切"；现有Audio-LLM适配方法（如LoRA）既未显式建模语言相关的提取需求，也难以保持与冻结下游模型的即插即用兼容性。

**模型架构：** 冻结WavLM Base+编码器加共享投影提取混合与enrollment表征，注册语音经注意力池化得到说话人嵌入并以FiLM注入每个沙漏块；Difficulty Estimator融合混合特征均值方差与说话人嵌入，预测需求δ∈[0,1]及easy/medium/hard三档预算，路由至6个共享沙漏块（提取器2.7M参数，块内为扩张深度可分离TCN+降采样全局注意力）；选中出口线性插值对齐到512点/128跳STFT网格，解码器联合预测掩码与有界残差，相位沿用混合信号经iSTFT重建波形。

**核心创新：** (1) 任务自适应音系难度指数PDI：以对最深出口质量差≤容差ε的最小处理深度定义d_ℓ=σ(a_ℓ)，stop-gradient防止浅出口退化，并用冻结的URIEL+/PHOIBLE音系相似度图在相关语言间平滑任务证据；PDI仅作训练弱监督，推理完全不需要语言标识。(2) 共享多出口条件计算：6个沙漏块形成三级嵌套出口并共享前缀而非复制专家，训练用直通Gumbel-Softmax路由并按路径加权损失+成本项λ_C·C_k抑制塌陷到最深路径，推理只执行所选前缀与出口。(3) 语义+频谱双路互补表征与波形级输出，可即插即用挂接任意冻结Audio LLM后端，论文在Qwen3-Omni上验证了信号级、ASR与语义理解全链路收益。

**训练策略：** 每出口负SI-SNR路由损失、说话人嵌入正则、L_DE与L_PDI按α/β/γ加权（验证集调参）；在线构造4秒混合、信噪比[-5,5] dB、16 kHz；Adam优化器，学习率1e-3、权重衰减1e-5，混合精度与梯度裁剪；Gumbel温度退火，先期以均匀路径采样预热并直接监督全部出口。

### 📊 实验结果
**数据集**：自建PolyExtract基准（8语种含英/中/粤/土/波兰/Viet/Zulu/Kinyarwanda、跨5语系，源自LibriSpeech、AISHELL-1、NCHLT、VIVOS、Common Voice，16 kHz，64个定向目标-干扰语言对等样本对照）

**主要指标**：
- 宏SI-SNRi：15.07 dB @0.30 GFLOPs，较最强基线TF-GridNet（13.8 dB @1.42 GFLOPs）高+1.27 dB，较大模型AD-Flow TSE（14.6 dB @5.8 GFLOPs）高+0.47 dB
- 宏PESQ/STOI：3.22 / 0.92；最差语言对SI-SNRi 14.0 dB（TF-GridNet为11.1 dB）
- 冻结Qwen3-Omni多语种ASR平均WER：14.6%，较TF-GridNet插件(16.8%)降2.2个百分点，前端仅0.2–0.4 TFLOPs（LoRA后端适配需18.2T参数）
- 难度估计校准：语言宏MAE 0.085，Spearman ρ=0.945；与oracle路由(15.23 dB)仅差0.16 dB
- 五项语义任务（槽填充/是非/归属/意图/情感）均显著优于混合语音直接输入

**是否开源**：暂无（论文未提供代码或Demo链接）

### ⭐ 评分：8/10
评分理由：首次将多语种提取的"算力需求异质性"归因于音系结构并以PDI作为训练先验，标签-free自适应路由设计优雅；实验覆盖信号级、ASR、语义理解与消融四个层次，质量-效率双优于重量级基线，工程落地价值高。不足在于PolyExtract为受控双人混合基准，未见口音与真实重叠验证，且暂未开源。

---

## [2] Efficient Audio-Visual Speech Enhancement via Reinforcement Learning-Based Neural Architecture Search

**arXiv ID**：2610.12796 | **方向**：语音前端

**作者**：Khubaib Ahmed, Ahsan Adeel, Nasir Saleem, Kia Dashtipour, Ahsan Ulhaq, Amir Hussain

**机构**：University of Stirling（英国）、Edinburgh Napier University（英国）、University of Technology and Applied Sciences（阿曼）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.12796 | **PDF**：https://arxiv.org/pdf/2610.12796.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
音频-视觉语音增强（AVSE）前沿模型普遍超过2200万参数，难以部署到手机、助听器等边缘设备。本文提出RL驱动的NAS框架：将搜索建模为带约束的MDP，用PPO+约束掩码的LSTM控制器在仅324个合法配置中逐步收缩骨干网络，奖励函数联合优化SI-SNRi保真度与模型紧凑度。框架仅评估35个候选架构即找到2.9M参数模型，SI-SNRi达14.5 dB（仅比22M基线低0.7 dB），压缩约9倍，移动CPU上RTF降低4.3倍，搜索效率比随机搜索高92%，验证了边缘端实时多模态增强的可行性。

### 🔧 技术方案

**问题背景：** AVSE利用唇动视觉线索提升噪声环境可懂度，但SOTA模型计算负担沉重，无法在受限设备实时运行；多模态间依赖使架构搜索空间巨大，且音频-视觉流须保持时间同步，逐候选训练评估的开销又随模态数倍增，现有NAS鲜少针对多模态语音增强设计。

**模型架构：** 解码骨干为TCN式双流网络：编码器通道E（{128/192/256}）、瓶颈通道B（{128/192/256}）、TCN重复数R（{2/3/4}）与每重复块数（{4/6/8}）、扩展比X（{1.5/2.0/2.5}）、视觉输出通道V（{128/256}），融合采用加法方式；搜索控制器为2层LSTM（各256隐单元），状态向量含[E/256, B/256, R, X, H/B, Params/22M, SI-SNR/15.2]，actor头输出12维离散动作（六维度各增/减）、critic头估值，并以基线22M架构嵌入做LSTM初始化实现热启动。

**核心创新：** (1) 约束化搜索空间设计：强制时间一致性（T_audio=T_visual，仅用保维点积卷积与残差）、通道兼容（B≤E）与算力上界（R×B≤24），将O(10^14)组合压缩到324个有效配置。(2) 多目标奖励与约束感知动作掩码：奖励=α·ΔSI-SNRi/baseline − β·max(0,超预算惩罚) − γ·违规惩罚（α=1.0，β=0.7，γ=10，经Pareto分析确定），掩码剔除非法动作，收敛提速约40%。(3) 渐进收缩策略：从22M基线出发，每步仅改一个维度，并用历史数据线性回归从10轮中间结果外推全训练SI-SNRi，大幅降低候选评估成本。

**训练策略：** 控制器用PPO训练，裁剪系数ε=0.2，动作选择ε-greedy且ε=0.3，AdamW（lr=3×10^-4，weight decay=10^-2），GAE λ=0.95，4个并行worker；共35个episode、每episode 5步、每候选训练10轮，合计1750 epoch当量，约为通用NAS的1/3开销；基线为22M参数AVSE网络，测试噪声SNR范围-5~5 dB。

### 📊 实验结果
**数据集**：LRS3（438小时同步音视频），噪声取自Clarity Enhancement Challenge 2（CEC2）真实助听场景，SNR -5~5 dB，评估于CEC2测试集

**主要指标**：
- SI-SNRi（改进量）：14.5 dB，达22M基线（15.2 dB）的95.4%，差值-0.7 dB
- 参数量：2.9M，较基线22M缩减约9倍（-87%），模型11.7 MB
- RTF（Intel i7-1185G7）：0.19，基线0.82，降低4.3倍；3秒音频约570 ms
- 对比随机搜索最优（2.4M、13.9 dB）：高0.6 dB；对比手工小模型（6.1M、14.8 dB）：多0.3 dB且少2.1M参数
- 搜索效率：仅评估35个架构，较随机探索高92%

**是否开源**：暂无代码/demo发布

### ⭐ 评分：6/10
评分理由：面向边缘部署的AVSE硬件感知NAS选题务实，约束空间+动作掩码+渐进收缩组合让搜索开销显著低于常规NAS，且揭示"浅而宽TCN、视觉通路可激进剪半"等可复现设计规律，工程参考价值明确。不足在于实验仅在LRS3/CEC2单一设定、指标以SI-SNRi与RTF为主，缺MOS等感知评估与多硬件对比，奖励系数与部分超参披露不全，且未开源，方法本身属增量式而非突破。

---

## [3] RDSE: Real-Time Directional Speech Enhancement Framework for Dual-Mic Commodity Smartphones

**arXiv ID**：2610.12476 | **方向**：语音前端

**作者**：Chinmay Deo, Danish Mahajan, Soudeep Ghoshal, Himanshu Buckchash

**机构**：印度国立理工学院 Jalandhar（NIT Jalandhar）、卡林加工业技术学院（KIIT Bhubaneswar）、奥地利 IMC 应用科学大学（Krems）

**发布日期**：2026-10-12 | **论文**：https://arxiv.org/abs/2610.12476 | **PDF**：https://arxiv.org/pdf/2610.12476.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
手机音频变焦系统依赖多麦克风标定阵列或连续视觉帧级嵌入，无法在普通双麦手机上落地。本文提出 RDSE：视觉仅在单次交互中确定并参数化波束导向矢量，音频侧由 U-Net 去混响、几何容差 MVDR 波束成形、Conv-TasNet 目标说话人提取、MetricGAN 去噪级联成实时链路。在自建 SpARZ100 上，消声条件 STOI 0.775、PESQ 2.576；RT60=0.5s 混响下 STOI 0.554、PESQ 1.819；流式核心 RTF 0.60，帧延迟中位 4.27ms 低于 8ms 跳步预算，满足实时约束，并在三星手机上完成真机验证。

### 🔧 技术方案

**问题背景：** 商用双麦阵列空间分辨率低、方向模糊明显，对空间协方差估计误差与麦克风几何失配高度敏感，经典 MVDR 性能急剧退化；端到端深度模型又假定固定几何、多麦或大数据分布，跨设备泛化差。紧耦合 AVSE 需连续视觉流，在遮挡、姿态变化下脆弱，且现有多麦方案均需 4 麦以上标定阵列。

**模型架构：** 双麦远场模型，频域导向矢量 a(f,θ)=[1, e^{−j2πfτ(θ)}]。级联四模块：通道独立的 U-Net 去混响网络（输入混响语音对数幅度 STFT：512 点窗、75% 重叠、256 有效频点，预测去混响谱后复用原始相位重建时域）；MVDR 波束器（每频点协方差按 0.5s 时间常数指数平均，迹比例对角加载），overlay 模式固定视向 90°；Conv-TasNet（one-rest 主说话人提取）细化波束输出；MetricGAN 时频幅度掩码去噪并保持相位。整体 16kHz 双通道输入、单通道增强输出。

**核心创新：** (1) 一次性视觉参数化：相机仅在准星对齐或点击时给出一个水平像素/方位角，用于初始化导向矢量，视觉流与音频推理彻底解耦，规避帧级 AVSE 对遮挡与域移的脆弱性。(2) 几何容差双麦 MVDR：无需精确阵列标定，真机麦克风间距未知时以 12cm 近似即可完成 90° 目标与 40° 干扰说话人的分离。(3) 可开关模块化级联与骨干选型：在 Conv-TasNet、SepFormer、FasNet-TAC 中按质量—算力折中选定 Conv-TasNet，推理较 SepFormer 加速约 3.8 倍（5s 音频 6.05s vs 22.79s）；去混响模块在轻混响场景可关闭以省约 2.6 倍耗时。

**训练策略：** 三个神经模块均直接复用预训练权重（U-Net 去混响、Conv-TasNet、MetricGAN），论文未报告新的微调轮数/学习率/优化器，属系统集成式贡献；MetricGAN 阶段以感知指标分数为对抗目标优化幅度掩码。评测集 SpARZ100 共 100 条仿真样本（4.9m 立方房间、阵列中心 1.5m 高、干扰源方位 30°、SNR 5dB；消声与 RT60=0.5s 混响各 50 条；目标取 LibriSpeech 男声、干扰取 MUSAN 女声）。流式预算：40ms 分块、512 点 Hann、hop 128（8ms）、重叠相加。

### 📊 实验结果
**数据集**：SpARZ100（自建双麦仿真，100 样本，16kHz，SNR 5dB，干扰源 30°）＋ Samsung F24 真机录制（目标男 90°、干扰女 40°，间距近似 12cm）

**主要指标**：
- 消声条件（完整 RDSE，去混响关闭）：STOI 0.7754 | ViSQOL 2.0053 | PESQ 2.5755 | 5s 音频推理 3.95s，实时可行
- 混响条件（RT60=0.5s）：STOI 0.5539 | ViSQOL 1.871 | PESQ 1.8185 | 推理 3.69s；对比消声 STOI 下降约 0.22（Wilcoxon p<1e−9）
- 实时性：流式核心 RTF=0.60（消声 0.351/混响 0.712），帧延迟中位 4.27ms、P95 7.27ms，低于 8ms hop 可确定实时
- 对比最强双麦基线 Li et al.（定性口径）：PESQ +0.55（2.58 vs 2.03）但 STOI −0.06；对比 6 麦 Nair et al.：PESQ +0.54 且本系统实时可行而两者均非实时
- 骨干对比 SepFormer：推理省约 3.8 倍；Nemenyi 检验显示四种 RDSE 变体 STOI 均显著优于 FasNet-TAC/SepFormer
- 消融负结果：开启 DereverbNet 反使 PESQ 跌至约 0.88；MetricGAN 使 STOI 微降 0.014 但 PESQ +0.66

**是否开源**：暂无，论文未释出代码、Demo 或 SpARZ100 数据

### ⭐ 评分：5/10
评分理由：一次性视觉参数化思路清晰，bootstrap/Friedman/Nemenyi 统计分析与真机延迟实测是其亮点；但各模块全部复用现成预训练模型、无新训练，评测仅靠自建 100 样本仿真且与先工作只能定性对比，去混响模块被自身消融证伪为负收益，代码数据均不公开，整体属有参考价值的增量式系统集成。

---

## 其他论文（未进入前 15，仅列标题）

13. **How Should We Evaluate Naturalness for Synthetic Speech with a Foreign Accent?** | 语音大模型 | arXiv: 2610.13175 | 评分：5/10 | https://arxiv.org/abs/2610.13175

14. **Revisiting Accent Classification with DistilHuBERT: Speaker-Disjoint Evaluation and Cross-Corpus Generalization** | 语音大模型 | arXiv: 2610.13440 | 评分：5/10 | https://arxiv.org/abs/2610.13440

15. **Vocal Intensity Conversion with Continuous SPL Control via Adversarial Training** | 语音大模型 | arXiv: 2610.13608 | 评分：5/10 | https://arxiv.org/abs/2610.13608

16. **Enhancing Speech Recognition through Text-to-Speech and Voice Conversion Augmentation** | 语音大模型 | arXiv: 2610.13662 | 评分：5/10 | https://arxiv.org/abs/2610.13662

17. **CircuitTree: Composing Circuits into A Syllable Transcriber** | 语音大模型 | arXiv: 2610.12520 | 评分：5/10 | https://arxiv.org/abs/2610.12520

18. **VoxAnon: A balanced dataset for a fair evaluation of speech anonymization** | 语音大模型 | arXiv: 2610.13313 | 评分：5/10 | https://arxiv.org/abs/2610.13313

19. **EmoGavel: Grounding-Aware Reinforcement Learning with Verifiable Rewards for Multimodal Emotion Preference Learning** | 语音大模型 | arXiv: 2610.13353 | 评分：5/10 | https://arxiv.org/abs/2610.13353

20. **Acoustic Biomarkers for Alzheimer's Disease Detection from Spontaneous Speech** | 语音大模型 | arXiv: 2610.12500 | 评分：4/10 | https://arxiv.org/abs/2610.12500

21. **Does Financial Speech Need Continual Learning Regularization? A Study of EWC and mini-KFAC on Earnings Call ASR** | 语音大模型 | arXiv: 2610.13432 | 评分：4/10 | https://arxiv.org/abs/2610.13432

22. **Lightweight Systems for Spatial Semantic Segmentation of Sound Scenes** | 语音前端 | arXiv: 2610.12693 | 评分：5/10 | https://arxiv.org/abs/2610.12693

23. **QC-MI-OVSEL: Benchmarking Query-Conditioned Multi-Instance Open-Vocabulary Sound Event Localization** | 语音前端 | arXiv: 2610.13198 | 评分：5/10 | https://arxiv.org/abs/2610.13198

---

*Generated on 2026-10-12*
