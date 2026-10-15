# 2026-10-14 语音论文速递

**共收录**: 46 篇 | **语音大模型**: 25 篇 | **语音前端**: 21 篇

> 目标日期 2026-10-14（北京时间）arXiv 语音相关论文共命中 46 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] D2: High-Capability Full-Duplex Spoken Language Models from Half-Duplex Backbones

**arXiv ID**：2610.17124 | **方向**：语音大模型

**作者**：Cheng-Kuang Chang, Alexander H. Liu, Brian Kingsbury, Hilde Kuehne, Rogerio Feris, Samuel Thomas, James Glass, Kai-Wei Chang

**机构**：MIT CSAIL、MIT-IBM Watson AI Lab

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.17124 | **PDF**：https://arxiv.org/pdf/2610.17124.pdf | **代码**：暂无 | **Demo**：https://d2-duplex-demo.github.io/

### 📌 简介
全双工语音大模型（FD-SLM）能边听边说，但综合能力普遍弱于半双工模型（HD-SLM）；已有转换工作受限于秒级音频块与高更新率下生成不稳。本文提出 Dialogue-to-Duplex（D2），通过"无解码器"流式编码器蒸馏 + 全双工 SFT 两阶段，把 Qwen3-Omni（30B-A3B MoE）与 LLaMA-Omni 2（7B）转为 80–100ms 细粒度块交互的 FD-SLM。Qwen3-Omni-D2 在 12.5Hz 下轮次接管率 99.2%（延迟 521ms）、打断接管率 99.5%，VoiceBench 达 70.1，超最强全双工基线 MiniCPM-o 4.5 约 9.1 分。

### 🔧 技术方案

**问题背景：** FD-SLM（Moshi、MiniCPM-o 4.5）交互自然但知识/推理/指令跟随落后于 HD-SLM；BayLing-Duplex 等转换方案依赖 4s 输入块与 800ms 大块，延迟达秒级，且缩小块长会显著退化，编码器非流式是核心瓶颈。

**模型架构：** D2 将对话统一为固定时长 τ（τ=N·Δ，Δ 为编码器帧率）的交互单元序列，HD 视为极端粗粒度特例。Stage I 把原离线音频编码器改造成流式 student：卷积前端仅用已到达音频重算，Transformer 内部改为块因果注意力（chunk 内双向、chunk 间因果），由冻结原编码器逐帧监督；Qwen3-Omni 用 AuT 编码器 12.5Hz（80ms），LLaMA-Omni 2 用 Whisper-large-v3 拼接 5 帧到 10Hz（100ms）。推理时每块将新用户音频与上一块自生成语音 prefill 进上下文，Thinker-Talker 自回归输出文本+16 码本语音帧，Code2Wav 增量合成。

**核心创新：** (1) HD→FD 细粒度转换范式：以"时间粒度"统一半/全双工建模，使强大 HD 底座直接获得 80ms 级交互能力，缓解高更新率下的性能塌方。(2) 无解码器流式蒸馏：student 与 teacher 间用 log-sigmoid 余弦相似度损失对齐表示，不需原训练解码器或转写标签，闭源底座亦可转换；消融显示去掉 Stage I 使 VoiceBench 34.7→30.9、打断后质量 3.33→2.75。(3) 控制信号重加权 SFT：从轮次对话构造 ≥720s 共享时间轴双流序列（50% 打断/30% 直连/20% 静默过渡，Kokoro TTS 统一音色），RESPONSE/INTERRUPT 权重 20、PAD 权重 0.05，可同时防止漏发声与错误抢话（去掉双权重轮次 TOR 跌至 62.2%）。

**训练策略：** Stage I：LibriSpeech clean-100+360（约338h）+AVQA（66.4h），30,000 步、batch 4，卷积前端常数 LR 5e-5、注意力层全参微调 2e-6、其余 LoRA 1e-4。Stage II：InstructS2S-200K（约380h）+SODA（200h）+AVQA（100h），10,000 步、batch 4，Transformer-XL 式 90s 段+分离 90s KV cache，AdamW（梯度裁剪 1.0、warmup 200 步、wd 0/0.01），BF16 训练，仅 LoRA/前端/控制嵌入等模块可训，Thinker 路由专家冻结 INT8 存储。

### 📊 实验结果
**数据集**：Full-Duplex-Bench（轮次/打断/停顿）、VoiceBench 九个子集（AlpacaEval、MMSU、OBQA、BBH、IFEval 等，每子集前 200 样本）；训练数据约 400h/680h 规模

**主要指标**：
- 轮次接管率/延迟：99.2% / 521ms；打断接管率/延迟：99.5% / 403ms（Qwen3-Omni-D2, 80ms chunk）
- VoiceBench 总分：70.1（1040ms 时 73.0，HD 底座 86.8）
- 关键对比：超最强 FD 基线 MiniCPM-o 4.5（61.0）9.1 分；打断响应质量 GPT-4o 评分 4.56 vs MiniCPM-o 4.45
- 实时性：单张 RTX PRO 6000，80ms 块平均计算 56.9ms（p95 57.2ms），RTF 0.711，全块长 RTF<1
- 停顿处理：80ms 时仅 21.3%，1040ms 升至 61.6%（响应性与容错权衡）

**是否开源**：仅 Demo 页面，代码与权重未开源

### ⭐ 评分：8/10
评分理由：把"全双工=更细粒度的普通对话"这一视角落地为无需解码器的两阶段可复现配方，工程价值高；80ms 块下同时拿到近满分 TOR 与 FD 模型 SOTA 的 VoiceBench，且系统给出块长-能力-算力三维消融与真实 RTF 测量，实验充分。局限在于能力仍显著低于 HD 底座（86.8→70.1）、停顿处理弱、训练数据源于轮次对话合成，且未开源代码，稍损影响力。

---

## [2] RUBATO: Decoupled Clocks Allow Full-Duplex Models to Think as Fast as They Can

**arXiv ID**：2610.14299 | **方向**：语音大模型

**作者**：Yi-Jen Shih, Puyuan Peng, Haohe Liu, David Harwath, Abdelrahman Mohamed

**机构**：UT Austin；FAIR, Meta Superintelligence Labs

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.14299 | **PDF**：https://arxiv.org/pdf/2610.14299.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
全双工语音模型的内部思考流本质上异步，而现有方法强制单一固定解码速率以适配特定硬件，导致推理无法随算力加速、跨GPU部署即失效。本文提出Rubato多流RoPE位置编码，为实时音频流与思考流分配独立时钟，使双流时间轴结构解耦，模型仅用两个极端思考预算（B=1与B=∞）训练即可零样本插值任意中间解码速度。在Spoken GSM8K上基线在插值速率下崩溃至1.7%，Rubato-Full稳持48.7%–51.1%精度，TTA随硬件加速缩短6.5倍且TTFR恒定；在全双工打断场景中达40.0%–45.1%而基线完全失败。

### 🔧 技术方案

**问题背景：** 流式全双工模型需在同一序列中编排严格实时的音频流与触发不规则的思考流；先验方法用单一共享位置计数器加固定帧率同步，推理预算偏离训练值时，中间思考token数量任意扭曲相邻实时token的位置距离，产生严重位置分布偏移。

**模型架构：** 基于Gemma-4 E4B-IT文本骨干（约4B参数），采用SCoT四流交织布局（ua/sa/ut/st）外加思考流tt，逐帧拼成扁平序列；音频用NanoCodec以12.5Hz（80ms帧）量化为4条码本×4032条目；每帧思考容量定义为动态预算B_f。核心是双时钟位置编码：实时时钟仅在ua/sa/ut/st上前进（保证p₀(ua_f)=4(f−1)恒定），思考时钟仅在tt上前进，每token携带二维位置向量；给出Rubato-Split（按子空间分割旋转）、Rubato-Gated（仅按key token时钟旋转其子空间）、Rubato-Full（按key时钟旋转全维度、保留原始RoPE频率基）三种注意力构造；训练时通过扩张隐维折叠时钟依赖以复用FlashAttention，推理时维护多套KV缓存并用log-sum-exp合并部分softmax，解码速度与单时钟持平。

**核心创新：** (1)解耦时钟多流位置编码：两条独立推进的时间轴彻底消除思考预算对音频时序的干扰，可零样本插值任意推理速度，且兼容现有融合注意力核无需自定义Triton。(2)按key时钟门控旋转：分析同钟/异钟query-key两种情形后归纳出"统一用key的时钟旋转"规则，Gated去除跨钟噪声，Full进一步避免频率分辨率稀释、与预置骨干RoPE基对齐。(3)双极端预算训练范式：仅在B=1（配语音频filler对齐思考时长）与B=∞（单帧内瞬时完成全trace）两种易生成布局上训练，中间速率全部为零样本内插，大幅简化语料构造。

**训练策略：** 各流加权交叉熵之和，λ_sa=1.0、λ_st=λ_tt=0.5、λ_ut=0.3，padding与<empty-think>降权至0.1；AdamW（β=0.9/0.95，权重衰减0.1），峰值LR 2×10⁻⁴（文本前端2×10⁻⁵），warmup 2000步后余弦退火至10%，梯度裁剪1.0，bf16+FSDP于2节点×8张H200。数据为Qwen3 TTS合成：Spoken GSM8K 365,691通（2474h）、Spoken BBH 54,330通（667h）、Overlapped GSM8K 161,198通（2184h）；思考trace取自Gemma自身输出并经校验，ASR(Parakeet)质检。

### 📊 实验结果
**数据集**：Spoken GSM8K test、BIG-Bench Audio；自建Overlapped Spoken GSM8K（80ms帧，打断同步听说想场景）

**主要指标**：
- Spoken GSM8K精度（全预算扫描）：Rubato-Full 48.7%–51.1% vs 单时钟基线插值下崩塌至1.7%
- 最大精度回落（端点→插值点）：Single-Clock 45.0 / Split 10.6 / Gated 1.1 / Full 0.6 pt
- Overlapped场景Q2精度：Rubato-Full 40.0%–45.1% vs 基线与Split仅1%–14%
- 时延：B=1→32中位TTA缩短6.5×，TTFR恒定；Full在BBA上高出Gated 6.3–12.2 pt
- 音频质量：Gated/Full的UTMOS与说话人相似度随预算稳定，Split显著退化

