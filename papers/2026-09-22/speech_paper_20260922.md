# 2026-09-22 语音论文速递

**共收录**: 35 篇 | **语音大模型**: 28 篇 | **语音前端**: 7 篇

> 目标日期 2026-09-22（北京时间）arXiv 语音相关论文共命中 35 篇。
> 以下是按评分排序的结果（前 15 篇完整精读，其余仅列标题、arXiv ID、评分与链接）。

---

## 语音大模型

## [1] MuLA-Bench: A Multilingual Long-Form Audio Understanding Benchmark via Multi-Tier Auditing

**arXiv ID**：2609.23416 | **方向**：语音大模型
**作者**：Zeyu Yang、Xinyu Zhang、Zibo Bi、Pei Zhang、Xize Cheng、Jin Xu、Baosong Yang、Satoshi Nakamura
**机构**：香港中文大学（深圳）、阿里巴巴Token Hub、西安交通大学
**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23416 | **PDF**：https://arxiv.org/pdf/2609.23416.pdf | **代码**：https://github.com/QwenLM/Omnilingua-Bench/tree/main/MuLA-Bench | **Demo**：暂无

### 📌 简介
长音频理解能力常被上下文长度与聚合准确率两个单一指标概括，掩盖了语言、证据与任务共同塑造的条件化难度。本文提出MuLA-Bench：基于1769条野生长录音（共1377.9小时）构建5038道开放式问题，覆盖16种语言、8个领域；语义轨在每个语言×领域格点严格均衡30题，声学轨保留自然出现的非语音事件，经证据锚定、捷径测试与母语专家复审做可审计质检。对10个音频-语言模型评测显示，最强Gemini 3.8 Flash总分仅73.4%，且语言排名随领域/任务漂移、时钟定位在事件已理解时仍失败。

### 🔧 技术方案
**问题背景：** 现有多语言或长音频基准依赖翻译共享源、合成注入事件，或保留原始录音却难以拆解变量，无法在控制问题分配的同时保留原生语音与自然声学证据。
**评测体系设计：** 评测空间为16语言×8领域共128格点。语义轨3840题，每格点固定为8事实、8推理、7时序、7长程，消除任务混合混杂；声学轨1198题按已验证自然事件可用度采样不以翻译或插音补齐。任务涵盖事实/完整性、多证据推理、事件排序与时点定位、跨10分钟以上间隔的长程检索，全部题目绑定局域化证据。
**核心创新：** (1)首个同时具备原生16语广覆盖、语言×领域受控语义分配与自然声学证据双轨设计的长音频基准；(2)证据优先构建管线：字幕时间戳对齐原子事实并由TimeAudio全片提议声学事件、经两遍盲测核验（先观察后对案，仅保留可听事件），问题与答案由独立调用解耦生成，过语言/锚定/唯一性/泄漏等自动门与任务感知转写捷径测试；(3)全量由16名母语专家终审校准，裁判采用GPT-5.6 SoL路由式评分细则与±3秒确定性时间匹配，人-机一致率97.4%。
**评测协议：** 模型仅输入音频与源语言问题；本地模型按原生上下文取最长前缀；缺失或违规按固定5038分母记零；诊断统计基于固定八模型队列。

### 📊 实验结果
**数据集**：1769条野生录音、1377.9小时（中位36.8分钟，单条上限3小时），16语言×8领域，5038题。
**主要指标**：
- 总体准确率：Gemini 3.8 Flash 73.40%、Gemini 3.7 Flash 73.12%；Qwen3.5-Omni-Plus 60.92%
- 声学-语义差：3.8 Flash为55.26/79.06；Gemini 3.1 Pro声学仅26.63，其事实题语义89.75对声学17.07，差距达-72.7pp
- 长程检索普遍最强：Flash系85.1–85.3，时序题仅66.4–66.7
- 开权重最强Qwen3-Omni-30B为24.91%，Audio Flamingo Next 13.60%、MOSS-Audio-8B 13.48%
- 条件诊断：越南语残差从娱乐+14.2pp移到产品-13.3pp；日语在3.8 Flash时序题从第1跌至第10，印地语长程从第8升至第1；推理声学差反转约+15pp；八队列中时序精度随证据距离从44.4%降至23.2%，Doubao排序48.7对时点仅8.1
**是否开源**：是，数据与代码已发布。

### ⭐ 评分：8/10
基准类工作中的高水准之作：受控语言×领域格点与自然声学证据的双轨设计补齐了现有评测空白，三层审计管线与固定队列条件化诊断揭示"长上下文≠可靠理解"，时钟定位与事件理解解耦等发现具方法论价值。扣分在于题目主要由自动管线生成且单一专家复审、诊断结论限于特定模型群体、无模型或训练层面贡献。

## [2] COT-TTS: Audio Context-Aware Text-to-Speech with Chain-of-Thought Reasoning

**arXiv ID**：2609.22697 | **方向**：语音大模型；**作者**：Weizhen Bian、Sitong Cheng、Rongxiu Zhong、Junlan Feng、Bei Liu、Wei Xue 等；**机构**：香港科技大学、中国移动九天研究院、北京大学多媒体信息处理国家重点实验室；**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.22697 | **PDF**：https://arxiv.org/pdf/2609.22697.pdf | **代码**：暂无（承诺发布数据构建管线、数据集、模型与训练代码）| **Demo**：https://luckybian.github.io/COT-TTS

### 📌 简介
现有TTS的表现力依赖用户显式风格指令，而自然对话中的说话方式应由上下文推断。本文提出音频上下文感知的推理式TTS任务COT-TTS：给定历史多说话人对话音频、目标文本与参考音色，模型先生成带情绪标签的历史转写和显式说话方式推理（CoT），再合成目标语音。作者构建了9M样本双语训练集（含1M高质量子集）与800条人审源隔离测试基准，并训练0.6B/1.7B端到端自回归模型，以约1/30的参数量达到与34–39B级联基线相当的整体表现，时长误差由5秒级降至约1秒。

### 🔧 技术方案
**问题背景：** 对话配音、情感支持等场景需从历史音频自动推断"怎么说"；现有数据集缺少"上下文到说话方式"的显式推理监督，级联方案（ASR+LLM+TTS）会丢失副语言信息且风格标签往往作用于整句而非局部。
**模型架构：** 以Qwen3（0.6B/1.7B）为骨干，采用Spark-TTS的BiCodec离散表示（32个全局token加单流语义token），将历史音频、参考语音、目标文本、CoT与目标语音统一为一条自回归序列；历史音频仅保留首个全局token块作声学锚点，语音仅预测语义token并用参考全局token解码以锁定音色；推理时可暂停并编辑中间CoT。
**核心创新：** (1)形式化COT-TTS任务，CoT含言语行为、场景语义、认知动机、预期沟通结果、情绪轨迹五维，外加时长与情绪强度属性及结构化总结；(2)可复用数据管线，从影视剧等约10万小时音频标注出23M样本，经目标去重、说话人一致性参考选择（嵌入余弦相似度阈值0.5）与质量过滤得到9M/1M训练集和源隔离基准；(3)三阶段训练：140K小时ASR/TTS模态对齐、9M主任务与辅助任务7:3混合并随机丢弃0–10%输入、1M+1M高质量精炼。
**训练策略：** VeOmni框架全参微调，损失仅计算输出token；辅助任务含ASR、TTS、说话人日志、SER与指令TTS。

### 📊 实验结果
**数据集**：自建COT-TTS双语基准800条（中英各400，源隔离、LLM加人工双重筛选），训练用9M/1M子集及140K小时开源语音。
**主要指标**：
- Human MOS（英文）：4.15（0.6B），最强基线3.60，提升约0.55
- 时长误差：1.16s/1.10s（英/中），基线多在5.1–12.5s，优4倍以上
- 情绪一致性：约0.95，优于全部基线（0.91–0.95）
- UTMOSv2：2.94（英文），低于Fish Audio 2级联的3.11–3.14
- LLM推理综合分：2.30（英文），低于最高基线3.60；编辑CoT后升至2.89，中文编辑版取得全场最高综合分
- WER/CER：4.1%，劣于最佳基线1.2%
**是否开源**：是，承诺开放数据管线、训练/评测数据、模型与代码。

### ⭐ 评分：7/10
首次形式化上下文音频推理TTS任务，并发布9M级CoT监督对话语音资源与评测协议，参数效率与时长/情绪一致性优势显著、人工MOS夺冠，属实质贡献。但端到端模型在自然度、内容准确率与推理细项上仍不及最优级联基线，CoT编辑对大幅改动敏感，影视源数据的版权与标注可靠性有待验证，尚不构成突破。

## [3] AURA: Uncertainty-Routed Activation Editing for Acoustic Grounding in Speech Foundation Models

**arXiv ID**：2609.23979 | **方向**：语音大模型；**作者**：Natarajan Balaji Shankar, Zilai Wang, Zihan Wang, Mohan Shi, Kaiyuan Zhang, Abeer Alwan；**机构**：加州大学洛杉矶分校（UCLA）电子与计算机工程系；**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23979 | **PDF**：https://arxiv.org/pdf/2609.23979.pdf | **代码**：https://github.com/balaji1312/aura | **Demo**：暂无

