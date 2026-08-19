# 2026-08-18 语音论文速递

**共收录**: 16 篇 | **语音大模型**: 12 篇 | **语音前端**: 4 篇

> 今日 arXiv 语音相关论文共命中 16 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

---

## [1] Listen, Reason, and Segment: Aligning LALMs with Editorial Judgment for Media Chapterization

**arXiv ID**：2608.16539 | **方向**：语音大模型 / 音频语言模型对齐

**作者**：Tony Alex, Wish Suharitdamrong, Sara Atito, Armin Mustafa, Muhammad Awais, Philip J. B. Jackson, Jiankang Deng, Ismail Elezi

**机构**：University of Surrey, Huawei Noah's Ark Lab（受 EPSRC 与 BBC 联合项目 AI4ME 资助）

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16539 | **PDF**：https://arxiv.org/pdf/2608.16539.pdf | **代码**：https://github.com/ta012/AudioChaps（录用后开源） | **Demo**：暂无

### 📌 简介
音频章节化（把连续音频流切分为主题连贯章节）依赖主观编辑判断而非客观声学事件，现有 ASR+LLM 流水线仅适用于纯语音场景，且无纯音频端到端方案与评测基准。本文提出 AudioChaps 后训练框架，以 Audio-Flamingo-3-Think-8B 为骨干，通过 CoT-SFT 冷启动加 GRPO 校准将模型边界决策对齐 YouTube 创作者标注。在 AudioChaps-Eval 上平均 F1 从骨干 28.6 提升至 77.8（bootstrap 增益 49.2 点），纯 GRPO（AudioChaps-R1-Zero）即提升约 33 点，最终模型还以约 1/4 参数量超越 32B Step-Audio-R1-32B。

### 🔧 技术方案

**问题背景：** LALM 在标准 benchmark 上进步很快，却难以落地媒体工作流。章节边界本质是创作者主观编辑判断，而非可客观检测的声学事件；现有研究仅限视频域（VidChapters-7M）或转写级联（Whisper-Large-V3+Qwen3-235B 测试仅 48.0 F1），在音乐、游戏、动态媒体上显著退化，且缺乏有监督的推理数据。

**模型架构：** 骨干为 AF3-Think-8B（另验证 MOSS-Think-8B 的通用性）。任务定义为 60 秒片段二元边界检测，正样本边界落在 20-40 秒中央窗口以提供前后各 20 秒上下文；因 AF3-Think-8B 无法稳定输出时间戳，故采用"是否有边界"的 flow 式判断，部署时用 60 秒窗+20 秒 hop 滑窗适配任意时长音频。

**核心创新：** (1) 音频到文本模态桥 CoT 数据管线：Step-Audio-R1-32B 先生成伪 CoT，再净化成不含提示词与标注的声学感知日志，最后由 Gemini 2.5 Pro 仅凭日志合成有据可依的 flow 式推理目标（AudioChaps-CoT 共 22k 条），避免标签泄漏。(2) 两阶段对齐：CoT-SFT 冷启动建立高召回、格式统一的推理先验，随后 GRPO 用规则奖励 r=r_format+r_accuracy（二值）强化与创作者标注一致的决策；G=8 条轨迹组内归一化优势，保留多样推理路径，无需奖励模型。(3) 构建三层数据集资源：AudioChaps-Alignment（约 30k 片段，13,347 正/16,636 负，按言语/游戏/音乐/动态媒体四类声学分层）、首个纯音频章节化基准 AudioChaps-Eval（约 16k 片段，749 源视频，按视频级划分）。

**训练策略：** SFT：2 轮、lr 1e-6、批 1+累积 4、bf16、ZeRO-2、8×H200-140GB 约 4 小时；GRPO：1 轮、lr 1e-6、max completion 768、G=8、KL 系数 β=0.04、8 节点×4×GH200 约 10 小时，奖励=格式+准确率二值相加，组内标准化为优势。

### 📊 实验结果
**数据集**：AudioChaps-Eval（约 16k 片段）；全长评测 40 条录音、387 个真值边界、均值 49 分钟（共约 33 小时）

**主要指标**：
- 片段级平均 F1：AudioChaps-R1 77.8 vs AF3-Think-8B 零样本 28.6 vs Step-Audio-R1-32B 59.3
- 分类别 F1：DM 73.4/G 75.5/M 84.6/SS 77.8，类别跨度由骨干的 43.9 收窄至 11.2
- 消融：直接 GRPO 平均 F1 约 61.1，SFT 冷启动 70.0→77.9（高召回先验），GRPO 进一步提精度（Music 上 Pre +20.7、F1 +10.5）
- 全长边界检测 F1：AudioChaps-R1 37.6（骨干 6.5、180s 固定间隔 9.5），中位偏差 38.0→10.0 秒
- 骨干泛化：MOSS-Think-8B 73.6→81.4；对比 Gemini 2.5 Flash 76.75、Qwen3-Omni-30B 75.29

**是否开源**：论文录用后发布代码、模型与数据集（GitHub: ta012/AudioChaps）

### ⭐ 评分：9/10
评分理由：将 R1-Zero 式 GRPO 引入音频后训练并配以模态桥 CoT 数据管线，方法论完整且可复现，属语音大模型对齐的少有工作。实验充分：四类声学域、全长评测、ASR 级联基线、多骨干泛化、bootstrap 显著性检验与超参数齐全。三个数据集+首个纯音频章节化基准实用价值高，若真正开源将直接推动媒体工作流落地；扣分点在于代码尚未发布且不支持生成长格式章节标题。

---

## [2] CineDub: Scaling End-to-End Video Dubbing to Multi-Speaker Dialogues with Coherent Sound Effects

**arXiv ID**：2608.15734 | **方向**：语音大模型 / 多说话人视频配音

**作者**：Yusheng Dai, Kangdi Wang, Baolong Gao, Yuxuan Jiang, Weiqiang Wang, Qiuhong Ke, Jianfei Cai

**机构**：蒙纳士大学 | 中国科学院大学 | 清华大学

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.15734 | **PDF**：https://arxiv.org/pdf/2608.15734.pdf | **代码**：暂无 | **Demo**：https://cinedub2026.github.io

### 📌 简介
CineDub 是一个统一扩散式视频配音框架，直接在未裁剪视频上实现多说话人多轮对话配音，无需人脸裁剪或说话人分离。通过隐式耦合整体条件（ICHC）范式结合语义捆绑转录，将 CineDub-Multi 上 cpWER 降到 13.93%，相对最强基线降低 68.0%；同时扩展出语音+音效联合生成，在 CineDub-SA 上 WER 达 18.65%、Desync 0.19。单说话人 GRID/CHEM 上也达 SOTA（GRID WER 13.27）。

### 🔧 技术方案

**问题背景：** 层级式方法（HPMDubbing、AlignDiT、FunCineForge）依赖人脸/嘴唇裁剪、主动说话人检测、说话人分离等多阶段预处理，管线脆弱且训练数据难以规模化；整体式/流式方法（DeepAudio、DeepDubber）直接处理全帧视频，但缺乏细粒度唇形时序对齐，且多说话人场景下存在说话人-话语漂移。现有 V2SA 级联方案还面临幻影语音与声道声学不一致问题。

**模型架构：** 基于潜空间扩散（16kHz 连续 VAE 去量化）+ DiT 去噪主干，语音克隆采用参考语音前缀拼接的 infilling 形式。三路条件：整体视觉条件 c_v 由冻结 SynchFormer 分段级特征提取（自监督音视频同步，训练于 AudioSet）；语义捆绑转录条件 c_t 由 Gemma-T5 编码；可选音频条件 c_a 用 8fps CLIP 或 Flan-T5 文本提示。

**核心创新：** (1) ICHC 范式：视觉与文本条件独立编码、经跨模态训练隐式耦合。SynchFormer 具有涌现式注意力切换（按语轮自动转向活动说话人），语义捆绑转录 P=⊕[d_k‖u_k] 由 Gemini 2.5 Pro 自动生成，消除 ASR/强制对齐/分离模块。(2) 环境-语言课程学习（ALC）：Stage 1 仅训 V2A 建立普适音频先验，Stage 2 再统一采样音频/语音/联合三任务，缓解共享视觉条件下语音与音频的梯度竞争与灾难性遗忘。(3) 解耦文本分支控制：DiT 内用两路独立交叉注意力分别处理 c_t 与 c_a，单任务推理时以可学习 meta-token 替代缺失分支，消除注意力稀释与跨提示泄漏。

**训练策略：** 噪声预测扩散损失 L_diff。Stage 1 用 Omni2Sound 协议构建 47 万 V-A-文本三元组预训练；Stage 2 采 SpeakerVid-5M 中 700h 单说话人与 400h 多说话人数据及 VGGSound/AudioSet 100h+ V2SA 片段微调，转录均由 Gemini 2.5 Pro 生成并人工校验。

### 📊 实验结果
**数据集**：GRID、CHEM（单说话人）；CineDub-Multi（139 条多说话人英语对话）；VGGSound test（V2A）；CineDub-SA（562 条 10 秒 V2SA 片段）

