---
layout: page
permalink: /publication/
title: Publication
description: 
nav: true
nav_order: 2
publication_explorer: true
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

.scholar-citation-badge img {
  height: 20px;
  margin-left: 2px;
  margin-bottom: -5px;
}
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
<li ><p>
<strong>MetaFormer Is Actually What You Need for Vision</strong><br />
Weihao Yu, Mi Luo, <strong>Pan Zhou</strong>, Chenyang Si, Yichen Zhou, Xinchao Wang, Jiashi Feng, Shuicheng Yan<br />
CVPR, 2022 (<font color="#FF0000"><strong>oral</strong></font>),
<a href="https://arxiv.org/abs/2111.11418">[arXiv]</a>
<a href="https://github.com/sail-sg/poolformer">[Code]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:mB3voiENLucC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for MetaFormer">
  <img src="/assets/img/scholar-citations/metaformer-original.svg"
       alt="Google Scholar citations for MetaFormer" />
</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/poolformer?style=social" alt="GitHub stars for sail-sg/poolformer">
<br />
<font color="#2770AB"><b>replacing attention with simple pooling still achieves high performance, breaking "attention is all you need" and revealing network design principle</b></font> <br />
</p>
</li>

<li ><p>
<strong>Prototypical Contrastive Learning of Unsupervised Representations</strong><br />
Junnan Li, <strong>Pan Zhou</strong>, Caiming Xiong, Steven Hoi<br />
ICLR, 2021,
<a href="https://openreview.net/pdf?id=KmykpuSrjcq">[OpenReview]</a>
<a href="../assets/bibtex/2021-ICLR-SSL.txt">[Bibtex]</a>
<a href="https://www.salesforce.com/blog/prototypical-contrastive-learning-pushing-the-frontiers-of-unsupervised-learning/">[Blog]</a>
<a href="https://github.com/salesforce/PCL">[Code]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:Zph67rFs4hoC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for Prototypical Contrastive Learning">
  <img src="/assets/img/scholar-citations/pcl.svg"
       alt="Google Scholar citations for Prototypical Contrastive Learning" />
</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/salesforce/PCL?style=social" alt="GitHub stars for salesforce/PCL"><br />
<font color="#2770AB"><b>the first clustering contrastive learning method to learn high-level semantics, i.e., data cluster structure</b></font> <br />
</p>
</li>

<li ><p>
<strong>Masked Diffusion Transformer is a Strong Image Synthesizer</strong><br />
Shanghua Gao, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br />
ICCV, 2023, <a href="https://arxiv.org/abs/2303.14389">[PDF]</a>
<a href="https://github.com/sail-sg/MDT">[Code]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:lSLTfruPkqcC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for Masked Diffusion Transformer">
  <img src="/assets/img/scholar-citations/mdt.svg"
       alt="Google Scholar citations for Masked Diffusion Transformer" />
</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/MDT?style=social" alt="GitHub stars for sail-sg/MDT">
<a href="https://arxiv.org/abs/2303.14389"
   target="_blank"
   rel="noopener noreferrer">
  <img
    style="margin-left: 2px; margin-bottom: -5px;"
    src="https://img.shields.io/badge/ImageNet%20256x256-SOTA%20FID%201.58%20%28Feb%202024%29-blue.svg"
    alt="SOTA FID 1.58 on ImageNet 256x256 as of February 2024"
  />
</a><br />
<font color="#2770AB"><b>SoTA image generative model</b> on ImageNet 256x256; <b>13x faster learning speed</b> than <a href="https://arxiv.org/abs/2212.09748">DiT</a> (core of <a href="https://openai.com/sora">SORA</a>) </font> <br />
</p>
</li>




<li ><p>
<strong>Consistent3D: Towards Consistent High-Fidelity Text-to-3D Generation with Deterministic Sampling Prior</strong><br />
Zike Wu, <strong>Pan Zhou<sup>+</sup></strong>, Xuanyu YI, Xiaoding Yuan, Hanwang Zhang<br />
CVPR, 2024,
<a href="https://arxiv.org/abs/2401.09050">[arXiv]</a>
<a href="https://github.com/sail-sg/Consistent3D">[Code]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:fPk4N6BV_jEC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for Consistent3D">
  <img src="/assets/img/scholar-citations/consistent3d.svg"
       alt="Google Scholar citations for Consistent3D" />
</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/Consistent3D?style=social" alt="GitHub stars for sail-sg/Consistent3D"><br />
<font color="#2770AB"><b>the first ODE-sampling guided Score Distillation Sampling</b> for 3D generation</font> <br />
</p>
</li>


<!-- Item: 1 -->
<li ><p>
<strong>Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models</strong><br />
Xingyu Xie<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Huan Li, Zhouchen Lin, Shuicheng Yan <br />
TPAMI, 2024 
<a href="https://arxiv.org/abs/2208.06677">[PDF]</a>
<a href="https://github.com/sail-sg/Adan">[Code]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:TFP_iSt0sucC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for Adan">
  <img src="/assets/img/scholar-citations/adan.svg"
       alt="Google Scholar citations for Adan" />
</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/Adan?style=social" alt="GitHub stars for sail-sg/Adan"><br />
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Adan&type=star&count=true" > -->
<font color="#2770AB"><b> 2X-faster and SoTA optimizer on 15+ networks</b> like ResNet, ConvNext, ViT, Swin, MAE, BERT, GPT2, LLAMA, Dreamfusion, DiT, PPO in RL,  etc. <b>Included by 
 popular deep-learning codebases</b> like <a href="https://github.com/NVIDIA/NeMo/blob/main/nemo/core/optim/adan.py">NVIDIA NeMo</a> for LLM,  <a href="https://github.com/huggingface/pytorch-image-models/blob/main/timm/optim/adan.py">HuggingFace Timm</a> and <a href="https://github.com/open-mmlab/mmpretrain/blob/dev-1.x/mmcls/engine/optimizers/adan_t.py">OpenMMLab</a> for CV tasks, <a href="https://github.com/Jittor/jittor/blob/master/python/jittor/optim.py">Jittor of Tsinghua University</a> for 3D.
</font> <br />
</p>
</li>

<!-- Item: 1 -->
<li ><p>
<strong>Win: Weight-Decay-Integrated Nesterov Acceleration for Faster Network Training</strong><br>
<strong>Pan Zhou</strong>, Xingyu Xie, Zhouchen Lin, Kim-Chuan Toh, Shuicheng Yan<br />
JMLR, 2024,
<a href="../assets/pdf/2024-JMLR-win.pdf">[PDF]</a>
<a href="https://github.com/sail-sg/win">[Code]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:bFI3QPDXJZMC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for Win">
  <img src="/assets/img/scholar-citations/win.svg"
       alt="Google Scholar citations for Win" />
</a>
<img style="margin-left: 2px; margin-bottom:-5px; color: black;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/win?style=social" alt="GitHub stars for sail-sg/win"><br />
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" > -->
<font color="#2770AB"><b>accelerate AdamW/Adam/LAMB/SGD by 1.5x on vision and language modeling tasks.</b></font> <br />
</p>
</li>

<li ><p>
<strong>LoCo: Low-Bit Communication Adaptor for Large-scale Model Training</strong><br />
Xingyu Xie, Zhijie Lin, Kim-chuan Toh, <strong>Pan Zhou<sup>+</sup></strong><br />
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2025<br />
<a href="https://arxiv.org/abs/2407.04480">[PDF]</a>
<a href="https://github.com/deepspeedai/DeepSpeed/pull/6730">[Code]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:Mojj43d5GZwC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for LoCo">
  <img src="/assets/img/scholar-citations/loco.svg"
       alt="Google Scholar citations for LoCo" />
</a>
<br />
<font color="#2770AB"><b>On Megatron-LM and FSDP, LoCo significantly improves communication efficiency, e.g., +14% to +40% improvement on Adam's overall training speed without performance degradation on LLaMAs and MoEs. LoCo has been included by the popular <a href="https://github.com/deepspeedai/DeepSpeed/pull/6730">DeepSpeed</a> codebase.</b></font> <br />
</p>
</li>


<li ><p>
<strong>Towards Understanding Convergence and Generalization of AdamW</strong><br>
<strong>Pan Zhou</strong>, Xingyu Xie, Zhouchen Lin, Shuicheng Yan<br />
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2024<br />
<a href="../assets/pdf/2024-TPAMI-AdamW.pdf">[PDF]</a>
<a href="../assets/pdf/2024-TPAMI-AdamW-supp.pdf">[Supp]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:ns9cj8rnVeAC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for AdamW convergence and generalization">
  <img src="/assets/img/scholar-citations/adamw.svg"
       alt="Google Scholar citations for AdamW convergence and generalization" />
</a>
<br />
<font color="#2770AB"><b>the first theory to establish the convergence rate and generalization bound of AdamW </b></font> <br />
</p>
</li>


<!-- Item: 1 -->
 <li ><p>
<strong>Towards Theoretically Understanding Why SGD Generalizes Better Than ADAM in Deep Learning</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng, Chao Ma, Caiming Xiong, Steven Hoi, and Weinan E<br /> 
NeurIPS, 2020, 
<a href="../assets/pdf/2020_generalization.pdf">[PDF]</a>
<a href="../assets/pdf/2020_generalization_supp.pdf">[SUPP]</a>
<a href="https://arxiv.org/pdf/2010.05627.pdf">[arXiv]</a>
<a href="../assets/bibtex/2020_generalization_bib.txt">[Bibtex]</a>
<a href="https://github.com/salesforce/comparison_SGD_ADAM">[Code]</a>
<a href="../assets/pdf/2020-NIPS-SGD-slides.pdf">[Slides]</a>
<a href="../assets/pdf/2020-NIPS-SGD-poster.pdf">[Poster]</a>
<a class="scholar-citation-badge"
   href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;user=0b7ZqlcAAAAJ&amp;citation_for_view=0b7ZqlcAAAAJ:4TOpqqG69KYC"
   target="_blank" rel="noopener noreferrer"
   aria-label="View Google Scholar citations for the SGD generalization paper">
  <img src="/assets/img/scholar-citations/sgd-generalization.svg"
       alt="Google Scholar citations for the SGD generalization paper" />
</a>
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

