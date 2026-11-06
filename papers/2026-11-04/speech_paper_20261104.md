# 2026-11-04 语音论文速递

**共收录**: 12 篇 | **语音大模型**: 8 篇 | **语音前端**: 4 篇

> 目标日期 2026-11-04（北京时间）arXiv 语音相关论文共命中 12 篇（批次 New+Cross 共 16 篇，过滤心音/呼吸音/音乐/无人机声学 4 篇，无历史重复）。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] TTSonic: A Unified Framework for Composable and Controllable Speech Generation

**arXiv ID**：2611.04282 | **方向**：语音大模型

**作者**：Zhedong Zhang, Kaiwen Zhou, Junyan Wu, Shengqiang Li, Xuran Chi, Xingui Zeng, Rui Yan, Xu Chen

**机构**：ByteDance Douyin Content Group（字节跳动抖音内容组）

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04282 | **PDF**：https://arxiv.org/pdf/2611.04282.pdf | **代码**：暂无 | **Demo**：https://bytedance.github.io/TTSonic/

### 📌 简介
现有语音生成系统多针对单一能力独立训练，难以在统一模型中保持质量与可控性一致。TTSonic 提出 2B 参数的统一可组合框架，以语义-声学解耦 speech tokenizer 为表征基座，组合文本、自然语言指令、参考音频、文本描述音色四类条件，支持 zero-shot TTS、声音/韵律克隆、指令跟随、语音转换与噪声参考克隆。Seed-TTS-Eval 中文 CER 0.78%、test-hard CER 5.64%，InstructTTSEval 中文 APS 88.8 超全部对比基线，音色设计碰撞率显著低于 Qwen3-TTS 与 VoxCPM2。

### 🔧 技术方案

**问题背景：** 实际语音基础模型需同时具备稳定质量、精确可控与多能力组合，而现有方法按任务单独建模，扩展新能力需重训端到端模型；核心难点在于构造既保留语义/韵律又剥离说话人声学特征的离散表征，使同一框架可按任务重组条件路径。

**模型架构：** 三模块加一个外挂组件。①Speech Tokenizer：16 kHz 波形经 80 维 filterbank，512 维 E-Branchformer 前 19 层（25 Hz）提取连续语义表征，FSQ 量化为 5 维隐变量（层级 [8,8,8,8,4]，隐式码本 16384，每 40 ms 一 token）。②Text-to-Semantic LM：从 Qwen3.5 初始化，语音 token 并入文本词表共享 embedding 与 LM head，自回归预测语义-韵律 token，可在 <think> 段内先生成 CoT 风格计划。③Acoustic Flow Matching：沿用 CosyVoice 3 因果条件流匹配，causal DiT 以 1:2 token-mel 比率渲染 80 维 50 Hz mel，可选叠加 CAM++ 192 维说话人嵌入与 prompt mel 前缀，causal HiFi-GAN/HiFT 声码器输出 24 kHz。④Text2Timbre：冻结 Qwen3-Embedding 编码音色描述，DiT 流匹配生成 CAM++ 空间的 192 维说话人嵌入。

**核心创新：** (1)两阶段语义-声学解耦 tokenizer：Stage I 在编码器第19层后插入 FSQ 瓶颈，用 encoder-decoder ASR+CTC+一致性正则联合监督迫使 token 保留语言与韵律信息；Stage II 冻结编码器仅更新 FSQ 映射，用声学分支（ECAPA-TDNN+Perceiver+第二 FSQ+12 层条件解码器+HiFi-GAN）做重建，损失含 mel、多分辨率 STFT、对抗与说话人量化一致性项。(2) CoT 引导指令跟随：将指令映射分解为"风格计划→语音 token"两段联合建模，训练随机采样多视角标注，推理先由 LLM 生成属性画像再续写语音。(3)统一生成接口：8 种生成范式仅通过选择/复用 codec、LLM、FM、vd 模块组合实现；VC 与语音增强绕过 LLM 直接用 codec token，且 VC 为完全未见过跨说话人 token-音色重组。

**训练策略：** LM 采用标准 next-token NLL；Flow 模块从 CosyVoice 3 流匹配权重初始化，数据以音频保真度为首要准则混合，随后用 FlowTTS-GRPO 多目标 RL 后训练；指令标注由 SOTA 专有 omni 模型多次生成；Text2Timbre 训练随机丢弃文本条件、推理用 CFG。论文未披露语料小时数、学习率、batch size 等具体超参。

### 📊 实验结果
**数据集**：Seed-TTS-Eval（zh/en/hard）、CV3-Eval（多语+跨语）、InstructTTSEval（中英）、Seed VC、VoiceBank-DEMAND-16k；指标：WER/CER、WavLM SIM、UTMOS/DNSMOS、ERes2Net SIM、碰撞率与主观分

**主要指标**：
- Seed-TTS-Eval：test-zh CER 0.78%/SIM 0.784（全表最低，超 dots.tts 0.96、FireRedTTS3 1.01）；test-en WER 1.66%；test-hard CER 5.64% 优于 Auk 5.91 与 CosyVoice 3 5.83
- CV3-Eval：en-to-zh WER 3.44%（最低），6 子集中 5 个 SIM 第一
- InstructTTSEval-ZH：APS 88.8（超 FireRedTTS3 85.8）；EN 侧 77.6/78.4/64.4 落后最强基线
- 音色多样性：>0.70 碰撞率 6.52% vs Qwen3-TTS 8.65%、VoxCPM2 9.46%
- 消融：FSQ 插第 18 层最优（WER 6.17% vs 第 6 层 7.16%）；Stage II 使 NMOS 3.94→4.08

**是否开源**：仅 demo 页，未开源权重或代码

### ⭐ 评分：8/10
评分理由：语义-声学解耦 tokenizer 的两阶段监督设计与 CoT 风格规划、Text2Timbre 模块化组合成真正可重组的统一框架，VC/噪声克隆等能力零专门监督即涌现，创新性扎实。实验覆盖 6 类任务、20 余个最新基线，中文侧多项 SOTA，充分性强。不足在于英文指令跟随明显弱于基线、训练数据规模与超参未披露、未开源权重，复现受限；整体属工业级统一语音生成的重要实质进展。

---

## [2] HyVox: Rethinking Low-Power Voice Intelligence towards Neuromorphic-von Neumann Edge Computing

**arXiv ID**：2611.03735 | **方向**：语音大模型

**作者**：Snehasis Addy, Eduardo Calle Ortiz, Prashant Shenoy, Phuc Nguyen

**机构**：University of Massachusetts Amherst

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.03735 | **PDF**：https://arxiv.org/pdf/2611.03735.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对电池供电边缘设备上开放集说话人识别（enroll/identify/reject）能耗过高的问题，本文提出 HyVox：一种"类脑-冯诺依曼"混合架构，由 Xylo Audio 3 神经形态芯片以稀疏事件驱动方式生成 32 维脉冲计数说话人嵌入，STM32L476 单片机负责gallery存储、余弦打分与拒识。核心是逐神经元学习突触时间常数的分层时间抽象 SNN 骨干（832 个 LIF 神经元）与episodic训练的脉冲嵌入提取器 SEE，配合芯片精确训练 CAST 消除仿真-硬件差距。在 20 组 Common Voice 家庭场景达 99.6%（n=2）/94.9%（n=20）top-1，单次推理 0.96s、动态能耗 1.63mJ，较最优 ANN 基线延迟低 42%、总能耗低 5.8 倍。

### 🔧 技术方案

**问题背景：** 边缘说话人识别主流 TinyML 管线将嵌入提取与打分全部压在冯诺依曼 MCU 上，推理能耗主导决策成本；神经形态处理器虽可消除访存开销，但无通用算力承载gallery检索与注册，且芯片神经元/突触/int8/事件率硬约束会摧毁传统编码器的时间建模能力。