**主要指标**：
- GRID：WER 13.27（优于 DeepAudio 19.18），SIM 0.94，MCD-DTW 4.35；零样本 CineDub* WER 10.36
- CHEM：WER 2.21，MCD-DTW 5.03，LSE-C 7.83
- CineDub-Multi：cpWER 13.93%（基线 AlignDiT 57.49 / DeepAudio 55.53 / FunCineForge 43.47），WER 13.06，Desync 0.255
- VGGSound V2A：KL 1.41，FDVGG 0.53，FDPaSST 49.91，IS 14.59
- CineDub-SA：WER 18.65，LSE-D 9.10，Desync 0.19（优于级联 AlignDiT+MMAudio 53.33）
- 课程消融：Native Joint WER 13.48 vs A→L 10.36

**是否开源**：未公开代码与模型，仅发布项目主页及两个基准（CineDub-Multi/CineDub-SA）

### ⭐ 评分：9/10
评分理由：提出 ICHC 隐式耦合范式与语义捆绑转录，直击多说话人场景无裁剪端到端配音痛点，创新度高。实验覆盖单/多说话人、V2A、V2SA 四类任务，含课程学习与分支控制消融，充分严谨。发布双基准对领域评估有实用价值。扣分点：模型与代码未开源，复现成本高，且 SynchFormer 注意力切换在重叠语音与镜头切换场景仍有失败案例。

---

## [3] INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval

**arXiv ID**：2608.16203 | **方向**：语音大模型 / 语音检索基准

**作者**：Chen-An Li, Hung-yi Lee

**机构**：National Taiwan University（台大）、NTU AI-CoRE

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16203 | **PDF**：https://arxiv.org/pdf/2608.16203.pdf | **代码**：https://github.com/lca0503/INSPIRE | **Demo**：暂无

### 📌 简介
语音检索现有系统依赖固定相似度匹配，无法适应多样用户意图。台大李宏毅组提出首个指令感知语音检索基准 INSPIRE，让自然语言指令动态指定语义内容、说话人身份、说话风格、环境声及多属性组合的匹配准则，并统一评测四种检索范式。结果发现无现有方法能稳健覆盖全部意图：级联流程在语义检索上最优（DailyTalk R@10=62.0），自监督语音模型更擅超音段属性（VCTK R@10=17.5），多属性综合子集仍近乎无解（R@10 最高 7.0），凸显统一指令感知架构的必要性。

### 🔧 技术方案

**问题背景：** 传统语音检索以固定声学/语义相似度或级联 ASR 检索定义相关性，一条查询只能对应一个目标；而真实场景中同一段语音在不同指令下应检索不同文档，现有方法无法按指令动态调节内容、说话人、风格、环境声等异构线索的权重，指令感知检索在文本/图像领域已有积累但在语音域尚属空白。

**模型架构：** 基准由四子集构成：DailyTalk 测语义延续、VCTK 测同说话人、Expresso 测说话人/风格、Synthetic 基于 Natural Questions 合成并叠加说话人、风格与环境声多属性约束。评价协议采用指令条件评分函数按分数排序，以 Recall@K 与重排阶段 NDCG@K 为指标。

**核心创新：** (1) 首次形式化并建立指令感知语音检索基准，680 个语音查询扩展为 4080 个查询-指令对，覆盖 17,225 文档，同一查询配不同指令对应不同正样本，指令由 GPT-5.2 每类生成 20 条并随机采样保证语言多样性。(2) 定义四种覆盖语义/说话人/风格/环境声的评测维度，并统一评估 LALM 嵌入、级联流程、自监督语音模型、对比音频语言模型四大范式及 LALM/文本重排序。(3) 系统实验揭示模态专业化分工与技术缺口，给出指令类型、指令敏感性、层级表示、Oracle 元数据、专用模型等八组分析。

**训练策略：** 数据来源为 DailyTalk、VCTK、Expresso 及 GPT-4o-mini TTS 合成数据（5 音色×3 风格×ESC-50 15 种环境声）；Synthetic 质量校验：Whisper 转写 WER 0.0314/0.0337，ECAPA-TDNN 说话人一致率 0.9998，emotion2vec 风格分类 0.8657/0.8780，UTMOS 3.76。LALM 基线用"Summarize the above sentence and speech in one word"提示取末 token 隐状态嵌入，级联用 Whisper-large-v3 转写再经 BM25/SentenceBERT/E5-Mistral/Qwen3-Embedding 检索。

### 📊 实验结果
**数据集**：INSPIRE（DailyTalk/VCTK/Expresso/Synthetic 四子集）

**主要指标**：
- DailyTalk（语义延续）R@10：Qwen3-Embedding 最高 62.00，优于 E5-Mistral 55.50、Qwen3-Omni 51.50、CLAP 0.00
- VCTK（说话人）R@10：WavLM-Large 17.50、HuBERT-Large 11.88，明显优于级联与 LALM（≤1.88）
- Synthetic（多属性）R@10：Qwen3-Embedding 7.02 最高，全部方法严重退化，接近随机水平
- 重排序：LALM 重排在 DailyTalk 上将该范式 R@10 最高提升至 46.32 NDCG，文本重排在其余子集增益有限
- 关键发现：指令增益仅出现在指令感知文本检索器；说话人信息编码在中低层、语义在中高层；Oracle 元数据对语义检索有害、对说话人匹配大幅增益（VCTK R@50 5.63→95.00）

**是否开源**：代码与数据公开（GitHub: lca0503/INSPIRE）

### ⭐ 评分：9/10
评分理由：填补语音域指令感知检索空白，任务形式化与数据构建（含合成数据质量校验、困难负样本设计）完整严谨。统一协议下横跨四大范式、多种重排器，对比既广且深，为社区提供可复现基线。实验说服力强，若补充联合微调的统一模型初步结果或盲测会更具前瞻指导意义。

---

## [4] The Null Token Knows: Reducing Message-Free Hallucination in ASR and NMT

**arXiv ID**：2608.15940 | **方向**：语音大模型 / ASR幻觉抑制

**作者**：Kirill Borodin, Vasiliy Kudryavtsev, Ivan Viakhirev, Grach Mkrtchian

**机构**：未标注

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.15940 | **PDF**：https://arxiv.org/pdf/2608.15940.pdf | **代码**：暂无（计划发表后随构件清单开源） | **Demo**：暂无

### 📌 简介
针对编码器-解码器系统在静音/房间底噪等无消息输入下流畅编造文本的幻觉问题，提出通过模型保留的 null token（ASR 的 EOT、翻译的 EOS、CTC/RNN-T 的 blank）分数实现弃权信号审计。系统比较标量 null-token bias、解析型 row graft 与训练型 EOT row 三类干预，发现提升 null token 分数可显著压制幻觉（Whisper-small LOR 91.7%→3.3%），但激进干预会删除有效语音（删除字数 1.58→33.05 词/分），低信噪比下误静默达 42.7%。主张以抑制与删除双成本评估弃权方法。

### 🔧 技术方案

**问题背景：** AED 模型即使输入无任何可恢复消息也会输出流畅文本，且该失败不随规模消失（六个 Whisper 检查点上 LOR 非单调）。现有手段包括原生 no-speech 分数、VAD/端检、重训注意力头、SAE 特征操控等，但均未系统检验保留输出坐标（EOT/EOS/blank）是否本身携带可用弃权信号；WER 无法区分幻觉与误识别词，也缺对删除成本的量化。

**模型架构：** 覆盖 15 个模型的 zoo：六个 Whisper 尺度、Canary-1B、OWSM v3.1、五个 CTC、两个 RNN-T、NLLB-200 与 MarianMT，另加 Distil-Whisper、SeamlessM4T-v2-large、Parakeet-TDT-1.1B 只做只读校验。度量指标为规范化的词法输出率 LOR，防御集含 630 非语音+430 语音片段（3.1h），并设 300/300 源不相交锁定评测。

**核心创新：** (1) null-token 多层级审计：用 logit lens 与 5 折逻辑探针揭示首解码块之后状态即线性可分（探针 AUROC 1.00），原生 EOT/nospeech 分数可区分条件但最终 margin 仍低于弃权边界，证明是 EOT 工作点而非缺少信号的问题。(2) 三类坐标干预：标量 bias 等价于常数先验对数几率平移，解析型 row graft 用有监督线性方向注入 EOT unembedding 行，训练型 EOT row 仅 768 参数即达零 LOR；并以条件先验漂移模型检验其工作点预测。(3) 冻结敏感性评测协议：预定义条件速率器 Cκ=F+κD（κ=0.5/1/2/5/10），在锁定 300/300 集上同时报告捏造与删除成本，防止只看幻觉抑制。

**训练策略：** EOT row 在 50/50 均衡锚定混合集（MUSAN 噪声/合成静音+空目标、LibriSpeech dev-clean+转写）上训练，AdamW/Adafactor，400 步、LR 1e-3、梯度裁剪 1.0，每 50 步评估；7 个非语音占比 p∈[0.1,0.9] 训练 126 个行，随机效应斜率 1.29（95%CI[0.94,1.65]）。

