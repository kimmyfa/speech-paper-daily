# 2026-09-10 语音论文速递

**共收录**: 25 篇 | **语音大模型**: 10 篇 | **语音前端**: 15 篇

> 目标日期 2026-09-10（北京时间）arXiv 语音相关论文共命中 25 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing

**arXiv ID**：2609.08936 | **方向**：语音大模型

**作者**：暂未知

**机构**：暂未知

**发布日期**：2026-09-08 | **论文**：https://arxiv.org/abs/2609.08936 | **PDF**：https://arxiv.org/pdf/2609.08936.pdf | **代码**：开源（源码与模型权重发布） | **Demo**：暂无

### 📌 简介
AuK 是一个开源语音基座模型，通过自然语言指令与音频上下文这一统一接口，把语音生成与编辑融合为单一框架。作者构建约 30.3 亿条指令-音频实例、195 万小时有效监督数据，覆盖语音生成、内容编辑、增强与分离、副语言编辑、声学编辑五大任务族。模型结合多模态大语言模型语义条件、语音/通用音频/音乐联合训练 VAE 声学条件，以及 dual-stream MMDiT 加 unified single-stream DiT 的混合 rectified-flow 架构。蒸馏所得 AuK-Flash 可实现 4 步推理且无需 classifier-free guidance，相比完整模型获得 4.5 倍墙钟加速，实验表明其在零样本与指令控制语音生成、通用指令编辑上领先，在信号级复原任务上具有竞争力。

### 🔧 技术方案

**问题背景：** 语音生成与编辑长期被拆分为零样本合成、内容替换、去噪分离、音色/风格迁移、声学属性修改等相互独立的子任务，各系统接口与数据结构不兼容、难以组合复用，缺乏统一的指令驱动通用模型。

**模型架构：** AuK 采用条件扩散生成框架：以多模态大语言模型（MLLM）解析自然语言指令与文本/语义条件提供语义控制；以在语音、通用音频、音乐上联合训练的 VAE 提供统一声学隐空间条件；生成主网为混合 rectified-flow Transformer，先经 dual-stream MMDiT 块进行语义与声学条件的双流交互，再进入 unified single-stream DiT 块完成统一生成/编辑解码。

**核心创新：** (1) 统一接口设计，使生成与编辑共享同一指令-上下文范式并覆盖五大任务族。(2) dual-stream MMDiT 与 single-stream DiT 的混合架构，兼顾跨模态条件对齐与容量效率。(3) 超大规模多任务预训练，30.3 亿实例与 195 万小时监督支撑通用能力。(4) 训练后优化与蒸馏管线，含一致性初始化与 task-routed Decoupled DMD，产出 4 步采样、免 CFG 的 AuK-Flash。

**训练策略：** 先做仅生成任务 warm-up，再进入生成-编辑联合预训练；后训练采用两路互补策略：对开放式编辑应用人类反馈偏好优化（HIFO 类），对语音生成应用 reward-based 强化学习；最后经蒸馏压缩推理成本。

### 📊 实验结果
**数据集**：五类任务约 30.3 亿指令-音频实例、195 万小时有效监督（技术报告，各 benchmark 定量细节未在摘要中披露）

**主要指标**：
- AuK-Flash：4 步推理、无需 CFG，相比完整模型 4.5 倍墙钟加速
- 零样本与指令控制语音生成、通用指令编辑：领先水平
- 信号级复原任务（增强/分离）：竞争力良好

**是否开源**：开源（源码与模型权重均已公开）

### ⭐ 评分：8.5/10
评分理由：以统一指令接口覆盖五大任务族并配套超大规模数据与开源权重，系统性与工程完整性突出，对领域有较强示范价值；训练后处理（偏好优化、RL、一致性初始化+task-routed Decoupled DMD 蒸馏）设计精巧，AuK-Flash 4 步免 CFG 推理与 4.5 倍加速具备实际落地意义。扣分点为技术报告未在摘要中披露 benchmark 定量结果，创新侧重工程集成而非全新机制。

---

## [2] TamilEOT: A Dataset and Model for Semantic End-of-Turn Detection in Tamil Telephone Speech

**arXiv ID**：2609.05631 | **方向**：语音大模型

**作者**：暂未知

**机构**：暂未知

**发布日期**：2026-09-04 | **论文**：https://arxiv.org/abs/2609.05631 | **PDF**：https://arxiv.org/pdf/2609.05631.pdf | **代码**：开源（数据、权重、代码公开） | **Demo**：暂无

### 📌 简介
语音代理必须在每个停顿处裁决用户是否说完，无语言模型时只能退化为固定静默超时。本文发布 TamilEOT 数据集（从 116 段真实泰米尔电话通话切出 18,485 条标注 turn 边界）及两个 audio-only 检测器（自 Smart Turn v3 微调，8.7MB 与 21MB）。在来自 30 通未见电话的 4,168 条 held-out 上，精度由零样本 70.30% 升至 83.71%/86.13%，ROC-AUC 由 0.751 升至 0.921，单线程笔记本 CPU 延迟低于 150ms，并诚实公开数据构建成本与负面结果。

### 🔧 技术方案

**问题背景：** 语义端轮（EOT）检测是语用层面判断，单纯静默时长是表面近似；现有开源语义 EOT 检测器均以英语等大语种为主，南印度语言完全空白。作者以实验揭示规则标签与模型任务不等价：规则在正类命中 95.9% 但负类仅 44.4%（低于随机），因规则回答的是"是否存在长静默"而模型需回答"用户话语是否完成"。

**模型架构：** 数据集层面，从 116 段真实泰米尔电话通话切出 18,485 条带标注 turn 边界，训练/评测按通话而非按 clip 划分，避免同通话泄熵。模型层面，两个仅音频检测器（8.7MB 与 21MB）由 Smart Turn v3 微调，满足 <150ms CPU 实时与轻量部署要求。

**核心创新：** (1) 首个面向南印语言的开放语义 EOT 数据集与检测器，填补语种覆盖空白。(2) 用 audio-LLM 标注管线（人工一致性 97.5%，仅 5.69 美元）替换不可用的规则标签，证明语义标注可低成本规模化。(3) 系统报告成本与负结果：规则负类低于随机、同配置同 seed 三连运行 0.87 点跨度作为显著性下限、生产链路 VAD+流式适配损失 2.60 点且 7.8% 边界从不呈现给模型。

**训练策略：** 自 Smart Turn v3 微调；系统性消融训练杠杆发现只有编码器容量能推动结果；同一批标注边界经生产 VAD 与流式适配重放后精度再降 2.60 点，量化从仿真到真实部署的落差。

