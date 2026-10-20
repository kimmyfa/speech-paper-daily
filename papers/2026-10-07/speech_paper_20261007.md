# 2026-10-07 语音论文速递

**共收录**: 24 篇 | **语音大模型**: 17 篇 | **语音前端**: 7 篇

> 目标日期 2026-10-07（/new 页头 "Showing new listings for Wednesday, 7 October 2026"）arXiv 语音相关论文共命中 24 篇（另剔除音乐/古琴/打击音材质/合成器FX/生物声学等 10 篇）。
> 以下是按评分排序的结果（前 15 篇完整精读，其余仅列标题、arXiv ID、评分与链接）。

---

## [1] 语音大模型

## [1] Conversation Is a Two-Body Problem: Dyadic Evaluation of Full-Duplex Dialogue Models

arXiv ID：2610.08125 | **方向**：语音大模型；**作者**：Sungnyun Kim、Sungwoo Cho、Jihwan Oh、Se-Young Yun；**机构**：韩国科学技术院（KAIST）；**发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.08125
**PDF**：https://arxiv.org/pdf/2610.08125
**代码**：暂未链接，计划发布场景、角色提示与录制/评分协议
**Demo**：无

### 📌 简介
全双工语音对话模型能边听边说，但现有基准普遍按"单边"会话打分：对无法反应的预录音频，或对只按固定题序提问、自身不被评分的自动考官。本文指出对话是两位说话人持续互相塑造的双体问题，单边评测只测了一半。作者提出DyaFDB双边评测框架：让两个全双工模型在同一帧级时钟平台上直接对话，各自持有分配的、常常冲突的角色，环内不设考官，双方录音由外部LLM法官离线共同打分。框架探针覆盖轮流发言、角色维持、信道争夺与目标冲突，并通过多模型配对证明任何单一固定对手都无法既当考官又当考生。

### 🔧 技术方案
**问题背景：** FDB-v1/v2/v3、MTR-DuplexBench、tau-Voice等全双工基准或喂给模型无法反应的预录音频与teacher-forcing上下文，或把对话方绑定到固定测试大纲且只评一边，无法把轮次、重叠、打断这些双方耦合产物的分数归因到模型自身还是诱导它的对手。
**方法：** 架设model-to-model桥：两路音频在80ms@24kHz锁步时钟上互为输入输出；PersonaPlex与Raon-SpeechChat原生逐帧生成，MiniCPM-o经适配器缓冲成约1秒chunk接入。任务分协作与冲突两族：T1角色保持、T2信息共享（隐藏画像设计，双方各持部分证据）、T3信道争夺、T4目标争夺（偏好说服与秘密窃取），8个原型各20场景共140个。PersonaPlex、MiniCPM-o、Raon三模型自博弈与交叉博弈共6种配对，角色与开场序反平权衡、重复3次，录制7560段1分钟对话共126小时。
**核心创新：** (1)首个双方平等打分、伙伴本身是被测全双工模型且作为设计变量的双边框架；(2)方差分解量化轮流行为归因：TOR_pause主要由模型自身决定（η²=0.74），而TOR_end与barge-in由伙伴让位行为决定（η²=0.65），backchannel交互项最大（η²=0.32）；(3)把得分拆成"是否行动"乘"行动后成功率"两级，并用30/60/120秒窗口测量时间预算的影响。
**评测协议：** 完全离线打分，机械指标（信道占有、字符串匹配）与Opus-5法官并用；法官看匿名转写，开场序反平抵消位置偏差；新模型可对照已发布的共享模型矩阵续评。

### 📊 实验结果
**数据集**：自建140场景、7560段真实录制（126小时双声道音频）
- 角色保持均分：Raon 0.68/0.83，MiniCPM-o 0.62/0.59，PersonaPlex 0.51/0.29
- 信息共享解决率：含Raon的队伍23%-35%，不含Raon的均低于20%（随机水平）；单模型仅透露39%的私有理由；文本对照Qwen3-8B披露74%、解决55%
- 秘密攻防：PersonaPlex攻击成功率0.46最高，MiniCPM-o防守最好（失守29%），Raon平均失守48%（泄露中位12.2秒）；同一防守方失守率随攻击者在39%-63%区间波动
- 信道占有：Raon施压方0.69最高，但作为回避方仅0.39、停不下来；MiniCPM-o是最听指令的回避方
- 时间窗口：30→60秒各项上升，超过60秒普遍饱和
**是否开源**：承诺发布场景、角色提示与录制评分协议，不含预录音频；代码库未见链接

### ⭐ 评分：8/10
理由：把游戏与多智能体领域的league/cross-play评测范式首次系统引入全双工语音，3模型6配对的方差分解实证了单边基准分数的伙伴依赖性，方法贡献明确、协议可复现且可扩展新模型；任务设计源自行为科学经典范式，发现（Raon协作强却在回避与防守角色全面失守）有洞察力。扣分在于评分依赖单一LLM法官、被测模型仅3个、信息共享任务天花板过低（解决率不足35%）短期区分力有限。
## [2] Logbook: Extremely Long-form Audio Event Understanding

arXiv ID：2610.07338 | **方向**：语音大模型 | **作者**：Kwanghee Choi、Suwon Shon、Dmitriy Serdyuk、Guitang Lan、Chao-Wei Huang 等 10 人 | **机构**：Meta Reality Labs、UT Austin | **发布日期**：2026-10-07 | **论文**：https://arxiv.org/abs/2610.07338 | **PDF**：https://arxiv.org/pdf/2610.07338 | **代码**：https://github.com/facebookresearch/logbook | **Demo**：无

### 📌 简介
本文提出 Logbook，首个小时级（10 分钟至 6 天）连续音频事件理解基准。任务要求系统对不间断录音输出无缝隙、无重叠的切分，每段附带一个事件标签与自由文本描述。作者将 Ego4D、EgoLife、SINS 三个公开数据集统一为日志式标注格式，评测 52 个系统（48 个级联 + 4 个端到端），并对微调、上下文窗口与推理预算做消融。结论：任务可行但最佳系统仍低于人工基线；过分割普遍存在，端到端模型随上下文变长而退化。

### 🔧 技术方案
**问题背景：** 现有音频基准建立在短且预切分的片段上（AudioSet、Clotho 等），长音频基准上限仅 20-30 分钟且偏重语音；声音事件检测器依赖固定词表，captioning 模型无论输入多长只输出一句话，导致模型设计无法应对全天连续听音场景。

**模型架构：** 非单一模型而是两类系统对比。端到端（E2E）：Qwen2.5-Omni-7B、Qwen3-Omni-30B-A3B、Audio Flamingo 3、Gemini 3.5 Flash 四个音频语言模型直接读 10 分钟音频窗口输出结构化结果。级联：6 个音频 captioner（上述 3 个开源模型改作描述器、Qwen3-Omni-Captioner、EnCLAP 与 MSCLAP，10 秒窗口）配 8 个文本 LLM（OLMo 3.1-32B、K2-V2-70B、Qwen 2.5-72B、Llama 3.3-70B、Qwen 3-32B、Gemma 4-31B、Gemini 3.5、GPT 5.6），caption 聚合为 10 分钟组后输出 JSON（起止分钟、标签、描述）。

**核心创新：** (1) 首次把长音频理解定义为 gap-free 分割任务，词表标签控制切分粒度、描述补足标签缺失信息，强制全覆盖防止弃答刷精度；(2) 构建双层评测：分割用 bF1（150 秒容差）、evER（序列编辑距离，诊断过分割）、fAcc（主指标），描述用原子事实分解 + BART-MNLI 文本蕴含（阈值 0.5）算 dR/dP/dF1，另报 PFLOPs 算力、Hit@1、冗余度，设双通道人工代理基线；(3) 系统消融三种改进杠杆：监督微调、5-45 分钟窗口、1024-4096 token 推理预算。

**训练策略：** 对 Gemma 4 与 Qwen3-Omni 用 LoRA（r=16、alpha=32、dropout=0.05）在 Ego4D 训练集（1350 会话、555.8 小时）微调 1 epoch，AdamW，batch size=8，lr=1e-4，余弦调度、3% 预热，每 200 步按验证损失保存最优；级联侧冻结 AF3 的 caption 输入。

### 📊 实验结果
**数据集**：Ego4D（train 555.8h / val 107.6h / test 82.1h）、EgoLife（test 240.6h）、SINS（单人 148.9h、约 6 天）
**主要指标**（Ego4D，人工基线 fAcc：0.646 / dF1：0.550）
- fAcc：最佳 E2E Gemini 3.5 为 0.445；Qwen3-o + SFT 达 0.633
- dF1：最佳未微调系统 Gemma 4 级联 0.238；Qwen3-o + SFT 提升至 0.422
- evER：GPT 5.6 级联过分割达 286%（Ego4D）/343%（EgoLife），SFT 后全部降到 100% 以下
- SINS：级联优于 E2E，Casc. Gemini 3.5 fAcc 0.571；算力上 E2E Qwen3-o 处理首 24 小时仅 11.97 PFLOPs，级联 AF3+Gemma 4 达 71.41
- 窗口消融：级联系统在 45 分钟仍稳定，E2E 在 5-10 分钟见顶后退化；推理仅 E2E Gemini 单调受益（解析失败率 15.4% 降至近零）
**是否开源**：基准数据、预处理管线、提示词均开源（CC BY-NC-SA 4.0 非商用）