### 📌 简介
Whisper等AED语音基础模型ASR性能优异，但在非语音、弱声学证据或 imperfect 标签输入下仍会输出流畅却无声学支撑的幻觉文本。本文提出AURA超高效表示编辑方法：冻结全部预训练权重，对解码器交叉注意力头施加稀疏缩放-平移编辑，并用三个交叉注意力不确定性特征（过度集中、熵弥散、帧间跳变）动态路由编辑强度。在非语音音频上无需预先识别幻觉头，将幻觉率从89.18%降至1.94%且不损坏干净语音WER；在imperfect标签语料上以约LoRA五百分之一的可训练参数量逼近其WER。

### 🔧 技术方案
**问题背景：** AED解码器自回归生成依赖内部语言模型，声学证据弱或缺失时仍可持续输出文本；已有头定向方法（如CALM-Whisper）需预先识别幻觉头，而静态表示编辑在每个token施加相同干预，无法应对幻觉的局部性。
**模型架构：** 冻结预训练模型，在每个解码器交叉注意力头输出上施加编辑：ã=(1+ĝ2·A)⊙a+ĝ1·v。有效门控为静态Hard-Concrete头选择门与动态不确定性门的乘积；动态门由max概率、归一化熵、argmax帧跳变三个因果特征经每头仅4参数的线性投影得到，实现"在哪编辑"与"何时激活"解耦，确认解码时编辑休眠、交叉注意力失稳时激活。
**核心创新：** (1)首次系统研究表示编辑作为ASR的超高效PEFT范式；(2)令牌级不确定性路由门控，联合学习稀疏头选择与编辑时机，免除头识别阶段；(3)编辑沿声学grounding路径置于交叉注意力，尊重AED-ASR的帧-令牌对齐结构。
**训练策略：** 标准ASR交叉熵损失加静态门期望L0稀疏正则，稀疏权重前10%步线性升至0.1；AdamW、批16、最多10k步；每头仅2d+6个可训练标量，Large-v3共85.8k参数。

### 📊 实验结果
**数据集**：AudioSet/DEMAND/MUSAN构成约105h非语音适配集，UrbanSound8K评幻觉，LibriSpeech test-clean/other评WER保持；MyST儿童语音（240h，unfiltered测试）、TED-LIUM 3（450h，unfiltered）、FluencyBank（5h不流利语音）。
**主要指标**：
- HRnorm：89.18%降至1.94%（15轮），25轮达0.93%
- MyST WER：14.2（Large-v3），优于LoRA 14.4与全量微调14.9
- TED-LIUM 3 WER：7.8，与LoRA 7.9持平
- FluencyBank WER：16.4（Medium），零样本32.0
**关键对比**：可训练参数85.8k对41.9M（1/500）；15轮幻觉率1.94%优于CALM报告的15.51%与头微调复现2.10%，且WER仅2.29/3.65（同点JoLA劣化至4.11/4.36）；对相同backbone的JoLA在15个数据-模型组合中13胜2平；消融显示熵特征贡献最大（去后+1.7）。不流利语音上仍逊LoRA约2.7个点，AURA+Enc证实编码器才是容量瓶颈。
**是否开源**：是，代码与模型已释出。

### ⭐ 评分：7/10
不确定性路由的动态门控是表示编辑方向的实质性推进，以五百倍参数效率逼近LoRA，并在非语音幻觉上显著超越CALM与头微调。实验诚实克制，主动剖析TED-LIUM空白段贡献与FluencyBank容量边界，交叉注意力可视化支撑机制解释。但幻觉仅在非语音场景直接度量，未覆盖语音LLM与流式解码，属扎实的增量式创新而非范式突破。

## [4] Listen, Critique, and Refine: RL-Based Self-Refinement for Instruction-Following Speech Synthesis

**arXiv ID**：2609.24163 | **方向**：语音大模型
**作者**：Chee-En Yu、Yi-Cheng Lin、Sung-Feng Huang、Yun-Shao Tsai、Ho-Lam Chung、Xuanjun Chen、Hung-yi Lee
**机构**：国立台湾大学电机/通讯工程研究所、NVIDIA Research、NTU AI研究中心
**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.24163 | **PDF**：https://arxiv.org/pdf/2609.24163.pdf | **代码**：https://github.com/Chee-En-Yu/ReflectTTS | **Demo**：暂无

### 📌 简介
指令跟随语音合成在需同时控制音高、语速、情感的复杂指令下，单遍生成常只实现部分属性。本文将自我反思推理范式首次扩展到音频token空间：单个大音频语言模型先生成语音草稿，"听"自己的输出并用文本 critiques 声学缺陷，再据此生成精炼版语音，形成生成-批评-精炼闭环。以GRPO强化学习训练，引入基于草稿改进量的refinement-aware奖励。InstructTTSEval上精炼输出相对提升7.15%，平均CLSP与LALM评审风格一致性较零样本分别提升6.5%、7.2%。

### 🔧 技术方案
**问题背景：** 文本LLM的自我精炼已证明无需外部评审即可提升生成质量，但音频生成领域模型必须先能"听"并批评自己的声学输出，此前音频推理（Audio-Reasoner、Step-Audio-R1等）仅限理解任务，推理链仍是文本。
**模型架构：** 基于Step-Audio-2-mini，统一词表内自回归交错文本与音频token，同一模型完成三步：首遍生成草稿语音v1；将v1作为音频输入生成文本批评c；以s、t、v1、c为条件生成精炼语音v2。音频detokenization用参考说话人池按性别关键词检索，缓解音色错配。
**核心创新：** (1)首个将模型自身生成的音频token作为推理轨迹用于生成任务的统一generate-critique-refine框架；(2)refinement-aware奖励：分析出GRPO组均值归一会使线性改进项Δ恒等抵消，改用tanh非线性变换保留相对改进信号；(3)奖励=CLSP风格对齐+λ·tanh(10Δ)−WER退化惩罚，兼顾风格、真实改进与可懂度。
**训练策略：** GRPO，组大小16，LoRA（r16/α32）微调，基座冻结作KL参考（β=0.05），批评每步on-policy重生成，vLLM侧车采样+NCCL同步，1000步，2×H200。

### 📊 实验结果
**数据集**：训练ParaSpeechCaps采样1000条；评测InstructTTSEval（APS/DSD/RP各1000条）。
**主要指标**：
- CLSP均值：0.538（零样本0.505、RL单跳0.527），弥合到真值差距64.7%
- Gemini-2.5-Pro风格一致性：65.9%（零样本61.5%、单跳64.2%）
- 人评指令遵循48.5、自然度54.7，较零样本相对提升24.4%、9.2%
关键对比：优于最强开源基线VoxInstruct（评审均值50.4）约2.6倍差距于零样本之上；OOD任务（APS/RP）CLSP较零样本提升7.1%，消融证明tanh奖励较线性再涨0.023均值CLSP。
**是否开源**：代码已开源。

### ⭐ 评分：7/10
首次把音频token级自我批评-精炼闭环引入指令TTS，填补推理范式在生成侧的空白；tanh奖励避免GRPO组内抵消的分析具有方法论价值且经验证。不足：绝对提升幅度温和（CLSP均值+0.033），精炼增益主要依赖RL后模型，基座与评审指标（CLSP/Gemini）单一，且人评跟随度仍远低于真值录音。

## [5] OmniEcho: Spatial Audio Understanding for Embodied Agents

**arXiv ID**：2609.23407 | **方向**：语音大模型
**作者**：Ruixun Liu、Yuxuan Wang、Jiacheng Xie、Yuhuan You、Donghua Cai、Junming Lin、Xiong-Hui Chen、Zhifang Guo、Yunfei Chu、Qize Yang、Xize Cheng、Jin Xu、Yiwu Zhong
**机构**：北京大学、阿里巴巴 Token Hub、清华大学
**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23407 | **PDF**：https://arxiv.org/pdf/2609.23407.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文聚焦具身智能体的空间音频理解问题：现有全模态大模型几乎只处理单声道语义音频，无法利用一阶高保真环绕声（FOA）线索对视野外或遮挡声源进行定位与导航。作者提出 OmniEchoBench——覆盖 6 类任务、基于 30 个真实环境采集、含 197 个场景、2972 条问答与 900 条导航样本的统一基准，并配套可控空间音频渲染管线合成人机视觉一致的百万级训练数据。模型 OmniEcho 在 Qwen3-Omni-30B-A3B 上并行接入 FOA 空间编码支路，三阶段训练。实验显示其音视频整体准确率 28.5，显著超过基座 18.5 与 SO-7B 的 11.4；声音引导导航 SR 达 16.2，逼近文本引导 VLN 方法。

