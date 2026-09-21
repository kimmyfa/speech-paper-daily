# 2026-09-18 语音论文速递

**共收录**: 17 篇 | **语音大模型**: 15 篇 | **语音前端**: 2 篇

> 目标日期 2026-09-18（北京时间）arXiv 语音相关论文共命中 17 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] Alignment-Path Distillation from Non-streaming ASR-LLMs for Streaming Speech Recognition

**arXiv ID**：2609.20121 | **方向**：语音大模型

**作者**：Yan Jia、Kai Huang、Junjie Chen、Feng-Long Xie、Xu Tang、Yao Hu

**机构**：Xiaohongshu Inc.（小红书）

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.20121 | **PDF**：https://arxiv.org/pdf/2609.20121.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对交错式流式 ASR-LLM 中外部 CTC 强制对齐（FA）构造的语音-文本训练序列与 LLM 自身学到的对齐分布不一致的问题，本文提出"对齐路径蒸馏"框架：从冻结的非流式 ASR-LLM 教师提取文本-语音注意力，低置信行回退为 FA 分布，再经全局单调搜索得到对齐锚点以重构学生交错训练序列，并叠加 logit 与隐状态蒸馏。中英文 6 个测试集上，仅用教师对齐路径即取得 5.2% 相对错误率下降（9.35%→8.86%）；完整框架达 7.80%，较无蒸馏 FA 训练相对降低 16.6%。

### 🔧 技术方案

**问题背景：** 交错式流式 ASR-LLM 中文本 token 分配到哪个音频块决定其可获得的声学上下文，传统做法依赖外部 CTC 模型 FA 时间戳切分转写，但该对齐与 LLM 内部注意力学到的对齐不一致，限制了流式识别精度。

**模型架构：** 学生为流式 Conformer 编码器+下采样 projector+Qwen2-1.5B，音频按 240ms 分块构成 [a1,y(1),…,aK,y(K)] 交错序列，beam search 解码且每块最多输出 7 个文本 token；教师是同结构的非流式模型（编码器/projector 由 FireRedASR2S 预训练参数初始化）全程冻结。取教师最后一层全头平均注意力在音频位置 softmax 得对齐矩阵，据此重构学生训练序列；教师与辅助模块仅训练期使用，推理为纯流式学生。

**核心创新：** (1) 置信度 FA 回退：注意力峰值概率低于阈值 0.30 时用 FA 分布替换该 token 行（训练数据中 59.44% 单元触发回退），避免嘈杂条件与英语虚词注意力弥散导致对齐失效，无回退时总错误率从 8.86% 恶化至 11.55%。(2) 全局单调锚点搜索：借鉴 Glow-TTS，以动态规划对全部文本单元联合求解单调约束下的最大对数和路径，借助前缀最大值实现 O(UF) 复杂度，避免逐峰独立选择的非单调与误差传播。(3) 分层蒸馏：logit KD（温度 τ=2 的 KL）对齐一对一目标 token 预测位置，隐状态 KD 在 {7,14,21,28} 层各配训练期双向辅助解码块后做余弦匹配，提供对齐之外的全上下文监督。

**训练策略：** 总损失 L_CE+λL_logit+hL_hid，TA+COMBO 取 λ=0.05、h=1.0；32 GPU 训 5 epoch，Adam 初始学习率 1e-3、plateau 调度、梯度裁剪 5、音频预算 90 秒/批；训练数据为 AISHELL、WeNetSpeech、LibriSpeech、GigaSpeech、KeSpeech，FA 标签用 MMS 多语言强制对齐器生成。

### 📊 实验结果
**数据集**：训练含中英文五套数据（约数万小时）；评测为 AISHELL test、KeSpeech test、WeNetSpeech test-net/test-meeting、LibriSpeech test-clean/test-other（中文 CER、英文 WER）

**主要指标**：
- 汇总错误率：非流式教师 3.99%，FA 基线（MMS）9.35%，教师对齐 TA 8.86%（相对降 5.2%）
- 完整框架 TA+COMBO 7.80%，较最强基线 MMS+COMBO（8.12%）相对降 3.9%，较无蒸馏 MMS 相对降 16.6%
- 流式行为：TA+COMBO flicker 3.18% 高于 MMS+COMBO 的 2.49%，平均发射延迟 128.3ms 与基线 127.3ms 相近

**是否开源**：暂无代码、模型或 Demo 发布

### ⭐ 评分：7/10
评分理由：将教师注意力对齐路径作为可蒸馏对象并配套回退与单调搜索，切入点新颖，消融覆盖各组件且中英文 6 测试集结果一致，属实质贡献。但绝对提升有限，教师对齐版 flicker 反而更高且未解决，与教师差距仍大；工业团队未开源，复现门槛偏高。

## [2] Decaf: A privacy preserving speech codec using speaker disentanglement and canonical voice conversion

**arXiv ID**：2609.19304 | **方向**：语音大模型

**作者**：Md Shakhrul Iman Siam、Dushyant Sharma、Stanislav Yu. Kruchinin、Peter Skala

**机构**：Ohio State University；Microsoft Health & Life Sciences AI

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.19304 | **PDF**：https://arxiv.org/pdf/2609.19304.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对语音上云传输中的说话人身份泄露问题，提出隐私保护神经语音编解码器 DECAF：把压缩本身作为混淆机制——发送端经 CTC 监督的信息瓶颈将语音剥离为无说话人内容嵌入，RVQ 量化后仅传内容流；接收端用两端预共享的 canonical 音色重建波形，实现确定性匿名。论文引入 CTC 辅助目标并发现 WavLM-base+ 优于 WavLM-large 且推理提速 3 倍。0.5 kbps 下对 ECAPA-TDNN 攻击达 EER 43.5%，微调 Whisper-medium 后平均 WER 5.49%，较 SOTA 相对降低 33.2%。

### 🔧 技术方案

**问题背景：** 语音上云需在保可懂度下隐藏说话人身份，现有信号处理、VC、对抗扰动及神经编解码匿名方法均把"先混淆、后编码"当作两个独立阶段，带宽成本付两次，且隐私-效用此消彼长，现有匿名系统即使高码率也带来数个百分点绝对 WER 退化。

**模型架构：** DECAF 由说话人解耦模块（SDM）、神经音频编解码器（NAC）、波形生成器与 canonical 说话人嵌入组成。SDM 沿用 FreeVC 骨架：WavLM 前端、WaveNet 瓶颈抽取器把 SSL 特征压至 192 维高斯后验，维度落差构成信息瓶颈以丢弃音色；说话人编码器仅在训练期使用。NAC 为线性编码+RVQ+线性解码，码本 1024，量化器数随码率调节（0.5–24 kbps）。接收端以归一化流+HiFi-GAN 结合固定 canonical 音色（取自 LibriSpeech 一条嵌入）重建波形，无任何说话人信息上链。

**核心创新：** (1) 将压缩融入混淆：只传内容流，带宽只付一次，瓶颈维度从架构上封顶可泄露的说话人信息，隐私成为编解码器固有属性。(2) 在 FreeVC 解耦目标上增设 CTC 辅助损失，内容嵌入接 6 层 8 头 transformer 预测转写，强迫特征经量化后仍保持音素判别性。(3) 系统发现更小的 WavLM-base+ 反优于 large 版本（匿名与 WER 均更好），并带来 V100 上 3 倍推理加速。

**训练策略：** SDM 与波形生成器联合训练于 VCTK，lr 2e-4、450k 步、batch 64，生成器损失=mel L1 重建+KL+对抗+特征匹配+CTC。NAC 在 LibriSpeech 960 小时上以冻结 SDM 输出为输入训练 20 epoch，lr 1e-4、batch 64，总损失=L2 重构+0.25×RVQ commitment。ASR 端在 DECAF 解码音频上微调冻结的 Whisper-medium。

### 📊 实验结果
**数据集**：VCTK（SDM 训练）、LibriSpeech 960 小时（NAC 训练与评测，test-clean/test-other，16 kHz）

