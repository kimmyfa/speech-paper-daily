# 2026-11-11 语音论文速递

**共收录**: 14 篇 | **语音大模型**: 11 篇 | **语音前端**: 3 篇

> 目标日期 2026-11-11（北京时间）arXiv 语音相关论文共命中 14 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] Walrus Technical Report

**arXiv ID**：2611.13689 | **方向**：语音大模型

**作者**：Alkis Koudounas, Osamu Take, Hayato Futami, Quentin Jodelet, Emiru Tsunoo

**机构**：Sony Group Corporation，Speech & Language AI Lab（东京）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13689 | **PDF**：https://arxiv.org/pdf/2611.13689.pdf | **代码**：https://github.com/sony-speech/walrus | **Demo**：https://sony-speech.github.io/Walrus-Demo/

### 📌 简介
本文提出 Walrus，一个 8B 参数的统一语音与音频基础模型，覆盖 ASR（含语码转换、多说话人重叠）、AST/S2ST、TTS、情感识别、字幕生成与音频理解等 20+ 任务、100+ 语言。其主张不是新架构而是数据中心配方：backbone 完全沿用 Gemma 4 E4B，靠三阶段课程学习+任务/数据集双权重训练 600M+ 样本。Walrus 在 CS-FLEURS 达 7.23 CER（先前最佳 32.30）、LibriMix cpWER 19.32、MMAU-Pro 71.92%，多数基准超过 4 倍规模的 Qwen3-Omni-30B。

### 🔧 技术方案

**问题背景：** 现有 SpeechLLM 研究聚焦扩参数、改架构，数据配方很少被系统披露；而真正困难的能力（语码转换、重叠说话、娱乐域音频、推理式音频问答）恰是公共语料缺失的数据问题。此外各任务 token 预算悬殊（TTS/S2ST 输出远超 ASR），朴素混合会让生成任务主导损失、破坏识别核心能力。

**模型架构：** decoder-only Gemma 4 E4B（约 4B 有效/8B 总参数）原封不动，USM 编码器将语音转为连续表征连同任务 prompt 输入主干，单权重按自然语言 prompt 选任务。生成侧扩展词表加入 8,192 个语音 token，主干自回归预测 25 Hz、325 bps 离散 token；后接单层 VQ tokenizer（对齐 W2v-BERT 2.0 第 20 层特征，3 层 Conformer，512 维码本）与基于 UniCATS+Vocos 的 GAN 声码器，后者以 W2v-BERT 第 8 层特征为条件迁移源说话人音色与韵律，实现 TTS/S2ST 高保真波形合成。

**核心创新：** (1) 三阶段数据课程（Foundation→Expansion→Specialization，87.5k/135k/150k steps）：阶段一用 CommonVoice、MLS、FLEURS 等干净大规模语料建多语识别核心；阶段二引入 AMI/AISHELL-4 真实会议、LibriMix 模拟混叠、语码转换、字幕与对话语境任务；阶段三补娱乐域、低资源语言与 AudioReason-10M。(2) 任务感知+数据集感知双权重：ASR 权重恒为最高（5.0→4.0），TTS 早期仅 0.25、阶段三才升至 2.0，配合数据集权重压低冗余大语料，实现"加新任务不遗忘旧技能"。(3) 全套难任务合成管线：语码转换由 Gemma 4 26B 生成文本、分段单语 TTS 拼接、NISQA≥3.5 且 Whisper WER≤5% 双重过滤；多说话人用 FastMSS 词级切割重排模拟；字幕场景由带标签语音/音效/音乐段库程序化合成；10M 推理式音频 QA 覆盖时序/说话人/空间/指令遵循五类技能。

**训练策略：** AdamW（β1=0.9, β2=0.95, wd=0.1），梯度裁剪 1.0，SDPA 注意力，max seq 1024，单卡 batch 8×梯度累积 2、128 张 H100 等效 batch 2048；学习率阶段一/二 2e-6、阶段三减半至 1e-6，warmup 1%、decay 5%，各阶段从前一 checkpoint 续训并换种子。总量 600M+ 样本，约 30 天、9.2 万 GPU 小时。转写先经 Qwen3.5-9B 恢复大小写标点，以 CER≤0.05+长度校验防幻觉。

### 📊 实验结果
**数据集**：MLS、FLEURS、VoxPopuli、LibriSpeech、CS-FLEURS、LibriMix、日语日常对话（CEJC）、CoVoST-2、CVSS-C、MMAU-Pro、MMSU、IEMOCAP、Clotho-v2、AudioCaps

**主要指标**：
- ASR：MLS 6.89 WER（先前最佳 8.20，降 1.31）；VoxPopuli 7.84 vs Gemma4 11.78；FLEURS 5.33（94.7% 词准，超 Qwen3-Omni-30B）
- CS-ASR：CS-FLEURS read 7.23 CER vs 32.30（降约 25 点），XTTS 15.01 vs 44.10
- MT-ASR：LibriMix 19.32 cpWER（Qwen3-Omni 37.04、专用 VibeVoice-ASR 59.34）；JA Daily Talk 56.29 vs 71.99 cpCER
- 翻译：AST CoVoST-2 42.63 BLEU（vs 39.33）；S2ST CVSS-C 43.63 ASR-BLEU 超 30B Qwen3-Omni（41.27）
- 理解：MMAU-Pro 71.92%（基线 52.20，+19.72；超 Gemini-Flash 70.40）；MMSU 64.14 vs AF3 61.40
- 短板：IEMOCAP SER 49.55 vs AF3 63.80；Clotho-v2 CIDEr 0.39 vs 0.50；LibriMix 为训练域内数据

**是否开源**：提供 GitHub 仓库与项目/Demo 页，论文标注 CC BY-NC-ND 4.0；模型权重是否发布未明确，另提供仅用商用授权数据训练的 Commercial-Ready 变体。

### ⭐ 评分：8/10
评分理由：创新性不在架构而在数据工程，三阶段课程+双权重与全套合成数据管线披露极为详尽，可复现参考价值高；实验覆盖 20+ 任务、对比同量级开源模型与 30B/专用大模型，切换说、多说话人、音频理解上优势显著。扣分点：LibriMix 在训练集内导致 MT-ASR 对比域内偏置、CR→R 增益无法解耦权重与数据的贡献、情感与字幕仍弱于专用基线，且未直接量化消融各管线的单独效果。整体是多任务语音"数据配方决定上限"的强有力实证。

---

## [2] Emilia2: A Large-Scale Dataset for Controllable Long-Form Speech Generation

**arXiv ID**：2611.13614 | **方向**：语音大模型

**作者**：Qinke Ni, Dekun Chen, Junwen Qiu, Huan Liao, Xu Li, 等，Zhizheng Wu（通讯）

**机构**：香港中文大学（深圳）、伊利诺伊大学厄巴纳-香槟分校（UIUC）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13614 | **PDF**：https://arxiv.org/pdf/2611.13614.pdf | **代码**：暂无 | **Demo**：https://charlesnii.github.io/Emilia2-demo/

### 📌 简介
开源语音语料多为数十秒短切片，长文本基准最多 2 说话人且缺每说话人参考音频，导致长时程、可控 TTS 缺乏训练与评测基础。本文用 Emilia2-Pipe 从 in-the-wild 音频构建 229K 小时、41 语言数据集，统一短句、单人长语音、多人对话三视图（>5 分钟样本占长语音时长 50.0%、对话 66.8%），并附 477 万条自然语言指令与 93.3 万条非言语（NV）标签，同时发布 23 小时双语 Emilia2-testset。在其上训练的 0.6B NAR 模型在 TTSD-Eval 取得最低中文 CER/英文 WER（5.27%/9.93%），优于 8B MOSS-TTSD；AR 模型在 InstructTTSEval 达 76.2/78.3，与 Qwen3-TTS-12Hz-VD（77.1/77.9）相当。

### 🔧 技术方案

**问题背景：** 零-shot TTS 拼接短片段生成长语音有音色漂移、停顿不自然、韵律断裂问题；现有长语音模型（HALL-E、MOSS-TTSD 等）缺大规模含表现力标注的长时训练语料，公开长时基准又在说话人数与参考音频覆盖上不足。

**模型架构：** 数据侧 Emilia2-Pipe 流水线：FFmpeg 统一到 44.1kHz 单声道→Mel-Band RoFormer 人声分离→DiariZen 说话人日志+FireRedVAD 切分→DNSMOS（zh/en≥3.0、其他≥2.4）与自建合成语音分类器过滤→FireRedLID 路由至 Qwen3-ASR-1.7B（30 语）/IndicConformer-600M（22 印度语）转录；依说话人时间轴构造 Short（0.5-30s）、Long（同人≥30s）、Dialogue（2-6 人≥30s）三视图，保留原始连续人声含停顿与跨句过渡。标注侧：年龄/性别/口音/音高/情绪/语速/响度属性模型（>30s 样本另保留带时间戳的情绪/语速/响度变化区间），由 Qwen3-Omni-30B-A3B-Captioner 生成 APS/DSD/RP 三类指令；Multilingual-NVASR 将 [Laughter][Cough][Sigh] 等 NV 标签与文字交织。模型侧：Emilia2-AR（Qwen3-0.6B 因果骨干+CosyVoice3 单码本 tokenizer+DiT 流匹配 mel 解码+Pupu-Vocoder，输出含 speaker-ID 标记）与 Emilia2-NAR（0.6B 骨干+MGM 架构+Fish Audio S2 Pro 多码本，掩码 token 并行生成）。