### ⭐ 评分：7/10
理由：填补了天级连续音频事件理解的评测空白，52 系统对比覆盖面广，"过分割普遍、E2E 长上下文退化、推理只改善指令遵循"三条结论对可穿戴音频与个性化助手方向有直接指导价值。扣分在于：标签由 LLM 推断且人工标注员看过视频，人类基线是有偏代理而非天花板；未提出新模型或算法，任务粒度受 6 类词表限制；AF3 作为最佳 captioner 却在 E2E 下完全失败，暴露格式敏感性评测噪声；SFT 在域外数据集增益有限，方法学突破不足。
## [3] HiPLEX: Hierarchical Policy Factorization for Full Duplex Speech Language Models

arXiv ID：2610.07727 | **方向**：语音大模型
**作者**：Kyudan Jung (KAIST/Qualcomm 实习)、Hyunsin Park、Yoonhyung Lee、Jinhwan Park、Jinhyeok Yang、KiHyun Nam、Jaegul Choo、Jinkyu Lee；**机构**：Qualcomm AI Research；**发布日期**：2026-10-07
**论文**：[arXiv](https://arxiv.org/abs/2610.07727) | **PDF**：[PDF](https://arxiv.org/pdf/2610.07727.pdf) | **代码**：未发布 | **Demo**：-

### 📌 简介
全双工语音模型要在流式帧里同时决定「说什么」与「何时说/停」。现有 RL 只把时机优势打到扁平 token 流或干脆不管内容语义。HiPLEX 把 Moshi 的文本策略无损拆成两层：控制层每帧选 pad/epad/cont（要不要出内容），条件内容层只在 cont 时选 token。交互奖励经事件因果掩码归到控制层，LLM-judge 语义优势归到内容层，双因子共用同一个头，零新增参数。在 Full-Duplex-Bench v1 上 Moshi+HiPLEX 平滑轮次 TOR 相对 GRPO 从 0.309 降到 0.127，被打断后重响应延时 0.66s→0.44s，Judge 4.083 仍居首。

### 🔧 技术方案

**问题背景：**
全双工 SLM 需在 80ms 帧粒度上持续听用户音频同时生成流式语音，涉及 turn-taking、user pause 静默、backchannel 短应答、barge-in 让位/重入四类时序行为；同时不能牺牲文本内容质量。先前工作（DuplexPO 只在标注窗口内做纯时序 GRPO）把语义排除在外，作者实测发现「纯时序训练」会拖低 Judge 分数并引发复读。

**模型架构：**
基座为 Moshi 7B 与 PersonaPlex，文本头输出 80ms 帧上的 token 概率。作者用温度 T_text=0.7 缩放后 logit，通过 log-sum-exp 把词表划分成 {pad}、{epad}、{cont} 三分组：π_ctrl 从三组 log-sum 里做 softmax，得到当前帧「是否启动发声」；一旦取到 cont，π_cont 在 cont 子词表上归一化选具体 token。两因子相乘精确还原原概率分布（附录 C 给出 KL 无损分解证明），不引入任何额外参数。

**核心创新：**
(1) 双层条件动作层级：把「当/何时说」和「说什么」拆到同一预训练头的两组优势上，各自用 PPO-clipped 目标 αc·L_ctrl+αl·L_cont，独立按各自被选中帧数归一化，防止长 pad 段稀释内容梯度。
(2) 事件因果的 credit mask：从模型自己的生成语音（Silero VAD → speech episode，≤1s 视作 backchannel，>1s 视作 sustained）+ 标注事件时间 + 优势符号三要素生成 per-frame 二值掩码。正 onset 优势强化「开始说」这一决策，而迟到惩罚打在「之前等待」的帧上而非最终那个 onset——固定窗口做不到这种方向区分。
(3) 语义反馈路由：先用 Parakeet-TDT-0.6B-v2 转写用户+模型语音后让 Gemini 2.5 Flash-Lite 给出 0/1/2 响应质量分，组内标准化后只在 ct=cont 帧上施加，与掩码解耦。

**训练策略：**
按四类交互窗口采样 G 个 rollout，每个奖励分量组内独立标准化得 A(k)。Turn-taking 三分量 r(on)/r(delay)/r(early)，Pause 两分量 r(intr)/r(frac)，Backchannel 五分量 r(F1)/r(time)/r(miss)/r(false)/r(long)，Interruption 三分量 r(yield)/r(re-onset)/r(re-delay)。总损失再叠加 βc·KL(π_ctrl||π_ref_ctrl)+βl·π_ctrl(cont)·KL(π_cont||π_ref_cont)。单阶段更新全参，掩码只覆盖扁平更新 20–30% 帧，因此对 Moshi HiPLEX 用 lr 4e-6、GRPO 基线要降到 1e-6 才不被梯度尺度差压垮；PersonaPlex lr 2e-6。

### 📊 实验结果

**数据集**：Full-Duplex-Bench v1，用户侧含 Candor 自然对话、Synthetic pause 与打断脚本，Moshi/PersonaPlex 各 3 seeds。

主要指标（Moshi 家族 seed-42 端点 ckpt，↓低好）：
- Candor pause takeover rate：Moshi 0.579 / GRPO 0.454 / HiPLEX 0.306
- Smooth turn-taking TOR：0.473 / 0.309 / 0.127
- Interruption post-latency（秒）：0.852 / 0.660 / 0.439
- Interruption LLM-Judge：3.773 / 3.942 / 4.083
- Backchannel Freq↑：0.126 / 0.110 / 0.134
- PersonaPlex 同族 pause takeover 0.218→0.018、smooth TOR 0.882→0.714（GRPO 反而 0.444/0.882 恶化）

时序分布层面 HiPLEX 在 merge pool 后的 turn/backchannel 边际上更接近人类 JSD。

**是否开源**：未发布代码/checkpoint，Reproducibility Statement 声明「训练/评测数据与配置以附录形式披露，代码后续释出」。

### ⭐ 评分：7/10
亮点：把 credit assignment 与「事件因果结构」严格对齐、纯因子分解零参数改造很优雅，且在两个模型家族上都同时改善时序与语义；扣分：基线依赖 Ohashi/DuplexPO 内部实现细节、开源缺失，PersonaPlex 的 backchannel JSD 反而变差、Syn-pause 上 GRPO/HiPLEX 都饱和到 1.000 暴露评测协议敏感。
## [4] AdaLoop: Adaptive-Depth Latent Reasoning for Audio Language Models

arXiv ID：2610.06949 | **方向**：语音大模型
**作者**：Lee Seung-woo、Bowen Qi
**机构**：首尔国立大学、上海交通大学
**发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.06949
**PDF**：https://arxiv.org/pdf/2610.06949.pdf
**代码**：暂无
**Demo**：暂无

### 📌 简介

音频大模型（LALMs）存在显著的"语义强、感知弱"失衡：音高比较、响度排序等信号级任务需要迭代式精细声学分析，而现有架构对难易问题消耗相同计算深度。AdaLoop在音频编码器与语言模型之间的连接器位置插入轻量循环潜块（RLB），共享权重反复迭代，并由以问题为条件、可学习的停机单元（ACT机制）自主决定每个样本精化的轮数（上限K_max=8）。新增参数仅占基座2.4%至2.9%，且不改动编码器与LLM本身，在MMSU、MMAU-Pro、MMAR三个基准上对Qwen2.5-Omni-7B、Kimi-Audio-7B、MiMo-Audio-7B三个异构骨干平均提升2.9至3.8个点，最大增益恰好落在感知密集子任务上。

### 🔧 技术方案

**问题背景：** MMSU/MMAR等评测显示LALMs语义理解可靠但声学感知薄弱，Qwen2.5-Omni的MMSU感知子项仅44.5%，固定深度的一过性推理路径是主要瓶颈。
**模型架构：** AdaLoop用共享权重的Recurrent Latent Block替换音频编码器到语言模型的线性投影连接器。每次迭代依次执行问题引导交叉注意力、尺度感知自注意力（8个注意力头分入4个尺度组，局部窗口w=2/4/8/16以同时捕捉快慢声学模式）、前馈加残差（FFN扩张比4）；采用pre-norm与截断至各窗口的RoPE，并以步 embedding e_k注入迭代次数；音频特征最多迭代K_max=8轮后送入LLM，音频输入上限3000 token（约30秒）。
**核心创新：** (1)可学习停机单元每步输出p_k=σ(wᵀ[池化音频状态;池化问题]+b)，累积R_k，当R_k≥1即停止，深度逐样本自适应；(2)沿用ACT软混合输出Σp_k·H(k)+r·H(K)，对停机参数全程可微、端到端训练；(3)引入λ=0.01的ponder cost惩罚迭代数，使模型在无深度标签下自发学会"难题多想"。
**训练策略：** 两阶段：阶段一只训RLB与停机单元（冻结编码器与LLM）1000步，学习率5e-5；阶段二解冻语言模型与RLB、停机单元联合微调3000步（编码器始终冻结），学习率1e-5，Adam、100步线性warmup加余弦衰减，4张A100-80G、单卡batch 2、梯度累积4（有效batch 32）。训练集为5万条可验证声学QA（韵律、说话人/对话、语音内容、声音事件、音乐、多片段场景），源自LibriSpeech、FSD50K、AudioSet、AudioCaps、MELD并经Qwen3-TTS、LeVo与Scaper合成，单类占比不超20%。

### 📊 实验结果

**数据集**：MMSU、MMAU-Pro、MMAR（训练数据基于EvoAudio可验证QA家族5万条）
主要指标
- Qwen2.5-Omni-7B三基准平均：59.3%→63.1%（+3.8），同数据仅调连接器SFT为60.5%（+1.2）、Fixed-4固定深度61.4%（+2.1）
- 感知子项：MMSU Perception 44.5%→53.1%，MMAR信号级55.8%→59.5%
- Kimi-Audio-7B-Instruct平均：53.3%→56.7%（+3.4）；MiMo-Audio-7B-Instruct平均：58.8%→61.7%（+2.9）
- 学到的推理深度：全局平均3.8轮，信号级任务5.7轮、语义仅2.6轮，9.3%样本1轮停止、4.2%打满8轮
- 消融：固定深度K=4掉1.7点，停机去问题条件掉1.6点，去尺度感知注意力掉1.2点，去ponder cost或K_max=4各掉0.8点
**是否开源**：论文未提供代码与Demo（暂无），仅基于公开模型与公开音频数据集训练。

### ⭐ 评分：7/10

将ACT自适应计算思想移植到音频大模型连接器、直击感知短板的定位准确，三个异构骨干一致涨点2.9至3.8且深度分布可解释、消融逐项到位；扣分在代码未开源、训练数据仅5万条偏小、缺少推理时延与算力开销的量化分析，方法上限受单遍即可解决问题收益收窄的限制。
## [5] EMODE: Dynamic Para-Semantic Experts for Emotion-Aware Speech Language Modeling

arXiv ID：2610.06956 | **方向**：语音大模型；**作者**：Jianan Pan、Yiwen Gu、Xinze Li、Rui Wang、Kejie Huang；**机构**：浙江大学（杭州）；**发布日期**：2026-10-07 | **论文** https://arxiv.org/abs/2610.06956 | **PDF** https://arxiv.org/pdf/2610.06956 | **代码**：暂无 | **Demo**：暂无（已被 ACM Multimedia 2026 接收）

### 📌 简介
大型语音-语言模型在跨模态理解与生成上表现强劲，但情感等副语言信息难以保留：单一纠缠声学表征使语言模型过度依赖转写出的词汇内容走捷径。本文提出情感感知语音语言模型 EMODE，核心模块为动态副语义专家 DPSE，将连续语音特征解耦为语义与副语言双通路，动态路由后融合再送入语言模型；配合三阶段课程训练与正交专家引导、语义-声学对齐、门控多样性正则三项约束。在九数据集 SER、SpeechAlpaca 共情回复及新建中英双语 MEPA 基准上，EMODE 在词汇保真与情感敏感之间取得更好平衡，跨库情感理解更稳健。

### 🔧 技术方案
**问题背景：** 现有语音连接器以语义转写为优化目标，情感隐含在单一表征中易丢失；模型可用词汇捷径完成情感任务，缺少对韵律、音色等声学证据的真正依赖，且自然带情感标注的对话语料稀缺。

**模型架构：** Whisper-base 编码器提取帧级特征，DPSE 含自注意力路由器与语义/副语言两个卷积下采样专家；路由器输出两路分布，副语言门控向量以残差方式融合，最终表征为 LayerNorm(语义序列 + 门控乘副语言序列)，再接入 Qwen2.5-7B-Instruct；训练期另设冻结文本教师通路提供参考分布与隐藏状态，副语言专家经注意力池化输出句级摘要供情感分类器使用。

**核心创新：** (1) DPSE 双专家动态路由与门控残差融合，先验分离"说了什么"与"怎么说的"；(2) 正交专家引导 OEG：语义分支用音素级 CTC 监督，副语言分支用句级情感交叉熵监督，防止路由坍缩；(3) 语义-声学对齐 SAA 用情感词元掩码拉近副语言表征与文本教师隐藏层余弦相似度（损失 1−cos），门控多样性正则 GDR 以负熵鼓励早期路由探索。

**训练策略：** 三阶段课程：Stage I 语义预热，冻结副语言专家、禁用路由，仅优化 KL 蒸馏 + 语义 CTC；Stage II 副语言激活，冻结语言模型，优化两项 OEG + GDR；Stage III 联合精调，在语音续说、情感续说与 SER 混合数据上加 LoRA，副语言 OEG 权重固定 0.02，SAA 权重从 0 线性升至 0.1，GDR 从 0.03 衰减到 0.01。Stage I 用 LibriSpeech、CommonVoice、GigaSpeech、WenetSpeech；情感监督来自 IEMOCAP、MELD、ESD、CMU-MOSEI、MEAD、EARS、EXPRESSO、MSP-Podcast，统一映射为中性/开心/生气/悲伤/惊讶五类。

### 📊 实验结果
**数据集**：域内 IEMOCAP、MELD；零样本跨库跨语言 RAVDESS、SAVEE、MERBench Test1/Test2（中）、RESD（俄）、AESDD（希腊）、CaFE（法）；共情回复 SpeechAlpaca；自建双语 MEPA（固定词汇、五种情感演绎）。

主要指标
- 九数据集 SER 平均准确率：72.10%，居所有对比模型之首（EmotionThinker 68.46，BLSP-Emo 65.21）；MELD 64.23、SAVEE 85.76、RAVDESS 75.58 均排第一，IEMOCAP 76.68 略低于 EmotionThinker 77.68
- SpeechAlpaca：SER 88.75%，Quality 7.12，Empathy 6.14（BLSP-Emo 为 83.8/6.90/5.91）
- MEPA：英文 Acc 56.4 / F1 54.7 / GLCA 12.1；中文 47.8 / 45.3 / 8.6，GLCA 较 EmotionThinker 提升 4.0/3.7 点
- 消融：去掉副语言 OEG 四库均值从 75.56 降至 69.64；连接器对比 DPSE 75.56 优于 CFormer 73.07 与 Subsampler 69.94

**是否开源**：暂未公开代码与模型，基准 MEPA 预计随论文发布；许可为 CC BY-NC-SA 4.0

### ⭐ 评分：7/10
理由：问题定位准确，副语言-语义显式解耦的归纳偏置设计干净，OEG/SAA/GDR 消融证据充分，九数据集含五种语言零样本评测与受控 MEPA 基准显著增强说服力；局限在于 MEPA 由 TTS 合成、共情评分依赖单一自动评审缺少人工评估，且未开源，整体为 MM 水准的扎实增量工作而非范式突破。
## [6] Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution

arXiv ID：2610.07641
**方向**：语音大模型
**作者**：Kyudan Jung、Hyunsin Park、Yoonhyung Lee、Jinhwan Park、Jinhyeok Yang、KiHyun Nam、Jaegul Choo、Jinkyu Lee
**机构**：Qualcomm AI Research；KAIST AI
**发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.07641
**PDF**：https://arxiv.org/pdf/2610.07641.pdf
**代码**：暂无
**Demo**：暂无

### 📌 简介
本文针对端侧级联（ASR-LLM-TTS）语音智能体中工具延迟串行暴露的问题，提出投机式工具执行框架。核心思想是利用流式ASR的部分识别假设，在用户尚未说完时提前预测并发起高延迟只读工具（如网页搜索）调用，将结果缓存并直接注入LLM提示，把工具延迟隐藏在用户说话时间内。方法由规则预测器、缓存校验回退与LLM自主回退三重机制组成，保证最坏情况不劣于串行基线。在完整实现的Android语音助手真机实测中，TTFA中位数从5.79s降至4.60s，标准差从3.49s降至2.81s，工具调用F1从44.8%提升至60.6%，响应更快且更可预测。

### 🔧 技术方案
**问题背景：** 级联架构须等用户说完、ASR定稿、LLM选出工具后才串行执行远程工具，时间线t0<tASR<tLLM-call<tTool<tLLM-resp<tTTS使网络延迟直接暴露给用户，端侧量化小模型工具选择准确率亦低。
**系统架构：** 全链路部署于手机：流式Conformer ASR与FastSpeech2 TTS运行于CPU，W4A16量化Llama-3.2-3B（QAIRT包经QNN）运行于NPU；CPU侧新增规则预测器持续监听部分假设，投机调用EXA搜索API并将结果存入缓存，经直接注入、缓存校验、常规执行三条路径消费。
**核心创新：** (1) 分句级规则预测器：按标点与and/but/then/while等并列词切分子句，单句多意图可并行投机，在累计6词后每5词及停顿超300ms时触发，topic取自12类粗粒度信息查询类别；(2) 直接缓存注入：tASR时刻将定稿转写与投机结果一并写入提示，省去工具往返轮次；(3) 校验回退与安全上界：LLM仍发工具请求时先查缓存防重复检索，规则校验丢弃用户自我更正导致的失效结果，投机仅限只读工具，误判不改动日历闹钟等用户数据，最坏延迟以基线串行流程为上界。
**实现细节：** 实测中LLM在13%场景仍发起工具调用、7%冗余请求已注入信息，均由校验路径吸收复用。

### 📊 实验结果
**数据集**：自建146条英文评测集（100条常规：单/多搜索、日历、闹钟、无需工具；22条含搜索关键词但不需搜索的硬负例；24条含更正、撤回、晚意图、话题切换的对抗样本），用Gemini-2.5-Flash-Preview-TTS合成约1.5小时音频实时流入Galaxy S26 Ultra（骁龙Elite Gen 5），完整评测约3小时。
主要指标：
- TTFA p50：4.60s vs 基线5.79s
- TTFA p99：15.10s vs 19.76s
- TTFA 均值±标准差：5.99±2.81s vs 6.69±3.49s
- 首次工具调用延迟FT p99：11.71s vs 22.44s
- 工具调用F1：60.6% vs 44.8%
- 消融：仅直接注入F1达63.0%（准确率主要来源），叠加校验回退后缓存命中率47.7%、浪费调用由47降至5
- 对抗集F1：90.2%，假读取率12.3%；硬负例假读取率9.1%
- 典型用例：15s查询含约10s搜索，TTFA由17s降至8s
**是否开源**：论文未提供代码与数据集链接，暂无开源发布。

### ⭐ 评分：7/10
理由：工程价值突出——首次在全实现Android端级联系统中实测投机工具执行，TTFA中位数降20%、p99降24%，F1意外提升15.8点；三层回退保证最坏不劣于基线且投机仅限只读工具，安全设计严谨。不足：预测器为纯规则方法、仅12类topic，评测集146条偏小且为合成音频，依赖高通私有栈与商业搜索API，泛化性待验证；创新偏系统级而非算法级，但落地参考价值高。
## [7] Voice Anonymization Made Simple: Training-Free Anonymization with Projected Classifier-Free Guidance

arXiv ID：2610.08276
**方向**：语音大模型
**作者**：Xiang Shi、Han Zhu、Ming Li、Xiaoxiao Miao（通讯作者）
**机构**：Duke Kunshan University、小米集团、香港中文大学（深圳）
**发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.08276
**PDF**：https://arxiv.org/pdf/2610.08276
**代码**：https://github.com/xs125-stack/voice_anon_simple
**Demo**：暂无

### 📌 简介
针对语音匿名化普遍依赖专门训练的问题，本文提出基于预训练流匹配语音转换系统 Seed-VC v2 的两阶段免训练匿名化方法。第一阶段在条件构造时用随机说话人上下文重新生成源内容 token，削弱表征中残留的源说话人信息；第二阶段在语音生成时用源语音估计与原说话人对应的生成方向，通过投射式无分类器引导（Projected CFG）抑制 token 引导中与源音色对齐的分量，同时保留内容引导。全程仅修改推理侧条件与引导规则，不更新任何预训练参数，在 VoicePrivacy 2026 Track 1 上取得隐私与效用的良好权衡。

### 🔧 技术方案
**问题背景**：语音匿名化需在隐藏说话人身份的同时保留语言内容与情感。现有方法（共振峰等信号处理、ASR+TTS 重合成、解耦表征合成、扩散/流匹配匿名化如 DiffAnon、F3-VA）大多需要匿名化专项训练或额外可学习模块，更换基座模型即需重训。核心问题：能否仅改变预训练流匹配 VC 模型的推理过程使其变成匿名化器？

**方法**：Stage 1（条件构造）：源窄带 token 提供语言序列，改以随机采样目标的窄带/宽带 token 作 AR 上下文与前缀，重新生成宽带 token 条件 mu_AR；为保持 prompt 对齐，token 提示 mu_prm、Mel 声学提示 p 与 CAM++ 风格嵌入 s 仍取自源语音，仅用于 Stage 2 暴露源条件影响。Stage 2（生成引导）：每个 ODE 步计算源条件方向 d_s=v_f-v_c 与 token 引导方向 d_c=v_c-v_u，将 d_c 按 global、Smooth-21（滑窗 K=21）、token 三种粒度投影到参考 q 上得到对齐分量 p_t，最终场 v_anon=v_c-lambda_s*p+lambda_c*d_c，以 v_c 为基点避免直接重建源声，Euler 求解后经 BigVGAN v2 声码器出波形。

**核心创新**：(1) 随机目标条件化 AR 重建，在表征层面削弱内容与源音色纠缠，固定引导尺度下三种投影模式 dev L-EER 均提升（如 Smooth-21 由 34.20% 到 34.79%），增益非超参差异所致；(2) 源条件感知投射 CFG：源提示与风格嵌入只作"方向参照"而非重建条件，主动剔除 token 引导中回灌源身份的残余分量；(3) lambda_s 与 lambda_c 作用解耦，可在 30 句筛选子集上以 0.1 步长扫描 0-3，按 WER<5% 约束选点，全量评测不再调参。

**协议**：遵循 VoicePrivacy 2026 Track 1（英语）官方评测：ASV 攻击以 lazy/semi-informed EER 衡量隐私，效用为 WER 与 SER 的 UAR；随机目标池为 LibriTTS train-other-500 中 500 位说话人各一条 3-6 秒短句，有放回采样、固定种子。

### 📊 实验结果
**数据集**：VPC2026 Track 1（LibriSpeech dev/eval 源语音 + VPC 官方攻击/ASR/SER 模型），基座 Seed-VC v2。
评测集（Smooth-21 且用随机目标 RT，lambda 1.1/2.8 对比 Built-in 0.7/0.7 与最强基线 B5）：
- Lazy-EER：29.39%（Built-in 28.19%，B5 25.65%）
- Semi-EER：21.51%（Built-in 17.78%，B5 17.05%）
- WER：4.46%（Built-in 4.58%，B5 4.44%）
- UAR：39.57%（Built-in 40.38%，原文 71.06%）
- Dev Lazy-EER：35.09%，为全表最高（Built-in 33.15%）
主要结论：两项干预均有独立贡献；隐私全面超越官方基线与内置匿名化，WER 几乎持平，UAR 略降。
**是否开源**：是，代码与音频样例见项目 GitHub 仓库，模型基于开源 Seed-VC v2。

### ⭐ 评分：7/10
理由：免训练即插即用的思路优雅、工程价值高，把"表征去耦+生成引导纠偏"落在纯推理侧；消融设计规范（尺度作用验证、固定尺度下 RT 对照、多投影粒度比较），指标在隐私维度显著超基线且效用损失小。不足：创新偏增量式推理技巧而非新模型；仅英语单语种；情感工具性低于内置模式（UAR -0.81 绝对值），Semi-EER 21.51% 距实用仍有差距；每换基座仍需在筛选集做二维网格搜索，lambda 与随机目标采样存在敏感性。
## [8] SkillFormer: Skill-Decomposed Adaptation for Audio Language Models

arXiv ID：2610.07533 | **方向**：语音大模型 | **作者**：Lee Seung-woo、Bowen Qi、Kim Min-jun、Jang Won-young | **机构**：釜山大学、上海交通大学、汉阳大学 | **发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.07533 | **PDF**：https://arxiv.org/pdf/2610.07533 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
音频大模型需同时掌握音高对比、说话人计数、音乐节奏估计、情感识别等数十种技能，联合训练存在明显的技能干扰：提升一项往往以牺牲另一项为代价。本文提出 SkillFormer，将音频理解为技能分解式适配问题：把不同技能路由到不同的低秩适配器参数上，推理时由问题条件路由器动态选择并加权组合 K=6 个技能专属 LoRA，使音高查询与曲风分类走不同参数路径。交替训练调度先让各适配器在专属技能簇上独立专精，再联合校准路由以避免多任务梯度冲突。方法仅增加基座模型 3.2%–3.8% 的参数，不改动音频编码器与语言主干，即插即用；在 Qwen2.5-Omni-7B、Kimi-Audio-7B、MiMo-Audio-7B 三种异构架构上，于 MMSU、MMAU-Pro、MMAR 三大音频推理理解基准平均提升 2.4–4.1 点，感知、推理、语义子类增益均衡。

### 🔧 技术方案
**问题背景：** 现有音频大模型改进集中在训练什么内容（课程学习、奖励塑形、自我进化如 EvoAudio）或推理多深（循环潜空间推理），均未回应哪个问题该激活哪些参数这一核心，导致技能间干扰与平均高但子项弱的现象。
**模型架构：** 在音频编码器与语言模型之间并联插入 K=6 个 rank r=16 的 LoRA 适配器，ΔH_k=H·B_k·A_k；B_k 正态初始化、A_k 零初始化，训练前输出为零以完整保留基座行为，B_k 与 A_k 间加 0.05 dropout。路由器将问题词元经均值池化、两层 MLP（GELU）与 top-n softmax（n=2)产生至多 2 个非零门控权重，合并 ΔH=Σα_k·ΔH_k 后送入语言主干，推理成本与 K 无关。
**核心创新：** (1) 无监督技能聚类：用基座 tokenizer 嵌入训练问题并 k-means 聚成 6 簇——语音韵律、说话人与对话、语音内容、声音事件、音乐、多片段场景，与 EvoAudio 问题分类吻合；(2) 问题条件稀疏路由：同一音频配不同问题激活不同适配器，仅按音频路由会使两类问题被迫同路径；(3) 交替训练调度：Phase A 每个适配器在自己簇上单独训练 500 步、其余适配器与路由器冻结，学习率 5e-5（Adam+余弦衰减）；Phase B 路由器与全部适配器在 50000 条全簇均衡样本上联合校准 2000 步，学习率降至 1e-5，此阶段解冻语言模型。
**训练策略：** 数据为 EvoAudio 工具箱的 50000 条可验证 QA 对，源自 LibriSpeech、FSD50K、AudioSet、MELD 及 Qwen3-TTS、LeVo、Scaper 合成；Phase A 每适配器约 8300 条，Phase B 使用全部数据；4 张 A100-80G，单卡 batch 2、梯度累积 4 步；新增参数占比 3.2%–3.8%。