<section class="publication-explorer" data-publication-explorer>
<div class="publication-controls" hidden>
  <div class="publication-filter-panels">
    <div class="publication-filter-dropdown" data-filter-dropdown>
      <button
        class="publication-filter-trigger"
        type="button"
        aria-haspopup="true"
        aria-expanded="false"
        data-filter-trigger
      >
        <span data-filter-label>All</span>
        <span class="publication-filter-chevron" aria-hidden="true"></span>
      </button>
      <div class="publication-filter-menu" role="group" aria-label="Research topic">
        <button class="publication-filter-option" type="button" data-research-line-filter="all" aria-pressed="true">All</button>
        {% for research_line in site.data.publication_taxonomy %}
          <button
            class="publication-filter-option"
            type="button"
            data-research-line-filter="{{ research_line.id }}"
            aria-pressed="false"
          >{{ research_line.label }}</button>
        {% endfor %}
      </div>
    </div>

    <div class="publication-subtopics" data-publication-subtopics hidden>
      {% for research_line in site.data.publication_taxonomy %}
        {% if research_line.subtopics.size > 0 %}
          <div
            class="publication-filter-dropdown"
            data-subtopic-group="{{ research_line.id }}"
            data-filter-dropdown
            hidden
          >
            <button
              class="publication-filter-trigger"
              type="button"
              aria-haspopup="true"
              aria-expanded="false"
              data-filter-trigger
            >
              <span data-filter-label>All</span>
              <span class="publication-filter-chevron" aria-hidden="true"></span>
            </button>
            <div class="publication-filter-menu" role="group" aria-label="{{ research_line.label }} subtopics">
              <button class="publication-filter-option" type="button" data-subtopic-filter="all" aria-pressed="true">All</button>
              {% for subtopic in research_line.subtopics %}
                <button
                  class="publication-filter-option"
                  type="button"
                  data-subtopic-filter="{{ subtopic.id }}"
                  aria-pressed="false"
                >{{ subtopic.label }}</button>
              {% endfor %}
            </div>
          </div>
        {% endif %}
      {% endfor %}
    </div>
  </div>

  <div class="publication-status" aria-live="polite">
    <span data-publication-count>96 publications</span>
  </div>
</div>

<!-- <div class="container">
	
	<button onclick="select()" class="bygroup">Selected Publications</button>	
	
    <button onclick="year()" class="bygroup">By Year</button>
    
    <button onclick="topic()" class="bygroup">By Topic</button>
    
    <button onclick="scholar()" class="bygroup">Google Scholar</button>
</div> -->

<!-- ### Full Publications -->
<!--
  New publication checklist:
  1. Copy an existing <li class="publication-item"> entry into the correct year.
  2. Give it a unique id and set data-year, data-research-line, and data-keywords.
  3. Efficiency Optimization and Learning Frameworks also require data-subtopic.
  4. Architecture Design must not have data-subtopic.
  5. Run: bundle exec ruby scripts/validate_publications.rb
-->
<div class="publication-list" data-publication-list>
<section class="publication-year-group" data-publication-year-group data-year="2026" aria-labelledby="publications-2026">
<h4 id="publications-2026" class="publication-year" data-year="2026">
<a name="2026"></a> 2026
</h4>
<ol class="biblist">
<li id="pub-2026-smart-when-is-it-actually-worth-expanding-a-speculative-tree" class="publication-item" data-year="2026" data-research-line="efficiency-optimization" data-subtopic="efficient-inference" data-keywords="efficient inference, model acceleration, decoding efficiency, speculative decoding, large language model"><p>
<strong>SMART: When is it Actually Worth Expanding a Speculative Tree?</strong><br />
Lifu Wang, <strong>Pan Zhou<sup>+</sup></strong><br /> 
European Conference on Computer Vision (<strong>ECCV</strong>), 2026 <br />
<a href="https://arxiv.org/pdf/2604.09731">[arXiv]</a>
<span>[Code coming soon]</span>
</p>
</li>
 
<li id="pub-2026-variational-speculative-decoding-rethinking-draft-training-from-token-likelihood-to-sequence-acceptance" class="publication-item" data-year="2026" data-research-line="efficiency-optimization" data-subtopic="efficient-inference" data-keywords="efficient inference, model acceleration, decoding efficiency, speculative decoding, large language model"><p>
<strong>Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance</strong><br />
Xiandong Zou, Jianshu Li, Jing Huang, <strong>Pan Zhou<sup>+</sup></strong><br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2026 <br />
<a href="https://arxiv.org/html/2602.05774v1">[arXiv]</a>
<span>[Code coming soon]</span>
</p>
</li>

 
<li id="pub-2026-towards-scalable-and-consistent-3d-editing" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model, 3D vision"><p>
<strong>Towards Scalable and Consistent 3D Editing</strong><br />
Ruihao Xia, Yang Tang<sup>+</sup>, <strong>Pan Zhou<sup>+</sup></strong><br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2026 <br />
<a href="https://arxiv.org/abs/2510.02994">[arXiv]</a>
<a href="https://www.lv-lab.org/3DEditFormer/">[Code]</a>
</p>
</li>

<li id="pub-2026-towards-uniformity-and-alignment-for-multimodal-representation-learning" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, vision language and speech"><p>
<strong>Towards Uniformity and Alignment for Multimodal Representation Learning</strong><br />
 Wenzhe Yin, <strong>Pan Zhou<sup>+</sup></strong>, Zehao Xiao, Jie Liu, Shujian Yu, Jan-Jakob Sonke, Stratis Gavves  <br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2026 <br />
<a href="https://arxiv.org/abs/2602.09507">[arXiv]</a>
<span>[Code coming soon]</span>
</p>
</li>

<li id="pub-2026-tranx-adapter-bridging-artifacts-and-semantics-within-mllms-for-robust-ai-generated-image-detection" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, large language model"><p>
<strong>TranX-Adapter: Bridging Artifacts and Semantics within MLLMs for Robust AI-generated Image Detection</strong><br />
Wenbin Wang, Yuge Huang, Jianqing Xu, Yue Yu, Jiangtao Yan, Shouhong Ding, <strong>Pan Zhou<sup>+</sup></strong>, Yong Luo<sup>+</sup> <br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2026 <br />
<a href="https://arxiv.org/abs/2602.21716">[arXiv]</a>
<span>[Code coming soon]</span>
</p>
</li>



<li id="pub-2026-anatomical-domain-shifts-test-time-heterogeneous-adaptation-for-3d-human-pose-prediction" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, 3D vision, domain adaptation"><p>
<strong>Anatomical Domain Shifts: Test-time Heterogeneous Adaptation for 3D Human Pose Prediction</strong><br />
Qiongjie Cui, <strong>Pan Zhou</strong>, Jingjing Chen, Na Zhao<br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2026<br />
  <!-- <a href="https://arxiv.org/abs/2510.17439">[arXiv]</a>
  <a href="https://falcon-vla.github.io/">[Code]</a> -->
  <!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br /> -->
</p>
</li>

<li id="pub-2026-from-spatial-to-actions-grounding-vision-language-action-model-in-spatial-foundation-priors" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, vision language and speech"><p>
<strong>From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors</strong><br />
Zhengshen Zhang, Hao Li, Yalun Dai, Zhengbang Zhu, Lei Zhou, Chenchen Liu, Dong Wang, Francis E. H. Tay, Sijin Chen, Ziwei Liu, Yuxiao Liu<sup>+</sup>, Xinghang Li<sup>+</sup>, <strong>Pan Zhou<sup>+</sup></strong><br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2026 <br />
  <a href="https://arxiv.org/abs/2510.17439">[arXiv]</a>
  <a href="https://falcon-vla.github.io/">[Code]</a>
  <!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br /> -->
</p>
</li>



<li id="pub-2026-dreamcs-geometry-aware-text-to-3d-generation-with-unpaired-3d-reward-supervision" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model, 3D vision"><p>
<strong>DreamCS: Geometry-Aware Text-to-3D Generation with Unpaired 3D Reward Supervision</strong><br />
Xiandong Zou, Ruihao Xia, Hongsong Wang, <strong>Pan Zhou<sup>+</sup></strong> <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2026 <br />
  <a href="https://arxiv.org/abs/2506.09814">[arXiv]</a>
  <span>[Code coming soon]</span>
  <!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br /> -->
</p>
</li>
 
<li id="pub-2026-bridging-draft-policy-misalignment-group-tree-optimization-for-speculative-decoding" class="publication-item" data-year="2026" data-research-line="efficiency-optimization" data-subtopic="efficient-inference" data-keywords="efficient inference, model acceleration, decoding efficiency, speculative decoding, large language model, deep optimization"><p>
<strong>Bridging Draft Policy Misalignment: Group Tree Optimization for Speculative Decoding</strong><br />
Shijing Hu, Jingyang Li, Zhihui Lu, <strong>Pan Zhou</strong><br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2026 <br />
  <a href="https://arxiv.org/abs/2509.22134">[arXiv]</a>
  <span>[Code coming soon]</span>
  <!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br /> -->
</p>
</li>


<li id="pub-2026-dragging-with-geometry-from-pixels-to-geometry-guided-image-editing" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model"><p>
<strong>Dragging with Geometry: From Pixels to Geometry-Guided Image Editing</strong><br />
Xinyu Pu, Hongsong Wang, Jie Gui, <strong>Pan Zhou</strong> <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2026 <br />
  <a href="https://arxiv.org/abs/2509.25740">[arXiv]</a>
  <span>[Code coming soon]</span>
  <!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br /> -->
</p>
</li>

<li id="pub-2026-stacked-from-one-multi-scale-self-injection-for-context-window-extension" class="publication-item" data-year="2026" data-research-line="efficiency-optimization" data-subtopic="efficient-inference" data-keywords="efficient inference, model acceleration, decoding efficiency, long context, context window, large language model"><p>
<strong>Stacked from One: Multi-Scale Self-Injection for Context Window Extension</strong><br />
Wei Han, <strong>Pan Zhou<sup>+</sup></strong>, Shuicheng YAN <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2026 <br />
  <a href="https://openreview.net/forum?id=lh3Aa1u7kU&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICLR.cc%2F2026%2FConference%2FAuthors%23your-submissions)">[OpenReview]</a>
  <span>[Code coming soon]</span>
  <!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br /> -->
</p>
</li>




<li id="pub-2026-distributional-vision-language-alignment-by-cauchy-schwarz-divergence" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, vision language and speech"><p>
<strong>Distributional Vision-Language Alignment by Cauchy-Schwarz Divergence</strong><br />
Wenzhe Yin, Zehao Xiao, <strong>Pan Zhou<sup>+</sup></strong>, Shujian Yu, Jiayi Shen, Jan-Jakob Sonke, Stratis Gavves <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2026 <br />
  <a href="https://arxiv.org/abs/2502.17028">[arXiv]</a>
  <span>[Code coming soon]</span>
  <!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br /> -->
</p>
</li>


<li id="pub-2026-architecture-agnostic-test-time-adaptation-via-backprop-free-embedding-alignment" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, domain adaptation"><p>
<strong>Architecture-Agnostic Test-Time Adaptation via Backprop-Free Embedding Alignment</strong><br />
MA Xiao, Young D. Kwon, <strong>Pan Zhou</strong>, Dong Ma<br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2026 <br />
  <a href="https://openreview.net/forum?id=7kLNGaAHaw">[OpenReview]</a>
  <span>[Code coming soon]</span>
  <!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br /> -->