**核心创新：** (1) 同一源录音切出三视图互补训练，长语音保留原生停顿与声学过渡而非独立切片拼接，直接监督长时内容对齐、说话人切换与轮次连续性。(2) 把指令与 NV 标注从短片段扩展到长样例（长语音+对话贡献指令时长的 79.6%），且>30s 样例含时间戳风格变化描述，首次提供分钟级表现力控制监督。(3) Emilia2-testset 为首个每说话人配参考音频、至多 4 说话人、最长 30 分钟、118 例 23.3 小时人工校验双语基准，按说话人数/时长分层可暴露聚合指标掩盖的退化模式。

**训练策略：** 四阶段课程学习：Short（30s 上限）→Long（上下文延至 30min）→Long+Dialogue 联合→指令/NV 子集表现力 SFT；8 卡 GPU、BF16。AR 用 AdamW（weight decay 0.01、梯度裁剪 1.0），前三阶段 lr 2×10⁻⁴、3% warmup+余弦衰减，token 上限 32,768（对话 50,480），SFT 恒学习率且梯度累积 4；NAR 前三阶段 lr 10⁻⁴、SFT 10⁻⁵；NAR 按 full/coarse-to-fine/independent 三种掩码策略以 30%/50%/20% 概率采样、逐 masked 条目 NLL 损失；AR 为 speech token+speaker-ID 标记的 next-token NLL。

### 📊 实验结果
**数据集**：Emilia2-testset（118 例/23.3h 中英双语、0.9-30min、≤4 人）、TTSD-Eval、Long-TTS-Eval、InstructTTSEval、NV-Bench、Seed-TTS-Eval；训练语料 229,388h/41 语言/约 2050 万条（去重后）

**主要指标**：
- TTSD-Eval：NAR 中文 CER 5.27%、英文 WER 9.93%，低于最强基线 8B MOSS-TTSD（6.08%/11.09%）约 0.8/1.2 点，ACC 95.30/94.89 几乎持平（MOSS 95.36/95.00）
- InstructTTSEval：AR 均值 76.2/78.3（zh/en），六项中四项优于 Qwen3-TTS-12Hz-VD（77.1/77.9）
- NV-Bench：NAR 中文单标签 PCER 28.15（CosyVoice3 为 57.69）、文本 CER 2.36%、SIM 0.78，全子集最低错误率
- Emilia2-testset：AR 中文 CER 3.67%、NAR 英文 WER 6.62%，六项中五项仅次于 MOSS-TTSD；长时主观 N-MOS≥4.20
- 关键发现：chunked 推理使 NAR 中文 CER 8.62%→1.73% 但 N-MOS 全线下降最多 0.75，证明长语音不能靠分片拼接

**是否开源**：已发布 testset（manifest+标注）及预处理/评测管线；229K 小时全量数据集承诺论文接收后以源 URL manifest+标注形式发布（不直接再分发原始音频）

### ⭐ 评分：8/10
评分理由：填补了长时可控语音在训练数据与评测基准上的双重空白，三视图+时间风格化指令+NV 交织标注的管线设计系统且验证充分。0.6B 模型即可对标 8B MOSS-TTSD、匹配 Qwen3-TTS，跨 AR/NAR 两种范式交叉验证说服力强；分层评测揭示的分片拼接韵律断裂现象有方法论价值。不足在于表现力标注依赖大模型自动 captioner，准确率上限受限；长时可控实验缺外部基线；全量数据仅承诺录用后以 manifest 形式发布，音频可复现性有折扣。

---

## [3] Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning

**arXiv ID**：2611.13845 | **方向**：语音大模型

**作者**：Sezgin Saygili, Emre Kaplaner, Oncel Ozgul, Fikri San Koktas

**机构**：PatientDesk AI

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13845 | **PDF**：https://arxiv.org/pdf/2611.13845.pdf | **代码**：https://huggingface.co/datasets/cloud0day3/alania-synthetic-speech-tr（数据集与评测 harness，权重不开源） | **Demo**：https://speech.patientdesk.ai

### 📌 简介
针对土耳其语等中资源语言 TTS 数字/缩写/外来词朗读不可靠、零样本克隆丢字的问题，提出 488M 参数的 Alania-2：采用 VoxCPM 架构（LM 骨干+扩散头生成连续音频潜变量），从零用 18,195 小时土耳其语语音（90% 为教师模型合成并自动过滤）训练，配合含 134 条读音规则的文本正则化器。Freya-TR-Eval 上 WER 达 1.44%（前代 5.99%），内置音色 CER 与 2.3B 模型差距不到 0.5 点；纯参考条件化使克隆丢字率从 21.9% 降至 1.7%，推理引擎优化后首音频延迟 32ms。

### 🔧 技术方案

**问题背景：** 主流零样本 TTS 以英中数据为主，开源土耳其语系统可懂度相差一个数量级；土耳其语数字/日期带须随读音一致变化的格后缀，大小写转换易破坏点 i/免点 i；前代 3.3B SNAC codec-LM 在基准上约 17 词错 1 词。

**模型架构：** 复用 VoxCPM2 文本 tokenizer 与冻结音频 VAE（16kHz 编码为 64 维 25fps 潜变量，解码 48kHz）。LM 骨干 16×1024（268M）+残差 LM 6×1024（72M）+特征编码器 8×768（69M）+扩散解码器 8×768（72M），共 488M；扩散 transformer 以 10 步流匹配+CFG 逐块预测 4 帧（0.16s）潜变量。前端含规则文本正则化器与外语品牌土耳其语音译词典。

**核心创新：** (1) 90% 合成数据配方：VoxCPM2 教师以 2,752 个设计音色+三模式生成 16,423 小时，经 CER≤0.05、语速 7–25 字/s、ECAPA≥0.45、UTMOS≥2.5、F0 性别一致五重自动过滤（人审通过率 79.2%），证明中资源语言上数据质量远比规模/参数量重要——同配方 7.6M 单音色模型即达全场最低 CER 0.20%。(2) 克隆纯参考条件化：放弃"续写参考音频+转录"改为仅用参考设音色，配合分块校验重试，丢字 21.9%→1.7% 且不损失相似度（0.569 vs 0.568）。(3) 服务端工程：rank-32 LoRA 约 2 分钟训练专属音色（相似度显著高于即时克隆）；Nano-vLLM 引擎加 batched VAE 解码（96 路 110→27ms/步）、CUDA-graph prefill（首音频 74→32ms）及 LoRA 前缀缓存键修复。

**训练策略：** 三阶段共约 210 H200 GPU·h：①早前 8,904h 混合约 64k 步；②18,195h 基础混合 70k 步，batch 32/GPU、梯度累积 2、lr 1e-4、wd 0.05；③音色设计/风格指令数据 lr 5e-5 至 4k 步。真实数据 2,398 小时源自 YODAS，经语言分类/DNSMOS≥2.4/AST 去音乐过滤。

### 📊 实验结果
**数据集**：Freya-TR-Eval（495 句土耳其语，Whisper large-v3 评 WER）；内部 292 条测试集；训练混合（1,772h 真实+16,423h 合成）

**主要指标**：
- Freya-TR-Eval WER：1.44%（Alania-1 为 5.99%，降约 4 倍；CER 0.28% vs 1.81%；UTMOS 3.67 vs 3.19；RTF 0.151 vs 2.49）
- 正则化消融：150 句含数字测试，原始文本 WER 66.7% vs 正则化 6.4%；96 条含数字句中关键信息完整保留 0 句 vs 86 句
- 关键对比：488M 与 2.3B 继续训练版 CER 仅差 0.3–0.5 点且吞吐 12 vs 8 req/s；Antalia-2 Mini（7.62M）WER 1.05%、CER 0.20%，接近其教师 VoxCPM2（0.92%/0.20%）；克隆参考 20–30s 最优（相似度 0.64–0.67）

**是否开源**：模型权重不开源；开源 Freya-TR-Eval 重跑 harness 与结果、2,398h 标注集、3,411h 合成语音、1.44M 句领域文本（HuggingFace），Antalia-2 Mini openly released。

### ⭐ 评分：7/10
评分理由：不是单点算法创新，而是中资源语言 TTS 全栈工程+实证研究的扎实范本：90% 合成数据配方、"参数量与可懂度几乎无关"的系统性证据（2.3B 仅提升 0.3–0.5 点）、克隆丢字根因分析与量化修复均有明确数值支撑且可复现。评测协议透明（统一重跑 15 个系统）。不足：权重不开源、无多人听测（自然度仅靠英语域 UTMOS）、大量结论单种子单轮，跨语言克隆（英→土相似度仅 0.41）仍弱。对工业落地参考价值高。

---

## [4] Antalia-2 Mini: A 7.6-million-parameter Turkish text-to-speech model trained entirely on synthetic speech

**arXiv ID**：2611.13811 | **方向**：语音大模型

**作者**：Sezgin Saygili, Emre Kaplaner, Oncel Ozgul, Fikri San Koktas

**机构**：PatientDesk AI

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13811 | **PDF**：https://arxiv.org/pdf/2611.13811.pdf | **代码**：https://huggingface.co/cloud0day3/antalia-mini（权重+推理，Apache-2.0） | **Demo**：https://huggingface.co/spaces/cloud0day3/antalia-mini

### 📌 简介
面向端侧 CPU 可运行的土耳其语单音色 TTS，本文提出 7.62M 参数的 Antalia-2 Mini，全部训练音频由约 300 倍大的 VoxCPM2（约 2.29B）克隆一条 9.88 秒合成参考音频生成，经自动质检保留约 1790 小时。模型为字符输入、无音素化器，采用 flow matching + shortcut 自一致生成器（8 步采样）与 Vocos 式 iSTFT 声码器，输出 48kHz。在 Freya-TR-Eval 公开 harness 上 WER 1.09%、CER 0.220%，配对 bootstrap 与 8.6M 的 EMA Lightning 及教师 VoxCPM2 均不可区分；声码器在生成 mel 上微调使 WER 从均值 3.89% 降至 1.75%。