### 🔧 技术方案
**问题背景：** 真实 FOA 数据采集昂贵且难标注；仿真数据须保持声源、视觉观测与智能体轨迹的几何一致性；如何将空间音频无损融入已有全模态预训练模型并保留其语义能力，此前缺乏系统方案与评测标准。
**模型架构**：以 Qwen3-Omni-30B-A3B 为主干，设双路音频编码：原生音频塔接收 W 通道下混的单声道信号以保留语义 token（冻结）；另设轻量 FOA 编码器，输入 5 通道表征（W 通道 log-mel 谱加三轴主动强度 ix、iy、iz 与扩散系数 delta），输出 384 维空间 token，重采样至 7Hz 音频网格后经可训练投影器嵌入 LLM，并插入对应语义音频 token 之后。
**核心创新：** (1) 首个面向全模态具身智能体的真实录音空间音频基准 OmniEchoBench，统一感知问答与声音导航两套评测；(2) 统一 FOA 渲染框架，由时变声源轨迹与听者位姿经球谐编码生成训练数据 36 万余条；(3) 三阶段训练策略，先语义对齐、再查询条件定位、最后冻结编码器嫁接主干。
**训练策略：** 第一阶段以 SigLIP 损失将 FOA 编码器对齐冻结 CLIP 文本编码器，使用 10 万条合成多声源场景；第二阶段加交叉注意力定位头回归方位角、俯仰角与距离，同时保留语义目标；第三阶段仅更新 LLM 与投影器，编码器、音频塔、视觉塔全部冻结，在 32 块 A100 上训练约 4 天。

### 📊 实验结果
**数据集**：OmniEchoBench-QA（2972 条真实场景问答）与 OmniEchoBench-Nav（30 个实景、12900 条 FOA 录音、900 条导航轨迹）；仿真导航在 VLN-CE R2R Val-Unseen 评测。
**主要指标**：
- 整体准确率（音视频）：28.5，对比基座 Qwen3-Omni 18.5，差值 +10.0；最强空间音频基线 SO-7B 为 11.4
- 音频单模态整体：21.8，超过所有单声道与 FOA 基线
- 导航 SR/SPL：16.2/11.5，与文本引导最强基线 InternVLA-N1（17.8/16.7）差 1.6/5.2，远超双耳音频 SoundSpaces（5.4/3.9）
- R2R 音频引导 SR：22.2，略超 Seq2Seq（21.0）与 CMA（22.0）
- 定位误差：方位 17.9 度、俯仰 7.7 度、距离 1.13 米，特征输入+第一阶段预热显著优于原始波形输入
**是否开源**：论文未给出代码地址，模型与数据开源情况暂未明确。

### ⭐ 评分：7/10
该工作首次把真实录制的 FOA 空间音频引入全模态具身模型，并同时建立感知与导航双基准，问题定义清晰、数据管线完整、消融充分，对社区有实质性推动。但整体准确率仍不足 30%，距离估计粗、Sim2Real 差距明显，导航性能与强文本方法尚存差距，且代码开源状态不明，限制了即插即用的实用价值。

## [6] Listen Then Reason: Perception-Grounded Test-Time Reinforcement Learning for Large Audio-Language Models

**arXiv ID**：2609.23589 | **方向**：语音大模型
**作者**：Jiaheng Dong、Xiaofeng Yu、Jean Honorio、Abhirup Ghosh、Hong Jia、Ting Dang
**机构**：墨尔本大学、奥克兰大学、伯明翰大学、ARC OPTIMA
**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23589 | **PDF**：https://arxiv.org/pdf/2609.23589.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
LALM 推理常依赖语言先验而非真实声学证据，且现有无标签测试时强化学习（TTRL）的多数投票奖励与模态无关，易强化语言捷径、加剧感知欠利用。本文通过注意力掩码量化逐层感知依赖，发现依赖峰值位于中间层，其与任务准确率（r≈0.51）及音频因果贡献（r≈0.59）正相关；据此提出感知接地 TTRL（PG-TTRL），以轨迹级声学接地分数校准 GRPO 优势，在 MMAR、MMAU 上最高提升 4.6 与 4.9 分。

### 🔧 技术方案
**问题背景**：MMAU/MMAR 显示 LALM 在需要声学感知的推理上仍薄弱；LVLM 研究证实多模态模型普遍依赖文本先验，LALM 沿用相同架构亦存在感知欠利用，而 TTRL 的伪标签优化会放大共享的语言侧捷径。
**模型架构**：以 Qwen2.5-Omni（3B/7B）为策略模型、冻结副本为参考模型，音频经编码器投影进入 LLM 表征空间；分析时对文本到音频的跨模态注意力施加掩码（置为负无穷），以原始与掩码两种条件下问题及选项 token 池化表征的余弦距离定义层级感知依赖。
**核心创新**：(1) 提出感知-推理边界层概念，证明峰值感知依赖与任务准确率及屏蔽音频后的性能下降量正相关，确立声学接地的因果价值；(2) 定义轨迹级接地分数 gi（full 与 mask 两次 teacher-forcing 逐 token 对数概率差均值）与声学接地边际 s（多数派与少数派 gi 之差），归一化映射为可靠性权重 r 介于 0.2 至 0.8；(3) 将 GRPO 优势改写为 Ai 等于 r 乘以投票边际（v 减 1/J），固定均匀基线保留共识题正信号，是首个感知接地的无标签 TTRL，不引入额外奖励项。
**训练策略**：冻结主干仅训 LoRA（r=8、α=16），每提示采样 8 条轨迹（温度 1.0、top-p 0.99），批大小 8，学习率 3e-6，KL 系数 0.05，负优势阻尼 0.4，全零优势组剔除，单轮训练，1 张 H100 加 1 张 A100 即可完成。

### 📊 实验结果
**数据集**：MMAR（1000 题，语音/声音/音乐/混合，16 子类）与 MMAU test-mini（1000 题，27 子类），更新阶段不使用任何真值标签。
**主要指标**：
- Greedy（MMAR，7B）：56.0，较 Base +2.8、较最强基线 TTRL +0.1
- Avg@8（MMAR，7B）：51.9，较 Base +4.6、较 TTRL +3.9
- Avg@8（MMAU，7B）：67.2，较 Base +4.9、较 TTRL +3.0
- Maj@8：提升有限，部分设置与 TTRL 持平
- Pass@k（1 至 8）：几乎全部采样预算下最强，小 k 增益最大，且避免了 TTRL 在大 k 时劣于 Base 的现象
逐层分析显示增益集中在后期层，说明其改善的是推理阶段的声学利用而非早期感知编码。
**是否开源**：论文未提供代码仓库，暂无。

### ⭐ 评分：7/10
首次系统量化 LALM 逐层感知依赖并给出因果关联证据，将接地可靠性注入 GRPO 优势的设计简洁即插、无需额外奖励网络，在两种模型规模与两个基准上一致有效，小采样预算优势具部署价值。但绝对增益温和、Maj@8 几乎无提升，相关性仅中等显著（p<0.1），实验覆盖窄且未开源，属实质性的扎实贡献而非范式突破。

## [7] ParA-LLM: A Unified Approach to Paralinguistic and Acoustic Speech Understanding

**arXiv ID**：2609.22771 | **方向**：语音大模型
**作者**：Nishit Anand、Jiaqi Su、Ke Chen、Yunyun Wang、Dinesh Manocha、Ramani Duraiswami、Rithesh Kumar、Zeyu Jin
**机构**：Adobe Research、马里兰大学帕克分校、OpenAI
**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.22771 | **PDF**：https://arxiv.org/pdf/2609.22771.pdf | **代码**：暂无（论文承诺发布模型、基准与数据） | **Demo**：https://nishitanand.github.io/paralinguistic-understanding-llm/

### 📌 简介
现有音频大模型在ASR上接近人类，但对副语言层面（说话人特质、表达变化、声学环境）理解薄弱：GPT-4o-Audio在自建基准仅36%准确率，而人类达78%。本文提出涵盖22项副语言特性的分类体系，通过声学仿真与模板/LLM生成构建120万条音频-QA数据，采用"原子属性到多属性联合"的两阶段课程训练ParA-LLM，并发布6000题的ParA-Bench。ParA-LLM总准确率43.53%，超GPT-4o-Audio 7.5个百分点，并在MMAU-Pro与MMAR语音子集分别提升1.13%与7.49%。

### 🔧 技术方案
**问题背景：** 音频LLM擅长回答"说了什么"，却难以刻画"怎么说的"。混响、噪底、音色、语速、情感等副语言信息长期被拆成单属性分类器（如Vox-Profile），缺乏跨属性联合的自由问答能力，且缺少系统性评测基准。
**模型架构：** 以Qwen2-Audio-7B-Instruct为底座，在音频编码器、多模态投影器与LLM三部分注入LoRA（rank 128、alpha 256、dropout 0.1），面向22个特性（10声学+7说话人固有的+5话语级语音）支持多属性自由问答。
**核心创新：** (1) 客观化特性体系：声学属性用DRR、RT60、ERR、DER、SNR、STOI等信号指标离散分档，说话人与语音属性用多数投票一致的语义标签，规避主观标注不一致。(2) 仿真数据引擎：以EARS、Emilia、Expresso、VoxCeleb干净语音卷积MIT IR Survey与EchoThief实测RIR（15类混响），叠加TAU等场景噪声（21类噪声、多档SNR），再施加削波、动态压缩、过载等后期效果，产出70万+带元数据音频并类均衡。(3) 两阶段课程数据配方：68.8万条模板生成的单属性QA打底，51.3万条Qwen2.5-7B经ICL生成的多属性QA练联合推理；ParA-Bench改用异构模型Mistral-Small-3.2生成以消除自参照偏差，300题人工核验。
**训练策略：** 两阶段各训1 epoch，学习率5e-5与4e-5，余弦调度加AdamW，8张A100、总批量128；阶段二加载阶段一LoRA适配器继续训练。

