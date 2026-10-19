# 2026-10-15 语音论文速递

**共收录**: 23 篇 | **语音大模型**: 14 篇 | **语音前端**: 9 篇

> 目标日期 2026-10-15（北京时间）arXiv 语音相关论文共命中 23 篇。
> 以下是按评分排序的结果。

### 速递说明

本批次精选前 15 篇进行完整模板精读，按评分由高到低排序；其余 8 篇论文仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），未展开精读。

---

## ELARSpeech: A 30K-Hour Dataset Across 675 Underrepresented Languages for Long-Tail Multilingual Speech Technologies

**arXiv ID**：arXiv:2610.19388 | **方向**：语音大模型

**作者**：Sangmin Lee, Yejin Jeon, David Ifeoluwa Adelani

**机构**：Yonsei University；McGill University；Mila - Quebec AI Institute；Canada CIFAR AI Chair

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.19388 | **PDF**：https://arxiv.org/pdf/2610.19388.pdf | **代码**：https://github.com/sanghyang00/elarspeech/ | **Demo**：暂无

### 📌 简介
现有语音资源在语言长尾上存在可及性、声学与域多样性、评测基准三重缺口。论文基于濒危语言档案（ELAR）田野录音构建ELARSpeech：共30,202小时、675种低资源语言，其中标注子集2,791小时（443语言）、无标注子集27,412小时（665语言），259种语言不被现有模型支持、53种无ISO 639-3编码。实验表明其可有效支撑ASR/TTS长尾适配，伪标签扩展带来最高6.1%相对CER下降，同时揭示现有自监督模型的长尾迁移局限。数据集、模型与管线全部开源。

### 🔧 技术方案

**问题背景：** 公开语料多仅覆盖数百语言，千语言级数据集因许可限制不可公开；MMS/XEUS等集中于圣经朗读域；ML-SUPERB等基准偏高资源语言，长尾有效性缺系统评测。

**模型架构：** 本作为资源型工作，核心是双管线：ELARSpeech-L经文件名子串匹配配对音频与EAF标注，用分层命名置信打分算法挑选转写tier并按时间戳切分，越界即整条丢弃；ELARSpeech-U用Brouhaha估计SNR/C50做剪枝（仅过滤不增强），pyannote-Precision-2说话人分离，保留0.5秒内重叠，超30秒片段用Silero VAD在最长静音处递归切分；全库统一24kHz、16-bit FLAC，RMS归一至-23 dBFS。

**核心创新：** (1) 以濒危语言档案为来源，30K小时覆盖675语言直达长尾，规模与公开性兼备，且对比显示公开标注资源中语言数第一。(2) 保留原始声学、不做语音增强的"保存优先于规范"原则，避免破坏小语种语音学线索。(3) 数据集兼作训练资源与测试床：支撑Whisper、OmniASR-CTC、OmniVoice适配，并以ML-SUPERB协议诊断自监督模型的长尾迁移能力。

**训练策略：** AdamW，8×H100，三段式学习率（5e-7至1e-5，warmup/hold/decay比0.1/0.5/0.4）。单语ASR：Whisper 25代、OmniASR 50代、batch 32；多语ASR 150K步、batch 128；TTS packed-sequence 50代、批时长2.5分钟、100K步；TTS训练仅用SNR/C50均大于20 dB样本；无ISO语言token从英文token热启动。

### 📊 实验结果
**数据集**：ELARSpeech（30,202小时，24 kHz，675语言；30个pivot语言、233语言全量评测，另有CV26与INEL跨域测试）

**主要指标**：
- ASR单语宏平均CER：Whisper 22.48%（30 pivot语言最优）
- 无ISO语言宏平均CER：OmniASR-CTC-300M 24.50%，优于Whisper 1.5B的24.63%
- 伪标签扩展：最高6.1%相对CER下降；Dawoodi在ELAR测试集93.99→22.68
- TTS宏平均：单语CER 16.98%/MOS 3.42，多语CER 17.78%/MOS 3.55
- 关键对比：多语ASR宏CER较单语恶化8.23；无ISO语言CER差距从ML-SUPERB的26.1%相对差压缩至ELARSpeech的3.5%

**是否开源**：数据集、ASR/TTS模型与完整构建管线已开源 @ https://github.com/sanghyang00/elarspeech/（CC BY-NC-SA 4.0）

### ⭐ 评分：8/10
评分理由：将30K小时推向675个长尾语言并完整开源数据、模型与管线，稀缺性与可复现性兼备。实验设计成熟：伪标签质量阈值、域泛化与自监督模型诊断均给出有信息量结论，如模型规模与语言覆盖并非长尾迁移主因。局限在于标注子集仅2.8K小时、MOS依赖非母语听者、跨域验证只覆盖4语言，且部分结论受自动指标偏差影响。作为资源类论文贡献扎实，具顶会水准。

---

## VoxTurn: Answering Several Turn-Taking Questions in One Pass with One Model

**arXiv ID**：arXiv:2610.21150 | **方向**：语音大模型

**作者**：Austin Xiao（HTML 正文未列全作者名单，发布账号为 AustinXiao）

**机构**：University of Melbourne（致谢提供算力，含 NCI Australia）

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21150 | **PDF**：https://arxiv.org/pdf/2610.21150.pdf | **代码**：https://huggingface.co/AustinXiao/voxturn | **Demo**：https://swagshaw.github.io/voxturn/

### 📌 简介
级联语音智能体须在用户每次静音中判断是否接话，开源检测器每多回答一个决策就要多一个模型或多次调用，且在 14 语言 eot-bench 上误切用户超四分之一。本文提出 VoxTurn：一个 0.8B 语音大模型，将轮次转换决策写成选择题、用线性头对选项隐状态打分，并以块隔离注意力掩码在一次前向传播中同时回答全部问题。模型在真实会话静音（决策时间随静音时长采样）上训练，英文 300ms 延迟预算下误切断率 11.5%，接近商用检测器；14 语言均值 19.9% 为开源最低，单次决策 8.3ms；零样本在 TurnBench 轮次结束检测排 24 个系统第 5。

### 🔧 技术方案

**问题背景：** 现有开源轮次检测器多在切分好的朗读语料上训练、仅在句尾打标，与部署时在真实静音内任意时刻被查询的设定失配，是其最大单一误差源；且每个额外决策需独立模型或调用，框架只在 VAD 报静音时查询一次、靠超时兜底，浪费了模型随静音增长而提升的置信度。

**模型架构：** 基座为 Qwen3-ASR-0.6B：冻结 AuT 语音编码器把 128 维 log-mel 转为 13 token/秒的音频 token（8 秒 104 个），经投影层接入 Qwen3-0.6B 语言模型，全部线性层加 LoRA（rank 16、alpha 32）。输入为聊天头、8 秒音频、可选转写、说话人标记，后接若干"Question/Options"块；不做生成，用线性头为每个选项末 token 隐状态打分并 softmax；仅训练投影层、LoRA 与头部共 11.8M 参数，覆盖 eot、resume、state4、intent、invalid 五个问题。

**核心创新：** (1) 把轮次决策统一为固定选项集的选择题，以判别式打分取代文本解码，概率校准良好（英文 eot ECE 仅 0.007）；题干配 12 种中英文改写做增广。(2) 块隔离注意力掩码：问题块彼此不可见但均可读取共享音频前缀，位置 id 按"单独提问"重排，数学上等价于逐题多次前向（fp32 最大概率差 1.5e-5），单遍即可答任意题集，前缀约 120 token 只编一次、每题仅加约 15 token。(3) 真实静音训练与标签派生：用 Silero VAD 从电话与面对面会话切出静音，据后续说话行为标 hold/end-of-turn，决策时间均匀采自静音前 min(d,1.5s)，resume 与 not-invalid 等辅助标签免费获得，并加双措辞对称 KL 一致性损失。

**训练策略：** 混合 300k 样本：Smart Turn 266k（18%）、Easy Turn 1.19M（25%）、MagicData-RAMC 181k（11%）、SpokenWOZ 95k（14%）、Seamless Interaction 179k（14%，一半降采样至 8kHz 防带宽泄露）、SemanticVAD 15k（4%）、MUSAN+VocalSound 非语音负例 17k（14%）。batch 128（4×32 微批），AdamW，lr 2e-4，beta(0.9,0.98)，weight decay 0.01，100 步 warmup 余弦衰减至 10%，梯度裁剪 1.0，bf16；损失为主 CE + 0.5×辅助 CE + 0.5×对称 KL；单卡 L40S 78 分钟。推理合并 LoRA、CUDA graph，静音期内每 0.25s 重询，阈值 theta=0.8。

### 📊 实验结果
**数据集**：eot-bench（14 语言真实用户轮，每 100ms 打分）、TurnBench（30 小时双人对话）、Easy Turn 中文测试集、TEN 文本测试集、OpenSLR 99 非言语发声集、Pipecat/LiveKit 框架回放（150 条英文轮）。

**主要指标**：
- eot-bench 英文误切断率：11.5%@300ms 延迟预算（6.0%@600ms；5% 误切断时需 669ms）
- 14 语言均值：19.9%，开源最低，较次佳开源 LiveKit v1-mini（28.4%）低 8.5 个百分点
- 关键对比：优于商用 Baton（12.3%）与 Deepgram Flux（12.9%），仅次闭源 LiveKit v1（9.9%）与 2.8B 的 turn-1（10.6%）
- TurnBench 零样本：EOT recall 0.924（FPR 0.076，24 系统第 5）；INT recall 0.951（FPR 0.112，中位延迟 332ms，第 6）
- 效率：单题 8.3ms、单遍 4 题 9.0ms（4 次前向 33.2ms），显存 1.9GB
- 框架回放切断率：Pipecat 45.3%→16.7%（延迟 1.32s→0.36s），LiveKit 18.0%→9.3%
- 同遍其他任务：Easy Turn 四态准确率 88.3%；OpenSLR 99 非言语标记率 99.6%，有效语音误拒仅 0.06%

