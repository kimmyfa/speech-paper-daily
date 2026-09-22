# 2026-09-21 语音论文速递

**共收录**: 20 篇 | **语音大模型**: 17 篇 | **语音前端**: 3 篇

> 目标日期 2026-09-21（北京时间）arXiv 语音相关论文共命中 20 篇。
> 以下是按评分排序的结果。

---

## 语音大模型

## [1] Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction

**arXiv ID**：2609.21392 | **方向**：语音大模型

**作者**：Qi Chen、Yunfei Chu、Haolin He、Yifan Yang、Zihan Liu、Yuxuan Wang、Ziyang Ma、Ruiyang Xu、Meng Gao、Yinsong Yan、Ling Wang、Hui Wang、Wen Huang、Yiheng Chen、Guanrou Yang、Qiuqiang Kong、Jin Xu、Xie Chen

**机构**：上海交通大学、上海创智学院、阿里巴巴 Token Hub（Alibaba Group）、香港中文大学、清华大学、香港理工大学、南开大学、约翰霍普金斯大学

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21392 | **PDF**：https://arxiv.org/pdf/2609.21392.pdf | **代码**：https://huggingface.co/datasets/qc316/odubench | **Demo**：https://odubench.github.io

### 📌 简介
真实音视频交互中的用户需求常以省略形式表达，需综合视觉、声学线索与对话历史推断，且"类请求"语音易误触发助手响应，而现有基准只评响应质量、缺需求理解评测。本文提出 ODU 任务与 ODU-Bench（2078 个场景、五维评测），对 14 个原生音频/音视频 MLLM 测评：最强的 Gemini 3.1 Pro 对须依上下文推断的关键信息仅恢复 44.7%，11/14 模型在无需求场景误触发率超 50%，暴露系统性能力缺口。

### 🔧 技术方案

**问题背景：** 语音助手面对的是自然音视频输入而非组织好的文本，用户真实需求常不在话语中显式说出（如"同一个测试""这个"），需从手势与对话史补全；反之环境播放或对他人的抱怨式请求不应触发响应。需求理解因此是独立于响应生成的多模态上下文推理问题，此前从未被显式评测。

**模型架构：** 以交互流中最后一个用户轮为评测对象、前文为上下文，输出五维：需求有无（M1，macro-F1，权重 0.15）、结构化意图与所需上下文（M2，原子关键点命中率，权重 0.60）、需求时间跨度（M3，temporal IoU，0.10）、转录（M4，1 减自适应 CER/WER，0.10）、用户画像（M5，0.05）；另单独报告无需求场景误触发率 FTR，加权总分以 M2 主导。

**核心创新：** (1) 新任务形式化：把需求理解从响应生成的隐含前提提升为显式开放式预测目标，是首个兼具口语输入、多轮对话、视觉/声学线索推断与开放语义需求的基准。(2) 挑战驱动分类体系：正样本由 4 个可组合挑战轴（视觉/声学依赖、对话依赖、间接表达、噪声条件）加 2 个描述轴构成，负样本按"类请求信号类型×无效化原因"独立分类，从难度来源组织覆盖。(3) Agentic 生成与媒体锚定标注：Qwen3.7-Max 按分类目标 coarse-to-fine 生成脚本，文本-only 判别器拒收仅凭话语即可推断意图或无需求状态明显的样本，保证上下文真实必需；渲染与真人录制后用 Fun-ASR 加多个 MLLM 从成片反推 ground truth，再全量人工核验。

**训练策略：** 基准研究，协议如下：共 2078 场景，含 1801 合成（音视频与 audio-only 双模态）与 30 名演员录制的 277 段真实交互；语义评分由 LLM judge（Qwen3.6-Flash）判断预测意图加所需上下文是否覆盖每个关键点，接受语义等价改写并审计多 judge 稳定性；文本基线 GPT-5.4 仅输入 ASR 转写、句级时间戳与历史助手回复；多轮只评最后用户片段。

### 📊 实验结果
**数据集**：ODU-Bench，2078 个需求/无需求场景，1801 合成、277 真人录制，音频与音视频双模态评测协议。

**主要指标**：
- 综合均分：音视频最佳 Gemini 3.1 Pro 为 72.6，开源最佳 Qwen3-Omni-Think 仅 59.9，差 12.7 个点；GPT-5.4 文本基线 59.0
- 语义 M2：Gemini 3.1 Pro 音视频 63.4%、Seed 2.0 Lite 音频 78.0%，主评测维度头部空间巨大
- 证据通道分解：Gemini 3.1 Pro 对口语请求自身关键点恢复 82.9%，对需视觉/声学/对话上下文的关键点仅 44.7%
- 误触发：11/14 模型 FTR 超 50%，Gemini 3.7 Flash 音频最低 16.0%；Seed 2.0 Lite 音频 M2 达 78.0 但 FTR 高达 80.7%
- 盲测 A/B：给定正确需求标注后，非平局判断中 85.8% 偏好其下游响应（平局 40.0%）
- 真实录制迁移：Gemini 3.1 Pro 均分反升 2.4，Ming-Flash-Omni 2.0 转录骤降 27.3 个点

**是否开源**：是，数据与评测方案发布于 HuggingFace，附 Demo 页；真人素材限学术用途。

### ⭐ 评分：8/10
评分理由：任务定义补上了多模态交互评测的关键盲区，五维协议与关键点评分设计严谨，挑战分类加媒体锚定标注加人工核验保证数据质量，证据通道分解直击 MLLM 上下文推理短板并有下游响应价值验证；属实质性贡献。不足在于合成场景生态效度仍存疑、只诊断不给出改进路径，且结论依赖 LLM judge。

## [2] OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue

**arXiv ID**：2609.21465 | **方向**：语音大模型

**作者**：Haolin He、Yunfei Chu、Qi Chen、Wen Huang、Yuan Feng、Muzhi Zhu、Zheqi Dai、Haoning Xu、Dongchao Yang、Chunyat Wu、Zining Liang、Zhengxi Liu、Xiquan Li、Xie Chen、Xize Cheng、Qize Yang、Jin Xu、Qiuqiang Kong（共18人）

**机构**：香港中文大学、阿里巴巴Token Hub（Qwen团队）、上海交通大学、上海创智学院、浙江大学

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21465 | **PDF**：https://arxiv.org/pdf/2609.21465.pdf | **代码**：暂无（论文承诺后续开源Bench与RL训练代码） | **Demo**：暂无

### 📌 简介
论文定义OmniVChat任务：全模态模型直接同时接收用户音视频流并输出文本回复，查询隐含在音画内容中，不依赖文本提问、外部字幕或ASR级联，以降低延迟并保留韵律与视觉线索。针对真实数据稀缺与开放回复难以评估两大瓶颈，作者提出三件套：OmniVChat-Studio多智能体合成引擎（1080P/44.1kHz音视频对话+分级评分细则）、OmniVChat-Bench（2800条合成实例+360条真人录音）、OmniVChat-RL奖励设计。用其训练Qwen3-Omni-Instruct后，Bench均分0.465升至0.652，真人录音集0.402升至0.632，回复效率RE由5.75升至18.38，风格达标率0.710升至0.992。

### 🔧 技术方案

**问题背景：** 全模态模型做原生视听对话时缺少"用户举着设备自拍提问"的公开数据，且好回复需兼顾环境、表情、附近物体，表达方式多样，关键词匹配式评测失效。近期智能体系统与视频生成的进展使"以生成服务理解"成为可行路径。

**模型架构：** Studio数据引擎以文本语料+子类目配置为输入，由四个智能体协作：Director负责全部文本侧生成与决策，Renderer将审核通过的提示词渲染为同步音视频片段，Reviewer对成片写描述caption与七项质量报告并回答聚焦问答，Validator按规则做确定性校验；单轮子系统走"采样-描述-计划-脚本-校验-渲染-复查-回复+细则"14模块闭环，多轮子系统拆分逐轮提示生成与媒体链接复用，Fixed/Flexible模块分离便于扩展新子类目。Bench由Studio合成，每条实例含参考回复与分级rubric，评测时由qwen3.7-max逐条判分。RL以Qwen3-Omni-30B-A3B-Instruct的Thinker为策略，在上述rubric、效率、风格信号上优化。

**核心创新：** (1) OmniVChat-Studio：可控可扩展的多智能体合成引擎，每模块带独立修复预算（重写/换种子/聚焦问答），产出不泄漏、可溯源的合成对话，训练用集5600条、开发560条、评测2800条且与训练视频无重叠。(2) 分级门控rubric评测协议：Tier 0检查回复语言，不失败不得分，失败清零；后续层级须满足全部前置层级才能得分，得分公式化（式1），按17子类目等权平均，规避关键词匹配缺陷。(3) OmniVChat-RL三信号联合奖励：正确性直接用rubric分数，效率奖励ρ(y)=r(y)/w(y)组内min-max归一化，按字符/词组计数长度，风格奖励为7项提示词规则全过才得1，总奖励R=r+0.5f+0.1e+0.5s。

**训练策略：** GSPO组序列策略优化（GRPO式组基线、无标准差归一化、按回复长度归一的概率比裁剪），LoRA rank 64，1000迭代，每步32输入×4采样回复，第940步取开发集最优检查点。rubric奖励0.308升至0.629，风格0.750升至0.992，平均回复长度91.5词降至36.6词。

### 📊 实验结果
**数据集**：OmniVChat-Bench（2550单轮+250多轮，17子类目、22场景域，英文1766/中文1034）、OmniVChat-Bench-Human（360条真人录制中文单轮）、OmniVChat-Bench-Train（5600条）。

