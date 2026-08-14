# 2026-08-13 语音论文速递

**共收录**: 11 篇 | **语音大模型**: 8 篇 | **语音前端**: 3 篇

> 今日 arXiv 语音相关论文共命中 11 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

---

## [1] Luna-TTS Family: A Unified Speech-Text Foundation Model

**arXiv ID**：2608.11593 | **方向**：语音大模型 / TTS

**作者**：Feng Yin, Shuai Shi, Junjie Zheng, Kechenying Zhou, Yiqiu Wang, Chenyang He, Qiuhua Jiang, Mengxiao Bi, Yanmin Qian, Mingxin Chen, Xun Gong, Tianteng Gu, Bing Han, Peng Jiang, Chenda Li, Haiyang Sun, Han Wang, Wei Wang, Yi Wang, Leying Zhang, Wangyou Zhang, Chushu Zhou

**机构**：VUI Labs, Alibaba DAMO Academy

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.11593 | **PDF**：https://arxiv.org/pdf/2608.11593.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对现有TTS系统在语音质量、自然度、可控性和多语言泛化能力上的不足，Luna-TTS提出基于扩散语言模型的统一语音-文本基座模型系列。模型基于Qwen3-0.6B通过渐进式因果→双向→块因果注意力适配，在100万小时中英日韩四语数据上预训练。Luna-TTS全非自回归版本在Seed-TTS-Eval上达到test-zh CER 0.73%/SIM 79.7%和test-en WER 1.49%/SIM 76.8%，Luna-TTS Realtime实时版实现0.024 RTF和41.6ms首块延迟。此外，Luna-Codec以25Hz帧率、8码本RVQ、2.2kbps码率，并通过WavLM蒸馏第一码本，实现了高质量语音离散化。

### 🔧 技术方案

**问题背景：** 现有TTS系统在多语言、多场景下的语音质量、自然度和可控性仍不理想，尤其是实时推理场景中非自回归模型与自回归模型之间的效率-质量权衡问题。扩散模型在TTS中展现出潜力，但缺乏统一的预训练框架和高效的实时解码方案。

**模型架构：** 基于Qwen3-0.6B（约6亿参数）作为语言模型基座，通过渐进式注意力适配策略进行改造：(1) 第一阶段保持因果注意力进行语言模型预训练；(2) 第二阶段切换为双向注意力进行语音理解；(3) 第三阶段采用块因果注意力（block-causal）实现语音生成。Luna-TTS全非自回归变体采用32步迭代并行解码；Luna-TTS Realtime采用块自回归架构，每块1.28秒，利用KV缓存实现流式推理。Luna-Codec采用25Hz帧率、8码本RVQ残差矢量量化，码率2.2kbps，第一码本通过WavLM蒸馏获得语义感知能力。

**核心创新：** (1) 渐进式注意力适配策略——从因果到双向再到块因果，使同一个0.6B模型能够同时支持语音理解、非自回归生成和流式生成三种任务范式，无需为每种任务单独训练模型。这与现有方法需要为不同任务设计不同架构的做法形成鲜明对比。(2) 全非自回归+块自回归双模式设计——Luna-TTS支持全非自回归（32步并行解码，高质量）和块自回归（KV缓存流式，低延迟）两种推理模式，用户可根据场景灵活选择，突破了传统TTS系统单一推理模式的限制。(3) 基于GRPO的强化学习后训练——引入带组相对策略优化的强化学习来优化生成质量，使模型在口语表达、韵律多样性等难以用传统损失函数衡量的维度上显著提升。(4) Luna-Codec的WavLM蒸馏语义感知——将第一码本显式蒸馏为语义感知特征，使后续码本只需关注声学细节，提升了整体编解码质量。

**训练策略：** 100万小时多语言数据（中文、英文、日文、韩文）。预训练阶段采用标准语言模型训练目标，后训练阶段采用GRPO强化学习。Luna-Codec训练采用多阶段码本学习和WavLM特征蒸馏。

### 📊 实验结果
**数据集**：Seed-TTS-Eval (test-zh, test-en)

**主要指标**：
- test-zh CER: 0.73%
- test-zh SIM: 79.7%
- test-en WER: 1.49%
- test-en SIM: 76.8%
- Luna-TTS Realtime RTF: 0.024
- Luna-TTS Realtime 首块延迟: 41.6ms
- Luna-Codec码率: 2.2kbps

**是否开源**：未开源

### ⭐ 评分：9/10
评分理由：规模化（100万小时、4语种）、架构创新性（渐进式注意力适配、双模式推理）、工程完备性（实时RTF 0.024）均达到业界顶尖水平。GRPO后训练引入强化学习是语音生成领域的重要探索。缺乏代码开源和更大规模参数量模型的消融实验是主要扣分点。