### 📊 实验结果
**数据集**：TamilEOT（4,168 条 held-out，来自 30 通未见电话）

**主要指标**：
- 精度：70.30%（零样本）→83.71%（8.7MB）→86.13%（21MB）
- ROC-AUC：0.751→0.921
- 延迟：<150ms 单线程笔记本 CPU

**是否开源**：开源（数据、权重、代码及全部负结果公开）

### ⭐ 评分：8.5/10
评分理由：数据与轻量检测器直接补齐南印语言语义 EOT 空白，从数据、标注到部署的闭环完整、实用价值突出；把规则标签失效、显著性与生产链路落差量化公开，这种诚实报告在研究中罕见。局限为骨架沿用 Smart Turn、缺乏核心算法创新，但工程完整度与可复现性足以建立低资源 EOT 研究基线。

---

## [3] X2Streaming-ASR: wait when uncertain, emit when ready for streaming ASR

**arXiv ID**：2609.08672 | **方向**：语音大模型

**作者**：Zhiwei Lin, Kaiqi Fu, Rime Wen, Zehan Liu, Shawn Qin, Roy Gan, Hao Wang, Qian Wang

**机构**：暂未知

**发布日期**：2026-09-08 | **论文**：https://arxiv.org/abs/2609.08672 | **PDF**：https://arxiv.org/pdf/2609.08672.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对实时语音代理与全双工对话场景，流式 ASR 需提供低 commit 延迟的准确 partial 结果。现有系统多采用固定 chunk、固定 look-ahead 或目标延迟，未显式优化"在单遍硬 commit 约束下每个输出位置该等多少额外上下文"。本文提出 X2Streaming-ASR，将流式识别解耦为"何时 commit"与"commit 什么"，三阶段训练首先建立流式识别能力，再用自动探测轨迹热启动 commit 策略，最后以字符级、段分配的 group-relative rewards 优化准确率与延迟。在 AISHELL-1/2/3 与 WenetSpeech 上平均字符级 commit 延迟降至 27-84ms（基线 409-585ms），并在 AISHELL-1/3 上取得最佳流式 CER。

### 🔧 技术方案

**问题背景：** 流式 ASR 的核心矛盾是准确率与延迟的权衡：等待更多上下文可降低歧义但增加延迟，过早输出则需回改。主流方案（固定 chunk 的 Transformer/Conformer streaming、可配置 chunk size、固定帧数 look-ahead、MRT/min-ALG 等最小延迟训练）均为全局统一的延迟-准确率折中，无法逐输出位置自适应决策，尤其在"硬 commit 单遍输出"约束下（一旦发出不可修正）如何按位置动态决定等待时长仍是开放问题。

**模型架构：** 方法基于 streaming speech encoder + 可延迟解码框架，核心为独立 commit policy 根据当前解码位置置信度与上下文风险决定延后输出，解码器负责"what to commit"。整体由三阶段训练完成。

**核心创新：** (1) "when to commit"与"what to commit"显式解耦，避免时机决策与 token 生成耦合导致的延迟-准确率难以分别优化问题。(2) 自动探测轨迹驱动策略热启动，预设在多种延迟档位下的 rollout 探测获取监督轨迹，使 commit 策略无需随机初始化即可学习合理等待行为。(3) 字符级、段分配的 group-relative reward 精细优化，在字符位置与语音段粒度对齐，用相对奖励规避绝对奖励尺度问题，对识别准确率与 commit 延迟联合建模。

**训练策略：** 三阶段 pipeline：先训练基础流式识别能力（保证前缀上下文产生 partial），再以探测轨迹热启动 commit 策略，最后用 character-level、segment-assigned 的 group-relative rewards 细化策略。摘要未披露损失权重与 RL 算法细节。

### 📊 实验结果
**数据集**：AISHELL-1/2/3, WenetSpeech

**主要指标**：
- 平均字符级 commit 延迟：27-84ms（vs 基线 409-585ms，约一个数量级降低）
- AISHELL-1/3 上取得最佳流式 CER，且延迟显著更低

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：将流式 ASR 的"when/what to commit"显式解耦并结合自动探测轨迹热启动与 group-relative 奖励，创新性与技术完整性突出；commit 延迟较基线降低约一个数量级并同步取得更优流式 CER，验证了方法在 4 个中文公开数据集上的普适性。局限为摘要未给出绝对 CER 数值与 CER-延迟曲线，实验集中于中文数据集，多语言与噪声场景迁移性待验证。

---

## [4] What Did I Just Say? Self-Listening for Full-Duplex Speech Models

**arXiv ID**：2609.05592 | **方向**：语音大模型

**作者**：暂未知

**机构**：暂未知

**发布日期**：2026-09-04 | **论文**：https://arxiv.org/abs/2609.05592 | **PDF**：https://arxiv.org/pdf/2609.05592.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音对话模型中，文本生成、语音合成与音频播放异步进行，导致模型"以为已说的内容"与用户实际听到的播放内容不一致，中断后难以合理恢复，即 anchor interruption 问题。本文提出 Self-Listening 方法，将用户语音、模型文本与模型实际播放的语音交织为统一输入流，把已播放语音反馈给模型，使中断恢复基于用户实际听到的内容。配合新构建的 AnchorSpeech 数据集（同质 train/test 划分），实验表明引入自听机制的模型 anchoring 表现优于全双工基线。

### 🔧 技术方案

**问题背景：** 全双工模型能在说话的同时持续监听，实现对打断与 backchannel 的实时响应。但文本解码、TTS 合成到最终播放三者异步推进，在被打断瞬间模型内部分词进度与实际播放进度存在漂移，模型"记忆"的已说话内容与用户真实听到的内容不一致。作者将"从中断中恢复、同时保持对模型已实现语音的感知"形式化定义为 anchor interruption 问题。

**模型架构：** 基于多流交织的全双工建模：将用户语音流、模型文本流与模型实际播放语音流交织为统一输入序列，已播放语音作为额外输入信号流反馈给模型，为中断恢复提供关于"用户究竟听到了什么"的 grounding 信息。

**核心创新：** (1) Self-Listening 自听机制：将实际播放的合成语音作为输入流反馈给模型自身，模型不仅听用户、也"听自己说出的声音"，这是对现有全双工输入流构成的关键扩展。(2) AnchorSpeech 数据集：面向 tracking/anchoring 任务构造，含同质 train/test split，标注有序结构化响应中"已实际说出的条目"，AnchorSpeech-test 评测模型在任意中断点后能否与最后完成条目保持一致地继续响应。

**训练策略：** 在 AnchorSpeech 训练子集上学习在交织输入流中正确追踪已说话条目进度；采用与测试同质的构造方式避免分布漂移导致对 anchoring 能力的虚高估计。具体 loss 与超参摘要未披露。