**主要指标**：
- Bench均分：0.652（基线Qwen3-Omni-Instruct 0.465），真人集0.632（基线0.402），RE 18.38，风格0.992
- 关键对比：与最强基线Gemini系列相比，Mean上0.652略低于Gemini-3.5-Flash的0.667，但Human上0.632大幅领先最佳闭源Gemini-3.7-Flash的0.575（+0.057），RE领先16.96，风格领先Gemini-3.1-Pro的0.871；开源组中全面第一
- 消融：去掉效率项Mean升至0.697、Human 0.691，但回复膨胀到99词、RE跌至7.12；去掉风格项风格分降至0.788
- 多轮泛化：本方法多轮-单轮差-0.026，Gemini-3.7-Flash为-0.114

**是否开源**：承诺开源Bench与RL训练代码，当前未发布。

### ⭐ 评分：7/10
评分理由：任务定义清晰，"合成-评测-训练"闭环完整且真人录音迁移验证令人信服，分级rubric奖励设计与效率/风格权衡有方法论价值；但依赖强LLM判分、合成数据分布对齐仅间接验证，RL提升幅度未全面超过最强闭源模型，属于扎实的实质性贡献而非突破。

## [3] GenTraceBench: A Benchmark for Tracing Audio Deepfakes Across Pre- and Post-training Stages

**arXiv ID**：2609.21738 | **方向**：语音大模型

**作者**：Li Wang、Kunyu Feng、Wan Lin、Dekun Chen、Qinke Ni、Xueyao Zhang、Lei Wang、Jie Shi、Haizhou Li、Zhizheng Wu

**机构**：香港中文大学（深圳）、Amphion Technology、华为技术有限公司

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21738 | **PDF**：https://arxiv.org/pdf/2609.21738.pdf | **代码**：暂无（论文承诺将公开该基准）| **Demo**：暂无

### 📌 简介
针对TTS部署普遍经SFT/DPO/GRPO适配后生成器指纹是否依然有效的问题，提出首个覆盖同一生成器系列预训练与后训练阶段的音频深伪溯源基准GenTraceBench：5架构、16变体、固定文本与说话人prompt生成的49728条语音，以train-on-foundation、test-on-adapted协议评测检测、归因与开集验证。DPO/GRPO大体保留指纹（归因变化不超过1.39点），部分SFT与数据变化致显著漂移，SingNet-only使W2V-BERT归因降10.15点；多shot注册将SFT验证EER从44.4%降至11.0%，SingNet-only仍不低于45%。

### 🔧 技术方案

**问题背景：** ASVspoof、WaveFake等现有音频深伪语料多评测固定的完整训练生成器，ShiftySpeech与STOPA面向跨系统与组件级扰动，均未回答生成器经过自身SFT与RL对齐后，取证前端捕获的模型特异指纹能否存续。

**模型架构：** 基准收录CosyVoice2、F5-TTS、FlexiVoice、MaskGCT、Vevo2五种架构，覆盖流匹配、自回归token与掩码生成式等范式。后训练分三类：通用对齐基于INTP数据做DPO（β按架构取0.1/10/1000）；模态扩展用NVSpeech对CosyVoice2做SFT以增加笑声等副语言发声；多阶段演化含Vevo2的DPO到GRPO及FlexiVoice三阶段流水线。另设Vevo2以Emilia、SingNet-only、Emilia+SingNet预训练的数据控制。16变体统一用Seed-TTS eval固定prompt合成（1088英文、2020中文），按同一划分切为1035/517/1556，共49728条含真人语音。

**核心创新：** (1) 首个同谱系checkpoint对照的受控基准：固定内容与说话人、仅沿生成器训练阶段追踪，隔离出训练阶段指纹漂移，与STOPA的跨组件覆盖互补。(2) 三任务统一取证协议：binary detection与closed-set attribution用线性头，open-set deepfake verification用512维AAM-Softmax嵌入（margin 0.3、scale 15）加余弦打分，并支持N条均值的多shot注册以抑制类内方差。(3) 方差驱动与结构漂移的机制分解：在嵌入空间分别量化类均值质心位移C与类内散布变化S，发现CosyVoice2 SFT漂移主要为方差驱动、可被原型平均消除，而SingNet-only是系统性均值位移、多shot无法挽回。

**训练策略：** 取证系统以W2V-BERT（580M）为主干并与WavLM、AASIST对照，AdamW训练100 epoch、batch 64。以验证集选点并另报3-epoch早期配置；归因以种子1/42/2026重复三次，固定种子用10000次配对bootstrap给出95%置信区间。

### 📊 实验结果
**数据集**：GenTraceBench（5类TTS、16种训练变体基于Seed-TTS eval prompt合成的49728条语音及对应真人语音）

**主要指标**：
- 归因下降（W2V-BERT三次验证选点均值）：RL对齐0.13±0.23点，CosyVoice2 SFT 0.64±0.06点，Vevo2 SingNet-only 10.15±0.97点，后两者bootstrap区间均不含零
- 检测：CosyVoice2 SFT降至87.28%，F5-TTS经DPO升至100%；跨backbone上RL归因最多降1.39点，SFT降0.64至8.16点随backbone而异
- 数据混合控制：Emilia+SingNet质量相当（WER 5.07%对3.18%）时归因变化−0.26至+0.26点且CI含零，说明改变数据配比不必导致漂移
- 验证EER（W2V-BERT，N从1到10）：域内5.2%降至1.6%，RL 14.0%降至10.9%，SFT 44.4%降至11.0%，SingNet-only始终不低于45%
- 关键对比：FlexiVoice约79%归因准确率，其99%错误被判给共享Emilia数据与FM声码器后端、嵌入相似度最高的Vevo2，呈谱系歧义

**是否开源**：暂无代码或数据地址，作者承诺公开发布；论文为ISCSLP 2026录用短文，CC BY-NC-SA授权。

### ⭐ 评分：7/10
评分理由：直面部署态TTS生命周期这一真实取证盲区，首个同谱系受控基准设计干净，固定内容生成、三任务协议、多种子重复、bootstrap统计与嵌入几何分解严谨，方差型与结构型漂移的区分对注册与系统更新决策有直接指导；扣分在仅一组SFT配置、中英干净语音、数据尚未放出，属增量资源而非方法突破。

## [4] Towards Zero-Shot Attribution of Synthetic Speech via Audio-Text Contrastive Retrieval

**arXiv ID**：2609.21581 | **方向**：语音大模型

**作者**：Cristian-Teodor Neamtu、Serban Mihalache、Stefan Smeu、Dan Oneata、Horia Cucu、Dragos Burileanu

**机构**：布加勒斯特理工大学（POLITEHNICA Bucharest）SpeeD语音与对话实验室、Bitdefender

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21581 | **PDF**：https://arxiv.org/pdf/2609.21581.pdf | **代码**：https://github.com/neamtucristian26/flame | **Demo**：暂无

### 📌 简介
现有合成语音溯源多为闭集分类，无法点名训练中未出现的TTS系统。本文将其重构为跨模态检索：用自然语言描述每个生成系统，在音频-文本联合嵌入空间中检索最近邻描述完成归因，新增系统只需写描述、无需重训。其FLAME模型在MLAAD v9（140个TTS、51种语言）上对未见系统达模型级MRR 58.4%、全库Hit@1 44.3%，远超约0.3%随机水平；即使归因错误仍能恢复声码器、语系等属性，实现优雅降级。

### 🔧 技术方案

**问题背景：** 音频深伪取证正从真假判定迈向来源归因。传统方法建模为多类分类或度量学习，只能覆盖训练时的系统；新TTS模型持续发布使闭集方案失效，而出域检测虽可标记未知样本，却无法提供任何来源线索。

**模型架构：** 双塔结构：音频侧冻结Wav2Vec2-BERT，取24层表征经可学习加权和聚合；文本侧冻结E5-large-v2。两塔各接可训练线性投影头（1024维到256维）并做L2归一化，以余弦相似度打分，可训练参数仅约0.5M。推理时音频查询与描述库逐一匹配，argmax即归因结果，亦支持文本到音频反向检索。

**核心创新：** (1) 溯源改写为音频与自然语言描述的匹配：以（模型，语言）对为归因单元，每系统5种风格描述（技术、取证、数据训练、能力定位、工程师视角）；描述先由Claude Opus 4.7、Gemini 3.1 Pro、GPT-5.5三家LLM在11维结构化事实表上投票并对照公开文档生成，再渲染成自由文本，以降低幻觉并保证溯源可查。 (2) 跨模态与模态内结合的四向对比目标：总损失为音频-文本双向监督对比取平均，加λ、γ加权的音频-音频、文本-文本模态内对比；批内256条按88个系统各32条采样构成多正例结构。 (3) 同一空间统一归因与属性画像：间接法检索全描述后抽取属性值，直接法用"This audio was generated using the [X] vocoder"模板查询，一套模型替代多个专用分类器。

**训练策略：** AdamW，学习率1e-4、权重衰减1e-4，100轮，首epoch线性预热后余弦退火至零；温度τcm=0.020、τa=0.045、τt=0.070，权重λ=0.298、γ=0.401由留出折网格搜索。文本增强含句级dropout与前缀截断；属性模板以10%概率采样且排除于文本-文本损失以避免梯度冲突。10折leave-models-out交叉验证（126见+14未见模型），3种子报告均值±标准差。

### 📊 实验结果
**数据集**：MLAAD v9（687.4小时合成语音、51语言、140个TTS模型、298个模型-语言系统）。

