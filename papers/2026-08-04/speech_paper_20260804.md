# 语音论文速递 2026-08-04

## 📌 本期亮点

- **全双工语音交互大模型**：京东发布 JoyAI-Talker，实现带打断能力的全双工语音对话
- **语音deepfake检测新突破**：OPPO 提出路由方案获 AT-ADD Challenge Track2 冠军（96.10% Macro-F1）
- **个性化情感TTS**：交互式遗传算法实现情感空间的用户自适应

---

## 🔧 语音合成 (TTS)

### 1. JoyAI-Talker: Full-Duplex Speech Interactive Large Model Built for Empathetic Voice Agents

📝 **作者**：Yinhao Bai, Jinming Chen 等（京东）  
🏫 **机构**：JD.COM  
📰 **arXiv**：2608.01119

**核心方法**：  
- **Thinker-Talker 架构**：Thinker 负责推理和共情，Talker 负责语音生成
- **统一语音-文本联合训练**：从预训练中期开始融合，缓解"认知退化"问题
- **PAER（人格适应共情响应）框架**：从音频中提取说话人属性（性别、年龄、情绪），结合 CoT 推理生成共情响应
- **Joy-Duplex**：基于状态的全双工交互框架，在 Full-Duplex-Bench v1.5 上实现 0.88 响应率，同时保持极低的误触发率

**实验结果**：
- 在 T2T 和 S2T 基准上达到竞争力性能
- MATH 基准 94.62%，保持强大推理能力
- 支持笑声、叹气等局部副语言事件控制

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：首个展示全双工语音交互能力的国产大模型，架构设计清晰，实验充分

---

### 2. Experience-Calibrated Contrastive Decoding for Mitigating Hallucinations in LM-Based TTS

📝 **作者**：Chenlin Liu, Minghui Fang 等（清华大学）  
🏫 **机构**：清华大学  
📰 **arXiv**：2608.00722

**核心方法**：  
- **条件信息视角**：区分文本来源的"对齐信息"和声学上下文来源的"经验信息"
- **ECCD（经验校准对比解码）**：在不解码时控制幻觉，不抑制有用的经验信息
- **经验兼容性系数 (ECC)**：动态调整增强强度

**实验结果**：
- 在 SeedTTS-Eval 上，四个模型 WER/CER 最多降低 55.6%
- 多语言 CV3-Eval 25 个设置中 24 个取得改进
- 主观评测 CMOS +0.644，同时保持说话人相似度

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：首个 TTS 解码时的条件信息分析方法，无需训练即可缓解幻觉

---

### 3. Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS

📝 **作者**：Wangzixi Zhou, Bagus Tris Atmaja, Sakriani Sakti（奈良先端科学技术大学院大学）  
🏫 **机构**：Nara Institute of Science and Technology, Japan  
📰 **arXiv**：2608.00998  
📌 **推荐理由**：INTERSPEECH 2026 接收论文

**核心方法**：  
- **交互式遗传算法 (IGA)**：根据用户偏好反馈迭代优化 arousal-valence (A-V) 坐标
- **情感控制器**：将低维 A-V 坐标映射到高维声学特征
- **个性化情感空间**：为每个听众获得个性化的 Russell 环效模型变体

**实验结果**：
- MOS 从 3.37 提升到 3.75（情感控制器）
- WER 相对降低 23.5%
- 中日印尼三国用户个性化偏好率 76%，文化适应偏好率 64-70%

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：首次系统研究情感感知的个文化和文化差异，对话式 AI 的重要方向

---

### 4. SwanTale: Unified Multi-Speaker Speech and Audio Generation

📝 **作者**：Yu Zhang, Ruiqi Li 等（字节跳动）  
🏫 **机构**：ByteDance  
📰 **arXiv**：2608.02023

**核心方法**：  
- **SwanData-Caption**：清洗原始语音数据，添加合成覆盖，标注多层次 caption
- **SwanTale**：支持 instruct 和 zero-shot 两种任务的多说话人表达语音生成模型
- **SwanVAE**：支持高质量多音频模态生成
- **GRPO 后训练**：课程学习和强化学习

**实验结果**：
- 在 zero-shot 和 instruct 指标上领先
- 支持涉及多说话人语音和音频的复杂 instruct 生成

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：字节在语音生成领域的最新工作，统一框架覆盖多种场景

---

## 📊 语音识别 (ASR)

### 5. Normal-Anchored FOMAML for Cleft Lip and Palate Speech Recognition

📝 **作者**：Susmita Bhattacharjee, Jagabandhu Mishra 等（印度理工学院古瓦哈蒂分校）  
🏫 **机构**：IIT Guwahati, University of Eastern Finland, Harvard Medical School  
📰 **arXiv**：2608.00186

**核心方法**：  
- **NA-FOMAML**：使用一级模型无关元学习对 Whisper 进行微调
- **正常语音锚定内层**：内层使用正常语音作为支持集，外层加入病理语音
- **部分编码器微调**：探索不同层的 Whisper 编码器微调策略

