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
        {% include figure.liquid loading="eager" path="assets/img/research7.jpg" title="research image" %}
    </div>
</div>



My research target is to build **”efficient and effective artificial intelligent systems”** so that machines can cognize, understand and interact with the environment. Currently, I mainly focus on three research topics across machine learning, computer vision and optimization.   

**1)	Learning Framework**: design effective learning framework / training task / loss to formulate a problem so that the AI models can learn desired knowledge to handle general / specific tasks. 


  * **a) Self-Supervised (multi-modal) Learning**: design effective and efficient self-supervised (multi-modal) learning frameworks that enable AI models to learn desired  knowledge and achieve human's data understanding and reasoning ability. 
    * <details> 
        <summary> <strong>Single-modal Learning</strong> (click here for representative works)</summary>

        <strong><a href="https://openreview.net/pdf?id=KmykpuSrjcq">PCL</a></strong> (ICLR, 800+ citations, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PCL&type=star&count=true" >
        </iframe>) is the first clustering contrastive learning method to learn data cluster structure,  and its improved version, <strong><a href="https://arxiv.org/abs/2203.14415">Mugs</a></strong> (<iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=mugs&type=star&count=true" >
        </iframe>), develops multi-granular contrastive learning for multi-granular representation learning. See more works like <strong><a href="https://arxiv.org/pdf/2106.14749.pdf">SANE</a></strong>(NeurIPS, spotlight), <strong><a href="https://arxiv.org/abs/2210.11016">TEC</a></strong>, and <strong><a href="https://arxiv.org/pdf/2106.09645.pdf">PGCL</a></strong> (TNNLS).
        

        </details> 

    * <details> 
        <summary> <strong>Multi-modal Learning</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/pdf/2212.09737.pdf">PTP</a></strong> (CVPR & TPAMI, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ptp&type=star&count=true" >
        </iframe>) is the pioneer to enhance grounding ability in multi-modal models, and LOVA<sup>3</sup> is to enpower models with humans' ability, including the answering, asking and accessing ability. See more works like <strong><a href="https://arxiv.org/abs/2312.02439">CLOT</a></strong>(CVPR, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=CLoT&type=star&count=true" >
        </iframe>) for exploring humans' creativity, <strong><a href="https://arxiv.org/abs/2302.13668">CoVGT</a></strong>  (TPAMI & ECCV, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=doc-doc&repo=CoVGT&type=star&count=true" >
        </iframe>) for video question answering,         <strong><a href="https://arxiv.org/abs/2312.06731">Genixer</a></strong> to empower multi-modal models as a powerful data generator,  <strong><a href="https://arxiv.org/pdf/2109.09161.pdf">Wav-BERT</a></strong> (AAAI) for acoustic and linguistic representation learning.

        </details> 


  * **b) Generative Models**: design  generative models like diffusion models that generate image/3D/video data and empower AI models with imagination and creativity akin to that of humans. 
      * <details> 
        <summary> <strong>Image Generation</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/abs/2303.14389">MDT</a></strong> (ICCV,
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="400px" height="20px"
            src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/masked-diffusion-transformer-is-a-strong/image-generation-on-imagenet-256x256" >
        </iframe>,
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=MDT&type=star&count=true" >
        </iframe>) achieves SoTA image synthesis performance on ImageNet (256x256), and improves the learning speed of <a href="https://arxiv.org/abs/2212.09748">DiT</a> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=facebookresearch&repo=DiT&type=star&count=true" >
        </iframe>), the core component of <a href="https://openai.com/sora">SORA</a>, by at least 10x.  See more works like <strong><a href="https://github.com/sail-sg/EditAnything">EditAnything</a></strong>  (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=EditAnything&type=star&count=true" >
        </iframe>), <strong><a href="https://arxiv.org/abs/2306.06991">FDT</a></strong> (
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=FDM&type=star&count=true" >
        </iframe>), <strong><a href="https://arxiv.org/pdf/2310.13545.pdf">ScaleLong</a></strong>  (NeurIPS, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ScaleLong&type=star&count=true" >
        </iframe>), and <strong><a href="https://arxiv.org/pdf/2006.06900.pdf">PPOGAN</a></strong>  (NeurIPS, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=Holmeswww&repo=PPOGAN&type=star&count=true" >
        </iframe>).
        </details> 

    * <details> 
        <summary> <strong>3D Generation</strong> (click here for representative works)</summary>

        <strong><a href="https://arxiv.org/abs/2401.09050">Consistent3D</a></strong> (CVPR, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Consistent3D&type=star&count=true" >
        </iframe>) is the pioneer to use ODE sampling as guidance in text-to-3D task, overcoming the unpredicable and unstable SDE guidance in  <a href="https://arxiv.org/abs/2209.14988">SDS/DreamFusion</a>. See more works, e.g., <strong><a href="ttps://github.com/yxymessi/DTC123/blob/main/DTC_CVPR.pdf">DTC123</a></strong> (CVPR, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=yxymessi&repo=DTC123&type=star&count=true" >
        </iframe>) and <strong><a href="https://arxiv.org/abs/2403.18795">Gamba</a></strong>  for image-to-3D generation, <strong><a href="https://arxiv.org/abs/2311.08403">Instant3D</a></strong> (IJCV, 
        <iframe
            style="margin-left: 2px; margin-bottom:-5px;"
            frameborder="0" scrolling="0" width="91px" height="20px"
            src="https://ghbtns.com/github-btn.html?user=ming1993li&repo=Instant3DCodes&type=star&count=true" >
        </iframe>) for fast text-to-3D task.


        </details> 


  <!-- * **c) Meta In-Context Learning**: design new meta-learning and prompt learning methods to aid a (pretrained) model in quickly learning from a few data, improving few-shot learning ability of AGI.  -->