**是否开源**：权重、代码与框架插件已开源 @ https://huggingface.co/AustinXiao/voxturn（CC BY-NC-SA 4.0），交互 demo @ https://swagshaw.github.io/voxturn/

### ⭐ 评分：8/10
评分理由：真实静音数据配合时序派生标签直击开源检测器的训练-部署失配，消融清晰量化了数据贡献（英文 26.2%→16.5%）大于骨干与多问训练；单遍多题掩码的等价性构造干净、推理成本降至 8.3ms/决策，工程价值突出；三基准加两大框架回放的实验非常充分且完全开源。不足是骨干仅为现成 ASR 模型的 LoRA 微调、方法层面增量，中文与印地语等偏弱，且尚无同行评审，故未达 9 分。

---

## MultiPartyTurnBench: Benchmarking Floor Control in Multi-Party Spoken Dialogue

**arXiv ID**：arXiv:2610.20172 | **方向**：语音大模型

**作者**：Puneet Mathur, Dinesh Manocha

**机构**：University of Maryland College Park

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.20172 | **PDF**：https://arxiv.org/pdf/2610.20172.pdf | **代码**：暂无 | **Demo**：https://multiparty-turnbench.github.io/

### 📌 简介
全双工语音系统须在多方场景中对话语权做出进入、保持与让出决策，而现有评测只覆盖双方轮次切换或端到端代理行为。本文提出 MultiPartyTurnBench：240 条通道分离合成对话（6.89 小时），覆盖 2-5 说话人与 6 种交互类型，定义 EOT（话轮结束）与 INT（成功打断）两个事件级任务，用误报率约束下的召回与带符号延迟做因果评测。结果显示显著不对称：预算内 EOT 召回最高 92.6%（FPR 7.5%），INT 仅 56.2%；五个全双工代理启动抢话平衡准确率 86.1-95.8%，选择性停止仅 46.9-54.7%，接近随机，确立选择性打断处理为未解挑战。

### 🔧 技术方案

**问题背景：** 双方基准只评事件、自然多方语料只评下一说话人预测、代理基准只评端到端行为，均缺受控多方下对真实话权交接与易混淆非事件的因果评测。

**模型架构：** 五阶段管线：GPT-4.1 按 TURN/CLAIM_FLOOR/VOCALIZE_NO_CLAIM 词表写事件脚本；离散事件编排器把动作解析为 hold/yield/interrupted，按 AMI 统计定时并在合成前定 EOT/INT 锚点；Kokoro-82M 以 24 个性别均衡互斥音色逐通道合成；叠加 SNR U(20,38) dB 噪声、MUSAN 音效与远处语音，输出 24 kHz 分轨；[t-0.25, t+3.0] 秒窗因果一对一匹配，dev 上 FPR≤10% 内选最大召回阈值并冻结。

**核心创新：** (1) 角色相对的话权状态分类学：六类事件映射为 EOT 正例 3,422/硬负例 241 与 INT 正例 367/负例 1,481，失败抢话因结果因果模糊不计分，反馈笑声作硬负例，度量话权变化而非语音活动。(2) 先标注后合成：话权与时间戳在 TTS 前确定，人数/风格/声学三轴独立可控、全种子可复现，实现自然语料无法支持的单变量消融。(3) 三层互补协议：12 系统离线因果检测、120 个 START/STOP 双探针场景测 5 个全双工代理共 1,800 试验，AMI 真实验证，以平衡准确率与动作偏置区分盲目让出与拒绝让出。

**训练策略：** 无训练环节。脚本温度 0.9、输出 8,000 token、JSON 校验坏例重生成；(N,类型) 每格 10 段，dev 48/test 192、音色不相交；五项声学质检全过、97.2% 重叠事件声学落地；3 名标注员独立校验，反馈声 Fleiss κ 0.92、成功打断 0.78，生成器-人类一致率 86.5-97.8%。

### 📊 实验结果
**数据集**：MPTB 240 段合成对话（6.89 h、24 kHz、通道分离）+ 15 场四方 AMI 会议。

**主要指标**：
- EOT 召回（预算内）：VAP 92.6%@FPR 7.5%、Kyutai SVAD 92.5%@4.3%、Mimi EP 90.5%@3.8%，最快 p50 143 ms
- INT 召回：最高 Kyutai SVAD 仅 56.2%@6.6%，VAP 11.7%、Mimi EP 13.9%、ESPnet 1.1%
- 声学基线：Silero VAD 97.2%@FPR 93.5%，超预算，不具选择性
- 代理行为：START 平衡准确率 86.1-95.8% 对 STOP 46.9-54.7%；Gemini-3.8-Live 误让 97.7% 反馈声（偏置 +0.98），MiniCPM-o-4.5 仅让 1.4% 真打断（-0.99）
- 关键对比：EOT 与 INT 最高合格召回差 36.4 个百分点；AMI 上 VAP 召回 35.9%@5.3%

**是否开源**：语料经项目页发布（双通道、事件日志与种子）；代码仓库直链暂无。

### ⭐ 评分：8/10
评分理由：将话权控制形式化为带硬负例的因果事件检测，先标注后合成机制带来精确锚点与三轴受控复现，实验含预算约束、延迟、人数/风格切片与人评校验，充分性高。EOT-INT不对称与五代理选择性停止近随机是有价值的阴性发现，直指全双工落地瓶颈。不足是仅英文合成语音、真实验证限于小样本 AMI、未提出解决方法，属高质量基准而非技术突破。

---

## Full-Duplex Interaction with Speech, Expressions and Gestures

**arXiv ID**：arXiv:2610.21452 | **方向**：语音大模型

**作者**：Siyin Wang, Wenyi Yu, Terumi Chiba, Xianzhao Chen, Xiaohai Tian, Jun Zhang, Lu Lu, Chao Zhang

**机构**：清华大学、字节跳动

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.21452 | **PDF**：https://arxiv.org/pdf/2610.21452.pdf | **代码**：https://github.com/bytedance/SALMONN/tree/ELLSA2 | **Demo**：暂无

### 📌 简介
本文提出 ELLSA 2，首个端到端全双工对话模型，联合优化语音交互与流式手势-表情生成，使模型在说与听两种状态下持续产出非语言行为。其分块合成器联合接收 LLM 的倾听隐状态与合成器的说话隐状态，并以调用头与模板引导解耦"是否调用语义手势"与"如何实现"。实验上 S2S 精度在三个 QA 基准达 78.0%/47.3%/63.6% 领先开源全双工模型，模板引导将人评语义分由 2.014 提至 2.711。

### 🔧 技术方案

**问题背景：** 全双工语音模型只输出语音，手势/表情生成器多为级联的说话驱动动画，依赖已生成语音、无法在静默倾听时反应，也缺少语义手势决策机制，二者未在统一对话过程中联合优化。

**模型架构：** 沿用 SALMONN-omni 全双工框架，总体 10.78B、可训练 776M。手势-表情合成器基于 Qwen2.5-0.5B（24 层，hidden 896），每 0.8s 块按"说话-倾听-手势/表情"交错序列自回归生成 6 步潜码，每步 18 个索引（上身6/手6/非嘴表情4/嘴2，码本 2048）。动作/表情基于 SMPL-H/FLAME，分区域 RVQ-VAE 将 30Hz 动作降至 7.5Hz，嘴部经 SVD 解出 8 维子空间单独建模，流式上下文 20s。

**核心创新：** (1) 双流隐状态条件化：倾听流取 LLM 骨干末层隐状态，说话流取合成器末层隐状态；发 <silence> 时说话条件换成可学习空表示，手势表情在言语静默期持续生成，支持点头微笑等倾听者反应。(2) 语境语义调用与模板引导：词典匹配短语后，由混合第 16/20/24 隐状态的三层 MLP 头预测是否调用语义手势，命中则从 3227 示例库（1125 族、2072 短语）检索 exemplar 置于块首引导生成；文本 look-ahead 保实时。(3) 课程训练与对话感知评估：新建 R_SL、对比式韵律对齐 A、MLLM duplex/semantic 四项指标与 138 条人验测试集。

**训练策略：** 总损失 L=L_text+0.5L_speech+L_GE+0.25L_call，GE 损失按 RVQ 深度加权（1→0.025）。独立生成器三阶段各 50k 步（峰值 lr 1e-4/4e-5/1e-4，bs 256/256/128）。整合训练 Stage1 ASR+QA：lr 2e-4、bs 256、40k 步；Stage2 加多轮对话：2e-4、128、60k；Stage3 冻结语音骨干、自由:引导=4:1，2e-5、64、2.5k；Stage4 联合优化，数据比 2:1:4:1，lr 2e-5、bs 64、20k，LoRA r=32/16，AdamW(0.9,0.95)、wd 0.1、bfloat16、ZeRO-2。手势数据为过滤后 81 说话人的 1318 条 Seamless 录音，FLAME 标注由 KaoLRM 反解。

