# 语音论文速递 2026-08-07

## 📌 本期亮点

- **LILAC**：首个保证幂等性的神经语音编解码器，解决编解码-重编码循环中的令牌重写问题
- **mHC**：流形约束超连接，替换残差连接提升说话人表示学习性能
- **AffectDF**：最大规模情感语音deepfake检测基准数据集

---

## 🔧 语音合成 (TTS)

### 1. Pixel-TTS: Image based Text Rendering for Robust Text-to-Speech

📝 **作者**：Adarsh Arigala, Arjun Gangwar, S Umesh, Yova Kostedjhieva  
🏫 **机构**：IIT Madras, MBZUAI  
📰 **arXiv**：2606.14750

**核心方法**：
- 将文本渲染为图像，利用2D卷积层生成嵌入，替代传统的字符级嵌入
- 消除跨语言微调时的嵌入矩阵扩展需求
- 基于ADMA架构进行双模态对齐

**实验结果**：
- LibriTTS-R测试集：UTMOS 4.14（0.75 kbit/s）
- 与SOTA sub-1 kbit/s神经编解码器相当
- 零样本跨语言泛化能力强

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：首个视觉 grounded TTS框架，解决字符嵌入的跨语言泛化问题

---

## 🔊 语音编码

### 2. LILAC: An Idempotent Neural Speech Codec

📝 **作者**：June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon  
🏫 **机构**：Seoul National University  
📰 **arXiv**：2608.05727

**核心方法**：
- 全卷积24kHz语音编解码器，码率0.75 kbit/s，latent频率9.375Hz
- 引入有限标量量化（FSQ）保证编解码幂等性：重编码解码后的音频返回完全相同的token流
- 首次从数学上证明编解码器的幂等性保证

**实验结果**：
- LibriSpeech测试集：UTMOS 4.14
- LibriTTS-R测试集：UTMOS 4.24
- 相比12个基线系统，token重写率从平均15%降至0%

**⭐ 评分**：⭐⭐⭐⭐⭐  
**推荐理由**：解决神经编解码器在流水线中重编码导致的质量退化问题，对LLM音频生成有重要意义

---

## 🎯 说话人识别/验证

### 3. Beyond Residual Connections: Manifold-Constrained Hyper-Connections for Robust Speaker Representation Learning

📝 **作者**：Zezhong Jin, Xiaoyu Wang, Zhe Li, Chong-Xin Gan, Zilong Huang, Man-Wai Mak, Kong Aik Lee  
🏫 **机构**：The Hong Kong Polytechnic University, Baidu Inc., The University of Hong Kong  
📰 **arXiv**：2608.05549  
📝 **备注**：已接收至INTERSPEECH 2026

**核心方法**：
- Manifold-Constrained Hyper-Connections (mHC)：将残差路径重新表述为多流演化
- 使用Sinkhorn-Knopp迭代确保能量守恒（保留信号强度和特征均值）
- 替换ECAPA-TDNN、ResNet-34、Res2Net、E-Res2Net中的标准残差连接

**实验结果**（VoxCeleb1）：
- 所有架构一致提升性能
- 稳定梯度传播，缓解复杂网络中的信号退化

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：从残差连接到超连接的范式转变，提升说话人表示的鲁棒性

---

## 🛡️ 语音深度伪造检测

### 4. AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks

📝 **作者**：Aurosweta Mahapatra, Xiutian Zhao, Shreeram Suresh Chandra, Zihan Zhang, Zongyang Du, Ismail Rasim Ulgen, Kong Aik Lee, Nicholas Andrews, Carlos Busso, Berrak Sisman  
🏫 **机构**：Johns Hopkins University, Hong Kong Polytechnic University, Carnegie Mellon University  
📰 **arXiv**：2608.05507

**核心方法**：
- 覆盖TTS、VC、情感VC、LALM攻击的语音deepfake基准
- 包含约260小时语音，21种攻击，5种情感状态
- 涵盖表演和自发情感语音

**实验结果**：
- 现有SDD系统在情感条件评估时性能严重下降
- 大规模情感训练不能一致提升跨域鲁棒性
- 情感状态、攻击家族、表演vs自发条件间鲁棒性差异显著

**⭐ 评分**：⭐⭐⭐⭐  
**推荐理由**：首个大规模情感语音deepfake基准，揭示当前SDD系统的fundamental limitation

---

## 📡 其他语音相关论文

### 5. Rethinking Automatic Music Mixing as Sequential Stem Blending

📝 **作者**：Yen-Tung Yeh, Chung-Jui Chan, Yun-Ning (Amy) Hung, Yi-Hsuan Yang  
📰 **arXiv**：2608.05506

