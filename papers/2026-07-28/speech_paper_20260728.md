# 2026-07-28 语音论文速递

**共收录**: 7 篇 | **语音大模型**: 2 篇 | **语音前端**: 5 篇

> 今日 arXiv 语音相关论文共命中 7 篇。
> 以下是按评分排序的结果。

---

## 🤖 语音大模型

## [1] Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers

**arXiv ID** 2607.23811 | **方向** 语音大模型

**作者：** Dongseong Hwang, Prasanth Yadla, Kaan Elgin, Shifas Padinjaru Veettil, Sivanand Achanta, Dipjyoti Paul, Ramya Rasipuram, Tyler Johnson, Emad Soroush, Chung-Cheng Chiu, Zhifeng Chen

**机构：** Apple

**发布日期：** 2026-07-26 | **论文** https://arxiv.org/abs/2607.23811 | **PDF** https://arxiv.org/pdf/2607.23811.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
Siri Expressive Voices基于Apple设备端AFM 3 Core Advanced基础模型实现实时设备端语音合成。本文介绍了该能力的内存高效音频合成架构：将基础模型生成的语义音频token转换为高保真音频的detokenizer，在Apple Matrix Coprocessor (AMX)的严格计算和内存预算下工作。通过三组件设计（流式编码器、时间解码器、深度解码器）系统化解耦时间和深度处理，使用单个可重用的深度解码器通过DiT风格的stage conditioning生成所有RVQ级别，取代之前多解码器架构中每级专用解码器的设计。因果滑动窗口注意力配合固定窗口KV缓存实现与序列长度无关的恒定内存复杂度。部署在AMX上，detokenizer每生成步约10ms，约16倍实时，峰值运行时内存仅21MB，支持20-320秒连续流式合成。

### 🔧 技术方案

**模型架构：** 三组件设计：流式编码器(Streaming Encoder)、时间解码器(Temporal Decoder)和深度解码器(Depth Decoder)。使用单个可重用的深度解码器通过Diffusion Transformer (DiT)风格的stage conditioning生成所有RVQ级别。因果滑动窗口注意力配合固定窗口key-value缓存。

**核心创新：** 系统化解耦时间和深度处理，统一深度解码器取代每级专用解码器，固定窗口KV缓存实现与序列长度无关的恒定内存复杂度。

**训练策略：** 待从全文补充。

### 📊 实验结果
**数据集：** AMX部署环境评估

**主要指标：** 推理延迟：每步约10ms；吞吐量：160ms音频/步(16倍实时)；峰值运行时内存：21MB；设备资产：329MB；支持20-320秒连续流式合成。MOS评估(1B参数激活)：总体4.15 vs 3.87 (+0.28)，对话语音4.24 vs 3.82 (+0.42)。

**是否开源：** 暂无

### ⭐ 评分：9/10
Apple将前沿研究直接应用于生产级设备的能力令人印象深刻。该架构解决了端侧设备上实时语音合成的核心挑战，在保持高质量的同时实现了显著的效率提升。实验结果显示了+0.42 MOS的提升，对于语音合成领域来说是显著进步。

---

## [2] StanceBench: A Benchmark for Audio LLM-Based Interpersonal Stance Evaluation from Speech

**arXiv ID** 2607.22658 | **方向** 语音大模型

**作者：** Yuzhe Wang, Thomas Thebaud, Jennifer Hu, Jesús Villalba-Lopez, Venkatesh Ravichandran, Georgi Tinchev, Najim Dehak, Laureano Moro-Velázquez

**机构：** 约翰霍普金斯大学, Amazon