### 📊 实验结果
**数据集**：MUSAN、ESC-50、UrbanSound8K、FLEURS、LibriSpeech test-clean、WHAM

**主要指标**：
- 锁定集 LOR：91.7%→3.3%（训练 row）；删除 1.58→33.05 词/分；误静默 8.0%（干净）/42.7%（低SNR）/38.7%（带口音）
- Cκ 网格：bias b=5 在 κ=0.5,1 最优，stock 在 κ≥2 最优，训练 row 从不最优
- Canary LOR 79.3→0.0%（WER 7.02→6.94）；OWSM 90.7→1.3%（WER 8.19→20.9）
- NLLB 27.5→1.0%（COMET 83.4→80.9）；Marian 7.0→0.0%（COMET 79.9→75.6）
- 参数对比：eot_row 768 参数 WER 5.11；LoRA 884,736 参数 5.5；AudioSAE α=1 幻觉率 94.6%、α=8 WER 100%
- 多语种：large/turbo 中位空输出 0.0%、CER +1.7/+0.1，韩语残余最差

**是否开源**：否，作者声明已备好代码与构件清单，计划发表后按上游许可开源，当前无公开链接。

### ⭐ 评分：9/10
评分理由：把 null token 从终止符重新定位为可审计、可干预的弃权诊断坐标，并以可证伪的先验漂移模型限制解释范围，方法论严谨。锁定冻结评测、源不相交分割、参数效率对比与多族模型边界测试设计规范，且诚实报告 AudioSAE、LLT 等基线失败。实用价值中等偏上：行编辑参数紧凑、部署可行，但低 SNR/口音下误静默风险限制了直接部署；不含人类裁决、无匿名开源定位是主要局限。

---

## [5] Speaker-Normalized Semantic Speech Tokens via Iterative S2U-T2U Refinement

**arXiv ID**：2608.16235 | **方向**：语音大模型 / 语义语音token

**作者**：Hanlin Zhang, Daxin Tan, Dehua Tao, Chengxi Deng, Xiao Chen, Linqi Song

**机构**：香港城市大学计算机系、华为 AI Lab、香港中文大学

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16235 | **PDF**：https://arxiv.org/pdf/2608.16235.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语义语音 token 应保留语言内容、抑制说话人与时长信息，但现有 S2U tokenizer 常继承这些声学因素。本文提出 ISTP（迭代语义 token 提纯）：通过迭代 S2U-T2U 交替训练，以 T2U 预测与文本一致性作为提纯信号，逐步将对齐导向文本可预测的 token 空间。中英文实验表明 S2U-T2U 一致性强鲁棒提升（WER 降 72.0%-86.7%，BLEU 增 58.88-73.39 点），VC/TTS 保持高可懂度且说话人相似度提升，跨说话人一致性大幅改善（UED 344.61→59.44，SelfBLEU-4 27.04→94.17）。

### 🔧 技术方案

**问题背景：** 现有 S2U tokenizer（如 HuBERT 量化）保留说话人、韵律和时长信息，同内容不同说话人产出不同 token 身份或序列长度，给 T2U 建模和隐私带来困难。已有方法依赖声学扰动（R-Spin）、并行话语（PINT）或对齐约束，且 BT4ST/DUB 等 T2U 反向翻译仅生成伪数据、不改动 tokenizer 本身。

**模型架构：** 初始 S2U（S0）采用 DSA-Tokenizer 语义分支：HuBERT 编码器提取表征后时间降采样，用 FSQ（6 维×4 级=4096 个单元，25Hz）量化，并用辅助音素 CTC 解码器训练后丢弃。T2U 为 BART 编解码器，输入 G2P 音素序列。合成解码器采用 Speech-Omni-Lite 的 CA-F5-TTS 结构：单元序列上采样作语义条件、掩码参考 mel 提供声学上下文，条件流匹配目标重建 mel。

**核心创新：** (1) 文本可预测性引导目标：将去重后的 S2U 序列作为 T2U 训练目标，T2U 从文本解码的伪目标无法接触源说话人/时序，从而过滤声学可变因素。(2) 迭代式 S2U-T2U 交替提纯：每轮用 CTC 目标重头初始化 S2U（非微调），形成 S0→T0→S1→T1→…循环，双方收敛于共享文本可预测 token 空间。(3) 去重：连续重复 token 合并消除显式时长信息，与 T2U 监督互补，同时抑制文本不可预测的 token 变化。

**训练策略：** 约 8000 小时中英文配对语音（英文：LibriSpeech、GigaSpeech、Libri-Heavy、Common Voice、The People's Speech；中文：AISHELL-2、WenetSpeech、MagicData-RAMC）。每轮 T2U 在去重 S2U 序列上训练；新 S2U 仅训练于 T2U 伪目标。迭代 0 和 4 的合成解码器分别用约 10 万小时 Emilia 中英文数据同架构训练。

### 📊 实验结果
**数据集**：Seed-TTS（TTS/VC）、VCTK（一致性）、自建中英文测试集

**主要指标**：
- S2U-T2U 对齐：T0→T4 WER 相对降 72.0%-86.7%，BLEU 增 58.88-73.39
- TTS 英文 WER：Iter0 1.80 / Iter4 1.97，SIM 0.63→0.71；对比 CosyVoice3 2.02/0.72、MaskGCT 2.62/0.71
- VC：Iter4 双语言 SIM 最优（英 0.71、中 0.77）
- VCTK 并行话语一致性：UED 344.61→59.44（降 82.7%），SelfBLEU-4 27.04→94.17；优于 R-Spin、StableToken
- 说话人探测：BiLSTM 分类准确率 0.10%→0.09%，低于 R-Spin（0.15%）、CosyVoice3（0.30%）

**是否开源**：未提供代码开源链接，暂无

### ⭐ 评分：8.5/10
评分理由：以"文本可预测性"作为提纯信号、迭代重初始化 S2U 而非简单伪数据增强，概念简洁且有理论自洽性。实验充分：覆盖跨模型对齐、生成质量、跨说话人一致性、隐私探测和语速控制五个维度，对比基线全面（含 R-Spin、StableToken 等强基线），中英双语验证。局限：未开源代码，且 token 空间是否过度退化为音素级序列有待探讨。

---

## [6] Iterative Self-Learning for Expressive Text-to-Speech Synthesis

**arXiv ID**：2608.15910 | **方向**：语音大模型 / 表达性TTS

**作者**：Nicholas Sanders, Gustav Eje Henter, Simon King, Korin Richmond

**机构**：KTH皇家理工学院 | 爱丁堡大学

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.15910 | **PDF**：https://arxiv.org/pdf/2608.15910.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
表达性 TTS 采用显式标签控制（如重音、情感）直观可解释，但大规模标注代价高昂。本文提出迭代自学习（ISL）框架：用种子数据训练 Matcha-TTS，冻结后用 Invert-Classify 梯度反演恢复无标注语音的离散情感/重音伪标签，再对合成数据+伪标签数据重训并循环。在词级重音（Naver-Prosody）与语句级情感（ESD）两任务、多档低资源切分下验证，1% 情感切分伪标签 F1 由 0.33 提升至 0.40（相对 +20%），5% 切分超 100% 全监督，主观 A/B 听辨中 ISL 显著胜出单次伪标签基线。

### 🔧 技术方案

**问题背景：** 显式条件标签控制提供可解释、可定向的表达控制，但情感/重音标注依赖人工听觉判断，大规模获取昂贵且主观性强。现有多数半监督 TTS 解决的是语音-文本配对或转写稀缺，而非表达性标签稀缺；自动分类器方案需针对每个任务/数据集单独设计且跨域适应差。ASR 中的迭代自学习（IPL）被证明行之有效，但尚无工作将其与表达性标签恢复机制结合用于生成式 TTS。

**模型架构：** 采用 Matcha-TTS（OT-CFM 流匹配配速模型）为骨干，从头训练、内部含 MAS 对齐。词级重音将二元标签嵌入词边界音素序列；语句级情感将情感嵌入向量拼接至文本编码器输出。总损失 L=OT-CFM+λdur·Ldur+λenc·Lenc，该损失同时用于反转优化。声码器为固定 HiFi-GAN V1。

**核心创新：** (1) 将 Invert-Classify 嵌入迭代自学习循环：冻结当前生成式 TTS，把缺失标签嵌入初始化为全部标签嵌入均值，对训练损失做梯度反演，再按余弦相似度量化到最近标签，实现"免分类器"伪标注；针对流匹配随机采样导致反演不收敛，固定时间步 t=0.9 与固定噪声张量保证梯度反映标签信号。(2) Select-and-Retrain 策略：在验证集监测各迭代伪标签准确率并选取最优迭代，用对应固定伪标签数据从零重训 1000 轮，解耦标签质量改善与迭代模型状态累积，抑制错误标签传播。(3) 首次系统研究生成式 ISL 的动态边界：3/10/50 轮训练对比显示 50 轮致模型崩塌（1% 重音 F1 由≈0.45 跌至≈0.24），10 轮最稳定；0.5% 数据不足无法启动自举、20% 则收益消失——ISL 仅适用于有界低资源区间。