**模型架构：** 数据流为 16kHz 麦克风→Xylo AFE→16 通道脉冲栅格（3s 窗口对应 T=293 步）→HTA-SNN 骨干→SEE 读出→32 个脉冲计数经 UART 传 STM32→L2 归一化减中心化→与gallery原型余弦打分/阈值拒识。HTA-SNN 由 5 级 LIF 构成（64/128/256/256/128 神经元），各级学习独立突触时间常数，另含两条跨尺度投影跳接把快声学证据直注慢整合层。SEE 为 32×128 无偏 int8 线性投影+32 神经元 LIF 读出，仅 4,128 可训练参数；注册即前向均值写 64 字节原型，零梯度。骨干稠密 188.4k 突触经 SpikeFit 逐突触 Fisher 分数剪至 29.0k（6.5×），再 bitshift QAT 与 CAST 微调。

**核心创新：** (1)混合分工范式：以 32 个脉冲计数为两处理器唯一接口，嵌入提取走事件驱动、决策逻辑走 MCU，注册/删除仅改 host 内存。(2)HTA 分层时间抽象：逐神经元可学 τ_syn 分配快/中/慢时间尺度加跳接，规避深度堆叠在 832 神经元预算内丢失瞬态结构。(3)芯片精确训练 CAST：把循环布局跳接折叠、int8 网格、每跳延迟、整阈值全部纳入可微副本（99.8% 复现脉冲计数），直接映射丢失 31.1 top-1 点被恢复到差距 1.6 点内。

**训练策略：** 骨干先在 VoxCeleb2（2.05M 段、5994 说话人）以 AAM-Softmax（m=0.2, s=24, lr 7.9e-4）预训练 1000 epoch；剪枝用 SpikeFit 14 步+codebook 感知微调；bitshift QAT 30 epoch、CAST 26 epoch（lr 3e-4）。SEE 在 VoxCeleb1 以 episodic FSOSL 训练 16,000 episode，损失为 supervised contrastive（τ_c=0.1）+ hinge 拒识（margin 0.4），Adam、lr 0.03 余弦衰减。

### 📊 实验结果
**数据集**：VoxCeleb2（骨干预训练）、VoxCeleb1（SEE 训练与部署测试）、Common Voice（20 口音池家庭模拟，n∈{2..20}，60s 注册+120s 查询）

**主要指标**：
- 家庭 top-1：99.6%（n=2，EER 5.5%）至 94.9%（n=20，EER 13.2%）
- 系统成本：延迟 961.9ms、动态能耗 1.63mJ/决策、总能耗 3.8mJ/决策、空闲 2.3mW
- 骨干对比 SynNet：top-1 39.6% vs 35.5%（同 29k 突触）
- 关键对比：较最快基线 DS-CNN-S 延迟低 42%、动态能耗低 13.5×、总能耗低 5.8×；CAST 较直接映射回勇 29.5 点 top-1
- 芯片精度无损：unquantized PyTorch 61.0% vs CAST 上芯 60.6%（差 0.4 点）

**是否开源**：论文未声明代码或数据发布计划，暂无

### ⭐ 评分：8/10
评分理由：首次将开放集说话人识别按嵌入边界切分到神经形态+MCU 混合平台，HTA 可学时间常数、episodic SEE 与 CAST 三件套各自解决表征、泛化、部署失真三个真问题，创新密度高且全部有消融支撑。实验在真实 Xylo Audio 3+STM32L476 上闭环验证"芯片即训练"，能效-精度 Pareto 优势显著。不足在于绝对精度仍落后云端级 x-vector、n=20 时 EER 13.2% 对严格拒识场景偏高，且未开源复现门槛大；但作为类脑语音部署路线的实质性系统工作，价值明确。

---

## [3] SciPhi-Chat: Training a Spatial Audio Agent for Question Answering, Dialogue, and Tool Use

**arXiv ID**：2611.04114 | **方向**：语音大模型

**作者**：Gijs Wijngaard, Hannes Gamper, Sebastian Braun

**机构**：Microsoft Research（美国华盛顿州雷德蒙德）

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04114 | **PDF**：https://arxiv.org/pdf/2611.04114.pdf | **代码**：https://github.com/microsoft/sciphi-chat | **Demo**：暂无

### 📌 简介
本文提出SciPhi-Chat，一个面向一阶 Ambisonic（FOA）录音、可回答空间问题、进行多轮对话并调用信号处理工具的空间音频智能体。现有音频语言模型多为单声道输入而缺乏方向信息，已有空间模型未同时支持推理、指代式对话与可执行工具调用。模型基于Phi-4-multimodal，用冻结的FOA-VAE空间编码器加LoRA微调，在550万条合成对话上训练，并发布含12,000样本、42类任务的MASU基准。MASU单轮得分44.9%，超此前SOTA 7.4个百分点；外部ASA-Bench上方位角与俯仰角精度达74.5%与60.0%。

### 🔧 技术方案

**问题背景：** 空间音频问答需将声音身份与方位、距离绑定并推理源间关系，但主流ALM用单声道音频丢失方向线索；BAT、Spatial-Omni、Sci-Phi等空间模型或仅支持固定模板问答、或不建模后续指代对话与工具调用，且现有基准任务覆盖窄（ASA-Bench 18任务、SO-Bench 16子任务）。

**模型架构：** 输入为AmbiX格式FOA（ACN序[W,Y,Z,X]，SN3D归一化，零填充至30 s，最多10个方向源加环境背景）。29.6M参数四通道卷积VAE（FOA-VAE）以7.8 Hz输出512维空间向量并全程冻结；三层空间投影器（12.6M可训练）将其映射为空间嵌入；W通道并行经Phi-4-multimodal冻结的441M Conformer语音编码。解码器为约4B级Phi-4-multimodal LLM，在注意力与前馈投影上加rank-16 LoRA（6.9M可训练）。统一输出格式：首回合产出推理段、结构化场景描述JSON（各源方位/俯仰/距离/电平与混响信息，留驻上下文供后续指代）与答案，并可发出tool_call调用四个固定工具（声强矢量计数与定位、直径优势检测定位、W通道门限活动检测），观测以tool_response回注续写。

**核心创新：** (1)首个在单一训练界面内融合空间多轮问答、中间推理与可执行工具调用的空间音频模型，后续问句可引用先前识别的声源。(2)推出MASU基准：12,000样本、42类9组，含反事实、视角旋转、起始-方向绑定等9类现有工作未覆盖任务，并含2,005条STARSS23真实录音检验sim-to-real迁移。(3)多LLM合成对话管线：6个LLM生成推理轨迹，正则校验拦截无依据数值、答案泄漏、非法工具引用，6次失败剔除场景。

**训练策略：** 两阶段：预训练用10M音频-JSON对将backbone适配至FOA-VAE；智能体阶段在5.50M对话/1.93M场景（每类≥0.5%）上微调LoRA，损失仅计assistant token，用户提示与工具返回mask。音频由pyroomacoustics鞋盒房FOA RIR卷积单声道素材（Freesound、BBC、Common Voice 8语种、FMA等）合成。WSD调度：1%线性预热，稳定期LR 1e-5、全局batch在0.9M样本后从40增至256再续5.53M样本，其后1.5M样本线性衰减至0；训练约8块B200 GPU×4天。

### 📊 实验结果
**数据集**：MASU（12,000样本：单轮3,000，对话轨9,000轮/3,000段三轮会话；真实2,005、合成9,995）；外部ASA-Bench L1空间物理4任务220题