### 📊 实验结果
**数据集**：AnchorSpeech（含 AnchorSpeech-test 同质测试集）

**主要指标**：
- 配备 self-listening 机制的模型相比全双工基线在 AnchorSpeech-test 上取得更好的 anchoring 性能（摘要未披露精确数值）

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：将"模型听到自己说过的内容"从数据层面解决方案化，切中全双工系统因异步播放导致中断恢复失准的关键痛点，贡献评测基准 AnchorSpeech（同质 split 设计科学）。不足在于摘要未披露自听机制的建模细节、量化实验数字与消融证据，方法验证限于自建数据集，若补充规模消融与开放域泛化结果，实用价值很高。

---

## [5] KABURI-TTS: Phoneme-Keyed Activity-conditioned Bi-channel Utterance Rendering for Interaction

**arXiv ID**：2609.07200 | **方向**：语音大模型

**作者**：暂未知

**机构**：暂未知

**发布日期**：2026-09-07 | **论文**：https://arxiv.org/abs/2609.07200 | **PDF**：https://arxiv.org/pdf/2609.07200.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工口语对话需大量"双通道、一说话者一通道"的会话语音数据，现有会话式 TTS 对双方同时发生的 backchannel、打断与重叠等自然对话现象不鲁棒。本文提出 KABURI-TTS：以 per-speaker 音素栅格为输入，在独立通道上渲染两位说话人的语音，并逐帧以说话人音素及其推导的 voice activity 为条件。主观评测表明其在 utterance 级与 interaction 级自然度上均优于强基线，voice activity 分析证实其产生更多重叠与更频繁的 turn-taking。

### 🔧 技术方案

**问题背景：** 真实全双工对话中双方会重叠发言、插入 backchannel 并用打断切换话轮，而主流会话 TTS 通常按轮次串行合成，难以复现这类同时性现象；双通道、逐说话人分隔的会话数据集采集成本高、规模有限，进一步制约模型对重叠语音的建模能力。

**模型架构：** KABURI-TTS 将两位说话人的语音在独立通道上渲染，输入为 per-speaker phoneme raster（按说话人分开的音素时间栅格）；生成过程逐帧以当前说话人的音素序列及由音素推导出的 voice activity 为条件，双通道输出天然保留每路声学独立性，便于叠加实现真实重叠而非两路轮流拼接。

**核心创新：** (1) Phoneme-keyed 条件机制：以 per-frame 音素及其推导的 voice activity 作为逐帧生成条件，实现内容与说话活动的细粒度对齐，使模型能感知对方是否在说话并相应产生 backchannel/打断等反应。(2) Bi-channel rendering：两说话人在独立通道合成，输出侧形成一通道一说话人的立体对话，重叠可在声学上自然叠加而非串行拼接。(3) 模块化解耦输入：音素栅格由外部独立模块供给，TTS 本身不承担 ASR/对话状态理解，可灵活接入上游语言理解模块实现可控双人对话渲染。

**训练策略：** 音素栅格来自配对的双通道会话数据；voice activity 由音素栅格推导使标注自洽、无需额外标签。训练 loss 细节（mel 回归、波形域损失等）摘要未披露。

### 📊 实验结果
**数据集**：双通道、one-speaker-per-channel 对话语料（名称未在摘要给出）

**主要指标**：
- 用户评测：utterance 级与 interaction 级自然度均优于强基线
- voice activity 分析：产生更多重叠与更频繁 turn-taking

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：以 phoneme raster + voice activity 条件的双通道渲染解决会话 TTS 对重叠/backchannel 不鲁棒的痛点，设计简洁且模块化解耦、可控性强，契合全双工交互场景。扣分点为摘要缺少客观指标（无 MOS 数值、无重叠率统计）、未披露数据集规模与 baseline 细节，音素栅格依赖上游模块的误差传播与端到端性待全文验证。

---

## [6] Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering

**arXiv ID**：2609.08204 | **方向**：语音大模型

**作者**：暂未知

**机构**：暂未知

**发布日期**：2026-09-08 | **论文**：https://arxiv.org/abs/2609.08204 | **PDF**：https://arxiv.org/pdf/2609.08204.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
Instruct-TTS 通过 LLM 将结构化风格标签改写为自然语言指令用于训练，但研究发现超过 40% 的无约束改写存在语义漂移，污染监督信号并削弱泛化能力，作者将其形式化为 instruction supervision instability 问题。提出的数据为中心稳定方案通过可控指令多样化、LLM 漂移过滤、attribute 对齐监督三机制同时提升覆盖度与保真度。在 InstructTTSEval 中文 split 上，指令跟随率从无微调 34.5%、naive 微调 51.0% 提升至 56.4%，漂移率从 40.4% 降至 15.4%。

### 🔧 技术方案

**问题背景：** Instruct-TTS 用 LLM 改写把结构化 style 标签展开成自然语言训练指令，期望模型学到"指令-韵律"对应关系。但无约束改写极易产生语义漂移（标签指定风格被弱化/替换/引入未标注属性），改写结果与真实音频语义不符，形成矛盾监督，即 instruction supervision instability：指令覆盖不足与单条指令失真的双重不稳定。

**模型架构：** 数据为中心的稳定方案三机制。其一，controllable instruction diversification：在受控约束下系统扩充指令覆盖面，生成多样但语义一致的改写。其二，LLM-based drift filtering：利用 LLM 识别并过滤发生语义漂移的指令，从源头控制监督噪声。其三，attribute-aligned supervision：将韵律控制指令 grounding 到可执行的声学 perturbation 上，使模型所学属性与声学变换之间建立显式对齐。

**核心创新：** (1) 可控指令多样化与"更多改写即更好"的主流思路相反，强调约束下系统性扩充，避免随机改写引入新漂移。(2) 显式漂移过滤使数据管线具备质量闸门，LLM 改写既是合成器也是审核器。(3) attribute 对齐监督首次把韵律控制指令锚定到具体声学扰动上，降低模型从噪声看齐中学错映射的风险。消融证明三机制互补。

**训练策略：** 在 InstructTTSEval 中文 split 上全流程微调；数据侧采用 constrained rewriting（保留原标签语义约束下生成指令），使语义漂移从 40.4% 显著降至 15.4%。

### 📊 实验结果
**数据集**：InstructTTSEval（中文 split）