---

## [2] Phoenix TTS: A Joint Training Framework for Tokenizer and Flow Matching Based Text-to-Speech

**arXiv ID**：2608.11737 | **方向**：语音大模型 / TTS

**作者**：Peijie Chen, Zhuanling Zha, Zhipeng Nie, Weijie Wu, Yiming Liu, Daiyu Huang, Junbo Li, Jun Fang, Naiqiang Tan, Hua Chai, Qingyang Hong

**机构**：Didichuxing Co. Ltd, Xiamen University

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.11737 | **PDF**：https://arxiv.org/pdf/2608.11737.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
Phoenix TTS针对语义token与声学空间之间的特征不匹配问题，提出联合训练语义Tokenizer和Flow Matching解码器的统一框架。UniSpeechTokenizer基于W2v-BERT 2.0第16层特征+6层Conformer编码器+VQ（码本8192），以25Hz帧率输出语义token，并通过LLM（Qwen2.5-0.5B，24层）预测语义token序列。Flow Matching解码器采用18层DiT，在110K小时（50K中文+60K英文）数据上训练。LibriSpeech-PC上WER 1.94%（低于GT 2.06%），SIM 0.718，主观SMOS 4.09（英文）和4.10（中文），并支持零样本语音转换。

### 🔧 技术方案

**问题背景：** 现有神经编解码语言模型TTS系统中，语义tokenizer和声学tokenizer/解码器通常独立训练，导致语义token携带的信息与声学解码器期望的特征之间存在不匹配。这种不匹配限制了语音质量和说话人相似度。

**模型架构：** Phoenix TTS由三部分组成：(1) UniSpeechTokenizer——基于W2v-BERT 2.0第16层Transformer输出，经过6层Conformer编码器后通过VQ（码本大小8192）得到25Hz语义token序列。Tokenizer总参数量约200M。(2) 语义LLM——基于Qwen2.5-0.5B（24层decoder-only Transformer），以语义token+文本token为输入，自回归预测语义token序列。(3) Flow Matching解码器——18层DiT（Diffusion Transformer），以LLM预测的语义token为条件，通过CFM生成Mel谱，再经HiFi-GAN合成波形。

**核心创新：** (1) 联合训练框架——Tokenizer、LLM和Flow Matching解码器通过端到端的联合训练实现语义特征与声学特征的对齐，消除了传统流水线方法中特征不匹配的问题。这与CosyVoice等独立训练各模块的方法有本质区别。(2) UniSpeechTokenizer的语义感知设计——利用W2v-BERT 2.0自监督语义特征（第16层）作为VQ输入，而非传统方法中的Mel谱或HuBERT离散特征，使语义token更自然地携带语言学内容，同时保留副语言信息。(3) 零样本语音转换的零微调能力——由于Tokenizer提取的是内容+说话人混合特征，在解码时只需改变说话人条件即可实现VC，无需额外训练或微调。

**训练策略：** Tokenizer训练：8×A100 (80GB)，960 samples/batch/GPU，10个epoch，lr=1e-4。LLM训练：32×A100 (80GB)，400 samples/batch/GPU，3个epoch，lr=3e-4。总训练数据110K小时（50K中文+60K英文）。对于LLM训练，采用下一token预测损失，语义token序列长度约对应音频时长×25。

### 📊 实验结果
**数据集**：LibriSpeech-PC, SeedTTS-EN, SeedTTS-ZH, 内部中文测试集

**主要指标**：
- LibriSpeech-PC WER: 1.94%（GT 2.06%）
- SeedTTS-EN WER: 1.56%
- SeedTTS-ZH CER: 1.16%
- SIM: 0.718 (LibriSpeech-PC), 0.720 (SeedTTS-EN), 0.778 (SeedTTS-ZH)
- SMOS: 4.09 (EN), 4.10 (ZH)

**是否开源**：未开源

### ⭐ 评分：8/10
评分理由：联合训练Tokenizer与解码器的思路新颖，解决了语义-声学特征不匹配的关键问题。WER优于GT说明合成语音的可懂度已超越真人录音。110K小时训练数据规模合理。缺点在于缺乏代码开源，且未在更大规模数据（百万小时级）上验证扩展性。

---

## [3] Confucius4-TTS: Cross-lingual Zero-Shot TTS

**arXiv ID**：2608.11650 | **方向**：语音大模型 / TTS

**作者**：Huaxuan Wang, Huimin Wang, Ruiyu Zhang, Yingjie Li, Yitao Duan

**机构**：NetEase Youdao, Beijing

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.11650 | **PDF**：https://arxiv.org/pdf/2608.11650.pdf | **代码**：https://github.com/netease-youdao/Confucius4-TTS | **Demo**：暂无