### 📊 实验结果
**数据集**：ParA-Bench（6000道多选，说话人-语音、声学、混合各2000题，测试集音频/RIR/噪声与训练严格不相交）；另以MMAU-Pro Speech与MMAR验证泛化。
**主要指标**：
- ParA-Bench总准确率：43.53%
- Speaker-Speech：55.85%（全场最优）
- Acoustic：34.80%（低于GPT-4o-Audio的41.85%）
- MMAU-Pro Speech：42.09%（较基线+1.13）
- MMAR Speech：42.86%（较基线+7.49）
**关键对比**：总准确率超最强基线Voxtral（38.80%）4.73个百分点、超GPT-4o-Audio（36.03%）约7.5个百分点；Qwen2.5-Omni仅14.47%、Mellow仅3.67%，说明多模态与显式推理机制均未带来副语言增益。与人类78%相比仍有约34个百分点差距。
**是否开源**：承诺发布ParA-LLM、ParA-Bench与全部数据，代码仓库当前暂未公开。

### ⭐ 评分：7/10
系统性突出：22维特性体系、仿真数据引擎、课程训练与全新基准四位一体，将副语言理解从单属性分类推进到多属性联合自由问答，且在第三方基准上有可验证的泛化增益。不足在于绝对性能仍远低于人类水平，声学单项逊于GPT-4o-Audio，训练与评测数据均源于同源仿真，真实录音泛化性存疑，属扎实的工程与数据贡献而非范式突破。

## [8] TTS-Guard: Black-Box Ownership Verification of Text-to-Speech Models via Adaptive Adversarial Speaker-Pair Fingerprints

**arXiv ID**：2609.23729 | **方向**：语音大模型
**作者**：Xubin Yue、Zhenhua Xu、Zhebo Wang、Mengting Li、Zijie Zhou、Wenpeng Xing、Dezhang Kong、Meng Han
**机构**：浙江大学、浙江大学滨江研究院、北航杭州创新研究院、GenTel.io、中国石油大学（北京）
**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23729 | **PDF**：https://arxiv.org/pdf/2609.23729.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
零样本TTS使高保真声音克隆泛滥，专有模型被窃取后经微调、量化、蒸馏洗白转售的黑市兴起，而TTS模型级版权验证长期空白。本文提出TTS-Guard，首个面向TTS的黑箱所有权验证框架：模型属主在关键说话人对的参考音频上优化对抗扰动构成"说话人对指纹"，向疑似API提交该音频并检验合成结果是否被误判归属目标说话人，以此证明衍生关系。在五个主流TTS上平均指纹成功率FSR达96.4%、单查询误报率FPR为5.8%，K=20多查询决策级FPR收紧至4.7%，同时保持可懂度与自然度。

### 🔧 技术方案
**问题背景：** 语音是连续波形，信号层指纹极易被重采样、MP3/Opus编码、DRC、EQ等常规处理抹除，且人耳听觉感知预算远严于视觉，图像水印与LLM指纹无法直接移植。零样本TTS显式依赖说话人嵌入条件，掌控该嵌入流形即可控制输出身份归属，故作者将防御性对抗扰动反转为进攻性版权信号。
**模型架构：** 三阶段管线：阶段一在Resemblyzer与ECAPA-TDNN两个架构互斥的嵌入空间联合最小化L2距离（α=0.5），选出声学相邻且跨验证器可迁移的关键说话人对KSP；阶段二自适应课程影子优化ACSO，按LoRA微调、30%/50%剪枝、INT8/INT4量化、0.5倍蒸馏student四级逐步扩展影子模型集合并优化加性扰动；阶段三黑箱验证以随机文本提示多次查询聚合判定。
**核心创新：** (1)双空间KSP选择并给出首个基于Bhattacharyya距离的FSR信息论下界，实测预测界差距仅1-2个百分点；(2)ACSO课程覆盖整个衍生模型流形，消融显示缺它蒸馏后FSR由0.62崩至0.32；(3)解耦斥力损失最大化非目标模型嵌入距离，将FPR压至取证可用水平。
**训练策略：** Adam优化500步，初始学习率0.1每50步衰减0.8；总损失为目标吸引项、非目标斥力项与L2/SNR/Bark尺度心理声学掩蔽质量项加权和，单张A800 GPU完成指纹生成。

### 📊 实验结果
**数据集**：LJSpeech（LoRA影子训练）、LibriTTS 100人+VCTK 50人（KSP候选池）。
**主要指标**：
- FSR（平均）：96.4%
- 单查询FPR：5.8%；决策级FPR：4.7%（K=20）、≤0.5%（K=40）
- STOI：0.822；NISQA-MOS：3.87，与干净参考差≤0.05
**关键对比**：对比跨域移植的IPGuard与指令指纹IF，基线干净FSR仅0.78/0.86，蒸馏后崩至0.31/0.40、De-AntiFake净化后0.38/0.44（本方法为0.62/0.83），FPR高至0.19/0.13。十种音频攻击下MP3 32kbps仍FSR≥0.69；六种模型修改平均FSR≥0.70（LoRA 0.93、INT8近无损）；换用ECAPA/ERes2Net/WavLM验证器FSR≥0.92（WavLM最坏0.82）；去除解耦损失FPR由0.058升至0.187。
**是否开源**：暂无。

### ⭐ 评分：7/10
首次将模型级所有权验证系统落地到语音合成，问题定义、双空间KSP、课程影子优化、统计校准与信息论下界形成完整闭环，评测覆盖五模型十攻击六修改两净化器并含P.808主观听测与操作点表，取证导向扎实。扣分在于对抗查询范式移植自IPGuard、方法学原创性中等，且威胁模型排除替换内部说话人编码器，风格迁移TTS可旁路使FSR降至0.55，载体假设随范式演进而承压。

## [9] StreamTN: A Low-Latency Streaming Chinese Text Normalization Model for Streaming TTS in Dialogue Systems

**arXiv ID**：2609.24267 | **方向**：语音大模型
**作者**：Wenhao Li、Jinrui Liang、Haoyu Zhang、Jingbin Hu、Xiaming Ren、Hanke Xie、Huakang Chen、Chengyou Wang、Dake Guo、Linhan Ma、Su Feng、Houdun Liu、Yunxiang Chen、Lei Xie
**机构**：西北工业大学语音与语言处理组（ASLP@NPU）；深圳皮美科技有限公司
**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.24267 | **PDF**：https://arxiv.org/pdf/2609.24267.pdf | **代码**：暂无（承诺随论文发表释放模型与基准） | **Demo**：https://supernova-neko.github.io/Stream-TN/

### 📌 简介
级联语音对话系统中，LLM生成的文本含大量非标词，送入流式TTS前必须完成文本规范化（TN）；规则方法泛化差，LLM提示方法首包延迟高且易幻觉。本文提出基于Qwen3-0.6B的轻量中文流式TN模型StreamTN，采用双流流式架构，用token延迟参数显式控制首包延迟。4帧配置下Micro-F1达0.8937、模型侧首包延迟仅213毫秒，并构建覆盖14类的对话TN基准（95793条训练、1262条测试），兼顾精度与延迟。

### 🔧 技术方案
**问题背景：** 级联对话系统中上游LLM按token流式输出，下游流式TTS要求TN增量产出规范化文本。离线TN需等完整句子，推高端到端延迟；规则系统依赖人工工程且难以覆盖未见模式；提示式LLM不稳定、有幻觉，微调核心LLM又会损伤其推理能力。

**模型架构：** StreamTN位于LLM与TTS之间，基于Qwen3-0.6B复用其嵌入表与因果Transformer。原始输入轨与规范化输出轨经嵌入逐位相加融合为单序列，delay与pad对齐符号以零向量实现，保持标准自回归解码与KV缓存兼容。

**核心创新：** (1)双流延迟生成建模：输出轨相对输入轨延迟d步，模型接收前d个原始token即开始规范化，实现部分上下文下的流式分解与可控前瞻；(2)端到端首包延迟分解：将FPD拆为上游LLM等待时间与TN自身计算时间，独立度量模块内在延迟；(3)对话导向TN数据管线：在FlatTN十分类基础上合并并新增化学式、数学公式等四类科学表达，共14类；以DuReader真实文本加Qwen3-32B生成科学语料，DeepSeek-R1-70B产出规范化目标，抽样人工核验一致率98.2%。

**训练策略：** 全参数微调，学习率1e-5经余弦退火至1e-6，训练5000步，4张A6000动态批处理；仅对有效目标token计算负对数似然；推理用贪心解码，5个随机种子重复取均值加减标准差；消融显示LoRA严重掉点。

### 📊 实验结果
**数据集**：自建中文对话TN基准，95793条训练、1262条测试，覆盖数字、日期、时间、电话号码、单位、化学式、数学公式等14类。
**主要指标**：
- Micro-F1：0.8937±0.0009（4帧，FPD 213ms）；Micro-P：0.8931
- 非流式上限Micro-F1：0.9639；延迟1帧增至16帧，F1从0.7030升至0.9239，FPD从75ms增至756ms
- 分类别：物理单位0.977最优，复杂数学公式0.750、化学式0.791最难
**关键对比**：最强基线为离线BiLSTM（F1 0.8941），StreamTN仅低0.0004但精确率高2.5个百分点（0.8931对0.8677）且支持流式增量处理；显著优于规则基线WeTextProcessing（0.7853）、FlatTN（0.7569）与提示式Qwen3-0.6B（0.4872）。
**是否开源**：模型与基准承诺随发表释出，当前仅demo页，暂无代码仓库。