### 🔧 技术方案

**问题背景：** 小模型可在本地设备运行、无需 GPU 与上云，但已有的小型土耳其语系统（Piper 16M、MMS-TTS 36M）WER 达 3.41%/6.38%，远低于 2.38B 的 Trendyol-TTS（1.16%）；同时高质量真人语料在低资源语言上昂贵稀缺。本文验证纯合成蒸馏能否让小模型逼近大系统可读性。

**模型架构：** 总计 7,620,931 参数。文本编码器 828K（47 字符 embedding×192 + 3 个 ConvNeXt 块 + 1 个 RoPE 自注意力块）；MAS 对齐先验与卷积时长预测器 173K（推理时用预测时长取代 MAS）；生成器 2.69M，5 层 DiT（宽 192、4 头、SwiGLU 512、adaLN-single、条件 ConvNeXt），以帧对堆叠（21.3ms/token）从噪声 8 步 flow matching 采样出 128 维、93.75fps 的 mel；声码器 3.93M，Vocos 式，8 个 ConvNeXt 块 + 线性头直出 1025 点幅度与相位，经 iSTFT 合成 48kHz（占参数 51.6%、计算仅 14.4%）。推理端还含规则文本规整器、隐藏前后缀与重复音拉长规则，末尾为固定 EQ/de-esser/限幅输出链。

**核心创新：** (1) 纯合成蒸馏闭环：不触教师内部特征，仅用其音频训练字符级声学模型，7.62M 学生 WER/CER 与 2.29B 教师统计不可区分，且系统披露教师缺陷的继承（ö 开头词首仅 26% 读对，用隐藏前缀音频并剪除来掩盖）。(2) 声码器在学生自身生成的 mel 上微调：声码器训练分布（真 mel）与推理分布（生成 mel）失配是 WER 高企主因，按 80% 概率采样生成 mel 微调后 WER 大幅下降，冻结对照组无此收益。(3) Shortcut 自一致训练与 flow matching 混合（1/4 batch 训练 shortcut 项，步长 d∈{1..1/64} 7 档采样），单一模型支持 1/2/4/8 步采样，默认 8 步 + CFG 2.0。

**训练策略：** 教师侧：8×H200 单机 23 小时生成 1,361,734 条，按 CER>10%、语速、ECAPA 相似度<0.45、F0 越界、UTMOS<2.8 等规则保留 97.4%（合计约 1,790h）。声学模型：AdamW（β=0.9/0.98，wd 0.01，clip 1.0，bf16，EMA 0.9995），主训练 420K 步（lr 3e-4），短片段微调 51,880 步（lr 1e-4→5e-6）。损失为 FM + shortcut 自一致 + 先验 + 时长，单位权重；10% 语料用空条件训练 CFG。声码器：GAN 损失 45·L1(多分辨率 mel)+对抗+2·特征匹配，5 周期+4 FFT 判别器，1.003s crop、32/GPU。整条 lineage 仅 114.5 GPU-hours。论文还复盘了 bf16 autocast 权重缓存导致生成器前 6,000 步零梯度的静默 bug。

### 📊 实验结果
**数据集**：Freya-TR-Eval（495 句土耳其语，3–13 词，3 takes，11,751 词/80,922 字符）；评分用 Whisper large-v3 + 8kHz 带宽匹配，UTMOS22-strong；基线 15 个系统

**主要指标**：
- Mini 1.0.1（公开 harness）：WER 1.09%，CER 0.220%，clean 句占比 92.9%，全带 UTMOS 3.18
- vs EMA Lightning 1.0.1（8.6M）：WER 差 +0.05 [−0.22,+0.32]、CER 差 −0.005，配对 bootstrap 不可区分；CER 为 11 个开源系统中最低
- vs 教师 VoxCPM2（2.29B）：WER 差 +0.10 [−0.25,+0.45]，不可区分，即 1/300 参数量达到教师可读性；UTMOS 低 0.24
- vs 小型基线：Trendyol-TTS（2.38B）WER 1.16%，Piper 3.41%，MMS-TTS 6.38%
- 消融：声码器生成 mel 微调使 7 组相邻检查点 WER 均值 3.89%→1.75%（CER 0.984→0.385，UTMOS 2.45→2.93）
- 速度：单 L4 GPU 35× 实时（RTF 0.029）；Apple M5 CPU 2 线程 41× 实时；fp32 权重 30.5MB

**是否开源**：权重、推理/规整代码、ONNX 图、benchmark harness 以 Apache-2.0 公开；训练代码、数据与数据生成脚本不公开。无任何人耳主观测试，且超参在同 495 句上挑选（作者自认分数偏乐观）。

### ⭐ 评分：7/10
评分理由：把"小模型纯合成蒸馏"做成可复现的工程范本，声码器分布失配→生成 mel 微调贡献 2+ 个百分点 WER 是方法层面最有迁移价值的发现；配对 bootstrap、双 harness、教师缺陷溯源与 bf16 梯度 bug 复盘的诚实度在同类技术报告中罕见。局限在于音色单一、仅土耳其语、无人工 MOS，关键设置在同一 benchmark 上挑选导致指标有选择偏差；架构组件（Vocos/DiT/flow matching）均为已有技术组合，原创性中等，实际端侧部署价值高。

---

## [5] ESDCodec: Ultra-Low Bitrate Speech Codec with Enhanced Semantic Disentanglement and Subband Decoding

**arXiv ID**：2611.14043 | **方向**：语音大模型

**作者**：Nan Xu, Kecan Mao, Xin Gu, Yi Zhao, Zhi Gong

**机构**：腾讯微信（WeChat, Tencent Inc，北京）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.14043 | **PDF**：https://arxiv.org/pdf/2611.14043.pdf | **代码**：https://github.com/vspeech/ESDCodec | **Demo**：暂无

### 📌 简介
针对神经语音编解码器在约 1kbps 以下码率重建质量急剧退化、且语义-声学解耦不充分的问题，本文提出双流编解码器 ESDCodec：语义路采用 SimVQ 式冻结码本加可学习线性投影器生成单枚语义 token 并做 SSL 蒸馏，声学路用 RVQ 补充细节；解码端引入仅 9.6M 参数的子带感知条件网络，预测子带幅度/相位先验注入上采样各级。模型 89.78M 参数，在 0.85kbps 下 PESQ 达 2.49、STOI 0.921、WER 4.18%、MUSHRA 88.2，全面优于 DualCodec；VALL-E TTS 实验中英文 WER 降至 3.31/2.39，说话人相似度 SIM 提升至 0.63/0.70。

### 🔧 技术方案

**问题背景：** 低码率（≤1kbps）下 RVQ 类编解码器重建质量显著劣化；单码本方法（WavTokenizer、Single-Codec）虽省码率但缺显式语义建模，双流方法（Mimi、SemantiCodec、DualCodec）语义-声学解耦与低码率目标仍难统一。

**模型架构：** DAC 风格卷积编码器（4 个下采样块，stride 4/5/6/8，snake 激活）将 24kHz 波形做 960 倍压缩为 25Hz 潜特征 Z∈R^{T×D}；语义量化器输出单 token q0（冻结码本 16384×1024），后接 4 个 ConvNeXt 块强化判别；声学路由 11 层 RVQ（码本 1024、维度 8）编码，推理仅激活 3 个量化器（1 语义+2 声学），总码率 0.85kbps。解码器用反卷积上采样重建波形，并联条件网络以 6 个 ConvNeXt 块（输入维 256、中间维 1024）预测 1/4 子带的幅度和相位，经 ISTFT 得子带波形后通过 stride 1/5/4 的下采样层逐 Stage 注入上采样特征。

**核心创新：** (1) SimVQ 增强的语义量化器：码本重参数化为随机初始化冻结基矩阵 S 与可学习投影 W 之积（C=S×W），整码本在线性空间联合更新、仅 W 可学，从机制上抑制码本塌缩、提升利用率，使单层语义码即可承载完整语义。(2) 子带感知条件解码：将低维量化特征到波形的病态映射显式加入谱先验监督，条件网络预测子带信号并在各上采样 Stage 融合，以 9.6M 轻量参数针对性修复频谱细节与基频。(3) 双流统一框架下语义分支零额外 token 开销：语义信息完全压入单码本，配合 w2v-BERT-2.0 与 ConvNeXt 双源蒸馏保证语义对齐。

**训练策略：** 损失为对抗+L1 特征匹配+全带/子带多尺度 Mel 重建+STFT+L2 SSL 蒸馏+码本/承诺损失的加权和；判别器复用 DAC 的 MS-STFT 与 MPD。数据用 Emilia 约 97000 小时中英双语语音（24kHz），随机截取 4 秒，batch size 12；生成器/判别器初始学习率 1e-4 指数衰减，AdamW（β=0.8/0.9），卷积权重归一化；codec 训 350K 步，TTS 用 8 码本训 600K 步，8×NVIDIA H20。

### 📊 实验结果
**数据集**：训练：Emilia（约 97k 小时中英双语，24kHz）；测试：LibriSpeech test-clean（2620 句，域外）、Seed-TTS-Eval