**发布日期：** 2026-06-27 | **论文** https://arxiv.org/abs/2607.22658 | **PDF** https://arxiv.org/pdf/2607.22658.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音到语音对话模型越来越依赖韵律和交互细节来传达社交意图，但此类线索的基准仍然有限。本文提出StanceBench，用于测量对话语音中人际立场并评估音频LLM作为自动化评判员的表现。使用Seamless Interaction语料库，StanceBench通过角色提示极定义9个立场维度，标准化单说话人和基于交互的评估，报告LLM作为评判员的鲁棒性、偏差和立场推断。同理心和礼貌最容易区分，诚实最难且显示高提示顺序偏差。

### 🔧 技术方案

**模型架构：** 基于Qwen2.5-Omni、Kimi-Audio、GPT、Gemini等LLM作为评判模型。

**核心创新：** 定义9个立场维度：温暖、同理心、礼貌、诚实、专注、社交参与、权力取向、冲突调节。提出两种评估模式：单说话人(无交互上下文)和交互式(有合作伙伴上下文)。设计极性顺序敏感性分析测试鲁棒性。

**训练策略：** 待从全文补充。

### 📊 实验结果
**数据集：** Seamless Interaction语料库

**主要指标：** 同理心(S1)最容易：AUROC 0.87-0.96；诚实(S4)最难：AUROC 0.50-0.72；交互式立场对上下文更敏感。GPT在5/9维度上达到最佳AUROC。

**是否开源：** 暂无

### ⭐ 评分：8/10
该基准填补了语音对话系统评估的重要空白。9个维度的系统设计全面，LLM-as-judge的评估方法有创新性。实验验证了多种LLM的表现差异，有实用价值。

---

## 🎵 语音前端

## [3] Expose Your Disguise: Recovering Source Speaker Identity From Voice Conversion

**arXiv ID** 2607.23650 | **方向** 语音前端

**作者：** Hanlei Zhang, Zhongming Ma, Mingyang Zhang, Tengfei Liu, Yushi Cheng, Yanjiao Chen

**机构：** 浙江大学, Ant Group

**发布日期：** 2026-07-26 | **论文** https://arxiv.org/abs/2607.23650 | **PDF** https://arxiv.org/pdf/2607.23650.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
语音转换(VC)允许攻击者模拟目标说话人，对生物识别安全构成重大威胁。在取证情境中，从转换后的音频中恢复源说话人身份对于缩小嫌疑人范围至关重要。本文提出TRIDENT，一个用于从转换音频样本中恢复源说话人原始身份的回溯框架。采用三叉戟架构：主提取器加两个辅助分支识别底层语音转换机制和提取目标说话人潜在表示。

### 🔧 技术方案

**模型架构：** 三叉戟架构：主提取器 + VC方法识别分支 + 目标说话人提取分支。

**核心创新：** VC方法识别分支利用主流转换方法的变体来指导恢复；目标说话人提取分支从复合转换音频中分离目标特定特征；主提取器利用两个辅助分支的洞察解耦混淆因素。使用AAM(加性角度边界)损失和COS(余弦相似度)损失进行训练。

**训练策略：** 待从全文补充。

### 📊 实验结果
**数据集：** 7种SOTA语音转换方法

**主要指标：** 总体最高准确率：90.99%；在telephony channels、unseen languages、adaptive scenarios下保持鲁棒性。

**是否开源：** 暂无

### ⭐ 评分：8.5/10
该研究解决了语音安全领域的重要问题。90%以上的溯源准确率展示了方法的实用性。跨语言泛化能力的验证证明了方法的普适性。技术创新点清晰，实验充分。

---

## [4] Disentangling Acoustic Cues in Alzheimer's Pathology and Perception: The Roles of Language and Gender

**arXiv ID** 2607.23977 | **方向** 语音前端

**作者：** Liu He, Yuanchao Li, Yin-Long Liu, Rui Feng, Yiming Wang, Jiaxin Chen, Yizhe Wang, Jiahong Yuan

**机构：** 中国科学技术大学, 爱丁堡大学

