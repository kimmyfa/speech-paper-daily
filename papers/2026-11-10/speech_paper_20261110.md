# 2026-11-10 语音论文速递

**共收录**: 15 篇 | **语音大模型**: 8 篇 | **语音前端**: 7 篇

> 目标日期 2026-11-10（北京时间）arXiv 语音相关论文共命中 15 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] M5-TTS: A Mini-Scale Multilingual and Multi-Dialect Text-to-Speech Language Model with Multi-Token Prediction

**arXiv ID**：2611.10162 | **方向**：语音大模型

**作者**：Wenhao Li, Jingbin Hu, Shengming Ling, Xiaming Ren, Haoyu Zhang, Liumeng Xue, Pengcheng Zhu, Lei Xie 等

**机构**：西北工业大学 ASLP@NPU、南京大学 ASLP@NJU、深圳匹麦科技、Moonstep AI、WeNet 开源社区

**发布日期**：2026-11-06 | **论文**：https://arxiv.org/abs/2611.10162 | **PDF**：https://arxiv.org/pdf/2611.10162.pdf | **代码**：https://github.com/ASLP-lab/M5-TTS | **Demo**：https://aslp-lab.github.io/M5-TTS-Demo-Page

### 📌 简介
面向端侧语音交互，M5-TTS 用仅 50M 参数（不含 codec）的语言模型实现多语言+中国方言零样本音色克隆与 CPU 流式合成。架构为时序主干 Transformer 预测第 0 码本 + 局部 MTP 模块逐帧自回归生成第 1–15 码本（Qwen3-TTS 12.5Hz 16 码本 tokenizer），并采用 GRPO 后训练：说话人相似度与停顿奖励组内归一化加权，叠加 CER 引导、从句内反向传播并投影到 codec 帧的局部过程反馈。在 LM 参数量减半的情况下，Seed-ZH CER 1.37%、Seed-EN WER 2.91%，较 MOSS-TTS-Nano 相对下降 62.2%/35.3%；4 核 CPU 上 RTF 0.653、首包 225 ms。

### 🔧 技术方案

**问题背景：** 现有 LM-based TTS（CosyVoice 2、Qwen3-TTS 等）模型规模与推理成本难以在 CPU 端侧做低延迟流式；轻量模型（MOSS-TTS-Nano 等）又难以兼顾多语言、方言覆盖与音色克隆质量。

**模型架构：** 50M 参数分层分解架构：因果时序主干对 16 码本嵌入求和后在 12.5 帧/秒的 codec 帧率上建模，输出头预测语义码本 0；轻量局部 Transformer（MTP）在同一帧内自回归生成声学码本 1–15，骨干 KV 缓存跨帧保留、MTP 缓存逐帧重置。条件序列为口音 ID、语言 ID（微调时加说话人 ID）+ 文本。

**核心创新：** (1) 帧内多码本 MTP 分解：把 16 码本展开折叠为"帧间时序+帧内层级"两级自回归，避免时间步膨胀 16 倍，使 50M 模型实现 12Hz 低帧率流式生成。(2) CER 引导的局部 GRPO 过程反馈：将 ASR 字符编辑数经组内比较、从句内指数衰减反向传播（只传负优势），再按强制对齐重叠时长投影到 codec 帧，与全局 SIM/停顿优势共享给帧内全部 16 个 token，为内容错误提供逐步信用分配。(3) VoiceJudge 多维语音奖励模型（约 10 万人工偏好对训练）用于自然度 A/B 自动评测与配对一致性检验。

**训练策略：** 基础预训练约 40 万小时（Emilia/Emilia-YODAS、16 万小时内部数据、WenetSpeech4TTS/Yue/Chuan），覆盖中英德法日韩+粤语川话；CPT 精选约 6.5 万小时高质量/表现力/难例数据。GRPO 中 SIM 与停顿权重 0.3/0.4，PPO 式裁剪+KL 正则（对冻结 SFT 策略）；说话人微调采用 M2VoC 2021 数据。推理侧 ONNX Runtime KV 缓存、QKV 融合、自适应分块解码（batch 4/8/16 动态选择）、GPU BF16+torch.compile。

### 📊 实验结果
**数据集**：Seed-TTS Eval、MiniMax 多语种测试集、WenetSpeech-Yue/Chuan 方言集

**主要指标**：
- Seed-ZH CER：1.37%（MOSS-TTS-Nano 3.62%，相对降 62.2%）；Seed-EN WER：2.91%（vs 4.50%，相对降 35.3%）
- Seed SIM：0.65/0.53 vs 0.64/0.50；Seed-Hard 上仍逊于 MOSS（CER 17.48% vs 15.77%）
- MiniMax 6 语种中 5 个内容错误率更低；VoiceJudge 自然度偏好 84.89%/86.50%（正反序），胜者一致率 92.60%
- CPU（Intel Xeon Gold 6530 四核）：RTF 0.653、暖启动首包 225 ms

**是否开源**：将开源推理代码、音色克隆与专属说话人 checkpoint（GitHub + HuggingFace + Demo/Space）

### ⭐ 评分：8/10
评分理由：在极小参数量上同时做到多语言、方言、零样本克隆、说话人定制与 CPU 流式，且 GRPO 局部过程反馈设计有真正的技术增量，实验对比充分并诚实报告 Seed-Hard 劣势。工程完备度高、可复现资源齐全；扣分在于依赖 Qwen3-TTS tokenizer、复杂中文输入仍偏弱、部分基线数据不全。

---

## [2] Guidance at Pure Noise Erodes Speaker Similarity in Few-Step Token-Conditioned Flow-Matching TTS

**arXiv ID**：2611.11179 | **方向**：语音大模型

**作者**：Jaeho Lee, Han-Lim Choi

**机构**：KAIST 航空航天工程系

**发布日期**：2026-11-08 | **论文**：https://arxiv.org/abs/2611.11179 | **PDF**：https://arxiv.org/pdf/2611.11179.pdf | **代码**：https://github.com/16jhlee/FSU | **Demo**：暂无

### 📌 简介
零样本 TTS 的 flow-matching 解码器在生产中常被压到 2–4 步 Euler，此时 WER 不变但说话人相似度（SIM）掉 1–6 分。本文证明损失主要来自首步 CFG：纯噪声点网络只能输出条件均值，制导演化使全部轨迹平移同一矢量，步长越长损失越大，后续步骤无法消除。据此提出免训练的 FSU（首步不去guidance）与 FSU-Mid（中点步），仅 3 次网络评估即在 CosyVoice 2/3 上恢复 85–97% 两步 SIM 损失，FSU-Mid 在 IndexTTS-2 上恢复 77–80%，在 CosyVoice 2/GLM-TTS 达到甚至超过十步 teacher。

### 🔧 技术方案

**问题背景：** 蒸馏/少步解码器普遍报告 SIM 下降但无文献解释成因；图像域 guidance 调度工作均在 5–250 步规模、以模式丢失/范数增长解释，未隔离单步作用，也不涉及语音。

**模型架构：** 分析对象为四个 token 条件解码器（CosyVoice 2/3、IndexTTS-2、GLM-TTS），文本条件 F5-TTS/ZipVoice 作边界对照；所有实验用公开 checkpoint、只改采样器，评测 ERes2Net SIM、Seed-TTS-eval ASR WER/CER、5 个自然度客观预测器。

**核心创新：** (1) Proposition 1 闭式首步平移：精确速度假设下，首步状态 = 条件路径点 + w₁·Δu·a（与噪声种子无关的平移），方差不变、偏离量随首步长线性增长，解释十步无害、两步主导（cosine 网格首步 w₁ 占比差约 25 倍）。(2) FSU/FSU-Mid 采样器：首步只用条件网络（阈值 t=0.5 处 guidance 幅值衰减到噪声点三分之一），FSU-Mid 用无导引首评估+中点导引一步，NFE 从 4 降到 3。(3) 适用边界定位：token 条件解码器中 tokens+prompt 已锁定内容与韵律、说话人是唯一自由属性，故纯平移伤 SIM；文本条件解码器首步承担对齐功能、去 guidance 会涨 WER，应保持。

**训练策略：** 无训练（inference-only）。8 个噪声种子重复、逐语句配对检验、Holm 校正显著性、以种子噪声为最小可分辨差的严格统计协议；对 8 个已发表 guidance 规则（Selective-CFG、TV-CFG、MAMBO-G、JRR-CFG 等）在 4×2 单元格统一两步重跑。

### 📊 实验结果
**数据集**：Seed-TTS-eval test-en 1088/test-zh 2020/hard 400 句 + LibriSpeech-PC 1127 对，多语言/含噪/流式补充集

