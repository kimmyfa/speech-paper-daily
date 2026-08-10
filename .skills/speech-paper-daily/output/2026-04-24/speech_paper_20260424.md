# 2026-04-24 语音论文速递

**共收录**: 8 篇 | **语音合成**: 1 篇 | **语音前端**: 3 篇 | **语音对话**: 1 篇 | **音频处理**: 3 篇

> 今日 arXiv 语音相关论文共命中 8 篇。以下是按评分排序的结果。

---

## [1] MAGIC-TTS: Fine-Grained Controllable Speech Synthesis with Explicit Local Duration and Pause Control

**arXiv ID** 2604.21164 | **方向** 语音合成

**作者** Jialong Mai, Xiaofen Xing, Xiangmin Xu

**机构** South China University of Technology

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.21164 | **PDF** https://arxiv.org/pdf/2604.21164.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
现代文本到语音系统缺少细粒度的本地时间控制能力。MAGIC-TTS是首个具有显式本地时长和暂停控制的TTS模型,通过显式token级时长条件、高置信度时长监督和鲁棒训练机制实现可靠的本地控制,同时保持自然的高质量合成。

### 🔧 技术方案

**模型架构** 基于Flow-based TTS backbone,集成显式token级时长条件到并行声学生成器,而非与自回归rollout纠缠。系统结合了现代零样本TTS的flow matching技术和显式本地时间控制。

**核心创新**
显式token级内容时长和暂停条件控制,首次在高质量TTS系统中实现细粒度本地时间操作。高置信度本地时间监督管道,包括交叉验证的高置信度时长数据集支持稳定的本地控制训练。零值校正机制,解决模型对零时长控制的偏见问题。鲁棒性训练使模型对缺失的本地控制具有适应性。

**训练策略**
损失函数包括flow matching主要损失和本地时长监督辅助损失。数据预处理包括高置信度时长数据准备,通过交叉验证确保时长标注质量。训练采用两阶段策略,首先在完全监督设置下训练基础TTS能力,然后逐步引入本地时间控制。零值校正通过特殊损失项防止模型对零时长产生偏见,鲁棒性训练通过随机丢弃部分本地控制信号实现。

### 📊 实验结果

**数据集** 自建时长控制基准数据集,涵盖导航引导、引导阅读和代码阅读等场景。

**主要指标** 在本地时间控制基准上,MAGIC-TTS显著改善了token级时长和暂停的跟随性能,相对于自发合成有大幅提升。即使在无时间控制的情况下,MAGIC-TTS仍保持自然的高质量合成性能。在场景化基准测试中,实现了可重现的统一时长基线,并将编辑区域移向请求的本地目标,平均偏差较低。

**是否开源** 暂未开源代码

### ⭐ 评分: 9/10
理由 首次实现token级细粒度时长控制的TTS系统,创新性极高。实验设计充分,涵盖多种实际应用场景。方法设计严谨,训练机制全面,既有理论贡献又有实用价值。

---

## [2] DiariZen Explained: A Tutorial for the Open Source State-of-the-Art Speaker Diarization Pipeline

**arXiv ID** 2604.21507 | **方向** 语音前端

**作者** Nikhil Raghav

**机构** Institute for Advancing Intelligence, TCG CREST + Department of Computer Science, RKMVERI

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.21507 | **PDF** https://arxiv.org/pdf/2604.21507.pdf | **代码** https://github.com/nikhilraghav29/diarizen-tutorial | **Demo** 暂无

### 📌 简介
DiariZen是当前开源SOTA说话人分离系统,但架构分散在多个仓库和框架中,难以理解和复现。本教程提供自包含的模块化解释,将完整pipeline分解为七个阶段,每个阶段提供概念动机、源代码引用、中间张量形状和可视化输出。

### 🔧 技术方案

**模型架构** 混合SD pipeline,结合EEND风格神经分割前端和VBx聚类后端。前端基于结构化剪枝的WavLM-Large编码器和Conformer with powerset分类,后端使用VBx聚类解析全局说话人身份。系统七个阶段包括音频加载和滑动窗口分割、WavLM特征提取与学习层加权、Conformer后端和powerset分类、分割聚合via overlap-add、说话人嵌入提取with overlap排除、VBx聚类with PLDA评分、重构和RTTM输出。