**主要指标**：
- EER（ECAPA-TDNN 攻击）：DECAF-small@0.5 kbps 平均 43.5%，Encodec@24 kbps 仅 16.4
- 微调 WER：平均 5.49%（clean 2.85/other 8.13），与原始音频差距 ≤1.8 个百分点
- 音质：0.5 kbps PESQ 1.58/STOI 0.89；24 kbps 达 4.57/1.0
- 关键对比：SOTA 匿名系统需 256 kbps、平均 EER 45.5% 但 WER 12.47%；DECAF 以约 1/500 码率实现相对 WER 降 33.2%

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：将混淆与编码统一为 content-only 传输+canonical 重建的新管线思路清晰，瓶颈维度封顶信息泄露具架构原则性，"小模型更优"与 CTC 辅助目标有实用价值；多码率、多指标实验较充分。不足在仅英文数据、单一 ASV 攻击者、固定 canonical 音色影响自然度、无主观评测且未开源。

## [3] Multimodal Conversational Context for LLM-Based ASR: Data Construction, Training, and Benchmark

**arXiv ID**：2609.19765 | **方向**：语音大模型

**作者**：Longhao Li、Jian Tang、Yuxiang Kong、Jie Chen、Binbin Zhang、Lei Xie、Xiangang Li

**机构**：阿里巴巴 Token Foundry（Qwen 团队）

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.19765 | **PDF**：https://arxiv.org/pdf/2609.19765.pdf | **代码**：https://github.com/llh666521/MM-ContextASR | **Demo**：暂无

### 📌 简介
针对上下文 ASR 仅依赖历史文本转录、易传播识别错误且丢弃发音/说话人信息的问题，提出面向 LLM-ASR 的多模态对话上下文框架：以实体池为起点构造近音混淆对并生成五类受控场景对话，将历史用户语音与助手文本响应交织后做 SFT，使模型在当前轮转录中同时利用语义与声学线索；并发布 MM-ContextASR Bench。在 Qwen3-Omni 与 Step-Audio-2-mini 上，Speech+Text 取得最高整体实体召回（87.84%/85.20%），并在口音方言与目标说话人 ASR 上验证历史语音价值。

### 🔧 技术方案

**问题背景：** 上下文 ASR 传统上依赖热点词或历史转录文本，历史 ASR 错误会经助手响应复用而在上下文中传播，且文本化丢弃发音、口音、说话人特征；现有工作缺乏对多模态对话历史的系统性受控评估与训练方案。

**模型架构：** 以 LLM-ASR 为基座，共享语音编码器与模态适配器将历史与当前语音映射入 LLM 嵌入空间；输入按对话顺序序列化任务指令、历史用户语音（及可选 ASR 假设）与助手文本响应，再接当前语音，仅对当前轮转录生成。定义四种匹配上下文：No Context、Text-only、Speech-only、Speech+Text，当前音频与目标转录固定以隔离模态贡献。基座为 Qwen3-Omni-30B-A3B-Instruct 与 Step-Audio-2-mini。

**核心创新：** (1) 场景受控数据管线：从约 17.5 万实体出发用声调无关拼音索引构造近音混淆对，由 LLM 生成 Irrelevant/Implicit/Explicit/Correction/Repeated Error 五类历史场景，Qwen-Audio TTS 合成并经 Paraformer 转录+CER 过滤，产出约 87.3 万训练样本。(2) 多模态上下文训练：交叉熵仅监督当前轮转录，历史与指令位置 mask，各配置训练独立 LoRA。(3) MM-ContextASR Bench：250 实体×5 场景共 1250 例、留出集不与训练重叠，以实体召回统一度量上下文理解与错误纠正。

**训练策略：** LoRA（rank 64、alpha 128）微调注意力投影，冻结语音编码器与适配器；学习率 1e-5，有效批 64，最大序列长 8192；MM-ContextASR 与 KeSpeech 训 1 epoch，CV-Yue 与 AliMeeting 训 5 epoch；ms-swift 框架、8 张 A100；AliMeeting 另构造 8 万训练段。

### 📊 实验结果
**数据集**：MM-ContextASR Bench（1250 例，中文）、KeSpeech（官方测试 19k 句）、CV-Yue（3.5k 句）、AliMeeting（2.8k 重叠远场段）；语音 24kHz 合成降至 16kHz

**主要指标**：
- 整体实体召回：Qwen3-Omni Speech+Text 87.84%，Step-Audio-2-mini 85.20%
- Repeated Error 场景：Speech-only 82.80% 显著高于 Text-only 77.20%；训练后 Speech+Text 比无上下文基线高 5.60/9.20 个百分点
- KeSpeech：Speech+Text CER 4.17%（Text-only 4.40%）、召回 84.93%；CV-Yue CER 3.74%
- AliMeeting：Context SFT 后 Speech-only CER 24.59%、Speech+Text 24.80%，对比 No Context 30.25%、Text-only 29.60%
- 关键对比：多说话人重叠远场下历史语音带来 5 个百分点量级 CER 改善，远超纯文本上下文

**是否开源**：是，基准数据与评测代码发布于 GitHub

### ⭐ 评分：7/10
评分理由：将"历史语音入上下文"这一被低估的信息通道系统化，数据管线与受控基准设计严谨，五场景可分离度好，跨口音/方言/目标说话人验证一致有效；不足在仅单轮历史、基座与对比方法较少、数据由 TTS 合成，真实对话泛化性待验证。工程可复现性强，有实质推动价值。

## [4] Multi-Dimensional Prosody Judgment For Live Streaming Speech Synthesis

**arXiv ID**：2609.20124 | **方向**：语音大模型

**作者**：Zifan Guan、Longyu Lu、Junan Zhang、Zhizheng Wu、Meiguang Jin、Junfeng Ma

**机构**：香港中文大学（深圳）；阿里巴巴淘天集团 TaoLive-AIGC 团队

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.20124 | **PDF**：https://arxiv.org/pdf/2609.20124.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对直播场景 TTS 需评估情感、语调、能量等高表现力韵律、而传统 MOS 模型失效且 Gemini 等闭源大模型成本过高的问题，提出从 Gemini 蒸馏到 Qwen3-Omni 的成对评审模型 LPJ，定义直播韵律七维准则。针对多维评审中所有维度盲目对齐整体偏好的"判定耦合"缺陷，进一步提出 D-LPJ：去除整体判定目标、按维度掩码不确定标签、并用 span-local GRPO 将各维度优势只回传到对应推理片段。10 样本推理的 LPJ 逐集点准确度超过单次 Gemini 调用，Best-of-8 选出的候选 85.29% 落入人类前三。

### 🔧 技术方案

**问题背景：** 直播 TTS 需衡量流畅度、语调、情感、带货表现力等细粒度韵律，参考无关 MOS 回归模型无法捕获交互模式切换等复杂现象；现有 SpeechJudge、GSRM 评审不含直播域，直接调用 Gemini 无法承担大规模推理与 RL 反馈开销。

**模型架构：** 评审任务为给定同文本两条音频，对每个维度输出推理文段与 1–10 分，按分数差符号给出 A/Tie/B 判定。准则含 4 个恒评核心维度（流畅自然、语调变化、情感表达、直播表现力）与 3 个文本触发的条件维度（关键信息重音、情绪切换、交互模式切换）。基座为 Qwen3-Omni 挂 LoRA；D-LPJ 仅输出核心四维，整体判定交由外部加权聚合。

**核心创新：** (1) 交换一致蒸馏与课程学习：教师对每对样本双向评分后映射回物理音频，仅保留 4–0 完美一致结果并平衡胜者位置，课程从人 vs TTS 过渡到跨模型、同模型对比。(2) 按维度监督与掩码：对每个核心维度单独查询 Gemini，pair-维度粒度保留可靠标签，不确定维度置零损失而不丢弃整对样本。(3) span-local GRPO：每维奖励独立组内归一化，token 级优势只作用于对应维度推理片段，避免维度间奖励互相抵消。

**训练策略：** LPJ 用 rank-32 LoRA；D-LPJ 两阶段 SFT 用 rank-64 QLoRA、学习率 5e-5、分别 8/14 epoch、批大小 1+8 步梯度累积；GRPO 组大小 8、学习率 1e-5、reverse-KL 系数 0.04、3 epoch。SWIFT 框架、bf16、4 张 72GB GPU，固定单一种子。

### 📊 实验结果
**数据集**：内部人工标注直播语料，主套件 1,043 对（135 说话人，5–30 秒，每对共享文本）+222 对 IndexTTS2 vs FireRedTTS 迁移集+140 对多维人标测试集；数据不公开

