# 2026-09-30 语音论文速递

**共收录**: 36 篇 | **语音大模型**: 34 篇 | **语音前端**: 2 篇

> 目标日期 2026-09-30（/new 页头批次日期，北京时间 09-30 上午公告）arXiv 语音相关论文共命中 36 篇（另剔除音乐/生物声学/临床声学/纯时延估计相邻的 8 篇后）。
> 以下是按评分排序的结果（前 15 篇完整精读，其余仅列标题、arXiv ID、评分与链接）。

---

## 语音大模型

## [1] WenetSpeech-Min: A Large-Scale Minnan Speech Corpus with Dual Transcriptions for Dialectal Speech Processing

arXiv ID：2609.36834 | 方向：语音大模型
作者：Haoyu Zhang、Chunjiang He（共同一作）、Hongtao Li、Zeyu Zhu、Shuai Wang、Binbin Zhang、Pengcheng Zhu、Lei Xie（通讯）等20人
机构：西北工业大学ASLP@NPU、南京大学、新南威尔士大学、WeNet开源社区、Moonstep AI、Nexdata、厦门大学
发布日期：2026-09-30 | 论文 https://arxiv.org/abs/2609.36834 | PDF https://arxiv.org/pdf/2609.36834.pdf | 代码/Demo：https://aslp-lab.github.io/WenetSpeech-Min-Repo/

### 📌 简介
闽南语长期缺乏大规模真实场景、同时配对"方言转写+书面普通话转写"的语料。本文发布WenetSpeech-Min：约10,000小时多源在线媒体闽南语音库，每条话语均配对闽南语方言转写与普通话转写双文本；并建立覆盖双转写目标的ASR基准（6小时人工校验）与闽南语TTS基准（Easy 500句+Hard 250句），配套发布在语料上微调的Qwen3-ASR、FireRedASR2、CosyVoice3系列模型，填补闽南语规模化开放数据与可复现评测的双重空白。

### 🔧 技术方案
**问题背景：** 闽南语覆盖福建、台湾及东南亚，但公开资源稀少：Common Voice仅小规模朗读语料，MinSpeech数千小时只有普通话转写，YT-THDC有方言-普通话配对却仅30小时，Breeze Taigi评测集不公开，跨模型公平比较与可复现评测缺失。

**数据管线：** 采集多源媒体音频后VAD切分，以SNR、时长计算WV-MOS声学质量分，经DaSheng事件检测过滤非语音、pyannote估计说话人数作元数据；用1,600小时人工闽南语转写分别微调Qwen3-ASR、FireRedASR2-AED、Fun-ASR-Nano作三个互补标注器，ROVER融合生成方言转写；有内嵌字幕的媒体用WeSubtitle提取OCR文本作普通话转写，否则用600小时双语文本LoRA微调的Qwen3-8B翻译模型生成。

**核心创新：** (1)首个万小时级真实闽南语双转写语料，含5,121,249条话语；(2)全自动异构媒体双转写生成管线，字幕直通与机器翻译双路径互补；(3)成对转写ASR基准同音频评两个目标，报D-CER、M-CER、M-BLEU，TTS基准含长文、重复句、绕口令的Hard子集及23名母语者主观评测。

**基准实验：** Qwen3-ASR分别微调出闽南版与普通话版；FireRedASR2-AED用两个可学习任务嵌入实现单模型双输出；CosyVoice3-WSM先单说话人CPT、再筛1,000小时高质量数据SFT、最后以CER/SIM构造偏好对做DPO。

### 📊 实验结果
**数据集**：约10,000小时，512万条话语，均值7.24秒，SNR时长加权均值21.3dB；域分布：剧集54.7%、有声书19.8%、娱乐13.9%
- 闽南转写D-CER：Qwen3-ASR-WSM-Min 17.59%，加内部数据15.21%，优于商业Hy-ASR-3.0的32.78%
- 普通话转写：WSM-Mandarin+内部数据平均M-CER 33.05%、M-BLEU 54.24，逼近SeedASR2.0的54.25
- TTS：CosyVoice3-WSM Easy子集CER 20.26%（基座63.69%）、Hard 35.98%（基座60.35%），开源系统中I-MOS最高，但SIM 0.678低于FireRedTTS3的0.747
**是否开源**：语料、基准与模型将发布；约1,500小时音频缺乏来源记录，存档电视剧子集WV-MOS仅1.09

### ⭐ 评分：8/10
万小时双转写填补闽南语核心数据瓶颈，管线工程完整，微调模型全面超越开源基线并逼近商业系统，开放可复现评测贡献突出；扣分在方言-普通话非逐词对齐致跨基准指标不可比、部分老素材声学质量偏低、TTS说话人相似度仍逊于竞品。
## [2] MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation

arXiv ID：2609.36903 | 方向：语音大模型
作者：Ke Wang、Houxing Ren、Zimu Lu、Yunqiao Yang、Zhuofan Zong、Mingjie Zhan、Hongsheng Li
机构：CUHK MMLab、CPII under InnoHK（NeurIPS 2026）
发布日期：2026-09-30 | 论文 https://arxiv.org/abs/2609.36903 | PDF https://arxiv.org/pdf/2609.36903.pdf | 代码：https://huggingface.co/datasets/MultiTalk/MultiTalkPT | Demo：暂无

### 📌 简介
现有端到端全双工语音模型受数据与评测双重瓶颈制约，难以支撑长时、多方、双语并存的真实会话（如会议、机器人接待）。MultiTalk沿长时序与多方两轴联合扩展Moshi范式：发布57.6k小时英中合成全双工并行流语料（MultiTalkPT 54.4k小时+MultiTalkFT 3.2k小时）及自动数据引擎；基于真实人类录音构建MultiTalkBench（104条、平均32.6分钟）；训练双语Moshi风格模型Moshi-MTB，最终得分13.15，超过开源最强MiniCPM-o-4.5（11.05），相对骨干提升182.2%，中文得分更从0.36跃升至16.27。

### 🔧 技术方案
**问题背景：** 开源多方会话语料合计仅约400小时且未按codec帧级全双工建模设计；长音频基准偏被动聆听，语音对话基准多为二方短会话，单一模型无法跨多说话人完成感知、归属、长程上下文跟踪与受话人选择。
**模型架构：** 完全沿用Moshi双流Mimi codec与RQ-Transformer，从公开moshiko-pytorch-bf16检查点初始化；非目标说话人混入用户通道，新增用户音频流预测目标，并保留Inner Monologue文本头与词级对齐；架构零修改，能力增量纯靠数据构成。
**核心创新：** (1) 自动数据引擎：两次LLM调用先固定场景与角色档（2-9人、50-300轮、每轮附情感/强度/语速/音量/方言五维TTS控制向量），再经JSON/长度/封闭度/内容四层质量过滤；IndexTTS2按句合成并用对话级音色抽取防止捷径，多通道装配后将间隙压至0.2-0.6秒（打断处1-2秒）制造真实重叠，MFA词级强制对齐。(2) MultiTalkBench：复用AMI、CHiME-6、AISHELL-4等真实语料测试集，按通用、多方IQ、四角色条件与参与率span比四组维度LLM-as-Judge打分。(3) 双语两阶段配方：先以约60%英/40%中采样预训练，再仅用多方语料继续训练以集中容量习得cross-talk。
**训练策略：** 全参数AdamW加one-cycle调度，全局批量21小时音频；预训练5000步峰值学习率3e-5，微调200步时temporal/depth transform分别降至2e-6/4e-6；首个codebook损失乘100，用户流权重0.5并500步线性预热，用户通道在线混合DNS-Challenge噪声增强鲁棒。

### 📊 实验结果
**数据集**：训练用MultiTalkPT（54.4k小时）与MultiTalkFT（3.2k小时）；评测用MultiTalkBench（104样本、56.5小时、平均32.6分钟）
- 最终得分：Moshi-MTB 13.15 vs MiniCPM-o-4.5 11.05、Moshiko-7B 4.66、Qwen3-Omni-30B 4.94、PersonaPlex-7B 2.52（人类参考68.74）
- 多方IQ：8.56（骨干2.41、+255.2%），说话人追踪14.56、群体感知15.80、噪声抵抗12.77均领先MiniCPM-o-4.5
- 双语：中文0.36→16.27约45倍、英文7.82→10.87（+39%）
- 交互行为：响应延迟870ms、停止延迟2230ms、附和延续率94.1%、旁谈忽略率98.8%
- 数据消融：多方占比0→100%使总分7.95→13.15，且收益可迁移至F-Actor（6.94→15.16）；LLM评审与人类Spearman相关ρ≥0.84
**是否开源**：数据引擎、两个语料与MultiTalkBench均发布于HuggingFace（CC BY 4.0），论文已被NeurIPS 2026接收

### ⭐ 评分：8/10
首个把长时、多方、双语三个难解轴同时落地的全双工工作：57.6k小时开源语料较此前全部公开多方会话语料总和无复量级跃升，基准取自真实录音且评审可信度经人工校验，模型在完全不动架构下取得可测增益并超开源基线。不足在于无方法层面创新、绝对得分仍距人类甚远、长时结论主要依赖离线评判，属实质性强贡献。
## [3] HEAR: Real Voices, Real Bias: A Large-Scale Human-Recorded, Demographically Diverse Benchmark for Audio Language Models

arXiv ID：2609.35952 | 方向：语音大模型
作者：Shen Yan、Duc Le、Irina-Elena Veliche
机构：Meta Superintelligence Labs
发布日期：2026-09-30 | 论文 https://arxiv.org/abs/2609.35952 | PDF https://arxiv.org/pdf/2609.35952.pdf | 代码/Demo：https://github.com/facebookresearch/hear_voice_bias_benchmark