**核心创新**
结构化剪枝的WavLM-Large编码器,通过知识蒸馏实现紧凑高效的特征提取。Powerset分类用于端到端神经diarization,处理可变说话人数量。Overlap-add聚合策略处理滑动窗口分割边界,Overlap排除策略提取纯说话人嵌入。VBx聚类with PLDA评分实现全局说话人身份解析。

**训练策略**
WavLM通过结构化剪枝和知识蒸馏优化,保留关键语音表征。Conformer backend使用powsset编码处理多说话人场景,损失函数为端到端训练。VBx聚类采用贝叶斯变分推断和PLDA评分,无需预训练聚类参数。每个阶段提供独立可执行脚本和端到端Jupyter notebook。

### 📊 实验结果

**数据集** AMI Meeting Corpus 30秒excerpt用于演示,系统在AMI、VoxSRC和DIHARD-III等多个基准达到SOTA性能。

**主要指标** 作为教程论文,重点提供系统解释而非性能基准。DiariZen原文显示其在多个benchmark上达到SOTA性能。教程提供30秒excerpt的完整可视化输出,包括WavLM层权重、powerset类概率、overlap-add覆盖图、嵌入余弦相似度矩阵和VBx聚类分配。

**是否开源** 已开源,提供独立Python脚本和Jupyter notebook

### ⭐ 评分: 8/10
理由 教程价值极高,填补了DiariZen系统理解和复现的空白。提供自包含的模块化解释、完整代码和可视化输出,对研究和实践都有重要贡献。虽非新算法,但开源和教程工作值得高分。

---

## [3] Full-Duplex Interaction in Spoken Dialogue Systems: A Comprehensive Study from the ICASSP 2026 HumDial Challenge

**arXiv ID** 2604.21406 | **方向** 语音对话

**作者** Chengyou Wang, Hongfei Yue, Guojian Li, Zhixian Zhao, Shuiyuan Wang, Shuai Wang, Xin Xu, Hui Bu, Lei Xie

**机构** Northwestern Polytechnical University + Nanjing University + AISHELL

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.21406 | **PDF** https://arxiv.org/pdf/2604.21406.pdf | **代码** https://github.com/ASLP-lab/HumDial-FDBench | **Demo** 暂无

### 📌 简介
ICASSP 2026 HumDial Challenge全双工交互赛道旨在推进全双工系统评估,提供处理实时中断、语音重叠和动态话轮协商的框架。发布高质量双通道人机对话数据集,包含中断、重叠语音和反馈机制,建立HumDial-FDBench基准评估系统处理中断能力,创建公开排行榜比较开源和专有模型性能。

### 🔧 技术方案

**挑战框架** ICASSP 2026 Human-like Spoken Dialogue Systems Challenge的Full-Duplex Interaction Track,聚焦实时中断处理、语音重叠处理、动态话轮协商。现有语音对话系统仍依赖严格的轮流制范式,难以在动态对话中自然响应。全双工交互是自然交流的关键元素,传统系统常缺失此能力。

**核心创新**
发布高质量双通道人机对话数据集,捕获真实对话现象如中断、重叠语音和动态话轮协商。HumDial-FDBench基准评估系统处理中断同时维持对话流畅度的能力。公开排行榜比较开源和专有模型,促进透明可重现评估。 Interruption场景包括Follow-up Questions、Negation or Dissatisfaction、Repetition Requests、Topic Switching、Silence or Termination。Rejection场景包括User Real-time Backchannels、Pause Handling、Third-party Speech、Speech Directed at Others。

**训练策略**
数据集包含Interruption和Rejection两大类共八个场景,训练集3631样本,开发集800样本,测试集2400样本。基准评估系统行为评估和指标,包括Interruption Handling、Response Timing、Dialogue Resumption等维度。提供baseline系统和开源代码支持。

### 📊 实验结果

**数据集** HumDial-FDBench数据集,涵盖8个场景的实时人机对话,包括中断和拒绝行为。

**主要指标** 作为挑战赛论文,提供框架和基准而非具体算法性能。公开排行榜显示多种开源和专有模型在基准上的表现,促进社区进步。 HumDial-FDBench评估全双交能力,包括中断处理、响应时序、对话恢复等指标。

**是否开源** 已开源数据集和基准代码

### ⭐ 评分: 8/10
理由 挑战赛和基准工作对社区有重要贡献,填补了全双工对话系统评估的空白。数据集设计周全,涵盖多种真实对话场景。虽然是框架工作而非算法创新,但对推动全双交对话研究有实际价值。