**主要指标**：
- FSU-Mid（NFE 3）：CosyVoice 2 SIM 74.87/81.27（两步官方 68.86/76.63，teacher 74.70/80.93），恢复 103%/108%；GLM-TTS 全 null 分支恢复 145%/135%
- 8 个已发表规则平均恢复率对比：FSU-Mid 100% 为最高，指导间隔法 76%，Selective-CFG 64%，JRR-CFG 11%，两个开源实现（CFG-Zero*、TV-CFG 原版）在全部解码器上崩溃（SIM<60）
- WER/CER 无显著上升；首包延迟与两步基线相同（省分支但官方 batch 下墙钟近零增益），Mel 空间闭式验证斜率≈1、guidance 差方向余弦相关 0.91–0.99

**是否开源**：代码与样例音频已开源 @ https://github.com/16jhlee/FSU

### ⭐ 评分：8/10
评分理由：以初等但干净的数学首次定位少步 flow-matching TTS SIM 损失的根因，推导—mel 空间直接检验—归因消融—边界样本的验证链条完整，结论可立即用于生产（免训练、还省一次 NFE），并重排了 8 个已发表规则。扣分：仅限公共 teacher（蒸馏学生未验证）、对文本条件解码器无解、单作者工业影响待检验。

---

## [3] Pandemonium: Longform Target-Speaker Speech Recognition with Cross-Speaker Interactions

**arXiv ID**：2611.10659 | **方向**：语音大模型

**作者**：Alexander Polok, Dominik Klement, Ivan Medennikov, Antoine Laurent, Petr Pálka, Samuele Cornell, Shinji Watanabe, Sanjeev Khudanpur, Jagadeesh Balam, Jan Černocký, Lukáš Burget, Matthew Wiesner

**机构**：布尔诺理工大学 BUT、NVIDIA、pyannoteAI、CMU、约翰霍普金斯大学（JSALT 2026）

**发布日期**：2026-11-07 | **论文**：https://arxiv.org/abs/2611.10659 | **PDF**：https://arxiv.org/pdf/2611.10659.pdf | **代码**：https://hf.co/BUT-FIT | **Demo**：暂无

### 📌 简介
针对 DiCoW 类目标说话人 ASR"各说话人独立解码、30 秒短窗"两个结构性缺陷，本文把 diarization 条件（STNO 掩码+FDDT 变换）集成进长form Parakeet FastConformer（DiCoP），并新增沿说话人轴的 cross-speaker attention（CSA）与 STNO 掩码精化器，让同一会话的多路解码在编码器内交互、互相消歧重叠段；用 DiCoW 对 YODAS2 自标注挖出 5.4k 小时真实多人会话。最终系统在 6 个会议基准（oracle 分离）平均 cpWER 14.7%（DiCoW v3.3 为 16.3%），AMI/NOTSOFAR-1/Mx6 等多处刷 SOTA，模型与伪标注数据全部开源。

### 🔧 技术方案

**问题背景：** TS-ASR 逐说话人独立前传，丢失跨说话人线索（重叠、轮次、backchannel）；Whisper 骨干 30 s 窗口限制长程上下文；SOT 类联合解码虽共享信息但对未知说话人数与重叠加噪泛化差。

**模型架构：** 长form Parakeet（FastConformer，局部窗口注意力+全局 token）为骨干，FDDT 用 4 类仿射变换按 STNO 概率逐帧调制每路编码器状态；同会话各说话人作为一个 batch，在选定层沿"说话人轴"做多头注意力（QKV 均为单帧跨说话人堆叠，无位置编码、说话人数可变），近零初始化保持热启动不变；掩码精化器从交互后的状态重估每说话人活动、重构 STNO 并经 sigmoid 门回掺。

**核心创新：** (1) CSA 首次让 TS-ASR 路间在编码器内交换证据，且以零初始化残差方式接入、不破坏单说话人能力。(2) STNO 掩码精化：解决重叠帧内多个说话人条件掩码相同、无法互分的固有缺陷。(3) TDT→CTC 迁移技巧：冻结 TDT 头、置零 predictor 状态使 joiner 帧同步化后用 CTC 训练，绕开长 chunk 下转递损失二次显存与 1024-token 核限制，greedy 解码极快。(4) 高质量伪标注管线：最高重叠度遴选 5.4k 小时 + Kimi LID 校验、n-gram 幻觉正则、跨说话人泄漏过滤。

**训练策略：** 四路数据：真实会议 115 h（NOTSOFAR-1+AMI）、DiCoW-orig 1.2k h、合成 4k h（FastMSS/Fisher-Sidon）、伪标注 YODAS2 4.6k h；CTC 变体从头训练，CSA/精化器两阶段接入，pyannoteAI Precision-3 提供预测分离。

### 📊 实验结果
**数据集**：评估 NOTSOFAR-1、AMI、ICSI、Mixer6、SBC、DiPCo、AISHELL-4、AliMeeting（cpWER，oracle/预测分离两种条件）

**主要指标**：
- Oracle 分离 6 集平均 cpWER：Pandemonium 14.7% vs DiCoW v3.3 16.3%、DiCoP 无 CSA 16.7%（CSA+精化器贡献约 2 个点）
- +MOVER 全麦克风解码融合后均值 13.0%（NSF 10.8%）；预测分离 19.2%、+MOVER 17.1%，逐集多数优于已发表 SOTA
- 单麦克风 SOTA：NSF 22.8/AMI 17.6/ICSI 20.9/Mx6 14.5/DiPCo 34.0 全面被超越；长form greedy 解码 RTFx 大幅提高

**是否开源**：DiCoP、Pandemonium 模型权重及 5.4k h 伪标注数据已开源 @ https://hf.co/BUT-FIT

### ⭐ 评分：8/10
评分理由：问题定位精准、模块设计（CSA/掩码精化/CTC 化）都直击 TS-ASR 的结构性短板，跨 8 个会议语料评测充分且诚实标注 oracle/预测差异，发布模型+数据双重开放对社区价值高。扣分：预测分离条件下增益收窄说明误差仍被分离质量钳制，方法本身偏系统工程整合、单模块创新度中等。

---

## [4] REAL: Reward Modeling through Evidence-Linked Analysis of Lifelikeness in Generated Speech

**arXiv ID**：2611.12406 | **方向**：语音大模型

**作者**：Yaodong Song, Jie Lian, Xusheng Yang, Genliang Zhao, Hongjie Chen, Jian Kang, Zhen-Hua Ling, Jie Li, Yongxiang Li

**机构**：中国科学技术大学、中国电信星辰大模型实验室（CTAI）

**发布日期**：2026-11-09 | **论文**：https://arxiv.org/abs/2611.12406 | **PDF**：https://arxiv.org/pdf/2611.12406.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有语音奖励模型的"解释文本"由单一理解模型生成、只按整句偏好一致性过滤，局部声学论断未必有音频依据。REAL 把"证据链"作为显式监督目标：REAL-Jury 用协调模型编排 Qwen3.5-Omni 与 Step-Audio-R1.1 交叉质证、强制对齐锚定时间戳、争议驱动的闭环审议合成证据关联报告；REAL-Judge 以 MiMo-Audio 为骨干 LoRA 蒸馏出带时间标记输入的单一奖励模型；配套两档基准 REAL-Eval。最终在 Standard/Fine 两档偏好预测达 84.43%/65.36%，较骨干提升 16.01/11.41 个百分点，全面超过 SpeechJudge 与 UniSRM。

### 🔧 技术方案

**问题背景：** MOS 协议贵且慢；已有生成式评价模型（WavReward、SpeechJudge-GRM 等）的监督定义在话语/配对级，推理与音频证据之间的忠实性未经验证，CoT 忠实性研究表明解释可能只是事后合理化。

**模型架构：** 三组件流水线：REAL-Jury=DeepSeek-V4 协调器+两个理解模型+Wav2Vec2 强制对齐（每对最多 15 次调用），产出"时间段→局部现象→受影响维度→整体判断"自下而上的报告；REAL-Judge=MiMo-Audio-Instruct 冻结骨干，音频以 T 秒粒度插入显式时间标记嵌入；REAL-Eval 分 Standard（SpeechJudge-Eval 400 对，6 个零样本 TTS）与 Fine（6 领域真实文本×OmniVoice/Qwen3-TTS/VoxCPM2/CosyVoice3，207 对，10 人标注多数票）。

**核心创新：** (1) 把证据关联结构（span-phenomenon-dimension-verdict 链）本身作为训练目标，而不只监督最终偏好，使"理由"必须与音频对齐。(2) 争议导向审议闭环：协调器在发音/停顿/情感/表现力/整体偏好不一致处发起针对性追问并复核指定字符与时间段，优于单模型一次性生成的幻觉。(3) 时间标记输入表示：随音频变长仍可精确指位，消融显示去标记降 1.5+点。

