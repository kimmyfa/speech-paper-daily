# 2026-08-17 语音论文速递

**共收录**: 8 篇 | **语音大模型**: 7 篇 | **语音前端**: 1 篇

> 今日 arXiv 语音相关论文共命中 8 篇（cs.SD 新提交 5 篇，eess.AS 新提交 5 篇，交叉列表 3 篇）。
> 以下是按评分排序的结果。

---

## 语音大模型

---

## [1] VoiceDesigner: Text-to-Voice Generation and Editing via Unified Diffusion Modeling and Data Augmentation

**arXiv ID**：2608.13613 | **方向**：语音大模型 / TTS

**作者**：Jiarui Hai, Karan Thakkar, Ke Chen, Yunyun Wang, Jiaqi Su, Rithesh Kumar, Mounya Elhilali, Zeyu Jin

**机构**：Johns Hopkins University, Adobe Research（Jiarui Hai在Adobe实习期间完成）

**发布日期**：2026-08-17 | **论文**：https://arxiv.org/abs/2608.13613 | **PDF**：https://arxiv.org/pdf/2608.13613.pdf | **代码**：暂无 | **Demo**：https://voicedesigner-demo.github.io/

### 📌 简介
现有文本到语音生成（TTV）系统面临两大核心挑战：一是生成声音的多样性不足，难以覆盖真实人类说话人和虚构角色；二是缺乏灵活的声音编辑能力，如声音克隆和属性修改。本文提出VoiceDesigner，一个统一的声音生成与编辑框架。在数据层面，作者设计了混合数据流水线，利用DSP音频效果合成（变调、共振峰偏移、混响等）和生成式仿真（零样本TTS+语音转换）来构造覆盖人类和非人类声音的多样化数据集。在模型层面，基于单流MM-DiT架构，引入token级自适应层归一化（AdaLN）和3D旋转位置编码（3D-RoPE），在统一框架内联合建模语音生成、克隆和指令引导编辑。主观和客观实验表明，VoiceDesigner在声音描述对齐和编辑指令遵循方面超越现有开源系统，WER仅1.22%，风格准确率0.66，同时保持具有竞争力的感知质量和可用性。

### 🔧 技术方案

**问题背景：** 现有TTV系统主要基于有声书和播客等自然语音数据训练，难以生成小说创作和游戏制作中所需的虚构角色声音（如龙、恶魔、机器人等），也无法处理如"低沉雷鸣般的龙吼"这类基于角色身份而非显式声学属性的描述。此外，声音克隆方法主要针对常规人声设计，对非传统或强风格化声音的克隆鲁棒性不足；指令式声音编辑方法编辑能力有限且难以保持语音质量。更重要的是，生成和编辑通常作为独立系统实现，增加了训练和部署成本。

**模型架构：** VoiceDesigner采用flow-matching扩散模型，整体基于DAC-VAE编码器-解码器在音频潜空间（48kHz采样率，25Hz潜帧率）中操作。核心骨干是1.0B参数的单流多模态扩散Transformer（MM-DiT），所有模态token在共享参数的统一Transformer中拼接处理，进入统一Transformer前每个模态先经过独立的小型Transformer模块。文本指令由T5Gemma-XL编码，文本由F5-TTS tokenizer编码。推理时使用句子级时长预测器（基于Qwen3-0.6B初始化，Dasheng编码器提取参考音频特征）估计目标语音时长，加性噪声初始化后由扩散模型去噪解码。

**核心创新：** (1) Token级AdaLN：针对统一潜空间中不同模态token具有异质扩散状态的问题（生成目标token加噪而条件token保持干净），为每个音频token分配连续时间嵌入t∈[0,1]，生成目标token的t从[0,1]采样，参考音频token固定t=1，并引入专用条件token [C]区分指令和文本条件。这使得模型显式区分条件信号与生成目标，加速收敛并提升性能，同时自然扩展到语音延续任务（前缀token保持t=1无噪，后续token注入扩散噪声）。(2) 3D-RoPE：将标准RoPE扩展到三维位置空间，指令token编码在x轴，文本token在y轴，干净和有噪音频token在z轴，对齐的文本-音频token对共享x坐标以保持时间对应关系。相比1D位置编码，避免了异构条件被强制压入单一序列结构的问题，保留了模态感知和对齐感知的位置先验。(3) 混合数据仿真流水线：DSP流水线通过Pedalboard、librosa、Parselmouth等库组合变调、共振峰偏移、混响、均衡、带通滤波和动态范围压缩等效果，将普通语音转换为龙、恶魔、机器人等非人类角色声音；生成式仿真流水线利用零样本TTS和语音转换模型扩增风格化数据，并通过多阶段过滤（WER<0.1、说话人相似度>0.6、双候选择优）保证数据质量。

**训练策略：** 采用AdamW优化器，三阶段训练。第一阶段预训练：在56,165小时多语言数据（Emilia、Common Voice、LibriTTS-R、HiFiTTS-2-44.1k子集）上训练400k步，批大小512x20s，学习率1.5x10^-4，64张A100 GPU。第二阶段任务适配：在微调数据集（ESD、RAVDESS、SAVEE、Expresso、EARS、CapSpeech-Agent、VCTK、DreamVoice等公开情感/口音/音色数据集，16小时内部角色声音数据集，以及DSP和生成式仿真扩充数据）上训练100k步，批大小384x30s，学习率8x10^-5，64张A100 GPU。第三阶段质量精炼：仅使用真实录音和少量高质量DSP仿真数据微调10k步，批大小128x30s，学习率1x10^-5，16张A100 GPU。

### 📊 实验结果
**数据集**：Seed-TTS test-en（客观评估）、内部构建的520条TTV benchmark、75条TTV-Traits和150条TTV-Character主观评测集、100条声音编辑评测对