### ⭐ 评分：7/10
切中LLM级联语音对话的真实工程痛点，双流延迟建模以极简改动让0.6B模型获得可控流式TN能力，精度-延迟权衡量化清晰、5种子方差小，14类基准填补对话TN评测空白。不足：选定操作点未超离线BiLSTM，最难的公式化学类仍弱，训练数据主要由大模型生成清洗、独立泛化验证有限，且代码与基准尚未释出，故评7分。

## [10] Beyond Encoder Fusion: Multi-View Discrete Token Augmentation for LLM-Based ASR

**arXiv ID**：2609.23525 | **方向**：语音大模型
**作者**：Paul Moïse Gangbadja、Mickael Rouvier、Fabrice Lefevre
**机构**：阿维尼翁大学 LIA 实验室（法国）；EDL
**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23525 | **PDF**：https://arxiv.org/pdf/2609.23525.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
基于离散语音 token 的大模型 ASR 对编码器选择高度敏感，而已有多编码器方法在输入层融合编码器输出，既不稳定又需多编码器推理。本文提出多视角离散 token 增强：把冻结的 HuBERT、WavLM、MMS-300M 视为同一语音的替代分词器，生成多种 token 视角联合训练一个共享 LLM 解码器，推理仅用单编码器即可。LibriSpeech 上全部视角超越独立基线，WavLM 视角达 test-clean 3.30%、test-other 8.13% WER；ROVER 组合进一步降至 3.03%/7.38%。预算匹配对照证明增益源于编码器多样性而非数据量。

### 🔧 技术方案
**问题背景：** 离散 token 可直接并入 LLM 词表、序列短且训练省，但单 tokenization 系统继承单一编码器的偏置；现有方法或量化前拼接 embedding（早融合）或量化后合并 token 流（晚融合），测试时需多编码器且效果不稳定。
**模型架构：** 波形经冻结 SSL 编码器提取帧级特征，K-means（K=2000）量化、连续去重、BPE（词表 6000）压缩，输入 Qwen2.5-0.5B 解码器（LoRA r=16 微调）自回归输出文本。三个编码器：HuBERT-Large 与 WavLM-Large 取第 24 层，MMS-300M 经 CTC 探针选第 15 层。
**核心创新：** (1) 多视角 token 增强：不在输入层融合，将 LLM 词表按编码器划分为三个互斥 BPE 块，样本前缀 encoder 身份标签以选择词表块并路由嵌入；(2) 训练时多样性正则：同一转写配三种 tokenization 共享参数训练，类似子词正则但视角差异来自模型偏置而非随机噪声，推理保留单编码器成本；(3) 输出互补性复用：测试可三视角各解码一次，用置信度加权 ROVER 在假设层再融合。
**训练策略：** LibriSpeech 960h 上以 3N 视角训练，共 5 epoch，AdamW、lr 2e-4、余弦调度、有效 batch 16；loss 仅算文本 token；推理 5 beam、重复惩罚 1.2。

### 📊 实验结果
**数据集**：LibriSpeech 960h（train、test-clean/other）与 Loquacious dev（泛化测试，剔除 YODAS）
**主要指标**：
- test-clean WER：3.30%（多视角 WavLM 视角，相对基线降 0.78 点）
- test-other WER：8.13%（相对基线降 1.42 点）
- ROVER 三假设融合：3.03% / 7.38%（全文最优）
- Oracle：2.39% / 5.96%；Loq. dev†：20.28%
最强基线为早融合 HuBERT⊕WavLM（3.55%/8.48%），多视角以单编码器推理成本仍全面超越；晚融合各变体不稳定。W-3x 同编码器重复对照达 4.99%，确认增益来自视角多样性
**是否开源**：未发布训练代码或模型，仅使用 NIST SCTK 等公开工具

### ⭐ 评分：7/10
思路简洁优雅，把子词正则迁移到语音离散 token 空间，用重复/预算/成对三类对照严谨地隔离了"多样性 vs 数据量"，且推理零额外成本。不足在于属受控概念验证：仅 0.5B 小模型与 960h 朗读语料，未验证连续表示与更大 LLM 场景，YODAS 域崩至 95%+ WER 暴露泛化短板，绝对性能距 Whisper 系大模型仍有差距。

## [11] MECT: Mixture of Experts with CNN-Transformer Network for Speaker verification

**arXiv ID**：2609.24061 | **方向**：语音大模型；**作者**：Yu Zheng、Jinghan Peng、ChangHao Zhang、Jian Liu（通讯）、Weiqiang Wang；**机构**：蚂蚁集团机器智能部（Ant Group, Machine Intelligence）；**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.24061 | **PDF**：https://arxiv.org/pdf/2609.24061.pdf | **代码**：https://github.com/ant-research/AntSpeaker | **Demo**：暂无

### 📌 简介

说话人验证全监督模型此前从未引入混合专家机制。本文提出MECT，首个在CNN-Transformer骨干中集成MoE的全监督SV模型，系统比较句子级/帧级与稠密/稀疏四种路由方案，仅增加0.17M参数即较无MoE基线取得平均EER相对提升4.7%、minDCF提升7.8%。MECT-B2（9.57M参数）在VoxCeleb1刷新SOTA，Vox1-O/E/H minDCF达0.012/0.026/0.048，以约1/60参数量超越587M的w2v-BERT 2.0微调模型；并通过因果重训练实现100ms分块的流式嵌入提取，EER接近离线水平，部署价值突出。

### 🔧 技术方案

**问题背景：** 现有SV中的MoE仅用于自监督预训练模型的层间融合微调，全监督端到端模型尚未利用动态专家路由；同时流式嵌入提取在短分块下性能严重退化。

**模型架构：** 基于ReDimNet的reshape-dimension策略，每个MECT块由CNN（ResNet）与带MoE的Transformer组成，经reshape与time-pooled维度重排连接；输入80维fbank，四个stage堆叠后经加权dense层融合，ASTP聚合得192维嵌入，SphereFace2损失训练；按通道数C与ResBlock数M派生A1/A2/B1/B2四种规模，B2为9.57M参数、14.43 GMACs（2秒语音）。

**核心创新：** (1) 首次将MoE引入全监督SV，把四种专家粒路与Top-K稀疏变体置于Transformer FFN首层线性投影处，帧级稠密4专家在VoxCeleb最优，Top-K稀疏在CN-Celeb更优；(2) 块结构改造：残差加于BN与ReLU之后、两层1D卷积位置编码、下sampling与通道扩展并入ResNet卷积、以简单shortcut替代dense connection，训练更稳且省算力；(3) 流式范式：将卷积改左侧padding、MHA加因果mask后重训练，推理时Conv2d缓存2/6帧、Conv1d缓存112帧、维护KV与ASTP统计缓存，100ms块即近离线精度；可视化显示专家自发按音素特化（擦塞音归E2、元音归E0）。

**训练策略：** 两阶段方案。第一阶段全量训练：速度扰动2倍扩张、MUSAN噪声与RIR混响增强，SGD动量0.9，学习率升至0.6再退火至4e-4，margin由0渐升至0.2；第二阶段大间隔微调（LMF）：去除速度扰动、截取6秒段、margin固定0.3、低学习率7轮。CN-Celeb沿用同配方。

### 📊 实验结果

**数据集**：VoxCeleb2开发集（另加VoxBlink2设置）训练，VoxCeleb1-Cleaned与Vox21-val评估；CN-Celeb1/2开发集训练，CN-Celeb Test评估。

**主要指标**：
- Vox1-O minDCF：0.012（EER 0.22%）
- Vox1-E minDCF：0.026（EER 0.28%）
- Vox1-H minDCF：0.048（EER 0.52%）
- CN-Celeb EER：4.87%（minDCF 0.297）
- 流式100ms块 Vox1-O EER：0.38%

关键对比：MECT-B2以更低参数超越最强监督基线ReDimNet2-B6，Vox1-H minDCF相对提升14.1%；联合VoxBlink2训练后较w2v-BERT 2.0（587M）平均EER/minDCF相对改善10.3%/24.4%，为当前VoxCeleb1最优；CN-Celeb较ReDimNet2-B6 EER领先0.35个点；流式消融中embedding平均与特征拼接在100ms块退化至12.34%/7.50% EER，因果重训练几乎无损。

**是否开源**：是，代码见github.com/ant-research/AntSpeaker。

### ⭐ 评分：7/10

首次将MoE引入全监督说话人验证，四种路由消融系统扎实，帧级稠密MoE近零参数代价换取稳定增益；9.6M参数刷新VoxCeleb1-Cleaned SOTA，效率突出；因果重训练流式方案100ms即近离线，工程落地价值高；专家按音素自发特化提供了可解释性亮点。不足在于相对同规模非MoE基线增益偏温和，CN-Celeb优势依赖稀疏结构、跨数据一致性一般，故属实质进展而非范式突破。

---

## 语音前端

## [12] EquiSELD: Efficient training of equivariant sound event localization and detection networks

**arXiv ID**：2609.23156 | **方向**：语音前端；**作者**：Goksenin Yuksel、Marcel van Gerven、Kiki van der Heijden；**机构**：拉德堡德大学Donders研究所；哥伦比亚大学Zuckerman研究所；**发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23156 | **PDF**：https://arxiv.org/pdf/2609.23156.pdf | **代码**：https://github.com/labhamlet/equiSELD | **Demo**：暂无