**主要指标**：
- 指令跟随率：34.5%（无微调）→51.0%（naive 微调）→56.4%（本方法）
- 语义漂移：40.4%→15.4%（constrained rewriting）

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：问题定位精准，"instruction supervision instability"将数据污染形式化并提供可复现度量，方法论既是 TTS 专区也是数据合成通用命题；三机制设计完整且有消融佐证，中文 split 上提升显著。不足为数值证据较薄，未见其他数据集或多语言验证，漂移过滤的漏检边界未量化。

---

## [7] TAD: Token-Adaptive Contrastive Decoding with Confidence-Guided Gating for Hallucination Mitigation in Large Audio-Language Models

**arXiv ID**：2609.07286 | **方向**：语音大模型

**作者**：Heyu Chang, Nianwen Si, Hao Zhang, Wenlin Zhang, Dan Qu

**机构**：暂未知

**发布日期**：2026-09-07 | **论文**：https://arxiv.org/abs/2609.07286 | **PDF**：https://arxiv.org/pdf/2609.07286.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
大音频语言模型（LALM）会幻觉音频对象，对不存在的音事件回答"yes"，损害音频问答可靠性。本文提出 Token-Adaptive Decoding（TAD），一种训练无关的幻觉缓解解码策略：将真实音频 logits 与匹配静音参考对比以锚定首步 yes/no 决策，并引入 token 自适应、置信门控机制（首步决策关键、对肯定类 token 类条件控制），用 audio-silent margin 避免证据弱或已充分时过度矫正。在 AudioCaps-Hallucination 上相对 Audio-Aware Decoding（AAD）基线，Qwen2 F1 提升 0.059-0.117，Gemma 提升 0.025-0.064；Clotho-AQA 上 Qwen2 F1 由 0.810 升至 0.816。

### 🔧 技术方案

**问题背景：** LALM 在音频 QA 中常对 absent 的声音事件输出幻觉性"yes"；现有对比解码类方法（如 AAD）使用全局固定对比强度，对上下文噪声敏感、易过度矫正或矫正不足，难以同时适应证据充分与证据缺失的 token。

**模型架构：** TAD 在首个解码步将真实音频与匹配静音参考的 logits 对比以锚定 yes/no 决策，用"有无声音证据"的差值引导首个二分类 token 的分布修正；引入 token 自适应置信门控，在决策关键的首步与肯定类 token 上做类条件控制，用 audio-silent margin 抑制过度矫正，在假阳性与假阴性间取得平衡。

**核心创新：** (1) 音频-静音对比锚定 yes/no，从统计上抵消模型对肯定回答的先天偏置，为幻觉缓解提供可计算参考量纲。(2) token 自适应置信门控，仅对决策关键步且属于肯定类别的 token 施加针对性修正，其余 token 保持默认解码行为，可叠加到 beam search 或 sampling 流水线而无需重训。

**训练策略：** 完全训练无关（training-free），仅需一次额外前向得到静音参考 logits；对比对象为固定对比强度的 AAD 基线。

### 📊 实验结果
**数据集**：AudioCaps-Hallucination（Popular/Adversarial/Random 三个 split）、Clotho-AQA

**主要指标**：
- AudioCaps-Hallucination：Qwen2 F1 提升 0.059-0.117，Gemma 提升 0.025-0.064（相对 AAD）
- Clotho-AQA：Qwen2 F1 0.810→0.816；Gemma 与 AAD 相当

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：提出训练无关的解码层幻觉缓解思路，将对比强度从全局固定升级为 token 自适应、置信门控，并利用音频-静音 margin 抑制过度矫正，机理清晰、与现有 LALM 流水线兼容性强、落地成本低。跨 Qwen2/Gemma 与两个基准的 F1 提升稳定。扣分点为指标增量有限（Clotho-AQA 上 Gemma 与基线相当），且缺少门控超参敏感性、计算开销及精确率/召回率权衡讨论。

---

## [8] ConversationalVoice: Full-Duplex Speech Data from Real Conversations through Source-Faithful Reconstruction and Conversation-Grounded Expansion

**arXiv ID**：2609.08147 | **方向**：语音大模型

**作者**：暂未知

**机构**：暂未知

**发布日期**：2026-09-08 | **论文**：https://arxiv.org/abs/2609.08147 | **PDF**：https://arxiv.org/pdf/2609.08147.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音模型需要保留 turn-taking、重叠、打断与 backchannel 行为的数据，但这些信号在含噪真实录音中跨说话人纠缠、难以直接使用。本文提出 ConversationalVoice 管线，将真实双说话人片段转化为三类互补训练数据：Separation（说话人分离）、Reconstruction（源忠实重建）与 Expansion（对话 grounded 扩增）。实验显示同说话人相似度 0.983-0.991、判别 margin 0.199-0.209，NISQA MOS 分别为 3.56/4.41/4.61，Gemini 评估者给出扩展数据上下文连贯 4.94/5、对话自然度 4.80/5。

### 🔧 技术方案

**问题背景：** 全双工语音模型训练的关键瓶颈在于：真实对话中 turn-taking、重叠、打断、backchannel 事件天然蕴含在原始波形中，但含噪录音中不同说话人的语音能量在时间与频域上相互纠缠，难以直接形成"干净单说话人+规范时序标注"的训练对；若简单用增强或合成数据替代，又易丢失真实对话中不规则的节奏与交互模式。

**模型架构：** 管线将一段真实双说话人录音转化为三类互补数据产物。(1) Separation：通过信号分离恢复 speaker-specific 音轨，配合稳定说话人分配、canonical transcript 与真实观察到的交互时序，产出最忠实于物理源的样本。(2) Reconstruction：基于固定源 transcript 以匹配音色重新生成语音，重建源对话的 turn 顺序、停顿与重叠，并附字级对齐与 delivery 指令。(3) Expansion：在源上下文、说话人和已观察交互模式约束下生成全新对话内容，用于可控扩增。

**核心创新：** (1) 三段式数据管线将"真实交互结构"与"高质量音质/内容可控性"解耦，三者形成互补。(2) 源忠实重建刻意保留源对话的 turn 顺序、停顿与重叠 pattern，避免生成模型"平滑掉"不规则交互事件。(3) 对话 grounded 扩增以真实对话语境为锚点生成新内容，使扩增数据在内容与结构上都有据可依。

**训练策略：** 论文不训练模型，仅评估数据属性：各阶段用自动说话人验证（SV）指标检验说话人身份保持，NISQA 预测语音质量 MOS，扩展数据由基于 Gemini 的自动评估者按上下文连贯与对话自然度打分。

### 📊 实验结果
**数据集**：真实双人对话片段（具体语料来源与规模摘要未明确）