**主要指标**：
- MASU单轮总分44.9%，vs Sci-Phi+Qwen3.5-4B的37.5%与Spatial-Omni的30.3%，领先最强基线7.4个百分点；方向组60.1%（俯仰角67.1% vs 基线31.6%）
- MASU对话轨36.7%，超最强基线Qwen2.5-Omni（28.2%）8.5个百分点
- ASA-Bench：方位角74.5%（TWNM-SAPO为54.5%）、俯仰角60.0%、环境声学85.5%（vs 69.1%），距离47.3%为短板
- 消融：去掉推理段使ASA-Bench降17.4个百分点而MASU仅降1.88；强制调用工具平均降5.1个百分点，但定向调用使计数46.0%→65.1%、首声方向56.7%→73.2%

**是否开源**：论文明确所有材料（模型与MASU基准）将发布于github.com/microsoft/sciphi-chat，FOA-VAE将另行发表；CC BY 4.0许可

### ⭐ 评分：8/10
评分理由：首次将推理、指代对话与工具调用统一进空间音频智能体训练界面，42类任务的MASU基准覆盖度远超现有工作，属实质性系统贡献。实验同时报告内部与外部基准，基线齐全（7个对比模型）、消融细致，SOTA提升7.4个百分点可信。不足在于绝对性能仍低于50%，距离估计与工具自主选择未解决，训练数据完全依赖LLM合成、基准问答亦经LLM改写，存在泄漏风险；整体处于顶会水准的扎实档。

---

## [4] ReListen: Training-Free Evidence Localization in Hour-Long Audio with Frozen Audio Language Models

**arXiv ID**：2611.04480 | **方向**：语音大模型

**作者**：Ming-Hao Hsu, Shujie Liu, Yuxiang Hu, Yuxiang Wang, Yingda Shen, Jinyu Li, Zhizheng Wu

**机构**：香港中文大学（深圳）数据科学学院、Microsoft CoreAI、Microsoft Research Asia

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04480 | **PDF**：https://arxiv.org/pdf/2611.04480.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
小时级音频难以放入音频语言模型上下文，且答案常取决于其中几秒。现有方案要么先转写（丢弃声音、音色、时序信息），要么训练模型回听音频（需为每个新模型重复微调）。本文提出 ReListen：完全免训练，让一个冻结的音频语言模型既做"检索器"又做"回答器"。它用扫描对每个 20 秒窗口的是非对数几率打分，取最高分的 1 分钟作答。在 VoiceGiraffe 上选中片段对标注证据命中率 88.5%（转写检索仅 58.8%），准确率超整段转写 9.2 分；LAT-Bench 时序定位 mIoU 47.7，持平经过训练的 LAT-Audio（46.3）；单卡每题 17.3 秒，比所有文本中介系统快 7-8 倍且显存恒定。

### 🔧 技术方案

**问题背景：** 主流长音频方案在模型前放独立"前端"（ASR 转写后检索/阅读，或音频嵌入检索），让模型退化为文本阅读器，丢掉非语音声音与说话人特质；另一类"重听"系统（LAT-Audio、Echo）需专门训练回听行为，每换模型就得重训。目标是让冻结模型自己搜索音频、无需前端与训练。

**模型架构：** 单一冻结 reader（Qwen3-Omni-30B-A3B-Instruct，贪心解码，16kHz 波形输入）贯穿全流程。组件：(1)扫描器——把录音切成窗口，对每个窗口喂入由问题构造的是非提示，取答案首 token 分布的对数几率 ℓ_i = log pθ(yes) − log pθ(no) 作相关分，不生成文本；(2)原生问题路径——按 ℓ_i 降序、跳过重叠窗口，取满预算窗口按时序拼接、相邻合并并标注起止时间，一次作答；(3)事件区间路径——从最高分窗口向左右扩展连续正分窗口；(4)出现监督扩展——两个 <1M 参数卷积声学检测器（速度/音量 0.63M 读 8 带能量+onset；内容编辑 0.71M 读 40 log-mel）与扫描高分窗口共同提议候选，logistic 校准得存在概率，再按 Poisson-binomial 后验（动态规划）选出第 k 次出现。

**核心创新：** (1)把长音频搜索归约为模型本就能做的小决策——用冻结 reader 自身的是非概率作相关性打分，零训练零前端，窗口独立成批使扫描成本随时长线性、显存恒定且可多卡并行。(2)读 yes 概率而非生成 yes/no 文本，单窗口仅一次前向（A100 上约 24 窗口/秒），扫描检查全录音而回答仅用 1 分钟。(3)针对相关性固有局限（k 次出现无法区分、音量/速度变化扫描分几乎无信息：AUC 仅 0.57/0.79），引入合成编辑训练的轻量声学检测器与 Poisson-binomial 序贯后验，避免阈值计数一次误报即整体偏移。

**训练策略：** 主方法完全 training-free；仅在出现扩展上训练检测器与校准。关键超参：窗口 τ=20s，跳步 δ=10s，预算 b=3（共 60s）；配置在 LongAudioSpan 开发半集选定后不变迁移至其他基准。检测器用 AdamW、one-cycle、峰值 lr 2e-3、weight decay 0.01、batch 32 个 400 秒裁剪、梯度裁剪 1，3 种子集成；合成编辑增益 5-14dB、tempo 0.33-0.67/1.5-3、掩蔽 5-35s。推理每题扫描约 295 次 reader 调用。

### 📊 实验结果
**数据集**：LongAudioSpan（360 段 10-164 分钟，1,080 选择题+180 出现链）、VoiceGiraffe（123 段 35-79 分钟，1,499 题）、LAT-Bench（247 段 ≤30 分钟，1,002 时序定位查询）

**主要指标**：
- 证据命中率（60s 预算）：ReListen 69.2%（LAS）/88.5%（VG），声音题 76.5%；转写检索 BM25 最高 47.8%/58.8%
- 选择题准确率：53.5（LAS）、62.0（VG），比整段转写高 9.2、比均匀采样高 8.5/21.3
- LAT-Bench 定位：mIoU 47.7 vs 训练过的 LAT-Audio 46.3；R@0.3 77.2、R@0.5 50.0
- 效率：单卡 17.3s/题（4 卡 5.6s），快于文本中介 27.6-1124s；扫描定位 3.1s 对比 LAT-Audio 173s；峰值显存 67.8 GiB 恒定
- 出现链得分：扩展 60.7，远超全录音带时标 17.2、Whisper 转写 10.2

**是否开源**：论文未提供代码、模型或 Demo 链接，暂无开源

### ⭐ 评分：7/10
评分理由：创新性扎实——首次证明冻结音频 LLM 可凭 yes 对数几率自检索小时级证据，免前端免训练且显存恒定，工程价值明确；实验覆盖三基准、听读对照、效率与上限分析充分，88.5% 命中率与 47.7 mIoU 持平训练模型说服力较强。局限在于证据仅来自单一 reader 与英/中文语音、出现扩展仍需训练检测器与标注校准、且扫描依赖逐题重跑，整体为高完成度的实质贡献而非范式突破。

---

## [5] Detector-Guided Vocoder Training for Adversarial Text-to-Speech Synthesis

**arXiv ID**：2611.04511 | **方向**：语音大模型

**作者**：Jiayan Cui, Davide Salvi, Paolo Bestagini, Stefano Tubaro

**机构**：米兰理工大学（Politecnico di Milano）电子信息与生物工程系

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04511 | **PDF**：https://arxiv.org/pdf/2611.04511.pdf | **代码**：https://github.com/polimi-ispl/adversarial-tts/ | **Demo**：https://github.com/polimi-ispl/adversarial-tts/（含生成音频样本）

### 📌 简介
针对语音deepfake检测器面临的反取证威胁，本文提出"检测器引导"的对抗TTS框架：冻结声学模型，将冻结的deepfake检测器损失直接并入BigVGAN声码器的微调目标（L_total = L_V + λL_D，λ=0.05），使合成波形天生具备对抗性、推理时无需任何后处理。单目标微调使RawNet2的EER从5.8%升至39.05%，多检测器联合微调推至43.87%（逼近随机猜测上限），未参与训练的AASIST的EER也从0.85%升至23.26%；同时FAD从31.25降至17.81，20人主观听音显示合成质量反而提升。