</p>
</li>



<li id="pub-2026-semat-semantic-enhanced-natural-image-interactive-matting" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, dense prediction"><p>
<strong>SEMat: Semantic Enhanced Natural Image Interactive Matting</strong><br />
Ruihao Xia, Yu Liang, Peng-Tao Jiang, Hao Zhang, Qianru Sun, Yang Tang,  Bo Li, and <strong>Pan Zhou</strong> <br /> 
IEEE Transactions on Circuits and Systems for Video Technology (<strong>TCSVT</strong>), 2026<br />
<a href="https://arxiv.org/html/2410.06593v1">[arXiv]</a>
<!-- <a href="../assets/bibtex/2021-AAAI-Medical.txt">[Bibtex]</a> -->
<a href="https://github.com/XiaRho/SEMat">[Code]</a>
<!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/ha-lins/GEML-MDG?style=social" alt="GitHub stars for ha-lins/GEML-MDG"> -->
</p>
</li>

<li id="pub-2026-revisiting-the-canonicalization-for-fast-and-accurate-crystal-tensor-property-prediction" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, low-rank representation"><p>
<strong>Revisiting the Canonicalization for Fast and Accurate Crystal Tensor Property Prediction</strong><br />
Haowei Hua, Jingwen Yang, Wanyu Lin, <strong>Pan Zhou</strong> <br /> 
Association for the Advancement of Artificial Intelligence (<strong>AAAI</strong>), 2026 (<strong>oral</strong>)<br />
<a href="https://arxiv.org/pdf/2410.02372">[arXiv]</a>
<!-- <a href="../assets/bibtex/2021-AAAI-Medical.txt">[Bibtex]</a>
<a href="https://github.com/ha-lins/GEML-MDG">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/ha-lins/GEML-MDG?style=social" alt="GitHub stars for ha-lins/GEML-MDG"> -->
</p>
</li>


<li id="pub-2026-realign-text-to-motion-generation-via-step-aware-reward-guided-alignment" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model, motion generation"><p>
<strong>ReAlign: Text-to-Motion Generation via Step-Aware Reward-Guided Alignment</strong><br />
Wanjiang Weng, Xiaofeng Tan, Junbo Wang, Guo-Sen Xie, <strong>Pan Zhou</strong>, Hongsong Wang<br /> 
Association for the Advancement of Artificial Intelligence (<strong>AAAI</strong>), 2026 <br />
<a href="https://arxiv.org/abs/2505.04974">[arXiv]</a>
<a href="https://wengwanjiang.github.io/ReAlign-page/">[Code]</a>
<!--<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/ha-lins/GEML-MDG?style=social" alt="GitHub stars for ha-lins/GEML-MDG"> -->
</p>
</li>

<li id="pub-2026-benchmarking-gaslighting-attacks-against-speech-large-language-models" class="publication-item" data-year="2026" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, large language model"><p>
<strong>Benchmarking Gaslighting Attacks Against Speech Large Language Models</strong><br />
Jinyang Wu, Bin Zhu<sup>+</sup>, Xiandong Zou, Qiquan Zhang, Xu Fang, <strong>Pan Zhou<sup>+</sup></strong><br /> 
IEEE International Conference on Acoustics, Speech, and Signal Processing  (<strong>ICASSP</strong>), 2026 <br />
<a href="https://arxiv.org/abs/2509.19858">[arXiv]</a>
<!--<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/ha-lins/GEML-MDG?style=social" alt="GitHub stars for ha-lins/GEML-MDG"> -->
</p>
</li>
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2025" aria-labelledby="publications-2025">
<h4 id="publications-2025" class="publication-year" data-year="2025">
<a name="2025"></a> 2025
</h4>
<ol class="biblist">
<li id="pub-2025-loco-low-bit-communication-adaptor-for-large-scale-model-training" class="publication-item" data-year="2025" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="efficient training, memory efficiency, scalable optimization, low-bit communication, distributed training, large language model, low-bit learning"><p>
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




<li id="pub-2025-a-causality-aware-paradigm-for-evaluating-creativity-of-multimodal-large-language-models" class="publication-item" data-year="2025" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, large language model, vision language and speech"><p>
<strong>A Causality-aware Paradigm for Evaluating Creativity of Multimodal Large Language Models</strong><br>
Zhongzhan Huang<sup>*</sup>, Shanshan Zhong<sup>*</sup>, <strong>Pan Zhou<sup>*</sup></strong>, Shanghua Gao, Marinka Zitnik, Liang Lin  <br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2025<br />
<a href="https://arxiv.org/abs/2501.15147">[PDF]</a>
<a href="https://lotbench.github.io/">[Code]</a>
<iframe
      title="GitHub stars for sail-sg/CLoT"
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=CLoT&type=star&count=true" >
</iframe>
</p>
</li>

<li id="pub-2025-gamba-marry-gaussian-splatting-with-mamba-for-single-view-3d-reconstruction" class="publication-item" data-year="2025" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design, 3D vision"><p>
<strong>Gamba: Marry Gaussian Splatting with Mamba for Single-View 3D Reconstruction</strong><br>
Qiuhong Shen, Zike Wu, Xuanyu Yi, <strong>Pan Zhou</strong>, Hanwang Zhang, Shuicheng Yan, Xinchao Wang  <br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2025<br />
<a href="https://arxiv.org/abs/2403.18795">[PDF]</a>
<a href="https://florinshen.github.io/gamba-project/">[Code]</a>
<iframe
      title="GitHub stars for SkyworkAI/Gamba"
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=SkyworkAI&repo=Gamba&type=star&count=true" >
</iframe>
</p>
</li>



<!-- Item: 1 -->
<li id="pub-2025-griffin-effective-token-alignment-for-faster-speculative-decoding" class="publication-item" data-year="2025" data-research-line="efficiency-optimization" data-subtopic="efficient-inference" data-keywords="efficient inference, model acceleration, decoding efficiency, speculative decoding, large language model"><p>
<strong>GRIFFIN: Effective Token Alignment for Faster Speculative Decoding</strong><br />
Shijing Hu, Jingyang Li, Xingyu Xie, Zhihui Lu, Kim-Chuan Toh, <strong>Pan Zhou</strong><br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2025<br />
<a href="https://arxiv.org/abs/2502.11018">[PDF]</a>
<a href="https://github.com/hsj576/GRIFFIN">[Code]</a> 
</p>
</li>


<!-- Item: 1 -->
<li id="pub-2025-sopo-text-to-motion-generation-using-semi-online-preference-optimization" class="publication-item" data-year="2025" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model, motion generation, deep optimization"><p>
<strong>SoPo: Text-to-motion generation using semi-online preference optimization</strong><br />
Xiaofeng Tan, Hongsong Wang, Xin Geng, <strong>Pan Zhou</strong><br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2025<br />
<a href="https://arxiv.org/abs/2412.05095">[PDF]</a>
<a href="https://xiaofeng-tan.github.io/projects/SoPo/">[Code]</a> 
</p>
</li>


<!-- Item: 1 -->
<li id="pub-2025-memory-efficient-4-bit-preconditioned-stochastic-optimization" class="publication-item" data-year="2025" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="efficient training, memory efficiency, scalable optimization, low-bit learning, deep optimization"><p>
<strong>Memory-Efficient 4-bit Preconditioned Stochastic Optimization</strong><br />
Jingyang Li, Kuangyu Ding, Kim-chuan Toh, <strong>Pan Zhou<sup>+</sup></strong><br /> 
International Conference on Computer Vision (<strong>ICCV</strong>), 2025<br />
<a href="https://arxiv.org/abs/2412.10663">[PDF]</a>
</p>
</li>
 
 
<!-- Item: 1 -->
<li id="pub-2025-zeroth-order-fine-tuning-of-llms-in-random-subspaces" class="publication-item" data-year="2025" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="efficient training, memory efficiency, scalable optimization, large language model, low-rank representation"><p>
<strong>Zeroth-Order Fine-Tuning of LLMs in Random Subspaces</strong><br />
Ziming Yu, <strong>Pan Zhou</strong>, Sike Wang, Jia Li, Mi Tian, Hua Huang<br /> 
International Conference on Computer Vision (<strong>ICCV</strong>), 2025<br />
<a href="https://arxiv.org/abs/2410.08989">[PDF]</a>
<a href="https://github.com/zimingyy/SubZero">[Code]</a> 
</p>
</li>

<!-- Item: 1 -->
<li id="pub-2025-probabilistic-prototype-calibration-of-vision-language-models-for-generalized-few-shot-semantic-segmentation" class="publication-item" data-year="2025" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, vision language and speech, few-shot and meta-learning, dense prediction"><p>
<strong>Probabilistic Prototype Calibration of Vision-language Models for Generalized Few-shot Semantic Segmentation</strong><br />
Jie Liu, Jiayi Shen, <strong>Pan Zhou<sup>+</sup></strong>, Jan-Jakob Sonke, Stratis Gavves<br /> 
International Conference on Computer Vision (<strong>ICCV</strong>), 2025<br />
<a href="https://arxiv.org/abs/2506.22979">[PDF]</a>
<a href="https://github.com/jliu4ai/FewCLIP">[Code]</a> 
</p>
</li>

 
<li id="pub-2025-hps-hard-preference-sampling-for-human-preference-alignment" class="publication-item" data-year="2025" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model"><p>
<strong>HPS: Hard Preference Sampling for Human Preference Alignment</strong><br />
Xiandong Zou, Wanyu Lin, Yuchen Li, <strong>Pan Zhou<sup>+</sup></strong><br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2025 <br />
<a href="https://arxiv.org/abs/2502.14400">[arXiv]</a>
<a href="https://github.com/LVLab-SMU/HPS">[Code]</a> 
</p>
</li>
 

<li id="pub-2025-probabilistic-interactive-3d-segmentation-with-hierarchical-neural-processes" class="publication-item" data-year="2025" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, 3D vision, dense prediction"><p>
<strong>Probabilistic Interactive 3D Segmentation with Hierarchical Neural Processes</strong><br />
Jie Liu, <strong>Pan Zhou<sup>+</sup></strong>, Zehao Xiao, Jiayi Shen, Wenzhe Yin, Jan-Jakob Sonke, Efstratios Gavves<br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2025 <br />
<a href="https://jliu4ai.github.io/media/NPISeg3D.pdf">[PDF]</a>
<a href="https://github.com/jliu4ai/NPISeg3D">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/NPISeg3D?style=social" alt="GitHub stars for jliu4ai/NPISeg3D"><br />
</p>
</li>
 