**训练策略：** 种子模型 100 轮（Iteration 0），每轮迭代训练 3/10/50 轮对比。Adam lr=4e-4、无权重衰减、梯度裁剪 5.0、batch=32；推理 Euler 采样 40 步、温度 1.0。反演：情感嵌入 200 步/lr=0.01，重音嵌入 100 步/lr=1e-4。数据切分：ESD 与 Naver-Prosody 均按 0.5%、1%、5%、20% 分层采样。

### 📊 实验结果
**数据集**：ESD 情感（5 类 10 人 14.5h）| Naver-Prosody 重音（26.7h/36600 句）

**主要指标**：
- 伪标签 F1（情感 1%）：0.33 → 0.40
- Emo2vec F1：1% ISL 29.87 vs 控制 26.58 | 5% ISL 49.58 vs 控制 39.38 vs 100%GT 45.95
- TTSDS 总平均：情感 1% 89.90 vs 88.70 | 重音 0.5% 93.15 vs 91.37
- A/B 听辨（Bradley-Terry，30 人）：重音 1% ISL vs 控制 0.678；情感 5% 0.633 vs 0.037

**是否开源**：论文未提供代码/Demo 链接，暂未开源。

### ⭐ 评分：8.5/10
评分理由：首次将迭代伪标签循环引入表达性 TTS 标签稀缺场景，并清晰刻画了训练时长—标签质量—合成可控性的三角关系，Select-and-Retrain 设计精巧。实验充分：双数据集、四档切分、三档训练时长、客观+主观双层验证，且坦诚讨论 emo2vec 域偏差。局限在于仅验证 Matcha-TTS 轻量骨干，未与分类器式伪标注做对齐预算的公平对比。

---

## [7] Adding Voice Cloning to Text-to-Audio-Video Models with a Single Zero-Initialised Layer

**arXiv ID**：2608.15690 | **方向**：语音大模型 / 声音克隆

**作者**：Ivan Mikheev, Viacheslav Vasilev, Anna Dmitrienko, Alexey Letunovskiy, Ivan Kirillov, Kirill Chernyshev, Denis Dimitrov

**机构**：Kandinsky Lab, Moscow, Russia

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.15690 | **PDF**：https://arxiv.org/pdf/2608.15690.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文针对文生音视频（T2AV）模型无法控制输出说话人身份的问题，提出在音频骨干上仅加一个零初始化的线性层，把预训练 T2AV 模型改造成参考语音克隆模型：参考音频扩散潜变量前置进音频流，冻结 Qwen3-TTS 编码器的全局说话人嵌入经该层以 FiLM 调制目标音频。在基于 VCTK 的 674 对说话人-文本、30 说话人基准上，微调后的 k6a_5b（5B）在三套说话人验证网上的 SECS（ECAPA-TDNN 0.766、WavLM-SV 0.944、Resemblyzer 0.866）均超过五个 TTS 基线，且无回归验证全指标改善。

### 🔧 技术方案

**问题背景：** 现有 T2AV 扩散模型（基于 Kandinsky 5.0、LTX-2、3MDiT 等）能按文本合成视频与配乐，却无法控制语音身份。TTS 语音克隆系统（XTTS、Qwen3-TTS 等）虽能克隆音色，但仅生成纯语音、依赖专用说话人分支架构，无法产出对应视频；给 T2AV 模型加此能力需昂贵的从头训练，或进行可能破坏视听先验的架构手术。

**模型架构：** 基座为非对称视听扩散 Transformer（AV-DiT）：32 个融合解码块，视频流宽度 1792、音频流宽度 896，块内通过交叉注意力融合；音频潜变量来自 44.1kHz 神经音频 VAE，视频潜变量来自 HunyuanVideo VAE，文本条件两流共享。实验用两个检查点：k5（5B）与 k5-lite（约 3B，其中音频分支约 0.6B）。唯一新增可学习层为 W_film：R^1024→R^(2×896)，将冻结的 Qwen3-TTS 说话人嵌入映射为 FiLM 的 scale/shift 系数。

**核心创新：** (1) 零初始化的单个线性层：W_film 权重与偏置初始化为零，微调首个前向时扩展模型输出与基座完全一致，是基座的严格功能超集，天然保留视听先验。(2) 参考潜变量前置注入：参考音频（1.2–4s）用同一音频 VAE 编码后拼接到目标音频序列前，目标 token 经 32 个块内已有 self-attention 完成条件化，无需新增注意力层；推理时参考部分固定、仅对目标部分扩散更新，强制跨去噪步音色一致。(3) 三路分离的 classifier-free guidance：训练以 0.1 概率独立丢弃文本与参考条件，推理用独立权重 w_t 与 w_r 分别调节文本忠实度与说话人拟合度（默认 w_t=5, w_r=4）。

**训练策略：** 基座检查点上单阶段微调（voice-aware），AdamW（β=(0.9,0.95)、weight decay 1e-3、grad norm 1.0），基座学习率 1e-5，新层与偏置乘 5 倍，8000 步 warmup；目标与参考之间留 0.5s 缓冲防浅拷贝，从 12s 搜索窗口采样 1.2–2.5s 语音参考；推理默认 50 个扩散步。

### 📊 实验结果
**数据集**：VCTK 语料（48kHz 原声），674 个样本、30 位母语英语说话人，文本 100% 唯一，每人含 1 条参考+3 条 enrollment+1 条保留目标文本

**主要指标**：
- k6a_5b SECS vs reference：ECAPA-TDNN 0.766 / WavLM-SV 0.944 / Resemblyzer 0.866，全部第一，三网平均领先最强基线 Qwen3-TTS 0.6B 达 0.041（Wilcoxon p<10^-89）
- 可懂度（k6a_5b）：WER 5.76%、CER 5.21%，弱于专用 TTS（WER<1.2%）
- 无回归检查（400 prompts）：FAD 相对变化 -30.6%，WER -46.0%，WER0 +113%，CLAP +29.4%，UTMOS +0.6%
- 纯音频推理：短路视频子块，约 30 倍加速，SECS 仅降约 0.09

**是否开源**：暂无代码/Demo；基座基于开源 Kandinsky 5.0 架构与公开的 Qwen3-TTS 说话人编码器。

### ⭐ 评分：8/10
评分理由：以单个零初始化线性层实现从 T2AV 到语音克隆的最小改动，设计巧妙且严格保持基座能力，配方具备向任意非对称 AV-DiT 迁移的普适性。实验充分，覆盖五基线、三说话人网络、显著性检验、无回归与人类评测及 82 次消融扫描。纯音频推理的约 30 倍加速与 CFG 双权重权衡提升实用价值；但可懂度明显弱于专用 TTS，且未开源模型，可复现性受限。

---

## [8] Cached LLM Probability Retrieval for Speech Recognition

**arXiv ID**：2608.16023 | **方向**：语音大模型 / ASR语言模型适配

**作者**：Sheng Li, Takahiro Shinozaki, Tatsuya Kawahara

**机构**：Institute of Science Tokyo（东京科学大学）、京都大学

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16023 | **PDF**：https://arxiv.org/pdf/2608.16023.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
提出无需训练的"缓存 LLM 概率检索"ASR 重打分方法：离线用本地 teacher LLM（Qwen2.5-0.5B/Qwen3-8B）对背景文本打分并缓存上下文-目标 token 概率，识别时通过查表、短上下文回退与选择性直接打分获得语言先验。在 6 类 ASR 模型、39 项全数据配置中 28 项优于 1-pass 解码（Whisper-large-v3 与 SpeechBrain 上收益有限），Whisper-small 全 9 项提升、平均绝对 WER/CER 降低 8.13%。对比训练式 GER/KD 无需配对数据与参数更新，K=8 短上下文即最佳，是轻量、可解释的 ASR 适配层。

### 🔧 技术方案

**问题背景：** 直接让 LLM 逐句自回归重打分 N-best 列表代价高昂（延迟、内存与部署复杂度）；GER/KD 虽能降低运行时成本但需配对监督数据、参数训练及额外适配流程。现有检索/缓存 LM 仅存储计数或最近邻嵌入，语言先验弱。论文旨在识别前将 LLM 转化为可复用、本地的打分资源，无需改动声学模型。

**模型架构：** 缓存键由上下文 token 序列与目标 token id 组成，存储 log p_θ(y_t|c_t)，缓存得分为 S_K(y)=Σ_t log p_θ(y_t|y_max(1,t-K):t-1)（K 为最大上下文长度）。在线解码时各假设加性叠加缓存分数，并与 ASR 分数及检索式 5-gram 分数按 λ 系数在开发集上插值融合。缺失键回退链 K→K/2→⋯→1，全部未命中则用中性 fallback。选择策略：当 top-2 假设分数差小于阈值 τ 时才对重要缺失对直接调用 LLM 打分。