### 🔧 技术方案

**问题背景：** 音频域对抗攻击长期依赖"生成后"处理（加性噪声、LTI滤波、Hammerstein注入等），对抗环节与合成管线割裂，引入额外计算并可能残留可被更鲁棒取证方法利用的伪影；把规避能力内嵌进合成过程、零后处理产生对抗语音是现有空白。

**模型架构：** 两级级联TTS：声学模型采用增强版FastSpeech2（Utterance/Phoneme级编码器、pyannote说话人嵌入、Conditional Layer、Random Window Discriminators）将文本映射为mel频谱；声码器采用BigVGAN合成22.05 kHz波形。训练三种声码器变体：V（仅原始损失基线）、V^R（RawNet2单目标）、V^RT（RawNet2+TSSD双目标）。检测端为RawNet2、TSSD（白盒参与训练）与AASIST（黑盒仅测试）。微调时声学模型与检测器全部冻结，梯度仅回传更新声码器参数，攻击在离线训练完成，推理延迟与原版完全一致。

**核心创新：** (1)检测器入环的对抗声码器训练：L_D定义为检测器输出与"真"标签的二元交叉熵，以λ=0.05叠加原声码器损失，生成"内生对抗"语音，彻底摆脱波形扰动式后处理。(2)多检测器加权联合优化：L_D推广为Σα_k·BCE_k，迫使声码器抑制跨架构共享的法证痕迹而非过拟合单一模型，显著提升对未见检测器的黑盒迁移性。(3)攻防与音质同向：检测器依赖的合成伪影恰与人耳可感知缺陷相关，对抗微调在降低检测器置信度的同时降低FAD并提升主观真实度。

**训练策略：** TTS在LibriTTS（约260小时、1158说话人、22.05 kHz）训练，丢弃短于3秒音频，90/10划分；BigVGAN微调混合真实mel与合成mel以匹配输出分布。检测器训练用内部均衡数据集251,154条（真实取自LibriTTS，伪造由基线V合成），Adam+交叉熵，超参沿用原始实现。硬件单机RTX 4090。评测协议固定真实音频、仅替换三种声码器生成的伪样本以隔离对抗效应。

### 📊 实验结果
**数据集**：LibriTTS（约260h/1158人/22.05 kHz）；检测器数据集251,154条；三套测试集共享同一真实语音、伪样本分别来自V/V^R/V^RT

**主要指标**：
- 基线检测（对V）：RawNet2/TSSD/AASIST EER为5.8%/3.40%/0.85%
- 单目标V^R：RawNet2 EER 39.05%（AUC 64.58%），TSSD 38.33%，AASIST 21.09%
- 多目标V^RT：RawNet2 EER 43.87%、TSSD 43.31%、未见AASIST 23.26%；RawNet2混淆矩阵TNR=0.946、TPR=0.073，几乎全部合成语音被误判为真
- 音质：FAD 31.25→22.95→17.81（每阶段约25%改善）；20位专家MUSHRA式听音中V^R/V^RT真实度逐步逼近真音频

**是否开源**：是，训练与评测代码及音频样本开源

### ⭐ 评分：7/10
评分理由：将冻结检测器的可微损失注入声码器微调是反取证领域范式级思路转移——从"生成后扰动"转向"生成本身对抗"，实现零推理开销，多检测器提升黑盒迁移性与"攻击-音质同向"两项发现均有洞察价值。实验覆盖白盒/黑盒、客观/主观，对照协议严谨。不足在于仅评估单一TTS管线与受控合成场景，未在LLM-TTS/codec类现代系统验证，防御侧对策讨论有限，属威胁建模创新突出但覆盖面尚窄的实质性贡献。

---

## [6] Confidence-Aware Aggregation for Multimodal Audio Reasoning

**arXiv ID**：2611.04580 | **方向**：语音大模型

**作者**：Michel Olvera, Paraskevas Stamatiadis, Gaël Richard

**机构**：LTCI、S2A 与 IDS 实验室，巴黎电信学院（Télécom Paris），巴黎综合理工学院（DCASE 2026 Workshop）

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04580 | **PDF**：https://arxiv.org/pdf/2611.04580.pdf | **代码**：https://github.com/michelolzam/lalm-self-consistency | **Demo**：暂无

### 📌 简介
语音大模型（LALM）在复杂声学场景推理中单步预测极不稳定：同一音频-问题对因解码差异会给出不同答案。本文提出免训练的推理时"置信度感知聚合"框架：对每题采样 N 条候选推理链，用长度归一化的对数概率自确定性打分，再按 Best-of-N、多数投票、Borda、LSE/SoftLSE 五种规则聚合。在 MMAR 上对 Qwen3-Omni、Qwen2-Audio、Audio Flamingo 3 等四个模型实验，Borda 使准确率随 N=3→16 提升 +3.50pp、LSE 使 ECE 下降 8.77pp，均优于传统多数投票，且在高分歧样本上优势最大（相对 MV +2.8pp）。

### 🔧 技术方案

**问题背景：** LALM 将音频编码器与 LLM 主干耦合做生成式推理，但输出方差大、单步预测不可靠。文本 self-consistency 迁移到音频面临两个隐含假设失效：采样推理路径近似独立、token 级对数概率可校准地反映正确性——音频信号存在重叠声源与弱定位证据，感知错误会直接污染推理链本身。

**模型架构：** 三阶段免训练管线：(1)采样——对每个音频-问题对以温度采样生成 N 条序列并解析出规范答案；(2)打分——对"推理链+答案"拼接的全序列计算自确定性 s(i)=(1/T_i)·Σ_t log p_θ(y_t|x,q,y_<t)，长度归一化消除冗长偏置；(3)聚合——五种确定性规则：Best-of-N 取 argmax 极值选择；Majority Vote 按频次均匀共识；Borda 按 s 降序排名赋幂次权重 w_i=(N−rank(i)+1)^α 后按答案累加；SoftLSE 以温度 τ 做 log-sum-exp 聚合 V_τ(a)=τ·log Σ exp(s(i)/τ)，τ→0 退化为极值选择、α→0 退化为均匀投票，在两类几何之间平滑插值。

**核心创新：** (1)首次系统研究 LALM 多步推理 AQA 的推理时聚合策略族，实证表明置信度作为加权信号远优于作为选择准则——Best-of-N 持续落后于 Borda/LSE/SoftLSE。(2)基于对数概率的打分管线：用 LLaMA 3.1 8B-Instruct 做确定性解析器抽取答案 span（不接触音频与分数），经固定选项精确匹配校验过滤，聚合只在有效答案池上进行。(3)采样预算 scaling 与按分歧度分解分析：以 Agr=max|I_a|/N 将样本分三档，量化各聚合规则的精度与校准增益来源。

**训练策略：** 无任何训练或参数更新，纯 test-time 推理。采样预算 N∈{3,4,8,16}，解码温度从 [0.1,1] 均匀抽固定一组、单次运行内跨样本复用；Borda 的 α 与 SoftLSE 的 τ 在 [0,4] 以 0.25 步长网格搜索。基线为候选池内均匀随机抽取。ECE 采用 10 bins，按方法定义聚合置信度。

### 📊 实验结果
**数据集**：MMAR 音频推理基准（1000 条真实视频来源音频-问答-选项三元组，覆盖 7 类内容与四级分类体系）；评测模型：Qwen3-Omni-Thinking/Instruct（30B/激活3B）、Audio Flamingo 3（7B）、Qwen2-Audio（8.4B）