**主要指标**（0.85kbps，LibriSpeech test-clean）：
- PESQ 2.49、STOI 0.921、V/UV F1 0.936、Pitch 误差 33.86、ViSQOL 2.74、WER 4.18%、MUSHRA 88.2（GT PESQ 4.64）
- 关键对比：同码率双流基线 DualCodec（PESQ 2.32/ViSQOL 2.61/WER 4.70/MUSHRA 85.8）全面让位，PESQ +0.17、ViSQOL +0.13、Pitch 误差 −4.9、主观分 +2.4；TTS 侧 VALL-E 下 EN/ZH WER 3.31/2.39（DualCodec 3.40/2.49），SIM 0.63/0.70（DualCodec 0.57/0.67）
- 消融：换普通 VQ 语义 PESQ 降至 2.43、WER 升 4.43；去条件网络最差，PESQ 2.42、WER 飙至 6.38、Pitch 36.21；语义码本 1024→16384 使 ViSQOL 2.58→2.74、WER 5.27→4.18

**是否开源**：是，代码与预训练模型已发布于 GitHub（vspeech/ESDCodec）

### ⭐ 评分：7/10
评分理由：将 SimVQ 冻结码本与子带条件解码两个各自已验证的思路系统融合进双流 codec，在 0.85kbps 严格同码率下对 DualCodec 取得全指标一致的客观+主观提升，消融充分且码本尺寸分析有参考价值，开源增信。创新属组合式而非范式突破，语义路仍依赖外部 SSL 蒸馏；测试域限于 LibriSpeech 英文为主、主观评测仅 10 人 15 句，且 4.18% WER 仍高于 X-Codec，噪声/多说话人泛化未验证。对低码率语音 token 化与 LLM-TTS 工程落地有直接的实用价值。

---

## [6] DialInstruct-TTS: Interactive Expressive Speech Generation via Multi-Turn Dialogue with Fine-Grained Temporal Control

**arXiv ID**：2611.13875 | **方向**：语音大模型

**作者**：Wangzixi Zhou, Bagus Tris Atmaja, Sakriani Sakti

**机构**：奈良先端科学技术大学院大学（NAIST，日本）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13875 | **PDF**：https://arxiv.org/pdf/2611.13875.pdf | **代码**：暂无 | **Demo**：https://anonymous.4open.science/w/eacl-demo-17C5/

### 📌 简介
现有指令式 TTS 仅支持整句一次性风格控制，微调需重述指令并重生成全句，无法保留已满意片段。本文提出 DialInstruct-TTS 交互式多轮表现力 TTS 框架：冻结的 Qwen3-8B 作为对话修订规划器，将上下文反馈解析为结构化 TemporalPlan；时间声学控制模块在 Irodori-TTS 骨干上实现情感/语速/音量/气声的 span 级局部控制；参考潜变量修订机制跨轮锁定非目标区域。主观评测中整体指令匹配度 4.283（Qwen3-TTS 为 3.077），局部控制盲测偏好率 92.1%，多轮修订获 29/30 听众优先选择。

### 🔧 技术方案

**问题背景：** 指令式 TTS（PromptStyle、CosyVoice3、Qwen3-TTS 等）为句子级一次性控制，迭代精修代价高且会破坏已接受区域；现有语音编辑（VoiceCraft、VoxEditor）多为一次性，缺上下文化的多轮增量修订与非目标保留。

**模型架构：** 两级框架。①Dialogue Revision Planner：本地部署冻结 Qwen3-8B，输入源文本、当轮反馈与上一轮完整输出（作为显式修订记忆），以 JSON 约束生成 resolved caption、delta plan 与完整 TemporalPlan，可解析"同一段""再强一点"等指代与 add/strengthen/weaken/replace/remove 操作。②Temporal Acoustic Control Module：基于 Irodori-TTS（RF-DiT+DACVAE 全部冻结），仅训练 174M 新参数（总声学模型 791M）。TemporalPlan 经 embedding 编码为控制 token，MFA 对齐构造 target/transition/non-target 掩码；Control Cross-Attention Adapter 以帧为 query、掩码约束的 plan token 为 key/value 注入低秩残差；Attribute Controller 含情感 ControlNet 分支（复制末 4 个 RF-DiT 块）、语速控制器（改写 duration predictor 并重映射掩码）、音量控制器（dB→连续条件+掩码残差缩放）、气声专用分支。修订建模为 masked flow inpainting：每采样步将非目标潜变量钳回上一轮同噪声轨迹，潜变量直接跨轮传递避免波形往返。

**核心创新：** (1) LLM 规划器+结构化 TemporalPlan 实现多轮上下文增量控制，用户只需说明改动而无需重述全部指令。(2) 属性解耦的帧级局部控制：帧-控制掩码交叉注意力加四条独立属性分支，把每处修改限定在指定时间区间且互相少干扰。(3) 参考潜变量钳制（reference-latent revision）从采样层面硬保证非目标区声学实现跨轮不变，配合非目标保留 L1 损失与边界 Huber 平滑损失。

**训练策略：** 自建日语数据：以中性语音为底，用 MFA+SoX 对语速/音量段做时域缩放与增益、插入 JVS 气声段、插入 JVNV 情感段，构造 8 类×1k 条（约 8–10s，48kHz）共 8k 条"中性-局部风格-中性"语料，7200 训练/800 验证。分阶段训练各控制器，损失=目标加权 flow-matching+时长/保留/边界项+属性监督（情感 CE+SmoothL1 与排序损失、语速 log 时长 L1、音量 Δlog 能量 L1、气声 CE）。AdamW（β=0.9/0.999，wd 0.01，clip 1.0），各阶段学习率 2e-6 至 2e-5，单卡 RTX PRO 6000 约 2 万步、20 GPU 小时，BF16。

### 📊 实验结果
**数据集**：自建 8k 条日语局部风格语料（48kHz）；全局控制 16 例、局部 48 条件、多轮 4 组三轮对话；30 名日语母语者听测

**主要指标**：
- 全局风格：Overall Match 4.283 / MOS 3.930（基线 Irodori 2.792/3.935、Qwen3-TTS 3.077/3.186、CosyVoice3 2.911/2.688），Match 较最强基线高 1.21
- 局部控制盲测：偏好率 92.1% vs Qwen3-TTS 7.9%；TS-MOS 约 4.0–4.08，TN-MOS 约 3.3–3.45 为短板
- CER：本系统与 Irodori 为 0，Qwen3-TTS 0.0089、CosyVoice3 0.0125
- 消融：去语速控制器时长误差 0.06→0.91s；去非目标钳制 log-F0 RMSE 0.092→0.270、log 能量 0.54→0.93；与拼接编辑器比情感 CER 1.07% vs 2.21%
- 多轮：便利性 4.183，最终偏好 29/30（96.7%）选多轮修订

**是否开源**：仅匿名 demo 音频页，正文未承诺代码/模型开源（EACL 匿名评审投稿）

### ⭐ 评分：7/10
评分理由：首次把指令式 TTS 从一次性整句控制推进到上下文感知多轮 span 级精修，规划器+掩码流钳制的组合设计清晰且消融充分支撑各组件有效性。实验主观部分达 30 人规模且对比同数据微调的 SOTA 基线，但仅覆盖日语、情感限于 4 类、局部控制训练数据靠 PCM 拼接合成，过渡自然度与音量/气声可靠性仍是明显短板；无代码开源也限制复现。整体为面向实际配音工作流的实质贡献，距离通用可用尚有迭代空间。

---

## [7] Earlybird: Predictive Streaming Speech Recognition in 29M Parameters

**arXiv ID**：2611.14421 | **方向**：语音大模型

**作者**：Sahil Mahendrakar

**机构**：arXiv 未提供（独立作者）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.14421 | **PDF**：https://arxiv.org/pdf/2611.14421.pdf | **代码**：https://huggingface.co/sahilmahendrakar/Earlybird-29M | **Demo**：暂无

### 📌 简介
流式 ASR 通常在说话人发音结束后 90–400ms 才输出词，拖慢语音智能体响应。本文提出 Earlybird——29M 参数（4-bit 仅 16.8MB）的预测式流式识别器：不改架构、不用未来音频，把音频按 80ms 粒度随机截断，以"已到期词全文+2 个预测下一词"为目标训练。在 LibriSpeech clean 上中位词在发音结束前 90ms 被正确预测，六大测试集均为最早；69% 的词在结束前预测正确（基线 3–25%），OAL 八集平均 WER 12.6%，与同尺寸 Whistle 相当。

### 🔧 技术方案

**问题背景：** 流式识别器"词说完才出词"的延迟直接侵占语音智能体的检索/规划时间。FastEmit、LocalAgreement 等只是逼近"词结束时刻"，无法提前；已有 predictive ASR 仅在句尾掩码音频上离线预测，不适用于逐帧流式场景。

**模型架构：** 基于 Moonshine streaming Tiny（34M 编解码器、80ms 分块）删减词表至 19,007 token 得 29M 模型；每个截断步 t 输出所有"到期词"（判据 τi=max(si+min(0.5(ei−si),50ms), ei−300ms)）的完整拼写，接 EOT token 后再附 2 个预测词；编码器输入尾部追加 3 帧由已有音频后接静音算出的 padding 帧；每词置信度=其 token 概率连乘；QAT 量化为 4-bit 权重+8-bit 前端，成品 16.8MB。

**核心创新：** (1) 随机截断+单调延长目标：相邻截断点的目标序列只增不减，模型从不被训练去撤回已写内容，天然获得输出稳定性。(2) 选择性蒸馏：仅当教师 Moonshine Tiny top-1 与标签一致的 token 位置施加 KD 项——教师拿不准时概率弥散，全盘模仿会弱化预测词决断性。(3) 静音 padding 帧与免校准置信：模型学会"假设说话人可能已停止"来提前收尾词（中位延迟 −50→−90ms），原始 token 概率对"仍在发音中的词"ECE 仅 3.7–5.5，应用端可直接按置信度行动。