<li id="pub-2025-collaborative-tree-search-for-enhancing-embodied-multi-agent-collaboration" class="publication-item" data-year="2025" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, embodied agent"><p>
<strong>Collaborative Tree Search for Enhancing Embodied Multi-Agent Collaboration</strong><br />
Lizheng Zu, Lin Lin, Song Fu, Na Zhao, <strong>Pan Zhou</strong> <br />  
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2025<br />
  <a href="../assets/pdf/2025-CVPR-CoTS.pdf">[PDF]</a> 
  <a href="https://github.com/zulihit/CoTS">[Code]</a>
  <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/zulihit/CoTS?style=social" alt="GitHub stars for zulihit/CoTS"><br />
</p>
</li>


<li id="pub-2025-towards-understanding-why-fixmatch-generalizes-better-than-supervised-learning" class="publication-item" data-year="2025" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework"><p>
<strong>Towards Understanding Why FixMatch Generalizes Better Than Supervised Learning</strong><br />
Jingyang Li, Jiachun Pan, Vincent Y. F. Tan, Kim-chuan Toh, <strong>Pan Zhou<sup>+</sup></strong><br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2025 (<strong>oral, 1.8% acceptance rate</strong>) <br />
  <a href="https://arxiv.org/abs/2410.11206">[arXiv]</a>
</p>
</li>

<li id="pub-2025-capo-cooperative-plan-optimization-for-efficient-embodied-multi-agent-cooperation" class="publication-item" data-year="2025" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, embodied agent, deep optimization"><p>
<strong>CaPo: Cooperative Plan Optimization for Efficient Embodied Multi-Agent Cooperation</strong><br />
Jie Liu, <strong>Pan Zhou<sup>+</sup></strong>, Yingjun Du, Ah-Hwee Tan, Cees G. M. Snoek, Jan-Jakob Sonke, Efstratios Gavves <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2025 <br />
  <a href="https://arxiv.org/abs/2411.04679">[arXiv]</a>
  <a href="https://github.com/jliu4ai/CaPo">[Code]</a>
  <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/jliu4ai/CaPo?style=social" alt="GitHub stars for jliu4ai/CaPo"><br />
</p>
</li>
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2024" aria-labelledby="publications-2024">
<h4 id="publications-2024" class="publication-year" data-year="2024">
<a name="2024"></a> 2024
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2024-win-weight-decay-integrated-nesterov-acceleration-for-faster-network-training" class="publication-item" data-year="2024" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Win: Weight-Decay-Integrated Nesterov Acceleration for  Faster Network Training</strong><br>
<strong>Pan Zhou</strong>, Xingyu Xie, Zhouchen Lin, Kim-Chuan Toh, Shuicheng Yan  <br /> 
Journal of Machine Learning Research (<strong>JMLR</strong>), 2024<br />
<a href="../assets/pdf/2024-JMLR-win.pdf">[PDF]</a>
<a href="https://github.com/sail-sg/win">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/win?style=social" alt="GitHub stars for sail-sg/win">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" > -->
</p>
</li>

<li id="pub-2024-adan-adaptive-nesterov-momentum-algorithm-for-faster-optimizing-deep-models" class="publication-item" data-year="2024" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models</strong><br />
Xingyu Xie<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Huan Li, Zhouchen Lin, Shuicheng Yan <br />
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2024<br />
<a href="https://arxiv.org/abs/2208.06677">[PDF]</a>
<a href="https://github.com/sail-sg/Adan">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/Adan?style=social" alt="GitHub stars for sail-sg/Adan"><br />
</p>
</li>

<!-- Item: 1 -->
<li id="pub-2024-instant3d-instant-text-to-3d-generation" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model, 3D vision"><p>
<strong>Instant3D: Instant Text-to-3D Generation</strong><br>
Ming Li, <strong>Pan Zhou</strong>, Jia-Wei Liu, Jussi Keppo, Min Lin, Shuicheng Yan, Xiangyu Xu  <br /> 
International Journal of Computer Vision (<strong>IJCV</strong>), 2024<br />
<a href="https://arxiv.org/abs/2311.08403">[PDF]</a>
<a href="https://ming1993li.github.io/Instant3DProj/">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/ming1993li/Instant3DCodes?style=social" alt="GitHub stars for ming1993li/Instant3DCodes">
<!-- src="https://ghbtns.com/github-btn.html?user=ming1993li&repo=Instant3DCodes&type=star&count=true" > -->
</p>
</li>

<!-- Item: 1 -->
<li id="pub-2024-enhancing-visual-grounding-in-vision-language-pre-training-with-position-guided-text-prompts" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, vision language and speech"><p>
<strong>Enhancing Visual Grounding in Vision-Language Pre-Training with Position-Guided Text Prompts</strong><br>
Alex Jinpeng Wang, <strong>Pan Zhou</strong>, Mike Zheng Shou, Shuicheng Yan  <br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2024<br />
<a href="https://ieeexplore.ieee.org/document/10363674">[PDF]</a>
<a href="https://github.com/sail-sg/ptp">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/ptp?style=social" alt="GitHub stars for sail-sg/ptp">,
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ptp&type=star&count=true" > -->
<a href="https://paperswithcode2.com/benchmark/78504"
   target="_blank"
   rel="noopener noreferrer">
  <img
    style="margin-left: 2px; margin-bottom: -5px;"
    src="https://img.shields.io/badge/COCO%20Retrieval-I2T%20R%401%2081.5%20%28Dec%202022%29-blue.svg"
    alt="PTP-BLIP image-to-text R@1 81.5 on COCO Retrieval in December 2022"
  />
</a>
</p>
</li>




<!-- Item: 1 -->
<li id="pub-2024-towards-understanding-convergence-and-generalization-of-adamw" class="publication-item" data-year="2024" data-research-line="efficiency-optimization" data-subtopic="optimization-theory" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Towards Understanding Convergence and Generalization of AdamW</strong><br>
<strong>Pan Zhou</strong>, Xingyu Xie, Zhouchen Lin, Shuicheng Yan <br />
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2024<br />
<a href="../assets/pdf/2024-TPAMI-AdamW.pdf">[PDF]</a>
<a href="../assets/pdf/2024-TPAMI-AdamW-supp.pdf">[Supp]</a>
</p>
</li>


<li id="pub-2024-unsupervised-modality-adaptation-with-text-to-image-diffusion-models-for-semantic-segmentation" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, diffusion model, domain adaptation, dense prediction"><p>
<strong>Unsupervised Modality Adaptation with Text-to-Image Diffusion Models for Semantic Segmentation</strong><br />
Ruihao Xia, Yu Liang, Peng-Tao Jiang, Hao Zhang, Bo Li, Yang Tang, <strong>Pan Zhou</strong> <br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024<br />
<a href="https://arxiv.org/abs/2410.21708">[arXiv]</a>
<a href="https://github.com/XiaRho/MADM">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/XiaRho/MADM?style=social" alt="GitHub stars for XiaRho/MADM">
</p>
</li>


<li id="pub-2024-lova3-learning-to-visual-question-answering-asking-and-assessment" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, vision language and speech"><p>
<strong>LOVA3: Learning to Visual Question Answering, Asking and Assessment</strong><br />
Hengyuan Zhao, <strong>Pan Zhou</strong><strong><sup>+</sup></strong>, Difei Gao, Mike Zheng Shou<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024<br />
<a href="https://arxiv.org/abs/2405.14974">[arXiv]</a>
<a href="https://github.com/showlab/LOVA3">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/showlab/LOVA3?style=social" alt="GitHub stars for showlab/LOVA3">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ScaleLong&type=star&count=true" > -->
</p>
</li>


<li id="pub-2024-4-bit-shampoo-for-memory-efficient-network-training" class="publication-item" data-year="2024" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="efficient training, memory efficiency, scalable optimization, low-bit learning, deep optimization"><p>
<strong>4-bit Shampoo for Memory-Efficient Network Training</strong><br />
Sike Wang, <strong>Pan Zhou</strong>, Jia Li, Hua Huang<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024<br />
<a href="https://arxiv.org/abs/2405.18144">[arXiv]</a>
<a href="https://github.com/Sike-Wang/low-bit-Shampoo">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/Sike-Wang/low-bit-Shampoo?style=social" alt="GitHub stars for Sike-Wang/low-bit-Shampoo">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ScaleLong&type=star&count=true" > -->
</p>
</li>


<li id="pub-2024-mvgamba-unify-3d-content-generation-as-state-space-sequence-modeling" class="publication-item" data-year="2024" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design, 3D vision"><p>
<strong>MVGamba: Unify 3D Content Generation as State Space Sequence Modeling</strong><br />
Xuanyu Yi, Zike Wu, Qiuhong Shen, Qingshan Xu, <strong>Pan Zhou</strong>, Joo Hwee Lim, Shuicheng YAN, Xinchao Wang, Hanwang Zhang<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2024<br />
<a href="https://arxiv.org/abs/2406.06367">[arXiv]</a>
<a href="https://github.com/SkyworkAI/Gamba">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/SkyworkAI/Gamba?style=social" alt="GitHub stars for SkyworkAI/Gamba">
</p>
</li>


<li id="pub-2024-genixer-empowering-multimodal-large-language-models-as-a-powerful-data-generator" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, large language model, vision language and speech"><p>
<strong>Genixer: Empowering Multimodal Large Language Models as a Powerful Data Generator</strong><br />
Henry Hengyuan Zhao, <strong>Pan Zhou</strong><strong><sup>+</sup></strong>, Mike Zheng Shou <br />
European Conference on Computer Vision (<strong>ECCV</strong>), 2024<br />
<a href="https://arxiv.org/abs/2312.06731">[PDF]</a>
<a href="https://github.com/zhaohengyuan1/Genixer">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/zhaohengyuan1/Genixer?style=social" alt="GitHub stars for zhaohengyuan1/Genixer"><br />
</p>
</li>

<li id="pub-2024-efficient-cascaded-multiscale-adaptive-network-for-image-restoration" class="publication-item" data-year="2024" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design"><p>
<strong>Efficient Cascaded Multiscale Adaptive Network for Image Restoration</strong><br />
Yichen Zhou, <strong>Pan Zhou</strong><strong><sup>+</sup></strong>, Teck Khim Ng <br />
European Conference on Computer Vision (<strong>ECCV</strong>), 2024<br />
</p>
</li>



<!-- Item: 1 -->
<li id="pub-2024-let-s-think-outside-the-box-exploring-leap-of-thought-in-large-language-models-with-multimodal-humor-generation" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, large language model, vision language and speech"><p>
<strong>Let's Think Outside the Box: Exploring Leap-of-Thought in Large Language Models with Multimodal Humor Generation</strong><br />
Shanshan Zhong, Zhongzhan Huang, Shanghua Gao, Wushao Wen, Liang Lin, Marinka Zitnik, <strong>Pan Zhou<sup>+</sup></strong><br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2312.02439">[arXiv]</a>
<a href="https://zhongshsh.github.io/CLoT/">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/CLoT?style=social" alt="GitHub stars for sail-sg/CLoT">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=CLoT&type=star&count=true" > -->
</p>
</li>