**主要指标**：
- 人类标签一致率（10 样本）：LPJ v1+GRPO 71.22–83.50%，全部超过单次 Gemini（58.00–73.33%）
- D-LPJ 四维池化一致率 86.10%，比单次 Gemini 高 7.45 点
- 位置偏差：LPJ 二槽加分差仅 +0.012（SpeechJudge-GRM 为 +0.978）
- 防坍缩：耦合 LPJ 非一致判定 0/140，D-LPJ span-GROI 达 100/140
- Best-of-8 锦标赛：Hit@1/2/3 为 72.06/77.94/85.29%（随机基线 12.5/25/37.5%）

**是否开源**：暂无（代码与数据均未发布，音频因版权限制不重新分发）

### ⭐ 评分：7/10
评分理由："判定耦合"现象的识别与"去整体目标+按维度掩码+span-local GRPO"解耦方案具实质新意，蒸馏后小模型点准确率超越单次 Gemini 且位置偏差近零，Best-of-8 验证实用价值。但全部实验基于内部数据、单一种子，统计显著性不足，也尚未用维度奖励实际优化 TTS，贡献偏工程闭环。

## [5] CoReLoop: Parameter-Efficient Controlled Recurrent Refinement for Audio Deepfake Detection

**arXiv ID**：2609.19818 | **方向**：语音大模型

**作者**：Kunyu Feng、Yuxiang Wang、Li Wang、Wan Lin、Zhizheng Wu

**机构**：香港中文大学（深圳）、Amphion Technology Co., Ltd.

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.19818 | **PDF**：https://arxiv.org/pdf/2609.19818.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对音频深伪检测器对未见攻击泛化差、扩充攻击数据不现实的问题，提出 CoReLoop：在不改动冻结 SSL 检测器（W2V-BERT 24 层、598M 参数）任何原始参数、不新增数据的条件下，通过受控循环精炼让多次编码器前向真正提升检测。作者先诊断出朴素递归复用会把 pooled EER 从 4.85% 恶化至最高 64.68%，进而用 LoopBridge、循环专属 LoRA、UpdateGate 与 ExitBridge 约 10M 可训练参数实现受控递归。14 个跨域测试集上双趟将 pooled EER 降至 3.74%（相对降 22.9%），可选 halting head 以平均 1.18 趟达到 3.73%。

### 🔧 技术方案

**问题背景：** SSL 编码器加分类器的深伪检测器在未见攻击上泛化有限，而已有循环深度方法假设共享层可端到端训练，直接套用冻结检测器会因输入输出空间错配导致性能崩塌。

**模型架构：** 检测器分解为声学前端、编码器核心与池化分类模块，全部冻结；第一趟完全等同基线。T≥2 时 LoopBridge 以前端特征 h0 为 Prelude 锚点，将上一趟端点偏差经轻量投影映射回核心输入空间，并由 anchor bank（第 6/12/18/24 层）配合 AnchorReader 提供上下文；编码器注意力与 FFN 上施加循环专属 LoRA（r=8、α=16），UpdateGate 输出句级 sigmoid 门控混合新旧状态，ExitBridge 残差对齐冻结分类器；halting head 逐句选择 1–3 趟深度。

**核心创新：** (1) 受控递归输入构造：LoopBridge 以固定声学锚点条件化残差注入，消融显示移除后 EER 从 3.74% 回退到 4.56%、接近朴素递归，是增益关键。(2) 分布对齐的循环适应：共享低秩因子加步长乘数，配合门控状态更新与 ExitBridge 输出对齐，保证首趟预测严格不变。(3) 自适应停机训练：以 δ=0.01 的逐深度 BCE 差构造继续标签，逆频率加权 BCE 与期望损失项缓解全深度监督与序贯推理的失配。

**训练策略：** 仅训练新增模块与 LoRA，使用原始数据，每 batch 均匀采样 T∈{2,3}，对终态预测做 BCE；AdamW、lr 1e-4、batch 32、10 epoch；基线检测器先经 30 epoch BCE 训练后冻结。

### 📊 实验结果
**数据集**：14 个公开语音数据集官方训练集训练（ASVspoof 2019 LA、ADD 2022/2023、DFADD、AISHELL-3 等，16 kHz），按 Speech DF Arena 的 14 个跨域测试集评测

**主要指标**：
- Pooled EER（T=2）：3.74%（基线 4.85%，相对降 22.9%，10/14 测试集改善）
- 单趟 LoRA 对比 4.24%：CoReLoop 优 0.5 点，证明增益来自递归模块而非 LoRA 本身
- 自适应 halting：3.73%@平均 1.18 趟，较固定双趟降 44.5%、核心评估省 41%
- 多 seed：固定 T=2 为 3.81±0.07%；3–24 层骨干均获 0.61–1.51 点改善；Oracle 停机 3.39% 提示仍有空间

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：朴素递归失效的诊断实验扎实，组件消融与三种子、跨骨干验证充分，冻结检测器上零数据增补即获 22.9% 相对 EER 下降，参数效率与自适应推理实用性强。不足在增益绝对值偏小、第三趟收益递减、halting 距 oracle 仍差，属组合式迁移而非全新范式。

## [6] PersianVox: A Prosody-Aware Approach for Speech Dataset Generation from In-the-Wild Data

**arXiv ID**：2609.19324 | **方向**：语音大模型

**作者**：Saeedreza Zouashkiani、Soheil Khalesi、Saman Soleimani Roudi、Sajjad Amini、Shahrokh Ghaemmaghami

**机构**：谢里夫理工大学电子研究所（伊朗）

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.19324 | **PDF**：https://arxiv.org/pdf/2609.19324.pdf | **代码**：https://huggingface.co/datasets/saeedzou/persianvox | **Demo**：https://saeedzou.github.io/persianvox-demo

### 📌 简介
针对低资源语言缺少大规模高保真语音数据、现成 in-the-wild 流水线用单模型 ASR 加静音 VAD 切分导致转写错误与韵律截断的问题，提出全自动数据生成流水线 PersianVox。核心是韵律感知切分（声学轮次检测+目标时长动态合并）与无真值的 dual-ASR 一致性过滤。最终从 6180 小时原始音频产出 2408.67 小时、625192 句、3248 说话人的当前最大开源波斯语数据集，并用其训练 TTS 得 WER 2.1、MOS 4.27。

### 🔧 技术方案

**问题背景：** 零样本 TTS 受限于数据规模与质量：对齐法需逐字稿难扩展，Emilia/AutoPrep 类流水线依赖强 ASR 且用静音阈值切分，产生大量句中截断短句、破坏长程韵律；DNSMOS 在波斯语上泛化差不可靠。

**模型架构：** 五阶段串行流水线：①预处理——Whisper Large v3 语种投票、统一 24kHz、UVR-MDX-Net 去背景音乐；②切分——Pyannote Segmentation 3.0 分离后用 Smart Turn v3.1 轮次检测判断边界完整性，按高斯 μ=12s、σ=4s 采样目标时长动态合并、硬上限 30s；③语音修复——SIDON（w2v-BERT 2.0 预测器+HiFi-GAN）重合成录音棚级音质；④过滤——语种置信+SCOREQ 阈值；⑤dual-ASR 一致性过滤并选标签。

**核心创新：** (1) 韵律感知目标驱动切分：弃用静音阈值，用声学轮次检测判定候选边界语言学完整性，将时长分布从 VAD 幂律短句右移为近高斯均衡曲线（实测均值 13.87±6.32s），保留长上下文供 TTS 学韵律。(2) dual-ASR 一致性：引入架构互补的 114M FastConformer-CTC 与 600M Parakeet-RNN-T，二者错误模式弱相关，交叉 CER<12.5%、WER<15% 且首尾边界 CER<50% 才保留，实现无真值可靠性过滤。(3) SIDON 修复+SQA 重选：修复使 SCOREQ 从 3.04 升至 4.03 且方差减半；对比五种 SQA 确立 SCOREQ 为波斯语最优滤波器。

**训练策略：** 数据源自 CC 许可波斯语 YouTube，9371.5 小时逐级过滤至 2408.67 小时。TTS 端将 WavTokenizer 换成 Vevo flow-matching 声学解码器；评估用 Parakeet 算 WER/CER、CAM++ 算 SECS、SCOREQ 算 MOS。