### 📊 实验结果
**数据集**：MMSU、MMAU-Pro（封闭非空间子集）、MMAR
- Qwen2.5-Omni-7B 三基准平均：Base 59.3 → SFT 60.6(+1.3) → Multi-LoRA 61.7(+2.4) → SkillFormer 63.4(+4.1)
- Qwen 分项 All：MMSU 61.4→66.5；MMAU-Pro 56.4→60.4；MMAR 60.2→63.3；MMSU 感知单项 44.5→52.5（最大 +8.0）
- Kimi-Audio-7B：53.3→57.1(+3.8)，MMAU-Pro 声音子类 37.1→42.8（+5.7，全模型最大单子类增益）
- MiMo-Audio-7B：58.8→61.2(+2.4)
- 消融（Qwen 均分 63.4 基准）：去路由器（均匀权重）61.7(-1.7)、随机路由 60.9(-2.5)、单一 LoRA 60.6、K=3 62.3、K=12 62.7、无交替调度 61.1(-2.3)、top-1 -0.6、稠密路由 -0.4、r=8 仅 -0.3
- 路由器权重可视化：韵律问题 71% 权重集中于 A1，音乐 68% 给 A5，声音事件 62% 给 A4，聚类与路由在无监督下自发对齐
**是否开源**：暂无（论文未提供代码、模型或 Demo 链接）