**主要指标**：
- 闭集系统级Hit@1：86.2%，低于专用分类器93.4%；模型级93.3%（分类器98.4%）
- 零样本全库unseen-full：模型级MRR 58.4%、Hit@1 44.3%；系统级MRR 50.0%、Hit@1 34.7%
- 受限库unseen-restricted：模型级MRR 81.4%；文本到音频检索趋势与音频到文本一致
- 未见属性画像：全描述法在架构、声学模型、声码器、说话人类型4项超专用分类器（如声码器70.6%对66.8%）
- 错误分析：错误Top1仍恢复正确声码器52.2%、语系79.5%；去除语言头仅使模型级Hit@1从44.3%降至41.8%
- 关键对比：298候选下随机Hit@1约0.3%，FLAME为34.7%，零样本归因远超随机基线

**是否开源**：代码与数据协议已在GitHub公开；描述生成依赖商用LLM接口。

### ⭐ 评分：7/10
评分理由：将溯源重构为自然语言检索的问题定义新颖且实用，统一开集归因与属性画像，多LLM投票与语言条件设计考虑周全；但模型本身仅冻结双塔加投影头，结构增量有限，闭集落后专用分类器，全库零样本Hit@1仅34.7%，描述质量依赖闭源LLM且仅在单一数据集验证，属实质性贡献而非突破。

## [5] Samsone: A Family of Open Small Audio Language Models for On-Device Inference

**arXiv ID**：2609.21666 | **方向**：语音大模型

**作者**：Piotr Masztalski、Michal K. Grzeszczyk、Olaf Sikorski

**机构**：三星波兰研究院（Samsung R&D Institute Poland）、波兰克拉科夫AGH科技大学

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21666 | **PDF**：https://arxiv.org/pdf/2609.21666.pdf | **代码**：https://github.com/SamsungLabs/samsone | **Demo**：暂无

### 📌 简介
音频大模型动辄3B-9B参数，难以满足端侧低延迟与隐私需求，现有小模型推理弱且缺乏真实手机部署验证。本文提出Samsone家族（99M/134M/356M）：Whisper-Tiny编码器经特征池化与投影器接入SmolLM2-135M/360M解码器，在ReasonAQA+AudioSkillsXL公开数据上单阶段微调。Samsone-134M在MMAU以61.33平均分刷新同级SOTA并超越8.4B的Qwen2-Audio，MMAU-Pro领先前SOTA约36%，99M版在Galaxy S25 Ultra CPU上达125 tok/s，代码、权重与安卓应用全部开源。

### 🔧 技术方案

**问题背景：** 音频SOTA大模型普遍3B-9B，隐私敏感与离线场景需要十亿参数以下的端侧模型；早期SALM如Pengi（323M）训练文本多样性不足难以推理，Mellow（167M）仅部分缓解，且移动部署验证几乎空白。

**模型架构：** 采用音频编码器、模态投影器、文本解码器三段式ALM结构。音频编码器为Whisper-Tiny encoder（约9M），帧级嵌入沿时间平均池化为固定50个音频token；投影器沿用Mellow的非线性设计（两层线性+GeLU+残差+LayerNorm，0.5M-1M）；LM为SmolLM2-135M或360M。投影音频嵌入与文本嵌入拼接输入LM，引入可训练SEP token分隔多段变长音频。三档变体：99M（词表缩减+LM从30层裁至20层）、134M（仅词表缩减，LM 125M）、356M（SmolLM2-360M骨干，LM 347M）。

**核心创新：** (1) 词表缩减VR：训练文本限定小写ASCII，删除含超4个空白符或超3个特殊字符的token，从49152词表裁掉15042个，embedding矩阵省8.7M参数；SmolLM2嵌入维576下原embedding层占总参数约21%，是最经济的瘦身点。(2) 深度剪枝DP：全部Transformer块可训练，直接移除LM末尾10层，每层省约3.5M参数，构造出99M亚亿级SALM，提供容量与体积间可控的缩放旋钮。(3) 首个端侧闭环开源SALM：导出ExecuTorch+XNNPACK移动检查点并提供安卓应用，在量产手机CPU完成实时推理验证，训练代码与权重全公开。

**训练策略：** 仅用两个公开数据集：AudioSkillsXL（800万QA，覆盖声音/音乐/语音）+ReasonAQA（100万推理QA，含双音频输入）；发现ReasonAQA选择题(b)选项严重过偏，训练时随机重排选项使答案分布均匀。单阶段训练（多阶段无增益），除LM embedding层外全部可训练，token级交叉熵，AdamW+余弦退火（10轮线性warmup，最低lr 1e-7），lr为3e-4（99M/134M）与1e-4（356M），单张RTX PRO 6000 Blackwell 96GB训练100 epochs（每epoch 20万样本），推理用贪心解码。

### 📊 实验结果
**数据集**：MMAU、MMAU-Pro、Clotho、AudioCaps、ClothoAQA、Clotho_CLE/AudioCaps_ACE；端侧在Samsung Galaxy S25 Ultra CPU上以15条音频-查询对测延迟。

**主要指标**：
- MMAU test平均分：Samsone-134M 61.33，较同级最强基线Mellow-167M（53.34）高8.0，语音子域47.90领先约12；99M即达58.13仍超Mellow，参数少40%
- MMAU-Pro：134M 37.57、99M 36.83，对Mellow（27.50）相对提升约34%-36%
- 关键对比：134M超过60倍规模的Qwen2-Audio-8.4B（57.40）与100倍SALMONN-13B（36.23），逼近Audio Flamingo 2-3B（61.06）
- 其他任务：ClothoAQA 73.8、CLE 93.4、ACE 93.7、Clotho captioning SPICE 11.6均超Mellow；AudioCaps SPICE 14.4低于Mellow（17.8，训练配比所致）
- 端侧速度：99M生成125 tok/s（音频编码667ms），134M为87 tok/s，356M为39 tok/s，未做硬件级优化
- 消融：换AST编码器、GPT-2 LM或线性投影器均使MMAU下降约2-4分，验证Whisper+SmolLM2+非线性投影器组合

**是否开源**：完全开源：训练代码、服务端与移动端权重、ExecuTorch检查点及安卓应用（github.com/SamsungLabs/samsone）

### ⭐ 评分：7/10
评分理由：架构为成熟组件组合，创新偏工程，但VR+DP与选项均衡化处理把十亿参数以下SALM的MMAU/MMAU-Pro天花板整体抬高8分以上，并首次在量产手机CPU验证百token/s级实时推理，且全面开源可复现；局限是LM通用文本能力退化、AudioCaps描述偏弱、未做量化与NPU优化，故为同量级上的实质性推进而非领域突破。

## [6] CGaLore: Curvature-Guided GaLore for Memory-Efficient Continual Adaptation of ASR Foundation Models

**arXiv ID**：2609.21336 | **方向**：语音大模型

**作者**：Steven Vander Eeckt、Hugo Van hamme

**机构**：鲁汶大学（KU Leuven）电机工程系 ESAT/PSI

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21336 | **PDF**：https://arxiv.org/pdf/2609.21336.pdf | **代码**：https://github.com/StevenVdEeckt/cgalore | **Demo**：暂无

### 📌 简介
ASR 基座模型适配新领域或口音时会灾难性遗忘预训练能力，全参微调又代价高；GaLore 以低秩梯度投影降低优化器显存，但投影基仅由当前梯度决定，无抗遗忘机制。本文提出 CGaLore：先用旧任务上估计的 KFAC 逆曲率（Kronecker 近似曲率）对当前任务梯度做预条件过滤，再对其做 SVD 选投影基，使低秩优化器子空间偏向利于新任务且不伤旧任务的方向。在 OWSM v3.2 small 口音连续适配中，实验一平均 WER 8.72、BWT -0.3，较 GaLore（11.98、-4.7）消除 93.6% 遗忘，较最强基线 CSSVD（9.51）提升 8.3%，GPU 峰值显存 10.56GB 与 LoRA 相当。

### 🔧 技术方案

**问题背景：** 语音基座模型在数十万小时多语种数据上预训练，适配新任务既要显存高效又不能覆盖旧能力。现有 ASR 持续学习方法或按任务存适配器、推理依赖任务身份，或依赖预训练期优化器状态与梯度，在仅有少量旧任务语音的公开模型适配场景均不可行，亟需务实设定下的高效抗遗忘方案。

**模型架构：** 基座为 OWSM v3.2 small（366.7M 参数，9 层 E-Branchformer 编码器加 9 层 Transformer 解码器，151 语种 180k 小时训练），仅更新线性层权重矩阵、冻结输出层。GaLore 将全秩梯度经正交基 P、R 投影到 r×r 子空间内执行 Adam 优化再映射回参数空间，以低显存实现全参数更新；CGaLore 先按 H 逆乘 G 乘 Q 逆（Q、H 为旧任务 KFAC 的输入协方差与输出梯度协方差）过滤当前梯度，再对其做 SVD 选投影基，采用双侧投影，每 T 步用随机化 SVD 更新基。

**核心创新：** (1) 曲率引导的子空间选择：由旧任务损失的二阶泰勒展开可知，以旧任务损失增量为界时最大对齐方向正比于逆 Hessian 方向；用层内 KFAC 近似该 Hessian 对梯度预条件后再选基，把曲率嵌入训练过程中，区别于事后修正更新量的 IHR。(2) KFAC 流式维护：每个任务适配后仅采样少量数据计算新因子，以系数 α 加权平均并入每层唯一一组 (Q,H)，无需存储各任务曲率或重放缓冲区，数据算完即可丢弃。(3) 零显存增加实现：KFAC 因子常驻 CPU、仅在基更新时移到 GPU 乘法；抗遗忘通过优化器轨迹而非约束参数更新形式实现，保留 GaLore 全秩可塑性。

**训练策略：** ESPnet2 框架，AdamW 学习率 5e-4 无调度器、20 epoch、等效批大小 64；秩 r=215、基更新间隔 T=200，优化器状态显存与 PECL 基线对齐；KFAC 用旧任务每语种 20k 句（约 28 小时）估计，阻尼 1e-3、融合系数 α=1/4；损失为常规 ASR 序列损失，无附加正则项。

