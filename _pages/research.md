---
layout: page
permalink: /research/
title: Research
description: 
nav: true
nav_order: 1
---


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/framework.png" title="research image" %}
    </div>
</div>

<!-- src="https://img.shields.io/github/stars/sail-sg/EditAnything?style=social" > -->

My research target is to build **”efficient and effective artificial intelligent systems”** so that machines can cognize, understand and interact with the environment. Currently, I mainly focus on three research topics across machine learning, computer vision and optimization.   


**1) Efficiency	Optimization**: improve the efficiency of training (including fine-tuning) and inference efficiency for AI models like LLMs.

  * **a) Faster Training Algorithms/Optimizers**: design more effective and efficient optimizers to faster train AI models especially for LLMs. 
    * <details> 
        <summary> <strong>Faster Optimizer</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/abs/2208.06677">Adan</a></strong> (TPAMI, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/Adan?style=social" >
        </iframe>) is about 2x faster than the SoTA optimizers, e.g. Adam, while achieving higher or comparable performance on many networks, e.g., CNNs, ViTs and MAE in the CV field, UNet and ViTs in AIGC field, GPT2 and billion-scale LLaMA in the NLP field, networks in RL tasks. It has been included in popular deep-learning codebases, e.g.,  <a href="https://github.com/NVIDIA/NeMo/blob/main/nemo/core/optim/adan.py">NVIDIA NeMo</a> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/NVIDIA/NeMo?style=social" >
        </iframe>) for training large language models and multi-modal models,  <a href="https://github.com/huggingface/pytorch-image-models/blob/main/timm/optim/adan.py">HuggingFace Timm</a> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/huggingface/pytorch-image-models?style=social" >
        </iframe>) and <a href="https://github.com/open-mmlab/mmpretrain/blob/dev-1.x/mmcls/engine/optimizers/adan_t.py">OpenMMLab</a> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/open-mmlab/mmpretrain?style=social" >
        </iframe>) which both train AI models for CV tasks like classification, detection and segmentation, <a href="https://github.com/Jittor/jittor/blob/master/python/jittor/optim.py">Jittor of Tsinghua University</a> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/Jittor/jittor?style=social" >
        </iframe>) for 3D generation, and is the default optimizer in <a href="https://github.com/ashawkey/stable-dreamfusion/blob/main/optimizer.py">DreamFusion</a> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/ashawkey/stable-dreamfusion?style=social" >
        </iframe>) and <a href="https://arxiv.org/abs/2303.14389">MDT</a>  (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/MDT?style=social" >
        </iframe>) for SoTA 3D and image generation tasks respectively.
        
        
        <p>See more works, e.g., <strong><a href="https://proceedings.neurips.cc/paper_files/paper/2021/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf">SLRLA</a></strong> (NeurIPS, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/SLRLA-optimizer?style=social" >
        </iframe>) which improves lookahead,  <strong><a href="https://ieeexplore.ieee.org/document/8792163">R-SPIDER</a></strong> (TPAMI & AISTATS), and  <strong><a href="https://arxiv.org/pdf/2009.09835.pdf">HSDMPG</a></strong> (ICML & TPAMI). </p>
        
        </details> 


    * <details> 
        <summary> <strong>Plug-and-play Acceleration Framework</strong> (click here for representative works)</summary>

        <strong><a href="../assets/pdf/2024-JMLR-win.pdf">Win</a></strong> (JMLR & ICLR, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/win?style=social" >
        </iframe>)  can accelerate AdamW, Adam, LAMB and SGD by 1.5X on vision classification tasks and language modeling tasks with both CNN and Transformer backbones.   
        
        </details> 
        


    * <details> 
        <summary> <strong>Network Optimization Theory</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/pdf/2010.05627.pdf">This work</a></strong> (NeurIPS, 200+ citations
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/salesforce/comparison_SGD_ADAM?style=social" >
        </iframe>) provides the first theory to explain  "why SGD generalizes better than ADAM in deep learning".  See more works like <strong><a href="https://proceedings.neurips.cc/paper_files/paper/2021/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf">SLRLA</a></strong> (NeurIPS, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/SLRLA-optimizer?style=social" >
        </iframe>) to analyzes  "why Lookahead generalizes better than SGD". 
        
        </details> 



  * **b) Inference Acceleration of AI Models like LLMs**: design faster inference techniques for AI models like LLMs and multimodal models.
    * <details> 
        <summary> <strong>Inference Acceleration of (multimodal) LLMs</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/pdf/2509.22134">GTO</a></strong> is the first one that aligns the training and inference decoding objectives in speculative decoding, and can accelerate the vanilla auto-regressive decoding by around 4 times. See more works like <strong><a href="https://arxiv.org/abs/2502.11018">GRIFFIN</a></strong> (NeurIPS).
        

        </details> 