**主要指标**：
- TTV生成：WER 1.22%（最低），Style-ACC 0.66（最高），MOS-C 3.93（开源最高）
- 声音克隆（Seed-TTS基准）：WER 1.70%（最低），SIM-o 0.757（开源最高，仅次于闭源SeedTTS）
- 角色声音克隆主观：MOS-T 3.93（最高），MOS-S 4.00（最高）
- 声音编辑：MOS-E 4.129（最高），SIM-t 0.884（最高）
- 实时性：生成RTF 0.36，编辑RTF 0.42（均优于对比方法）

**是否开源**：未开源（提供了Demo页面和内部数据集收集指南促进可复现性）

### ⭐ 评分：8.5/10
评分理由：VoiceDesigner在TTV领域做出了实质性贡献，首次在统一框架中同时支持声音生成、克隆和编辑三大任务，混合数据流水线设计巧妙且实用，有效解决了非人类角色声音数据稀缺问题。实验充分全面，在多个基准上均达到开源最优水平，消融实验清晰验证了Token-level AdaLN和3D-RoPE的有效性。扣分原因：模型和数据集均未开源限制了可复现性；与ElevenLabs等商业系统在感知质量上仍有差距；角色声音数据主要依赖内部16小时录音和DSP仿真，真实角色声音数据规模有限。

---

## [2] AT-ADD: All-Type Audio Deepfake Detection Challenge Summary

**arXiv ID**：2608.14249 | **方向**：语音大模型 / 音频深度伪造检测

**作者**：Yuankun Xie, Haonan Cheng, Jiayi Zhou, Xiaoxuan Guo, Tao Wang, Changhao Zhang, Jian Liu, Weiqiang Wang, Ruibo Fu, Xiaopeng Wang, Hengyan Huang, Xiaoying Huang, Long Ye, Guangtao Zhai

**机构**：中国传媒大学、蚂蚁集团、中国科学院自动化研究所、北京理工大学、上海交通大学

**发布日期**：2026-08-17 | **论文**：https://arxiv.org/abs/2608.14249 | **PDF**：https://arxiv.org/pdf/2608.14249.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
本文是ACM Multimedia 2026 AT-ADD大挑战赛的总结报告，针对音频深度伪造检测领域两大核心问题：一是在真实声学与信道变化下的鲁棒语音深度伪造检测（Track 1），二是跨语音、环境音、歌声和音乐四种类型的全类型音频深度伪造检测（Track 2）。挑战赛采用封闭设置，参赛者仅可使用组织者提供的训练/开发数据、信号级数据增强和可追溯的通用预训练模型。Track 1评估集包含26种未见生成方法产生的假语音并引入多种信号变换，Track 2评估集涵盖四类音频并引入域外真实样本。最终Track 1冠军WaveShield取得90.71% Macro-F1，Track 2冠军starfire取得96.10% Macro-F1。参赛系统普遍采用大规模自监督音频表征、丰富的数据增强、多裁剪推理以及结构化融合或路由策略。

### 🔧 技术方案

**问题背景：** 现有ADD研究在ASVspoof和ADD挑战系列中取得显著进展，但实际部署面临两大关键瓶颈：一是真实声学环境和信道条件下的鲁棒性不足，现有基准测试中的真实语音多来自受控环境，而实际场景中录音设备、声学环境、语言种类等因素存在巨大变化；二是面对异构音频类型（语音、环境音、歌声、音乐）时的泛化能力有限，生成式AI已能合成各种类型的高保真音频，而现有检测器大多仅针对单一语音类型设计。

**模型架构：** 参赛系统普遍采用"自监督预训练前端 + 专用后端"的架构范式，在不同规模（300M/1B/2B）的XLSR、W2V-BERT 2.0等SSL模型上构建检测器。Track 1冠军WaveShield基于W2V-BERT 2.0前端，集成AASIST、AASIST3和Adapter-MFA三种后端，通过三子系统logit平均融合。Track 2冠军starfire采用硬音频类型路由架构：用冻结的BEATs路由器将输入分为四类，语音分支使用XLSR+AASIST，非语音分支使用EAT-large+AASIST，最后应用类特定阈值和保守多裁剪池化策略。

**核心创新：** (1) Track 2首次将音频深度伪造检测从单一语音类型扩展到语音、环境音、歌声和音乐四种异构音频类型，并设计类型不可知的检测协议，测试时音频类型标签不提供，使任务更贴近真实部署场景。(2) 构建了大规模多类型音频深度伪造基准数据集，Track 1评估集包含26种未见生成方法并引入多种信号扰动，Track 2评估集引入域外真实样本检验泛化能力，数据集规模达十万级。(3) 明星系统starfire提出的硬音频类型路由架构（BEATs路由器+分支专用检测器）和类特定阈值策略，为处理异构音频类型的深度伪造检测提供了可复现的有效范式。

**训练策略：** 各系统广泛采用数据增强策略，包括MUSAN噪声、RIR混响、编解码/重编码（g711alaw/mp3/opus）、RawBoost、信号级扰动（量化/动态范围压缩/裁剪/EQ/掩蔽/重采样/变速/变调）、重放模拟、片段级操作（随机裁剪/真实片段拼接）等。损失函数方面使用AM-Softmax、focal loss、加权交叉熵等。训练策略包括分阶段冻结-LoRA到联合微调、两阶段优化（先全微调编解码增强，后冻结SSL前端加RIR视图一致性MSE损失）、DANN和GroupDRO域适应正则化等。

### 📊 实验结果
**数据集**：AT-ADD Track 1（训练集49,575条，开发集49,734条，评估集146,346条）/ AT-ADD Track 2（训练集146,781条，开发集91,069条，评估集229,373条，含语音/环境音/歌声/音乐四类）

**主要指标**：
- Track 1冠军WaveShield（w2vBERT2.0-AASIST）：Macro-F1 90.71%
- Track 1亚军Fosafer（ssl_gfcc_multiscale_ensemble）：Macro-F1 86.67%
- Track 1季军sonomsl：Macro-F1 86.63%
- Track 2冠军starfire（starfire_track2_audio_type_routed_ensemble）：Macro-F1 96.10%
- Track 2亚军orange9（E2E-ATADD）：Macro-F1 95.58%
- Track 2季军ThreeTO（MEDS）：Macro-F1 93.95%

