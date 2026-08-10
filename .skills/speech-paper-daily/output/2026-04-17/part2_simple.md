
---

##  

## [4] Towards Fine-grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt

**arXiv ID**: 2604.13715
****: 
****: Yanfeng Shi, Pengfei Cai, Jun Liu, Qing Gu, Nan Jiang, Lirong Dai, Ian McLoughlin, Yan Song
****: University of Science and Technology of China, Singapore Institute of Technology
****: 2026-04-15
****: https://arxiv.org/abs/2604.13715
**PDF **: https://arxiv.org/pdf/2604.13715.pdf
****: 
**Demo **: 

###  
TimePro-RL(LALMs)Audio-Side Time PromptAudio GroundingSound Event DetectionDense Audio Captioning

###  

****Qwen2-Audio/Qwen2.5-Omnitokenizer750Timestamp Tokens0-30sstride=0.04sTimestamp Embeddingsubword embeddings

****
1. Audio-Side Time Prompt (ASTP)
2. Timestamp Embeddingsubword embeddings
3. Event-based F1 (r_main)mIoU/METEOR (r_aux)

****
- SFT: 3 epochs, lr=1e-5, LoRA (r=8, =32)
- RL: GRPO, 1 epoch, lr=1e-6, group size=4, subset=10,200 samples
- Eb-F1=1e-6

###  
****FTAR (Audio Grounding)DESED (Sound Event Detection)FTAR (Dense Audio Captioning)
****
- Audio Grounding: R@0.5 80.1%, R@0.7 66.3%, R@0.9 39.8%, mIoU 74.4%
- Sound Event Detection: Eb-F1 57.6%
- Dense Audio Captioning: METEOR 33.9%, Eb-F1 40.7%

****

###  8/10
****Audio-Side Time Prompt + RL

---

## [5] Graph Propagated Projection Unlearning: A Unified Framework for Vision and Audio Discriminative Models

**arXiv ID**: 2604.13127
****: 
****: Shreyansh Pathak, Jyotishman Das
****: Indian Institute of Technology Jodhpur
****: 2026-04-13
****: https://arxiv.org/abs/2604.13127
**PDF **: https://arxiv.org/pdf/2604.13127.pdf
****: 
**Demo **: 

###  
Graph-Propagated Projection Unlearning (GPPU)10-20

###  

****ResNetsVision TransformersAudio Transformers (Wav2Vec2/HuBERT)

****
1. Graph-based Forget Directionk-NNk=8forget direction g_c
2. Projection-Based Unlearningforget directionh_proj = h - (hg)g
3. Projection Loss + Retention LossL_projforget directionL_retain

****
- ViT: 1-2 transformer blocks, CNN: final conv block, Audio: 2-3 transformer layers
- _proj=1.0, _retain=0.5, lr=1e-5, epochs=3, weight decay=1e-2
- FAISSk-NN

###  
****CIFAR-10/100SVHNFlowers102STL-10FashionMNISTLibriSpeech-100hSpeechCommands v2VoxCeleb1
****
- Forget Accuracy1/C
- Retain Accuracy
- 10-20 vs Fisher Forgetting/Gradient Ascent
- VoxCeleb1: Speaker 10005

****

###  8/10
****Graph propagation + Projection unlearning10-20/

---

## [6] Few-Shot and Pseudo-Label Guided Speech Quality Evaluation with Large Language Models

**arXiv ID**: 2604.13528
****: 
****: Ryandhimas E. Zezario, Dyah A. M. G. Wisnu, Szu-Wei Fu, Sabato Marco Siniscalchi, Hsin-Min Wang, Yu Tsao
****: 
****: 2026-04-15
****: https://arxiv.org/abs/2604.13535
**PDF **: https://arxiv.org/pdf/2604.13528.pdf
****: 
**Demo **: 

###  
GatherMOSGatherMOSRMSZCRMFCCDNSMOS/VQScoreLLMMOSVoiceBank-DEMANDGatherMOSDNSMOSVQScoreCNN-BLSTM/MOS-SSL

###  

****GPT-5 + MOS

****
1. Meta-EvaluatorLLMDNSMOS/VQScore
2. Zero-shot vs Few-shotzero-shotfew-shot
3. MFCC + spectrogram statistics

****
- RMSZCRclipping ratiodurationMFCC13mel-spectrogram statistics
- Zero-shot
- Few-shotKcontext
- minibatch=10session resetcross-sample conditioning

###  
****VoiceBank-DEMAND (200 utterances, 10 listeners)
****
- GatherMOS-ZS: LCC 0.6439, SRCC 0.6014
- GatherMOS-ZS* (with MFCC/spectrogram): LCC 0.6495, SRCC 0.6069
- vs DNSMOS: LCC 0.6021, SRCC 0.5314
- vs VQScore: LCC 0.5753, SRCC 0.4476
- vs CNN-BLSTM (limited data): LCC 0.3192, SRCC 0.2971
- vs MOS-SSL (limited data): LCC 0.4888, SRCC 0.4732

****

###  7/10
****LLM

---

*Speech-paper-daily    arXiv*