**核心创新：** (1) 缓存 teacher LLM 概率而非计数——检索值编码了比原始频次更强的语言先验，作为与经典 n-gram 重打分和训练式 GER 之间的中间方案，本地、透明、不训练参数。(2) 双层回退设计，全本地策略离线构建缓存后零在线 LLM 调用，选择性策略仅在 margin 低于阈值 τ 的歧义句调用 teacher，把昂贵计算保留在可能改变排序处。(3) 系统化揭示方法适用区间：N-best 多样性、缓存覆盖率与首 pass 分数共同决定收益，且 K 短上下文即足够（K>32 仅增加缓存构建成本无收益）。

**训练策略：** 无训练。缓存仅由非测试文本（训练/开发/领域或语言匹配 FLEURS 文本）构建；插值权重在开发 N-best 上调节。GER 基线用 LoRA 微调 Qwen2.5-0.5B（rank 8）与 Qwen3-8B（4-bit，rank 4），各 1 epoch。

### 📊 实验结果
**数据集**：LibriSpeech test-other、5dB 噪声 LibriSpeech test-other、AMI IHM、FLEURS（en/de/es/fr 用 WER，cmn/ja 用 CER）

**主要指标**：
- 28/39 配置优于 1-pass，25/39 为最低非 oracle 错误（K=32）
- Whisper-small：全 9 项提升，平均降低 8.13% 绝对 WER/CER
- 最大增益：AMI IHM 降低 13.01% WER，中文 FLEURS 降低 9.22% CER，噪声 LibriSpeech 降低 8.86% WER
- 上下文扫描：67 行 K=8 最佳或并列最佳，无配置偏好 K>32

**是否开源**：论文未提供代码/模型/数据链接，暂无。

### ⭐ 评分：8/10
评分理由：创新性地把 LLM 概率作为可缓存的本地资源用于 ASR 重打分，与 n-gram 缓存和训练式 GER 形成清晰定位，观点新颖且实用价值高。实验覆盖面广（6 种 ASR×2 种 teacher×4 语言数据集×上下文全扫描），28/39 与上下文 K=8 结论充分支撑论点，且诚实报告了 Whisper-large-v3 等负向区域。但方法依赖精确匹配、泛化弱于训练式模型，且未见代码开源。

---

## [9] DuplexGen: Decoupling Content, Timing, and Acoustics for Synthetic Dialogue Speech

**arXiv ID**：2608.16053 | **方向**：语音大模型 / 对话语音合成

**作者**：Pengcheng Wang, Sheng Li, Jiyi Li, Takahiro Shinozaki

**机构**：Institute of Science Tokyo（东京科学大学）/ 北海道大学

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16053 | **PDF**：https://arxiv.org/pdf/2608.16053.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有对话合成管线先生成内容、再用标记或规则插入重叠/打断/反馈词，时序是"规定"而非"涌现"。DuplexGen 将内容、时序、声学显式解耦：DeepSeek-V4 生成脚本，两个 Moshi 式 full-duplex 对话模型实时互听执行脚本（时序自然涌现），CosyVoice 无改时序重渲染。FTO Wasserstein 距离由 0.695 降至 0.366（相对降 47%），重叠转变比例 38.5%（真实 42.8%）。并构建带构造期标注的 MedDialSpeech 医患对话语料。

### 🔧 技术方案

**问题背景：** 常规方法（Behavior-SD、PersonaPlex 等）依赖对话标记、行为标签或手工时序规则拼接语音，重叠间隔分布坍缩到单一峰值，背离真实对话；而 full-duplex 模型（Moshi、SyncLLM）交互自然但自由生成、无法遵循预设脚本。可控内容与涌现交互难以兼得，二者结合少被探索。本文假设对话生成应按语义、交互、声学三类决策独立解耦，实现零训练管线。

**模型架构：** 三段式流水线，各阶段互不共享决策。S1 内容：LLM（DeepSeek-V4）生成按说话人有序排列的脚本 token 序列及游标。S2 时序：两实例基于 Moshi inner-monologue 架构，每帧先预测文本 token 再生成音频帧，双方持续互听对方的音频流。S3 声学：duplex 模型输出符号化交互乐谱（活跃说话人、话轮边界、重叠区、反馈词位置），由 CosyVoice 渲染成高保真语音。

**核心创新：** (1) 脚本约束双工解码：每帧拦截文本预测，将候选词表限制为{ PAD, 下一脚本 token }（有话语权者）或{ PAD, 反馈词白名单 }（听者），内容锁定与涌现两全。(2) 涌现时序与三控旋钮：无全局时间表，仅用 handoff window、max_padding 和 bc_refractory 调节事件频率，话轮交接起点、重叠时长均由在线音频交互决定。(3) 保真重渲染与相对时序迁移：因 duplex 模型与 TTS 语速不同，重叠过渡按相对位置迁移，静默过渡直接保留时长；滑动 prompt 维持长对话说话人一致性，打断语音物理截断加短 crossfade，词时间戳、说话人活动、重叠标签直接读自符号乐谱，自动获得构造期标注。

**训练策略：** 零训练框架，全复用现成组件（DeepSeek-V4、Moshi 式 duplex 模型、CosyVoice），不额外训练；脚本覆盖通用域与医疗域，基准按三档时序参数构造（180 段/175 分钟）。

### 📊 实验结果
**数据集**：PriMock57（参考分布，5,611 次话轮转移）+ 自建 MedDialSpeech 医患对话语料

**主要指标**：
- FTO Wasserstein 距离：0.366（拼接基线 0.695，降 47%）；KS 0.197（基线 0.432）
- 重叠转变/长尾间隔比例：38.5%/30.8%（真实 42.8%/20.5%）
- 重渲染 WER：≤1.7%；说话人一致性（CAM++）：0.82
- 反馈词落于韵律边界：95.5%（随机基线 71.7%）
- Whisper 重叠区 WER：28.3→48.1→56.7%（三档递增）
- 2×2 消融：渲染方式主导下游难度（truncate+fade 18.8% vs equal-volume 44.1%），时序影响不显著

**是否开源**：文章声明发布含标注的 180 段医疗评测基准，但正文未提供代码/模型链接；框架为零训练、复用开源组件构建。

### ⭐ 评分：8/10
评分理由：首次显式解耦内容/时序/声学，用脚本约束双工解码在词法锁定的同时保留交互涌现，方法简单有效且零训练。实验充分：覆盖分布真实性、管线忠实性、交互可控性与下游 ASR 压力测试，2×2 消融清晰区分时序与渲染的贡献。实用性较高：通向大规模自动构造具真实对话动态且带对齐标注的语料。扣分在交互仅部分涌现、重叠限于话轮过渡且无句中深打断，基准仅基于单一语料。

---

## [10] ARENA: Automated Red-Teaming for Large Audio Language Models

**arXiv ID**：2608.15578 | **方向**：语音大模型 / 音频语言模型安全

**作者**：Jiaming He, Zhicong Huang, Tian Jin, Zhen Sun, Cheng Hong, Yi Yu, Wenbo Jiang, Xudong Jiang

**机构**：未标注

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.15578 | **PDF**：https://arxiv.org/pdf/2608.15578.pdf | **代码**：https://github.com/Leanwithming/ARENA | **Demo**：暂无

### 📌 简介
针对文本侧安全而音频侧藏有害意图的"音频接地"攻击，本文提出 ARENA 闭环红队框架：用独立 2000 条文本-音频规格训练控制器，MD-Judge 提供训练奖励与自适应搜索反馈，仅由非自适应的 Llama Guard 3 独立裁决最终结果。在 520 条 AdvBench 目标上，ARENA 在 Audio Flamingo 3、Qwen2-Audio、MiMo-Audio、GPT-Audio 上 FDR/PSR 分别达 87.9/100.0%、71.5/96.3%、68.1/100.0%、75.4/98.5%，大幅超越静态基准，消融证明反馈式精炼与音效变体搜索显著提升攻击发现率，代码已开源。

### 🔧 技术方案

**问题背景：** 现有 LLM/多模态红队聚焦文本或视觉，LALM 的音频通道使无恶意的文本查询结合语音/环境音后可能诱导有害行为，且静态音频越狱集（AJailBench、JALMBench）无法自适应不同目标模型；失败响应中的识别失败、拒绝、事件复述等结构信号未被利用。

**模型架构：** 控制器策略 πθ 将危害目标 x 映射为结构化规格 z=(qp,pa,m)，m∈{speech,sound} 选择合成模态（Piper TTS 合成语音；TangoFlux 合成 4 秒环境音，带"no speech/no music"约束）；控制器为 LoRA 微调的 Qwen3-32B，输出 JSON 式 text_query/audio_prompt/modality/strategy_tags。执行时先对单独 qp 做文本守卫，再分两步查询目标（先识别查询 r_rec 再红队查询 r），最后用两个独立 Llama Guard 3 调用做输入检查与终局评估，MD-Judge 标签只进奖励与搜索、不进报告指标。