**发布日期：** 2026-07-27 | **论文** https://arxiv.org/abs/2607.23977 | **PDF** https://arxiv.org/pdf/2607.23977.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
声学生物标志物在检测阿尔茨海默病(AD)方面显示潜力，但驱动诊断AI的线索与人类听众关注的线索是否一致在语言和性别间尚未得到充分探索。本文训练模型预测临床AD状态（病理）和跨Mandarin和Greek语言、男女性别说话人的人类感知评分。结果揭示了情境依赖的差异：病理-感知对齐在Mandarin和女性说话人中显著，但在Greek和男性说话人中消失。

### 🔧 技术方案

**模型架构：** 双任务建模：临床AD分类(病理) + 人类感知评分预测(感知)。

**核心创新：** SHAP可解释性分析提取全局特征重要性；GLMER统计验证控制年龄、教育等混杂因素；跨语言和跨性别系统性分析。

**训练策略：** 待从全文补充。

### 📊 实验结果
**数据集：** Mandarin和Greek语音语料库

**主要指标：** Mandarin: 病理分类AUC 0.83*，感知回归r 0.84*；Greek: 病理分类AUC 0.60 ns，感知回归r 0.54*；Male: 病理分类AUC 0.52 ns，感知回归r 0.73*；Female: 病理分类AUC 0.79*，感知回归r 0.74*。

**是否开源：** 暂无

### ⭐ 评分：8.5/10
该工作揭示了临床语音AI中重要的公平性问题。跨语言和跨性别的系统性分析非常有价值，为可信部署提供了重要指导。发现全局XAI解释可能掩盖关键人口统计差异是重要贡献。

---

## [5] Improving Zero-Shot Phonetic Classification through Language-Agnostic Articulatory Features

**arXiv ID** 2607.23606 | **方向** 语音前端

**作者：** Ryo Magoshi, Jaeyoung Lee, Shinsuke Sakai, Tatsuya Kawahara

**机构：** 京都大学, NTT

**发布日期：** 2026-07-26 | **论文** https://arxiv.org/abs/2607.23606 | **PDF** https://arxiv.org/pdf/2607.23606.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
当前语音到IPA的音素基础模型(PFM)依赖G2P标签，但这些标签在语音上并不忠实。本文在中文送气音和日本鼻音的零样本分类任务上评估了模型，发现G2P训练的PFM表现很差。提出基于连续发音特征(AF)向量的分类方法，该方法优于离散token方法，尤其对罕见音素。最优时间聚合策略对目标区分至关重要：送气音用单帧分类最佳，鼻音用片段分类显著提升。

### 🔧 技术方案

**模型架构：** 使用24维连续发音特征向量(来自PanPhon系统)，通过L1距离计算AF向量与模板向量的相似度。

**核心创新：** 发音特征(AF)分类方法替代离散IPA token；最优时间聚合策略：送气音用单帧分类，鼻音用片段分类。

**训练策略：** 待从全文补充。

### 📊 实验结果
**数据集：** 中文送气音和日本鼻音分类任务

**主要指标：** 中文送气音分类(平衡准确率)：XLS-R+AFCM单帧95.4%，显著优于Decoder方法53.1%和CTC单帧56.7%。日本鼻音分类：XLS-R+AFCM片段分类72.6%，对罕见音素[ɲ]的召回率达到38.5%。

**是否开源：** 暂无

### ⭐ 评分：8/10
该工作揭示了音素基础模型的关键局限性，并提出了有效的解决方案。AF方法对罕见音素的显著改进具有重要实际意义。时间聚合策略的分析深入且有洞见。

---

## [6] Music-Source-Separation-Training (MSST): A Unified Framework for Training and Evaluating Music Demixing Models

**arXiv ID** 2607.23395 | **方向** 语音前端

**作者：** Roman Solovyev, Ilya Kiselev, Alexander Stempkovskiy, Tatiana Gabruseva

**机构：** MVSep.com, HSE大学, AlphaChip LLC