---

## [4] Materialistic RIR: Material Conditioned Realistic RIR Generation

**arXiv ID** 2604.21119 | **方向** 音频处理

**作者** Mahnoor Fatima Saad, Sagnik Majumder, Kristen Grauman, Ziad Al-Halah

**机构** University of Utah + UT Austin

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.21119 | **PDF** https://arxiv.org/pdf/2604.21119.pdf | **代码** https://github.com/mahnoor-fatima-saad/MatRIR | **Demo** https://mahnoor-fatima-saad.github.io/MatRIR.html

### 📌 简介
声音不仅受空间布局影响,还受场景中物体和表面材料影响。现有声学建模方法常将空间和材料影响纠缠在相关表示中,限制用户控制并降低生成声学真实感。提出材料可控房间冲激响应生成新方法,显式解耦空间和材料线索影响,使用空间模块捕获空间布局影响,材料模块根据用户指定材料配置调制空间RIR,实现细粒度用户控制。

### 🔧 技术方案

**模型架构** 双模块设计,空间模块捕获场景空间布局影响,材料模块根据用户指定材料配置调制空间RIR。空间模块包括空间编码器、空间RIR解码器和音频特征上采样网络。材料模块包括材料编码器、材料RIR编码器和材料感知音频特征上采样器。两个模块通过Cross-Modal Correspondence Network连接,实现空间和材料线索的显式解耦。

**核心创新**
显式解耦空间和材料对室内声学的贡献,允许用户轻松修改场景材料配置并观察声学影响。Cross-Modal Correspondence Network学习空间和材料特征对应关系。材料分类准确度和材料分布准确度作为评估指标,量化模型对材料线索的敏感性。基于Acoustic Wonderland Dataset (AcoW)训练和评估。

**训练策略**
空间编码器从RGB-D场景图像提取空间特征,深度预测器估计场景深度图。材料编码器从材料图像提取材料特征。空间RIR解码器从空间特征生成空间RIR,材料RIR编码器编码空间RIR。音频特征上采样网络融合空间和材料特征生成最终RIR。损失函数包括重建损失、材料分类损失和对抗损失。

### 📊 实验结果

**数据集** Acoustic Wonderland Dataset (AcoW),包含多种材料配置的真实RIR数据。

**主要指标** 在声学指标上相比之前方法提升高达16% RTE,在材料指标上提升高达70%。人类感知研究证明模型相比最强baseline在真实感和材料敏感性上有所提升。消融实验验证各模块重要性,定性结果展示材料修改对声学的影响。

**是否开源** 已开源代码和Project Page

### ⭐ 评分: 8/10
理由 空间和材料线索的显式解耦设计新颖,有重要理论和实用价值。实验设计充分,包括声学指标、材料指标和人类感知研究。在VR、机器人、建筑设计等领域有广泛应用潜力。

---

## [5] Sema: Semantic Transport for Real-Time Multimodal Agents

**arXiv ID** 2604.20940 | **方向** 音频处理

**作者** Jiaying Meng, Bojie Li

**机构** 暂未明确

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.20940 | **PDF** https://arxiv.org/pdf/2604.20940.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
实时多模态agent使用为人设计的网络栈传输原始音频和屏幕截图,优化感知保真度和平滑播放。但agent模型作为事件驱动处理器,没有固有的物理时间感,消费任务相关语义而非实时重建信号。这种根本差异将传输目标从信号保真度技术问题转变为语义保持问题。Sema语义传输系统结合离散音频tokenizer和混合屏幕表示,消除抖动缓冲区,在模拟WAN条件下减少上行带宽64x音频和130-210x截图,同时保持任务精度。

### 🔧 技术方案

**系统架构** 语义传输系统,结合离散音频tokenizer和混合屏幕表示。混合屏幕表示包括无损可访问树或OCR文本加紧凑视觉token。突发token交付消除抖动缓冲区,避免传统传输中的时间同步问题。

**核心创新**
从信号保真度转向语义保持的传输目标设计。离散音频tokenizer压缩音频数据同时保留任务相关语义。混合屏幕表示结合文本和视觉表示,平衡可访问性和效率。突发token交付模式避免抖动缓冲区,减少传输延迟。

