---
layout: page
permalink: /publication/
title: Publication
description: 
nav: true
nav_order: 2
---



You can also browse my <a href="https://scholar.google.com/citations?user=0b7ZqlcAAAAJ&hl=en" target="_blank" style="text-decoration:underline;">Google Scholar profile</a>.  <strong><sup>*</sup></strong> denotes equal contribution; <strong><sup>+</sup></strong> denotes corresponding author.

  <br>

<style>
.biblist { }

/* The item */
.biblist li { }

/* You can define custom styles for plstyle field here. */


/*************************************
   The box that contain BibTeX code
 *************************************/
div.noshow { display: none; }
div.bibtex {
  margin-right: 0%;
  margin-top: 1.2em;
  margin-bottom: 1.3em;
  border: 1px solid silver;
  padding: 0.3em 0.5em;
  background: #eeeeee;
}
div.bibtex pre { font-size: 75%; overflow: auto;  width: 100%; }
</style>

<script>
function toggleBibtex(articleid) {
  var bib = document.getElementById('bib_'+articleid);
  if (bib) {
    if(bib.className.indexOf('bibtex') != -1) {
    bib.className.indexOf('noshow') == -1?bib.className = 'bibtex noshow':bib.className = 'bibtex';
    }
  } else {
    return;
  }
}
</script>


##### **Featured Publications** 