**发布日期：** 2026-07-25 | **论文** https://arxiv.org/abs/2607.23395 | **PDF** https://arxiv.org/pdf/2607.23395.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
音乐源分离(MSS)是从复调混合中恢复单个声音成分的任务，应用广泛。本文提出MSST，一个用于MSS任务的通用开源框架，统一训练、验证和推理流程。框架支持各种模型架构、数据预处理和增强、多种损失函数和评估指标。框架还支持多项提升分离质量的实用技术，如滑动窗口推理+交叉fade、测试时增强、模型集成、LoRA微调。

### 🔧 技术方案

**模型架构：** 支持Band-Split RoFormer、Mel-Band RoFormer、HTDemucs、SCNet等多模型架构。

**核心创新：** YAML配置驱动便于快速实验；支持pitch/tempo变化、codec伪影、混响等数据增强；推理技术包括滑动窗口+交叉fade、TTA、模型集成、LoRA微调；损失函数支持L1/MSE、多分辨率STFT loss、masked loss、logWMSE等。

**训练策略：** 待从全文补充。

### 📊 实验结果
**数据集：** 框架已在多个模型上验证有效性

**主要指标：** 消融研究证明各项技术可提升分离质量。

**是否开源：** 开源

### ⭐ 评分：7.5/10
该框架降低了音乐源分离研究的门槛，提供了完整的训练和推理流程。工程化程度高，对研究社区有实际价值。开源便于复现和进一步改进。

---

## [7] Speech Entrainment in Multi-Party Conversations with a Digital Agent

**arXiv ID** 2607.22939 | **方向** 语音前端

**作者：** Nicholas Mehlman, Kaitlin Zareno, Kleanthis Avramidis, Anfeng Xu, Shrikanth Narayanan

**机构：** 南加州大学

**发布日期：** 2026-07-24 | **论文** https://arxiv.org/abs/2607.22939 | **PDF** https://arxiv.org/pdf/2607.22939.pdf | **代码** 暂无 | **Demo** 暂无

### 📌 简介
已有广泛观察表明参与对话的个人倾向于调整说话风格以匹配对方。但之前大多数工作集中在人类之间的双人交互。本文研究一种新设置：人类群体和数字代理之间的多方交互。研究发现个体在局部上与其他人entrain，但全局entrainment以及与代理的entrainment有限且依赖于队列。

### 🔧 技术方案

**模型架构：** 分析方法：局部Entrainment（同一轮次内特征相似性）和全局Entrainment（会话开头vs结尾特征差异）。

**核心创新：** 研究多方对话中人类与数字代理交互时的语音entrainment效应；数据集包含成人组和家庭组（父母/儿童）会话；特征类型：手工特征(振幅、音高、情感) + 深度学习特征(Whisper, Mimi)。

**训练策略：** 待从全文补充。

### 📊 实验结果
**数据集：** 成人组：30场会话，337分钟；家庭组：10场会话，65分钟

**主要指标：** 成人组局部Entrainment：几乎所有特征维度都显示显著正entrainment。家庭组局部Entrainment：无振幅或音高entrainment，但有情感特征和深度学习embedding的entrainment。两组均未显示与数字代理的局部entrainment。

**是否开源：** 暂无

### ⭐ 评分：7.5/10
该研究探索了语音交互的新兴场景，对设计更自然的数字代理有重要启示。发现人类本能地区分对待代理和人类伙伴是重要的观察。数据集设计合理，分析方法系统。

---

## 本期总结

本期论文涵盖：

- **TTS/语音合成**：Apple高效端侧合成架构
- **语音转换安全**：TRIDENT溯源框架
- **语音基础模型**：零样本音素分类的发音特征方法
- **音乐源分离**：MSST统一框架
- **临床语音**：阿尔茨海默病检测的公平性问题
- **对话系统评估**：StanceBench立场评估基准
- **语音交互**：多方对话中的entrainment现象

**推荐关注**：Apple端侧合成、TRIDENT溯源、阿尔茨海默病公平性研究