**实验结果（NMCPC 数据集）**：
- 正常到 Normal+Mild+Moderate 配置：WER 4.40% (正常), 5.53% (轻度), 16.14% (中度), 52.07% (重度)
- 音素级错误分析显示严重语音在摩擦音、破擦音、鼻音、流音、塞音和元音上错误率高

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：针对病理语音识别的公平性问题，提出创新性元学习方案

---

### 6. Latent Softmax for Data-Efficient Phoneme-Based Multilingual ASR

📝 **作者**：Saierdaer Yusuyin, Nanling Jiang, Hao Huang, Zhijian Ou（清华大学）  
🏫 **机构**：清华大学  
📰 **arXiv**：2608.01281

**核心方法**：  
- **潜在 Softmax**：为带调语言和无声调语言的多语言 ASR 设计
- **音素子类建模**：将带调元音建模为子类，基元音为母类
- **边缘化推断**：仅观测到基元音母类标签时，边缘化带调元音子类

**实验结果**：
- S2P 音素错误率相比标准 Softmax 多语言基线降低：
  - AISHELL-1: 8.4%
  - LibriSpeech test-clean: 17.5%
  - test-other: 12.6%
- 代码切换后，项目器式接口混合错误率进一步降低

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：针对声调语言的创新性多语言 ASR 方案

---

## 🔐 语音安全 (Speech Security)

### 7. Hidden-Domain Routing for All-Type Audio Deepfake Detection

📝 **作者**：Yifan Gao, Yao Tian, Hongbin Suo, Haonan Lu（OPPO）  
🏫 **机构**：OPPO AI Center, 北京 & 深圳  
📰 **arXiv**：2608.00493  
📌 **推荐理由**：ACMMM 2026 接收论文，AT-ADD Challenge Track2 冠军

**核心方法**：  
- **路由系统**：首先恢复隐藏音频类型，然后在该分支内解释检测器分数
- **AudioType-BEATs-6s Router**：从 6 秒窗口估计音频类型
- **分支检测器**：Speech-XLSR（语音）、SoundMusic-EAT（声音/音乐）、Singing-EAT（歌唱）
- **分支局部分数解释**：每个分支使用各自的决策阈值

**实验结果**：
- 官方 AT-ADD Track2 最终评估得分：96.10% Track2 Macro-F1（排名第一）
- 各类型 Macro-F1：语音 88.07%, 声音 98.18%, 歌唱 99.07%, 音乐 99.08%

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：业界领先的全类型音频deepfake检测方案，架构设计创新

---

### 8. REIMU: Efficient Heterogeneous Hierarchical Reasoning for SSL-Based Speech Deepfake Detection

📝 **作者**：Kwok-Ho Ng, Tingting Song, Bingwen Feng, Peiya Li  
🏫 **机构**：西北工业大学  
📰 **arXiv**：2608.00857

**核心方法**：  
- **异构层次推理**：比较单次前向、权重共享循环、同质 HRM 和异构 HRM
- **异构操作分配**：高级模块使用 MHSA，低级模块使用线性注意力（GDN2 或 Raven）
- **参数高效**：比匹配基线减少 10.8% 的下游参数

**实验结果（ASVspoof 2019 & 2021）**：
- 异构配置在多个设置下达到竞争力性能
- 在 19LA、21LA、21DF 上 EER 表现优异

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：系统比较不同层次推理架构对语音deepfake检测的影响

---

### 9. Anomalous Sound Detection Meets Noise-Aware Self-Supervised Learning

📝 **作者**：Takuya Fujimura, Gordon Wichern, Yoshiki Masuyama 等（NTT）  
🏫 **机构**：NTT Corporation  
📰 **arXiv**：2608.00447  
📌 **推荐理由**：DCASE 2026 Challenge Task 2 冠军方案

**核心方法**：  
- **噪声感知自监督学习 (NA-SSL)**：利用远场麦克风录音作为辅助信息提取近场麦克风的干净 SSL 表示
- **模拟双通道录音**：使用 FSD50K（目标声音）+ WHAM!/DEMAND/QUT-NOISE（噪声）
- **NA-BEATs/NA-EAT/NA-Dasheng**：三种基础 SSL 模型的噪声感知扩展

**实验结果（DCASE 2026 Challenge Task 2）**：
- NA-BEATs 在官方评估中得分 70.24%（排名第一）
- 第二名得分 65.46%
- 官方基线得分 59.80%

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：首个将噪声感知 SSL 应用于异常声音检测的工作，获挑战赛冠军

---

## 🎵 语音增强与处理

### 10. AnyBand: Unified Multi-Bandwidth Speech Extension

📝 **作者**：Junchuan Zhao, Minh Duc Vu, Bowen Zhang, Ye Wang  
🏫 **机构**：National University of Singapore  
📰 **arXiv**：2608.00572