**训练策略：** 数据为 LibriSpeech 960h＋People's Speech 约 300h＋Kokoro 合成约 25h，按 1:3:3:3:1 采样；词级时间戳用 MFA、wav2vec2.0 CTC 对齐器与合成音素时长；仅保留 Moonshine Medium 能逐字转对的转写。四阶段单 GPU、batch 48：词表截断后 10k 步流式截断训练（lr 5e-5）、20k 步加 2 预测词的前缀训练（5e-5）、5k 步加 padding 帧（2e-5）、5k 步 4-bit QAT（2e-5），全程带 KD 项。

### 📊 实验结果
**数据集**：LibriSpeech clean/other、TED-LIUM 3、People's Speech、Earnings-22、Kokoro 合成 WikiText；Open ASR Leaderboard 八个英文集；加性白噪声/人声 chatter（10/5dB）

**主要指标**：
- 中位词延迟：LibriSpeech clean −90ms（发音结束前），对比 Moonshine Tiny runtime +270ms、Whistle +400ms、Whisper base +90ms，六集全为最早
- 结束前正确预测词占比：68.8%（clean）vs 基线 3.4–25.4%；p95 延迟 +80ms vs Moonshine +520ms
- OAL 八集：4-bit 平均 WER 12.6%，全八集胜 Moonshine Tiny runtime（14.4%），与同尺寸 Whistle（12.2%）基本持平
- 置信度校准：发音中词 ECE 3.7–5.5，conf≥0.9 的词实际正确率 91–96%
- 效率：单 CPU 线程每 80ms 步 39ms（约 2 倍实时）；代价为撤回率 1.29 词/词；chatter 10dB 下 WER 32.0% 劣于 Whisper base 8.9%

**是否开源**：是，权重与加载器 MIT 协议发布于 HuggingFace

### ⭐ 评分：7/10
评分理由：仅改训练配方、不动架构、不耗未来音频，就把小型流式模型做到"词未说完即预测正确"，并首次在同一 harness 下同时评测提前性、稳定性、标准精度与置信度校准，含噪声、量化、多 seed 与 padding 帧消融，方法透明可复现，对车载/语音助手链路有直接实用价值。不足是撤回率偏高、混响人声下精度明显掉队于 Whisper base、预测下词命中率仅 12–16%、英文单语且域外命令语音校准退化。

---

## [8] Swanada: Split-Encoder Capability-Routed Conformer CTC and Sub-30 MB On-Device Speech Recognition Across Twelve Scripts

**arXiv ID**：2611.13814 | **方向**：语音大模型

**作者**：Hemanth HM

**机构**：独立研究者（arXiv 未提供正式机构）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13814 | **PDF**：https://arxiv.org/pdf/2611.13814.pdf | **代码**：https://github.com/hemanth/swanada | **Demo**：暂无

### 📌 简介
针对 12 种印度/古典文字（梵语、印地英语及 10 种印度语言）端侧 ASR 中单语言 Conformer 体积过大（12 语言超 2.1 GiB）、ONNX 导出常数膨胀、CTC 流式前缀抖动及移动 WebAudio 不稳四大瓶颈，提出 Swanada 开源系统：共享 INT8 Conformer 编码器按能力路由到 17 层 177 MiB Studio 与蒸馏 14 层 25.35 MiB Mobile 两档，配 12 个可热切换的 515 KiB 原生文字 CTC 头，存储缩减最高 67.8 倍。在 480 条 held-out 与 1280 条公开测试上 Studio 取得 5.43%/8.87% CER，流式 TTFT 中位 30.6 ms、前缀回退率 0.00%。

### 🔧 技术方案

**问题背景：** 逐语言部署量化 Conformer-Large 需 12×177 MiB，超出浏览器缓存与手机内存预算；联合大词表 softmax 又带来 12 倍投影算力开销与跨文字漏字。静态相对位置编码表（10–20 MB FP32）与 1×1 Conv1d 触发的 ConvInteger 缺 WASM SIMD 快速内核，进一步阻碍子 30 MB 导出。

**模型架构：** 16 kHz 输入→80 维 log-mel（25 ms 窗/10 ms hop）→2 级步幅卷积前端（4× 下采样到 40 ms 帧率）→macaron 式 Conformer 块（半程 FFN+相对位置自注意力+depthwise k=31 卷积+半程 FFN），末端 layer_norm 输出 H∈R^{T′×512}；语言头为 257×512 线性 CTC 投射（515 KiB）。Studio：17 层/d=512/dff=2048/8 头，115.2M 参数；Mobile：14 层/d=256，23.56M 参数，外接 256→512 适配 LayerNorm 对齐教师坐标空间。运行时用零依赖 protobuf 补丁器（<2 ms）暴露编码器隐层，切语言<20 ms。

**核心创新：** (1) 分离编码器+能力路由文字头：脚本隔离 SentencePiece 词表（256 子词+blank，各头仅 515 KiB），杜绝跨文字 Unicode 泄漏并共享声学骨干。(2) 子 30 MB 导出三件套：DynamicRelPositionalEncoding 仅存 128 个逆频率向量、按当前帧长实时 sin/cos 合成位置编码，省 10.24 MB 常数；1×1 逐点卷积改写为 MatMul+保留 FP32 depthwise，使动态 INT8 量化 100% 落入 MatMulIntegersimd 路径。(3) 冻结头蒸馏与量化后校准：教师头全程冻结保持决策超平面静止，最小化 cos+mse+KL+CTC 四项对齐损失；量化后在真实 ONNX 输出特征上再微调各头；辅以因果 80 Hz 高通+50/60 Hz 陷波+Ephraim–Malah Wiener 增强与双区 LCP 流式稳定器保证已提交前缀零抖动。

**训练策略：** Mobile 蒸馏 20 轮、bf16 混合精度、AdamW lr=1.1e-3、batch 64，损失权重 λcos=2.5、λmse=2.5、λkl=0.38、λctc=0.16、τ=1.5；教师层经截断 SVD 投影到 top-256 奇异子空间暖启动。数据含 Shrutilipi/Vistaar、FLEURS、Sushrota、IndicTTS、GLOBE、AMI，并以 SHA-1 隔离全部测试集，零泄漏。

### 📊 实验结果
**数据集**：Held-out 12 语言录音棚集 N=480（~2186 s）；16 个公开测试集 N=1280（FLEURS、Sushrota 野生梵语、LibriSpeech test-clean/other、GLOBE、AMI，3.4 h）；多口音/俚语集 N=150；流式审计 N=72 会话

**主要指标**：
- Held-out CER：Studio 5.43%（WER 25.88%）；Mobile 18.56%
- Open 12-lang CER：Studio 8.87%，全部 16 集 12.06%；Mobile 19.23%/21.85%
- 关键对比：与 12 个单体 Conformer-L（2128.5 MiB）精度完全持平（CER 同为 5.43%），12 语言车队存储降 11.6×（183.4 MiB）/Mobile 降 67.8×（31.39 MiB）；Mobile RTF 0.0097×（103× 实时）；TTFT 中位 30.6 ms、churn 0.00%；口音增强+多口音校准使 CER 20.04%→17.44%、Hinglish WER 74.80%→60.89%

**是否开源**：是，代码、评测脚本与权重全部开源（GitHub: hemanth/swanada，CC BY 4.0）

### ⭐ 评分：7/10
评分理由：工程系统性极强的端侧 ASR 工作，protobuf 尾巴手术、零表位置合成、MatMul 可量化改写与量化后头校准直击浏览器部署真实痛点，存储/精度权衡（67.8× 压缩下 CER 不涨）和流式零抖动指标可信且可复现。局限在于评测以自测指标为主、缺少同规模量化开源基线（如 sherpa-onnx、Whisper-tiny INT8）横向对比，蒸馏与校准带来的精度收益近乎边际，且单作者无机构、会话重叠与混响场景 CER 仍偏高（AMI 41.5%）。实用价值突出，学术新颖性中等。

---

## [9] AURA: Auditory Spatial Intelligence via a Unified Representation from a General-Audio Encoder through Complete Alignment

**arXiv ID**：2611.13687 | **方向**：语音大模型

**作者**：Boyan Han, Xiaoyan Wang, Zhe Sun, Ziqi Wang, Yujun Cai, Hongli Cao, Yiwei Wang, Ming-Hsuan Yang, Liang An

**机构**：Southeast University、Rutgers University、University of California Merced

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13687 | **PDF**：https://arxiv.org/pdf/2611.13687.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有空间音频语言模型依赖单独训练的空间编码器，使空间与语义处理分裂在不同特征空间。本文发现无空间监督训练的通用音频编解码器（X-Codec）冻结表征本身保留空间信息，但双声源场景下 LLM 对其左右方向预测处于随机水平，并将其归因于"音频-文本信息不对称"。据此提出 AURA：六槽双耳表征（显式耳间差分）加场景/几何监督完成音频-文本对齐，编解码器与 Qwen3-8B 全程冻结，仅训练 64.63M 参数。在 SpatialSoundQA 上双声源 DoA 达 48.21%，超最强专用系统 10.31 点。

### 🔧 技术方案

**问题背景：** 空间音频理解系统需专用空间编码器（BAT/OWL 等），通用 LALM 在空间任务上接近随机（Qwen2-Audio 单声源方向 8.85% vs 随机 12.57%）。核心问题是：不经空间监督的通用编解码器能否同时支撑"识别声音"与"定位声音"，其空间信息为何不可用。