### 📌 简介
Confucius4-TTS针对跨语言零样本TTS中参考音频缺乏转录文本的问题，提出无需参考音频转录本的跨语言语音克隆方法，支持14种语言。两阶段架构包括T2S（24层decoder-only Transformer，hidden size 1280）和S2A（DiT CFM），说话人编码器结合ECAPA-TDNN和w2v-BERT 2.0自监督特征。在500K小时14语言数据上训练，CV3-Eval跨语言平均WER 3.73%，Seed-TTS-Eval上英文WER 1.49%/SIM 0.700，中文CER 0.94%/SIM 0.765。

### 🔧 技术方案

**问题背景：** 跨语言零样本TTS面临两个核心挑战：(1) 目标语言的参考音频通常没有对应文本转录，限制了训练数据的可用性；(2) 跨语言场景中说话人特征与语言特征的解耦困难，容易出现"口音泄露"问题。

**模型架构：** 两阶段设计：(1) T2S（Text-to-Semantic）——24层decoder-only Transformer，hidden size 1280，以文本+说话人嵌入为条件，自回归预测语义token序列（25Hz）。说话人编码器将ECAPA-TDNN（说话人身份特征）与w2v-BERT 2.0第16层SSL特征（语言无关的声学-语义特征）拼接，通过注意力融合得到说话人嵌入。(2) S2A（Semantic-to-Acoustic）——基于DiT的条件流匹配模型，将语义token序列转换为Mel谱，再经HiFi-GAN合成波形。

**核心创新：** (1) 无需参考音频转录本的训练范式——T2S阶段虽然以文本为条件，但训练时不需要参考音频的对应文本，而是通过自监督语义token的预测目标来隐式学习文本-语音对齐。这极大扩展了可用训练数据范围。(2) 双模式克隆——支持reference cloning（给定参考音频克隆风格）和continuation cloning（仅给定说话人特征，不依赖参考音频风格），后者的灵活性在现有方法中较少见。(3) 说话人编码器的SSL-ECAPA融合——w2v-BERT 2.0提供的语言无关特征与ECAPA-TDNN的身份特征互补，使模型在跨语言场景中能更好地分离语言与说话人信息。

**训练策略：** 500K小时14语言数据。T2S训练：32×A40 GPU。S2A训练：CFM损失函数。训练数据包含中文、英文、日文、韩文、法文、德文、西班牙文、葡萄牙文、阿拉伯文、俄文、意大利文、荷兰文、波兰文、土耳其文共14种语言。

### 📊 实验结果
**数据集**：CV3-Eval (跨语言), Seed-TTS-Eval

**主要指标**：
- CV3-Eval 跨语言平均WER: 3.73%
- Seed-TTS-Eval EN WER: 1.49%
- Seed-TTS-Eval EN SIM: 0.700
- Seed-TTS-Eval ZH CER: 0.94%
- Seed-TTS-Eval ZH SIM: 0.765

**是否开源**：代码已开源（GitHub）

### ⭐ 评分：8/10
评分理由：无需参考音频转录本的训练范式具有重要的实用价值，14语言支持覆盖面广。代码已开源是重要加分项。500K小时训练数据规模合理。缺点：跨语言WER 3.73%相比单语言系统仍有差距，且iWAS的说话人相似度在跨语言场景下提升空间较大。

---

## [4] CookVoice: Unified Voice-Singing Generation

**arXiv ID**：2608.11590 | **方向**：语音大模型 / 语音+歌声生成

**作者**：Haowei Lou, Hye-Young Paik, Dai Jia, Kai Li, Lina Yao

**机构**：UNSW Sydney, Dolby Laboratories

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.11590 | **PDF**：https://arxiv.org/pdf/2608.11590.pdf | **代码**：暂无 | **Demo**：https://haoweilou.github.io/CookVoice/

### 📌 简介
CookVoice提出统一的语音与歌声生成框架，将语音信号分解为内容（content）、韵律（prosody）和风格（style）三个正交要素，并分别建模。Flow Matching DiT结合HiFi-GAN自编码器，总参数量仅43.51M（DiT-S），在168小时数据上训练。模型支持文本/语音风格控制和离散/连续韵律控制，F0相对音高归一化有效解耦风格与韵律。S-SIM达91.65%（TTS）和95.00%（TTSV），F0-CORR达0.7102（TTS）和0.8425（TTSV），仅需4步ODE采样即可推理。

### 🔧 技术方案

**问题背景：** 语音生成和歌声生成通常由独立系统处理，缺乏统一的生成框架。现有方法在风格控制、韵律控制和内容保真度之间的权衡不理想，且参数量大、推理效率低。