**主要指标**：
- 准确率缩放增益（N=3→16，跨模型均值）：Borda +3.50pp、LSE +3.35pp、SoftLSE +3.23pp、Majority Vote +2.77pp、Best-of-N +1.11pp；增益在 N>8 后饱和
- 校准增益（ΔECE）：LSE −8.77pp、Borda −7.76pp、MV −7.69pp、BoN −5.06pp
- 高分歧档（N=16）相对 MV 增益：Borda +2.8pp、SoftLSE +2.6pp；MV 自身准确率随分歧从约 67% 跌至约 32%
- 有效性过滤提升答案率：Audio Flamingo 3 +5.26pp、Qwen3-Omni-Instruct +4.60pp

**是否开源**：代码已开源

### ⭐ 评分：7/10
评分理由：首次将置信度加权 self-consistency 系统化引入 LALM 多步音频推理，"置信度宜作权重而非选择准则"的结论清晰且有启发性，完全免训练、即插即用，实用价值高。实验覆盖四个异构模型并给出预算 scaling、校准与分歧度三维分析，论证较充分。局限在于仅评测单一数据集 MMAR、准确率绝对增益约 2–3pp 量级、α/τ 需逐数据集网格搜索，且未探索音频专属不确定性信号，属扎实推进而非突破。

---

## [7] NepTTS-Bench: Native-Speaker Benchmarking and NepaliMOS for Nepali Text-to-Speech

**arXiv ID**：2611.03718 | **方向**：语音大模型

**作者**：Ashish Thapa, Rupak Ghimire, Lekhnath Sharma Pathak

**机构**：Ampixa Labs；Kathmandu University；Tribhuvan University 中央语言学系

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.03718 | **PDF**：https://arxiv.org/pdf/2611.03718.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
尼泊尔语已有多套开源与商用 TTS，却无共享评测基准，各论文测试文本、听音人与协议互不可比。本文提出 NepTTS-Bench：205 句音系学驱动提示（含 77 组最小对立对）、180 名母语者产生的 6,962 条 MOS 评分、7 个 ASR 回环 CER 与 SCOREQ 自动基线，并训练语言匹配预测器 NepaliMOS。关键结果：自动指标与母语判断严重背离（ElevenLabs SCOREQ 第一但人评第四，Piper SCOREQ 第八但人评第二），人评第一为自然语音 3.95，最高合成系统 TingTing Asmita 3.55；NepaliMOS 系统级 ρ=0.90，但 LOSO 迁移降至 0.43。

### 🔧 技术方案

**问题背景：** 低资源语言 TTS 评测缺乏统一测试集、听音池与协议，MOS 高度协议依赖；现有自动指标（SCOREQ、DNSMOS、UTMOS、ASR 回环）主要在高资源语种验证，只奖励"信号干净、易转录"，对尼泊尔语送气/卷舌等音系错误不敏感。

**模型架构：** 基准侧为"提示生成—盲评—多指标交叉"流水线：205 句（147 句构成 77 组最小对立对，覆盖声门送气对立、卷舌-齿音、口鼻元音、gemination、schwa 删除；另 58 句覆盖疑问语调、情感、对比重音、语码混合、绕口令、新闻体），部署语料含 40 个系统/音色音频。NepaliMOS 为纯音频 MOS 预测器：IndicWav2Vec base 编码 → 掩码均值池化得 768 维 clip 表征 → 两层回归头 768→256→1（ReLU、dropout 0.1），底层冻结、顶部 4 层 Transformer 解冻；回归头 197k 参数、可训练主干 28.4M。

**核心创新：** (1)首个音系学接地的尼泊尔语 TTS 基准，最小对立对专门暴露"尼泊尔语模型实际输出印地语发音行为"的失效模式。(2)单一受控协议下的跨类别对比：闭源 API、开源本地、人声参考同池盲评，180 名母语者 1–5 分 MOS，同句刺激间隔至少 3 位、系统身份隐藏，并用 2,000 次 rater 聚类 bootstrap 给出 95% CI。(3)NepaliMOS 及失效边界的诚实量化：同时报告 in-distribution 与 leave-one-system-out（LOSO）迁移，据此给出"新供应商必须人类校准"的使用准则。

**训练策略：** 监督目标为每条唯一音频的 clip 级母语评分均值（MSE 损失）。匹配集 1,697 条唯一 clip，由 5,865 条带音频匹配评分聚合。主 checkpoint 采用分层 90/10 utterance 级划分：1,530 训练/167 验证；差分学习率 1e-4（头）/1e-5（解冻主干），batch size 2。最小对立对经语法与拼写审计，替换 12 组、修正 6 组。统计上用 Spearman ρ、Benjamini–Hochberg 校正、Krippendorff α。

### 📊 实验结果
**数据集**：NepTTS-Bench（205 句、77 最小对立对；40 系统音频；密集面板 10 TTS + 2 人声；180 母语者、6,962 条评分；NepaliMOS 训练 1,697 clip）

**主要指标**：
- 人评 MOS：自然语音 3.95、TingTing Asmita 3.55、Piper 3.50、ElevenLabs v3 3.47、Edge TTS Sagar 3.38、gTTS 2.60
- 与人类 MOS 相关性（n=9，BH 校正）：NepaliMOS ρ=0.90（p=0.001，唯一显著）；ASR CER 类 0.22–0.60、SCOREQ 0.40
- 排名背离：ElevenLabs SCOREQ 第 1 但人评第 4；Piper SCOREQ 第 8 但人评第 2
- 泛化：NepaliMOS in-distribution ρ=0.59 → LOSO ρ=0.43；评分者一致性 α=0.17
- 负向发现：Whisper large-v3-turbo 有 2%–10% 文件 CER>1.0（幻觉），必须做幻觉过滤

**是否开源**：论文承诺录用后释出提示、评分、音频、评测 CLI 与 NepaliMOS；当前无公开仓库链接

### ⭐ 评分：7/10
评分理由：把"音系学最小对立对 + 母语者受控盲评 + 语言匹配 MOS 预测器"组合成可复用基准，并首次量化自动指标与母语判断在低资源语言上的系统性背离，"评测即发现"结论有真实价值。实验在其范围内充分（180 人、6,962 评分、LOSO 与置信区间），且主动报告负面局限，学术诚实度高。不足在于仅覆盖单一语种、密集面板条件数偏少致统计功效低，NepaliMOS 本身为常规 SSL 微调无方法新意，代码数据尚未释出。定位为低资源 TTS 社区的实质基础设施贡献。

---

## [8] Clean-anchored excess-emission control for CTC adaptation under competing speech

**arXiv ID**：2611.03900 | **方向**：语音大模型

**作者**：Yuanbo Zhou, Junjie Xiong

**机构**：Missouri University of Science and Technology

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.03900 | **PDF**：https://arxiv.org/pdf/2611.03900.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对竞争说话人场景下CTC识别器经自适应后易产生"过剩发射"（多余整词插入）的问题，本文提出clean锚定的过剩发射控制：冻结教师模型在配对干净语音上计算期望折叠token数并缓存为标量锚点，学生仅在噪声端计数超出锚点时受单边二次惩罚，推理时零额外模块。仅用147,456个可训练LoRA参数，LibriSpeech锁定测试中语音干扰WER从45.198%降至44.323%，干净WER仅变化0.004点；对未见VCTK干扰说话人改善0.307点。

### 🔧 技术方案

**问题背景：** 重叠语音下主流方案依赖增强信号、说话人条件化或PIT多流输出，需推理时分离或注册音频。作者发现仅用CTC损失对混合语音做自适应常导致过发射（插入词激增），blank-logit校准只能部分缓解，故转而约束"输出范围"而非说话人身份。

**模型架构：** 基座为wav2vec 2.0 Base加CTC头，贪心解码、无语言模型；主干与CTC头全部冻结，仅在第0、1层encoder的query/value四个投影上挂rank-24 LoRA（A为24×768、B为768×24），共147,456参数。训练时冻结教师对干净语音前向一次、按闭式统计量缓存每句一个折叠计数标量；学生以混合语音+目标转写训练，辅助项只作用于被污染样本；推理移除教师与损失，结构与CTC-only基线完全一致。