### 📌 简介
Meta 推出 HEAR，是首个完全基于真实人声（非 TTS 合成）的大规模 Audio-LLM 人口统计偏见评测基准，含 87k 条真人录音、843 名人口多样性的美国参与者，覆盖性别、年龄、母语等维度。任务分 Spoken BBQ 多选题与开放式长回答两类，同时评测端到端 speech-to-speech 与 speech-to-text 两种架构。结果揭示语音条件偏见是模型特有属性，个性化系统指令会系统性加剧人口差异，为 Audio-LLM 偏见度量与后续缓解提供了基础框架与可复现数据。

### 🔧 技术方案
**问题背景：**文本 LLM 偏见评测（如 BBQ）已较成熟，但 Audio-LLM 不仅听到内容，还听到说话的声音，副语言与声学线索会在与任务无关处影响推理与建议。既有语音偏见基准多依赖 TTS 合成音，生态效度低、规模有限，且没有同时覆盖语音到语音与语音到文本两类架构的工作。
**构建方法：**在美国招募 843 名人口多样性成年参与者，签署公开授权后通过手机 App 在家按脚本录音，共得 87k 条唯一样本；任务一是将 BBQ 歧义语境配负向/非负向问句口语化的 Spoken BBQ（MCQA），任务二是职业建议、生活推荐等手写开放式 QA。
**核心创新：**(1) 首个 100% 真实人声、非合成的规模化语音偏见基准；(2) 提出细粒度指标：内容侧 SIR（说话人归因率，测谄媚）与 FR（换参照方翻转率），声学侧 VCD（否定/肯定框架下两人群回答一致性之差）与 DMD（说话人与参照方人口匹配与否的敏感度差）；(3) 统一评测 GPT-Realtime、Gemini-Realtime 与 Qwen3-Omni-30B-A3B、Gemma4-E4B 共 4 个模型，并对比默认与个性化两类系统指令。
**评测协议：**同一语境仅改动问句框架或说话人 demographics，统计回答类别（说话人/参照方/无法判断）分布；用 Mann-Whitney U 检验指标分布显著性；开放式回答以卡方检验得 DDR 分布差异率，同时计算有用率防止用泛泛而谈掩盖差异；个性化指令要求模型先分析说话人人口特征再作答。

### 📊 实验结果
**数据集**：HEAR（87k 真实人声、843 人，英语为主、含非母语组），Spoken BBQ MCQA 与开放式 QA 双任务。
- VCD(Female,Male)：Qwen-Omni 默认 26.34%，GPT-Realtime 默认 18.42%，Gemini-Realtime 默认仅 12.57%（全模型中最低）
- DMD(Age)：GPT-Realtime 默认 -12.73%，Qwen-Omni 个性化 -25.47%
- SIR 非负向题：Qwen-Omni 27.01% 最高，Gemini-Realtime 6.05% 最低，所有模型非负向 SIR 高于负向，显示谄媚倾向
- Open QA DDR：Qwen-Omni 个性化指令下达 54%（默认 22%），有用率随之从 76.85% 降至 68.76%
- 规律：各模型对男性、年轻、母语英语说话人回答更稳定；Spoken BBQ 中个性化指令普遍放大人口差异
**是否开源**：是，数据集与基准代码已在 GitHub 开源，许可 CC BY-NC-SA 4.0，录音均有书面知情同意。

### ⭐ 评分：8/10
以真实人声填补了语音偏见基准生态效度的空白，87k 样本与 843 人规模显著超越既有 TTS 合成工作；指标体系区分内容与声学两条路径，SIR/VCD/DMD/DDR 设计清晰且配有统计检验；同时覆盖 S2S 与 S2T 并量化个性化指令风险，结论对工业部署有直接指导意义。扣分在于：仅英语与美国受试限制泛化，只评 4 个模型且两个为闭源 API 难以复现，止步于度量未给出缓解方案，开放 QA 手写 prompt 覆盖面较窄。
## [4] Learning as Deepfakes Evolve: RF-Prompt for Continual Audio Deepfake Detection

**arXiv ID**：2609.37586 | **方向**：语音大模型
**作者**：Yuankun Xie、Xiaoxuan Guo、Xiaopeng Wang、Siqing Qin、Shaole Li、Kong Aik Lee
**机构**：香港理工大学、中国传媒大学、北京理工大学
**发布日期**：2026-09-30 | **论文** https://arxiv.org/abs/2609.37586 | **PDF** https://arxiv.org/pdf/2609.37586.pdf | **代码**：https://github.com/xieyuankun/RF-Prompt | **Demo**：论文未提供公开演示页面，开源代码库即为验证入口

### 📌 简介
语音生成系统（Qwen3-TTS、Seed-TTS、GPT-Live、Gemini Live 等）以周或月为周期快速迭代，部署后的音频深伪检测器面对的是持续移动的靶标：必须在不遗忘历史真伪知识的前提下纳入新出现的伪造方法。现有持续学习评测普遍按数据集组织任务，把真实语音域变化与伪造机制变化耦合在一起，难以分辨究竟在更新何种知识。本文从任务组织与检测器自适应两个维度联合入手：提出真实锚定机制增量协议 RAMI，以复现的混合域真实语音为背景、按生成机制增量组织假语音任务；并提出 RF-Prompt 非对称持续提示学习方法，用被余弦锚定保护的共享真实提示与随任务扩展的虚假专家库适配新知识，输入自适应融合使推理时无需任务身份。在 RAMI 上取得 10.110% 平均 EER 与 10.370% 池化 EER，为所有持续学习方法中最低。

### 🔧 技术方案
问题背景：持续音频深伪检测的输出类别始终为真与假两类，演化的是类别内部的伪造分布，这与传统类增量识别本质不同。DFWF、RAWM、RWM、RegO 等方法虽在更新约束上各有设计，但任务按数据集边界切分，而不同数据集可能共享生成机制、单个数据集也可包含多个机制，导致真实域漂移与伪造机制演进的影响无法解耦。
方法：作者先从完全相同的训练、开发、评估样本池构造五种任务组织协议，交叉控制真实语音到达方式与假语音组织方式；其中 RAMI（协议 5）每个任务提供四个已知域各 600 条全新真实语音与单一机制的 2400 条假语音。检测器侧，RF-Prompt 冻结 24 层 XLS-R 300M 主干，每层注入 5 个共享真实提示 token 与 5 个虚假提示 token，经可训练 AASIST 后端输出二分类 logits。
核心创新：（1）RAMI 协议首次把"复用已有真实语音知识、增量学习新伪造机制"的真实更新场景显式化为可控基准，五种协议在同预算下对比，证明机制组织方式直接影响持续学习效率。（2）非对称提示容量分配：真实知识写入可持续训练但受参数级余弦锚定约束的共享提示，无需保留历史音频或教师前向；假知识写入随任务增长并冻结的专家库，二者天然对应真实紧凑、伪造多样的先验。（3）继承加正交残差学习：新专家按当前任务假语音查询与历史专家向量的余弦相似度选继承基，仅学习被软正交正则约束在历史残差补空间的残差；推理时按样本相似度对所有专家做温度 softmax 加权融合，注入长度固定为 10，专家库增长不增加提示序列。
训练策略：每任务 50 epoch、批量 32、Adam 加余弦学习率，检查点按本任务开发集 EER 选择；总损失为 BCE 加 λreal=1 的锚定项与 λorth=0.1 的正交项，融合温度 τ=0.1；全部实验使用单一种子 2026。

### 📊 实验结果
数据集：ASVspoof 2019 LA、ASVspoof 5 Track 1、CodecFake、AT-ADD Track 2  clean 子集；训练与开发池各含 9600 真与 9600 假，评估池各 20000，五协议共享 19200/19200/40000 总量。主干为 XLS-R 300M 加 AASIST。
主要指标（RAMI，最终检查点）：
- 平均 EER：10.110%，优于 SinglePrompt 11.665%、RAWM 11.295%、EWC 12.255%、Sequential 13.130%
- 池化 EER：10.370%，较最强提示基线 SinglePrompt 12.105% 低 1.735%，与离线联合训练 9.420% 仅差 0.950%
- 平均遗忘 AF：4.560%，低于 Sequential 6.433% 与 RAWM 5.753%
- 机制级保留：学完四任务后 M1 10.40%、M3 13.12%，均优于 Sequential 的 14.50% 与 18.78%
- 协议对比：RAMI 公共平均 10.110%，显著优于数据集组织的协议 1（16.400%）与协议 2（15.675%）
- 组件消融：去除残差正交损失池化 EER 升至 12.805%（最大退化），去除自适应融合升至 12.480%，去除余弦锚定升至 11.365%
- 低资源：每任务仅 100 条假语音时池化 EER 12.375%，对比最强基线 17.645%
- 跨主干：XLS-R 1B 与 2B 池化 EER 达 9.570% 与 9.550%，W2V-BERT 2.0 为 10.040%，对 Sequential 全面占优
开源情况：代码已开源，含协议构造与训练实现；未提供在线 Demo，论文中 AI 仅用于写作润色。

### ⭐ 评分：8/10
理由：本文最大价值在于把任务组织提升为与算法同级的研究对象，RAMI 的五协议控制变量设计对社区有基准级贡献；非对称提示分配精准契合真实语音紧凑可复用、伪造机制多样需扩展的先验，且免历史数据重放、免蒸馏前向，参数效率高，五个维度（基线对比、协议、消融、低资源、跨主干）验证充分。不足：全部结果仅单一种子、无显著性检验，任务序列只有 4 步较短，M3 神经编解码重建类仍是薄弱环节（13.12%），对更长序列与真正未见生成器的泛化尚未验证，余弦锚定属软约束而无结构保证。
## [5] Almost Human, Except When It Matters: VoxParity and the Decisions a Voice Should Change