**核心创新：** (1) 双阶段控制器训练：奖励加权 SFT（按 R_Aud 加权并作过采样优先级）后接 DPO（同目标内按奖励配对偏好三元组，剔除目标侧识别错误主导的对）。(2) 模态感知的音频变体搜索：控制器学习在 speech/声音间选模态，失败时依据 MD-Judge 分层反馈（识别失败→简化声学事件或换模态；事件复述→改提问框架；拒绝→软化文本）迭代精炼，最多 K 轮，按 MD-Judge 阈值停止。(3) 评估解耦：MD-Judge 承担训练奖励与搜索反馈的"自适应"角色，Llama Guard 3 作为冻结的一次性终局裁判（FDR=PSR×ASR），杜绝直接针对评判器的优化。

**训练策略：** 2000 条独立种子池（1200 语音+800 环境音，基于 AudioGuard 风险分类学，与 AdvBench 严格不相交）；奖励 R=κ+w⁺ᵀs⁺−w⁻ᵀs⁻，κ=0.05；解码温度 0.7、top-p=0.95、256 新 token；精炼预算 K=30。

### 📊 实验结果
**数据集**：AdvBench（520 条有害目标，分 6 类）

**主要指标**：
- FDR：AF3 87.9% | Qwen2-Audio 71.5% | MiMo-Audio 68.1% | GPT-Audio 75.4%（PSR：100.0/96.3/100.0/98.5%）
- 基线对比：AJailBench FDR 仅 31.2/10.8/25.3/24.6%
- 转移性：AF3 发现用例迁移至 Qwen/MiMo/GPT-Audio 达 59.7/60.0/50.4% ASR
- 消融：K=0 时 ASR 仅 23-30%，K=30 升至 88/74/68%；环境音变体 M 从 1 增至 16 时 AF3 从 70%→95%

**是否开源**：代码开源（GitHub: Leanwithming/ARENA）

### ⭐ 评分：8/10
评分理由：首次把"文本安全+音频有害"双面约束下的 LALM 自动化红队形式化，双阶段控制器训练与 LLM 裁判+MD-Judge 分角色评价设计严谨。实验覆盖开源与 API 闭源模型、含转移性与系统消融，数值充分。作为红队/安全评测工具实用价值高。但机构未公开、未与现有音频越狱自动化方法做细粒度对比，且 MD-Judge 自举可能引入评测偏差。

---

## [11] ACE-Cap: Active Evidence Acquisition via Agentic Co-Evolution for Long-Paragraph Fine-Grained Audio Captioning

**arXiv ID**：2608.16162 | **方向**：语音大模型 / 音频字幕生成

**作者**：Fengji Ma, Yan Rong, Xu Li, Xuenan Xu, Chen Zhang, Li Liu

**机构**：未明确列出（首作者在 Kling Team 实习期间完成）

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16162 | **PDF**：https://arxiv.org/pdf/2608.16162.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
长段落细粒度音频字幕生成要求模型覆盖多样化声学事实，但现有字幕器均为被动一次性生成器，遗漏细节后无法自查、定向查询音频或自适应决定何时证据充分。本文将任务重构为主动证据采（Active Evidence Acquisition）问题，提出 ACE-Cap：由 Captioner 生成初始描述，文本-only 的 Composer 多轮提问、由音频条件化的 Instruct 回答，证据累积后 Composer 决定停止并合成最终长段落字幕，通过统一 gold-to-prediction 奖励与 LOOP-GRPO 训练。在统一 caption-as-evidence 协议下，ACE-Cap 在 MMAU/MMAR/MMSU 上达到 73.0/64.1/70.4，在 Omni-Cloze 上以 64.4% 超过所有闭源基线。

### 🔧 技术方案

**问题背景：** 现有一键式字幕生成模型在粗粒度或短句生成上表现良好，但面对长段落细粒度字幕时一旦遗漏细节便无法补救；扩大模型与数据规模无法获得主动信息获取机制。同时多轮交互训练存在两大难题：异构动作（提问/停止/合成）的跨回合信用分配（相邻差分法受回合顺序与分数饱和影响、给予早问以首动者优势）；多智能体共同优化时的目标移动导致训练不稳定。

**模型架构：** 三角色框架：音频条件化的 Captioner f_φ 产出初始字幕 c0；文本-only 的 Composer π_θ 依据 c0 与交互历史采样 ASK(q) 或 READY 动作、停止后合成最终字幕；音频条件化的 Instruct p_ψ 回答每个问题。训练时离线从每对音频-黄金字幕构建固定 Gold-MCQ 题库（每题 5 选项，E 恒为 Not Given），冻结的 caption-only judge 仅看候选文本打分。

**核心创新：** (1) 统一 G2P 奖励：判断题选中正确选项得 +1、Not Given 得 -0.5、错误得 -1，全题平均作为 R_G(y)，支持/遗漏/冲突事实分别对应三种分值，所有训练阶段共用同一 judge 与尺度。(2) LOOP-GRPO：以 leave-one-out 反事实信用代替轨迹级标量优势，提问信用 u^Q、停止信用 u^S（质量-长度权衡）、合成信用 u^F（证据保持效用），并按动作类型分组归一化后对齐到对应 token span，保留 clipped GRPO 目标。(3) 循序热身-交替协同进化：三角色先各自 SFT+单策略 GRPO 热身，随后 Captioner 永久冻结，Composer 与 Instruct 交替更新，使每次更新均为良定义的单策略优化问题。

**训练策略：** 训练数据 50,000 条来自 ASID-1M 的音频，黄金字幕由 Gemini 3.1 Pro 生成，Gold-MCQ 来自 3,000 对子集；Captioner 与 Instruct 初始化为 Qwen2.5-Omni-7B，Composer 初始化为 Qwen3-8B；GRPO rollout 组大小 G，预算 K 截断时停止信用省略。

### 📊 实验结果
**数据集**：ASID-1M（训练），MMAU/MMAR/MMSU/Omni-Cloze（测试）

**主要指标**：
- MMAU：73.0（超最强开源 5.1pp、超 Gemini 2.5 Pro 3.0）
- MMAR：64.1（超最强开源 8.8pp、与 Gemini 2.5 Pro 持平）
- MMSU：70.4（超最强开源 2.2pp）
- Omni-Cloze：64.4%（全方法最优，超 Qwen3-Omni-30B 6.9pp、超 Gemini 3.1 Pro 0.3）
- 查询预算：冻结 Composer 在 K=6/8 时证据保留率升至 1.83/1.49pp，K=2–4 性价比最优
- 查询行为：训练后 Composer 更聚焦语音与转写（SP 48.1%）

**是否开源**：暂未提供代码、模型与数据

### ⭐ 评分：8/10
评分理由：将主动证据采、leave-one-out 反事实信用分配的 LOOP-GRPO 与交替协同进化系统性整合到音频字幕生成，方法设计严密。实验充分：覆盖开源与闭源基线、四个基准与逐阶段消融，Omni-Cloze 的细粒度证据保留表现突出。框架思路对未来 agentic 音频理解有借鉴意义。扣分点：机构信息不明、无代码开源、单协议评测、数据仅用 5 万条 ASID-1M 子集泛化性待验证。

---

## [12] How Fragile Is Your Watermark? Training-Free Structural Removal of Neural Audio Watermarks

**arXiv ID**：2608.16566 | **方向**：语音大模型 / AI语音水印安全

**作者**：Likith Kumar

**机构**：Indian Institute of Technology Madras, Chennai, India

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16566 | **PDF**：https://arxiv.org/pdf/2608.16566.pdf | **代码**：https://github.com/i-618/audio-watermark-fragility | **Demo**：暂无

### 📌 简介
论文提出"先诊断后移除"的免训练框架：从少量干净/含水印配对信号计算四个廉价结构探针，估计水印嵌入域并据此选择单一匹配攻击，取代固定失真集的盲目扫描。在 10 种水印方案上，幅度域方案 WavMark、SilentCipher、audiowmark 被单次匹配攻击在近乎透明质量（PESQ≥3.6）下擦除载荷，AudioSeal 检测标志被移除；潜在域方案 VoiceMark、WMCodec、AlignMark、AWARE 抵抗所有免训练攻击。提出无阈值 fragility 分数量化脆弱性，探针签名还能在 10 方案中识别水印方案（84%）。

### 🔧 技术方案

**问题背景：** 现有鲁棒性评估（AudioMarkBench、RAW-Bench、SoK）对全部方案盲目施加同一固定失真集，仅报告聚合准确率/检测率，掩盖了攻击者真正关心的两个问题：水印嵌入在哪里、哪种扰动移除代价最低。已有移除方式要么是经典估计/减法、谐波攻击，需训练跨域去除网络。