**核心创新：** (1)期望折叠token计数：对帧级softmax独立采样路径给出折叠后非blank符号数的精确期望L̂(p)=Σ_k p₁(k)+Σ_{t≥2}Σ_k p_t(k)[1−p_{t−1}(k)]；区别于帧质量统计量，能区分连续重复与blank分隔的重复发射。(2)单边clean锚定惩罚：L_ex=[max(0,(L_θ−L_0)/max(L_0,1))]²，仅超出锚点时激活、低于锚点导数为零不干扰CTC梯度，对称版本会误罚欠发射。(3)零开销实现：每句缓存标量避免常驻第二模型，计数量O(T|V|)复用CTC已算logits，无需干净/噪声后验帧对齐。

**训练策略：** 目标语音取Mini LibriSpeech train-clean-5的2小时确定性子集（631句）；每次采样以0.5概率保持干净，否则按0–20dB均匀signal-to-masker比混入MUSAN噪声/音乐/语音干扰。AdamW，lr 1e-4，梯度累积4，400步更新，梯度裁剪1.0，λ=1。blank偏置b在−2~+2以0.25步长搜索，在干净退化≤0.2点约束下最小化池化噪声WER；锁定测试为全部2620句test-clean于0/5/10/20dB、b=0.5；配对bootstrap按目标说话人重采样2000次。

### 📊 实验结果
**数据集**：LibriSpeech（631句训练、2620句test-clean锁定测试）+ MUSAN干扰（0–20dB）+ VCTK 0.92（20说话人600句做未见干扰迁移）

**主要指标**：
- 语音干扰WER：45.198%→44.323%（−0.875点）；池化噪声WER：25.652%→25.311%（95%CI [−0.383,−0.298]）；干净WER仅+0.004点
- 错误分解（vs CTC-LoRA）：插入−1258、替换−1534、删除+640
- VCTK未见干扰：总体WER 42.967%→42.660%（−0.307点，CI [−0.482,−0.112]）
- 训练预算：延至800步时语音差距扩大至−4.782点，但噪声/音乐分别劣化0.414/0.403点，暴露插入-删除权衡

**是否开源**：论文未提供代码链接，暂无

### ⭐ 评分：6/10
评分理由：把"输出范围"作为可从干净教师迁移的utterance级统计量并以单边惩罚规避欠发射，思路精准且推理零开销，属小而干净的机制创新。实验控制极为严谨：匹配基线、三seed复现、锁定测试、成分消融、配对CI与错误分解，且诚实报告噪声/音乐回退。不足是绝对增益小（<1点）、单一基座+合成混合+贪心解码、未与分离或目标说话人方法对比，实用价值主要在于为竞争语音CTC自适应提供可复用的轻量正则基线，属增量但方法论扎实的工作。

---

## 语音前端

## [9] VeriSpoof: Beyond Real or Fake with One Audio LLM

**arXiv ID**：2611.04634 | **方向**：语音前端

**作者**：Yang Xiao, Ting Dang

**机构**：The University of Melbourne（墨尔本大学）

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04634 | **PDF**：https://arxiv.org/pdf/2611.04634.pdf | **代码**：https://github.com/swagshaw/verispoof | **Demo**：https://huggingface.co/spaces/AustinXiao/VeriSpoof-demo

### 📌 简介
现有检测模型只能回答"真或假"，而司法取证还需知道由哪个系统生成、两段音频是否同源、结论依据什么证据。本文提出VeriSpoof，一个2.85B参数（仅训练29.7M）的音频语言模型，用一套权重统一深伪检测、生成器/声学模型/声码器归属、录音条件分析、合成区间定位与来源验证五类任务，把每个取证问题写成候选答案句子并按似然差读为分数，同时以可逐条核验的结构化rationale给出证据。在Speech-DF-Arena的14个测试集上Plus版达2.14% pooled EER，28系统中排第三、开源第一；对未见生成器同源对验证6.2% EER；推理后判定捕获99.6%的PartialEdit局部深伪（一步回答仅78.4%）。

### 🔧 技术方案

**问题背景：** 一个分数只能回答一个问题，来源追溯与成对验证需另训孪生网络；已有音频LLM的解释是教师模型蒸馏的自由文本，既不校验其真实性也不检验决策是否依赖它；且学界未量化ALM瓶颈在编码器表征、特征用法还是LLM。

**模型架构：** 8秒波形（成对任务两段拼接）输入Qwen3-ASR编码器（25层，冻结，仅第一阶段训DoRA adapter，r=16），全部25层隐状态经学习加权融合后送入audio tokenizer，输出两路分辨率：16个utterance token承载全局属性与52个0.16秒frame token保留时间信息，每0.8秒插入文本时间标记，使LLM能以秒陈述区间。LLM为MiniCPM5-2B，LoRA（r=16、α=32）加在注意力投影。总分由正负答案句log似然差给出，无任何任务头；另有OC-softmax单类真伪辅助损失和per-token帧级真假头。

**核心创新：** (1)取证问题统一为答案打分：检测、归属、录音条件、成对同源验证均为"问题+候选答案句"，分数可按操作点阈值化；来源验证集按SAME/REVERSAL/DIFF三层平衡，防止属性匹配捷径。(2)可核验的结构化rationale：观测陈述（SNR、电平、削波、带宽）由dataloader对模型实际接收的波形直接物理测量、定位对照标注span、source profile对照生成器元数据，每条陈述都有不依赖模型的checker；决策写在最后且与定位严格一致。(3)反事实忠实性训练：20%的rationale样本把定位翻转，仅监督其后的决策，教模型"决策必须跟随所给证据"而非陈述虚假观测。

**训练策略：** 三阶段：PA感知对齐（冻结LLM，训tokenizer+DoRA，lr 1e-4）→QT取证问题微调（加LLM LoRA多任务指令）→RT证据rationale微调（lr降至2e-5，重放QT任务）。Base仅用8个语料官方训练集加局部深伪语料约0.38M条；三阶段步数8k/20k/10k，global batch 32，单张48GB GPU约14 GPU小时。Plus再加12个语料共+4.0M条，欺骗侧按211个source、真实侧按18个数据集平衡，PA跑6个平衡epoch（79.2k步、batch 64、双卡）。增强含MUSAN噪声、混响、窄带codec且每样本重采样。

### 📊 实验结果
**数据集**：Speech-DF-Arena 14套（2.34M trials）、SpoofRadar v1.0 16套（含XMAD-Bench七语言）；自建发布VeriSpoof-Bench：54子集177,852条

**主要指标**：
- Speech-DF-Arena pooled/mean EER：Plus 2.14%/1.79%，比次优开源DF-Arena-1B（9.52%）降一半以上，总榜第三（仅次于两个闭源系统）；仅0.38M数据的Base即达4.43%
- SpoofRadar pooled EER：Plus 4.04%、Base 4.23%，最强开源基线9.96%；未见语言XMAD上Base 0.24%
- 来源验证：unseen模型6.17%/unseen架构15.0% EER，对照冻结编码器pair probe的26.5%/24.8%；六个通用音频LLM零样本近chance（Base为95.9%）
- 忠实性：改写翻转定位后99.5%决策跟随（无反事实训练仅73.8%）；受控研究表明表征决定检测、LLM决定比较能力；codec深伪必须加source监督
- 部署：推理约6–7GiB显存，8GB GPU可跑；vLLM批量生成rationale加速46×

**是否开源**：是。两个模型、推理代码（含vLLM后端）、demo与VeriSpoof-Bench全部发布