**是否开源**：未开源

### ⭐ 评分：8/10
评分理由：本文作为ACM Multimedia 2026挑战赛总结，系统性地定义并解决了音频深度伪造检测领域的两大关键问题——鲁棒性和跨类型泛化。数据集规模大、类型覆盖广、评估协议设计严谨（含26+种未见生成方法和域外样本）。论文对参赛系统的技术方案分析详尽，揭示了SSL表征+数据增强+多裁剪推理+结构化融合的有效模式。但作为挑战赛总结，未提出全新的检测方法，且无开源代码或数据集，技术复现门槛较高。

---

## [3] VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents

**arXiv ID**：2608.13831 | **方向**：语音大模型 / TTS

**作者**：Edresson Casanova, Jaehyeon Kim, Mariana Graterol Fuenmayor, Shehzeen Hussain, Viacheslav Klimkov, Valentin Mendelev, Mikyas Desta, Paarth Neekhara, Piotr Zelasko, Chen Chen, Elena Rastorgueva, Ke Hu, Ankita Pasad, Xuesong Yang, Aya Alja'fari, Rajarshi Roy, Rohan Badlani, Jason Roche, Jason Li, Zhehuai Chen

**机构**：NVIDIA Corporation

**发布日期**：2026-08-17 | **论文**：https://arxiv.org/abs/2608.13831 | **PDF**：https://arxiv.org/pdf/2608.13831.pdf | **代码**：https://github.com/NVIDIA-NeMo/Speech | **Demo**：暂无

### 📌 简介
现有语音语言模型大多局限于轮次式交互，无法支持用户实时打断（barge-in）等全双工行为。近期端到端双工S2S模型虽降低了延迟，但因ASR、打断处理和高质量合成需联合优化，往往牺牲语音质量。本文提出VoiceChat-TTS，一种低延迟、连续、流式的TTS模型，可直接消费LLM文本token流，通过控制token支持显式打断，并在无文本输入时生成静音。模型在保持模块化和高语音质量的同时实现持续响应的语音生成。在LibriTTS test-clean上，VoiceChat-TTS单轮合成WER为2.00%、Squim-MOS达4.38，在FDB双工测试中打断遵从率（IOR@320ms）达96.8%，声学token帧间延迟仅为7.16ms。

### 🔧 技术方案

**问题背景：** 现有流式TTS系统（如Audio Flamingo 3-Chat、VoXtream、SpeakStream、Qwen3-TTS）主要解决单轮响应内的流式生成，但缺乏全双工交互所需的持续始终在线行为——解码器需在对话时间内保持活跃，无文本时生成静音，并在用户打断时迅速停止。端到端S2S模型虽能降低延迟，但架构复杂且语音质量下降。

**模型架构：** VoiceChat-TTS基于Audio Flamingo 3-Chat流式语音解码器构建，总参数量977M（778M Gemma 3流式TTS模块 + 199M编解码器）。核心组件包括：(1) 全因果卷积音频编解码器，22kHz波形压缩至12.5Hz帧率，31码本RVQ，每帧对应80ms语音；(2) NVIDIA Nemotron Nano 2子词分词器，新增BOS和打断token；(3) 字符感知子词编码器用于处理LLM子词OOV问题；(4) 混合高斯估计头（MoGH）加速深度RVQ解码；(5) 3秒参考音频提示条件化；(6) 边界嵌入与门控融合机制。

**核心创新：** (1) 字符感知子词编码器：将输入子词转换为字符序列，经浅层Transformer编码后平均池化，获得对未见子词具有泛化能力的字符感知嵌入，解决了LLM词表与TTS训练语料间子词分布不匹配问题。(2) 基于控制token的显式打断机制：引入BOS token标记助手的轮次开始，打断token标记应停止说话并过渡到静音的位置，支持在无需重置KV cache的情况下进行句中打断。(3) 统一训练策略：将标准单轮TTS数据（70,159小时）与合成多轮对话数据（2.5k小时，50%含打断模拟）和真实对话数据（Fisher语料库）联合训练，对50%单轮数据随机前置0.5-5秒静音以消除双工场景中的模态分布差异。

**训练策略：** 两阶段训练：第一阶段在8块NVIDIA A100 GPU上使用单轮TTS数据预训练140万步，第二阶段在32块NVIDIA H100 GPU上使用完整混合数据微调20万步。微调数据配比：40%单轮TTS、15%词和专有名词列表、10%真实对话、35%合成双工对话。优化器：AdamW，学习率4e-5。推理时使用top-p采样（p=0.95）、CFG尺度0.2、MoG噪声尺度0.001、8次MoGH迭代。

### 📊 实验结果
**数据集**：LibriTTS test-clean（未见说话人）、5个训练集内说话人（见说话人）、Full-Duplex-Bench Smooth Turn Taking和User Interruption子集

**主要指标**：
- 未见说话人单轮CER：1.00% | WER：2.00% | SECS：0.757 | Squim-MOS：4.380
- 未见说话人四轮CER：1.20% | WER：2.20% | SECS：0.685 | Squim-MOS：4.376
- 见说话人单轮CER：1.20% | WER：2.40% | SECS：0.785 | Squim-MOS：4.365
- 打断IOR@320ms：96.8%（无强制静音）/ 100.0%（强制静音）
- 停止延迟：228.3ms（无强制静音）/ 89.9ms（强制静音）
- 声学token ITL（并发1）：7.16ms | 编解码器：2.46ms | 总延迟：9.62ms（对比Qwen3-TTS-12Hz总延迟20.34ms）
- 与PersonaPlex对比：CER从4.06%降至2.05%，WER从5.00%降至2.42%，Squim-MOS从4.094提升至4.292

**是否开源**：是（代码开源在NVIDIA NeMo Speech，模型权重在Hugging Face nvidia/NVIDIA-NemotronLabs-VoiceChat-11B）