arXiv ID：2609.35922
方向：语音大模型
作者：Bhavik Mangla
机构：独立研究者（Independent Research）
发布日期：2026-09-30
论文：https://arxiv.org/abs/2609.35922
PDF：https://arxiv.org/pdf/2609.35922.pdf
代码/Demo：https://github.com/bhavik-mangla/voxparity-bench（Zenodo 存档 doi:10.5281/zenodo.23008159）

### 📌 简介

语音智能体已在真实电话线中执行转账、药品续方、关停服务、紧急派发等动作，而急救调度、反电诈、民航话务、赌博年龄核验等行业规范均承认：来电者"听起来如何"可以改变正确动作。VoxParity 是针对此盲区的基准：同一转写文本保持不变，只改变声音（哭泣、监护仪报警、背景中的 Mayday、儿童嗓音、噪声掩盖药名），正确的工具调用随之翻转。它以纯文本管线作对照零假设，检验模型是否真正因"听见"而改变决策，并揭示系统性偏见——当声音要求保护时，几乎所有智能体仍偏执行字面请求，甚至识别到线索也不行动。

### 🔧 技术方案

**问题背景：** ASR 转写几乎丢失全部副语言信息：论文实测 Whisper 在 150 条以语气、不流畅、说话人身份为线索的通话上未向文本传递任何线索，丢弃 36 条第二人称声源中的 35 条、13 条环境事件中的 11 条；纯文本智能体能处理普通呼叫，却恰好在规则为其而写的场景违规。
**方法：** 构建 183 个场景，覆盖催收、银行、航空海事、医疗、公用事业、博彩、应急等 14 个行业，含 7 类可听线索（情感语气 93 项、第二声源 32 项、不流畅或静默 12 项、环境声 11 项、说话人年龄 9 项、掩蔽词 7 项、反讽 8 项）加通道对照。每场景一条固定文本渲染为多个仅声音不同的变体，各配可翻转的黄金带类型工具调用、部分学分备选动作与强迫选择感知探针，用无裁判的确定性匹配器打分，菜单逐题乱序防位置策略。
**核心创新：** (1) 提出"纯文本零假设"检验：对同一批单元做双重差分，音频版动作变化减去转写版变化须超过纯文本级联的基线才判"因听而动"；(2) 最小对比集设计使黄金动作在 132 个双变体可运行场景中 130 个发生翻转，测的是执行动作而非感知；(3) 引入约 20 名志愿玩家在同一音频同一菜单上操作作为人类参照。
**协议：** 28 个音频原生系统（11 家厂商）于 2026-09-15 至 25 在冻结题库上经同一管线与评分器评测：13 个文件模式 API、9 个生产实时智能体、6 个本地开源权重；统计用按场景聚类的 95% bootstrap 区间与 Holm 修正。

### 📊 实验结果

**数据集**：VoxParity 冻结题库（309 个计分子单元、206 个含线索单元；主用 Gemini-TTS 合成音频，另有作者 49 条真人录音与第二引擎作稳健性复现；开发子集 40 项/81 单元随代码发布）。
主要指标：
- 零假设通过：23 个有文本路径的系统中仅 11 个通过，7 个可测生产实时智能体只有 1 个；28 系统中位数得分 0.34，与纯文本级联持平
- 榜首线索得分：gemini-3.7-flash 0.57、Qwen3.8-Omni 0.56、MiMo-V2.6-Pro 0.56，人类玩家 0.61
- 保护性偏误：全套 28 系统在保护性呼叫上执行字面请求 41% 对净呼叫过度触发 12%；四强为 34% 对 18%
- 听到后的决策：对急性惊恐仅 6% 取字面动作，对平静状态达 52%
- 瓶颈定位：完美听觉仅加 0.04 学分，完美决策加 0.28；提示中加声音描述加规则后 gemini-3.7-flash 未陈述规则情感题从 0.40 升至 0.83；带描述的纯文本模型达 0.76，高于一切无辅助音频系统（至多 0.57）
**是否开源**：评测框架、无裁判评分器与生成脚本以 Apache-2.0 发布并 Zenodo 存档，开发子集含音频 CC BY 4.0；其余 143 题持出以避污染，附金丝雀字符串与逐项 SHA-256 哈希。

### ⭐ 评分：8/10

首创在"可执行工具调用"层面用无裁判、零假设对照量化智能体是否依据声音改变决策，统计严谨、14 行业规范锚定黄金答案，对人类参照与污染防护到位，对语音智能体安全落地与审计采购有直接价值，且"听而不动"的结论与失败地图（陈述规则、描述语音两个杠杆）可操作。扣分点：情感刺激几乎依赖单一合成引擎与单一音色，真人验证线索子集上表现明显下滑；单人独立作者、多数深层分析为探索性事后分析，榜单对厂商与代际组合敏感。
## [6] FD-VAD: Semantic Endpoint Detection for Streaming Full-Duplex Speech

arXiv ID：2609.35791 | 方向：语音大模型
作者：Puneet Mathur、Dinesh Manocha
机构：University of Maryland, College Park
发布日期：2026-09-30
论文：https://arxiv.org/abs/2609.35791
PDF：https://arxiv.org/pdf/2609.35791.pdf
代码/Demo：https://fd-vad.github.io/

### 📌 简介

全双工流式语音交互需要从partial语音判断暂停是犹豫还是语义完整，传统声学VAD只能检测静音、无法感知语义完整性，而ASR级联方案又引入转录错误与额外延迟。本文将语义端点检测重构为因果音频-语言推理任务，提出FD-VAD：一个免ASR的流式endpointer，把有界因果音频窗口直接映射为Continue/Stop决策，以语义端点检测取代声学VAD。模型由冻结语音编码器、轻量模态适配器与参数高效微调语言模型组成，配合置信度门控提交与边界难例采样。域内语句级准确率0.976，TurnBench dev零样本下FP≤0.10时EOT召回0.853居首，证明无需中间ASR或对话状态跟踪即可完成语义端点判断。

### 🔧 技术方案

**问题背景：** 全双工语音代理中端点误差是非对称的：过早Stop会打断用户，保守决策只增加延迟。声学VAD如Silero误判犹豫停顿，chunk级false-stop率高达22.5%；Whisper+TEN级联整体语句准确仅0.800且无法流式。端点判断本质是语义问题，且必须在因果partial音频下持续更新。

**模型架构：** 冻结WavLM-base-plus将2.56秒因果音频窗口编码为50Hz约128帧特征；两层线性ReLU适配器按每4帧聚合降采样为12.5Hz约32个音频token，与指令prompt拼接后输入Qwen2.5-0.5B-Instruct，输出Continue/Stop状态token。仅训练适配器与LoRA(r=16)参数，共1030万可训练参数（占总参数1.7%）。

**核心创新：** (1) 音频到LLM决策的端到端流式语义端点检测，去除转录、CTC或 silence 触发等中间机制，独立于下游对话代理；(2) 置信度门控端点提交，仅当连续K次P(Stop)≥τ才提交，显式控制中断-延迟权衡；(3) 边界聚焦难负例采样，过采样真实端点±2chunk内的窗口，推理结构不变而边界决策更准。

**训练策略：** 在smart-turn-v3.1英文子集63,386条（31,338完整/32,048不完整，约156小时，42,529人录+20,857条TTS）上训练1个epoch，AdamW学习率2e-4、余弦衰减、3%warmup、有效batch 64、bf16、双A100；采用last-chunk目标仅监督每窗口最后一个chunk，推理以320ms步长在10ms切片网格增量预测，固定成本。

### 📊 实验结果

**数据集**：smart-turn-v3.1英文官方划分留测1,000条（500完整/500不完整，中位时长9.1s）做域内评测；TurnBench dev真实双通道对话做零样本EOT迁移；三随机种子取均值。

主要指标：
- Chunk级F1：0.832（Silero VAD 0.251、WavLM-large causal 0.191、VAP 0.279）
- Chunk false-stop率：0.6%（Silero 22.5%、VAP 20.1%）
- 语句级总体准确率：0.976，完整/不完整0.972/0.969；对比非流式Smart Turn 0.965、UltraVAD 0.880、Whisper+TEN 0.800
- TurnBench零样本EOT recall：0.853（FP≤0.10限定系统最高），中位提交延迟1019ms，VAP为84.1%召回/463ms
- 每2.56s窗口推理45.8ms（p90 46.8ms），延迟不随语音时长增长；τ=0.9、K=1时端点延迟中位190ms、误中断率2.0%
- 消融：边界采样使near-boundary F1升至0.880、strict句准确0.476；冻结适配器全指标下降，纯TTS训练在人类语音 utterance 级退化

**是否开源**：代码与模型经fd-vad.github.io发布，训练数据为开源pipecat smart-turn-v3.1语料。

### ⭐ 评分：7/10

问题定位精准、工程闭环完整：last-chunk流式监督、置信度门控与边界采样均有部署价值，以1.7%可训练参数在域内与零样本上全面超越声学及级联基线，单窗口45.8ms成本恒定。不足在于编码器-适配器-LLM架构本身新意有限，评测以英文孤立句和单一对话基准为主，TurnBench延迟不占优，多语言、噪声与真实车载场景泛化有待验证。
## [7] Louder, Longer, Livelier: Acoustic Shortcuts and Underspecified Rationales in Speech LLM Judges