**训练策略** 音频tokenizer在语音数据上预训练,学习离散token表示。视觉tokenizer在图像数据上预训练,生成紧凑视觉token。混合表示根据内容类型动态选择最优表示方式。突发交付策略根据网络条件动态调整传输频率。

### 📊 实验结果

**数据集** 在模拟WAN条件下的多模态agent交互场景。

**主要指标** 上行带宽减少64x音频和130-210x截图,同时保持任务精度在原始基线的0.7个百分点内。在视频会议、代码协作等多模态任务上验证有效性。

**是否开源** 暂未开源

### ⭐ 评分: 7/10
理由 语义传输vs信号传输的思路新颖,实际应用价值高。带宽压缩性能显著,对实时多模态系统有重要意义。但实验相对简单,缺少更多基准对比和应用场景验证。

---

## [6] Do LLM Decoders Listen Fairly? Benchmarking How Language Model Priors Shape Bias in Speech Recognition

**arXiv ID** 2604.21276 | **方向** 语音前端

**作者** Srishti Ginjala, Eric Fosler-Lussier, Christopher W. Myers, Srinivasan Parthasarathy

**机构** 暂未明确

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.21276 | **PDF** https://arxiv.org/pdf/2604.21276.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
预训练大语言模型取代任务特定解码器后,关键问题出现了:文本导出的先验是否使跨人口群体的识别更公平或更偏颇?评估九个模型跨越三个架构代(CTC无语言模型、encoder-decoder隐式LLM、LLM-based显式预训练解码器),在Common Voice 24和Meta的Fair-Speech受控提示数据集上约43000个话语,涵盖五个 demographic axis。在干净音频上发现三个挑战假设:LLM解码器不放大种族偏见、Whisper在印度口音语音上出现病理性幻觉、音频压缩比LLM缩放更能预测口音公平性。在12种声学退化条件下测试发现严重退化反而压缩公平性差距。

### 🔧 技术方案

**评估模型** 九个模型跨越三个架构代: CTC with no language model、encoder-decoder with implicit LM、LLM-based with explicit pretrained decoder。包括Whisper各版本、Granite等大模型。

**核心发现**
LLM解码器不放大种族偏见,Granite-8B在种族公平性上表现最佳。Whisper在印度口音语音上出现病理性幻觉,在large-v3上插入率激增至9.62%。音频压缩比LLM缩放更能预测口音公平性。严重退化下所有群体收敛到高WER,反而压缩公平性差距。静默注入放大Whisper口音偏见至4.64x,触发人口选择性幻觉。Masking下Whisper进入灾难性重复循环,显式LLM解码器产生38x更少插入。高压缩音频编码重新引入重复病理。

**训练策略** 跨架构系统性评估,使用Common Voice 24和Fair-Speech受控提示数据集消除词汇混淆。测试12种声学退化条件包括噪声、混响、静默注入、chunk masking等。总共216次推理运行。

### 📊 实验结果

**数据集** Common Voice 24、Meta Fair-Speech受控提示数据集,涵盖种族、口音、性别、年龄、第一语言五个 demographic axis。

**主要指标** Granite-8B种族公平性最佳,最大最小WER比为2.28。Whisper在印度口音语音上插入率激增至9.62%。音频压缩比LLM缩放更能预测口音公平性。静默注入放大口音偏见4.64x。显式LLM解码器插入率仅为Whisper的1/38。

**是否开源** 暂未开源

### ⭐ 评分: 7/10
理由 ASR公平性研究有重要社会意义,跨架构系统性评估有价值。关键发现如音频编码器设计是公平性关键,对实际应用有指导意义。但主要是评估工作而非方法创新,实际应用价值依赖于社区采纳。

---

## [7] Time vs. Layer: Locating Predictive Cues for Dysarthric Speech Descriptors in wav2vec 2.0

**arXiv ID** 2604.21628 | **方向** 语音前端

**作者** Natalie Engert, Dominik Wagner, Korbinian Riedhammer, Tobias Bocklet

**机构** 暂未明确

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.21628 | **PDF** https://arxiv.org/pdf/2604.21628.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Wav2vec 2.0在病理性语音分析中显示强性能,有效捕获非典型语音特征。但其学习表示中哪些组件对特定下游任务最信息丰富仍不清楚。本研究通过Speech Accessibility Project数据集的病理性语音描述符回归调查此问题,聚焦五个描述符分别解决语音或语音生产的不同方面:可懂度、辅音不精确、不恰当静默、刺耳声音和单调响度。语音表征从基于W2V2的特征提取器导出,系统比较layer-wise和time-wise聚合策略使用attentive statistics pooling。结果显示可懂度通过layer-wise表征最佳捕获,而不精确辅音、刺耳声音和单调响度从time-wise建模中获益。不恰当静音方面两种方法均无明确优势。