### ⭐ 评分：8/10
评分理由：VoiceChat-TTS在流式TTS的全双工交互能力上做出了实质性贡献，字符感知子词编码器和打断控制token的设计简洁有效。实验覆盖了单轮/多轮合成质量、打断延迟、流式延迟等多个维度，与Qwen3-TTS和PersonaPlex的对比具有说服力。模型已作为NVIDIA Nemotron VoiceChat-11B的双工语音解码器落地，实用价值高。扣分点在于缺乏用户音频条件化（无法动态适配韵律），未进行系统的消融实验量化各组件贡献，且未见说话人多轮场景的SECS衰减（从0.757降至0.685）仍需改进。

---

## [4] Trajectory Dynamics in Self-Supervised Learning Latent Space for Audio Deepfake Detection

**arXiv ID**：2608.13817 | **方向**：语音大模型 / 语音深度伪造检测

**作者**：Tomás Andrade Weber

**机构**：Barcelona Supercomputing Center (BSC), CASE Department

**发布日期**：2026-08-17 | **论文**：https://arxiv.org/abs/2608.13817 | **PDF**：https://arxiv.org/pdf/2608.13817.pdf | **代码**：https://doi.org/10.5281/zenodo.21879214 | **Demo**：暂无

### 📌 简介
现有语音深度伪造检测方法大多依赖SSL特征提取器加全局池化，丢弃了时序顺序信息，在跨语料库泛化时性能急剧下降。本文提出利用人类语音生理约束在SSL潜空间中产生的结构化轨迹动态进行检测：训练一个因果LSTM下一帧预测器（Stage 1），仅在ASVspoof 2019的真实语音上学习轨迹动态，以预测误差作为异常分数；可选Stage 2将冻结的LSTM隐状态均值池化后训练一个有监督MLP分类器。在ASVspoof 2019/2021、Codecfake、In-the-Wild、MLAAD-EN和Deepfake-Eval-2024六个基准上取得竞争性或最优结果，包括ASVspoof 2021上最佳已发布EER 0.75%。在跨语料库困难基准上，纯单类Stage 1超越了NII-GAP有监督基线（DE2024: 30.35% vs 52.52%），证明轨迹动态携带了超越语句级统计量的检测信号。

### 🔧 技术方案

**问题背景：** 现有SSL检测方法（如AntiDeepfake、SLIM、QAMO、BreathNet）大多对帧级嵌入做全局平均池化或注意力加权汇总，完全丢弃时序顺序。少量利用时序结构的工作（FGFM、TRACE、BreathNet）要么针对局部拼接伪影，要么需要伪造监督信号，均未建模整段语音的全局生理合理性轨迹。

**模型架构：** 采用两阶段级联架构。前端使用Wav2Vec2-Large-AntiDeepfake（固定，不做微调）提取1024维帧级嵌入，帧率50fps。Stage 1是一个2层因果LSTM轨迹预测器，隐层维度512，输入帧序列后因果预测下一帧，仅在ASVspoof 2019 LA训练集的2,580条真实语音上训练。异常分数为整段语音上预测帧与真实帧之间的MSE均值。Stage 2将冻结的Stage 1 LSTM所有帧的隐状态均值池化，得到512维语句级表示，训练一个三层MLP分类器（512->256->128->1，dropout 0.3），在ASVspoof 2019 LA全部25,380条语音上做有监督二分类。

**核心创新：** (1) 提出因果LSTM轨迹预测器作为单类异常检测方法：在SSL潜空间中对真实语音的时序轨迹进行建模，以预测误差衡量当前语音轨迹偏离真实生理约束的程度，无需任何伪造数据即可检测深度伪造。(2) 构建了与静态GAP基线严格受控的对比实验：使用完全相同的前端特征，仅通过是否保留时序顺序来隔离轨迹动态的贡献，证明在困难跨域基准上轨迹动态带来的增益（MLAAD-EN: 22.86%->5.71%，DE2024: 52.52%->30.35%）。(3) 揭示了一个重要的泛化反转现象：在域内基准上Stage 2有监督优于Stage 1，但在跨域困难基准上Stage 1单类方法反而优于Stage 2，说明ASVspoof 2019的伪造监督信号本身成为跨域泛化的瓶颈，单类真实语音建模具有更好的泛化鲁棒性。

**训练策略：** Stage 1 LSTM训练500轮，AdamW优化器，余弦退火与热重启（T0=50，T_mult=2），初始学习率1e-3，dropout 0.1，最大序列长度500帧。Stage 2 MLP训练100轮，dropout 0.3。训练前对所有语音做静音预处理：去除超过500ms的长静音，替换为200ms的自然停顿。所有实验在单张H100 GPU上完成。为估计方差，训练5个独立Stage 1模型（不同随机种子），每个Stage 1模型训练5个独立Stage 2 MLP，共25次运行。

### 📊 实验结果
**数据集**：ASVspoof 2019 LA eval、ASVspoof 2021 DF eval、Codecfake、In-the-Wild、MLAAD-EN (v9)、Deepfake-Eval-2024 (DE2024)

**主要指标**（EER%，越低越好）：
- ASVspoof 2019：Stage 1 = 2.57，Stage 2 = 1.11，Static = 1.51
- ASVspoof 2021：Stage 1 = 1.88，Stage 2 = 0.75（最佳已发表），Static = 0.98
- Codecfake：Stage 1 = 5.21，Stage 2 = 2.43，Static = 3.21
- In-the-Wild：Stage 1 = 4.84，Stage 2 = 3.28，Static = 4.03
- MLAAD-EN：Stage 1 = 5.71，Stage 2 = 10.02，Static = 22.86
- DE2024：Stage 1 = 30.35，Stage 2 = 35.41，Static = 52.52

**是否开源**：是（代码已开源Zenodo DOI: 10.5281/zenodo.21879214）