### 📊 实验结果
**数据集**：Llama Questions/Web Questions/TriviaQA、AlpacaEval；人验 138 片段（67 全双工+71 语义）手势表情测试集；训练数据为 Seamless Interaction 子集。

**主要指标**：
- S2S 准确率：78.0%/47.3%/63.6%（LlamaQ/WebQ/TriviaQA），较 SALMONN-omni 提升 4.4/3.6/7.6 个百分点
- AlpacaEval GPTScore：3.97/3.20（S2T/S2S），与 SALMONN-omni 4.01/3.22 持平
- 轮换成功率：均值 95.2%
- 语义调用头：F1 87.8%，准确率 87.0%
- 手势：对齐 A 0.723、人评 duplex 3.201 最优；引导版 R_SL 1.597、人评语义 2.711（无引导 2.014）、MLLM 语义 0.495
- 表情：LVE 8.74mm、MHD 1.88mm，优于最佳基线 UniLS 的 9.37/2.06mm
- MLLM-人类系统级 Pearson 相关：duplex 0.853、semantic 0.919（均值聚合后）

**是否开源**：数据管线与独立生成器代码已开源 @ https://github.com/bytedance/SALMONN/tree/ELLSA2，完整模型与 checkpoint 录用后开源。

### ⭐ 评分：8/10
评分理由：首次将全双工语音交互与流式手势表情统一到端到端联合优化，双流条件与语义调用解耦设计针对性强，语音指标不降反升，验证联合建模有效。自建数据管线、138 条人验基准与 MLLM 评审相关性分析有社区价值。不足在于评估依赖 MLLM 判断、语义分绝对值仍低（2.7/5），完整代码暂未全部释出。

---

## Speaking Longer Than Learned: Training-Free Long-Form Generation for Full-Stream Text-to-Speech

**arXiv ID**：arXiv:2610.19553 | **方向**：语音大模型

**作者**：Jeseung Lim, Jiseong Woo, Heeseung Kim

**机构**：首尔市立大学（University of Seoul）物理系、AI系

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.19553 | **PDF**：https://arxiv.org/pdf/2610.19553.pdf | **代码**：暂无 | **Demo**：https://voxtend.github.io

### 📌 简介
针对预训练全流式TTS模型VoXtream2在超出训练长度后无法稳定生成的长度外推问题，本文系统分析其基于attention sink的周期性KV缓存重置策略，发现50秒训练边界附近WER从首个10秒窗口的2.74%陡增至11.23%，说话人相似度由0.760渐降至0.695。论文进一步诊断出WER骤升源于训练末段的分布外位置而非缓存重置本身，且相似度衰减源于声学提示注意力被持续稀释。据此提出两项免训练修改：将注意力窗口收缩至W=375帧以规避分布外位置，对提示键pre-softmax注意力logits加常数偏置b=1.5。最终整体WER从8.63%降至3.58%，SPK-SIM从0.659升至0.759，MOS保持4.03不变。

### 🔧 技术方案

**问题背景：** 全流式TTS要求文本到达即低延迟合成，但长时配对语音语料稀缺，模型只能在有限长度（VoXtream2为50秒/625帧裁剪）上训练，推理超出后即退化。已有免训练长文本方案多不面向流式输入，流式长文本生成仍需额外训练；VoXtream2官方继承StreamingLLM的SinkAttention缓存重置并未被诊断其失效根因。

**模型架构：** VoXtream2以参考语音编码的Mimi codec token作为声学提示，由Phoneme Transformer（增量编码音素）、Temporal Transformer（以12.5Hz自回归预测语义与时长token）、Depth Transformer（生成其余codebook）组成；时长token融合shift状态s∈{0,1,2}与音素计数状态u∈{0,1}，单帧音素推进量s+u∈{0,1,2,3}。Temporal Transformer的SinkAttention以本地位置索引缓存帧，上限W=625，达到W即触发重置：保留P个提示帧与τ=⌊W/2⌋个近期帧并重新编号位置。

**核心创新：** (1) 位置与重置的解耦诊断：推理时改变W（400/625/900）使重置点移动而训练范围末端固定在625，发现每帧音素推进率在位置600以下约0.8，接近625时跳至1.9倍与2.6倍；W=900时重置延迟275帧但WER仍于跨越625处从7.3%升至49.8%，重置附近仅47.8%变44.2%，删除错误从0.7%升至16.6%，证明退化跟随本地位置而非缓存重置。(2) 注意力窗口收缩：将W限为375帧，使推理位置始终停留在训练充分覆盖区间，配合提示帧保留维持近期上下文。(3) 声学提示注意力偏置：30秒后屏蔽提示键导致SPK-SIM从0.73崩至0.23，表明提示是上下文中唯一完好的显式说话人参考；对Temporal Transformer全部头与层级的提示键logits施加L'=L+b常数偏置，免训练免改结构，效果优于SpotLight自适应注意力引导。

**训练策略：** 完全免训练，基于官方VoXtream2预训练检查点仅推理期干预；W在{625,500,375,250}、b在{0.5,1.0,1.5,2.0}网格及SpotLight的ψ_target∈{0.1..0.5}上于LibriSpeech-Long dev-clean调参，最终选W=375、b=1.5；RTX 3090上RTF仅由0.415升至0.433，保持实时。

### 📊 实验结果
**数据集**：LibriSpeech-Long dev-clean，281条长录音（最长约4分钟，共15.89小时），取开头平均7.88秒句子作声学提示，其余文本为目标；评估音频统一重采样至16kHz，WER由whisper-large-v3转写并用Qwen3-ForcedAligner-0.6B强制对齐后按10秒窗口统计。

**主要指标**：
- WER（整体）：3.58%，较VoXtream2原型的8.63%降低5.05个百分点；180-210秒分段3.96%，原模型为9.79%
- SPK-SIM（ECAPA-TDNN余弦相似度，整体）：0.759，较原0.659提升0.100；180-210秒0.754，原0.595，而长文本训练的Qwen3-TTS同段跌至0.560
- MOS（5分制，158名听者、325条评分/模型）：4.03±0.09，与原模型4.03持平，接近Mimi重建上限4.10
- 关键对比：WER仍逊于Qwen3-TTS-1.7B（1.59%）与MOSS-TTS-v1.5（1.77%），受限于VoXtream2自身稳定区间；但长时SPK-SIM稳定性显著优于两者

**是否开源**：代码暂未提供（基于官方VoXtream2实现与公开检查点）；项目页 https://voxtend.github.io 提供音频demo。

### ⭐ 评分：7/10
评分理由：诊断部分设计干净，通过移动重置点解耦"位置 vs 缓存重置"的对照实验说服力强，提示屏蔽实验亦扎实定位了相似度衰减根因。方法极简、免训练、即插即用且RTF几乎不变，对实时语音对话系统落地有直接工程价值。不足在于仅覆盖单一基座模型与英文单语料，WER绝对值仍未达到长文本训练模型水平，跨模型泛化性未验证，属实质贡献但非突破。

---

## Long-Prompt Zero-Shot TTS: Benchmarking Prosody Reproduction Beyond Voice Cloning

**arXiv ID**：arXiv:2610.19774 | **方向**：语音大模型

**作者**：Dekun Chen, Renjie Xu, Yingda Shen, Qinke Ni, Zhizheng Wu

**机构**：The Chinese University of Hong Kong, Shenzhen；Amphion Technology Co., Ltd.

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.19774 | **PDF**：https://arxiv.org/pdf/2610.19774.pdf | **代码**：暂无（声明录用后释出） | **Demo**：暂无

### 📌 简介
零样本TTS通常以数秒短prompt为条件，只能传达音色，难以复现说话人语速、停顿、重音与语调等长期韵律习惯；逐说话人微调则有额外训练与管理成本。本文将推理时使用分钟级长prompt、不更新目标说话人参数以复现其特定韵律的任务形式化为Long-Prompt Zero-Shot TTS，构建中英双语LP-TTS-Bench（37位说话人、63.95小时prompt、2728条测试句）及九项客观指标加P-MOS的多维评测协议，并以带分层长prompt编码器的LPTTS作为参考系统。实验中文P-MOS达3.529、CER 1.03%，每语言8项韵律指标中6项优于微调基线。

### 🔧 技术方案

**问题背景：** 短prompt只能捕捉音色，韵律随语境与习惯变化仅暴露局部实现；说话人适配需逐人训练，多utterance prompt实现如Mega-TTS 2/PerTTS未公开；现有评测以可懂度与相似度为主，缺少韵律复现的对齐指标。

**模型架构：** Qwen3TTS-Base为骨干，音色沿用原生speaker encoder，韵律由长prompt编码器建模：取16个RVQ码本全量特征，长prompt切成≤30秒chunk压缩为与时长无关的32个定长向量（8个global韵律token+24个由目标文本query检索的local token），经Flamingo式门控交叉注意力注入Qwen3 LM第16/20/24/26层，门控初始0.01。

**核心创新：** (1) 提出任务与LP-TTS-Bench：时间（SRD、PD）、重音（PCC）、语调（IC、PRD，半音）、表征（MPM-SIM、AutoPCP）经ForcedAligner逐句对齐比较，限定各系统WER/CER<0.1的公共子集。(2) 分层编码器解耦长度处理与韵律提取，文本条件检索有统计支撑（closer rate 62.6%，p<0.001）。(3) 同说话人正负prompt排序目标（margin 0.05、权重0.2，用于40%长批次并剔除目标周边防捷径）；再以基准外约20小时微调教师做on-policy蒸馏：自生成轨迹token级JS散度，仅更新编码器与注入模块。