arXiv ID：2609.36979 | 方向：语音大模型
作者：Mingyue Huo、Shivam Mehta、Bhavin Jawade、Yinghong Lan、Haoqi Li
机构：伊利诺伊大学厄巴纳-香槟分校（UIUC）、Netflix
发布日期：2026-09-30 | 论文 https://arxiv.org/abs/2609.36979 | PDF https://arxiv.org/pdf/2609.36979.pdf
代码/Demo：https://huggingface.co/datasets/mingyue66/SpeechJudgeAudit/（语音评审审计工具集）

### 📌 简介

语音大模型正日益充当TTS与语音交互质量"评审"甚至训练奖励信号。本文首次系统刻画语音评审的模态特有风险"声学捷径"：评审把易感知的声学线索（音量、内容丰富度、情绪演绎）误当作质量证据，或给予远超人类听众的权重。作者对六个语音评审做控制变量审计，发现评审系统性偏好更响、内容更丰富的音频，并把 Happy 等情绪演绎转成质量偏好；更令人担忧的是，其配套理由解释反复复用水泛化的"自然度、韵律"等评价词汇，几乎不点出真正改变判断的声学线索，处于"声学欠规定"状态。研究呼吁可靠的语音评审既要抵御声学捷径，也要让解释扎根于局部声学证据。

### 🔧 技术方案

**问题背景：** 语音质量多维且依赖细粒度声学感知，MOS等人工听测慢而昂贵，神经MOS预测器不透明、难泛化；SpeechJudge、SQ-LLM、UniSRM等专用评审与Gemini等通用音频大模型正被用于打分、偏好选择与奖励建模。文本评审已知存在位置、长度偏差，但语音评审是否以目标准则可辩护的方式使用声学线索，此前从未被系统检验。

**方法：** 提出声学捷径审计框架：对语音刺激做单一因子控制操纵，检验其是否系统性改变最终判断，并在改变发生时追问理由是否点名该线索；对可能合理影响感知的因子引入人类偏好校准作为基准。共审计六个评审：SpeechJudge-BTRM、SpeechJudge-GRM、UniSRM、SQ-LLM（均基于Qwen2.5-Omni）与Gemini-2.5-pro、Gemini-3.1-pro（零样本提示），同时评测pointwise打分与pairwise比较两种模式。

**核心创新：** (1) 提出"声学捷径"概念，区分无效证据线索与被过度加权线索两类偏差；(2) 构造三类单因子受控刺激：仅RMS电平变化的音量、语义等价的简洁-丰富配对、说话人与文本完全匹配的情绪演绎，并用静音补齐与重复作为时长/内容对照；(3) 首个双维理由审计：跨条件词频复用分析加预定义词典的"点名率"检测，揭示决策偏差与解释断裂两个独立问题。

**协议：** 音量用LibriTTS test-clean 80句（4个TTS系统各20句），归一化−30 LUFS后施加±3/±6 dB增益；内容丰富度用ASSET 149对；情绪用ESD 800条录音（10说话人×20句×中性/开心/悲伤/愤怒），归一化−23 LUFS。15名母语或近母语听者对60个唯一配对给出449条有效偏好判断；pairwise双向顺序测试，平局计0.5，项目级bootstrap置信区间。

### 📊 实验结果

**数据集**：LibriTTS test-clean、ASSET、ESD受控刺激池（含4种架构TTS合成语音），发布SpeechJudgeAudit审计工具集。

主要指标：
- 音量捷径：+6 dB时5个pairwise评审全部偏向更响音频，均值偏好0.578（个体0.541-0.616），人类基准0.612（显著但非有效质量证据）
- 内容丰富度过度加权：评审对同语义丰富语音偏好0.71，人类仅0.547（置信区间跨机运）；时长对照（静音补齐0.41、重复0.46）不能复现该偏好
- 情绪捷径：悲伤语音评审均值0.403 vs 人类0.217（惩罚与听者共享）；开心语音评审0.531 vs 人类0.407，3个评审显著偏Happy（评审特有偏差）
- 理由欠规定：被操纵线索点名率大多仅百分之几，UniSRM理由无任何响度词；重复为部分例外（5.7%-27.9%）
- 模式差异：SQ-LLM响度变化下pointwise分数不动但pairwise稳定偏好更响；UniSRM边界加1000 ms静音后pointwise几乎不变，对补齐片偏好跌至0.069

**是否开源**：是，SpeechJudgeAudit刺激与评估工具已在HuggingFace发布，可复用于其他评审。

### ⭐ 评分：7/10

理由：问题定义精准且切中语音LLM-as-a-judge作为奖励信号的实际痛点；实验设计严谨——单因子操纵、时长对照、顺序平衡、人类校准，使"哪些是评审特有偏差、哪些与听者共享"结论可信；"决策偏差+解释欠规定"双重发现有明确工程启示（先归一化音量剪静音、双模式互检、训练时注入定位声学证据的理由数据）。局限：仅英语、刺激池受控导致结论为池内有效；人类校准规模有限（15人449判断）；审计型论文未给出缓解方法或新模型；理由审计基于词法层面难以触达内部表征。贡献扎实、实用价值高，故7分。
## [8] InstCharVoice: Grounding Natural-Language Instructions for Character-Level Control in Text-to-Speech

arXiv ID：2609.36287 | 方向：语音大模型
作者：Sihang Nie、Xueru Li、Xiaofen Xing（通讯）、Deyi Tuo、Cheng-Bin Jin、Jingyuan Xing、Jinxin Ji
机构：华南理工大学、虎牙公司、香港理工大学
发布日期：2026-09-30 | 论文 https://arxiv.org/abs/2609.36287 | PDF https://arxiv.org/pdf/2609.36287.pdf | 代码/Demo：Demo https://xxh333.github.io/instcharvoice-demo/ ，代码暂无

### 📌 简介
现有指令驱动TTS对"哪几个字要变、怎么变"是隐式的，字级可控TTS又要求用户手动配置声学属性，两者之间存在接口与可解释性断层。本文提出InstCharVoice，将自然语言指令落地（grounding）到字级声学控制：先用Qwen3-Omni结合字级标注生成带定位标签的指令，再训练自回归模型在生成语音token前识别指令相关字符并预测其时长、边界、能量、音高、音调五维属性，实现可解释、可干预的细粒度表现力控制。

### 🔧 技术方案
**问题背景：** ITTS系统直接从文本与指令生成语音，指令短语、目标文本单元与声学变化间的对应关系隐式不透明；而WordVoice等字级可控方案虽精确可检查，却需用户逐项指定声学属性，长句下配置繁琐。
**模型架构：** 以Qwen2.5-0.5B为底座，CosyVoice3 tokenizer离散化语音，CAMPPlus提取说话人嵌入；每字符块依"属性输入+五维属性embedding+对齐语音token"组织，推理时辅助定位头判断该字是否被指令覆盖，五个属性头并行预测完整属性，未给定属性由指令与上下文补全，语音token交WordVoice-FM合成波形。
**核心创新：** (1)基于Qwen3-Omni-30B-A3B的三阶段LLM辅助标注流水线，在WordVoice-5A-zh上产出214.3万句指令、597.8万关键词及定位标签（边界388.2万、能量283万、音调90.1万、时长60.9万、音高20.2万）；(2)字符块级自回归建模，先规划定位与声学属性再生成语音，统一指令跟随与显式字级控制；(3)关键词预测头加grounding感知损失加权，边界/能量k=5、其余k=3，配合不确定性多任务加权。
**训练策略：** Adam，学习率2e-5，8×A800；两阶段：先5轮不加权训练全局指令到语音与属性建模，再启用重加权续训3轮强化局部控制；能量/音高各量化20档，边界5类、音调7类，属性训练时随机掩码支持部分指定。

### 📊 实验结果
**数据集**：WordVoice-5A-zh（源自LEMAS，约2546小时中文）；对比FireRedTTS3、Qwen3-TTS、CosyVoice3
- DNSMOS：3.686（四系统最高，真值3.616）
- CER：3.58%（最优2.89%，差距0.69个百分点）
- kD-MAE：0.0769 | kE-MAE：0.1271 | kP-MAE：0.1857
- kB-RER：14.04% | kT-RER：37.05%（全部关键词指标最优）
- NMOS：3.528 | IMOS：3.602（双第一）| SMOS：3.173（低于CosyVoice3的3.374）
- 显式字级控制：与WordVoice持平，B-ER 12.14%对12.72%、T-RER 21.87%对24.29%
- 消融：移除GLW劣化大于KP；加字级声学线索后指令一致率35.75%升至84.50%
**是否开源**：提供Demo音频页；模型权重与标注数据未明确开源

### ⭐ 评分：7/10
首次将自然语言指令系统性落地为五维字级声学规划，标注流水线与grounding加权设计可迁移，客观关键词指标全面领先且保留显式控制能力。扣分在于仅0.5B模型与2546小时中文数据、未建模情感等抽象风格、说话人相似回退、主观评测规模小（14条/27人），且用LLM自标数据训练存在循环验证风险。综合为工程完整度扎实的局部突破，给7分。
## [9] ReDimNet2+: Multi-Corpus Data Scaling for Robust Speaker Verification

arXiv ID：2609.37014 | 方向：语音大模型
作者：Kirill Borodin、Vasilii Kudryavtsev、Maxim Maslov、Grach Mkrtchian
机构：lab260（埃里温，亚美尼亚）、BitmanagerAI（迪拜，阿联酋）、MTUCI（莫斯科，俄罗斯）
发布日期：2026-09-30 | 论文 https://arxiv.org/abs/2609.37014 | PDF https://arxiv.org/pdf/2609.37014.pdf | 代码/Demo：https://github.com/lab260ru/redimnet2-plus（预训练权重 https://huggingface.co/lab260/redimnet2-plus）