<!-- Item: 1 -->
<li id="pub-2024-inceptionnext-when-inception-meets-convnext" class="publication-item" data-year="2024" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design"><p>
<strong>InceptionNeXt: When Inception Meets ConvNeXt</strong><br />
Weihao Yu, <strong>Pan Zhou</strong>, Shuicheng YAN, Xinchao Wang <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2303.16900">[arXiv]</a>
<a href="https://github.com/sail-sg/inceptionnext">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/inceptionnext?style=social" alt="GitHub stars for sail-sg/inceptionnext">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=inceptionnext&type=star&count=true" > -->
</p>
</li>

 

<!-- Item: 1 -->
<li id="pub-2024-consistent3d-towards-consistent-high-fidelity-text-to-3d-generation-with-deterministic-sampling-prior" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model, 3D vision"><p>
<strong>Consistent3D: Towards Consistent High-Fidelity Text-to-3D Generation with Deterministic Sampling Prior</strong><br />
Zike Wu, <strong>Pan Zhou<sup>+</sup></strong>, Xuanyu YI, Xiaoding Yuan, Hanwang Zhang <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2401.09050">[arXiv]</a>
<a href="https://github.com/sail-sg/Consistent3D">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/Consistent3D?style=social" alt="GitHub stars for sail-sg/Consistent3D">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Consistent3D&type=star&count=true" > -->
</p>
</li>


<!-- Item: 1 -->
<li id="pub-2024-friendly-sharpness-aware-minimization" class="publication-item" data-year="2024" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Friendly Sharpness-Aware Minimization</strong><br />
Tao Li, <strong>Pan Zhou<sup>+</sup></strong>, Zhengbao He, Xinwen Cheng, Xiaolin Huang<br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2403.12350">[arXiv]</a>
<a href="https://github.com/nblt/F-SAM">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/nblt/F-SAM?style=social" alt="GitHub stars for nblt/F-SAM">
<!-- src="https://ghbtns.com/github-btn.html?user=nblt&repo=F-SAM&type=star&count=true" > -->
</p>
</li>



<!-- Item: 1 -->
<li id="pub-2024-few-shot-learner-parameterization-by-diffusion-time-steps" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, diffusion model, few-shot and meta-learning"><p>
<strong>Few-shot Learner Parameterization by Diffusion Time-steps</strong><br />
Zhongqi Yue, <strong>Pan Zhou<sup>+</sup></strong>, Richang Hong, Hanwang Zhang, Qianru Sun <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://arxiv.org/abs/2403.02649">[arXiv]</a>
<a href="https://github.com/yue-zhongqi/tif">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/yue-zhongqi/tif?style=social" alt="GitHub stars for yue-zhongqi/tif">
<!-- src="https://ghbtns.com/github-btn.html?user=yue-zhongqi&repo=tif&type=star&count=true" > -->
</p>
</li>


<!-- Item: 1 -->
<li id="pub-2024-diffusion-time-step-curriculum-for-one-image-to-3d-generation" class="publication-item" data-year="2024" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model, 3D vision, diffusion model"><p>
<strong>Diffusion Time-step Curriculum for One Image to 3D Generation</strong><br />
Xuanyu Yi, Zike Wu, Qingshan Xu, <strong>Pan Zhou<sup>+</sup></strong>, Joo Hwee Lim, Hanwang Zhang  <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2024<br />
<a href="https://github.com/yxymessi/DTC123/blob/main/DTC_CVPR.pdf">[PDF]</a>
<a href="https://github.com/yxymessi/DTC123">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/yxymessi/DTC123?style=social" alt="GitHub stars for yxymessi/DTC123">
<!-- src="https://ghbtns.com/github-btn.html?user=yxymessi&repo=DTC123&type=star&count=true" > -->
</p>
</li>
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2023" aria-labelledby="publications-2023">
<h4 id="publications-2023" class="publication-year" data-year="2023">
<a name="2023"></a> 2023
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2023-metaformer-baselines-for-vision" class="publication-item" data-year="2023" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design"><p>
<strong>MetaFormer Baselines for Vision</strong><br />
Weihao Yu, Chenyang Si, <strong>Pan Zhou</strong>, Mi Luo, Yichen Zhou, Jiashi Feng,
Shuicheng Yan,  Xinchao Wang<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2023<br />
<a href="https://arxiv.org/abs/2210.13452">[arXiv]</a>
<a href="https://github.com/sail-sg/metaformer">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/metaformer?style=social" alt="GitHub stars for sail-sg/metaformer">,
<a href="https://paperswithcode2.com/benchmark/78397"
   target="_blank"
   rel="noopener noreferrer">
  <img
    style="margin-left: 2px; margin-bottom: -5px;"
    src="https://img.shields.io/badge/ImageNet--C-SOTA%20mCE%2030.8%20%28Oct%202022%29-blue.svg"
    alt="CAFormer-B36 SOTA mCE 30.8 on ImageNet-C in October 2022"
  />
</a>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=metaformer&type=star&count=true" > -->

<!-- Item: 1 -->
<li id="pub-2023-contrastive-video-question-answering-via-video-graph-transformer" class="publication-item" data-year="2023" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, self-supervised learning, video understanding"><p>
<strong>Contrastive Video Question Answering via Video Graph Transformer</strong><br />
Junbin Xiao, <strong>Pan Zhou</strong>, Angela Yao, Yicong Li, Richang Hong, Shuicheng Yan, Tat-Seng Chua<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2023<br />
<a href="https://arxiv.org/abs/2302.13668">[PDF]</a>
<a href="https://github.com/doc-doc/CoVGT">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/doc-doc/CoVGT?style=social" alt="GitHub stars for doc-doc/CoVGT">
<!-- src="https://ghbtns.com/github-btn.html?user=doc-doc&repo=CoVGT&type=star&count=true" > -->
</p>
</li>

<!-- Item: 1 -->
<li id="pub-2023-iterative-graph-self-distillation" class="publication-item" data-year="2023" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework"><p>
<strong>Iterative Graph Self-Distillation</strong><br />
Hanlin Zhang, Shuai Lin, Weiyang Liu, <strong>Pan Zhou</strong>, Jian Tang, Xiaodan Liang, Eric P. Xing <br /> 
IEEE Transactions on Knowledge and Data Engineering (<strong>TKDE</strong>), 2023 <br />
<a href="https://arxiv.org/abs/2010.12609">[arXiv]</a>
</p>
</li>



<!-- Item: 1 -->
<li id="pub-2023-scalelong-towards-more-stable-training-of-diffusion-model-via-scaling-network-long-skip-connection" class="publication-item" data-year="2023" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design, diffusion model"><p>
<strong>ScaleLong: Towards More Stable Training of Diffusion Model via Scaling Network Long Skip Connection</strong><br />
Zhongzhan Huang, <strong>Pan Zhou<sup>+</sup></strong>, Shuicheng Yan, Liang Lin<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2023<br />
<a href="https://arxiv.org/pdf/2310.13545.pdf">[arXiv]</a>
<a href="https://github.com/sail-sg/ScaleLong">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/ScaleLong?style=social" alt="GitHub stars for sail-sg/ScaleLong">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ScaleLong&type=star&count=true" > -->
</p>
</li>
 

<!-- Item: 1 -->
<li id="pub-2023-masked-diffusion-transformer-is-a-strong-image-synthesizer" class="publication-item" data-year="2023" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model, diffusion model"><p>
<strong>Masked Diffusion Transformer is a Strong Image Synthesizer</strong><br />
Shanghua Gao, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br /> 
International Conference on Computer Vision (<strong>ICCV</strong>), 2023<br />
<a href="https://arxiv.org/abs/2303.14389">[PDF]</a>
<a href="https://github.com/sail-sg/MDT">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/MDT?style=social" alt="GitHub stars for sail-sg/MDT">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=MDT&type=star&count=true" > -->
<a href="https://arxiv.org/abs/2303.14389"
   target="_blank"
   rel="noopener noreferrer">
  <img
    style="margin-left: 2px; margin-bottom: -5px;"
    src="https://img.shields.io/badge/ImageNet%20256x256-SOTA%20FID%201.58%20%28Feb%202024%29-blue.svg"
    alt="SOTA FID 1.58 on ImageNet 256x256 as of February 2024"
  />
</a>
<!-- <iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="150px" height="20px"
    src="https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg" >
</iframe>  -->
</p>
</li>
 

<!-- Item: 1 -->
<li id="pub-2023-editanything-empowering-unparalleled-flexibility-in-image-editing-and-generation" class="publication-item" data-year="2023" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model"><p>
<strong>EditAnything: Empowering Unparalleled Flexibility in Image Editing and Generation</strong><br />
Shanghua Gao, Zhijie Lin, Xingyu Xie, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br /> 
ACM International Conference on Multimedia (<strong>ACMMM</strong>), 2023<br />
<a href="https://dl.acm.org/doi/10.1145/3581783.3612680">[PDF]</a>
<a href="https://github.com/sail-sg/EditAnything">[Code]</a> 
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/EditAnything?style=social" alt="GitHub stars for sail-sg/EditAnything">
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=EditAnything&type=star&count=true" > -->
<!-- <iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="150px" height="20px"
    src="https://huggingface.co/spaces/shgao/EditAnything" >
</iframe>  -->
</p>
</li>

 

<!-- Item: 1 -->
<li id="pub-2023-stprivacy-spatio-temporal-privacy-preserving-action-recognition" class="publication-item" data-year="2023" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, video understanding"><p>
<strong>STPrivacy: Spatio-Temporal Privacy-Preserving Action Recognition</strong><br />
Ming Li, Xiangyu Xu, Hehe Fan, <strong>Pan Zhou</strong>, Jun Liu, Jia-Wei Liu, Jiahe Li, Jussi Keppo, Mike Zheng Shou, Shuicheng Yan<br /> 
International Conference on Computer Vision (<strong>ICCV</strong>), 2023<br />
<a href="https://arxiv.org/abs/2301.03046">[PDF]</a>
</p>
</li>
 


 