**核心方法**：将自动音乐混音重新定义为顺序stem融合任务，使用latent流匹配模型

---

### 6. EG-VAE: A Unified Framework for Electric Guitar Tone Transfer and Removal

📝 **作者**：Yen-Tung Yeh, Yun-Ning (Amy) Hung, Yi-Hsuan Yang  
📰 **arXiv**：2608.05513

**核心方法**：统一建模电吉他音色迁移和去除，使用变分自编码器解耦内容与音色表示

---

### 7. PD-GS: Phoneme-Driven 3DGS for Audio-Driven Talking Heads

📝 **作者**：Ao Fu, Yi Zhou  
📰 **arXiv**：2608.05218  
📝 **备注**：已接收至ACM MM 2026

**核心方法**：引入音素驱动的3D Gaussian Splatting，通过语言融合模块（LFM）融合音频上下文与音素嵌入

---

### 8. Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming

📝 **作者**：Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
📰 **arXiv**：2608.05663

**核心方法**：实时长语音视频生成框架，使用Teacher Forcing + Diffusion Forcing混合训练和DMD蒸馏

---

### 9. PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs

📝 **作者**：Artem Dementyev, Wazeer Zulfikar, Sinan Hersek, Pascal Getreuer, Anurag Kumar, Vivek Kumar  
📰 **arXiv**：2601.21124

**核心方法**：麦克风几何无关的空间音频编码器，实现任意麦克风阵列的定位和空间推理

---

### 10. EchoEdit: Stabilizing Inversion-Free Audio Editing via Optimal Transport Geometry

📝 **作者**：Zhongyuan Fu, Yuhang Jia, Hui Wang, Pengjun Chen, Jian Gao, Cun Liu, Wenjia Zeng, Yong Chen, Yong Qin  
📰 **arXiv**：2606.15149

**核心方法**：无 inversion 音频编辑框架，通过最优传输正则化稳定编辑路径

---

### 11. Temporal Pooling Strategies for Training-Free Anomalous Sound Detection

📝 **作者**：Kevin Wilkinghoff, Sarthak Yadav, Zheng-Hua Tan  
📰 **arXiv**：2603.04605

**核心方法**：提出相对偏差池化（RDP）和广义均值池化（GeM），在DCASE2025 ASD数据集上达到SOTA

---

### 12. Integrating Human Linguistic Insights into AI: Theory-Driven Representation for Multilingual Text-to-Speech

📝 **作者**：Cong Zhang, Huinan Zeng, Huang Liu, Jiewen Zheng  
📰 **arXiv**：2204.07228  
📝 **备注**：已接收至Phonetica

**核心方法**：使用Featurally Underspecified Lexicon (FUL)作为理论驱动的TTS输入表示

---

### 13. Speaker Verification Under Real Classroom Conditions for English Speech

📝 **作者**：Saba Tabatabaee, Jing Liu, Meghavarshini Krishnasamy, Carol Espy-Wilson  
📰 **arXiv**：2608.03623

**核心方法**：在真实教室环境下进行说话人验证，使用WavLM-TDNN模型

---

### 14. Identity-Faithful Audio-Visual Target Speaker Extraction with REAL-2MIX and VOXBLINK2-AVSE

📝 **作者**：Peijun Yang, Zhan Jin, Xiaoyi Qin, Ruiyi Gan, Hao Wang, Juan Liu, Ming Li  
📰 **arXiv**：2608.03964

**核心方法**：提出REAL-2MIX基准数据集，使用AV-HuBERT特征进行目标说话人提取

---

### 15. MoDAl: Self-Supervised Neural Modality Discovery via Decorrelation for Speech Neuroprosthesis

📝 **作者**：Yuanhao Chen, Peter Chin  
📰 **arXiv**：2605.00025  
📝 **备注**：已接收至ICMI 2026

**核心方法**：通过对比学习和解相关目标发现互补神经模态，在Brain-to-Text Benchmark '24上WER从26.3%降至21.6%

---

### 16. A Study of ASR Adaptation and Representation Dimensionality Reduction in Persian Speech Emotion Recognition Using Whisper

📝 **作者**：Ali Shendabadi, Parnia Izadirad, Mostafa Salehi  
📰 **arXiv**：2608.05165

**核心方法**：使用Whisper进行波斯语语音情感识别，研究ASR适配和表示维度压缩

---

## 📊 论文统计

- 本期共筛选语音相关论文：**16篇**
- 分类统计：
  - TTS：3篇
  - 语音编码：1篇
  - 说话人识别：3篇
  - 语音检测：2篇
  - 音频生成/编辑：4篇
  - 音乐/音频处理：3篇