### 📌 简介
面向设备、房间与压缩链路差异导致的说话人验证退化问题，本文在固定 ReDimNet2 紧凑骨干（12.3M 参数）的前提下，通过七个公开语料（63,934 说话人、约 8,675 小时）的数据规模化、编解码器与波形增强、大间隔微调（LMFT）以及图结构检索重排序，在统一的随机 4 秒评估窗口协议下将 VoxCeleb1 池化 EER 从 2.42% 降至 0.82%，26 条件鲁棒性压力测试 EER 从 7.21% 降至 1.99%，并给出可复现的本地开源基准对比。

### 🔧 技术方案
**问题背景：** 现代 ASV 系统在干净基准上 EER 已低于 1%，但在未见信道、激进压缩、短片段与开放集检索下显著退化。作者分析 VoxBlink2 子集（训练 673,277 条、11,053 人、约 1,458 小时；评估 134,697 条）发现域失配：FLAC 中位字节率从训练侧 21,040 B/s 降到评估侧 14,021 B/s，NISQA 色彩度预测低于 2.0 的文件占比从 6.2% 升至 41.4%，884 位多录音说话人的组内字节率标准差中位数为 1,753，提示录音通道与压缩异质性，由此引出显式编解码器仿真。

**模型架构：** 不改动骨干，沿用 ReDimNet2-B6（时间池化维度重塑，12.3M 参数）；输出 L2 归一化说话人嵌入，以余弦相似度打分；分类头为 SphereFace2 的 one-versus-all 二分类目标。

**核心创新：** (1) 数据分析驱动的编解码器增强：MP3、Opus、AAC、Vorbis、G.723.1、IMA ADPCM、G.722、A-law/μ-law、Speex、AMR-NB 等在 8/16 kHz 仿真，与带通/带阻/高低通滤波、MUSAN 与 RawBoost 噪声、RIR 混响、0.9–1.1 十档变速按 0.5/0.2/0.2/0.1 四模式联合施加，特征级 SpecAugment+CutMix 概率 0.2；(2) 分阶段多语料微调与 LMFT：先用七语料适配公共检查点（训练窗从 32,200 逐步扩到 48,300 样本），再以固定间隔 0.3、6 秒窗（96,000 样本）LMFT，池化 EER 沿 2.42→1.42→0.82% 逐级下降；(3) 免训练两阶段检索重排序：均值链挑选局部一致邻居，K-NN 图重打分结合排名、互反、共同邻居与枢纽度惩罚（权重 1.0/1.5/2.0/0.3，三次迭代）。

**训练策略：** Parquet 清单+随机窗口解码，比全量解码快 2.6 倍，损坏文件自动回退邻样本；谱图计算移至 GPU 使吞吐提升 1.53 倍；六卡 FSDP、BFloat16、AdamW、梯度裁剪 20、种子 42；检查点在 VoxCeleb1 开发集上选择。

### 📊 实验结果
**数据集**：训练七语料共 63,934 说话人、约 460 万条、8,675 小时；评估 VoxCeleb1-O/E/H（统一 4 秒随机窗，O/E/H 试验对 37,611/579,818/550,894）与 VoxBlink2 检索子集
- VoxCeleb1-O EER：0.351%（基线 1.601%）
- VoxCeleb1-E EER：0.523%
- VoxCeleb1-H EER：1.055%
- 池化 EERp：0.824%（基线 2.420%）
- 26 条件压力测试 EERph：1.991%（基线 7.214%）
- 同协议最佳 WeSpeaker CAM++ EERo：0.787%
- VoxBlink2 子集 Pr@kk：重排后 0.7687（重排前 0.7413）
- VoxCeleb1 Pr@45：99.6992%（重排前 99.2404%）

**是否开源**：代码与 HuggingFace 预训练权重均开源，基准含校验和、嵌入缓存与环境快照。

### ⭐ 评分：7/10
理由：工程完整度与可复现性突出，在不动架构的前提下用数据规模化+编解码器增强+LMFT 把短窗与强退化场景 EER 压到 SOTA 区间，并诚实区分本地协议与发表结果；扣分在于未隔离单个因子的贡献、压力测试为合成退化、缺真实电话/VoIP 数据验证，且骨干与检索协议均为既有设计的组合而非方法学突破。
## [10] Pruning for Efficiency, Paying in Fairness: Demographic Disparities in Pruned Speech-LLMs

- arXiv ID：2609.38106 | 方向：语音大模型
- 作者：Ganesh Pavan Kartikeya Bharadwaj Kolluri、Michael Kampouridis、Ravi Shekhar
- 机构：英国埃塞克斯大学计算机科学与电子工程学院（University of Essex）
- 发布日期：2026-09-30 | 论文 https://arxiv.org/abs/2609.38106 | PDF https://arxiv.org/pdf/2609.38106.pdf | 代码/Demo https://github.com/KarthikKolluriKB/SpeechLLM-Pruning-Fairness

### 📌 简介
语音大模型推理开销大，剪枝压缩是部署前的常规步骤，但业界普遍只用聚合词错误率（WER）验收剪枝模型，可能掩盖其对不同人口学群体的不均衡损害。本文对SLAM-ASR管线（冻结Whisper编码器+可训练投影器+冻结Qwen2.5-3B）开展首个系统性公平性审计：在Fair-Speech与Common Voice上逐步剪枝编码器并在每个深度重训投影器，逐群体测量WER。结果剪枝使种族与性别差距扩大，聚合指标甚至反向掩盖最差群体退化；LoRA恢复聚合精度但对优势群体受益更多，进一步拉大差距比。主张剪枝验收必须纳入最差群体WER。

### 🔧 技术方案
**问题背景：** ASR对Black说话人的高错误率早已被证实（商用系统Black约35%对White约19%），而语音大模型压缩环节的公平性影响此前无任何系统研究；聚合WER作为唯一验收指标是否掩盖剪枝造成的群体退化，是本文三个研究问题（RQ1剪枝是否放大差距并被掩盖；RQ2是否依赖编码器规模与语言资源；RQ3 LoRA恢复是否群体均等）。
**方法：** 采用SLAM-ASR架构，Whisper编码器（Small 12层/Medium 24层/Large-v2 32层）经ConcatLinear投影器接冻结Qwen2.5-3B解码器；自上而下每次移除2层编码器（L-2至L-8），每个深度从头重训投影器，得到真正可部署的配置；训练与选择全程不使用任何人口学标签。音频16kHz、80通道log-Mel；AdamW学习率1e-4、余弦调度、bfloat16、单张A6000（48GB）、单随机种子42；LoRA施加于LLM全部注意力投影，英语/荷语r=16（约1.5M参数）、丹麦语r=8（约0.8M参数）。
**核心创新：** (1) 首个跨剪枝深度、模型规模、LoRA三变量联动的语音大模型人口学公平审计；(2) 预注册式三级差异度量：最差组WER、绝对差距Δ（百分点）、规模无关差距比ρ，配2000次配对bootstrap显著性检验；(3) 揭示"聚合掩盖"现象：Large-v2首次剪枝聚合WER从21.6降至21.1（p=.038），而Black群体反升0.9pp（p=.009），群体比ρ从1.99升至2.15，为唯一上升的规模。
**协议：** 训练用Common Voice 22英语100小时（另建荷语54小时、丹麦语4.2小时系统）；评测主用Fair-Speech 26417条（族裔/社会经济/性别/年龄/母语五轴），跨语言用CV英语/荷语/丹麦语（口音/性别/年龄）；组分析门槛为至少200条且30分钟音频；可用范围限定聚合WER≤40%；解码beam search宽度2。

### 📊 实验结果
**数据集**：Common Voice 22（训练：英语58140条/荷语43458条/丹麦语3592条；测试：英语16391/荷语12033/丹麦语2684条）+ Fair-Speech 26417条仅评测。
- Black-Asian WER差距（Large-v2）：13.5→24.5pp，L-8时Black 51.0%对Asian 26.5%
- 首次剪枝掩盖效应：聚合21.6→21.1%（p=.038），Black +0.9pp（p=.009）；small/medium聚合分别恶化10.8/2.3pp，退化直接可见
- 其他轴：性别差距3.3→11.1pp；SES差距5.9→7.2pp（比1.36→1.24）；年龄差距因最老组退化最慢而"拉平式"收窄
- LoRA：L-0聚合21.6→17.7%，可用剪枝深度延长2层，但Black/Asian比在每个深度均扩大（L-0从1.99→2.20）；L-10为Asian恢复8.0pp、Black仅3.3pp
- 跨语言：CV英语印度/南亚口音相对比1.42→1.39稳定，荷语比利时组比1.1-1.3，差距持续但不放大；丹麦语L-4即超40%且标注稀疏，仅报告覆盖率
**是否开源**：代码已开源于GitHub（KarthikKolluriKB/SpeechLLM-Pruning-Fairness）。

### ⭐ 评分：7/10
理由：审计类工作中问题真实且系首次系统研究，"聚合改善而最差群体显著退化"的主结论统计严谨、工程协议规范（每深度重训投影器），结论对部署验收有直接可执行价值（以worst-group WER为准入门槛），三量度+配对bootstrap设计值得沿用。不足在于仅单一架构族与单一压缩方式、单随机种子、未测试任何缓解方法、缺乏交叉群体分析，且荷语/丹麦语结论受限于标注稀疏，创新性偏审计而非方法贡献。
## [11] τ-Multilingual: Benchmarking Voice Agents Across Languages

