---
layout: page
permalink: /publication/
title: Publication
description: 
nav: true
nav_order: 2
---



You can also browse my <a href="https://scholar.google.com/citations?user=0b7ZqlcAAAAJ&hl=en" target="_blank" style="text-decoration:underline;">Google Scholar profile</a>.  <strong><sup>*</sup></strong> denotes equal contribution; <strong><sup>+</sup></strong> denotes corresponding author.

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


### Manuscripts
<!-- Generated from JabRef by PubList by Truong Nghiem at 09:00 on 2015.11.04. -->

<!-- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/masked-diffusion-transformer-is-a-strong/image-generation-on-imagenet-256x256)](https://paperswithcode.com/sota/image-generation-on-imagenet-256x256?p=masked-diffusion-transformer-is-a-strong)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mugs-a-multi-granular-self-supervised/self-supervised-image-classification-on)](https://paperswithcode.com/sota/self-supervised-image-classification-on?p=mugs-a-multi-granular-self-supervised) -->

<!-- [![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/masked-diffusion-transformer-is-a-strong/image-generation-on-imagenet-256x256)](https://paperswithcode.com/sota/image-generation-on-imagenet-256x256?p=masked-diffusion-transformer-is-a-strong)

[![HuggingFace space](https://img.shields.io/badge/🤗-HuggingFace%20Space-cyan.svg)](https://huggingface.co/spaces/shgao/MDT) -->

<ol class="biblist">
<!-- Item: 1 -->
<li ><p>
<strong>Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models</strong><br />
Xingyu Xie<strong><sup>*</sup></strong>, <strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Huan Li, Zhouchen Lin, Shuicheng Yan <br />
<strong><font color="#FF0000">SoTA optimizer</font> on ResNet, ConvNext, ViT, Swin, MAE, LSTM, Transformer-XL, BERT, GPT2, Dreamffusion, PPO in RL  etc</strong> <br />
<a href="https://arxiv.org/abs/2208.06677">[PDF]</a>
<a href="https://github.com/sail-sg/Adan">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Adan&type=star&count=true" >
</iframe>
</p>
<!-- <div id="bib_lu2020tensor" class="bibtex noshow">
<pre>
@article{Adan,
  author = {Xingyu Xie<span>&#42;</span>, <strong>Pan Zhou</strong><span>&#42;</span>, Huan Li, Zhouchen Lin, Shuicheng Yan},
  title = {Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence (<b>TPAMI</b>)},
  year = {2024}
}
</pre></div> -->
</li>
 
 
</ol>




### Journal and Conference Publications
<ol class="biblist">


<h4>
<a name='2024'></a> 2024
</h4>

<!-- Item: 1 -->
<li ><p>
<strong>Win: Weight-Decay-Integrated Nesterov Acceleration for  Faster Network Training</strong><br>
<strong>Pan Zhou</strong>, Xingyu Xie, Zhouchen Lin, Kim-Chuan Toh, Shuicheng Yan  <br /> 
Journal of Machine Learning Research (<strong>JMLR</strong>), 2024<br />
<!-- <a href="../assets/pdf/2024-JMLR-win.pdf">[PDF]</a> -->
<a href="https://github.com/sail-sg/win">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" >
</iframe>
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
    src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ptp&type=star&count=true" >
</iframe>,
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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=CLoT&type=star&count=true" >
</iframe>
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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=inceptionnext&type=star&count=true" >
</iframe>
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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=Consistent3D&type=star&count=true" >
</iframe>
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
      src="https://ghbtns.com/github-btn.html?user=nblt&repo=F-SAM&type=star&count=true" >
</iframe>
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
      src="https://ghbtns.com/github-btn.html?user=yue-zhongqi&repo=tif&type=star&count=true" >
</iframe>
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
      src="https://ghbtns.com/github-btn.html?user=yxymessi&repo=DTC123&type=star&count=true" >
</iframe>
</p>
</li>



<h4>
<a name='2023'></a> 2023
</h4>

<!-- Item: 1 -->
<li ><p>
<strong>MetaFormer Baselines for Vision</strong><br />
Weihao Yu, Chenyang Si, <strong>Pan Zhou</strong>, Mi Luo, Yichen Zhou, Jiashi Feng,
Shuicheng Yan, and Xinchao Wang<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2023<br />
<a href="https://arxiv.org/abs/2210.13452">[Axriv]</a>
<a href="https://github.com/sail-sg/metaformer">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=metaformer&type=star&count=true" >
</iframe>,  <iframe
        style="margin-left: 2px; margin-bottom:-5px;"
        frameborder="0" scrolling="0" width="700px" height="20px"
        src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/metaformer-baselines-for-vision/domain-generalization-on-imagenet-c" >
    </iframe>
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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ScaleLong&type=star&count=true" >
</iframe>
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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=MDT&type=star&count=true" >
</iframe>
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
Shanghua Gao, <strong>Pan Zhou<sup>+</sup></strong>, Ming-Ming Cheng, Shuicheng Yan<br /> 
ACM International Conference on Multimedia (<strong>ACMMM</strong>), 2023<br />
<a href="https://dl.acm.org/doi/10.1145/3581783.3612680">[PDF]</a>
<a href="https://github.com/sail-sg/EditAnything">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=EditAnything&type=star&count=true" >
</iframe>
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
<strong>Contrastive Video Question Answering via Video Graph Transformer</strong><br />
Junbin Xiao, <strong>Pan Zhou</strong>, Angela Yao, Yicong Li, Richang Hong, Shuicheng Yan, Tat-Seng Chua<br /> 
IEEE Transactions on Pattern Analysis and Machine Intelligence (<strong>TPAMI</strong>), 2023<br />
<a href="https://arxiv.org/abs/2302.13668">[PDF]</a>
<a href="https://github.com/doc-doc/CoVGT">[Code]</a> 
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=doc-doc&repo=CoVGT&type=star&count=true" >
</iframe>
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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=ptp&type=star&count=true" >
</iframe>,
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/position-guided-text-prompt-for-vision/zero-shot-cross-modal-retrieval-on-coco-2014" >
</iframe>
</p>
</li>
 

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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=win&type=star&count=true" >
</iframe>
</p>
</li>
 

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
      src="https://ghbtns.com/github-btn.html?user=DongSky&repo=LPT&type=star&count=true" >
</iframe>,
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/lpt-long-tailed-prompt-tuning-for-image/long-tail-learning-on-cifar-100-lt-r-100" >
</iframe>
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




<h4>
	<a name='2022'></a> 2022
</h4>



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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=iFormer&type=star&count=true" >
</iframe>
</p>
</li>
 
<li ><p>
<strong>Mugs: A Multi-Granular Self-Supervised Learning Framework</strong><br />
<strong>Pan Zhou</strong><strong><sup>*</sup></strong>, Yichen Zhou<strong><sup>*</sup></strong>, Chenyang Si<strong><sup>*</sup></strong>,  Weihao Yu, Teck Khim Ng, Shuicheng Yan<br />
<strong> Workshop of Neural Information Processing Systems, 2022. (<font color="#FF0000">SoTA SSL performance on ImageNet without extra data</font> under linear probing and KNN evaluation settings </strong>) <br />
<a href="https://arxiv.org/abs/2203.14415">[PDF]</a>
<a href="https://github.com/sail-sg/mugs">[Code]</a>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="91px" height="20px"
    src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=mugs&type=star&count=true" >
</iframe>
<iframe
    style="margin-left: 2px; margin-bottom:-5px;"
    frameborder="0" scrolling="0" width="400px" height="20px"
    src="https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mugs-a-multi-granular-self-supervised/self-supervised-image-classification-on" >
</iframe>
</p>
</li>


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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=dualformer&type=star&count=true" >
</iframe>
</p>
</li>
 

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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=VGT&type=star&count=true" >
</iframe>
</p>
</li>
 

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
      src="https://ghbtns.com/github-btn.html?user=DongSky&repo=few-shot-vit&type=star&count=true" >
</iframe>
</p>
</li>
 

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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=poolformer&type=star&count=true" >
</iframe>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Prototypical Graph Contrastive Learning</strong><br />
Lin Shuai, Liu Chen, <strong>Pan Zhou</strong>, Hu Zi-yuan, Wang Shuojia, Zhao Ruihui, Zheng Yefeng, Lin Liang, Xing Eric, Liang Xiaodan<br /> 
IEEE Transactions on Neural Networks and Learning Systems (<strong>TNNLS</strong>), 2022 <br />
<a href="https://arxiv.org/abs/2106.09645">[Axriv]</a>
<a href="https://github.com/ha-lins/PGCL">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=ha-lins&repo=PGCL&type=star&count=true" >
</iframe>
</p>
</li>
 

 
<h4>
	<a name='2021'></a> 2021
</h4>


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
      src="https://ghbtns.com/github-btn.html?user=sail-sg&repo=SLRLA-optimizer&type=star&count=true" >
</iframe>
</p>
</li>
 

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
<strong>Prototypical Graph Contrastive Learning</strong><br />
<strong>Task Similarity Aware Meta Learning: Theory-inspired Improvement on MAML</strong><br />
<strong>Pan Zhou</strong>, Yingtian Zou, XiaoTong Yuan, Jiashi Feng, Caiming Xiong, and Steven Hoi<br /> 
International Conference on Uncertainty in Artificial Intelligence  (<strong>UAI</strong>), 2021 (NeurIPS'20 Meta Learning Workshop Paper) <br />
<a href="https://meta-learn.github.io/2020/papers/69_paper.pdf">[PDF]</a>
<a href="https://meta-learn.github.io/2020/papers/69_supplementary.pdf">[SUPP]</a>
<a href="https://github.com/Carbonaraa/TSA-MAML">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=Carbonaraa&repo=TSA-MAML&type=star&count=true" >
</iframe>
</p>
</li>
 

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
Junnan Li, <strong>Pan Zhou</strong>, Caiming Xiong, Richard Socher, and Steven Hoi<br /> 
International Conference on Learning Representations (<strong>ICLR</strong>), 2021 <br />
<a href="https://openreview.net/pdf?id=KmykpuSrjcq">[Axriv]</a>
<a href="../assets/bibtex/2021-ICLR-SSL.txt">[Bibtex]</a>
<a href="https://blog.einstein.ai/prototypical-contrastive-learning-pushing-the-frontiers-of-unsupervised-learning/">[Blog]</a>
<a href="https://github.com/salesforce/PCL">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PCL&type=star&count=true" >
</iframe>
</p>
</li>
 
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
      src="https://ghbtns.com/github-btn.html?user=ha-lins&repo=GEML-MDG&type=star&count=true" >
</iframe>
</p>
</li>
 

<!-- Item: 1 -->
<li ><p>
<strong>Adversarial Meta Sampling for Multilingual Low-Resource Speech Recognition</strong><br />
Yubei Xiao, Ke Gong, <strong>Pan Zhou</strong>, Guolin Zheng, Xiaodan Liang and Liang Lin <br /> 
Association for the Advancement of Artificial Intelligence (<strong>AAAI</strong>), 2021 <br />
<a href="https://arxiv.org/pdf/2012.11896.pdf">[Axriv]</a>
<a href="../assets/bibtex/2021-AAAI-ASR.txt">[Bibtex]</a>
<a href="https://github.com/iamxiaoyubei/AMS">[Code]</a>
<iframe
      style="margin-left: 2px; margin-bottom:-5px;"
      frameborder="0" scrolling="0" width="91px" height="20px"
      src="https://ghbtns.com/github-btn.html?user=iamxiaoyubei&repo=AMS&type=star&count=true" >
</iframe>
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
      src="https://ghbtns.com/github-btn.html?user=salesforce&repo=PR-DARTS&type=star&count=true" >
</iframe>
</p>
</li>
 

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
      src="https://ghbtns.com/github-btn.html?user=salesforce&repo=comparison_SGD_ADAM&type=star&count=true" >
</iframe>
</p>
</li>
 

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
      src="https://ghbtns.com/github-btn.html?user=Holmeswww&repo=PPOGAN&type=star&count=true" >
</iframe>
</p>
</li>
 

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
</p>
</li>

 <h4>
	<a name='2017'></a> 2017
</h4>

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