### ⭐ 评分：7/10
问题切入准确，技能干扰是音频大模型微调的真实现状，"调哪些参数"视角补足了课程学习与推理深度两条主线之外的空白。工程验证扎实：约 3.5% 参数换来三个异构基座上一致收益，消融干净地分离出路由器（-1.7）与交替调度（-2.3）各自的贡献，路由可视化令人信服。局限在于概念组合（LoRA 专家库+稀疏路由）略显可预期，仅 5 万条数据与单次调度，且未与自我进化或 RL 课程正交组合验证上限。
## [9] Region-Aware Masking for Accent-Robust Cross-Lingual Text-to-Speech

arXiv ID：2610.07524 | **方向**：语音大模型；**作者**：Haoqi Li、Shivam Mehta、Ravi Teja Gadde、Yinghong Lan；**机构**：Netflix Inc., USA；**发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.07524 | **PDF**：https://arxiv.org/pdf/2610.07524 | **代码**：暂无 | **Demo**：https://doubleblindauthor.github.io/region-aware-masking-TTS-demo

### 📌 简介
跨语言零样本TTS常出现口音泄漏：模型在保留参考音色的同时，把源语言发音习惯带入目标语言输出。在掩码重建式TTS中，训练用同语言上下文、推理却用跨语言上下文，该失配进一步放大问题。本文提出区域感知掩蔽：将两种语言语句拼接为一条训练样本，掩码相对语言边界放置，使训练复现推理的跨语言提示模式，无需语言ID、口音标签、平行语料或架构改动。母语听者评测将感知口音从4.3降至0.5（0-5分制），清晰度与自然度无可测损失，且可泛化至未见源语言。