<!-- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/masked-diffusion-transformer-is-a-strong/image-generation-on-imagenet-256x256)](https://paperswithcode.com/sota/image-generation-on-imagenet-256x256?p=masked-diffusion-transformer-is-a-strong)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mugs-a-multi-granular-self-supervised/self-supervised-image-classification-on)](https://paperswithcode.com/sota/self-supervised-image-classification-on?p=mugs-a-multi-granular-self-supervised) -->

<!-- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/masked-diffusion-transformer-is-a-strong/image-generation-on-imagenet-256x256)](https://paperswithcode.com/sota/image-generation-on-imagenet-256x256?p=masked-diffusion-transformer-is-a-strong)

[![HuggingFace space](https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg)](https://huggingface.co/spaces/shgao/MDT) -->


<!-- [PaddlePaddle/Parakeet ![](https://img.shields.io/github/stars/PaddlePaddle/PaddleSpeech?style=social)](https://github.com/PaddlePaddle/PaddleSpeech)

[EditAnything ![](https://img.shields.io/github/stars/sail-sg/EditAnything?style=social)](https://github.com/sail-sg/EditAnything) -->






<ol class="biblist">
<!-- Item: 1 -->
<!-- <li ><p>
<strong>EditAnything: Empowering Unparalleled Flexibility in Image Editing and Generation</strong><br />
Shanghua Gao, Zhijie Lin, Xingyu Xie, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br /> 
ACMMM, 2023, 
<a href="https://dl.acm.org/doi/10.1145/3581783.3612680" style="color: black;">[PDF]</a>
<a href="https://github.com/sail-sg/EditAnything" style="color: black;">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/EditAnything?style=social" >
</iframe><br />
<font color="#2770AB"><b>the first a few pioneers for highly-flexible image editing,</b> e.g., cross-image  dragging like try-on, region-interactive editing, controllable layout generation, and virtual character replacement.  </font> <br />
</p>
</li> -->



<li ><p>
<strong>Masked Diffusion Transformer is a Strong Image Synthesizer</strong><br />
Shanghua Gao, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br /> 
ICCV, 2023, <a href="https://arxiv.org/abs/2303.14389" style="color: black;">[PDF]</a>
<a href="https://github.com/sail-sg/MDT" style="color: black;">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/MDT?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=MDT&type=star&count=true" > -->
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/masked-diffusion-transformer-is-a-strong/image-generation-on-imagenet-256x256" >
</iframe><br /> 
<font color="#2770AB"><b>SoTA image generative model</b> on ImageNet 256x256; <b>13x faster learning speed</b> than <a href="https://arxiv.org/abs/2212.09748">DiT</a> (core of <a href="https://openai.com/sora">SORA</a>) </font> <br />
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>EditAnything: Empowering Unparalleled Flexibility in Image Editing and Generation</strong><br />
Shanghua Gao, Zhijie Lin, Xingyu Xie, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br /> 
ACMMM, 2023, 
<a href="https://dl.acm.org/doi/10.1145/3581783.3612680" style="color: black;">[PDF]</a>
<a href="https://github.com/sail-sg/EditAnything" style="color: black;">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/EditAnything?style=social" >
</iframe><br />
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=EditAnything&type=star&count=true" > -->
<font color="#2770AB"><b>the first a few pioneers for highly-flexible image editing,</b> e.g., cross-image  dragging like try-on, region-interactive editing, controllable layout generation, and virtual character replacement.  </font> <br />
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Consistent3D: Towards Consistent High-Fidelity Text-to-3D Generation with Deterministic Sampling Prior</strong><br />
Zike Wu, <strong>Pan Zhou<sup>+</sup></strong>, Xuanyu YI, Xiaoding Yuan, Hanwang Zhang <br /> 
CVPR, 2024, 
<a href="https://arxiv.org/abs/2401.09050" style="color: black;">[Axriv]</a>
<a href="https://github.com/sail-sg/Consistent3D" style="color: black;">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/Consistent3D?style=social" >
</iframe><br />
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Consistent3D&type=star&count=true" > -->
<font color="#2770AB"><b>the first ODE-sampling guided Score Distillation Sampling</b> for 3D generation</font> <br />
</p>
</li>




<!-- Item: 1 -->
<li ><p>
<strong>Prototypical Contrastive Learning of Unsupervised Representations</strong><br />
Junnan Li, <strong>Pan Zhou</strong>, Caiming Xiong, Steven Hoi<br /> 
ICLR, 2021, 
<a href="https://openreview.net/pdf?id=KmykpuSrjcq" style="color: black;">[Axriv]</a>
<a href="../assets/bibtex/2021-ICLR-SSL.txt" style="color: black;">[Bibtex]</a>
<a href="https://blog.einstein.ai/prototypical-contrastive-learning-pushing-the-frontiers-of-unsupervised-learning/" style="color: black;">[Blog]</a>
<a href="https://github.com/salesforce/PCL" style="color: black;">[Code]</a>, 900+ citations,
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/salesforce/PCL?style=social" >
</iframe><br />
<!-- src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PCL&type=star&count=true" > -->
<font color="#2770AB"><b>the first clustering contrastive learning method to learn high-level semantics, i.e., data cluster structure</b></font> <br />
</p>
</li>


<li ><p>
<strong>MetaFormer Baselines for Vision</strong><br />
Weihao Yu, Chenyang Si, <strong>Pan Zhou</strong>, Mi Luo, Yichen Zhou, Jiashi Feng,
Shuicheng Yan,  Xinchao Wang<br /> 
TPAMI & CVPR, 2023, 
<a href="https://arxiv.org/abs/2111.11418#:~:text=Based%20on%20the%20extensive%20experiments,on%20the%20token%20mixer%20modules" style="color: black;">[Axriv]</a>
<a href="https://github.com/sail-sg/poolformer" style="color: black;">[Code]</a>, 600+ citations, 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/poolformer?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=poolformer&type=star&count=true" > -->
<!-- <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="490px" height="20px"
        src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/metaformer-baselines-for-vision/domain-generalization-on-imagenet-c" >
</iframe> -->
<br />
<font color="#2770AB"><b>replacing attention with simple pooling still achieves high performance, breaking "attention is all you need" and revealing network design principle</b></font> <br />
</p>
</li>




<!-- Item: 1 -->
<li ><p>
<strong>Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models</strong><br />
Xingyu Xie<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Huan Li, Zhouchen Lin, Shuicheng Yan <br />
TPAMI, 2024 
<a href="https://arxiv.org/abs/2208.06677" style="color: black;">[PDF]</a>
<a href="https://github.com/sail-sg/Adan" style="color: black;">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://img.shields.io/github/stars/sail-sg/Adan?style=social" >
</iframe><br />
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Adan&type=star&count=true" > -->
<font color="#2770AB"><b> 2X-faster and SoTA optimizer on 15+ networks</b> like ResNet, ConvNext, ViT, Swin, MAE, BERT, GPT2, LLAMA, Dreamfusion, DiT, PPO in RL,  etc. <b>Included by 
 popular deep-learning codebases</b> like <a href="https://github.com/NVIDIA/NeMo/blob/main/nemo/core/optim/adan.py">NVIDIA NeMo</a> for LLM,  <a href="https://github.com/huggingface/pytorch-image-models/blob/main/timm/optim/adan.py">HuggingFace Timm</a> and <a href="https://github.com/open-mmlab/mmpretrain/blob/dev-1.x/mmcls/engine/optimizers/adan_t.py">OpenMMLab</a> for CV tasks, <a href="https://github.com/Jittor/jittor/blob/master/python/jittor/optim.py">Jittor of Tsinghua University</a> for 3D.
</font> <br />
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Win: Weight-Decay-Integrated Nesterov Acceleration for  Faster Network Training</strong><br>
<strong>Pan Zhou</strong>, Xingyu Xie, Zhouchen Lin, Kim-Chuan Toh, Shuicheng Yan  <br /> 
JMLR & ICLR, 2024
<a href="../assets/pdf/2024-JMLR-win.pdf" style="color: black;">[PDF]</a> 
<a href="https://github.com/sail-sg/win" style="color: black;">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px; color: black;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://img.shields.io/github/stars/sail-sg/win?style=social" >
</iframe><br />
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" > -->
<font color="#2770AB"><b>accelerate AdamW/Adam/LAMB/SGD by 1.5x on vision and language modeling tasks.</b></font> <br />
</p>
</li>

<!-- Item: 1 -->
 <li ><p>
<strong>Towards Theoretically Understanding Why SGD Generalizes Better Than ADAM in Deep Learning</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng, Chao Ma, Caiming Xiong, Steven Hoi, and Weinan E<br /> 
NeurIPS, 2020, 
<a href="../assets/pdf/2020_generalization.pdf" style="color: black;">[PDF]</a>
<a href="../assets/pdf/2020_generalization_supp.pdf" style="color: black;">[SUPP]</a>
<a href="https://arxiv.org/pdf/2010.05627.pdf" style="color: black;">[Axriv]</a>
<a href="../assets/bibtex/2020_generalization_bib.txt" style="color: black;">[Bibtex]</a>
<a href="https://github.com/salesforce/comparison_SGD_ADAM" style="color: black;">[Code]</a>
<a href="../assets/pdf/2020-NIPS-SGD-slides.pdf" style="color: black;">[Slides]</a>
<a href="../assets/pdf/2020-NIPS-SGD-poster.pdf" style="color: black;">[Poster]</a>, 200+ citations
<!-- <iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=salesforce&repo=comparison_SGD_ADAM&type=star&count=true" >
</iframe> -->
<br />
<font color="#2770AB"><b>the first theory to explain "why SGD generalizes better than ADAM in deep learning"</b></font> <br />
</p>
</li>

</ol>

  <br> 

##### **Full Publications** 

<!-- <div class="container">
	
	<button onclick="select()" class="bygroup">Selected Publications</button>	
	
    <button onclick="year()" class="bygroup">By Year</button>
    
    <button onclick="topic()" class="bygroup">By Topic</button>
    
    <button onclick="scholar()" class="bygroup">Google Scholar</button>
</div> -->

<!-- ### Full Publications -->
<ol class="biblist">


<h4>
<a name='2025'></a> 2025
</h4>

<li ><p>
<strong>LoCo: Low-Bit Communication Adaptor for Large-scale Model Training</strong><br>
Xingyu Xie, Zhijie Lin, Kim-chuan Toh, <strong>Pan Zhou<sup>+</sup></strong><br />
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2025<br />
<a href="https://arxiv.org/abs/2407.04480">[PDF]</a>
<a href="https://github.com/deepspeedai/DeepSpeed/pull/6730">[Code]</a> <br />
<!-- <iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=deepspeedai&repo=DeepSpeed&type=star&count=true" >
</iframe> -->
<!-- <font color="#2770AB"> -->
<b> On Megatron-LM and FSDP, LoCo significantly improves communication efficiency, e.g.,
+14% to +40% improvement on Adam's overall training speed  without performance degradation on LLAMAs and MoEs. LoCo has been included by 
 popular <a href="https://github.com/deepspeedai/DeepSpeed/pull/6730">DeepSpeed</a> codebase like <a href="https://github.com/deepspeedai/DeepSpeed/pull/6730">Zero++</a>. </b>
<!-- </font>  -->
<br />
</p>
</li>




<li ><p>
<strong>A Causality-aware Paradigm for Evaluating Creativity of Multimodal Large Language Models</strong><br>
Zhongzhan Huang<sup>*</sup>, Shanshan Zhong<sup>*</sup>, <strong>Pan Zhou<sup>*</sup></strong>, Shanghua Gao, Marinka Zitnik, Liang Lin  <br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2025<br />
<a href="https://arxiv.org/abs/2501.15147">[PDF]</a>
<a href="https://lotbench.github.io/">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=CLoT&type=star&count=true" >
</iframe>
</p>
</li>

<li ><p>
<strong>Collaborative Tree Search for Enhancing Embodied Multi-Agent Collaboration</strong><br />
Lizheng Zu, Lin Lin, Song Fu, Na Zhao, <strong>Pan Zhou</strong> <br />  
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2025<br />
  <a href="https://cvpr.thecvf.com/virtual/2025/poster/32902">[PDF]</a> 
</p>
</li>



<li ><p>
<strong>Towards Understanding Why FixMatch Generalizes Better Than Supervised Learning</strong><br />
Jingyang Li, Jiachun Pan, Vincent Y. F. Tan, Kim-chuan Toh, <strong>Pan Zhou<sup>+</sup></strong><br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2025 (<strong>oral, 1.8% acceptance rate</strong>) <br />
  <a href="https://arxiv.org/abs/2410.11206">[Axriv]</a> 
</p>
</li>

<li ><p>
<strong>CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation</strong><br />
Jie Liu, <strong>Pan Zhou<sup>+</sup></strong>, Yingjun Du, Ah-Hwee Tan, Cees G. M. Snoek, Jan-Jakob Sonke, Efstratios Gavves <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2025 <br />
  <a href="https://arxiv.org/abs/2411.04679">[Axriv]</a> 
</p>
</li>


<h4>
<a name='2024'></a> 2024
</h4>



<!-- Item: 1 -->
<li ><p>
<strong>Win: Weight-Decay-Integrated Nesterov Acceleration for  Faster Network Training</strong><br>
<strong>Pan Zhou</strong>, Xingyu Xie, Zhouchen Lin, Kim-Chuan Toh, Shuicheng Yan  <br /> 
Journal of Machine Learning Research (<strong>JMLR</strong>), 2024<br />
<a href="../assets/pdf/2024-JMLR-win.pdf">[PDF]</a>
<a href="https://github.com/sail-sg/win">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://img.shields.io/github/stars/sail-sg/win?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" > -->
</p>
</li>

<li ><p>
<strong>Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models</strong><br />
Xingyu Xie<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Huan Li, Zhouchen Lin, Shuicheng Yan <br />
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2024<br />
<a href="https://arxiv.org/abs/2208.06677">[PDF]</a>
<a href="https://github.com/sail-sg/Adan">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://img.shields.io/github/stars/sail-sg/Adan?style=social" >
</iframe><br />
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Instant3D: Instant Text-to-3D Generation</strong><br>
Ming Li, <strong>Pan Zhou</strong>, Jia-Wei Liu, Jussi Keppo, Min Lin, Shuicheng Yan, Xiangyu Xu  <br /> 
International Journal of Computer Vision (<strong>IJCV</strong>), 2024<br />
<a href="https://arxiv.org/abs/2311.08403">[PDF]</a>
<a href="https://ming1993li.github.io/Instant3DProj/">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://img.shields.io/github/stars/ming1993li/Instant3DCodes?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=ming1993li&repo=Instant3DCodes&type=star&count=true" > -->
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Enhancing Visual Grounding in Vision-Language Pre-Training with Position-Guided Text Prompts</strong><br>
Alex Jinpeng Wang, <strong>Pan Zhou</strong>, Mike Zheng Shou, Shuicheng Yan  <br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2024<br />
<a href="https://ieeexplore.ieee.org/document/10363674">[PDF]</a>
<a href="https://github.com/sail-sg/ptp">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://img.shields.io/github/stars/sail-sg/ptp?style=social" >
</iframe>,
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ptp&type=star&count=true" > -->
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/position-guided-text-prompt-for-vision/zero-shot-cross-modal-retrieval-on-coco-2014" >
</iframe>
</p>
</li>




<!-- Item: 1 -->
<li ><p>
<strong>Towards Understanding Convergence and Generalization of AdamW</strong><br>
<strong>Pan Zhou</strong>, Xingyu Xie, Zhoucheng Lin, Shuicheng Yan <br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2024<br />
<a href="../assets/pdf/2024-TPAMI-AdamW.pdf">[PDF]</a>
<a href="../assets/pdf/2024-TPAMI-AdamW-supp.pdf">[Supp]</a>
</p>
</li>


<li ><p>
<strong>Unsupervised Modality Adaptation with Text-to-Image Diffusion Models for Semantic Segmentation</strong><br />
Ruihao Xia, Yu Liang, Peng-Tao Jiang, Hao Zhang, Bo Li, Yang Tang, <strong>Pan Zhou</strong> <br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024<br />
<a href="https://arxiv.org/abs/2405.18144">[Axriv]</a>
<a href="https://github.com/XiaRho/MADM">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/XiaRho/MADM?style=social" >
</iframe>
</p>
</li>


<li ><p>
<strong>LOVA3: Learning to Visual Question Answering, Asking and Assessment</strong><br />
Hengyuan Zhao, <strong>Pan Zhou</strong><strong><sup>+</sup></strong>, Difei Gao, Mike Zheng Shou<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024<br />
<a href="https://arxiv.org/abs/2405.14974">[Axriv]</a>
<a href="https://github.com/showlab/LOVA3">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/showlab/LOVA3?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ScaleLong&type=star&count=true" > -->
</p>
</li>


<li ><p>
<strong>4-bit Shampoo for Memory-Efficient Network Training</strong><br />
Sike Wang, <strong>Pan Zhou</strong>, Jia Li, Hua Huang<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024<br />
<a href="https://arxiv.org/abs/2405.18144">[Axriv]</a>
<a href="https://github.com/Sike-Wang/low-bit-Shampoo">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/Sike-Wang/low-bit-Shampoo?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ScaleLong&type=star&count=true" > -->
</p>
</li>


<li ><p>
<strong>MVGamba: Unify 3D Content Generation as State Space Sequence Modeling</strong><br />
Xuanyu Yi, Zike Wu, Qiuhong Shen, Qingshan Xu, <strong>Pan Zhou</strong>, Joo Hwee Lim, Shuicheng YAN, Xinchao Wang, Hanwang Zhang<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024<br />
<a href="https://arxiv.org/abs/2406.06367">[Axriv]</a>
<a href="https://github.com/SkyworkAI/Gamba">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/SkyworkAI/Gamba?style=social" >
</iframe>
</p>
</li>


<li ><p>
<strong>Genixer: Empowering Multimodal Large Language Models as a Powerful Data Generator</strong><br />
Henry Hengyuan Zhao, <strong>Pan Zhou</strong><strong><sup>+</sup></strong>, Mike Zheng Shou <br />
European Conference on Computer Vision (<strong>ECCV</strong>), 2024<br />
<a href="https://arxiv.org/abs/2312.06731">[PDF]</a>
<a href="https://github.com/zhaohengyuan1/Genixer">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://img.shields.io/github/stars/zhaohengyuan1/Genixer?style=social" >
</iframe><br />
</p>
</li>

<li ><p>
<strong>Efficient Cascaded Multiscale Adaptive Network for Image Restoration</strong><br />
Yichen Zhou, <strong>Pan Zhou</strong><strong><sup>+</sup></strong>, Teck Khim Ng <br />
European Conference on Computer Vision (<strong>ECCV</strong>), 2024<br />
</p>
</li>



<!-- Item: 1 -->
<li ><p>
<strong>Let's Think Outside the Box: Exploring Leap-of-Thought in Large Language Models with Multimodal Humor Generation</strong><br />
Shanshan Zhong, Zhongzhan Huang, Shanghua Gao, Wushao Wen, Liang Lin, Marinka Zitnik, <strong>Pan Zhou<sup>+</sup></strong><br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2312.02439">[Axriv]</a>
<a href="https://zhongshsh.github.io/CLoT/">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/CLoT?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=CLoT&type=star&count=true" > -->
</p>
</li>


<!-- Item: 1 -->
<li ><p>
<strong>InceptionNeXt: When Inception Meets ConvNeXt</strong><br />
Weihao Yu, <strong>Pan Zhou</strong>, Shuicheng YAN, Xinchao Wang <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2303.16900">[Axriv]</a>
<a href="https://github.com/sail-sg/inceptionnext">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/inceptionnext?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=inceptionnext&type=star&count=true" > -->
</p>
</li>

 

<!-- Item: 1 -->
<li ><p>
<strong>Consistent3D: Towards Consistent High-Fidelity Text-to-3D Generation with Deterministic Sampling Prior</strong><br />
Zike Wu, <strong>Pan Zhou<sup>+</sup></strong>, Xuanyu YI, Xiaoding Yuan, Hanwang Zhang <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2401.09050">[Axriv]</a>
<a href="https://github.com/sail-sg/Consistent3D">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/Consistent3D?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Consistent3D&type=star&count=true" > -->
</p>
</li>


<!-- Item: 1 -->
<li ><p>
<strong>Friendly Sharpness-Aware Minimization</strong><br />
Tao Li, <strong>Pan Zhou<sup>+</sup></strong>, Zhengbao He, Xinwen Cheng, Xiaolin Huang<br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2403.12350">[Axriv]</a>
<a href="https://github.com/nblt/F-SAM">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/nblt/F-SAM?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=nblt&repo=F-SAM&type=star&count=true" > -->
</p>
</li>



<!-- Item: 1 -->
<li ><p>
<strong>Few-shot Learner Parameterization by Diffusion Time-steps</strong><br />
Zhongqi Yue, <strong>Pan Zhou<sup>+</sup></strong>, Richang Hong, Hanwang Zhang, Qianru Sun <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2403.02649">[Axriv]</a>
<a href="https://github.com/yue-zhongqi/tif">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/yue-zhongqi/tif?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=yue-zhongqi&repo=tif&type=star&count=true" > -->
</p>
</li>


<!-- Item: 1 -->
<li ><p>
<strong>Diffusion Time-step Curriculum for One Image to 3D Generation</strong><br />
Xuanyu Yi, Zike Wu, Qingshan Xu, <strong>Pan Zhou<sup>+</sup></strong>, Joo Hwee Lim, Hanwang Zhang  <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://github.com/yxymessi/DTC123/blob/main/DTC_CVPR.pdf">[Axriv]</a>
<a href="https://github.com/yxymessi/DTC123">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/yxymessi/DTC123?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=yxymessi&repo=DTC123&type=star&count=true" > -->
</p>
</li>



<h4>
<a name='2023'></a> 2023
</h4>

<!-- Item: 1 -->
<li ><p>
<strong>MetaFormer Baselines for Vision</strong><br />
Weihao Yu, Chenyang Si, <strong>Pan Zhou</strong>, Mi Luo, Yichen Zhou, Jiashi Feng,
Shuicheng Yan,  Xinchao Wang<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2023<br />
<a href="https://arxiv.org/abs/2210.13452">[Axriv]</a>
<a href="https://github.com/sail-sg/metaformer">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/metaformer?style=social" >
</iframe>,  <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="700px" height="20px"
        src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/metaformer-baselines-for-vision/domain-generalization-on-imagenet-c" >
    </iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=metaformer&type=star&count=true" > -->

<!-- Item: 1 -->
<li ><p>
<strong>Contrastive Video Question Answering via Video Graph Transformer</strong><br />
Junbin Xiao, <strong>Pan Zhou</strong>, Angela Yao, Yicong Li, Richang Hong, Shuicheng Yan, Tat-Seng Chua<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2023<br />
<a href="https://arxiv.org/abs/2302.13668">[PDF]</a>
<a href="https://github.com/doc-doc/CoVGT">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/doc-doc/CoVGT?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=doc-doc&repo=CoVGT&type=star&count=true" > -->
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Iterative Graph Self-Distillation</strong><br />
Hanlin Zhang, Shuai Lin, Weiyang Liu, <strong>Pan Zhou</strong>, Jian Tang, Xiaodan Liang, Eric P. Xing <br /> 
IEEE Transactions on Knowledge and Data Engineering (<strong>TKDE</strong>), 2023 <br />
<a href="https://arxiv.org/abs/2010.12609">[Axriv]</a>
</p>
</li>



<!-- Item: 1 -->
<li ><p>
<strong>ScaleLong: Towards More Stable Training of Diffusion Model via Scaling Network Long Skip Connection</strong><br />
Zhongzhan Huang, <strong>Pan Zhou<sup>+</sup></strong>, Shuicheng Yan, Liang Lin<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2023<br />
<a href="https://arxiv.org/pdf/2310.13545.pdf">[Axriv]</a>
<a href="https://github.com/sail-sg/ScaleLong">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/ScaleLong?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ScaleLong&type=star&count=true" > -->
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Masked Diffusion Transformer is a Strong Image Synthesizer</strong><br />
Shanghua Gao, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br /> 
International Conference on Computer Vision (<strong>ICCV</strong>), 2023<br />
<a href="https://arxiv.org/abs/2303.14389">[PDF]</a>
<a href="https://github.com/sail-sg/MDT">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/MDT?style=social" >
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=MDT&type=star&count=true" > -->
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/masked-diffusion-transformer-is-a-strong/image-generation-on-imagenet-256x256" >
</iframe>
<!-- <iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="150px" height="20px"
    src="https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg" >
</iframe>  -->
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>EditAnything: Empowering Unparalleled Flexibility in Image Editing and Generation</strong><br />
Shanghua Gao, Zhijie Lin, Xingyu Xie, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br /> 
ACM International Conference on Multimedia (<strong>ACMMM</strong>), 2023<br />
<a href="https://dl.acm.org/doi/10.1145/3581783.3612680">[PDF]</a>
<a href="https://github.com/sail-sg/EditAnything">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/EditAnything?style=social" >
      
</iframe>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=EditAnything&type=star&count=true" > -->
<!-- <iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="150px" height="20px"
    src="https://huggingface.co/spaces/shgao/EditAnything" >
</iframe>  -->
</p>
</li>

 

<!-- Item: 1 -->
<li ><p>
<strong>STPrivacy: Spatio-Temporal Privacy-Preserving Action Recognition</strong><br />
Ming Li, Xiangyu Xu, Hehe Fan, <strong>Pan Zhou</strong>, Jun Liu, Jia-Wei Liu, Jiahe Li, Jussi Keppo, Mike Zheng Shou, Shuicheng Yan<br /> 
International Conference on Computer Vision (<strong>ICCV</strong>), 2023<br />
<a href="https://arxiv.org/abs/2301.03046">[PDF]</a>
</p>
</li>
 


 

<!-- Item: 1 -->
<li ><p>
<strong>Position-guided Text Prompt for Vision-Language Pre-training</strong><br />
Alex Jinpeng Wang,  <strong>Pan Zhou<sup>+</sup></strong>, Mike Zheng Shou, Shuicheng Yan <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2023<br />
<a href="https://arxiv.org/pdf/2212.09737.pdf">[Axriv]</a>
<a href="https://github.com/sail-sg/ptp">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/ptp?style=social" >
</iframe>,
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/position-guided-text-prompt-for-vision/zero-shot-cross-modal-retrieval-on-coco-2014" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ptp&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Win: Weight-Decay-Integrated Nesterov Acceleration for Adaptive Gradient Algorithms</strong><br />
<strong>Pan Zhou</strong>, Xingyu Xie, Shuicheng Yan <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2023 (<font color="#FF0000"><strong>oral</strong></font>)<br />
<a href="https://openreview.net/pdf?id=CPdc77SQfQ5">[Axriv]</a>
<a href="https://github.com/sail-sg/win">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/win?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Towards Understanding Why Mask Reconstruction Pretraining Helps in Downstream Tasks</strong><br />
Jiachun Pan<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Shuicheng Yan<br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2023 <br />
  <a href="https://arxiv.org/pdf/2206.03826.pdf">[Axriv]</a> 
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>LPT: Long-tailed Prompt Tuning for Image Classification</strong><br />
Bowen Dong, <strong>Pan Zhou</strong>, Shuicheng Yan, Wangmeng Zuo <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2023 <br />
<a href="https://arxiv.org/abs/2210.01033">[Axriv]</a>
<a href="https://github.com/DongSky/LPT">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/DongSky/LPT?style=social" >
</iframe>,
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/lpt-long-tailed-prompt-tuning-for-image/long-tail-learning-on-cifar-100-lt-r-100" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=DongSky&repo=LPT&type=star&count=true" > -->







<h4>
	<a name='2022'></a> 2022
</h4>

<!-- Item: 1 -->
<li ><p>
<strong>Prototypical Graph Contrastive Learning</strong><br />
Shuai Lin,  Chen Liu, <strong>Pan Zhou</strong>,  Zi-yuan Hu,  Shuojia Wang,  Ruihui Zhao,  Yefeng Zheng,  Liang Lin,  Eric Xing,  Xiaodan Liang<br /> 
IEEE Transactions on Neural Networks and Learning Systems (<strong>TNNLS</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2106.09645">[Axriv]</a>
<a href="https://github.com/ha-lins/PGCL">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/ha-lins/PGCL?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=ha-lins&repo=PGCL&type=star&count=true" > -->
 


<!-- Item: 1 -->
<li ><p>
<strong>Inception Transformer</strong><br />
Chenyang Si<strong><sup>*</sup></strong>, Weihao Yu<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong>, Yichen Zhou, Xinchao Wang, Shuicheng Yan<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2022 (<font color="#FF0000"><strong>oral</strong></font>)<br />
<a href="https://arxiv.org/abs/2205.12956">[Axriv]</a>
<a href="https://github.com/sail-sg/iFormer">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/iFormer?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=iFormer&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Mugs: A Multi-Granular Self-Supervised Learning Framework</strong><br />
<strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Yichen Zhou<strong><sup>*</sup></strong>, Chenyang Si<strong><sup>*</sup></strong>,  Weihao Yu, Teck Khim Ng, Shuicheng Yan<br />
Workshop of Neural Information Processing Systems, 2022.<br />
<a href="https://arxiv.org/abs/2203.14415">[Axriv]</a>
<a href="https://github.com/sail-sg/mugs">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/mugs?style=social" >
</iframe>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mugs-a-multi-granular-self-supervised/self-supervised-image-classification-on" >
</iframe><br />
<font color="#2770AB"><b>Top linear probing and KNN performance on ImageNet without extra data</b></font><br />
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=mugs&type=star&count=true" > -->


<!-- Item: 1 -->
<li ><p>
<strong>DualFormer: Local-Global Stratified Transformer for Efficient Video Recognition</strong><br />
Yuxuan Liang, <strong>Pan Zhou</strong>, Roger Zimmermann, Shuicheng Yan <br /> 
European Conference on Computer Vision (<strong>ECCV</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2112.04674">[Axriv]</a>
<a href="https://github.com/sail-sg/dualformer">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/dualformer?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=dualformer&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Video Graph Transformer for Video Question Answering</strong><br />
Junbin Xiao, <strong>Pan Zhou</strong>, Tat-Seng Chua, Shuicheng Yan <br /> 
European Conference on Computer Vision (<strong>ECCV</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2207.05342">[Axriv]</a>
<a href="https://github.com/sail-sg/VGT">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/VGT?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=VGT&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Self-Promoted Supervision for Few-Shot Transformer</strong><br />
Bowen Dong, <strong>Pan Zhou</strong>, Shuicheng Yan, Wangmeng Zuo <br /> 
European Conference on Computer Vision (<strong>ECCV</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2203.07057">[Axriv]</a>
<a href="https://github.com/DongSky/few-shot-vit">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/DongSky/few-shot-vit?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=DongSky&repo=few-shot-vit&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
  <strong>MetaFormer is Actually What You Need for Vision</strong><br />
  Weihao Yu, Mi Luo, <strong>Pan Zhou</strong>, Chenyang Si, Yichen Zhou, Xinchao Wang, Jiashi Feng, Shuicheng Yan <br /> 
  IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2022 (<font color="#FF0000"><strong>oral</strong></font>) <br />
  <a href="https://arxiv.org/abs/2111.11418#:~:text=Based%20on%20the%20extensive%20experiments,on%20the%20token%20mixer%20modules.">[Axriv]</a>
  <a href="https://github.com/sail-sg/poolformer">[Code]</a>
  <iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/poolformer?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=poolformer&type=star&count=true" > -->
 


 
<h4>
	<a name='2021'></a> 2021
</h4>


<!-- Item: 1 -->
<li ><p>
<strong>A Hybrid Stochastic-Deterministic Minibatch Proximal Gradient Method for Efficient Optimization and  Generalization</strong><br />
<strong>Pan Zhou</strong>, XiaoTong Yuan, Zhouchen Lin, and Steven Hoi<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2021<br />
<a href="../assets/pdf/2021-TPAMI-HSDN.pdf">[PDF]</a>
<a href="../assets/pdf/2021-TPAMI-HSDN-supp.pdf">[SUPP]</a>
<a href="../assets/bibtex/2021-PAMI-HSDN-bib.txt">[Bibtex]</a>
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Efficient Gradient Support Pursuit with Less Hard Thresholding for Cardinality-Constrained Learning</strong><br />
Fanhua Shang, Bingkun Wei, Hongying Liu, Yuanyuan Liu, <strong>Pan Zhou</strong>, and Maoguo Gong <br /> 
IEEE Transactions on Neural Networks and Learning Systems (<strong>TNNLS</strong>), 2021 <br />
<a href="https://ieeexplore.ieee.org/abstract/document/9463415">[PDF]</a> 
</p>
</li>
 


<!-- Item: 1 -->
<li ><p>
<strong>A Theory-Driven Self-Labeling Refinement Method for Contrastive Representation Learning</strong><br />
<strong>Pan Zhou</strong>, Caiming Xiong, Xiaotong Yuan, Steven Hoi<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2021 (<font color="#FF0000"><strong>spotlight</strong></font>) <br />
<a href="../assets/pdf/2021-NIPS-SLR.pdf">[PDF]</a>
<a href="../assets/pdf/2021-NIPS-SLR-supp.pdf">[SUPP]</a>
<a href="https://arxiv.org/abs/2106.14749">[Axriv]</a>
<a href="../assets/bibtex/2021-NIPS-SLR-bib.txt">[Bibtex]</a>
<a href="https://openreview.net/forum?id=P84bifNCpFQ&referrer=%5BAuthor%20Console%5D">[Code]</a>
<a href="../assets/pdf/2021-NIPS-SLR-Slide.pdf">[Slides]</a>
<a href="../assets/pdf/2021-NIPS-SLR-poster.pdf">[Poster]</a>
</p>
</li>
 


<!-- Item: 1 -->
<li ><p>
<strong>Towards Understanding Why Lookahead Generalizes Better Than SGD and Beyond</strong><br />
<strong>Pan Zhou</strong>, Hanshu Yan, Xiaotong Yuan, Jiashi Feng, Shuicheng Yan<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2021 <br />
<a href="../assets/pdf/2021-NIPS-LA.pdf">[PDF]</a>
<a href="../assets/pdf/2021-NIPS-LA-supp.pdf">[SUPP]</a>
<a href="../assets/bibtex/2021-NIPS-LA-bib.txt">[Bibtex]</a>
<a href="https://github.com/sail-sg/SLRLA-optimizer">[Code]</a>
<a href="../assets/pdf/2021-NIPS-LA-Slide.pdf">[Slides]</a>
<a href="../assets/pdf/2021-NIPS-LA-poster.pdf">[Poster]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/sail-sg/SLRLA-optimizer?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=SLRLA-optimizer&type=star&count=true" > -->
 


 

<!-- Item: 1 -->
<li ><p>
<strong>Task Similarity Aware Meta Learning: Theory-inspired Improvement on MAML</strong><br />
<strong>Pan Zhou</strong>, Yingtian Zou, XiaoTong Yuan, Jiashi Feng, Caiming Xiong, and Steven Hoi<br /> 
International Conference on Uncertainty in Artificial Intelligence  (<strong>UAI</strong>), 2021 (NeurIPS'20 Meta Learning Workshop Paper) <br />
<a href="https://meta-learn.github.io/2020/papers/69_paper.pdf">[PDF]</a>
<a href="https://meta-learn.github.io/2020/papers/69_supplementary.pdf">[SUPP]</a>
<a href="https://github.com/Carbonaraa/TSA-MAML">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/Carbonaraa/TSA-MAML?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=Carbonaraa&repo=TSA-MAML&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Wav-BERT: Cooperative Acoustic and Linguistic Representation Learning for Low-Resource Speech Recognition</strong><br />
Guolin Zheng, Yubei Xiao, Ke Gong, <strong>Pan Zhou</strong>, Xiaodan Liang, and Liang Lin<br /> 
Conference on Empirical Methods in Natural Language Processing  (<strong>EMNLP</strong>), 2021 (Findings) <br />
<a href="https://arxiv.org/pdf/2109.09161.pdf">[Axriv]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>How Important is the Train-Validation Split in Meta-Learning?</strong><br />
Yu Bai, Minshuo Chen, <strong>Pan Zhou</strong>, Tuo Zhao, Jason D. Lee, Sham Kakade, Huan Wang, Caiming Xiong<br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2021 <br />
<a href="https://arxiv.org/pdf/2010.05843.pdf">[Axriv]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Prototypical Contrastive Learning of Unsupervised Representations</strong><br />
Junnan Li, <strong>Pan Zhou</strong>, Caiming Xiong, and Steven Hoi<br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2021 <br />
<a href="https://openreview.net/pdf?id=KmykpuSrjcq">[Axriv]</a>
<a href="../assets/bibtex/2021-ICLR-SSL.txt">[Bibtex]</a>
<a href="https://blog.einstein.ai/prototypical-contrastive-learning-pushing-the-frontiers-of-unsupervised-learning/">[Blog]</a>
<a href="https://github.com/salesforce/PCL">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/salesforce/PCL?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PCL&type=star&count=true" > -->
 
<!-- Item: 1 -->
<li ><p>
<strong>Graph-Evolving Meta-Learning for Low-Resource Medical Dialogue Generation</strong><br />
Shuai Lin, <strong>Pan Zhou</strong>, Xiaodan Liang, Jianheng Tang, Ruihui Zhao, Ziliang Chen and Liang Lin <br /> 
Association for the Advancement of Artificial Intelligence (<strong>AAAI</strong>), 2021 <br />
<a href="https://arxiv.org/pdf/2012.11988.pdf">[Axriv]</a>
<a href="../assets/bibtex/2021-AAAI-Medical.txt">[Bibtex]</a>
<a href="https://github.com/ha-lins/GEML-MDG">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/ha-lins/GEML-MDG?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=ha-lins&repo=GEML-MDG&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Adversarial Meta Sampling for Multilingual Low-Resource Speech Recognition</strong><br />
Yubei Xiao, Ke Gong, <strong>Pan Zhou</strong>, Guolin Zheng, Xiaodan Liang and Liang Lin <br /> 
Association for the Advancement of Artificial Intelligence (<strong>AAAI</strong>), 2021 <br />
<a href="https://arxiv.org/pdf/2012.11896.pdf">[Axriv]</a>
<a href="../assets/bibtex/2021-AAAI-ASR.txt">[Bibtex]</a>
<!-- <a href="https://github.com/iamxiaoyubei/AMS">[Code]</a> -->
<!-- <iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/iamxiaoyubei/AMS?style=social" >
</iframe> -->
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=iamxiaoyubei&repo=AMS&type=star&count=true" > -->
 



 
<h4>
	<a name='2020'></a> 2020
</h4>

<!-- Item: 1 -->
<li ><p>
<strong>Theory-Inspired Path-Regularized Differential Network Architecture Search</strong><br />
<strong>Pan Zhou</strong>, Caiming Xiong, Richard Socher, and Steven Hoi<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2020 (<font color="#FF0000"><strong>oral</strong></font>) <br />
<a href="../assets/pdf/2020_NAS.pdf">[PDF]</a>
<a href="../assets/pdf/2020_NAS_supp.pdf">[SUPP]</a>
<a href="https://arxiv.org/pdf/2006.16537.pdf">[Axriv]</a>
<a href="../assets/bibtex/2020_NAS_bib.txt">[Bibtex]</a>
<a href="https://blog.einstein.ai/theory-inspired-network-architecture-search/">[Blog]</a>
<a href="https://github.com/salesforce/PR-DARTS">[Code]</a>
<a href="../assets/pdf/2020-NIPS-NAS-slides.pdf">[Slides]</a>
<a href="../assets/pdf/2020-NIPS-NAS-poster.pdf">[Poster]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/salesforce/PR-DARTS?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PR-DARTS&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Towards Theoretically Understanding Why SGD Generalizes Better Than ADAM in Deep Learning</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng, Chao Ma, Caiming Xiong, Steven Hoi, and Weinan E<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2020<br />
<a href="../assets/pdf/2020_generalization.pdf">[PDF]</a>
<a href="../assets/pdf/2020_generalization_supp.pdf">[SUPP]</a>
<a href="https://arxiv.org/pdf/2010.05627.pdf">[Axriv]</a>
<a href="../assets/bibtex/2020_generalization_bib.txt">[Bibtex]</a>
<a href="https://github.com/salesforce/comparison_SGD_ADAM">[Code]</a>
<a href="../assets/pdf/2020-NIPS-SGD-slides.pdf">[Slides]</a>
<a href="../assets/pdf/2020-NIPS-SGD-poster.pdf">[Poster]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/salesforce/comparison_SGD_ADAM?style=social" >
</iframe>
</p>
</li>
<!-- %src="https://ghbtns.com/github-btn.html?user=salesforce&repo=comparison_SGD_ADAM&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Improving GAN Training with Probability Ratio Clipping and Sample Reweighting</strong><br />
Yue Wu, <strong>Pan Zhou</strong>, Andrew Gordon Wilson, Eric Xing, and Zhiting Hu<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2020<br />
<a href="../assets/pdf/2020_GAN.pdf">[PDF]</a>
<a href="https://arxiv.org/pdf/2006.06900.pdf">[Axriv]</a>
<a href="../assets/bibtex/2020_GAN_bib.txt">[Bibtex]</a>
<a href="https://github.com/Holmeswww/PPOGAN">[Codes]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://img.shields.io/github/stars/Holmeswww/PPOGAN?style=social" >
</iframe>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=Holmeswww&repo=PPOGAN&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li ><p>
<strong>Hybrid Stochastic-Deterministic Minibatch Proximal Gradient: Less-Than-Single-Pass Optimization with Nearly Optimal Generalization</strong><br />
<strong>Pan Zhou</strong> and Xiaotong Yuan<br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2020 <br />
<a href="../assets/pdf/2020_hybrid_proximal_minibatch.pdf">[PDF]</a>
<a href="https://arxiv.org/pdf/2009.09835.pdf">[Axriv]</a>
<a href="../assets/bibtex/2020_optimization_bib.txt">[Bibtex]</a>
</p>
</li>
 

 
<h4>
	<a name='2019'></a> 2019
</h4>


<!-- Item: 1 -->
<li ><p>
<strong>Tensor Low-rank Representation for Data Recovery and Clustering</strong><br />
<strong>Pan Zhou</strong>, Canyi Lu, Jiashi Feng, Zhouchen Lin, Shuicheng Yan<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2019 <br />
<a href="../assets/pdf/2019-TPAMI-tensor.pdf">[PDF]</a>
<a href="../assets/pdf/2019-TPAMI-tensor-supp.pdf">[SUPP]</a>
<a href="../assets/bibtex/2019-PAMI-tensor.txt">[Bibtex]</a>
<a href="../assets/code/TLRR-code.zip">[Codes]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Faster First-Order Methods for Stochastic Non-Convex Optimization on Riemannian Manifolds</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Shuicheng Yan, Jiashi Feng<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2019 <br />
<a href="https://ieeexplore.ieee.org/document/8792163">[PDF]</a>
<a href="../assets/bibtex/2019-PAMI-RSPIDER.txt">[Bibtex]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Efficient Meta Learning via Minibatch Proximal Update</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Huan Xu, Shuicheng Yan, Jiashi Feng<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2019 (<font color="#FF0000"><strong>spotlight</strong></font>) <br />
<a href="../assets/pdf/2019-NIPS-metaleanring.pdf">[PDF]</a>
<a href="../assets/pdf/2019-NIPS-metaleanring-supplementary.pdf">[SUPP]</a>
<a href="../assets/bibtex/2019-NIPS-meta.txt">[Bibtex]</a>
<a href="../assets/code/MetaMinibatchProx.zip">[Codes]</a>
<a href="../assets/pdf/2019neurips-slides.pdf">[Slides]</a>
<a href="../assets/pdf/2019-NIPS-poster.pdf">[Poster]</a>
</p>
</li>
 




<!-- Item: 1 -->
<li ><p>
<strong>Generalized Majorization-Minimization for Non-Convex Optimization</strong><br />
Hu Zhang, <strong>Pan Zhou</strong>, Yi Yang, Jiashi Feng<br />
International Joint Conference on Artificial Intelligence (<strong>IJCAI</strong>), 2019 <br />
<a href="https://www.ijcai.org/proceedings/2019/0591.pdf">[PDF]</a>
<a href="../assets/bibtex/2019-IJCAI-MM.txt">[Bibtex]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Faster First-Order Methods for Stochastic Non-Convex Optimization on Riemannian Manifolds</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Jiashi Feng<br />
International Conference on Artificial Intelligence and Statistics (<strong>AISTATS</strong>), 2019 <br />
<a href="https://arxiv.org/pdf/1811.08109.pdf">[PDF]</a>
<a href="../assets/bibtex/2019-AISTATIC-RSPIDER.txt">[Bibtex]</a>
</p>
</li>
 


 
<h4>
	<a name='2018'></a> 2018
</h4>

<!-- Item: 1 -->
<li ><p>
<strong>Efficient Stochastic Gradient Hard Thresholding</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Jiashi Feng<br />
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2018 <br />
<a href="http://papers.nips.cc/paper/7469-efficient-stochastic-gradient-hard-thresholding">[PDF]</a>
<a href="../assets/bibtex/2018-NIPS-hardthresholding.txt">[Bibtex]</a>
<a href="../assets/code/HSGHTcode.rar">[Codes]</a>
</p>
</li>
 


<!-- Item: 1 -->
<li ><p>
<strong>New Insight into Hybrid Stochastic Gradient Descent:
Beyond With-Replacement Sampling and Convexity</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Jiashi Feng<br />
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2018 <br />
<a href="http://papers.nips.cc/paper/7399-new-insight-into-hybrid-stochastic-gradient-descent-beyond-with-replacement-sampling-and-convexity">[PDF]</a>
<a href="../assets/bibtex/2018-NIPS-withreplacement.txt">[Bibtex]</a>
</p>
</li>

 


<!-- Item: 1 -->
<li ><p>
<strong>Understanding Generalization and Optimization Performance of Deep CNNs</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng<br />
International Conference on Machine Learning (<strong>ICML</strong>), 2018 <br />
<a href="../assets/pdf/2018-ICML-deepCNNs.pdf">[PDF]</a>
<a href="https://arxiv.org/abs/1805.10767">[Axriv]</a>
<a href="../assets/bibtex/2018-ICML-AnalysisCNN.txt">[Bibtex]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Deep Adversarial Subspace Clustering</strong><br />
<strong>Pan Zhou</strong>, Yunqing Hou, Jiashi Feng<br />
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2018 <br />
<a href="../assets/pdf/2018-CVPR-DSCN.pdf">[PDF]</a>
<a href="../assets/code/dsc_code.zip">[Codes]</a>
<a href="../assets/bibtex/2018-CVPR-DSCN.txt">[Bibtex]</a>
</p>
</li>
 


<!-- Item: 1 -->
<li ><p>
<strong>Empirical Risk Landscape Analysis for Understanding Deep Neural Networks</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng<br />
International Conference on Learning Representations (<strong>ICLR</strong>), 2018 <br />
<a href="../assets/pdf/2018-ICLR-AnalysisDNN.pdf">[PDF]</a>
<a href="https://arxiv.org/abs/1705.07038">[Axriv]</a>
<a href="../assets/bibtex/2018-ICLR-AnalysisDNN.txt">[Bibtex]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Task Relation Networks</strong><br />
Jianshu Li, <strong>Pan Zhou</strong>, Yunpeng Chen, Jian Zhao, Sujoy Roy, Yan Shuicheng, Jiashi Feng, and  Terence Sim<br />
IEEE Winter Conference on Applications of Computer Vision (<strong>WACV</strong>), 2019 <br />
<a href="https://ieeexplore.ieee.org/document/8658407">[PDF]</a>
</p>
</li>

 <h4>
	<a name='2017'></a> 2017
</h4>


<!-- Item: 1 -->
<li ><p>
<strong>Tensor Factorization for Low-Rank Tensor Completion</strong><br />
<strong>Pan Zhou</strong>, Canyi Lu, Zhouchen Lin, Chao Zhang<br />
IEEE Transactions on Image Processing
(<strong>TIP</strong>), 2017 <br />
<a href="../assets/pdf/2017-TIP-TCTF.pdf">[PDF]</a>
<a href="../assets/pdf/2017-TIP-TCTF-supplementary.pdf">[SUPP]</a>
<a href="../assets/code/TCTF_code.rar">[Codes]</a>
<a href="../assets/bibtex/2017-TIP-TCTF.txt">[Bibtex]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Dictionary Learning with Structured Noise</strong><br />
<strong>Pan Zhou</strong>, Cong Fang, Zhouchen Lin, Chao Zhang, Edward Y. Chang<br />
Neurocomputing, 2017 <br />
<a href="../assets/pdf/2017-NEUCOM-DLSN.pdf">[PDF]</a>
<a href="../assets/bibtex/2017-NEUCOM-DLSN.txt">[Bibtex]</a>
</p>
</li>



<!-- Item: 1 -->
<li ><p>
<strong>Feature Learning via Partial Differential Equation with Applications to Face Recognition</strong><br />
Cong Fang, Zhenyu Zhao, <strong>Pan Zhou</strong>, Zhouchen Lin<br />
Pattern Recognition
(<strong>PR</strong>), 2017 <br />
<a href="../assets/pdf/2017-PR-FE-PDE.pdf">[PDF]</a>
<a href="../assets/code/LPDE_featurelearning_code.rar">[Codes]</a>
<a href="../assets/bibtex/2017-PR-FE-PDE.txt">[Bibtex]</a>
</p>
</li>


<!-- Item: 1 -->
<li ><p>
<strong>Outlier-Robust Tensor PCA</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng<br />
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2017 <br />
<a href="../assets/pdf/2017-CVPR-RTPCA.pdf">[PDF]</a>
<a href="../assets/pdf/2017-CVPR-RTPCA-supp.pdf">[SUPP]</a>
<a href="../assets/code/OR_TPCA_code.rar">[Codes]</a>
<a href="../assets/bibtex/2017-CVPR-TRPCA.txt">[Bibtex]</a>
</p>
</li>
 

<h4>
	<a name='2016'></a> 2016
</h4>

<!-- Item: 1 -->
<li ><p>
<strong>Bilevel Model Based Discriminative Dictionary Learning for Recognition</strong><br />
<strong>Pan Zhou</strong>, Chao Zhang, Zhouchen Lin<br />
IEEE Transactions on Image Processing
(<strong>TIP</strong>), 2016 <br />
<a href="../assets/pdf/2016-TIP-bilevel.pdf">[PDF]</a>
<a href="../assets/pdf/2016-TIP-bilevel-supp.pdf">[SUPP]</a>
<a href="../assets/bibtex/2016-TIP-bilevel.txt">[Bibtex]</a>
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Integrated Low-Rank-Based Discriminative Feature Learning for Recognition</strong><br />
<strong>Pan Zhou</strong>, Zhouchen Lin, Chao Zhang<br />
IEEE Transactions on Neural Networks and Learning Systems (<strong>TNNLS</strong>), 2016 <br />
<a href="../assets/pdf/2016-TNNLS-Integrated-Low-Rank.pdf">[PDF]</a>
<a href="../assets/pdf/2016-TNNLS-Integrated-Low-Rank-supp.pdf">[SUPP]</a>
<a href="../assets/code/integrated_low_rank code.rar">[Codes]</a>
<a href="../assets/bibtex/2016-TNNLS-Integrated-Low-Rank.txt">[Bibtex]</a>
</p>
</li>



</ol>

 <br>

##### **Books and Patents**
<ol class="biblist"> 
<!-- Item: 1 -->
<li ><p>
<strong>Tensors for Data Processing</strong><br> 
Chapter 6 is contributed by <strong>Pan Zhou</strong>, Canyi Lu, Zhouchen Lin  <br /> 
Elsevier, 2022.   
<a href="https://www.sciencedirect.com/science/article/abs/pii/B9780128244470000121">[PDF]</a>
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Neural network based scene text recognition</strong><br> 
<strong>Pan Zhou</strong>, Peng Tang, Ran Xu, Chu Hong Hoi<br /> 
US Patent, 2022.   
<a href="https://patentimages.storage.googleapis.com/2c/b3/d2/d0a3dcc343b870/US20220237403A1.pdf">[PDF]</a>
</p>
</li>

 
<!-- Item: 1 -->
<li ><p>
<strong>Systems and methods for contrastive learning with self-labeling refinement</strong><br> 
<strong>Pan Zhou</strong>, Caiming Xiong, Chu Hong Hoi<br /> 
US Patent, 2022.   
<a href="https://patentimages.storage.googleapis.com/26/48/86/29fb78a23ee73c/US20220269946A1.pdf">[PDF]</a>
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>System and method for differential architecture search for neural networks</strong><br> 
<strong>Pan Zhou</strong>, Chu Hong Hoi<br /> 
US Patent, 2021.   
<a href="https://patentimages.storage.googleapis.com/ea/8a/b2/ed2e17a1d3937e/US20210383188A1.pdf">[PDF]</a>
</p>
</li>

</ol>