**主要指标**：
- 同说话人相似度 0.983-0.991，判别 margin 0.199-0.209
- NISQA MOS：separation 3.56 / reconstruction 4.41 / expansion 4.61
- 扩展数据：Gemini 评估上下文连贯 4.94/5、对话自然度 4.80/5
- expansion 相对 reconstruction：turn 率低 4.6%、overlap-event 率低 8.0%、backchannel 率低 13.2%、interruption 率低 16.0%

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：问题定位精准，三段式分离/重建/扩增设计逻辑清晰可复用，评估体系完整（音频质量、说话人一致性、文本层面交互统计与 LLM 对话质量多维交叉验证），并诚实交代"仅评估数据属性、下游增益留待未来"。扣分点为摘要未交代语料来源与规模、分离/重建具体模型，且 expansion 在 backchannel 与 interruption 两项上明显偏低，真实交互结构仍有折损。

---

## 语音前端

## [1] Noise Adaptive Streaming Audio-Visual Speech Token Enhancement for Robust Full-Duplex Spoken Dialogue Models

**arXiv ID**：2609.08390 | **方向**：语音前端

**作者**：Bella Godiva, Yeonju Kim, Yong Man Ro

**机构**：暂未知

**发布日期**：2026-09-08 | **论文**：https://arxiv.org/abs/2609.08390 | **PDF**：https://arxiv.org/pdf/2609.08390.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工对话系统需同时听说，但其纯音频感知在背景噪声与重叠语音下常失效，产生不连贯响应。现有音视频对话方案多直接改造大型语音对话模型以处理视觉输入，多模态训练代价高。本文提出 AV-STE，一种模块化流式音视频前端，在带噪音频与唇部视频输入下、于送入语音 LLM 之前恢复被破坏的语义 speech token，下游对话模型（如 Moshi）完全冻结。集成实验显示 GPT-4o 评判的平均响应连贯性在同一数据集说话人干扰下由 1.42 提升至 1.91，增益并迁移至跨域场景。

### 🔧 技术方案

**问题背景：** 全双工系统（如 Moshi 类 streaming speech-to-speech 模型）的感知链对音频毁坏敏感，噪声或说话人重叠会使语义 speech token 严重受损产生不连贯响应；近年研究显示唇部视觉线索可增强音频毁坏下的鲁棒性，但典型做法是让语音对话模型本身融合视觉模态，需昂贵复杂的多模态后训练。

**模型架构：** AV-STE 作为流式音视频前端位于语音对话模型之前：输入为带噪音频流与唇部视频，输出为恢复后的语义 speech token，再送入完全冻结的语音 LLM。其"噪声自适应流式"设计意味着按当前噪声条件调节增强强度，并以流式方式逐块处理，符合全双工低延迟推理要求；前端作用于语义 token 层级，最小化对生成音质链路的侵入。

**核心创新：** (1) 模块化前端与冻结 LLM 解耦：下游对话模型完全冻结，保留预训练对话与交互能力，避免重训大型语音对话模型的多模态代价，可即插即用接入现有说话人模型。(2) 噪声自适应流式 token 增强：前端感知环境状况按需增强，配合流式约束可部署于实时交互。(3) 唇部视频提供强信息监督：视觉模态与音频损坏正交，为语义 token 恢复提供鲁棒参考。

**训练策略：** 前端在与部署一致的带噪与说话人干扰条件下训练增强损坏信号；同时集成到冻结 Moshi 进行端到端评估，验证修复后的 token 确能改善下游对话质量；跨域（OOD）测试采用 Seamless Interaction 数据检验泛化能力。

### 📊 实验结果
**数据集**：带噪与同数据集说话人干扰条件，以及跨域 Seamless Interaction 测试集（名称与样本量摘要未给出）

**主要指标**：
- 集成冻结 Moshi：GPT-4o 评判平均响应连贯性 1.42→1.91（同数据集说话人干扰），并基本保持 turn-taking 行为
- 跨域 Seamless Interaction 上亦有增益

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：以模块化前端+冻结下游模型方式解决全双工系统的噪声鲁棒性问题，思路简洁、工程落地性强，避免重训大型对话模型的多模态成本，连贯性 1.42→1.91 提升显著且跨域泛化得到验证。扣分点为摘要信息有限，无前端参数规模、量化指标细节与消融，流式实现的具体机制属推断。

---

## [2] Disentangled Global-Local Feature Learning with E-Branchformer for Audio Deepfake Detection

**arXiv ID**：2609.08948 | **方向**：语音前端

**作者**：Phuong Tuan Dat, Ho Bao Thu, Nguyen Tran Trung, Pham Viet Hoang, Nguyen Thi Thu Trang

**机构**：暂未知

**发布日期**：2026-09-08 | **论文**：https://arxiv.org/abs/2609.08948 | **PDF**：https://arxiv.org/pdf/2609.08948.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
TTS 与 VC 等语音合成技术的快速进步对说话人认证等语音业务系统构成严重威胁，亟需鲁棒深度伪造检测。本文提出基于 E-Branchformer 的新架构，有效利用自监督语音表征进行音频深度伪造检测：并行双分支（multi-head self-attention 与 depthwise 卷积）同步建模全局上下文与局部时序模式，并在特征合并后引入 DWConv 与 Squeeze-and-Excitation 模块富化分类 token。在 ASVspoof 2021 LA、DF 及 In-the-Wild 三个数据集上取得 EER 0.88%、1.85%、6.30% 的当前最优性能。

### 🔧 技术方案

**问题背景：** 语音合成与转换技术日益逼真，伪造语音可轻易欺骗基于声纹/说话人认证的系统；同时真实场景中伪造攻击类型不可预知、声学条件复杂，检测器必须同时把握整段话语的全局语义上下文与细粒度局部时序伪迹（频谱不连续、共振峰抖动、人工痕迹等），单一结构难以兼顾。

**模型架构：** 基于 E-Branchformer：一个分支用 multi-head self-attention 捕获全局上下文依赖，另一分支用卷积建模局部时序模式，并行合并实现全局-局部特征解耦学习；前端集成自监督语音表征；特征合并阶段后经 depthwise convolution 与 Squeeze-and-Excitation 模块将 patch token 信息聚合并注入分类 token。

**核心创新：** (1) 双支路全局-局部解耦，注意力支路与卷积支路判别信息互补，消融证实双支路缺一不可。(2) 层次化 token 富化：特征合并后经 DWConv 与 SE 从 patch token 精炼判别性增量并丰富 class token。(3) SE-Aggregation 显著改善自监督特征融合质量，说明简单拼接/平均不足以发挥 SSL 表征潜力。

**训练策略：** 以 ASVspoof 2021 LA、DF、In-the-Wild 基准训练与评估（LA 为逻辑访问/合成，DF 为非特定合成攻击，In-the-Wild 为真实世界伪造语音）。