arXiv ID：2609.35820 | 方向：语音大模型
作者：Soham Ray、Edgard dos Santos Paiva、Ruben Valenzuela、Karthik Narasimhan、Keshav Dhandhania、Victor Barres
机构：Sierra、Mercor、普林斯顿大学
发布日期：2026-09-30 | 论文 https://arxiv.org/abs/2609.35820 | PDF https://arxiv.org/pdf/2609.35820.pdf | 代码/Demo：https://github.com/sierra-research/tau2-bench/tree/tau-multilingual

### 📌 简介
现有语音智能体基准几乎只测英语，仅覆盖行为分布的狭窄切片。本文提出 τ-Multilingual，将 τ-Voice（τ-bench 系列的全双工语音版）扩展到西班牙语、巴西葡萄牙语、印地语、韩语、中文五语言，构建由母语者审核、同时度量任务完成、交互质量与生成质量的多语言全双工语音智能体基准，含九百个本地化任务实例、五种语音配置四千五百通电话并设文本对照。结果显示西/葡/印地语基本保持、韩语与中文显著回落且失败模式各异；Grok 任务完成率最高但生成质量垫底。论文释放语言包、经校验评审与评测工具链，支撑社区构建本地语言文化规范的语音智能体评测。

### 🔧 技术方案
**问题背景：** τ-Voice、FDB-v3、EVA-Bench 等语音智能体基准均为英语单语；已有多语言资源以文本为主或缺可执行工具任务，无基准同时覆盖多语言全双工语音、任务、交互与语言质量。
**方法：** 基于 τ-Voice 200 毫秒步进全双工运行时，以 LanguageFactory 构建语言包：保留任务、工具与二值奖励，仅本地化来电者人格、读法规范、身份实体（如 Reeves→Neha Gupta）与评测规则，母语者审核冻结。900 个任务实例（50 任务×3 域×6 语言）跑 5 种配置共 4500 通电话——GPT（gpt-realtime-2）、Gemini 3.1 Flash Live Preview、Grok Voice Think Fast 1.0 各推理档，级联方为 gpt-5.5 文本加 Eleven v3 语音——另两个文本系统对照 1800 通。指标三层：任务完成（环境奖励通过率）、交互质量（100 减未应答、插话、选择性、超 45 秒独白、工具误用五类失败率均值）、生成质量（通过自然度与保真校验的话语占比，多模态评审比对音频与文本）。
**核心创新：** (1) 母语者原创、任务对齐的语言包工作流，本地化人格与文化规范而非翻译脚本；(2) 新增人工校验的自然度与语音保真评估轴，与任务、交互分开报告；(3) 失败模式定位：韩语未应答率 46.3% 对英语 27.8%，中文插话率 90.9%，认证精确查找成功率英语 81–85%、韩语仅 26–56%。
**协议：** LLM 评审门槛为精确率/召回率≥0.75、F1>0.80、Cohen’s κ>0.60；任务完成用 150 簇配对置换检验与 10000 次 BCa 重采样，交互与生成用 100000 次标签交换并 Holm 校正；每语言抽 30 通人审归因。

### 📊 实验结果
**数据集**：τ-Multilingual（零售/电信/航空三域、六语言匹配任务包，5334 通语音加文本呼叫）
主要指标：
- 任务完成：西/葡/印地语相对英语回落≤3.2 点且不显著；韩语 −18.8 点（95% CI：14.8–23.3）、中文 −9.5 点（CI：6.0–13.4），Holm 校正 p<0.00005
- 交互质量：五语言相对英语分别下降 4.6/3.7/3.1/12.6/11.8 点，全部显著
- 生成质量：GPT xhigh 最高 67.5%（完成率仅 55.7%）；Grok 六语言均值完成率 75.1% 居首但生成 52.3% 垫底；80.0% 的 Grok 话语无实质性听觉错误，其余系统 91.3–93.8%
- 语音-文本差距：所有语言中语音配置落后文本对照 16.8–41.1 点，韩语最剧（40.9% 对 82.0%）
- 域难度错配：电信完成率最低 44.1%，却生成质量最高 63.2%
- 评审器可信度：工具使用 micro-F1 97.7%、自然度 89.4%、音频保真 90.2%
**是否开源**：是，代码、语言包、校验评审器与审计规则已发布（GitHub：sierra-research/tau2-bench 的 tau-multilingual 分支）

### ⭐ 评分：7/10
理由：基准工程质量一流——严格匹配的任务包设计、母语者审核、带接受阈值的评审器体系与规范的配对统计，把「能不能完成任务、聊得自不自然、说得像不像母语」三轴拆开报告，对韩语/中文认证与轮换失败的定位具直接工程价值。扣分在于：仅覆盖三个闭源托管模型家族与单一语音栈、无开源权重系统；跨语言自然度未校准导致不能对语言排序；30 任务的本地化消融细胞仅具探索性；部分结论受单一试验（Grok）与成本限制。
## [12] When Capabilities Fail to Compose: Diagnosing the Compositionality Gap in Large Audio-Language Models

**arXiv ID**：2609.36921 | **方向**：语音大模型
**作者**：Chien-Feng Liu、Chih-Kai Yang、Bo-Han Feng、Yu-Hsuan Li Liang、Hung-yi Lee（李宏毅）、Cheng-Fu Chou
**机构**：国立台湾大学（NTU）、NTU AI-CoRE、华硕开放云基础设施软件中心（ASUS OCIS）
**发布日期**：2026-09-30 | **论文** https://arxiv.org/abs/2609.36921 | **PDF** https://arxiv.org/pdf/2609.36921.pdf | **代码**：https://github.com/steven-lunar/audio-compositionality-gap | **Demo**：无公开演示

### 📌 简介

大型音频语言模型（LALM）在单点音频任务上表现强劲，但其能力能否可靠组合仍是未知盲区。本文提出一个控制变量式诊断框架，将复合任务拆解为原子能力识别、线索条件化片段选择、下游执行三个层级，要求模型在两段连续语音中依据环境声、性别、情绪线索定位目标片段后再完成 ASR、数学问答或常识问答。对四个开源 LALM 的系统评测显示：组合式问答准确率在 40 个"模型—任务—线索"设置中的 39 个显著下滑，平均下降 26.7 个百分点；组合式 ASR 的 WER 同样在 39 个设置中上升，平均恶化 28.5 个百分点。研究进一步通过输出格式、位置偏好与思维链探针定位失败来源，揭示"拥有单项能力"与"可靠组合能力"之间存在系统性缺口，且该缺口并非由单一瓶颈造成，为 LALM 复杂音频理解的可信度评估提供了新范式。

### 🔧 技术方案

**问题背景**：LLM 与 VLM 领域已发现组合性缺口——组件技能单独可用但联合推理失败。音频领域中 SAKURA、CompA、PolyBench、ART 等工作涉及多跳或组合推理，但均未显式地将组合任务性能与其构成的原子能力逐项对照，无法回答"能力究竟在哪一问环节断裂"。

**方法**：构造两段串联语音样本 X=S1|S2，每段绑定一个声学属性（环境声/说话人性别/情绪）与一个下游目标（ASR/数学 QA/事实 QA），文本查询指定目标属性，另一段作为干扰项。评测分三层：原子识别（直接报告两段属性）、原子下游（对两段分别执行任务）、片段选择（预测目标段索引 i*）、完整组合（先按线索选段再执行任务）。语音由 CosyVoice 3 合成（CREMA-D 六说话人、三情绪），环境声取 ESC-50 五类并按 0/10/20 dB SNR 混入；事实 QA 取 TriviaQA 1000 题，数学 QA 取 Spoken-MQA，共得 4800 个双段样本。用 emotion2vec、UTMOSv2、Whisper 做自动质检并人工复核。四个模型（Qwen2.5-Omni-7B、MiniCPM-o 4.5、MiMo-Audio-7B、Kimi-Audio-7B）零样本、贪心解码，QA 采用标签解析与 GPT-4o-mini LLM 解析双通道。

**核心创新**：(1) 首创三层可分解的组合能力诊断协议，把端到端掉分归因到感知、绑定、执行、输出控制各环节；(2) 系统量化 40 个设置下原子到组合的一致性退化，证明强原子识别不保证强片段绑定（如 Qwen2.5-Omni 性别识别 95.42% 而选择仅 76.67%）；(3) 发现位置偏好随线索显著性增强（E0 到 E20 偏离 50% 单调增大），且组合引入额外格式失控（MiniCPM-o 格式符合率 92.71%→54.91%），CoT 提示不能普遍弥合缺口。

**协议**：控制输入长度与多段上下文（原子任务同样含两段）、目标位置与干扰类均衡、双解析器对照，确保退化来于组合本身而非数据或格式偏差。

### 📊 实验结果

数据集：自建 4800 样本组合基准（环境声 E0/E10/E20 + 性别/情绪，数学 QA 与事实 QA 各 4×600 子集），基于 CosyVoice 3、CREMA-D、ESC-50、TriviaQA、Spoken-MQA。

主要指标（LLM 解析口径）：
- 组合式 QA 退化：40 个设置中 39 个下滑，平均 −26.7 个百分点
- 组合式 ASR：39 个设置 WER 上升，平均 +28.5 个百分点
- 极例对比：MiniCPM-o 事实 QA E20 下 WER 由原子 8.55% 升至组合 67.97%；Qwen2.5-Omni 数学 QA E20 准确率由 83.50% 跌至 40.50%
- 片段选择：Qwen2.5-Omni 最强（环境声 75.50–88.67%），MiMo-Audio 多数接近随机
- 情绪识别 35.50–49.00%，仅略高于 33.3% 随机基线
- 格式符合率：MiniCPM-o 组合阶段跌至 54.91%，数学 QA 解析器差异高达 +48.87
- CoT 干预：事实 QA 四模型均提升 1.9–14.63，数学 QA 则 Qwen −11.17、MiMo +20.53，无一贯收益