**是否开源**：暂无（给出完整可复现配方但未发布代码/数据）

### ⭐ 评分：8/10
评分理由：精准命中全双工+思考流部署的核心痛点，双时钟RoPE设计简洁优雅且数学上等价可验证，"双极端训练+零样本插值"显著降低语料构造成本，创新性突出。实验覆盖五个推理任务与重叠打断场景，鲁棒性、时延、音质、混合比消融充分，Decode无速度罚。不足在于全部使用合成音频、仅验证单思考流，未开源代码影响采纳速度。

---

## [3] What Matters in Preference Post-Training of Continuous Autoregressive Speech Language Models

**arXiv ID**：2610.16276 | **方向**：语音大模型

**作者**：Yingda Shen, Yao Qian, Dekun Chen, Yufei Liu, Junan Zhang, Chong Jing, Han Wang, Yuxiang Wang, Zhizheng Wu

**机构**：The Chinese University of Hong Kong, Shenzhen；Microsoft Research

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.16276 | **PDF**：https://arxiv.org/pdf/2610.16276.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对连续自回归语音大模型（AR backbone + flow/diffusion head）偏好后训练中"如何构对、选哪个flow time、更新哪个模块"的三联决策，本文在统一flow-matching偏好目标下控制变量研究候选扰动构造、时间采样与可训练模块。受控重放与单patch干预表明：采样噪声改动会经自回归反馈传导至后续backbone状态，而表征变化幅度并不必然反映音质。在Ming与dots.tts上冻结head仅更新backbone最后16层效果最强：held-out集reward +0.737、WER 0.143→0.060、说话人相似度0.466→0.508；CV3-Eval英语zero-shot WER由30.56%降至5.74%。

### 🔧 技术方案

**问题背景：** DiTAR/dots.tts/Ming等连续AR SLM用flow-matching head生成声学patch且patch回喂AR历史，局部采样变化会级联影响后续生成；但DPO依赖序列对数似然难以应用于flow head，且目标本身不告诉你该比较哪些候选、更新backbone还是head，既有工作（ARDM-DPO等）亦缺乏对这三者交互的受控研究。

**模型架构：** backbone F_φ由文本/历史c与既往patch得隐状态h_k，head v_θ以h_k为条件生成patch；VAE将波形编码为K×d维latent序列z，flow time t下插值x_t,k=(1−t)ε_k+t·z_k拟合目标速度u_k=z_k−ε_k。在Ming(UniAudio，SDE)与dots.tts(ODE-only)两个预训练连续AR模型上做后训练，仅LoRA(rank 8)参数可训。

**核心创新：** (1)闭环rollout、冻结轨迹重放、单patch重采样三干预：改一个patch的噪声后TTS的backbone分歧扩大、语音去噪(DNS)先升后降；冻结重放下latent距离0.95反而使DNSMOS OVRL降0.282，闭环rollout虽latent距离1.22却+0.013，证明偏好必须在完整语音上评估。(2)从生成变异性直接构对：NP扰动SDE采样注入噪声，CP共享初始噪声扰动ODE/CFG/NFE配置；诊断池显示最高频胜者仅在19.4%prompt上最优、oracle可多得0.16–0.36标准奖励，20160组比较按margin 0.1/0.2/0.5留存12867/8366/2978组。(3)flow能量替代DPO似然：E取pair内速度场MSE均值，reference为同模型禁用LoRA并用相同h_k^ref重算，L=−log σ(βM)，M为win/lose的ΔE之差；pair共享同一t与噪声seed，系统化flow-time模块消融发现最优t≠训练最优损失对应t。

**训练策略：** 奖励组合Whisper-large-v3 WER、WavLM说话人相似、emotion2vec相似、DNSMOS、时长与合法性；训练prompt按LibriTTS-R朗读语料与EARS情感语料1:1混合，每prompt取6个合法候选的最高/最低者成对且reward margin≥0.1（模块消融用687对NP偏好对）。β=200、LoRA rank 8、恒定学习率5e-5、有效batch 128；主实验t从[0.3,0.6]离散调度步均匀采样、训练teacher forcing、评测自回归生成整句；对比组含chosen-only SFT与按原文配置更新的ARDM-DPO基线。

### 📊 实验结果
**数据集**：LibriTTS-R + EARS（1:1混合作训练prompt源）；评测为100条held-out英语prompt及CV3-Eval英语650条（500 zero-shot+150 emotion）

**主要指标**（held-out，Ming）：
- Δreward：AR-16 +0.737（95%CI[0.361,1.169]），Joint 16+8 +0.701，head-only仅+0.076
- WER：0.143→0.060；SIM：0.466→0.508；DNSMOS：2.82→2.88
- time消融：固定t=0.3训练损失最低但reward+0.131（CI跨零），t=0.45得+0.137（CI全正），U(0,1)为−0.069
- CV3-Eval：Ming zero-shot WER 30.56%→5.74%(AR-16 NP)、emotion 12.36%→4.94%；dots.tts AR-16 CP WER 5.22%→4.47%
- 关键对比：ARDM-DPO在Ming WER 31.33%劣于base，本文AR-16 NP较其降25.6个百分点；chosen-only SFT在dots.tts反升至8.38%

**是否开源**：无代码/demo发布，仅依赖公开语料与Ming、dots.tts开源权重

### ⭐ 评分：7/10
评分理由：问题聚焦的后训练实证消融研究，"受控重放干预+奖励池诊断+flow能量surrogate"三板斧扎实，且给出两个反直觉结论——最低训练损失不选最优flow time、冻结head更新backbone反而最有效。覆盖Ming与dots.tts两模型、带95%CI、WER提升幅度大，CV3-Eval官方口径可核。不足在于有效训练对仅687组、未做听感偏好验证、未披露数据与算力绝对规模、无代码，复现性与说服力受限，属实质贡献但非突破之作。

---

## [4] PhonoVoxtLM: Exploring Single-Codebook Phonological Tokens for Speech Understanding and Generation

**arXiv ID**：2610.18469 | **方向**：语音大模型

**作者**：Mingrui Liang, Kentaro Onda, Shinji Watanabe

**机构**：Johns Hopkins University、University of Tokyo、Carnegie Mellon University

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.18469 | **PDF**：https://arxiv.org/pdf/2610.18469.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对统一语音语言模型中输入/输出共享表示往往偏向理解或生成一侧的问题，作者提出 PhonoVoxtLM：在 VoxtLM 框架内，将经 ASR+重合成双目标、可微 k-means 训练的音系 token（冻结 WavLM-large 第21层、2000 单元单码本）同时作为语音输入与生成目标，不添加任何 token 预测模块。四任务全面优于 HuBERT 基线（ASR WER 7.1/17.8→4.2/8.6，TTS CER 2.51→1.61），扩展口语问答后 Part II 准确率升至 46.76%。

### 🔧 技术方案

**问题背景：** 语音与文本需在共享自回归框架中建模，同一离散表示要同时满足理解与生成的信息需求：声学 codec 利于合成、语义单元利于识别；DualSpeechLM、SpiRit-LM 等靠附加声学预测分支或多码本 token 流折中，结构复杂，故单码本能否兼顾两能力成为核心疑问。

**模型架构：** 沿用 VoxtLM 统一 decoder-only 框架：冻结 Phonological Tokenizer（微调 WavLM-large 编码器、第 21 层特征、可微 k-means 2000 聚类）离散化语音；码本索引按 Unicode 0x4E00+dᵢ 一对一映射为汉字编码，与文本共同训练 10K SentencePiece unigram 联合子词表；单一 OPT-350M 初始化的自回归 Transformer 以 ⟨sS⟩/⟨sT⟩/⟨gS⟩/⟨gT⟩ 控制前缀统一建模 TextLM/SpeechLM/ASR/TTS/SQA；语音输出经逆映射送 LJSpeech 上训练的单元条件 HiFi-GAN 声码器还原波形，无额外 token 转换分支。

**核心创新：** (1)首次系统评测音系 token 作共享输入-输出表示：与同 2K 码本的 HuBERT-2K 相比在识别、语音判别、合成上全面占优，证明增益源于 tokenizer 训练目标而非码本规模。(2)揭示理解-生成 trade-off：与同层 WavLM-large k-means 单元对比，音系 token 识别稍弱（WER 4.2/8.6 vs 3.7/6.5）但合成显著更强（UTMOS 3.98 vs 3.62–3.70，F0 相关 0.282 vs 0.144–0.159），论证共享表示须双能力评估。(3)零新组件扩展到口语问答：同一序列接口+回放混合微调，Part II 由 35.73%→46.76%，且原任务相对优势保留。

**训练策略：** teacher forcing + label-smoothed CE（smooth 0.1）；Adam，峰值 LR 3e-4、warmup 2500 步、weight decay 1e-6、20 累积 batch、梯度裁剪 1.0、混合精度，按 dev 目标 token 准确率选点。D_Bal 混合：LibriLight 300K 语音+LibriSpeech-LM 300K 纯文本+LibriSpeech 960h 281K ASR 配对+LibriTTS/VCTK 399K TTS 配对；D_3M 将两路非配对各增至 3M。SQA 微调 LR 降至 1e-4、warmup 300、patience 4 epoch 早停；数据为 LibriSQA I+II 约 204K+65K 回放（ASR/TextLM/TTS/SpeechLM 各 25/25/10/5K）共约 269K，token 级近均衡。

### 📊 实验结果
**数据集**：LibriLight、LibriSpeech（960h）、LibriTTS、VCTK、LJSpeech、LibriSQA Part I/II；评测含 sWUGGY/sBLIMP 与 VERSA 自动指标