### 📊 实验结果
**数据集**：ASVspoof 2021 LA、DF、In-the-Wild

**主要指标**：
- EER：LA 0.88%、DF 1.85%、In-the-Wild 6.30%

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：将 E-Branchformer 双支路解耦思想引入深度伪造检测，机制清晰且与 SSL 表征有机结合，三个基准（含真实世界 In-the-Wild）的低 EER 具备较强说服力，消融覆盖双支路互补性、SE 聚合与 token 增强。扣分点为摘要未提供参数规模/计算量/微调细节，In-the-Wild 6.30% 仍高于 LA/DF 说明真实场景仍是瓶颈。

---

## [3] Lead Vocal Separation from Vocal Ensemble Mixtures Using Phoneme Alignment

**arXiv ID**：2609.06488 | **方向**：语音前端

**作者**：暂未知

**机构**：暂未知

**发布日期**：2026-09-06 | **论文**：https://arxiv.org/abs/2609.06488 | **PDF**：https://arxiv.org/pdf/2609.06488.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现代阿卡贝拉演唱常呈现主唱+伴唱织体，主唱声部（Vo）承载主旋律，其余人声提供伴奏。由于目标与干扰源均为歌声、声学特性相似且常时间重叠，声学线索十分有限。本文提出以 Vo 部分音素对齐作为辅助信息的分离模型：基于 band-split RoPE Transformer（BS-RoFormer），通过 feature-wise linear modulation（FiLM）将帧级音素标签引入中间表示。实验表明音素对齐条件优于纯音频基线，且较仅使用 Vo 演唱/静默活动标签获得更大平均增益；伴唱声部越少，音素标签信息的优势越大。

### 🔧 技术方案

**问题背景：** 与乐器伴奏分离不同，纯人声合奏中主唱与伴唱同为歌声，基频范围、发声机制和音色高度接近且常同时发声，传统低层声学线索难以区分二者，属于"同源对抗"型分离难题。仅有的可用线索是主唱在旋律中承担歌词语义而与伴唱在衬词、和声上定位不同，这为音素级条件信息提供了理论支撑。

**模型架构：** 采用 BS-RoFormer 作为骨干（band-split 频谱划分 + RoPE 编码 Transformer，在音乐源分离基准上领先），将帧级音素标签改写为条件向量，经 FiLM 对中间表示做逐通道缩放与偏移，在不显著增加参数量与解码复杂度前提下实现条件调制，可与 mask-based 时频掩蔽估计流程自然衔接。

**核心创新：** (1) 以 Vo 音素对齐作为语义级辅助条件而非仅依赖低层声学特征，将"唱了什么词"这一更高语义信息显式注入缓解声学线索不足，且音素标签是训练期可获得的地面真值，避免误差累积。(2) 采用 FiLM 调制实现条件注入，帧级标签与时间对齐，在掩蔽估计过程中逐帧引导网络关注与歌词相关的语音结构。

**训练策略：** 与仅以 Vo singing/silence 活动为条件的方案对比，音素条件平均增益更优，说明细粒度语义信息（音素）比粗粒度活动信息提供更多判别依据；具体超参与 loss 细节摘要未给出。

### 📊 实验结果
**数据集**：含多轨人声声部的阿卡贝拉/合唱歌集（名称未在摘要给出）

**主要指标**：
- 音素对齐条件在各指标上优于 audio-only 基线
- 优于仅以 Vo singing/silence 活动条件的变体
- 剩余伴唱声部越少，音素标签带来的相对优势越大

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：切中纯人声分离中"同源难分"的真实痛点，将音素对齐这一语音识别成熟信息迁移至分离任务，思路新颖且与歌词识别下游天然协同；在 SOTA 分离骨干上以轻量 FiLM 注入条件，工程上务实。扣分点为摘要未披露数据集规模、指标数值与基线设置，音素对齐获取成本与推广性待原文验证。

---

## [4] Emotion as a Distribution: Joint Valence-Arousal Probability Learning for Speaker-Independent Multimodal Emotion Recognition

**arXiv ID**：2609.05755 | **方向**：语音前端

**作者**：暂未知

**机构**：暂未知

**发布日期**：2026-09-04 | **论文**：https://arxiv.org/abs/2609.05755 | **PDF**：https://arxiv.org/pdf/2609.05755.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
人类情感是渐变且常为混合状态，但多数多模态识别器将其压成单一硬标签，丢失大量信息。本文提出 text+speech 系统在类别决策之外同时输出 V-A 平面上的 9×9 概率矩阵，以二维高斯软目标在 KL/交叉熵目标下训练。在 IEMOCAP 严格 speaker-independent 留一会话外评估中，双头系统达 73.0%±0.3 UA，超 Transformer 融合基线 3.0 点，换用冻结 WavLM-Large 特征后提升至 76.6%±1.3。

### 🔧 技术方案

**问题背景：** 情感在 Valence-Arousal 平面的特征是连续渐变且常呈混合叠加，单一硬标签无法表达"7 分高兴、3 分平静"这类状态，且标注者间常存在歧义。论文论证识别器应输出 affective space 上的分布而非单点，面向心理咨询辅助（counseling support）这类对情感精细度与不确定性表达要求更高的场景。

**模型架构：** text+speech 系统由 encoder、fusion、head 三部分组成，在分类 head 之外增设分布 head 共同输出 9×9 概率矩阵覆盖 V-A 平面，用二维高斯软目标对齐分布形状。在固定 encoder-fusion-head 管线内对比 Transformer 与 Mamba-1/2/3 state-space 骨干（深度宽度匹配，T≈550 与 T≈2750 两档验证）。

**核心创新：** (1) 联合 V-A 概率分布输出：9×9 概率矩阵+二维高斯软目标，使模型暴露情感分布而非单点。(2) 严格 speaker-independent 评估协议：5 折留一会话外验证+旋转会话内验证，头指标只在 held-out 会话上报告，杜绝说话人泄漏。(3) 在同一 pipeline 内系统对比 Transformer 与 Mamba 家族骨干，并验证冻结 WavLM-Large 特征对同一架构的提升。

**训练策略：** 采用 5 折 leave-one-session-out 的 speaker-independent IEMOCAP 协议，内层用旋转会话选择超参，headline 指标仅在 held-out 会话语义上计算（按会话而非 utterance 划分避免说话人泄漏）；前端约 1M 可训练参数，对照路线为冻结 WavLM-Large 特征仅训练层权重。

### 📊 实验结果
**数据集**：IEMOCAP