**模型架构：** 总参数量43.51M（DiT-S），包含：(1) 内容编码器——提取音素级别的语言学内容；(2) 韵律编码器——建模F0、能量、时长等韵律特征，采用F0相对音高归一化（relative pitch normalization）以消除风格对韵律的影响；(3) 风格编码器——从参考音频提取全局风格表征；(4) 生成器——Flow Matching DiT以内容、韵律、风格三要素为条件，生成Mel谱；(5) 解码器——HiFi-GAN自编码器将Mel谱转换为波形。三要素在帧级别对齐，支持文本风格控制（通过文本描述控制风格）和语音风格控制（通过参考音频控制风格）。

**核心创新：** (1) 三要素正交分解——将语音信号显式分解为content/prosody/style三个正交要素，每个要素由独立编码器建模。这种解耦使模型能够独立控制每个维度，例如在保持内容不变的情况下改变风格或韵律。(2) F0相对音高归一化——将F0转换为相对音高（相对于该说话人的平均音高），有效消除了风格信息对韵律特征的干扰，使韵律编码器更专注于节奏、重音等纯韵律信息。(3) 极轻量级设计——43.51M参数在单张RTX 5090上即可训练800K步，仅需4步ODE采样即可推理，远低于主流扩散TTS模型所需的数十步采样。

**训练策略：** 168小时训练数据（包含语音和歌声）。Flow Matching损失函数。单张RTX 5090 GPU训练800K步。推理时采用4步ODE采样（DPM-Solver）。

### 📊 实验结果
**数据集**：内部测试集

**主要指标**：
- S-SIM (TTS): 91.65%
- S-SIM (TTSV): 95.00%
- F0-CORR (TTS): 0.7102
- F0-CORR (TTSV): 0.8425
- 推理步数: 4 ODE steps
- 参数量: 43.51M

**是否开源**：未开源，有Demo页面

### ⭐ 评分：8/10
评分理由：统一语音+歌声生成框架设计精巧，三要素分解思路清晰且有效。43.51M极轻量级参数具有实际部署价值，4步推理效率突出。F0相对音高归一化是简单但有效的设计。缺点：训练数据仅168小时，在大规模数据上的扩展性未验证；缺乏在标准公开基准上的评测结果。

---

## [5] On-Policy Self-Distillation for Multi-Dialect ASR

**arXiv ID**：2608.11898 | **方向**：语音大模型 / ASR

**作者**：Shuiyuan Wang, Bingshen Mu, Pengshen Zhang, Chengyou Wang, Yujie Liao, Chengdong Liang, Binbin Zhang, Qiangze Feng, Lei Xie

**机构**：Northwestern Polytechnical University, WeNet Community, NEXDATA

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.11898 | **PDF**：https://arxiv.org/pdf/2608.11898.pdf | **代码**：https://github.com/ASLP-lab/CN-MultiDialect-ASR | **Demo**：暂无

### 📌 简介
针对多方言ASR系统在提升方言识别能力时容易导致普通话识别能力下降（灾难性遗忘）的问题，提出三阶段适配框架：持续预训练（CPT）→监督微调（SFT）→On-Policy自蒸馏（OPSD）。基于Qwen3-ASR-1.7B，在100K小时CPT数据后，方言CER从15.37%降至12.79%，普通话CER从3.46%降至3.27%，内部方言从21.01%降至12.42%。OPSD阶段通过冻结教师+学生on-policy前缀+KL散度，仅用5K小时子集即可实现显著提升。

### 🔧 技术方案

**问题背景：** 多方言ASR面临方言识别与普通话保持之间的矛盾：增加方言数据提升方言识别能力时，通常会破坏模型对标准普通话的识别能力（灾难性遗忘）。现有微调方法难以在提升方言性能的同时保持普通话性能。

**模型架构：** 基于Qwen3-ASR-1.7B（1.7B参数语音-文本大模型）。三阶段适配：(1) CPT——在100K小时多方言数据上持续预训练，更新全部参数；(2) SFT——在有监督数据上进行指令微调；(3) OPSD——核心创新阶段，冻结教师模型（来自SFT阶段），学生模型以on-policy方式生成前缀token，通过KL散度约束学生输出分布接近教师，同时学生模型在真实方言数据上优化。