**主要指标**：
- ASR WER（D_Bal）：4.2/8.6（clean/other），对比 HuBERT-1K 7.1/17.8、HuBERT-2K 7.4/17.5
- 语音判别 sWUGGY/sBLIMP：66.98/57.31，超 HuBERT-1K 的 61.43/54.35
- TTS：CER 1.61、UTMOS 3.98、SpeechBERTScore 0.821、F0 相关 0.282，四项全胜 HuBERT
- SQA 微调后：BLEU-4 30.75 / ROUGE-L F1 49.01 / BERTScore F1 55.64 / 选择题 acc 46.76%（HuBERT-1K 适配版 29.50/49.00/55.40/45.10）
- 关键对比：350M 模型超 1.3B VoxtLM-k200（sWUGGY 69.1 vs 66.1，WER 4.3/8.3 vs 4.6/12.1，无 MLS）；数据扩展至 3M 后优势保持但非均衡（CER 1.61→2.26）

**是否开源**：无专门代码/Demo 仓库链接；流程基于 ESPnet 与已发布 VoxtLM、Phonological Tokenizer 实现

### ⭐ 评分：7/10
评分理由：方法本身为增量式（既有框架+既有 tokenizer 的表示替换），但实验设计严谨：码本尺寸匹配对照、同层 WavLM 消融、数据规模曲线与 SQA 保留评估俱全，清晰量化了单码本表示的理解-生成权衡，工程可复现价值高；局限在仅英语朗读语料、单一 350M 骨干、合成全靠自动指标无听测，故介于增量与实质贡献之间偏上。

---

## [5] Training a Compact, Strong, and Realistic Text-to-Speech Model（Audio8-TTS）

**arXiv ID**：2610.14776 | **方向**：语音大模型

**作者**：Runyuan Cai, Yu Lin, Yiming Wang, Xiaodong Zeng

**机构**：AutoArk（Edge0）

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.14776 | **PDF**：https://arxiv.org/pdf/2610.14776.pdf | **代码**：https://github.com/Edge0-AI/Audio8_TTS | **Demo**：暂无

### 📌 简介
现有TTS以WER与说话人相似度(SIM)为优化目标，均无法刻画韵律自然度，导致"低WER高SIM仍像合成音"的真实感鸿沟。本文提出0.6B双自回归零声音克隆模型Audio8-TTS，并构造三阶段训练：多语SFT→WER/SIM奖励GRPO→以"参考锚定真实感评估器"为奖励的GRPO。评估器由6个开源TTS的盲听Elo质量阶梯加Praat停顿压缩退化链训练，并引入身份擦除与时长约束。最终CV3九语错误率4.86%、SIM 0.661，Seed-TTS错误率1.25%，盲听Elo显著高于前两阶段。

### 🔧 技术方案

**问题背景：** WER只管词是否被识别、SIM只约束说话人身份，节奏/停顿/演绎风格游离于优化目标之外；纯堆数据与大模型、或用WER/SIM做RL都无法直接优化感知自然度，且RL易被"长时长保停顿"捷径带偏。

**模型架构：** 冻结音频tokenizer将波形编为21.5 Hz×10本码本（每本4096）的token矩阵，冻结codec解码器还波。解码端为fast-slow双自回归：slow分支以Qwen2.5 0.5B为骨干（hidden 896、24层，GQA 14Q/2KV），在帧率上预测文本与第1码本；浅层fast分支4层并行预测其余9码本。AR部分合计601M参数；推理仅帧级串行。CPU端ONNX权重INT4，M2上内存峰值1.1–1.2 GiB，模型文件572 MiB。

**核心创新：** (1) 参考锚定真实感评估器：候选句与同一句同声音的人类参考配对打分，盲听Elo质量阶梯（人类居顶）+ Praat PSOLA停顿逐级压缩构造组内有序监督，损失=L_rank(跨系统BCE排序)+λm·L_mono(相邻退化级margin铰链)+λe·L_era(全扁平端点跨系统分数对齐的身份擦除)+L_nuis(惩罚时长/能量可预测分)；WavLM-large第8层25Hz池化+显式基频/能量/清音轨迹，仅训约3M打分头，输出s=−30·tanh(d/30)。(2) 双轴融合的GRPO：真实感阶段先组内标准化fidelity(0.7·ASR+0.3·SIM)与critic分数（方差下限0.005/0.3）再合成为单一奖励，避免低方差轴被过度放大。(3) 时间尺度漂移约束：对时长比ρ>1.35施加单侧对数惩罚并组内中心化，λ经对偶上升使超阈比例稳定在15%，防止策略偏好"停顿多=时长长"的捷径。

**训练策略：** SFT数据为清洗后Emilia+YODAS2+私有补充语料，按ASR比对/语言/时长/错误率过滤，中英各约30%、其余语言≤3%；先训slow、冻结slow训fast、再联合微调，交叉熵损失。GRPO的WER/SIM阶段提示约2/3来自CV3九语；真实感阶段提示中英约各半。WER用Whisper-large-v3（中文用ARK-ASR-3B），奖励为clip(1−WER/2.0)与clip(SIM/0.85)；评估器验证集5600组句-音、89600条合成语音，留出系统Fish S2/Spark-TTS仍保持正确层级。优化器/学习率/batch论文未披露。

### 📊 实验结果
**数据集**：Seed-TTS test、CV3九语+22语、MiniMax 24语测试集；训练为Emilia/YODAS2+私有大规模多语数据

**主要指标**：
- CV3九语错误率：5.41%(SFT)→5.01%(WER/SIM)→4.86%(真实感)；SIM 0.639→0.643→0.661
- 13个低资源语：错误率22.36→20.77，SIM 0.638→0.679（真实感阶段全部语言提升）
- Seed-TTS en/zh：错误率1.25%，SIM 0.704；MiniMax 24语 5.89% / 0.754
- 关键对比：0.6B参数优于CosyVoice3-1.5B(SEED 1.67/0.750)，错误率接近Qwen3-TTS-1.7B(1.01)但SIM略低于IndexTTS-2.5(0.852)；盲听Elo显著高于SFT与WER/SIM阶段模型
- 时长越阈率<5%语句超参考50%

**是否开源**：代码、模型权重与部署（ONNX INT4）已开源

### ⭐ 评分：7/10
评分理由：首次把"感知真实感"做成可训练的参考对照式奖励，身份擦除与停顿退化链设计针对reward hacking，方法论创新扎实；三+二语基准对比全面且盲听验证有效，0.6B达到强基线附近极具部署价值。不足是SIM绝对值不及IndexTTS-2.5、未披露关键训练超参、真实感奖励仅覆盖停顿时间轴（对音高能量监督不均衡），故未达8分档。

---

## [6] VoTSpeech: Decoupling Voice Design from Speech Generation in Instruction-Following TTS

**arXiv ID**：2610.14694 | **方向**：语音大模型

**作者**：Wenbing Yang, Qihang Lu, Zihan Sun, Peilei Jia, Yingming Gao, Ya Li, Jun Gao

**机构**：北京邮电大学、Hello Group（中国）

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.14694 | **PDF**：https://arxiv.org/pdf/2610.14694.pdf | **代码**：https://github.com/ywbn/VoTSpeech | **Demo**：同代码仓库（含音频样例）

### 📌 简介
指令式TTS常把语音描述当作文本上下文喂进模型，"造什么样的声音"与"说什么"耦合，缺乏显式目标音色表示。论文提出VoTSpeech，沿用dots.tts共享Causal LLM主干，引入Voice DiT（流匹配）先"想"出连续语音latent，再经双路条件注入LLM与Acoustic DiT；目标latent由CAM++说话人嵌入与时间池化音频VAE特征拼合。1543.52小时中文数据上，它在InstructTTSEval-ZH的DSD达78.5%、RP达66.9%、CER 2.58%，主观AMOS 4.26，超越Qwen3-TTS-1.7B-VD等开源对手。

### 🔧 技术方案

**问题背景：** 现有指令TTS把语音指令直接拼进文本，语音设计隐式混在话语生成里，无法显式控制"先定音色、再发声"；参考音频式说话人表示虽可靠，却不适用于纯文本驱动场景，且既有文本驱动latent多偏静态身份，缺少动态声学层次。

**模型架构：** "think-before-speak"两段式。序列组织为 [c, ⟨v⟩, e_v, x, ℓ_1:T]：c为语音指令，⟨v⟩为生成标记，其隐状态 h_c 经流匹配Voice DiT（4层Transformer，hidden 512，8头）采样连续语音latent z。z反标准化后拆出说话人/声学分量，构建双路条件：前缀 e_v=P_z(z)+P_h(h_c) 供LLM做韵律规划，g_v=G_s+G_a+G_h 供Acoustic DiT做声学渲染，语音latent再经音频VAE解码为波形。目标 z*=norm([E_spk(y); pool(E_vae(y))])，融合身份与全局声学。

**核心创新：** (1)显式语音设计-生成分离，用中间连续latent替代"指令即上下文"，推理走预填两段并复用指令KV cache，Voice DiT仅作轻量预计算（训练2步、推理16步积分）。(2)混合目标与双路条件接口：speaker嵌入+池化VAE特征共同监督z*，无需额外解耦损失；零初始化残差 P_h/G_h 注入指令上下文，说话人slice与声学slice权重分别为1.0/0.25。(3)一致性可控标注管线：Qwen3-Omni对每条采两版描述，DeepSeek-V4做属性级矛盾检查，区分说话人固有特质与话语动态风格两级注解；以stop-gradient阻断语音损失污染LLM表示，并用渐进调度采样（0→0.75）缓解train/infer暴露偏差。

**训练策略：** 总损失 L=L_speech+L_voice，后者为标准流匹配速度场回归。8×A100、20k步（约17个epoch，1543.52h中文数据）；主干LLM lr=1e-5，语音设计模块 lr=1e-4；编码器E_spk/E_vae冻结。源数据含PromptDialog、Genshin及ISCSLP2026-CoT-TTS改写标签。

### 📊 实验结果
**数据集**：InstructTTSEval-ZH（APS/DSD/RP三类指令遵循）；训练中文库1543.52h；CER用Paraformer-ZH；主观由24人评10条/系统