**训练策略：** 编码器用约5万小时野外中英说话人配对语音，70%批次取1至30分钟长prompt、损失为CE加0.2倍排序项；全训编码器与GCA，骨干仅16层LoRA其余冻结。基线用10秒prompt，SFT为37人各全参微调5轮选点，LPTTS推理用10分钟prompt；P-MOS为100句3听众1-5分盲评。

### 📊 实验结果
**数据集**：LP-TTS-Bench（中文17人+英文20人，63.95小时prompt，3559条验证、2728条测试句，每人57至80条大于5秒测试句，与5万小时训练数据互斥且不入prompt）

**主要指标**：
- 中文LPTTS：CER 1.03%（基线0.73%、SFT 1.78%），SRD 0.137、PD 0.067、PCC 0.410、IC 0.474、PRD 4.532半音、MPM-SIM 0.734、SIM-O 0.57
- 英文LPTTS：WER 1.64%、SRD 0.112、PD 0.061、IC 0.335、PRD 3.279、MPM-SIM 0.681、SIM-O 0.78
- P-MOS（1-5分）：中文3.529、英文3.533，高于SFT的3.471/3.267与基线2.941/3.133
- 关键对比：零训练下每语言8项韵律指标中6项优于目标说话人SFT且CER更低；prompt增至约10分钟收益最大后饱和，SIM-O全程稳定

**是否开源**：基准、评测脚本与音频样本声明论文录用后发布，当前未释出

### ⭐ 评分：7/10
评分理由：任务定义填补了说话人特定韵律复现难以评测的空白，九指标配合强制对齐与显著性检验具方法论原创性；中英双语、主观P-MOS与prompt长度消融使结论可信。不足是可懂度仍逊于base、PRD与AutoPCP未全面领先，参考系统偏初始且暂未开源，总体是扎实的社区贡献。

---

## ACR-Net: Mitigating Semantic Dominance via Contrastive Acoustic-Semantic Decoupling

**arXiv ID**：arXiv:2610.20114 | **方向**：语音大模型

**作者**：Mengke Zhang, Yanda Shao, Tianhe Wu, Kai Feng

**机构**：北京邮电大学（中国北京）

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.20114 | **PDF**：https://arxiv.org/pdf/2610.20114.pdf | **代码**：https://github.com/zmkshakespar/ACR-Net | **Demo**：暂无

### 📌 简介
针对语音情绪识别与语音LLM在语调与文本语义冲突时盲目信任文本的"语义主导"现象，本文用EmotiVoice对抗合成配对冲突语音构建ASPIRE基准，并提出SOP与LDD两指标量化文本过自信与潜层纠缠。ACR-Net以冻结Whisper双流加LoRA为骨干，经跨模态注意力定位冲突后，用对比解耦损失将矛盾表征投影至正交潜空间。结果显示现有模型在极性冲突下近乎失效（ACC低于45%、SOP高于0.5），而ACR-Net在ASPIRE上达ACC 76.5%、SOP 0.128、LDD 0.864，较最强基线MCR提升28个百分点，五个一致数据集上仍保持88.5%至93.1%的准确率。

### 🔧 技术方案

**问题背景：** 多模态SER与Audio LLM在音义一致语料反复训练后形成僵化语义先验，文本token的低方差语义捷径压制细微声学线索，标准情感集筛除不一致样本更甚。已有缓解手段仅做融合层重加权、移动决策边界，无法恢复已塌缩的声学表征。

**模型架构：** 结构隔离双流编码器：音频流为冻结的Whisper-Medium，向每个自注意力块注入LoRA以学习气息、音高等细粒度线索，输出E_a；文本流用冻结Whisper文本编码器提取纯语义序列E_t作锚点。CMA以E_a为Query、E_t为Key/Value，经残差与时间均值池化得h_a、h_t，经线性分类器出四类情绪。

**核心创新：** (1) ASPIRE对抗基准与探针指标：1800条冲突提示由EmotiVoice-1.5B合成，重采样16kHz后经emotion2vec+剔除低置信与提示不符样本并经专家终审，得四类19对共1200条无歧义冲突样本；SOP量化文本相对声学的概率优势，LDD度量h_a与h_t的正交度。(2) 将CMA由模态混合器重构为主动不一致检测器：让声学序列扫描语义序列、定位与语调相悖的词元，为空间解耦提供时序对齐依据。(3) 对比解耦损失L=L_CE+λL_Decouple：正常样本拉近h_a与h_t的余弦相似度，冲突样本按margin m铰链推斥至正交子空间；仅CMA时ACC 53.0%、仅解耦损失62.1%，两者互补、区别于纯权重转移。

**训练策略：** 5折交叉验证，每折960条训练微调、240条留验，另200条独立测试统一评测；最优λ=0.1、m=0.5，λ=1.0时LDD达0.890但ACC降至71.2%、λ=0.01欠解耦仅60.4%；标签统一映射为Angry/Happy/Sad/Neutral四类，基线均zero-shot评测；优化器与学习率等论文未披露。

### 📊 实验结果
**数据集**：ASPIRE（1200条对抗合成加200条独立测试，16kHz）与EmoDB、CASIA、SAVEE、CREMA-D、RAVDESS五个跨语种情感语料

**主要指标**：
- ASPIRE总体ACC：76.5%，较MCR（48.5%）绝对提升28.0个百分点，高于Tensor Fusion（43.8%）与朴素拼接（41.2%）
- SOP：0.128（MCR为0.628、朴素拼接0.824）
- LDD：0.864（MCR为0.242），四类冲突下均超0.812
- 分冲突ACC：极性68.4%、唤醒85.2%、效价75.8%、抑制78.5%，较融合基线FAS高25.9、16.8、20.2、25.7个百分点
- 一致场景ACC：SAVEE 88.6%全场最高；EmoDB 88.5%超过全部多模态基线；RAVDESS 93.1%与CASIA 86.8%仅次可能受数据污染影响的Qwen2-Audio（94.2%、91.8%）

**是否开源**：代码与数据集开源 @ https://github.com/zmkshakespar/ACR-Net

### ⭐ 评分：7/10
评分理由：选题切中Audio LLM文本捷径偏差的真实痛点，基准、指标、架构三者自洽，消融与λ、margin敏感性分析支撑方法必要性，一致场景几无退化。局限在于ASPIRE全为TTS合成且仅千余条，ACR-Net在本基准微调而基线zero-shot的对比存在结构性优势，训练细节披露不足影响复现。

---

## Noise-Aware Lombard Speech Synthesis via Flow-GRPO for Intelligibility Optimization

**arXiv ID**：arXiv:2610.20181 | **方向**：语音大模型

**作者**：Zhaoyang Wang, Dingding Yao, Chengzhong Wang, Junfeng Li

**机构**：中国科学院声学研究所言语声学与内容理解重点实验室、中国科学院大学

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.20181 | **PDF**：https://arxiv.org/pdf/2610.20181.pdf | **代码**：暂无 | **Demo**：https://kalenon.github.io/NIL-TTS-demo/

### 📌 简介
语音交互智能体普遍声学不敏感，难以复现人类听觉-发声反馈的Lombard效应。本文提出NIL-TTS：在F5-TTS流匹配骨干中引入FiLM环境条件注入，采用"Lombard配对语料监督微调+Flow-GRPO以可懂度为直接目标的强化后训练"两阶段范式。−6 dB噪声下Seed-TTS test-zh平均WER由基线0.378降至0.224，ESTOI从0.246升至0.298，主观识别正确率由0.367升至0.598，RTF仅0.27。

### 🔧 技术方案

**问题背景：** 现有Lombard TTS依赖稀缺配对语料的监督微调、SNR反馈的响度启发式调节或静态风格嵌入，本质上优化与训练数据的L2声学相似度而非可懂度，且无法建模对环境噪声谱形与强度的依赖动态，泛化差、在恶劣噪声下可靠性退化。

**模型架构：** 基座为F5-TTS：DiT骨干22层、d_model=1024、16头，ConvNeXt V2文本编码器（512维），生成100维mel谱经Vocos声码器输出24 kHz波形。环境感知分支以预训练DAC编码器（44.1 kHz）提取噪声嵌入E_noise，MLP将标量SNR投影为E_snr，二者AvgPool后拼接投影为全局条件c_env，经逐层线性映射生成缩放/偏移参数γ_i、β_i，对i>2的深层DiT块隐状态做特征级线性调制，总参数382M。

**核心创新：** (1) FiLM环境感知通路：将噪声波形谱与SNR强度显式建模为全局条件注入深层DiT块，保留浅层学习自干净语音的音素对齐；区别于静态风格向量，输出可随噪声类型与强度连续自适应。(2) 强化学习与声学反馈机制同构化：将确定性ODE采样重构为保持边缘分布的SDE采样（σ_t=a√(t/(1−t))，a=0.4），每提示生成G=24条轨迹做组相对优势估计，Flow-GRPO直接在连续mel空间在线优化，无需critic模型。(3) 听觉反馈代理奖励：rollout混入目标噪声后由SenseVoice-Small转录，R_acc=1−WER；辅以WeSpeaker嵌入余弦相似度R_spk约束音色不失真，权重λ_acc=6.0、λ_spk=1.0。