**核心创新：** (1) On-Policy自蒸馏（OPSD）——与传统off-policy知识蒸馏（使用教师固定的输出分布）不同，OPSD让学生模型在训练过程中动态生成前缀序列，教师基于学生生成的前缀提供软标签。这种on-policy方式使学生模型能够逐步适应自己的生成分布，避免了off-policy蒸馏中的分布漂移问题。这是OPSD区别于知识蒸馏（KD）和自蒸馏（Self-Distillation）的关键。(2) 三阶段渐进式适配——CPT→SFT→OPSD的递进设计使模型逐步从通用语音理解过渡到方言特定优化，每阶段解决不同层次的问题。(3) 冻结教师+学生on-policy前缀的设计——教师模型完全冻结防止灾难性遗忘，学生通过on-policy前缀动态调整，有效平衡了方言识别提升与普通话保持。

**训练策略：** CPT阶段：100K小时多方言数据。SFT阶段：有监督方言数据。OPSD阶段：5K小时子集，lr=1e-4，温度系数τ=0.8。训练配置：8×RTX A6000，DeepSpeed ZeRO-2。

### 📊 实验结果
**数据集**：普通话测试集、方言测试集、内部方言测试集

**主要指标**：
- 普通话CER: 3.46% → 3.27%（提升）
- 方言CER: 15.37% → 12.79%（相对降低16.8%）
- 内部方言CER: 21.01% → 12.42%（相对降低40.9%）

**是否开源**：代码已开源（GitHub）

### ⭐ 评分：8/10
评分理由：OPSD方法解决多方言ASR中灾难性遗忘问题的思路新颖且有效，内部方言40.9%的相对降低幅度显著。代码开源、实验设计严谨（含消融研究）。缺点：仅基于Qwen3-ASR-1.7B验证，未探索更大规模模型；OPSD与现有KD方法的对比分析可以更深入。

---

## [6] MiDashengLM-Gen: Unified Audio Scene Generation

**arXiv ID**：2608.11804 | **方向**：语音大模型 / 音频生成

**作者**：Xingwei Sun, Heinrich Dinkel, Gang Li, Jiahao Mei, Yadong Niu, Zerui Han, Yuepeng Jiang, Jiahao Zhou, Lichun Fan, Jian Luan

**机构**：Xiaomi

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.11804 | **PDF**：https://arxiv.org/pdf/2608.11804.pdf | **代码**：https://github.com/xiaomi-research/midashenglm-gen | **Demo**：https://xingws.github.io/midashenglm-gen-demo/

### 📌 简介
MiDashengLM-Gen提出基于LLM驱动的自回归流匹配统一框架，实现语音、音乐和音效三种音频场景的端到端统一生成。模型采用LLM+per-token条件流匹配架构，无需依赖外部声码器或编解码器。在Seed-TTS基准上WER达2.79%，在MECAT benchmark上达到竞争性结果。代码和Demo已全部开源。

### 🔧 技术方案

**问题背景：** 现有音频生成系统通常针对单一场景（语音、音乐或音效）独立设计，缺乏统一的生成框架。不同场景的音频在时域结构、频域分布和语义内容上差异巨大，统一建模面临挑战。

**模型架构：** 端到端LLM+per-token条件流匹配架构。核心设计为：LLM自回归预测每个token的流匹配条件，然后通过per-token流匹配模块并行生成所有token对应的连续音频表示。这种设计融合了自回归模型的全局建模能力和流匹配的并行生成效率。模型直接输出连续波形表示，无需外部声码器或编解码器进行后处理。

**核心创新：** (1) LLM+per-token流匹配的混合架构——自回归LLM负责全局语义建模和序列生成，per-token流匹配负责局部波形生成。这种"自回归+并行流匹配"的混合设计在保持全局一致性的同时实现了高效生成。(2) 统一三种音频场景的端到端框架——同一个模型同时支持语音、音乐和音效生成，无需为每种场景配置不同的解码器或后处理模块。(3) 无需外部声码器——模型直接输出波形，消除了编解码器级联带来的信息损失和延迟。

**训练策略：** 多阶段训练：先在大规模多类型音频数据上预训练，再在特定场景数据上微调。具体训练细节（数据量、训练轮数等）待论文全文确认。

### 📊 实验结果
**数据集**：Seed-TTS, MECAT benchmark

**主要指标**：
- Seed-TTS WER: 2.79%（专用TTS参考: 1.24%）
- MECAT benchmark: 竞争性结果

**是否开源**：代码和Demo已开源（GitHub）

### ⭐ 评分：8/10
评分理由：统一语音+音乐+音效生成的端到端框架设计领先，LLM+per-token流匹配的混合架构具有创新性。代码和Demo完全开源，透明度高。Seed-TTS上WER 2.79%与专用TTS（1.24%）有差距，说明统一模型在语音生成专项上仍有优化空间，但这是统一框架的合理取舍。

---

## [7] SLT SmartGlasses Challenge: Multi-Speaker ASR for Smart Glasses

**arXiv ID**：2608.12034 | **方向**：语音大模型 / ASR