**主要指标**：
- 双头系统 UA：73.0%±0.3（三 seed，独立 rerun 72.1%），超 Transformer 融合基线 3.0 UA 点（95% bootstrap CI [1.0,4.7]，配对 t 检验与会话级 bootstrap 均显著）
- 冻结 WavLM-Large 特征：76.6%±1.3
- 分布质心追踪 V-A：CCC 0.66/0.66；分布熵与类别标注者歧义弱相关

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：把"情感是分布"落到可训练的 9×9 概率输出并配二维高斯软目标，形式新颖且直接服务 counseling 等细粒度应用；评估协议严格（speaker-independent 留会话外+显式控制组），声明边界清晰，诚实承认分布 head 的核心价值在于归一化分布本身。扣分点为规模有限（单数据集、单一语言），9×9 与高斯软目标的校准与跨数据集泛化待验证。

---

## [5] Clean Accuracy Does Not Guarantee Provenance Robustness: A Prospective Codec-Stress Evaluation of Audio Attribution

**arXiv ID**：2609.07981 | **方向**：语音前端

**作者**：Gang Shi

**机构**：暂未知

**发布日期**：2026-09-07 | **论文**：https://arxiv.org/abs/2609.07981 | **PDF**：https://arxiv.org/pdf/2609.07981.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
音频溯源归属（判断合成话语由哪个系统产生）在干净 benchmark 上报告接近满分，但分析师实际拿到的音频通常经过转码，性能大幅衰减。本文提出前瞻注册式测量协议：在训练任何归属模型前用保真元数据固定分析区域，评估单阶段 codec 转码后的 closed-set 归属。实验显示 WavLM-Base+ 在 support 内损失 53.5 与 70.3 点 Macro-F1，W2V2-BERT 2.0 损失 61.0 与 49.8 点；干净精度本身不能刻画部署鲁棒性。

### 🔧 技术方案

**问题背景：** 音频溯源归属检测在实际取证中面对的音频几乎都经过转码传输，而现有评测多在无扰动干净信号上进行，导致近满分精度与真实性能脱节；衰减同时强依赖被测表征类型与 codec 条件，需要一个在训练前就固定评估范畴、避免选择偏差的协议。

**模型架构：** 前瞻注册式（prospectively registered）测量协议：训练前仅凭保真元数据确定分析区域，随后进行 closed-set 归属；任务跨两个语料库、覆盖单阶段 codec 转码网格。编码器采用 WavLM-Base+ 与 W2V2-BERT 2.0，并加入 clean-qualified ECAPA-TDNN 与 Proxy-Anchor head 作为对照，排除结果仅属某一表征家族或弱线性头的可能。

**核心创新：** (1) 前瞻注册协议：分析区域在模型训练前即固定，杜绝事后调整分析范围带来的乐观偏差，使衰减量成为可复核的诚实数字。(2) 条件依赖系统量化：将衰减分解为码率与表示两个维度，同一 support 网格内损失可从 -0.4 波动到 +53.5 点，直接证明"干净精度-鲁棒性"关系不成立。

**训练策略：** 固定分析区域后训练归属模型，再在预定义 codec 网格（多种码率与转码类型）上评估；指标除 Macro-F1 外对齐 SI-SDR 与 PESQ-WB 交叉验证。

### 📊 实验结果
**数据集**：两个语料库（support-in 结构由保真元数据事先固定）

**主要指标**：
- support 内损失：WavLM-Base+ 53.5 [43.5,63.6] 与 70.3 [63.0,77.5] Macro-F1；W2V2-BERT 2.0 61.0 [56.8,65.1] 与 49.8 [41.6,57.9]
- 单一 support 网格内 WavLM 损失范围 -0.4 至 +53.5；两编码器在 12 条件中的 6 个超出 ±5 点 margin
- MP3 8kbit/s 在 SI-SDR 上居网格中位、PESQ-WB 垫底，却造成最大损失

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：用前瞻注册协议系统反证"干净精度等于鲁棒性"这一常见假设，实验设计在对照组与跨表征验证上扎实，量化了转码条件与表示类型对溯源衰减的作用，codec 条件、失真测度与损失之间不一致的发现具有很强工程警示意义。扣分点为匹配保真度比较未能估计、未披露代码与完整网格细节，且缺少修复手段方向性讨论。

---

## [6] RAFM_SER++: A Lightweight Multimodal Emotion Recognition Framework for Real-Time Behavioral Monitoring in Surveillance Systems

**arXiv ID**：2609.07409 | **方向**：语音前端

**作者**：Ngo Truong Dinh, Tung-Lam Bui, Chi-Trung Duong, Vien Nguyen Thi, Viet-Anh Nguyen, Phuc-Lu Le

**机构**：暂未知

**发布日期**：2026-09-07 | **论文**：https://arxiv.org/abs/2609.07409 | **PDF**：https://arxiv.org/pdf/2609.07409.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
交互式跨模态 transformer 虽使多模态语音情感识别达到高精度，但计算开销大，难部署于延迟敏感、资源受限的监控系统。本文提出轻量级多模态 SER 框架 RAFM_SER++，以非对称 Residual Attention Fusion Mechanism（RAFM）单向残差注意力路径将情感语音线索注入语义文本表征，规避昂贵双向跨模态交互，配合 BYOL 启发式跨模态对齐目标与 attention-guided pooling。在 IEMOCAP 与 ESD 上 BACC 分别达 81.10% 与 95.39%，可训练参数较 SOTA 减少 60% 以上，推理达 79.60 it/s。

### 🔧 技术方案

**问题背景：** 主流高性能多模态 SER 依赖交互式跨模态 transformer，通过双向 cross-attention 对齐音频与文本模态，精度高但训练与推理成本陡增，无法满足监控、安检等时延敏感且算力受限场景的实时情感行为监测需求。

**模型架构：** RAFM_SER++ 整体延续音频编码器与文本编码器双流设计，核心为 RAFM 融合模块：非对称单向残差注意力把情感语音线索经残差连接注入语义文本表示（信息单向由语音流向文本，避免双向往返交互），配合 BYOL 式跨模态对齐目标与 attention-guided pooling 完成多模态表示学习。

**核心创新：** (1) 非对称单向残差注意力融合：以轻量残差注意力路径替代交互式 transformer 的双向交互，大幅降低计算量。(2) BYOL 启发式跨模态对齐：借鉴无监督自蒸馏范式促进模态间表征对齐。(3) attention-guided pooling：以注意力权重引导时序池化，突出情感判别力强的语音片段，代替简单 mean/max 池化提升下游分类效用。

**训练策略：** 在 IEMOCAP 与 ESD 基准上与 HuBERT-Base 基线对比，以 SOTA 交互式跨模态 transformer MemoCMT 作为精度-效率权衡标杆。