**主要指标**：
- DSD：78.5%（Qwen3-TTS-1.7B-VD 76.0，dots.tts-soar FT 75.0，+3.5pp）
- RP：66.9%（次优dots.tts-soar 64.3，+2.6pp）
- APS：84.8%（Qwen3-TTS 87.1为最高）
- CER：2.58%（与最优VoxCPM2持平）
- NMOS/EMOS/AMOS：4.12/4.30/4.26，均第一（AMOS比FT +0.30）
- 消融：去LLM侧条件 RP 降3.0pp；去VAE目标DSD、RP分别降0.8、3.3pp

**是否开源**：代码、模型与音频样例均开源（GitHub）

### ⭐ 评分：7/10
评分理由："显式语音latent+双路条件+混合目标"解耦设计思路清晰、实证充分，消融直接指向每处设计动因，主观与客观指标齐备且超越多个强开源基线，实用价值明确。局限在于DSD/RP优势幅度中等、APS不及Qwen3-TTS，主干参数量未披露，且latent仍是句级全局描述（作者自承），缺少帧时序与显式解耦，故为扎实的实质贡献而非突破性工作。

---

## [7] Beyond Fixed Targets: On-Policy One-Shot Speaker Personalization for Autoregressive Text-To-Speech Models

**arXiv ID**：2610.17838 | **方向**：语音大模型

**作者**：Sangkwon Park, Che Hyun Lee, Heeseung Kim, Sungroh Yoon

**机构**：首尔国立大学 ECE / IPAI、AIIS、ASRI、INMC、ISRC；首尔市立大学

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.17838 | **PDF**：https://arxiv.org/pdf/2610.17838.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
AR-TTS 用单条参考语音做 one-shot 个性化时，SFT 反复拟合固定目标会导致推理时紧跟参考序列输出 EOS、生成空白语音，WER 飙升。本文定位"固定离策略监督"为根因，提出两种在线策略方法：GRPO 直接以解码语音与参考语音的说话人嵌入余弦相似度为奖励做组相对优化；OPSD 让无参考上下文的学生在自己采样的轨迹上向"带参考特权上下文"的冻结教师做 token 级 KL 软蒸馏，含 Reference-Only 与 Text-Augmented 两个变体。在 LLaSA-1B、Seed-TTS-Eval 英文集上，GRPO 达 SIM 0.647、WER 3.0%，优于零样本基线（0.574/3.7%）；OPSD 无奖励模型即达 SIM 0.609，且适配速度约为 GRPO 的 8 倍。

### 🔧 技术方案

**问题背景：** 单参考对 SFT 对 AR TTS 严重失效（全参 SFT WER 18.2%、LoRA 反而 35.0%），根因是 teacher-forcing 下反复最大化 r→EOS 似然；已有数据多样化手段能否解决、on-policy 是否才是关键，此前不明。

**模型架构：** 底座为 LLaSA-1B（Llama 架构自回归 TTS，输出 XCodec2 codec token，经 codec 解码器合成波形）。个性化设定：仅有目标说话人一对 (c,r)；零样本克隆以 ⟨c⊕x,r⟩ 前缀条件生成。评估侧用 ECAPA-TDNN 提取说话人嵌入算 SIM，whisper-large-v3 算 WER。

**核心创新：** (1) 诊断并提出 Zero-Shot Distilled SFT 对照：用零样本模型生成多样伪配对做固定目标训练，消除了空白输出但 SIM 仅微升、WER 翻倍，证明"目标多样性"不足以解释失效，需 on-policy 监督。(2) 将 GRPO 引入 one-shot 说话人个性化：每条文本采 G=8 条 rollout，奖励为解码语音与参考语音的 ECAPA 余弦相似度，组内标准化优势加 PPO-clip 与对预训练模型的 KL 项，无需目标说话人额外语音。(3) 提出 OPSD 两变体：Reference-Only 用 ⟨c⊕c,r⟩ 作教师上下文、Text-Augmented 用零样本克隆配置 ⟨c⊕xₐ,r⟩ 作教师，教师在 top-K=64 logits 上给学生轨迹提供软监督，并支持 rollout 批次复用 k=10 次更新省算力。

**训练策略：** 每个说话人独立适配。SFT/LoRA 与 OPSD-RO 批次 B=1；ZSD 与 OPSD-TA/GRPO 的 B=4；OPSD-RO 采样 G=10 rollout，OPSD-TA 4 条文本×G=10=40 rollout，GRPO 4 文本×G=8=32 rollout；rollout 采样温度 0.9、top-p 0.95、top-k 50、上限 500 token；推理温度 0.8、top-p 1.0、上限 2048 token；无配对文本池取自 LibriTTS 英文句子。论文未报告学习率、优化器与总步数。

### 📊 实验结果
**数据集**：Seed-TTS-Eval 英文子集（每人单条参考+转写）；文本池为 LibriTTS 英文句

**主要指标**：
- SIM：GRPO 0.647 / OPSD-TA 0.609 / OPSD-RO 0.608（零样本 0.574）
- WER：GRPO 3.0% / OPSD-TA 3.7%（零样本 3.7%，SFT 18.2%）
- NMOS（93 人 120 评）：GRPO 3.87±0.15、OPSD-TA 3.80±0.15 vs SFT 3.42±0.21，逼近真值 4.38
- 关键对比：GRPO 较 SFT SIM +0.111、WER 降 15.2 个百分点；OPSD 单步耗时约为 GRPO 的 1/8（5.8× vs 45.2× SFT）

**是否开源**：暂无代码/Demo 链接（底座 LLaSA 为开源模型）

### ⭐ 评分：7/10
评分理由：问题诊断清晰且有机制解释（EOS 坍缩），ZSD 对照巧妙地把"数据多样性"与"on-policy"解耦，消融与 rollout 复用分析扎实。GRPO/OPSD 双双在 SIM 与 WER 上同超零样本基线，结论可信。局限是仅一个 1B 底座、单一英文评测集、说话人范围窄，GRPO 依赖外部声纹奖励与高算力（45× 步时），学习率等复现细节缺失，故为实质贡献但非突破之作。

---

## [8] Collapse, Repair, and Drift: Dissecting Fine Tuning Dynamics in Speech Language Models

**arXiv ID**：2610.18192 | **方向**：语音大模型

**作者**：Yichi Wang, Wangjin Zhou, Yizhou Zhang, Xin Gu, Wei Tan, Yi Zhao, Gong Zhi

**机构**：京都大学情报学研究科、腾讯WXG、中国传媒大学

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.18192 | **PDF**：https://arxiv.org/pdf/2610.18192.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
语音大模型SFT通常仅以loss曲线监控，掩盖了识别功能的瞬态劣化。作者将Qwen3-ASR-1.7B、MiMo-Audio-7B、FireRedASR2-LLM在387小时五方言语料上于1e-5至1e-3学习率微调，把SFT动力学拆解为可分离的坍缩、修复、漂移三过程：坍缩期CER飙至200%而loss变化平缓。经双向层patching与梯度谱定位功能不相容，并用AdamW更新迁移干预证明绕开早期坍缩后普通话退化仍会发生。

### 🔧 技术方案

**问题背景：** loss只度量被优化目标，不反映推理功能在同一轨迹上的演化；已有遗忘研究多比终点、缺过程机制。作者在方言适配中观察到loss平稳但CER剧烈先崩后复的现象，故提出loss之外的动力学细粒度解剖。

**模型架构：** 三个独立speech LLM（声学编码器+音频-语言投影器+文本decoder），仅全量微调decoder、冻结声学部分；LLM层数28（Qwen3-ASR/FireRed）与36（MiMo），规模1.7B/7B。诊断框架三件套：双向层patching（预训练1:n层与SFT n+1:L层拼合，扫深度得CER兼容曲线）；五方言梯度余弦相似与原始梯度矩阵奇异谱（D_eff=1/Σp_k²∈[1,5]）；AdamW师生更新迁移干预。

**核心创新：** (1)首次提出collapse/repair/drift三分动力学，实证loss严重低估功能变化：1e-4下step3的CER达177.78–200%（重复退化输出），而1e-3失败run最终eval loss超收敛run两倍以上。(2)双向层patching揭示可恢复坍缩伴随结构化的跨checkpoint功能不相容：破坏深度依模型而异，1e-3时失配弥散全网、无单层区可挽回；pairwise梯度余弦在高维空间仅近零无诊断力，谱分布更可靠——收敛run的D_eff早期升至近5并长期稳定，失败run谱集中或持续波动。(3)更新迁移只混合完整AdamW位移：学生前10步冻结但复制教师优化器状态，s=10–70按(a,b)系数混合后回归常规SFT，成功绕过早期坍缩峰，但Mandarin CER仍随后漂移，证明瞬态坍缩不是持续性遗忘的必要原因。

**训练策略：** teacher-forcing交叉熵只监督转写token（排除前缀/控制符）；AdamW恒定学习率无warmup、梯度范数裁剪1.0；训练250k句/387.18h、验证25k/38.62h、方言测试5k/7.66h；有效batch 640（每device每方言1微批×8卡×16累积）；1 epoch=391次优化更新；干预实验seed 5230。

### 📊 实验结果
**数据集**：自建五方言库（长沙/客家/闽南/南昌/宁波，训练387h/25万句）；源域普通话用SpeechIO-3（1683句/2.39h）

**主要指标**：
- 瞬态坍缩CER峰值：177.78%–200%（Qwen3-ASR, 1e-4, step3）
- 持续失败（1e-3）：最终eval loss>收敛run 2倍，CER长期未回基线
- 梯度谱D_eff：收敛run稳定于近5；失败run接近1或剧烈波动
- 更新迁移学生：早期双域CER峰被消除，后期普通话漂移同教师
- warmup(0.02)消融：最终CER与无warmup相当，未改善普通话保留

**是否开源**：暂无（私有语料且未发布代码/checkpoint）

### ⭐ 评分：7/10
评分理由：非模型类工作，但把speech LLM微调动力学解剖做得系统完整，collapse/repair/drift分离对语音大模型适配实践（如方言上线调LR）有直接指导价值；跨3模型×3学习率交叉验证充分，层patching与更新迁移两类机制干预说服力强。局限是结论偏依赖轨迹可视化与示例数值、终态CER绝对值披露不足，数据与代码不开源难复现，且验证warmup无效后未给出更好的缓解方案。

