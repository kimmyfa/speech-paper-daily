# OTHER RELATED（按评分降序）

共 131 篇

## [3 VoxPrivacy: A Benchmark for Evaluating Interactional Privacy of Speech Language Models](https://arxiv.org/abs/2601.19956)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-01-27
- **一句话贡献**：SLM正从个人设备走向共享智能家居等多人环境，却缺乏区分说话人并管理信息流的"交互式隐私"能力。本文提出首个交互式隐私评测基准VoxPrivacy：7107条32.86小时中英双语数据、三层递进任务（遵守保密指令→以声音为钥匙的条件放行→主动推断敏感信息）。评测9个SLM发现开源模型在条件隐私任务上接近随机（约50%），微调Kimi-Audio后Tier2英文F1升至82.65（Gemini-2.
- **关键技术点**：** 现有SLM基准只测"说了什么"不测"谁在说"；隐私基准只针对密码等全局敏感信息，忽略"本不敏感但在特定语境下变敏感"的信息。作者将交互式隐私定义为共享环境中阻止A用户信息泄露给B用户，并论证逐轮声纹验证或硬性历史隔离均不可行。
- **主要指标**：
- **代码**：官方发布 | **Demo**：https://interactionalprivacy.github.io/

---
## [2 ParaBridge: Bridging Paralinguistic Perception and Dialogue Behavior in Speech Language Models](https://arxiv.org/abs/2606.10581)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-06-09
- **一句话贡献**：针对SLM"能感知副语言线索却不据此调整开放对话行为"的感知-行为鸿沟（如Qwen3-Omni在VoxSafeBench儿童语音任务SAR仅6.1%），本文提出ParaBridge，基于on-policy自蒸馏的后训练方法：同一模型在scaffold加持下充当稠密逐token教师，向无scaffold学生分布蒸馏。仅1000条数据即可使无scaffold SAR从14.64%升至40.33%（超过
- **关键技术点**：** 现有SLM在MMSU副语言感知任务上可达52.8%，说明模型已具备线索识别能力，但普通请求中几乎不据此调整回复。推理时前置副语言提示scaffold可显著激发潜在能力（SAR 14.6%→29.0%），但此类scaffold在多轮长上下文、指令竞争下易失效；SFT需人工标注且有偏移风险，RFT只保留单条被选轨迹存在暴露偏差，GRPO仅提供稀疏标量奖励。
- **主要指标**：
- **代码**：暂无（承诺随上游许可发布LoRA适配器） | **Demo**：暂无

---
## [3 Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments with Turn Action GRPO](https://arxiv.org/abs/2607.27756)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-07-30
- **一句话贡献**：现实社交环境中语音助手需在多人对话和背景噪音中决定是否响应、继续倾听还是忽略。本文提出Cocktail-Talker，基于Qwen2.5-Omni-7B的语音LLM框架，通过三种行动token（respond/listen/ignore）建模助手的对话行为。使用Cocktail-DialogGen数据管道模拟14,400个独特对话、72,000个带噪音频混合物（约1,280小时），涵盖18种see
- **关键技术点**：** 现有语音对话系统假设干净的双人交互环境，用户话语直接面向助手。但真实社交场景中多人同时说话、背景噪音存在，每个话语可能面向助手、其他说话人或完全无关。助手需要决定是否回应、继续倾听还是忽略。这是一个多说话人-单助手的口语对话建模问题，目前缺乏系统性解决方案。
- **主要指标**：
- **代码**：https://github.com/xi-j/Cocktail-Talker | **Demo**：暂无