**训练策略：** 训练语料取 SpeechJudge 公开偏好对经 REAL-Jury 全流程构造 11,947 对证据链报告；LoRA rank 64/alpha 128，峰值 lr 1e-4 余弦、warmup 0.03、bf16、global batch 32、8×A800；仅报告 token 上自回归 NLL；推理不需要 Jury 与人工标签。

### 📊 实验结果
**数据集**：REAL-Eval-Standard（400 对中文）与 REAL-Eval-Fine（207 对、训练域外系统/文本/参考语音三 disjoint）

**主要指标**：
- REAL-Judge：Standard 84.43%、Fine 65.36%（骨干 MiMo-Audio 68.42%/53.95%，相对提升 +16.01/+11.41pt）
- 对比开源奖励模型：SpeechJudge 83.00%/58.45%、UniSRM 80.75%/63.29%；两档均被 REAL-Judge 超越
- 闭源对照 Gemini-3.1-Pro/Qwen3.5-Omni Fine 档 67.31%/67.63% 仍领先约 2 点；下-CER 启发式仅 18.75%/6.76% 说明"低错误率≠像人"
- Jury 集成 80.92% 高于任一成员模型（Qwen3.5-Omni 79.82、Step-Audio-R1.1 75.33）

**是否开源**：承诺发布代码与模型权重，暂未上线；中文单语范围

### ⭐ 评分：7/10
评分理由：切中"解释是否忠实于音频"这一评价建模真问题，Jury-蒸馏-两档评测的闭环设计与 Fine 档的域外泛化协议较严谨，收益幅度真实。不足：数据构造依赖多模型调用成本高、偏好准确率仍是主指标（证据忠实性无独立人评）、Fine 档未超商用 omni 模型、评测仅中文。

---

## [5] SCLAP: Temporal Structural Alignment Improves Localization in Long-Form Audio

**arXiv ID**：2611.12124 | **方向**：语音大模型

**作者**：Yacouba Kaloga, Ina Kodrasi

**机构**：Idiap 研究所（瑞士）

**发布日期**：2026-11-09 | **论文**：https://arxiv.org/abs/2611.12124 | **PDF**：https://arxiv.org/pdf/2611.12124.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
CLAP 类模型把音频帧与文本 token 均匀池化成全局向量，丢弃时间结构，在长录音、低事件占比场景下检索被稀释且无法定位。SCLAP 在每对音频-字幕内部用单调一维最优传输直接耦合帧与 token：两个轻量标量网络各自预测边缘权重，transport-加权余弦相似度替换 InfoNCE 中的池化相似度，仅凭 clip 级字幕即学到细粒度时间监督。短音频（Clotho/TACOS）检索持平基线、零样本定位大幅改善（AudioSet-strong pAUROC 72.36→76.13）；长音频（CASTELLA ≤300 s）检索最优，且事件被无关上下文稀释越狠定位优势越大（320 s 上下文 R@1@IoU0.3 7.60 vs CLAP 6.10）。

### 🔧 技术方案

**问题背景：** 时间定位类方法需时序标注或额外监督；TAP（文本感知注意池化）只给全句一个注意力分布、无 token-帧对齐且权重从不作定位监督；已有 OT 只用于 batch 内池化样本间匹配而非对内部序列对齐。

**模型架构：** 双编码器：AudioSet 预训练（AudioSet-strong 帧级微调）ASiT 谱变换器输出每 clip 1491 个帧嵌入 + RoBERTa-base 文本 token，线性投影至共享 1024 维 L2 归一化；SCLAP 仅改训练相似度：音频侧与文本侧各接一个轻量标量网络以 softmax 产出边缘 α、β，帧-token 代价用余弦，单调一维耦合由累积分布唯一确定、复杂度 O(n+m)。

**核心创新：** (1) 对偶预测边缘的单调 OT 对比目标：因 α 只由音频序列、β 只由文本序列独立计算，训练迫使每个模态单侧识别"字幕所指内容"的位置，等价于免费获得细粒度时间监督。(2) 推理免解 OT：检索用边缘加权池化 s_P（与普通 CLAP 点积同价），定位直接用帧-文本余弦 s=cos(x_i, ȳ)，可预计算嵌入库。(3) 单调节假设为 ASR 域 SOTD 的迁移，靠"近零质量位自动退出对齐"缓解多事件顺序任意问题。

**训练策略：** 端到端微调 20 epoch、AdamW 余弦；CASTELLA batch 16（4 步累积）/Clotho+TACOS batch 32；温度 τ 先定、再音频边缘温度、最后 lr，文本边缘温度 β=1；CASTELLA 上 τ 可训练；3 个随机种子报均值±方差。

### 📊 实验结果
**数据集**：Clotho、TACOS（15–30 s 短音频）、AudioSet-strong（零样本事件检测）、CASTELLA（60–300 s 长音频全局字幕训练，其局部字幕/时间戳仅用于评测）

**主要指标**：
- 短音频定位（AudioSet-strong）：SCLAP-T pAUROC 76.13±0.69 vs CLAP 72.36±1.18，PSDS1-macro 13.96 vs 12.57；TAP 的 AV 读数 PSDS1 近零（0.46）
- 长音频定位：全指标第一，R@1@IoU0.3 7.60±1.05 vs CLAP 6.10/TAP 4.67；稀释实验：20 s 上下文三法接近（TAP 18.25 略胜），40 s 起 SCLAP 持续领先且差距随上下文增大（320 s：7.60 vs 6.10 vs 4.67）
- 检索：短音频与 CLAP/TAP 差异在种子噪声内；CASTELLA 上 SCLAP-P mAP@10 均值最高，且推理可池化预计算（TAP 需每对重算注意力）

**是否开源**：承诺录用后公开代码与模型

### ⭐ 评分：6/10
评分理由：动机清晰、方法简洁（仅改相似度函数、不动骨干），"训练时 OT、推理时零成本"是实用卖点，长音频定位随稀释度增加的优势有说服力，实验按种子重复较规范。局限：数据规模小（仅 AudioSet 预训练后微调）、绝对性能仍属低水平（R@1 个位数 %）、缺与有监督 moment retrieval 方法对比、暂未开源，整体为扎实但增量式的表示学习改进。

---

## [6] Capability-Guided Iterative Online Optimization of Cascaded Spoken-Dialogue Modules

**arXiv ID**：2611.11322 | **方向**：语音大模型

**作者**：Yuhang Qiu, Bohan Li, Wenbin Huang, Zhihan Li, Yiwei Guo, Hankun Wang, Xie Chen, Kai Yu

**机构**：上海交通大学 X-LANCE 实验室

**发布日期**：2026-11-08 | **论文**：https://arxiv.org/abs/2611.11322 | **PDF**：https://arxiv.org/pdf/2611.11322.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
级联语音对话系统中 ASR 与 TTS 的"语音↔内容"接口近似互逆，单侧数据可互为监督：语音可伪标注训 TTS，文本可渲染成语音训 ASR。但 teacher-student 方向随语言/领域强弱变化，固定排程会把弱方误差传染给强方。本文提出两阶段能力引导的迭代在线优化：先用共享可懂度探针在留验域上测双向错误得到"域级能力先验"，再逐路由强作 teacher 构造在线监督、规则过滤、更新弱的一侧，优化器/学习率状态跨周期延续，并以双侧 on-policy 蒸馏（OPD）约束偏离。实例化 Whisper large-v3 + CosyVoice2 后，MAGICDATA-RAMC 上 Whisper CER 14.18→10.77、CosyVoice2 同模型回读 CER 4.78→4.04。

### 🔧 技术方案

**问题背景：** speech-chain/TTS-to-ASR 等既有工作固定学习方向、一次性物化合成数据；弱模块当 teacher 会传误差，监督分布无法跟上模块更新。