**模型架构：** 冻结 xcodec_hubert_general_audio_v2（50Hz、8 层 RVQ、码字维 1024）分别编码左右耳；L0–L2 码字求和为内容带、L3–L7 为声学带，得 [LS,LA,RS,RA] 四槽，再各加一条耳间差分槽 S=½(L−R) 构成六槽。内容带做 max 池化、声学带做 mean 池化（窗口 w=4），10 秒音频得 750 token；两层 MLP 投影器映射进 Qwen3-8B（冻结+rank16 LoRA）。目标文本先列场景清单（各声源类别/三轴方向/距离）与几何比较，再给最终答案。

**核心创新：** (1) 受控层级分析证明无空间监督的 RVQ 层间分化：浅层敏感声源内容（换源 L0 相似度 0.316），深层敏感耳间差、房间与混响（左右相似度 L0 0.742→L7 0.130）；左右信息仅靠跨通道差分可靠解码（单声源 L/R 74.0%→93.0%）。(2) 提出信息不对称假说并 2×2 受控验证：双声源音频含两源而答案只写被问源，导致"读出但不绑定"（同侧 F/B 80.4% vs 异侧 50.5%）；场景监督或差分表征任一可恢复左右读出（50.2%→69.8%/72.8%），绑定需两者组合（异侧 L/R 50.0%→70.4%，交互 +18.0 点，McNemar p<10⁻⁴⁸）。(3) 六槽表征+场景/几何监督对应两个病因，无需任何空间编码器或外部声学特征。

**训练策略：** 三阶段课程学习（单源 0.33M→加双源 0.85M→加关系 1.94M 样本），每阶段 1 epoch，AdamW（lr 1e-4，cosine+warmup，clip 1.0，无权重衰减，bf16，seed 42），全局 batch 16（投影对齐阶段 32），4 GPU；损失仅为目标 token 交叉熵，无辅助损失。LoRA 注入注意力和 FFN 全部投影，α=32，dropout 0.05，可训练参数 64.63M（投影器 20.98M+LoRA 43.65M）。

### 📊 实验结果
**数据集**：SpatialSoundQA（AudioSet 源 + SoundSpaces2.0 仿真 BRIR，16kHz 双耳，单/双声源，MMAU/MMAR/AIR-Bench 作泛化评测）

**主要指标**：
- 单声源 DoA 73.58%（BAT 72.28%，DSPAST-BAT† 80.84%）；双声源 DoA 48.21%（最强基线 37.90%，+10.31）
- 单/双声源 DER 42.69%/64.72%（全表最低）；关系方向 BA 68.86%
- MMAU 44.50%、MMAR 34.80%、AIR-Bench 32.71%，全面超 BAT/OWL 等专用系统（BAT MMAU 33.20%）
- 左右探针：单源 93.0%（双耳）vs 74.0%（单耳），锁定差分是关键线索

**是否开源**：论文未提供代码链接

### ⭐ 评分：7/10
评分理由：问题诊断（信息不对称假说）与 2×2 受控实验设计是真正的科学贡献，因果链条清晰且统计严谨；仅训练约 40% 参数即超专用系统并兼顾通用音频理解，实用价值高。局限在于依赖仿真 BRIR 数据、未验证真实录音端到端 QA、绑定增益仍受限（异侧 L/R 70.4% 远低于同侧 89.0%），且无代码释出。属有实质洞察、实验较充分的强工作，但结论的通用性有待独立检验。

---

## [10] AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark

**arXiv ID**：2611.13957 | **方向**：语音大模型

**作者**：Haotian Qi, Gabriel Skantze

**机构**：KTH 皇家理工学院 语音、音乐与听觉系（斯德哥尔摩）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13957 | **PDF**：https://arxiv.org/pdf/2611.13957.pdf | **代码**：https://github.com/Haotian-Qi/AVCC | **Demo**：暂无

### 📌 简介
多人下一说话人预测（NSP）领域缺乏匹配真实机器人"单摄像头+单麦克风"条件的公开基准，也没有人类在同一切点的表现参照。本文将 31 小时双人/三人在线对话语料 AVCC 扩展为公开基准：新增说话人不重叠的 7 视频测试集（865 hold+865 shift 互静默间隙事件）、全语料词级强制对齐转写，并采集 154 名受试者在相同预测点的人类基线。评测 RoleVAP 与 MuVAP：MuVAP 在 NSP 上 63.3%（比平均受试者高 3.8 点、比多数投票低 4.4 点），hold/shift 平衡准确率 67.9%（RoleVAP 为 66.5%）。

### 🔧 技术方案

**问题背景：** 现有 NSP 研究多用逐人传感器（眼动仪、近讲麦、每人一摄像头）且各自定义事件，VAP 路线则依赖 Switchboard 等每说话人干净通道的电话语料；无任何公开基准覆盖机器人实际的单摄单麦多人场景，也无人类参照，导致"65% 准确率离信号上限多远"无从判断。

**模型架构：** 基准建立在 AVCC 上：29 段无剪辑在线视频（播客访谈/圆桌/游戏解说），InsightFace（SCRFD+ArcFace+匈牙利匹配）做人脸轨迹，TalkNet 初始化语音活动并逐段人工修正，Voxtral 转录+MFA 词级强制对齐后全量人工纠错。轮次事件定义为互静默间隙（原始间隙<3s、含 padding 后仍有≥0.1s 静音、下一发言者在前 1s 独占发言且 2s 内发话≥1s、无笑声），hold 随机下采样与 shift 配平。评测 RoleVAP（音频、角色相对 VAP）与 MuVAP（多模态），hold/shift 判决由训练集上拟合的逻辑回归探针从预测点嵌入读出。

**核心创新：** (1) 首个单摄单麦多人（2-3 人）NSP 公共基准：说话人不重叠的 7 视频测试分割（2-speaker 各 417 对、3-speaker 各 448 对事件），并附可复现全部数字的脚本。(2) 与模型评测点完全一致的人类参照基准：154 人（82 母语/40 近母语/32 高级）在 10 秒音视频切片上预测下一说话人并给 1-5 置信度。(3) 全语料词级强制对齐转写与系统性分析维度：按说话人数、按置信度、hold/shift 分类拆解模型-人类差距。

**训练策略：** 复用 MuVAP 原始训练配置，仅在其训练分割（17 视频 20 小时 39 分；验证 5 视频 2 小时 41 分）上拟合逻辑回归探针读出，不重新训练主干；测试 7 视频共 7 小时 41 分。人类实验经三条质量规则过滤（188 人中剔除 34 人）。

### 📊 实验结果
**数据集**：AVCC，31 小时（29 视频、2/3 人对话、单静态摄像头+单声道音轨），测试集 1730 事件（865 hold/865 shift）

**主要指标**：
- NSP 平衡准确率：MuVAP 63.3%（2-speaker 67.5%、3-speaker 59.4%）；Human-Ind 59.5%，Human-Maj 67.7%
- Hold/shift 平衡准确率：MuVAP 67.9%、RoleVAP 66.5%；Human-Ind 64.0%，Human-Maj 70.1%；随机基线 50%
- 关键对比：MuVAP 高平均人类 3.8 点（NSP）但低多数投票 4.4 点；视频较纯音频 hold/shift 提升 1.4 点；两模型均过预测 shift（hold 仅 54.9%/58.7% vs 人类 72.5%）；人类 2→3 人 NSP 掉 6.1 点，MuVAP 掉 8.1 点
- 人类 hold 准确率随置信度 1→5 从 43.2% 升至 85.0%，shift 置信度几乎无信息（51.5%-60.1%）

**是否开源**：是，标签、转写、逐条人类数据与复现脚本发布于 GitHub（Haotian-Qi/AVCC）

### ⭐ 评分：7/10
评分理由：填补了单摄单麦多人轮次预测无公开基准、无人类参照的明确空白，语料标注管线（人工校验 VAP/人脸/强制对齐）扎实且全量开源，可复现性强。人类基线是最大亮点，置信度分析揭示"shift 低置信难预测"对数据筛选有直接价值。局限在于模型侧仅评测既有 RoleVAP/MuVAP 并只加探针读出，未探索文本线索或更新的多模态方法，且测试事件在视频间分布不均（单视频贡献超 60%），泛化结论需谨慎；作为资源型论文实验仍属充分。

---

## [11] On the information rate of phones, syllables and words

**arXiv ID**：2611.13990 | **方向**：语音大模型

**作者**：Herman Kamper

**机构**：Stellenbosch University 电子与电气工程系（南非）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13990 | **PDF**：https://arxiv.org/pdf/2611.13990.pdf | **代码**：https://github.com/kamperh/inforate/ | **Demo**：暂无

### 📌 简介
编码同样语音内容时，phone、音节、词、词组哪个语言学单元信息率最低？文献报告的 phone 约 50 bps、音节约 39 bps 口径不一、不可直接比较。作者在 LibriSpeech 960h 英语有声书的强制对齐音素序列上，先用概率链式法则证明完美模型下所有切分单位的信息率严格相等，进而在"有限建模预算"下用 n-gram 与 20M 参数 transformer 统一以留出集交叉熵率计算 bps。结果显示词单元最优（28.07 bps），略大于词的 word-BPE 合并偶有小增益，phone（29.56）、音节与过多合并的长单元均更差；Qwen2.5-3B 可达 25.26 bps 作为参照上限。

### 🔧 技术方案

**问题背景：** 信息率是语音单元选择、人类语言效率理论与零资源单元发现的核心度量，但既有研究定义与估计数据各异无法横比。作者指出该问题在理想信源编码下平凡（单位等价），只有模型容量受限时切分粒度才影响比特开销，现有文献缺少同数据、同预算的系统对比。