### 📊 实验结果
**数据集**：初始任务为 Common Voice 英/德/西，TEDLIUM 与瑞典/意大利/俄语作为不参与 KFAC 估计的留出旧任务；L2-Arctic 非母语英语按口音分为 L2/1、L2/2，CGN 荷兰语按荷兰/比利时口音分两任务连续适配。

**主要指标**：
- 实验一：平均 WER 8.72、BWT -0.3，对比 GaLore 11.98、-4.7（消除 93.6% 遗忘），对比最强 PECL 基线 CSSVD 9.51（相对提升 8.3%，Wilcoxon 检验显著）
- 实验二：平均 WER 17.68、BWT -2.7，对比 GaLore 28.93、-17.2（遗忘降低 84.3%），对比 CSSVD 18.33
- 效率：A100 峰值显存 10.56GB（LoRA 10.90GB），总训练时长 0.90 倍于 LoRA，KFAC 开销仅 0.4%；KFAC 数据降至每任务 8.3 分钟性能几乎不变，5 秒时仍比 GaLore 少遗忘超 60%
- 叠加事后 IHR 修正后第二任务平均 WER 16.33 降至 16.09、BWT 从 -1.3 改善到 -0.6；未参与 KFAC 估计的留出旧任务遗忘同样下降

**是否开源**：是，代码、配置与数据划分已发布于 GitHub

### ⭐ 评分：7/10
评分理由：以旧任务 KFAC 逆曲率引导 GaLore 子空间选基的思路简洁，证据链完整：零显存增长、分钟级旧数据即可用、留出旧任务受保护、可与事后 IHR 叠加且附显著性检验，首次务实处理公开基座模型仅有少量旧数据时的 ASR 显存高效持续学习。不足在于方法本质是 KFAC 与 GaLore 成熟组件的组合创新，实验局限于单一 367M 模型与两任务序列的口音/语种适配，规模化验证缺乏，属实质进展档上部。

## [7] All I Hear is Noise: Investigating Clever Hans Effects in Clinical Speech Datasets

**arXiv ID**：2609.21080 | **方向**：语音大模型

**作者**：Melanie Jouaiti、Ning Ma

**机构**：University of Birmingham；University of Sheffield

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21080 | **PDF**：https://arxiv.org/pdf/2609.21080.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
既有发现在 Pitt 语料上仅用静默段即达到 Alzheimer 检测近 100% 准确率，引发对临床语音数据集捷径学习的担忧。本文对五个主流健康语音语料（DAIC-WoZ 抑郁、TORGO 构音障碍、Neurovoz 与 MDVR-KCL 帕金森、UCLASS 口吃）系统审计：对比仅首秒音频、VAD 非语音静默段、全音频在 eGeMAPS、Compare16、wav2vec 2.0 三种表征及原始/去噪信号下的加权 F1。结果显示静默段分类常持平甚至超过全音频（TORGO 静默 0.90、UCLASS 静默 0.89），表明大量性能来自数据集混杂因素而非病变语音特征。

### 🔧 技术方案

**问题背景：** 临床语音语料采集条件异质（麦克风、环境、预处理流程不一），诊断标签可能与非临床因素产生虚假相关，模型借此捷径即可获得高分；除 Pitt 外该现象是否跨语料普遍存在尚不清楚。

**模型架构：** 审计框架为三种受限输入加统一分类器。Silero VAD（threshold 0.8，min_silence 50 ms，未检出语音时逐步降阈）提取非语音段并拼接，保留噪声与信道等录音级特性；首秒条件中 TORGO 85%、DAIC 84% 样本经检测不含有效语音；特征三套并行：OpenSMILE eGeMAPSv02（88 维）、Compare16（6373 维）、wav2vec 2.0 嵌入；分类器统一为 Gradient Boosting（100 棵树、lr 1.0、max depth 5、balanced sample weights）；去噪用 noisereduce 谱门控，另以 SHAP 做特征归因。

**核心创新：** (1) 首次将 Clever Hans 审计从单一抑郁症语料扩展到抑郁、构音障碍、帕金森、口吃四类疾病五数据集，证明捷径效应是领域普遍问题而非孤例。(2) 原始与去噪信号交叉对照揭示预处理双刃剑：去噪使 DAIC 静默段 F1 由 0.67 升至 0.72、TORGO 首秒达 0.91，但 Neurovoz 静默段由 0.71 跌至 0.54，说明模型依赖被处理扰动或消除的录音特征。(3) 可解释性归因与缓解实验：SHAP 显示 TORGO 最重要特征为响度类（受拾音距离与增益影响），施加 RMS 归一化后静默段 F1 仍 0.92、首秒 0.83，能量混杂无法简单去除。

**训练策略：** 全部实验采用一致的说话人独立划分（约 80% 说话人训练、20% 测试）以控制对比，报告加权 F1；协议目标不是优化精度而是探测约束输入下的信息量；附加跨条件泛化实验：仅用训练集首秒拟合、测试集全音频评估。

### 📊 实验结果
**数据集**：DAIC-WoZ（275 人抑郁访谈）、TORGO（15 人）、Neurovoz（112 人西语）、MDVR-KCL（37 人）、UCLASS（128 名口说者，仅分类录音场地）

**主要指标**：
- TORGO：全音频 F1 0.72-0.87，静默段 0.82-0.90，去噪首秒 0.91（文献基线 0.98）
- UCLASS：全音频 0.76-0.85，静默段最高 0.89，场地推断 F1 0.89
- DAIC-WoZ：首秒/全音频/静默三种条件几乎无差（0.66-0.75）
- 仅首秒训练、全音频测试 F1：TORGO 0.73、DAIC 0.75、UCLASS 0.84、MDVR-KCL 0.65、Neurovoz 0.78
- 关键对比：五数据集上静默或首秒相对全音频的 F1 差值普遍在 ±0.15 内甚至反超，与"病变语音主导判别"的预期相悖

**是否开源**：五个数据集均公开可获取；论文未提供自有代码仓库。

### ⭐ 评分：7/10
评分理由：论文无新模型，但完成了首个跨语料跨疾病的临床语音 Clever Hans 系统审计，以统一协议加 SHAP 归因证明"只看静音也能分类"的混杂信号贯穿全录音并跨条件泛化，直接动摇既有声学标志物文献可信度，方法论警示价值高；不足是未定位混杂的确切来源，也未延伸到端到端大模型系统，属重要实证提醒而非技术突破。

## [8] I'll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance

**arXiv ID**：2609.21183 | **方向**：语音大模型

**作者**：Amit Kumar Singh、Ritvik Yadav、Xuan Zhang、Seungwhan Moon、Shashank Jain、Pinar Donmez、Babak Damavandi

**机构**：Meta Reality Labs

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21183 | **PDF**：https://arxiv.org/pdf/2609.21183.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
现有AudioLLM只能被动应答查询，无法持续监听并在恰当时机主动提醒。本文提出"主动音频辅助"新任务，面向听障用户可穿戴场景，设计模型无关的ISM范式：在LLM解码词表中嵌入特殊token实现四状态主动决策。基于Qwen2-Audio-7B训练后，ESC-50上打断F1达99.6%、去重召回100%；零样本迁移Epic-Sounds取得最高打断F1 67.5，流式平均延迟3.5秒。

### 🔧 技术方案

**问题背景：** 传统声音感知系统按固定类别持续报警，不含用户意图与交互历史，导致同一持续事件反复提示造成"通知疲劳"。主动辅助要求模型仅凭一条watch-out意图，对流式音频逐步因果判断何时打断、何时静默，且须满足实时延迟约束。

**模型架构：** PALLM以Qwen2-Audio-7B为骨干（Whisper-large-v3音频编码器加7B LM，约8B参数），音频重采样16kHz转128维mel谱，stride 2池化得约40ms每token。意图与历史经Qwen2文本tokenizer编码，无需独立文本编码器。ISM在词表增加两个特殊token：触发时解码打断路径生成"<interrupt>加响应文本"，静默时仅输出"<silent>"，对应四状态：I1起始检测（不相关到相关的转折点）、I2持续相关触发（整窗相关无前置静默，防漏检）、S1无关静默、S2历史感知去重静默（依据对话历史抑制重复警报）。

**核心创新：** (1) 首次形式化AudioLLM主动辅助任务并定义四状态决策框架与配套指标（分型精确率/召回与以起始召回为主算的打断F1），把去重列为一等建模目标。(2) ISM仅靠词表扩展与自回归解码注入主动行为，不改架构，可平移到GAMA等任意AudioLLM，消融证明主动能力源于训练范式而非骨干。(3) 构建三套主动评测协议：ESC-50四状态平衡测试集、Epic-Sounds零样本迁移，以及15秒三段拼接、5秒滚动窗、含事件边界真值的流式协议，实测因果延迟与去重行为。

**训练策略：** 两阶段SFT：先以交叉熵做 reactive分类微调建立声学理解；再做proactive SFT，按事件边界[t1,t2]合成四类样本，打断样本目标序列为"<interrupt>加响应token"、静默样本仅"<silent>"，损失为二者交叉熵之和，并对静默样本下采样保持I/S数量1:1平衡、免额外加权。LoRA秩8、alpha 32、dropout 0.1，AdamW学习率5e-4余弦调度、5%预热、权重衰减0.1，训练10轮，有效batch 384（24乘16步梯度累积），最长2048 token，6张H100。

### 📊 实验结果
**数据集**：ESC-50（2000条5秒、50类环境声，5折交叉验证）；Epic-Sounds（44类第一视角厨房声，仅评测零样本迁移）。