**核心方法**：  
- **统一多带宽扩展**：将 BWE 重新表述为上下文频谱填充
- **频率感知 Diffusion Transformer**：建模跨频率交互和长距离时序依赖
- **Easy-to-Balanced cutoff 课程**：从高截止频率逐渐过渡到均匀采样
- **多视角对抗细化**：频谱 realism、包络一致性、谐波一致性

**实验结果（VCTK & EARS）**：
- 2 kHz 输入：LSD 1.248, NISQA 3.125, STOI 0.8214
- 8 kHz 输入：LSD 1.086, NISQA 4.014, STOI 0.9870
- 不规则带宽泛化性能优异

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：创新性地将 BWE 统一为频谱填充任务，支持任意带宽输入

---

### 11. DroneAudioNet: Noise Suppression for Drone Audition-based Search and Rescue

📝 **作者**：Chitralekha Gupta, Soundarya Ramesh, Yifei Luo, Suranga Nanayakkara  
🏫 **机构**：National University of Singapore  
📰 **arXiv**：2608.00875

**核心方法**：  
- **噪声估计重构**：将源分离模型重新表述为无人机噪声估计器
- **可学习 mask 缩放**：允许 mask 幅度超过 1（解决噪声主导问题）
- **加性残差校正**：额外的复数残差项改进噪声估计和源恢复

**实验结果**：
- 人类语音分类 F1 分数最大提升 10.6%（-20 到 -10 dB SNR）
- 域外泛化：在 DREGON 数据集上有效

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：针对无人机搜救场景的噪声抑制，对低 SNR 有独特优化

---

### 12. SoniSpeech: Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces

📝 **作者**：Ruidong Zhang, Jiacheng Liu, François Guimbretière, Cheng Zhang（康奈尔大学）  
🏫 **机构**：Cornell University  
📰 **arXiv**：2608.00803

**核心方法**：  
- **三模态数据集**：超声回波profile + 有声音频 + 前视视频
- **声学传感眼镜**：使用 FMCW  chirp 捕捉面部运动
- **SODA 对话语料**：当代会话英语，5356 个唯一词汇
- **CTC ResNet-34 基线**：开放词汇无声语音识别 WER 26.3%

**实验结果**：
- 纯无声训练：WER 33.7%（首次基准）
- 有声+无声联合训练：WER 26.3%
- 训练数据规模效应：数据越多性能越好

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：首个大规模可穿戴无声语音接口数据集，推动该领域研究

---

### 13. Beyond Prompt Adherence: Auditing Attribute-Level Voice Control in Speech Generation

📝 **作者**：Xianhao Zhou, Jianghao Wu  
🏫 **机构**：Intelligence 团队  
📰 **arXiv**：2608.00545

**核心方法**：  
- **配对审计**：将条件化输出与中性基线配对比较
- **属性级控制评估**：测量目标属性变化和非目标属性变化
- **VoDER-Cal**：无需训练的候选选择器，保留强目标响应同时偏好更小非目标偏差
- **三候选池**：联合成功率从 4.8% 提升到约 14%

**实验结果**：
- CosyVoice3: deep 响应率 84.4%，但 93.8% 有非目标变化
- VoDER-Cal 在保留目标响应方面优于基线选择

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：首个系统评估语音生成中属性控制保真度的研究

---

## 📋 论文列表汇总

| ID | 方向 | 论文标题 | 机构 | 评分 |
|---|---|---|---|---|
| 2608.01119 | TTS | JoyAI-Talker | 京东 | ⭐⭐⭐⭐⭐ |
| 2608.00722 | TTS | ECCD for LM-based TTS | 清华 | ⭐⭐⭐⭐⭐ |
| 2608.00998 | TTS | Personalized Emotional TTS | 奈良先端 | ⭐⭐⭐⭐ |
| 2608.02023 | TTS | SwanTale | 字节 | ⭐⭐⭐⭐ |
| 2608.01281 | ASR | Latent Softmax Multilingual ASR | 清华 | ⭐⭐⭐⭐ |
| 2608.00186 | ASR | NA-FOMAML CLP Speech | IIT Guwahati | ⭐⭐⭐⭐ |
| 2608.00493 | 安全 | Hidden-Domain Routing | OPPO | ⭐⭐⭐⭐⭐ |
| 2608.00857 | 安全 | REIMU | 西北工大 | ⭐⭐⭐⭐ |
| 2608.00447 | 安全 | NA-SSL ASD | NTT | ⭐⭐⭐⭐⭐ |
| 2608.00572 | 增强 | AnyBand | NUS | ⭐⭐⭐⭐ |
| 2608.00875 | 增强 | DroneAudioNet | NUS | ⭐⭐⭐⭐ |
| 2608.00803 | 接口 | SoniSpeech | Cornell | ⭐⭐⭐⭐⭐ |
| 2608.00545 | 评估 | Voice Control Audit | Intelligence | ⭐⭐⭐⭐ |

---

*本期共 13 篇精选论文，涵盖 TTS、ASR、语音安全、语音增强、无声语音接口等方向。*