### 📊 实验结果
**数据集**：PersianVox（2408.67 小时、625192 句、3248 说话人、词表 212216，24kHz 单声道）；1.6 小时 564 句人工 MOS 标注子集

**主要指标**：
- TTS 合成 WER：2.1；CER：0.3；说话人 SECS：79.8
- 合成 MOS（SCOREQ）：4.27（参考真值 4.31）
- SQA 相关性 PLCC/SRCC：SCOREQ 0.6658/0.6271，较最强基线 DNSMOS（0.5590/0.5182）提升约 0.107
- 语音修复 SCOREQ 较仅 UVR 提升 +0.99
- 关键对比：数据规模为当前最大开源波斯语集，大幅领先既有资源

**是否开源**：是，数据集与 MOS 标注以 CC-BY-4.0 发布于 HuggingFace，并提供 Demo

### ⭐ 评分：7/10
评分理由：面向低资源语言的工程化贡献扎实，韵律感知切分与 dual-ASR 一致性均击中现有流水线真实痛点，产出最大开源波斯语集与首个波斯语 SQA 基准，实用价值高。不足在各模块均为现成模型组合、缺消融与主观听感对比，TTS 验证单薄，创新偏集成而非方法突破。

## [7] CircleMatch: Prototype Matching with Circular Temporal Statistics for Tiny Keyword Spotting

**arXiv ID**：2609.20070 | **方向**：语音大模型

**作者**：Jiajun Sun、Zhe Gao

**机构**：上海师范大学

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.20070 | **PDF**：https://arxiv.org/pdf/2609.20070.pdf | **代码**：https://github.com/ora942878/CircleMatch | **Demo**：暂无

### 📌 简介
针对边缘设备关键词唤醒（KWS）在极小参数预算下精度难保证的问题，提出超轻量匹配框架 CircleMatch：编码器按子带独立压缩并融合为帧特征，与每类 5 个可学习原型的匹配产生时序响应曲线；再将时间位置绕到复数单位圆上，用无参数圆统计聚合响应分布与相对时序，配合动态规划有序路径分数与线性读出分类。1k～7k 参数四个变体在 GSC v1/v2 与 MSWC 英/西子集上取得有竞争力的精度—参数权衡，比 SparkNet-C4 少 30.6% 参数高 3.44 点，GSC v2 最高 96.23%。

### 🔧 技术方案

**问题背景：** 资源受限设备 KWS 需在极小参数量下保持高精度；现有 tiny 模型依赖高效卷积或学习型紧凑表示，而均值池化等时序聚合丢失响应的时间分布与相对顺序信息，在 1k～10k 参数区间判别力不足。

**模型架构：** 输入 1 秒 32 带宽 log-Mel，编码器经 8 通道卷积+深度可分离块后切 4 个子带，各自压至每帧 4 维（权重仅为密集投影的 1/4），点级融合后用两个 lifting 块建模时序上下文。每类 5 个原型与帧特征做带可学习尺度的余弦匹配生成 5 条响应曲线；曲线 softmax 归一化后在复基 exp(i2πqt/T)（q=1,2）上加权平均，取模得 10 个 Magnitude、相邻原型交叉矩得 8 维 Cross，共 18 个零参数圆统计；再与 5 维强度、1 维有序路径分数拼成 24 维证据向量线性读出。D4～D32 四变体仅 982～6694 参数。

**核心创新：** (1) 类特定原型匹配：每类 5 个可学习参考向量仅靠类别标签端到端训练，无需帧级对齐，输出可解释的逐原型响应曲线。(2) 无参数循环时序统计：将时间映射到单位圆，一阶/二阶复矩对响应曲线的共同循环移位严格不变，以零新增参数编码分布集中度与原型间相对时序。(3) 有序路径分数：对满足 5 原型按序触发的路径做 log-sum-exp 软聚合（τp=0.25），前缀 DP 以 O(KMT) 计算全部类别分数，原型自发形成时序分工。

**训练策略：** 交叉熵端到端训练。特征 32 带宽 log-Mel（25ms 窗、10ms 跳、16kHz）；增强含 ±100ms 随机移位与白噪混合；AdamW、batch 256、权重衰减 1e-4、OneCycle 峰值 lr 3e-3、100 epoch、label smoothing 0.05、dropout 0.1；5 个随机种子取均值±标准差。

### 📊 实验结果
**数据集**：Speech Commands v1/v2（12 类官方划分）；MSWC EN31/ES20（31 英文/20 西文类）；统一 16kHz 截取 1 秒

**主要指标**：
- GSC v2：96.23%±0.08（Circle-D32，6694 参数）；GSC v1：95.44%±0.30
- MSWC EN31：92.87%±0.27；ES20：93.66%±0.36
- 关键对比：Circle-D4 比 SparkNet-C4 少 30.6% 参数且高 3.44 点，刷新最小参数端 Pareto 前沿；Circle-D16 EN31 90.29% 略超 YAMNet 且远小于预训练方案
- 消融：去循环统计 −1.27、去有序路径 −0.62、去交叉矩 −0.43、换均值池化+线性 −2.93 点

**是否开源**：是，代码与模型权重已开源

### ⭐ 评分：7/10
评分理由：原型匹配、循环时序统计与有序路径分数三者逻辑自洽，移位不变性设计巧妙，在 1k～10k 参数区间实质推进 Pareto 前沿；5 种子结果、完整消融与跨语言验证较扎实。不足是最优精度增益随宽度收窄、等变性仅定性验证、未测端侧延迟。

## [8] Model-Agnostic and Language-Agnostic Voice Pipeline Improvement for the Agriculture Domain

**arXiv ID**：2609.20504 | **方向**：语音大模型

**作者**：Aakash Singh、Lakshmi Pedapudi、Chandrashekar M S、Sanyam Singh、Naga Ganesh、Vineet Singh

**机构**：Digital Green

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.20504 | **PDF**：https://arxiv.org/pdf/2609.20504.pdf | **代码**：https://github.com/aakashdg/agri-voice-pipeline | **Demo**：https://huggingface.co/spaces/DigiGreen/farmerchat-voice-pipeline-demo

### 📌 简介
针对小农户田间录音（廉价手机、农机噪声、旁帮说话人、密集成语农业词）下通用 ASR 转写差、且错误集中在改变语义的核心词的问题，提出包裹零改动 ASR 的五模块流水线：信号特征门控的 DeepFilterNet3 增强、说话人分离与目标人选择、可替换 ASR、加权农词词典规则修复、质量门控。在 Hindi/Telugu/Odia 人工标注语料上，完整流水线对三个云端 ASR 降低相对 WER 16%～23%、端侧模型 5%，多说话人音频降 32%～42%，全程不微调 ASR、不调用大模型。

### 🔧 技术方案

**问题背景：** 通用 ASR 在低信噪比、多说话人、语言混合的田间音频上严重劣化，且 WER 对内容词与功能词一视同仁，无法暴露作物/农药/剂量类词错误改变提问的危险；微调 ASR 与端到端多模态路线分别受限于标注不可靠、成本与可测性。

**模型架构：** 五段线性流水线：M0 由 RMS、静音占比、SNR 等 20 维波形特征门控 DeepFilterNet3（衰减上限 6dB、纯 CPU）；M1 用 Silero VAD 与微调 pyannote segmenter 分离说话人，按平均响度+时长下限选农户声轨；M2 在统一接口后无缝替换云端（Gemini、Sarvam、Azure）与端侧 CTC（IndicConformer 600M）；M3 对照约 1.8 万条挖掘农词的逐对标注同音词表做修复；M4 以 ASR 置信度+高权重农词双门控拒发坏转录（仅设计）。

**核心创新：** (1) 模型与语言无关性：除 segmenter 外全用现成模型，增强与修复按各模型自身证据条件化开关，同一效果在四个异构 ASR、三种语言上成立。(2) 安全词典工程：同音对经 LLM 判定逐对标注，修复仅限词典外"幻觉词"、多候选平局拒改、双写法跳过，以保守换高精度。(3) 错误代价评测体系：AWWER 按 4/3/2/1 四档加权农词，并列报告条目率与 cpWER，并实证 DER 与下游转写仅弱相关（r=0.60），故 segmenter 按 cpWER 排序调优。