**作者**：Dehui Gao, Zhixian Zhao, Zhennan Lin, Yujie Liao, Yuhang Dai, Yike Zhu, Longshuai Xiao, Hui Bu, Xin Xu, Xie Chen, Shuai Wang, Liumeng Xue, Zhonghua Fu, Jun Du, Eng-Siong Chng, Jun Zhou, Lei Xie

**机构**：Northwestern Polytechnical University

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.12034 | **PDF**：https://arxiv.org/pdf/2608.12034.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
SLT SmartGlasses Challenge提出面向智能眼镜场景的多说话人语音识别与理解基准，聚焦于真实世界中的复杂声学环境（多说话人重叠、远场、噪声）。该基准包含专门设计的评估协议和数据集，旨在推动智能眼镜设备上的语音交互技术发展。

### 🔧 技术方案
**问题背景：** 智能眼镜场景中的语音识别面临独特的挑战：多说话人同时说话、设备远场采集、环境噪声干扰、以及有限的算力资源。现有ASR基准主要针对近场单说话人场景，难以反映智能眼镜实际使用条件。

**模型架构：** 本文为挑战赛设置和基准论文，提出了评估框架和数据集构建方法，包括多说话人混合语音的录制协议、标注规范和评估指标。具体模型架构由参赛队伍自行设计。

**核心创新：** (1) 首个面向智能眼镜场景的多说话人ASR基准；(2) 真实的声学环境模拟（多说话人重叠、远场、噪声）；(3) 标准化的评估协议以促进公平比较。

**训练策略：** N/A（基准论文）

### 📊 实验结果
**数据集**：SLT SmartGlasses Challenge数据集

**主要指标**：待挑战赛结果

**是否开源**：未开源

### ⭐ 评分：7/10
评分理由：首个面向智能眼镜场景的ASR基准具有重要的实用价值，填补了现有基准的空白。多说话人重叠+远场+噪声的复合场景设计贴近真实使用。但作为基准论文，缺少具体的模型方案和实验结果，实际影响力取决于挑战赛参与度和后续结果。

---

## [8] Infant Audio Understanding via Whisper + LoRA

**arXiv ID**：2608.11587 | **方向**：语音大模型 / 音频理解

**作者**：Xulin Fan, Jialu Li, Mohammad Nur Hossain Khan, Kexin Hu, Bashima Islam, Mark Hasegawa-Johnson, Nancy L. McElwain

**机构**：University of Illinois Urbana-Champaign

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.11587 | **PDF**：https://arxiv.org/pdf/2608.11587.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出基于Whisper encoder + LoRA微调的方法，用于婴儿中心音频理解任务（如婴儿哭声检测、情感状态分类等）。创新性地设计了因子化说话人token机制，将共享层级token与家族特定偏移结合，实现跨家族的婴儿音频理解。采用多层级音频标记和序列级平滑损失函数来提升模型性能。

### 🔧 技术方案

**问题背景：** 婴儿音频理解面临数据稀缺和跨个体泛化两大挑战：婴儿音频数据收集困难且标注成本高，不同婴儿的发声特征差异巨大，导致模型在未见过的婴儿上性能显著下降。

**模型架构：** Whisper encoder作为骨干网络，通过LoRA（Low-Rank Adaptation）进行参数高效微调，仅更新约1-2%参数。轻量Transformer分类头用于多层级音频标记。因子化说话人token设计：共享层级token（所有婴儿共享）和家族特定偏移（每个家族独有的偏移量）相加得到最终说话人嵌入。

**核心创新：** (1) 因子化说话人token——将说话人表示分解为共享部分和家族特定部分，共享部分学习婴儿发声的通用特征，家族特定偏移捕捉个体差异。这种设计使模型在仅见过少数家族成员的情况下，也能更好地泛化到新家族。(2) 序列级平滑损失——在时间序列维度上施加平滑约束，使模型对输入噪声和时序偏移更鲁棒。(3) 参数高效微调——LoRA微调Whisper encoder，避免全量微调带来的过拟合和数据需求。

**训练策略：** 使用Whisper encoder预训练权重，LoRA秩（rank）为8。序列级平滑损失的权重通过网格搜索确定。数据集为婴儿音频记录（含多个家族的多模态数据）。INTERSPEECH 2026录用。

### 📊 实验结果
**数据集**：婴儿音频记录数据集（多家族）

**主要指标**：待论文全文确认具体数值

**是否开源**：未开源

### ⭐ 评分：7/10
评分理由：因子化说话人token的设计思路新颖，针对婴儿音频数据稀缺和跨个体泛化问题给出了有效解决方案。LoRA参数高效微调实用性强。缺点：任务场景较为垂直（婴儿音频理解），通用性有限；缺乏在公开标准基准上的评测结果。