**模型架构：** 四个探针均基于干净/水印对残差 r=y-h 计算：Concentration 为残差 DFT 能量在 16 频带中的最大占比（高→窄带载波→band-stop 陷波）；Coherence 为不同频带间载荷奇异向量重叠度（高→频率冗余→band-sweep）；Estimability 为宿主无关幅度模版跨样本的投影复现性（高→统一加性载波→模板减法）；Linearity 为逐位翻转在不同上下文间的余弦一致性（高→线性嵌入→估计减法）。探针仅需 39 次编码器查询/片段（最低预算 145 次）。

**核心创新：** (1) 诊断即移除：探针按其所度量的结构命名、不运行其选定的攻击，避免循环论证，使移除效果可归因于诊断而非专属攻击，全程零梯度、零参数、零训练。(2) 无阈值 fragility 分数：扫掠匹配攻击绘制精度-质量前沿，fragility=1-∫a·(q)dq，单一数字同时编码准确率与质量权衡，与操作点无关。(3) 附加识别能力与设计反向：同一探针签名经随机森林可在 10 方案上以 83.7% 准确率识别水印方案（随机 10%），并反向给出水印加固建议（分散频谱、联合跨带载荷、宿主自适应、非线性嵌入）。

**训练策略：** 无需训练；攻击均为闭式操作（幅度减法、滤波、足迹估计减法），零参数量，每片段约 17 MFLOP，一次性拟合最多 150 次编码器查询。数据含 LibriSpeech、VCTK、MUSDB18、VocalSet 及 XTTS-v2/F5-TTS/CosyVoice2 合成语音，N=100/方案。

### 📊 实验结果
**数据集**：LibriSpeech、VCTK、MUSDB18、VocalSet、XTTS-v2/F5-TTS/CosyVoice2 合成语音

**主要指标**：
- WavMark：模板减法后 bit-acc 降至 5.9%，PESQ 4.17，fragility 0.87
- SilentCipher：RMS 自适应减法后 10.3%，PESQ 3.84，fragility 0.84
- audiowmark：48.4%，PESQ 4.22，fragility 0.85
- AudioSeal：band-stop 消除检测标志（det 0.05，PESQ 3.62）
- DNN-AWM：2.25kHz 低通 band-sweep 58.9%，PESQ 3.34
- 鲁棒锚点：VoiceMark/WMCodec/AWARE/AlignMark fragility 0.27-0.39
- 方案识别：随机森林 83.7%（十类）；对比 HarmonicAttack 的 233 GFLOP/片段，本方法 17 MFLOP/片段

**是否开源**：开源，代码托管于 https://github.com/i-618/audio-watermark-fragility

### ⭐ 评分：8/10
评分理由：诊断式鲁棒评估视角新颖，探针设计严谨避免循环论证，fragility 指标为解决准确率-质量权衡提供实用方案。实验覆盖 10 种方案、5 类内容、PESQ/ViSQOL 双指标且开源。局限：排除同步攻击、仅单作者、未实现加固方案验证，fragility 仅为最廉价攻击的下界，属合理的免训练上界结论。

---

## 语音前端

---

## [13] Prototype-Rectified Iterative Self-supervised Manifold Denoising under Severe Acoustic Shift

**arXiv ID**：2608.15037 | **方向**：语音前端 / 测试时自适应

**作者**：Ashish Anand Shukla, Rini Smita Thakur, Aryan Das, Vinod K. Kurmi

**机构**：印度博帕尔科学教育与研究院（IISER Bhopal）、韦洛尔理工学院博帕尔分校（VIT Bhopal）

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.15037 | **PDF**：https://arxiv.org/pdf/2608.15037.pdf | **代码**：https://github.com/Ashish-1108/PRISM | **Demo**：暂无

### 📌 简介
音频-文本基础模型（ATM，如 CLAP）在严重声学噪声下性能骤降，现有 TTA 方法或依赖梯度而放大噪声，或需特权噪声标注。论文提出 PRISM（原型修正迭代自监督流形去噪），一个训练无关、源无关、噪声提示无关的 transductive TTA 框架：基于 Affine Noise Hypothesis 将严重噪声视为潜空间低秩仿射变形，以冻结文本原型为几何锚，用 OPCA、CCVD、逐类平移三种闭式校正经 Affine Bias Regression 编译为单一静态投影矩阵，推理仅一次矩阵乘（0.0009ms）。在 UrbanSound8K 上较 zero-shot 提升 +12.94pp，并超越获得特权噪声提示的 oracle TTA 基线 ContextDA 达 +9.41pp。

### 🔧 技术方案

**问题背景：** 三类现有方法均不匹配恶劣声学环境：静态几何对齐（协方差白化、线性探测）将噪声视为刚性整体平移，无法应对每个环境独特的旋转/平移/低秩变形；梯度 TTA（TENT 等）在 <0dB 多音噪声下产生确认偏差，把高置信伪标签反馈回循环等于在噪声底上训练；提示优化（TPT、ContextDA）需推理时不可得的噪声类型特权标注且迭代反传与实时流不兼容。

**模型架构：** 全流程嵌入空间闭式线性代数。校准阶段以无标注测试批迭代 3 轮：(1) OPCA 以置信门控（p=0.8 分位数）伪标签构造置信加权类质心，解 Orthogonal Procrustes 问题得最优旋转，附加自适应各向同性缩放 s∈[0.8,1.2]；(2) CCVD 基于逆 Fisher 比取前 K=60 特征向量为噪声子空间，用正交投影剔除（保留 q=0.7 高分样本）；(3) 逐类残差平移以强度 α=0.3 将各样本拉向预测文本质心。推断阶段零梯度、零批量统计，单样本一次 O(d^2) 矩阵向量乘。

**核心创新：** (1) Affine Noise Hypothesis：四种环境 SVD 实证显示噪声失真能量超 90% 集中于前 60 主成分，将严重噪声形式化为潜空间仿射变形，使得无需成对干净-噪声音频即可闭式求逆。(2) ABR 将三类校正编译为单一静态仿射映射：对原始输入增广全 1 偏置列，岭回归（λ=0.01）闭式解采集线性与平移两部分，并每轮锚定原始观测空间防止多轮漂移累加，使校准与批量无关推断彻底分离。(3) 发现 Polyphonic Trap 并提出 Confidence-Aware Regression：宽带多音类语义类内方差在谱上重叠"噪声方向"，CCVD 误删信号成分致 -17.20pp 崩塌；CAR 用 sigmoid 置信权重在噪声嵌入与 PRISM 输出间插值，为受影响最重类恢复 +8.16pp。

**训练策略：** 无梯度无优化器，零可训练参数。超参全场景固定：K=60、p=0.8、q=0.7、λ=0.01、α=0.3、R=3 轮，文本质心为每类 20 个提示模板嵌入均值。组件消融：OPCA +9.58pp、CCVD +3.09pp、ABR +0.27pp。

### 📊 实验结果
**数据集**：UrbanSound8K（8732 条/10 类/10 折，注入 TAU 2019 的 10 种噪声）、ESC-50（2000 条/50 类/5 折）、DCASE/TAU 2019

**主要指标**：
- US8K 准确率：71.71%，较 zero-shot +12.94pp，超 PCA++ +3.83pp、超 oracle ContextDA +9.41pp
- -6dB 严重区间：57.45% vs zero-shot 32.69%（+24.76pp）
- ESC-50：93.39%，超 TDA +2.29pp、超 PCA++ +15.82pp
- DCASE（假设违背场景）：PRISM+CAR 是唯一超 zero-shot 的方法
- 推理延迟 0.0009ms/样本，较 PCA++ 快 9 倍、较 CoNMix 快 5 个数量级

**是否开源**：代码开源（https://github.com/Ashish-1108/PRISM）

### ⭐ 评分：9/10
评分理由：将严重噪声形式化为可实证的低秩仿射变形并以纯闭式几何校正实现源无关 TTA，与梯度/提示方法形成清晰范式差异，理论-消融-诊断闭环完整。实验充分：构建了 10 背景×10 折的大规模 transductive 评测、覆盖 -6dB 严重 SNR 扫描与组件增量消融。实用价值突出：0.0009ms 延迟与零参数使其直接适用于边缘实时推理。扣分点：仅验证 CLAP 单一模型，CAR 与最优版本在精度/鲁棒间存在取舍。

---

## [14] A Novel Binaural Cue Preservation Loss for DNN-Based Binaural Speech Enhancement

**arXiv ID**：2608.16299 | **方向**：语音前端 / 双耳语音增强

**作者**：Jayteerth Amble, Thomas Haubner, Hendrik Schröter, Christoph Hoog Antink, Henning Puder

**机构**：德国达姆施塔特工业大学（TU Darmstadt）与 WSA（WS Audiology, Erlangen）联合团队

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16299 | **PDF**：https://arxiv.org/pdf/2608.16299.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
面向助听器 DNN 双耳语音增强，本文提出两种新颖双耳线索保持损失以缓解降噪引入的通道间关系畸变：双耳重建误差损失（L_BRE）直接惩罚时频掩蔽对左右谱关系的破坏，联合双耳线索损失（L_BC）将 ILD 与 IPD 在复单位圆上联合建模以规避相位缠绕。与 SOTA 的 L_ILD+10·L_IPD 基线 cue loss 相比，两种损失均保持接近仅降噪模型的 SI-SDR 与 MBSTOI，同时降低双耳重建误差；其中 L_BC 还取得最低 ILD 误差（IWAENC 2026 接收）。