**模型架构：** Stage 1 能力评估：对每个域 D 构造探针集（参考文本、真实波形、VAD 或说话人池提示音），计算感知侧 E_p=CER(ASR(x),y) 与生成侧 E_g=CER(ASR(TTS(y',p')),y')得域级先验，结合可用单侧数据池（语音池 S / 内容池 C）路由更新对象。Stage 2 迭代在线：感知占优→ASR 伪转写真日语语音、经往返可懂度检查后对原波形训练 TTS；生成占优→TTS 合成中文语音、经时长/学生侧可懂度/ReadScore 过滤后更新 ASR；每周期重建 checkpoint，决策模块 LLM 不动。

**核心创新：** (1) 以互为回读的可懂度探针统一度量两端强弱，把 teacher 方向变成数据驱动的每域决策。(2) 在线监督构造+检查点刷新：过滤决策随最新 student/teacher 变化，区别于一次性伪标注语料。(3) 双侧偏离约束：以原始模块为参照的 on-policy distillation 限制每侧更新幅度，防双向优化漂移与灾难性遗忘；所有能力/路由/选择/停止规则均手工固定、不引入可学习策略。

**训练策略：** Whisper large-v3 仅 200 步、CosyVoice2 600 步的极小预算在线优化；路由到日语用真实语音（CV）、中文用源文本（MAGICDATA-RAMC）；matched step-budget 与学习率排程下与 one-shot 静态参照对比。

### 📊 实验结果
**数据集**：MAGICDATA-RAMC（中文）、Common Voice（日语）

**主要指标**：
- Whisper CER：中文 14.18%→10.77%；日语 15.23%→15.10%
- CosyVoice2 回读 CER：中文 4.78%→4.04%；日语 14.85%→11.18%
- 与 one-shot 静态伪标注对照：在线迭代 Whisper 两测试集均更优；但在线 CosyVoice2 在日语略差于静态参照、中文亦落后——作者如实报告双向不对称收益

**是否开源**：暂无

### ⭐ 评分：6/10
评分理由："能力先验路由+在线重建监督+OPD 防漂移"对级联系统自进化是个设计完整的框架，收益真实且成本极低（数百步），对比设置诚实。不足：实验仅两个模型/两种语言、无与 joint chain-training 的强基线数值对比、日语侧收益边际、未开源，方法学创新主要在组合层面而非单点突破。

---

## [7] Ninada: Sub-Clause Split-Graph VITS Streaming and Capability-Routed 24 kHz Speech Synthesis Across Twelve Scripts

**arXiv ID**：2611.10035 | **方向**：语音大模型

**作者**：Hemanth HM

**机构**：个人开源项目（独立研究者）

**发布日期**：2026-11-05 | **论文**：https://arxiv.org/abs/2611.10035 | **PDF**：https://arxiv.org/pdf/2611.10035.pdf | **代码**：https://github.com/hemanth/ninada | **Demo**：暂无

### 📌 简介
浏览器端 VITS 整句 ONNX 一次性执行导致 TTFA 达 2–4 秒，且印度语系多脚本客户端部署受模型体积、移动 GPU 编译停顿、big.LITTLE 线程屏障与移动 Web Audio 限制四重瓶颈。Ninada 给出开源方案：48 个检查点车队（24 桌面 HiFi-GAN 27.9MB + 24 移动蒸馏 iSTFTNet 21.7MB + 0MB Klatt 兜底）覆盖英/梵/10 种印度语言原生文字；运行时以零依赖 protobuf"外科手术"把单文件拆成 prior/flow/vocoder 三个子会话流式执行，配 12 帧 halo+升余弦交叠消除接缝。实测桌面 WebGPU 首帧 89–155 ms，Pixel 10 Pro XL 真机 538–649 ms 零欠载流式（RTF 0.75）， held-out 录音 0–8kHz MCD 3.22dB，远优于 1.5GB 的 Meta MMS 车队（5.17dB）。

### 🔧 技术方案

**问题背景：** MMS-TTS 16kHz+138.8MB/语、罗马化合并脚本引发跨语口音沾染与查图/马拉雅拉姆特殊字符丢失；WebGPU 在手机上着色器编译停顿 6–14 s 且暖机仍超实时；全尺寸 HiFi-GAN 在手机 WASM 上 RTF>1，任何窗口都无法阻止缓冲枯竭。

**模型架构：** 每语一单一说话人 VITS：6 层相对位置 Transformer 文本编码器（原生 Unicode 直接 tokenize）、有理二次样条随机时长预测器、4 层残差仿射耦合流，帧移 10.67 ms；双 vocoder 按能力路由：桌面 HiFi-GAN v1（28.8 GMAC/s）、移动 c8c8_384 iSTFTNet——将最后一级上采样换成"用固定 Cos/Sin 基的静态实值 ConvTranspose1d 精确实现 NOLA 逆 STFT"，零复数算子、5.09 GMAC/s；0MB Paninian/Klatt Akshara 规则兜底。

**核心创新：** (1) 运行时二进制 ONNX 子图手术：扫描顶层 GraphProto wire tag、以 conv_post 潜变量与 conv_pre 张量为拓扑切点，~5ms 内把一个 .onnx 拆成三个子会话，免发布三件套资产。(2) 稳定性界推导：有效 RTF r·F/(F−2n) <1 才可单调增长缓冲（F 窗长、n halo），据此论证 iSTFTNet 蒸馏的必要性与窗口/线程策略。(3) 移动管线组合拳：6 线程宽池绕开 E 核屏障、句级子句准入缓冲门限（Qmin=1.5 s）、24→48kHz C1 Hermite 整数帧 AudioBufferSourceNode 队列、iOS WKWebView 触摸内同步解锁+静音桥。

**训练策略：** iSTFTNet 学生以冻结 prior+flow 配对教师潜变量蒸馏 30,000 步，多分辨率 STFT/子带幅值/mel/MPD 特征匹配损失；W8A32+FP16 混合量化（编码器/流 INT8、卷积与傅里叶基 FP16），学生平均教师-学生 MCD 仅 1.33 dB、重建 SNR 108.2 dB。

### 📊 实验结果
**数据集**：ai4bharat/Rasa 与 hifi-tts 24 kHz 干录音演播室语料，12 语言各 150 句 held-out

**主要指标**：
- 0–8 kHz DTW MCD：桌面 Studio ONNX 3.22 dB、移动 iSTFTNet 3.09 dB vs Meta MMS 车队 5.17 dB（体积 27.9 MB vs 1526.8 MB，−97.3%/语言）；8–12 kHz 误差 6.07 vs 64.97 dB（全频带优势）
- TTFA：桌面 WebGPU 89–155 ms；真机 Pixel 10 Pro XL 538–649 ms 首帧、连续播放 0.75–0.76 RTF 零欠载
- 量化：FP32→ONNX 波形直接 MCD 差 0.01 dB；单一 mms-tts-hin 在非天城文脚本上仅 29.4% 可发声，Ninada 12/12 脚本原生支持

**是否开源**：全套训练/推理代码与 48 个检查点开源 @ https://github.com/hemanth/ninada

### ⭐ 评分：6/10
评分理由：罕见的移动端语音 synthesis 系统级论文，从图手术、NOLA 逆 STFT 到稳定性界的推导完整、真机遥测数据扎实，12 语系原生正字法+全开源代码实用性高。扣分：非语音大模型而是经典 VITS 工程化，声学上限是单语者录音室声音、无 MOS/主观评估、无自适应音色，学术新颖性有限但工程参考价值高。

---

## [8] Industry case studies of adapting TTS for smooth interactions

**arXiv ID**：2611.09914 | **方向**：语音大模型

**作者**：Paige Tuttösí, Eléonore Ferrier-Barbut, Anais Scipioni, Olivia Yung, Ha Eun Shim, Ajla Basic, Yue Wang, H. Henny Yeung

**机构**：Enchanted Tools（法国）、Simon Fraser 大学语言学系/计算科学系、PUMCH、北京回龙观医院等

**发布日期**：2026-11-05 | **论文**：https://arxiv.org/abs/2611.09914 | **PDF**：https://arxiv.org/pdf/2611.09914.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
产业界 TTS 几乎都按"默认用户"设计，对听力衰退老人、障碍人群与高噪声环境缺乏自适应。本文由机器人公司 Enchanted Tools 报告 Mirokaï 社交机器人在美国养老机构（27 位老人，均龄 83.5）与法国里昂机场（263 次交互、138 份反馈）两个真实部署中观察到的对话破裂，并实施轻量 TTS 适配：80%/75% 语速减速、音量-音高线性联动噪声模式（pitch 75→90 cents）、音素级目标减速（迁移至 Matcha-TTS 支持 phoneme duration 控制）与用户语音控速/控音量指令。后续回访中"听不清"投诉大幅减少，老人总体接受度高（舒适 4.59/5），作者呼吁社区建设面向非默认用户的自适应 TTS。

### 🔧 技术方案

**问题背景：** 研究界 TTS 追求 human-likeness 却在真实 HRI 场景失效：老人反馈机器人说太快太轻，机场最大音量仍被环境噪声淹没且喇叭饱和失真；商用自适应 TTS 系统几乎空白。

**模型架构：** 机器人端嵌入式 TTS，初版基于 FastPitch（英/法双语），后升级 Matcha-TTS 架构获得音素级时长控制、在声码前施加修改；适配层用 SoX 做语速/音高变换（wizard-of-oz 起步）；"噪声模式"=语速 75% + 音量 75–100% 区间线性升 pitch 75–90 音分。

**核心创新：** (1) 从 L2 听者研究迁移"目标词减速"到老年用户，避免全句匀速放慢带来的负面态度。(2) 把环境感知量（输出音量档位）直接耦合进韵律参数形成单一噪声模式。(3) 系统记录两种用户组失效模式的可复现案例框架，供更大规模研究参照。

**训练策略：** 无模型训练，属部署实践报告；数据来自机构日常活动与机场问询的自然交互+每日 5 点 Likert 问卷与自由文本反馈。

### 📊 实验结果
**数据集**：真实场景：美国养老机构（N=27 老人，1v1 8–10 分钟+团体 15–20 分钟活动）、里昂机场（N=263 交互，家庭带儿童占 40.6%）及回访残障人士护理院（≥15 人）

**主要指标**：
- 老人 Likert：喜欢 4.22（SD 0.70）、舒适 4.59、安全 4.74、愿意再来 4.11；最低"帮助连接他人"3.59
- 机场：互动容易度 3.77、回答有用性 4.00；8% 表示回答不可理解，但 14.4% 面访旅客提及负面体验且绝大多数为理解问题；65% 认为航班类问题答不好
- 适配后回访：理解类投诉"大幅减少"、噪声模式下无老人式的"pitch 过高"抱怨；但均为定性观察，无统计对照

**是否开源**：暂无

### ⭐ 评分：4/10
评分理由：真实产业部署+弱势用户视角的稀缺案例记录，问题陈述有号召力、Likert 数据具体；但作为 TTS 论文技术含量很低——SoX 变速变调即核心手段，评估是定性观察与无对照问卷，噪声模式"后续研究尚未完成"，样本小且不可复现。适合作 HRI/无障碍方向的案例参考，不建议语音技术研究者深挖。

---

## 语音前端

## [9] Nemotron 3 Diarization: Advancing the Accuracy–Efficiency Frontier in Streaming Speaker Diarization

**arXiv ID**：2611.12246 | **方向**：语音前端

**作者**：Ivan Medennikov, Taejin Park, Tatiana Timofeeva, He Huang, Alexander Polok, Sofia Kostandian, Weiqing Wang, Dongji Gao, Jagadeesh Balam, Boris Ginsburg

**机构**：NVIDIA、布尔诺理工大学（合著）

**发布日期**：2026-11-09 | **论文**：https://arxiv.org/abs/2611.12246 | **PDF**：https://arxiv.org/pdf/2611.12246.pdf | **代码**：https://huggingface.co/nvidia/Nemotron-3-Diarization | **Demo**：暂无

### 📌 简介
把开源流式 Sortformer 从 4 说话人/80ms 输出升级到 8 说话人/10ms：骨干由 FastConformer+Transformer 117M 简化为纯 31 层 RoPE Transformer 99M，顶上加 subpixel 卷积把 80ms 帧映射到 10ms 分辨率，AOSC 缓存 188→264 帧并将静音 embedding 改为可学习。新增活动损失与"幽灵说话人"惩罚，配混合数据+变上下文块因果训练，单权重覆盖离线到 0.32s 低延迟。DIHARD III DER 12.73%、CALLHOME 9.10% 刷新开源 SOTA；训练显存降 2.8×、2.2× 快、推理吞吐最高 6.4×；条件 DiCoW 后在 AMI/NOTSOFAR-1 上再刷 tcpWER SOTA。代码与 OpenMDW-1.1 权重全开源。

### 🔧 技术方案

**问题背景：** Streaming Sortformer-v2.1 限 4 人、预测 80ms 步进，说话人容量↑→缓存与推理成本↑、空通道易误激活（phantom）、10ms 帧步会爆炸注意力序列——四者互相耦合。

**模型架构：** 8 倍特征堆叠下采样+31 层 RoPE Transformer 编码器（80ms 帧步）；宽度 3 的一维 subpixel 卷积把每帧 768 维映射为 8×768 并重塑为 8 个 10ms 状态，几乎零开销地把输出头提到 10ms 分辨率；带到达序说话人缓存 AOSC（264 帧）与可学习均值分离 embedding；PIL+ATS 双主损失+三分类活动辅助头（静/单/重叠）+空通道负样本 phantom 约束（γ=0.4, β=4 对数均值池化）。

**核心创新：** (1) 精度-效率解耦设计：粗帧编码+可学习上采样替代细帧编码，兼顾边界精度与成本。(2) 幽灵损失直击 8 通道冗余下的高置信误激活，log-mean-exp 池化对最大虚假激活敏感而不随帧数线性放大。(3) 训练时每 batch 以 0.5 概率施加 1–8 帧 block-causal 尾部掩码，同一 checkpoint 统一支持离线与全部延迟档。(4) NEST 自监督初始化（90 万小时 Granary-v2 预训练）+真实/伪标签/82.6k 小时 FastMSS 仿真混合。

**训练策略：** 两阶段：64×A100、bf16-mixed，先纯仿真离线 Sortformer（PIL/ATS/activity/phantom 权重 0.5/0.5/0.5/0，80ms 原生分辨率），后流式微调（真实+仿真 105 s 样本、双段拼接概率 0.5、权重 0.75/0.25/0.5/0.1，引入 10ms 上采样头）；SpecAugment 频率遮罩×2（≤24 bin）；采样偏向多活动说话人。

### 📊 实验结果
**数据集**：DIHARD III、CALLHOME Part 2、AliMeeting near/far、AMI MHM/SDM、NOTSOFAR-1 MHM/SC（全部计重叠，强制对齐参考标签）

**主要指标**：
- 离线（30.4s 缓冲）DER：DIHARD III 12.73 vs DiariZen 14.5、Sortformer-v2.1 19.09；CALLHOME 9.10 新 SOTA；NSF1-SC 11.00 vs v2.1 的 30.49
- 0.32s 超低延迟仍全面领先 v2.1 约 6–18 个点；30.4→0.32s 退化仅 0.79–3.53 点（优雅降级）
- 训练显存 ÷2.8、迭代 2.2× 快、推理吞吐至 6.4×（RTX PRO 5000 batch32 RTFx 高两个数量级）
- 下游：条件 DiCoW-v3.3-large 后 AMI/NSF1 单麦 tcpWER 新 SOTA，后验软条件一致性优于硬段条件（首次观察到 DiCoW 软>硬）

**是否开源**：模型权重 HuggingFace（OpenMDW-1.1 许可），训练代码在 NVIDIA NeMo Speech 仓库

### ⭐ 评分：8/10
评分理由：把"更多说话人+更细时间分辨率+更低算力"这三个相互矛盾的轴同时推进，每处取舍都有架构级理由和消融支撑，效率收益对生产极有价值；评测覆盖 8 数据集×3 延迟档且有下游 ASR 交叉验证。扣分：核心思想均在 Sortformer 框架内做增量工程化，8 说话人上限与英文/近讲数据偏重，极端流式（≤0.08s）未给出定量。

---

## [10] When Normality Shifts: Multi-Level WavLM Modeling for Open-World Audio Deepfake Detection

**arXiv ID**：2611.11465 | **方向**：语音前端

**作者**：Daniel Niekurzak, Daniel Kozuch, Weronika Folwarska, Khan Muhammad, Rafał Scherer

**机构**：切斯托霍瓦理工大学、AGH 克拉科夫科技大学、成均馆大学

**发布日期**：2026-11-08 | **论文**：https://arxiv.org/abs/2611.11465 | **PDF**：https://arxiv.org/pdf/2611.11465.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
监督反作弊器依赖已知攻击标签、易学生成器捷径。本文严格检验"只用真实语音"的免攻击协议：MLN-WavLM 在冻结 WavLM Base+ 的 6/10/14/18 层池化嵌入上各拟合一个收缩-马氏正常密度（无梯度参数、无伪造标签参与任何拟合/阈值/融合），等权融合标准化距离。2019 LA 上源域排名 EER 8.45%，紧咬同前瞻的全监督 WavLM-HM-Conformer（7.86%）；但冻结跨到 2021 DF，EER 恶化至 22.12%，且以真实样本标定的操作点在域移下失效——无标签阈值再校准在域移流上低 FPR 召回全面崩塌。结论直接：冻结正常性可完成源域排序，但不构成稳定的开放世界决策规则。

### 🔧 技术方案

**问题背景：** 攻击标签获取永远落后于新合成器；one-class 检测假设真实语音近似单高斯，而说话人/信道/编解码变异使"正常簇"本身漂移；既有 one-class 深伪工作多用可训练后端，混淆了"冻结 SSL 表征容量"与"后端表达力"两种解释。

**模型架构：** 冻结 WavLM Base+ 取 4 深度 masked-mean 池化 768 维向量；每层独立 StandardScaler→可选 PCA128→Ledoit-Wolf 协方差的马氏距离；bona fide 训练集 median/MAD 稳健层内标准化后等权平均成融合分；操作阈值=开发集真实分 99 分位。预固定对照评分器：PCA/欧氏、KNN(k=20)、RBF-OC-SVM、k-means 多中心。

**核心创新：** (1) 协议贡献：把"免攻击拟合/标定"与"有标签比较评估"在时间线上严格分离，超参与层集在见任何 2021 标签前冻结。(2) 部署流仿真：半量真实+受控流行率伪造的无标签流，对比流分位数、robust median/MAD 重锚定、oracle 三种再校准，量化污染容忍域。(3) 机理诊断：leave-one-layer-out 证明浅层（6）主导；漂移分解为排序退化与阈值失配两个正交故障面。

**训练策略：** 零梯度优化参数（MLN-WavLM 训练=拟合协方差/标准化）。2019 LA 仅用 2,580 条真实训练语音拟合；4s@16kHz 裁/补；嵌入提取单张 12GB 消费级 GPU；bootstrap 20000 次置信区间，层间相关+置换检验。

### 📊 实验结果
**数据集**：源域 ASVspoof 2019 LA eval（7355 真+63882 伪），冻结跨域 ASVspoof 2021 DF（611828 条解码成功）

**主要指标**：
- 源域：MLN-WavLM-Full EER 8.45% / AUC 0.9875 vs 全监督 WavLM-HM-Conformer 7.86%（免攻击排名接近）
- 跨域：2021 DF EER 恶化至 22.12%（约监督基线 14.94%），相对退化显著
- 阈值操作点：真实标定 99 分位在 in-domain ≤10% 污染下 median/MAD 重校准稳健，但 2021 DF 域移流重校准后低 FPR 召回崩塌；oracle 阈值行证明瓶颈在排序本身而非再校准
- 控制评分器（KNN/OCSVM/多中心）全部不及马氏等权融合；去浅层 6 即明显劣化

**是否开源**：代码/权重：文中未提供

### ⭐ 评分：6/10
评分理由：对"免攻击正常性能否开放世界部署"给出了罕见诚实、协议严谨的负结果，阈值-排序分离诊断与再校准污染实验对实际应用有直接警示价值。扣分：方法上仅是已知技术堆叠（冻结 SSL+收缩马氏+等权融合）缺乏新模型贡献，8.45% vs 7.86% 的源域胜利在跨域被 22.12% 抵消，无新数据集/没有 SOTA 竞争力，属于高质量的"证伪型"测量论文。

---

## [11] Textraction: Unified Text-Guided Speaker Extraction and Enhancement for Single- and Multi-Channel Audio

**arXiv ID**：2611.12493 | **方向**：语音前端

**作者**：Aviad Eisenberg, Sharon Gannot, Shlomo E. Chazan

**机构**：Bar-Ilan 大学、OriginAI（以色列）

**发布日期**：2026-11-09 | **论文**：https://arxiv.org/abs/2611.12493 | **PDF**：https://arxiv.org/pdf/2611.12493.pdf | **代码**：暂无 | **Demo**：https://aviad3189.github.io/Textraction/

### 📌 简介
现有文本引导提取消要 LLM 嵌入（贵）要么只支持单通道/绝对方位、无法表达 keep/remove 指令极性。Textraction 用一个统一网络覆盖单/双通道、语义/空间提示与增强任务：SC/MC 专用编码器+5 个共享 TF-Locoformer 块，提示与 SC/MC 身份经 cross-attention 注入每一层，一次前向直接输出目标，无分离-选择两阶段；文本侧用对比微调的轻量 E5-small（2.6k token）取代 LLM，显式分离"keep the loud man / remove the loud man"极性。属性提取双通道 SI-SDR 11.11 dB（单通道 10.83），空间引导仅比 oracle-DOA 的 SSF/SpatialNet 落后，增强达 18.66 dB。

### 🔧 技术方案

**问题背景：** 注册语音/摄像头/阵列几何等条件常缺失；LLM 嵌入器计算重且需 LoRA 微调；冻结 CLAP 对指令极性不敏感（keep/remove 余弦近重合）；既有工作不联合单/多通道、不支持任意 keep/remove 组合或相对空间关系。

**模型架构：** STFT RI 表示；SC 编码器（2 通道）与 MC 编码器（4 通道 RI×2 麦）各自 conv+1 个 TF-Locoformer，5 个共享 TF-Locoformer（频-时交替自注意力+卷积 FFN）+转置卷积解码；每层后 cross-attention 以条件序列（池化 E5 嵌入+token 级状态+可学习 SC/MC 嵌入，64 维、4 头）为 KV、全 TF bin 为 query，六处注入。

**核心创新：** (1) E5 triple 对比微调：Gemma3 构造"锚-改写正例-极性翻转负例"三元组、margin 0.5 triplet 损失，训练前/后 keep vs remove 余弦从 0.989 压到 0.25，随后以低 lr 随提取网络联合微调，用 52M 总参（文本编码器占 33M）替代 LLM。(2) 混合提示协议：keep-only/remove-only/both 三类 15 种改写+互补提示（同音频双目标）强制网络读文本；可分离说话人强制性别/响度属性差异。(3) 相对空间文本描述+从 4 源 PIT 分离器权重初始化共享块、交叉注意力输出层零初始化。

**训练策略：** 8kHz 仿真数据 70k/1k/1k（LibriSpeech+VGGSound，RT60 0.2–0.6s、SNR 0–20、SIR −5–15 dB、随机阵列/DOA）；损失 −SI-SDR+3.0·log-mag MSE+β_CLAP·CLIP 型 (1−cos)（β=90 仅提取任务）。

### 📊 实验结果
**数据集**：自建仿真文本引导混合数据集（测试集与训练/验证不重叠，固定种子）

**主要指标**：
- 属性提取：MC SI-SDR 11.11 dB / STOI 0.797 / WER 76.1→33.3%；SC 10.83 dB（语义提示下第二麦仅 +0.28 dB，作者如实分析）
- 空间引导提取：SI-SDR 10.53 dB，接近用 oracle DOA 的 SSF 与 oracle 置换的 SpatialNet，且无需校准
- 增强：MC 18.66 / SC 18.15 dB，与专用 TF-GridNet、HDDEMUCS-TF 相当或更优
- 提示鲁棒性：keep/remove/both 三种句式、拼写错误注入下性能基本稳定
- DNSMOS OVRL 1.61（8k 上采样协议天花板所限）

**是否开源**：示例音频见 demo 页；代码未开源

### ⭐ 评分：7/10
评分理由：统一性目标明确且达成度高（SC/MC、属性/空间/keep/remove/增强一模型），指令极性敏感的轻量对比文本编码器是有迁移价值的细节，与全 oracle 基线的诚实对比加分。不足：仅仿真 8k 数据、无真实录音与主观听测、说话人属性只到性别/响度粒度、MC 在属性任务增益有限说明空间-语义融合不深。

---

## [12] Task-adaptive anonymisation enables privacy-preserving sharing of clinical speech data

**arXiv ID**：2611.11273 | **方向**：语音前端

**作者**：Ziyun Cui, Haoyu Niu, Wen Wu, Hao Sun, Sihan Zhang, …, Ji Wu, Chao Zhang（清华/北医/协和/港理工/上海AI实验室/伦敦大学学院 多学科团队）

**机构**：清华大学电子系、北京清华长庚医院、北京回龙观医院、协和医院、港理工、上海 AI Lab、UCL

**发布日期**：2026-11-08 | **论文**：https://arxiv.org/abs/2611.11273 | **PDF**：https://arxiv.org/pdf/2611.11273.pdf | **代码**：https://github.com/JaderOx/AnonymiseAgent | **Demo**：暂无

### 📌 简介
临床语音既是数字生物标志又双重泄露隐私（声纹+所说内容），而不同病的评估依赖不同语音特性——固定匿名化流程顾此失彼。CASA 把匿名化变成任务引导的优化：LLM 控制体接收自然语言任务描述+隐私-效用要求，自主规划"声纹方法×内容脱敏"策略组合，通过递归自改进（RSI）按任务反馈迭代调整参数并将成败经验写入跨任务记忆。在 5 语言、11 个数据集 14 个临床任务（抑郁/自杀风险/AD/PD/言语障碍等）上，CASA 满足"说话人 EER≥20%、敏感内容 F1≥0.75、下游 BACC 降<3pt"三项联合标准的比例 14/14，最强固定方法仅 8/14、SecureSpeech 4/14；经验复用使新任务策略评估次数减 31.3%。

### 🔧 技术方案

**问题背景：** 通用 VoicePrivacy 类方法压制声纹同时毁掉临床相关特征；疾病专用方案互不兼容。实证发现不同匿名方法对不同疾病的影响方向不一致（声障碍对 Resyn/Neural VC 极敏感，精神/认知任务耐受高）——不存在一劳永逸。

**模型架构：** LLM 控制体 + 工具池：五种声纹匿名器（Pitch、LPCC Formant、谱缩放 Formant、Neural VC、转录-重合成 Resyn）+本地部署 Qwen2.5-32B-Instruct 的敏感内容定位与遮蔽；三维评估器（说话人 EER、敏感定位 F1、下游 BACC）驱动闭环；跨任务记忆保存粗粒度摘要+细粒度实验记录。

**核心创新：** (1) 首个把"任务属性→策略选择→参数→评估→记忆"做成 agent 回路的临床语音匿名化框架，方法选择本身成为可学习的决策变量。(2) RSI 的递归评估+经验蒸馏降低新任务搜索成本（-31.3%），支持跨语言/跨病扩展。(3) 严格隐私定义：外部攻击者设定下验证——半知情重训攻击者（VoicePrivacy 协议，均 EER 0.338 全通过）与 SALMONN-2-8B SpeechLLM 攻击者（均验证错误率 0.441），双模态攻击+本地部署防泄露。

**训练策略：** 无端到端训练，逐任务由 agent 优化（选方法、调参）；判定阈值 EER≥20%、F1≥0.75、ΔBACC<3pt 三标准联合；显著性用单侧精确二项检验；临床专家盲评可用性。

### 📊 实验结果
**数据集**：11 个临床语音数据集/14 任务：MODMA、Androids-Corpus(访谈/朗读)、Suicide-YF(1223人)、Crisis、NCMMSC-AD、ADReSS、Ivanova、NeuroVoz、ENNI、Saarbrücken×3 亚型、PUMCH 腭裂，中英意西德 5 语言

**主要指标**：
- 联合达标率：CASA 14/14 vs 最强固定方法 8/14 vs SecureSpeech 4/14；ΔBACC 全任务优于 SecureSpeech
- 敏感内容定位：F1 0.861 vs SecureSpeech-NER 0.570（Crisis热线）、0.914 vs 0.343（PUMCH）
- 抗重识别：半知情攻击者 EER 0.338（全部达标）、SpeechLLM 攻击错误率 0.441
- RSI 经验迁移：新任务策略迭代次数 −31.3%
- 机理分析：5 种声纹方法在 EER-F0 保持(ΔPCC)-临床敏感度上互相权衡（Resyn 语音障碍任务近随机、Formant 保真最好但最弱 EER）

**是否开源**：控制体/工具链代码开源 @ https://github.com/JaderOx/AnonymiseAgent（临床数据含自建数据集不外发）

### ⭐ 评分：8/10
评分理由：问题真实（多中心临床语音共享的合规瓶颈）且被系统解决，任务级实证刻画了"匿名强度-各病效用"非单调权衡，14 任务 5 语言的评测广度+双攻击者设定+真临床专家盲评在同类工作中罕见；RSI 的经验复用效率提升有量化证据。扣分：方法核心是 LLM 编排既有匿名器、语音层无新模型，agent 成本与可复现性依赖 LLM 版本，自建数据集使部分结论无法外部复算。

---

## [13] Towards Trustworthy Mobile Speech Interaction: Ensuring Voice Authenticity and Transmission Integrity

**arXiv ID**：2611.11777 | **方向**：语音前端

**作者**：Guodong Liu, Lei Wang, Dongxu Liu, Qianran Qiao, Haipeng Dai, He Huang, Guihai Chen

**机构**：南京大学、苏州大学（发表于 IMWUT/UbiComp）

**发布日期**：2026-11-09 | **论文**：https://arxiv.org/abs/2611.11777 | **PDF**：https://arxiv.org/pdf/2611.11777.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语音克隆让"声纹=身份"的移动端认证体系失效，现有音频水印多为离线、只管内容不管"是否真人当场说的"。MoBiMark 是首个把超声声道生物特征与语音水印结合的在线实时系统：手机听筒发射不可闻多频超声探针，录音麦克风接收声道路径回波，回波动态特征与语音内容嵌入融合生成双层动态水印（系统持久 UID+逐句 SID），联合训练的嵌入器/检测器在完成采集时嵌入水印。50 用户×4 机型、25 h 正样本+290 h 攻击样本上，源级攻击平均检出 99.59%、传播级 99.91%（合计 99.79%），INT8 量化模型 58.8 MB、延迟最大 −72%，感知质量几乎无损。

### 🔧 技术方案

**问题背景：** 内容水印可被私有模型去除/重打；静态水印缺活体绑定；离线防护赶不上"边说边的伪造"；防御需在无专用硬件、端侧算力受限条件下闭环"信源真实性+传播完整性"。

**模型架构：** 超声编码器编码声道回波（多频探针经听筒发射、麦克风阵列采集），语音编码器出内容相关嵌入；用户验证模块融合两者→双层动态编码（UID 持久+SID 随语音内容逐窗口更新，20 ms 步进/1 s 窗口）；Speech Stabilizer（降噪+增强）同时接在嵌入端与检测端对齐特征分布；嵌入器-检测器联合训练（AudioSeal 协议），QAT+INT8（权重对称/激活非对称）端侧部署。

**核心创新：** (1) 首次把超声 articulatory 生物特征作为水印生成条件，伪造语音无法与真实声道回波建立一致跨模态对应，从"检测伪影"转为"绑定物理信源"。(2) UID×SID 双层动态水印同时覆盖源级攻击（重放/克隆/自适应模仿）与传播级攻击（删改/拼接/挪用）。(3) 帧序调整策略+外部稳定器抵抗良性信道扰动，使水印比特鲁棒。

**训练策略：** 全系统 QAT 微调 200 epoch、AdamW、batch 64、QNNPACK 后端；损失沿用预训练目标；FP32 170.66 MB→INT8 58.83 MB（−65.5%）；正样本准确率 93.15%（双模态联合较单超声+33.15pt），AUC 0.9630、EER 0.055%；1s 短窗口下仍 89.57%。

### 📊 实验结果
**数据集**：自建 50 志愿者语料：25 h 正样本+290+ h 攻击样本（Samsung S10/S22 Ultra、vivo X200 Pro、OnePlus 15 四机型）

**主要指标**：
- 源级攻击（重放/克隆/联合攻击）平均防御 99.59%；传播级（片段编辑/删除/拼接/水印挪用/伪造）平均 99.91%；最难 P1/P2 编辑下水印相似度降至 76.59%/81.02%（真人 99.73%）
- 感知与可懂度：SI-SNR/PESQ/ViSQOL/STOI 按 AudioSeal 协议接近未加水印（INT8 vs FP32 仅微退化）
- 鲁棒性：重采样/转码/压缩与删除/静音攻击下 FP32/INT8 成绩相当；距离 10–25 cm、角度 ±20° 稳定 ≥87.5%
- 端侧：INT8 延迟 −71.9%、功耗 −19.35%，满足实时通信

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：方向开辟性好（生物特征绑定时实水印），跨模态一致性验证思路天然抗新一代克隆，真实手机+真实受试者+双类攻击面的评测体量与部署数据（模型体积/延迟/功耗）完整，是 IMWUT 级别的系统贡献。扣分：语音技术内核薄（超声传感成熟、水印侧沿用 AudioSeal 框架）、正样本 93% 级识别与"99.79%"防御率不在同一口径且未讨论阈值-代价权衡、未开源、超声在嘈杂开放环境/非近距离姿态的适用边界未验证。

---

## [14] Virtual-Flow: Virtual Microphone-based Speech Enhancement via Semi-supervised Flow Matching

**arXiv ID**：2611.11130 | **方向**：语音前端

**作者**：Dongheon Lee, Ashutosh Pandey, Sanjeel Parekh, Zhaoheng Ni, Daniel Wong, Jacob Donley, Buye Xu, Juan Azcarreta

**机构**：KAIST、Meta Reality Labs Research

**发布日期**：2026-11-08 | **论文**：https://arxiv.org/abs/2611.11130 | **PDF**：https://arxiv.org/pdf/2611.11130.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
虚拟麦克风估计（neural-VME）想用小型阵列等效大阵列，但监督式扩展需要每个虚拟位真值、数据集随 VM 数爆炸。Virtual-Flow 把 VME 建成条件 flow matching 生成任务并只依赖伪目标：利用"直达路径语音在 RM 间只是时延叠加"这一先验，用激励语音估计各 RM 时延、在 μ±3σ 等距网格取虚拟时延、生成 RM 时移相干叠加的伪 VM 谱，配合真实 4-rm 输入监督波束形成损失。16 通道全向阵列中任意 4 麦生成 12 路 VM+MVDR/MCWF 后端，VM-BF PESQ 2.74(有监督)/2.79(半监督)，超过有真值的 GAN 式 Spatial-Magnifier（2.61）；16 物理麦 2.82 的性能被 4 麦系统逼近；reflow 蒸馏后单步 NFE、7.8 G MAC/s 低于多数生成式基线 0.8–4.8T 数个量级。另有真实录音、实时因果、阵列无关扩展。

### 🔧 技术方案

**问题背景：** 消费设备麦数≤4 限制空间分辨率；已有 VME 单 VM 或需真值多 VM；判别式网络难当生成任务、GAN（Spatial-Magnifier）训练不稳且仍要目标；大规模 VM 数组的最优排布无解。

**模型架构：** 双支路：轻量 Spatial-Magnifier（分组卷积压缩通道+去选道模块）作引导先验出初版 VM，PeriodWave-VME（周期分段并行共享参数 U-Net+瓶颈后多带 MB 块融合引导线索）预测 STFT RI 向量场，沿概率路径 ODE 积分；生成 VM 与 RM 拼成 16 通道→冻结预训练 MC-SE（SpatialNet-small）估协方差→MCWF/MVDR 波束形成。"半监督"定义：无 VM 真值，仅用含噪 RM+训练期激励/干净参考；推理只需 RM。

**核心创新：** (1) 延迟空间伪 VM 目标：x̃_v=Σa_i^x SFTTx_i(t+τ_i) 由激励-时延互相关构造，免除几何仿真真值，等距 τ 网格+无位置重叠约束，且仅在相位相关成立的直达路径维度近似——残余由 BF 端到端损失继续修正。(2) 半监督 SARL-S：先训 4 通道 MC-SE、再把编码器卷积核换成 16 声道、分隔器/解码器热启动，解决 SARL 需预训练多麦 SE 的鸡生蛋问题。(3) reflow 蒸馏拉直概率路径实现 1-NFE 推理，引导线索训练/推理同现避免域差；固定权重 0.3·log-λCFM+0.7·SNR-BF 联合优化，训练时整条 ODE 可微回传。

**训练策略：** DNS-2020 语音/噪声重建：5 万/2 千/3 千 10s 片段，Pyroomacoustics RT60 0.2–0.6 s、SNR 0–20/SIR −5–15 dB，干扰人≤5、FoV 60°；16 麦球阵取 4 麦四面体为 RM；16 kHz、STFT 16/8 ms；32×H100、Adam lr 1e-4、100 epoch×两阶段、批 64。

### 📊 实验结果
**数据集**：DNS-Challenge 仿真多说话人混响数据集（+附录真实录制实验）

**主要指标**：
- VM-BF PESQ（4麦生成12虚拟麦）：半监督 Virtual-Flow 2.79±0.02 > 有真值的 Spatial-Magnifier 2.61±0.06、FlowSE 2.40、SGMSE+ 2.38；SI-SDR 10.3 dB vs 未处理 −11.4
- 上界差距：16 物理麦 SpatialNet-MCWF PESQ 2.82，4 麦+生成即逼近 4×硬件；半监督超自身有监督版（2.79 vs 2.74）
- 复杂度：+13.1 M 参数、7.8 G MAC/s，比 FlowSE（0.8T）/SGMSE+（4.8T）低 100×+，比 ArrayDPS（405M/2.5T）低更多；reflow 后单步
- 消融：去半监督伪目标 9.2 dB→有伪目标 10.3 dB；学习权重反而崩到 6.5

**是否开源**：暂无（Meta 研究院工作）

### ⭐ 评分：7/10
评分理由：把"需要逐 VM 真值"变成"只需时延先验伪目标"是聪明且可推广的松弛，机理分析（VM 增益源于强化空间滤波而非隐式去噪）与大量附录实验（不同阵列几何/波束器/真实录音/实时因果版）充分，半监督反超监督是有说服力的细节。扣分：全虚拟位置受限于时延空间、无端到端可微阵列构型寻优、依赖 32 卡训练、生成式 VME 的高频幅相伪影仅由 STFT 指标间接覆盖，代码未开。

---

## [15] BAmbiDrop: Array-Agnostic Speech Enhancement with Zero-Shot Binaural Reproduction using Multi-center Ambisonics Encoding

**arXiv ID**：2611.10561 | **方向**：语音前端

**作者**：Michael Tatarjitzky, Vladimir Tourbabin, Boaz Rafaely

**机构**：本古里安大学、Meta Reality Labs Research

**发布日期**：2026-11-07 | **论文**：https://arxiv.org/abs/2611.10561 | **PDF**：https://arxiv.org/pdf/2611.10561.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
阵列无关增强网络（AmbiDrop）只出单通道，而双耳增强方法只适配固定器件几何。BAmbiDrop 利用"球谐/ Ambisonics 原点可平移到空间任意点"的性质，把冻结的 AmbiDrop 网络在阵列每个麦克风位置各平移一次原点、估计一组复掩码，融合成全阵共享掩码后作用于原始麦克风信号，最后用固定 BSM 滤波器渲染双耳——任何阵列免重训直接支持双耳输出。21 种自由场/刚性球阵列平均：共享掩码融合版全面优于逐麦独立掩码——SI-SDR −0.30 dB、PESQ 1.62、且 IC/ILD/SI-SDR-Dir 同时更好，证明掩码融合既增强又保双耳线索；直接麦域训练的 MIMO 基线全面崩溃（SI-SDR −6.1），凸显 Ambisonics 域的几何无关优势。

### 🔧 技术方案

**问题背景：** 学习类双耳增强要么学死某一族阵列的渲染器、要么每麦独立掩码破坏 BSM 依赖的通道间相干性；现有阵列无关方法（TAC/跨道注意力/AmbiDrop）只给单通道结果。

**模型架构：** 管道：麦克风信号→以第 μ 个麦为原点的对齐 ASM 编码（正则最小二乘，平面波幅度仅相位平移、SH 矩阵不变）→冻结 AmbiDrop（2 层 64 单元 BLSTM+复掩码头，仅 142,594 参数，理想 3 阶 Ambisonics+最多 3 通道 dropout 训练，训练参考改为混响目标人而非直达声以保外部化线索）→得 Nμ 个逐麦掩码→复数均值融合为共享掩码→掩码乘各原始麦信号→固定 BSM（≥分频点用幅值最小二乘）合成双耳，Neumann KU100 HRTF 参考。

**核心创新：** (1) 多中心 Ambisonics 编码：原点重定位只需把传播项折进平面波幅度（exp 项精确相消），因此同一网络可"移动视心"逐麦出掩码，零额外训练/参数。(2) 融合假设的验证：独立掩码给增强留更多自由度，但同时破坏 BSM 的通道关系先验（SI-SDR-Dir −3.23 dB vs 融合 +0.69）；复均值共享掩码反而两头都赢。(3) 变体矩阵（Fusion/Center/Per-Mic/MIMO×2）系统分离"原点位置"与"掩码共享"两因素。

**训练策略：** 无训练：完全复用已发表 AmbiDrop 权重与超参（dropout≤3 通道、p=0.2、STFT 20 ms Hamming 50%），BSM/ASM 各阵列设计一次即复用；WSJ0 干净语音+1+5 干扰人、20 个仿真阵列+模拟 Aria 眼镜阵列的 100 条/阵列测试集。

### 📊 实验结果
**数据集**：21 种仿真阵列（线性/平面/体分布，<10 cm 球内，自由场+刚性球，含 Aria 眼镜模型）100×21 条测试样本；参考为 KU100 双耳

**主要指标**：
- Fusion（主推）：21 阵列上平均 SI-SDR −0.30 dB、PESQ 1.62、STOI 0.785、SI-SDR-Dir +0.69 dB——除 IC 外全列最佳并居中于参考 BSM Clean（2.25/3.69）
- Per-Mic：SI-SDR −2.51 dB、SI-SDR-Dir −3.23 dB、IC 与 ILD 同时劣化；Center 单掩码略逊于 Fusion
- MIMO FT-JNF（麦域直训基线）：SI-SDR −6.13、−7.16 dB，跨全阵列不泛化
- 头/耳三中心附加掩码并入平均仅 +<1 dB，故舍弃；论文自认所有方法 SI-SDR 绝对值偏低

**是否开源**：暂无

### ⭐ 评分：5/10
评分理由："Ambisonics 原点平移免重训得到逐麦掩码、复均值融合护住双耳线索"这一观察优雅且经 21 阵列消融验证，负结果（Per-Mic 破坏 SI-SDR-Dir、MIMO 基线崩溃）诚实。但方法为纯推理时组合、无新模型，142k 参数 BLSTM 表达力弱，仿真 6 kHz 级 WSJ0 条件下各项绝对指标与 BSM Clean 差距大、无语音失真之外的主观听测，属会议短文级增量工作，参考"域无关掩码复用"思路即可。

---

## 附：抓取失败清单

无。本批次 15 篇 arXiv HTML 全文均抓取解析成功。

---

*Generated on 2026-11-10*