### 📌 简介
一阶 ambisonics（FOA）信号具有严格的O(3)旋转反射对称性，但现有声事件定位与检测（SELD）方法要么靠旋转增广近似学习该对称性，要么使用计算昂贵的SO(3)等变网络，无法处理同类重叠声源且未利用反射对称。本文提出EquiSELD，首个对完整O(3)群精确等变的SELD注意力网络：将每个时频token处理为"O(3)不变标量+等变声强向量"双流，经Multi-ACCDOA读出不变活动强度与等变DOA。在仿真TAU2021与真实录制STARSS23上以2.25M参数取得综合分ℰS=0.40与0.56，超越所有基线，训练耗时仅为既有等变网络CGNet-STS的约1/19。

### 🔧 技术方案
**问题背景：** SELD系统普遍以FOA为输入，但多用非等变CNN/Transformer，依赖旋转数据增广统计性学习对称约束，浪费数据与算力；已有的群等变方案基于CG积网络，仅保证SO(3)等变、计算开销大，且输出结构不支持同类重叠声事件。
**模型架构：** 每帧提取64 mel频带token，各含5个不变标量（W/B对数带能、主动/反应声强范数及二者余弦相似度）与2个等变声强向量。主干为等变注意力块：频带注意力、ISAB/PMA池化、时间与轨道注意力；标量流经LayerNorm与GELU，向量流经无偏置线性混合与Frobenius范数RMS归一化；输出头合成每类K=3轨的Multi-ACCDOA目标。
**核心创新：** (1) 精确O(3)等变参数化：注意力权重与全部非线性仅由不变标量和向量范数计算，向量仅用跨坐标共享权重的线性映射混合，实测等变偏差2.8e-7；(2) 将标量-向量双流等变注意力引入SELD，2.25M参数比CGNet-STS少2.9倍；(3) 设计匹配参数的SO(3)-only变体与非等变AttnSELD/AttnSELD+，分离量化反射对称与等变约束的独立贡献。
**训练策略：** ADPIT损失+Multi-ACCDOA，5秒片段；AdamW（lr 3e-4、wd 0.05、beta 0.9/0.95），2000步线性warmup+余弦退火至1%，梯度裁剪1.0；TAU2021训100轮、STARSS23训200轮，无需任何方向增广。

### 📊 实验结果
**数据集**：TAU2021（实测RIR仿真动态场景，fold1-4训练/5验证/6测试）与STARSS23（真实录制，最多6源重叠）。
**主要指标**：
- TAU2021 ℰS：0.40（最强基线SELDNet+ 0.47、CGNet-STS 0.51，差-0.11）
- STARSS23 ℰS：0.56（SELDNet+ 0.60、CGNet-STS 0.72，差-0.04/-0.16）
- TAU2021：LE 16.4°、F20° 49.8%、LR 63.9%、ER 0.64
- 成本：0.77 GPU时（单A100），约为CGNet-STS的1/19；精确等变，74个O(3)元素下得分0.56±0.00
等大约束的AttnSELD显著更差（STARSS23 ℰS 0.70），加O(3)增广可追近（0.58）但成本翻倍；EquiSELD检出12/13类，数据从100分钟扩到400分钟时ℰS由0.55单调降至0.40，验证等变优势随规模扩大。
**是否开源**：代码与模型已开源。

### ⭐ 评分：8/10
首次将精确O(3)等变性嵌入SELD，架构严谨、训练成本数量级下降、方向鲁棒性有数学保证，且通过SO(3)匹配变体与非等变对照系统归因，实验设计堪称典范。不足在于反射对称独立收益有限、真实场景与增广基线差距较小、仍受限于FOA低阶输入。属实质性强、可复现推广的架构创新。

## [13] Bearings: Self-Supervised Soundfield Embeddings from First-Order Ambisonics

**arXiv ID**：2609.23152 | **方向**：语音前端 | **作者**：Goksenin Yuksel, Marcel van Gerven, Kiki van der Heijden | **机构**：拉德堡德大学 Donders 机器学习与神经计算系；哥伦比亚大学 Zuckerman 脑行为研究所 | **发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23152 | **PDF**：https://arxiv.org/pdf/2609.23152.pdf | **代码**：https://github.com/labhamlet/Bearings | **Demo**：暂无

### 📌 简介
主流自监督音频编码器只回答"是什么"而缺失"在哪里"，对空间近乎失明。本文提出 Bearings，一个从无标注一阶环绕声（FOA）中学习可复用声场嵌入的自监督框架：以掩码自编码方式重构方向分布与双时间尺度扩散度，解码器交叉注意冻结单通道编码器的声学嵌入。所得声场嵌入经轻量融合头即可直接接入任意冻结声学编码器，无需重训任一模型，使 SELD 的定位相关 F 分数从 4 以下跃至 50.4（TAU-NIGENS 2021）与 38.9（STARSS23），是首个可与冻结编码器即插即用的自监督声场编码器。

### 🔧 技术方案
**问题背景：** 通用自监督音频表征（BEATs、Dasheng 等）仅建模单声道内容；现有空间音频预训练（w2v-SELD、GRAM-Ambisonics、BAT）把空间与声学纠缠于单一骨干并绑定特定 SELD 配置，空间表征难以复用到不断更新的冻结声学编码器上。

**模型架构：** 输入为 7 通道时空频特征：B00 与三个方向通道的 4 张 log-mel 谱（128 mel 带）及按频带归一化的 3 维主动强度向量。声场编码器为 6 层 ViT（宽度 384，1090 万参数），2D 卷积分块加正弦余弦位置编码；4 层解码器先自注意、再交叉注意冻结 GRAM-Clean 的单声道嵌入，在掩码位置预测方向与扩散度。

**核心创新：** (1) 声学条件化掩码重构：以冻结单声道内容嵌入为条件重构空间场，迫使表征专注空间结构；(2) 解析式监督目标：方向项在 256 点 Fibonacci 球面网格上用 von Mises-Fisher 核密度构成分布并以能量加权交叉熵监督，扩散度项采用 DirAC 公式、约 50ms 与 350ms 双时间尺度 L1 回归；(3) 模块化可插拔：双编码器全冻结，仅训练 130 万至 190 万参数的融合投影与 SELDNet 式头即可跨架构嫁接定位能力。

**训练策略：** 在 YT-AmbiGen（360°YouTube 视频爬取的约 10.2 万条 5 秒 FOA 片段）预训练 5 万步，AdamW、批 256、峰值学习率 2e-4、余弦衰减；80% 管状掩码（40% 整时间轴、20% 随机块、40% 右侧截断未来帧），每片段随机取两个 2 秒裁剪。

### 📊 实验结果
**数据集**：TAU-NIGENS 2021（实测 RIR 合成的动态混响场景）与 STARSS23（真实 Ambisonic 阵列录音，按 DCASE2023 任务 3 基线协议）；另在 Matterport3D 仿真房间做定位与 RT60 探针。
**主要指标**：
- TAU-NIGENS 2021（GRAM-Clean 融合）：F20° 2.8→50.4，ER20° 0.83→0.55，LE_CD 102.1°→19.3°
- STARSS23：F20° 2.5→38.9，ER20° 0.83→0.51，LE_CD 147.8°→22.0°
- 对比联合预训练 GRAM-Ambisonics：TAU-NIGENS 全指标胜出（F20° 50.4 对 41.0），STARSS23 基本持平；对比监督 SELDNet：两数据集除 LE_CD 持平方差全优于
- 消融：预训练冻结优于从头端到端（F20° 50.4 对 35.7）；25% 标签时仍比域内基线高 41%（F20° 30.6 对 21.7）；去方向损失使探针 DOA 误差 16.1° 恶化至 49.2°
**是否开源**：代码与模型已开源于 GitHub（labhamlet/Bearings）。

### ⭐ 评分：7/10
理由：首个可即插即用于冻结声学编码器的自监督声场表征，以 DirAC/主动强度解析目标实现空间与内容解耦，SELD 增益巨大并超越监督基线，消融、标签效率与探针验证充分；但绝对性能未达 DCASE 冠军系统，方向监督本质是手工空间线索的蒸馏，任务与数据规模较窄，属实质性强贡献而非范式突破。

## [14] Generative Learning for Ambisonic Upscaling

**arXiv ID**：2609.23479 | **方向**：语音前端 | **作者**：Amit Milstein、Nir Shlezinger、Boaz Rafaely | **机构**：以色列本古里安大学ECE系 | **发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.23479 | **PDF**：https://arxiv.org/pdf/2609.23479.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
Ambisonic上混（AU）长期由确定性方法主导：混响中扩散声场破坏方向稀疏假设，使模型基与判别式网络的输出出现空间模糊、性能骤降。本文将AU重构为给定低阶观测下高阶球谐分量的条件生成问题，首次系统比较两大连续时间范式——得分模型（SGM）与流匹配（FM）。混响HARP测试集上FM高阶通道平均STFT-SDR达7.53 dB，较最强判别基线CTN（4.90 dB）高2.63 dB，方向角误差低至0.45度；主观MUSHRA测试中FM感知质量与真值HOA3无显著差异，且仅需3步采样。