**2)	Network Architecture Design**: develop innovative network topology that posses high capacity and efficiency for acquiring knowledge, thereby improving the overall model capacity of AI.
* <details> 
    <summary> <strong>Manually-Designed Network</strong> (click here for representative works)</summary>

    <strong><a href="https://arxiv.org/abs/2111.11418#:~:text=Based%20on%20the%20extensive%20experiments,on%20the%20token%20mixer%20modules.">MetaFormer</a></strong> (CVPR ORAL, 600+ citations, 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=poolformer&type=star&count=true" >
    </iframe>) replaces self-attention in ViT with pooling and convolutions independently,  and achieves impressive performance, breaking the slogan “self-attention is all you need”. It reveals network design princeples that if a network contains two kinds of operations, including  spatial information exchanging operations (e.g., attention, pooling and convolution) and  channel information exchanging operations  (e.g., MLP), then the network can perfor well.  Its improved version CAFormer network sets a new recording accuracy of 85.5% on ImageNet under supervised settings without extra training data, and achives top-2 performance on ImageNet-C( 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="400px" height="20px"
        src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/metaformer-baselines-for-vision/domain-generalization-on-imagenet-c" >
    </iframe>). See more works like <strong><a href="https://arxiv.org/abs/2205.12956">IFormer</a></strong>  (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=iFormer&type=star&count=true" >
    </iframe>), <strong><a href="https://arxiv.org/abs/2303.16900">InceptionNeXt</a></strong>  (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=inceptionnext&type=star&count=true" >
    </iframe>), <strong><a href="https://arxiv.org/abs/2112.04674">DualFormer</a></strong> (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=dualformer&type=star&count=true" >
    </iframe>), and <strong><a href="https://arxiv.org/abs/2203.07057">SUN</a></strong>  (ECCV, 
    <iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=DongSky&repo=few-shot-vit&type=star&count=true" >
    </iframe>).

    </details> 

 


* <details> 
    <summary> <strong>Automatically-Designed Network</strong> (click here for representative works)</summary>

    <strong><a href="https://arxiv.org/abs/2006.16537">PR-DARTS</a></strong> (NeurIPS ORAL, 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PR-DARTS&type=star&count=true" >
    </iframe>)  automatically designs effective network architectures, reducing the reliance on expert trial and error. It provides the first theory to show why previous network search methods (a.k.a. AutoML) often collapse due to selecting too many skip-connections, and then proposes a new method that can avoid previous collapse and thus automatically selects and combines various network operations, e.g. pooling and convolution, to search more effective network.
    
    </details> 