---

## [9] SemiCodec: Bridging Speech Tokenization and High-fidelity Reconstruction with Semi-discrete Representations

**arXiv ID**：2610.14834 | **方向**：语音大模型

**作者**：Kecan Mao, Nan Xu, Zhaoyang Meng, Zhengyao Ma, Yingming Gao, Yi Zhao, Ya Li

**机构**：北京邮电大学人工智能学院；腾讯微信

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.14834 | **PDF**：https://arxiv.org/pdf/2610.14834.pdf | **代码**：暂无 | **Demo**：https://pennyw1-se.github.io/SemiCodec-Demo-Page/

### 📌 简介
语音表征需同时支持离散建模接口与高保真波形重建，但离散token丢失细粒度声学信息、连续latent又依赖专用生成目标。本文提出SemiCodec半离散神经语音codec，同步输出SSL引导的离散token与64维连续latent并相加融合重建；针对联合训练中连续通路"重建捷径"问题，设计Preserve-then-Ground两阶段训练范式。在LibriSpeech test-other上PESQ-WB达4.03、WER 5.02%、MUSHRA 86.95，显著超越全离散基线并与连续表征持平。

### 🔧 技术方案

**问题背景：** 语音兼具离散语言内容与连续声学信息，DAC/Mimi/SAC等离散codec便于next-token预测但低帧率下丢失声学细节；Semantic-VAE、dots.tts等连续表征保真度高却需回归/流匹配/扩散等特殊目标。直接联合优化双通路时，信息量大的连续路径会抢走重建梯度，导致离散token欠训练、码本利用不足。

**模型架构：** 共享编码器为因果步幅卷积+Qwen2式因果Transformer骨干（沿用TS3-Codec），输出25帧/秒特征h；连续分支经变分瓶颈采样64维latent z_a；离散分支逐帧VQ量化，码本4096项、8维嵌入，STE回传梯度；两支路投影到共享合成空间相加，经转置卷积上采样+Qwen2式Transformer+iSTFT头（Vocos式）直接重建波形，全程低帧率统一接口。

**核心创新：** (1)半离散表征：离散token（每帧1/4096符号）与64维连续latent在同一25Hz帧率下逐帧同步，离散流提供紧凑建模接口，连续流承载说话人/韵律等难量化信息，相加融合使解码器输入维度固定。(2)Preserve-then-Ground两阶段训练：Stage I仅训练连续通路建立高保真合成空间；Stage II冻结编码器与连续分支作声学锚点，引入离散分支联合wav+SSL蒸馏（w2v-BERT 2.0第17层cosine对齐）+VQ损失优化，避免连续捷径。(3)Acoustic Dropout：Stage II按Bernoulli(1−p)随机丢弃连续支路，强制解码器依赖已落地的离散token。

**训练策略：** 波形损失=多尺度mel L1+LSGAN对抗（MPD+MRD判别器）+特征匹配L1，Stage I加KL正则，Stage II加SSL与commitment/codebook损失。数据约79.5万小时（Emilia+LibriTTS 9.5万、内部70万），统一重采样24kHz、随机裁剪9.6秒。AdamW（β=0.8/0.9），warmup-hold-cosine调度；Stage I主模块/判别器LR为2e-4/1e-4，Stage II离散分支/解码器/判别器为2e-4/2e-5/4e-5。BF16精度，32张NVIDIA H20训练。

### 📊 实验结果
**数据集**：LibriSpeech test-other（24kHz）客观评测 + 20人MUSHRA主观听测（8条utterance）

**主要指标**：
- PESQ-NB/WB：4.15 / 4.03（GT为4.55/4.64）
- STOI / ViSQOL / SIM / WER：0.975 / 3.77 / 0.96 / 5.02%
- MUSHRA：86.95±1.35
- 关键对比：25FPS下超越最强离散基线SAC（62.5FPS，PESQ-WB 2.39、WER 5.71%、MUSHRA 74.39）；对比同帧率dots.tts VAE（48k）PESQ更高（4.03 vs 3.95），仅ViSQOL/SIM略逊；消融Joint→Stage I→II→+AD：PESQ-WB 3.58→3.99→4.02→4.03，码本使用率82.71%→97.31%

**是否开源**：提供Demo音频页，模型代码暂未开源

### ⭐ 评分：7/10
评分理由：针对离散/连续codec各自的根本短板给出半离散统一方案，Preserve-then-Ground与Acoustic Dropout直接命中联合训练的梯度捷径问题，码本使用率从82.7%升至97.3%是有力证据。79.5万小时数据与32卡H20的规模化训练、客观+主观双评测较充分。不足：仅在重建任务验证，未实测下游TTS/SLM离散接口收益；24kHz域评测与44.1/48k基线的公平性略有争议；代码未开源限制复现。

---

## [10] LLM-HB: Language-Aware LLM-Guided Hotword Biasing for Code-Switching ASR

**arXiv ID**：2610.16579 | **方向**：语音大模型

**作者**：Yuxuan He, Genshun Li, Pengcheng Huang, Gongping Gao, Jianqing Qian, Yanmin Qian

**机构**：上海交通大学听觉认知与计算声学实验室、科大讯飞AI研究院、武汉大学电子信息学院

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.16579 | **PDF**：https://arxiv.org/pdf/2610.16579.pdf | **代码**：https://anonymous.4open.science/r/IS26-ASRU2019-Hotword-List/（仅热词表，模型未开源） | **Demo**：暂无

### 📌 简介
针对中英混合码语（CS）语音中频繁语言切换导致的识别与专有名词偏置难题，本文提出首个将LLM引导热词偏置引入CS-ASR的框架LLM-HB：在Whisper编码器后接MoE适配器实现语言专业化表征，附加语言预测头提供显式监督，热词经LLM分词编码后以prompt注入。在ASRU2019测试集（15干扰热词）上，相对基线MER降低20.30%达5.85%，CER 4.94%、WER 13.21%，B-MER从22.11%降至8.99%。

### 🔧 技术方案

**问题背景：** 现有CS-ASR方法聚焦缓解跨语言干扰（双编码器、MoE、语言后验注入），而上下文偏置技术主要针对单语系统，二者鲜有融合；已有跨语偏置工作亦未利用LLM的自适应多语偏置能力。

**模型架构：** 输入梅尔频谱经预训练Whisper-medium编码器（1024维，联合微调）提取声学特征，通过稠密MoE适配器（2专家、top-2门控，FFN聚合+LayerNorm）投影至2560维对齐Qwen3-4B输入空间（LLM主干仅LoRA适配）；热词表（含<no-bias>标记）经冻结LLM分词器与文本编码器得到热词嵌入，与语音嵌入、目标文本嵌入构成序列送入LLM解码；LLM隐状态另接辅助语言头（FFN投影3类：中/英/其他，仅训练时使用）。

**核心创新：** (1) MoE适配器置于编码器与LLM之间，路由器top-K门控聚合专家FFN输出，实现语言专业化声学表征，且双语场景下2专家即饱和。(2) 辅助语言预测头在LLM输出隐状态上加CE语言监督，虽不显式监督路由，但经共享表征反传间接驱动门控按语言一致性分配token，巩固专家分工。(3) 热词以LLM原生分词嵌入直接prompt进解码上下文，配合偏置损失对热词位置token最大化后验，实现中英双语自适应偏置。

**训练策略：** 总损失 L=L_ASR+λ1·L_Bias+λ2·L_Lan，λ1=0.6、λ2=0.3，ASR与语言损失均为CE。数据为AISHELL-2(1000h)+LibriSpeech(960h)+ASRU2019-CS(200h)共约2200小时；每batch中每条语音以50%概率被选做偏置，随机采样1–4个token构成热词表。AdamW优化器，三角学习率调度，单周期47040步、共2周期94080步，峰值学习率1.5×10⁻⁴，8颗寒武纪MLU590 GPU。

### 📊 实验结果
**数据集**：ASRU2019中英码语评测集（200h训练+测试，热词表含每句15干扰项；训练含AISHELL-2 1000h、LibriSpeech 960h）

**主要指标**：
- MER：5.85%（基线7.34%，相对降20.30%）
- CER / WER：4.94% / 13.21%（相对基线降1.98% / 49.29%）
- B-MER / B-CER / B-WER：8.99% / 3.01% / 10.93%（基线22.11% / 19.26% / 22.90%）
- 消融：仅200h CS训练时完整模型MER 7.36%；MoE配置2选2最优（7.19%）优于4选2（7.47%）；λ1=0.6时CER/WER权衡最均衡

**是否开源**：仅释放ASRU2019抽取热词表（匿名仓库），模型代码暂无

### ⭐ 评分：6/10
评分理由：首次将LLM引导热词偏置引入CS-ASR，问题切口新颖，B-MER 22.11%→8.99%的偏置收益显著且消融充分（专家数、λ1曲线）。但架构为Whisper+Qwen3+MoE适配器的工程组合，单模块创新有限，且因训练数据规模差异未与已有SOTA直接对比，仅内部基线比较削弱说服力。热词表匿名开源有实用价值但无模型代码，整体属扎实的增量工作。

---

## 语音前端

## [1] What Do Deepfake Audio Detectors Hear? From Self-Supervised Models to Audio LLMs

**arXiv ID**：2610.17617 | **方向**：语音前端

**作者**：Wanying Ge, Xin Wang, Junichi Yamagishi

**机构**：日本国立信息学研究所 National Institute of Informatics

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.17617 | **PDF**：https://arxiv.org/pdf/2610.17617.pdf | **代码**：https://github.com/nii-yamagishilab/AntiDeepfake-AudioLLM | **Demo**：暂无