<!-- Item: 1 -->
<li id="pub-2023-position-guided-text-prompt-for-vision-language-pre-training" class="publication-item" data-year="2023" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, vision language and speech"><p>
<strong>Position-guided Text Prompt for Vision-Language Pre-training</strong><br />
Alex Jinpeng Wang,  <strong>Pan Zhou<sup>+</sup></strong>, Mike Zheng Shou, Shuicheng Yan <br /> 
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2023<br />
<a href="https://arxiv.org/pdf/2212.09737.pdf">[arXiv]</a>
<a href="https://github.com/sail-sg/ptp">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/ptp?style=social" alt="GitHub stars for sail-sg/ptp">,
<a href="https://paperswithcode2.com/benchmark/78504"
   target="_blank"
   rel="noopener noreferrer">
  <img
    style="margin-left: 2px; margin-bottom: -5px;"
    src="https://img.shields.io/badge/COCO%20Retrieval-I2T%20R%401%2081.5%20%28Dec%202022%29-blue.svg"
    alt="PTP-BLIP image-to-text R@1 81.5 on COCO Retrieval in December 2022"
  />
</a>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ptp&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2023-win-weight-decay-integrated-nesterov-acceleration-for-adaptive-gradient-algorithms" class="publication-item" data-year="2023" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Win: Weight-Decay-Integrated Nesterov Acceleration for Adaptive Gradient Algorithms</strong><br />
<strong>Pan Zhou</strong>, Xingyu Xie, Shuicheng Yan <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2023 (<font color="#FF0000"><strong>oral</strong></font>)<br />
<a href="https://openreview.net/pdf?id=CPdc77SQfQ5">[OpenReview]</a>
<a href="https://github.com/sail-sg/win">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/win?style=social" alt="GitHub stars for sail-sg/win">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2023-towards-understanding-why-mask-reconstruction-pretraining-helps-in-downstream-tasks" class="publication-item" data-year="2023" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework"><p>
<strong>Towards Understanding Why Mask Reconstruction Pretraining Helps in Downstream Tasks</strong><br />
Jiachun Pan<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Shuicheng Yan<br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2023 <br />
  <a href="https://arxiv.org/pdf/2206.03826.pdf">[arXiv]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li id="pub-2023-lpt-long-tailed-prompt-tuning-for-image-classification" class="publication-item" data-year="2023" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework"><p>
<strong>LPT: Long-tailed Prompt Tuning for Image Classification</strong><br />
Bowen Dong, <strong>Pan Zhou</strong>, Shuicheng Yan, Wangmeng Zuo <br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2023 <br />
<a href="https://arxiv.org/abs/2210.01033">[arXiv]</a>
<a href="https://github.com/DongSky/LPT">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/DongSky/LPT?style=social" alt="GitHub stars for DongSky/LPT">,
<a href="https://paperswithcode2.com/benchmark/61182"
   target="_blank"
   rel="noopener noreferrer">
  <img
    style="margin-left: 2px; margin-bottom: -5px;"
    src="https://img.shields.io/badge/CIFAR--100--LT%20rho%3D100-%231%20Error%2010.9%20%28Oct%202022%29-blue.svg"
    alt="LPT ranked first with error rate 10.9 on CIFAR-100-LT rho 100 in October 2022"
  />