### 🔧 技术方案

**问题背景：** 现有 DNN 双耳语音增强普遍以独立的 ILD 误差与 IPD 误差加权项作为空间保持目标。其缺陷有三：直接相位相减在 ±π 边界受相位缠绕干扰；误差均基于增强输出，无法隔离 T-F 掩蔽本身引入的通道间畸变；显式 cue 损失通常以牺牲降噪性能为代价。且评估缺乏统一标准。

**模型架构：** 采用编码-GRU-解码结构：6 层 2D 卷积编码器，输出通道{16,16,32,64,128,128}，核(5,3)、步长(2,1)；解码器用转置卷积镜像并带跳连；瓶颈为 2 层 hidden=128 的 GRU 加线性层。输入左右麦克风 STFT 并与幅度压缩 c=0.3，输出左右通道复数掩码；模型约 0.8M 参数。

**核心创新：** (1) 提出 L_BRE 损失：以最小二乘估计时不变 RTF，依据"通道间关系保持则一通道可由另一通道重构"原则，用压缩因子 γ=0.3 的 CCMSE 约束 X_L≈H̃_LR X_R 与 X_R≈H̃_RL X_L，从而把掩蔽诱导畸变与降噪目标解耦。(2) 提出 L_BC 损失：定义联合表示 Q(t,f)=|ILD|·e^{j·IPD}，损失项由 IBM 加权的 ILD 幅值平方差与 Q 复数域平方差两部分组成，将 IPD 编码在复单位圆上避免相位缠绕。(3) 将 L_BRE 同时作为评测指标，并采用 λ 按每一步降噪损失与空间损失比值动态计算的加权策略。

**训练策略：** 降噪损失用多分辨率 STFT 谱损失（窗 10/20/32/40ms，CCMSE，γ=0.3）；总损失 L=L_NR+λL_spatial。AdamW 训练 60 轮，初始 lr=1e-3、plateau 降 0.1，weight decay=1e-5；IBM 阈值 Γ=20dB；16kHz，FFT 512、hop 256；训练 SNR∈{-5,0,5,10,15}dB。

### 📊 实验结果
**数据集**：训练/验证用 LibriSpeech、TIMIT、EARS 经 KEMAR 头躯干 HRIR 空间化；测试 2700 条 LibriSpeech；噪声为 NOISEX-92 五种噪声，消声条件

**主要指标**：
- SI-SDR：仅 L_NR 基线最高；L_BC 与 L_BRE 接近该基线且优于 baseline cue loss
- MBSTOI：L_BC、L_BRE 与 L_NR-only 相当，均优于 baseline cue loss
- ILD 误差：L_NR-only 最差，L_BC 最低（优于 baseline cue loss）
- L_BRE 重建误差：L_BRE 训练模型最低，L_BC 亦低于 baseline cue loss

**是否开源**：论文未提供代码与 Demo 链接（license 为 CC BY-SA 4.0）。

### ⭐ 评分：8/10
评分理由：基于 masked RTF 重构的双耳重建误差损失思路独特，将掩蔽畸变与降噪解耦；联合 ILD-IPD 复表示简洁而有效地规避相位缠绕，对助听器实用价值较高。实验设计合理（五类噪声、多 SNR、多方位），但仅在无混响条件下验证，结论以图呈现缺乏表格化具体数值与统计显著性分析，模型仅 0.8M 参数的内部对比、未与外部 SOTA 比较，故扣分。整体为方法新颖、工程可落地的优质会议工作。

---

## [15] Navigating Speech Enhancement for Real-Time MRI: A Systematic Assessment of Signal Quality, Source Preservation, and Downstream Tasks

**arXiv ID**：2608.16125 | **方向**：语音前端 / 语音增强评测

**作者**：Huang-Cheng Chou, Sean Foley, Haley Hsu, Kevin Huang, Szu-Jui Chen, Rong Chao, Louis Goldstein, Khalil Iskarous, Dani Byrd, Yu Tsao, Sudarsana Reddy Kadiri, John H. L. Hansen, Shrikanth Narayanan

**机构**：南加州大学 | 德州大学达拉斯分校 | 台湾中央研究院资讯科技创新研究中心

**发布日期**：2026-08-18 | **论文**：https://arxiv.org/abs/2608.16125 | **PDF**：https://arxiv.org/pdf/2608.16125.pdf | **代码**：暂无 | **Demo**：https://rmridemo.huangchengchou.com

### 📌 简介
实时 MRI（rtMRI）同步录音被扫描仪梯度噪声严重污染，通用语音增强能否真正改善信号可用性此前缺乏系统验证。本文对 Denoiser、PASE、RE-USE 三个离架增强系统在五个 rtMRI 语料库上展开跨信号质量、源保真与下游任务的多端点评测。核心结论是增强效果与端点强相关：RE-USE 在 15 组对比中 11 组降低 WER，Denoiser 却在 13 组升高 WER；配对加噪探针中 PASE 与 RE-USE 显著提升 STOI/ESTOI/PESQ，Denoiser 虽提升 STOI 却降低说话人相似度。任何系统均非普适最优，增强输出应视为任务相关的变换派生信号。

### 🔧 技术方案

**问题背景：** rtMRI 语音受 MRI 梯度噪声（周期性强宽带瞬变叠加谐波）污染，即使经定制光纤麦克风、自适应对消与 DSP 处理仍有残留，严重影响 ASR、说话人建模、情绪识别与发音学研究。现有评测聚焦常规含噪语音，未验证跨语料库（0.55T/1.5T 场强、不同麦克风）时增强是否保留测量相关属性；且学习型 MOS 预测器对域外数据的效度未经检验。

**模型架构：** 三种互补架构的公开预训练模型全部离架应用、不微调：Denoiser 为因果波形域 LSTM 编码器-解码器（DNS dns64, H=64, 16kHz）；PASE 为 WavLM 去噪加双流声码器的生成式系统；RE-USE 为双向 Mamba 通用增强模型。评测端覆盖质量预测器、RawNet3 说话人相似度、wav2vec2 音素序列相似度、STOI/ESTOI/PESQ、PLV 调变一致性、共振峰 ABX、三种 ASR、emotion2vec 情绪识别等。

**核心创新：** (1) 构建五语料库、三增强模型、三识别器、多端点的系统评测框架，用 Raw/DSP/Lab 三输入条件分离"处理诱发改变"与"扫描噪声下的性能"。(2) 设计 clean-input 探针与存档配对加噪探针（370 对，中位 SNR -14.54dB），借四名 TIMIT 说话人的 Lab 参考实现源保真的配对检验。(3) 首次引入 PLV 调制相位锁定、共振峰 ABX 判别与抖动度量，连接信号质量与声学-音系属性，并以说话人聚类双阶段自举（5000 次）做配对区间推断。

**训练策略：** 模型零微调，输入切为≤60s 片段。加噪探针 SNR 中位数 -14.54dB；共振峰用 new-fave 的 LPC 加 DCT 平滑；置信区间为 95% 百分位 bootstrap。

### 📊 实验结果
**数据集**：LSS、USC-TIMIT、USC 75-Speaker、USC-EMO-MRI、Child（5 个 rtMRI 语料库）

**主要指标**：
- WER（RE-USE）：15 组 DSP 对比 11 组下降，均值 ΔWER=-1.28 点；LSS Raw 上 Qwen3 6.29→4.90%
- WER（Denoiser）：13/15 组升高（Δ+3.04 点），LSS Raw Qwen3 6.29→10.02%
- STOI/ESTOI/PESQ（加噪探针）：RE-USE 达 0.66/0.54/2.05 最优
- SpkSim：Denoiser 使 SpkSim 下降 -0.30，RE-USE 提升 +0.09
- SER（EMO-MRI）：RE-USE Macro-F1 48.50→56.83，sad 类 F1 29.42→44.94
- 关键发现：预测质量分升高不必然对应 ASR 或源保真改善，无系统普适最优

**是否开源**：无正式代码仓库，分析代码与派生分数经通讯作者申请提供；提供交互式 Demo。

### ⭐ 评分：8/10
评分理由：确立"增强即任务相关变换"这一反直觉结论，并首次用 clean-input 与配对加噪双探针解耦处理改变与噪声性能，方法论严谨（说话人聚类 bootstrap、配对区间）。覆盖面广（5 语料库、3 识别器、近 10 类端点）。局限在于输出级评测无法定位机制，加噪探针混合脚本已丢失且仅含 4 名说话人，未含主观听感实验。

---

## [16] Separate First, Then Associate: A Two-Stage Approach for Real-World Audio-Visual Speech Enhancement

**arXiv ID**：2608.14812 | **方向**：语音前端 / 音视频语音增强 | **评分**：7.5/10

**链接**：https://arxiv.org/abs/2608.14812

---

*Generated on 2026-08-18*