**主要指标**：
- ESC-50：打断F1 99.6%、打断精确率99.4%、S2去重召回100%、R_I1 99.8%；reactive分类准确率94.7%，与PANN持平、逼近AST 95.7%；零样本基线S2召回仅0.2%（肯定偏置）、reactive SFT的S2仅10.1%
- Epic-Sounds零样本：PALLM打断F1 67.5，高于Zero-Shot 66.9与Reactive SFT 65.2，是唯一兼顾R_I1 96.7%且不崩塌为过触发或过静默的方法，但S1召回10.1%、I2召回41.2%为明显短板；细粒度分类34.5%低于音频SOTA 53.8%
- 流式：400条15秒拼接样本，平均打断延迟3.5秒；I2消融使I2召回提升约10个百分点

**是否开源**：暂无（论文未释出代码/模型；基于开源Qwen2-Audio与公开数据集）

### ⭐ 评分：7/10
评分理由：任务定义有开拓性，四状态框架把去重作为一等目标切中通知疲劳痛点，方法简洁可移植，实验含流式协议与消融较完整。扣分在于ESC-50成绩近饱和部分源于域内构造数据，零样本迁移静默召回崩塌暴露泛化不足，且无DHH真实用户研究，工程验证深度有限。

## [9] Enhancing Audio Reasoning via Semantic Summary Prediction

**arXiv ID**：2609.20849 | **方向**：语音大模型

**作者**：Francesco Bonzi、Pooneh Mousavi、Cem Subakan、Mirco Ravanelli

**机构**：Concordia University、Mila - Quebec AI Institute、Université Laval（加拿大）

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.20849 | **PDF**：https://arxiv.org/pdf/2609.20849.pdf | **代码**：https://github.com/FrancescoBonzi/SPARE | **Demo**：https://my-demo-hub.github.io/spare/

### 📌 简介
大型音频语言模型（LALM）存在"推理鸿沟"：显式 Chain-of-Thought 反而比直接回答准确率更低（SALMONN 上 MMAU 从 36.02% 跌至 18.03%），作者假设是长推理链使注意力漂离音频输入。本文提出 SPARE：在 CoT 序列前注入一个寄存器 token，用余弦相似度损失将其末层隐状态与结论的 Sentence-BERT 语义嵌入对齐，训练后丢弃全部辅助参数。SALMONN 13B 上 MMAU 达 58.03%、MMAR 达 40.32%，较 SFT 基线提升 3.38%，推理零额外开销。

### 🔧 技术方案

**问题背景：** LALM 生成冗长中间推理步骤时，注意力从声学信号转向已生成的文本 token，导致流畅但脱离音频的答案，CoT 提示甚至低于直接回答。现有缓解方案依赖大规模监督数据堆叠或计算昂贵的强化学习，缺乏训练期架构正则化路线。

**模型架构：** 基座为 SALMONN 13B，采用双音频编码器（Whisper 处理语音、BEATs 处理非语音音频），经 Q-Former 与线性投影接入 Vicuna 13B。训练序列格式为［问题、音频、选项、[REG]、CoT、结论］，CoT 含 summary/caption/reasoning 三个章节。[REG] 用自定义因果掩码：可查看前文，但后续 token 不可关注它，因此推理动态与标准 SFT 完全一致，对齐头与寄存器在推理时全部丢弃。

**核心创新：** (1) 语义总结预测对齐：取 Conclusion 标签内文本，经冻结的 all-MiniLM-L6-v2 编码为目标语义嵌入 v_target，与寄存器末层隐状态 h_[REG] 计算余弦距离损失，迫使模型在推理开始前就把最终语义目标"种"进潜空间，充当自顶向下的语义锚点。(2) 与 MuToR 的本质区别：MuToR 寄存器预测局部未来偏移片段，只学句法细节；SPARE 直接对齐终端语义结论，监督整条推理链的起点，保证全局一致性。(3) 机制可解释性：通过六随机种的注意力图分析证明，SPARE 的 [REG] 在首层对音频帧的注意力显著高于自回归答案 token，早期声学关注度的提升沿层次向文本域过渡，实证缓解音频漂移。

**训练策略：** 总损失为交叉熵加 λ 倍对齐损失，λ=2.0 为经验最优；数据为 AF-Think 标注的 YouTube8M 子集，16 万训练、4 万验证样本，SALMONN 基座未在推理数据上训练过，保证评测干净。

### 📊 实验结果
**数据集**：MMAU（多模态音频理解）、MMAR（音频推理），零样本评测；训练集为 AF-Think 标注的 YouTube8M 子集。

**主要指标**：
- MMAU：58.03%（±1.50），MMAR：40.32%（±0.57）
- 关键对比：较 SFT（54.65%）提升 3.38%，较 Audio MuToR（53.02%）提升 5.01%；零样本 CoT 崩溃至 18.03% 凸显推理鸿沟问题；与工业级模型仍有差距（Audio Flamingo 3 为 73.30%，Qwen2.5-Omni 为 71.50%）
- 消融：λ 取 1.0/2.0/3.0 均稳健（57.60–58.03），λ=3.0 方差达 ±2.83；每章节多寄存器变体降至 55.43% 且训练不稳定，验证单一序列首锚点最优。

**是否开源**：代码（GitHub）与 demo 页面均已开源。

### ⭐ 评分：7/10
评分理由：直指 LALM 推理鸿沟这一真实痛点，用简洁的训练期潜空间对齐换取零推理开销增益，且有注意力图机制分析与多组消融支撑，思路完整可复现。局限在于仅 SALMONN 13B 单一基座、Interspeech 篇幅下实验规模有限，绝对性能不及工业大模型，未与 Audio Reasoner 等 RL 路线直接对比，属实质性强、通用性待验证的工作。

## [10] Reusing Latent Speech Representations for Query-Conditioned Topic Localization in Transcripts

**arXiv ID**：2609.21844 | **方向**：语音大模型

**作者**：Steffen Freisinger、Philipp Seeberger、Thomas Ranzenberger、Tobias Bocklet、Korbinian Riedhammer

**机构**：纽伦堡应用技术大学（Technische Hochschule Nürnberg Georg Simon Ohm）

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21844 | **PDF**：https://arxiv.org/pdf/2609.21844.pdf | **代码**：https://github.com/steffrs/speech-topic-localization | **Demo**：暂无

### 📌 简介
针对语音长转录输入下游 NLP 系统低效且含大量无关上下文的问题，本文研究"查询条件化主题定位"：给定主题标题作查询，预测转录中最佳对应句子跨度。方法将冻结的 Whisper large-v3 顶层编码器状态按句子对齐区间池化为句级声学表示，与文本句嵌入门控融合后输入 VSLNet 与 QMSum-Pointer 两类定位头。Euronews 上 VSLNet 的 EM 从 45.26 升至 69.11（+23.85 点），严格边界下增益最大；跨域对结构化内容有效，自由会议增益有限。

### 🔧 技术方案

**问题背景：** 长转录直接输入检索、问答与摘要管线时注意力开销随长度二次增长且易"丢失中间信息"，而固定窗口切分与查询无关的主题分段均无法对齐用户信息需求。现有跨度定位以文本/视觉为主，弃用了停顿、韵律、说话人与场景切换等可标示主题边界的声学线索，而这些线索天然存在于语音链路必经的 ASR 编码器内部状态中。

**模型架构：** 离线阶段将 VAD 切分后不超过 30 秒的音频块经 ASR 转写并保留编码器状态；转录以 Punkt 分句，句子时间戳框定的帧序列经 Temporal 池化（Mean-ext，向两侧各扩 1.28 秒）得句级声学向量，与文本句嵌入（MiniLM）分别线性投影到 d=128、门控融合为 V，再经 QANet 式卷积加自注意力编码得与查询无关、可缓存的上下文矩阵 C。在线阶段查询以同一编码器做词级编码，交由定位头预测起止：VSLNet 用上下文-查询注意力加查询引导高亮与起止 softmax；QMSum-Pointer 用起点指针先打分、终点指针条件于起点表示。定位模型结构不变，仅增强输入表示。

**核心创新：** (1) 首次把 ASR 编码器状态零额外成本复用为句级声学表示做查询条件化定位，无需独立音频编码器；对照专用 wav2vec 2.0 编码器反而更差（EM 67.00 对 69.11），确立"搭便车"范式。(2) 系统消融四种池化（Mean、Mean-ext、Mean+Std、首尾 2.56 秒边界窗）、三种融合（求和、拼接、门控）与层级选择：Mean-ext 加门控最优且各变体差距小，性能随层数加深单调提升，末层最佳。(3) 用线性探针检验边界敏感假设：在 Euronews 上声学探针的主题起始/结束/边界分类 AUC 达 97.76/96.33/95.05，显著高于文本探针的 82.90/62.76/71.69，印证 ASR 状态携带边界线索。

**训练策略：** AdamW，权重衰减 0.01，学习率 3e-4 配余弦衰减与 5% 线性预热，批大小 32，至多 20 轮、dev 早停耐心 2；损失为起止交叉熵，VSLNet 另加高亮损失（扩展率 0.1）。冻结全部 ASR 与文本编码器，仅训练投影、融合、编码定位层；三种输入各训一个模型。

### 📊 实验结果
**数据集**：Euronews（六语新闻）与 YTSeg（19299 个英语 YouTube 视频）训练与域内评测；AMI（英语会议）与 Videoaula（葡语讲座）零训练跨域迁移。