### ⭐ 评分：8/10
评分理由：本文从语音生理约束的独特视角出发，提出了一种优雅且简洁的轨迹动态建模方法，ASVspoof 2021上0.75% EER以及DE2024上单类超越有监督的结果具有说服力。实验设计严谨，通过静态基线及25次重复运行实现严格消融。缺点是创新点相对集中（LSTM预测器本身并非新颖架构），在ASVspoof 2019上未超越BreathNet（0.23% vs 1.11%），DE2024上30.35% EER在实际应用中仍有较大提升空间，且未探索Transformer等更先进的序列建模方案。

---

## [5] StreamHear: Domain-Adapted Pseudo-Labeling for Semi-Supervised Streaming Speech Recognition

**arXiv ID**：2608.13717 | **方向**：语音大模型 / ASR

**作者**：Zefang Liu, Chenyang Zhu, Sangwoo Cho, Xujun Peng, Shi-Xiong Zhang, Sambit Sahu

**机构**：Capital One, USA

**发布日期**：2026-08-17 | **论文**：https://arxiv.org/abs/2608.13717 | **PDF**：https://arxiv.org/pdf/2608.13717.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
流式ASR模型在域迁移场景下性能显著下降，而标注域内数据成本高昂，未标注数据却大量可得。本文提出StreamHear，一种半监督流水线方法：先在全量标注集上微调离线RNN-T教师模型，再用其生成未标注数据的伪标签，最后混合标注和伪标签数据微调流式学生模型。为修正训练数据中词级chunk边界对齐误差，引入基于先验正则化的动态规划重新对齐算法（Needleman-Wunsch），利用Whisper假设锚点重新分配单词到正确chunk。在Earnings-21、Earnings-22、SPGISpeech和BankCall四个数据集上，StreamHear相比有监督学生微调在测试集上WER降低0.18-0.88个百分点，在未标注集上降低0.44-1.85个百分点，最接近离线教师模型仅差0.11个百分点。

### 🔧 技术方案

**问题背景：** 预训练流式ASR模型（如cache-aware FastConformer-RNN-T）在域外数据（金融电话会议、带口音英语、窄带客服对话）上性能退化严重。域内微调需要chunk粒度的标注数据，成本高昂。现有半监督伪标签方法依赖迭代自训练、EMA教师动量更新或辅助LLM纠错等复杂机制，增加了训练开销和工程复杂度。针对cache-aware流式架构的简单高效域适应方案尚未被探索。

**模型架构：** 整体框架包含三个顺序阶段：(1) 教师微调——将离线全上下文RNN-T教师模型Parakeet-TDT-0.6B-v3在有标注训练集上微调，使其适应目标域分布；(2) 伪标签生成——微调后的教师以贪心解码转录未标注音频，可选按序列平均对数似然过滤Top-K%伪标签；(3) 学生微调——cache-aware流式学生模型Nemotron-Speech-Streaming-EN-0.6B（0.6B参数FastConformer-RNN-T，支持多延迟右上下文采样）在混合数据集上以标准RNN-T损失微调。关键数据准备步骤包括：VAD（pyannote-3.0）分割音频，CTC-Segmentation（Parakeet-CTC-0.6B）计算词级时间戳，然后通过DP重新对齐纠正残余误差。

**核心创新：** (1) 单次传递的伪标签流水线：使用固定、域适应的离线教师，仅需一次伪标签生成和一次学生微调，无需迭代、EMA教师或辅助神经模块，极大简化训练流程。(2) 先验正则化DP重新对齐算法：将真实文本和ASR假设展平为两个词流，每个词携带chunk索引标签，通过Needleman-Wunsch算法进行全局对齐，匹配得分中引入chunk索引位移的先验惩罚项，使匹配词继承假设词的chunk归属，未匹配词保留原chunk，再经两遍扫描保证单调顺序。在Earnings-21和Earnings-22上对齐质量WER分别降低9.45和9.57个百分点。(3) 首次在cache-aware流式ASR架构上验证伪标签域适应的有效性，并在四个差异显著的域（金融电话、准备演讲、电话质量对话）上系统评估。

**训练策略：** 损失函数为标准RNN-T损失。AdamW优化器，学习率2e-4，betas=[0.9,0.98]，权重衰减1e-3，余弦调度+10%预热，最小学习率1e-6。训练10轮，bf16精度，SpecAugment（2个频率掩码x10个时间掩码）。流式学生有效批大小64（4xA100-SXM-40GB，每GPU批大小4，梯度累积4），教师微调每GPU批大小2+梯度累积8。每个实验重复5个随机种子，报告均值和标准差。

### 📊 实验结果
**数据集**：Earnings-21（金融电话会议），Earnings-22（多口音全球英语电话会议），SPGISpeech（金融演讲，含解说和Q&A），BankCall（专有银行客服电话，双声道）

**主要指标**：
- Earnings-21测试WER：StreamHear 6.63% vs FT Student 7.19%（降0.56pp），未标注7.77% vs 9.62%（降1.85pp）
- Earnings-22测试WER：StreamHear 11.76% vs FT Student 12.46%（降0.70pp），未标注9.56% vs 10.81%（降1.25pp）
- SPGISpeech测试WER：StreamHear 2.59% vs FT Student 2.77%（降0.18pp），未标注2.26% vs 2.70%（降0.44pp）
- BankCall测试WER：StreamHear 9.80% vs FT Student 10.68%（降0.88pp）
- 消融实验：DP对齐提升9.45-9.57pp；置信度过滤中K越大越好（100%最优）

**是否开源**：否（使用NVIDIA NeMo框架，代码未单独开源）

### ⭐ 评分：8/10
评分理由：提出简洁高效的流式ASR半监督域适应流水线，创新性适中但实用价值高——单次传递无需迭代的设计大幅降低工程部署成本。DP重新对齐算法优雅地解决了chunk级对齐的工程痛点。实验覆盖四个数据集、五种消融，实验设计充分且结果一致。不足在于教师固定后未探索伪标签质量进一步提升的机制，且未与其他半监督方法（如EMA教师、迭代伪标签）进行公平对比。整体而言，方法论清晰实用，对工业界流式ASR域适应有较强的参考价值。

---