---
## [1 JoyAI-Talker: Full-Duplex Speech Interactive Large Model for Empathetic Voice Agents](https://arxiv.org/abs/2608.01119)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：京东提出JoyAI-Talker，一个全双工语音对话系统，采用模块化Thinker-Talker架构将认知规划、对话状态协调和语音生成解耦。通过统一的语音-文本联合训练流程缓解"认知退化"问题，在MATH基准上达到94.62%的推理准确率，同时在全双工交互中实现0.88的响应率和极低误触发率。PAER框架从音频中提取说话人属性（性别、年龄、情绪）并结合CoT推理生成共情响应。
- **关键技术点**：** 现有语音对话系统将语音交互作为独立模块附加在LLM后，导致模型在扩展到语音模态时出现"认知退化"——核心文本推理、STEM和逻辑能力显著下降。全双工交互中的打断、插话等复杂对话管理尚未得到系统解决。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 Hidden-Domain Routing for All-Type Audio Deepfake Detection](https://arxiv.org/abs/2608.00493)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：语音深度伪造检测（SDD）系统在传统基准上表现良好，但现有方法难以处理所有类型的音频deepfake（语音、环境声音、歌唱、音乐）。OPPO提出隐藏域路由方案，首先用AudioType-BEATs-6s路由器从6秒窗口估计音频类型，然后路由到对应的分支检测器：Speech-XLSR（语音）、SoundMusic-EAT（声音/音乐）、Singing-EAT（歌唱）。在AT-ADD Challeng
- **关键技术点**：** 全类型音频deepfake检测需要在推理时音频类型未知的条件下，对语音、环境声音、歌唱、音乐四种类型的音频做出真假判断。不同类型音频的特征分布差异巨大，单一检测器难以同时处理。在AT-ADD Challenge Track2中，隐藏域设置（hidden-domain condition）要求系统在无类型标签的条件下进行检测。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [10 Anomalous Sound Detection Meets Noise-Aware Self-Supervised Learning](https://arxiv.org/abs/2608.00447)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：异常声音检测（ASD）在工业设备监控中至关重要，但实际工厂环境中的背景噪声严重干扰检测性能。本文提出噪声感知自监督学习（NA-SSL），利用双麦克风录音设置（近场麦克风靠近目标机器，远场麦克风捕捉噪声），训练NA-SSL模型从含噪信号中提取干净表示。使用FSD50K（目标声音）+ WHAM!/DEMAND/QUT-NOISE（噪声）模拟双通道录音。在DCASE 2026 Challenge Tas
- **关键技术点**：** 工业ASD需要在工厂环境中检测机器异常声音，但严重背景噪声导致标准ASD方法性能大幅下降。DCASE 2026 Challenge Task 2首次引入噪声感知ASD（NA-ASD）任务，提供双麦克风录音：近场（靠近机器，目标信号主导）和远场（远离机器，噪声主导）。挑战在于如何利用远场噪声信息辅助近场信号的干净表示学习。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [13 SoniSpeech: Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces](https://arxiv.org/abs/2608.00803)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-04
- **一句话贡献**：无声语音接口（SSI）允许用户在不发出声音的情况下与设备交互，但受限于小词汇量数据集。本文提出SoniSpeech，首个大规模开放词汇可穿戴无声语音接口三模态数据集，包含34小时、18000个话语，三个同步模态：超声回波profile（通过声学传感眼镜捕获面部运动）、有声音频和前视视频。语料来自SODA对话数据集，包含5356个唯一词汇和完整音素覆盖。CTC ResNet-34基线在纯无声模式下W
- **关键技术点**：** 无声语音接口允许用户在安静环境下（如图书馆、会议室）或隐私敏感场景下与设备交互。现有研究受限于小词汇量（通常<100词）和封闭词汇集，缺乏大规模开放词汇的基准数据集。可穿戴硬件如面部电极（EMG）虽然精度高但佩戴不便。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks](https://arxiv.org/abs/2608.05507)

- **方向**：语音深度伪造检测 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-06
- **一句话贡献**：现有语音深度伪造检测（SDD）系统在ASVspoof等传统基准上表现强劲，但情感表达和LALM攻击的覆盖极为有限。AffectDF是目前最全面的情感语音深度伪造基准，包含约260小时语音，21种欺骗攻击（TTS/VC/EVC/LALM-EVC四种范式），覆盖5种情感状态（中性/高兴/愤怒/悲伤/惊讶），同时包含表演性和自发性情感语音。评测发现：ASVspoof2019训练的模型在AffectDF上
- **关键技术点**：** 现有ASVspoof基准主要关注中性语音，情感欺骗数据集（EmoFake 7种VC攻击，EmoSpoof-TTS 3种TTS攻击）规模小、攻击多样性不足且缺乏LALM攻击。情感语音在基频、能量、语速、shimmer等方面引入巨大变异性，可能掩盖或改变SDD系统依赖的伪造痕迹。 **数据集构建：** 基于ESD（表演性情感语音，4个说话人）和MSP-Podcast（自发性情感语音，4个说话人）两个语料库。21种攻击：LALM-EVC（Qwen2.5-Omni, Kimi-Audio, MiniCPM-o 4.5，含steered版本）、TTS（CosyVoice/2/3, Qwen3-TT
- **主要指标**：
- **代码**：https://affectdf33-data.github.io/AffectDF-Data/ | **Demo**：暂无

---
## [1 SemBridge: Semantic Token Anchoring for Continuous-Latent Autoregressive Speech Generation](https://arxiv.org/abs/2608.07462)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-07
- **一句话贡献**：连续潜向量自回归语音生成避免了离散 token 的量化损失，但连续声学目标不提供显式 token 级语言结构，导致 LM 需间接学习语言结构，损害内容保真度。SemBridge 提出训练阶段语义 token 锚定框架，使用离散语义 token（GLM-4-Voice, 12.5Hz, 16384 词表）直接监督 AR LM 状态，并引入语义对齐声学 VAE（SA-VAE）组织连续目标空间。语义监督
- **关键技术点**：** 连续 AR 语音生成中，LM 需从声学预测中推断语言结构，缺乏显式 token 级语义目标。现有方法使用连续语义特征对齐（如 SemaVoice、MELA-TTS），但离散语义 token 提供更明确的分类目标且能抑制与语言无关的声学变化。
- **主要指标**：
- **代码**：https://github.com/ASLP-lab/SemBridge | **Demo**：https://tiamojames.github.io/SemBridge_demo/

---
## [1 Listen, Reason, and Segment: Aligning LALMs with Editorial Judgment for Media Chapterization](https://arxiv.org/abs/2608.16539)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-18
- **一句话贡献**：音频章节化（把连续音频流切分为主题连贯章节）依赖主观编辑判断而非客观声学事件，现有 ASR+LLM 流水线仅适用于纯语音场景，且无纯音频端到端方案与评测基准。本文提出 AudioChaps 后训练框架，以 Audio-Flamingo-3-Think-8B 为骨干，通过 CoT-SFT 冷启动加 GRPO 校准将模型边界决策对齐 YouTube 创作者标注。在 AudioChaps-Eval 上平
- **关键技术点**：** LALM 在标准 benchmark 上进步很快，却难以落地媒体工作流。章节边界本质是创作者主观编辑判断，而非可客观检测的声学事件；现有研究仅限视频域（VidChapters-7M）或转写级联（Whisper-Large-V3+Qwen3-235B 测试仅 48.0 F1），在音乐、游戏、动态媒体上显著退化，且缺乏有监督的推理数据。
- **主要指标**：
- **代码**：https://github.com/ta012/AudioChaps（录用后开源） | **Demo**：暂无

---
## [3 INSPIRE: A Benchmark for Instruction-Aware Speech Retrieval](https://arxiv.org/abs/2608.16203)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-18
- **一句话贡献**：语音检索现有系统依赖固定相似度匹配，无法适应多样用户意图。台大李宏毅组提出首个指令感知语音检索基准 INSPIRE，让自然语言指令动态指定语义内容、说话人身份、说话风格、环境声及多属性组合的匹配准则，并统一评测四种检索范式。结果发现无现有方法能稳健覆盖全部意图：级联流程在语义检索上最优（DailyTalk R@10=62.0），自监督语音模型更擅超音段属性（VCTK R@10=17.5），多属性综
- **关键技术点**：** 传统语音检索以固定声学/语义相似度或级联 ASR 检索定义相关性，一条查询只能对应一个目标；而真实场景中同一段语音在不同指令下应检索不同文档，现有方法无法按指令动态调节内容、说话人、风格、环境声等异构线索的权重，指令感知检索在文本/图像领域已有积累但在语音域尚属空白。
- **主要指标**：
- **代码**：https://github.com/lca0503/INSPIRE | **Demo**：暂无

---
## [13 Prototype-Rectified Iterative Self-supervised Manifold Denoising under Severe Acoustic Shift](https://arxiv.org/abs/2608.15037)

- **方向**：语音前端 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-18
- **一句话贡献**：音频-文本基础模型（ATM，如 CLAP）在严重声学噪声下性能骤降，现有 TTA 方法或依赖梯度而放大噪声，或需特权噪声标注。论文提出 PRISM（原型修正迭代自监督流形去噪），一个训练无关、源无关、噪声提示无关的 transductive TTA 框架：基于 Affine Noise Hypothesis 将严重噪声视为潜空间低秩仿射变形，以冻结文本原型为几何锚，用 OPCA、CCVD、逐类平移
- **关键技术点**：** 三类现有方法均不匹配恶劣声学环境：静态几何对齐（协方差白化、线性探测）将噪声视为刚性整体平移，无法应对每个环境独特的旋转/平移/低秩变形；梯度 TTA（TENT 等）在 <0dB 多音噪声下产生确认偏差，把高置信伪标签反馈回循环等于在噪声底上训练；提示优化（TPT、ContextDA）需推理时不可得的噪声类型特权标注且迭代反传与实时流不兼容。
- **主要指标**：
- **代码**：https://github.com/Ashish-1108/PRISM | **Demo**：暂无

---
## [1 SpeechSense: A Paralinguistic-Focused Dataset for Fine-Grained Speech Sentiment Analysis](https://arxiv.org/abs/2608.17931)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-19
- **一句话贡献**：现有语音情感分析存在两大局限：文本中心pipeline经ASR转写后丢弃韵律、语调等副语言线索，且标签粒度停留于基本情绪类别，难以刻画社交场景所需的人际立场。本文提出SpeechSense数据集，定义8类可主要由韵律线索识别的人际立场标签体系，通过语义-韵律解耦文本设计+角色扮演TTS合成+人工双阶段验证构造高质量数据。实验显示，具备声学访问的多模态LLM（Qwen2.5-Omni-7B 宏F1达
- **关键技术点**：** 现有方法的局限有二。其一，文本中心pipeline将语音经ASR转成文本后再做文本情感分析，不可避免丢弃韵律、语调、停顿、重音、语速等副语言线索，且ASR转写错误会传播恶化下游情感性能，例如"We can't wait another decade"全靠声学表达区分"热情支持"与"不耐烦"。其二，标签粒度失配：IEMOCAP、RAVDESS、CREMA-D等主流数据集仅标注happy/sad等基本情绪；Ekman和Plutchik的离散情绪框架面向内部情感状态而非面向交谈对象的人际立场，口语场景尚无标准化标注体系。
- **主要指标**：
- **代码**：https://github.com/Sher13cked/SpeechSense | **Demo**：暂无

---
## [1 Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learners](https://arxiv.org/abs/2608.19863)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-20
- **一句话贡献**：本文提出 NAPE（Next-Audio-Patch-Embedding prediction），将大语言模型中"预测下一个元素"的自回归范式引入自监督音频表示学习：把一个因果 Transformer 训练为，仅凭之前谱图模块的嵌入去预测下一个 patch 的连续嵌入。设计刻意极简，只用因果掩码加 stop-gradient 作为全部训练信号，彻底摆脱了重建解码器、声学 tokenizer、tea
- **关键技术点**：
- **主要指标**：
- **代码**：https://github.com/umbertocappellazzo/nape | **Demo**：暂无

---
## [5 Explainability by Design: Structured Kolmogorov-Arnold Networks over Probabilistic Attributes for Speech Deepfake Source Tracing](https://arxiv.org/abs/2608.20213)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：9/10 | **日期**：2026-08-20
- **一句话贡献**：现代语音合成技术可生成高度逼真的伪造语音，因此深度伪造语音溯源（识别伪造语句背后的具体生成器）对取证、内容溯源与平台问责日益重要。本文在作者此前"透明概率属性"工作（将语句表示为合成器子组件的概率分布）的基础上做了两项关键扩展：一是用多任务学习（MTL）联合训练概率属性提取器，二是引入结构化 Kolmogorov-Arnold 网络（SKM）作攻击分类器。SKM 的拓扑显式遵循 ASVspoof 
- **关键技术点**：
- **主要指标**：
- **代码**：https://github.com/HoangHPham/KAN-Probabilistic-Deepfake-Attribution | **Demo**：暂无

---
## [1 Do SpeechLMs Hear Their Own Opinions? Diagnosing and Mitigating Previous-Belief Contamination in Streaming Emotion Understanding](https://arxiv.org/abs/2608.20769)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：9/10 | **日期**：2026-08-24
- **一句话贡献**：流式语音情感理解普遍将模型上一时刻的预测作为历史上下文注入当前推理，本文通过反事实干预证明这种"历史信念"会污染当前音频的感知：固定音频、仅更换注入的上一个情感标签，CREMA-D-Stream 上准确率从 72.50% 跌至 30.42%，65.69% 的预测发生翻转，且效应强标签不对称（先验拉动率 4.76%~98.20%），作者称之为前人信念污染（PBC）。为此提出 EmoUpdate，一个
- **关键技术点**：** 现有流式情感系统将上一次预测当作历史文本直接写入感知提示，模型会"听见自己的观点"：错误状态递归回注并随时间放大，不同于普通识别误差或外部上下文偏见。单一粘性参数或提示词无法修复——10 个地面提示中 7 个明确要求忽略上一标签，错误先验拉动率仍不低于 59.7%，且随先验盲准确率上升而上升（Pearson r=0.81）。历史并非只是"权重大小"问题，而是参与了当前观测本身的形式化。
- **主要指标**：
- **代码**：暂无（论文声明将发布完整复现工件与SHA-256审计日志，正文未附公开仓库链接） | **Demo**：暂无

---
## [1 Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue](https://arxiv.org/abs/2609.04250)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-08-28
- **一句话贡献**：口语对话模型（SDM）只能产出语音而不能产出伴随动作，语音驱动动作模型则无法规划对话应答，常规级联方案需在音频完成后再做一次完整动作推理，且动作目标无法反向更新语音与对话参数。本文提出 Motion-Omni，首个原生端到端输出面部表情与手、上体、下体全身动作的口语对话框架，动作直接从产出语音的 Speech Generator 隐状态生成。以 Qwen2.5-7B-Instruct 为骨干的 M
- **关键技术点**：** 级联方案存在两大结构性代价：动作模型在音频生成完成后要执行第二次独立推理；运动目标永远无法更新语音或对话参数。近年口语运动模型也未完全解决该问题。核心挑战有三：语音与动作处于异构帧率（12.5 Hz 语音单元 vs 30 Hz 动作）、共享参数时两条损失互相干扰，且没有大规模一致嗓音的运动监督与公开评测基准。
- **主要指标**：
- **代码**：GitHub 与 Hugging Face（论文注明 Code and data available） | **Demo**：https://step-out.github.io/Motion-Omni-Page/

---
## [3 SonicCaps: Large-Scale Diverse and Fine-Grained Captioning for Improved Audio-Retrieval](https://arxiv.org/abs/2609.02343)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-09-02
- **一句话贡献**：现有音频-语言数据集普遍存在语义多样性低、描述缺乏声学细节、单对单映射无法反映听觉感知歧义等问题。本文提出大规模音频标题数据集 SonicCaps，含约70万音频片段与约1500万条标题，由多模态大语言模型 Qwen3-Omni 以音频和文本为条件联合生成，并针对每个音频生成约24条多粒度标题。消融实验表明，标题多样性的提升显著优于质量提升，能使 CLAP 模型在检索与零样本分类上一致获益，并提升
- **关键技术点**：** 音频感知天生具有一对多的语义歧义，而现有数据集通常每段音频只有一两条标题；LLM 生成的标题重复单调、缺乏细粒度声学细节，手工标注又难以规模化且存在主观偏差。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 Summary of the ChinaVoices Challenge 2026: Data, Tasks, Baseline, and Methods](https://arxiv.org/abs/2609.03471)

- **方向**：语音大模型 | **子方向**：Other | **评分**：9/10 | **日期**：2026-09-03
- **一句话贡献**：为填补中文方言语音缺乏统一公开评测平台的空白，本文介绍与NCMMSC 2026联合举办的ChinaVoices Challenge 2026：覆盖16个方言类别，定义多方言识别与多方言ASR双任务，提供约320小时、说话人不相交的三类评测音频。基于Qwen3-ASR-1.7B的统一基线达到53.62% ACC与18.10% CER；最佳参赛系统分别冲到83.19% ACC与11.08% CER，且
- **关键技术点**：** 标准普通话ASR已趋成熟，但真实语音方言众多，方言类别判定与内容转写仍是难点。既有研究使用各方言语料但清单、训练资源与评测集各不相同，缺乏公开可复现、可公平比较的统一平台，同时需评测"识别方言"与"准确转写"两种相关但不同的能力。 **任务与数据：** 16个方言标签，数据约320小时（每方言约20小时），分参考集、开放评测集、隐藏评测集，三集严格说话人不相交，真值转写全部人工生成并质检。识别用macro ACC，ASR用macro CER；每任务设受限与开放双赛道。基线基于Qwen3-ASR-1.7B，LoRA只更新语言模型，把"方言标签+转写"统一为条件生成任务，开放集达到53.62
- **主要指标**：
- **代码**：https://github.com/ASLP-lab/ChinaVoices-Challenge | **Demo**：https://aslp-lab.github.io/ChinaVoices-Challenge/

---
## [1 VoiceDesigner: Text-to-Voice Generation and Editing via Unified Diffusion Modeling and Data Augmentation](https://arxiv.org/abs/2608.13613)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-17
- **一句话贡献**：现有文本到语音生成（TTV）系统面临两大核心挑战：一是生成声音的多样性不足，难以覆盖真实人类说话人和虚构角色；二是缺乏灵活的声音编辑能力，如声音克隆和属性修改。本文提出VoiceDesigner，一个统一的声音生成与编辑框架。在数据层面，作者设计了混合数据流水线，利用DSP音频效果合成（变调、共振峰偏移、混响等）和生成式仿真（零样本TTS+语音转换）来构造覆盖人类和非人类声音的多样化数据集。在模型
- **关键技术点**：** 现有TTV系统主要基于有声书和播客等自然语音数据训练，难以生成小说创作和游戏制作中所需的虚构角色声音（如龙、恶魔、机器人等），也无法处理如"低沉雷鸣般的龙吼"这类基于角色身份而非显式声学属性的描述。此外，声音克隆方法主要针对常规人声设计，对非传统或强风格化声音的克隆鲁棒性不足；指令式声音编辑方法编辑能力有限且难以保持语音质量。更重要的是，生成和编辑通常作为独立系统实现，增加了训练和部署成本。
- **主要指标**：
- **代码**：暂无 | **Demo**：https://voicedesigner-demo.github.io/

---
## [5 Speaker-Normalized Semantic Speech Tokens via Iterative S2U-T2U Refinement](https://arxiv.org/abs/2608.16235)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：语义语音 token 应保留语言内容、抑制说话人与时长信息，但现有 S2U tokenizer 常继承这些声学因素。本文提出 ISTP（迭代语义 token 提纯）：通过迭代 S2U-T2U 交替训练，以 T2U 预测与文本一致性作为提纯信号，逐步将对齐导向文本可预测的 token 空间。中英文实验表明 S2U-T2U 一致性强鲁棒提升（WER 降 72.0%-86.7%，BLEU 增 58.88
- **关键技术点**：** 现有 S2U tokenizer（如 HuBERT 量化）保留说话人、韵律和时长信息，同内容不同说话人产出不同 token 身份或序列长度，给 T2U 建模和隐私带来困难。已有方法依赖声学扰动（R-Spin）、并行话语（PINT）或对齐约束，且 BT4ST/DUB 等 T2U 反向翻译仅生成伪数据、不改动 tokenizer 本身。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 FireRedTTS3: Unified Speech Generation and Editing with Semantically Enriched Speech Representations](https://arxiv.org/abs/2608.17492)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：面向连续自回归TTS（LLM-DiT范式）中误差累积导致的音色漂移、韵律崩塌等问题：现有方案或经VQ量化损失声学细节，或需额外语义模块与多阶段tokenizer训练管道。本文提出FireRedTTS3，在表示层面缓解误差累积：新tokenizer RedAE通过冻结的多任务音频理解编码器对潜空间做语义蒸馏，单阶段GAN训练，无需额外模块；配合轻量LLM-DiT框架，Base变体支持24语言21方言
- **关键技术点**：** Flow-matching类方法依赖预训练文本编码器、非自回归架构难以下游对齐文本LLM的指令跟随能力；VQ/RVQ类量化方法会在语音编辑等声学敏感任务上产生失真。连续自回归（LLM-DiT）框架把离散token预测改写为潜变量去噪，可复用文本LLM的指令跟随能力，但连续特征处于无界空间，预测误差在自回归步间累积，造成音色漂移与韵律崩塌。此前方案或需额外语义模块/多阶段tokenizer训练（Ming-UniAudio、VibeVoice、dots.tts），或引入FSQ瓶颈增加架构复杂度（VoxCPM），本文旨在以表示级语义增强在保持简单架构的前提下解决该问题。
- **主要指标**：
- **代码**：https://github.com/FireRedTeam/FireRedTTS3 | **Demo**：暂无

---
## [5 DAMOS: Learning Distortion-Aware Speech Quality Assessment through Explicit Distortion Localization](https://arxiv.org/abs/2608.21176)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-24
- **一句话贡献**：针对现有语音质量评估（SQA）模型仅以句级 MOS 作为监督、缺乏对感知关键失真位置的显式建模这一局限，本文首次将显式失真定位作为辅助知识引入 MOS 预测。作者构建了首个带帧级失真标注的部分失真语音数据集（15,000 条、覆盖五类 23 种失真），并训练 BAM 定位模型输出帧级失真掩码；在此基础上提出 DAMOS 框架，通过 DSLA、DistortionFiLM 与 LQR 三个模块渐进地
- **关键技术点**：** 现有 SQA 模型依赖句级 MOS 粗粒度监督，既无法指示失真正发生在哪些时域区域，也难以刻画"整体质量往往由少数显著失真区主导"这一感知特征；对于 TTS/VC 等合成语音，发音错误、局部语音塌陷、声码器伪影等短时局部失真会不成比例地拉低听感。作者指出当前 SQA 缺的不是更复杂的网络结构，而是描述"失真在哪"的辅助知识，但公开数据集无帧级标注，且定位信息如何融入预测管道尚待探索。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection](https://arxiv.org/abs/2609.03620)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对真实场景"真伪线索共存"（时间切换、声源重叠或混合）这一传统整段二分类难以处理的问题，提出ToolDF——以音频大语言模型为编排器、经监督工具调用轨迹训练的"工具集成推理"框架。框架自适应分析声学场景、按需调用Demucs分离与人声/背景域专用检测器并聚合证据输出可解释判决。在混合真实性基准上，ToolDF复合类型检测C-Avg达81.89，较最强单体基线XLSR-AASIST提升3.72个点
- **关键技术点**：** 现有ADD普遍假设单域、整段二分类（ASVspoof、CtrSVDD、EnvSDD各自独立）。但真实操控音频可为"混合真实性"：一段剪辑内可同时含真语音到合成歌唱的切换、叠在真实背景乐上的伪元素等。域专属检测器遇到域外声源失效，整段分类器易漏检局部操控，固定先分离再检测的流水线对无需分离的输入引入伪影，直接ALLM做分类器则是黑箱。
- **主要指标**：
- **代码**：https://github.com/rlataewoo/tooldf | **Demo**：暂无

---
## [6 Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://arxiv.org/abs/2609.04102)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对Apple端上Dictation等常驻音频tokenizer与稀疏激活大模型共享DRAM预算的问题，本文提出在预量化潜空间做编码器蒸馏的压缩配方：学生编码器在平方误差目标下回归教师逐帧潜变量，仅加一层仿射层弥合宽度差，无需标签、无需微调即以2.8倍压缩在六组师生对中的五组保持相对WER损失≤1.9%，并比同容量独立训练的tokenizer相对改善3.9%。
- **关键技术点**：** 系统级Dictation的tokenizer（每80ms输出一个向量）常驻内存且与IFP剪枝的200亿参数稀疏模型共享DRAM预算，需至少2.8倍参数压缩且不损失识别精度。若在离散token或解码器输出上蒸馏，前者须穿过不可微argmin，后者让学生容量浪费在端上并不存在的解码器上，故目标选在量化与bridge之前、两种token接口共享的末层潜变量。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 EffVOC: Low-Delay Efficient Speech Waveform Reconstruction from Spectral Representations Without Phase](https://arxiv.org/abs/2609.04226)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-14
- **一句话贡献**：EffVOC 面向无相位谱表示的低延迟语音波形重建。现有方法中，Griffin-Lim 算法（GLA）算法延迟极高；RTISI 系列在 20 ms 延迟下质量骤降；DiffPhase、BAPEN 等神经网络方法依赖整句重建、延迟无限；BigVGAN、Vocos、MelFlow 等生成式声码器普遍存在 32 ms 以上延迟。EffVOC 在已有 20 ms 低延迟声码器基础上统一支持幅度谱与 Mel
- **关键技术点**：** GLA 及其快速变体需大量迭代、算法延迟极高；RTISI 虽延迟 20 ms，但缺少前视致重建精度严重下降。神经网络方法用生成式手段大幅提升质量，但依赖整句重建或延迟超 32 ms；MelFlow 用流匹配实现实时，仍为 32 ms 延迟。低延迟声码器目前仅支持 Mel 输入与宽带合成，幅度谱输入及更高带宽的适用性尚无定论。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 Robust Speech Emotion Recognition under Tone-Word Conflict: A Benchmark and Framework](https://arxiv.org/abs/2609.04236)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-07-27
- **一句话贡献**：现有语音情感识别（SER）系统默认音调与词义一致，但现实交互中普遍存在"声调-词义冲突"（反讽、冷怒等），主流方法在此场景下性能崩溃。针对这一问题，论文构建了首个高密度冲突基准 TWIN-SER（378 条多语言样本，经 LLM 场景生成与 TTS 合成），并提出 DAS（解耦声学-语义融合）框架：通过 MingTok-Audio 声学 tokenizer 与 Whisper 语义编码器双路径解耦
- **关键技术点**：** 论文指出现有方法存在三类结构缺陷：一是语音-文本联合预训练模型（Whisper、CLAP）存在语义偏置，模型被字面含义"污染"；二是 SSL 编码器（HuBERT、wav2vec2、WavLM）产出声学与语义纠缠表征，冲突难以消解；三是大语音语言模型（Qwen2-Audio、Qwen2.5-Omni）的编码器优先语义而削弱韵律情感线索。同时社区缺乏控制变量式的高密度冲突评测基准。
- **主要指标**：
- **代码**：https://github.com/24DavidHuang/FAS | **Demo**：暂无

---
## [9 Rethinking Speech Codecs: From Compression to Autoregressive Generative Modeling](https://arxiv.org/abs/2609.04237)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-27
- **一句话贡献**：主流神经语音编解码器以压缩保真为目标训练，其离散 token 序列缺乏自回归建模所需的时序条件依赖，统计分布偏离自然语言的 Zipf 幂律，与 LLM 的下一个 token 预测范式严重错位，导致语音大模型续训效率低下。本文提出 ARDDS 编解码器训练框架：在 codec 训练中引入辅助自回归解码器，通过温度控制的软量化实现梯度回传，显式约束 token 序列的自回归可预测性；同时提出异构下采样
- **关键技术点**：** 现有语音编解码器以多尺度梅尔谱重建损失、LSGAN 判别损失等联合优化，仅关注率失真与感知质量，对 token 序列的时序结构没有任何约束。作者统计发现各代表 codec 的 token 频率-排名关系明显偏离文本 Zipf 幂律分布，token 缺乏可预测的条件依赖；且第一层语义 token 速率（如 XCodec 50 Hz）远高于对应文本，增加语音大模型续训练负担。这是"压缩目标"与"生成目标"的结构性错位。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 WeSep: A Modular and Cue-Composable Framework for Target Speaker Extraction](https://arxiv.org/abs/2607.27436)

- **方向**：语音大模型 | **子方向**：Separation | **评分**：8/10 | **日期**：2026-07-29
- **一句话贡献**：目标说话人提取（TSE）在给定辅助线索（如说话人注册、空间方向、视频信号或文本描述）的情况下从混合语音中分离目标说话人。现有系统通常针对单一线索类型设计，当线索可用性随场景动态变化时缺乏灵活性。本文提出WeSep统一框架，将TSE重新表述为异构线索条件学习问题，通过标准化接口解耦线索模块与分离器骨干网，支持可配置的线索注入和灵活的多模态集成。在Libri2Mix上，文本关键词线索DAE-TSE达到
- **关键技术点**：** 目标说话人提取（TSE）依赖辅助线索指定目标说话人，但现有系统针对特定线索类型定制架构和训练流程，难以扩展到新线索或多线索组合。实际场景中线索可用性动态变化（注册语音可能不匹配当前状态、空间线索依赖稳定定位、视觉信号可能退化），但缺乏统一框架来系统研究异构图线索条件下的提取行为。
- **主要指标**：
- **代码**：https://github.com/wenet-e2e/WeSep | **Demo**：暂无

---
## [5 Cloned Voices, Real Consequences: Evaluating Bias in Political Deepfake Detection for Electoral Integrity in Brazil](https://arxiv.org/abs/2607.28770)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-07-30
- **一句话贡献**：生成式AI使制作假音频更容易，在选举期间放大政治虚假信息。本文引入ParlaSpoof-BR，一个基于巴西众议院官方录音构建的葡萄牙语政治语音deepfake数据集，包含40名说话人（性别和地区平衡）、2,000个真实样本，通过5种TTS、5种语音转换和部分操控（音频infilling）扩展至134,400个文件（11,200真实/123,200伪造）。评估发现：AASIST和AASIST-L在P
- **关键技术点**：
- **主要指标**：
- **代码**：https://huggingface.co/datasets/freds0/ParlaSpoof-BR | **Demo**：https://ermisai.github.io/parlaspoof-br-demo

---
## [2 Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens](https://arxiv.org/abs/2607.29363)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-07-31
- **一句话贡献**：自回归语音生成中，高帧率高容量表示保留更多信号细节但易受分布漂移和误差累积影响，低帧率压缩表示简化AR建模但可能丢弃重要信息。本文提出协同设计低帧率（8Hz）、高维（768维）、高带宽连续表示与流式生成框架。Locodec tokenizer通过局部编码和训练目标塑造表示空间几何——围绕低维核心流形组织高维空间以改善可插值性，同时保持高维坐标能量层次以改善可辨识性。MP-ELD生成框架使用多路径信
- **关键技术点**：** 自回归语音生成面临信息容量与长程稳定性的权衡。高带宽表示保留更多信号细节但预测误差在AR系统中累积导致漂移（响度、音色、语速、频谱质量退化甚至崩溃）。现有方法依赖语义-声学解耦（如SSL/ASR模型提供语义空间）来降低建模难度，但外部模型引入偏置，限制了tokenizer编码非语义信息的能力。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 SwanTale: Unified Multi-Speaker Speech and Audio Generation](https://arxiv.org/abs/2608.02023)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-04
- **一句话贡献**：字节跳动提出SwanTale，一个统一的多说话人表达性语音和音频生成模型，同时支持零样本和指令（instruct）两种任务。SwanTale从数据和模型两端入手：数据方面提出SwanData-Caption流水线进行数据清洗、合成覆盖增强和多层级标注；模型方面提出SwanVAE支持高质量多音频模态生成，结合Flow-based Transformer、统一MoE、课程学习和GRPO后训练。在零样本
- **关键技术点**：** 动画配音、音频剧、广告、游戏等场景需要同时支持多种语音生成任务：没有参考录音的语音设计（指令任务）、基于参考音频的语音克隆（零样本任务）、环境音效控制、说话人风格自然语言控制等。现有方法通常只支持其中一种任务，缺乏统一框架。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 Normal-Anchored MAML for Whisper Fine-Tuning for Cleft Lip and Palate Speech](https://arxiv.org/abs/2608.00186)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-04
- **一句话贡献**：唇腭裂（CLP）患者的语音在声学和发音上存在显著变异性，导致标准ASR系统识别性能严重下降。本文提出Normal-Anchored FOMAML（一阶模型无关元学习）框架，对Whisper进行CLP语音微调，旨在提升不同严重程度CLP语音的识别公平性。内层使用正常语音作为锚定支持集，外层使用不同严重程度的CLP语音。在NMCPC和AIISH数据集上，正常语音WER 4.40%，轻度CLP 5.53
- **关键技术点**：** CLP语音因腭裂导致发音器官结构异常，在声学和发音上与典型语音差异显著，且不同个体的严重程度和发音模式差异大。标准微调方法训练的模型在CLP语音上表现差，且难以泛化到不同CLP群体。公平性问题：ASR设备对病理语音的识别能力显著下降，影响医疗和辅助通信应用。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 Beyond Prompt Adherence: Auditing Attribute-Level Voice Control in Speech Generation](https://arxiv.org/abs/2608.00545)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-04
- **一句话贡献**：现有语音生成模型的评估仅关注prompt遵循度，忽视属性级控制保真度。本文提出配对审计框架，系统评估CosyVoice3、VoxCPM2、Fish-Speech-S2三个系统的属性级语音控制能力。通过5940个输出样本覆盖6个参考说话人、10段文本、3个随机种子和11种条件。研究发现目标属性变化经常伴随非目标属性的意外变化，CosyVoice3的deep响应率84.4%但93.8%有非目标变化。提
- **关键技术点**：** 语音生成模型支持自然语言描述控制语音属性（如"用低沉的声音说话"、"带点口音"），但现有评估仅检查输出是否与prompt匹配（如是否真的低沉），忽略其他属性是否意外变化（如说话人身份、语速、音色是否改变）。这种评估方式无法发现"属性耦合"问题。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [11 AnyBand: Unified Multi-Bandwidth Speech Extension](https://arxiv.org/abs/2608.00572)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-04
- **一句话贡献**：带宽扩展（BWE）旨在从窄带输入恢复缺失的高频信息。传统方法针对特定带宽设计，当输入带宽变化时需要重新训练。AnyBand将统一多带宽扩展重新表述为上下文频谱填充问题，使用频率感知Diffusion Transformer（DiT）将观测到的低频段作为频率域prompt，条件化生成高频段。在VCTK数据集上，2kHz输入：LSD 1.248, NISQA 3.125, STOI 0.8214；8k
- **关键技术点**：** 实际场景中语音信号的带宽可能因采集设备、传输条件等而变化（如2kHz、4kHz、8kHz），传统BWE方法需要为每个带宽训练专门的模型。理想方案应该用一个统一模型处理任意输入带宽，同时支持规则和不规则（如缺失中频段）的频谱填充。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 MeloCodec: Harnessing Melodic Priors for High-Fidelity Singing Voice Representation](https://arxiv.org/abs/2608.03021)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-05
- **一句话贡献**：神经音频编解码器是LLM音频生成的基础tokenizer。现有工作广泛使用语义先验增强语言可懂度，但显式声学先验的整合仍缺乏探索。MeloCodec提出"Tokenize-then-Fuse"范式，预训练独立的离散旋律分支锁定旋律结构（音高、节奏），再进行特征融合，解决直接融合导致的优化不稳定问题。两阶段训练策略防止码本坍塌。在歌唱声音表示上优于基线，提升音高一致性，支持可控音高操控，最小化音色退
- **关键技术点**：** 神经音频编解码器（如EnCodec、DAC、SoundStream）将音频编码为离散token，作为LLM音频生成（如TTS、音乐生成）的输入。现有工作主要引入语义先验（如HuBERT、WavLM特征）提升可懂度，但显式声学先验（如旋律、音高、节奏）的整合尚未被充分探索。直接融合声学先验可能导致优化不稳定（如码本坍塌、收敛困难），特别是对于歌唱这类对音高敏感的领域。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [10 TurnFSM for Full-Duplex Dialogue System: Internalizing State-Machine Logic for Streaming Semantic Voice Activity Detection and Utterance-Level Rejection](https://arxiv.org/abs/2609.04240)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-05
- **一句话贡献**：全双工语音助手需在持续播放语音的同时监听用户输入，实时处理打断、流式分工和无效输入拒绝。现有端到端方案会让模型在下游推理能力上退化，级联流水线则引入额外推理开销和手工状态机控制逻辑。本文提出 TurnFSM，一种基于 LLM 的流式控制状态预测框架，将级联管线的外部决策逻辑内化为显式有限状态转移（Start、Silence、Listen、Submit、Accept、Reject 六态），并设计一阶
- **关键技术点**：** 现有全双工系统分两类：端到端统一建模（如 Moshi、GLM-4-Voice）接口简洁、天然处理重叠，但语音域适配会损害预训练文本推理与工具调用能力；工业级联管线（声学 VAD、语义 VAD、话语级拒绝逐级串联）稳健但引入额外开销、级间误差传播和手工状态机。折中方案是在共享流式骨干上加双预测头，但两任务决策准则异构，平行标签会在共享表征上产生梯度冲突。TurnFSM 的出发点即消除这种多任务耦合。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663)

- **方向**：音视频生成 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-06
- **一句话贡献**：实时长形式虚拟人音视频生成需要因果连续合成，但预训练双向模型（如LTX2.3）在自回归推理中面临暴露偏差累积和语音内容时序错位两大难题。Vorch-Streamer提出后训练框架，通过合成80K虚拟人片段语料库，结合mixed Teacher Forcing/Diffusion Forcing训练因果生成器，并采用长视野Self Forcing与DMD蒸馏将双向教师模型质量迁移至因果轨迹。引入基于
- **关键技术点**：** 现有双向音视频扩散模型（如LTX2.3）依赖全局双向注意力进行去噪，无法增量式流式输出。自回归复用生成块作为上下文时产生暴露偏差，导致误差累积和视觉漂移。此外，全局文本提示描述了完整语音内容，但因果块只能利用有限局部上下文，无法确定当前应生成哪部分语音。
- **主要指标**：
- **代码**：暂无 | **Demo**：https://vorch-project.github.io/Vorch-Streamer-project/

---
## [4 Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust Speaker Representation](https://arxiv.org/abs/2608.05549)

- **方向**：说话人识别 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-06
- **一句话贡献**：标准残差连接的恒等映射将信息流限制在单一路径，导致深层网络中特征冗余。mHC（Manifold-Constrained Hyper-Connections）将残差路径重写为多流演化，通过Sinkhorn-Knopp迭代将可学习混合矩阵投影到双随机流形上，保证能量守恒（信号强度和特征均值保持）。在ECAPA-TDNN、ResNet-34、Res2Net、E-Res2Net四种骨干网络上，mHC一致提
- **关键技术点**：** 标准残差连接的逐通道相加（y=x+f(x)）缺乏跨通道信息交换机制，随着网络加深产生高度相关特征。Hyper-Connections (HC) 通过多流并行和可学习混合矩阵促进信息交换，但失去恒等映射性质导致信号爆炸/衰减。mHC在保留HC多流交互优势的同时，通过双随机流形约束恢复恒等映射的稳定性。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 Audio-to-Score Transcription using Pre-trained Features, Data Augmentation, and SheetSage-A2S Dataset](https://arxiv.org/abs/2608.06165)

- **方向**：音乐transcription | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-06
- **一句话贡献**：现有音频到乐谱（A2S）系统主要聚焦古典音乐，流行音乐应用严重缺乏数据集和方法探索。本文提出SheetSage-A2S数据集（61小时音频，9468个**kern乐谱片段，来自6066首流行歌曲，为首个真实录音的流行音乐A2S数据集），并引入MuQ预训练特征提取模型和数据增强（音高偏移±3半音+时间伸缩0.9-1.1×）改进A2S方法。在古典Quartets上SER从15.3%降至4.98%（相对
- **关键技术点**：** 现有A2S数据集全部依赖合成音频（MIDI+虚拟乐器渲染），无法泛化到真实录音。流行音乐A2S完全未被探索。此外，缺乏预训练模型和数据增强等常规ML技术的应用，限制了A2S性能天花板。
- **主要指标**：
- **代码**：https://github.com/Multimodal-Music-Research-Lab/SheetSage2Kern_model | **Demo**：暂无

---
## [1 Pixel-TTS: Image based Text Rendering for Robust Text-to-Speech](https://arxiv.org/abs/2606.14750)

- **方向**：TTS | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-06
- **一句话贡献**：传统TTS系统依赖离散Unicode字符嵌入，每个字符独立处理，导致跨语言适配时需扩展嵌入矩阵且在未见字符上泛化能力差。Pixel-TTS提出首个基于视觉文本渲染的端到端语音合成框架：将文本渲染为16×16灰度图像，经2D卷积层投影为像素级嵌入，利用视觉相似性使结构相似字符（如A-À、e-é）产生相近嵌入。在LibriSpeech-PC上WER 2.28%（对比Text-TTS 2.53%），MO
- **关键技术点**：** 传统TTS将每个字符映射为独立one-hot嵌入向量，Unicode编码不同的视觉相似字符（如A和À）被完全独立处理。跨语言适配时需扩展嵌入矩阵，未见字符无法处理。此外，Unicode同形攻击和l33tspeak噪声下传统方法性能急剧下降。
- **主要指标**：
- **代码**：即将发布 | **Demo**：暂无

---
## [4 VocalCoachBench: Benchmarking Audio-Language Models on Expert Feedback for Singing](https://arxiv.org/abs/2609.04241)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-06
- **一句话贡献**：当前音频语言模型评测集中于描述、识别与问答，缺乏对"面向专家的分析式反馈"能力的检验。本文提出 VocalCoachBench，首个面向演唱声乐教练式反馈的专家标注评测基准：含 515 条演唱录音，由 18 位职业声乐教师产出 1052 份反馈与 12051 条原子教练断言。基准将确定性结构化任务（三元组排序、Top-3 问题标签、分段问题分类）与基于原子断言的开放式诊断/纠正评测分离。实测 12
- **关键技术点**：** 现有歌唱自动评估聚焦打分、排序等感知质量判断，基准数据多为小型、平台私有，音乐表演反馈资源面向钢琴/器乐且不将诊断与纠正的有效性本身作为评测目标。关键难点在于声乐教练反馈天然开放——同一演唱不同教练会给出不同主次问题与纠正策略，单一标量分无法刻画。两轮预实验证实标量评分格式失败：4 位专家对齐评分标准后整体 Krippendorff's α 仅约 0.323，分歧源于刻度"阈值校准"，故最终移除标量评分。
- **主要指标**：
- **代码**：暂无具体 URL（标注数据、提示词与评估代码将公开释放） | **Demo**：暂无

---
## [11 Training-Free Speech-Centric Omni Understanding with Frozen VLMs](https://arxiv.org/abs/2609.04242)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-07
- **一句话贡献**：原生 Omni 模型需引入专用音频编码器并依赖大规模音视频文本联合训练，音频通路与特定 VLM 骨干强耦合，成本高且脆弱，并可能削弱其既有视觉、推理与领域能力。本文提出 TFO（Training-Free Omni），一个即插即用的免训练框架：仅用 Whisper 将音频转为经过置信度过滤、带时间戳的转写文本，经 VLM 原有语言接口注入，视觉通路完全不变。在 56 个基准、21 种语言、四个模型
- **关键技术点**：** 原生 Omni 模型通过为 VLM 附加音频编码器并做大规模多模态对齐获得语音能力，但存在三点根本困难：一是每次 VLM 骨干升级都要重做音频通路适配；二是音频信号须与语音内容和视觉事件精确对齐，文献表明原生训练的视听模型仍会忽略相关音频、凭视觉臆测声音；三是修改并联合训练骨干会削弱既有能力。现有评估缺乏与原生训练严格对照的免训练基线，无法回答"音频通路是否对每类任务都必需"。
- **主要指标**：
- **代码**：https://github.com/mbzuai-oryx/OmniEvalKit | **Demo**：https://mbzuai-oryx.github.io/OmniEvalKit

---
## [3 SonicWeave: Chunk-Routed Mixture-of-Experts for Unified Audio Scene Generation](https://arxiv.org/abs/2608.09571)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-10
- **一句话贡献**：文本条件通用音频生成正从孤立的语音、音乐和音效合成走向单一模型组合可控连贯音频场景。SonicWeave 提出基于分块路由 MoE 的流匹配模型，核心是冲突门控先验-证据路由机制（CPE-MoE），通过结合全局先验（编码文本条件和扩散相位）和局部证据（进化声学状态）来路由连续声学块。当局部状态不可靠时，学习到的冲突门偏向先验；当区域偏离全局场景上下文时，允许局部证据影响路由。支持语音、音乐、音效、
- **关键技术点**：** 统一音频场景生成中，异构组件（语音、音乐、音效）对共享骨干提出冲突的结构要求，复杂混合场景可能包含局部不同或重叠内容，需要细粒度适应。现有音频 MoE 主要在域级别路由，token 级路由忽略声学信号的局部连续性。
- **主要指标**：
- **代码**：暂无 | **Demo**：https://caiyunrui.github.io/SonicWeave

---
## [7 RAG-Audio: Retrieval-Augmented Generation for Faithful Brain-to-Audio Reconstruction](https://arxiv.org/abs/2608.09331)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-10
- **一句话贡献**：脑到音频重建受限于"先验主导"问题：当预训练生成器以弱神经信号为条件时，会产生逼真但刺激不准确的音频。RAG-Audio 将 fMRI 解码为语义音频 embedding，检索匹配的真实音频样本，从该样本初始化冻结生成器的采样轨迹，同时保留解码 embedding 作为条件。在 Brain2Music 上，10 路刺激识别从 0.14-0.18（直接生成，接近随机 0.10）提升到 0.40-0.
- **关键技术点**：** 脑到音频重建中，fMRI 信号空间分辨率有限（~2mm），时间分辨率低（~1s），导致条件信号弱。预训练生成器倾向于产生"先验主导"的输出——逼真但与刺激无关。现有方法难以区分 generator 先验和神经信号驱动的重建。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 From Inaudible Inputs to Model Failures: Low-Frequency Safety Risks in LALMs](https://arxiv.org/abs/2608.09158)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-10
- **一句话贡献**：大型音频语言模型（LALM）已展示理解多样音频输入的能力，包括人类听不见的低频信号。该工作提出间歇性低频锁定（ILL）攻击方法，使用通用波形模板在黑盒设置中评估此风险。ILL 使用句子注意力尺度估计确定活跃区间，频率混淆转移从语料谱变化构建连续相位低频波形。提出分布重查询守卫（DRG）检测低频分布偏移并条件性请求第二次录音进行语义恢复。在 6 个 LALM 和多个音频理解任务上，ILL 降低准确率
- **关键技术点**：** LALM 处理人类可听频段（20Hz-20kHz）和不可听低频（<20Hz）信号，但低频输入对 LALM 安全性的实际影响尚未被探索。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 The GENEA Challenge 2026: Large-Scale Disentangled Evaluation of Speech-Driven Gesture Generation](https://arxiv.org/abs/2608.10839)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-11
- **一句话贡献**：GENEA Challenge 2026 是第四届语音驱动手势生成挑战赛，在 Seamless Interaction 对话数据集上对 5 个参赛系统进行大规模人类评估。采用解构评估方法分别评估动作质量和语音对齐，消除两者混淆效应，并引入新的语义手势生成任务和文本失配评估方法。在四个大规模用户研究中收集了 869 名测试者的 23000+ 投票。关键发现：数据集中过滤片段在动作质量上远超所有参赛系
- **关键技术点**：** 语音驱动手势生成评估中，动作质量和语音对齐通常相互混淆——高质量动作可能因与语音不匹配而评分低，反之亦然。现有方法未有效分离这两个维度。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Never Stop Speaking: a Denial-of-Service Attack on End-to-End Speech Language Models](https://arxiv.org/abs/2608.10405)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-11
- **一句话贡献**：现有文本 DoS 攻击主要针对纯文本 LLM，端到端语音 LLM 的 DoS 漏洞尚未被探索。该工作提出基于扰动的 DoS 攻击，优化不可感知的声学扰动以影响 E2E 语音 LLM 的自回归生成过程，在保持原始输入长度的同时抑制 EOS 生成、鼓励延长解码。使用 VAD 仅在有声区域注入扰动。在三个开源 E2E 语音 LLM 上实现了稳定攻击成功率，显著增加生成长度和 GPU 资源消耗，揭示了现代
- **关键技术点**：** 文本 LLM 的 DoS 攻击通过 prompt 工程（对抗后缀、语义诱导）实现，但无法直接迁移到连续语音输入。现有语音模型安全研究主要关注 ASR/TTS 系统，未涉及 E2E 语音 LLM 的 DoS 脆弱性。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 VoxSumm: A Multilingual Corpus of Long-Form Spoken News for Joint Summarization and Translation](https://arxiv.org/abs/2608.10359)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-11
- **一句话贡献**：长文档摘要研究仍以文本为中心，多语言语音研究主要优先翻译而非压缩。VoxSumm 正式定义联合语音摘要与翻译（JSumT）任务——从源语言长口语文档直接生成目标语言简洁忠实摘要。构建首个多语言跨语言基准，包含 10045 个 BBC 文章-摘要对，覆盖 24 种语言，约 703 小时语音数据。评估代表性语音语言模型，Gemini3.1-Pro 表现最佳，英语摘要普遍优于非英语目标语言生成，先翻译整
- **关键技术点**：** 多语言语音研究主要关注翻译（保留源内容），长文档摘要研究主要关注文本。两者结合——从语音直接生成跨语言摘要——尚未被正式定义和基准化。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 CookVoice: Unified Voice-Singing Generation](https://arxiv.org/abs/2608.11590)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-12
- **一句话贡献**：CookVoice提出统一的语音与歌声生成框架，将语音信号分解为内容（content）、韵律（prosody）和风格（style）三个正交要素，并分别建模。Flow Matching DiT结合HiFi-GAN自编码器，总参数量仅43.51M（DiT-S），在168小时数据上训练。模型支持文本/语音风格控制和离散/连续韵律控制，F0相对音高归一化有效解耦风格与韵律。S-SIM达91.65%（TTS
- **关键技术点**：** 语音生成和歌声生成通常由独立系统处理，缺乏统一的生成框架。现有方法在风格控制、韵律控制和内容保真度之间的权衡不理想，且参数量大、推理效率低。
- **主要指标**：
- **代码**：暂无 | **Demo**：https://haoweilou.github.io/CookVoice/

---
## [6 MiDashengLM-Gen: Unified Audio Scene Generation](https://arxiv.org/abs/2608.11804)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-12
- **一句话贡献**：MiDashengLM-Gen提出基于LLM驱动的自回归流匹配统一框架，实现语音、音乐和音效三种音频场景的端到端统一生成。模型采用LLM+per-token条件流匹配架构，无需依赖外部声码器或编解码器。在Seed-TTS基准上WER达2.79%，在MECAT benchmark上达到竞争性结果。代码和Demo已全部开源。
- **关键技术点**：** 现有音频生成系统通常针对单一场景（语音、音乐或音效）独立设计，缺乏统一的生成框架。不同场景的音频在时域结构、频域分布和语义内容上差异巨大，统一建模面临挑战。
- **主要指标**：
- **代码**：https://github.com/xiaomi-research/midashenglm-gen | **Demo**：https://xingws.github.io/midashenglm-gen-demo/

---
## [2 VoxAudio: Vocalized Audio Synthesis via Multi-Reward Autoregressive Flow Matching](https://arxiv.org/abs/2608.12951)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-13
- **一句话贡献**：有声语音合成（vocalized audio synthesis）指在环境声景中嵌入可理解语音的音频生成任务，现有 T2A 系统要么将引述语音退化为不可理解的嘟囔，要么依赖独立的 TTS 模型后期混合，丧失对语音发生时机和场景交互的控制。VoxAudio 提出因果自回归流匹配模型，在架构层面采用逐块因果分解与独立噪声级别，支持滑动窗口流式推理和 KV 缓存；在偏好层面引入多奖励负感知微调（NFT）
- **关键技术点**：** 现有文本到音频（T2A）系统无法在环境声景中生成可理解语音，引述台词通常变为不可理解的发声纹理。解耦流水线（分别合成语音和背景音再后期混合）无法控制语音与场景的时序交互和相对响度，破坏了听觉场景的连贯性。根本原因在于数据层面缺乏联合标注、架构层面非自回归公式不支持流式输出、训练范式缺乏人类偏好对齐。
- **主要指标**：
- **代码**：https://voxaudio.github.io | **Demo**：https://voxaudio.github.io

---
## [2 AT-ADD: All-Type Audio Deepfake Detection Challenge Summary](https://arxiv.org/abs/2608.14249)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-17
- **一句话贡献**：本文是ACM Multimedia 2026 AT-ADD大挑战赛的总结报告，针对音频深度伪造检测领域两大核心问题：一是在真实声学与信道变化下的鲁棒语音深度伪造检测（Track 1），二是跨语音、环境音、歌声和音乐四种类型的全类型音频深度伪造检测（Track 2）。挑战赛采用封闭设置，参赛者仅可使用组织者提供的训练/开发数据、信号级数据增强和可追溯的通用预训练模型。Track 1评估集包含26种未
- **关键技术点**：** 现有ADD研究在ASVspoof和ADD挑战系列中取得显著进展，但实际部署面临两大关键瓶颈：一是真实声学环境和信道条件下的鲁棒性不足，现有基准测试中的真实语音多来自受控环境，而实际场景中录音设备、声学环境、语言种类等因素存在巨大变化；二是面对异构音频类型（语音、环境音、歌声、音乐）时的泛化能力有限，生成式AI已能合成各种类型的高保真音频，而现有检测器大多仅针对单一语音类型设计。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 Trajectory Dynamics in Self-Supervised Learning Latent Space for Audio Deepfake Detection](https://arxiv.org/abs/2608.13817)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-17
- **一句话贡献**：现有语音深度伪造检测方法大多依赖SSL特征提取器加全局池化，丢弃了时序顺序信息，在跨语料库泛化时性能急剧下降。本文提出利用人类语音生理约束在SSL潜空间中产生的结构化轨迹动态进行检测：训练一个因果LSTM下一帧预测器（Stage 1），仅在ASVspoof 2019的真实语音上学习轨迹动态，以预测误差作为异常分数；可选Stage 2将冻结的LSTM隐状态均值池化后训练一个有监督MLP分类器。在AS
- **关键技术点**：** 现有SSL检测方法（如AntiDeepfake、SLIM、QAMO、BreathNet）大多对帧级嵌入做全局平均池化或注意力加权汇总，完全丢弃时序顺序。少量利用时序结构的工作（FGFM、TRACE、BreathNet）要么针对局部拼接伪影，要么需要伪造监督信号，均未建模整段语音的全局生理合理性轨迹。
- **主要指标**：
- **代码**：https://doi.org/10.5281/zenodo.21879214 | **Demo**：暂无

---
## [6 Omni-LiveAvatar: Minute-Level Real-Time Streaming Joint Audio-Visual Avatar Generation](https://arxiv.org/abs/2608.13602)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-17
- **一句话贡献**：现有联合音视频生成模型依赖双向注意力与多步去噪，推理延迟高且仅能生成短视频，无法用于实时长时交互。本文提出Omni-LiveAvatar，首个支持分钟级实时流式联合音视频数字人生成的框架。核心贡献包括：(1) 渐进式自回归蒸馏，将19B参数的双向联合音视频扩散模型LTX-2转化为4步因果生成器，无需辅助稳定机制，在单卡H200上实现33倍加速（21.99 FPS）；(2) 同步音视频长短时记忆机制
- **关键技术点**：** 现有联合音视频生成模型（如LTX-2、Ovi）依赖双向注意力与多步去噪，推理速度慢且仅能生成短片段。近期工作如OmniForcing和Hallo-Live尝试通过自回归蒸馏实现实时生成，但依赖音频sink token、额外未来音频上下文或外部奖励模型等模态特定补偿手段，而非从本质上解决蒸馏框架的不稳定性。此外，现有方法局限于短片段生成，分钟级流式数字人生成尚未被探索，主要面临三大挑战：大尺度多模态模型蒸馏困难，音频建模与跨模态耦合增加蒸馏难度；跨模态漂移，视觉与音频漂移随时间累积并相互放大；异构语义调度，需协调缓慢变化的视觉上下文与快速变化的语音内容。
- **主要指标**：
- **代码**：https://github.com/Aoko955/Omni-LiveAvatar | **Demo**：暂无

---
## [9 DuplexGen: Decoupling Content, Timing, and Acoustics for Synthetic Dialogue Speech](https://arxiv.org/abs/2608.16053)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：现有对话合成管线先生成内容、再用标记或规则插入重叠/打断/反馈词，时序是"规定"而非"涌现"。DuplexGen 将内容、时序、声学显式解耦：DeepSeek-V4 生成脚本，两个 Moshi 式 full-duplex 对话模型实时互听执行脚本（时序自然涌现），CosyVoice 无改时序重渲染。FTO Wasserstein 距离由 0.695 降至 0.366（相对降 47%），重叠转变比例
- **关键技术点**：** 常规方法（Behavior-SD、PersonaPlex 等）依赖对话标记、行为标签或手工时序规则拼接语音，重叠间隔分布坍缩到单一峰值，背离真实对话；而 full-duplex 模型（Moshi、SyncLLM）交互自然但自由生成、无法遵循预设脚本。可控内容与涌现交互难以兼得，二者结合少被探索。本文假设对话生成应按语义、交互、声学三类决策独立解耦，实现零训练管线。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [11 ACE-Cap: Active Evidence Acquisition via Agentic Co-Evolution for Long-Paragraph Fine-Grained Audio Captioning](https://arxiv.org/abs/2608.16162)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：长段落细粒度音频字幕生成要求模型覆盖多样化声学事实，但现有字幕器均为被动一次性生成器，遗漏细节后无法自查、定向查询音频或自适应决定何时证据充分。本文将任务重构为主动证据采（Active Evidence Acquisition）问题，提出 ACE-Cap：由 Captioner 生成初始描述，文本-only 的 Composer 多轮提问、由音频条件化的 Instruct 回答，证据累积后 Com
- **关键技术点**：** 现有一键式字幕生成模型在粗粒度或短句生成上表现良好，但面对长段落细粒度字幕时一旦遗漏细节便无法补救；扩大模型与数据规模无法获得主动信息获取机制。同时多轮交互训练存在两大难题：异构动作（提问/停止/合成）的跨回合信用分配（相邻差分法受回合顺序与分数饱和影响、给予早问以首动者优势）；多智能体共同优化时的目标移动导致训练不稳定。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [12 How Fragile Is Your Watermark? Training-Free Structural Removal of Neural Audio Watermarks](https://arxiv.org/abs/2608.16566)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-18
- **一句话贡献**：论文提出"先诊断后移除"的免训练框架：从少量干净/含水印配对信号计算四个廉价结构探针，估计水印嵌入域并据此选择单一匹配攻击，取代固定失真集的盲目扫描。在 10 种水印方案上，幅度域方案 WavMark、SilentCipher、audiowmark 被单次匹配攻击在近乎透明质量（PESQ≥3.6）下擦除载荷，AudioSeal 检测标志被移除；潜在域方案 VoiceMark、WMCodec、Ali
- **关键技术点**：** 现有鲁棒性评估（AudioMarkBench、RAW-Bench、SoK）对全部方案盲目施加同一固定失真集，仅报告聚合准确率/检测率，掩盖了攻击者真正关心的两个问题：水印嵌入在哪里、哪种扰动移除代价最低。已有移除方式要么是经典估计/减法、谐波攻击，需训练跨域去除网络。
- **主要指标**：
- **代码**：https://github.com/i-618/audio-watermark-fragility | **Demo**：暂无

---
## [3 Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges](https://arxiv.org/abs/2608.17605)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：本综述系统覆盖多轮对话AI从文本向多模态交互的演进，横跨纯文本对话、AudioLLM/语音原生系统、多模态/全模态系统与工具增强智能体四类体系，以session级持续交互（而非单轮响应）为分析单元，沿数据集与基准、建模范式、训练策略、评测设置与跨领域挑战组织文献（初筛约4K篇，经PRISMA-ScR筛选精读200篇）。核心发现：多模态感知/说话/行动能力进步快于跨轮连贯交互能力，持久记忆、跨轮gr
- **关键技术点**：** 真实对话中用户会澄清目标、修订请求、打断答复、切换话题、引入新证据，并要求系统保留上下文。现有前沿模型即使信息在上下文窗口内也常利用不足，任务分散在多轮时性能退化（Lost in Multi-turn、MultiChallenge），且此类失败只在session级显现、轮级评测会漏检；语音/多模态/工具设置下错误还会跨轮传播（ASR错误、视觉grounding衰减、工具外部状态）。
- **主要指标**：
- **代码**：https://github.com/faiza-sfa/multiturn-conversational-ai-survey | **Demo**：暂无

---
## [4 Emotion Across Speech and Faces: Shared Affective Mechanisms in Multimodal Foundation Models](https://arxiv.org/abs/2608.17102)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：多模态基础模型（MFM）识别语音与面部情绪时，是依赖共享的情感功能单元还是模态特异通路，此前尚无定论。本文以语音情感识别（SER）和面部表情识别（FER）为互补探针，在 Gemma-4-12B-it、MiniCPM-o-4.5、Qwen2.5-Omni-7B 中利用对比激活边际（ConAct）定位稀疏解码器情感敏感神经元（ESN）。结果显示：去激活 ESN 选择性损害对应情绪（Gemma FER 
- **关键技术点**：** 心理学与情感计算长期争论情感感知源于跨模态共享类别还是模态特异线索。本文以语音和面部情绪识别作为测试床，首次在激活层面对齐 MFM 内部情感表征：识别 ESN、分析结构对齐并因果验证，判定情感处理是否收敛于共享的解码器组件（基于 Introduction）。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 The Last Mile of Deepfake Speech Detection: An Industry-Academia Experience Report](https://arxiv.org/abs/2608.17585)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：本文是捷克内政部 SECTECH 项目（VB02000060）资助、Phonexia 与布尔诺理工大学合作三年、面向捷克警方交付深度伪造语音检测器的产业-学术经验报告。核心问题：公开 benchmark 宣称 sub-1% 错误率，但现实部署在"最后一公里"失效。三大 barrier：公开语料不可商用授权（数据灰色地带）、真实输入是长录音/codec 退化/部分合成而非 4 秒干净片段、LLR 2
- **关键技术点**：** 现有合成语音检测 benchmark（ASVspoof 系列、in-the-wild 语料）宣称 in-domain 亚 1% 错误率，但 Müller 等报道跨域 EER 退化达 1000%，社区共识是深度伪造检测本质为 OOD 泛化问题。本文不提出新模型，而是从引擎内部视角记录生产化过程，指出 in-domain 精度无法证明部署就绪。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 DNN-Based Frequency-Dependent Estimation of Speech, Music, and Noise Power in Acoustic Mixtures for Hearing-Aid Scene Analysis](https://arxiv.org/abs/2608.17482)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：当前助听器场景分析依赖多个独立估计器（场景分类、VAD、SNR 估计），计算开销大且未利用任务间依赖。本文提出统一可解释的场景表示：用低复杂度因果 CRNN 将混合谱分解为语音/音乐/噪声三类时-频相关相对功率比例，再与混合功率相乘恢复各类功率谱。开发集总体对数误差 1.40 dB、PCC 0.891；未见数据集为 1.71 dB、0.875。下游 VAD 经简单阈值化即可达到与 SOTA Sil
- **关键技术点**：** SOTA 场景分析通常由多个独立估计器组成（场景分类、VAD、SNR 估计、源定位/方向分析），输出控制压缩、降噪与程序自动切换。该模块化设计有两方面缺陷：一是计算低效，而深度学习算法进入助听器后台算力更趋紧张；二是独立估计器无法利用相关任务间的依赖，且多从同一混合声提取重叠信息（如 VAD 与 SNR 估计）。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 A Multiplication-Free Feature Extractor for Signal Classification: Keyword Spotting Case Study](https://arxiv.org/abs/2608.17108)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-19
- **一句话贡献**：关键词唤醒（KWS）需要极低复杂度的信号分类链，而MFCC含FFT、DCT与对数等乘法运算、CNN特征提取器计算量大，难以部署于超低功耗TinyML平台。本文提出完全无乘法的next iRDT特征提取器，仅依赖加减、比较等能量高效算术运算。在Google KWS 12类数据集上，配合baseline分类器其准确率与MFCC/CNN特征提取器相当，换用另一分类器达到94.7%验证准确率；CPU处理时
- **关键技术点**：** KWS是TinyML的典型应用，要求信号分类链复杂度极低。主流特征提取器（MFCC的FFT/DCT/对数/滤波组、CNN方案的乘加密集算子）依赖大量乘法运算，在无硬件乘法器、内存受限的MCU上代价高昂，是超低功率部署的主要瓶颈。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 Represented but Ignored: A Causal Account of Prosodic Underuse in Audio-Language Models](https://arxiv.org/abs/2608.19211)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-20
- **一句话贡献**：人类语音的韵律承载着超越词汇内容的语言与情感信息，理想的音频语言模型（audio-LLM）应能理解"怎么说"而不只是"说了什么"，但现有基准只评测最终答案，无法定位模型韵律失败的根源。本文提出一个分阶段的探针阶梯（probe ladder），把韵律失败划分为三大机制：F1 感知失败（语音通路未保留韵律对比）、F2 解释失败（内部表征了错误的韵律类别）、F3 使用不足（内部表征正确但未充分表达在答案
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Tracking the Trend in How Speech Synthesizers Deceive People](https://arxiv.org/abs/2608.19959)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-20
- **一句话贡献**：早期研究普遍报告人对深度伪造语音有 70–80% 的检出率，但这些结论大多基于 2019 年左右的旧一代合成器。本文针对 2019、2022、2024 三个不同发布时期的合成工具（RTVC、YourTTS、ElevenLabs）开展受控实证比较：82 名 IT 从业者在明确被告知"存在深度伪造"的条件下，对全合成（full spoof）与局部替换（partial spoof）语音做逐句真实性判断，
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 Grounded Decoding for Autoregressive Speech Enhancement via Adaptive Code-Space Grounding and Local LLM Refinement](https://arxiv.org/abs/2609.04245)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：8/10 | **日期**：2026-08-21
- **一句话贡献**：LLM 自回归语音增强（SE）能借助干净语音先验生成自然语音，但易产生输入不支持的内容幻觉；确定性增强更忠实保留观测证据，却常残留噪声或局部失真。本文提出证据锚定的生成式 SE 框架：以 Whisper 引导的 DPRNN 确定性增强器输出作为观测耦合证据，与带噪观测混合后经 FSQ 分词得到离散证据序列用于条件生成，并设计 Code-Space Grounding（CSG）按 FSQ 空间中的汉
- **关键技术点**：** 确定性 SE 在 DNN 输出层保留语言内容但残留噪声与局部失真；LLM 类生成式 SE 利用长程上下文恢复重度退化区域，但强先验可能覆盖模糊声学证据造成幻觉。已有低幻觉生成式 SE 主要改进送入生成器的信息，并不显式约束解码过程本身。本文核心出发点是把确定性输出当作不完美但观测耦合的证据而非最终结果或伪干净目标。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 A Factorial Ablation of a Speech-to-SFT Pipeline: Differential Effects on Data Quality and Downstream Transfer](https://arxiv.org/abs/2608.20394)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-24
- **一句话贡献**：语音转SFT数据流水线在工业界广泛应用，但各阶段的边际价值此前从未被公开逐阶段验证。本文针对韩国医学与金融会议录音驱动的三段式流水线（Phase 0转录精炼、Phase 1 QA生成、Phase 2质量精炼）设计2x2因子消融，四种条件各生成约2600条QA，微调5大厂商9个（2.4B-70B）LLM，并以4个跨厂商LLM评判员、6位盲评领域专家及KMMLU/KMMLU-Pro/MMLU三个基准评
- **关键技术点**：** 现有语音转SFT工作（COSMIC、SIFT-50M、LiveCC、PodGPT等）或面向通用能力或采用持续预训练而非文本LLM SFT，均未对精炼环节做逐阶段消融，各阶段边际价值对实践者未知；且当数据源为语音时有转录噪声、命名实体对齐、语篇结构缺失等文档源不存在的前端挑战。
- **主要指标**：
- **代码**：https://github.com/flitto/speech-to-sft-ablation-paper | **Demo**：暂无

---
## [3 WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](https://arxiv.org/abs/2608.22704)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：长音频输入的语音LLM其推理瓶颈由模型参数转移到KV缓存（10分钟音频即占7500-15000个KV位置）。现有prefill-only压缩方法在长音频上失效：prefill注意力集中于音频开头（attention-sink），而decode注意力分布均匀。本文提出WnW，通过离线校准将KV头分类为anchor/tidal/fixed三类，解码期以anchor头注意力作为重要性观测信号，将tida
- **关键技术点**：** 现有H2O、SnapKV、Ada-KV、AudioKV等方法均在prefill阶段利用提示注意力一次性打分并固定保留集，其核心假设"prefill注意力能预测decode期注意力"在长音频上不成立。论文实测prefill注意力呈attention-sink分布（前10%位置占47.9%质量），而decode累积注意力近乎均匀（前10%仅9.8%）；240个KV头逐头Jaccard（K=100）在0.006-0.641间。一旦prefill期将位置永久丢弃、无恢复通道，压缩方法就结构性受损。
- **主要指标**：
- **代码**：https://github.com/XMUDeepLIT/WnW | **Demo**：暂无

---
## [4 MetaSICL: Globalizing Auditory LLMs for Underserved Speakers and Languages via Meta Speech In-Context Learning](https://arxiv.org/abs/2601.18904)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：听觉大语言模型多在高资源英语成人数据上训练，对儿童语音、语音翻译方向及文化性音频理解等低资源场景表现差，直接微调在分布偏移下易过拟合甚至退化。作者提出MetaSICL后训练配方，仅用充沛的高资源ASR+ST数据以上下文学习（ICL）格式构建episode，教会模型"如何使用演示"做测试时适配。在两个backbone（MiMo-Audio与Qwen2.5-Omni）上，MetaSICL相比vanil
- **关键技术点**：** 全球化生成式AI要求听觉LLM适配低资源用户、语言、方言与年龄组，但现有模型被成人英语等高资源数据主导。多数目标社区在训练数据中覆盖不足，而收集标注充分的域内语料成本高、难以代表真实测试分布，直接监督微调会过拟合到数据集特有伪影。文本领域MetaICL等已证明元训练可增强ICL能力，但该范式是否适用于听觉LLM仍属空白。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Reasoning-Oriented Post-Training and Inference-Time LoRA Rescaling for Audio-Dependent Question Answering](https://arxiv.org/abs/2608.23092)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：针对 DCASE 2026 Task 5 ADQA 任务，本文提出结构化思维链（Structured CoT）后训练框架与推理时 LoRA 缩放机制，并在 Qwen2.5-Omni 与 MOSS-Audio-8B-Thinking 两个骨干上系统分析适配行为。Qwen 系统经 SFT+GRPO/GDPO 后 top-1 从基线 54.39% 提升至 58.93%，推理时将 LoRA 缩放因子降至 
- **关键技术点**：** 现有听觉问答基准存在语言先验泄露，模型替换音频为静音仍能答对部分题，无法证明真正基于音频推理。ADQA 通过 Audio-Dependency Filtering 筛选强音频依赖样本解决该问题，但答案级奖励不监督中间推理是否扎根于声学证据，可能产生未落地或退化的推理轨迹；且任务特定后训练并非对所有模型有益。
- **主要指标**：
- **代码**：https://github.com/WeitengHu/DCASE2026-Task5 | **Demo**：暂无

---
## [2 AT-ADD: A Benchmark and Challenge for Robust and All-Type Audio Deepfake Detection](https://arxiv.org/abs/2608.23437)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：本文提出 AT-ADD 基准与 ACM Multimedia 2026 大挑战，针对现有 ADD 检测以语音为中心、忽略真实信道变化与多类型音频的问题，构建两大任务：Track1 为覆盖47个生成模型、11,299说话人、96种语言及噪声/混响/重放/压缩等扰动的鲁棒语音深伪检测；Track2 为语音、环境声、歌声、音乐四类音频在测试时类型未知条件下的全类型检测。官方最强基线 FT-XLSR-AA
- **关键技术点**：** 现有 ADD 基准（ASVspoof、ADD、SVDD等）以语音为中心且多在受控条件下评估，对压缩、噪声、混响、重放等真实信道变化鲁棒性差；对 ALLM 合成与 neural codec 等新范式及非语音音频类型泛化不足。AT-ADD 以渐进式双赛道弥合理想研究与真实多媒体取证之间的差距，全程采用闭合设置，仅允许使用官方 train/dev 数据。
- **主要指标**：
- **代码**：https://github.com/xieyuankun/AT-ADD-Baseline | **Demo**：https://at-add.com

---
## [3 Separating Voice from Age in COPD Screening](https://arxiv.org/abs/2608.21599)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-25
- **一句话贡献**：本文针对 COPD 语音筛查结果可被"年龄混淆"琐碎解释的问题，重新评估公开的 COPDVD 持续元音语料（1246条录音、68名参与者），首次在严格的参与者级年龄匹配队列上验证语音是否携带超越年龄的疾病信息。作者发现常规合并评估在年龄严重失衡（SMD=0.726）下无法区分语音病理与年龄信号，遂提出以"混淆变量自身的判别力"（原始年龄 AUC 0.510、性别0.479，均为随机水平）为已核验对
- **关键技术点**：** COPD 强年龄相关且发声随年龄衰老变化，病例组普遍比对照组年老时，模型可能学到的是年龄或其声学代理而非疾病。仅"剔除年龄变量"的训练并不充分：特征与年龄相关时，灵活学习器可从相关声学特征中重构年龄驱动决策边界。作者审计数据发现：按参与者计对照组比 COPD 组年轻7.7岁、SMD=0.726，而按录音加权则方向反转——源论文声称的年龄匹配基于录音而非参与者统计。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 SpeechGym: An Audio-Native Gym for Training Voice Agents via Reinforcement Learning](https://arxiv.org/abs/2608.26432)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-26
- **一句话贡献**：语音智能体必须完全通过语音调用工具、遵守领域策略并把多轮对话驱动到可验证的终态，但主流范式仍在文本中训练、在边缘拼接语音。现有方案要么在专有语音API外级联TTS/ASR（梯度不可回传、按次计费使在线RL不可行），要么停留在纯文本。论文提出SpeechGym，一个音频原生智能体环境：两个全模态模型用原生音频对话——冻结的用户模型扮演来电者，可训练的Thinker-Talker智能体在结构化工具调用
- **关键技术点**：** 语音智能体必须用语音完成文本智能体的一切动作，而主流做法在文本中训练策略、在边缘附加语音，假定文本能力能穿过音频回路而存活。τ-Voice将τ²-bench包进语音循环并报告了陡峭的文本到语音性能落差，却无法弥合：梯度无法穿过封闭API，且延迟与价格排除了在线RL所需的rollout规模（单epoch API成本超200美元，7轮超1400美元，千epoch接近20万美元）。全模态模型在架构上消解了级联，但只在无工具、无对话对象的单轮任务上做过RL。作者指出失败本质是感知缺陷而非推理缺陷：智能体选对了工具与参数槽，却把从波形中误听的数值填进去，该错误级联为调用失败、重复重试与步数预算浪费
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 Closing the Verification Loop: Self-Check Captioning for Long-Paragraph Detailed Audio Captioning](https://arxiv.org/abs/2608.30713)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-08-31
- **一句话贡献**：本文针对长段落、细粒度且与转写文本逐字对齐的详细音频字幕生成（long-paragraph detailed audio captioning）这一任务。现有视听多模态大语言模型因数据匮乏与生成模式失效两大结构性问题而失败，后者的证据是正确音频与打乱音频多选问答准确率存在44.8~46.4个百分点差距。作者提出自检字幕生成框架（SCC），将基于音频接地问答作为各生命周期阶段的验证原语，产出包含50
- **关键技术点**：** 长段落详细音频字幕生成要求对细粒度音频内容进行密集且忠实于转写的描述。现有视听大模型在该任务上失败源于两大结构性原因：一是数据贫困，公开语料无法同时提供长音频、段落级字幕与逐字转写保真度；二是生成模式失效，模型在"听错音频也能答对"的表现下产生幻觉式字幕。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 Perceptible or Not? Diagnosing Passive Fingerprints for Speech Deepfake Attribution](https://arxiv.org/abs/2609.00765)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：被动指纹可用于深度伪造语音溯源，但其持久性、可复现性与内容无关性尚未被验证。本文提出可感知-不可感知被动指纹诊断协议（PIPDP），通过残差能量、可复现性、显著性分析等多证据验证，结合感知透明扰动与提示驱动情绪变化两类干预剖析两类指纹。在10个语音生成器与3个溯源检测器上，不可感知指纹能提供持久溯源线索；感知透明扰动使HiggsAudioV3上溯源准确率最高下降48.2%。
- **关键技术点**：** 深度伪造归因依赖生成器遗留的被动指纹，但指纹跨模型更新、跨内容的稳定性从未被系统验证。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 Heard but Not Heeded: Paralinguistic Information Encoding and Loss in Audio-Language Models](https://arxiv.org/abs/2609.00727)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：音频大模型能否真正捕捉"怎么说"而非仅"说什么"仍无定论。本文对Whisper-large-v2、Qwen2-Audio-7B、Qwen2.5-Omni-7B、Chroma-4B四个模型，在Expresso数据集受控说话风格下进行机制级分析。结合CKA、留一说话人线性探测、开放式音调预测与内容-韵律泄漏指标，追踪风格信息从编码器到输出的流动。结果所有模型在编码器后1/3层强烈编码说话风格，但在到达
- **关键技术点**：** 韵律、情绪等副语言信息对真实语音理解至关重要，但现有音频语言模型是否真正利用这些信息缺乏机制级证据。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 BiMTokenizer: Preserving Semantic-Acoustic Balance in Low-Bitrate Speech Tokenization via Bidirectional State-Space Modeling](https://arxiv.org/abs/2609.00562)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：语音编解码器面临声学保真与语义保真的冲突。近期方案普遍采用双塔架构解耦语义与声学建模，但结构开销巨大。本文回归单塔范式，提出BiMTokenizer——约1.1 kbps的低码率编解码器，采用双向状态空间骨干结合残差球面网格量化（RSLQ）。实验在干净与噪声环境下均取得最优声学重建与最低WER，参数量不足双塔基线一半，下游语音理解任务上展现强语义表征。代码与权重已开源。
- **关键技术点**：** 传统低码率编解码器难以兼顾声学重建与语义保真；双塔架构虽缓解冲突却带来参数冗余。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [10 Ontology-based Target Sound Extraction](https://arxiv.org/abs/2609.00752)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：目标声音提取（TSE）旨在给定语义查询从混合声中分离目标音源。现有TSE系统锚定于逐一声类标签的固定类表示，无法利用层级组织关系。本文提出ontology-based TSE新任务：单一模型可提取声音本体中任意层级的声音（从cat、dog到animal）。作者提出覆盖AudioSet派生本体全部节点的可学习类别嵌入表，并用Cophenetic相关系数（CPCC）损失约束嵌入距离与本体最短路径距离一
- **关键技术点**：** 现有TSE使用one-hot类标签，各类别嵌入彼此独立，无法编码类间上下位关系，模型只能在训练见过的类别上工作。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 Sensing Bone-Conducted Speech with Earbuds](https://arxiv.org/abs/2609.02165)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-02
- **一句话贡献**：针对无线入耳式耳机在噪声环境下自身语音（OV）采集困难的问题，本文系统分析了佩戴者语音诱发的耳机壳振动（骨导语音）的频谱与空间特性。基于 Anker P3i 与 A20i 两款耳机、17 名受试者的实测数据，发现该振动呈显著低通特性：400 Hz 以上以约 -93 dB/decade 滚降，100-400 Hz 为高功率频段（平均约 530 µg）。空间分析表明耳机主要沿耳道口进出方向振动，且个体
- **关键技术点**：** 骨导语音可提升 TWS 在噪声下的自语音采集，但耳机壳振动的带宽与空间特性缺乏系统测量，致使加速度计轴数选择、安装方向以及单轴/三轴方案缺乏设计依据，现有多项研究用法不一、未达共识。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 VoxReason: Listener-Free Evaluation of Source-Grounded Speech Planning Before Synthesis](https://arxiv.org/abs/2609.03203)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-02
- **一句话贡献**：表达性语音系统在合成前就决定情感、音高、能量、语速等，但这段隐藏的"说话计划"一旦编码进波形就难以审计，模型可能"听起来对但理由错了"。VoxReason把该决策升级为第一类可验证预测：输出带源引用的说话计划，由确定性验证器检查引用合法性、槽位一致性与反事实局部性。在1440条RAVDESS样本上，去掉源记录使7B模型引用必需分下降0.488；定位SFT+CF修复把计划槽准确率/反事实一致性从0.
- **关键技术点**：** 现有上下文感知TTS评估都只对最终波形或自由文本解释打分，很少暴露"哪条源记录授权了哪个交付字段"这一上游决策。作者主张把评分前移到合成之前，以受控干预检测源使用而非风格。
- **主要指标**：
- **代码**：https://github.com/MENGZHEGENG/voxreason | **Demo**：暂无

---
## [9 Is Semantics Enough for Speech Mean Opinion Score Prediction?](https://arxiv.org/abs/2609.03283)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：本文系统回答"语义表征是否足以支撑语音MOS预测"。对SSL模型、纯声学NAC、统一NAC三类表征进行首次大规模对比，在冻结编码器与全微调两种协议下于BVCC及两个OOD数据集上评测。"语义+声学"协同表征（尤其Xcodec-wavlm）在域内达最高上限（微调SRCC 0.882），而纯SSL在跨语言场景泛化更优（BC2019上wavlm_base零样本SRCC 0.674）。结论：语义不足够，需
- **关键技术点**：** 现有SOTA MOS预测器几乎都以SSL（Wav2Vec 2.0、HuBERT、WavLM）为特征骨干，其掩码预测预训练目标天然鼓励抽象高层语义、舍弃噪声与波形失真等声学细节，给自然度MOS预测施加表征上限。既往工作未在冻结编码器下探测表征固有信息含量，也未系统对比语义与声学两大范式。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 Masked Autoregressive Speech Enhancement with Continuous Neural Audio Codec Representations](https://arxiv.org/abs/2609.03940)

- **方向**：语音前端 | **子方向**：Codec | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：针对基于NAC的SE研究大多依赖离散token、且缺少对不同解码策略权衡的系统研究，本文提出掩码自回归语音增强（MARSE），在连续NAC编码器输出上把迭代解码建模为分块自回归概率过程。在相同Conformer、相同DAC与训练设置下比较因果/非因果随机/非因果oracle三种解码策略。MARSE性能与开销介于C-NAR与C-AR之间，可灵活权衡。
- **关键技术点**：** 基于token的SE因离散量化损失对音质与可懂度至关重要的声学细节；近期研究证明使用DAC量化前的连续表示为音质与可懂度带来显著提升。同时token类方法通常各自固定一种解码策略、实验设置各异，缺少对"解码策略"维度的公平对比。
- **主要指标**：
- **代码**：https://yotofujita.github.io/marse | **Demo**：https://yotofujita.github.io/marse

---
## [7 Beyond .WAV: Design and Software Verification of VocalCap, a Traceable Browser-Based Audio Capture System for Vocal Biomarker Research](https://arxiv.org/abs/2609.03320)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：远程语音采集往往只交付一个音频文件，缺少"信号如何被捕获、传输、处理与验收"的证据。VocalCap为受试者自助式语音采集设计机构可控浏览器系统，每个录音同时保留浏览器原生对象、客户端无损Float32 WAV与服务端规范单声道PCM16 WAV，并关联完整性与转换溯源证据。软件验证证实40ms连续性边界在8/16/44.1/48kHz正确生效，活动声道选择RMS偏差超低频低于0.001dB。
- **关键技术点**：** 语音生物标志物研究要求把采集技术验证与下游推断分开，远程自助采集时无受训人员在场，权限处理、编码与持久化均不可见。同类系统各覆盖部分环节，但没有一个把双工件配对、逐字节校验、版本化规范化等整合为单一验收契约。SPIRA项目（6000+语音捐献者）的空白录音问题直接催生本设计。 **系统设计：** Flask服务端+移动优先Web前端，协议通用任务执行器（麦克风测试、持续元音、标准句、计数、自发语音5任务）。同一MediaStream并行馈入MediaRecorder（原生对象N）与AudioWorklet（Float32 WAV无损L）双路径。采集记录含完整清单M（SHA-256）、采集
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 Discriminative Flow Matching: Beyond Time-Conditioning in Generative Restoration via Flow-State Representations](https://arxiv.org/abs/2609.04525)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：条件流匹配（CFM）以显式时间坐标 t 同时驱动插值路径与速度网络的条件化，但恢复任务中源与目标分布统计相关（目标信号内嵌于含噪输入），同一 t 可能对应不同的退化程度与传输进度，时间条件存在固有歧义。本文提出判别式流状态假设并据此提出判别式流匹配（DFM）：用冻结判别式增强模型编码器提取的判别式流状态表征（DFSR）替代显式时间 t 条件化速度网络，并实现样本自适应推理。在 Interspeec
- **关键技术点**：** CFM 的目标向量场随时间变化，故需用 t 条件化速度网络。标准 OT-CFM 中源与目标统计独立，流状态 S(p_t)=W_2(p_t,p_1) 满足线性关系，t 是传输进度的可靠代理。但恢复任务初值 x_0=αx_1+βν，命题 2 证明存在不同的 (α,β,t) 组合产生相同边际分布，即同一状态可在不同 t 达成，全局插值坐标无法无歧义描述传输进度；近期工作（如 ARF）直接移除时间条件化，又丢失按进度自适应调节速度的机制。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 ProLombard: Structured Multi-Scale Modeling for Normal-to-Lombard Speech Conversion](https://arxiv.org/abs/2609.04828)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-04
- **一句话贡献**：常规语音到 Lombard 语音转换（N2L）旨在噪声环境下提升语音可懂度，但现有方法仅在语句级或帧级建模 Lombard 效应，忽略了其层级结构及其与说话人身份、音素级内容纠缠的本质，导致说话人表征中 Lombard 泄漏、内容特征分离不彻底。本文提出 ProLombard，一种结构化多尺度 N2L 框架，在语句级、音素级和帧级三个时间尺度上显式建模 Lombard 效应：设计对齐说话人编码器（
- **关键技术点**：** 现有解耦式 N2L 方法（如 PGD-N2L、LombardTokenizer）面临两大瓶颈。其一为 Lombard-说话人纠缠：预训练说话人确认模型以身份判别为目标而非去除风格变化，导致 Lombard 信息残留在说话人嵌入中（Lombard 泄漏）；对抗式或互信息式解耦缺少显式跨风格对齐监督，在说话人稀缺的低资源场景下难以兼顾身份保持与解耦。其二为 Lombard-内容纠缠：Lombard 效应随音素变化（共振峰位移、元音时长延长），帧级解耦无法覆盖；现有音素级方法多用外部模型分割后做简单池化，分割边界不可靠且会损伤内容保真。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 KanAdapter: A Kolmogorov-Arnold Network-based Plug-and-Play Module for Efficient Fine-tuning of Foundation Speech Models](https://arxiv.org/abs/2609.05281)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-04
- **一句话贡献**：全文微调自监督（SSL）语音大模型计算开销巨大，而现有参数高效微调（PEFT）方法主要依赖 MLP 适配器，其固定激活函数在紧凑参数预算下表征能力受限。本文提出 KanAdapter，一种基于 Group-Rational KAN（GR-KAN）的即插即用适配器框架，采用并行瓶颈设计，在冻结的 Transformer 编码器旁插入可训练 GR-KAN 分支，并从预训练 MLP 层迁移权重实现稳定初
- **关键技术点**：** 现有 PEFT 方法应用到语音 SSL 模型时建模能力受限：LoRA 本质是无非线性激活的线性低秩分解，难以刻画伪造痕迹、情感分布等复杂语音特征；AdaptFormer 的 MLP 瓶颈使用固定激活，表达力不足。针对语音 SSL 的 PEFT 研究仍少见，将 KAN 类可学习激活模块用作适配器此前尚属空白。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [13 Tracing Audio Grounding and Answer Selection in Audio LLMs](https://arxiv.org/abs/2609.04637)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-04
- **一句话贡献**：音频大语言模型（Audio LLM）常依赖文本线索或语言先验答题而非真实听音，即便音频信息极度缺乏时仍能保持较高 AudioQA 准确率。现有应对方法用"无法仅凭文本作答"的数据训练，精度确有提升，但模型内部发生了什么改变仍不清晰。本文对 Qwen2-Audio 与 Qwen2.5-Omni 两个模型、在零样本（ZS）与 LoRA 微调（FT）状态下开展机制可解释性分析，回答"训练如何增强音频证据
- **关键技术点**：** 现有评测关注预测是否真正由声学证据支撑（幻觉、模态冲突、证据缺失），但已有研究指出模型可在几乎无声学证据时保持高 AudioQA 性能，说明基准精度与实际听音之间存鸿沟。机制层面工作虽已探究音频信息在模型中的表示与传播位置，却未说明训练如何改变音频信息最终驱动答案选择的过程。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 Cleaner Speech, Weaker Generalization: Revisiting Pitt-Derived Benchmarks for Alzheimer's Disease Detection](https://arxiv.org/abs/2609.00276)

- **方向**：语音大模型 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-01
- **一句话贡献**：基于语音的阿尔茨海默病（AD）检测日益依赖Pitt语料库的增强版本。本文系统重访预处理与数据整理对AD检测的副作用：增强数据集上域内性能提升但跨域稳健性下降；训练/测试匹配增强只能缓解无法消除退化。LALM同样敏感，增强数据诱发更强的类别不平衡与预测偏移。结论提示"更干净"的语音数据集对真实世界AD检测未必更可靠。
- **关键技术点**：** AD语音检测常把语音增强、样本筛选等当作有利预处理，但这些转换可能在域内制造虚高成绩。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 StrixAE: An Intelligent Agent for Audio Enhancement under Complex Distortion Coupling in Real-World Scenarios](https://arxiv.org/abs/2609.03414)

- **方向**：语音前端 | **子方向**：Other | **评分**：8/10 | **日期**：2026-09-03
- **一句话贡献**：StrixAE面向真实世界中噪声、混响、干扰说话人等多失真耦合与个性化增强并存的难题，提出以MLLM（Audio-Reasoner）为控制器、编排多个开源专家增强模型作为工具的音频增强智能体范式。采用"CoT监督微调+音频感知强化学习（APRL）"两阶段训练。在真实盲测集上全面超越TF-GridNet等开源方法，多数指标优于部分闭源方案。
- **关键技术点**：** 现有音频增强要么单任务方法、要么全一模型，二者均无法同时应对真实场景未知组合的复合失真与按人定制需求；标注含混合失真的配对数据稀缺，且缺乏统一基准评测泛化性。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 Does EEG Foundation Models Transfer to Speech? A Benchmark on Overt and Imagined Speech Decoding](https://arxiv.org/abs/2607.27268)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-29
- **一句话贡献**：EEG基础模型（LaBraM在~2,500小时EEG上预训练，EEGMamba在~16,000小时上预训练）在运动imagery、癫痫检测、睡眠分期等任务上显著超越CNN基线，但其向语音解码的迁移效果尚未被系统验证。本文首次对EEG基础模型与卷积基线在语音解码任务上进行系统基准测试，覆盖overt、covert和imagined speech三种模式。在UGR-MINDVOICE数据集上，16K参
- **关键技术点**：** EEG基础模型在运动imagery、癫痫检测等任务上表现优异，但语音解码涉及腹侧感觉运动皮层和颞上回的皮层动态，与基础模型预训练语料（静息态、运动imagery、临床事件）主导的范式有本质差异。现有研究仅在EEGMamba中将BCI Competition 2020 Track 3作为6个下游任务之一进行了评估，缺乏针对语音解码的受控比较。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Model-Agnostic Meta-Learning Initialization for Distributed Multichannel Active Noise Control](https://arxiv.org/abs/2607.29117)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-07-31
- **一句话贡献**：分布式多通道主动噪声控制（DMCANC）是大面积降噪的可扩展框架，但现有方法依赖零或随机初始化，导致自适应滤波器收敛缓慢，限制了节点间协作效率。本文提出基于模型无关元学习（MAML）的初始化策略，通过聚合不同节点和声学环境的异构声学特征（主通道和次通道脉冲响应），学习可泛化的初始控制滤波器系数。在6节点DMCANC系统上验证，使用宽带噪声（100-2000Hz多种范围）进行MAML训练。结果表明该
- **关键技术点**：** DMCANC系统中多个节点独立运行本地单通道ANC控制器并通过间歇通信交换信息实现全局控制。现有DMCANC实现依赖零或随机初始化，在时变噪声和大规模系统中收敛缓慢。自适应滤波器初始化对ANC系统收敛行为至关重要，但DMCANC领域此前未系统研究。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 REIMU: Efficient Heterogeneous Hierarchical Reasoning for SSL-Based Speech Deepfake Detection](https://arxiv.org/abs/2608.00857)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-08-04
- **一句话贡献**：基于自监督学习（SSL）的语音深度伪造检测中，下游骨干网络通常通过单次前向处理SSL表示。本文系统研究循环层次推理对检测性能的影响，比较单次前向、权重共享循环、同质HRM和异构HRM四种架构。异构HRM在高层次模块使用MHSA（多头自注意力），低层次模块使用线性注意力（GDN2），在保持竞争力的同时减少10.8%的下游参数。代码开源。
- **关键技术点**：** SSL模型（如WavLM、HuBERT）在语音deepfake检测中取得进展，但下游骨干网络的设计选择缺乏系统研究。单次前向（single forward pass）能否充分利用SSL表示的多层次信息？循环和层次推理是否带来提升？这些问题尚未被系统回答。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 KVAE: Family of Tokenizers for Multimodal Generative Models](https://arxiv.org/abs/2608.05798)

- **方向**：多模态tokenizer | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-06
- **一句话贡献**：LDM的生成质量高度依赖tokenizer的latent空间特性，但重建指标无法可靠预测下游生成性能。KVAE系列提出面向音频、图像和视频的统一tokenizer方案：KVAE-Audio是48kHz全频带连续音频tokenizer（50Hz latent, 64通道）；KVAE-3D提供4×16×16和4×8×8两种因果视频tokenizer；KVAE-2D为8×压缩的32通道图像tokeniz
- **关键技术点**：** 视觉tokenizer的latent空间特性（diffusability）直接影响扩散模型的训练动态和生成质量，但重建指标（PSNR等）与下游生成性能之间存在reconstruction-generation dilemma。现有开源tokenizer如Wan-2.2（48通道）×16×16）、HunyuanVideo-1.5（32通道×16×16）在压缩率和通道数选择上各有局限。
- **主要指标**：
- **代码**：https://github.com/kandinskylab/kvae | **Demo**：暂无

---
## [6 Explicit and Stable Pseudospectral Time-Domain Method for Föppl-von Kármán Equations](https://arxiv.org/abs/2608.06139)

- **方向**：声学模拟 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-06
- **一句话贡献**：模态合成是乐器动力学模拟的常用技术，但Föppl-von Kármán板方程的非线性项导致模态域中四阶张量计算代价极高（O(N_x^4)）。本文提出伪谱时域方法：在空域网格上计算乘积项（O(N_x^2 log N_x)），在模态域中精确计算空间导数，通过离散正弦/余弦变换施简支边界条件，并利用标量辅助变量技术实现显式稳定时间积分。数值实验在44.1kHz采样率下验证了能量守恒到机器精度，且漂移调控
- **关键技术点**：** Föppl-von Kármán板方程的非线性耦合由四阶张量描述，纯模态方法需要评估O(M_x^4)个耦合项，在GPU上才能实现实时。现有数值方法（Kirby & Yosibash）使用隐式迭代方案，计算效率低。
- **主要指标**：
- **代码**：https://github.com/victorzheleznov/fa2026 | **Demo**：https://victorzheleznov.github.io/fa2026

---
## [2 MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection](https://arxiv.org/abs/2608.09593)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：语音合成和音频生成的最新进展使得高保真声学伪造低成本且难以归因，实现了语音和背景音频可被独立操纵的现实攻击场景。但现有研究要么关注视觉操纵，要么孤立处理语音检测，或将语音和非语音音频混为一谈。MADBench 是首个将语音和环境音频视为不同声学组件的基准，支持组件感知的音频深度伪造检测评估。实验揭示：环境音频操纵比合成语音更容易被通用编码器检测；现有预训练检测器对两种声学组件均失败；操纵环境音频不
- **关键技术点**：** 真实攻击场景中，攻击者可独立操纵视频中的语音轨道和背景音频，但现有检测基准将语音和背景音频视为单一标签，忽视了两者不同的伪造特征和检测难度。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 AudioMap: Cloze-and-Choice Reinforcement Learning for Time-Aware Dense Audio Captioning](https://arxiv.org/abs/2608.09559)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：时间感知密集音频描述（TDAC）旨在生成具有精确时间边界的多个细粒度音频属性。现有方法主要依赖监督微调，性能次优。AudioMap 提出基于填空-选择强化学习（RL）的 TDAC 框架，引入证据充分性奖励（ESR）的不对称分层评分机制以提高细粒度准确性和描述丰富性，以及事件条件时间奖励（ECTR）通过时间 IoU 将时间戳绑定到事件语义。构建首个时间感知细粒度音频描述数据集 AudioMapCap
- **关键技术点**：** TDAC 需要同时生成细粒度多属性描述和精确时间边界，现有监督微调方法难以优化两个目标。现有奖励函数过于粗糙，无法细粒度监督多事件、多属性、多关系描述；自由格式 caption 的时间监督困难。
- **主要指标**：
- **代码**：https://github.com/ryysayhi/AudioMap | **Demo**：暂无

---
## [5 Dynamic Clustering for Cross-Segment Permutation Alignment in Long Speech Separation](https://arxiv.org/abs/2608.09451)

- **方向**：语音大模型（语音前端） | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：长语音分离通常采用分段-分离-拼接范式，其挑战在于预测跨段排列。该工作提出免训练的动态聚类方法，使用说话人 embedding 参考池进行跨段排列对齐。方法基于当前段 embedding 与参考池的余弦相似度预测排列，通过保留与现有参考整体余弦相似度最具代表性的说话人 embedding 来更新参考池。作为与现有分离模型兼容的即插即用后处理模块，在密集和稀疏长语音场景中优于现有方法，尤其在具有扩展
- **关键技术点**：** 长语音分离中，录音被分割为短段独立处理，然后拼接。跨段排列对齐（segment 1 的说话人 A 对应 segment 2 的哪个输出）是关键挑战，尤其在稀疏场景中说话人可能长时间不出现。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 Neural Array-Generic Direction-of-Arrival Estimation Exploiting Array Transfer Functions](https://arxiv.org/abs/2608.09425)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：DOA 估计是多通道音频处理的关键组件，但许多深度学习方法与训练时使用的麦克风阵列绑定，对未见设备泛化差。该工作提出阵列通用神经 DOA 估计框架，使用测量或模拟的复值方向阵列传递函数（ATF）匹配真实多麦克风设备。使用独立卷积编码器处理多通道频谱图和 ATF 元数据，通过交叉注意力融合表示，使用多源笛卡尔向量输出预测源方向。在混响和扩散噪声下的模拟 2D 和 3D 定位任务中，方法泛化到未见阵列
- **关键技术点**：** 现有神经 DOA 方法通常针对特定阵列配置训练，当部署到不同阵列（如不同麦克风数量、几何形状）时性能严重下降，需要重新训练。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation](https://arxiv.org/abs/2608.09288)

- **方向**：语音大模型（语音前端） | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：真实世界条件下音视频语音增强因不可靠的视觉输入和缺乏大规模真实声学条件训练数据而具有挑战性。现有方法通常将视觉特征直接融合到分离网络中，使其对退化视觉信号脆弱。DAVE 提出解耦音视频增强框架：构建 DAVE-Corpus（219,411 个混合样本，从公共会议语料库通过组合声学增强生成），引入渐进多目标优化策略联合改善语音分离、可懂度、说话人身份保持和感知质量，发展认证选择性增强链（仅对无参考分
- **关键技术点**：** 真实世界中视觉输入可能被遮挡、模糊或低光，现有方法将视觉特征直接融合到分离网络，使系统在视觉退化时性能严重下降。同时缺乏大规模真实声学条件的训练数据。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [10 Structured Phonological Representations for Audio-Articulatory rtMRI Speech Classification](https://arxiv.org/abs/2608.09767)

- **方向**：语音大模型（语音前端） | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-10
- **一句话贡献**：实时 MRI 可以观察语音中的声道发音，但将这些发音模式映射到音系类别仍具挑战性。该工作研究 PhonoQ（一个训练识别结构音系特征的音频模型）是否为音频-发音建模提供有用信息。从 PhonoQ 的 Conformer 模块提取表示（其训练受方式、位置、发声、元音特征监督），使用发音轮廓与同步音频特征结合，对比 WavLM-large 和 HuBERT-large 基线。在未见语音和未见说话人设置
- **关键技术点**：** rtMRI 提供了高时间分辨率（~80fps）的声道发音观测，但发音数据维度高、标注困难，映射到音系类别需要有效的特征表示。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 DuplexWorld: Can Voice Agents Help You Get Through the Day?](https://arxiv.org/abs/2608.10716)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-11
- **一句话贡献**：语音到语音（S2S）语音代理越来越多地集成到企业中用于客户服务和日常陪伴。DuplexWorld 引入六个世界（银行、保险、旅行、医疗保健、物流和路径规划），共 156 个场景和 350+ 小时对话，全面评估语音代理的代理能力、对话能力和语音自然度。评估显示即使最佳语音代理在三方面仍有巨大提升空间：Pass@1 仅 0.490，轮次切换 0.653，DNSMOS 3.378。
- **关键技术点**：** 现有语音代理基准主要测试代理工具调用能力，未充分覆盖日常活动的对话多样性，也未测试代理在数据库操作之外的多步骤任务协助能力。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 DINO-A: Adapting Self-Distillation Vision Transformers to General Audio Representation Learning](https://arxiv.org/abs/2608.10659)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-11
- **一句话贡献**：DINO-A 将视觉自蒸馏方法 DINO 适配到通用音频表示学习。保留 DINO 的多裁剪、EMA 教师和高维投影，仅将输入模态和增强替换为 log-mel 频谱图和 BYOL-A v2 增强块。在 FSD50K 上预训练三种骨干（ViT 8×8, ViT 16×16, 卷积编码器），在 ESC-50、Speech Commands v2、UrbanSound8K 和 GTZAN 上用线性探测评估
- **关键技术点**：** DINO 已成为视觉自监督学习的标准方法，但之前没有工作将标准 DINO 以 BYOL-A 将 BYOL 带到音频的方式系统性地适配到通用音频分类。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 In Defense of Using Worst-case Privacy Disclosure as Privacy Evaluation Metric of Voice Anonymization](https://arxiv.org/abs/2608.10318)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-11
- **一句话贡献**：语音匿名化社区主要使用 EER 评估语音身份保护性能，但 EER 最优系统在 LLR 空间中可能无法正确评估信息泄漏。该论文为 privacy-ZEBRA 框架（最坏情况隐私泄露评估）进行辩护，基于 Shannon 完美保密概念解释 EER 的局限性，展示基于排名的指标如何等价于完美保密原则。在模拟数据和 VoicePrivacy Challenge 数据上展示结果，为语音匿名化评估提供理论指导。
- **关键技术点**：** 语音匿名化主要使用 EER（等错误率）评估隐私保护，但 EER 衡量的是平均性能，可能掩盖单个说话人的信息泄露。privacy-ZEBRA 框架提出最坏情况评估，但其理论基础和与其他指标的关系尚未被充分解释。
- **主要指标**：
- **代码**：https://github.com/nii-yamagishilab/paper-archive-spsc2026-privacy-llr | **Demo**：暂无

---
## [8 Infant Audio Understanding via Whisper + LoRA](https://arxiv.org/abs/2608.11587)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-12
- **一句话贡献**：本文提出基于Whisper encoder + LoRA微调的方法，用于婴儿中心音频理解任务（如婴儿哭声检测、情感状态分类等）。创新性地设计了因子化说话人token机制，将共享层级token与家族特定偏移结合，实现跨家族的婴儿音频理解。采用多层级音频标记和序列级平滑损失函数来提升模型性能。
- **关键技术点**：** 婴儿音频理解面临数据稀缺和跨个体泛化两大挑战：婴儿音频数据收集困难且标注成本高，不同婴儿的发声特征差异巨大，导致模型在未见过的婴儿上性能显著下降。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model](https://arxiv.org/abs/2608.13101)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-13
- **一句话贡献**：自动口语评估（ASA）需要同时评估语音表达（怎么说）和内容（说什么），现有语音 LLM 方法依赖大规模多模态骨干网络，计算开销大且缺乏对声学/内容信息贡献的分离分析。CASA 提出双分支架构，将 Whisper-medium 编码器（声学分支，LoRA 适配）与 Qwen3.5-2B（内容分支）结合，在 Speak & Improve Corpus 2025 上以 3.13B 总参数量（约 NTN
- **关键技术点**：** 口语评估中语音表达（流利度、发音）和内容（词汇、语法、主题发展）是多源交互的证据，现有方法要么使用大参数语音 LLM 但计算开销大且缺乏可解释性，要么依赖多 grader 组合和手工特征增加系统复杂度。现有实现均未开源，限制了可重复性和进一步研究。
- **主要指标**：
- **代码**：https://github.com/aalto-speech/casa | **Demo**：暂无

---
## [9 A Regularized Block Diagonal RLS Algorithm for Acoustic Echo Cancellation](https://arxiv.org/abs/2608.20693)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-24
- **一句话贡献**：针对经典RLS算法计算复杂度高达O(N²)、且长滤波器下数值不稳定而难以在资源受限设备上实时部署的问题，本文提出正则化分块对角RLS算法（RBD-RLS）。该算法将N阶自相关矩阵近似为M个L×L分块对角结构（N=ML），把大规模矩阵递归更新分解为互相独立可并行的子块运算，复杂度降至O(NL)；同时对每个子块施加Tikhonov正则化以保证初始阶段数值稳定。在N=512、最优配置（λ=0.9999,
- **关键技术点**：** AEC需用自适应滤波实时估计回声路径h(n)。NLMS等LMS族复杂度仅O(N)，但输入强相关（如语音）时收敛慢；RLS利用输入二阶统计量，收敛最优，但每步更新P(n)含O(N²)矩阵运算，滤波器阶数N通常为512~2048，且P(n)递归中减法易在有限精度下破坏正定性，导致增益向量发散。FRLS虽将复杂度降至O(N)，但数值不稳定；RLS-DCD数值稳健，却仍隐含O(N²)的数据拷贝开销，通用处理器上延迟不可接受。上述矛盾促使作者寻求兼顾收敛、复杂度与数值稳定性的折中方案。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 Multi-Task Learning for Non-Canonical Phoneme Recognition via Articulatory Feature Decomposition](https://arxiv.org/abs/2608.22273)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-25
- **一句话贡献**：针对病理/非标准语音中系统性的发音偏差与临床标注数据稀缺，本文将音素识别从"原子类别分类"重构为发音特征维度（manner/place/voicing/height 等）的多任务预测，提出基于 WavLM 的分层多任务（HMTL）架构，通过 cross-attention 融合发音特征表示后经 BiLSTM 与 CTC 输出音素序列。结合 Momentum Pseudo-Labeling 半监督与
- **关键技术点**：** 病理/非标准语音（如运动言语障碍、儿童言语失用）音素识别 PER 高达 42%-69%。现有模型在健康语音上训练，会把非标准发音"自动纠正"为最近的规范音素；且把音素当作原子标签无法刻画"部分特征保留、部分偏离"的系统性错误结构。病理语音标注稀缺且标注者间一致性差，故用 L2-ARCTIC 口音语音作为病理发音的代理。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 LipsAM: Lipschitz-continuous Neural Networks for Convergent Plug-and-Play Audio Signal Recovery](https://arxiv.org/abs/2608.23038)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-25
- **一句话贡献**：传统语音 DNN 将复数 STFT 的幅度与相位分开处理，由于 sign 函数在零点不连续，此类网络即使幅度部分 Lipschitz 连续，整体也必然不连续，无法纳入现有 Lipschitz 理论框架。本文推导了幅度修正器（AM）满足 Lipschitz 连续性的充要条件（定义 LipsAM），并给出 LipsAM-E、LipsAM-M（时频掩蔽）两类可证连续的架构及 Lipschitz 常数紧凑
- **关键技术点**：** 现有 Lipschitz 网络构造（谱归一化、正则化、结构法）均针对实值图像网络；而语音常用的复数谱网络通过幅度映射加 sign(z) 分离处理幅度相位，sign(z) 在 z=0 处不连续，导致即使幅度映射本身 Lipschitz 连续，整体映射仍非 Lipschitz。这阻碍了基于 Lipschitz 条件的 PnP 收敛保证在语音中的应用。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 EXAM$^2$: Extending Audio Understanding in Multilingual and Multimodal Analysis](https://arxiv.org/abs/2608.23758)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：本文提出多语言多模态音频理解基准 EXAM²，系统评估现有音频语言模型在多语言、多模态理解上的表现，发现模型存在明显的多语言跨模态理解差距。作者进一步构建微调的 Gemma3n-EXAM² 模型，其性能较基线显著提升，为多语言音频理解研究提供了新的评测工具与改进方向。核心价值在于填补了现有基准对非英语语言与多模态结合场景覆盖不足的空白。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 GRGA: Graph-based Retrieval-Generation Agent for Long-form Audio Meeting Understanding](https://arxiv.org/abs/2608.24048)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：针对长音频会议理解任务中问答数据集稀缺、现有语音模型声学信息丢失与长期记忆能力差的问题，本文构建了 LongAudioQA 数据集，并提出基于图的检索-生成智能体（GRGA）。GRGA 利用智能体规划实现检索与答案生成，将语义信息组织为图结构以缓解长期记忆与信息丢失问题。该工作已被 ACL Findings 2026 接收，为长会议场景下的语音理解提供了新的数据资源与建模范式。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 Visually-Guided Spatial Audio Generation for 360° In-the-Wild Speech Scenes](https://arxiv.org/abs/2608.24579)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：面向野外 360° 语音场景中空间音频采集设备受限、质量有限的问题，本文提出视觉引导的第一阶声场（FOA）语音空间化方法，并构建 YT-SPEECH 数据集。采用 Localizer-Renderer 框架，从视觉信息估计声源方向并重建定向 FOA 信号，实用地提升了音频相关性能。该工作已被 INTERSPEECH 2026 接收。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 Array-Agnostic Ambisonics Encoding via Diffusion Posterior Sampling](https://arxiv.org/abs/2608.24558)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：现有 Ambisonics 编码方案受固定麦克风阵列布局限制。本文提出生成式框架 ADEPS（Array-agnostic Diffusion Encoding via Posterior Sampling），将物理采集模型嵌入扩散后验采样推理过程，从而补偿阵列失真并实现对任意麦克风阵列的零样本编码，性能优于传统基线。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 AudioSpan: Spanning the Duration and Depth of Audio Comprehension](https://arxiv.org/abs/2608.26431)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：现有音频理解基准大多在数秒级短片段上评测，得分快速饱和；近期长音频类基准虽把时长拉长，评测方式却仍沿用短音频的抽取式问答，未触及认知深度。本文提出AudioSpan：将音频时长从10分钟跨度到2小时以上，配套3,240道题，划分为知觉、理解、推理三个认知层级。题目由两条路径生成——Native QA从音频真实内容取材，每道题同时给出四选一选择题和按详细评分表打分的开放题；Anchor QA则向音频
- **关键技术点**：** 现有基准（秒级剪辑QA）上分数饱和、模型趋同，说明短片段测试已丧失区分度；近期长改工作虽在时长上突破，评测仍按"把长音频当短音频"的抽取式问答处理，既没有覆盖跨数小时的完整内容流，也没有触及深于事实检索的认知层次。同时LALM正走向多模态（语音、声音、音乐全覆盖），训练目标与评测方式脱节。AudioSpan同时扩展"时长"与"认知深度"两个轴：时长轴检验长上下文能力，深度轴检验从简单感知到复杂推理的认知全过程。
- **主要指标**：
- **代码**：https://huggingface.co/datasets/holvan/AudioSpan | **Demo**：暂无

---
## [2 GAN-based Joint Dereverberation and Directional Filtering](https://arxiv.org/abs/2608.26403)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：神经方向滤波（NDF）可在紧凑阵列上按期望指向性模式重建虚拟指向性麦克风（VDM）信号，但强混响会破坏空间线索，而一阶心形的方向性指数仅约4.8 dB、难以抑制混响能量。本文提出NDDF，将去混响与方向滤波统一为单一学习问题，直接从阵列输入重建去混响VDM信号，并用判别式与GAN两种范式实现。实验表明NDDF全面超越级联基线（一阶目标、RT60=0.2s时PESQ 4.34 vs 3.08，fwS
- **关键技术点**：** NDF通过学习理想指向性麦克风的输入输出行为，可在小孔径阵列上获得高指向、频率无关的响应，但高指向对应窄主瓣，而X-Y立体声等录音格式要求固定的一阶心形（DI仅约4.8 dB），在强混响下无法抑制反射能量，重建的VDM混响严重、空间线索被掩盖。级联"去混响前端+NDF"流水线逐级独立优化，各级最优未必导致整体最优，因而需要统一公式同时处理去混响与方向滤波。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [3 Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition](https://arxiv.org/abs/2608.26213)

- **方向**：语音前端 | **子方向**：ASR | **评分**：7/10 | **日期**：2026-08-26
- **一句话贡献**：LLM驱动的音视频语音识别（AVSR）在噪声场景下具有鲁棒性，但固定强度的对比解码（CD）面临"鲁棒性-干净语音"权衡：强干预利于恶劣噪声却会在干净条件下过度纠正可靠预测。本文提出基于可靠性感知的CD自适应缩放：在同一LLM内分别以"纯音频"与"音频+视觉"条件化作为弱/强对比分支，并按token依据注意力动态与跨分支预测分歧度动态调制对比强度，三者经乘法融合得到权重因子。在LRS3上，该方法使L
- **关键技术点**：** 近年LLM式AVSR（如Llama-AVSR）借助大模型的语音先验在噪声下表现优异，但模型对音频模态存在过度依赖：声学输入严重退化时仍倾向沿用音频线索，而视觉信息本可纠正这些错误。对比解码原本是让弱模型与强模型在推理时互相对比以稳定LLM生成。本文将CD引入AVSR：以同一模型的音频条件化为Amateur、音频+视觉条件化为Expert。任何固定对比权重都无法同时适配干净与强噪声环境（robustness-clean speech trade-off），这是本文要解决的核心问题。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction](https://arxiv.org/abs/2608.26005)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：面向实时语音交互中语音大模型（SLM）缺乏记忆的痛点，本文提出 VoiceMem"双脑流式记忆"架构，将短时工作记忆与长期记忆结合，构建了完整的记忆感知 SLM 训练、评估与部署流水线。实验显示其在记忆准确性、情感个性化与实时性上均有显著优势，为实时语音交互提供了实用的记忆基础。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 A Training-Free Proactive Defense Against Partial Speech Manipulation via Self-Embedding Steganography](https://arxiv.org/abs/2608.25285)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：部分（局部）语音被替换、拼接式的深度伪造难以被整段检测器捕获。本文提出一种无需训练的主动防御方法，将自嵌入策略与现有音频隐写术结合，在待保护语音中内嵌自身摘要，解码器据此修复被操纵区域从而实现操纵检测。该方法无需重新训练模型、数据效率高，可与被动检测互补。已被 Interspeech 2026 接收。
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 When Text Misleads: Inconsistent-Aware Reasoning for Audio-Grounded Dialogue](https://arxiv.org/abs/2608.27176)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：本文针对语音对话理解中的隐藏失败模式——模型仅凭转写文本即可作答，并未真正把预测建立在语音声学证据上（模态塌缩）。作者将文本与声学线索相矛盾的场景形式化为跨模态不一致，并据此构建受控评测基准ContraTalk，包含501道多选题，覆盖互动行为、情绪状态、对话行为、社会立场和会话意图五个话语维度，其中333道冲突题与168道一致题。同时提出代理式推理框架Audio Twin，将语音转写对齐的声学线
- **关键技术点**：** 当前多模态评测普遍允许模态捷径：在VQA和对话情绪识别中已有"语言先验主导"的共识，近期语音语言模型研究也常出现仅凭词汇或数据集先验即获高分的现象。当基准可仅由单模态求解时，另一模态在功能上可被忽略，导致模态塌缩。现有基准大多评估模态"协同/互补"情形，几乎没有把"解决显式跨模态冲突"作为推理前提，因此作者将跨模态不一致定义为一条独立且未充分探索的评测轴。仅靠隐式多模态融合不够，模型需自行判定转写推理是否充分、定位相关声学证据并在文本与语音分歧时比较竞争解释。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [4 Mapping Written Words to Spoken Words in a Different Language Using Only Visual Grounding](https://arxiv.org/abs/2608.26925)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-27
- **一句话贡献**：针对低资源语言连语音采集都很困难的现状，本文研究如何仅凭视觉grounding（图像配印地语口语描述）将英文书面关键词映射到印地语语音中对应的词段，全程无需目标语言转录、无需训练任何神经网络。方法把无监督词发现与视觉监督结合：用现成的图像描述系统自动生成英文caption作为弱文本监督，据此把话语划分为正/负两类，再基于HuBERT自监督表征进行对齐，并通过interval piling聚合、减去
- **关键技术点**：** 世界上绝大多数语言缺乏文本资源和书写系统，难以构建传统语音技术。项目Vaani正通过让说话人描述图像来采集语音，但此类视觉grounding数据缺乏语音-文字对应关系。此前工作用单一图像tagger为注意力式音频-关键词神经网络提供弱监督，关键词种类固定且限定在单个tagger的输出域，分段也不精确。本文希望动态构建与语料相关的词表，仅利用无监督词发现思路，把印地语口语词段与英文书面词建立跨语言映射，支撑语言记录与保护。
- **主要指标**：
- **代码**：https://github.com/gabitza-tech/vgs-cl-vocab | **Demo**：暂无

---
## [6 A Shaky Voice Is Not Always a Dodge: Benchmarking Textual and Vocal Evasion Detection in Earnings Calls](https://arxiv.org/abs/2608.28040)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：现有财报电话会中的"答非所问"检测仅依赖转写文本，把规避行为当作单一维度现象。本文认为口语交流中的规避本质上是多维度的：高管"说什么"与"怎么说"携带相互独立且互补的信息（两类标签弱相关，32.1%的样本出现跨模态不一致）。为此构造了首个带独立文本+语音双重标签的基准DualEvasion，含60场电话会、505个Q&A问答对，分别标注文本规避（直接/规避）与声学置信度（自信/不自信）。实验表明：
- **关键技术点**：** 现有研究（SubjECTive-QA、EvasionBench等）均将规避检测建模为纯文本分类任务，忽略了语音通道。作者用填充停顿、犹豫、语调等韵律线索将"怎么说"操作化为说话人置信度，指出关键难点是说话人依赖性：同一声学表现对不同高管意义不同，必须做说话人感知评估。此前的语音前端研究为音频级建模提供了基础，但尚无工作把文本规避与声学置信度联合建模。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [1 Multirate State Space Models for End-to-End Processing of Pulse Density Modulated Speech Signals](https://arxiv.org/abs/2608.28472)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：针对低功耗常开边缘设备上的SSM语音处理依赖PCM、且PDM转PCM需低通滤波与抽取带来高昂硬件开销的问题，本文提出一种仅用16kHz PCM训练、即可天然泛化到任意采样率PDM数据的端到端语音处理架构。其核心是使用FouT/LegT初始化的SSM编码层，利用其连续时间参数化特性把PCM与PDM输入映射为调制方式与采样率无关的SSM系数表示，并借助连续时间记忆窗在不做抗混叠的情况下对系数序列进行大
- **关键技术点**：** PDM MEMS麦克风兼具噪声鲁棒、低成本与可变采样率（多档位）省电优点，但现有算法都要求先做PDM转PCM（级联滤波+抽取），给资源受限硬件带来开销。已有两条绕开路径均不理想：一是用CNN把滤波与抽取融合为一个输入模块，二是端到端直接喂PDM进DNN。二者共同缺陷是必须在高达2MHz级别的PDM采样率下训练，序列过长导致训练耗时且内存占用大；同时只在单一采样率上训练，无法泛化到其他OSR。其可行性依据在于：PCM与PDM在PCM奈奎斯特频率（8kHz）以下共享完全相同频谱内容。
- **主要指标**：
- **代码**：https://github.com/NECOTIS/ssm-speech-processing.git | **Demo**：暂无

---
## [1 Low-Power End-to-End Cochlear Implant Speech Denoising with Spiking Neural Networks](https://arxiv.org/abs/2608.28493)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：人工耳蜗（CI）可帮助重度至极重度听障人群恢复听觉，但用户在噪声环境下仍难以理解语音。现有基于深度神经网络（DNN）的增强方案虽有效，却因能耗过高不适合低功耗CI处理器。本文提出一种受Deep ACE架构启发的脉冲神经网络（SNN），以单一网络端到端同时完成语音增强与CI编码两项任务。实验表明，该模型在声码化短时客观可懂度（VSTOI）和信噪比改善量（SNRi）上与Deep ACE持平，同时能耗降
- **关键技术点**：** CI处理链需在受限功耗与体积的硬件上将麦克风信号实时转为电刺激脉冲，噪声环境下倾听尤为困难。Deep ACE等深度方案用DNN联合增强与编码，效果显著但乘法密集、功耗高，难以嵌入电池供电的CI处理器。SNN采用事件驱动的二值脉冲通信，能耗极低且天然适配神经形态硬件，但如何在不损失CI编码性能的前提下实现低功耗增强尚待解决。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [2 Exploring the Design Space of Representation Learning for Audio Transformations](https://arxiv.org/abs/2608.28127)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-28
- **一句话贡献**：现有神经音频表示学习主要面向内容类任务（如检索、分类），其表征在处理类任务上能力有限；且处理感知表征究竟应编码"与源内容解耦的处理本身"还是"保留内容的处理后音频"，学界缺乏共识。本文提出统一框架，以处理一致性、描述对齐、前向预测等变三类目标在受控设置下穷举组合对比，系统揭示各目标的相对优势与交互效应；框架同时产出变换嵌入与处理后音频嵌入，二者职责互补——距离度量型任务偏好前者，探针型任务偏好后者
- **关键技术点**：** 既要回答"处理感知表征应捕获什么"这一表征设计问题，又要解决"模型、数据、评测各异导致无法归因行为差异"的对比公平性问题。现有方法各自隐式承诺单一表征范式，缺乏在统一条件下的系统比较。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [5 Beyond Speech: Dual-Domain SSL Fusion for Unified All-Type Audio Deepfake Detection](https://arxiv.org/abs/2608.29021)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-08-29
- **一句话贡献**：本文针对输入音频类型未知（语音、环境音、歌声、音乐四类）的统一全类型音频深度伪造检测问题，提出双域SSL融合框架。以EAT-large与wav2vec 2.0 XLS-R-300M为互补前端，通过逐层加权融合与token级拼接消除帧级对齐需求，经多头注意力统计池化聚合、二分类MLP头判别，并在其上叠加保守语音精炼。在AT-ADD Track 2评测集上核心双域模型达94.44% Macro-F1，
- **关键技术点**：** 现有音频深度伪造检测主要集中于语音，依赖音素、说话人等语音专属线索，而当前生成模型可产出音乐、歌声与环境音，待测类别未知且只需二分类输出。不同域伪影形式差异大，现有类型相关方案难以泛化。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [7 Stride-k Subsampling: Train-Free Audio Token Reduction for Whisper](https://arxiv.org/abs/2608.30927)

- **方向**：语音大模型 | **子方向**：Other | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：Whisper编码器将语音映射为固定1500个音频token，该接口已成为ASR解码器与Whisper类语音语言模型（SpeechLM）的默认表示，但其冗余性鲜被研究。本文提出stride-k下采样：一种无需训练的确定性索引操作，在卷积stem或编码器Transformer之后仅保留每第k个token。五种Whisper规模下k=2在stem与编码器输出两处均保持基线WER，CKA归因该稳定性源于
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [15 Parallel Time-Band Mixing with Learned Observation-Adding for Robust ASR Front-Ends](https://arxiv.org/abs/2608.30326)

- **方向**：语音前端 | **子方向**：ASR | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：面向鲁棒ASR的语音增强前端通常依赖循环时序与跨频带模块，串行依赖限制了并行效率。本文提出基于并行时-频带混合器（PTBM）块的序列并行频带分离增强前端：PTBM将频带内时序混合与逐帧跨频带注意力统一于单一并行架构，消除块内循环展开，并引入学习型观测叠加（LOA）抑制ASR敏感伪影。以冻结Whisper为后端在DNS Challenge与CHiME-4上验证，前端网络仅需0.96M参数、0.58 
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [16 Perceptually Better, Semantically Worse: Measuring Speech Enhancement Impact on LLM-Based Voice Systems](https://arxiv.org/abs/2608.30348)

- **方向**：语音前端 | **子方向**：SpeechLM | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：语音增强（SE）常作为语音AI流水线的预处理模块，其隐含假设是提升音频质量可改善下游任务表现。本文提出输出发散率（ODR），量化SE处理相对于干净语音改变LLM意图分类结果的频率，并在2,974条SLURP音频、五种条件及Whisper large-v3与wav2vec2-large串联系统上验证。结果显示所有条件下ODR均显著大于零（p<0.001），MetricGAN+虽改善PESQ却使ODR
- **关键技术点**：
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [6 SISER: Speaker-Invariant Speech Emotion Recognition with Entropy-Based Adversarial Training](https://arxiv.org/abs/2609.02941)

- **方向**：语音前端 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-08-31
- **一句话贡献**：针对SER中标注数据稀缺与说话人差异两大痛点，提出SISER框架，将wav2vec 2.0作为特征编码器、ECAPA-TDNN作为说话人判别器，融入基于熵最大化的对抗训练。在IEMOCAP说话人独立10折交叉验证下取得测试集UA 60.63%（WA 58.53%），相比复现基线（51.15%）提升9.48%，超越无对抗的wav2vec 2.0系统（56.46%）。
- **关键技术点**：** 语音中音素、说话人特性与情感状态在声学层面深度交织，SER模型在说话人独立设置下易学到说话人特有相关关系导致泛化退化。先验工作将熵最大化用于对抗解耦，但其CNN+GRU编码器与浅层FC判别器未能利用强预训练表示，弱判别器无法对残留说话人维度施压。
- **主要指标**：
- **代码**：https://github.com/slp-lab-research/siser.git | **Demo**：暂无

---
## [8 A Unified Uncertainty-Aware Back-End for Speaker Verification: Scoring, Normalization, and Calibration](https://arxiv.org/abs/2609.01221)

- **方向**：语音大模型 | **子方向**：Speaker/Verification | **评分**：7/10 | **日期**：2026-09-01
- **一句话贡献**：说话人验证（SV）后端通常组合相似度打分、分数归一化与校准，但说话人嵌入置信度随时长、噪声、信道而变化。现有不确定性感知方法多只改进编码器，不确定度未贯穿归一化与校准。本文将每条语音表示为"后验均值+协方差"，提出统一不确定性感知后端：UIA-cosine打分、UAS-Norm与UQMF校准。ECAPA-TDNN与ResNet上EER一致下降。
- **关键技术点**：** SV传统后端假设每条试听可靠性相同；短语音、噪声使某些嵌入天然不可靠。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [8 VAANI Noise Event Dataset: A curated spontaneous speech dataset annotated with timestamps for noise events](https://arxiv.org/abs/2609.02474)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-02
- **一句话贡献**：现有音效语料要么面向通用音频标记，要么面向纯净语音分离，缺少叠加在自发性真实语音上、带时间戳的强噪声标注。VAANI Noise Event Dataset 基于 Project VAANI 在印度自发性语音现场录音，为背景噪声事件添加精确起止时间戳，构成七类语义分类法（动物、交通、婴儿/儿童、音乐、信号/报警、家电、非言语人声）。数据集含 72,756 段语音（122.17 小时、38,541 
- **关键技术点**：** 真实印度场景中语音与车辆、动物、婴儿等非平稳背景噪声共存，噪声起止与语音的重叠关系直接决定识别误差与增强质量。现有语料要么合成混合（WHAM!、DESED 合成子集）、仅帧/片段级弱标签（AVA-Speech、FSD50K、AudioSet）、或无噪声标注（CHiME-6）；iNoise 与 Kathbath-Noisy 虽面向印度，却分别缺少语音与噪声事件标注。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
## [9 Removing Speech, Keeping Activities: A Privacy Firewall for Acoustic Sensing in Assisted Living](https://arxiv.org/abs/2609.02376)

- **方向**：语音前端 | **子方向**：Other | **评分**：7/10 | **日期**：2026-09-02
- **一句话贡献**：为解决辅助生活环境中声学感知系统采集日常活动声时泄露居民言语内容的隐私问题，本文提出"隐私防火墙"流水线：卷积 U-Net 编解码器在 log-mel 频谱域去除语音分量、保留环境活动声，全程仅用合成数据训练；下游活动识别采用 VGGish+SVM 迁移学习。在 ESC-50 和 SINS 上所有语音电平下残言语音均降为 0% VAD 可检测（Silero），ESC-50 40% 语音电平下精确率
- **关键技术点**：** 声学感知能非侵入监测老人日常活动，但居民与护理人员最担忧系统录制私人对话。ADAPTIVE 养老院部署中采用 VAD 触发静音捕获，遇广播语音频繁误触发导致大量活动信号丢失；且真实部署数据标注昂贵、收集窗口短，需契合实际工业部署约束（ADAPTIVE 项目经验启发）。
- **主要指标**：
- **代码**：暂无 | **Demo**：暂无

---