**主要指标**：
- EM 与 R@1（IoU≥0.7/0.5/0.3）：VSLNet 在 Euronews 上 T+A 达 EM 69.11、R@1@0.5 79.66，YTSeg 达 EM 20.56、R@1@0.5 48.63，双数据集双定位头均最优。
- 与文本-only 基线差值：Euronews EM +23.85（Whisper）与 +18.23（Canary），YTSeg +6.68；增益在 EM 与 IoU≥0.7 下最大，说明改善集中在边界精度。跨域迁移中 VSLNet T+A 在全部四数据集取得最高 R@1，优于固定窗口与 BM25/稠密检索基线；但 AMI 上 EM 仅 1.04，QMSum-Pointer 融合音频后 R@1 反降 0.56。
- 计算：T+A 离线 FLOPs 较文本-only 增约 74%（220M 对 126M），在线计算与存储上下文规模完全不变。

**是否开源**：公开评测代码、定位模型权重与 Euronews 章节标题抽取脚本（GitHub：steffrs/speech-topic-localization），无 Demo 页面。

### ⭐ 评分：7/10
评分理由：工程复用思路务实有效，免训练地以 ASR 中间状态显著提升跨度定位精度，且经两 ASR、两定位头、四数据集、探针与声学线索分析交叉验证，结论可信。不足在于模型侧仅冻结编码器与浅融合，无架构创新；自由对话域几乎失效；查询依赖标注主题标题；未定位声学增益的具体线索来源。属部署价值明确的扎实增量工作。

## [11] Per-Aetiology Contrastive Severity Embeddings with Phonological Pseudo-Labelling for Multilingual Dysarthric Speech

**arXiv ID**：2609.21789 | **方向**：语音大模型

**作者**：Bernard Muller、Antonio Armando Ortiz Barrañón、LaVonne Roberts

**机构**：The Scott-Morgan Foundation（英国）、蒙特雷理工学院（墨西哥）、SMF Labs（法国）

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21789 | **PDF**：https://arxiv.org/pdf/2609.21789.pdf | **代码**：暂无（录用后开源） | **Demo**：暂无

### 📌 简介
多病因构音障碍严重度系统常把所有病因混入单一标签空间，本文首次在架构、配方、评测全对齐条件下检验该"混合假设"：同一 HuBERT-base 骨干与三阶段对比训练，分别训练 CP、PD、ALS 病因专属模型与混合基线，并用免训练音系 d-prime 伪标签扩充少数严重度类。说话人不相交、泄漏过滤的留出测试上，分病因模型全面胜出：CP macro F1 0.829 对 0.676（相对 +22.6%），PD 0.715 对 0.511（+40.0%），ALS 0.788 对 0.596（+32.3%）；CP 上伪标签再贡献 +4.3 个百分点。

### 🔧 技术方案

**问题背景：** CP、PD、ALS 的临床量表数值语义不可互换，音系退化模式亦不同：PD 少动型晚期才丢辅音对比，CP 痉挛型早期即崩解 stridency 与发音方式对比。SpICE 等大模型隐含假设严重度是跨病因单一可学习构念，从未受控验证。

**模型架构：** HuBERT-base（95M、12 层，顶 4 层解冻），帧级隐状态均值池化为 768 维，经两层 MLP 投影头（768→512→256）L2 归一化为单位超球面 256 维嵌入；下游用冻结嵌入上的不加权线性 probe，kNN-15 作无权重偏置对照。按 CP/PD/ALS/混合共训四模型。

**核心创新：** (1) 首个受控分病因对混合对比：仅改标签空间，其余全固定；共交集重评与"混合编码器+分病因头"消融证明增益在编码器本身——换头仍落后分病因编码器 0.09–0.20 F1。(2) 三阶段课程对比：Stage1 全库健康-障碍二分类 InfoNCE（批 256、AdamW 1e-4，四模型共享初始化）；Stage2a 边界相邻类作 3 倍加权困难负例（温度 0.07），Stage2b 序数三元组按秩距用 0.2/0.4 margin；Stage3 同严重度跨语言对齐并保留三元组正则。(3) 免训练音系伪标签：MFA 对齐、冻结 HuBERT 按音素池化、同语言健康人上算 9 方向 d-prime，11 维合成分数按分位数映射 Stipancic 四级，为 5 库 7 语 1181 名无标注说话人打序数标签。

**训练策略：** Stage1 用 1,429,582 样本、30 库 10 语（含 11 个健康大库做类平衡负例）；后两阶段限 10 个临床标注库加伪标签子集，CP/PD/ALS 各 3/7/5 语。健康对照按语言匹配、上限为最大严重度类、占比控制 28–42% 防语言捷径。各阶段验证 F1 早停（patience 2），四模型合计约 68 GPU 小时（单 H100）。教训：ALS 上加权 probe 使 moderate 类崩塌（F1 0.038），改不加权后 macro F1 由 0.586 升至 0.788。

### 📊 实验结果
**数据集**：UA-Speech、TORGO、CDSD、SSNCE-Tamil、VOC-ALS、MDSC、EWA-DB、Neurovoz、SAP 等多语注册表；Phase2 过滤评测池 89,068 样本、8 语言，按目标病因加语言匹配健康对照评分。

**主要指标**：
- CP：macro F1 0.829（准确率 88.5%）对混合 0.676，差 +0.153（+22.6%）
- PD：0.715 对 0.511（+40.0%）；ALS：0.788 对 0.596（+32.3%），mild/moderate/severe 逐类同升
- 伪标签消融：CP 纯临床 0.786，加 144 SAP+44 CDSD 伪标签说话人至 0.829（+4.3pt）
- 稳健性：说话人交集重评 6 格中 5 格方向保持；UA-Speech LOSO 准确率 80.0% 超 SALR 9.5pt；置信度≥0.9 保留 64% 样本达 0.924 F1；隐患：伪标签逐例对临床 κ 仅 0.069，ALS/PD 测试 SAP 占 94%/67%

**是否开源**：代码、清单与权重承诺录用后公开；伪标签音系管线为前作开源实现。

### ⭐ 评分：7/10
评分理由：以严谨受控实验动摇病因混池训练主流范式，共交集重评与头消融使结论可信，对多语言构音障碍数据策略有直接实践价值；但模型为既有组件组合，伪标签个体级与临床一致性很低（κ 0.069），测试高度英语/SAP 集中、单种子，属实质实验发现而非方法突破。

## [12] Partial Accent-Control Editing in Frozen Speech Representations for Accent Conversion

**arXiv ID**：2609.22031 | **方向**：语音大模型

**作者**：Yangyang Qu、Michele Panariello、Massimiliano Todisco、Nicholas Evans

**机构**：EURECOM（法国索邦安提波利斯）

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.22031 | **PDF**：https://arxiv.org/pdf/2609.22031.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
口音转换系统多依赖训练生成器，转换强度在推理时不可控。本文提出 PACE：一种免生成器训练的口音转换框架，在冻结 WavLM 第6层1024维表征上做局部编辑——先用非平衡最优传输估计目标口音参考并沿口音预测子空间加性更新源特征，再在目标口音参考库上 top-k 检索并按权重 γ 受控融合。在 L2-ARCTIC 5000 对跨口音协议下，默认工作点口音分类器准确率 39.0%（DART 28.2%、MLV 24.3%），WER 16.0% 与 STOI 0.802 显著优于生成式基线，代价是说话人相似度降至 0.583。

### 🔧 技术方案

**问题背景：** 口音转换需在保留语言内容与说话人属性的同时使语音贴近目标口音。现有方法以训练好的生成模型为主，口音修改强度由模型或条件输入固化，推理时无法调节，难以量化"口音强度—源保持"的折中。

**模型架构：** 系统分两阶段，全程基于冻结 WavLM-Large 第6层帧特征，不训练任何声学生成器。首先用训练集带口音标签数据经偏最小二乘回归得到正交化口音预测子空间投影 P_ac 并固定。阶段一对源帧与目标口音参考库（每口音约5万帧）在子空间内做熵正则非平衡最优传输匹配，按传输权重加权得到目标参考帧，将子空间内偏移映射回原空间以 α 尺度仅沿口音方向加性更新。阶段二在口音子空间对编辑后源帧做 top-k（k=4）余弦检索，用命中索引取回 WavLM 原空间的参考帧均值，按 γ 与源帧凸组合融合。最终序列经固定的 kNN-VC 后端（mel 投影加 HiFi-GAN 声码器）在 16kHz 合成波形。

**核心创新：** (1) 将非平行口音转换形式化为冻结自监督表征上的可控局部编辑，α 与 γ 成为推理时可连续调节的工作点旋钮，直接暴露口音证据与源保真的权衡曲线，而非由训练固定的生成器行为。(2) 非平衡最优传输提供无帧级对齐下的软目标参考：KL 不守恒项容忍源帧在目标库中无近邻、库帧不被使用的非平行情形，且更新被限制在口音可预测方向，保护内容与说话人分量。(3) "子空间检索、原空间融合"双空间设计：检索在低维口音敏感空间完成，融合特征取自全维 WavLM 空间以保留声学细节；消融显示直接在原 WavLM 空间检索虽提升准确率到 52.7%，但 SECS 跌至 0.470，证明子空间的必要性。

**训练策略：** 无可训练模块，WavLM、mel 投影、HiFi-GAN 全部冻结；评测协议为 1000 条源语句各转 5 个非自身口音共 5000 对，参考库与源说话人严格不相交。指标含 Whisper-base 转录一致性 WER/CER、STOI 可懂度、Resemblyzer 说话人嵌入余弦相似 SECS，及外部 DistilHuBERT 口音分类器目标口音准确率。超参 α=1.0、γ=0.7、λ=0.1、ε=0.01。

### 📊 实验结果
**数据集**：L2-ARCTIC（阿拉伯语、印地语、韩语、普通话、西班牙语、越南语六种 L1 口音）