## [6] Omni-LiveAvatar: Minute-Level Real-Time Streaming Joint Audio-Visual Avatar Generation

**arXiv ID**：2608.13602 | **方向**：语音大模型 / 音视频生成

**作者**：Lunjie Zhu, Xingtong Ge, Fangyu Lin, Yi Zhang, Zhening Liu, Mengfei Li, Yumeng Zhang, Guanglu Song, Yu Liu, Jun Zhang

**机构**：上海交通大学与商汤科技联合

**发布日期**：2026-08-17 | **论文**：https://arxiv.org/abs/2608.13602 | **PDF**：https://arxiv.org/pdf/2608.13602.pdf | **代码**：https://github.com/Aoko955/Omni-LiveAvatar | **Demo**：暂无

### 📌 简介
现有联合音视频生成模型依赖双向注意力与多步去噪，推理延迟高且仅能生成短视频，无法用于实时长时交互。本文提出Omni-LiveAvatar，首个支持分钟级实时流式联合音视频数字人生成的框架。核心贡献包括：(1) 渐进式自回归蒸馏，将19B参数的双向联合音视频扩散模型LTX-2转化为4步因果生成器，无需辅助稳定机制，在单卡H200上实现33倍加速（21.99 FPS）；(2) 同步音视频长短时记忆机制，结合周期性重锚定长程记忆与滚动KV缓存，在有界记忆预算下维持全局一致性；(3) 层次化滚动提示规划，将文本提示分解为固定全局提示与逐块局部提示，实现语义平滑过渡。实验表明，在5秒和60秒生成任务中，Omni-LiveAvatar在视频质量、人类身份保持、音质和音画同步上全面超越OmniForcing和Hallo-Live等实时基线。

### 🔧 技术方案

**问题背景：** 现有联合音视频生成模型（如LTX-2、Ovi）依赖双向注意力与多步去噪，推理速度慢且仅能生成短片段。近期工作如OmniForcing和Hallo-Live尝试通过自回归蒸馏实现实时生成，但依赖音频sink token、额外未来音频上下文或外部奖励模型等模态特定补偿手段，而非从本质上解决蒸馏框架的不稳定性。此外，现有方法局限于短片段生成，分钟级流式数字人生成尚未被探索，主要面临三大挑战：大尺度多模态模型蒸馏困难，音频建模与跨模态耦合增加蒸馏难度；跨模态漂移，视觉与音频漂移随时间累积并相互放大；异构语义调度，需协调缓慢变化的视觉上下文与快速变化的语音内容。

**模型架构：** Omni-LiveAvatar基于19B参数的LTX-2联合音视频扩散模型构建。整体框架包含三个核心模块：(1) 渐进式自回归蒸馏管道，分为三阶段——Stage I用联合音视频DMD损失将双向教师蒸馏为双向少步生成器；Stage II将双向少步生成器通过块因果注意力掩码转换为因果少步生成器，并用双向少步生成器生成的ODE轨迹回归训练以避免轨迹不匹配；Stage III引入联合滚动窗口（M=4个噪声水平递增的宏块），窗口内允许双向交互抑制单向误差传播。(2) 同步音视频长短时记忆，保留首个宏块的KV状态作为长程记忆，对所有后续块持久可见，每5秒用RoPE重锚定缩小位置偏移；同时维护最近L个宏块的滚动KV缓存作为短程记忆。(3) 层次化滚动提示规划，将全提示分解为固定全局提示（身份、场景、整体运动）和逐块局部提示（语音内容），滚动窗口前进时局部提示平滑移入移出。

**核心创新：** (1) 渐进式自回归蒸馏管道，不同于OmniForcing先DMD再因果ODE回归（导致轨迹不匹配），本文提出分三阶段渐进式方案：先双向蒸馏获得少步生成器，再用其自身生成轨迹配对进行因果初始化（轨迹对齐），最后引入联合滚动窗口进行双向交互训练。该方案无需辅助稳定机制即可实现稳定因果化。(2) 同步音视频长短时记忆机制，首次在联合音视频流式生成中引入同步长程记忆，保留首个宏块KV状态提供稳定的身份、场景、音色参考，并通过周期性RoPE重锚定（每5秒）解决位置偏移导致的记忆衰减问题。(3) 层次化滚动提示规划，针对联合滚动强制推理范式下提示切换导致语义冲突的问题，提出将提示分解为全局+局部层次，局部提示随滚动窗口平滑过渡，协调慢变视觉语义与快变语音内容的不同粒度需求。

**训练策略：** 训练分三阶段：Stage I用联合音视频DMD损失（lambda_v=lambda_a=1.0，视频CFG scale=3，音频CFG scale=5），训练4,000步，lr=2x10^-5；Stage II用ODE回归损失，训练3,000步，lr=1x10^-4；Stage III用联合DMD损失（滚动窗口M=4），训练3,000步，lr=2x10^-5。优化器为AdamW，全局batch size=8，bf16精度，在8张NVIDIA H200 GPU上训练。使用内部35K文本提示数据集，推理时4步去噪，分辨率512x768。

### 📊 实验结果
**数据集**：内部35K文本提示数据集（未公开）

**主要指标（5秒生成，实时自回归模型对比）**：
- 速度：19.57 FPS（OmniForcing 16.11，Hallo-Live 16.50）
- 视频质量：QS 81.72（OmniForcing 80.05，Hallo-Live 74.21）
- 人类身份保持：HI 100.00（OmniForcing 98.51，Hallo-Live 97.42）
- 音质：UTMOS 3.19 / DNSMOS 3.95 / NISQA 3.06
- 音画同步：Sync-C 6.16（OmniForcing 1.60，Hallo-Live 4.50）

**主要指标（60秒分钟级生成）**：
- 速度：21.99 FPS（OmniForcing 16.18，Hallo-Live 13.80）
- 人类身份保持：HI 98.61（OmniForcing 50.19，Hallo-Live 67.60）
- 音画同步：Sync-C 6.76（OmniForcing 0.28，Hallo-Live 0.72）
- 文本-视频对齐：VA 9.82（OmniForcing 6.68，Hallo-Live 5.46）