### 🔧 技术方案

**特征提取** 基于Wav2vec 2.0的特征提取器导出语音表征,系统比较layer-wise和time-wise聚合策略使用attentive statistics pooling。

**核心发现**
可懂度通过layer-wise表征最佳捕获,说明此描述符需要跨时间聚合的全局特征。不精确辅音、刺耳声音和单调响度从time-wise建模中获益,说明这些描述符需要局部时间精度。不恰当静音方面两种方法均无明确优势,可能需要更复杂建模。结果显示不同病理性语音描述符需要不同的表征策略。

**训练策略** 使用Speech Accessibility Project数据集的标注进行回归训练。Layer-wise聚合跨W2V2层特征进行attentive statistics pooling。Time-wise聚合跨时间步特征进行attentive statistics pooling。回归目标为五个病理性语音描述符。

### 📊 实验结果

**数据集** Speech Accessibility Project数据集,包含病理性语音和标注。

**主要指标** 不同描述符在不同聚合策略下表现差异显著。可懂度layer-wise表现最佳,不精确辅音、刺耳声音、单调响度time-wise表现最佳。不恰当静音无明确优势策略。

**是否开源** 暂未开源

### ⭐ 评分: 6/10
理由 研究病理性语音表征有价值,对不同描述符需要不同聚合策略的发现有意义。但方法相对常规,创新性有限。应用场景较窄,主要服务于病理性语音分析领域。

---

## [8] Dilated CNNs for Periodic Signal Processing: A Low-Complexity Approach

**arXiv ID** 2604.21651 | **方向** 音频处理

**作者** Eli Gildish, Michael Grebshtein, Igor Makienko

**机构** 暂未明确

**发布日期** 2026-04-24 | **论文** https://arxiv.org/abs/2604.21651 | **PDF** https://arxiv.org/pdf/2604.21651.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
周期信号去噪和准确波形估计是多个信号处理领域的核心任务,包括语音、音乐、医疗诊断、无线电和声纳。虽然深度学习方法最近显示出比传统方法的性能提升,但需要大量计算资源且通常为每次信号观测单独训练。本研究提出基于膨胀CNN和重采样的计算高效方法R-DCNN,设计用于严格功耗和资源约束下的操作。该方法针对具有变化基频的信号,只需要单次观测进行训练,通过轻量级重采样步骤将不同频率信号的时间尺度对齐以重用相同网络权重。尽管计算复杂度低,R-DCNN达到与state-of-the-art经典方法如自回归方法以及常规单独训练每个观测的DCNNs相当的性能。这种效率和性能的组合使得该方法特别适合在资源受限环境中部署而不牺牲去噪或估计精度。

### 🔧 技术方案

**模型架构** 基于膨胀CNN和重采样的R-DCNN,针对不同基频信号设计轻量级重采样步骤对齐时间尺度以重用网络权重。

**核心创新**
轻量级重采样步骤对齐不同频率信号时间尺度,允许重用相同网络权重。单次观测训练机制,减少计算和存储需求。针对变化基频信号设计,适合语音、音乐等周期信号。计算复杂度低,适合IoT设备等资源受限环境。

**训练策略** 单次观测训练,避免为每次信号单独训练。重采样步骤将不同频率信号对齐到标准时间尺度。膨胀CNN捕获周期信号的长期依赖。损失函数为重构损失或估计损失。

### 📊 实验结果

**数据集** 语音、音乐、医疗诊断等多个周期信号数据集。

**主要指标** 与state-of-the-art经典方法如AR方法性能相当,与常规DCNNs性能相当。计算复杂度显著降低,适合资源受限环境。

**是否开源** 暂未开源

### ⭐ 评分: 6/10
理由 针对资源受限环境的低复杂度方法有实际价值。单次观测训练和重采样策略设计合理。但创新性有限,方法相对常规。应用广泛但缺少特定领域深入分析。

---

*由Speech-paper-daily工具 自动生成 · 数据来源:arXiv*