**主要指标**：
- 默认 PACE：WER 16.0%、CER 8.3%、STOI 0.802、SECS 0.583、准确率 39.0%
- γ 从 0.3 到 0.7：准确率 10.6%→39.0%，WER 12.9%→16.0%，SECS 0.770→0.583
- 关键对比：较最强基线 DART 准确率 +10.8pt、WER −13.7pt、STOI +0.600；仅 SECS 落后 0.241；参考替换极限点准确率 66.5%；分口音西语/越语达 91.7%/97.2%，韩语仅 9.2%

**是否开源**：论文未提供代码与 Demo 链接，暂无

### ⭐ 评分：7/10
评分理由：把口音转换重构为冻结 SSL 表征上的局部编辑，OT 加子空间检索融合的组合简洁有效，共享协议下全面超越两个复现生成式基线并给出可量化权衡曲线，方法论贡献实质。但仅靠分类器代理指标、无人听评测，说话人相似度受损，韩语转换近乎失败，限制其高度。

---

## 语音前端

## [13] BLINC: Blind Calibration For Training-Free Speech Enhancement Adaptation

**arXiv ID**：2609.21898 | **方向**：语音前端

**作者**：Tobias Raichle、Ekaterina Gavrilko、Bin Yang

**机构**：斯图加特大学信号处理与系统理论研究所（德国斯图加特）

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21898 | **PDF**：https://arxiv.org/pdf/2609.21898.pdf | **代码**：https://github.com/tobiaaa/SETTA | **Demo**：暂无

### 📌 简介
语音增强模型在域偏移下性能退化，而多数测试时自适应（TTA）方法需反向传播更新权重，存在永久改变模型与误差累积风险。本文提出BLINC，一种免训练TTA：不动模型权重，用直方图匹配把预测的时频掩码重量化为双峰目标分布，分布参数仅由含噪信号的语音活动占比等盲特征估计，系数在验证域离线以PESQ拟合。在EARS/WHAM!/VoiceBank/DNS多域评测中，BLINC在AM与CMGAN两模型上取得全方法最高PESQ、CSIG、COVL（CMGAN平均PESQ 2.66），RTF仅0.003，以近乎零开销追平或超过全部基于损失的TTA基线。

### 🔧 技术方案

**问题背景：** 训练数据无法覆盖说话人与声学环境的全部多样性，SE模型部署时必然遭遇域偏移；含噪录音的干净参考不可恢复，自适应只能无监督。域偏移下掩码型SE模型的TF掩码丧失双峰特性、取值向中间堆积，增强性能随之下降。现有TTA用自监督损失更新部分权重，需要测试时梯度计算并永久改变模型。

**模型架构：** 纯后处理校准方法，无训练。数据流：冻结的掩码型SE模型对含噪谱Y预测掩码M，估计X̂=M⊙Y。BLINC对M全体元素用经验CDF（概率积分变换）映到均匀分布，再经目标分位函数映回，得重量化掩码M̃；复合重映射单调不减，保留各TF bin的相对排序、只替换其取值。目标分位函数为三参数sigmoid形式Q(x)=(1-c)·σ(a(x-b))+c，b对应噪声模式bin占比、a控制陡峭度、c为下限以保留被错排的语音并避免全抑制伪影。三参数写成盲特征语音活动占比P_Sp的仿射函数，输出波形再按盲SNR估计做功率重标定P_out=SNR/(1+SNR)·P_in。

**核心创新：** (1) 先行预知"正确预测"的形态：论证理想掩码分布可被紧凑参数化双峰族捕获，使原地校正无需RaR式的在线非侵入指标优化，从根源消除其延迟开销。(2) 盲特征构建目标分布：用单个语音活动占比同时预测陡峭度、中点、下限，无需干净参考或经典算法参考分布；仅6个仿射系数，在验证域上以PESQ为准则黑盒搜索离线拟合，因而不要求指标可微。(3) 校准误差与排序误差的分解分析：直方图匹配只能消除校准误差，消融中免构型oracle界定一切保序校正的性能上限，明确划出本方法饱和点与权重自适应保留优势的场景。

**训练策略：** 无任何测试时训练，只离线拟合6个系数：以DAPS录音混合TAU环境噪构成验证域，与全部目标域不重叠，系数一次拟合处处沿用；AM与CMGAN分别拟合，因二者排序可靠性与复数加性项下掩码角色不同。

### 📊 实验结果
**数据集**：源域EARS+WHAM!；目标域EARS+DEMAND、VoiceBank+WHAM!、VoiceBank+DEMAND、DNS挑战赛测试集（覆盖六语种）；验证域DAPS+TAU。

**主要指标**：
- 感知质量（跨目标域平均）：AM模型PESQ 2.17、CSIG 3.21、COVL 2.66，CMGAN模型PESQ 2.66、COVL 3.22，两模型均为全方法最高
- 关键对比：AM上PESQ较最强基线LaDen（2.13）高0.04，CMGAN上较MPol（2.64）高0.02；RTF 0.003与未适应源模型持平，远低于LaDen 0.372与RaR复现0.903
- 代价与边界：信号级SI-SDR明显回退（AM 11.50 dB、CMGAN 9.42 dB，低于源模型），CMGAN在多数DNS条件下落后LaDen与MPol
- 消融（AM，VBD）：常目标PESQ仅2.45，BLINC 2.55，域内拟合2.65，逐条sigmoid oracle 2.75、免构型oracle 2.79

**是否开源**：代码已开源

### ⭐ 评分：7/10
评分理由：以封闭形式重量化取代测试时权重更新，思路优雅且实用，RTF近零而感知质量全面领先，误差分解分析透彻。局限在于只修复校准误差、无法纠正排序退化，信号级指标明显受损，系数拟合绑定PESQ准则且依赖验证域选择，对强模型增益跨域不稳。属扎实实质贡献而非突破。

## [14] Online Algorithms for Independent Low-Rank Matrix Analysis and Rank-Constrained Spatial Covariance Matrix Estimation Based on Maximum Weighted Likelihood Estimation

**arXiv ID**：2609.21180 | **方向**：语音前端

**作者**：Yuto Ishikawa、Norihiro Takamune、Tomohiko Nakamura、Daichi Kitamura、Hiroshi Saruwatari、Yu Takahashi、Kazunobu Kondo

**机构**：东京大学信息理工学研究科、香川高专门学校、雅马哈公司

**发布日期**：2026-09-18 | **论文**：https://arxiv.org/abs/2609.21180 | **PDF**：https://arxiv.org/pdf/2609.21180.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
扩散噪声下的实时多通道目标语音提取问题：此前块批式B-RCSCME假设批内空间特性平稳，说话人移动时性能骤降。本文将最大加权似然估计（MWLE）引入NSR-ILRMA与RCSCME，推导逐帧在线更新算法，并配套稳定化与加速技巧。仿真实验（JVS语音+DEMAND噪声+镜像法混响，T60约346毫秒）与东京大学实测录音中，所提O-RCSCME在全部六种噪声条件下SDR/SIR改善均优于O-IVA、O-SR-IVE与B-RCSCME，距离线上界SDR差距小于1分贝，最大帧处理时间低于32毫秒移位长度，满足实时约束。

### 🔧 技术方案

**问题背景：** 离线最先进的RCSCME类方法（ILRMA/NSR-ILRMA前端加秩约束空间协方差估计后端）在扩散噪声下提取精度最高，但整流程难以在STFT移位长度内完成；已有块批实现B-RCSCME依赖批内空间平稳假设，且RCSCME初始化含 Moore-Penrose 伪逆等高开销矩阵运算，无法跟踪目标说话人移动。

**模型架构：** 两级逐帧流水线：在线NSR-ILRMA部分更新解混矩阵W与NMF变量r，输出目标通道分离信号及时不变空间参数（目标导向矢量、秩M-1噪声协方差、补全向量b）；在线RCSCME部分固定上述参数，在线更新目标/噪声时变方差与秩1系数λ，最后经多通道维纳滤波提取目标源像。推导分三步：（一）按MWLE对各帧似然施加随时间衰减的权重构造帧代价函数；（二）用MM/ME辅助函数法得到朴素更新规则；（三）将含时间求和的中间量（加权空间协方差、NMF分式累加）用上一帧估计近似，实现O(1)递推在线更新。

**核心创新：** (1) 首次把MWLE框架应用于时变生成模型（ILRMA的NMF方差与RCSCME的秩约束协方差），克服了作者前作逐帧生成式建模只能处理时不变模型（IVA）的局限，且权重结构设计使递推更新自然涌现，遗忘因子β=γ=0.95兼顾跟踪与稳定。(2) 在线NSR-ILRMA稳定化技术：仅更新前min(⌈τ/2⌉,K)个NMF基并设基变量重置阈值ε_basis=0.4防止病态收敛，配合正则权重归一化μ̄与方差下限ε_ILRMA=1e-3，显著改善起始与长时阶段性能。(3) 在线RCSCME加速技术：把更新式中涉及逆矩阵的运算解析变形为可预计算的标量中间变量（κ/ν量），使每帧迭代退化为纯标量运算，并以平均特征值×超参ι替代最小特征值初始化λ，绕开MP伪逆瓶颈，实测比块批RCSCME每帧省约10毫秒。

**训练策略：** 无学习模型，纯迭代优化实现。Python+CPU双精度；K=10个NMF基；RCSCME时变参数用最近C=30帧；在线NSR-ILRMA每帧1次迭代、在线RCSCME每帧2次；逆伽马稀疏先验超参ϱ̄=1.6、ς̄=1e-16；方向先验未知时目标通道索引n(t)固定为N。

### 📊 实验结果
**数据集**：仿真：JVS数据集100说话人语音拼接20/60秒；DEMAND六场景噪声（车站/咖啡馆/交通/自助餐厅/餐馆/公共广场）各24条；Pyroomacoustics镜像法生成RIR（T60约346毫秒），四通道圆阵半径3厘米，输入SNR 0分贝，16千赫兹，STFT汉宁窗64毫秒/移位32毫秒；移动场景在10至20秒、30至40秒恒定速度绕阵移动。实测：东京大学伊藤国际研究中心，10人讲话云加顶部音乐扬声器，T60约750毫秒。