**是否开源**：是（https://github.com/Aoko955/Omni-LiveAvatar）

### ⭐ 评分：8/10
评分理由：该工作是首个实现分钟级实时流式联合音视频数字人生成的系统，在工程创新上突出——渐进式蒸馏管道从根本上解决了现有方法依赖辅助稳定机制的问题，长短时记忆和层次化提示规划的设计精巧且有效。实验设计全面，覆盖5秒和60秒两个尺度，包含6个维度10+项指标，消融实验充分验证各组件必要性。扣分原因：仅在内部35K数据集上训练，缺乏公开基准上的公平对比；训练数据规模和来源未披露，结果可复现性存疑。

---

## [7] Measuring Fairness in Large Audio Language Models via Semantic-Aware Bias Estimation

**arXiv ID**：2608.13624 | **方向**：语音大模型 / 音频语言模型公平性

**作者**：Zhe Liu

**机构**：Meta Platforms, Inc., Menlo Park, USA

**发布日期**：2026-08-17 | **论文**：https://arxiv.org/abs/2608.13624 | **PDF**：https://arxiv.org/pdf/2608.13624.pdf | **代码**：暂无 | **Demo**：暂无

### 📌 简介
大音频语言模型（LALM）在语音识别和音频问答等任务中广泛应用，但其跨人口子组的公平性评估面临语义混杂和说话人特性相关的混淆因素挑战。现有方法未考虑不同子组间语音内容的语义难度差异，导致虚假公平性结论。本文提出一种语义感知混合效应回归框架，将参考文本的句子级语义嵌入作为协变量，说话人身份作为随机效应，从而在公平性评估中显式控制语义和说话人混杂。在模拟实验中，传统方法将性别间分数比错误估计为1.124（置信区间不含1），而本文方法将比值校正至1.000-1.003（置信区间含1），消除虚假阳性。在LibriSpeech真实数据上，原始WER比显示性别间显著差异（Test-Clean比值为0.719），语义感知模型将比值校正至1.017-1.020范围内且不再显著。

### 🔧 技术方案

**问题背景：** LALM在语音输入场景下，不同人口子组（如性别）的语音内容在语义复杂度上可能存在系统性差异。例如，某一性别群体的语音可能包含更多语义密集或难度更高的内容。此外，同一说话人的多个话语之间存在相关性。如果这些因素在公平性评估中不加控制，会导致模型偏差被高估或误判。现有方法（如Liu et al., ICASSP 2022）针对传统ASR系统提出了基于混合效应的统计框架，但依赖外部语义表示（如fastText、BERT），且未覆盖LALM场景。本文首次针对LALM场景提出语义感知公平性评估框架。

**模型架构：** 本文提出语义感知混合效应回归框架，由两个关键组件构成：(1) 统计回归模型：采用Poisson回归建模插入错误，Binomial回归建模删除+替换错误，以参考词数为偏移量。模型包含固定效应（目标因子如性别对错误率的影响）、语义协变量（控制语义变化）、以及说话人级随机效应（捕获说话人特异性）。(2) 语义嵌入提取方法：提出两种从LALM自身提取参考文本语义嵌入的策略——Embed-AGG：将参考文本送入LALM，取第一层、中间层和最后一层Transformer隐藏状态在各token上平均后再取三层平均；Embed-EOWL：使用显式单词限制提示模板，取LALM下一token预测的logits作为紧凑语义表示。当嵌入维度较高时，通过PCA降至8维以保证回归稳定性。

**核心创新：** (1) 提出语义感知混合效应回归框架，首次在LALM公平性评估中同时控制语义变化（通过句子嵌入协变量）和说话人依赖性（通过随机效应），相比传统方法显著减少虚假公平性发现。(2) 创新性地利用被评估的LALM自身提取参考文本的语义嵌入（Embed-AGG和Embed-EOWL两种方法），而非依赖外部语义模型。这种设计确保嵌入与模型内部对输入语义的感知一致，比使用fastText/BERT等外部表示更精确地捕获模型自身的语义判断。(3) 框架具有模型无关和属性无关的通用性，不仅适用于ASR任务的WER分析，还可扩展至音频问答等更广泛的音频理解任务。

**训练策略：** 本文不涉及模型训练，而是提出评估框架。在回归模型拟合中使用最大似然估计，通过自适应Gauss-Hermite求积近似随机效应积分。语义嵌入提取时使用Qwen2-Audio作为被评估LALM，PCA降维至8维。模拟实验中使用Llama-3 70B生成2000个文本问题（半简单半困难），通过TTS合成音频，其中女性800个困难+200个简单、男性200个困难+800个简单，人为制造语义难度与性别的混淆。真实数据实验使用LibriSpeech（Test-Clean 2620句/40说话人，Test-Other 2939句/33说话人）和AIR-Bench-Chat。

### 📊 实验结果
**数据集**：LibriSpeech（Test-Clean和Test-Other）、AIR-Bench-Chat、模拟数据集（2000个TTS合成问题）

**主要指标**：
- 模拟数据（性别分数比）：Vanilla估计1.124（假阳性）-> 语义感知Embed-AGG 1.003（正确阴性）
- LibriSpeech Test-Clean（WER性别比）：Vanilla 0.719（显著）-> 语义感知Embed-AGG 0.802（不显著）
- LibriSpeech Test-Other（WER性别比）：Vanilla 1.162（显著）-> 语义感知Embed-AGG 1.020（不显著）
- AIR-Bench-Chat（分数性别比）：Vanilla 0.969（不显著）-> 语义感知Embed-AGG 1.004（不显著）

**是否开源**：暂无

### ⭐ 评分：7/10
评分理由：问题定义清晰且具有实际意义，统计建模方法严谨，混合效应回归结合语义嵌入的设计合理且有效。模拟实验和真实数据实验设计完整，充分验证了语义混杂导致虚假公平性结论的问题。不足在于仅评估了Qwen2-Audio单一模型和性别单一属性，缺乏跨模型和跨属性的泛化验证；且Embed-EOWL方法需要额外prompt工程，实用性和可复现性有待加强。整体而言，为LALM公平性评估提供了有价值的统计方法论框架。