**模型架构：** 比特率定义为留出集上 −log2Pθ(wt|w1:t−1) 之和除以语音时长（秒）。两类有限模型：(1) 三阶 n-gram，绝对折扣平滑，逐阶按 d=n1/(n1+2n2) 设折扣并钳制在 [0.1,0.9]，未见的音节/词回退到音素拼写 n-gram 模型；(2) OPT-125M 改造的 decoder-only transformer，主体约 20M 参数（6 层、512 维、8 头、FFN 2048、上下文 2048、pre-LN+ReLU、输入输出 embedding 绑定），仅输出层随单元变化（phone 层 39 类、词层约 56k 类）。单元体系：39 个无重音 ARPABET 音素、规则法音节、按唯一语音实现定义的词型，并在词级 token 上做 BPE 合并（200/1000/5000 次）构造多词单元，所有大单元展开为音素保证一一对应。

**核心创新：** (1) 理论澄清+统一口径：证明完美模型下任意 tokenisation 的信息率相同，把研究问题精炼为"受限建模预算下的相对编码效率"，并用留出交叉熵率替代 zero-resource 挑战的 unigram/bigram 期望口径，兼顾泛化。(2) 词级 BPE：把 BPE 从字符迁移到词 token 层面生成多词单元，并保留音素可逆映射，首次在 phone—音节—词—短语粒度谱系上公平对比。(3) 多层 sanity check：子词 BPE（2000 词表）插值验证、以字符为原子的正字切分层复验、用数据与参数规模巨大的 Qwen2.5 验证估计值接近真实比特率下界。

**训练策略：** n-gram 在 960h 训练集上阶数 1–5 搜索，多数单元三阶最优，拼写模型固定三阶。transformer 在单张 RTX3070（8GB）上训练约 20 个 epoch，有效 batch 40，AdamW，前 8% 步线性 warmup 至 1e-3 后余弦退火至 2e-5；手机 token/参数比约 1.69，5 个随机种子报标准差；用 B=10000 说话人级 bootstrap 检验显著性；Qwen 检查对每条评测语句前置 train-clean-100 小写无标点 primer 以适配其训练域。

### 📊 实验结果
**数据集**：LibriSpeech 960h 训练集（音素 33.46M tokens/39 types、音节 13.03M/13,656、词 9.40M/84,163）强制对齐，dev-clean 评测（5.4h、40 位说话人）

**主要指标**（bps，音素层）：
- transformer 词单元：28.07（全场最优）
- 音素：29.56；word-BPE 5000 合并：29.27；phone 子词 BPE（2k 词表）：28.98±0.28
- n-gram：word-BPE 200 最优，词与 word-BPE 1000 并列 31.05，phone 子词 BPE 31.59
- 字符层最优（正字词）：27.48；Qwen2.5-1.5B/3B：25.90/25.26
- 关键对比：transformer 下最优词 28.07 vs 最差音素 29.56，差 1.49 bps（约 5%）；音节与短语级单元均劣于词

**是否开源**：是，代码发布于 https://github.com/kamperh/inforate/

### ⭐ 评分：7/10
评分理由："完美模型下单位等价、预算受限时才分高下"的理论澄清加上同数据同预算的系统对比，是语音 LM 建模单元（SyllableLM、Sylber 等）与零资源单元发现社区急需的参考基准，词/略大于词单元优于音节与长短语的结论有 bootstrap 统计支撑。实验设计严谨、多层 sanity check 到位，但仅覆盖英语、纯文本/音素序列而非真实语音，20M 预算偏小且词与最优 BPE 差距有限，实用指导偏定性。属扎实的中上层贡献，非突破。

---

## 语音前端

## [12] Which Acoustic Features Survive Compression? Tracker-Estimated First-Formant Statistics for Codec-Robust Audio Deepfake Detection

**arXiv ID**：2611.13258 | **方向**：语音前端

**作者**：Yash Sukhdeve, Aaron Storey, Masudul H. Imtiaz

**机构**：Clarkson University（美国波茨坦，电子与计算机工程系/计算机科学与工程系）

**发布日期**：2026-11-09 | **论文**：https://arxiv.org/abs/2611.13258 | **PDF**：https://arxiv.org/pdf/2611.13258.pdf | **代码**：暂无（代码与预计算结果随补充材料发布，未提供公开仓库链接） | **Demo**：暂无

### 📌 简介
在干净录音上训练的深伪检测器经过电话/流媒体编解码后常大幅退化，但"哪些手工声学描述子在压缩后仍具判别力"从未被逐特征量化。本文对 36 个 utterance 级特征（共振峰、PNCC、LFCC、韵律）在 ASVspoof 2019 LA 上筛选，并在官方 ASVspoof 2021 LA 的 7 种 codec 条件下评估。33 个特征统计显著，但仅 4 个达到大效应量（|r|>0.5），且全部为第一共振峰 F1 统计量（高度冗余，PC1 解释 79% 方差）。4 特征 RBF-SVM 在 codec 失配下 EER 仅退化 5.9pp（17.0%→22.9%），远优于 36 特征模型的 14pp 退化（9.5%→23.5%），跨条件 EER 波动 3.4pp 对比 13.1pp。

### 🔧 技术方案

**问题背景：** 司法与生物识别场景中，检测器依赖的精细谱线索会被有损压缩扭曲或抹除，且神经嵌入不可解释。现有工作把前端当整体黑盒，缺乏逐特征、逐 codec 条件的退化测量。

**模型架构：** 无深度网络，是一条"特征存活分析流水线"：共振峰用 Praat/parselmouth Burg 法（25ms 窗、ceiling 5500Hz、F1 限 200–1200Hz 作为浊音帧代理）；PNCC 为 40 通道 gammatone（80–7500Hz）13 阶；LFCC 为 20 线性滤波器 8 阶；韵律含 pYIN F0、RMS 能量等 7 项，共 36 个 utterance 级标量。筛选按递进协议：分布检验→Mann-Whitney+Benjamini-Hochberg→rank-biserial 效应量（bootstrap 95%CI，阈值 |r|>0.5）→跨攻击 Kruskal-Wallis→PCA 冗余分析→逐 codec EER，最终用 RBF-SVM（C=1.0、γ=scale、balanced 类权重）检测。

**核心创新：** (1) 把"统计显著"与"实用可部署"解耦：25K 样本下 33/36 特征 p 值显著，但效应量筛后只剩 4 个 F1 指标，说明显著性不足以指导部署特征选择。(2) 发现 F1 是唯一大效应存活族且四点同向——真人语音 F1 更高、更宽、方差更大（合成音低估声道共振物理变化），4 个描述子共享一个潜维度（PC1=79%）。(3) 多路验证闭环：反事实扰动显示沿 F1 方向平移使 76.4% 边界样本翻转（随机方向仅 5.1%），混合效应模型控制说话人后 p 极显著，配对 codec 分析量化 MP3/AAC 仅侵蚀 1–10% 类间隔而 G.711 侵蚀 13–51%。

**训练策略：** 仅在 ASVspoof 2019 LA 干净训练集（25,380 条：2,580 真/22,800 假，6 种 TTS/VC 攻击）训练，遵守 2021 协议不微调；SVM 取 scikit-learn 默认、5 种子复现（std<0.2%）；辅以逻辑回归/MLP/随机森林验证结论不依赖分类器族。

### 📊 实验结果
**数据集**：ASVspoof 2021 LA 官方评估集（181,566 条，13 种未见攻击 A07–A19×7 种 codec 条件，每条件 25,938 条）+ In-the-Wild（31,779 条）跨库探针

**主要指标**：
- 4 特征 F1-SVM：2021 LA 总体 EER 22.9%（范围 21.6–25.0%，最差 G.711 μ-law），跨 codec 波动 3.4pp；36 特征 SVM 23.5%，PSTN 达 31.1%，波动 13.1pp
- 对比 AASIST：干净集 1.73%→2021 LA 30.7%（约 18 倍退化，PSTN 46.7%），F1-SVM 仅约 1.2 倍退化
- ITW 跨库：F1-SVM 34.7% EER，36 特征模型崩至 50.0%（随机水平）
- 关键差值：dev→eval 退化 F1 仅 +5.9pp vs 全特征 +14pp

**是否开源**：代码与预计算结果在论文补充材料中；数据集来自 ASVspoof 联盟与 Zenodo，无公开 GitHub 链接

### ⭐ 评分：7/10
评分理由：提问角度独特且实用——不做新模型而系统量化"特征存活率"，筛选协议（显著性/效应量解耦、bootstrap CI、混合效应、反事实探针）统计严谨，对司法取证场景价值明确。实验覆盖官方 2021 LA 逐 codec 条件与跨库 ITW，充分性较好。局限是绝对性能（20–25% EER）远逊神经 SOTA，共振峰追踪器本身在退化音频上的偏差难以完全排除（作者自己承认），且"稳定性优于精度"的定位削弱了单独部署价值。属于实质贡献扎实的测量型分析工作。

---

## [13] GigaEdge Spench: An SDK for Practical Streaming Speech Enhancement

**arXiv ID**：2611.13243 | **方向**：语音前端

**作者**：Artem Sokolov, Artem Khaidarov, Yana Lysova, Alexander Gladkikh, Vitaliy Yulis

**机构**：SberDevices / Sber（salute-developers）

**发布日期**：2026-11-09 | **论文**：https://arxiv.org/abs/2611.13243 | **PDF**：https://arxiv.org/pdf/2611.13243.pdf | **代码**：https://github.com/salute-developers/gigadenoiser | **Demo**：暂无

