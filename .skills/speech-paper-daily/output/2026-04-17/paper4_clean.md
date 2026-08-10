##  

## [4] Towards Fine-grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt

**arXiv ID**: 2604.13715
****: 
****: Yanfeng Shi, Pengfei Cai, Jun Liu, Qing Gu, Nan Jiang, Lirong Dai, Ian McLoughlin, Yan Song
****: University of Science and Technology of China, Singapore Institute of Technology
****: 2026-04-15
****: [URL]
**PDF **: [URL]
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