---

## 语音前端

---

## [9] RT-SEMamba: Real-Time Speech Enhancement with Progressive Knowledge Distillation

**arXiv ID**：2608.12099 | **方向**：语音前端 / 语音增强

**作者**：Rong Chao, Sung-Feng Huang, Moreno La Quatra, Sabato Marco Siniscalchi, Wen-Huang Cheng, Szu-Wei Fu, Yu Tsao

**机构**：Academia Sinica

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.12099 | **PDF**：https://arxiv.org/pdf/2608.12099.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
RT-SEMamba提出基于因果Mamba的实时语音增强模型，并采用渐进式知识蒸馏策略将8层教师模型压缩为1层学生模型。因果时频Mamba块在保持Mamba状态空间模型高效序列建模能力的同时，引入因果约束实现实时流式处理。在Voicebank-DEMAND上，8层教师PESQ达3.32，蒸馏后的1层学生PESQ 3.18（优于朴素1层模型的3.06），推理速度提升2.75倍。

### 🔧 技术方案

**问题背景：** 状态空间模型（如Mamba）在语音增强中展现出潜力，但非因果Mamba无法用于实时场景。同时，Mamba模型的计算开销与层数成正比，如何在保持增强质量的同时大幅降低推理延迟，是实现实时部署的关键。

**模型架构：** (1) 因果时频Mamba块——在标准Mamba基础上引入因果约束，确保每个时间步的输出仅依赖于当前和过去的输入，满足实时流式处理要求。时频Mamba同时在时间和频率维度上进行状态空间建模。(2) 8层教师模型——全尺寸因果时频Mamba，提供高质量增强参考。(3) 1层学生模型——单层因果时频Mamba，通过渐进式知识蒸馏从教师模型学习。

**核心创新：** (1) 因果Mamba的实时语音增强——首次将因果Mamba应用于实时语音增强，解决了Mamba在流式场景中的因果约束问题，同时保留了状态空间模型在长序列建模上的优势。(2) 渐进式知识蒸馏——从8层到1层的渐进式压缩策略，通过中间层蒸馏+输出层蒸馏的多阶段方式，使1层模型学会模拟8层模型的复杂映射。蒸馏后的1层PESQ 3.18显著优于朴素1层3.06，证明了蒸馏策略的有效性。(3) 2.75倍推理加速——在保持接近教师模型质量的前提下实现近3倍加速，具有实际部署价值。

**训练策略：** Voicebank-DEMAND数据集。教师模型训练标准语音增强损失。蒸馏阶段：中间层特征蒸馏损失 + 输出层L1损失 + 判别器对抗损失。渐进式：先蒸馏到4层，再蒸馏到2层，最后蒸馏到1层。

### 📊 实验结果
**数据集**：Voicebank-DEMAND

**主要指标**：
- 8层教师 PESQ: 3.32
- 蒸馏1层学生 PESQ: 3.18
- 朴素1层基线 PESQ: 3.06
- 推理加速: 2.75x

**是否开源**：未开源

### ⭐ 评分：7/10
评分理由：因果Mamba在实时语音增强中的应用具有创新性，渐进式蒸馏策略设计合理且效果显著。PESQ 3.18（1层）接近教师3.32（8层），蒸馏效率高。缺点：仅在Voicebank-DEMAND单一数据集上验证，缺乏在真实噪声场景和多种SNR条件下的评估；缺少与其他实时SE方法的推理速度对比。

---

## [10] Rethinking LM-Based Generative Speech Enhancement

**arXiv ID**：2608.12082 | **方向**：语音前端 / 语音增强

**作者**：Yihui Fu, Zhengyang Li, Tim Fingscheidt

**机构**：Technische Universität Braunschweig

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.12082 | **PDF**：https://arxiv.org/pdf/2608.12082.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出统一比较框架，系统评估了6种基于语言模型（LM）的生成式语音增强范式，包括离散域（D/CAR, D/CNAR）和连续域（DDiff, CFM）方法。研究发现连续域方法整体优于离散域方法，其中CNAR（条件非自回归）在离散域中表现最佳。辅助损失微调显著提升DNSMOS、NISQA、PESQ和POLQA指标。在URGENT 2025数据上完成实验。

### 🔧 技术方案

**问题背景：** 基于语言模型的生成式语音增强方法近年来涌现出多种范式，但缺乏统一的比较框架。不同方法在离散域vs连续域、自回归vs非自回归、扩散vs流匹配等维度上的优劣缺乏系统性分析。