### 📌 简介
针对神经降噪模型难以在真实应用中满足流式回调、状态保持、多采样率与多平台部署的问题，提出开源 SDK GigaEdge Spench：以共享 C++ 核心构建可配置"增强通道"（神经降噪+可选归一化 DSP 链+SpeexDSP AEC），一套代码覆盖服务器/Android/iOS/浏览器（ONNX Runtime 与 TFLite），流上下文共享模型实例且一次推理可处理连续多帧。释放 8k INT8 与 48k FP32 判别式/混合三个模型。EARS-WHAM v2 上 48k 混合模型 PESQ-WB 1.87、NISQA MOS 3.20 全面优于 RNNoise（1.53/2.17），共享模型并发容量 151 路（判别式）与 56 路（混合）为 sherpa-onnx/DPDFNet2 的 10.07/3.73 倍，全部配置超实时。

### 🔧 技术方案

**问题背景：** 实验室降噪模型落地需对接音频回调的任意块大小、保留逐流状态并承担完整信号链成本；已有系统（Asteroid/ESPnet-SE 偏科研，sherpa-onnx 的 GTCRN/DPDFNet 流式实现将模型与单一状态耦合、每次推理仅一帧）未提供可配置管道与部署权衡研究。

**模型架构：** 分层"增强通道"：可选 AEC（SpeexDSP 1.2.1）→可选择块的归一化链（响度控制/AGC/动态压缩/噪声门/限幅器，可无模型独立运行）→神经降噪→输出重采样，输入/输出采样率可与模型率独立。判别式模型基于改造 FullSubNet，32ms 窗/16ms hop；混合模型在冻结的判别式增强器外接 GAN 训练的生成组件。共享 C++ 核心+ONNX 适配器，流状态（RNN/卷积历史/重采样器/统计量）与推理 session 分离，新流不新建 session；单帧调用可沿时间轴打包 m 个连续谱帧（chunk=m×16ms）。

**核心创新：** (1) 模型/上下文显式分离+时间帧分组：一次推理处理同流多帧，使 chunk 大小成为可调的吞吐-延迟旋钮，实验证明大 chunk 可替代多进程（如 128ms×2 进程吞吐超 16ms×8 进程）。(2) 端到端部署研究：统一口径对比加权 MAC、整链 RTF 与共享模型并发容量，揭示算术量与实测容量不成比例（混合模型算术为 DPDFNet2 的 57.8% 但容量比为 3.73）。(3) 一核多平台封装：C/C++/Android/iOS/WebAssembly(AudioWorklet+共享内存)，含自适应缓冲策略（B_k=64ms+32ms×补播次数）。

**训练策略：** 三模型均用内部数据训练（不含 EARS/WHAM 素材），48k 输出延迟 16ms；SDK 不含训练/量化工具。8k 模型 INT8：397,688 MAC/16ms hop（24.86 MMAC/音频秒）；48k 判别式/混合 FP32 ONNX；RNNoise 稀疏口径 107.33、DPDFNet2 2283.97 MMAC/音频秒。

### 📊 实验结果
**数据集**：EARS-WHAM v2（886 对噪声/clean，48kHz；8k 条件降采样输入；Intel Core Ultra 5 125H/18 逻辑核，WSL2）

**主要指标**：
- 48kHz：判别式/混合 PESQ-WB 1.88/1.87，ESTOI 0.76/0.77，SI-SDR 12.62/12.86dB，NISQA MOS 2.69/3.20，DNSMOS P.808 3.19/3.45；DPDFNet2 最优（2.21/0.81/14.69dB/3.81）
- 8kHz：Spench INT8 PESQ-NB 2.28、SI-SDR 10.99dB，优于 RNNoise 全带处理后降采样（2.16/9.03dB，+1.96dB）
- 关键对比：混合较 RNNoise NISQA MOS +1.03 但算术 +12.3 倍；较 DPDFNet2 算术省 42.2%；单流整链 RTF 原生 0.65–9.89%、Web 1.42–24.38% 音频时长，均超实时；并发容量：8k INT8 593±8 路、判别式 151±1、混合 56±1，RNNoise 1089±30 路最高

**是否开源**：是，SDK 与三个模型已开源（GitHub）

### ⭐ 评分：6/10
评分理由：作为工程/部署类论文较扎实——模型-状态分离、帧分组推理等机制虽非全首创，但其集成方式与"模型×chunk×并发流"联合实验设计填补了部署度量口径的空白，对会议软件选型有直接价值。不足：核心 48k 混合模型架构与训练细节被声明超出范围，无主观听测，仅一台设备与单一基准，DPDFNet2 容量对比经过作者改造而非原生使用方式。质量上限不及 DPDFNet2 而容量优势明显，属高质量增量式系统工作而非算法突破。

---

## [14] Off-target posterior mass: A training-free diagnostic for fine-tuning spoken language diarization probes

**arXiv ID**：2611.13430 | **方向**：语音前端

**作者**：Zhuoyan Tao, Aditya Kommineni, Shrikanth Narayanan

**机构**：南加州大学（USC）Signal and Image Processing Institute（第一作者现属 CMU LTI）

**发布日期**：2026-11-10 | **论文**：https://arxiv.org/abs/2611.13430 | **PDF**：https://arxiv.org/pdf/2611.13430.pdf | **代码**：暂无（论文声明接收后开源） | **Demo**：暂无

### 📌 简介
口语语言日志化（SLD）中微调预训练语音模型探针带来的 LDER 增益强依赖语料，但事先无法判断某未标注语料是否值得标注与微调。本文提出免训练、免标签的诊断指标 OTPM：预训练模型 LID 后验落在非目标语言上的概率质量占比，并用 OLS 拟合预测 probe gain。在 FLEURS 合成的 19 个未见双语对上，Whisper base/large-v3 的 Spearman 相关达 0.56–0.69；迁移到 SEAME/VoxPopuli/DISPLACE 真实语料仍有正相关（ρ 0.23/0.27），且显著优于 LDER 基线（MSE 42.6 vs 428）。

### 🔧 技术方案

**问题背景：** SLD 级联管线（VAD→预训练模型逐窗后验/嵌入→AHC 聚类）的微调增益随语料差异极大；现有可迁移性指标（NCE、H-score、LEEP、LogME）均需已标注目标数据，无法用于标注前的数据策展决策。

**模型架构：** 三段级联：Silero VAD 切语音；10 s 窗、0.4 s 跳长，从 Whisper base（74 M）或 large-v3（1.55 B）提取（a）99/100 维 LID 后验，或（b）均值池化的 512/1280 维编码器输出；冻结主干上训练逻辑回归探针（posterior probe / encoder probe），替换后验后做余弦平均链接 AHC（GMM 标定阈值+0.015 偏移）+ VBx 重分割，dscore 计 LDER（无 collar、含重叠）。OTPM 定义为每窗对非目标语言集合 L∖T 的后验质量和、按窗与 utterance 平均。

**核心创新：** (1) OTPM 指标：仅凭语料的目标语言集合即可从预训练后验直接计算，零训练零标签，输出 [0,1]，值越大说明后验越"跑偏"到非目标语言、微调可重分配的空间越大。(2) 假设检验框架：以 32 个合成双语对拟合 Δ̂=α+β·OTPM，在 19 个未见语言对上验证增益预测，并配套"collapse"（聚类塌缩成单簇）现象的识别与剔除分析。(3) 系统对比与消融：与预训练 LDER 基线、训练集规模 N∈{50..400} 交互、以及 Whisper 预训练时长先验（与 OTPM 相关 −0.77，但在未见对上 ρ 仅 0.31–0.32，明显输给 OTPM）逐项对照。

**训练策略：** FLEURS 每语言取 10 条测试句拼接、0.3 s 间隔合成 45 句/对；探针在每对上以 N=400 句训练；真实语料分别用 150/60/34 条录音做域内训练。统计用 10k 残差自助 CI、LOO Q²、单侧 Spearman 与分层 ρ。

### 📊 实验结果
**数据集**：FLEURS 合成双语对（32 训练+19 测试）；SEAME 中英（30 条/21.0 h）、VoxPopuli 德英（40 场/36.2 h）、DISPLACE 2024 远场英/印地/马拉雅拉姆（32 条/17 h）

**主要指标**：
- 合成未见对 Spearman ρ：posterior probe 0.68、encoder probe 0.56（base）；large-v3 达 0.65/0.69
- OLS 拟合（N=400）：encoder probe β=33.75 [25.1,42.4]，R²=0.65、Q²=0.60；posterior probe 剔 collapse 后 β=21.75，Q²=0.62
- 真实语料：probe 实测增益 SEAME +3.34/+3.81、VoxPopuli +6.20/+6.62、DISPLACE +2.28/+4.44 LDER 点；OTPM 分层 ρ=0.23（encoder）/0.27（posterior）
- 关键对比：真实域预测 MSE 42.6（OTPM）vs 428（LDER 基线）；base 与 large-v3 间 mean OTPM 0.46 vs 0.26、mean 增益 8.7 vs 5.8 pt

**是否开源**：数据全部公开；代码与逐对结果承诺论文接收后开源，暂未发布

### ⭐ 评分：6/10
评分理由：问题设定实用——为 SLD 数据策展提供免标注的"该不该微调"判据，视角新颖且统计规范（自助 CI、LOO、分层 ρ、collapse 归因）。但本质是单一启发式指标+线性回归的增量工作，OTPM 完全忽略目标语言间混淆（土阿、希乌对严重低估增益），合成数据等比例拼接与真实代码转换分布错配导致 OLS 外推到语料级过预测 2–3 倍，真实域 ρ≈0.25 只能作弱排序信号。对语音前端工程团队有直接采纳价值，学术突破有限。

---

本批次 14 篇 arXiv HTML 全文均抓取解析成功。

---

*Generated on 2026-11-11*