### 📌 简介
真实录音是语音与环境声的混合，现有深伪检测器究竟听到哪一路、证据落在哪个频段并不清楚。本文在语音与事件各自可真可假的 CompSpoof V2 混合库上，对比 XLS-R、Whisper 编码器接分类头的主流方案与 Qwen2-Audio 音频大模型两种读出方式，用逐组件打分与逐子带静音探针回答两个研究问题。结果显示所有系统对假事件的 EER（8.29%–13.38%）远低于假语音（21.21%–23.74%），但经来源分解，该差距主要来自对未见 SoulX-Podcast 域的泛化失败而非固有难度；子带探针证明证据分布由前端编码器决定。

### 🔧 技术方案

**问题背景：** 深伪检测器假定只监听语音，但真实场景混有背景事件；非语音成分多被视为干扰，而合成事件本身也带伪影。现有方法不清楚检测器跟随哪个组件、伪影集中在频谱何处。

**模型架构：** 四类反制措施共用 16 kHz 波形前端。标准 CM 用预训练编码器（XLS-R 语音自监督、Whisper 编码器）输出帧级隐状态，时间均值池化后接线性分类头。ALLM-based CM 以 Qwen2-Audio-7B-Instruct 为骨干，Whisper 音频经线性投影对齐 LLM 嵌入维度，注入固定 forensic 提示词；分 Generative（LM Head 取 real/fake 两 token 的 logits 做 softmax）与 Discriminative（替换为二分类头）两种读出。

**核心创新：** (1) 首次让语音与事件两个组件在训练/评估中被独立解耦打分，量化检测器对各组件敏感度。(2) 按假语音来源分解 EER，用 SoulX/MLAAD/ASVspoof5 三个源拆解性能差距，揭示假事件优势主要源于未见域泛化失败而非难度差异。(3) 基于 8 阶零相位 Butterworth 的六子带带阻探针（仅推理不改参），论证前端编码器而非分类骨干决定证据频率位置，并对比生成式与判别式 ALLM 的 token 语义差异。

**训练策略：** 交叉熵损失，AdamW 优化器，类别均衡采样；峰值学习率 4×10⁻⁵，200 warm-up 步，batch size 8，每 200 步验证，上限 30000 步（约 5 个 epoch），按最低验证损失选 checkpoint。ALLM 用 LoRA rank=16、α=32 同时适配编码器与骨干。单张 H100 GPU，三随机种子平均。训练集各标签文件数为 25189/50361/21759/29413。

### 📊 实验结果
**数据集**：CompSpoof V2（ESDD2 挑战赛库，语音-事件混合，16 kHz）

**主要指标**：
- 假事件 EER：Whisper 最低 8.29%（XLS-R 9.50/ALLM disc 13.38/gen 12.91）
- 假语音 EER：XLS-R 最低 21.21%，ALLM disc 最高 23.74%
- SoulX 来源假语音 EER：达 36.70%–49.52%（vs 已见 MLAAD 仅 4.21%）
- 子带抑制证据：屏蔽 7.2–8 kHz 使 Whisper 假事件 EER 从 8.29% 骤升至 27.23%；屏蔽 0–0.8 kHz 使 XLS-R 假语音 EER 从 21.21% 升至 32.53%
- 双假条件反而更易检测（如 XLS-R 假语音 36.70% → 双假 16.34%）

**是否开源**：源代码与权重已发布于 NII 山岸实验室 GitHub

### ⭐ 评分：8/10
评分理由：选题精准切中深伪检测落地痛点，用可控架构对比与子带探针形成清晰归因链条，泛化失败与前端主导两大发现对社区有实质启示；实验在三随机种子下 EER std 控制在 1–3 个点，可信度高。局限在于仅覆盖一个混合库、CM 结构简化，且 ALLM 骨干仅 7B 一种，泛化结论稍显单薄。

---

## [2] LiveAnon: Improving Privacy and Utility in Streaming Speaker Anonymization with Codec Language Models

**arXiv ID**：2610.15379 | **方向**：语音前端

**作者**：Yejin Kim, Kyungsu Kim, Seungu Han, Kyogu Lee

**机构**：首尔国立大学音乐与音频研究组 MARG / 信息与智能系

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.15379 | **PDF**：https://arxiv.org/pdf/2610.15379.pdf | **代码**：暂无 | **Demo**：https://jin1025.github.io/LiveAnon/

### 📌 简介
流式说话人匿名化需在有限延迟内隐藏说话人身份，同时保留语言内容与情感；现有流式系统依赖离散内容瓶颈，常丢失情感且需情感专用监督。本文提出 LiveAnon，一个基于语音转换的流式匿名化系统：将冻结的流式 Zipformer ASR 编码器隐层特征直接作为自回归 codec 语言模型的内容条件，并以 VALL-E 式参考 codec prompt 续写指定目标音色，无需分离说话人编码器。同时提出封顶 RVQ 解码（capped delay）压缩码本生成延迟。在 VPC24 协议下全面优于固定目标的 Stream-Voice-Anon（WER 4.31 vs 4.54，情感 UAR 44.09 vs 39.71，semi-informed EER 32.28 vs 15.92），算法延迟 500 ms、RTF 0.17。

### 🔧 技术方案

**问题背景：** 语音中身份与情感/内容联合编码，匿名化存在隐私—效用权衡；离散量化瓶颈虽抑制speaker信息，但同时丢弃情感线索，流式场景又受限于未来上下文与延迟，现有方法需额外的韵律或情感蒸馏组件。

**模型架构：** 三模块级联：①冻结流式 Zipformer ASR 编码器（16 帧/320 ms chunk）取末级下采样前 512 维 50-Hz 特征，线性投影至 256 维，前移 6 帧对齐后经 FiLM 仿射调制注入每层 Transformer；②JHCodec 流式神经音频 codec（16 kHz、50 fps、8 个 RVQ 码本、码本大小 1024），将 3 秒目标参考语音转为 codec token 作声学 prompt；③12 层因果 Transformer 解码器（hidden 768、8 头、FFN 3072、ALiBi），对 prompt+生成 token 做单一自回归流续写，输出经 codec 解码器还原波形。

**核心创新：** (1) 直接以流式 ASR 隐层特征作内容条件，线性探针显示其情感 UAR 55.17、说话人分类准确率仅 28.75（SVA 为 39.95/32.50），天然"少身份、多情感"，免情感专用监督。(2) 参考 codec 序列与生成序列共享码本嵌入构成单一自回归流（VALL-E 式 prompt 续写），推理时 prompt 预填 KV-cache 一次处理，不计入逐帧延迟。(3) Capped RVQ pattern：d_k=min(k,δmax)，把 MusicGen 延迟模式截断为 δmax=3（码本延迟仅 60 ms），保留粗码本间依赖、其余码本并行预测。

**训练策略：** 损失为全序列 codec token 交叉熵（教师强制）；数据为 LibriTTS train-clean-100+360（约 460 h，16 kHz），取 ≥6 s 语句切成 3 s 参考+3 s 目标两段；AdamW，峰值学习率 1e-4，余弦退火，400k 步，单卡 RTX 3080 Ti。

### 📊 实验结果
**数据集**：训练 LibriTTS（~460h/16kHz）；评测 WER/EER 用 LibriSpeech，情感 UAR 用 IEMOCAP，固定 VCTK 单目标说话人，VPC24/26 协议

**主要指标**：
- WER：4.31%（原始 1.83）
- 情感 UAR：44.09%（原始 70.07）
- EER-S / EER-L：32.28% / 48.75%
- 关键对比：优于 SVA vctk-1fix（WER 4.54、UAR 39.71、EER-S 15.92），EER-S 提升 +16.36；UAR 接近情感 prompting 的 SVA（44.59）；VPC26 中四项指标均第二强；算法延迟 500 ms、RTF 0.17（RTX 4090），δmax=1/3/7 消融确认 3 最优

**是否开源**：暂无代码仓库，官方 Demo 页面已上线

### ⭐ 评分：7/10
评分理由：首次将 codec LM 的条件从离散瓶颈换成冻结流式 ASR 隐层，以探针分析佐证其情感保留与身份弱化的机理，创新性扎实且免情感标注；capped RVQ 是简洁可推广的延迟-质量权衡手段。实验覆盖 VPC24/26 双协议、四基线、延迟与消融，隐私—效用平衡优势明确。不足是仅单一固定 target prompt、情感 UAR 距原始仍有大 gap，且未开源代码，实用复现受限。

---

## [3] FlowGRPO for Vocal Separation: From Reward Analysis to Reward Design

**arXiv ID**：2610.15780 | **方向**：语音前端

**作者**：Lishi Zuo, Chong-Xin Gan, Zezhong Jin, Youzhi Tu, Man-Wai Mak, KongAik Lee

**机构**：香港理工大学电气与电子工程系

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.15780 | **PDF**：https://arxiv.org/pdf/2610.15780.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
Flow Matching分离模型在中间隐状态监督速度场，而SI-SDR、ViSQOL等波形/感知指标在VAE解码后计算且不可微，导致后训练对齐困难。本文将FlowGRPO（GRPO作用于Flow Matching轨迹、以端点波形奖励优化）引入人声分离，并提出"先分析、后设计"范式：在策略优化前统计组内最优-均值奖励差距与数据质量因子的回归关联，据此改造ViSQOL为通道RMS对齐+首末活跃帧区间的ViSQOL_act，并叠加样本质量过滤。最终FlowGRPO使预训练分离器的ViSQOL从3.525升至3.675、SI-SDR从5.927升至7.045、SDR从6.946升至8.293，分离与感知质量全面提升。

### 🔧 技术方案

**问题背景：** 人声分离的正向生成流程以隐空间流匹配为目标，与最终波形的客观质量指标脱节；多数语音指标不可微或依赖预训练模型管线，无法直接作为生成梯度信号。已有FlowGRPO虽可用端点奖励做RL后训练，但奖励选择与错配（reward hacking）直接影响优化效果，此前缺乏训练前的奖励诊断手段。