### 🔧 技术方案
**问题背景：** Voicebox、E2 TTS、F5-TTS等掩码重建范式训练时从同语言上下文复原被掩码区域，跨语言推理却须依赖外语声学上下文，模型倾向从参考音频复制语言相关属性（尤其中口音）。同说话人平行跨语言语料稀缺昂贵，语言ID、对抗口音抑制等显式解耦方案条件复杂。

**模型架构：** 基于预训练多语言F5-TTS：非自回归扩散Transformer，以最优传输条件流匹配（OT-CFM）做文本引导语音填充。架构与条件输入完全不变，仅改训练样本构造：从两语料各采一条语句拼接log-mel频谱，字符序列以"|"分隔，拼接顺序均匀采样；语言边界仅决定掩码位置，不向模型传入语言身份。

**核心创新：** (1)区域感知掩码分布：定义random、part0-only、part1-only、two-region四种策略，在各区域按占比s~U[0.7,1.0]取连续掩码span，uniform为四策略等概率混合；模型被迫在一侧跨语言声学上下文下重建另一侧目标，训练条件与推理对齐，只传目标文本负责发音、跨边界传递音色。(2)掩码几何权衡分析：证明权衡由"掩在哪"而非"掩多少"决定——random与two-region期望均掩85%，但双区域掩蔽同时更抑口音并保音色；part1-only期望仅掩42.5%，口音最低却音色偏移最严重（20项内部集45.3%、FLEURS未见语言集42.1%的样本音色判变）。(3)可选说话人相似伪对：ECAPA-TDNN嵌入加FAISS预检索Top-K=10跨语言近邻，检索对比度ρ=2.37远优于x-vector的1.06，当掩蔽消除说话人证据时提供音色锚点。

**训练策略：** 从同一预训练多语言checkpoint热启动避免从零训练；p_single=0.2，即80%样本为拼接双语、保留20%单语防灾难性遗忘；AdamW学习率1e-4，4000步warmup；所有系统统一2.04个训练epoch预算保证公平对比；推理仍以参考音频+目标文本拼接提示生成。

### 📊 实验结果
**数据集**：内部英语21.2M、西语9.3M条单说话人语句（说话人不相交，无平行）；评测为内部ES→EN 20对与FLEURS 90对（西/法/葡→英）；20名英语母语者主观打分。
主要指标（基线B vs 推荐two-region系统M2，FLEURS未见语言FR/PT→EN）：
- 感知口音（0-5）：4.21 → 0.69，内部集4.28 → 0.32，M3最低0.22
- 音色判变占比：1.5% → 15.1%
- Joint合格率（口音≤1且音色保留）：3.1% → 69.6%，M2+P达69.7%
- 说话人相似SIM（WavLM/ECAPA）：0.960/0.710 → 0.704/0.234
- WER（Whisper large-v3）：0.122 → 0.066
- UTMOS：3.20 → 3.94
相对仅双语适配M1，区域感知掩蔽在已见场景降口音18-51%、未见源语言降35-55%；口音评分者一致性α=0.98。

**是否开源**：代码暂无，Demo音频提供于补充网站，训练数据为内部语料，复现受限。

### ⭐ 评分：7/10
优点：精准指出掩码重建TTS训练-推理失配这一被忽视的口音泄漏根源；方法只改掩码分布，零架构与标注成本、即插即用；掩码几何对比实验给出明确可操作结论（推荐two-region），并提示高SIM可能反映口音复制、不可单独作为选型标准，洞察有价值；增益可泛化到未见源语言。不足：语言对仅西/法/葡→英单向，评测规模小（20-90条、20位听者），口音依赖人工听测无客观指标，数据内部不公开，微调后客观说话人相似度明显下降且代码未开源。属高工程价值的简洁方法，方法论新颖性中等。
## [10] Exposing and Mitigating Neural Codec Vulnerabilities in Audio Deepfake Detection

arXiv ID：2610.07216 | **方向**：语音大模型；**作者**：Abdullah、Awais Khan、Khalid Mahmood Malik；**机构**：密歇根大学弗林特分校创新与技术学院（University of Michigan-Flint，NSF Grant 2409577资助）；**发布日期**：2026-10-07 | **论文**：https://arxiv.org/abs/2610.07216 **PDF**：https://arxiv.org/pdf/2610.07216 **代码**：暂未公开 **Demo**：无

### 📌 简介
主流音频大模型（ALM）普遍以神经编解码器作为波形的重合成模块，其生成伪影与传统MP3/AAC后处理压缩性质不同。本文首次系统揭示：七个SOTA音频深伪检测（ADD）模型在七种神经codec压缩下性能大幅崩塌，平均EER达28.67%，其中以codec重合成（CoRS）数据训练的系统最脆弱，经合法压缩的真实语音常被判为假。作者构建ANC-Spoof数据集，并提出PCL-NET，用成对一致性学习把codec伪影从真假判定中解耦，将平均EER降至12.77%，同时保留一定的CoSG深伪检测能力。

### 🔧 技术方案
**问题背景：** 既有ADD鲁棒性工作默认压缩是生成后独立施加的扰动（加性噪声、信道效应、MP3/AAC低码率等），未触及与生成过程耦合的失真。ALM类TTS/VC用codec解码器从离散token重建波形，codec实为生成器的一部分；社区又以CoRS作CoSG训练代理，隐含风险是检测器学会把codec失真当作"假"的判别线索，从而把语音消息等合法codec压缩的真语音误报为深伪。