开源情况：代码已开源（GitHub: steven-lunar/audio-compositionality-gap），数据集构建脚本随仓库发布；无商用许可限制说明。

### ⭐ 评分：6/10

这是一篇扎实的诊断型评测论文：三层分解协议设计干净、控制变量严格，40 设置中 39 设置一致退化的结论有说服力，格式/位置/CoT 三类探针将"缺口不在单一环节"论证得较充分，对音频智能体研发有直接警示价值。不足在于：仅覆盖 7B 级开源模型与两段短音频，未验证闭源大模型与更长场景；数据全为 TTS 合成，生态效度有限；只诊断不治疗，未提出训练或架构层面的补救方案。作为 ICASSP 短文体量合适，作为独立贡献深度中等。
## [13] RAWD-TTS: Ratio-Free Reward Alignment for Discrete-Diffusion Voice Cloning

arXiv ID：2609.37028 | 方向：语音大模型
作者：Maxim Maslov、Kirill Borodin、Vasilii Kudryavtsev、Nikita Vasiliev、Grach Mkrtchian
机构：lab260（埃里温）、BitmanagerAI（迪拜）、MTUCI（莫斯科）
发布日期：2026-09-30
论文：https://arxiv.org/abs/2609.37028 | PDF：https://arxiv.org/pdf/2609.37028.pdf | 代码/Demo：https://github.com/lab260ru/RAWD-TTS

### 📌 简介
本文提出RAW D-TTS（免比例优势加权去噪），针对离散扩散零样本语音克隆的奖励对齐难题。传统监督token预测无法直接优化波形级的可懂度与说话人保持，而自回归/连续流匹配的RL方法在离散扩散中失效，因为token选择与揭示位置共同决定采样轨迹。作者用终态样本的组内相对优势加权掩码重建损失，无需反向轨迹似然与目标音频，在500条俄语CV3-Eval上将WER从3.18%降至2.42%，同时WavLM说话人余弦从0.733升至0.748。

### 🔧 技术方案
**问题背景：** 零样本TTS需同时保证内容准确与音色保持。离散扩散OmniVoice以迭代掩码预测生成C=8个Higgs音频码本，token取值与揭示顺序联合决定解码路径，最终波形无法简单累乘自回归概率，故F5R-TTS等基于轨迹的策略优化难以直接迁移。

**模型架构：** 基座为0.6B OmniVoice加LoRA（rank16、alpha32、dropout0），codec冻结。提示q=（目标文本、参考音频及转写）经原生采样器生成token并解码为波形，冻结ASR与说话人编码器打分。

**核心创新：** (1) 联合奖励：r=exp(-2.5·WER)与(1+cos)/2按λasr=λspk=1相加，组内标准化得优势A（ε=1e-6，∑A=0）；(2) 终态免比例去噪替代：对detached token做K次前向腐蚀，组内共享腐蚀比例ρ~U(0,1)作共同随机数，先按码本内平均再跨码本融合，得到长度归一化的有符号ELBO型REINFORCE替代；(3) wd1加权对照：用softmax差ω替换线性A以检验梯度形状与尺度影响。

**训练策略：** 8000条Balalaika俄语提示（参考10.96h、均值4.93s），B=4/G=8/K=3~5，AdamW学习率1e-5、10步warmup、梯度裁剪1，无KL与监督锚损失；单卡RTX6000 Ada训练2000迭代9.25 GPU时（16.65s/更新），rollout 32步无CFG。

### 📊 实验结果
**数据集**：训练用Balalaika YouTube分区，评测用CV3-Eval俄语500条。
主要指标
- WER（Whisper）：基座3.18→选点Joint K=5为2.42%（相对降24.0%），末点2.58%（19.0%）
- WavLM说话人余弦：基座0.733→0.748（选点）/0.755（末点）
- 独立评估Qwen3-ASR WER：4.38→3.76%；ERes2Net余弦0.704→0.724
- ASR-only降WER至2.35但余弦跌到0.705，Speaker-only余弦0.763但WER升到3.34，体现识别-音色权衡
- SFT对照2.94%/0.765；wd1加权2.61%未优于线性2.41%
- 消融：K=5优于K=1/3（2.47%），(B,G)=(4,8)优于(8,4)/(2,16)
- DistilMOS：对齐后≥基座3.18，Joint K=5为3.25

**是否开源**：代码与配置已开源。

### ⭐ 评分：6/10
免比例优势加权迁移到离散扩散语音克隆是干净有效的贡献，终态腐蚀共享比例与组内基线设计优雅，独立评估者验证增益非奖励黑客。缺陷：仅单backbone、单语、单种子实验；无KL/trust region致训练奖励上升而基准非单调；自选择checkpoint偏置明显；缺人类主观听测与CFG扫频，且音色仍低于CosyVoice3与SFT。属扎实的工程实证而非方法突破。
## [14] Interpreting and Evaluating Dynamic-Rate Speech Codec Boundaries

arXiv ID：2609.36951
方向：语音大模型
作者：Han Wang、Jiaqi Li、Yingda Shen、Yuxiang Wang、Zhizheng Wu（前两者同等贡献）
机构：香港中文大学（深圳）、Amphion Technology Co., Ltd.、浙江大学
发布日期：2026-09-30
论文：https://arxiv.org/abs/2609.36951
PDF：https://arxiv.org/pdf/2609.36951.pdf
代码/Demo：https://github.com/Hanzz3/dfr-codec-boundaries

### 📌 简介
动态帧率（DFR）神经语音编解码器用变长token取代均匀时间栅格，使边界摆放成为表示的一部分，但边界究竟编码了什么、可解释的边界是否真的有利于重建长期不明。本文首次将边界解释与受控重建评测结合：预测边界与音素、音节、BPE、词、声学事件、V/UV六类参考边界对齐，再在统一编解码接口下比较六种DFR算法与固定帧率基线的重建质量。核心发现：边界的含义取决于底层表示与其深度，ASR导向编码器浅层偏语音与声学转换、深层转向音节与子词结构；高层语言对齐与更低池化失真、更好重建正相关，音节尺度是语义化语音token分配的有效组织粒度。

### 🔧 技术方案
**问题背景：**传统SoundStream、EnCodec、DAC等神经编解码器帧间隔均匀，与语音信息密度不均（稳态元音、静音、辅音过渡）不匹配；FlexiCodec、CodecSlime等DFR方法虽可合并冗余帧，但不同边界分配机制在相近平均帧率下把token放在完全不同区域，其语言学与声学含义、以及对重建的实际收益从未被系统检验。

**方法：**EXP1以12.5Hz潜变量栅格上的FlexiCodec为共同骨架，比较Similarity、CodecSlime、PLE、TADPC、A-ToMe与Entropy-Mass六种免训练边界算法及Uniform基线，边界F1在40ms容差内单调最优匹配，参考边界由MFA强制对齐、NLTK音节规则、GPT-2 BPE与声学启发式构造；并将同一判据沿SenseVoice、Whisper、HuBERT、WavLM的层深追踪。EXP2在共享编码器与解码器（LibriTTS多帧率混合微调后冻结）下测q1与q1:8重建WER、NMSE、PESQ、说话人相似，并在帧率匹配条件下直接比较音素派生（8.06Hz）与音节派生（4.47Hz）固定分区。

**核心创新：**(1) 首个面向DFR编解码边界的可解释性评测协议，六类参考边界加密度校正的ΔUniform对比；(2) 揭示边界含义随表示族与层深漂移：ASR监督编码器深层音节、BPE、词F1上升，自监督编码器仅浅层声学对齐强；(3) 帧率匹配消融证明音节粒度有效而音素粒度无效：音节派生分区WER从17.61%降至13.85%，优于Similarity的14.99%，音素派生反而从6.47%升至7.10%。

**协议：**同一冻结特征（SenseVoice第49层）、同一量化器与解码器、标称6.25/8.33/10Hz三档速率下仅更换边界算法，隔离边界摆放本身的影响。

### 📊 实验结果
**数据集**：TIMIT测试集1680条语句（评测），LibriTTS train-clean-100（解码器微调），LibriSpeech test-clean（NMSE排序验证）
- 音节边界F1：Similarity 0.557 / CodecSlime 0.535，Uniform仅0.38；音素F1各法均窄幅0.497-0.532
- q1:8重建WER：CodecSlime 5.394%最低，Uniform 6.226%；CodecSlime NMSE 0.0627（Uniform 0.0943）
- 音节、BPE、词对齐与重建WER/NMSE的Spearman相关：6.25Hz下达0.79-0.93，跨三档速率一致
- 运行时：Similarity仅0.277ms，CodecSlime 19.546ms，Entropy-Mass 31.017ms，PLE以0.283ms逼近最优WER（5.415%）
**是否开源**：是，代码与实现细节公开于GitHub

### ⭐ 评分：6/10
作为分析型工作，其评测协议严谨、控制变量充分，"音节优先于音素的分配先验"对低帧率语音token化与语音LLM设计有直接指导价值，且完全可复现。但不足亦明显：仅覆盖英语与12.5Hz栅格上限，未训练新的边界分配模型，结论停留在关联与匹配消融、因果性有限，且仅适用于语义化丰富的表征。方法学价值高于模型创新，故评6分。