**模型架构：** 在冻结的预训练音频VAE（ϵar-VAE）隐空间做条件人声分离：混合与目标人声编码为C×L隐表示，从高斯噪声沿线性路径由条件流匹配模型预测速度场，推理时积分至端点再经解码器还原波形。分离生成器为10亿参数连续Transformer（24层、隐维1536、24头），FlowGRPO仅更新它。采样将概率流ODE换成保边缘分布的SDE，N=10步、扩散系数σ_t=a√((1−t)/t)（a=0.7），只在随机起点n₀∈{1,…,5}的K=2步窗口内注噪，窗口前用共享ODE路径复制出G=8条轨迹；策略损失为带clip ε=0.2的GRPO裁剪目标，组内优势按均值/标准差归一。

**核心创新：** (1) 训练前组内奖励分析：对1500条混合以旧策略采G=8轨迹，计算MRSTFT、SI-SDR、ViSQOL三种奖励的"最优-均值差距"，并对RMS、活跃比、边缘静音比、立体声RMS差、通道起始延迟五因子做标准化控制回归，发现ViSQOL差距与边缘静音比（−0.063）、立体声RMS差（−0.107）关联最强，暴露其受数据质量干扰。(2) 奖励改造：提出ViSQOL_act——逐通道先将生成波形缩放到与参考相同的活跃区间RMS，再仅在首个到末个活跃帧之间打分，消除增益与首尾静音捷径；MRSTFT奖励取−log(1+ℓ_MRSTFT)，各分量按batch标准化后等权组合。(3) 样本质量过滤：按固定波形阈值剔除低电平/欠活跃/削波/错位/不平衡目标（RMS≥−25 dBFS、−40 dBFS以上活跃≥3 s、削波比≤0.01等），使GRPO优化更稳定。

**训练策略：** 5万条20秒内部混合训练、50条留测；AdamW，学习率2×10⁻⁶，权重衰减10⁻³，5k优化步、batch=4混合、每步一次内更新，2张80GB A100；VAE解码器冻结，奖励在解码后波形上计算。

### 📊 实验结果
**数据集**：50k条20秒内部音乐混合（无公开集），50条留作测试

**主要指标**（最优 vs 预训练基线）：
- ViSQOL：3.675（预训练3.525，+0.150）
- SI-SDR：7.045（5.927，+1.118 dB）；SDR：8.293（6.946，+1.347 dB）
- PESQ：2.112（2.076，+0.036）
- MRSTFT loss：1.084（1.148；单奖励MRSTFT行最低1.067）
- 关键对比：同过滤条件下ViSQOL_act较原始ViSQOL在SI-SDR上+0.145 dB；加过滤较不加SI-SDR+0.558 dB，全指标一致提升

**是否开源**：暂无代码/Demo发布，训练数据与分离器均为内部资产

### ⭐ 评分：6/10
评分理由：方法论亮点是"优化前用组内奖励差距回归指导奖励重设计"，思路清晰且消融充分（改奖励、加过滤均带来全指标一致增益），验证了预分析可替代昂贵RL实验的价值。但实验局限于50条内部测试集的自比较，缺少与BS-RoFormer等外部SOTA分离器的对比，绝对SI-SDR约7 dB仍距专业分离工具差距明显；数据、模型、代码均不开源且未做主观听测，实际影响力与可复现性受限，属扎实但偏增量的工作。

---

## [4] Spiking Neural Beamforming for Multichannel Speech Enhancement on the Edge

**arXiv ID**：2610.16430 | **方向**：语音前端

**作者**：Hanan Beit-On, Eli Shapira, Boaz Rafaely

**机构**：本古里安大学电气与计算机工程学院（以色列）；Neuromorphic Lab

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.16430 | **PDF**：https://arxiv.org/pdf/2610.16430.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
针对现有脉冲神经网络（SNN）语音增强局限于单通道、无法利用麦克风阵列空间分集，且模型规模偏大的问题，本文提出首个全脉冲驱动的多通道语音增强框架 FC-SNN。该框架由紧凑全连接 ANN 基线转化而来，以 LIF 神经元替换 ReLU，配合序列式脉冲编码与解码，仅用 37K 参数估计复数 TF 掩码。实验显示直接编码在 N=50 时取得 4.03 dB SI-SDR、PESQ 1.629，有效 MAC 率较 FC-ANN 降低约 10 倍，参数量比 Spiking-S4 等先前 SNN 模型小一个数量级，但质量仍落后 FT-JNF 基线。

### 🔧 技术方案

**问题背景：** 戴式与边缘设备需在增强质量与功耗/内存间取舍；DNN 多通道波束形成性能强但算力开销大，而已有可训练 SNN 增强方法只处理单通道或采用混合 ANN 结构与高维脉冲表示，难以享受事件驱动的全层稀疏计算收益。

**模型架构：** 输入为 C=6 路麦克风 STFT 实部虚部堆叠加频率索引与逐 bin 归一化幅值，共 2C+2 维；经 Spike Encoding → Linear(H)→LIF → Linear(H/2)→LIF → Output(2)→LIF → Spike Decoding（N 步平均后取 logit）输出 2 通道复数掩码，乘参考麦克 STFT 得目标语音。隐藏宽度 H=64~512 对应 3.1K~139.5K 参数，工作点取 H=256（37K）。编码分直接编码（输入逐时刻恒定，首层密集计算）与率编码（Bernoulli 采样，全层脉冲驱动）。

**核心创新：** (1) 首次将全脉冲网络用于多通道波束形成式增强，把 SNN 语音增强从单通道扩展到阵列空间信息利用；(2) 采用序列式脉冲编码替代高维脉冲表征，参数量降至 37K，比 Spiking-S4（530K）、Spiking-FullSubNet（965K）、DPSNN（1.4M）小一个数量级；(3) 系统刻画性能随模型规模与脉冲序列长度 N 的缩放规律（直接编码 H=512 不收敛；率编码 N=200 仍不敌直接编码 N=10），据此为边缘部署给出"重质量选直接、重全事件驱动选率编码"的工作点选择策略。

**训练策略：** 损失 L = −SI-SDR；Adam，学习率 1e-3，batch size = 1，训练 250 epoch，取验证损失最低 checkpoint；脉冲层用 snnTorch 的代理梯度训练；STFT 512 点 FFT、32 ms 窗、16 ms 跳；输入按 max magnitude 归一化到 [0,1] 以适配率编码。

### 📊 实验结果
**数据集**：WSJ0（16 kHz）仿真混音，6 麦克风半圆弧阵列（半径 8 cm）、目标 0°方位、5 个干扰说话人，gpuRIR 生成 RIR（T60 0.2–0.5 s），6000 训练/1000 验证/600 测试，每条截 6 s

**主要指标**：
- FC-SNN（direct, H=256, N=50）：SI-SDR 4.03 dB，PESQ 1.629，STOI 0.826，37K 参数，有效 0.058 GMAC/s、3.37 GSynOp/s
- 关键对比：落后 FC-ANN（5.07 dB）1.04 dB、大幅落后 FT-JNF（7.83 dB）3.8 dB；但优于 oracle MVDR（2.06 dB）与未处理（−7.18 dB）
- rate 编码（N=100）：SI-SDR 1.21 dB，全层脉冲驱动，10.18 GSynOp/s
- 规模/长度消融：direct H=64→256 使 SI-SDR 2.79→3.42 dB（H=256 N=50 时4.03 dB）；N=10→50 从 2.89→4.03 dB

**是否开源**：暂无（文中未提供代码与演示链接）

### ⭐ 评分：6/10
评分理由：提出首个面向多通道语音增强的全脉冲框架，参数效率比先前 SNN 方法高出约一个数量级，且直接/率编码、规模与序列长度的缩放分析对边缘部署有实际参考价值；诚实报告有效 MAC 记账而非笼统转换能耗，值得肯定。但增强质量明显低于 FC-ANN 与 FT-JNF 等 ANN 基线，SNN 尚未证明"以更低算力获得可用质量"的完整闭环；实验仅基于 WSJ0 仿真阵列，缺真实录音与硬件实测能耗，泛化性与实用收益有待验证，属有价值的开创性增量工作。

---

## [5] Active noise cancellation extends the benefit of AI speech enhancement in real hearing-aid recordings

**arXiv ID**：2610.17287 | **方向**：语音前端

**作者**：Andrew T. Sabin, Linkai Li

**机构**：Bose Corporation；Orka

**发布日期**：2026-10-14 | **论文**：https://arxiv.org/abs/2610.17287 | **PDF**：https://arxiv.org/pdf/2610.17287.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
助听器中提升信噪比的算法只作用于放大通路，而声经通气孔直达鼓膜的非处理直通路噪声会封顶鼓膜处可实现的 SNR，低频尤其严重。本文在真实 RIC 助听器（Orka O1 标准机 vs Orka O1 Pro ANC 机关/开）上以 KEMAR 录音验证"ANC 衰减直通路可释放 AI 语音增强（AI-SE）收益"的机制：AI-SE 在三种硬件的高频峰值收益同为约 4 dB，但 ≥1 dB 收益下限频率从 1500 Hz（标准机）降至 600 Hz（封闭耦合）再降至 130 Hz（ANC 开）；鼓膜处 SII 加权新增 SNR 在 ANC 开+AI-SE 开达 5.1 dB，为标准机的 3 倍，而单开 ANC 仅 +0.2 dB。

### 🔧 技术方案

**问题背景：** 助听器算法的 SNR 改善仅在放大通路存在，鼓膜总信号是放大通路与直通路（经 vent 或未密封耦合泄漏）之和；处理越强，未处理直通路噪声占比越大，低频受益被封顶。此前仿真研究预测：环境声级越高、设备 SNR 改善超过约 4 dB、ANC 越强，ANC 收益越大，但缺乏真机实验证据。

**模型架构：** 本文非神经网络训练论文，而是硬件对照实验框架：三种硬件条件（标准 RIC：平衡电枢受话器+郁金香耳塞；ANC-capable RIC：动圈受话器+封闭耳塞+壳体 vent，ANC 关/开）× AI-SE 开/关共 6 条件，AI-SE 为 proprietary 算法（结构与参数量未公开）。分析端用 STFT（2048 点 Hann 窗、512 帧移）对齐干净语音参考，按 40 百分位谱地板 +12 dB 阈值生成二值时频掩码，估计语音/噪声谱并计算逐频带 SNR；宽带汇总用 ANSI S3.5-1997 频带重要性函数加权（SII-weighted SNR）。