**2)	Learning Framework**: design effective learning framework / training task / loss to formulate a problem so that the AI models can learn desired knowledge to handle general / specific tasks. 


  * **a) Self-Supervised (multi-modal) Learning**: design effective and efficient self-supervised (multi-modal) learning frameworks that enable AI models to learn desired  knowledge and achieve human's data understanding and reasoning ability. 
    * <details> 
        <summary> <strong>Single-modal Learning</strong> (click here for representative works)</summary>

        <strong><a href="https://openreview.net/pdf?id=KmykpuSrjcq">PCL</a></strong> (ICLR, 800+ citations, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/salesforce/PCL?style=social" >
        </iframe>) is the first clustering contrastive learning method to learn data cluster structure,  and its improved version, <strong><a href="https://arxiv.org/abs/2203.14415">Mugs</a></strong> (<iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/mugs?style=social" >
        </iframe>), develops multi-granular contrastive learning for multi-granular representation learning. See more works like <strong><a href="https://arxiv.org/pdf/2106.14749.pdf">SANE</a></strong> (NeurIPS, spotlight), <strong><a href="https://arxiv.org/abs/2210.11016">TEC</a></strong>, and <strong><a href="https://arxiv.org/pdf/2106.09645.pdf">PGCL</a></strong> (TNNLS).
        

        </details> 

    * <details> 
        <summary> <strong>Multi-modal Learning</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/pdf/2212.09737.pdf">PTP</a></strong> (TPAMI & CVPR, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/ptp?style=social" >
        </iframe>) is the pioneer to enhance grounding ability in multi-modal models, and <strong><a href="https://arxiv.org/abs/2405.14974">LOVA<sup>3</sup></a></strong> is to empower models with humans' ability, including the answering, asking and accessing ability. See more works like <strong><a href="https://arxiv.org/abs/2312.02439">CLOT</a></strong>(CVPR, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/CLoT?style=social" >
        </iframe>) for exploring humans' creativity, <strong><a href="https://arxiv.org/abs/2302.13668">CoVGT</a></strong>  (TPAMI & ECCV, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/doc-doc/CoVGT?style=social" >
        </iframe>) for video question answering,         <strong><a href="https://arxiv.org/abs/2312.06731">Genixer</a></strong> (ECCV) to empower multi-modal models as a powerful data generator,  <strong><a href="https://arxiv.org/pdf/2109.09161.pdf">Wav-BERT</a></strong> (AAAI) for acoustic and linguistic representation learning.

        </details> 


    * <details> 
        <summary> <strong>Agentic Learning</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/abs/2411.04679">CaPo</a></strong> (ICLR) introduces a two-phase cooperation framework—meta-plan generation followed by progress-adaptive execution—enabling LLM-based agents to form coherent long-term plans and refine them dynamically via multi-turn discussions, eliminating redundant actions and improving efficiency. Then  <strong><a href="https://panzhous.github.io/assets/pdf/2025-CVPR-CoTS.pdf">CoTS</a></strong> (CVPR) incorporates an LLM-driven Monte Carlo tree search and a plan-evaluation module that stabilizes updates and ensures timely plan revisions, further enhancing the scalability and reliability of multi-agent collaboration.
        

        </details> 

  * **b) Generative Models**: design  generative models like diffusion models that generate image/3D/video data and empower AI models with imagination and creativity akin to that of humans. 
      * <details> 
        <summary> <strong>Image Generation</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/abs/2303.14389">MDT</a></strong> (ICCV,
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="335px" height="20px"
            src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/masked-diffusion-transformer-is-a-strong/image-generation-on-imagenet-256x256" >
        </iframe>,
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/MDT?style=social" >
        </iframe>) achieves SoTA image synthesis performance on ImageNet (256x256), and improves the learning speed of <a href="https://arxiv.org/abs/2212.09748">DiT</a> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/facebookresearch/DiT?style=social" >
        </iframe>), the core component of <a href="https://openai.com/sora">SORA</a>, by at least 10x.  See more works like <strong><a href="https://github.com/sail-sg/EditAnything">EditAnything</a></strong>  (ACMMM, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/EditAnything?style=social" >
        </iframe>), <strong><a href="https://arxiv.org/abs/2306.06991">FDT</a></strong> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/FDM?style=social" >
        </iframe>), <strong><a href="https://arxiv.org/pdf/2310.13545.pdf">ScaleLong</a></strong>  (NeurIPS, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/ScaleLong?style=social" >
        </iframe>), and <strong><a href="https://arxiv.org/pdf/2006.06900.pdf">PPOGAN</a></strong>  (NeurIPS, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/Holmeswww/PPOGAN?style=social" >
        </iframe>).
        </details> 

    * <details> 
        <summary> <strong>3D Generation</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/abs/2401.09050">Consistent3D</a></strong> (CVPR, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/sail-sg/Consistent3D?style=social" >
        </iframe>) is the pioneer to use ODE sampling as guidance in text-to-3D task, overcoming the unpredicable and unstable SDE guidance in  <a href="https://arxiv.org/abs/2209.14988">SDS/DreamFusion</a>. See more works, e.g., <strong><a href="ttps://github.com/yxymessi/DTC123/blob/main/DTC_CVPR.pdf">DTC123</a></strong> (CVPR, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/yxymessi/DTC123?style=social" >
        </iframe>) and <strong><a href="https://arxiv.org/abs/2403.18795">Gamba</a></strong>  for image-to-3D generation, <strong><a href="https://arxiv.org/abs/2311.08403">Instant3D</a></strong> (IJCV, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://img.shields.io/github/stars/ming1993li/Instant3DCodes?style=social" >
        </iframe>) for fast text-to-3D task.


        </details> 


  <!-- * **c) Meta In-Context Learning**: design new meta-learning and prompt learning methods to aid a (pretrained) model in quickly learning from a few data, improving few-shot learning ability of AGI.  -->