**训练策略：** 阶段一SFT：plain与Lombard mel沿时间维拼接为复合目标，EMALG（10,200句、34人，40/55/80 dB SPL）与LombardGrid（5,400句、54人）配对语料叠加DEMAND六类环境噪声，SNR均匀采样U(−7,5)dB，掩码流匹配损失；冻结DiT仅训FiLM模块，AdamW、lr 1e-4、批大小8、68万步、2×NVIDIA A40。阶段二GRPO：全模型解冻，WenetSpeech4TTS-Premium 945小时（DNSMOS>4.0）+ICASSP2021 DNS噪声约181小时150类，SNR U(−10,15)dB，lr 1e-6、400步warmup、共4,800步，rollout NFE=32，KL系数β=0。推理用ODE 32 NFE、CFG=2.0。

### 📊 实验结果
**数据集**：Seed-TTS客观集（2,020条中文DiDiSpeech+1,088条英文Common Voice），合成语音混入NoiseX-92的Babble/Factory/Pink/White四类噪声，SNR 6至−9 dB六档，评测重采样16 kHz。

**主要指标**：
- WER（test-zh，−6 dB四噪声均值）：0.224，基线F5-TTS为0.378，绝对降低0.154（95% CI [0.219,0.228]）
- ESTOI（test-zh，−6 dB）：0.298，基线0.246，提升0.052
- WER（test-en，−6 dB）：0.434，基线0.568，降低0.134，可零样本跨语言迁移
- 主观识别正确率（Babble，−6 dB，12人听测，360条）：0.598 对 基线0.367，提升0.231（p<0.001）
- 关键对比：优于SFT-only（WER 0.289）与RL-only（0.323）；超越SS/SSDRC信号处理与F5-TTS-Style Lomb、MetaVoice-1B Lomb等神经基线
- 效率：382M参数、RTF 0.27（基线336M/0.26），远低于MetaVoice-1B Lomb的1.2B/3.04

**是否开源**：发布Demo音频页，代码暂无。

### ⭐ 评分：7/10
评分理由：首次将在线强化学习引入Lombard语音合成，以ASR-WER奖励显式优化可懂度，机制类比与实验设计扎实；消融了KL系数、NFE与扩散强度，主客观结论一致，推理开销近乎可忽略，车载等场景实用价值高。局限在奖励绑定SenseVoice-Small存在奖励过拟合风险，Lombard配对语料规模有限，且未报告自然度MOS。

---

## Probing Neural Audio Codecs with Speaker Traits and Speech Characteristics

**arXiv ID**：arXiv:2610.20955 | **方向**：语音大模型

**作者**：Jihwan Lee, Tiantian Feng, Minu Kim, Junhyeok Lee, Sean Foley, Thanathai Lertpetchpun, Najim Dehak, Dani Byrd, Shrikanth Narayanan

**机构**：Signal Analysis and Interpretation Lab (SAIL), University of Southern California; Center for Language and Speech Processing, Johns Hopkins University

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.20955 | **PDF**：https://arxiv.org/pdf/2610.20955.pdf | **代码**：暂无 | **Demo**：https://jihwanlee15.github.io/codec-trait-depth/

### 📌 简介
针对RVQ神经音频码本堆栈如何编码说话人特质与语音特性不明的问题，本文对17个公开多码本编解码器在性别、年龄、口音、嗓音质量、情感、语流、非语言声七种特质上做探针分析：用前k个码本部分解码重构语音，由机器听者比较其在原始音频与重构上的判定，定义trait depth为重加权Cohen's κ首达全深度90%时的相对码本深度。结果显示性别特质深度最浅、语流次之，嗓音质量与年龄组需更深堆栈，其余特质居中，表明码本层级并非均匀粗到细，须按特质评估与设计。

### 🔧 技术方案

**问题背景：** 语音大模型社区普遍假设RVQ堆栈从粗到细、首码本承载说话人身份，蒸馏类编解码器又把语音内容压入首码本，但性别、口音、情感等具体特质在第几层被编码并可恢复仍不明；现有评测局限于可懂度、说话人相似度或单一特质，缺少跨深度跨特质的系统定位。

**模型架构：** 本文为探针协议而非新模型：编码c_{1:K}=E(x)，以前k个码本前缀解码x̂_k=D(c_{1:k})；被测17个公开编解码器（EnCodec、DAC、Mimi、SpeechTokenizer、FunCodec、DualCodec、PAST及流式版、X-Codec、MaskGCT、TAAE、MOSS、JHCodec等），帧率12.5-75Hz、码本4-32个、码率0.95-24kbps；机器听者用VoxProfile（性别/年龄/嗓音/情感/语流）、Voxlect（口音）、SSLAM（非语言声），另有辅助听者交叉验证。

**核心创新：** (1) 提出trait depth度量：d_t=min{(k−1)/(K−1): κ_t(k)≥0.9κ_t(K)}，以单一阈值回答编码深度，无需逐编解码器训练探针。(2) 对Cohen's κ重加权：按后分层与重要性加权，用正确/错误乘多数/少数类四分层赋权，参考分布取七特质均值且固定不变，消除类分布与听者精度偏差。(3) 17编解码器乘7特质的逐类逐深度曲线探针面，并以DualCodec/FunCodec/PAST同族配对隔离帧率、蒸馏、流式化变量。

**训练策略：** 本研究不做任何训练，编解码器与听者均用已发布checkpoint仅做推理与评分，约1400 GPU时（A40/L40S/P100/A100）；输入统一16kHz再重采样至各码原生率，解码后回16kHz；码本≤12的模型解码全部前缀1..K，25/32码本解码至8后稀疏取点，DAC取前8个码本。

### 📊 实验结果
**数据集**：口音用Voxlect英语集（39,911条/82.18h），性别年龄用TIMIT+VoxCeleb+CommonVoice（12,619条/23.45h），嗓音用ParaSpeechCaps（13,076条/27.16h），非语言声用VocalSound（3,591条/4.14h），语流用SEP-28k+FluencyBank测试集20%（1,622条/1.35h），情感用IEMOCAP随机10%（600条）。

**主要指标**：
- 17编解码器均值下性别trait depth最浅、语流次之，嗓音质量与年龄组最深，情感/口音/非语言声居中
- 语流六类均在相对深度约30-40%处达90% κ，类间差异最小
- 非语言声中笑仅需约20%相对深度，喷嚏、咳嗽需50-60%
- 帧率与蒸馏：同设计下25Hz DualCodec、50Hz FunCodec比低帧率版在更早码本保留多数特质；蒸馏类首码本保留更多但trait depth整体更深，特质并未集中于首码本
- 关键对比：PAST离线版全深度κ在7特质中6个高于PAST-streamable，流式化对首码本几乎无影响、全深度影响更大

**是否开源**：分析代码未开源，仅提供交互式结果网页（见Demo），且出于伦理不发布特质编辑工具。

### ⭐ 评分：7/10
评分理由：首次系统量化特质的码本编码深度，trait depth定义简洁、重加权统计严谨，17个编解码器与同族配对为语音LM选tokenizer与匿名化设计提供参考。不足是度量依赖机器听者而非人类感知、数据集规模悬殊且以英语为主、聚合对比混杂变量未完全控制，属增量但扎实的评测分析（本工作实际偏"语音大模型/表示分析"）。

---

## What Does LALM Post-training Learn? Rethinking Audio Understanding and Reasoning Capabilities

**arXiv ID**：arXiv:2610.19476 | **方向**：语音大模型

**作者**：Hua-Hsuan Chen, Xuanjun Chen, Wei-Chung Lu, Chih-Kai Yang, Yu-Xiang Lin, Sung-Feng Huang, Haibin Wu, Hung-yi Lee

**机构**：National Taiwan University、NVIDIA、NTU AI-Core

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.19476 | **PDF**：https://arxiv.org/pdf/2610.19476.pdf | **代码**：暂无（所用开源模型为既有checkpoint） | **Demo**：暂无

### 📌 简介
LALM（Qwen2.5-Omni、Qwen2-Audio 等）的后训练在 MMAU/MMAR 等基准带来大幅提升，但增益究竟来自听觉能力还是文本/题型捷径长期缺乏干净证据。本文用两项受控协议解耦二者：①把评测音频替换为等长静音，量化"静音下仍保留的增益"；②把多选题改为开放式作答，消除选项先验。结论是多数后训练增益在无音频时仍存在、换格式即消失——后训练主要教会模型利用文本线索与答题模式而非"听懂"。该结果对语音基准的可信度构成直接冲击。

### 🔧 技术方案

**问题背景：** LALM 基准分数提升普遍归因于音频理解与推理增强，但静音对照与题型消融此前从未在统一预算下做过；若不区分真实听觉贡献与格式适应，后训练方法（SFT/RL/VCRL）的比较实际上都在优化捷径。

**模型架构：** 不提出新架构；在 Qwen2.5-Omni-3B/7B 与 Qwen2-Audio-7B-Instruct 上复现受控对照：评测时将音频换为等长静音、多选题改为开放式作答，由 Qwen3.6-27B 做 LLM 裁判判语义等价；另统一预算对比 SFT/RFT/GRPO/VCRL 及 R1-AQA、Ke-Omni-R 等开源后训练模型。

**核心创新：** (1) Audio/Silence Gain 指标：相对基座量化后训练增益中静音条件下仍保留的比例，把真实听觉贡献与文本捷径分离；GRPO+Qwen2-Audio MMAU 增益 45.2→60.0（+14.8），其中静音下仍 +11.2。(2) 题型解耦协议：开放式作答消除选项先验后，后训练增益几乎全部消失，证明原增益高度依赖多选格式。(3) 纯静音训练对照：仅在静音音频上训练也能在真实音频上提升，AudioMCQ 上静音增益（+6.4）反超音频（+5.0），坐实文本线索主导。