**训练策略：** ASR、增强、修复、门控零训练；唯一微调是 pyannote segmenter，在项目自有三语田间音频上训练，Powerset 多类交叉熵损失，冻结留出集 0.25s collar 评分（DER 0.214）；所有阈值权重为配置项，测得系统无 LLM 推理调用。

### 📊 实验结果
**数据集**：与 IISc 合作人工质检评测集约 2,700 条（多说话人 522、单说话人 2,151，Hindi/Telugu/Odia）；词表挖掘自约 10 万条农户查询

**主要指标**：
- 全语料相对 WER 降幅：Gemini −22.8%（0.439→0.339）、Sarvam −19.3%、Azure −16%、端侧 IndicConformer −4.9%
- 多说话人相对降幅：云端 −32%～−42%、端侧约 −16%
- 分离 DER：微调 segmenter 0.214，最优云分离 0.249，stock pyannote 0.417
- 关键对比：门控增强仅在 Gemini 高噪段净降 0.147，对 Sarvam/Azure 反升 0.034/0.061，证明须按模型开关；自托管分离约 $0.02/音频小时 vs 云 $0.18
- 成本：M0 RTF 约 0.02，76% 流量被门控跳过

**是否开源**：是：评测集（CC-BY-4.0）、18k 词表、微调 segmenter 权重（MIT）、流水线与评测代码、HF 演示

### ⭐ 评分：7/10
评分理由：贡献是系统级应用工程而非模型创新，路线简单却在四 ASR×三语言上以配对 bootstrap 显著验证，并暴露"降噪可能伤 ASR""DER 不映射转写质量"等有价值的反直觉发现，部署成本透明且全部开源。不足是质量门未实验、词表仅覆盖天城文、多说话人下绝对 WER 仍高。

## [9] Robust Workflow Generation via Adversarial Learning for Audio Deepfake Detection

**arXiv ID**：2609.20063 | **方向**：语音大模型

**作者**：Xiang Li、Pin-Yu Chen、Wenqi Wei

**机构**：Fordham University；IBM Research（Yorktown Heights）

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.20063 | **PDF**：https://arxiv.org/pdf/2609.20063.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对音频深伪检测器在真实噪声、压缩、编解码等扰动下泛化失败的问题，提出 ROGUE 框架，把检测工作流构建为扰动下的序贯决策：扰动智能体从可学习类别分布中采样最具破坏性的音频变换，策略智能体（LLM/DSPy 控制器）自适应选择编排检测工具。在 15 种扰动上平均准确率 0.91，较无对抗 DSPy 基线（0.88）和最强专用检测器 DF_Arena_1B（0.89）均有提升，跨数据集平均 0.95，显著改善 EnCodec 等困难扰动与分布外泛化。

### 🔧 技术方案

**问题背景：** 现有深伪检测器在受控条件下性能强，但在噪声、压缩、混响、神经编解码等真实损坏下严重退化，且没有单一检测器能在所有条件下稳定领先；既有 LLM 工作流生成只优化良性输入，缺乏对扰动与分布漂移的鲁棒建模。

**模型架构：** 两个交互智能体。扰动智能体维护 15 类扰动工具（音高、时间、Opus、EnCodec、量化等）上的可学习类别分布，每步采样最坏变换合成扰动音频。策略智能体是 LLM/DSPy 控制器，把检测工具集（元数据取证、CQCC-GMM、LFCC-LCNN/ResNet、AASIST/RawGAT-ST、HuBERT/Wav2Vec2-BERT）按状态逐步选择、执行、累积证据直至终止，输出预测，形成 4 阶段由粗到细的编排工作流。