**模型架构：** 统一比较框架包含6种范式：(1) D/CAR——离散域/条件自回归，将增强语音建模为离散token序列的自回归预测；(2) D/CNAR——离散域/条件非自回归，离散token的并行预测；(3) DDiff——离散域扩散模型；(4) CFM——连续域流匹配。所有范式共享相同的骨干网络结构和训练数据，确保公平比较。

**核心创新：** (1) 统一的LM基SE范式比较框架——首次在相同骨干网络、相同数据条件下系统比较6种范式，为社区提供了清晰的范式选择指南。(2) 连续域>离散域的核心发现——连续域方法（CFM, DDiff）在几乎所有指标上优于离散域方法，表明离散化带来的信息损失对语音增强任务的影响大于对TTS任务的影响。(3) CNAR>CAR的发现——在离散域中，非自回归（CNAR）优于自回归（CAR），说明语音增强的token级条件足够强，无需自回归依赖。(4) 辅助损失微调策略——在预训练LM基础上添加辅助损失（如频谱L1、STFT一致性损失）进行微调，显著提升客观指标。

**训练策略：** URGENT 2025数据集。各范式共享相同的训练配置。辅助损失微调阶段：预训练LM权重固定，在输出层添加辅助损失权重。

### 📊 实验结果
**数据集**：URGENT 2025

**主要指标**：
- DNSMOS (CNAR vs CFM etc.)
- NISQA
- PESQ
- POLQA
- 辅助损失微调：所有指标显著提升

**是否开源**：未开源

### ⭐ 评分：7/10
评分理由：系统比较6种生成式语音增强范式的价值很高，连续域>离散域、CNAR>CAR的发现具有指导意义。辅助损失微调策略实用性强。缺点：主要依赖客观指标，缺乏主观听感测试（如CMOS）验证；仅在URGENT 2025单数据集上验证，泛化性需更多数据支持。

---

## [11] Cloud-Boosted Speech Enhancement for Edge Devices

**arXiv ID**：2608.07423 | **方向**：语音前端 / 语音增强

**作者**：Xulin Fan, Juan Azcarreta, Ashutosh Pandey, Jesus Alvarez, Ke Tan, Jacob Donley, Ritwik Giri, Buye Xu

**机构**：Reality Labs, Meta

**发布日期**：2026-08-12 | **论文**：https://arxiv.org/abs/2608.07423 | **PDF**：https://arxiv.org/pdf/2608.07423.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
Cloud-Boosted SE提出边缘设备与云端服务器协作的语音增强框架，通过三种技术路径提升边缘SE质量：延迟服务器输出作为额外输入、层级特征增强、协作MWF波束成形。该框架在保持边缘设备低延迟的同时，利用云端更大模型的计算能力提升增强效果。

### 🔧 技术方案

**问题背景：** 边缘设备的算力和内存限制使得大型语音增强模型无法直接部署，而纯云端方案存在网络延迟和隐私问题。如何在边缘设备上实现接近云端质量的语音增强，同时保持低延迟和隐私保护，是实际部署中的核心挑战。

**模型架构：** 边缘-云端协作框架包含三种技术：(1) 延迟服务器输出作为额外输入——边缘设备先进行快速SE，同时将音频发送到云端进行高精度SE，云端结果（延迟）作为额外输入特征反馈给边缘模型进行修正。(2) 层级特征增强——云端的中间层特征作为边缘模型的层级特征增强输入，实现知识迁移。(3) 协作MWF（多通道维纳滤波）波束成形——边缘设备进行初始波束成形，云端利用更多麦克风通道信息进行优化。

**核心创新：** (1) 边缘-云端双向协作设计——不同于传统的"全部上云"或"全部本地"方案，该方法让边缘和云端各司其职：边缘负责低延迟初始处理，云端负责高质量优化，结果再反馈到边缘。这种闭环设计在延迟和质量之间取得最优平衡。(2) 三种互补技术路径——延迟服务器输出、层级特征增强、协作MWF从不同角度解决边缘-云端协作中的信息融合问题，形成完整的解决方案。(3) 实际部署导向——针对AR/VR眼镜等穿戴设备的实际约束设计，考虑网络延迟、带宽、功耗等工程因素。

**训练策略：** 边缘和云端模型联合训练，边缘模型以云端输出为辅助目标。INTERSPEECH 2026录用。

### 📊 实验结果
**数据集**：Meta内部测试集

**主要指标**：待论文全文确认具体数值

**是否开源**：未开源

### ⭐ 评分：7/10
评分理由：边缘-云端协作SE的框架设计具有实际部署价值，三种技术路径互补性强。针对AR/VR眼镜等产品的工程导向明确。缺点：缺乏在公开基准上的评测结果，三种技术路径的独立贡献和组合效果需消融实验详细说明，使其对其他团队的借鉴价值受限。

---

*Generated on 2026-08-14*