**训练策略：** 训练池 12,267 条 MC 音频 QA（7,129 段/17.4h，AudioSet 6,196/Medley 4,913/DailyTalk 1,158 条），10,446 训练+1,821 留出；四种后训练方法统一 LoRA 200 步、3 个随机种子、共享最终答案匹配奖励；音频级匹配确认训练-评测零泄漏。

### 📊 实验结果
**数据集**：MMAU test-mini（1,000 条）与 MMAR（1,000 条）；训练域 AudioSet/Medley/DailyTalk。

**主要指标**：
- MMAU：GRPO 提升 +14.8 分，其中 +11.2 在静音下保持；R1-AQA +23.4（静音 +17.2）
- 类目：MMAU 推理/信息抽取类目静音增益普遍约 +7 分
- 开放式作答：后训练增益几乎全部消失（跨模型一致）
- AudioMCQ：静音增益 +6.4 > 音频增益 +5.0；纯静音训练在真实音频上仍有提升
- 关键对比：跨 3 个基座、6 种后训练方法结论一致，增益主体为文本线索与答题模式

**是否开源**：论文未给出代码发布链接，暂无；所用模型均为公开权重。

### ⭐ 评分：7/10
评分理由：诊断设计干净（静音/格式双对照+纯静音训练的反直觉消融），跨模型跨方法交叉验证使"后训练教猜不教听"的结论可信且有冲击力，对 LALM 评测方法学有直接价值。局限在于纯分析工作、未提出改进方案，训练语料偏小（17.4h），且基座限于 Qwen 系，对更大规模/多模态融合模型的普适性待验证。

---

## TVPara: Paralinguistic Captioning of Expressive TV-Series Speech in Complex Acoustic Environments

**arXiv ID**：arXiv:2610.19678 | **方向**：语音大模型

**作者**：Ziyang Zhang, Wenyi Yu, Wen Wu, Xuenan Xu, Chao Zhang

**机构**：清华大学；上海人工智能实验室

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.19678 | **PDF**：https://arxiv.org/pdf/2610.19678.pdf | **代码**：暂无（承诺后续开源标注与代码） | **Demo**：https://windowso.github.io/TVPara/

### 📌 简介
本文提出TVPara，一个基于19部英语电视剧构建的副语言描述数据集，针对大型音频语言模型（LALMs）在强烈情绪与复杂背景声共存语音上描述粗糙失准的问题。数据集定义单话语（约492小时）与多话语（约213小时）两个副语言描述任务，采用LALM预标注加人工精修的闭环流程标注。微调SALMONN与Qwen2.5-Omni后，模型在复杂声学环境下的副语言理解平均相对提升31.26%，且增益可泛化到未见过的电视剧与更干净的跨领域VoxCeleb语音。

### 🔧 技术方案

**问题背景：** 现有副语言语料多为录音室采集、干净语音库重新标注或TTS合成，极少同时具备强烈情绪与背景声；少数野外语料只有类别或维度标签而无自由文本描述，且逐条孤立标注，无法刻画情绪跨话语的动态变化。

**模型架构：** TVPara取自19部英剧官方YouTube音轨，含单话语副语言描述（256,212条，492小时，均长6.91秒，caption均长32.8词）与多话语描述（45,402条，213小时，均长16.89秒，58.1词）两任务，围绕情绪、语速、音高、音量四项属性做自由文本描述，后者强调属性随时间的变化轨迹。

**核心创新：** (1) 提出多话语副语言描述任务：从同一集截取N（N∈[3,5]）条相邻话语为连续音频，用LLM将内部已精修的单话语caption按时间顺序合并为一条caption，显式建模副语言属性跨话语变化（55.5%相邻话语情绪类别不同），为现有语料所无。(2) 迭代式人机协同标注管线：SALMONN-13B预标注、GPT-4o-mini润色、商业标注员逐条对照音频修正幻觉与遗漏；修正约50小时后用其微调预标注模型再标注剩余数据，人工改动率由38%降至17%，初始双子标注一致率87%。(3) 细粒度LLM-as-a-Judge评测与感知验证：GPT-5-mini从生成与金标caption中抽取四原子属性逐项比对打0-4分；另用Spearman相关检验增益源于音频感知而非拟合标签分布。

**训练策略：** 冻结音频编码器，微调跨模态adapter，LLM用LoRA（r=8，α=32）；在NVIDIA H200上做SFT，单/多话语数据打乱共享一个checkpoint，10 epochs，batch size 24，cosine调度峰值学习率3e-6并5% warmup；SALMONN用官方代码库、Qwen2.5-Omni用ms-swift。按集留出约5小时测试（训练约487小时），另整体留出一部剧作unseen系列测试集。

### 📊 实验结果
**数据集**：TVPara（合计约705小时，19部英剧；非中性情绪67.2% 对 VoxCeleb的2.9%，含背景声36.2% 对 8.0%）；unseen系列与VoxCeleb（134条）跨域测试集。

**主要指标**：
- SALMONN单话语音量分：2.31→3.58（zero-shot→SFT，0-4分制）
- SALMONN多话语音量/情绪分：1.04→1.81 / 1.09→1.60
- Qwen2.5-Omni多话语情绪分：0.99→1.46
- 关键对比：SFT对zero-shot平均单元格相对提升31.26%（Wilcoxon p<0.01）；unseen系列中含背景声clip提升32.4%，无背景声仅19.9%
- 感知校验：SALMONN预测音量与音频能量Spearman相关由0.03升至0.85，unseen系列/VoxCeleb上保持0.87/0.73

**是否开源**：将发布副语言标注、源视频链接与时间戳（不分发音频），代码承诺开源；样例页 https://windowso.github.io/TVPara/ 已上线。

### ⭐ 评分：7/10
评分理由：论文命中LALM副语言理解的真实数据缺口，TVPara以约705小时规模首次同时提供表现情绪、复杂声学环境与自由文本描述，多话语任务是新设定；迭代人机标注与相关性去混淆分析体现方法深度。不足在于评测依赖LLM裁判且绝对分值偏低，底座模型仅两个，结论普适性有限，属数据集资源型的实质性贡献。

---

## Zero-Shot Spoken Language Understanding with SLAM-ASR: What Do Monolingual ASR-Trained Linear Projectors Enable?

**arXiv ID**：arXiv:2610.20844 | **方向**：语音大模型

**作者**：Edwin Arkel Rios, Sneh Sourabh, Jocelyn Zaruma, Girish Ewoorkar, Julian Mack, Bo-Cheng Lai

**机构**：阳明交通大学（台湾）、Tranxform AI、印度理工大学海德拉巴分校、法国东方语言文化学院与新Sorbonne大学、Cohere 与 Cohere Labs Community

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.20844 | **PDF**：https://arxiv.org/pdf/2610.20844.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文检验SLAM-ASR配方的零样本口语理解（SLU）能力：对11种语言各仅用WorldSpeech转录损失训练一个线性投影器，编码器与LLM解码器完全冻结。提示模型回答关于音频的是非问题，平均指令遵循率IFR为49.8%，未遵循时退回转录；改用数字模板问主题，IFR升至81.3%，但主题平衡准确率仅23.2%（机会14.3%），同一解码器输入参考转写文本可达71.5%。结论：ASR监督已能自发涌现指令遵循，SLU瓶颈在投影器未向解码器传递语义。

### 🔧 技术方案

**问题背景：** SLAM-ASR路线的既有研究几乎止步于ASR能力评估，少数零样本SLU探索改用可训练Transformer投影器，系统成本上升。纯线性投影器加ASR监督能否支撑转录之外的理解任务，此前缺乏系统验证，也没有定位瓶颈是投影器还是解码器的诊断手段。

**模型架构：** 三段式：冻结Whisper-medium语音编码器、可训练线性投影器（配Tiny Aya时2.1M参数，配Qwen3-4B时2.6M；整体3.66B/4.33B）、冻结的Tiny Aya Global文本解码器。每语言一个投影器在WorldSpeech转录数据上训练，输入语音不超过30秒。评测涵盖转录、是非问答与SIB-Fleurs七类主题分类；音频输出仅在恰好命名一个选项且其他词不超过8个时判为有效作答。

**核心创新：** (1) 首次系统研究纯ASR监督下SLU的零样本涌现：六个冻结解码器乘以11种语言共66个投影器，全程无任务训练与任务标注，并以IFR区分"不遵循指令"与"答错"，发现超过半数语言可稳定以短答案形式应答而非转录。(2) 揭示提示格式的强敏感性：数字模板平均IFR 81.3%，开放式提问至多16.0%；译文版语言内模板降至65.0%；且识别质量不预测指令遵循，印地语与法语CER几乎相同（15.25 对 15.26），IFR却是3.6% 对 79.3%。(3) 语音、级联、文本上限三级归因诊断：主题BAcc从音频的23.2%升到先转录的52.5%，再到参考文本的71.5%，证明主题知识存在于解码器、失败点为投影器的音文对齐；是非问答则是解码器自身真实能力缺口。

**训练策略：** 只训练线性投影器，优化音频转录的token交叉熵损失；1000步，有效批大小512条，AdamW与余弦调度，warmup 10步；Tiny Aya学习率1.5e-3，Qwen3-4B为1.0e-3；各语言训练规模差异大（印地语约2,189小时，乌尔都语约81小时），样本限30秒内。