**方法：** PCL-NET以预训练XLS-R-300M为前端编码器，取全部L层隐状态（d=1024），各层时间池化后经共享线性投影与sigmoid得标量注意力权重，再加权融合；后端为BatchNorm+SELU+时间max-pooling与log-softmax分类头。训练中对每条语音xi用codec Ck生成压缩版本xic，共享编码器得到表征zi与zic，以L1距离最小化成对表征差异（一致性损失），该约束仅作用于损失层面；总损失为交叉熵（对原始与压缩视图均计算）加λ乘一致性项，λ=0.7。推理只需单次前向。

**核心创新：** (1) 首个系统暴露ADD在神经codec压缩下脆弱性的研究，证实CoRS训练显著放大该漏洞；(2) 构建ANC-Spoof基准：BigCodec（159M参数、约1kbps）、DAC（低至8kbps）、HiggsV2（25帧/秒）、Mimi（24kHz→12.5Hz）、SNAC、SpeechTokenizer、WavTokenizer共7种codec施加于3个基准，产出1269704条标签保持的压缩语音；(3) 成对一致性学习协议，codec重合成作为保标签增强同时注入真假两侧，迫使模型学到codec不变特征。

**协议：** 用ASVspoof2019 LA的train/valid训练，在ASV19、In-the-Wild、FoR评测集测7种codec及MP3/AAC/Opus（12K/24K/48K/96K）鲁棒性，指标为EER；另在CodecFake+与CDD的真实-CoSG子集验证无CoSG反噬。

### 📊 实验结果
**数据集**：ANC-Spoof（ASVspoof2019 LA + In-the-Wild + FoR，158713原始+1110991压缩=1269704条）；辅测CodecFake+、CDD。
- SOTA平均codec压缩EER：28.67%；CoRS系最脆弱，XLS-R-2B在FoR原始1.01%→压缩均值51.2%（近随机）
- PCL-NET(All，7 codec随机)平均EER：12.77%，分集ASV19 5.15%、Wild 23.44%、FoR 9.82%
- 常规压缩同步改善：FoR 12K EER从35.78%降至7.38%
- CoSG检测：CodecFake+ 31.28%、CDD 23.09%，优于非CoRS基线（AASIST约42%）但逊于CoRS专用SOTA（XLS-R-2B 3.67%）
- 面向压缩的codec（BigCodec、SNAC）比CoSG向tokenizer带来更强鲁棒增益
**是否开源**：数据集承诺论文接收后发布至Hugging Face；模型代码未公开。

### ⭐ 评分：6/10
选题切中ALM时代真实安全漏洞，暴露"CoRS代理训练反噬合法压缩真语音误报"的问题有洞见，实验覆盖7 codec×3基准×多SOTA、分析充分，ANC-Spoof对社区有共享价值。扣分：仅用后处理重合成代理原生CoSG（作者自认局限），Wild集EER仍高（23.44%），且一致性学习属常规正则化技巧、在CoSG检测上明显落后专用模型，方法新颖性与实用上限有限。
## [11] Exploiting Acoustic and Content-Oriented Speaker Verification Attacks Against Multilingual Voice Assistants

arXiv ID：2610.08107 | **方向**：语音大模型
**作者**：Ridwan Arefeen, Ze Li, Rong Tong, Ming Li, Xiaoxiao Miao（通讯：Xiaoxiao Miao）
**机构**：新加坡理工大学（SIT）、武汉大学、香港中文大学、昆山杜克大学
**发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.08107
**PDF**：https://arxiv.org/pdf/2610.08107
**代码**：https://github.com/monkeyDarefeen/DAST（代码、预训练模型与MultiVC数据集开源）
**Demo**：无（已被IEEE SLT 2026接收）

### 📌 简介
本文以声学通道（WavLM-ECAPA）与内容通道（w2v-BERT-MFA）双说话人验证攻击系统，评测多语种语音匿名化（英德法中西日六语种，VPC 2026 Track 2）的重识别脆弱性，构建71.4万条多语种语音转换数据集MultiVC。结果表明攻击有效性受匿名化语音语言效用耦合：声学攻击整体更鲁棒，语言信息保留完好时内容攻击差距收窄；MultiVC可部分缩小跨语言EER差距。

### 🔧 技术方案
**问题背景：** 语音匿名化攻击者ASV系统此前几乎只在英语下评测，多语种行为未知。VPC 2026挑战赛中同一共享攻击模型在英语获得最低EER、中文与日本语显著劣化，且各语言匿名化语音WER差异大，但缺口根因（数据稀缺还是语言结构）尚不明确。

**攻击框架：** 六语种语音先经BM1（HuBERT嵌入替换+HiFi-GAN声码）或BM2（Whisper转写+WGAN伪说话人嵌入+Toucan TTS）匿名化，再由两类攻击模型重识别：声学导向WavLM-ECAPA双流（冻结WavLM+梅尔谱频双路ECAPA-TDNN融合）与内容导向w2v-BERT-MFA（24层Conformer+多尺度特征聚合+LoRA微调），同步用Whisper-Large-v3计算ASR效用作诊断，EER越低攻击越强。

**核心创新：** (1) 首次诊断出跨语言重识别缺口与ASR效用（WER/CER）的声学-语言耦合：BM2下中文CER达70.3%、日本语45.1%，重识别同步崩溃，表明可懂度受损稀释身份线索。(2) 构建MultiVC数据集：以TidyVoiceX（4474说话人、40语言、32.1万句）为目标池、7个VC系统各转换102066条，按说话人轮转分10折保证目标不相交，共714462条。(3) 在lazy-informed与semi-informed两种威胁模型下系统比较双攻击范式对匿名化的鲁棒性。

**协议：** 训练用VPC 2026官方集与SSTC英语VC数据；评测含英德法西WER与中日CER、各语言EER及均值；semi-informed按VPC2026官方脚本在目标匿名化数据上微调。

### 📊 实验结果
**数据集**：VPC 2026 Track 2六语种测试集；日语Common Voice/JVS；中文AISHELL-3

- 主要指标（EER，%）
- Lazy-BM1 WavLM-ECAPA均值：15.77（+MultiVC后8.99）
- Lazy-BM1 w2v-BERT-MFA均值：25.86（+MultiVC后17.66）
- Lazy-BM2 WavLM-ECAPA均值：29.76（+MultiVC后24.83）
- Semi-BM1最优攻击（WavLM+MultiVC）均值EER：3.66，英语2.79
- Semi-BM2 WavLM均值EER：15.23 vs w2v-BERT 34.88
- BM2中文CER：70.3（BM1仅30.2）
- BM2日语CER：45.1（BM1仅9.7）
- BM1英语WER：5.4（BM2升至16.0）

**是否开源**：是，代码/模型/MultiVC数据集已开源

### ⭐ 评分：6/10
理由：首次系统揭示语音匿名化跨语言攻击瓶颈与语言效用的耦合规律，MultiVC数据集规模可观且全部开源，实验对lazy/semi双威胁模型、双攻击范式的对比设计规范，对SLT社区有实际参考价值；但攻击方法本身无新模型贡献，属实证诊断型工作，且耦合结论仅为相关性分析而非因果证明，六语种仍偏少、未覆盖口音与噪声条件。
## [12] Neural Representations, Natural Connections: What Transfers From Human Speech Foundation Models

arXiv ID：2610.07107 | **方向**：语音大模型；**作者**：Tomás Arias-Vergara、Christopher Hauer、Héloïse Brotier、Elmar Nöth、Andreas Maier、Lee Koren；**机构**：Erlangen-纽伦堡大学（FAU）模式识别实验室、Amberg-Weiden应用技术大学、巴伊兰大学Gonda多学科脑研究中心；**发布日期**：2026-10-07

**论文**：https://arxiv.org/abs/2610.07107 | **PDF**：https://arxiv.org/pdf/2610.07107 | **代码**：论文内未提供 | **Demo**：无

### 📌 简介
本文系统研究人类语音基础模型表征向动物发声的可迁移性，回答"语音预训练究竟习得了何种可跨物种复用的声学结构"。作者冻结15个编码器（单语/多语语音、说话人验证、动物生物声学、通用音频），在岩蹄兔、斑胸草雀、纵纹腹小鸮、幼狨猴4个物种上做主叫者识别，另在3物种上做叫声类型分类。结果显示语音表征不逊于甚至显著优于动物专用预训练模型，且迁移增益高度依赖层级与前端形式，为小样本生物声学分析提供了模型选择与层选择指南。

### 🔧 技术方案
**问题背景：**语音SSL模型（wav2vec 2.0、HuBERT、WavLM）的表征已证实可编码说话人与声学信息并迁移至动物发声，但决定跨物种迁移成败的因素——语言覆盖度、预训练域、说话人专业化——缺乏受控比较，此前结论碎片化。

**方法：**统一预处理为16 kHz单声道，按人工标注切分发声单元（不足0.4 s的用周边音频扩展或零填充；曾测试生物声降噪模型，因抑制身份相关频段而弃用）。取各编码器逐层输出，经均值加标准差池化为1538/2048维特征，接类别平衡逻辑回归分类。对照组为121维MFCC+对数时长手工基线。