**核心创新：** (1) 将工作流级鲁棒性扩展为对抗学习，联合优化扰动与策略智能体的 min–max 目标，使鲁棒性源于自适应工作流构建而非单模型增强。(2) 扰动智能体以可学习类别分布聚焦最具破坏性变换，奖励 R=1−R(π,x',y) 驱动权重 softmax 更新，自动优先 EnCodec/Opus/音高等高危扰动。(3) 策略智能体引入代价惩罚 λ·C(π)，鼓励便宜工具处理简单样本、困难情形才升级重型检测器的自适应早退策略。

**训练策略：** 以 GPT-5 为主骨干（另验证 Claude Sonnet 4.6、Gemini 3 Pro）。在 WaveFake 上训练，真实样本取自 LJSpeech，1:1 均衡。RL 公式与 DSPy 度量驱动累积奖励 1[ŷ=y]−λ·C(π) 最大化；每样本搜索 M 步扰动取最坏构成对抗批，按温度 softmax 更新类别权重，多轮交替。

### 📊 实验结果
**数据集**：WaveFake+LJSpeech（训练/鲁棒测试）；跨数据集含 ASVspoof2019/2021LA、CodecFake、Fake-or-Real、DFADD、In-the-Wild、SONAR、LibriSeVoc

**主要指标**：
- 平均鲁棒准确率：0.91（DSPy 0.88，DF_Arena_1B 0.89）
- EnCodec 压缩：0.67（HuBERT 0.56，DSPy 0.62）；Opus：0.72（基线最佳 0.69）
- 跨数据集平均：0.95（DSPy 0.92），CodecFake/In-the-Wild 较 DSPy 提升约 9%/3%
- 关键对比：去除 EnCodec 扰动训练后平均鲁棒精度从 0.74 降至 0.68，验证其关键性

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：将对抗学习引入 LLM 智能体的工作流级鲁棒性属新颖，扰动优先级、留一与置换分析支撑充分。但困难编解码扰动下绝对精度仍偏低（EnCodec 仅 0.67），基线对比与代码缺失削弱可复现性，实用价值中等。

## [10] VākQA: A Benchmark and Evaluation Study for Telugu Spoken Factoid Question Answering

**arXiv ID**：2609.19879 | **方向**：语音大模型

**作者**：Bhavana Akkiraju、Ravi Sastry Kolluru、Charan Devarakonda、Srihari Bandarupalli、Santosh Kesiraju、Anil Kumar Vuppala

**机构**：IIIT-Hyderabad（印度）、布尔诺理工大学 Speech@FIT（捷克）

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.19879 | **PDF**：https://arxiv.org/pdf/2609.19879.pdf | **代码**：https://hf.co/datasets/Bhavanaakkiraju/VakQA | **Demo**：暂无

### 📌 简介
针对泰卢固语语音问答基准空白及低资源语言自动评测可靠性未量化的问题，提出 VākQA：首个泰卢固语语音事实问答基准，含 2,001 对问答、2.53 小时真实竞赛音频、双语转写与人工校验参考答案。先用 400 条人工评分校验评测方法，发现 Gemini-as-judge 与人类相关性最高（Spearman ρ=0.86）但严格度非均匀，小模型裁判会系统性错罚表述不同的正确答案。基准测试表明专有模型显著优于开源模型，语音输入与级联 ASR→MT 逐级引入误差，文化域对翻译最敏感。

### 🔧 技术方案

**问题背景：** 现有 SQA 基准多为英语或以 TTS 合成/翻译而来，泰卢固语仅有文本基准；EM/F1 对释义与 ASR 噪声脆弱，LLM-as-a-judge 在低资源语言上的可信度此前未被系统验证。

**模型架构：** 三段式半自动管线：①从 YouTube 竞赛节目采集六域音频（科学 27%、常识 23%、政治 16%、历史 13%、文化 12%、地理 10%）；②Pyannote VAD 切 7 秒块，用约 900 小时数据微调的 Seamless-large-v2 转写合并，LLM 逐字抽取 QA 对，再用 IndicWhisper 词级时间戳经相似度 ≥85% 模糊对齐精修音频边界；③5 名标注者核验音文一致性并人工英译。最终 2,001 题、2.53 小时、平均单条 4.55 秒。

**核心创新：** (1) 首个泰卢固语原生语音开放问答基准，问题直接源于真实口语交互而非合成或翻译，附双语转写与人工校验答案。(2) 首次量化泰卢固语 QA 评测可靠性：以 1–5 分人工评分（Krippendorff α=0.836）为金标准，系统对比多种裁判与 EM、F1、BLASER-2.0，揭示裁判选择主导评测结论。(3) 系统消融输入语言、模态、模型规模与域，构造 2 ASR×2 MT 级联以定位翻译歧义与音近混淆等失败模式。

**训练策略：** 评测协议：抽样 100 题×4 个 QA 模型生成 400 条三元组，5 名母语者按五级量规打分，剔除离群后用 Spearman ρ、Kendall τ 度量一致性；随后以 Gemini 为主裁判，在 9 种输入配置（oracle 文本、双 ASR、四种级联、直接语音）下基准测试 9 个模型。

### 📊 实验结果
**数据集**：VākQA（2,001 条泰卢固语音事实问答，2.53 小时，6 领域）

**主要指标**：
- 裁判与人类相关性：Gemini ρ=0.86、τ=0.77、MAE=0.46；EM ρ=0.37、F1 ρ=0.49
- QA 得分（1–5）：oracle 泰语文本 3.63、直接语音 3.28、ASR 文本 3.09–3.40、ASR→MT 级联 2.44–2.80
- 开源最佳 Gemma-3-27B 仅 2.55，其余 ≤2.0
- Seamless 微调 ASR WER 30.25/CER 10.12；级联后 BLEU 由 37.22 降至 27.95
- 关键对比：换用弱裁判使 46.2% 答案得分被系统性压低，评测协议选择即结论

**是否开源**：是，数据在 HuggingFace 公开（CC BY 4.0）

### ⭐ 评分：7/10
评分理由：填补泰卢固语语音问答基准空白，并以人工金标准严谨量化 LLM 裁判在低资源语言的可靠性偏差，评测-分析-消融三位一体，对语音问答管线设计有直接参考价值。但采集域偏窄（竞赛问答）、QA 抽取依赖闭源模型、缺改进方案，属资源型实质贡献。

## [11] A Cross-Lingual Acoustic Disease-Alignment Framework for Respiratory Health Assessment from Spontaneous Speech

**arXiv ID**：2609.19398 | **方向**：语音大模型

**作者**：Roksana Khanom、Raghib Asfak Tasnim、Bodrun Nahar Bithi、Shafia Shirin Supty、Saiful Islam Raju、Ashok Agrawala、Nirupam Roy

**机构**：University of Maryland, College Park；Sylhet MAG Osmani Medical College Hospital（孟加拉国）等

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.19398 | **PDF**：https://arxiv.org/pdf/2609.19398.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
自发语音是无创评估呼吸健康（如 COPD）的可扩展信号，但疾病相关声学改变与语言特有音系、韵律变化纠缠，导致单语模型跨语言失效。本文提出跨语言疾病对齐框架 CL-DAF：基于 201 名英语者与 75 名新采集孟加拉语者构建共同 272 维声学表征，用带符号 rank-biserial 效应量与语言不变性分数（LIS）筛选疾病方向跨语言一致的特征。孟加拉语单语 COPD 检测 AUC 0.849，但 133 个（48.9%）特征疾病方向跨语言反转、全表征迁移仅剩 0.49；CL-DAF 的 26 个对齐特征将双向迁移 AUC 提升至 0.825 与 0.722。

### 🔧 技术方案

**问题背景：** 现有呼吸语音研究均在单语队列内开发，缺乏跨语言可复用的声学标志物；单语内判别力强的特征在新语言中可能变弱甚至极性反转，单语 AUC 高并不代表适合多语临床建模，核心问题是"哪些疾病信号分量在语言切换后仍可靠"。

**模型架构：** 框架分两层。共同声学表征：录音重采样 16kHz，能量 VAD 保留语音段，3 秒窗 50% 重叠，Praat/Librosa 提取 136 维手工特征（F0、jitter/shimmer、HNR、CPP、共振峰、MFCC 及差分、谱质心等），两级聚合成 272 维说话人向量。疾病对齐层：每特征在两种语言内独立做 Mann-Whitney U 检验算 signed rank-biserial 效应量，BH-FDR 控制显著性；LIS 在双语符号一致时取两侧 |r| 最小值、不一致取负值，以阈值 τ 选出疾病对齐子集，LIS<0 集作负对照。

**核心创新：** (1) 首个医生标注的孟加拉语自发语音 COPD 队列（75 人），与英语 SpiroPhonia 配对构成英-孟共同空间，证实孟加拉语自发语音单独携带 COPD 信号（AUC 0.849，置换检验 p<0.01）。(2) 提出 LIS"最小效应量+符号一致性"度量，将特征空间显式划分为 26 个疾病对齐、113 个弱一致与 133 个符号反转，量化单语判别性与跨语一致性的解耦。(3) 双向迁移+target-held-out 特征选择协议：统一固定类别均衡 L2 逻辑回归避免模型混淆，并令目标说话人不参与选择，量化池化乐观偏差。

**训练策略：** 统计分析框架。单语评估 10×重复说话人分层五折交叉验证，缺失填补与标准化仅训练折内拟合；迁移仅源语言训练、目标域测试；95%CI 由 1000 次说话人级 bootstrap 给出；主阈值 τ=0.147 并做敏感性扫描与多分类器验证。

### 📊 实验结果
**数据集**：SpiroPhonia 英语自发语音（102 COPD/99 对照）+ 孟加拉语临床队列（26 COPD/49 对照），共 276 人，16 kHz

**主要指标**：
- 孟加拉语单语内 AUC：0.849±0.026（BAcc 0.765）
- 全 272 特征迁移 AUC（EN→BN / BN→EN）：0.663 / 0.488
- CL-DAF 26 特征迁移 AUC：0.825 / 0.722；符号反转子集仅 0.268 / 0.341（显著低于随机，负对照成立）
- target-held-out 选择下 AUC：0.785±0.015 / 0.630±0.022
- 关键对比：BN→EN 方向较全特征提升 +0.234；CL-DAF 子集跨语效应量相关 ρ=0.785 vs 全表征 0.189

**是否开源**：孟加拉语数据以学术用途按需申请提供；代码暂无

### ⭐ 评分：7/10
评分理由：将跨语言呼吸语音建模重构为疾病效应方向一致性问题，LIS 度量简洁可解释且双向可验证，48.9% 特征极性反转的发现具方法论警示价值；首个医生标注孟加拉语队列与留出协议体现严谨性。不足是样本量小、仅手工特征+逻辑回归、未与自监督表征对比且只覆盖两种语言。

## [12] Music Hallucination in Audio-Language Models: A Hierarchical Formulation and Empirical Study

**arXiv ID**：2609.20195 | **方向**：语音大模型

**作者**：Yu Liu、Jiahui Liu、Zhilin Liu、Cong Cao、Fangfang Yuan、Yuling Yang、Pin Xu、Yanbing Liu

**机构**：中科院信息工程研究所、国科大网络空间安全学院、中央音乐学院、电子科技大学

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.20195 | **PDF**：https://arxiv.org/pdf/2609.20195.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
音频语言模型常生成自信却无音频依据的音乐描述，而现有幻觉基准仅把音乐当泛音频、以"参考未提及即幻觉"误判。本文首次将音乐幻觉形式化为按可验证性划分的五层感知落地失败（声音事件/时序/调性/风格/情感），提出矛盾式三值判决与多范式诊断框架 MuseDiag：硬层用信号工具客观核验，软层用 LLM 裁判。评测 9 个模型后人声误知是普遍弱点、调性是架构分水岭，仅 Audio-Flamingo-3 三范式均领先；两种免训练缓解（ADD-M、TPA）在探测有收益但常不迁移至自由生成。

### 🔧 技术方案

**问题背景：** 音乐描述天然选择性输出，正确属性未被提及不等于幻觉，单一目标存在性检查无法覆盖乐器、人声、速度、调性、风格、情感等异质证据需求；此前未回答"哪层失效、为何失效、缓解能否跨范式迁移"。

**模型架构：** 五层按认识确定性分硬层 L1-L3（信号工具可客观验证：人声用 VAD 浊音帧比、BPM 映射粗分类并设 [75,85]∪[115,125] 模糊带、调性置信门限 0.8）与软层 L4-L5（LLM 矛盾判定），判决输出矛盾/兼容/不确定三值抑制假阳性；三互补范式（约 6500 个 yes/no 探测、440 首自由描述、多维结构化查询）作诊断仪表盘而非合并总分，指标含覆盖度校正的分层幻觉率与肯定性偏见 YB。

**核心创新：** (1) 以可验证性组织的五层音乐幻觉分类与矛盾式评测，显式不确定态避免 caption 遗漏误罚。(2) 证据路由验证管线：claim 按语义层路由至信号工具或 LLM 裁判，阈值全局固定防按模型调参，并对工具与裁判做专家一致性审计。(3) 两个免训练干预探针：ADD-M 在 logit 空间用音频消融 KL 散度作音频依赖分数、高熵+低 ADS 双条件门控校正；TPA 在上下文空间用 k=4 层特定感知探针构造锚定语境。

**训练策略：** 无需训练。greedy 解码，ADD-M 仅用于开源四模型（API 不暴露 logits）、系数 α=1.0，缓解效应全部用同 prompt 配对比较量化。

### 📊 实验结果
**数据集**：MusicCaps 抽样 500 clips（440 可用）+ IRMAS 测试集 2,874 clips 乐器核验；9 模型（Qwen2-Audio、SALMONN、Audio-Flamingo-3、Qwen2.5-Omni 及 5 个闭源）

**主要指标**：
- Audio-Flamingo-3 最优：探测 Acc 74.0%、总幻觉率 25.8%、软层 HR 9.7%、结构化 Avg Acc 61.0%
- 人声幻觉率全模型居高 45.9%–61.3%；自由生成调性幻觉率跨 34.8%–90.5%
- 调性分化：Qwen2.5-Omni key 准确率 68.6% vs Qwen2-Audio 3.0%、SALMONN 5.1%
- 肯定性偏见 YB 跨度 20.2%–99.0%（SALMONN 极端）
- 缓解迁移：ADD-M 探测 +1.0~+4.7pp，但四模型自由生成幻觉率反升 +1.3~+5.9pp；TPA 使 Qwen2-Audio key 准确率 1.2%→43.2% 却使 Omni 降 4.8pp
- 关键对比：跨范式排序相关性仅 ρ=0.17，探测强不等于生成好

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：首个音乐特异、分层、多范式幻觉实证研究，矛盾式判决与阈值审计体现方法学严谨度，"缓解不跨范式迁移"的负结果有价值。局限在评测型贡献、无新模型、干预仅覆盖四个开源模型，但诊断协议对音频理解系统有直接参考意义。

## [13] A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound

**arXiv ID**：2609.20595 | **方向**：语音大模型

**作者**：Thomas J Stoll、Ross K Maddox

**机构**：密歇根大学 Kresge 听力研究所

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.20595 | **PDF**：https://arxiv.org/pdf/2609.20595.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
人类听觉计算模型通常只针对单一通路阶段或范式，难以跨神经时间尺度整合发现。本文提出人脑听觉电生理"基础模型"：完全因果的编码器—解码器网络，将双耳原始声波形端到端映射为高采样率连续 EEG，在 92 名被试、约 250 小时数据（纯音、语音、音乐）上训练。固定权重、零微调下，模型重现了 pABR 的刺激率/频率效应、自然语音皮层下与皮层 TRF 以及双耳交互成分（BIC 潜伏期 6.40 ms）；模型—总均值相关 0.604–0.944，基本落在被试级人类分布内。

### 🔧 技术方案

**问题背景：** 传统手工听觉模型只覆盖单阶段单时间尺度，难以扩展至多神经发生器；已有数据驱动模型要么只瞄准单一通路环节、依赖动物侵入式记录，要么建模行为而非脑响应。

**模型架构：** 双耳 40 kHz 音频经每耳 24 频带因果滤波器组（100 Hz–16 kHz）、对数压缩、平均池化降至 5 kHz 与 EEG 对齐；9 层因果 WaveNet（核 8、膨胀 2^d、门控激活）编码，4 层 1×1 卷积瓶颈压缩至 16 个潜在神经成分，经 montage 特定空间权重映射至任意通道 EEG，以被试身份与听力学元数据条件化。另设并行线性伪迹通路（4 ms 卷积、对称填充补偿声管延迟）分离电伪迹，神经通路保持严格因果。

**核心创新：** (1) 首个跨范式、跨时间尺度的音频→EEG 全因果基础模型，单模型同时再现脑干波与皮层追踪响应，评估时零微调、零个体校准（被试 dropout 训出"默认被试"实现总体响应零样本预测）。(2) 先算预测误差再取变换的 STFT 域对数损失（F=251、ε=1e-6），既惩罚相位/时间误差又避免高功率低频主导梯度，显著优于 MSE。(3) 以单例统计（Crawford-Howell）+被试级人类分布做模型-人等价性检验，为 in silico 听觉实验定标准。

**训练策略：** 约 1 分钟片段端到端训练，Adam lr 1e-4、batch 4、AMP 梯度缩放与范数裁剪 1.0；10% 留测按测试损失选 epoch；EEG 降采样至 5 kHz、因果 0.1 Hz 高通；刺激含频率特异性纯音、语音、音乐与临床瞬态声。

### 📊 实验结果
**数据集**：92 名被试（22.6±4.1 岁）约 250 小时、≥10 kHz 采集、2 至 64+ 通道 EEG

**主要指标**：
- pABR 模型—人类总均值 Pearson 相关：0.604–0.944（500 Hz–8 kHz）
- 皮层下/皮层语音 TRF 相关：0.39–0.93；率—幅曲线相关 ≥0.961
- 预测 BIC 潜伏期 6.40 ms（文献规范 5.58–6.90 ms 内）；幅值超规范但 Crawford-Howell 不显著（p=0.135）
- 关键对比：14 个条件中除 1 项（男性高 F0 皮层 TRF）外全部落在被试级人类分布内；未与既有模型定量对比

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：以单一全因果模型统一再现 pABR、TRF、BIC 三类经典听觉范式，并用单例统计严格验证，属方向性新工作；约 250 小时数据规模有限、无定量基线对比、未开源、存在串列响应偏大等系统偏差，削弱可复现度与实用强度。

## [14] Reading Emotions in the Token Space: Discriminative Adaptation of SpeechLLMs for Emotion Recognition

- **arXiv ID**：2609.20081 | **方向**：语音大模型 | **评分**：6/10
- SpeechLLM 判别式读出：冻结主干上取最终 prompt token 隐状态接单层线性分类头做 SER，单次前向出标签、消除标签集外幻觉并抑制多数类偏置；IEMOCAP 双架构上 Macro F1 提升（ASR 转写下降益最大 74.47→76.50），并超 EmoBox 榜首与 Audio Flamingo 3；线性头投影回 token 空间揭示情感类锚定的是镜像网络文本偏见的间接语义场。增量式技巧但分析有价值，代码暂无。
- **作者**：Hasindri Watawana 等（Idiap、EPFL、Uniphore、BUT）｜**论文**：https://arxiv.org/abs/2609.20081 | **PDF**：https://arxiv.org/pdf/2609.20081.pdf | **代码**：暂无 | **Demo**：暂无

## [15] Consensus-Guided Shared-Specific Tri-View Learning for Speech Emotion Recognition

- **arXiv ID**：2609.19826 | **方向**：语音大模型 | **评分**：6/10
- 三视图 SER：把谱图/MFCC/HuBERT 各分解为共享与专属成分，跨视图共识聚合全局参照（CCL），视图专属 sigmoid 门控逐元素融合（VGI），加软差异正则抑制信息重叠。说话人独立评测 IEMOCAP 74.19% WA/75.17% UA、EmoDB 94.36% WA，较最强多视图基线提升 4.39/2.77 点。DSN/MISA 思路的迁移重组，HuBERT 单视图已达 72.51 WA 说明三视图收益偏工程性；代码已开源（github.com/Luxikun669/TriCGF）。
- **作者**：Bing Huang、Yujian Ma、Xikun Lu、Xianquan Jiang、Jinqiu Sang（华东师范大学等）｜**论文**：https://arxiv.org/abs/2609.19826 | **PDF**：https://arxiv.org/pdf/2609.19826.pdf | **代码**：https://github.com/Luxikun669/TriCGF | **Demo**：暂无

---

## 语音前端

## [16] Foreground Voice Activity Detection: Learning Speaker Selectivity from Supervision

**arXiv ID**：2609.19856 | **方向**：语音前端

**作者**：Guangzhao Yang、Muhammad Huzaifah、Yu Pan、Jinya Sakurai、Ningjie Bai

**机构**：Recho Inc. R&D Team，东京

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.19856 | **PDF**：https://arxiv.org/pdf/2609.19856.pdf | **代码**：暂无（承诺发布 Mix-Interference 基准） | **Demo**：暂无

### 📌 简介
本文形式化定义"前景 VAD（FVAD）"：无注册、帧级二分类，仅将"持续存在"的主动说话人标为正，单说话人时退化为传统 VAD。作者发现说话人选择性主要来自训练监督而非架构：用全自动化数据配方（前景标签+竞争说话人远场混叠）训练，即可让普通流式 VAD 获得选择能力。提出 BG-FAR 指标与 Mix-Interference 基准。Mamba-FVAD（约 0.6M 参数）前景 F1 达 0.88–0.92、BG-FAR 低至 0.05–0.40，显著优于 Silero 等商用 VAD 及带注册说话人系统，CPU 单帧延迟 1–2ms。

### 🔧 技术方案

**问题背景：** 商用 VAD 把所有语音（含背景他人声）判为有效活动，在嘈杂场景引发 ASR 污染、轮次切换失效、虚假打断三类故障。既有补救（能量门控、增强前端、说话人注册）要么不可靠要么依赖外部先验，无法在单一轻量流式检测器内解决。

**模型架构：** 可学习 LEAF 前端（去时间池化改全局平均池化以保 31.25Hz 帧分辨率）+ 时序骨干 + 逐帧分类头。主系统用 Mamba 状态空间解码器实现逐帧 O(1) 内存；对比等参数量 LSTM 与 Transformer 以研究长程上下文影响。

**核心创新：** (1) FVAD 任务与 BG-FAR 指标：以"前景静默且背景活跃"帧的虚警率量化身份承诺，前景 F1 作门控。(2) 全自动化抗干扰配方：Silero-v6 伪标签+能量自适应边缘细化，1–3 段竞争语音按 0–15dB TIR 经 RIR 与 1–4kHz 低通远场化后混入，标签只保留前景。(3) 控制性基准 Mix-Interference：同噪声同干扰者仅变 SNR 的 7 个帧对齐变体，配 VOiCES 真实远场外推校验；等架构对比证明监督配方而非时序建模容量决定选择性。

**训练策略：** AdamW（lr 1e-4、wd 0.01、cosine+warmup）、batch 16、dropout 0.3、bf16；训练集为日语真实呼叫中心 1128h + LibriSpeech 拼接；以 LibriVAD 配方同架构模型作对照隔离配方贡献。

### 📊 实验结果
**数据集**：Mix-Interference（LibriSpeech test-other+合成干扰，16kHz）、VOiCES、KAIST、VoxConverse、TEN-VAD、in-house 日语 9.8h、LibriVAD-concat

**主要指标**：
- Mix-Interference 前景 F1：0.88–0.92，BG-FAR 0.05(17dB)–0.40(9dB)
- VOiCES：tele 场景 BG-FAR 0.07 与 music 基线持平，babble 0.12
- 关键对比：同架构换 LibriVAD 普通配方后 BG-FAR 崩溃至 >0.8（任意语音触发）；商用 Silero-v6 仅 F1 相当而选择性差 2–4 倍；带注册 pVAD BG-FAR≈0.23 但前景 F1 明显更低
- 传统 VAD 能力多数基准比最强专家低几个点，−5dB SSN 为短板（0.70）

**是否开源**：承诺开源 Mix-Interference 基准，代码/模型暂无

### ⭐ 评分：7/10
评分理由：新颖任务定义与反直觉的"监督>架构"结论具实质贡献，消融设计严谨（同架构换配方即崩溃），BG-FAR 门控评估有洞察；训练数据与基准偏合成、单一公司验证、模型未开源，−5dB 等场景退化。工程实用价值高，属扎实的应用层贡献。

## [17] Beyond the Stability–Plasticity Frontier in Streaming Target Speaker Extraction

**arXiv ID**：2609.20463 | **方向**：语音前端

**作者**：Yuesheng Ma、Linyang He、Nima Mesgarani

**机构**：哥伦比亚大学电气工程系

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.20463 | **PDF**：https://arxiv.org/pdf/2609.20463.pdf | **代码**：https://github.com/ym2976/anchor-fast-weight | **Demo**：暂无

### 📌 简介
流式目标说话人提取需在目标静默、被掩蔽或声学漂移时维持"提取谁"的状态，而手工 EMA/门控更新规则被困在稳定性–可塑性权衡前沿。本文冻结 2.9M 分离 Backbone 与 0.26M 说话人编码器，仅对 41k 参数的锚定快权重（AFW）记忆经闭环元训练，让更新器直面自身污染证据。AFW 在严重注册失配下达 10.9 dB SI-SNRi，较最佳启发式提升 3.0 dB，同时 30 秒静默后仅比静态注册低 0.9 dB，运行时开销不足 5%；GRU 对照证明增益源于闭环学习原理而非 AFW 本身。

### 🔧 技术方案

**问题背景：** 流式 TSE 的说话人状态需在目标缺席时保持身份、在注册–混听失配时适应，两者互斥。在 22 种自适应启发式配置（含 oracle VAD 门控）上的系统测量表明该权衡构成前沿：即使完美目标活动检测也无法同时解决两轴——活动不等于身份，失配时残差仍会写入干扰者证据。

**模型架构：** 闭环状态学习：250ms 混听分块经因果 FiLM-TCN 分离 Backbone 输出，用冻结说话人编码器再编码为证据 e_t。AFW 是 128×128 联想记忆，W₀=0，按 delta 规则带遗忘地写入 k_t、v_t；64 单元门控 MLP 由证据、相似度余弦与输出能量预测写入率 η_t 与遗忘率 λ_t。读出为固定注册锚点 a 加内容寻址方向残差 s_t=norm(a+W_t q)，仅 41k 可训练参数，推理只需 rank-1 写入与矩阵向量积。

**核心创新：** (1) 首次实证刻画流式说话人状态的稳定性–可塑性前沿，证明 oracle 活动门控即启发式边界，界定手工规则的能力上限。(2) 经 52–104 个分块（13–26 秒）闭环反向传播元训练更新动力学，使更新器暴露于自生成历史而突破前沿；115k GRU 同目标训练验证原理普适。(3) AFW 提供可解释小模型：严重失配下写入残差增大且与目标偏移方向余弦达 0.419、对干扰者近正交（−0.018），属方向性修正而非多写。

**训练策略：** 损失为 −SI-SNR（目标活跃样本）+0.1×缺席功率惩罚（16s 缺席抑制输出），无显式身份损失；训练含至多 4s 缺席与信道严重度 0–3（谱倾斜/峰化/电话带通）；主结果 3 种子平均，混淆由外部 ECAPA-TDNN 判定。

### 📊 实验结果
**数据集**：LibriSpeech train-clean-360/test-clean（说话人无泄露），每条件 150 序列；另用 RWCP/AIR/REVERB 325 条实测 RIR 与 Libri2Mix

**主要指标**：
- 严重失配 SI-SNRi：AFW 10.9 dB vs 最佳启发式 7.9 dB（+3.0 dB）、GRU 10.5 dB
- 30s 缺席后恢复：AFW 6.2、GRU 7.3、静态 7.1 dB（差距 ≤0.9）
- 说话人混淆率 4–5%（启发式 15–31%）；16s 缺席抑制 17.2–18.7 dB
- 效率：RTF 0.074（A100），运行开销 <5%；oracle 证据诊断再 +0.4 dB
- 关键对比：匹配 Libri2Mix 上略低于静态（7.93 vs 8.40 dB），体现适应的代价

**是否开源**：代码开源（GitHub: ym2976/anchor-fast-weight）

### ⭐ 评分：7/10
评分理由：问题定义清晰、以受控实验严谨实证启发式前沿，闭环元训练+锚定快权重构成实质方法贡献，GRU 对照与残差方向分析增强可信度。不足在增益限定于冻结 Backbone 的状态机制设定，失配与缺席未联合评测，匹配条件略回退。41k 参数与可解释性具备落地价值。

---

*Generated on 2026-09-18*