### ⭐ 评分：8/10
评分理由：将五类取证问题统一为可阈值化的答案打分，并把"可解释"落到有独立checker的证据陈述加反事实忠实性训练，是方法论上的实质推进而非模块堆叠；实验极充分，覆盖两张公开榜单、单变量受控研究与配对bootstrap区间，"表征决定检测、LLM决定比较""codec深伪必须source监督"等结论有直接指导价值。不足在于组件基本沿用现成模型、Plus在未见语言真实音频上存在阈值校准漂移、区间定位IoU仍偏低（0.25–0.61）。

---

## [10] Averaging Collusion Breaks Traceability in Personalized Neural Audio Watermarking

**arXiv ID**：2611.04400 | **方向**：语音前端

**作者**：Yangming Liu, Haiyun Li, Dongfu Song, Ziang Xu, Jiehui Luo, Yining Zhang, Zhiyong Wu

**机构**：清华大学（深圳）

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04400 | **PDF**：https://arxiv.org/pdf/2611.04400.pdf | **代码**：https://github.com/Silwan5z/neural-audio-watermark-collusion-attack | **Demo**：暂无

### 📌 简介
个性化神经音频水印通过嵌入用户专属payload实现泄露溯源，但现有评测均默认攻击者只持有单一副本。本文发现对同一内容的多份合法副本做逐样本平均即可摧毁溯源性：仅平均2份副本，在五个主流系统上溯源失败率达87.7%–99.7%，且音质几乎无损。进一步提出payload感知的Target-Bit Margin加权攻击，可将解码结果定向嫁接到选定非联盟成员，在TimbreWM上目标成功率达92.3%；基于解码器置信度的初步筛查可拦截多数合谋输出。

### 🔧 技术方案

**问题背景：** 神经音频水印的既有鲁棒性评测均假设攻击者逐份处理单个副本，而现实中攻击者可收集同一录音的多份带不同payload的合法副本；经典扩频水印的合谋码分析无法回答端到端问题：学习式解码器如何映射平均混合信号、输出payload是否仍指向联盟成员。

**模型架构：** 威胁模型：成员i获得 y_i = x + w(x,m_i)，x为共享语音、w为payload相关水印残差。攻击组件一为Uniform Averaging：y̅_K=(1/K)Σy_i = x+(1/K)Σw(x,m_i)，共享语音保留而水印残差相互抵消，攻击者无需干净参考、模型参数或解码器查询。组件二为Target-Bit Margin：以签名支持度 γ_j=(2t_j−1)(Σ_i a_i b_ij−0.5) 度量目标比特j的软支持，最大化各比特margin的soft-min并加熵正则，约束凸混合权重且有效合谋规模 K_eff≥ρK，全程不查询解码器。防御侧为置信度筛查器：用解码器原生的最小置信度、平均置信度与置信度对数方差三个统计量对输出做接受/拒绝。

**核心创新：** (1)首个系统性多副本合谋评测：覆盖三个bit-based系统（AudioSeal、WavMark 16-bit，TimbreWM 10-bit）与两个latent-based系统（VoiceMark、WMCodec 16-bit），K∈{2,3,5,8}每格300次试验，并验证时移与有损编码下失效持续。(2)解码器归因行为分析：对照经典interleaving的理想bit-choice参考，量化各系统对联盟bit support的响应差异，并通过cross-bit耦合实验揭示latent-based系统会连带破坏双方一致的比特。(3)可控定向嫁接到初步防御：Target-Bit Margin使bit-based系统输出可被操纵指向选定非成员，而置信度筛查可将其大幅压制。

**训练策略：** 不训练新模型，直接作用于预训练水印系统原生采样率（AudioSeal/WavMark/VoiceMark 16kHz、TimbreWM 22.05kHz、WMCodec 24kHz）。Target-Bit Margin超参数：逆温度8、熵权重0.05、ρ=0.6跨系统固定；每trial按soft-min margin选Top-10非成员目标，K=5/8下各统计300×10次尝试。筛查阈值按说话人五折交叉验证（80%校准/20%测试），校准至保留≥95%合法单副本输出。

### 📊 实验结果
**数据集**：300条10秒录音、100位说话人（每人3条），AISHELL-3与LibriSpeech各占一半

**主要指标**：
- 均匀平均溯源失败率（K=2）：AudioSeal 99.0%、WavMark 96.7%、TimbreWM 87.7%、VoiceMark 93.7%、WMCodec 99.7%；PESQ 4.20–4.60、STOI 0.983–0.999，音质近乎无损
- 鲁棒性变体：K=5下±10/20/50ms时移平均TF仍>96.5%；MP3 128kbps/Opus 64kbps编码后TF 96.5%–96.9%
- 定向误嫁成功率（K=8）：TimbreWM 92.3%、WavMark 54.4%、AudioSeal 43.6%，latent-based两系统仅约1%
- 防御后：单副本接受率94.3%–95.0%，bit-based系统均匀平均输出100%被拒，TimbreWM目标成功率92.3%→0.0%，五系统残留最高4.4%

**是否开源**：代码与结果已在GitHub开源

### ⭐ 评分：7/10
评分理由：首次将多副本合谋确立为神经音频水印的独立评测维度，攻击实现极简（逐样本平均）而破坏力显著，跨系统解码器归因分析与定向嫁接实验均有深度，结论对AIGC音频溯源部署具直接警示价值。不足在于数据规模有限（300条录音）、未评测长音频与更多codec条件，防御仅为初步置信度筛查，尚未提出根本抗合谋的水印方案；整体属实验充分、有实质贡献的安全分析型工作。

---

## [11] Attendance-guided speaker enrollment across meetings

**arXiv ID**：2611.04394 | **方向**：语音前端

**作者**：Minjae Lee, Hee-Soo Heo, Youngki Kwon, Bong-Jin Lee

**机构**：NAVER Cloud Corporation（韩国）

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04394 | **PDF**：https://arxiv.org/pdf/2611.04394.pdf | **代码**：暂无（承诺发布基准生成器与评测代码，尚无URL） | **Demo**：暂无

### 📌 简介
说话人感知应用依赖注册语音档案，但让每位参会者专门录制注册音频不现实。本文将会议档案（diarized 匿名说话人簇+会前邀请名单元数据）交叉比对，为常参会者自动提取注册语音，正式化为"多参与者自动注册"任务，需处理两类名单噪声：listed 但沉默（inclusion）与发言但未被列出（omission）。作者提出基于 VoxBlink2、按 63 场内部会议语料校准的合成基准与污染敏感评测协议，并给出单阈值的跨会话链打分参考方法。合成集上 10% 污染预算达强成功率 35.16%/污染 9.34%，但阈值直接迁移到真实会议仅 8.00%/4.00%，暴露显著的合成-真实差距。

### 🔧 技术方案

**问题背景：** 注册档案通常被下游研究默认为干净已知，而真实系统需自行构建；已有元数据辅助注册工作仅针对录音者本人且无定量评测与公开基准。现有公开会议语料无法同时提供跨会话一致的说话人身份、足够的复现与出勤变化、以及独立收集的预期出勤名单。

**模型架构：** 免训练四阶段流程。每场会议提供音频与名单，前端（假设 oracle 会话内聚类、去除重叠语音、丢弃 <4 s 短段）产出匿名簇。(1)链构建：以任一簇为种子，逐场选取与种子段组成对余弦相似度最高的簇构成跨会话链；(2)出勤对比打分：参与者-链关联分数=名单所列会话的链平均相似度−未列会话的平均相似度，均值归一化避免偏向高频列名者；(3)全局一对一指派：对列名 ≥m=3 场的参与者用匈牙利算法匹配链，分数低于阈值则拒绝，出勤模式重名的两个名字均弃权；(4)注册段选择：保留链中该参与者列名会话的簇，池化嵌入取距均值嵌入余弦最近的 3 段。声学表征为预训练 ReDimNet2-B3（VoxCeleb2 训练，attentive statistics pooling 输出 192 维嵌入），不做基准特定训练。