---

## 语音前端

## [15] Perception-Inspired Bayesian Causal Fusion for Audiovisual Source Localization

**arXiv ID**：2609.36441 | **方向**：语音前端 | **作者**：Kyung Yun Lee、Sungnyun Kim、Sebastian J. Schlecht、Tae-Hyun Oh、Vesa Välimäki | **机构**：阿尔托大学（芬兰）、KAIST（韩国）、埃尔朗根-纽伦堡大学（德国） | **发布日期**：2026-09-30 | **论文** https://arxiv.org/abs/2609.36441 | **PDF** https://arxiv.org/pdf/2609.36441.pdf | **代码**：未开源（依赖公开的 DCASE2025 SELD 基线 checkpoints、DCASE2024 ngcc-seld 模型与 Grounding DINO）| **Demo**：无

### 📌 简介
多模态融合只有在模态共享同一因果来源时才有益；声源被遮挡或位于视野外时，视觉通道与目标条件独立，盲目融合只会污染估计。本文将"是否融合"的决策建模为贝叶斯因果推断，借鉴人类多感知最优观察者模型（Körding 等），在冻结的音频与视觉模型之上实现即插即用的因果门控层，用于声事件定位与检测（SELD）。模型先对可见候选物体推断共因后验，再按该后验对精度加权融合进行门控。实验显示无条件融合使方向误差翻倍以上，而因果门控在无联合重训练的情况下改善屏内定位并控制屏外退化。

### 🔧 技术方案
问题背景：受限视场相机与多通道麦克风组合中，声源常"可听不可见"，端到端联合训练网络缺乏显式的模态因果判断，不确定性加权方法也只做连续调制而不回答是否存在共享原因。模型架构：完全冻结的音频 SELD 模型输出事件类别与球面方向，冻结的开放词汇检测器（Grounding DINO Tiny）输出候选边界框并投影为相机视线；融合层作为后验插件叠加于二者之上。核心创新（1）：将双线索球面共因推断推广到多视觉候选，用 von Mises–Fisher 角似然构造球面贝叶斯因子，结合于训练集估计的模态 RMS 误差与共因先验；（2）：以共因后验 P_AV 为连续门控权重，实现精度加权融合与音频估计的模型平均，避免硬阈值与 argmax 带来的不连续跳变，后验趋零时自然退化为纯音频估计；（3）：零训练成本，任何更强的单模态模型可直接替换。训练策略：不做任何联合训练，仅在训练划分上估计 σ_a、σ_v 与屏内先验 π_vis 并冻结。

### 📊 实验结果
数据集：DCASE2025 Task 3 立体声数据集及作者构建的四通道麦克风（STARSS23）全球面版本。主要指标：
- 共因分类 AUROC：0.920（对比 Gate-20 硬门控 0.828、Forced 0.500），AP 0.847，Brier 0.093，ECE 0.060
- MIC 全球面 DOAE：Causal 29.50° 对比纯音频 30.41°、强制融合 61.47°；屏内改善 2.75°、屏外仅退化 0.26°
- 立体声对比：Causal 屏内 DOAE 13.78°，优于纯音频 16.59° 与联合-training AV-base 19.13°；屏内外分类准确率 0.76 对 0.74
开源情况：方法代码未宣布开源，实验基于公开数据集与公开基线模型。

### ⭐ 评分：7/10
将感知科学的规范因果推断模型落地为免训练即插即用融合门，思路优雅、校准良好、对屏内定位的提升真实超过联合训练基线，工程价值明确；但总体增益受屏内事件占比限制而偏小，依赖人工类别映射与检测器质量，未开源且缺乏与更多学习的融合方法对比，方法学新颖度大于绝对性能突破。

---

## 其余论文（仅列标题、arXiv ID、评分与链接）
### [16] Estimation of Room Impulse Responses from Handclaps
- **arXiv ID**：2609.35839 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.35839 | **PDF**：https://arxiv.org/pdf/2609.35839.pdf | **代码**：暂无 | **Demo**：暂无

### [17] Model-Guided Design of Low-Context Speech Probes for Cochlear Synaptopathy
- **arXiv ID**：2609.36272 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36272 | **PDF**：https://arxiv.org/pdf/2609.36272.pdf | **代码**：暂无 | **Demo**：暂无

### [18] Enabling Immersive Audio-Visual Experience from Any Video
- **arXiv ID**：2609.36295 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36295 | **PDF**：https://arxiv.org/pdf/2609.36295.pdf | **代码**：暂无 | **Demo**：暂无

### [19] Distill Locally, Schedule Globally: Flow Maps for Few-Step Text-to-Speech
- **arXiv ID**：2609.36324 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36324 | **PDF**：https://arxiv.org/pdf/2609.36324.pdf | **代码**：暂无 | **Demo**：暂无

### [20] UDSS-BWE: Uncertainty- and Decision-Science Inspired Swin BandWidth Extension
- **arXiv ID**：2609.36379 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36379 | **PDF**：https://arxiv.org/pdf/2609.36379.pdf | **代码**：暂无 | **Demo**：暂无

### [21] InterBias-SV: Compound Conditions in Speaker Verification
- **arXiv ID**：2609.36500 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36500 | **PDF**：https://arxiv.org/pdf/2609.36500.pdf | **代码**：暂无 | **Demo**：暂无

### [22] Long-Term Memory-Guided Enhancement for Target Perception in Audio-Language Models
- **arXiv ID**：2609.36577 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36577 | **PDF**：https://arxiv.org/pdf/2609.36577.pdf | **代码**：暂无 | **Demo**：暂无

### [23] Reconstructing the Vocal Tract with Differentiable Acoustic Simulation
- **arXiv ID**：2609.36737 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36737 | **PDF**：https://arxiv.org/pdf/2609.36737.pdf | **代码**：暂无 | **Demo**：暂无

### [24] Does a prosody-trained representation help beyond trainable fusion? A parameter-matched study with frozen HuBERT
- **arXiv ID**：2609.36754 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36754 | **PDF**：https://arxiv.org/pdf/2609.36754.pdf | **代码**：暂无 | **Demo**：暂无

### [25] Repetition, Not Length: Isolating the Counting Failure in Neural Text-to-Speech
- **arXiv ID**：2609.36974 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.36974 | **PDF**：https://arxiv.org/pdf/2609.36974.pdf | **代码**：暂无 | **Demo**：暂无

### [26] RVQ Position Aware Speculative Decoding for On Device Text to Speech
- **arXiv ID**：2609.37007 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37007 | **PDF**：https://arxiv.org/pdf/2609.37007.pdf | **代码**：暂无 | **Demo**：暂无

### [27] Prediction-Layer Branch Calibration for Multimodal Sentiment Analysis
- **arXiv ID**：2609.37100 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37100 | **PDF**：https://arxiv.org/pdf/2609.37100.pdf | **代码**：暂无 | **Demo**：暂无

### [28] Multichannel Audio Quality Assessment: Extending Pretrained Perceptual Models to Spatial Audio
- **arXiv ID**：2609.37116 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37116 | **PDF**：https://arxiv.org/pdf/2609.37116.pdf | **代码**：暂无 | **Demo**：暂无

### [29] SENSE: Semantic Neural Speech Synthesis from Brain Dynamics via Spatial Graph Encoding
- **arXiv ID**：2609.37601 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37601 | **PDF**：https://arxiv.org/pdf/2609.37601.pdf | **代码**：暂无 | **Demo**：暂无

### [30] Selective Lookahead for Attention-Based Streaming ASR
- **arXiv ID**：2609.37611 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37611 | **PDF**：https://arxiv.org/pdf/2609.37611.pdf | **代码**：暂无 | **Demo**：暂无

### [31] AS$^2$D: Accelerating On-Demand Audio Understanding on Mobile Devices
- **arXiv ID**：2609.37617 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37617 | **PDF**：https://arxiv.org/pdf/2609.37617.pdf | **代码**：暂无 | **Demo**：暂无

### [32] Signal-Independent and Signal-Dependent Neural Ambisonic Matrix Encoding for Arbitrary Arrays with Variable Microphone C
- **arXiv ID**：2609.37691 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37691 | **PDF**：https://arxiv.org/pdf/2609.37691.pdf | **代码**：暂无 | **Demo**：暂无

### [33] Zephyr: An Efficient Audio Denoising System Using Spiking Neural Networks Enabled With A Sparsity-Aware Flexible FPGA PE
- **arXiv ID**：2609.37711 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37711 | **PDF**：https://arxiv.org/pdf/2609.37711.pdf | **代码**：暂无 | **Demo**：暂无

### [34] GLaS-JEPA: Gaussian-Regularized Speech SSL without Engineered Prediction Targets
- **arXiv ID**：2609.37798 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.37798 | **PDF**：https://arxiv.org/pdf/2609.37798.pdf | **代码**：暂无 | **Demo**：暂无

### [35] QK-GCC: Learnable Query-Key Spectral Matching for Robust Time Delay Estimation
- **arXiv ID**：2609.38000 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.38000 | **PDF**：https://arxiv.org/pdf/2609.38000.pdf | **代码**：暂无 | **Demo**：暂无

### [36] EmoRES-TTS: Residual-Enhanced Vector Steering for Emotional Speech Generation
- **arXiv ID**：2609.38157 | **评分**：5/10（未精读，按摘要粗评）
- **论文**：https://arxiv.org/abs/2609.38157 | **PDF**：https://arxiv.org/pdf/2609.38157.pdf | **代码**：暂无 | **Demo**：暂无

---

*Generated on 2026-09-30*