**核心创新：**(1)首个跨预训练域的统一基准：15个冻结编码器涵盖单语（wav2vec2-large、HuBERT-base、WavLM-base+、Whisper-small.en）、多语（XLS-R-300m、mHuBERT-147、XEUS）、说话人验证（ECAPA-TDNN、wav2vec2-SV、UniSpeech-SAT-SV、WavLM-SV）、动物域（AVES-bio、AVES2-all/bio）与通用音频（BEATs），双任务7个设置；(2)架构对齐的受控消融：HuBERT/mHuBERT与wav2vec2/XLS-R配对量化语言覆盖影响（差值均不超过0.040 UAR），固定BEATs主干仅换预训练域，排除架构混淆；(3)逐层探针发现前端决定最优层深：原始波形模型峰值在浅层（相对深度0.15-0.51），频谱patch模型在深层（0.64-0.88），证明仅评最后一层会误判迁移能力。

**协议：**3折交叉验证，主叫者识别按录音会话分折、叫声分类按个体分折；层深与正则系数C经训练折内2折联合选择；配对聚类自助法检验显著性，Holm-Bonferroni校正；补充会话独立性敏感性分析。

### 📊 实验结果
**数据集**：岩蹄兔16只（3863 bout/19970元素）、草雀33只（3090声）、小鸮16只（952声）、幼狨10只（72921声），总评测时长89/21/20/464分钟。
**主要指标**
- 主叫者识别语音最优 vs 动物最优差值：-0.027至+0.119 UAR，草雀+0.119（p<0.001）、狨猴+0.086（p<0.001）、蹄兔+0.006，3/7显著优、4/7无显著差、0个设置动物显著优
- 各任务最佳：小鸮0.757（BEATs）、蹄兔0.474（AVES2-bio）、草雀0.581（Whisper）、狨猴0.482（Whisper）
- 说话人验证x-vector头低于同模型所有编码器层0.10-0.32 UAR（21设置全败），ECAPA-TDNN在全部7设置低于MFCC基线
- 叫声分类：XLS-R蹄兔0.939、Whisper草雀0.866、MFCC基线0.579-0.873
- 模型规模无效：最大编码器XEUS在两任务均最弱（草雀0.205）
**是否开源**：论文CC BY 4.0公开，未见代码与数据发布链接。

### ⭐ 评分：6/10
优点：受控消融设计严谨（架构配对、主干固定、聚类自助+多重校正、会话独立性分析直面身份泄漏风险），"负结果"归因清晰，逐层发现具实践指导价值。不足：仅评估既有冻结模型、无新方法贡献；物种与任务规模有限，结论多为统计不显著，上限受probing协议影响；模型规模与前端混淆未完全解耦，可外推性一般。
## [13] InterCorrect: Intersection-Aware Correction of Demographic Model Merging for Fair ASR

arXiv ID：2610.08604
**方向**：语音大模型
**作者**：Ashley E. Bravo-Bravo、Yuchen Zhang、Haralambos Mouratidis、Ravi Shekhar、Monorama Swain
**机构**：PUCP、University of Essex（IADS/CSEE）、JKU Linz
**发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.08604 | **PDF**：https://arxiv.org/pdf/2610.08604 | **代码**：未公开（Under Review） | **Demo**：未公开

### 📌 简介
本研究面向语音大模型Speech-LLM ASR的人口学公平问题，提出交集感知修正的群体模型合并方法。以SLAM-ASR为基座，仅在人口学子群数据上微调连接器，再将子群适配器合并为全局模型；接着借助子群WER与任务向量冲突识别关键跨轴人口学对，向全局合并模型注入交集专属修正向量。在Fair-Speech上，TIES加WER修正将总体WER从7.38%降到5.13%，相对降低约30.5%，首次在参数合并层面同时改善聚合精度与交叉群体表现。

### 🔧 技术方案
**问题背景：** ASR在年龄、性别、族裔、社会经济、第一语言等群体上性能不均，且属于多群体的说话人误差最难修复；现有公平方法依赖额外数据、专用损失、显式平衡或适配模块，子群体优化难以迁移到交叉群体。模型合并此前多用于鲁棒性与任务适配，缺少面向人口学与交叉公平的应用。
**方法：** 基座为SLAM-ASR，编码器Whisper-large-v3、语言模型TinyLlama 1.1B均冻结，仅训练线性连接器；在全量训练集得到基座，再在18个人口学子群上分别微调连接器，用五种策略合并：Linear均值、Task Arithmetic缩放1/18、TIES保留Top 20%、Breadcrumbs阈值0.90/0.99、DARE-TIES丢弃20%后合并。
**核心创新：** (1)首次把模型合并与语音大模型的人口学交叉公平连接，无需额外训练数据。(2)用各轴最差子群的WER与子群任务向量余弦相似度（低相似度即高冲突）双准则筛选跨轴候选对，并按融合后的融合惩罚P排序。(3)在两两合并模型上以交集训练集微调得到修正向量δ，经网格搜索系数加回全局模型，构成Method1/2/3三变体。
**协议：** 采用Fair-Speech分层70/15/15划分，五个轴，验证集选对与超参，Rand基线用随机选对三次取均值做对照。

### 📊 实验结果
**数据集**：Fair-Speech（Meta开源命令词数据集，含人口学标注）。
主要指标
- Base总体WER：7.38%；全局合并：6.38–6.77%
- TIES+Method1（WER修正）最优总体WER：5.13%（相对降低30.5%）
- Breadcrumbs+Method3：5.63%
- TIES+M1子群：年龄6.27→4.71、性别6.62→5.26、族裔6.08→4.77
- 选定交集相对WER：TIES+M3 74.80%、Breadcrumbs+M1 77.41%、Linear+M2 70.00%
- 警告：TIES+M1虽降均值，却增大年龄与社会经济两轴的组内差距
**是否开源**：CC BY 4.0许可，正文未附代码与模型链接。

### ⭐ 评分：6/10
理由：选题新颖，首次将模型合并引入语音大模型的人口学交叉公平，方法简洁且复用同一数据即把总体WER降30%；但仅在单数据集、连接器这一小参数子空间验证，交集修正收益高度依赖合并策略且对组内差距存在反作用，开源缺失与命令词场景限制其通用性。
## [14] A Novel Sentence Stress Detection Framework Leveraging Auxiliary Word-Stress Modeling and Loss Optimization

arXiv ID：2610.07626 | **方向**：语音大模型；**作者**：Tien-Hong Lo、Fong-Chun Hsieh、Ting-An Lo、Yu-Hsuan Hsu、Yao-Ting Chen、Berlin Chen；**机构**：台湾师范大学（NTNU）；**发布日期**：2026-10-07 | **论文**：https://arxiv.org/abs/2610.07626 | **PDF**：https://arxiv.org/pdf/2610.07626.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
句子重音（SSD）与词重音（WSD）是自动发音评估（APA）的核心韵律指标，但既有方法大多将两个任务孤立建模，忽视了它们对基频、时长、强度等声学线索的共同依赖。本文提出STRAW框架，在冻结的Whisper骨干上联合建模SSD与辅助WSD，并引入词跨度重音正则器（WSR），解决子词切分导致重音概率在词内扩散的问题。在TinyStress-15K基准上，SSD的F1达0.934，较WhiStress基线提升2.5个点，辅助WSD任务F1为0.920，验证了统一韵律建模板的有效性。

### 🔧 技术方案
**问题背景：** 韵律重音检测分句级与词级两个层次，以往工作各自为政；Whisper子词切分使一个标注为重的词对应多个token，SSD头可能在多个token上都输出高概率，词内重音分配欠约束。
**模型架构：** 骨干为冻结的whisper-small，取编码器与解码器第9层隐状态。SSD分支解码器状态作query、编码器状态作key/value，经一层Transformer解码模块加FCNN对token输出二分类后验；WSD分支以CMU风格G2P音素序列的嵌入作query，与编码器状态做交叉注意力，再由FCNN输出音素级重音二分类。仅训练两个任务头与音素嵌入层，骨干参数全部冻结。
**核心创新：** (1) 统一框架：同一冻结Whisper骨干同时支撑句级SSD与词级WSD两条任务特定分支，共享韵律表征；(2) WSR正则：对每个标注重音词的子词跨度，用ω(w)=|1−Σp|度量跨度内概率和偏离1的程度作权重，将argmax位置的token概率推向1并抑制跨度内其余token，实现词内重音锐化；(3) 联合优化：总损失为α·L_SSD+β·L_WSD+λ·L_WSR，实验中α=β=λ=1.0。
**训练策略：** AdamW优化器，批大小16，初始学习率1e-4，训练20个epoch，单张RTX 3090；以验证集SSD二值F1最优选择checkpoint。训练集13,500句、171,206个token（含22,537个重音token），验证1,500句、测试1,000句。推理时直接利用参考文本的Whisper token与G2P音素序列，无需额外ASR过程，WSD分支可选关闭。

### 📊 实验结果
**数据集**：TinyStress-15K（合成语音，沿用官方划分并留出10%训练数据作验证集）
主要指标
- SSD F1：STRAW 0.934（精确率0.945/召回率0.924），对比WhiStress 0.909、GT对齐BLSTM 0.858、MFA对齐BLSTM 0.815
- 消融：去WSD降为0.922，去WSR降为0.929，两者全而去0.915，完整配置最优
- WSD F1：STRAW 0.920（精确率0.924/召回率0.916），去WSR仅微变至0.921
- 词性误差分析：功能词（PART、DET、AUX、ADP）漏检率下降，误检率保持低位
**是否开源**：代码未开源，仅使用公开的whisper-small预训练模型与G2P工具