**3)	Network Architecture Design**: develop innovative network topology that posses high capacity and efficiency for acquiring knowledge, thereby improving the overall model capacity of AI.
* <details> 
    <summary> <strong>Manually-Designed Network</strong> (click here for representative works)</summary>

    <strong><a href="https://arxiv.org/abs/2111.11418#:~:text=Based%20on%20the%20extensive%20experiments,on%20the%20token%20mixer%20modules.">MetaFormer</a></strong> (CVPR ORAL, 600+ citations, 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://img.shields.io/github/stars/sail-sg/poolformer?style=social" >
    </iframe>) replaces self-attention in ViT with pooling and convolutions independently,  and achieves impressive performance, breaking the slogan “self-attention is all you need”. It reveals network design princeples that if a network contains two kinds of operations, including  spatial information exchanging operations (e.g., attention, pooling and convolution) and  channel information exchanging operations  (e.g., MLP), then the network can perfor well.  Its improved version CAFormer network sets a new recording accuracy of 85.5% on ImageNet under supervised settings without extra training data, and achives top-2 performance on ImageNet-C( 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="400px" height="20px"
        src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/metaformer-baselines-for-vision/domain-generalization-on-imagenet-c" >
    </iframe>). See more works like <strong><a href="https://arxiv.org/abs/2205.12956">IFormer</a></strong>  (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://img.shields.io/github/stars/sail-sg/iFormer?style=social" >
    </iframe>), <strong><a href="https://arxiv.org/abs/2303.16900">InceptionNeXt</a></strong>  (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://img.shields.io/github/stars/sail-sg/inceptionnext?style=social" >
    </iframe>), <strong><a href="https://arxiv.org/abs/2112.04674">DualFormer</a></strong> (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://img.shields.io/github/stars/sail-sg/dualformer?style=social" >
    </iframe>), and <strong><a href="https://arxiv.org/abs/2203.07057">SUN</a></strong>  (ECCV, 
    <iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/DongSky/few-shot-vit?style=social" >
    </iframe>).

    </details> 

 


* <details> 
    <summary> <strong>Automatically-Designed Network</strong> (click here for representative works)</summary>

    <strong><a href="https://arxiv.org/abs/2006.16537">PR-DARTS</a></strong> (NeurIPS ORAL, 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://img.shields.io/github/stars/salesforce/PR-DARTS?style=social" >
    </iframe>)  automatically designs effective network architectures, reducing the reliance on expert trial and error. It provides the first theory to show why previous network search methods (a.k.a. AutoML) often collapse due to selecting too many skip-connections, and then proposes a new method that can avoid previous collapse and thus automatically selects and combines various network operations, e.g. pooling and convolution, to search more effective network.
    
    </details> 