### 🔧 技术方案
**问题背景：** AU从低阶信号恢复高阶成分（本文FOA→三阶HOA），是欠定线性逆问题：截断选择矩阵的伪逆把能量均匀摊到空间域造成模糊；混响晚期反射更使平面波稀疏与确定性回归双重失效。
**模型架构：** 主干部采用NCSN++（隐藏维256，约2.62亿参数）并改造为多通道输入；信号经STFT、压缩幅度变换（α=0.5、β=0.15）及实虚部通道拼接送入网络；生成过程只合成缺失的12个二、三阶通道，再与实测FOA级联输出HOA3，条件即为低阶时频观测。
**核心创新：** (1)生成式AU表述：对高阶通道做条件后验采样而非均值回归，适配混响下随机空间结构；(2)连续时间双范式对比：SGM用VE-SDE与P-C采样（50次函数评估），FM用OT线性路径确定性ODE（仅3次评估）；(3)定向重建策略：完全保留物理可靠的低阶观测，生成算力集中于欠定高阶部分，FM训练采用log(1+t)加权损失提升稳定性。
**训练策略：** 以MOTUS实测与HARP仿真的1-4个球谐RIR卷积WSJ0干语音构成约100小时2秒@16kHz样本，N3D归一化、三阶；随机源增益与声场旋转增强保证旋转不变性；小批量SGD训练并用EMA维护推理权重影子。

### 📊 实验结果
**数据集**：与训练零环境重叠的HARP模拟RIR（T60 0.1-1.25s、DRR -5~10dB、约2小时）与MOTUS实测（T60 0.5-1.0s、DRR -5~0dB），另设消声1-4人对照组；基线含CTN、级联GRU（单向/双向）、PWD-CS、HO-DirAC、COMPASS。
**主要指标**：
- STFT-SDR（混响HARP四人数平均）：FM 7.53 dB，较CTN（4.90）+2.63、较SGM（4.69）+2.84、较COMPASS（3.27）+4.26 dB
- STFT-SDR（消声平均）：FM 15.03 dB优于CTN 10.97，SGM因随机噪声注入反降至10.02
- Δσ（低DRR段单源）：FM 0.45度 vs CTN 2.61度、FOA输入4.68度；ΔDI为SGM最优（0.23 dB）
- 相干性：生成模型全频段平稳，判别模型高频显著退化；性能瓶颈为DRR而非T60
- MUSHRA（11人经验听音）：FM与真值HOA3无显著差异（p=0.837），显著优于PWD-CS（p=0.013），CTN存在咔哒伪影
**是否开源**：未发布代码与音频demo；所用MOTUS、HARP、WSJ0数据均公开可用。

### ⭐ 评分：7/10
将AU从确定性回归重构为条件生成并提出"保留实测低阶、只生成欠定高阶"的通道级策略，问题表述扎实；FM/SGM系统对比与客观+主观双轨评估证据充分，3步ODE采样与感知逼近真值的结果尤有说服力。不足在于主干净用NCSN++原创性有限，2.62亿参数离实时部署尚远，且仅限RIR合成语音场景，属实质进展而非范式突破。

## [15] P2Flow: Phoneme-aware Progressive Flow Matching for Extreme Speech Super-Resolution
**arXiv ID**：2609.24138 | **方向**：语音前端 | **作者**：Ningyuan Yang, Yize Li, Pu Zhao, Diego A. Cuji, Kanad Sarkar, Ryan M. Corey, Xue Lin, Andrew C. Singer | **机构**：Stony Brook University、Northeastern University、UIUC、UIC | **发布日期**：2026-09-22 | **论文**：https://arxiv.org/abs/2609.24138 | **PDF**：https://arxiv.org/pdf/2609.24138.pdf | **代码**：https://github.com/ningyuan33/P2Flow | **Demo**：暂无

### 📌 简介
生成模型在语音超分辨（SSR）中潜力显著，但现有工作集中于标准或通用设定，1/2 kHz→16 kHz 的极端带宽受限场景几乎空白，当前方法在此出现显著性能崩塌。本文提出 P2Flow，一个音素感知渐进流匹配框架：以 HuBERT 音素后验引导补全缺失高频，配合分频带渐进重建与声码器后训练。在 TIMIT、VCTK 的 2 kHz→16 kHz 设定下取得 LSD 0.935、ViSQOL 3.954、STOI 0.908，多项指标全面超越代表性基线，达 SOTA。

### 🔧 技术方案
**问题背景：** 判别式 SSR 易过平滑，扩散/GAN/FM 等生成式方法多面向 8 kHz 以上输入；当输入限至 1–2 kHz 时声学线索严重不足，现有模型明显退化，而该场景对骨传导拾音等应用极为关键。
**模型架构：** 在 80 维 mel 域做条件式少步 FM：将流状态、LR mel、音素后验拼接线性投影后送入三个级联 Transformer（4/2/2 层，隐维 1024，含自适应 RMSNorm、RoPE 自注意力与 GEGLU），每个模块接速度头分别预测 0–2/2–4/4–8 kHz 频段，波形由 HiFi-GAN 合成。
**核心创新：** (1) 音素引导：用与 SSR 输入同分布退化的语音训练 HuBERT+线性头音素分类器，产出 39 类帧级后验条件化 FM，后验保留不确定性，比硬标签更鲁棒；(2) 渐进建模：将超难的全带恢复分解为低中高三个频带的递进估计，后续模块利用已精化表示，倒金字塔层分配把容量优先给不确定性最大的首阶段；(3) 声码器后训练：冻结 FM，用对抗+特征匹配+MR-STFT 损失在估计 mel 上微调 HiFi-GAN，弥合自然 mel 与生成 mel 的分布差异。
**训练策略：** 分类器 20 轮；FM 训练 40 万步、批 128、lr 3e-4；声码器微调 20 轮、损失权重 (1,10,1)、三档 STFT 分辨率；推理默认 5 步 ODE；单张 RTX A6000 完成全部实验。

### 📊 实验结果
**数据集**：TIMIT（官方划分）与 VCTK（100/8 说话人划分），均为 1 kHz 与 2 kHz→16 kHz 极端设定，LR 输入由切比雪夫低通加降采样合成。
**主要指标**：
- LSD：0.935（TIMIT 2k→16k），较最强基线 AP-BWE 0.998 低 0.063
- ViSQOL：3.954，较 FLowHigh 3.712 高 0.242；STOI：0.908，较 AP-BWE 0.875 高 0.033
- VCTK 同样全面领先：LSD 0.979、ViSQOL 3.913；1k→16k 的 STOI 0.849 大幅优于 FLowHigh 0.799
- 音素分类器在 2k/1k 输入下达 82.55%/75.64% 精度；消融显示三组件均有增益；1 步推理 ViSQOL 3.946 几乎无损
**是否开源**：代码已开源于 GitHub，未见模型权重与 demo。

### ⭐ 评分：7/10
清晰界定并系统评测了被忽视的极端带宽受限 SSR 问题，三项策略互补且各有消融支撑，两个数据集多指标稳定领先，方法务实有效。但组件多为已有技术的整合而非范式突破，数据仅限英语语料、退化仅理想低通合成，缺少真实骨传导与主观听测验证，实用结论的推广性有待加强。
---

## 其余论文（仅列标题、评分与链接）

### [16] ART-NAD: An Articulatory Inversion-based Neural Acoustic Distance for Pathological Speech Intelligibility Assessment
- **arXiv ID**：2609.24046 | **方向**：语音大模型 | **评分**：7/10 ｜ 构音反演声道收紧变量替换 SSL 特征，病理语音可懂度评测追平 NAD（r=0.71）且通道级可视化可解释
- **论文**：https://arxiv.org/abs/2609.24046 | **PDF**：https://arxiv.org/pdf/2609.24046.pdf | **代码**：https://github.com/karkirowle/pathbench | **Demo**：暂无

### [17] Reducing Speaker Residual by Considering Pinhole Effect in Voice Anonymization
- **arXiv ID**：2609.23433 | **方向**：语音大模型 | **评分**：7/10 ｜ 针孔损失显式度量并压制匿名语音的同源可链接性，多框架即插微调改善隐私-效用平衡（Interspeech 2026）
- **论文**：https://arxiv.org/abs/2609.23433 | **PDF**：https://arxiv.org/pdf/2609.23433.pdf | **代码**：https://anonymous.4open.science/r/Pinhole-loss-fine-tunning-4628 | **Demo**：暂无

### [18] Adaptive Depth and Expert Refinement for Efficient Speech Enhancement (ADER)
- **arXiv ID**：2609.22824 | **方向**：语音前端 | **评分**：6/10 ｜ 自适应深度早退+条件专家路由+出口感知中间监督，MP-SENet 参数减 70.4%/算力减 51.3%，VCTK-DEMAND WB-PESQ 3.37（ICASSP27 投稿）
- **论文**：https://arxiv.org/abs/2609.22824 | **PDF**：https://arxiv.org/pdf/2609.22824.pdf | **代码**：暂无 | **Demo**：暂无