**主要指标**：
- 平稳仿真：O-RCSCME六种噪声下SDR/SIR全面领先四个基线；与潜在离线上界Potential差距小于1分贝SDR
- 在线NSR-ILRMA单评：比块批B-NSR-ILRMA后期SDR改善高约2分贝
- 消融：Online-Online组合最优；在线RCSCME比块批版每帧最大处理时间少约10毫秒；所有方法帧时间均低于32毫秒实时阈值
- 移动说话人与实测场景：仍优于B-RCSCME、O-SR-IVE、O-IVA-IP/ISS（dB数值以曲线图给出，未列表）

**是否开源**：未提供代码/Demo。

### ⭐ 评分：7/10
评分理由：把B-RCSCME完整在线化，MWLE为时变BSS模型给出统一的逐帧推导框架，稳定化与标量化加速工程扎实，实验覆盖平稳/移动/实测并含消融分析，实时性验证充分；不足为增量式扩展自会议论文、依赖目标方向先验、缺少逐条件定量SDR表与听觉测试，理论贡献大于实际新范式。

## [15] HAMMER: Harmonic-Aware Parallel Context Modeling and Discriminator-Free Perceptual Optimization for Speech Enhancement

**arXiv ID**：2609.21171 | **方向**：语音前端

**作者**：Shang-Fu Chen、Szu-Wei Fu、Sung-Feng Huang、Rong Chao、Wen-Huang Cheng、Yu Tsao

**机构**：台湾大学、中研院信息所、NVIDIA、VinUni（4家，NTU与中研院/台大成员联合主导）

**发布日期**：2026-09-21 | **论文**：https://arxiv.org/abs/2609.21171 | **PDF**：https://arxiv.org/pdf/2609.21171.pdf | **代码**：https://github.com/shangfuu/HAMMER.git | **Demo**：暂无

### 📌 简介

单通道语音增强中，Attention+Mamba混合仅作为通用序列混合器，未显式建模浊音谐波周期性；又因PESQ不可导而普遍依赖度量判别器，带来复杂度与对抗不稳定。本文提出HAMMER：TF-HAM块沿频谱时间/频率两轴并行运行RoPE自注意力与双向Mamba2，再接语音适配的自相关前馈网络（AFFN）编码局部周期结构；MEPR以Soft-PESQ与可微LLR损失直接提供感知监督，完全无判别器。仅2.39M参数在VoiceBank+DEMAND达PESQ 3.69、COVL 4.41，持平或超越对抗式系统；推理时感知对比拉伸使PESQ升至3.79，无需重训。

### 🔧 技术方案

**问题背景：** 现有混合架构按固定顺序堆叠注意力与状态空间模型，忽略浊音谐波栅格与重复时频模式这一强先验；MetricGAN式方法用学习型判别器代理不可导的PESQ，而可微替代算子又因硬阈值/饱和产生梯度死区。

**模型架构：** 沿用SEMamba双解码器框架：STFT幅度（c=0.3幂压缩）与相位作两通道输入，DenseEncoder后堆叠N=4个TF-HAM块（C=64通道、4头、dstate=16、expand=4），幅/相双解码器iSTFT重建，共2.39M参数。每个TF-HAM块=时间轴与频率轴各一次"并行Attention-Mamba混合器"，后接AFFN。

**核心创新：** (1)并行混合头：借鉴Hymba，注意力与Mamba2分支处理同一RMSNorm特征，各自输出再归一化求和投影，避免一分支先被另一分支过滤；残差式沿两轴依次施加。(2)谐波感知AFFN：将Flickerformer自相关模块迁移到时频P×P patch，依Wiener–Khinchin定理由2D FFT功率谱求自相关R_p，经FFT2^{-1}(X_p+αS_p)+βR_p强化周期分量（α、β可学习），零初始化γ残差注入。(3)MEPR：基于P.862可微管线软化三处硬算子——泄漏死区（λ=0.05保留亚阈值梯度）、不对称sigmoid门（τ_g=0.5）、软上限替代min饱和（τ_s=2），并新增16阶LPC可微LLR（480窗/120跳、批量Levinson-Durbin、逐句截断最低95%帧均值），实现无判别器直接感知优化。

**训练策略：** 总损失=0.9幅度+0.3相位+0.1复谱+0.2时域+0.1组合+0.2 Soft-PESQ（内部再缩放0.5）+0.1 LLR，无对抗项；VB+DEMAND训练集（11572句×28人，SNR 0/5/10/15dB）取2秒段，AdamW lr=5e-4逐epoch×0.99，bf16、双卡batch4、梯度裁剪1.0、EMA 0.999，约70 epoch收敛。

### 📊 实验结果

**数据集**：VoiceBank+DEMAND（test：824句×2未见过说话人，SNR 2.5–17.5dB，16kHz）

**主要指标**：
- 无PCS：PESQ 3.69／CSIG 4.83／CBAK 3.97／COVL 4.41／STOI 0.96，参数2.39M
- 关键对比：较最强基线Mamba-Former（3.64/4.39，2.14M）PESQ+0.05、COVL+0.02；较SEMamba+0.12/+0.12；PCS α=0.65推理即达PESQ 3.79（超过需重训PCS的Mamba-SEUNet L的3.73），但CBAK 3.97略低于Mamba-Former 4.02
- 消融：仅Soft-PESQ 3.58→并行TF-HAM后3.69/COVL 4.39→+LLR COVL 4.41；同损失串行变体3.67/4.40，证实并行融合更优

**是否开源**：代码承诺发布于GitHub（"will be available"），暂未上线；无demo页；评测使用公开基准与参考实现计分，可复现性预期良好。

### ⭐ 评分：6/10

评分理由：三点创新组合（并行混合、AFFN谐波先验、无判别器感知损失）工程扎实，刷新VB+DEMAND最优并证明可绕开MetricGAN判别器，推理时PCS可控PESQ–CBAK权衡有实用价值；但对最强基线仅+0.05 PESQ，仅单数据集、缺泛化与听感实验，谐波模块借自视觉任务且周期性收益未独立量化，整体属高质量增量工作而非方法突破。

---

## 其余论文（仅列标题与链接）

### [16] The Hidden Cost of Digits: Number Normalization and WER in ASR Systems

- **arXiv ID**：2609.21084 | **方向**：语音大模型 | **评分**：6/10
- 揭示 WER 评测中数字归一化缺口：波兰语等高屈折语言下缺失数字归一化可致 WER 差异超 2 个百分点、甚至颠倒多语言榜单系统排名；对 VoxPopuli 与波兰议会语料做系统归一化对照实验
- **论文**：https://arxiv.org/abs/2609.21084 | **PDF**：https://arxiv.org/pdf/2609.21084.pdf | **代码**：暂无 | **Demo**：暂无

### [17] Cross-Lingual Parkinson's Disease Severity Assessment Using Pre-trained Speech Embeddings: A Multi-Class Evaluation

- **arXiv ID**：2609.20875 | **方向**：语音大模型 | **评分**：6/10
- 用四个开源语音基础模型嵌入在三个数据集上做多语言 PD 严重度多分类的 zero/k-shot 评测：k-shot 跨语言适配提升 F1 达 10-30 分且源语音不受损，性能对数据集属性与适配策略敏感（IEEE SLT 2026）
- **论文**：https://arxiv.org/abs/2609.20875 | **PDF**：https://arxiv.org/pdf/2609.20875.pdf | **代码**：暂无 | **Demo**：暂无

### [18] The Spoken Wikipedia Presentation Corpus

- **arXiv ID**：2609.21676 | **方向**：语音大模型 | **评分**：6/10
- 发布 553 小时英/德/荷多语种"演讲音频+LLM 生成幻灯片"对齐语料，面向多模态 ASR；音频-only 最佳模型 micro-WER 10.23%/CER 6.48%，多模态零样本 omni 模型仍难用好幻灯片上下文（SLT 2026）
- **论文**：https://arxiv.org/abs/2609.21676 | **PDF**：https://arxiv.org/pdf/2609.21676.pdf | **代码**：暂无 | **Demo**：暂无

### [19] Voice-Light: A Full-Duplex Cascaded Voice Agent with Causal Turn-Taking and Speculative Generation

- **arXiv ID**：2609.20995 | **方向**：语音大模型 | **评分**：5/10
- 全双工级联语音智能体系统论文：因果适配器共享流式 ASR 编码器、可回滚播放控制与私有投机生成，端到端首个音频中位延迟 758ms；诚实报告学习型端点检测召回仅 12.53% 故保留混合控制器；数据/代码/模型全开源
- **论文**：https://arxiv.org/abs/2609.20995 | **PDF**：https://arxiv.org/pdf/2609.20995.pdf | **代码**：https://github.com/BertilBraun/Voice-Light | **Demo**：https://voice.bertil-braun.de

### [20] Curriculum-Based Noise Adaptation for Phoneme-to-Text Reconstruction in Visual Speech Recognition

- **arXiv ID**：2609.20839 | **方向**：语音大模型 | **评分**：5/10
- PECT 课程学习框架渐进适配 NLLB 音素-文本重建模型（合成扰动+多域/目标域伪标签），LRS2/LRS3 上对 V-ASR/PV-ASR/HP-VSR 多前端一致改善（HP-VSR WER 23.3→22.2），增量式工程改进
- **论文**：https://arxiv.org/abs/2609.20839 | **PDF**：https://arxiv.org/pdf/2609.20839.pdf | **代码**：暂无 | **Demo**：暂无

---

*Generated on 2026-09-21*