### 📊 实验结果
**数据集**：训练用WorldSpeech（11语言单语转录子集）；评测用FLEURS朗读语音与SIB-Fleurs主题标签（点名句子占13.1%，是非伪标签由教师模型从平行参考文本生成）。

**主要指标**：
- 是非问答IFR：平均49.8%（英语93.5%最高，泰米尔语0.2%最低）
- 是非问答BAcc：45.5%-54.0%，均处机会水平（50%）
- 主题分类（数字模板）：IFR 81.3%，BAcc 23.2%（机会14.3%）
- 与Qwen2-Audio-7B对比：后者BAcc 39.4%，高出16.2个百分点，但仍有4种语言低于多数类预测
- 归因梯度：主题BAcc音频23.2%、级联52.5%、参考文本71.5%；指令微调文本端稳定在71.4%-73.8%，Base变体仅17.4%
- 转录质量：CER从西班牙语3.09%到泰米尔语87.87%

**是否开源**：论文未给出代码或Demo链接，暂无。

### ⭐ 评分：6/10
评分理由：这是一篇诊断性质的实证研究：66投影器矩阵与三级归因设计干净，IFR指标恰当，"瓶颈在投影器对齐、不在解码器知识"的结论对SLAM-ASR后续的可控对齐训练有直接参考价值。不足在于无任何方法创新，绝对性能距实用很远，是非伪标签未经独立验证，仅单随机种子与朗读式窄域数据，且模板格式敏感性未做消融，结论鲁棒性有限。

---

## Revise-TTS: A Non-Masking Refinement Framework for Masked Diffusion Models in Text-to-Speech

**arXiv ID**：arXiv:2610.19499 | **方向**：语音大模型

**作者**：Wanli Sun, Dan Su, Anton Ragni

**机构**：谢菲尔德大学计算机科学学院（UK）、HojoAI（北京，一作于HojoAI实习期间完成）

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.19499 | **PDF**：https://arxiv.org/pdf/2610.19499.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
基于掩码扩散模型（MDM）的零样本TTS每步仅提交最高置信度的预测位置，token一经提交便无法修改，导致错误沿去噪步累积传播。本文提出单阶段框架Revise-TTS：用层次二值量化（HBQ）替代FSQ，为语音token引入显式粗到细的二值层级结构；同时引入生成式精炼网络（GRN），训练时从真实与随机token的混合物中重建完整token图，推理时迭代丢弃一小部分已预测位置并随机重置后重新预测，实现自我纠错。主模型在Seed-zh取得WER 1.19%、UTMOS略超录音真值，HBQ在同等码本容量下显著优于FSQ，可推广至任意MDM-based TTS。

### 🔧 技术方案

**问题背景：** MDM解码按互不重叠的掩码调度提交预测，被错误提交的token在后续步无法修正，且误差难以归因于两级系统的具体模块；另一方面，FSQ对每个隐维独立取固定标量电平，表征扁平，提精度需增维或扩码本，大码本又使token预测空间膨胀、训练困难。

**模型架构：** 骨干沿用OmniVoice的单阶段MDM，以文本x与prompt语音token为条件，由双向Transformer对声学token图Y_0∈V^{T×Q}并行去噪；语音tokenizer用XCodec2.0，其声学编码器与语义编码器特征拼接为融合表征H∈R^{T×C}后经HBQ量化。两种表示对应两种模式：GRN_ind输出索引token（C·2^M路分类），GRN_bit输出展平二值token（CM路二分类）。

**核心创新：** (1) 首个错误可修正的MDM-based TTS：将视觉合成中的GRN范式引入语音，把生成视为迭代全局精炼而非masked-token预测，训练时对完好与损坏token统一做交叉熵重建，天然摆脱掩码调度约束。(2) HBQ语音token量化：先tanh归一化，再做M轮二分，第m轮以中心c_m=Σ(2b_r−1)/2^r判0/1，每轮区间减半，码字对应宽度2^{1−M}的区间、最大误差2^{−M}，精度可随M扩展而不增大分类空间。(3) 重叠解码自纠错：推理从全随机token图出发，共K=32步，每步按保留率l=ρ[1−cos(πτ/2)]（ρ=0.999）的余弦调度选保留位置，其余重置为随机token重预测，无需额外误差定位头或策略网络。

**训练策略：** 损失为token图上所有T×Q位置的交叉熵，保留率l~U(0,1)均匀采样以覆盖连续腐蚀强度。消融模型用LibriTTS-R（585小时英文24kHz）+WenetSpeech4TTS premium（945小时中文16kHz），4×A100、batch 1.8k秒、100k步；主模型用Emilia英文46.8k小时+中文49.9k小时，16×A100、batch 6.5k秒（每GPU 20480 token）、250k步约1 epoch；AdamW（β1=0.9，β2=0.999，ε=1e-8），lr=1e-4；微调对比实验8×GPU、100k迭代。

### 📊 实验结果
**数据集**：评测用LibriSpeech-PC test-clean（2215条英文）与Seed-TTS中英双语基准（2020条中文）；训练用Emilia（EN 46.8k h+ZH 49.9k h）、LibriTTS-R（585h@24kHz）、WenetSpeech4TTS premium（945h@16kHz）

**主要指标**：
- SIM（LS-PC）：HBQ [2^2]^8 GRN_ind 0.427 对 FSQ [4]^8 0.290，同码本容量下提升0.137
- WER（LS-PC/Seed-en/Seed-zh）：HBQ [2^2]^8为1.86/5.06/1.83，为消融中最低；主模型Seed-zh WER 1.19%（真值1.25%）
- UTMOS：主模型LS-PC 4.03，略高于真值4.01；三测试集均接近或超过真值
- 关键对比：LS-PC SIM 0.519落后OmniVoice（0.697）约0.178；主观CMOS EN −0.34±1.67、ZH −0.63±1.88，与F5-TTS（−0.30）MaskGCT（−0.21）相当，OmniVoice +0.28最高

**是否开源**：暂无（论文全文未给出代码与Demo链接）

### ⭐ 评分：6/10
评分理由：首次把GRN纠错范式与HBQ量化引入MDM-based TTS，思路清晰、免额外纠错模块，且可即插即用地扩展至任意MDM TTS，消融覆盖多组(C,M)配置与bit/ind两种模式，较系统。但主模型在说话人相似度与英文WER上仍明显落后OmniVoice，GRN微调略逊于同数据masking微调，纠错收益未在主结果中充分兑现，且未开源，属有参考价值的增量探索。

---

## From Detection to Anticipation: Continuous Onset Forecasting for Stuttered Speech

**arXiv ID**：arXiv:2610.19235 | **方向**：语音前端

**作者**：Tampu Ravi Kumar, Ayoub Daliri, Vivek Gupta

**机构**：亚利桑那州立大学计算与增强智能学院、健康解决方案学院

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.19235 | **PDF**：https://arxiv.org/pdf/2610.19235.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有口吃自动系统几乎都在不流畅发生之后才做检测，无法支撑选择性听觉反馈等预期式干预。本文首次将口吃预测形式化为连续因果的时间到事件预报：每100毫秒基于事件前的语音估计未来窗口内口吃 onset 的风险，并人工扩充 FluencyBank Timestamped 得到36说话人2872个 onset 事件。方法为冻结 Whisper-large-v3 编码局部2秒音频、再用3.67M参数因果 Conformer 建模时间演化，1.5秒视距下 AUROC 达0.630，在25%报警占空比条件下可提前覆盖58.6%的事件，证明口吃 onset 之前存在可测量的时间信息。

### 🔧 技术方案

**问题背景：** 已有工作以"检测已发生的不流畅"为主；最近的片段级方法只预测未来3秒片段是否含口吃，既不定位 onset 也不连续估计风险紧迫度；口吃 onset 前的声学时间信息能否被因果模型利用，此前缺乏任务定义、标注与基线。

**模型架构：** 两级解耦：冻结 Whisper-large-v3 编码器每100毫秒独立编码以 t 结尾的2秒波形（零填充至30秒输入，避免双向注意力泄露未来），50Hz 帧五帧平均为1280维末层状态；其上接4块因果 Conformer，状态投影到192维，含 macaron FFN（192→768→192）、4头因果自注意力（最多左看200步约20秒）、核长15的因果深度卷积与 LayerNorm、无位置编码，可训练参数3.67M，总感受野约22秒；对比静态 Whisper 池化、1.12M 参数因果 TCN 与 GRU。

**核心创新：** (1) 严格因果的100毫秒连续预报任务：目标为y=1[0<T_t≤Δ]，剔除事件内部帧防止退化为检测，正样本输入永不含目标事件，并统计正负帧紧邻既往 onset 的占比以控制"事件近期性"混淆。(2) Onset 对齐标注层：以 CrisperWhisper 对齐词级时间戳后全量人工复听补标，合并0.5秒内相邻不流畅，得到2593重复、129延长、150阻塞共2872事件，双标 Fleiss κ 为0.54/0.73/0.56，onset 偏差中位数80毫秒。(3) 离散时间生存多头：单次前向输出15个100毫秒分箱条件风险，累积概率按1−∏(1−h)组合，单模型即得300毫秒至1.5秒单调一致的风险轨迹，而独立累积分类器在68.9%帧上违反单调序。

**训练策略：** 用 focal loss（γ=2、α=0.75）对抗4.93%正例率；AdamW，lr 2e-4，weight decay 0.01，dropout 0.2，梯度裁剪5，按验证 AP 早停（patience 8）；训练序列40秒（200步因果缓冲不计算损失+200步计分）；6个说话人不相交折、每折3个种子平均；生存头改用普通 BCE（dropout 0.3）保持概率校准；特征缓存后时间模型单卡分钟级训练。