**核心创新：** (1) 首次用商用 RIC 真机录音验证"ANC 是使能技术而非 SNR 改善技术"：ANC 同等衰减直通路语音与噪声，本身不改变直通路 SNR，只抬高放大通路改善传导到鼓膜的频率上限。(2) 定量揭示收益边界与 REOIG（真实耳阻塞插入增益）严格对应：直通路接近 0 dB 透传处 AI-SE 收益消失；封闭耦合将边界从 1500 Hz 推至 600 Hz，ANC 开（100 Hz 处 −10 dB、200 Hz–1 kHz −20~−28 dB）推至 130 Hz。(3) 给出产品设计结论：ANC 价值随 SNR 增强算法强度线性放大，AI-SE 开通 ANC 净增 1.8 dB，AI-SE 关仅 0.2 dB。

**训练策略：** 无模型训练环节。实验协议：按 Bisgaard N3 听力图以 NAL-NL2（experienced user）验配；KEMAR 置于 8 扬声器环中心，采用 HearAdvisor 实验室协议，ARTE 库中 7 个噪声级 >70 dB SPL 场景（均值 75 dB SPL、名义 SNR 均值 1.2 dB），每场景 1/2/3 说话人×2 版本共 42 条录音/条件，双耳 44.1 kHz 立体声；每助听录音配对的开放耳录音与干净语音用于计算新增 SNR。

### 📊 实验结果
**数据集**：ARTE 环境声数据库 7 个 >70 dB SPL 场景（KEMAR 真机录音，42×6 条件，44.1 kHz 双通道）

**主要指标**：
- 高频 AI-SE 峰值收益：约 4 dB（4–6 kHz，三硬件一致）
- AI-SE 收益 ≥1 dB 频率下限：1500 / 600 / 130 Hz（标准 / ANC 机关 / ANC 机开），对应语音谱重要性 53% / 84% / 100%
- SII 加权新增 SNR（AI-SE 开）：标准机 1.6 dB，ANC 机关 3.3 dB，ANC 机开 5.1 dB
- 开 ANC 净增益：AI-SE 开 +1.8 dB vs AI-SE 关 +0.2 dB
- 逐频带新增 SNR 峰值：标准机 ~5.5 dB（4–5 kHz），ANC 机 ~7.5 dB（1.5 kHz）

**是否开源**：暂无（AI-SE 算法、录音数据均未开源；ARTE 与 HearAdvisor 协议为公开资源）

### ⭐ 评分：6/10
评分理由：实验设计严谨，真机对照与 REOIG 测量闭环清晰，首次将先前仿真预测落到商用硬件，对助听器产品集成 ANC 的决策有直接实用价值。但算法侧无贡献（AI-SE 为闭源黑箱，无法复现），且仅以 SII 加权 SNR 为指标、未做听者行为可懂度实验，单一人工耳、单一 N3 验配目标限制泛化。属于扎实的增量性验证工作而非方法突破。

---

## 其他论文（未进入前 15，仅列标题）

1. **ATTEST: Evidence-Grounded Reinforcement Learning for Long-Audio Temporal Understanding** | 语音大模型 | arXiv: 2610.17149 | 评分：7/10 | https://arxiv.org/abs/2610.17149

2. **AMemOps: Evaluating Memory Updates in Long Audio Streams** | 语音大模型 | arXiv: 2610.18652 | 评分：6/10 | https://arxiv.org/abs/2610.18652

3. **SpectralBridge: Adding High-Frequency Capability to Large Audio-Language Models** | 语音大模型 | arXiv: 2610.17048 | 评分：6/10 | https://arxiv.org/abs/2610.17048

4. **RefTAG: Reflection-aware Temporal Audio Grounding in Large Audio Language Models** | 语音大模型 | arXiv: 2610.16217 | 评分：6/10 | https://arxiv.org/abs/2610.16217

5. **SSEmb: Training a Generalizable Speech Retrieval Model Using Only Automatic Speech Recognition Data** | 语音大模型 | arXiv: 2610.17813 | 评分：6/10 | https://arxiv.org/abs/2610.17813

6. **Prime-EVC: One-Step Expressive Emotional Voice Conversion via Emotion-Primed Flow Matching** | 语音大模型 | arXiv: 2610.16036 | 评分：6/10 | https://arxiv.org/abs/2610.16036

7. **AlignAudio: A Unified Dual-Alignment Framework for Noise-Robust Speech-Conditioned Generation** | 语音大模型 | arXiv: 2610.14697 | 评分：6/10 | https://arxiv.org/abs/2610.14697

8. **Cross-Lingual TTS for Indian Languages: A Benchmark and Inference-Time Duration Estimation Strategies** | 语音大模型 | arXiv: 2610.14826 | 评分：6/10 | https://arxiv.org/abs/2610.14826

9. **Towards Privacy-Preserving ASR: Speaker-Level Machine Unlearning** | 语音大模型 | arXiv: 2610.16196 | 评分：6/10 | https://arxiv.org/abs/2610.16196

10. **SpikCTU: A Compact Spiking Network with Adaptive Recurrent Computation for Speech Command Recognition** | 语音大模型 | arXiv: 2610.14594 | 评分：6/10 | https://arxiv.org/abs/2610.14594

11. **Speech event detector: Timestamped detection of non-verbal vocalizations and background sounds for rich speech transcription** | 语音前端 | arXiv: 2610.14232 | 评分：6/10 | https://arxiv.org/abs/2610.14232

12. **What Makes Codec Tokens Effective for Target Speaker Extraction? A Semantic-Acoustic Disentanglement Perspective** | 语音前端 | arXiv: 2610.16858 | 评分：6/10 | https://arxiv.org/abs/2610.16858

13. **Learning Where to Split: Dynamic Band Splitting for Audio Source Separation** | 语音前端 | arXiv: 2610.14993 | 评分：6/10 | https://arxiv.org/abs/2610.14993

14. **BridgeCodec: Mamba Enhanced Neural Audio Codec with Schrödinger Bridge at Low Bitrate** | 语音前端 | arXiv: 2610.15453 | 评分：6/10 | https://arxiv.org/abs/2610.15453

15. **HE-NAC: High-Efficiency Neural Audio Coding via Hierarchical and Residual Multi-Band Quantization** | 语音前端 | arXiv: 2610.15243 | 评分：6/10 | https://arxiv.org/abs/2610.15243

16. **Co-Adaptive Entropy Modeling and Rate-Distortion-Optimal Bit Allocation for Perceptual Audio Coding** | 语音前端 | arXiv: 2610.17459 | 评分：6/10 | https://arxiv.org/abs/2610.17459

17. **FOAdapter: A Plug-and-Play Spatial Tokenizer for Low-Bitrate FOA Speech Coding** | 语音前端 | arXiv: 2610.16202 | 评分：6/10 | https://arxiv.org/abs/2610.16202

18. **KOMOS: Automatic Mean Opinion Score Estimation for Korean Speech** | 语音前端 | arXiv: 2610.15353 | 评分：6/10 | https://arxiv.org/abs/2610.15353

19. **MixedTruth: Component-Level Detection of Synthetic Speech and Synthetic Background in Mixed Audio** | 语音前端 | arXiv: 2610.14141 | 评分：6/10 | https://arxiv.org/abs/2610.14141

20. **Unsupervised Data Drift Monitoring for Deployed Deepfake Speech Detectors** | 语音前端 | arXiv: 2610.16826 | 评分：6/10 | https://arxiv.org/abs/2610.16826

21. **Adaptive Compression and Targeted Perturbation: A Unified Framework for Generalized Audio Deepfake Detection** | 语音前端 | arXiv: 2610.16049 | 评分：6/10 | https://arxiv.org/abs/2610.16049

22. **Synthesizing Ultrasonic Echo Profiles from Text for Open-Vocabulary Silent Speech Recognition** | 语音前端 | arXiv: 2610.15671 | 评分：6/10 | https://arxiv.org/abs/2610.15671

23. **Self-Supervised Source-Filter Model of Speech Production** | 语音前端 | arXiv: 2610.18120 | 评分：6/10 | https://arxiv.org/abs/2610.18120

24. **CAST-ASD: Causal Attention over Speakers and Time for Online Active Speaker Detection** | 语音前端 | arXiv: 2610.14676 | 评分：6/10 | https://arxiv.org/abs/2610.14676

25. **GeoMER: A Joint Euclidean-Hyperbolic Geometry Framework for Multimodal Emotion Recognition** | 语音大模型 | arXiv: 2610.18587 | 评分：5/10 | https://arxiv.org/abs/2610.18587

26. **Multimodal Contrastive Representation Learning Based Voice Conversion for Electrolaryngeal Speech Enhancement** | 语音大模型 | arXiv: 2610.17716 | 评分：5/10 | https://arxiv.org/abs/2610.17716

27. **Hearing's Blind Spots: Toward Perceptual Compute Allocation in Neural Text-to-Speech** | 语音大模型 | arXiv: 2610.14056 | 评分：5/10 | https://arxiv.org/abs/2610.14056

28. **GAMW: Generation-Aware Mel-Domain Watermarking for TTS Traceability** | 语音大模型 | arXiv: 2610.15082 | 评分：5/10 | https://arxiv.org/abs/2610.15082

29. **The NVVSpeech Challenge 2026: Overview and Lessons for Speech Understanding and Generation with Nonverbal Vocalizations** | 语音大模型 | arXiv: 2610.16076 | 评分：5/10 | https://arxiv.org/abs/2610.16076

30. **Word-Aligned Prosody Reflects Speaker Differences More Than Depression or PTSD Severity** | 语音前端 | arXiv: 2610.15181 | 评分：5/10 | https://arxiv.org/abs/2610.15181

31. **Unsupervised Cross-device Speaker Diarization And Linking Through Spatiotemporal Structure** | 语音前端 | arXiv: 2610.15978 | 评分：5/10 | https://arxiv.org/abs/2610.15978

---

*Generated on 2026-10-14*