---

## 语音前端

---

## [8] Singer-Informed Vocal Source Separation for Multi-Singer Music Mixtures

**arXiv ID**：2608.14516 | **方向**：语音前端 / 语音分离

**作者**：Jocelyn Xu, Minje Kim

**机构**：University of Illinois Urbana-Champaign / Sony AI

**发布日期**：2026-08-17 | **论文**：https://arxiv.org/abs/2608.14516 | **PDF**：https://arxiv.org/pdf/2608.14516.pdf | **代码**：https://github.com/jocelynxu01/singer-separation-paper | **Demo**：暂无

### 📌 简介
现有音乐源分离系统通常提取单一歌声轨道，无法区分多歌手混合中的不同歌手。本文提出一种歌手感知的歌声源分离框架，利用目标歌手的短时长注册录音提取歌手嵌入向量，通过特征拼接或特征线性调制（FiLM）条件化分离模型，使其聚焦目标歌手并抑制干扰。基于DAMP-VSEP数据集构建了含质量过滤和非重叠注册段的二重唱数据集。实验表明：在二重唱场景下，基线方法的target-singer SI-SDR仅为0.33 dB，而所提方法最高提升至5.58 dB；Fréchet Audio Distance（FAD）进一步验证了感知质量的改善，残差FAD最低降至0.06。代码和模型已开源，被IWAENC 2026接收。

### 🔧 技术方案

**问题背景：** 传统音乐源分离系统（如Open-Unmix、Demucs、Spleeter）将混合信号中的所有人声视为单一源，提取的是"所有歌声之和"而非特定歌手。在多歌手场景（如二重唱）中，歌声在时频域高度重叠，传统模型无法区分不同歌手。语音领域的说话人提取（如SpeakerBeam、VoiceFilter、SpEx+）已证明注册音频引导分离的有效性，但将其迁移到歌声面临两大挑战：一是缺乏含干净人声和多歌手混合的标注数据集；二是歌声在音高、音色和表达方式上的变化远大于语音，使条件化过程更加困难。

**模型架构：** 整体框架由两个模块组成：(1) 歌手嵌入模型——基于GRU的歌声表征网络，输入为注册音频的幅度谱图，输出固定维度的歌手嵌入向量；(2) 分离模型——基于Open-Unmix架构，操作于幅度谱图并预测频谱掩码，结合混合信号相位重建波形。Open-Unmix采用全连接层+双向LSTM+全连接层的编解码器结构，输入为混合信号的STFT幅度谱特征。在二重唱场景中，歌手嵌入通过拼接或FiLM方式注入分离网络。

**核心创新：** (1) 提出首个面向多歌手混合的歌手条件化歌声分离框架，通过短注册音频（>3秒）提取目标歌手身份嵌入，将传统"通用歌声分离"转变为"目标歌手提取"，实验证明在二重唱场景下target-singer SI-SDR从0.33 dB跃升至5.58 dB。(2) 系统对比了两种条件化策略——特征拼接和特征线性调制（FiLM），发现拼接在残差重建指标上更优（残差SI-SDR达7.98 dB），而FiLM在目标歌手提取上更一致（vocal SI-SDR 3.39 dB高于拼接的2.92 dB）。双损失函数（L_v+r = L_v + lambda*L_r）进一步平衡了声乐提取与残差抑制，lambda=0.1时取得最佳综合效果。(3) 基于DAMP-VSEP构建了完整的二重唱数据集构建流程，包括DNSMOS非侵入式质量过滤（阈值3.0）、基于能量的VAD注册段提取（能量阈值0.001，段长>3秒）、以及合成二重唱生成（每锚点歌手配对10个不同歌手，人声-20 dB、伴奏-26 dB），最终产生55,780个二重唱训练样本和559首真实二重唱测试集。

**训练策略：** 分离模型以SI-SDR为损失函数，Adam优化器，学习率1e-3，权重衰减1e-5，训练6秒片段，应用学习率衰减和早停。双损失策略在vocal loss基础上叠加residual loss，lambda取{0.05, 0.1, 0.2}。歌手嵌入模型为2层GRU（隐藏层32维），采用二分类交叉熵损失进行对比学习。数据集按8:1:1划分，二重唱测试集仅使用原始录音（559首）以反映真实场景。

### 📊 实验结果
**数据集**：DAMP-VSEP（经DNSMOS过滤后保留14,381首独唱和6,389首二重唱，合成扩展至55,780个二重唱训练样本）

**主要指标（二重唱测试集）**：
- SI-SDR（目标vocal）：Baseline 0.33 dB -> Concat + L_v+r (lambda=0.1) 5.58 dB
- SI-SDR（残差）：Baseline 1.47 dB -> Concat + L_v+r (lambda=0.1) 7.98 dB
- FAD（目标vocal）：Baseline 2.28 -> Concat + L_v 0.37
- FAD（残差）：Baseline 2.44 -> Concat + L_v+r (lambda=0.1) 0.06
- 独唱场景SI-SDR：Baseline 17.80 dB优于条件化模型（预期结果）

**是否开源**：是（代码和模型权重已开源）

### ⭐ 评分：7/10
评分理由：该文首次将说话人提取思路系统性地引入多歌手歌声分离场景，问题定义清晰且具有实际应用价值。实验对比了两种条件化策略和多种损失配置，在二重唱场景下取得了显著提升（target SI-SDR +5.25 dB，残差FAD降至0.06）。然而，创新点本质上是对现有技术的组合应用（Open-Unmix + GRU embedding + FiLM），缺乏架构层面的突破性设计；实验局限于最多2位歌手，且未考虑注册音频含噪或音高变化等更实际的挑战。总体而言，这是一篇有工程价值的探索性工作，但理论深度和实验完备性尚有提升空间。

---

*Generated on 2026-08-17*