### [19] The Bairong System for MLC-SLM 2026: Dynamic Question-Aware Evidence Routing for Multilingual Conversational Speech Understanding
- **arXiv ID**：2609.22214 | **方向**：语音大模型 | **评分**：6/10 ｜ 转写为骨干、问题感知证据路由动态选择音频/说话人/全局声学证据，MLC-SLM Task2 达 94.84%（Interspeech 2026 挑战赛）
- **论文**：https://arxiv.org/abs/2609.22214 | **PDF**：https://arxiv.org/pdf/2609.22214.pdf | **代码**：暂无 | **Demo**：暂无

### [20] Speech Language Models for Full-Meeting Speaker Diarization: Capabilities and Limitations
- **arXiv ID**：2609.23114 | **方向**：语音大模型 | **评分**：6/10 ｜ ESPnet-SpeechLM 以结构化 token 自回归生成 SD：事件式表征比帧式稳定，长会议全跟踪与重叠仍是瓶颈，显式说话人链接后处理大幅减混淆（SLT 2026）
- **论文**：https://arxiv.org/abs/2609.23114 | **PDF**：https://arxiv.org/pdf/2609.23114.pdf | **代码**：暂无 | **Demo**：暂无

### [21] Causal Localization of the Refusal Direction in Audio Language Models
- **arXiv ID**：2609.22260 | **方向**：语音大模型 | **评分**：6/10 ｜ 干预实验定位 LALM 拒绝方向：主要继承自文本 LLM 中后层（Qwen2.5-Omni L16 −7.10）、音频接口方向几乎无效，安全审计应结合干预与探针（ISCSLP 2026）
- **论文**：https://arxiv.org/abs/2609.22260 | **PDF**：https://arxiv.org/pdf/2609.22260.pdf | **代码**：暂无 | **Demo**：暂无

### [22] SEABED: SouthEast Asian Benchmark for Evaluating Audio Reasoning
- **arXiv ID**：2609.22586 | **方向**：语音大模型 | **评分**：6/10 ｜ 东南亚真实开源语音构建 6 类音频推理 QA 5,404 题，六个前沿/区域音频 LLM 中 Gemini 3.5 Flash 加权最高仅 50.3%（EMNLP SALMA）
- **论文**：https://arxiv.org/abs/2609.22586 | **PDF**：https://arxiv.org/pdf/2609.22586.pdf | **代码**：https://huggingface.co/datasets/CentificAIResearch/SEABED | **Demo**：暂无

### [23] Discrete vs. Continuous: A Comprehensive Study of Unified Audio Understanding in LALMs
- **arXiv ID**：2609.22851 | **方向**：语音大模型 | **评分**：6/10 ｜ UniARC 框架在 135M-8B 规模、语音/声效/音乐域对照连续特征与离散 token：token 化语义约束是理解关键，扩参数补不回表示信息损失（Interspeech 2026）
- **论文**：https://arxiv.org/abs/2609.22851 | **PDF**：https://arxiv.org/pdf/2609.22851.pdf | **代码**：暂无 | **Demo**：暂无

### [24] If You Hear It, Help Find It: Orthogonal Knowledge Distillation for Open-Vocabulary Audio Understanding
- **arXiv ID**：2609.23376 | **方向**：语音大模型 | **评分**：6/10 ｜ 正交知识蒸馏做开放词汇声学标记（本批 cs.SD 尾部条目，与音视频理解交叉）
- **论文**：https://arxiv.org/abs/2609.23376 | **PDF**：https://arxiv.org/pdf/2609.23376.pdf | **代码**：暂无 | **Demo**：暂无

### [25] LiteCASS: A Lightweight End-to-End Network for Real-Time Stereo Cinematic Audio Source Separation
- **arXiv ID**：2609.23453 | **方向**：语音前端 | **评分**：6/10 ｜ 首个实时立体声影视三轨（对白/音乐/音效）轻量网络：确定性子带重排+双紧凑 U-Net，1.06M 参数 0.72G MACs/s 平均 SI-SDR 超基线
- **论文**：https://arxiv.org/abs/2609.23453 | **PDF**：https://arxiv.org/pdf/2609.23453.pdf | **代码**：暂无 | **Demo**：暂无

### [26] XSQ-AST: An Explainable Audio Spectrogram Transformer Framework for Localising Synthetic Speech Artifacts
- **arXiv ID**：2609.24770 | **方向**：语音大模型 | **评分**：6/10 ｜ SQ-AST+WhisperX 音素对齐+多显著性方法免重训定位合成语音伪影时间分布，40 人听测验证与听众标注相关性（ICASSP27 投稿）
- **论文**：https://arxiv.org/abs/2609.24770 | **PDF**：https://arxiv.org/pdf/2609.24770.pdf | **代码**：暂无 | **Demo**：暂无

### [27] Low-Rank Frequency Convolution and Noise-Range Augmentation for Real-Time Pitch Estimation on Edge Devices
- **arXiv ID**：2609.23340 | **方向**：语音前端 | **评分**：5/10 ｜ 低频卷积网络低秩化参数减 35.9%，证明训练噪声下限比架构更能决定强干扰行为；自写 83kB C 内核比 ONNX Runtime 快 3.8×
- **论文**：https://arxiv.org/abs/2609.23340 | **PDF**：https://arxiv.org/pdf/2609.23340.pdf | **代码**：暂无 | **Demo**：暂无

### [28] Misrecognition or Abstraction? Rethinking Outputs of Sound Event Recognition
- **arXiv ID**：2609.23411 | **方向**：语音大模型 | **评分**：5/10 ｜ 提议"类别+置信度+拟声描述"三元输出表征，类别模糊时拟声仍传递环境信息，LLM 评审与主观听测均偏好（DCASE 2026）
- **论文**：https://arxiv.org/abs/2609.23411 | **PDF**：https://arxiv.org/pdf/2609.23411.pdf | **代码**：暂无 | **Demo**：暂无

### [29] Long-Tail Rebalancing for Non-Verbal Vocalization-Aware ASR
- **arXiv ID**：2609.23462 | **方向**：语音大模型 | **评分**：5/10 ｜ NVVSpeech 挑战赛 Track1 系统：跨数据集标签归一+平方根采样→均匀类别两阶段配平长尾，官方 63.86 分第四名
- **论文**：https://arxiv.org/abs/2609.23462 | **PDF**：https://arxiv.org/pdf/2609.23462.pdf | **代码**：暂无 | **Demo**：暂无

### [30] Entropy-aware Logistic Regression for Fusion of Large-Scale Speaker Recognition Systems
- **arXiv ID**：2609.23727 | **方向**：语音大模型 | **评分**：5/10 ｜ 将模型熵驱动的句子级不确定度引入打分融合，大规模说话人识别下优于固定系数 LR（SLT 2026）
- **论文**：https://arxiv.org/abs/2609.23727 | **PDF**：https://arxiv.org/pdf/2609.23727.pdf | **代码**：暂无 | **Demo**：暂无

### [31] Synthetic Speech Detection in Brazilian Portuguese through Accent-Related Features
- **arXiv ID**：2609.23807 | **方向**：语音大模型 | **评分**：5/10 ｜ 利用 TTS"方言稀释"音韵矛盾：音素级地理方差特征+KDE 无监督即分真伪，可解释轻量并可增强基础模型（pt-BR 反 spoofing）
- **论文**：https://arxiv.org/abs/2609.23807 | **PDF**：https://arxiv.org/pdf/2609.23807.pdf | **代码**：暂无 | **Demo**：暂无

### [32] DFD-Lab: A Modular Audio-Visual Deepfake Detection Pipeline
- **arXiv ID**：2609.23830 | **方向**：语音大模型 | **评分**：5/10 ｜ 模块化音视频深伪检测实验管线；工程系统论文
- **论文**：https://arxiv.org/abs/2609.23830 | **PDF**：https://arxiv.org/pdf/2609.23830.pdf | **代码**：暂无 | **Demo**：暂无

### [33] HaikuS2S: A Cascaded System For Responding In Verse
- **arXiv ID**：2609.23951 | **方向**：语音大模型 | **评分**：4/10 ｜ 级联语音对话系统以俳句式回复为输出风格约束；创意应用，非语音技术主线
- **论文**：https://arxiv.org/abs/2609.23951 | **PDF**：https://arxiv.org/pdf/2609.23951.pdf | **代码**：暂无 | **Demo**：暂无

### [34] Morpho-VITS: Variational Inference with Morphological Modeling for End-to-End Speech Synthesis of a Tonal Bantu Language
- **arXiv ID**：2609.24310 | **方向**：语音大模型 | **评分**：5/10 ｜ 音节文字无调标注的基尼亚卢旺达语 TTS：词素序列编码器+音素-词素注意力注入形态句法先验，自然度/语调/可懂度显著提升
- **论文**：https://arxiv.org/abs/2609.24310 | **PDF**：https://arxiv.org/pdf/2609.24310.pdf | **代码**：暂无 | **Demo**：暂无

### [35] Automated Assessment of L2 Speech Rhythm Using Low-Frequency Amplitude Modulations
- **arXiv ID**：2609.24818 | **方向**：语音大模型 | **评分**：5/10 ｜ 免对齐的 L2 节奏自动评估：CNN 直接回归语音振幅包络低频调制特征，speechocean762 流利度/韵律与人类相关性超时长类指标，代码开源（SLT 2026）
- **论文**：https://arxiv.org/abs/2609.24818 | **PDF**：https://arxiv.org/pdf/2609.24818.pdf | **代码**：暂无 | **Demo**：暂无

---

*Generated on 2026-09-22*