### 📊 实验结果
**数据集**：FluencyBank Timestamped（36说话人，录音6.41小时、转写参与者语音5.13小时；扩充后2872事件、164694个可评帧，Δ=300毫秒时正例率4.93%）

**主要指标**：
- AUROC（Δ=300毫秒）：因果 Conformer 0.6300，AP 0.0769（为患病率基线的1.56倍）
- 关键对比：AUROC 比最佳时序基线因果 TCN（0.5889）提升0.0411（95% CI [0.0196, 0.0615]）；静态 Whisper 仅0.5682，且把静态窗从2.0秒扩到3.8秒反而降至0.5666
- 按事件类型 AUROC：重复0.630、延长0.655、阻塞0.612；说话人内 wAUROC 0.5727（重复类0.576，97%说话人超过0.5）
- 因果历史长度：5秒历史 AUROC 0.621，10/20秒不再增益
- 操作指标：25% duty cycle 覆盖58.6%事件；最大 F1 阈值提前预测43.9%事件、平均提前196毫秒，但每分钟产生27.6次虚警

**是否开源**：暂无（论文未给出代码/Demo 链接；标注建立在公开 FBT 许可之上）

### ⭐ 评分：6/10
评分理由：首次把口吃预期建模为连续因果时间到事件预报，任务构造严谨（因果性、负类组成、删失处理），并给出占空比约束下的事件级评估协议与 onset 对齐标注资源，对预期式干预研究有框架价值。但绝对性能尚弱（AUROC 0.63，延长/阻塞在说话人内水平落入随机区间），操作点虚警率高，数据规模仅36人且未开源，属奠基性但离可用尚远的增量探索。

---

## SEA-HELM Audio: Evaluating Multilingual ASR-LLM Pipeline Performance Across SEA-HELM Subsets

**arXiv ID**：arXiv:2610.19869 | **方向**：语音大模型

**作者**：Yixian Tan, Aulia Adila, Jonathan Heng, Kunat Pipatanakul, Donghang Wu, Anocha Sutaveephamochanon

**机构**：AI Singapore

**发布日期**：2026-10-15 | **论文**：https://arxiv.org/abs/2610.19869 | **PDF**：https://arxiv.org/pdf/2610.19869.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
纯文本基准无法预测语音智能体的真实可靠性：语音输入会引入转写错误、音位歧义与领域性退化，而 VoiceBench 等现有语音评测几乎只覆盖英语，对东南亚语言信息有限。本文提出 SEA-HELM Audio，将 SEA-HELM 文本基准扩展为语音评测框架：用 TTS 把原生提示合成为语音，经 ASR 转写后由 LLM 作答，与同模型同验证器的纯文本通路对照。关键结果：五语言（中、英、马来、印尼、泰米尔）上多选推理准确率下降 9.00–18.50 个百分点，指令遵循下降 20.00–42.86 个百分点，泰米尔语损失超 40 分，瓶颈被定位为声学转写层而非 LLM 推理。

### 🔧 技术方案

**问题背景：** 语音智能体部署中，用户"说"相对"打字"付出的准确率代价缺乏区域化、可复现的量化手段；现有语音基准依赖人工录音、以英语为主，无法衡量东南亚语言与代码转换场景下的级联误差传导。

**模型架构：** 双通路级联评测框架。语音通路：TTS（Global-MMLU-Lite 用 OmniVoice，IFEval 用 ElevenLabs v3）合成提示语音，ASR（Qwen3-ASR-1.7B 覆盖 en/zh/ms/id；区域适配的 MERaLiON3-ASR-3B 覆盖 ta；商用 API ElevenLabs Scribe Realtime 覆盖全部五语言）转写为文本，LLM 生成回答；文本通路：同一 LLM 直接回答原始提示。被测 LLM 为区域开源模型 SEA-LION-4.5-27B 与商用模型 Gemini 3.5 Flash。两通路共用 SEA-HELM 程序化规则验证器打分，核心指标为 speech gap Δ = Score_text − Score_speech（百分点），另独立报告 ASR 转写的 WER/CER。

**核心创新：** (1) 文本原生基准到语音模态的受控迁移：同一提示、同一 LLM、同一验证器双路各测一次，Δ 可严格归因于 TTS-ASR 前端，相比 VoiceBench 的人工录音设计成本更低且可复现。(2) 可说话提示构造协议：仅合成用户真正会说出口的内容，选择题的选项标签与答案键从不进语音（中文场景将 A–D 及答题标记改写为中文词读法），IFEval 约束仅打分时使用，避免把书面格式伪影污染语音输入。(3) 转写质量与任务损失解耦分析：同时测 WER/CER 与任务准确率，结合任务格式（MCQ 语义可恢复、IFEval 词法/长度/格式约束被 ASR 丢词即判负）定位退化机制，区分声学瓶颈与语义瓶颈。

**训练策略：** 论文为纯评测框架，不涉及任何模型训练，全部组件即插即用。开源 ASR 均用 greedy 解码保证转写可复写，商用 ASR 用供应商默认解码；两个 LLM 均 temperature=0 确定性生成，确保两通路差异只来自输入而非采样；每次运行 Global-MMLU-Lite 400 样本、IFEval 105 样本；IFEval 验证器逐条检查显式约束并校验回答语言，MCQ 抽取选项字母做精确匹配。

### 📊 实验结果
**数据集**：SEA-HELM Global-MMLU-Lite（中/英四选一常识推理，400 样本每运行）与 SEA-HELM IFEval（英/马来/印尼/泰米尔指令遵循，105 样本每运行）。

**主要指标**：
- MCQ 中文：语音 71.50% 对 文本 80.50%，Δ=9.00 个百分点（Qwen3-ASR+SEA-LION）；商用栈语音 79.75% 对 90.50%，Δ=10.75 个百分点
- MCQ 英文：Δ=18.50 与 15.50 个百分点，显著大于中文
- IFEval 泰米尔：最差 Δ=40.00 个百分点（MERaLiON3 栈 47.62% 对 87.62%；商用栈 41.90% 对 81.90%）
- IFEval 马来/印尼开源栈：Δ=32.38/33.33 个百分点，商用栈收窄至 20.00/31.43 个百分点
- 关键对比：印尼 IFEval 上 SEA-LION-4.5-27B 文本 94.29% 反超 Gemini 3.5 Flash 的 89.52%，但端到端语音仅 60.95%，证明区域开源栈瓶颈在 ASR 层而非 LLM

**是否开源**：论文未提供代码仓库或 Demo 链接，暂无；所用模型均为公开权重或商用 API。

### ⭐ 评分：6/10
评分理由：将区域文本基准系统性改造为模态对照评测并定义可复现的 speech gap 指标，填补了东南亚语音智能体评测空白，"投资本地化 ASR 微调优于继续扩 LLM"的结论对落地有直接指导价值。局限在于仅激活两个子集、样本量 105–400 偏小且全为合成语音输入，与真实口音场景存在偏差，正文与表格存在数值不一致痕迹，方法层面属基准工程增量而非建模创新。

---

## 📄 更多语音论文（紧凑列表）

> 以下 8 篇为当日语音相关论文，未进入精读队列，仅列出基础信息（标题 / arXiv ID / 方向 / 评分 / 链接），按预估评分从高到低排列。

**Quantizer Redundancy and Exact Index Recoding in a Frozen Neural Audio Codec**
- **arXiv ID**：arXiv:2610.20471 | **方向**：语音前端 | **评分**：7/10 | **链接**：https://arxiv.org/abs/2610.20471（未精读，按摘要评分）

**SNOAR: Self-training with Noise filtering, Observation adding, and Remixing for Speech Denoising Without Clean References**
- **arXiv ID**：arXiv:2610.20863 | **方向**：语音前端 | **评分**：7/10 | **链接**：https://arxiv.org/abs/2610.20863（未精读，按摘要评分）

**Rethinking Batch Composition: Promoting Feature Diversity for Speech Enhancement**
- **arXiv ID**：arXiv:2610.21803 | **方向**：语音前端 | **评分**：7/10 | **链接**：https://arxiv.org/abs/2610.21803（未精读，按摘要评分）

**Frame-Wise Streaming for Efficient Learned Speech Compression**
- **arXiv ID**：arXiv:2610.21998 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.21998（未精读，按摘要评分）

**Bridging the Gap: Converting Read Text to Conversational Dialogue**
- **arXiv ID**：arXiv:2605.18001 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2605.18001（未精读，按摘要评分）

**An Initial Study of Physiological Markers for Deepfake Speech Detection**
- **arXiv ID**：arXiv:2610.18934 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.18934（未精读，按摘要评分）

**Soloist: A Generative Model for Blind Voice Separation in the Wild**
- **arXiv ID**：arXiv:2610.19716 | **方向**：语音前端 | **评分**：6/10 | **链接**：https://arxiv.org/abs/2610.19716（未精读，按摘要评分）

**Few-Shot Adaptation for Anomalous Sound Detection at Low False-Positive Rate**
- **arXiv ID**：arXiv:2610.19893 | **方向**：语音前端 | **评分**：5/10 | **链接**：https://arxiv.org/abs/2610.19893（未精读，按摘要评分）

*Subagents used for reading: 15* | Generated on 2026-10-15 语音论文批次, by Kimmy's research agent | Powered by VAgent SpeechAI Researcher