**3)	Parameter Optimizer**: design efficient optimizers to train AI models efficiently.
* <details> 
    <summary> <strong>Faster Optimizer</strong> (click here for representative works)</summary>

    <strong><a href="https://arxiv.org/abs/2208.06677">Adan</a></strong> (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Adan&type=star&count=true" >
    </iframe>) is about 2x faster than the SoTA optimizers, e.g. Adam, while achieving higher or comparable performance on many networks, e.g., CNNs, ViTs and MAE in the CV field, UNet and ViTs in AIGC field, GPT2 and billion-scale LLaMA in the NLP field, networks in RL tasks. It has been included in popular deep-learning codebases, e.g.,  <a href="https://github.com/NVIDIA/NeMo/blob/main/nemo/core/optim/adan.py">NVIDIA NeMo</a> (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=NVIDIA&repo=NeMo&type=star&count=true" >
    </iframe>) for training large language models and multi-modal models,  <a href="https://github.com/huggingface/pytorch-image-models/blob/main/timm/optim/adan.py">HuggingFace Timm</a> (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=huggingface&repo=pytorch-image-models&type=star&count=true" >
    </iframe>) and <a href="https://github.com/open-mmlab/mmpretrain/blob/dev-1.x/mmcls/engine/optimizers/adan_t.py">OpenMMLab</a> (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=open-mmlab&repo=mmpretrain&type=star&count=true" >
    </iframe>) which both train AI models for CV tasks like classification, detection and segmentation, <a href="https://github.com/Jittor/jittor/blob/master/python/jittor/optim.py">Jittor of Tsinghua University</a> (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=Jittor&repo=jittor&type=star&count=true" >
    </iframe>) for 3D generation, and is the default optimizer in <a href="https://github.com/ashawkey/stable-dreamfusion/blob/main/optimizer.py">DreamFusion</a> (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=ashawkey&repo=stable-dreamfusion&type=star&count=true" >
    </iframe>) and <a href="https://arxiv.org/abs/2303.14389">MDT</a>  (
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=MDT&type=star&count=true" >
    </iframe>) for SoTA 3D and image generation tasks respectively.
    
    
    <p>See more works, e.g., <strong><a href="https://proceedings.neurips.cc/paper_files/paper/2021/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf">SLRLA</a></strong> (NeurIPS, 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=SLRLA-optimizer&type=star&count=true" >
    </iframe>) which improves lookahead,  <strong><a href="https://ieeexplore.ieee.org/document/8792163">R-SPIDER</a></strong> (TPAMI & AISTATS), and  <strong><a href="https://arxiv.org/pdf/2009.09835.pdf">HSDMPG</a></strong> (ICML & TPAMI). </p>
    
    </details> 


* <details> 
    <summary> <strong>Plug-and-play Acceleration Framework</strong> (click here for representative works)</summary>

    <strong><a href="../assets/pdf/2024-JMLR-win.pdf">Win</a></strong> (JMLR & ICLR, 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" >
    </iframe>)  can accelerate AdamW, Adam, LAMB and SGD by 1.5X on vision classification tasks and language modeling tasks with both CNN and Transformer backbones.   
    
    </details> 
    


* <details> 
    <summary> <strong>Network Optimization Theory</strong> (click here for representative works)</summary>

    <strong><a href="https://arxiv.org/pdf/2010.05627.pdf">This work</a></strong> (NeurIPS, 200+ citations
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=salesforce&repo=comparison_SGD_ADAM&type=star&count=true" >
    </iframe>) provides the first theory to explain  "why SGD generalizes better than ADAM in deep learning".  See more works like <strong><a href="https://proceedings.neurips.cc/paper_files/paper/2021/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf">SLRLA</a></strong> (NeurIPS, 
    <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="91px" height="20px"
        src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=SLRLA-optimizer&type=star&count=true" >
    </iframe>) to analyzes  "why Lookahead generalizes better than SGD". 
    
    </details> 
 
