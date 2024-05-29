# 3D Gaussian Splatting Papers

## 📢 改版公告 / Update Notice

由于论文数量激增，页面变得过长。为方便查阅，我们计划从2024年6月开始对页面进行调整，届时新文章将按时间倒序排列，旧文章将进行[📁 归档]。

Due to the rapid increase in the number of papers, the page has become too long.
To improve accessibility, we plan to implement the following changes starting from June 2024:
new articles will be displayed in reverse chronological order, and older articles will be [📁 archived].

[![更新日志](https://img.shields.io/badge/💡-更新日志-informational.svg?style=flat)](Changelog.md)
[![发现错误](https://img.shields.io/badge/🐛-发现错误-yellow.svg?style=flat)](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/issues)
[![提交修改](https://img.shields.io/badge/👐-提交修改-brightgreen.svg?style=flat)](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/pulls)


**⚡ 快捷链接**: [[10](#10-lightgaussian-unbounded-3d-gaussian-compression-with-15x-reduction-and-200-fps)]
                 [[30](#30-gaufre-gaussian-deformation-fields-for-real-time-dynamic-novel-view-synthesis)]
                 [[50](#50-fast-dynamic-3d-object-generation-from-a-single-view-video)]
                 [[70](#70-ges-generalized-exponential-splatting-for-efficient-radiance-field-rendering)]
                 [[90](#90-gaussiangrasper-3d-language-gaussian-splatting-for-open-vocabulary-robotic-grasping)]
                 [[100](#100-compact-3d-gaussian-splatting-for-dense-visual-slam)]
                 [[120](#120-radsplat-radiance-field-informed-gaussian-splatting-for-robust-real-time-rendering-with-900-fps)]
                 [[140](#140-splatface-gaussian-splat-face-reconstruction-leveraging-an-optimizable-surface)]
                 [[160](#160-per-gaussian-embedding-based-deformation-for-deformable-3d-gaussian-splatting)]
                 [[180](#180-srgs-super-resolution-3d-gaussian-splatting)]
                 [[200](#200-bootstrap-3d-reconstructed-scenes-from-3d-gaussian-splatting)]
                 [[220](#220-gs-planner-a-gaussian-splatting-based-planning-framework-for-active-high-fidelity-reconstruction)]
                 [[240](#240-magicdrive3d-controllable-3d-generation-for-any-view-rendering-in-street-scenes)]
                 [[250](#250-sa-gs-semantic-aware-gaussian-splatting-for-large-scene-reconstruction-with-geometry-constrain)]（最新）





**📚 会议期刊**:
- [[ICLR2024](./ICLR2024.md)] (2 篇)
  [[3DV2024](./3DV2024.md)] (1 篇)
  [[CVPR2024](./CVPR2024.md)] (62 篇)
  [[WACV2024](./WACV2024.md)] (1 篇)
  [[ICML2024](./ICML2024.md)] (2 篇)
- [[SIGGRAPH2024](./SIGGRAPH2024.md)] (4 篇)
  [[IJCAI2024](./IJCAI2024.md)] (1 篇)
  [ECCV2024]

---

#### [S0] A Survey on 3D Gaussian Splatting
- **🧑‍🔬 作者**：Guikun Chen, Wenguan Wang
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2401.03890.md)] [[arXiv:2401.03890](https://arxiv.org/abs/2401.03890)]
- **📝 说明**：🔥 首篇综述

#### [S1] 3D Gaussian as a New Vision Era: A Survey
- **🧑‍🔬 作者**：Ben Fei, Jingyi Xu, Rui Zhang, Qingyuan Zhou, Weidong Yang, Ying He
- **🏫 单位**：Fudan University ⟐ Nanyang Technological University
- **🔗 链接**：[[中英摘要](./abs/2402.07181.md)] [[arXiv:2402.07181](https://arxiv.org/abs/2402.07181)]
- **📝 说明**：👍 相对比较全面，推荐精读

#### [S2] Recent Advances in 3D Gaussian Splatting
- **🧑‍🔬 作者**：Tong Wu, Yu-Jie Yuan, Ling-Xiao Zhang, Jie Yang, Yan-Pei Cao, Ling-Qi Yan, Lin Gao
- **🏫 单位**：Chinese Academy of Sciences ⟐ VAST ⟐  University of California
- **🔗 链接**：[[中英摘要](./abs/2403.11134.md)] [[arXiv:2403.11134](https://arxiv.org/abs/2403.11134)]
- **📝 说明**：🔥 第三篇综述，涵盖了更多最新进展

#### [S3] Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review
- **🧑‍🔬 作者**：Anurag Dalal, Daniel Hagen, Kjell G. Robbersmyr, Kristian Muri Knausgård
- **🏫 单位**：University of Agder
- **🔗 链接**：[[中英摘要](./abs/2405.03417.md)] [[arXiv:2405.03417](https://arxiv.org/abs/2405.03417)]
- **📝 说明**：🔥 第四篇综述

---

#### [0] 3D Gaussian Splatting for Real-Time Radiance Field Rendering
- **🧑‍🔬 作者**：Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
- **🏫 单位**：Université Côte d’Azurl ⟐ Max-Planck-Institut für Informatik
- **🔗 链接**：[[中英摘要](./abs/2308.04079.md)] [[arXiv:2308.04079](https://arxiv.org/abs/2308.04079)] [[ACM TOG](https://dl.acm.org/doi/10.1145/3592433)] [[Code](https://github.com/graphdeco-inria/gaussian-splatting)]
- **📝 说明**：🚀 开山之作，必读；🏆 SIGGRAPH 2023 Best Paper

#### [1] Flexible Techniques for Differentiable Rendering with 3D Gaussians
- **🧑‍🔬 作者**：Leonid Keselman, Martial Hebert
- **🏫 单位**：Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2308.14737.md)] [[arXiv:2308.14737](https://arxiv.org/abs/2308.14737)] [[Code](https://github.com/leonidk/fmb-plus)]
- **📝 说明**：✏️

#### [2] Drivable 3D Gaussian Avatars
- **🧑‍🔬 作者**：Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito, Michael Zollhöfer, Justus Thies, Javier Romero
- **🏫 单位**：Meta Reality Labs Research ⟐ Technical University of Darmstadt ⟐ Max Planck Institute for Intelligent Systems
- **🔗 链接**：[[中英摘要](./abs/2311.08581.md)] [[arXiv:2311.08581](https://arxiv.org/abs/2311.08581)] [Code]
- **📝 说明**：✏️

#### [3] SplatArmor: Articulated Gaussian splatting for animatable humans from monocular RGB videos
- **🧑‍🔬 作者**：Rohit Jena, Ganesh Subramanian Iyer, Siddharth Choudhary, Brandon Smith, Pratik Chaudhari, James Gee
- **🏫 单位**：University of Pennsylvania ⟐ Amazon.com, Inc.
- **🔗 链接**：[[中英摘要](./abs/2311.10812.md)] [[arXiv:2311.10812](https://arxiv.org/abs/2311.10812)] [[Code](https://github.com/rohitrango/splatarmor)]
- **📝 说明**：✏️

#### [4] GaussianDiffusion: 3D Gaussian Splatting for Denoising Diffusion Probabilistic Models with Structured Noise
- **🧑‍🔬 作者**：Xinhai Li, Huaibin Wang, Kuo-Kun Tseng
- **🏫 单位**：Harbin Institute of Technology (Shenzhen)
- **🔗 链接**：[[中英摘要](./abs/2311.11221.md)] [[arXiv:2311.11221](https://arxiv.org/abs/2311.11221)] [Code]
- **📝 说明**：✏️

#### [5] An Efficient 3D Gaussian Representation for Monocular/Multi-view Dynamic Scenes
- **🧑‍🔬 作者**：Kai Katsumata, Duc Minh Vo, Hideki Nakayama
- **🏫 单位**：The University of Tokyo
- **🔗 链接**：[[中英摘要](./abs/2311.12897.md)] [[arXiv:2311.12897](https://arxiv.org/abs/2311.12897)] [[Code](https://github.com/raven38/EfficientDynamic3DGaussian)]
- **📝 说明**：✏️

#### [6] LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes
- **🧑‍🔬 作者**：Jaeyoung Chung, Suyoung Lee, Hyeongjin Nam, Jaerin Lee, Kyoung Mu Lee
- **🏫 单位**：Seoul National University
- **🔗 链接**：[[中英摘要](./abs/2311.13384.md)] [[arXiv:2311.13384](https://arxiv.org/abs/2311.13384)] [[Code](https://github.com/luciddreamer-cvlab/LucidDreamer)]
- **📝 说明**：✏️

#### [7] Depth-Regularized Optimization for 3D Gaussian Splatting in Few-Shot Images
- **🧑‍🔬 作者**：Jaeyoung Chung, Jeongtaek Oh, Kyoung Mu Lee
- **🏫 单位**：Seoul National University
- **🔗 链接**：[[中英摘要](./abs/2311.13398.md)] [[arXiv:2311.13398](https://arxiv.org/abs/2311.13398)] [[Code](https://github.com/robot0321/DepthRegularizedGS)]
- **📝 说明**：Empty code repo

#### [8] Relightable 3D Gaussian: Real-time Point Cloud Relighting with BRDF Decomposition and Ray Tracing
- **🧑‍🔬 作者**：Jian Gao, Chun Gu, Youtian Lin, Hao Zhu, Xun Cao, Li Zhang, Yao Yao
- **🏫 单位**：Nanjing University ⟐ Fudan University
- **🔗 链接**：[[中英摘要](./abs/2311.16043.md)] [[arXiv:2311.16043](https://arxiv.org/abs/2311.16043)] [[Code](https://github.com/NJU-3DV/Relightable3DGaussian)]
- **📝 说明**：✏️

#### [9] Animatable 3D Gaussian: Fast and High-Quality Reconstruction of Multiple Human Avatars
- **🧑‍🔬 作者**：Yang Liu, Xiang Huang, Minghan Qin, Qinwei Lin, Haoqian Wang
- **🏫 单位**： Tsinghua University ⟐ Gala Sports
- **🔗 链接**：[[中英摘要](./abs/2311.16482.md)] [[arXiv:2311.16482](https://arxiv.org/abs/2311.16482)] [[Code](https://github.com/jimmyYliu/Animatable-3D-Gaussian)]
- **📝 说明**：✏️

#### [10] LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and 200+ FPS
- **🧑‍🔬 作者**：Zhiwen Fan, Kevin Wang, Kairun Wen, Zehao Zhu, Dejia Xu, Zhangyang Wang
- **🏫 单位**：University of Texas at Austin ⟐ Xiamen University
- **🔗 链接**：[[中英摘要](./abs/2311.17245.md)] [[arXiv:2311.17245](https://arxiv.org/abs/2311.17245)] [[Code](https://github.com/VITA-Group/LightGaussian)]
- **📝 说明**：✏️

#### [11] CG3D: Compositional Generation for Text-to-3D via Gaussian Splatting
- **🧑‍🔬 作者**：Alexander Vilesov, Pradyumna Chari, Achuta Kadambi
- **🏫 单位**：University of California, Los Angeles
- **🔗 链接**：[[中英摘要](./abs/2311.17907.md)] [[arXiv:2311.17907](https://arxiv.org/abs/2311.17907)] [Code]
- **📝 说明**：✏️

#### [12] Compact3D: Compressing Gaussian Splat Radiance Field Models with Vector Quantization
- **🧑‍🔬 作者**：KL Navaneet, Kossar Pourahmadi Meibodi, Soroush Abbasi Koohpayegani, Hamed Pirsiavash
- **🏫 单位**：University of California, Davis
- **🔗 链接**：[[中英摘要](./abs/2311.18159.md)] [[arXiv:2311.18159](https://arxiv.org/abs/2311.18159)] [[Code](https://github.com/UCDvision/compact3d)]
- **📝 说明**：✏️

#### [13] Periodic Vibration Gaussian: Dynamic Urban Scene Reconstruction and Real-time Rendering
- **🧑‍🔬 作者**：Yurui Chen, Chun Gu, Junzhe Jiang, Xiatian Zhu, Li Zhang
- **🏫 单位**：Fudan University ⟐ University of Surrey
- **🔗 链接**：[[中英摘要](./abs/2311.18561.md)] [[arXiv:2311.18561](https://arxiv.org/abs/2311.18561)] [[Code](https://github.com/fudan-zvg/PVG)]
- **📝 说明**：✏

#### [14] DynMF: Neural Motion Factorization for Real-time Dynamic View Synthesis with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Agelos Kratimenos, Jiahui Lei, Kostas Daniilidis
- **🏫 单位**：University of Pennsylvania
- **🔗 链接**：[[中英摘要](./abs/2312.00112.md)] [[arXiv:2312.00112](https://arxiv.org/abs/2312.00112)] [[Code](https://github.com/agelosk/dynmf)]
- **📝 说明**：✏️

#### [15] SparseGS: Real-Time 360° Sparse View Synthesis using Gaussian Splatting
- **🧑‍🔬 作者**：Haolin Xiong, Sairisheek Muttukuru, Rishi Upadhyay, Pradyumna Chari, Achuta Kadambi
- **🏫 单位**：University of California, Los Angeles
- **🔗 链接**：[[中英摘要](./abs/2312.00206.md)] [[arXiv:2312.00206](https://arxiv.org/abs/2312.00206)] [[Code](https://github.com/ForMyCat/SparseGS)]
- **📝 说明**：✏️

#### [16] FSGS: Real-Time Few-shot View Synthesis using Gaussian Splatting
- **🧑‍🔬 作者**：Zehao Zhu, Zhiwen Fan, Yifan Jiang, Zhangyang Wang
- **🏫 单位**：University of Texas at Austin
- **🔗 链接**：[[中英摘要](./abs/2312.00451.md)] [[arXiv:2312.00451](https://arxiv.org/abs/2312.00451)] [[Code](https://github.com/VITA-Group/FSGS)]
- **📝 说明**：✏️

#### [17] MD-Splatting: Learning Metric Deformation from 4D Gaussians in Highly Deformable Scenes
- **🧑‍🔬 作者**：Bardienus P. Duisterhof, Zhao Mandi, Yunchao Yao, Jia-Wei Liu, Mike Zheng Shou, Shuran Song, Jeffrey Ichnowski
- **🏫 单位**：National University of Singapore ⟐ Stanford University ⟐ Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2312.00583.md)] [[arXiv:2312.00583](https://arxiv.org/abs/2312.00583)] [[Code](https://github.com/momentum-robotics-lab/md-splatting)]
- **📝 说明**：✏️

#### [18] Gaussian Grouping: Segment and Edit Anything in 3D Scenes
- **🧑‍🔬 作者**：Mingqiao Ye, Martin Danelljan, Fisher Yu, Lei Ke
- **🏫 单位**：ETH Zurich
- **🔗 链接**：[[中英摘要](./abs/2312.00732.md)] [[arXiv:2312.00732](https://arxiv.org/abs/2312.00732)] [[Code](https://github.com/lkeab/gaussian-grouping)]
- **📝 说明**：✏️

#### [19] NeuSG: Neural Implicit Surface Reconstruction with 3D Gaussian Splatting Guidance
- **🧑‍🔬 作者**：Hanlin Chen, Chen Li, Gim Hee Lee
- **🏫 单位**：National University of Singapore
- **🔗 链接**：[[中英摘要](./abs/2312.00846.md)] [[arXiv:2312.00846](https://arxiv.org/abs/2312.00846)] [Code]
- **📝 说明**：✏️

#### [20] Segment Any 3D Gaussians
- **🧑‍🔬 作者**：Jiazhong Cen, Jiemin Fang, Chen Yang, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian
- **🏫 单位**：Shanghai Jiao Tong University ⟐ Huawei Inc.
- **🔗 链接**：[[中英摘要](./abs/2312.00860.md)] [[arXiv:2312.00860](https://arxiv.org/abs/2312.00860)] [[Code](https://github.com/Jumpat/SegAnyGAussians)]
- **📝 说明**：✏️

#### [21] GaussianHead: Impressive 3D Gaussian-based Head Avatars with Dynamic Hybrid Neural Field
- **🧑‍🔬 作者**：Jie Wang, Xianyan Li, Jiucheng Xie, Feng Xu, Hao Gao
- **🏫 单位**：Nanjing University of Posts and Telecommunications ⟐ Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2312.01632.md)] [[arXiv:2312.01632](https://arxiv.org/abs/2312.01632)] [[Code](https://github.com/chiehwangs/gaussian-head)]
- **📝 说明**：✏️

#### [22] HeadGaS: Real-Time Animatable Head Avatars via 3D Gaussian Splatting
- **🧑‍🔬 作者**：Helisa Dhamo, Yinyu Nie, Arthur Moreau, Jifei Song, Richard Shaw, Yiren Zhou, Eduardo Pérez-Pellitero
- **🏫 单位**：Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2312.02902.md)] [[arXiv:2312.02902](https://arxiv.org/abs/2312.02902)] [Code]
- **📝 说明**：✏️

#### [23] MonoGaussianAvatar: Monocular Gaussian Point-based Head Avatar
- **🧑‍🔬 作者**：Yufan Chen, Lizhen Wang, Qijing Li, Hongjiang Xiao, Shengping Zhang, Hongxun Yao, Yebin Liu
- **🏫 单位**：Harbin Institute of Technology ⟐ Tsinghua University ⟐ Communication University of China
- **🔗 链接**：[[中英摘要](./abs/2312.04558.md)] [[arXiv:2312.04558](https://arxiv.org/abs/2312.04558)] [[Code](https://github.com/yufan1012/MonoGaussianAvatar)]
- **📝 说明**：✏️

#### [24] EAGLES: Efficient Accelerated 3D Gaussians with Lightweight EncodingS
- **🧑‍🔬 作者**：Sharath Girish, Kamal Gupta, Abhinav Shrivastava
- **🏫 单位**：University of Maryland
- **🔗 链接**：[[中英摘要](./abs/2312.04564.md)] [[arXiv:2312.04564](https://arxiv.org/abs/2312.04564)] [[Code](https://github.com/Sharath-girish/efficientgaussian)]
- **📝 说明**：✏️

#### [25] Learn to Optimize Denoising Scores for 3D Generation: A Unified and Improved Diffusion Prior on NeRF and 3D Gaussian Splatting
- **🧑‍🔬 作者**：Xiaofeng Yang, Yiwen Chen, Cheng Chen, Chi Zhang, Yi Xu, Xulei Yang, Fayao Liu, Guosheng Lin
- **🏫 单位**：Nanyang Technological University ⟐ OPPO US Research Center ⟐ A*STAR
- **🔗 链接**：[[中英摘要](./abs/2312.04820.md)] [[arXiv:2312.04820](https://arxiv.org/abs/2312.04820)] [[Code](https://github.com/yangxiaofeng/LODS)]
- **📝 说明**：✏️

#### [26] GIR: 3D Gaussian Inverse Rendering for Relightable Scene Factorization
- **🧑‍🔬 作者**：Yahao Shi, Yanmin Wu, Chenming Wu, Xing Liu, Chen Zhao, Haocheng Feng, Jingtuo Liu, Liangjun Zhang, Jian Zhang, Bin Zhou, Errui Ding, Jingdong Wang
- **🏫 单位**：Beihang University ⟐ Peking University ⟐ Baidu VIS
- **🔗 链接**：[[中英摘要](./abs/2312.05133.md)] [[arXiv:2312.05133](https://arxiv.org/abs/2312.05133)] [Code]
- **📝 说明**：✏️

#### [27] iComMa: Inverting 3D Gaussians Splatting for Camera Pose Estimation via Comparing and Matching
- **🧑‍🔬 作者**：Yuan Sun, Xuan Wang, Yunfan Zhang, Jie Zhang, Caigui Jiang, Yu Guo, Fei Wang
- **🏫 单位**：Xi’an Jiaotong University ⟐ Ant Group
- **🔗 链接**：[[中英摘要](./abs/2312.09031.md)] [[arXiv:2312.09031](https://arxiv.org/abs/2312.09031)] [Code]
- **📝 说明**：✏️

#### [28] Text2Immersion: Generative Immersive Scene with 3D Gaussians
- **🧑‍🔬 作者**：Hao Ouyang, Kathryn Heal, Stephen Lombardi, Tiancheng Sun
- **🏫 单位**：HKUST ⟐ Google
- **🔗 链接**：[[中英摘要](./abs/2312.09242.md)] [[arXiv:2312.09242](https://arxiv.org/abs/2312.09242)] [Code]
- **📝 说明**：✏️

#### [29] Exploring the Feasibility of Generating Realistic 3D Models of Endangered Species Using DreamGaussian: An Analysis of Elevation Angle's Impact on Model Generation
- **🧑‍🔬 作者**：Selcuk Anil Karatopak, Deniz Sen
- **🏫 单位**：Huawei Türkiye R&D Center
- **🔗 链接**：[[中英摘要](./abs/2312.09682.md)] [[arXiv:2312.09682](https://arxiv.org/abs/2312.09682)] [Code]
- **📝 说明**：✏️

#### [30] GauFRe: Gaussian Deformation Fields for Real-time Dynamic Novel View Synthesis
- **🧑‍🔬 作者**：Yiqing Liang, Numair Khan, Zhengqin Li, Thu Nguyen-Phuoc, Douglas Lanman, James Tompkin, Lei Xiao
- **🏫 单位**：Meta ⟐ Brown University
- **🔗 链接**：[[中英摘要](./abs/2312.11458.md)] [[arXiv:2312.11458](https://arxiv.org/abs/2312.11458)] [[Supp](https://lynl7130.github.io/gaufre/static/pdfs/suppl.pdf)] [Code]
- **📝 说明**：✏️

#### [31] Repaint123: Fast and High-quality One Image to 3D Generation with Progressive Controllable 2D Repainting
- **🧑‍🔬 作者**：Junwu Zhang, Zhenyu Tang, Yatian Pang, Xinhua Cheng, Peng Jin, Yida Wei, Munan Ning, Li Yuan
- **🏫 单位**：Peking University ⟐ Pengcheng Laboratory ⟐  National University of Singapore ⟐ Wuhan University
- **🔗 链接**：[[中英摘要](./abs/2312.13271.md)] [[arXiv:2312.13271](https://arxiv.org/abs/2312.13271)] [[Code](https://github.com/PKU-YuanGroup/repaint123)]
- **📝 说明**：✏️

#### [32] Compact 3D Scene Representation via Self-Organizing Gaussian Grids
- **🧑‍🔬 作者**：Wieland Morgenstern, Florian Barthel, Anna Hilsmann, Peter Eisert
- **🏫 单位**：Fraunhofer Heinrich Hertz Institute ⟐ Humboldt University of Berlin
- **🔗 链接**：[[中英摘要](./abs/2312.13299.md)] [[arXiv:2312.13299](https://arxiv.org/abs/2312.13299)] [[Code](https://github.com/fraunhoferhhi/Self-Organizing-Gaussians)]
- **📝 说明**：✏️

#### [33] SWAGS: Sampling Windows Adaptively for Dynamic 3D Gaussian Splatting
- **🧑‍🔬 作者**：Richard Shaw, Jifei Song, Arthur Moreau, Michal Nazarczuk, Sibi Catley-Chandar, Helisa Dhamo, Eduardo Perez-Pellitero
- **🏫 单位**：Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2312.13308.md)] [[arXiv:2312.13308](https://arxiv.org/abs/2312.13308)] [Code]
- **📝 说明**：✏️

#### [34] Gaussian Splatting with NeRF-based Color and Opacity
- **🧑‍🔬 作者**：Dawid Malarz, Weronika Smolak, Jacek Tabor, Sławomir Tadeja, Przemysław Spurek
- **🏫 单位**：Jagiellonian University ⟐ University of Cambridge
- **🔗 链接**：[[中英摘要](./abs/2312.13729.md)] [[arXiv:2312.13729](https://arxiv.org/abs/2312.13729)] [[Code](https://github.com/gmum/ViewingDirectionGaussianSplatting)]
- **📝 说明**：✏️

#### [35] Deformable 3D Gaussian Splatting for Animatable Human Avatars
- **🧑‍🔬 作者**：HyunJun Jung, Nikolas Brasch, Jifei Song, Eduardo Perez-Pellitero, Yiren Zhou, Zhihao Li, Nassir Navab, Benjamin Busam
- **🏫 单位**：Technical University of Munich ⟐ Huawei Noah’s Ark Lab ⟐ 3dwe.ai
- **🔗 链接**：[[中英摘要](./abs/2312.15059.md)] [[arXiv:2312.15059](https://arxiv.org/abs/2312.15059)] [[Code](https://github.com/Junggy/pardy-human)]
- **📝 说明**：Code link 404

#### [36] Human101: Training 100+FPS Human Gaussians in 100s from 1 View
- **🧑‍🔬 作者**：Mingwei Li, Jiachen Tao, Zongxin Yang, Yi Yang
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2312.15258.md)] [[arXiv:2312.15258](https://arxiv.org/abs/2312.15258)] [[Code](https://github.com/longxiang-ai/Human101)]
- **📝 说明**：✏️

#### [37] Sparse-view CT Reconstruction with 3D Gaussian Volumetric Representation
- **🧑‍🔬 作者**：Yingtai Li, Xueming Fu, Shang Zhao, Ruiyang Jin, S. Kevin Zhou
- **🏫 单位**：University of Science and Technology of China ⟐ Chinese Academy of Sciences
- **🔗 链接**：[[中英摘要](./abs/2312.15676.md)] [[arXiv:2312.15676](https://arxiv.org/abs/2312.15676)] [Code]
- **📝 说明**：✏️

#### [38] 2D-Guided 3D Gaussian Segmentation
- **🧑‍🔬 作者**：Kun Lan, Haoran Li, Haolin Shi, Wenjun Wu, Yong Liao, Lin Wang, Pengyuan Zhou
- **🏫 单位**：University of Science and Technology of China ⟐ HKUST(GZ)
- **🔗 链接**：[[中英摘要](./abs/2312.16047.md)] [[arXiv:2312.16047](https://arxiv.org/abs/2312.16047)] [Code]
- **📝 说明**：✏️

#### [39] DreamGaussian4D: Generative 4D Gaussian Splatting
- **🧑‍🔬 作者**：Jiawei Ren, Liang Pan, Jiaxiang Tang, Chi Zhang, Ang Cao, Gang Zeng, Ziwei Liu
- **🏫 单位**：Nanyang Technological University ⟐ Shanghai AI Laboratory ⟐ Peking University ⟐ University of Michigan
- **🔗 链接**：[[中英摘要](./abs/2312.17142.md)] [[arXiv:2312.17142](https://arxiv.org/abs/2312.17142)] [[Code](https://github.com/jiawei-ren/dreamgaussian4d)]
- **📝 说明**：✏️

#### [40] 4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency
- **🧑‍🔬 作者**：Yuyang Yin, Dejia Xu, Zhangyang Wang, Yao Zhao, Yunchao Wei
- **🏫 单位**：Beijing Jiaotong University ⟐ University of Texas at Austin
- **🔗 链接**：[[中英摘要](./abs/2312.17225.md)] [[arXiv:2312.17225](https://arxiv.org/abs/2312.17225)] [[Code](https://github.com/VITA-Group/4DGen)]
- **📝 说明**：✏️

#### [41] Deblurring 3D Gaussian Splatting
- **🧑‍🔬 作者**：Byeonghyeon Lee, Howoong Lee, Xiangyu Sun, Usman Ali, Eunbyung Park
- **🏫 单位**：Sungkyunkwan University ⟐ Hanhwa Vision
- **🔗 链接**：[[中英摘要](./abs/2401.00834.md)] [[arXiv:2401.00834](https://arxiv.org/abs/2401.00834)] [[Code](https://github.com/benhenryL/Deblurring-3D-Gaussian-Splatting)]
- **📝 说明**：✏️

#### [42] Street Gaussians for Modeling Dynamic Urban Scenes
- **🧑‍🔬 作者**：Yunzhi Yan, Haotong Lin, Chenxu Zhou, Weijie Wang, Haiyang Sun, Kun Zhan, Xianpeng Lang, Xiaowei Zhou, Sida Peng
- **🏫 单位**：Zhejiang University ⟐ Li Auto
- **🔗 链接**：[[中英摘要](./abs/2401.01339.md)] [[arXiv:2401.01339](https://arxiv.org/abs/2401.01339)] [[Code](https://github.com/zju3dv/street_gaussians)]
- **📝 说明**：✏️

#### [43] FMGS: Foundation Model Embedded 3D Gaussian Splatting for Holistic 3D Scene Understanding
- **🧑‍🔬 作者**：Xingxing Zuo, Pouya Samangouei, Yunwen Zhou, Yan Di, Mingyang Li
- **🏫 单位**：Google
- **🔗 链接**：[[中英摘要](./abs/2401.01970.md)] [[arXiv:2401.01970](https://arxiv.org/abs/2401.01970)] [Code]
- **📝 说明**：✏️

#### [44] PEGASUS: Physically Enhanced Gaussian Splatting Simulation System for 6DOF Object Pose Dataset Generation
- **🧑‍🔬 作者**：Lukas Meyer, Floris Erich, Yusuke Yoshiyasu, Marc Stamminger, Noriaki Ando, Yukiyasu Domae
- **🏫 单位**：Friedrich-Alexander-Universität Erlangen-Nürnberg-Fürth ⟐ Industrial CPS Research Center, National Institute of Advanced Industrial Science and Technology, Japan
- **🔗 链接**：[[中英摘要](./abs/2401.02281.md)] [[arXiv:2401.02281](https://arxiv.org/abs/2401.02281)] [[Code](https://github.com/meyerls/PEGASUS)]
- **📝 说明**：✏️

#### [45] Characterizing Satellite Geometry via Accelerated 3D Gaussian Splatting
- **🧑‍🔬 作者**：Van Minh Nguyen, Emma Sandidge, Trupti Mahendrakar, Ryan T. White
- **🏫 单位**：Florida Institute of Technology
- **🔗 链接**：[[中英摘要](./abs/2401.02588.md)] [[arXiv:2401.02588](https://arxiv.org/abs/2401.02588)] [Code]
- **📝 说明**：✏️

#### [46] AGG: Amortized Generative 3D Gaussians for Single Image to 3D
- **🧑‍🔬 作者**：Dejia Xu, Ye Yuan, Morteza Mardani, Sifei Liu, Jiaming Song, Zhangyang Wang, Arash Vahdat
- **🏫 单位**：The University of Texas at Austin ⟐ NVIDIA
- **🔗 链接**：[[中英摘要](./abs/2401.04099.md)] [[arXiv:2401.04099](https://arxiv.org/abs/2401.04099)] [Code]
- **📝 说明**：✏️

#### [47] DISTWAR: Fast Differentiable Rendering on Raster-based Rendering Pipelines
- **🧑‍🔬 作者**：Sankeerth Durvasula, Adrian Zhao, Fan Chen, Ruofan Liang, Pawan Kumar Sanjaya, Nandita Vijaykumar
- **🏫 单位**：University of Toronto
- **🔗 链接**：[[中英摘要](./abs/2401.05345.md)] [[arXiv:2401.05345](https://arxiv.org/abs/2401.05345)] [Code]
- **📝 说明**：✏️

#### [48] CoSSegGaussians: Compact and Swift Scene Segmenting 3D Gaussians
- **🧑‍🔬 作者**：Bin Dou, Tianyu Zhang, Yongjia Ma, Zhaohui Wang, Zejian Yuan
- **🏫 单位**：Xi’an Jiaotong University
- **🔗 链接**：[[中英摘要](./abs/2401.05925.md)] [[arXiv:2401.05925](https://arxiv.org/abs/2401.05925)] [Code]
- **📝 说明**：✏️

#### [49] TRIPS: Trilinear Point Splatting for Real-Time Radiance Field Rendering
- **🧑‍🔬 作者**：Linus Franke, Darius Rückert, Laura Fink, Marc Stamminger
- **🏫 单位**：Friedrich-Alexander-Universität Erlangen-Nürnberg
- **🔗 链接**：[[中英摘要](./abs/2401.06003.md)] [[arXiv:2401.06003](https://arxiv.org/abs/2401.06003)] [[Code](https://github.com/lfranke/trips)]
- **📝 说明**：✏️

#### [50] Fast Dynamic 3D Object Generation from a Single-view Video
- **🧑‍🔬 作者**：Zijie Pan, Zeyu Yang, Xiatian Zhu, Li Zhang
- **🏫 单位**：Fudan University ⟐ University of Surrey
- **🔗 链接**：[[中英摘要](./abs/2401.08742.md)] [[arXiv:2401.08742](https://arxiv.org/abs/2401.08742)] [[Code](https://github.com/fudan-zvg/Efficient4D)]
- **📝 说明**：✏️

#### [51] GaussianBody: Clothed Human Reconstruction via 3d Gaussian Splatting
- **🧑‍🔬 作者**：Mengtian Li, Shengxiang Yao, Zhifeng Xie, Keyu Chen, Yu-Gang Jiang
- **🏫 单位**：Shanghai University ⟐ Fudan University ⟐ Shanghai Engineering Research Center of Motion Picture Special Effects ⟐ Tavus Inc.
- **🔗 链接**：[[中英摘要](./abs/2401.09720.md)] [[arXiv:2401.09720](https://arxiv.org/abs/2401.09720)] [Code]
- **📝 说明**：✏️

#### [52] Deformable Endoscopic Tissues Reconstruction with Gaussian Splatting
- **🧑‍🔬 作者**：Lingting Zhu, Zhao Wang, Zhenchao Jin, Guying Lin, Lequan Yu
- **🏫 单位**：The University of Hong Kong ⟐  The Chinese University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2401.11535.md)] [[arXiv:2401.11535](https://arxiv.org/abs/2401.11535)] [[Code](https://github.com/HKU-MedAI/EndoGS)]
- **📝 说明**：✏️

#### [53] EndoGaussian: Gaussian Splatting for Deformable Surgical Scene Reconstruction
- **🧑‍🔬 作者**：Yifan Liu, Chenxin Li, Chen Yang, Yixuan Yuan
- **🏫 单位**：Chinese University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2401.12561.md)] [[arXiv:2401.12561](https://arxiv.org/abs/2401.12561)] [[Code](https://github.com/yifliu3/EndoGaussian)]
- **📝 说明**：✏️

#### [54] PSAvatar: A Point-based Morphable Shape Model for Real-Time Head Avatar Creation with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zhongyuan Zhao, Zhenyu Bao, Qing Li, Guoping Qiu, Kanglin Liu
- **🏫 单位**：Pengcheng Laboratory ⟐ Peking University ⟐ University of Nottingham ⟐ Shenzhen University
- **🔗 链接**：[[中英摘要](./abs/2401.12900.md)] [[arXiv:2401.12900](https://arxiv.org/abs/2401.12900)] [Code]
- **📝 说明**：✏️

#### [55] LIV-GaussMap: LiDAR-Inertial-Visual Fusion for Real-time 3D Radiance Field Map Rendering
- **🧑‍🔬 作者**：Sheng Hong, Junjie He, Xinhu Zheng, Hesheng Wang, Hao Fang, Kangcheng Liu, Chunran Zheng, Shaojie Shen
- **🏫 单位**：HKUST
- **🔗 链接**：[[中英摘要](./abs/2401.14857.md)] [[arXiv:2401.14857](https://arxiv.org/abs/2401.14857)] [[Code](https://github.com/sheng00125/LIV-GaussMap)]
- **📝 说明**：✏️  Empty code repo

#### [56] Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting
- **🧑‍🔬 作者**：Yutao Feng, Xiang Feng, Yintong Shang, Ying Jiang, Chang Yu, Zeshun Zong, Tianjia Shao, Hongzhi Wu, Kun Zhou, Chenfanfu Jiang, Yin Yang
- **🏫 单位**：University of Utah ⟐ Zhejiang University ⟐ UCLA
- **🔗 链接**：[[中英摘要](./abs/2401.15318.md)] [[arXiv:2401.15318](https://arxiv.org/abs/2401.15318)] [Code]
- **📝 说明**：✏️

#### [57] Endo-4DGS: Distilling Depth Ranking for Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting
- **🧑‍🔬 作者**：Yiming Huang, Beilei Cui, Long Bai, Ziqi Guo, Mengya Xu, Hongliang Ren
- **🏫 单位**：The Chinese University of Hong Kong ⟐  Shun Hing Institute of Advanced Engineering, CUHK ⟐ Shenzhen Research Institute, CUHK
- **🔗 链接**：[[中英摘要](./abs/2401.16416.md)] [[arXiv:2401.16416](https://arxiv.org/abs/2401.16416)] [Code]
- **📝 说明**：✏️

#### [58] VR-GS: A Physical Dynamics-Aware Interactive Gaussian Splatting System in Virtual Reality
- **🧑‍🔬 作者**：Ying Jiang, Chang Yu, Tianyi Xie, Xuan Li, Yutao Feng, Huamin Wang, Minchen Li, Henry Lau, Feng Gao, Yin Yang, Chenfanfu Jiang
- **🏫 单位**：UCLA ⟐ HKU ⟐ Utah ⟐ ZJU ⟐ Style3D Research ⟐ CMU ⟐ Amazon
- **🔗 链接**：[[中英摘要](./abs/2401.16663.md)] [[arXiv:2401.16663](https://arxiv.org/abs/2401.16663)] [Code]
- **📝 说明**：✏️

#### [59] Segment Anything in 3D Gaussians
- **🧑‍🔬 作者**：Xu Hu, Yuxi Wang, Lue Fan, Junsong Fan, Junran Peng, Zhen Lei, Qing Li, Zhaoxiang Zhang
- **🏫 单位**：The Hong Kong Polytechnic University ⟐ Center for Artificial Intelligence and Robotics, HKISI, CAS ⟐
Institute of Automation, Chinese Academy of Sciences ⟐ University of Chinese Academy of Sciences ⟐ Chongyue Technology
- **🔗 链接**：[[中英摘要](./abs/2401.17857.md)] [[arXiv:2401.17857](https://arxiv.org/abs/2401.17857)] [[Code](https://github.com/Jumpat/SegAnyGAussians)]
- **📝 说明**：✏️

#### [60] Optimal Projection for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Letian Huang, Jiayang Bai, Jie Guo, Yanwen Guo
- **🏫 单位**：Nanjing University
- **🔗 链接**：[[中英摘要](./abs/2402.00752.md)] [[arXiv:2402.00752](https://arxiv.org/abs/2402.00752)] [Code]
- **📝 说明**：✏️

#### [61] 360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming
- **🧑‍🔬 作者**：Jiayang Bai, Letian Huang, Jie Guo, Wen Gong, Yuanqi Li, Yanwen Guo
- **🏫 单位**：Nanjing University
- **🔗 链接**：[[中英摘要](./abs/2402.00763.md)] [[arXiv:2402.00763](https://arxiv.org/abs/2402.00763)] [Code]
- **📝 说明**：✏️

#### [62] GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting
- **🧑‍🔬 作者**：Joanna Waczyńska, Piotr Borycki, Sławomir Tadeja, Jacek Tabor, Przemysław Spurek
- **🏫 单位**：Jagiellonian University ⟐ University of Cambridge
- **🔗 链接**：[[中英摘要](./abs/2402.01459.md)] [[arXiv:2402.01459](https://arxiv.org/abs/2402.01459)] [[Code](https://github.com/waczjoan/gaussian-mesh-splatting)]
- **📝 说明**：✏️

#### [63] SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM
- **🧑‍🔬 作者**：Mingrui Li, Shuhong Liu, Heng Zhou
- **🏫 单位**：Dalian University of Technology ⟐ The University of Tokyo ⟐ Columbia University
- **🔗 链接**：[[中英摘要](./abs/2402.03246.md)] [[arXiv:2402.03246](https://arxiv.org/abs/2402.03246)] [Code]
- **📝 说明**：✏️

#### [64] 4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes
- **🧑‍🔬 作者**：Yuanxing Duan, Fangyin Wei, Qiyu Dai, Yuhang He, Wenzheng Chen, Baoquan Chen
- **🏫 单位**：Peking University ⟐ Princeton University ⟐ NVIDIA ⟐ National Key Lab of General AI, China
- **🔗 链接**：[[中英摘要](./abs/2402.03307.md)] [[arXiv:2402.03307](https://arxiv.org/abs/2402.03307)] [Code]
- **📝 说明**：✏️

#### [65] Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos
- **🧑‍🔬 作者**：Alfredo Rivero, ShahRukh Athar, Zhixin Shu, Dimitris Samaras
- **🏫 单位**：Stony Brook University ⟐ Adobe Research
- **🔗 链接**：[[中英摘要](./abs/2402.03723.md)] [[arXiv:2402.03723](https://arxiv.org/abs/2402.03723)] [Code]
- **📝 说明**：✏️

#### [66] Mesh-based Gaussian Splatting for Real-time Large-scale Deformation
- **🧑‍🔬 作者**：Lin Gao, Jie Yang, Bo-Tao Zhang, Jia-Mu Sun, Yu-Jie Yuan, Hongbo Fu, Yu-Kun Lai
- **🏫 单位**：University of Chinese Academy of Sciences ⟐  City University of Hong Kong ⟐ Cardiff University
- **🔗 链接**：[[中英摘要](./abs/2402.04796.md)] [[arXiv:2402.04796](https://arxiv.org/abs/2402.04796)] [Code]
- **📝 说明**：✏️

#### [67] LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation
- **🧑‍🔬 作者**：Jiaxiang Tang, Zhaoxi Chen, Xiaokang Chen, Tengfei Wang, Gang Zeng, Ziwei Liu
- **🏫 单位**：Peking University ⟐ Nanyang Technological University ⟐ Shanghai AI Lab
- **🔗 链接**：[[中英摘要](./abs/2402.05054.md)] [[arXiv:2402.05054](https://arxiv.org/abs/2402.05054)] [[Code](https://github.com/3DTopia/LGM)]
- **📝 说明**：✏️

#### [68] HeadStudio: Text to Animatable Head Avatars with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zhenglin Zhou, Fan Ma, Hehe Fan, Yi Yang
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2402.06149.md)] [[arXiv:2402.06149](https://arxiv.org/abs/2402.06149)] [[Code](https://github.com/ZhenglinZhou/HeadStudio)]
- **📝 说明**：✏️

#### [69] GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided Generative Gaussian Splatting
- **🧑‍🔬 作者**：Xiaoyu Zhou, Xingjian Ran, Yajiao Xiong, Jinlin He, Zhiwei Lin, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang
- **🏫 单位**：Peking University ⟐ Google Research ⟐ University of California, Merced
- **🔗 链接**：[[中英摘要](./abs/2402.07207.md)] [[arXiv:2402.07207](https://arxiv.org/abs/2402.07207)] [[Code](https://github.com/VDIGPKU/GALA3D)]
- **📝 说明**：✏️

#### [70] GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering
- **🧑‍🔬 作者**：Abdullah Hamdi, Luke Melas-Kyriazi, Guocheng Qian, Jinjie Mai, Ruoshi Liu, Carl Vondrick, Bernard Ghanem, Andrea Vedaldi
- **🏫 单位**：VGG, University of Oxford ⟐ KAUST ⟐ Columbia University ⟐ Snap Inc.
- **🔗 链接**：[[中英摘要](./abs/2402.10128.md)] [[arXiv:2402.10128](https://arxiv.org/abs/2402.10128)] [[Code](https://github.com/ajhamdi/ges-splatting)]
- **📝 说明**：✏️

#### [71] GaussianObject: Just Taking Four Images to Get A High-Quality 3D Object with Gaussian Splatting
- **🧑‍🔬 作者**：Chen Yang, Sikuang Li, Jiemin Fang, Ruofan Liang, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian
- **🏫 单位**：Shanghai Jiao Tong University ⟐ Huawei ⟐ University of Toronto
- **🔗 链接**：[[中英摘要](./abs/2402.10259.md)] [[arXiv:2402.10259](https://arxiv.org/abs/2402.10259)] [[Code](https://github.com/GaussianObject/GaussianObject)]
- **📝 说明**：✏️

#### [72] GaussianHair: Hair Modeling and Rendering with Light-aware Gaussians
- **🧑‍🔬 作者**：Haimin Luo, Min Ouyang, Zijun Zhao, Suyi Jiang, Longwen Zhang, Qixuan Zhang, Wei Yang, Lan Xu, Jingyi Yu
- **🏫 单位**：ShanghaiTech University ⟐ Huazhong University of Science and Technology ⟐ Deemos Technology ⟐ LumiAni Technology
- **🔗 链接**：[[中英摘要](./abs/2402.10483.md)] [[arXiv:2402.10483](https://arxiv.org/abs/2402.10483)] [Code]
- **📝 说明**：✏️

#### [73] Identifying Unnecessary 3D Gaussians using Clustering for Fast Rendering of 3D Gaussian Splatting
- **🧑‍🔬 作者**：Joongho Jo, Hyeongwon Kim, Jongsun Park
- **🏫 单位**：Korea University
- **🔗 链接**：[[中英摘要](./abs/2402.13827.md)] [[arXiv:2402.13827](https://arxiv.org/abs/2402.13827)] [Code]
- **📝 说明**：✏️

#### [74] Spec-Gaussian: Anisotropic View-Dependent Appearance for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Ziyi Yang, Xinyu Gao, Yangtian Sun, Yihua Huang, Xiaoyang Lyu, Wen Zhou, Shaohui Jiao, Xiaojuan Qi, Xiaogang Jin
- **🏫 单位**：Zhejiang University ⟐ The University of Hong Kong ⟐ ByteDance Inc.
- **🔗 链接**：[[中英摘要](./abs/2402.15870.md)] [[arXiv:2402.15870](https://arxiv.org/abs/2402.15870)] [Code]
- **📝 说明**：✏️

#### [75] GEA: Reconstructing Expressive 3D Gaussian Avatar from Monocular Video
- **🧑‍🔬 作者**：Xinqi Liu, Chenming Wu, Xing Liu, Jialun Liu, Jinbo Wu, Chen Zhao, Haocheng Feng, Errui Ding, Jingdong Wang
- **🏫 单位**：Baidu Inc.
- **🔗 链接**：[[中英摘要](./abs/2402.16607.md)] [[arXiv:2402.16607](https://arxiv.org/abs/2402.16607)] [Code]
- **📝 说明**：✏️

#### [76] 3D Gaussian Model for Animation and Texturing
- **🧑‍🔬 作者**：Xiangzhi Eric Wang, Zackary P. T. Sin
- **🏫 单位**：The Hong Kong Polytechnic University
- **🔗 链接**：[[中英摘要](./abs/2402.19441.md)] [[arXiv:2402.19441](https://arxiv.org/abs/2402.19441)] [Code]
- **📝 说明**：✏️

#### [77] Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps
- **🧑‍🔬 作者**：Timothy Chen, Ola Shorinwa, Weijia Zeng, Joseph Bruno, Philip Dames, Mac Schwager
- **🏫 单位**：Stanford University ⟐ University of California San Diego ⟐ Temple University
- **🔗 链接**：[[中英摘要](./abs/2403.02751.md)] [[arXiv:2403.02751](https://arxiv.org/abs/2403.02751)] [Code]
- **📝 说明**：✏️

#### [78] Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis
- **🧑‍🔬 作者**：Yuanhao Cai, Yixun Liang, Jiahao Wang, Angtian Wang, Yulun Zhang, Xiaokang Yang, Zongwei Zhou, Alan Yuille
- **🏫 单位**：Johns Hopkins University ⟐ HKUST(GZ) ⟐ Shanghai Jiao Tong University
- **🔗 链接**：[[中英摘要](./abs/2403.04116.md)] [[arXiv:2403.04116](https://arxiv.org/abs/2403.04116)] [[Code](https://github.com/caiyuanhao1998/X-Gaussian)]
- **📝 说明**：✏️

#### [79] BAGS: Blur Agnostic Gaussian Splatting through Multi-Scale Kernel Modeling
- **🧑‍🔬 作者**：Cheng Peng, Yutao Tang, Yifan Zhou, Nengyu Wang, Xijun Liu, Deming Li, Rama Chellappa
- **🏫 单位**：Johns Hopkins University
- **🔗 链接**：[[中英摘要](./abs/2403.04926.md)] [[arXiv:2403.04926](https://arxiv.org/abs/2403.04926)] [[Code](https://github.com/snldmt/BAGS)]
- **📝 说明**：✏️

#### [80] GSEdit: Efficient Text-Guided Editing of 3D Objects via Gaussian Splatting
- **🧑‍🔬 作者**：Francesco Palandra, Andrea Sanchietti, Daniele Baieri, Emanuele Rodolà
- **🏫 单位**：Sapienza University of Rome
- **🔗 链接**：[[中英摘要](./abs/2403.05154.md)] [[arXiv:2403.05154](https://arxiv.org/abs/2403.05154)] [Code]
- **📝 说明**：✏️

#### [81] SemGauss-SLAM: Dense Semantic Gaussian Splatting SLAM
- **🧑‍🔬 作者**：Siting Zhu, Renjie Qin, Guangming Wang, Jiuming Liu, Hesheng Wang
- **🏫 单位**：Shanghai Jiao Tong University ⟐ University of Cambridge
- **🔗 链接**：[[中英摘要](./abs/2403.07494.md)] [[arXiv:2403.07494](https://arxiv.org/abs/2403.07494)] [Code]
- **📝 说明**：✏️

#### [82] StyleGaussian: Instant 3D Style Transfer with Gaussian Splatting
- **🧑‍🔬 作者**：Kunhao Liu, Fangneng Zhan, Muyu Xu, Christian Theobalt, Ling Shao, Shijian Lu
- **🏫 单位**：Nanyang Technological University ⟐ Max Planck Institute for Informatics ⟐ UCAS-Terminus AI Lab
- **🔗 链接**：[[中英摘要](./abs/2403.07807.md)] [[arXiv:2403.07807](https://arxiv.org/abs/2403.07807)] [[Code](https://github.com/Kunhao-Liu/StyleGaussian)]
- **📝 说明**：✏️

#### [83] ManiGaussian: Dynamic Gaussian Splatting for Multi-task Robotic Manipulation
- **🧑‍🔬 作者**：Guanxing Lu, Shiyi Zhang, Ziwei Wang, Changliu Liu, Jiwen Lu, Yansong Tang
- **🏫 单位**：Tsinghua Shenzhen International Graduate School ⟐ Carnegie Mellon University ⟐ Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2403.08321.md)] [[arXiv:2403.08321](https://arxiv.org/abs/2403.08321)] [Code]
- **📝 说明**：✏️

#### [84] Gaussian Splatting in Style
- **🧑‍🔬 作者**：Abhishek Saroha, Mariia Gladkova, Cecilia Curreli, Tarun Yenamandra, Daniel Cremers
- **🏫 单位**：Technical University of Munich
- **🔗 链接**：[[中英摘要](./abs/2403.08498.md)] [[arXiv:2403.08498](https://arxiv.org/abs/2403.08498)] [Code]
- **📝 说明**：✏️

#### [85] GaussCtrl: Multi-View Consistent Text-Driven 3D Gaussian Splatting Editing
- **🧑‍🔬 作者**：Jing Wu, Jia-Wang Bian, Xinghui Li, Guangrun Wang, Ian Reid, Philip Torr, Victor Adrian Prisacariu
- **🏫 单位**：University of Oxford ⟐ Mohamed bin Zayed University of Artificial Intelligence
- **🔗 链接**：[[中英摘要](./abs/2403.08733.md)] [[arXiv:2403.08733](https://arxiv.org/abs/2403.08733)] [Code]
- **📝 说明**：✏️

#### [86] A New Split Algorithm for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Qiyuan Feng, Gengchen Cao, Haoxiang Chen, Tai-Jiang Mu, Ralph R. Martin, Shi-Min Hu
- **🏫 单位**：Tsinghua University ⟐ Cardiff University
- **🔗 链接**：[[中英摘要](./abs/2403.09143.md)] [[arXiv:2403.09143](https://arxiv.org/abs/2403.09143)] [Code]
- **📝 说明**：✏️

#### [87] Hyper-3DG: Text-to-3D Gaussian Generation via Hypergraph
- **🧑‍🔬 作者**：Donglin Di, Jiahui Yang, Chaofan Luo, Zhou Xue, Wei Chen, Xun Yang, Yue Gao
- **🏫 单位**：Space AI, Li Auto ⟐ Tsinghua University ⟐ University of Science and Technology of China ⟐ Harbin Institute of Technology
- **🔗 链接**：[[中英摘要](./abs/2403.09236.md)] [[arXiv:2403.09236](https://arxiv.org/abs/2403.09236)] [[Code](https://github.com/yjhboy/Hyper3DG)]
- **📝 说明**：✏️

#### [88] Relaxing Accurate Initialization Constraint for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Jaewoo Jung, Jisang Han, Honggyu An, Jiwon Kang, Seonghoon Park, Seungryong Kim
- **🏫 单位**：Korea University
- **🔗 链接**：[[中英摘要](./abs/2403.09413.md)] [[arXiv:2403.09413](https://arxiv.org/abs/2403.09413)] [[Code](https://github.com/KU-CVLAB/RAIN-GS)]
- **📝 说明**：✏️

#### [89] Reconstruction and Simulation of Elastic Objects with Spring-Mass 3D Gaussians
- **🧑‍🔬 作者**：Licheng Zhong, Hong-Xing Yu, Jiajun Wu, Yunzhu Li
- **🏫 单位**：Stanford University ⟐ University of Illinois Urbana-Champaign
- **🔗 链接**：[[中英摘要](./abs/2403.09434.md)] [[arXiv:2403.09434](https://arxiv.org/abs/2403.09434)] [[Code](https://github.com/Colmar-zlicheng/Spring-Gaus)]
- **📝 说明**：✏️

#### [90] GaussianGrasper: 3D Language Gaussian Splatting for Open-vocabulary Robotic Grasping
- **🧑‍🔬 作者**：Yuhang Zheng, Xiangyu Chen, Yupeng Zheng, Songen Gu, Runyi Yang, Bu Jin, Pengfei Li, Chengliang Zhong, Zengmao Wang, Lina Liu, Chao Yang, Dawei Wang, Zhen Chen, Xiaoxiao Long, Meiqing Wang
- **🏫 单位**： Beihang University ⟐ Chinese Academy of Sciences ⟐ Tsinghua University ⟐ Imperial College London ⟐ China Mobile Research Institute ⟐ Wuhan University ⟐ Shanghai AI Laboratory ⟐ University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2403.09637.md)] [[arXiv:2403.09637](https://arxiv.org/abs/2403.09637)] [[Code](https://github.com/MrSecant/GaussianGrasper)]
- **📝 说明**：✏️

#### [91] Touch-GS: Visual-Tactile Supervised 3D Gaussian Splatting
- **🧑‍🔬 作者**：Aiden Swann, Matthew Strong, Won Kyung Do, Gadiel Sznaier Camps, Mac Schwager, Monroe Kennedy III
- **🏫 单位**：Stanford University
- **🔗 链接**：[[中英摘要](./abs/2403.09875.md)] [[arXiv:2403.09875](https://arxiv.org/abs/2403.09875)] [Code]
- **📝 说明**：✏️

#### [92] Controllable Text-to-3D Generation via Surface-Aligned Gaussian Splatting
- **🧑‍🔬 作者**：Zhiqi Li, Yiming Chen, Lingzhe Zhao, Peidong Liu
- **🏫 单位**：Zhejiang University ⟐ Westlake University ⟐ Tongji University
- **🔗 链接**：[[中英摘要](./abs/2403.09981.md)] [[arXiv:2403.09981](https://arxiv.org/abs/2403.09981)] [[Code](https://github.com/WU-CVGL/MVControl-threestudio)]
- **📝 说明**：✏️

#### [93] Texture-GS: Disentangling the Geometry and Texture for 3D Gaussian Splatting Editing
- **🧑‍🔬 作者**：Tian-Xing Xu, Wenbo Hu, Yu-Kun Lai, Ying Shan, Song-Hai Zhang
- **🏫 单位**：Tsinghua University ⟐ Tencent AI Lab ⟐ Cardiff University
- **🔗 链接**：[[中英摘要](./abs/2403.10050.md)] [[arXiv:2403.10050](https://arxiv.org/abs/2403.10050)] [Code]
- **📝 说明**：✏️

#### [94] GGRt: Towards Generalizable 3D Gaussians without Pose Priors in Real-Time
- **🧑‍🔬 作者**：Hao Li, Yuanyuan Gao, Dingwen Zhang, Chenming Wu, Yalun Dai, Chen Zhao, Haocheng Feng, Errui Ding, Jingdong Wang, Junwei Han
- **🏫 单位**：Northwestern Polytechnical University ⟐ Baidu Inc. ⟐ Nanyang Technological University
- **🔗 链接**：[[中英摘要](./abs/2403.10147.md)] [[arXiv:2403.10147](https://arxiv.org/abs/2403.10147)] [Code]
- **📝 说明**：✏️

#### [95] FDGaussian: Fast Gaussian Splatting from Single Image via Geometric-aware Diffusion Model
- **🧑‍🔬 作者**：Qijun Feng, Zhen Xing, Zuxuan Wu, Yu-Gang Jiang
- **🏫 单位**：Fudan University
- **🔗 链接**：[[中英摘要](./abs/2403.10242.md)] [[arXiv:2403.10242](https://arxiv.org/abs/2403.10242)] [Code]
- **📝 说明**：✏️

#### [96] SWAG: Splatting in the Wild images with Appearance-conditioned Gaussians
- **🧑‍🔬 作者**：Hiba Dahmani, Moussab Bennehar, Nathan Piasco, Luis Roldao, Dzmitry Tsishkou
- **🏫 单位**：Noah’s Ark, Huawei Paris Research Center
- **🔗 链接**：[[中英摘要](./abs/2403.10427.md)] [[arXiv:2403.10427](https://arxiv.org/abs/2403.10427)] [Code]
- **📝 说明**：✏️

#### [97] GS-Pose: Cascaded Framework for Generalizable Segmentation-based 6D Object Pose Estimation
- **🧑‍🔬 作者**：Dingding Cai, Janne Heikkilä, Esa Rahtu
- **🏫 单位**：Tampere University ⟐ University of Oulu
- **🔗 链接**：[[中英摘要](./abs/2403.10683.md)] [[arXiv:2403.10683](https://arxiv.org/abs/2403.10683)] [[Code](https://github.com/dingdingcai/GSPose)]
- **📝 说明**：✏️

#### [98] DarkGS: Learning Neural Illumination and 3D Gaussians Relighting for Robotic Exploration in the Dark
- **🧑‍🔬 作者**：Tianyi Zhang, Kaining Huang, Weiming Zhi, Matthew Johnson-Roberson
- **🏫 单位**：Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2403.10814.md)] [[arXiv:2403.10814](https://arxiv.org/abs/2403.10814)] [[Code](https://github.com/tyz1030/neuralight)]
- **📝 说明**：✏️

#### [99] Analytic-Splatting: Anti-Aliased 3D Gaussian Splatting via Analytic Integration
- **🧑‍🔬 作者**：Analytic-Splatting: Anti-Aliased 3D Gaussian Splatting via Analytic Integration
- **🏫 单位**：South China University of Technology ⟐ Tencent AI Lab ⟐ City University of Hong Kong ⟐ The Chinese University of Hong Kong, Shenzhen
- **🔗 链接**：[[中英摘要](./abs/2403.11056.md)] [[arXiv:2403.11056](https://arxiv.org/abs/2403.11056)] [[Code](https://github.com/lzhnb/Analytic-Splatting)]
- **📝 说明**：✏️

#### [100] Compact 3D Gaussian Splatting For Dense Visual SLAM
- **🧑‍🔬 作者**：Tianchen Deng, Yaohui Chen, Leyan Zhang, Jianfei Yang, Shenghai Yuan, Danwei Wang, Weidong Chen
- **🏫 单位**：Shanghai Jiao Tong University ⟐ Nanyang Technological University
- **🔗 链接**：[[中英摘要](./abs/2403.11247.md)] [[arXiv:2403.11247](https://arxiv.org/abs/2403.11247)] [Code]
- **📝 说明**：✏️

#### [101] BrightDreamer: Generic 3D Gaussian Generative Framework for Fast Text-to-3D Synthesis
- **🧑‍🔬 作者**：Lutao Jiang, Lin Wang
- **🏫 单位**：HKUST(GZ) ⟐ HKUST
- **🔗 链接**：[[中英摘要](./abs/2403.11273.md)] [[arXiv:2403.11273](https://arxiv.org/abs/2403.11273)] [[Code](https://github.com/lutao2021/BrightDreamer)]
- **📝 说明**：✏️

#### [102] GeoGaussian: Geometry-aware Gaussian Splatting for Scene Rendering
- **🧑‍🔬 作者**：Yanyan Li, Chenyu Lyu, Yan Di, Guangyao Zhai, Gim Hee Lee, Federico Tombari
- **🏫 单位**：Technical University of Munich ⟐ Tianjin University ⟐ National University of Singapore ⟐ Google
- **🔗 链接**：[[中英摘要](./abs/2403.11324.md)] [[arXiv:2403.11324](https://arxiv.org/abs/2403.11324)] [Code]
- **📝 说明**：✏️

#### [103] 3DGS-ReLoc: 3D Gaussian Splatting for Map Representation and Visual ReLocalization
- **🧑‍🔬 作者**：Peng Jiang, Gaurav Pandey, Srikanth Saripalli
- **🏫 单位**：Texas A&M University
- **🔗 链接**：[[中英摘要](./abs/2403.11367.md)] [[arXiv:2403.11367](https://arxiv.org/abs/2403.11367)] [Code]
- **📝 说明**：✏️

#### [104] BAGS: Building Animatable Gaussian Splatting from a Monocular Video with Diffusion Priors
- **🧑‍🔬 作者**：Tingyang Zhang, Qingzhe Gao, Weiyu Li, Libin Liu, Baoquan Chen
- **🏫 单位**：Peking University ⟐ Shandong University ⟐ The Hong Kong University of Science and Technology ⟐
- **🔗 链接**：[[中英摘要](./abs/2403.11427.md)] [[arXiv:2403.11427](https://arxiv.org/abs/2403.11427)] [[Code](https://github.com/Talegqz/BAGS)]
- **📝 说明**：✏️

#### [105] Motion-aware 3D Gaussian Splatting for Efficient Dynamic Scene Reconstruction
- **🧑‍🔬 作者**：Zhiyang Guo, Wengang Zhou, Li Li, Min Wang, Houqiang Li
- **🏫 单位**：University of Science and Technology of China ⟐ Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
- **🔗 链接**：[[中英摘要](./abs/2403.11447.md)] [[arXiv:2403.11447](https://arxiv.org/abs/2403.11447)] [Code]
- **📝 说明**：✏️

#### [106] Bridging 3D Gaussian and Mesh for Freeview Video Rendering
- **🧑‍🔬 作者**：Yuting Xiao, Xuan Wang, Jiafei Li, Hongrui Cai, Yanbo Fan, Nan Xue, Minghui Yang, Yujun Shen, Shenghua Gao
- **🏫 单位**：Shanghai Tech University ⟐ Ant Group ⟐ Xi’an Jiaotong University ⟐ University of Science and Technology of China
- **🔗 链接**：[[中英摘要](./abs/2403.11453.md)] [[arXiv:2403.11453](https://arxiv.org/abs/2403.11453)] [Code]
- **📝 说明**：✏️

#### [107] Fed3DGS: Scalable 3D Gaussian Splatting with Federated Learning
- **🧑‍🔬 作者**：Teppei Suzuki
- **🏫 单位**：Denso IT Laboratory, Inc.
- **🔗 链接**：[[中英摘要](./abs/2403.11460.md)] [[arXiv:2403.11460](https://arxiv.org/abs/2403.11460)] [[Code](https://github.com/DensoITLab/Fed3DGS)]
- **📝 说明**：✏️

#### [108] 3DGS-Calib: 3D Gaussian Splatting for Multimodal SpatioTemporal Calibration
- **🧑‍🔬 作者**：Quentin Herau, Moussab Bennehar, Arthur Moreau, Nathan Piasco, Luis Roldao, Dzmitry Tsishkou, Cyrille Migniot, Pascal Vasseur, Cédric Demonceaux
- **🏫 单位**：Noah’s Ark ⟐ Universite de Bourgogne ⟐ Universite de Picardie Jules Verne
- **🔗 链接**：[[中英摘要](./abs/2403.11577.md)] [[arXiv:2403.11577](https://arxiv.org/abs/2403.11577)] [Code]
- **📝 说明**：✏️

#### [109] UV Gaussians: Joint Learning of Mesh Deformation and Gaussian Textures for Human Avatar Modeling
- **🧑‍🔬 作者**：Yujiao Jiang, Qingmin Liao, Xiaoyu Li, Li Ma, Qi Zhang, Chaopeng Zhang, Zongqing Lu, Ying Shan
- **🏫 单位**：Tsinghua Shenzhen International Graduate School ⟐ Tencent AI Lab ⟐ The Hong Kong University of Science and Technology
- **🔗 链接**：[[中英摘要](./abs/2403.11589.md)] [[arXiv:2403.11589](https://arxiv.org/abs/2403.11589)] [Code]
- **📝 说明**：✏️

#### [110] GaussNav: Gaussian Splatting for Visual Navigation
- **🧑‍🔬 作者**：Xiaohan Lei, Min Wang, Wengang Zhou, Houqiang Li
- **🏫 单位**：Univerisity of Science and Technology of China ⟐ Hefei Comprehensive National Science Center
- **🔗 链接**：[[中英摘要](./abs/2403.11625.md)] [[arXiv:2403.11625](https://arxiv.org/abs/2403.11625)] [Code]
- **📝 说明**：✏️

#### [111] NEDS-SLAM: A Novel Neural Explicit Dense Semantic SLAM Framework using 3D Gaussian Splatting
- **🧑‍🔬 作者**：Yiming Ji, Yang Liu, Guanghu Xie, Boyu Ma, Zongwu Xie
- **🏫 单位**：Harbin Institute of Technology
- **🔗 链接**：[[中英摘要](./abs/2403.11679.md)] [[arXiv:2403.11679](https://arxiv.org/abs/2403.11679)] [Code]
- **📝 说明**：✏️

#### [112] BAD-Gaussians: Bundle Adjusted Deblur Gaussian Splatting
- **🧑‍🔬 作者**：Lingzhe Zhao, Peng Wang, Peidong Liu
- **🏫 单位**：Westlake University ⟐ Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2403.11831.md)] [[arXiv:2403.11831](https://arxiv.org/abs/2403.11831)] [[Code](https://github.com/WU-CVGL/BAD-Gaussians)]
- **📝 说明**：✏️

#### [113] View-Consistent 3D Editing with Gaussian Splatting
- **🧑‍🔬 作者**：Yuxuan Wang, Xuanyu Yi, Zike Wu, Na Zhao, Long Chen, Hanwang Zhang
- **🏫 单位**：Nanyang Technological University ⟐ Singapore University of Technology and Design ⟐ Hong Kong University of Science and Technology ⟐ Skywork AI
- **🔗 链接**：[[中英摘要](./abs/2403.11868.md)] [[arXiv:2403.11868](https://arxiv.org/abs/2403.11868)] [Code]
- **📝 说明**：✏️

#### [114] VideoMV: Consistent Multi-View Generation Based on Large Video Generative Model
- **🧑‍🔬 作者**：Qi Zuo, Xiaodong Gu, Lingteng Qiu, Yuan Dong, Zhengyi Zhao, Weihao Yuan, Rui Peng, Siyu Zhu, Zilong Dong, Liefeng Bo, Qixing Huang
- **🏫 单位**：Alibaba Group ⟐ CUHKSZ ⟐ Fudan University ⟐ Peking University ⟐ The University of Texas at Austin
- **🔗 链接**：[[中英摘要](./abs/2403.12010.md)] [[arXiv:2403.12010](https://arxiv.org/abs/2403.12010)] [[Code](https://github.com/alibaba/VideoMV)]
- **📝 说明**：✏️

#### [115] GaussianFlow: Splatting Gaussian Dynamics for 4D Content Creation
- **🧑‍🔬 作者**：Quankai Gao, Qiangeng Xu, Zhe Cao, Ben Mildenhall, Wenchao Ma, Le Chen, Danhang Tang, Ulrich Neumann
- **🏫 单位**：University of Southern California ⟐ Google ⟐ Pennsylvania State University ⟐ Max Planck Institute for Intelligent Systems
- **🔗 链接**：[[中英摘要](./abs/2403.12365.md)] [[arXiv:2403.12365](https://arxiv.org/abs/2403.12365)] [[Code](https://github.com/Zerg-Overmind/GaussianFlow)]
- **📝 说明**：✏️

#### [116] High-Fidelity SLAM Using Gaussian Splatting with Rendering-Guided Densification and Regularized Optimization
- **🧑‍🔬 作者**：Shuo Sun, Malcolm Mielle, Achim J. Lilienthal, Martin Magnusson
- **🏫 单位**：Orebro University ⟐ Technical University of Munich
- **🔗 链接**：[[中英摘要](./abs/2403.12535.md)] [[arXiv:2403.12535](https://arxiv.org/abs/2403.12535)] [Code]
- **📝 说明**：✏️  Submitted to IROS24

#### [117] RGBD GS-ICP SLAM
- **🧑‍🔬 作者**：Seongbo Ha, Jiung Yeon, Hyeonwoo Yu
- **🏫 单位**：Sungkyunkwan University
- **🔗 链接**：[[中英摘要](./abs/2403.12550.md)] [[arXiv:2403.12550](https://arxiv.org/abs/2403.12550)] [Code]
- **📝 说明**：✏️

#### [118] GVGEN: Text-to-3D Generation with Volumetric Representation
- **🧑‍🔬 作者**：Xianglong He, Junyi Chen, Sida Peng, Di Huang, Yangguang Li, Xiaoshui Huang, Chun Yuan, Wanli Ouyang, Tong He
- **🏫 单位**：Shanghai AI Lab ⟐ Tsinghua Shenzhen International Graduate School ⟐ Shanghai Jiao Tong University ⟐ Zhejiang University ⟐ VAST
- **🔗 链接**：[[中英摘要](./abs/2403.12957.md)] [[arXiv:2403.12957](https://arxiv.org/abs/2403.12957)] [Code]
- **📝 说明**：✏️

#### [119] Gaussian Splatting on the Move: Blur and Rolling Shutter Compensation for Natural Camera Motion
- **🧑‍🔬 作者**：Otto Seiskari, Jerry Ylilammi, Valtteri Kaatrasalo, Pekka Rantalankila, Matias Turkulainen, Juho Kannala, Esa Rahtu, Arno Solin
- **🏫 单位**：Spectacular AI ⟐ ETH Zurich ⟐ Aalto University ⟐ Tampere University
- **🔗 链接**：[[中英摘要](./abs/2403.13327.md)] [[arXiv:2403.13327](https://arxiv.org/abs/2403.13327)] [[Code](https://github.com/SpectacularAI/3dgs-deblur)]
- **📝 说明**：✏️

#### [120] RadSplat: Radiance Field-Informed Gaussian Splatting for Robust Real-Time Rendering with 900+ FPS
- **🧑‍🔬 作者**：Michael Niemeyer, Fabian Manhardt, Marie-Julie Rakotosaona, Michael Oechsle, Daniel Duckworth, Rama Gosula, Keisuke Tateno, John Bates, Dominik Kaeser, Federico Tombari
- **🏫 单位**：Google
- **🔗 链接**：[[中英摘要](./abs/2403.13806.md)] [[arXiv:2403.13806](https://arxiv.org/abs/2403.13806)] [Code]
- **📝 说明**：✏️

#### [121] Mini-Splatting: Representing Scenes with a Constrained Number of Gaussians
- **🧑‍🔬 作者**：Guangchi Fang, Bing Wang
- **🏫 单位**：The Hong Kong Polytechnic University
- **🔗 链接**：[[中英摘要](./abs/2403.14166.md)] [[arXiv:2403.14166](https://arxiv.org/abs/2403.14166)] [[Code](https://github.com/fatPeter/mini-splatting)]
- **📝 说明**：✏️

#### [122] Isotropic Gaussian Splatting for Real-Time Radiance Field Rendering
- **🧑‍🔬 作者**：Yuanhao Gong, Lantao Yu, Guanghui Yue
- **🏫 单位**：Shenzhen University ⟐ Guangdong Key Laboratory of Intelligent Information Processing ⟐ Adobe Inc.
- **🔗 链接**：[[中英摘要](./abs/2403.14244.md)] [[arXiv:2403.14244](https://arxiv.org/abs/2403.14244)] [Code]
- **📝 说明**：✏️

#### [123] HAC: Hash-grid Assisted Context for 3D Gaussian Splatting Compression
- **🧑‍🔬 作者**：Yihang Chen, Qianyi Wu, Jianfei Cai, Mehrtash Harandi, Weiyao Lin
- **🏫 单位**：Shanghai Jiao Tong University ⟐ Monash University
- **🔗 链接**：[[中英摘要](./abs/2403.14530.md)] [[arXiv:2403.14530](https://arxiv.org/abs/2403.14530)] [[Code](https://github.com/YihangChen-ee/HAC)]
- **📝 说明**：✏️

#### [124] Gaussian Frosting: Editable Complex Radiance Fields with Real-Time Rendering
- **🧑‍🔬 作者**：Antoine Guédon, Vincent Lepetit
- **🏫 单位**：Univ Gustave Eiffel
- **🔗 链接**：[[中英摘要](./abs/2403.14554.md)] [[arXiv:2403.14554](https://arxiv.org/abs/2403.14554)] [Code]
- **📝 说明**：✏️

#### [125] GRM: Large Gaussian Reconstruction Model for Efficient 3D Reconstruction and Generation
- **🧑‍🔬 作者**：Yinghao Xu, Zifan Shi, Wang Yifan, Hansheng Chen, Ceyuan Yang, Sida Peng, Yujun Shen, Gordon Wetzstein
- **🏫 单位**：Stanford University ⟐ The Hong Kong University of Science and Technology ⟐ Shanghai AI Laboratory ⟐ Zhejiang University ⟐ Ant Group
- **🔗 链接**：[[中英摘要](./abs/2403.14621.md)] [[arXiv:2403.14621](https://arxiv.org/abs/2403.14621)] [[Code](https://github.com/justimyhxu/GRM)]
- **📝 说明**：✏️

#### [126] MVSplat: Efficient 3D Gaussian Splatting from Sparse Multi-View Images
- **🧑‍🔬 作者**：Yuedong Chen, Haofei Xu, Chuanxia Zheng, Bohan Zhuang, Marc Pollefeys, Andreas Geiger, Tat-Jen Cham, Jianfei Cai
- **🏫 单位**：Monash University ⟐ ETH Zurich ⟐ University of Tübingen ⟐ University of Oxford ⟐ Microsoft ⟐ Nanyang Technological University
- **🔗 链接**：[[中英摘要](./abs/2403.14627.md)] [[arXiv:2403.14627](https://arxiv.org/abs/2403.14627)] [[Code](https://github.com/donydchen/mvsplat)]
- **📝 说明**：✏️

#### [127] STAG4D: Spatial-Temporal Anchored Generative 4D Gaussians
- **🧑‍🔬 作者**：Yifei Zeng, Yanqin Jiang, Siyu Zhu, Yuanxun Lu, Youtian Lin, Hao Zhu, Weiming Hu, Xun Cao, Yao Yao
- **🏫 单位**：Nanjing University ⟐ Institution of Automation, Chinese Academy of Science ⟐ Fudan University
- **🔗 链接**：[[中英摘要](./abs/2403.14939.md)] [[arXiv:2403.14939](https://arxiv.org/abs/2403.14939)] [[Code](https://github.com/zeng-yifei/STAG4D)]
- **📝 说明**：✏️

#### [128] EndoGSLAM: Real-Time Dense Reconstruction and Tracking in Endoscopic Surgeries using Gaussian Splatting
- **🧑‍🔬 作者**：Kailing Wang, Chen Yang, Yuehao Wang, Sikuang Li, Yan Wang, Qi Dou, Xiaokang Yang, Wei Shen
- **🏫 单位**： Shanghai Jiao Tong University ⟐ The Chinese University of Hong Kong ⟐ East China Normal University
- **🔗 链接**：[[中英摘要](./abs/2403.15124.md)] [[arXiv:2403.15124](https://arxiv.org/abs/2403.15124)] [[Code](https://github.com/endogslam/EndoGSLAM)]:
- **📝 说明**：✏️

#### [129] Pixel-GS: Density Control with Pixel-aware Gradient for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zheng Zhang, Wenbo Hu, Yixing Lao, Tong He, Hengshuang Zhao
- **🏫 单位**：The University of Hong Kong ⟐ Tencent AI Lab ⟐ Shanghai AI Lab
- **🔗 链接**：[[中英摘要](./abs/2403.15530.md)] [[arXiv:2403.15530](https://arxiv.org/abs/2403.15530)] [[Code](https://github.com/zhengzhang01/Pixel-GS)]
- **📝 说明**：✏️

#### [130] Semantic Gaussians: Open-Vocabulary Scene Understanding with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Jun Guo, Xiaojian Ma, Yue Fan, Huaping Liu, Qing Li
- **🏫 单位**：BIGAI ⟐ Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2403.15624.md)] [[arXiv:2403.15624](https://arxiv.org/abs/2403.15624)] [[Code](https://github.com/sharinka0715/semantic-gaussians)]
- **📝 说明**：✏️

#### [131] Gaussian in the Wild: 3D Gaussian Splatting for Unconstrained Image Collections
- **🧑‍🔬 作者**：Dongbin Zhang, Chuming Wang, Weitao Wang, Peihao Li, Minghan Qin, Haoqian Wang
- **🏫 单位**：Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2403.15704.md)] [[arXiv:2403.15704](https://arxiv.org/abs/2403.15704)] [Code]
- **📝 说明**：✏️

#### [132] CG-SLAM: Efficient Dense RGB-D SLAM in a Consistent Uncertainty-aware 3D Gaussian Field
- **🧑‍🔬 作者**：Jiarui Hu, Xianhao Chen, Boyin Feng, Guanglin Li, Liangjing Yang, Hujun Bao, Guofeng Zhang, Zhaopeng Cui
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2403.16095.md)] [[arXiv:2403.16095](https://arxiv.org/abs/2403.16095)] [[Code](https://github.com/hjr37/CG-SLAM)]
- **📝 说明**：✏️

#### [133] latentSplat: Autoencoding Variational Gaussians for Fast Generalizable 3D Reconstruction
- **🧑‍🔬 作者**：Christopher Wewer, Kevin Raj, Eddy Ilg, Bernt Schiele, Jan Eric Lenssen
- **🏫 单位**：Max Planck Institute for Informatics ⟐ Saarland University
- **🔗 链接**：[[中英摘要](./abs/2403.16292.md)] [[arXiv:2403.16292](https://arxiv.org/abs/2403.16292)] [[Code](https://github.com/Chrixtar/latentsplat)]
- **📝 说明**：✏️

#### [134] GSDF: 3DGS Meets SDF for Improved Rendering and Reconstruction
- **🧑‍🔬 作者**：Mulin Yu, Tao Lu, Linning Xu, Lihan Jiang, Yuanbo Xiangli, Bo Dai
- **🏫 单位**：Shanghai Artificial Intelligence Laboratory ⟐ The Chinese University of Hong Kong ⟐ University of Science and Technology of China ⟐ Cornell University
- **🔗 链接**：[[中英摘要](./abs/2403.16964.md)] [[arXiv:2403.16964](https://arxiv.org/abs/2403.16964)] [[Code](https://github.com/city-super/GSDF)]
- **📝 说明**：✏️

#### [135] DreamPolisher: Towards High-Quality Text-to-3D Generation via Geometric Diffusion
- **🧑‍🔬 作者**：Yuanze Lin, Ronald Clark, Philip Torr
- **🏫 单位**：University of Oxford
- **🔗 链接**：[[中英摘要](./abs/2403.17237.md)] [[arXiv:2403.17237](https://arxiv.org/abs/2403.17237)] [[Code](https://github.com/yuanze-lin/DreamPolisher)]
- **📝 说明**：✏️

#### [136] DN-Splatter: Depth and Normal Priors for Gaussian Splatting and Meshing
- **🧑‍🔬 作者**：Matias Turkulainen, Xuqian Ren, Iaroslav Melekhov, Otto Seiskari, Esa Rahtu, Juho Kannala
- **🏫 单位**：ETH Zurich ⟐ Tampere University ⟐ Aalto University ⟐ Spectacular AI
- **🔗 链接**：[[中英摘要](./abs/2403.17822.md)] [[arXiv:2403.17822](https://arxiv.org/abs/2403.17822)] [[Code](https://github.com/maturk/dn-splatter)]
- **📝 说明**：✏️

#### [137] 2D Gaussian Splatting for Geometrically Accurate Radiance Fields
- **🧑‍🔬 作者**：Binbin Huang, Zehao Yu, Anpei Chen, Andreas Geiger, Shenghua Gao
- **🏫 单位**：ShanghaiTech University ⟐ University of Tübingen
- **🔗 链接**：[[中英摘要](./abs/2403.17888.md)] [[arXiv:2403.17888](https://arxiv.org/abs/2403.17888)] [Code]
- **📝 说明**：✏️

#### [138] Octree-GS: Towards Consistent Real-time Rendering with LOD-Structured 3D Gaussians
- **🧑‍🔬 作者**：Kerui Ren, Lihan Jiang, Tao Lu, Mulin Yu, Linning Xu, Zhangkai Ni, Bo Dai
- **🏫 单位**：Shanghai Artificial Intelligence Laboratory ⟐ Tongji University ⟐ University of Science and Technology of China ⟐ The Chinese University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2403.17898.md)] [[arXiv:2403.17898](https://arxiv.org/abs/2403.17898)] [[Code](https://github.com/city-super/Octree-GS)]
- **📝 说明**：✏️

#### [139] Modeling uncertainty for Gaussian Splatting
- **🧑‍🔬 作者**：Luca Savant, Diego Valsesia, Enrico Magli
- **🏫 单位**：Politecnico di Torino
- **🔗 链接**：[[中英摘要](./abs/2403.18476.md)] [[arXiv:2403.18476](https://arxiv.org/abs/2403.18476)] [Code]
- **📝 说明**：✏️

#### [140] SplatFace: Gaussian Splat Face Reconstruction Leveraging an Optimizable Surface
- **🧑‍🔬 作者**：Jiahao Luo, Jing Liu, James Davis
- **🏫 单位**：University of California ⟐ ByteDance Inc.
- **🔗 链接**：[[中英摘要](./abs/2403.18784.md)] [[arXiv:2403.18784](https://arxiv.org/abs/2403.18784)] [Code]
- **📝 说明**：✏️

#### [141] Gamba: Marry Gaussian Splatting with Mamba for single view 3D reconstruction
- **🧑‍🔬 作者**：Qiuhong Shen, Xuanyu Yi, Zike Wu, Pan Zhou, Hanwang Zhang, Shuicheng Yan, Xinchao Wang
- **🏫 单位**：National University of Singapore ⟐ Singapore Management University ⟐ Nanyang Technology University ⟐ Sea AI Lab ⟐ Skywork AI
- **🔗 链接**：[[中英摘要](./abs/2403.18795.md)] [[arXiv:2403.18795](https://arxiv.org/abs/2403.18795)] [Code]
- **📝 说明**：✏️

#### [142] CoherentGS: Sparse Novel View Synthesis with Coherent 3D Gaussians
- **🧑‍🔬 作者**：Avinash Paliwal, Wei Ye, Jinhui Xiong, Dmytro Kotovenko, Rakesh Ranjan, Vikas Chandra, Nima Khademi Kalantari
- **🏫 单位**：Texas A&M University ⟐ Meta Reality Labs ⟐ LMU Munich
- **🔗 链接**：[[中英摘要](./abs/2403.19495.md)] [[arXiv:2403.19495](https://arxiv.org/abs/2403.19495)] [Code]
- **📝 说明**：✏️

#### [143] SA-GS: Scale-Adaptive Gaussian Splatting for Training-Free Anti-Aliasing
- **🧑‍🔬 作者**：Xiaowei Song, Jv Zheng, Shiran Yuan, Huan-ang Gao, Jingwei Zhao, Xiang He, Weihao Gu, Hao Zhao
- **🏫 单位**：Tsinghua University ⟐ Tongji University ⟐ Ocean University of China ⟐ Duke Kunshan University ⟐ Haomo.ai
- **🔗 链接**：[[中英摘要](./abs/2403.19615.md)] [[arXiv:2403.19615](https://arxiv.org/abs/2403.19615)] [[Code](https://github.com/zsy1987/SA-GS)]
- **📝 说明**：✏️

#### [144] GauStudio: A Modular Framework for 3D Gaussian Splatting and Beyond
- **🧑‍🔬 作者**：Chongjie Ye, Yinyu Nie, Jiahao Chang, Yuantao Chen, Yihao Zhi, Xiaoguang Han
- **🏫 单位**：CUHKSZ ⟐ Technical University of Munich
- **🔗 链接**：[[中英摘要](./abs/2403.19632.md)] [[arXiv:2403.19632](https://arxiv.org/abs/2403.19632)] [[Code](https://github.com/GAP-LAB-CUHK-SZ/gaustudio)]
- **📝 说明**：✏️

#### [145] GaussianCube: Structuring Gaussian Splatting using Optimal Transport for 3D Generative Modeling
- **🧑‍🔬 作者**：Bowen Zhang, Yiji Cheng, Jiaolong Yang, Chunyu Wang, Feng Zhao, Yansong Tang, Dong Chen, Baining Guo
- **🏫 单位**：University of Science and Technology of China ⟐ Tsinghua University ⟐ Microsoft Research Asia
- **🔗 链接**：[[中英摘要](./abs/2403.19655.md)] [[arXiv:2403.19655](https://arxiv.org/abs/2403.19655)] [[Code](https://github.com/GaussianCube/GaussianCube)]
- **📝 说明**：✏️

#### [146] HO-Gaussian: Hybrid Optimization of 3D Gaussian Splatting for Urban Scenes
- **🧑‍🔬 作者**：Zhuopeng Li, Yilin Zhang, Chenming Wu, Jianke Zhu, Liangjun Zhang
- **🏫 单位**：Zhejiang University ⟐ Baidu Research
- **🔗 链接**：[[中英摘要](./abs/2403.20032.md)] [[arXiv:2403.20032](https://arxiv.org/abs/2403.20032)] [Code]
- **📝 说明**：✏️

#### [147] SGD: Street View Synthesis with Gaussian Splatting and Diffusion Prior
- **🧑‍🔬 作者**：Zhongrui Yu, Haoran Wang, Jinze Yang, Hanzhang Wang, Zeke Xie, Yunfeng Cai, Jiale Cao, Zhong Ji, Mingming Sun
- **🏫 单位**：ETH Zürich ⟐ Baidu Research ⟐ University of Chinese Academy of Sciences ⟐ Harbin Institute of Technology ⟐ Tianjin University
- **🔗 链接**：[[中英摘要](./abs/2403.20079.md)] [[arXiv:2403.20079](https://arxiv.org/abs/2403.20079)] [Code]
- **📝 说明**：✏️

#### [148] HGS-Mapping: Online Dense Mapping Using Hybrid Gaussian Representation in Urban Scenes
- **🧑‍🔬 作者**：Ke Wu, Kaizhao Zhang, Zhiwei Zhang, Shanshuai Yuan, Muer Tie, Julong Wei, Zijun Xu, Jieru Zhao, Zhongxue Gan, Wenchao Ding
- **🏫 单位**：Fudan University ⟐ Harbin Institute of Technology ⟐ Shanghai Jiao Tong University
- **🔗 链接**：[[中英摘要](./abs/2403.20159.md)] [[arXiv:2403.20159](https://arxiv.org/abs/2403.20159)] [Code]
- **📝 说明**：✏️

#### [149] Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces
- **🧑‍🔬 作者**：Mauro Comi, Alessio Tonioni, Max Yang, Jonathan Tremblay, Valts Blukis, Yijiong Lin, Nathan F. Lepora, Laurence Aitchison
- **🏫 单位**：University of Bristol ⟐ Google Zurich ⟐ NVIDIA
- **🔗 链接**：[[中英摘要](./abs/2403.20275.md)] [[arXiv:2403.20275](https://arxiv.org/abs/2403.20275)] [Code]
- **📝 说明**：✏️

#### [150] InstantSplat: Unbounded Sparse-view Pose-free Gaussian Splatting in 40 Seconds
- **🧑‍🔬 作者**：Zhiwen Fan, Wenyan Cong, Kairun Wen, Kevin Wang, Jian Zhang, Xinghao Ding, Danfei Xu, Boris Ivanovic, Marco Pavone, Georgios Pavlakos, Zhangyang Wang, Yue Wang
- **🏫 单位**：University of Texas at Austin ⟐ Nvidia Research ⟐ Xiamen University ⟐ Georgia Institute of Technology ⟐ Stanford University ⟐ University of Southern California
- **🔗 链接**：[[中英摘要](./abs/2403.20309.md)] [[arXiv:2403.20309](https://arxiv.org/abs/2403.20309)] [Code]
- **📝 说明**：✏️

#### [151] 3DGSR: Implicit Surface Reconstruction with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Xiaoyang Lyu, Yang-Tian Sun, Yi-Hua Huang, Xiuzhe Wu, Ziyi Yang, Yilun Chen, Jiangmiao Pang, Xiaojuan Qi
- **🏫 单位**：The University of Hong Kong ⟐ Zhejiang University ⟐ Shanghai AI Lab
- **🔗 链接**：[[中英摘要](./abs/2404.00409.md)] [[arXiv:2404.00409](https://arxiv.org/abs/2404.00409)] [Code]
- **📝 说明**：✏️

#### [152] MM3DGS SLAM: Multi-modal 3D Gaussian Splatting for SLAM Using Vision, Depth, and Inertial Measurements
- **🧑‍🔬 作者**：Lisong C. Sun, Neel P. Bhatt, Jonathan C. Liu, Zhiwen Fan, Zhangyang Wang, Todd E. Humphreys, Ufuk Topcu
- **🏫 单位**：University of Texas at Austin
- **🔗 链接**：[[中英摘要](./abs/2404.00923.md)] [[arXiv:2404.00923](https://arxiv.org/abs/2404.00923)] [Code]
- **📝 说明**：✏️

#### [153] CityGaussian: Real-time High-quality Large-Scale Scene Rendering with Gaussians
- **🧑‍🔬 作者**：Yang Liu, He Guan, Chuanchen Luo, Lue Fan, Junran Peng, Zhaoxiang Zhang
- **🏫 单位**：Chinese Academy of Sciences ⟐ University of Chinese Academy of Sciences ⟐ Centre for Artificial Intelligence and Robotics ⟐ State Key Laboratory of Multimodal Artificial Intelligence Systems
- **🔗 链接**：[[中英摘要](./abs/2404.01133.md)] [[arXiv:2404.01133](https://arxiv.org/abs/2404.01133)] [[Code](https://github.com/DekuLiuTesla/CityGaussian)]
- **📝 说明**：✏️

#### [154] Mirror-3DGS: Incorporating Mirror Reflections into 3D Gaussian Splatting
- **🧑‍🔬 作者**：Jiarui Meng, Haijie Li, Yanmin Wu, Qiankun Gao, Shuzhou Yang, Jian Zhang, Siwei Ma
- **🏫 单位**：Peking Universiy
- **🔗 链接**：[[中英摘要](./abs/2404.01168.md)] [[arXiv:2404.01168](https://arxiv.org/abs/2404.01168)] [Code]
- **📝 说明**：✏️

#### [155] Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing
- **🧑‍🔬 作者**：Ri-Zhao Qiu, Ge Yang, Weijia Zeng, Xiaolong Wang
- **🏫 单位**：University of California San Diego ⟐ Massachusetts Institute of Technology ⟐ Institute for Artificial Intelligence and Fundamental Interactions
- **🔗 链接**：[[中英摘要](./abs/2404.01223.md)] [[arXiv:2404.01223](https://arxiv.org/abs/2404.01223)] [[Code](https://github.com/vuer-ai/feature_splatting)]
- **📝 说明**：✏️

#### [156] Surface Reconstruction from Gaussian Splatting via Novel Stereo Views
- **🧑‍🔬 作者**：Yaniv Wolf, Amit Bracha, Ron Kimmel
- **🏫 单位**：Israel Institute of Technology
- **🔗 链接**：[[中英摘要](./abs/2404.01810.md)] [[arXiv:2404.01810](https://arxiv.org/abs/2404.01810)] [Code]
- **📝 说明**：✏️

#### [157] TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Surrounding Autonomous Driving Scenes
- **🧑‍🔬 作者**：Cheng Zhao, Su Sun, Ruoyu Wang, Yuliang Guo, Jun-Jun Wan, Zhou Huang, Xinyu Huang, Yingjie Victor Chen, Liu Ren
- **🏫 单位**：Bosch Research North America ⟐ Purdue University ⟐ XC Cross Domain Computing
- **🔗 链接**：[[中英摘要](./abs/2404.02410.md)] [[arXiv:2404.02410](https://arxiv.org/abs/2404.02410)] [Code]
- **📝 说明**：✏️

#### [158] GaSpCT: Gaussian Splatting for Novel CT Projection View Synthesis
- **🧑‍🔬 作者**：Emmanouil Nikolakakis, Utkarsh Gupta, Jonathan Vengosh, Justin Bui, Razvan Marinescu
- **🏫 单位**：University of California
- **🔗 链接**：[[中英摘要](./abs/2404.03126.md)] [[arXiv:2404.03126](https://arxiv.org/abs/2404.03126)] [Code]
- **📝 说明**：✏️

#### [159] OmniGS: Omnidirectional Gaussian Splatting for Fast Radiance Field Reconstruction using Omnidirectional Images
- **🧑‍🔬 作者**：Longwei Li, Huajian Huang, Sai-Kit Yeung, Hui Cheng
- **🏫 单位**：Sun Yat-Sen University
- **🔗 链接**：[[中英摘要](./abs/2404.03202.md)] [[arXiv:2404.03202](https://arxiv.org/abs/2404.03202)] [Code]
- **📝 说明**：✏️

#### [160] Per-Gaussian Embedding-Based Deformation for Deformable 3D Gaussian Splatting
- **🧑‍🔬 作者**：Jeongmin Bae, Seoha Kim, Youngsik Yun, Hahyun Lee, Gun Bang, Youngjung Uh
- **🏫 单位**：Yonsei University ⟐ Electronics and Telecommunications Research Institute
- **🔗 链接**：[[中英摘要](./abs/2404.03613.md)] [[arXiv:2404.03613](https://arxiv.org/abs/2404.03613)] [[Code](https://github.com/JeongminB/E-D3DGS)]
- **📝 说明**：✏️

#### [161] Robust Gaussian Splatting
- **🧑‍🔬 作者**：François Darmon, Lorenzo Porzi, Samuel Rota-Bulò, Peter Kontschieder
- **🏫 单位**：Meta Reality Labs Zurich
- **🔗 链接**：[[中英摘要](./abs/2404.04211.md)] [[arXiv:2404.04211](https://arxiv.org/abs/2404.04211)] [Code]
- **📝 说明**：✏️

#### [162] Z-Splat: Z-Axis Gaussian Splatting for Camera-Sonar Fusion
- **🧑‍🔬 作者**：Ziyuan Qu, Omkar Vengurlekar, Mohamad Qadri, Kevin Zhang, Michael Kaess, Christopher Metzler, Suren Jayasuriya, Adithya Pediredla
- **🏫 单位**：Dartmouth College ⟐ Arizona State University ⟐ Carnegie Mellon University ⟐ University of Maryland
- **🔗 链接**：[[中英摘要](./abs/2404.04687.md)] [[arXiv:2404.04687](https://arxiv.org/abs/2404.04687)] [Code]
- **📝 说明**：✏️

#### [163] GauU-Scene V2: Expanse Lidar Image Dataset Shows Unreliable Geometric Reconstruction Using Gaussian Splatting and NeRF
- **🧑‍🔬 作者**：Butian Xiong, Nanjun Zheng, Zhen Li
- **🏫 单位**：The Chinese University of Hong Kong, Shenzhen
- **🔗 链接**：[[中英摘要](./abs/2404.04880.md)] [[arXiv:2404.04880](https://arxiv.org/abs/2404.04880)] [[Code](https://github.com/saliteta/lidar_SfM_alignment)]
- **📝 说明**：✏️

#### [164] Dual-Camera Smooth Zoom on Mobile Phones
- **🧑‍🔬 作者**：Renlong Wu, Zhilu Zhang, Yu Yang, Wangmeng Zuo
- **🏫 单位**：Harbin Institute of Technology
- **🔗 链接**：[[中英摘要](./abs/2404.04908.md)] [[arXiv:2404.04908](https://arxiv.org/abs/2404.04908)] [Code]
- **📝 说明**：✏️

#### [165] StylizedGS: Controllable Stylization for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Dingxi Zhang, Zhuoxun Chen, Yu-Jie Yuan, Fang-Lue Zhang, Zhenliang He, Shiguang Shan, Lin Gao
- **🏫 单位**：The University of Chinese Academy of Sciences
- **🔗 链接**：[[中英摘要](./abs/2404.05220.md)] [[arXiv:2404.05220](https://arxiv.org/abs/2404.05220)] [Code]
- **📝 说明**：✏️

#### [166] Revising Densification in Gaussian Splatting
- **🧑‍🔬 作者**：Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder
- **🏫 单位**：Meta Reality Labs Zurich
- **🔗 链接**：[[中英摘要](./abs/2404.06109.md)] [[arXiv:2404.06109](https://arxiv.org/abs/2404.06109)] [Code]
- **📝 说明**：✏️

#### [167] Gaussian Pancakes: Geometrically-Regularized 3D Gaussian Splatting for Realistic Endoscopic Reconstruction
- **🧑‍🔬 作者**：Sierra Bonilla, Shuai Zhang, Dimitrios Psychogyios, Danail Stoyanov, Francisco Vasconcelos, Sophia Bano
- **🏫 单位**：University College London
- **🔗 链接**：[[中英摘要](./abs/2404.06128.md)] [[arXiv:2404.06128](https://arxiv.org/abs/2404.06128)] [[Code](https://github.com/smbonilla/GaussianPancakes)]
- **📝 说明**：✏️

#### [168] DreamScene360: Unconstrained Text-to-3D Scene Generation with Panoramic Gaussian Splatting
- **🧑‍🔬 作者**：Shijie Zhou, Zhiwen Fan, Dejia Xu, Haoran Chang, Pradyumna Chari, Tejas Bharadwaj, Suya You, Zhangyang Wang, Achuta Kadambi
- **🏫 单位**：University of California, Los Angeles ⟐ University of Texas at Austin ⟐ DEVCOM Army Research Laboratory
- **🔗 链接**：[[中英摘要](./abs/2404.06903.md)] [[arXiv:2404.06903](https://arxiv.org/abs/2404.06903)] [Code]
- **📝 说明**：✏️

#### [169] Gaussian-LIC: Photo-realistic LiDAR-Inertial-Camera SLAM with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Xiaolei Lang, Laijian Li, Hang Zhang, Feng Xiong, Mu Xu, Yong Liu, Xingxing Zuo, Jiajun Lv
- **🏫 单位**：Zhejiang University ⟐  AMAP ⟐ Technical University of Munich
- **🔗 链接**：[[中英摘要](./abs/2404.06926.md)] [[arXiv:2404.06926](https://arxiv.org/abs/2404.06926)] [Code]
- **📝 说明**：✏️

#### [170] RealmDreamer: Text-Driven 3D Scene Generation with Inpainting and Depth Diffusion
- **🧑‍🔬 作者**：Jaidev Shriram, Alex Trevithick, Lingjie Liu, Ravi Ramamoorthi
- **🏫 单位**：University of California, San Diego ⟐  AMAP ⟐ University of Pennsylvania
- **🔗 链接**：[[中英摘要](./abs/2404.07199.md)] [[arXiv:2404.07199](https://arxiv.org/abs/2404.07199)] [Code]
- **📝 说明**：✏️

#### [171] Reinforcement Learning with Generalizable Gaussian Splatting
- **🧑‍🔬 作者**：Jiaxu Wang, Qiang Zhang, Jingkai Sun, Jiahang Cao, Yecheng Shao, Renjing Xu
- **🏫 单位**：The Hong Kong University of Science and Technology (Guangzhou), China ⟐  Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2404.07950.md)] [[arXiv:2404.07950](https://arxiv.org/abs/2404.07950)] [Code]
- **📝 说明**：✏️

#### [172] OccGaussian: 3D Gaussian Splatting for Occluded Human Rendering
- **🧑‍🔬 作者**：Jingrui Ye, Zongkai Zhang, Yujiao Jiang, Qingmin Liao, Wenming Yang, Zongqing Lu
- **🏫 单位**：Tsinghua Shenzhen International Graduate School, Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2404.08449.md)] [[arXiv:2404.08449](https://arxiv.org/abs/2404.08449)] [Code]
- **📝 说明**：✏️

#### [173] LoopGaussian: Creating 3D Cinemagraph with Multi-view Images via Eulerian Motion Field
- **🧑‍🔬 作者**：Jiyang Li, Lechao Cheng, Zhangye Wang, Tingting Mu, Jingxuan He
- **🏫 单位**：Zhejiang University HangZhou, China ⟐ Hefei University of Technology Hefei, China ⟐ University of Manchester Manchester, United Kingdom
- **🔗 链接**：[[中英摘要](./abs/2404.08966.md)] [[arXiv:2404.08966](https://arxiv.org/abs/2404.08966)] [[Code](https://github.com/Pokerlishao/LoopGaussian)]
- **📝 说明**：✏️

#### [174] EGGS: Edge Guided Gaussian Splatting for Radiance Fields
- **🧑‍🔬 作者**：Yuanhao Gong
- **🏫 单位**：Electronics and Information Engineering, Shenzhen University, China
- **🔗 链接**：[[中英摘要](./abs/2404.09105.md)] [[arXiv:2404.09105](https://arxiv.org/abs/2404.09105)] [Code]
- **📝 说明**：✏️

#### [175] DreamScape: 3D Scene Creation via Gaussian Splatting joint Correlation Modeling
- **🧑‍🔬 作者**：Xuening Yuan, Hongyu Yang, Yueming Zhao, Di Huang
- **🏫 单位**：Beihang University Beijing, China
- **🔗 链接**：[[中英摘要](./abs/2404.09227.md)] [[arXiv:2404.09227](https://arxiv.org/abs/2404.09227)] [Code]
- **📝 说明**：✏️

#### [176] DeferredGS: Decoupled and Editable Gaussian Splatting with Deferred Shading
- **🧑‍🔬 作者**：Tong Wu, Jia-Mu Sun, Yu-Kun Lai, Yuewen Ma, Leif Kobbelt, Lin Gao
- **🏫 单位**：Institute of Computing Technology
- **🔗 链接**：[[中英摘要](./abs/2404.09412.md)] [[arXiv:2404.09412](https://arxiv.org/abs/2404.09412)] [Code]
- **📝 说明**：✏️

#### [177] CompGS: Efficient 3D Scene Representation via Compressed Gaussian Splatting
- **🧑‍🔬 作者**：Xiangrui Liu, Xinju Wu, Pingping Zhang, Shiqi Wang, Zhu Li, Sam Kwong
- **🏫 单位**：City University of Hong Kong ⟐ University of Missouri-Kansas City ⟐ Lingnan University
- **🔗 链接**：[[中英摘要](./abs/2404.09458.md)] [[arXiv:2404.09458](https://arxiv.org/abs/2404.09458)] [Code]
- **📝 说明**：✏️

#### [178] 3D Gaussian Splatting as Markov Chain Monte Carlo
- **🧑‍🔬 作者**：Shakiba Kheradmand, Daniel Rebain, Gopal Sharma, Weiwei Sun, Jeff Tseng, Hossam Isack, Abhishek Kar, Andrea Tagliasacchi, Kwang Moo Yi
- **🏫 单位**：University of British Columbia ⟐ Google Research ⟐ Google DeepMind ⟐ Simon Fraser University ⟐ University of Toronto
- **🔗 链接**：[[中英摘要](./abs/2404.09591.md)] [[arXiv:2404.09591](https://arxiv.org/abs/2404.09591)] [Code]
- **📝 说明**：✏️

#### [179] LetsGo: Large-Scale Garage Modeling and Rendering via LiDAR-Assisted Gaussian Primitives
- **🧑‍🔬 作者**：Jiadi Cui, Junming Cao, Yuhui Zhong, Liao Wang, Fuqiang Zhao, Penghao Wang, Yifan Chen, Zhipeng He, Lan Xu, Yujiao Shi, Yingliang Zhang, Jingyi Yu
- **🏫 单位**：ShanghaiTech University ⟐ DGene ⟐ Stereye ⟐ NeuDim
- **🔗 链接**：[[中英摘要](./abs/2404.09748.md)] [[arXiv:2404.09748](https://arxiv.org/abs/2404.09748)] [Code]
- **📝 说明**：✏️

#### [180] SRGS: Super-Resolution 3D Gaussian Splatting
- **🧑‍🔬 作者**：Xiang Feng, Yongbo He, Yubo Wang, Yan Yang, Zhenzhong Kuang, Yu Jun, Jianping Fan, Jiajun ding
- **🏫 单位**：Hangzhou Dianzi University
- **🔗 链接**：[[中英摘要](./abs/2404.10318.md)] [[arXiv:2404.10318](https://arxiv.org/abs/2404.10318)] [Code]
- **📝 说明**：✏️

#### [181] AbsGS: Recovering Fine Details for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zongxin Ye, Wenyu Li, Sidun Liu, Peng Qiao, Yong Dou
- **🏫 单位**：National University of Defense Technology Changsha, China
- **🔗 链接**：[[中英摘要](./abs/2404.10484.md)] [[arXiv:2404.10484](https://arxiv.org/abs/2404.10484)] [[Code](https://github.com/TY424/AbsGS)]
- **📝 说明**：✏️

#### [182] Gaussian Splatting Decoder for 3D-aware Generative Adversarial Networks
- **🧑‍🔬 作者**：Florian Barthel, Arian Beckmann, Wieland Morgenstern, Anna Hilsmann, Peter Eisert
- **🏫 单位**：Fraunhofer Heinrich Hertz Institute, HHI ⟐ Humboldt University of Berlin
- **🔗 链接**：[[中英摘要](./abs/2404.10625.md)] [[arXiv:2404.10625](https://arxiv.org/abs/2404.10625)] [Code]
- **📝 说明**：✏️

#### [183] Gaussian Opacity Fields: Efficient and Compact Surface Reconstruction in Unbounded Scenes
- **🧑‍🔬 作者**：Zehao Yu, Torsten Sattler, Andreas Geiger
- **🏫 单位**：University of Tübingen, Tübingen AI Center, Germany ⟐ Czech Technical University in Prague, Czech Republic
- **🔗 链接**：[[中英摘要](./abs/2404.10772.md)] [[arXiv:2404.10772](https://arxiv.org/abs/2404.10772)] [[Code](https://github.com/autonomousvision/gaussian-opacity-fields)]
- **📝 说明**：✏️

#### [184] DeblurGS: Gaussian Splatting for Camera Motion Blur
- **🧑‍🔬 作者**：Jeongtaek Oh, Jaeyoung Chung, Dongwoo Lee, Kyoung Mu Lee
- **🏫 单位**：Seoul National University ⟐ Seoul National University
- **🔗 链接**：[[中英摘要](./abs/2404.11358.md)] [[arXiv:2404.11358](https://arxiv.org/abs/2404.11358)] [Code]
- **📝 说明**：✏️

#### [185] InFusion: Inpainting 3D Gaussians via Learning Depth Completion from Diffusion Prior
- **🧑‍🔬 作者**：Zhiheng Liu, Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Jie Xiao, Kai Zhu, Nan Xue, Yu Liu, Yujun Shen, Yang Cao
- **🏫 单位**：University of Science and Technology of China ⟐ The Hong Kong University of Science and Technology ⟐ Ant Group ⟐ Alibaba Group
- **🔗 链接**：[[中英摘要](./abs/2404.11613.md)] [[arXiv:2404.11613](https://arxiv.org/abs/2404.11613)] [[Code](https://github.com/ali-vilab/infusion)]
- **📝 说明**：✏️

#### [186] Dynamic Gaussians Mesh: Consistent Mesh Reconstruction from Monocular Videos
- **🧑‍🔬 作者**：Isabella Liu, Hao Su, Xiaolong Wang
- **🏫 单位**：University of California, San Diego
- **🔗 链接**：[[中英摘要](./abs/2404.12379.md)] [[arXiv:2404.12379](https://arxiv.org/abs/2404.12379)] [[Code](https://github.com/Isabella98Liu/DG-Mesh)]
- **📝 说明**：✏️

#### [187] Does Gaussian Splatting need SFM Initialization?
- **🧑‍🔬 作者**：Yalda Foroutan, Daniel Rebain, Kwang Moo Yi, Andrea Tagliasacchi
- **🏫 单位**：Simon Fraser University ⟐ University of British Columbia ⟐ University of Toronto ⟐ Google DeepMind
- **🔗 链接**：[[中英摘要](./abs/2404.12547.md)] [[arXiv:2404.12547](https://arxiv.org/abs/2404.12547)] [Code]
- **📝 说明**：✏️

#### [188] EfficientGS: Streamlining Gaussian Splatting for Large-Scale High-Resolution Scene Representation
- **🧑‍🔬 作者**：Wenkai Liu, Tao Guan, Bin Zhu, Lili Ju, Zikai Song, Dan Li, Yuesong Wang, Wei Yang
- **🏫 单位**：Huazhong University of Science and Technology ⟐ Wuhan Farsee2 Technology Co., Ltd. ⟐ University of South Carolina
- **🔗 链接**：[[中英摘要](./abs/2404.12777.md)] [[arXiv:2404.12777](https://arxiv.org/abs/2404.12777)] [Code]
- **📝 说明**：✏️

#### [189] Contrastive Gaussian Clustering: Weakly Supervised 3D Scene Segmentation
- **🧑‍🔬 作者**：Myrna C. Silva, Mahtab Dahaghin, Matteo Toso, Alessio Del Bue
- **🏫 单位**：Pattern Analysis and Computer Vision (PAVIS), Istituto Italiano di Tecnologia (IIT) Genoa, Italy
- **🔗 链接**：[[中英摘要](./abs/2404.12784.md)] [[arXiv:2404.12784](https://arxiv.org/abs/2404.12784)] [Code]
- **📝 说明**：✏️

#### [190] GScream: Learning 3D Geometry and Feature Consistent Gaussian Splatting for Object Removal
- **🧑‍🔬 作者**：Yuxin Wang, Qianyi Wu, Guofeng Zhang, Dan Xu
- **🏫 单位**：HKUST ⟐ Monash University ⟐ Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2404.13679.md)] [[arXiv:2404.13679](https://arxiv.org/abs/2404.13679)] [Code]
- **📝 说明**：✏️

#### [191] GaussianTalker: Speaker-specific Talking Head Synthesis via 3D Gaussian Splatting
- **🧑‍🔬 作者**：Hongyun Yu, Zhan Qu, Qihang Yu, Jianchuan Chen, Zhonghua Jiang, Zhiwen Chen, Shengyu Zhang, Jimin Xu, Fei Wu, Chengfei Lv, Gang Yu
- **🏫 单位**：Alibaba Group ⟐ Zhejiang University ⟐ Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2404.14037.md)] [[arXiv:2404.14037](https://arxiv.org/abs/2404.14037)] [Code]
- **📝 说明**：✏️

#### [192] CLIP-GS: CLIP-Informed Gaussian Splatting for Real-time and View-consistent 3D Semantic Understanding
- **🧑‍🔬 作者**：Guibiao Liao, Jiankun Li, Zhenyu Bao, Xiaoqing Ye, Jingdong Wang, Qing Li, Kanglin Liu
- **🏫 单位**：Peking University ⟐ Baidu Inc. ⟐ Peng Cheng Laboratory
- **🔗 链接**：[[中英摘要](./abs/2404.14249.md)] [[arXiv:2404.14249](https://arxiv.org/abs/2404.14249)] [[Code](https://github.com/gbliao/CLIP-GS)]
- **📝 说明**：✏️

#### [193] TalkingGaussian: Structure-Persistent 3D Talking Head Synthesis via Gaussian Splatting
- **🧑‍🔬 作者**：Jiahe Li, Jiawei Zhang, Xiao Bai, Jin Zheng, Xin Ning, Jun Zhou, Lin Gu
- **🏫 单位**：Beihang University ⟐ Chinese Academy of Sciences ⟐ Griffith University ⟐ RIKEN AIP ⟐ The University of Tokyo
- **🔗 链接**：[[中英摘要](./abs/2404.15264.md)] [[arXiv:2404.15264](https://arxiv.org/abs/2404.15264)] [Code]
- **📝 说明**：✏️

#### [194] OMEGAS: Object Mesh Extraction from Large Scenes Guided by Gaussian Segmentation
- **🧑‍🔬 作者**：Lizhi Wang, Feng Zhou, Jianqin Yin
- **🏫 单位**：Beijing University of Posts and Telecommunications
- **🔗 链接**：[[中英摘要](./abs/2404.15891.md)] [[arXiv:2404.15891](https://arxiv.org/abs/2404.15891)] [[Code](https://github.com/CrystalWlz/OMEGAS)]
- **📝 说明**：✏️

#### [195] GaussianTalker: Real-Time High-Fidelity Talking Head Synthesis with Audio-Driven 3D Gaussian Splatting
- **🧑‍🔬 作者**：Kyusun Cho, Joungbin Lee, Heeji Yoon, Yeobin Hong, Jaehoon Ko, Sangjun Ahn, Seungryong Kim
- **🏫 单位**：Korea University ⟐ NCSOFT
- **🔗 链接**：[[中英摘要](./abs/2404.16012.md)] [[arXiv:2404.16012](https://arxiv.org/abs/2404.16012)] [[Code](https://github.com/KU-CVLAB/GaussianTalker)]
- **📝 说明**：✏️

#### [196] DIG3D: Marrying Gaussian Splatting with Deformable Transformer for Single Image 3D Reconstruction
- **🧑‍🔬 作者**：Jiamin Wu, Kenkun Liu, Han Gao, Xiaoke Jiang, Lei Zhang
- **🏫 单位**：Hong Kong University of Science and Technology ⟐ International Digital Economy Academy (IDEA) ⟐ The Chinese University of Hong Kong, Shenzhen
- **🔗 链接**：[[中英摘要](./abs/2404.16323.md)] [[arXiv:2404.16323](https://arxiv.org/abs/2404.16323)] [Code]
- **📝 说明**：✏️

#### [197] SLAM for Indoor Mapping of Wide Area Construction Environments
- **🧑‍🔬 作者**：Vincent Ress, Wei Zhang, David Skuddis, Norbert Haala, Uwe Soergel
- **🏫 单位**：Institute for Photogrammetry and Geoinformatics, University of Stuttgart, Germany
- **🔗 链接**：[[中英摘要](./abs/2404.17215.md)] [[arXiv:2404.17215](https://arxiv.org/abs/2404.17215)] [Code]
- **📝 说明**：✏️

#### [198] Reconstructing Satellites in 3D from Amateur Telescope Images
- **🧑‍🔬 作者**：Zhiming Chang, Boyang Liu, Yifei Xia, Youming Guo, Boxin Shi, He Sun
- **🏫 单位**：Simon Fraser University ⟐ University of British Columbia ⟐ University of Toronto ⟐ Google DeepMind
- **🔗 链接**：[[中英摘要](./abs/2404.18394.md)] [[arXiv:2404.18394](https://arxiv.org/abs/2404.18394)] [Code]
- **📝 说明**：✏️

#### [199] 3D Gaussian Splatting with Deferred Reflection
- **🧑‍🔬 作者**：Keyang Ye, Qiming Hou, Kun Zhou
- **🏫 单位**：State Key Lab of CAD&CG, Zhejiang University, Hangzhou, China
- **🔗 链接**：[[中英摘要](./abs/2404.18454.md)] [[arXiv:2404.18454](https://arxiv.org/abs/2404.18454)] [Code]
- **📝 说明**：✏️

#### [200] Bootstrap 3D Reconstructed Scenes from 3D Gaussian Splatting
- **🧑‍🔬 作者**：Yifei Gao, Jie Ou, Lei Wang, Jun Cheng
- **🏫 单位**：University of Electronic Science and Technology of China ⟐ Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences ⟐ Sichuan Yuanzhigu Technology Co., Ltd
- **🔗 链接**：[[中英摘要](./abs/2404.18669.md)] [[arXiv:2404.18669](https://arxiv.org/abs/2404.18669)] [Code]
- **📝 说明**：✏️

#### [201] DGE: Direct Gaussian 3D Editing by Consistent Multi-view Editing
- **🧑‍🔬 作者**：Minghao Chen, Iro Laina, Andrea Vedaldi
- **🏫 单位**：Visual Geometry Group, University of Oxford
- **🔗 链接**：[[中英摘要](./abs/2404.18929.md)] [[arXiv:2404.18929](https://arxiv.org/abs/2404.18929)] [[Code](https://github.com/silent-chen/DGE)]
- **📝 说明**：✏️

#### [202] MeGA: Hybrid Mesh-Gaussian Head Avatar for High-Fidelity Rendering and Head Editing
- **🧑‍🔬 作者**：Cong Wang, Di Kang, He-Yi Sun, Shen-Han Qian, Zi-Xuan Wang, Linchao Bao, Song-Hai Zhang
- **🏫 单位**：Tsinghua University ⟐ Tencent AI Lab ⟐ Technical University of Munich ⟐ Carnegie Mellon University ⟐ University of Birmingham
- **🔗 链接**：[[中英摘要](./abs/2404.19026.md)] [[arXiv:2404.19026](https://arxiv.org/abs/2404.19026)] [[Code](https://github.com/conallwang/MeGA)]
- **📝 说明**：✏️

#### [203] GSTalker: Real-time Audio-Driven Talking Face Generation via Deformable Gaussian Splatting
- **🧑‍🔬 作者**：Bo Chen, Shoukang Hu, Qi Chen, Chenpeng Du, Ran Yi, Yanmin Qian, Xie Chen
- **🏫 单位**：Shanghai Jiaotong University ⟐ Nanyang Technological University
- **🔗 链接**：[[中英摘要](./abs/2404.19040.md)] [[arXiv:2404.19040](https://arxiv.org/abs/2404.19040)] [Code]
- **📝 说明**：✏️

#### [204] SAGS: Structure-Aware 3D Gaussian Splatting
- **🧑‍🔬 作者**：Evangelos Ververas, Rolandos Alexandros Potamias, Jifei Song, Jiankang Deng, Stefanos Zafeiriou
- **🏫 单位**：Imperial College London ⟐ Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2404.19149.md)] [[arXiv:2404.19149](https://arxiv.org/abs/2404.19149)] [Code]
- **📝 说明**：✏️

#### [205] MicroDreamer: Zero-shot 3D Generation in ∼20 Seconds by Score-based Iterative Reconstruction
- **🧑‍🔬 作者**：Luxi Chen, Zhengyi Wang, Chongxuan Li, Tingting Gao, Hang Su, Jun Zhu
- **🏫 单位**：Renmin University of China ⟐ Tsinghua University ⟐ Kuaishou Technology
- **🔗 链接**：[[中英摘要](./abs/2404.19525.md)] [[arXiv:2404.19525](https://arxiv.org/abs/2404.19525)] [[Code](https://github.com/ML-GSAI/MicroDreamer)]
- **📝 说明**：✏️

#### [206] GS-LRM: Large Reconstruction Model for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Kai Zhang, Sai Bi, Hao Tan, Yuanbo Xiangli, Nanxuan Zhao, Kalyan Sunkavalli, Zexiang Xu
- **🏫 单位**：Adobe Research ⟐ Cornell University
- **🔗 链接**：[[中英摘要](./abs/2404.19702.md)] [[arXiv:2404.19702](https://arxiv.org/abs/2404.19702)] [Code]
- **📝 说明**：✏️

#### [207] Spectrally Pruned Gaussian Fields with Neural Compensation
- **🧑‍🔬 作者**：Runyi Yang, Zhenxin Zhu, Zhou Jiang, Baijun Ye, Xiaoxue Chen, Yifei Zhang, Yuantao Chen, Jian Zhao, Hao Zhao
- **🏫 单位**：Tsinghua University ⟐ Imperial College London ⟐ Beihang University ⟐ Beijing Institute of Technology ⟐ UCAS ⟐ CUHK ⟐ China Telecom
- **🔗 链接**：[[中英摘要](./abs/2405.00676.md)] [[arXiv:2405.00676](https://arxiv.org/abs/2405.00676)] [[Code](https://github.com/RunyiYang/SUNDAE)]
- **📝 说明**：✏️

#### [208] Efficient Data-driven Scene Simulation using Robotic Surgery Videos via Physics-embedded 3D Gaussians
- **🧑‍🔬 作者**：Zhenya Yang, Kai Chen, Yonghao Long, Qi Dou
- **🏫 单位**：The Chinese University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2405.00956.md)] [[arXiv:2405.00956](https://arxiv.org/abs/2405.00956)] [Code]
- **📝 说明**：✏️

#### [209] HoloGS: Instant Depth-based 3D Gaussian Splatting with Microsoft HoloLens 2
- **🧑‍🔬 作者**：Miriam Jäger, Theodor Kapler, Michael Feßenbecker, Felix Birkelbach, Markus Hillemann, Boris Jutzi
- **🏫 单位**：Institute of Photogrammetry and Remote Sensing (IPF), Karlsruhe Institute of Technology (KIT)
- **🔗 链接**：[[中英摘要](./abs/2405.02005.md)] [[arXiv:2405.02005](https://arxiv.org/abs/2405.02005)] [Code]
- **📝 说明**：✏️

#### [210] DreamScene4D: Dynamic Multi-Object Scene Generation from Monocular Videos
- **🧑‍🔬 作者**：Wen-Hsuan Chu, Lei Ke, Katerina Fragkiadaki
- **🏫 单位**：Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2405.02280.md)] [[arXiv:2405.02280](https://arxiv.org/abs/2405.02280)] [[Code](https://github.com/dreamscene4d/dreamscene4d)]
- **📝 说明**：✏️

#### [211] A Construct-Optimize Approach to Sparse View Synthesis without Camera Pose
- **🧑‍🔬 作者**：Kaiwen Jiang, Yang Fu, Mukund Varma T, Yash Belhe, Xiaolong Wang, Hao Su, Ravi Ramamoorthi
- **🏫 单位**：University of California
- **🔗 链接**：[[中英摘要](./abs/2405.03659.md)] [[arXiv:2405.03659](https://arxiv.org/abs/2405.03659)] [Code]
- **📝 说明**：✏️

#### [212] Splat-MOVER: Multi-Stage, Open-Vocabulary Robotic Manipulation via Editable Gaussian Splatting
- **🧑‍🔬 作者**：Ola Shorinwa, Johnathan Tucker, Aliyah Smith, Aiden Swann, Timothy Chen, Roya Firoozi, Monroe Kennedy III, Mac Schwager
- **🏫 单位**：Stanford University
- **🔗 链接**：[[中英摘要](./abs/2405.04378.md)] [[arXiv:2405.04378](https://arxiv.org/abs/2405.04378)] [Code]
- **📝 说明**：✏️

#### [213] GDGS: Gradient Domain Gaussian Splatting for Sparse Representation of Radiance Fields
- **🧑‍🔬 作者**：Yuanhao Gong
- **🏫 单位**：Electronics and Information Engineering, Shenzhen University, China
- **🔗 链接**：[[中英摘要](./abs/2405.05446.md)] [[arXiv:2405.05446](https://arxiv.org/abs/2405.05446)] [Code]
- **📝 说明**：✏️

#### [214] NGM-SLAM: Gaussian Splatting SLAM with Radiance Field Submap
- **🧑‍🔬 作者**：Mingrui Li, Jingwei Huang, Lei Sun, Aaron Xuxiang Tian, Tianchen Deng, Hongyu Wang
- **🏫 单位**：Dalian University of Technology ⟐ University of Electronic Science and Technology of China ⟐ University of Pennsylvania
- **🔗 链接**：[[中英摘要](./abs/2405.05702.md)] [[arXiv:2405.05702](https://arxiv.org/abs/2405.05702)] [Code]
- **📝 说明**：✏️

#### [215] DragGaussian: Enabling Drag-style Manipulation on 3D Gaussian Representation
- **🧑‍🔬 作者**：Sitian Shen, Jing Xu, Yuheng Yuan, Xingyi Yang, Qiuhong Shen, Xinchao Wang
- **🏫 单位**：Beijing Institute of Technology
- **🔗 链接**：[[中英摘要](./abs/2405.05800.md)] [[arXiv:2405.05800](https://arxiv.org/abs/2405.05800)] [Code]
- **📝 说明**：✏️

#### [216] I3DGS: Improve 3D Gaussian Splatting from Multiple Dimension
- **🧑‍🔬 作者**：Jinwei Lin
- **🏫 单位**：Monash University, Clayton Victoria, Australia
- **🔗 链接**：[[中英摘要](./abs/2405.06408.md)] [[arXiv:2405.06408](https://arxiv.org/abs/2405.06408)] [Code]
- **📝 说明**：✏️

#### [217] OneTo3D: One Image to Re-editable Dynamic 3D Model and Video Generation
- **🧑‍🔬 作者**：Jinwei Lin
- **🏫 单位**：Monash University, Clayton Victoria, Australia
- **🔗 链接**：[[中英摘要](./abs/2405.06547.md)] [[arXiv:2405.06547](https://arxiv.org/abs/2405.06547)] [[Code](https://github.com/lin-jinwei/OneTo3D)]
- **📝 说明**：✏️

#### [218] Direct Learning of Mesh and Appearance via 3D Gaussian Splatting
- **🧑‍🔬 作者**：Ancheng Lin, Jun Li
- **🏫 单位**：School of Computer Science, Australian Artificial Intelligence Institute (AAII) ⟐  University of Technology Sydney, Sydney, NSW 2007, Australia
- **🔗 链接**：[[中英摘要](./abs/2405.06945.md)] [[arXiv:2405.06945](https://arxiv.org/abs/2405.06945)] [Code]
- **📝 说明**：✏️

#### [219] GaussianVTON: 3D Human Virtual Try-ON via Multi-Stage Gaussian Splatting Editing with Image Prompting
- **🧑‍🔬 作者**：Haodong Chen, Yongle Huang, Haojian Huang, Xiangsheng Ge, Dian Shao
- **🏫 单位**：Northwestern Polytechnical University ⟐  The University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2405.07472.md)] [[arXiv:2405.07472](https://arxiv.org/abs/2405.07472)] [Code]
- **📝 说明**：✏️

#### [220] GS-Planner: A Gaussian-Splatting-based Planning Framework for Active High-Fidelity Reconstruction
- **🧑‍🔬 作者**：Rui Jin, Yuman Gao, Haojian Lu, Fei Gao
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2405.10142.md)] [[arXiv:2405.10142](https://arxiv.org/abs/2405.10142)] [Code]
- **📝 说明**：✏️

#### [221] Photorealistic 3D Urban Scene Reconstruction and Point Cloud Extraction using Google Earth Imagery and Gaussian Splatting
- **🧑‍🔬 作者**：Kyle Gao, Dening Lu, Hongjie He, Linlin Xu, Jonathan Li
- **🏫 单位**：Department of Systems Design Engineering, University of Waterloo
- **🔗 链接**：[[中英摘要](./abs/2405.11021.md)] [[arXiv:2405.11021](https://arxiv.org/abs/2405.11021)] [Code]
- **📝 说明**：

#### [222] MotionGS : Compact Gaussian Splatting SLAM by Motion Filter
- **🧑‍🔬 作者**：Xinli Guo, Peng Han, Weidong Zhang, Hongtian Chen
- **🏫 单位**：Shang Hai Jiao Tong University, China
- **🔗 链接**：[[中英摘要](./abs/2405.11129.md)] [[arXiv:2405.11129](https://arxiv.org/abs/2405.11129)] [Code]
- **📝 说明**：

#### [223] MirrorGaussian: Reflecting 3D Gaussians for Reconstructing Mirror Reflections
- **🧑‍🔬 作者**：Jiayue Liu, Xiao Tang, Freeman Cheng, Roy Yang, Zhihao Li, Jianzhuang Liu, Yi Huang, Jiaqi Lin, Shiyong Liu, Xiaofei Wu, Songcen Xu, Chun Yuan
- **🏫 单位**：Tsinghua University ⟐ Huawei Noah’s Ark Lab ⟐ University of Toronto ⟐ University of Chinese Academy of Sciences
- **🔗 链接**：[[中英摘要](./abs/2405.11921.md)] [[arXiv:2405.11921](https://arxiv.org/abs/2405.11921)] [Code]
- **📝 说明**：

#### [224] GGAvatar: Geometric Adjustment of Gaussian Head Avatar
- **🧑‍🔬 作者**：Xinyang Li, Jiaxin Wang, Yixin Xuan, Gongxin Yao, Yu Pan
- **🏫 单位**：Zhejiang University ⟐ Hangzhou Dianzi University
- **🔗 链接**：[[中英摘要](./abs/2405.11993.md)] [[arXiv:2405.11993](https://arxiv.org/abs/2405.11993)] [Code]
- **📝 说明**：

#### [225] Gaussian Head & Shoulders: High Fidelity Neural Upper Body Avatars with Anchor Gaussian Guided Texture Warping
- **🧑‍🔬 作者**：Tianhao Wu, Jing Yang, Zhilin Guo, Jingyi Wan, Fangcheng Zhong, Cengiz Oztireli
- **🏫 单位**：University of Cambridge, United Kingdom
- **🔗 链接**：[[中英摘要](./abs/2405.12069.md)] [[arXiv:2405.12069](https://arxiv.org/abs/2405.12069)] [Code]
- **📝 说明**：

#### [226] CoR-GS: Sparse-View 3D Gaussian Splatting via Co-Regularization
- **🧑‍🔬 作者**：Jiawei Zhang, Jiahe Li, Xiaohan Yu, Lei Huang, Lin Gu, Jin Zheng, Xiao Bai
- **🏫 单位**：Beihang University ⟐  Macquarie University ⟐ RIKEN AIP ⟐ The University of Tokyo
- **🔗 链接**：[[中英摘要](./abs/2405.12110.md)] [[arXiv:2405.12110](https://arxiv.org/abs/2405.12110)] [Code]
- **📝 说明**：

#### [227] Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo
- **🧑‍🔬 作者**：Tianqi Liu, Guangcong Wang, Shoukang Hu, Liao Shen, Xinyi Ye, Yuhang Zang, Zhiguo Cao, Wei Li, Ziwei Liu
- **🏫 单位**：Huazhong University of Science and Technology ⟐  Nanyang Technological University ⟐  Great Bay University ⟐ Shanghai AI Laboratory
- **🔗 链接**：[[中英摘要](./abs/2405.12218.md)] [[arXiv:2405.12218](https://arxiv.org/abs/2405.12218)] [[Code](https://github.com/TQTQliu/MVSGaussian)]
- **📝 说明**：

#### [228] AtomGS: Atomizing Gaussian Splatting for High-Fidelity Radiance Field
- **🧑‍🔬 作者**：Rong Liu, Rui Xu, Yue Hu, Meida Chen, Andrew Feng
- **🏫 单位**：University of Southern California
- **🔗 链接**：[[中英摘要](./abs/2405.12369.md)] [[arXiv:2405.12369](https://arxiv.org/abs/2405.12369)] [[Code](https://github.com/RongLiu-Leo/AtomGS)]
- **📝 说明**：

#### [229] GarmentDreamer: 3DGS Guided Garment Synthesis with Diverse Geometry and Texture Details
- **🧑‍🔬 作者**：Boqian Li, Xuan Li, Ying Jiang, Tianyi Xie, Feng Gao, Huamin Wang, Yin Yang, Chenfanfu Jiang
- **🏫 单位**：UCLA ⟐ Utah ⟐ HKU ⟐ Amazon ⟐ Style3D Research
- **🔗 链接**：[[中英摘要](./abs/2405.12420.md)] [[arXiv:2405.12420](https://arxiv.org/abs/2405.12420)] [Code]
- **📝 说明**：

#### [230] Gaussian Control with Hierarchical Semantic Graphs in 3D Human Recovery
- **🧑‍🔬 作者**：Hongsheng Wang, Weiyue Zhang, Sihao Liu, Xinrui Zhou, Shengyu Zhang, Fei Wu, Feng Lin
- **🏫 单位**：Zhejiang University ⟐ Zhejiang Lab, China
- **🔗 链接**：[[中英摘要](./abs/2405.12477.md)] [[arXiv:2405.12477](https://arxiv.org/abs/2405.12477)] [[Code](https://github.com/3DHumanRehab/SemanticGraph-Gaussian)]
- **📝 说明**：

#### [231] LAGA: Layered 3D Avatar Generation and Customization via Gaussian Splatting
- **🧑‍🔬 作者**：Jia Gong, Shenyu Ji, Lin Geng Foo, Kang Chen, Hossein Rahmani, Jun Liu
- **🏫 单位**：Singapore University of Technology and Design ⟐ Netease ⟐ Lancaster University
- **🔗 链接**：[[中英摘要](./abs/2405.12663.md)] [[arXiv:2405.12663](https://arxiv.org/abs/2405.12663)] [[Code](https://github.com/richzhang/webpage-template)]
- **📝 说明**：

#### [232] MOSS: Motion-based 3D Clothed Human Synthesis from Monocular Video
- **🧑‍🔬 作者**：Hongsheng Wang, Xiang Cai, Xi Sun, Jinhong Yue, Shengyu Zhang, Feng Lin, Fei Wu
- **🏫 单位**：Zhejiang University ⟐ Zhejiang Lab, China
- **🔗 链接**：[[中英摘要](./abs/2405.12806.md)] [[arXiv:2405.12806](https://arxiv.org/abs/2405.12806)] [[Code](https://github.com/3DHumanRehab/MOSS)]
- **📝 说明**：

#### [233] Gaussian Time Machine: A Real-Time Rendering Methodology for Time-Variant Appearances
- **🧑‍🔬 作者**：Licheng Shen, Ho Ngai Chow, Lingyun Wang, Tong Zhang, Mengqiu Wang, Yuxing Han
- **🏫 单位**：Tsinghua Shenzhen International Graduate School, Tsinghua University ⟐ Zero-Zero Lab ⟐ Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2405.13694.md)] [[arXiv:2405.13694](https://arxiv.org/abs/2405.13694)] [Code]
- **📝 说明**：

#### [234] Monocular Gaussian SLAM with Language Extended Loop Closure
- **🧑‍🔬 作者**：Tian Lan, Qinwei Lin, Haoqian Wang
- **🏫 单位**：Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2405.13748.md)] [[arXiv:2405.13748](https://arxiv.org/abs/2405.13748)] [Code]
- **📝 说明**：

#### [235] DoGaussian: Distributed-Oriented Gaussian Splatting for Large-Scale 3D Reconstruction Via Gaussian Consensus
- **🧑‍🔬 作者**：Yu Chen, Gim Hee Lee
- **🏫 单位**：National University of Singapore
- **🔗 链接**：[[中英摘要](./abs/2405.13943.md)] [[arXiv:2405.13943](https://arxiv.org/abs/2405.13943)] [[Code](https://github.com/aibluefisher/DoGaussian)]
- **📝 说明**：

#### [236] NeuroGauss4D-PCI: 4D Neural Fields and Gaussian Deformation Fields for Point Cloud Interpolation
- **🧑‍🔬 作者**：Chaokang Jiang, Dalong Du, Jiuming Liu, Siting Zhu, Zhenqiang Liu, Zhuang Ma, Zhujin Liang, Jie Zhou
- **🏫 单位**：PhiGent Robotics ⟐ Shanghai Jiaotong University ⟐ Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2405.14241.md)] [[arXiv:2405.14241](https://arxiv.org/abs/2405.14241)] [[Code](https://github.com/jiangchaokang/NeuroGauss4D-PCI)]
- **📝 说明**：

#### [237] D-MiSo: Editing Dynamic 3D Scenes using Multi-Gaussians Soup
- **🧑‍🔬 作者**：Joanna Waczyńska, Piotr Borycki, Joanna Kaleta, Sławomir Tadeja, Przemysław Spurek
- **🏫 单位**：Jagiellonian University ⟐ Warsaw University of Technology ⟐ University of Cambridge
- **🔗 链接**：[[中英摘要](./abs/2405.14276.md)] [[arXiv:2405.14276](https://arxiv.org/abs/2405.14276)] [Code]
- **📝 说明**：

#### [238] RoGS: Large Scale Road Surface Reconstruction based on 2D Gaussian Splatting
- **🧑‍🔬 作者**：Zhiheng Feng, Wenhua Wu, Hesheng Wang
- **🏫 单位**：Shanghai Jiao Tong University
- **🔗 链接**：[[中英摘要](./abs/2405.14342.md)] [[arXiv:2405.14342](https://arxiv.org/abs/2405.14342)] [Code]
- **📝 说明**：

#### [239] TIGER: Text-Instructed 3D Gaussian Retrieval and Coherent Editing
- **🧑‍🔬 作者**：Teng Xu, Jiamin Chen, Peng Chen, Youjia Zhang, Junqing Yu, Wei Yang
- **🏫 单位**：Huazhong University of Science and Technology
- **🔗 链接**：[[中英摘要](./abs/2405.14455.md)] [[arXiv:2405.14455](https://arxiv.org/abs/2405.14455)] [Code]
- **📝 说明**：

#### [240] MagicDrive3D: Controllable 3D Generation for Any-View Rendering in Street Scenes
- **🧑‍🔬 作者**：Ruiyuan Gao, Kai Chen, Zhihao Li, Lanqing Hong, Zhenguo Li, Qiang Xu
- **🏫 单位**：The Chinese University of Hong Kong ⟐ Hong Kong University of Science and Technology ⟐ Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2405.14475.md)] [[arXiv:2405.14475](https://arxiv.org/abs/2405.14475)] [Code]
- **📝 说明**：

#### [241] GS-Hider: Hiding Messages into 3D Gaussian Splatting
- **🧑‍🔬 作者**：Xuanyu Zhang, Jiarui Meng, Runyi Li, Zhipei Xu, Yongbing Zhang, Jian Zhang
- **🏫 单位**：Peking University ⟐ Harbin Institute of Technology (Shenzhen)
- **🔗 链接**：[[中英摘要](./abs/2405.15118.md)] [[arXiv:2405.15118](https://arxiv.org/abs/2405.15118)] [Code]
- **📝 说明**：

#### [242] HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed via Gaussian Splatting
- **🧑‍🔬 作者**：Yuanhao Cai, Zihao Xiao, Yixun Liang, Yulun Zhang, Xiaokang Yang, Yaoyao Liu, Alan Yuille
- **🏫 单位**：Johns Hopkins University ⟐ HKUST (GZ) ⟐ Tsinghua University ⟐ Shanghai Jiao Tong University
- **🔗 链接**：[[中英摘要](./abs/2405.15125.md)] [[arXiv:2405.15125](https://arxiv.org/abs/2405.15125)] [[Code](https://github.com/caiyuanhao1998/HDR-GS)]
- **📝 说明**：

#### [243] DisC-GS: Discontinuity-aware Gaussian Splatting
- **🧑‍🔬 作者**：Haoxuan Qu, Zhuoling Li, Hossein Rahmani, Yujun Cai, Jun Liu
- **🏫 单位**：Singapore University of Technology and Design ⟐ Central South University ⟐ Lancaster University ⟐ Nanyang Technological University
- **🔗 链接**：[[中英摘要](./abs/2405.15196.md)] [[arXiv:2405.15196](https://arxiv.org/abs/2405.15196)] [Code]
- **📝 说明**：

#### [244] GSDeformer: Direct Cage-based Deformation for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Jiajun Huang, Hongchuan Yu
- **🏫 单位**：Bournemouth University
- **🔗 链接**：[[中英摘要](./abs/2405.15491.md)] [[arXiv:2405.15491](https://arxiv.org/abs/2405.15491)] [Code]
- **📝 说明**：

#### [245] Feature Splatting for Better Novel View Synthesis with Low Overlap
- **🧑‍🔬 作者**：T. Berriel Martins, Javier Civera
- **🏫 单位**：University of Zaragoza
- **🔗 链接**：[[中英摘要](./abs/2405.15518.md)] [[arXiv:2405.15518](https://arxiv.org/abs/2405.15518)] [Code]
- **📝 说明**：

#### [246] Sp2360: Sparse-view 360 Scene Reconstruction using Cascaded 2D Diffusion Priors
- **🧑‍🔬 作者**：Soumava Paul, Christopher Wewer, Bernt Schiele, Jan Eric Lenssen
- **🏫 单位**：Max Planck Institute for Informatics ⟐ Saarland University
- **🔗 链接**：[[中英摘要](./abs/2405.16517.md)] [[arXiv:2405.16517](https://arxiv.org/abs/2405.16517)] [Code]
- **📝 说明**：

#### [247] Splat-SLAM: Globally Optimized RGB-only SLAM with 3D Gaussians
- **🧑‍🔬 作者**：Erik Sandström, Keisuke Tateno, Michael Oechsle, Michael Niemeyer, Luc Van Gool, Martin R. Oswald, Federico Tombari
- **🏫 单位**：Google ⟐ ETH Zürich ⟐ INSAIT ⟐ University of Amsterdam ⟐ TU München
- **🔗 链接**：[[中英摘要](./abs/2405.16544.md)] [[arXiv:2405.16544](https://arxiv.org/abs/2405.16544)] [[Code](https://github.com/eriksandstroem/Splat-SLAM)]
- **📝 说明**：

#### [248] PyGS: Large-scale Scene Representation with Pyramidal 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zipeng Wang, Dan Xu
- **🏫 单位**：HKUST
- **🔗 链接**：[[中英摘要](./abs/2405.16829.md)] [[arXiv:2405.16829](https://arxiv.org/abs/2405.16829)] [Code]
- **📝 说明**：

#### [249] Sync4D: Video Guided Controllable Dynamics for Physics-Based 4D Generation
- **🧑‍🔬 作者**：Zhoujie Fu, Jiacheng Wei, Wenhao Shen, Chaoyue Song, Xiaofeng Yang, Fayao Liu, Xulei Yang, Guosheng Lin
- **🏫 单位**：Nanyang Technological University ⟐ A*STAR
- **🔗 链接**：[[中英摘要](./abs/2405.16849.md)] [[arXiv:2405.16849](https://arxiv.org/abs/2405.16849)] [Code]
- **📝 说明**：

#### [250] SA-GS: Semantic-Aware Gaussian Splatting for Large Scene Reconstruction with Geometry Constrain
- **🧑‍🔬 作者**：Butian Xiong, Xiaoyu Ye, Tze Ho Elden Tse, Kai Han, Shuguang Cui, Zhen Li
- **🏫 单位**：CUHK, Shenzhen ⟐ Beijing Institute of Technology ⟐ Auki Labs ⟐ The University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2405.16923.md)] [[arXiv:2405.16923](https://arxiv.org/abs/2405.16923)] [Code]
- **📝 说明**：

#### [251] F-3DGS: Factorized Coordinates and Representations for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Xiangyu Sun, Joo Chan Lee, Daniel Rho, Jong Hwan Ko, Usman Ali, Eunbyung Park
- **🏫 单位**：Sungkyunkwan University ⟐ KT
- **🔗 链接**：[[中英摘要](./abs/2405.17083.md)] [[arXiv:2405.17083](https://arxiv.org/abs/2405.17083)] [[Code](https://github.com/Xiangyu1Sun/Factorize-3DGS)]
- **📝 说明**：

#### [252] Memorize What Matters: Emergent Scene Decomposition from Multitraverse
- **🧑‍🔬 作者**：Yiming Li, Zehong Wang, Yue Wang, Zhiding Yu, Zan Gojcic, Marco Pavone, Chen Feng, Jose M. Alvarez
- **🏫 单位**：NYU ⟐ NVIDIA ⟐ USC ⟐ Stanford University
- **🔗 链接**：[[中英摘要](./abs/2405.17187.md)] [[arXiv:2405.17187](https://arxiv.org/abs/2405.17187)] [Code]
- **📝 说明**：

#### [253] DOF-GS: Adjustable Depth-of-Field 3D Gaussian Splatting for Refocusing,Defocus Rendering and Blur Removal
- **🧑‍🔬 作者**：Yujie Wang, Praneeth Chakravarthula, Baoquan Chen
- **🏫 单位**：National Key Lab of General AI, China ⟐ Peking University ⟐ University of North Carolina at Chapel Hill
- **🔗 链接**：[[中英摘要](./abs/2405.17351.md)] [[arXiv:2405.17351](https://arxiv.org/abs/2405.17351)] [Code]
- **📝 说明**：

#### [254] GaussianFormer: Scene as Gaussians for Vision-Based 3D Semantic Occupancy Prediction
- **🧑‍🔬 作者**：Yuanhui Huang, Wenzhao Zheng, Yunpeng Zhang, Jie Zhou, Jiwen Lu
- **🏫 单位**：Tsinghua University ⟐ University of California, Berkeley ⟐ PhiGent Robotics
- **🔗 链接**：[[中英摘要](./abs/2405.17429.md)] [[arXiv:2405.17429](https://arxiv.org/abs/2405.17429)] [[Code](https://github.com/huang-yh/GaussianFormer)]
- **📝 说明**：