### 📊 实验结果
**数据集**：IEMOCAP, ESD

**主要指标**：
- BACC：IEMOCAP 81.10%、ESD 95.39%
- 可训练参数较 MemoCMT 减少 60%+，推理 79.60 it/s
- 结果一致性超越 HuBERT-Base 基线

**是否开源**：摘要未提及

### ⭐ 评分：8/10
评分理由：动机清晰且契合监控实时监测需求，以单向非对称融合+BYOL 对齐+attention-guided pooling 换取 60%+ 参数压缩，精度-效率权衡数据完整、说服力较强。局限为仅报告 BACC 宏观均值，缺少混淆矩阵与细类召回分析，真实监控噪声场景下的鲁棒性尚待验证。

---

## [7] AdoDAS: A Privacy-Preserving Multimodal Challenge for Adolescent Depression, Anxiety, and Stress Assessment

**arXiv ID**：2609.07038 | **方向**：语音前端

**作者**：Zhaojie Luo, Junkun Wang, Tianhua Qi, Yuxuan Wu, Xin Zhao, Tetsuya Takiguchi, Tomoko Matsui, Kun Qian, Fei Wang, Shuqiong Wu, Zhengjun Yue, Hiroshi Ishiguro, Xinyuan Qian, Haizhou Li 等

**机构**：暂未知

**发布日期**：2026-09-07 | **论文**：https://arxiv.org/abs/2609.07038 | **PDF**：https://arxiv.org/pdf/2609.07038.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
青少年抑郁、焦虑与压力（D/A/S）需要可扩展的自动评估工具补充而非替代专业诊断，AdoDAS Grand Challenge 在严格的隐私保护政策下拒发未成年人原始录音，仅分发匿名化音视频表征与 ASR 衍生文本。其 6,000 名参与者提供 24,000 个片段（1 次脚本阅读+3 次开放式会话）；设置多任务二分类筛查与 21 项 DASS-21 条目序数预测双赛道。191 个注册团队中 95 个进入筛查榜、64 个进入条目预测榜；基线 mean F1 0.4604 与 mean QWK 0.2675，领先方案达 0.5921 与 0.2776。

### 🔧 技术方案

**问题背景：** 青少年心理评估依赖专业访谈，成本高、覆盖面有限；而未成年人语音含高度敏感个人信息，直接发布原始音频面临严重隐私与伦理风险。AdoDAS 以"表征替代原始信号"为核心，探索大规模数据共享与隐私保护的平衡点。

**模型架构：** 采用特征分发范式——主办方保留原始波形，向参赛团队提供去标识化音视频表征与 ASR 文本，参赛者仅在表征层构建模型。数据为 6,000 参与者、24,000 片段（每人 1 次脚本阅读+3 次开放式会话）。赛道一为 D/A/S 三项多任务二分类筛查，赛道二为 21 项 DASS-21 条目逐项序数预测。

**核心创新：** (1) 隐私保护下的表征分发范式，保护未成年人身份的同时共享数据价值，可成为同类心理健康数据发布的参照模板。(2) 大规模青少年音频-文本心理评估数据集与统一评测任务，降低方法横向对比门槛。(3) 以 DASS-21 心理学结构驱动任务设计，将细粒度条目序数预测与粗粒度筛查双轨结合，兼顾临床可解释性与实用筛查需求。

**训练策略：** 191 个注册团队经合规筛选后 95 个筛查队与 64 个条目预测队合格入榜；优胜方案共性包括跨会话建模、时序多模态融合、心理测量结构感知与任务感知校准。

### 📊 实验结果
**数据集**：AdoDAS（6,000 参与者，24,000 片段；仅分发匿名音视频表征与 ASR 文本）

**主要指标**：
- 筛查赛道：音视频基线 mean F1 0.4604，领先提交 0.5921
- 条目预测：基线 mean QWK 0.2675，领先提交 0.2776

**是否开源**：摘要未提及（受隐私政策限制，原始数据公开可能性低）

### ⭐ 评分：8/10
评分理由：选题极具现实意义，隐私保护下的表征分发范式直面未成年人数据安全硬约束，为心理健康数据共享树立可复用赛制模板；6,000 人级规模与 DASS-21 心理测量结构驱动的双赛道设计严谨。扣分点为 QWK 从 0.2675 仅提升至 0.2776，增益有限且绝对水平偏低，提示去标识表征可能损失关键声学信息。

---

### 其余论文速览（命中但未进入前 15 详读）

语音大模型：
- TASTE2: Text-Aligned Speech Modeling and Deployment toward Full-Duplex Voice Interaction | **arXiv ID**：2609.08956 | **评分**：7.5/10 | https://arxiv.org/abs/2609.08956
- TontaubeV1: Streaming Text-to-Speech with Hierarchical Codec Modeling and Bounded Context | **arXiv ID**：2609.08703 | **评分**：7/10 | https://arxiv.org/abs/2609.08703
- Where Does the Sound Go? Tracing Acoustic Information Loss in Audio-Conditioned LLMs | **arXiv ID**：2609.05871 | **评分**：6/10 | https://arxiv.org/abs/2609.05871

语音前端：
- Semantic Refinement of Universal Audio Representations through Audio-Description Alignment | **arXiv ID**：2609.08429 | **评分**：8/10 | https://arxiv.org/abs/2609.08429
- Comparing Self-Supervised and Domain-Invariant Features for Cross-Domain Voice Phishing Detection | **arXiv ID**：2609.07079 | **评分**：7.5/10 | https://arxiv.org/abs/2609.07079
- Iterative Audio Separation with Mixture Consistency via MIMO Model Extension | **arXiv ID**：2609.07226 | **评分**：7/10 | https://arxiv.org/abs/2609.07226
- From Scores to Evidence: Auditable Decisions Can Improve Speech Deepfake Detection | **arXiv ID**：2609.08899 | **评分**：7/10 | https://arxiv.org/abs/2609.08899
- SETEAB: Multiscale approach with Squeeze-and-Excitation Temporal Enhanced Aware Block for Speech Emotion Recognition | **arXiv ID**：2609.06101 | **评分**：7/10 | https://arxiv.org/abs/2609.06101
- Direction-Preserving Active Noise Control with a Conditional Control-Filter Estimation Network | **arXiv ID**：2609.07173 | **评分**：7/10 | https://arxiv.org/abs/2609.07173
- When Speech Meets Lips: Interpretable Audio-Visual Synchronization for L2 Pronunciation Assessment | **arXiv ID**：2609.06788 | **评分**：6.5/10 | https://arxiv.org/abs/2609.06788

---

*Generated on 2026-09-10*