### ⭐ 评分：5/10
词跨度正则动机清楚、消融完整，句重音F1较最强基线提升2.5个点，结果可信。但贡献偏增量：训练与评测仅限定15k合成语料，未验证真人自发语音；骨干冻结且两分支参数独立，作者自认未证明WSD对SSD的知识迁移；无代码发布影响复现，整体为一篇小而稳的方向性短文。

---

## [2] 语音前端

## [15] Audiovisual Joint Learning for End-to-End Hearing Aids
arXiv ID：2610.08579 | **方向**：语音前端
**作者**：You-Jin Li, Yu Tsao, Borching Su, Kuan-Chung Ting, Fan-Gang Zeng
**机构**：台湾大学、中研院信息创新研究所、台北荣民总医院、阳明交通大学、加州大学尔湾分校
**发布日期**：2026-10-07
**论文**：https://arxiv.org/abs/2610.08579 | **PDF**：https://arxiv.org/pdf/2610.08579 | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文提出AV-NeuroAMP，首个把视听语音增强与神经听力损失补偿统一为端到端框架的助听器方法。模型同时输入带噪语音、目标说话人脸视频与听者纯音测听图，联合完成降噪、个性化放大与动态范围压缩，直接优化听者特定的最终输出，规避传统两级级联带来的误差传递。视觉线索为竞争说话人场景提供互补的发音信息，正是纯音频方案难以获得的增益来源。论文还提出AC-FiLM听图条件化调制，并在英语域内与普通话域外噪声条件下均显著领先。

### 🔧 技术方案
**问题背景：** 现有助听器普遍将语音增强与听力损失补偿分两级串联，增强阶段的残留干扰、失真与电平偏差会被放大级继续继承；纯音频增强在面对竞争说话人时，因目标语与干扰语声学特征高度相似而难以有效分离。

**模型架构：** 在音频版NeuroAMP基础上扩展为AV-NeuroAMP，以AVMamba为双路骨干，同时估计目标幅度与相位，融合三路输入：带噪语音y、目标说话人视频v、测听图a（250–6000Hz共六频点阈值）。视觉侧由冻结的ResNet-18人脸抽取器与可训练TCN适配器构成，输出与频谱特征对齐后融合。

**核心创新：** (1)端到端联合完成增强、个性化NAL-R放大与WDRC动态范围压缩，直接以处理后的干净目标语音为优化终态，杜绝级联误差；(2)AC-FiLM含局部频点相关与全局共享两条分支，在instance norm之后再施加乘性缩放与加性偏移，避免听图信息被归一化抹平；(3)采用sigmoid门控的零初始化残差连接，自适应控制注入强度，仅21824可训练参数、GMAC开销小于0.01。

**训练策略：** 16kHz采样、512点STFT、128跳步、0.3幂律压缩，随机裁剪2秒同步音视频段；AdamW，初始lr为5e-4并每epoch按0.99指数衰减，全局batch 16，4张H100训练200 epoch。总损失由一致性、时域、幅度、复谱、相位五项加权，系数0.1、0.2、0.9、0.1、0.3。

### 📊 实验结果
**数据集**：训练与域内评测用AVSEC-2（源自LRS3，34524音视频对、605目标/405干扰说话人、13.8万带听图训练对）；听图取自Clarity Challenge（166训练/106测试耳）；域外泛化与主观听音用台湾普通话TMSV（240句，竞争语/粉噪/babble/引擎/街道噪声，SNR 8/5/2/−1/−4 dB，6000样本）。基线含Conventional、Two-stage(A)、Twostage(AV)、NeuroAMP。
主要指标：
- HASPI（可懂度，域内噪声）：AV-NeuroAMP 0.780，NeuroAMP 0.419，Conventional 0.449
- HASQI（质量，域内噪声）：0.625，对比0.268与0.283
- MBGE多频带短时增益误差：3.48 dB，NeuroAMP为11.30 dB
- MSE：1.1e-3，NeuroAMP为2.6e-2；目标参考SNR：10.20 dB，NeuroAMP为−2.98 dB
- 域外普通话噪声：HASPI 0.598、HASQI 0.454，仍全面领先
- 主观听音竞争语（听损用户12人20耳）：质量2.05/1.68/1.37，可懂度0.264/0.167/0.027，差异均显著
AC-FiLM消融在全部五项指标上优于直接拼接听图。**是否开源**：暂无自有代码与Demo释放。

### ⭐ 评分：8/10
视听端到端神经放大为该方向首创，AC-FiLM设计针对性强且有干净消融佐证，新指标MBGE贴合助听多频带增益评估，英语到普通话跨语言泛化稳健，并同时跑了正常听力模拟与真实听损用户的主观实验，证据链完整。扣分在于目标依赖线性NAL-R处方而非主流非线性、仅单耳评测、假设视频始终对应目标说话人，落地多人与双耳场景仍待验证。

### [16] Where Does the Audio Jailbreak Live? A Controlled Frequency-Depth Audit of AdvWave-P on Qwen2-Audio
- **arXiv ID**：2610.07005 | **方向**：语音大模型 | **评分**：6/10（未精读，按摘要评分）
- 频率-深度受控审计定位 Qwen2-Audio 音频越狱攻击面
- **论文**：https://arxiv.org/abs/2610.07005 | **PDF**：https://arxiv.org/pdf/2610.07005.pdf | **代码**：暂无 | **Demo**：暂无

### [17] Pronunciation-Oriented Reinforcement Learning for Japanese Text-to-Speech with Kana-Domain ASR Rewards
- **arXiv ID**：2610.07575 | **方向**：语音大模型 | **评分**：6/10（未精读，按摘要评分）
- 假名域 ASR 奖励的日语 TTS 发音导向强化学习
- **论文**：https://arxiv.org/abs/2610.07575 | **PDF**：https://arxiv.org/pdf/2610.07575.pdf | **代码**：暂无 | **Demo**：暂无

### [18] HINTT Submission to the 2nd MLC-SLM Challenge: Comparing Cascaded and Unified Approaches to Diarized ASR
- **arXiv ID**：2610.08063 | **方向**：语音大模型 | **评分**：6/10（未精读，按摘要评分）
- MLC-SLM2 挑战赛：级联与统一路线的 diarized ASR 系统对比
- **论文**：https://arxiv.org/abs/2610.08063 | **PDF**：https://arxiv.org/pdf/2610.08063.pdf | **代码**：暂无 | **Demo**：暂无

### [19] SEAL: Mixture-Closed Additive Reconstruction and Refinement-Aware Expert Routing for Efficient Speech Enhancement
- **arXiv ID**：2610.07047 | **方向**：语音前端 | **评分**：6/10（未精读，按摘要评分）
- 混合闭合加性重构+精炼感知专家路由的高效语音增强
- **论文**：https://arxiv.org/abs/2610.07047 | **PDF**：https://arxiv.org/pdf/2610.07047.pdf | **代码**：暂无 | **Demo**：暂无

### [20] Loud and Clear: Dynamic Activation Steering for Improving Speech Intelligibility in Noisy Environments
- **arXiv ID**：2610.07647 | **方向**：语音前端 | **评分**：6/10（未精读，按摘要评分）
- 模型内动态激活引导提升噪声环境可懂度（非前端信号处理）
- **论文**：https://arxiv.org/abs/2610.07647 | **PDF**：https://arxiv.org/pdf/2610.07647.pdf | **代码**：暂无 | **Demo**：暂无

### [21] AccentCL: Robust Accent Classification with Incremental Expansion
- **arXiv ID**：2610.07426 | **方向**：语音前端 | **评分**：6/10（未精读，按摘要评分）
- 增量类别扩容实现开放集口音分类
- **论文**：https://arxiv.org/abs/2610.07426 | **PDF**：https://arxiv.org/pdf/2610.07426.pdf | **代码**：暂无 | **Demo**：暂无

### [22] GIVE-KWS: Gated Injection of Visual Evidence for Noise-Robust Query-by-Example Keyword Spotting
- **arXiv ID**：2610.07046 | **方向**：语音前端 | **评分**：5/10（未精读，按摘要评分）
- 门控注入视觉证据的噪声鲁棒 QbE 关键词唤醒
- **论文**：https://arxiv.org/abs/2610.07046 | **PDF**：https://arxiv.org/pdf/2610.07046.pdf | **代码**：暂无 | **Demo**：暂无

### [23] WavePrune: One period is often enough for RoPE
- **arXiv ID**：2610.06963 | **方向**：语音前端 | **评分**：5/10（未精读，按摘要评分）
- RoPE 波形任务单周期位置编码剪枝
- **论文**：https://arxiv.org/abs/2610.06963 | **PDF**：https://arxiv.org/pdf/2610.06963.pdf | **代码**：暂无 | **Demo**：暂无

### [24] Feature Encoding in VAE-based Audio Decoders: Effects of Input, Depth and Distribution
- **arXiv ID**：2610.07966 | **方向**：语音前端 | **评分**：5/10（未精读，按摘要评分）
- VAE 音频解码器特征编码的输入/深度/分布消融研究
- **论文**：https://arxiv.org/abs/2610.07966 | **PDF**：https://arxiv.org/pdf/2610.07966.pdf | **代码**：暂无 | **Demo**：暂无

---

*Generated on 2026-10-07*