**核心创新：** (1)首次形式化多参与者自动注册任务并给出污染敏感协议：在开发集上按污染预算 ε 选阈值、原样应用到评测集，报告污染-成功曲线与饱和点。(2)合成基准按内部语料校准出勤统计（63 场/84 人、每场中位 6 人、63.8% 说话人对永不同场、inclusion/omission 率 13.5%/8.3%），设 main/clean/inclusion-only/omission-only 四条件隔离两类噪声机制。(3)参考方法仅含一个可调阈值，并定量分析合成开发阈值向真实会议迁移的 synthetic-to-real gap。

**训练策略：** 无损失函数与梯度训练，仅做阈值选择：每条件在 12 个开发 episode 上池化计数、最大化强成功且满足污染预算，平局依次用弱成功与段召回打破；评测集 36 个 episode，与开发集说话人不相交，main 条件 2099 个目标。每名字最多输出 3 段。

### 📊 实验结果
**数据集**：合成基准（基于 VoxBlink2，每 episode 63 场、84 候选身份，12 dev/36 eval）；内部真实会议语料（63 场、84 人，评测群体 50 人，名单来自独立记录的邀请元数据）

**主要指标**：
- 合成评测 main 条件：0 预算强成功 1.00%/污染 0.00%，10% 预算 35.16%/9.34%，20% 预算 50.83%/18.82%，饱和 51.50%/21.53%
- 对照条件：clean 20% 预算 51.82%/11.11%；inclusion-only 饱和 54.28%/22.46%；omission-only 饱和 49.42%/11.34%
- 关键对比：合成→真实阈值直接迁移：10% 预算下 35.16%/9.34% 跌至 8.00%/4.00%，真实标签重拟合仅恢复到 22.00%/8.00%；用 HEE 说话人分离系统替换 oracle 聚类，饱和强成功约下降三分之一

**是否开源**：暂无（承诺发布基准生成器、manifests、配置与评测代码；内部语料与名单不公开）

### ⭐ 评分：6/10
评分理由：首次定义并基准化"从噪声出勤名单为多名常参会者抽取具名注册语音"这一实用问题，污染敏感协议与四条件噪声隔离设计专业规范，参考方法简洁可解释，作为评测基建成有实质贡献。但方法本身免训练、偏 baseline，创新性有限；真实验证仅依赖单一私有 63 场语料、评测群体只有 50 人，置信度不足；低污染预算下绝对成功率仅 1%–4%，且合成-真实鸿沟被作者确认为未解决的开放问题，实用性尚远。

---

## [12] Cross-Codec Robustness in Speech Watermarking

**arXiv ID**：2611.04716 | **方向**：语音前端

**作者**：Olli-Pekka Pauna, Xin Wang, Lauri Juvela

**机构**：阿尔托大学信息通信工程系（芬兰）、日本国立信息学研究所（东京）

**发布日期**：2026-11-04 | **论文**：https://arxiv.org/abs/2611.04716 | **PDF**：https://arxiv.org/pdf/2611.04716.pdf | **代码**：https://github.com/ljuvela/DAREA | **Demo**：暂无

### 📌 简介
深度语音水印虽可抗传统DSP攻击，却极易被神经音频编解码器重合成消除，且针对单一codec训练的鲁棒性难以泛化到未见codec。本文提出以Descript Audio Codec（DAC）为生成器、AASIST为检测器的零比特水印系统，并系统研究训练时"神经codec信道增强"的选择如何影响跨codec鲁棒性。实验表明Mimi+SNAC双codec增强对未见神经codec与DSP攻击泛化最广：EnCodec 12kbps攻击下TPR@1%FPR达97.90%，Mimi攻击83.60%，远超AudioSeal（1.30%）与WavMark（0.21%）；音质CMOS为-0.092±0.300、PESQ 4.385，与自然语音几乎无差。

### 🔧 技术方案

**问题背景：** 欧盟AI Act等法规强制对AI生成语音做主动标识，协作式水印靠训练时信道增强求鲁棒，但现有模型面对未见的神经codec重合成、声码器、降噪攻击仍大面积失效；codec架构与训练差异导致重构行为不同，何种增强配方能泛化到未见codec尚无结论。

**模型架构：** 零比特全局水印管线：冻结预训练DAC（24kHz、stride 320、32码本×1024、24kbps）的编码器与量化器（保持码本向后兼容），仅微调解码器得x_wm；检测器用预训练AASIST并去除BatchNorm与dropout以强化对抗训练；水印目标为最小二乘GAN损失 L_W=E[(1−D(C(x_org)))²+D(C(x_wm))²]，C(·)为冻结神经codec信道增强；生成器总损失λ_Mel=15、λ_Adv=1、λ_Fm=2、λ_W=1。作者修改EnCodec/SpeechTokenizer/Mimi官方源码，使STE量化在冻结推理模式下仍可端到端反传，该增强工具已开源。

**核心创新：** (1)新型DAC生成器零比特水印系统，编解码重构质量高且码本兼容下游codec语言模型。(2)首次横向量化7种增强配方对未见攻击泛化的影响，提出低码率高音质codec（Mimi 1.1kbps、SNAC 0.98kbps）的窄瓶颈迫使水印嵌入信号更本质成分、隐式逼近跨codec共享潜空间的机制假设。(3)Mimi+SNAC双codec增强（每mini-batch随机选一）取得最宽泛化，并开源通用神经codec信道增强实现。

**训练策略：** 基础DAC在LJSpeech+VCTK+LibriTTS-R clean-train-100上按默认配方训练100万迭代、batch 4（单A100）；水印微调用LibriTTS-R train-clean-100共40k迭代、batch 8、样本裁剪/补零至1秒；AdamW（β1=0.8, β2=0.99），权重初始化后重置优化器与LR调度器；以250样本dev-clean子集EER选最佳模型。7个变体：无增强、EnCodec 6kbps、DAC 8kbps、SpeechTokenizer 4kbps、Mimi 1.1kbps、SNAC 0.98kbps、Mimi+SNAC双增强。

### 📊 实验结果
**数据集**：LibriTTS-R test-clean抽1000条（最长10秒）；攻击含8种神经codec（含未见NanoCodec 1.89kbps）、MP3/Vorbis/Opus多码率、MUSAN加噪、MIT RIR混响、低通/高通滤波及codec顺序重合成；主观评测29条语句、Prolific平台28人中26人通过注意力检查

**主要指标**：
- TPR@1%FPR（Mimi+SNAC双增强对未见攻击）：EnCodec 12kbps 97.90、DAC 8kbps 98.00、Opus 32kbps 92.40、MP3 64kbps 96.90、NanoCodec 77.20、SpeechTokenizer仅62.60、两codec顺序重合成50.90
- 关键对比：Mimi攻击下83.60 vs AudioSeal 1.30/WavMark 0.21；AudioSeal/WavMark对多数神经codec攻击普遍崩溃（约0.2-2.2%）
- 音质：CMOS（对自然语音）双增强-0.092±0.300、PESQ 4.385，AudioSeal -0.138/4.339，WavMark -0.292/4.133

**是否开源**：信道增强实现开源，水印模型权重未见发布

### ⭐ 评分：6/10
评分理由：核心发现"增强codec选择显著决定跨codec泛化"对水印鲁棒性研究与AI Act合规落地有实际指导价值，开源增强管线是可直接复用的贡献，属实质但偏增量性的工作。系统由DAC、AASIST、codec增强既有组件组合而成，方法创新有限。实验覆盖7变体×约20种攻击并含统计校正的主观评测，较充分；但数据仅英文朗读语音，Mimi与SNAC互不泛化、对SpeechTokenizer/NanoCodec/顺序重合成明显退化，且未评测声码器与降噪攻击。

---

*Generated on 2026-11-06 (补录)*