</a>
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=DongSky&repo=LPT&type=star&count=true" > -->
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2022" aria-labelledby="publications-2022">
<h4 id="publications-2022" class="publication-year" data-year="2022">
<a name="2022"></a> 2022
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2022-prototypical-graph-contrastive-learning" class="publication-item" data-year="2022" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, self-supervised learning"><p>
<strong>Prototypical Graph Contrastive Learning</strong><br />
Shuai Lin,  Chen Liu, <strong>Pan Zhou</strong>,  Zi-yuan Hu,  Shuojia Wang,  Ruihui Zhao,  Yefeng Zheng,  Liang Lin,  Eric Xing,  Xiaodan Liang<br /> 
IEEE Transactions on Neural Networks and Learning Systems (<strong>TNNLS</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2106.09645">[arXiv]</a>
<a href="https://github.com/ha-lins/PGCL">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/ha-lins/PGCL?style=social" alt="GitHub stars for ha-lins/PGCL">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=ha-lins&repo=PGCL&type=star&count=true" > -->
 


<!-- Item: 1 -->
<li id="pub-2022-inception-transformer" class="publication-item" data-year="2022" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design"><p>
<strong>Inception Transformer</strong><br />
Chenyang Si<strong><sup>*</sup></strong>, Weihao Yu<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong>, Yichen Zhou, Xinchao Wang, Shuicheng Yan<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2022 (<font color="#FF0000"><strong>oral</strong></font>)<br />
<a href="https://arxiv.org/abs/2205.12956">[arXiv]</a>
<a href="https://github.com/sail-sg/iFormer">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/iFormer?style=social" alt="GitHub stars for sail-sg/iFormer">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=iFormer&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2022-mugs-a-multi-granular-self-supervised-learning-framework" class="publication-item" data-year="2022" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, self-supervised learning"><p>
<strong>Mugs: A Multi-Granular Self-Supervised Learning Framework</strong><br />
<strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Yichen Zhou<strong><sup>*</sup></strong>, Chenyang Si<strong><sup>*</sup></strong>,  Weihao Yu, Teck Khim Ng, Shuicheng Yan<br />
Workshop of Neural Information Processing Systems, 2022.<br />
<a href="https://arxiv.org/abs/2203.14415">[arXiv]</a>
<a href="https://github.com/sail-sg/mugs">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/mugs?style=social" alt="GitHub stars for sail-sg/mugs">
<a href="https://arxiv.org/abs/2203.14415"
   target="_blank"
   rel="noopener noreferrer">
  <img
    style="margin-left: 2px; margin-bottom: -5px;"
    src="https://img.shields.io/badge/ImageNet--1K%20Linear-SOTA%2082.1%25%20%28Mar%202022%29-blue.svg"
    alt="Mugs SOTA linear probing accuracy 82.1 percent on ImageNet-1K in March 2022"
  />
</a><br />
<font color="#2770AB"><b>Top linear probing and KNN performance on ImageNet without extra data</b></font><br />
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=mugs&type=star&count=true" > -->


<!-- Item: 1 -->
<li id="pub-2022-dualformer-local-global-stratified-transformer-for-efficient-video-recognition" class="publication-item" data-year="2022" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design, video understanding"><p>
<strong>DualFormer: Local-Global Stratified Transformer for Efficient Video Recognition</strong><br />
Yuxuan Liang, <strong>Pan Zhou</strong>, Roger Zimmermann, Shuicheng Yan <br /> 
European Conference on Computer Vision (<strong>ECCV</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2112.04674">[arXiv]</a>
<a href="https://github.com/sail-sg/dualformer">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/dualformer?style=social" alt="GitHub stars for sail-sg/dualformer">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=dualformer&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2022-video-graph-transformer-for-video-question-answering" class="publication-item" data-year="2022" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design, video understanding"><p>
<strong>Video Graph Transformer for Video Question Answering</strong><br />
Junbin Xiao, <strong>Pan Zhou</strong>, Tat-Seng Chua, Shuicheng Yan <br /> 
European Conference on Computer Vision (<strong>ECCV</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2207.05342">[arXiv]</a>
<a href="https://github.com/sail-sg/VGT">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/VGT?style=social" alt="GitHub stars for sail-sg/VGT">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=VGT&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2022-self-promoted-supervision-for-few-shot-transformer" class="publication-item" data-year="2022" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, few-shot and meta-learning"><p>
<strong>Self-Promoted Supervision for Few-Shot Transformer</strong><br />
Bowen Dong, <strong>Pan Zhou</strong>, Shuicheng Yan, Wangmeng Zuo <br /> 
European Conference on Computer Vision (<strong>ECCV</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2203.07057">[arXiv]</a>
<a href="https://github.com/DongSky/few-shot-vit">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/DongSky/few-shot-vit?style=social" alt="GitHub stars for DongSky/few-shot-vit">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=DongSky&repo=few-shot-vit&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2022-metaformer-is-actually-what-you-need-for-vision" class="publication-item" data-year="2022" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design"><p>
  <strong>MetaFormer is Actually What You Need for Vision</strong><br />
  Weihao Yu, Mi Luo, <strong>Pan Zhou</strong>, Chenyang Si, Yichen Zhou, Xinchao Wang, Jiashi Feng, Shuicheng Yan <br /> 
  IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2022 (<font color="#FF0000"><strong>oral</strong></font>) <br />
  <a href="https://arxiv.org/abs/2111.11418#:~:text=Based%20on%20the%20extensive%20experiments,on%20the%20token%20mixer%20modules.">[arXiv]</a>
  <a href="https://github.com/sail-sg/poolformer">[Code]</a>
  <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/poolformer?style=social" alt="GitHub stars for sail-sg/poolformer">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=poolformer&type=star&count=true" > -->
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2021" aria-labelledby="publications-2021">
<h4 id="publications-2021" class="publication-year" data-year="2021">
<a name="2021"></a> 2021
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2021-a-hybrid-stochastic-deterministic-minibatch-proximal-gradient-method-for-efficient-optimization-and-generalization" class="publication-item" data-year="2021" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>A Hybrid Stochastic-Deterministic Minibatch Proximal Gradient Method for Efficient Optimization and  Generalization</strong><br />
<strong>Pan Zhou</strong>, XiaoTong Yuan, Zhouchen Lin, and Steven Hoi<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2021<br />
<a href="../assets/pdf/2021-TPAMI-HSDN.pdf">[PDF]</a>
<a href="../assets/pdf/2021-TPAMI-HSDN-supp.pdf">[SUPP]</a>
<a href="../assets/bibtex/2021-PAMI-HSDN-bib.txt">[Bibtex]</a>
</p>
</li>

<!-- Item: 1 -->
<li id="pub-2021-efficient-gradient-support-pursuit-with-less-hard-thresholding-for-cardinality-constrained-learning" class="publication-item" data-year="2021" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Efficient Gradient Support Pursuit with Less Hard Thresholding for Cardinality-Constrained Learning</strong><br />
Fanhua Shang, Bingkun Wei, Hongying Liu, Yuanyuan Liu, <strong>Pan Zhou</strong>, and Maoguo Gong <br /> 
IEEE Transactions on Neural Networks and Learning Systems (<strong>TNNLS</strong>), 2021 <br />
<a href="https://ink.library.smu.edu.sg/sis_research/9049/">[Publication record]</a>
</p>
</li>
 


<!-- Item: 1 -->
<li id="pub-2021-a-theory-driven-self-labeling-refinement-method-for-contrastive-representation-learning" class="publication-item" data-year="2021" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, self-supervised learning"><p>
<strong>A Theory-Driven Self-Labeling Refinement Method for Contrastive Representation Learning</strong><br />
<strong>Pan Zhou</strong>, Caiming Xiong, Xiaotong Yuan, Steven Hoi<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2021 (<font color="#FF0000"><strong>spotlight</strong></font>) <br />
<a href="../assets/pdf/2021-NIPS-SLR.pdf">[PDF]</a>
<a href="../assets/pdf/2021-NIPS-SLR-supp.pdf">[SUPP]</a>
<a href="https://arxiv.org/abs/2106.14749">[arXiv]</a>
<a href="../assets/bibtex/2021-NIPS-SLR-bib.txt">[Bibtex]</a>
<a href="https://openreview.net/forum?id=P84bifNCpFQ&referrer=%5BAuthor%20Console%5D">[Code]</a>
<a href="../assets/pdf/2021-NIPS-SLR-Slide.pdf">[Slides]</a>
<a href="../assets/pdf/2021-NIPS-SLR-poster.pdf">[Poster]</a>
</p>
</li>
 


<!-- Item: 1 -->
<li id="pub-2021-towards-understanding-why-lookahead-generalizes-better-than-sgd-and-beyond" class="publication-item" data-year="2021" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Towards Understanding Why Lookahead Generalizes Better Than SGD and Beyond</strong><br />
<strong>Pan Zhou</strong>, Hanshu Yan, Xiaotong Yuan, Jiashi Feng, Shuicheng Yan<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2021 <br />
<a href="../assets/pdf/2021-NIPS-LA.pdf">[PDF]</a>
<a href="../assets/pdf/2021-NIPS-LA-supp.pdf">[SUPP]</a>
<a href="../assets/bibtex/2021-NIPS-LA-bib.txt">[Bibtex]</a>
<a href="https://github.com/sail-sg/SLRLA-optimizer">[Code]</a>
<a href="../assets/pdf/2021-NIPS-LA-Slide.pdf">[Slides]</a>
<a href="../assets/pdf/2021-NIPS-LA-poster.pdf">[Poster]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/sail-sg/SLRLA-optimizer?style=social" alt="GitHub stars for sail-sg/SLRLA-optimizer">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=SLRLA-optimizer&type=star&count=true" > -->
 


 

<!-- Item: 1 -->
<li id="pub-2021-task-similarity-aware-meta-learning-theory-inspired-improvement-on-maml" class="publication-item" data-year="2021" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, few-shot and meta-learning"><p>
<strong>Task Similarity Aware Meta Learning: Theory-inspired Improvement on MAML</strong><br />
<strong>Pan Zhou</strong>, Yingtian Zou, XiaoTong Yuan, Jiashi Feng, Caiming Xiong, and Steven Hoi<br /> 
International Conference on Uncertainty in Artificial Intelligence  (<strong>UAI</strong>), 2021 (NeurIPS'20 Meta Learning Workshop Paper) <br />
<a href="https://meta-learn.github.io/2020/papers/69_paper.pdf">[PDF]</a>
<a href="https://meta-learn.github.io/2020/papers/69_supplementary.pdf">[SUPP]</a>
<a href="https://github.com/Carbonaraa/TSA-MAML">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/Carbonaraa/TSA-MAML?style=social" alt="GitHub stars for Carbonaraa/TSA-MAML">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=Carbonaraa&repo=TSA-MAML&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2021-wav-bert-cooperative-acoustic-and-linguistic-representation-learning-for-low-resource-speech-recognition" class="publication-item" data-year="2021" data-research-line="learning-frameworks" data-subtopic="multimodal-learning-agent" data-keywords="multimodal learning, cross-modal alignment, agent reasoning, vision language and speech"><p>
<strong>Wav-BERT: Cooperative Acoustic and Linguistic Representation Learning for Low-Resource Speech Recognition</strong><br />
Guolin Zheng, Yubei Xiao, Ke Gong, <strong>Pan Zhou</strong>, Xiaodan Liang, and Liang Lin<br /> 
Conference on Empirical Methods in Natural Language Processing  (<strong>EMNLP</strong>), 2021 (Findings) <br />
<a href="https://arxiv.org/pdf/2109.09161.pdf">[arXiv]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li id="pub-2021-how-important-is-the-train-validation-split-in-meta-learning" class="publication-item" data-year="2021" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, few-shot and meta-learning"><p>
<strong>How Important is the Train-Validation Split in Meta-Learning?</strong><br />
Yu Bai, Minshuo Chen, <strong>Pan Zhou</strong>, Tuo Zhao, Jason D. Lee, Sham Kakade, Huan Wang, Caiming Xiong<br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2021 <br />
<a href="https://arxiv.org/pdf/2010.05843.pdf">[arXiv]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li id="pub-2021-prototypical-contrastive-learning-of-unsupervised-representations" class="publication-item" data-year="2021" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, self-supervised learning"><p>
<strong>Prototypical Contrastive Learning of Unsupervised Representations</strong><br />
Junnan Li, <strong>Pan Zhou</strong>, Caiming Xiong, and Steven Hoi<br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2021 <br />
<a href="https://openreview.net/pdf?id=KmykpuSrjcq">[OpenReview]</a>
<a href="../assets/bibtex/2021-ICLR-SSL.txt">[Bibtex]</a>
<a href="https://www.salesforce.com/blog/prototypical-contrastive-learning-pushing-the-frontiers-of-unsupervised-learning/">[Blog]</a>
<a href="https://github.com/salesforce/PCL">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/salesforce/PCL?style=social" alt="GitHub stars for salesforce/PCL">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PCL&type=star&count=true" > -->
 
<!-- Item: 1 -->
<li id="pub-2021-graph-evolving-meta-learning-for-low-resource-medical-dialogue-generation" class="publication-item" data-year="2021" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, few-shot and meta-learning"><p>
<strong>Graph-Evolving Meta-Learning for Low-Resource Medical Dialogue Generation</strong><br />
Shuai Lin, <strong>Pan Zhou</strong>, Xiaodan Liang, Jianheng Tang, Ruihui Zhao, Ziliang Chen and Liang Lin <br /> 
Association for the Advancement of Artificial Intelligence (<strong>AAAI</strong>), 2021 <br />
<a href="https://arxiv.org/pdf/2012.11988.pdf">[arXiv]</a>
<a href="../assets/bibtex/2021-AAAI-Medical.txt">[Bibtex]</a>
<a href="https://github.com/ha-lins/GEML-MDG">[Code]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/ha-lins/GEML-MDG?style=social" alt="GitHub stars for ha-lins/GEML-MDG">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=ha-lins&repo=GEML-MDG&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2021-adversarial-meta-sampling-for-multilingual-low-resource-speech-recognition" class="publication-item" data-year="2021" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, vision language and speech, few-shot and meta-learning"><p>
<strong>Adversarial Meta Sampling for Multilingual Low-Resource Speech Recognition</strong><br />
Yubei Xiao, Ke Gong, <strong>Pan Zhou</strong>, Guolin Zheng, Xiaodan Liang and Liang Lin <br /> 
Association for the Advancement of Artificial Intelligence (<strong>AAAI</strong>), 2021 <br />
<a href="https://arxiv.org/pdf/2012.11896.pdf">[arXiv]</a>
<a href="../assets/bibtex/2021-AAAI-ASR.txt">[Bibtex]</a>
<!-- <a href="https://github.com/iamxiaoyubei/AMS">[Code]</a> -->
<!-- <img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/iamxiaoyubei/AMS?style=social" alt="GitHub stars for iamxiaoyubei/AMS"> -->
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=iamxiaoyubei&repo=AMS&type=star&count=true" > -->
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2020" aria-labelledby="publications-2020">
<h4 id="publications-2020" class="publication-year" data-year="2020">
<a name="2020"></a> 2020
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2020-theory-inspired-path-regularized-differential-network-architecture-search" class="publication-item" data-year="2020" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design"><p>
<strong>Theory-Inspired Path-Regularized Differential Network Architecture Search</strong><br />
<strong>Pan Zhou</strong>, Caiming Xiong, Richard Socher, and Steven Hoi<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2020 (<font color="#FF0000"><strong>oral</strong></font>) <br />
<a href="../assets/pdf/2020_NAS.pdf">[PDF]</a>
<a href="../assets/pdf/2020_NAS_supp.pdf">[SUPP]</a>
<a href="https://arxiv.org/pdf/2006.16537.pdf">[arXiv]</a>
<a href="../assets/bibtex/2020_NAS_bib.txt">[Bibtex]</a>
<a href="https://www.salesforce.com/blog/theory-inspired-network-architecture-search/">[Blog]</a>
<a href="https://github.com/salesforce/PR-DARTS">[Code]</a>
<a href="../assets/pdf/2020-NIPS-NAS-slides.pdf">[Slides]</a>
<a href="../assets/pdf/2020-NIPS-NAS-poster.pdf">[Poster]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/salesforce/PR-DARTS?style=social" alt="GitHub stars for salesforce/PR-DARTS">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PR-DARTS&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2020-towards-theoretically-understanding-why-sgd-generalizes-better-than-adam-in-deep-learning" class="publication-item" data-year="2020" data-research-line="efficiency-optimization" data-subtopic="optimization-theory" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Towards Theoretically Understanding Why SGD Generalizes Better Than ADAM in Deep Learning</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng, Chao Ma, Caiming Xiong, Steven Hoi, and Weinan E<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2020<br />
<a href="../assets/pdf/2020_generalization.pdf">[PDF]</a>
<a href="../assets/pdf/2020_generalization_supp.pdf">[SUPP]</a>
<a href="https://arxiv.org/pdf/2010.05627.pdf">[arXiv]</a>
<a href="../assets/bibtex/2020_generalization_bib.txt">[Bibtex]</a>
<a href="https://github.com/salesforce/comparison_SGD_ADAM">[Code]</a>
<a href="../assets/pdf/2020-NIPS-SGD-slides.pdf">[Slides]</a>
<a href="../assets/pdf/2020-NIPS-SGD-poster.pdf">[Poster]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/salesforce/comparison_SGD_ADAM?style=social" alt="GitHub stars for salesforce/comparison_SGD_ADAM">
</p>
</li>
<!-- %src="https://ghbtns.com/github-btn.html?user=salesforce&repo=comparison_SGD_ADAM&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2020-improving-gan-training-with-probability-ratio-clipping-and-sample-reweighting" class="publication-item" data-year="2020" data-research-line="learning-frameworks" data-subtopic="generative-learning" data-keywords="generative learning, content generation, generative model"><p>
<strong>Improving GAN Training with Probability Ratio Clipping and Sample Reweighting</strong><br />
Yue Wu, <strong>Pan Zhou</strong>, Andrew Gordon Wilson, Eric Xing, and Zhiting Hu<br /> 
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2020<br />
<a href="../assets/pdf/2020_GAN.pdf">[PDF]</a>
<a href="https://arxiv.org/pdf/2006.06900.pdf">[arXiv]</a>
<a href="../assets/bibtex/2020_GAN_bib.txt">[Bibtex]</a>
<a href="https://github.com/Holmeswww/PPOGAN">[Codes]</a>
<img style="margin-left: 2px; margin-bottom:-5px;" width="91" height="20" loading="lazy" src="https://img.shields.io/github/stars/Holmeswww/PPOGAN?style=social" alt="GitHub stars for Holmeswww/PPOGAN">
</p>
</li>
<!-- src="https://ghbtns.com/github-btn.html?user=Holmeswww&repo=PPOGAN&type=star&count=true" > -->
 

<!-- Item: 1 -->
<li id="pub-2020-hybrid-stochastic-deterministic-minibatch-proximal-gradient-less-than-single-pass-optimization-with-nearly-optimal-generalization" class="publication-item" data-year="2020" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Hybrid Stochastic-Deterministic Minibatch Proximal Gradient: Less-Than-Single-Pass Optimization with Nearly Optimal Generalization</strong><br />
<strong>Pan Zhou</strong> and Xiaotong Yuan<br /> 
International Conference on Machine Learning (<strong>ICML</strong>), 2020 <br />
<a href="../assets/pdf/2020_hybrid_proximal_minibatch.pdf">[PDF]</a>
<a href="https://arxiv.org/pdf/2009.09835.pdf">[arXiv]</a>
<a href="../assets/bibtex/2020_optimization_bib.txt">[Bibtex]</a>
</p>
</li>
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2019" aria-labelledby="publications-2019">
<h4 id="publications-2019" class="publication-year" data-year="2019">
<a name="2019"></a> 2019
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2019-tensor-low-rank-representation-for-data-recovery-and-clustering" class="publication-item" data-year="2019" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, low-rank representation"><p>
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
<li id="pub-2019-faster-first-order-methods-for-stochastic-non-convex-optimization-on-riemannian-manifolds" class="publication-item" data-year="2019" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Faster First-Order Methods for Stochastic Non-Convex Optimization on Riemannian Manifolds</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Shuicheng Yan, Jiashi Feng<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2019 <br />
<a href="https://ieeexplore.ieee.org/document/8792163">[PDF]</a>
<a href="../assets/bibtex/2019-PAMI-RSPIDER.txt">[Bibtex]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li id="pub-2019-efficient-meta-learning-via-minibatch-proximal-update" class="publication-item" data-year="2019" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, few-shot and meta-learning"><p>
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
<li id="pub-2019-generalized-majorization-minimization-for-non-convex-optimization" class="publication-item" data-year="2019" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Generalized Majorization-Minimization for Non-Convex Optimization</strong><br />
Hu Zhang, <strong>Pan Zhou</strong>, Yi Yang, Jiashi Feng<br />
International Joint Conference on Artificial Intelligence (<strong>IJCAI</strong>), 2019 <br />
<a href="https://www.ijcai.org/proceedings/2019/0591.pdf">[PDF]</a>
<a href="../assets/bibtex/2019-IJCAI-MM.txt">[Bibtex]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li id="pub-2019-faster-first-order-methods-for-stochastic-non-convex-optimization-on-riemannian-manifolds-2" class="publication-item" data-year="2019" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Faster First-Order Methods for Stochastic Non-Convex Optimization on Riemannian Manifolds</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Jiashi Feng<br />
International Conference on Artificial Intelligence and Statistics (<strong>AISTATS</strong>), 2019 <br />
<a href="https://arxiv.org/pdf/1811.08109.pdf">[PDF]</a>
<a href="../assets/bibtex/2019-AISTATIC-RSPIDER.txt">[Bibtex]</a>
</p>
</li>


<!-- Item: 1 -->
<li id="pub-2019-task-relation-networks" class="publication-item" data-year="2019" data-research-line="architecture-design" data-keywords="architecture design, vision architecture, network design"><p>
<strong>Task Relation Networks</strong><br />
Jianshu Li, <strong>Pan Zhou</strong>, Yunpeng Chen, Jian Zhao, Sujoy Roy, Yan Shuicheng, Jiashi Feng, and Terence Sim<br />
IEEE Winter Conference on Applications of Computer Vision (<strong>WACV</strong>), 2019 <br />
<a href="https://ieeexplore.ieee.org/document/8658407">[PDF]</a>
</p>
</li>
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2018" aria-labelledby="publications-2018">
<h4 id="publications-2018" class="publication-year" data-year="2018">
<a name="2018"></a> 2018
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2018-efficient-stochastic-gradient-hard-thresholding" class="publication-item" data-year="2018" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Efficient Stochastic Gradient Hard Thresholding</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Jiashi Feng<br />
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2018 <br />
<a href="http://papers.nips.cc/paper/7469-efficient-stochastic-gradient-hard-thresholding">[PDF]</a>
<a href="../assets/bibtex/2018-NIPS-hardthresholding.txt">[Bibtex]</a>
<a href="../assets/code/HSGHTcode.rar">[Codes]</a>
</p>
</li>
 


<!-- Item: 1 -->
<li id="pub-2018-new-insight-into-hybrid-stochastic-gradient-descent-beyond-with-replacement-sampling-and-convexity" class="publication-item" data-year="2018" data-research-line="efficiency-optimization" data-subtopic="efficient-training" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>New Insight into Hybrid Stochastic Gradient Descent:
Beyond With-Replacement Sampling and Convexity</strong><br />
<strong>Pan Zhou</strong>, Xiaotong Yuan, Jiashi Feng<br />
Neural Information Processing Systems (<strong>NeurIPS</strong>), 2018 <br />
<a href="http://papers.nips.cc/paper/7399-new-insight-into-hybrid-stochastic-gradient-descent-beyond-with-replacement-sampling-and-convexity">[PDF]</a>
<a href="../assets/bibtex/2018-NIPS-withreplacement.txt">[Bibtex]</a>
</p>
</li>

 


<!-- Item: 1 -->
<li id="pub-2018-understanding-generalization-and-optimization-performance-of-deep-cnns" class="publication-item" data-year="2018" data-research-line="efficiency-optimization" data-subtopic="optimization-theory" data-keywords="optimization theory, convergence analysis, generalization theory, deep optimization"><p>
<strong>Understanding Generalization and Optimization Performance of Deep CNNs</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng<br />
International Conference on Machine Learning (<strong>ICML</strong>), 2018 <br />
<a href="../assets/pdf/2018-ICML-deepCNNs.pdf">[PDF]</a>
<a href="https://arxiv.org/abs/1805.10767">[arXiv]</a>
<a href="../assets/bibtex/2018-ICML-AnalysisCNN.txt">[Bibtex]</a>
</p>
</li>
 

<!-- Item: 1 -->
<li id="pub-2018-deep-adversarial-subspace-clustering" class="publication-item" data-year="2018" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, low-rank representation"><p>
<strong>Deep Adversarial Subspace Clustering</strong><br />
<strong>Pan Zhou</strong>, Yunqing Hou, Jiashi Feng<br />
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2018 <br />
<a href="../assets/pdf/2018-CVPR-DSCN.pdf">[PDF]</a>
<a href="../assets/code/dsc_code.zip">[Codes]</a>
<a href="../assets/bibtex/2018-CVPR-DSCN.txt">[Bibtex]</a>
</p>
</li>
 


<!-- Item: 1 -->
<li id="pub-2018-empirical-risk-landscape-analysis-for-understanding-deep-neural-networks" class="publication-item" data-year="2018" data-research-line="efficiency-optimization" data-subtopic="optimization-theory" data-keywords="optimization theory, convergence analysis, generalization theory"><p>
<strong>Empirical Risk Landscape Analysis for Understanding Deep Neural Networks</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng<br />
International Conference on Learning Representations (<strong>ICLR</strong>), 2018 <br />
<a href="../assets/pdf/2018-ICLR-AnalysisDNN.pdf">[PDF]</a>
<a href="https://arxiv.org/abs/1705.07038">[arXiv]</a>
<a href="../assets/bibtex/2018-ICLR-AnalysisDNN.txt">[Bibtex]</a>
</p>
</li>
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2017" aria-labelledby="publications-2017">
<h4 id="publications-2017" class="publication-year" data-year="2017">
<a name="2017"></a> 2017
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2017-tensor-factorization-for-low-rank-tensor-completion" class="publication-item" data-year="2017" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, low-rank representation"><p>
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
<li id="pub-2017-dictionary-learning-with-structured-noise" class="publication-item" data-year="2017" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, low-rank representation"><p>
<strong>Dictionary Learning with Structured Noise</strong><br />
<strong>Pan Zhou</strong>, Cong Fang, Zhouchen Lin, Chao Zhang, Edward Y. Chang<br />
Neurocomputing, 2017 <br />
<a href="../assets/pdf/2017-NEUCOM-DLSN.pdf">[PDF]</a>
<a href="../assets/bibtex/2017-NEUCOM-DLSN.txt">[Bibtex]</a>
</p>
</li>



<!-- Item: 1 -->
<li id="pub-2017-feature-learning-via-partial-differential-equation-with-applications-to-face-recognition" class="publication-item" data-year="2017" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework"><p>
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
<li id="pub-2017-outlier-robust-tensor-pca" class="publication-item" data-year="2017" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, low-rank representation"><p>
<strong>Outlier-Robust Tensor PCA</strong><br />
<strong>Pan Zhou</strong>, Jiashi Feng<br />
IEEE Conference on Computer Vision and Pattern Recognition (<strong>CVPR</strong>), 2017 <br />
<a href="../assets/pdf/2017-CVPR-RTPCA.pdf">[PDF]</a>
<a href="../assets/pdf/2017-CVPR-RTPCA-supp.pdf">[SUPP]</a>
<a href="../assets/code/OR_TPCA_code.rar">[Codes]</a>
<a href="../assets/bibtex/2017-CVPR-TRPCA.txt">[Bibtex]</a>
</p>
</li>
</ol>
</section>

<section class="publication-year-group" data-publication-year-group data-year="2016" aria-labelledby="publications-2016">
<h4 id="publications-2016" class="publication-year" data-year="2016">
<a name="2016"></a> 2016
</h4>
<ol class="biblist">
<!-- Item: 1 -->
<li id="pub-2016-bilevel-model-based-discriminative-dictionary-learning-for-recognition" class="publication-item" data-year="2016" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, low-rank representation"><p>
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
<li id="pub-2016-integrated-low-rank-based-discriminative-feature-learning-for-recognition" class="publication-item" data-year="2016" data-research-line="learning-frameworks" data-subtopic="representation-generalization" data-keywords="representation learning, generalization, learning framework, low-rank representation"><p>
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
</section>
</div>
</section>

 <br>

##### **Books and Patents**
<ol class="biblist"> 
<!-- Item: 1 -->
<li ><p>
<strong>Tensors for Data Processing</strong><br> 
Chapter 6 is contributed by <strong>Pan Zhou</strong>, Canyi Lu, Zhouchen Lin  <br /> 
Elsevier, 2022.   
<a href="https://doi.org/10.1016/B978-0-12-824447-0.00012-1">[Publication record]</a>
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
