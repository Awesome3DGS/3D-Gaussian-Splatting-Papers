# 3D Gaussian Splatting Papers

[![更新日志](https://img.shields.io/badge/💡-更新日志-informational.svg?style=flat)](Changelog.md)
[![发现错误](https://img.shields.io/badge/🐛-发现错误-yellow.svg?style=flat)](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/issues)
[![提交修改](https://img.shields.io/badge/👐-提交修改-brightgreen.svg?style=flat)](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/pulls)


**⚡ 快捷链接**: [[10](#10-animatable-3d-gaussians-for-high-fidelity-synthesis-of-human-motions)]
                 [[20](#20-md-splatting-learning-metric-deformation-from-4d-gaussians-in-highly-deformable-scenes)]
                 [[30](#30-gir-3d-gaussian-inverse-rendering-for-relightable-scene-factorization)]
                 [[40](#40-human101-training-100fps-human-gaussians-in-100s-from-1-view)]
                 [[50](#50-characterizing-satellite-geometry-via-accelerated-3d-gaussian-splatting)]
                 [[60](#60-liv-gaussmap-lidar-inertial-visual-fusion-for-real-time-3d-radiance-field-map-rendering)]
                 [[70](#70-4d-gaussian-splatting-towards-efficient-novel-view-synthesis-for-dynamic-scenes)]
                 [[80](#80-identifying-unnecessary-3d-gaussians-using-clustering-for-fast-rendering-of-3d-gaussian-splatting)]（最新）


**📚 会议期刊**: [[ICLR2024](./ICLR2024.md)] (2 篇)
                 [[CVPR2024](./CVPR2024.md)] (59 篇)

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

---

#### [0] 3D Gaussian Splatting for Real-Time Radiance Field Rendering
- **🧑‍🔬 作者**：Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis
- **🏫 单位**：Université Côte d’Azurl ⟐ Max-Planck-Institut für Informatik
- **🔗 链接**：[[中英摘要](./abs/2308.04079.md)] [[arXiv:2308.04079](https://arxiv.org/abs/2308.04079)] [[ACM TOG](https://dl.acm.org/doi/10.1145/3592433)] [[Code](https://github.com/graphdeco-inria/gaussian-splatting)]
- **📝 说明**：🚀 开山之作，必读；🏆 SIGGRAPH 2023 Best Paper

#### [1] Dynamic 3d gaussians: Tracking by persistent dynamic view synthesis
- **🧑‍🔬 作者**：Jonathon Luiten, Georgios Kopanas, Bastian Leibe, Deva Ramanan
- **🏫 单位**：Carnegie Mellon University ⟐ RWTH Aachen University ⟐ Inria & Universite C´ ote d’Azur
- **🔗 链接**：[[中英摘要](./abs/2308.09713.md)] [[arXiv:2308.09713](https://arxiv.org/abs/2308.09713)] [[Code](https://github.com/JonathonLuiten/Dynamic3DGaussians)]
- **📝 说明**：🏆 Accepted to 3DV 2024

#### [2] Flexible Techniques for Differentiable Rendering with 3D Gaussians
- **🧑‍🔬 作者**：Leonid Keselman, Martial Hebert
- **🏫 单位**：Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2308.14737.md)] [[arXiv:2308.14737](https://arxiv.org/abs/2308.14737)] [[Code](https://github.com/leonidk/fmb-plus)]
- **📝 说明**：✏️

#### [3] Dynamic Gaussian Splatting from Markerless Motion Capture can Reconstruct Infants Movements
- **🧑‍🔬 作者**：R. James Cotton, Colleen Peyton
- **🏫 单位**：Shirley Ryan AbilityLab ⟐ Northwestern University
- **🔗 链接**：[[中英摘要](./abs/2310.19441.md)] [[arXiv:2310.19441](https://arxiv.org/abs/2310.19441)] [Code]
- **📝 说明**：🏆 Accepted to WACV 2024 Workshop

#### [4] Drivable 3D Gaussian Avatars
- **🧑‍🔬 作者**：Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito, Michael Zollhöfer, Justus Thies, Javier Romero
- **🏫 单位**：Meta Reality Labs Research ⟐ Technical University of Darmstadt ⟐ Max Planck Institute for Intelligent Systems
- **🔗 链接**：[[中英摘要](./abs/2311.08581.md)] [[arXiv:2311.08581](https://arxiv.org/abs/2311.08581)] [Code]
- **📝 说明**：✏️

#### [5] SplatArmor: Articulated Gaussian splatting for animatable humans from monocular RGB videos
- **🧑‍🔬 作者**：Rohit Jena, Ganesh Subramanian Iyer, Siddharth Choudhary, Brandon Smith, Pratik Chaudhari, James Gee
- **🏫 单位**：University of Pennsylvania ⟐ Amazon.com, Inc.
- **🔗 链接**：[[中英摘要](./abs/2311.10812.md)] [[arXiv:2311.10812](https://arxiv.org/abs/2311.10812)] [[Code](https://github.com/rohitrango/splatarmor)]
- **📝 说明**：✏️

#### [6] GaussianDiffusion: 3D Gaussian Splatting for Denoising Diffusion Probabilistic Models with Structured Noise
- **🧑‍🔬 作者**：Xinhai Li, Huaibin Wang, Kuo-Kun Tseng
- **🏫 单位**：Harbin Institute of Technology (Shenzhen)
- **🔗 链接**：[[中英摘要](./abs/2311.11221.md)] [[arXiv:2311.11221](https://arxiv.org/abs/2311.11221)] [Code]
- **📝 说明**：✏️


#### [7] An Efficient 3D Gaussian Representation for Monocular/Multi-view Dynamic Scenes
- **🧑‍🔬 作者**：Kai Katsumata, Duc Minh Vo, Hideki Nakayama
- **🏫 单位**：The University of Tokyo
- **🔗 链接**：[[中英摘要](./abs/2311.12897.md)] [[arXiv:2311.12897](https://arxiv.org/abs/2311.12897)] [[Code](https://github.com/raven38/EfficientDynamic3DGaussian)]
- **📝 说明**：✏️

#### [8] LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes
- **🧑‍🔬 作者**：Jaeyoung Chung, Suyoung Lee, Hyeongjin Nam, Jaerin Lee, Kyoung Mu Lee
- **🏫 单位**：Seoul National University
- **🔗 链接**：[[中英摘要](./abs/2311.13384.md)] [[arXiv:2311.13384](https://arxiv.org/abs/2311.13384)] [[Code](https://github.com/luciddreamer-cvlab/LucidDreamer)]
- **📝 说明**：✏️

#### [9] Depth-Regularized Optimization for 3D Gaussian Splatting in Few-Shot Images
- **🧑‍🔬 作者**：Jaeyoung Chung, Jeongtaek Oh, Kyoung Mu Lee
- **🏫 单位**：Seoul National University
- **🔗 链接**：[[中英摘要](./abs/2311.13398.md)] [[arXiv:2311.13398](https://arxiv.org/abs/2311.13398)] [[Code](https://github.com/robot0321/DepthRegularizedGS)]
- **📝 说明**：Empty code repo

#### [10] Animatable 3D Gaussians for High-fidelity Synthesis of Human Motions
- **🧑‍🔬 作者**：Keyang Ye, Tianjia Shao, Kun Zhou
- **🏫 单位**：Unknown
- **🔗 链接**：[[中英摘要](./abs/2311.13404.md)] [[arXiv:2311.13404](https://arxiv.org/abs/2311.13404)] [Code]
- **📝 说明**：✏️ This paper has been withdrawn by Keyang Ye

#### [11] Relightable 3D Gaussian: Real-time Point Cloud Relighting with BRDF Decomposition and Ray Tracing
- **🧑‍🔬 作者**：Jian Gao, Chun Gu, Youtian Lin, Hao Zhu, Xun Cao, Li Zhang, Yao Yao
- **🏫 单位**：Nanjing University ⟐ Fudan University
- **🔗 链接**：[[中英摘要](./abs/2311.16043.md)] [[arXiv:2311.16043](https://arxiv.org/abs/2311.16043)] [[Code](https://github.com/NJU-3DV/Relightable3DGaussian)]
- **📝 说明**：✏️

#### [12] Animatable 3D Gaussian: Fast and High-Quality Reconstruction of Multiple Human Avatars
- **🧑‍🔬 作者**：Yang Liu, Xiang Huang, Minghan Qin, Qinwei Lin, Haoqian Wang
- **🏫 单位**： Tsinghua University ⟐ Gala Sports
- **🔗 链接**：[[中英摘要](./abs/2311.16482.md)] [[arXiv:2311.16482](https://arxiv.org/abs/2311.16482)] [[Code](https://github.com/jimmyYliu/Animatable-3D-Gaussian)]
- **📝 说明**：✏️


#### [13] LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and 200+ FPS
- **🧑‍🔬 作者**：Zhiwen Fan, Kevin Wang, Kairun Wen, Zehao Zhu, Dejia Xu, Zhangyang Wang
- **🏫 单位**：University of Texas at Austin ⟐ Xiamen University
- **🔗 链接**：[[中英摘要](./abs/2311.17245.md)] [[arXiv:2311.17245](https://arxiv.org/abs/2311.17245)] [[Code](https://github.com/VITA-Group/LightGaussian)]
- **📝 说明**：✏️

#### [14] CG3D: Compositional Generation for Text-to-3D via Gaussian Splatting
- **🧑‍🔬 作者**：Alexander Vilesov, Pradyumna Chari, Achuta Kadambi
- **🏫 单位**：University of California, Los Angeles
- **🔗 链接**：[[中英摘要](./abs/2311.17907.md)] [[arXiv:2311.17907](https://arxiv.org/abs/2311.17907)] [Code]
- **📝 说明**：✏️

#### [15] Compact3D: Compressing Gaussian Splat Radiance Field Models with Vector Quantization
- **🧑‍🔬 作者**：KL Navaneet, Kossar Pourahmadi Meibodi, Soroush Abbasi Koohpayegani, Hamed Pirsiavash
- **🏫 单位**：University of California, Davis
- **🔗 链接**：[[中英摘要](./abs/2311.18159.md)] [[arXiv:2311.18159](https://arxiv.org/abs/2311.18159)] [[Code](https://github.com/UCDvision/compact3d)]
- **📝 说明**：✏️

#### [16] Periodic Vibration Gaussian: Dynamic Urban Scene Reconstruction and Real-time Rendering
- **🧑‍🔬 作者**：Yurui Chen, Chun Gu, Junzhe Jiang, Xiatian Zhu, Li Zhang
- **🏫 单位**：Fudan University ⟐ University of Surrey
- **🔗 链接**：[[中英摘要](./abs/2311.18561.md)] [[arXiv:2311.18561](https://arxiv.org/abs/2311.18561)] [[Code](https://github.com/fudan-zvg/PVG)]
- **📝 说明**：✏

#### [17] DynMF: Neural Motion Factorization for Real-time Dynamic View Synthesis with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Agelos Kratimenos, Jiahui Lei, Kostas Daniilidis
- **🏫 单位**：University of Pennsylvania
- **🔗 链接**：[[中英摘要](./abs/2312.00112.md)] [[arXiv:2312.00112](https://arxiv.org/abs/2312.00112)] [[Code](https://github.com/agelosk/dynmf)]
- **📝 说明**：✏️

#### [18] SparseGS: Real-Time 360° Sparse View Synthesis using Gaussian Splatting
- **🧑‍🔬 作者**：Haolin Xiong, Sairisheek Muttukuru, Rishi Upadhyay, Pradyumna Chari, Achuta Kadambi
- **🏫 单位**：University of California, Los Angeles
- **🔗 链接**：[[中英摘要](./abs/2312.00206.md)] [[arXiv:2312.00206](https://arxiv.org/abs/2312.00206)] [Code]
- **📝 说明**：✏️

#### [19] FSGS: Real-Time Few-shot View Synthesis using Gaussian Splatting
- **🧑‍🔬 作者**：Zehao Zhu, Zhiwen Fan, Yifan Jiang, Zhangyang Wang
- **🏫 单位**：University of Texas at Austin
- **🔗 链接**：[[中英摘要](./abs/2312.00451.md)] [[arXiv:2312.00451](https://arxiv.org/abs/2312.00451)] [[Code](https://github.com/VITA-Group/FSGS)]
- **📝 说明**：✏️

#### [20] MD-Splatting: Learning Metric Deformation from 4D Gaussians in Highly Deformable Scenes
- **🧑‍🔬 作者**：Bardienus P. Duisterhof, Zhao Mandi, Yunchao Yao, Jia-Wei Liu, Mike Zheng Shou, Shuran Song, Jeffrey Ichnowski
- **🏫 单位**：National University of Singapore ⟐ Stanford University ⟐ Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2312.00583.md)] [[arXiv:2312.00583](https://arxiv.org/abs/2312.00583)] [[Code](https://github.com/momentum-robotics-lab/md-splatting)]
- **📝 说明**：✏️

#### [21] Gaussian Grouping: Segment and Edit Anything in 3D Scenes
- **🧑‍🔬 作者**：Mingqiao Ye, Martin Danelljan, Fisher Yu, Lei Ke
- **🏫 单位**：ETH Zurich
- **🔗 链接**：[[中英摘要](./abs/2312.00732.md)] [[arXiv:2312.00732](https://arxiv.org/abs/2312.00732)] [[Code](https://github.com/lkeab/gaussian-grouping)]
- **📝 说明**：✏️

#### [22] NeuSG: Neural Implicit Surface Reconstruction with 3D Gaussian Splatting Guidance
- **🧑‍🔬 作者**：Hanlin Chen, Chen Li, Gim Hee Lee
- **🏫 单位**：National University of Singapore
- **🔗 链接**：[[中英摘要](./abs/2312.00846.md)] [[arXiv:2312.00846](https://arxiv.org/abs/2312.00846)] [Code]
- **📝 说明**：✏️

#### [23] Segment Any 3D Gaussians
- **🧑‍🔬 作者**：Jiazhong Cen, Jiemin Fang, Chen Yang, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian
- **🏫 单位**：Shanghai Jiao Tong University ⟐ Huawei Inc.
- **🔗 链接**：[[中英摘要](./abs/2312.00860.md)] [[arXiv:2312.00860](https://arxiv.org/abs/2312.00860)] [[Code](https://github.com/Jumpat/SegAnyGAussians)]
- **📝 说明**：✏️

#### [24] GaussianHead: Impressive 3D Gaussian-based Head Avatars with Dynamic Hybrid Neural Field
- **🧑‍🔬 作者**：Jie Wang, Xianyan Li, Jiucheng Xie, Feng Xu, Hao Gao
- **🏫 单位**：Nanjing University of Posts and Telecommunications ⟐ Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2312.01632.md)] [[arXiv:2312.01632](https://arxiv.org/abs/2312.01632)] [[Code](https://github.com/chiehwangs/gaussian-head)]
- **📝 说明**：✏️

#### [25] SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM
- **🧑‍🔬 作者**：Nikhil Keetha, Jay Karhade, Krishna Murthy Jatavallabhula, Gengshan Yang, Sebastian Scherer, Deva Ramanan, Jonathon Luiten
- **🏫 单位**：CMU ⟐ MIT
- **🔗 链接**：[[中英摘要](./abs/2312.02126.md)] [[arXiv:2312.02126](https://arxiv.org/abs/2312.02126)] [[Code](https://github.com/spla-tam/SplaTAM)]
- **📝 说明**：✏

#### [26] HeadGaS: Real-Time Animatable Head Avatars via 3D Gaussian Splatting
- **🧑‍🔬 作者**：Helisa Dhamo, Yinyu Nie, Arthur Moreau, Jifei Song, Richard Shaw, Yiren Zhou, Eduardo Pérez-Pellitero
- **🏫 单位**：Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2312.02902.md)] [[arXiv:2312.02902](https://arxiv.org/abs/2312.02902)] [Code]
- **📝 说明**：✏️

#### [27] MonoGaussianAvatar: Monocular Gaussian Point-based Head Avatar
- **🧑‍🔬 作者**：Yufan Chen, Lizhen Wang, Qijing Li, Hongjiang Xiao, Shengping Zhang, Hongxun Yao, Yebin Liu
- **🏫 单位**：Harbin Institute of Technology ⟐ Tsinghua University ⟐ Communication University of China
- **🔗 链接**：[[中英摘要](./abs/2312.04558.md)] [[arXiv:2312.04558](https://arxiv.org/abs/2312.04558)] [[Code](https://github.com/yufan1012/MonoGaussianAvatar)]
- **📝 说明**：✏️

#### [28] EAGLES: Efficient Accelerated 3D Gaussians with Lightweight EncodingS
- **🧑‍🔬 作者**：Sharath Girish, Kamal Gupta, Abhinav Shrivastava
- **🏫 单位**：University of Maryland
- **🔗 链接**：[[中英摘要](./abs/2312.04564.md)] [[arXiv:2312.04564](https://arxiv.org/abs/2312.04564)] [[Code](https://github.com/Sharath-girish/efficientgaussian)]
- **📝 说明**：✏️

#### [29] Learn to Optimize Denoising Scores for 3D Generation: A Unified and Improved Diffusion Prior on NeRF and 3D Gaussian Splatting
- **🧑‍🔬 作者**：Xiaofeng Yang, Yiwen Chen, Cheng Chen, Chi Zhang, Yi Xu, Xulei Yang, Fayao Liu, Guosheng Lin
- **🏫 单位**：Nanyang Technological University ⟐ OPPO US Research Center ⟐ A*STAR
- **🔗 链接**：[[中英摘要](./abs/2312.04820.md)] [[arXiv:2312.04820](https://arxiv.org/abs/2312.04820)] [Code]
- **📝 说明**：✏️

#### [30] GIR: 3D Gaussian Inverse Rendering for Relightable Scene Factorization
- **🧑‍🔬 作者**：Yahao Shi, Yanmin Wu, Chenming Wu, Xing Liu, Chen Zhao, Haocheng Feng, Jingtuo Liu, Liangjun Zhang, Jian Zhang, Bin Zhou, Errui Ding, Jingdong Wang
- **🏫 单位**：Beihang University ⟐ Peking University ⟐ Baidu VIS
- **🔗 链接**：[[中英摘要](./abs/2312.05133.md)] [[arXiv:2312.05133](https://arxiv.org/abs/2312.05133)] [Code]
- **📝 说明**：✏️

#### [31] iComMa: Inverting 3D Gaussians Splatting for Camera Pose Estimation via Comparing and Matching
- **🧑‍🔬 作者**：Yuan Sun, Xuan Wang, Yunfan Zhang, Jie Zhang, Caigui Jiang, Yu Guo, Fei Wang
- **🏫 单位**：Xi’an Jiaotong University ⟐ Ant Group
- **🔗 链接**：[[中英摘要](./abs/2312.09031.md)] [[arXiv:2312.09031](https://arxiv.org/abs/2312.09031)] [Code]
- **📝 说明**：✏️


#### [32] Text2Immersion: Generative Immersive Scene with 3D Gaussians
- **🧑‍🔬 作者**：Hao Ouyang, Kathryn Heal, Stephen Lombardi, Tiancheng Sun
- **🏫 单位**：HKUST ⟐ Google
- **🔗 链接**：[[中英摘要](./abs/2312.09242.md)] [[arXiv:2312.09242](https://arxiv.org/abs/2312.09242)] [Code]
- **📝 说明**：✏️

#### [33] Exploring the Feasibility of Generating Realistic 3D Models of Endangered Species Using DreamGaussian: An Analysis of Elevation Angle's Impact on Model Generation
- **🧑‍🔬 作者**：Selcuk Anil Karatopak, Deniz Sen
- **🏫 单位**：Huawei Türkiye R&D Center
- **🔗 链接**：[[中英摘要](./abs/2312.09682.md)] [[arXiv:2312.09682](https://arxiv.org/abs/2312.09682)] [Code]
- **📝 说明**：✏️

#### [34] GauFRe: Gaussian Deformation Fields for Real-time Dynamic Novel View Synthesis
- **🧑‍🔬 作者**：Yiqing Liang, Numair Khan, Zhengqin Li, Thu Nguyen-Phuoc, Douglas Lanman, James Tompkin, Lei Xiao
- **🏫 单位**：Meta ⟐ Brown University
- **🔗 链接**：[[中英摘要](./abs/2312.11458.md)] [[arXiv:2312.11458](https://arxiv.org/abs/2312.11458)] [[Supp](https://lynl7130.github.io/gaufre/static/pdfs/suppl.pdf)] [Code]
- **📝 说明**：✏️

#### [35] Repaint123: Fast and High-quality One Image to 3D Generation with Progressive Controllable 2D Repainting
- **🧑‍🔬 作者**：Junwu Zhang, Zhenyu Tang, Yatian Pang, Xinhua Cheng, Peng Jin, Yida Wei, Munan Ning, Li Yuan
- **🏫 单位**：Peking University ⟐ Pengcheng Laboratory ⟐  National University of Singapore ⟐ Wuhan University
- **🔗 链接**：[[中英摘要](./abs/2312.13271.md)] [[arXiv:2312.13271](https://arxiv.org/abs/2312.13271)] [[Code](https://github.com/PKU-YuanGroup/repaint123)]
- **📝 说明**：✏️

#### [36] Compact 3D Scene Representation via Self-Organizing Gaussian Grids
- **🧑‍🔬 作者**：Wieland Morgenstern, Florian Barthel, Anna Hilsmann, Peter Eisert
- **🏫 单位**：Fraunhofer Heinrich Hertz Institute ⟐ Humboldt University of Berlin
- **🔗 链接**：[[中英摘要](./abs/2312.13299.md)] [[arXiv:2312.13299](https://arxiv.org/abs/2312.13299)] [[Code](https://github.com/fraunhoferhhi/Self-Organizing-Gaussians)]
- **📝 说明**：✏️

#### [37] SWAGS: Sampling Windows Adaptively for Dynamic 3D Gaussian Splatting
- **🧑‍🔬 作者**：Richard Shaw, Jifei Song, Arthur Moreau, Michal Nazarczuk, Sibi Catley-Chandar, Helisa Dhamo, Eduardo Perez-Pellitero
- **🏫 单位**：Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2312.13308.md)] [[arXiv:2312.13308](https://arxiv.org/abs/2312.13308)] [Code]
- **📝 说明**：✏️

#### [38] Gaussian Splatting with NeRF-based Color and Opacity
- **🧑‍🔬 作者**：Dawid Malarz, Weronika Smolak, Jacek Tabor, Sławomir Tadeja, Przemysław Spurek
- **🏫 单位**：Jagiellonian University ⟐ University of Cambridge
- **🔗 链接**：[[中英摘要](./abs/2312.13729.md)] [[arXiv:2312.13729](https://arxiv.org/abs/2312.13729)] [[Code](https://github.com/gmum/ViewingDirectionGaussianSplatting)]
- **📝 说明**：✏️

#### [39] Deformable 3D Gaussian Splatting for Animatable Human Avatars
- **🧑‍🔬 作者**：HyunJun Jung, Nikolas Brasch, Jifei Song, Eduardo Perez-Pellitero, Yiren Zhou, Zhihao Li, Nassir Navab, Benjamin Busam
- **🏫 单位**：Technical University of Munich ⟐ Huawei Noah’s Ark Lab ⟐ 3dwe.ai
- **🔗 链接**：[[中英摘要](./abs/2312.15059.md)] [[arXiv:2312.15059](https://arxiv.org/abs/2312.15059)] [[Code](https://github.com/Junggy/pardy-human)]
- **📝 说明**：Code link 404

#### [40] Human101: Training 100+FPS Human Gaussians in 100s from 1 View
- **🧑‍🔬 作者**：Mingwei Li, Jiachen Tao, Zongxin Yang, Yi Yang
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2312.15258.md)] [[arXiv:2312.15258](https://arxiv.org/abs/2312.15258)] [[Code](https://github.com/longxiang-ai/Human101)]
- **📝 说明**：✏️

#### [41] Sparse-view CT Reconstruction with 3D Gaussian Volumetric Representation
- **🧑‍🔬 作者**：Yingtai Li, Xueming Fu, Shang Zhao, Ruiyang Jin, S. Kevin Zhou
- **🏫 单位**：University of Science and Technology of China ⟐ Chinese Academy of Sciences
- **🔗 链接**：[[中英摘要](./abs/2312.15676.md)] [[arXiv:2312.15676](https://arxiv.org/abs/2312.15676)] [Code]
- **📝 说明**：✏️

#### [42] 2D-Guided 3D Gaussian Segmentation
- **🧑‍🔬 作者**：Kun Lan, Haoran Li, Haolin Shi, Wenjun Wu, Yong Liao, Lin Wang, Pengyuan Zhou
- **🏫 单位**：University of Science and Technology of China ⟐ HKUST(GZ)
- **🔗 链接**：[[中英摘要](./abs/2312.16047.md)] [[arXiv:2312.16047](https://arxiv.org/abs/2312.16047)] [Code]
- **📝 说明**：✏️

#### [43] DreamGaussian4D: Generative 4D Gaussian Splatting
- **🧑‍🔬 作者**：Jiawei Ren, Liang Pan, Jiaxiang Tang, Chi Zhang, Ang Cao, Gang Zeng, Ziwei Liu
- **🏫 单位**：Nanyang Technological University ⟐ Shanghai AI Laboratory ⟐ Peking University ⟐ University of Michigan
- **🔗 链接**：[[中英摘要](./abs/2312.17142.md)] [[arXiv:2312.17142](https://arxiv.org/abs/2312.17142)] [[Code](https://github.com/jiawei-ren/dreamgaussian4d)]
- **📝 说明**：✏️

#### [44] 4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency
- **🧑‍🔬 作者**：Yuyang Yin, Dejia Xu, Zhangyang Wang, Yao Zhao, Yunchao Wei
- **🏫 单位**：Beijing Jiaotong University ⟐ University of Texas at Austin
- **🔗 链接**：[[中英摘要](./abs/2312.17225.md)] [[arXiv:2312.17225](https://arxiv.org/abs/2312.17225)] [[Code](https://github.com/VITA-Group/4DGen)]
- **📝 说明**：✏️

#### [45] Deblurring 3D Gaussian Splatting
- **🧑‍🔬 作者**：Byeonghyeon Lee, Howoong Lee, Xiangyu Sun, Usman Ali, Eunbyung Park
- **🏫 单位**：Sungkyunkwan University ⟐ Hanhwa Vision
- **🔗 链接**：[[中英摘要](./abs/2401.00834.md)] [[arXiv:2401.00834](https://arxiv.org/abs/2401.00834)] [[Code](https://github.com/benhenryL/Deblurring-3D-Gaussian-Splatting)]
- **📝 说明**：✏️

#### [46] Street Gaussians for Modeling Dynamic Urban Scenes
- **🧑‍🔬 作者**：Yunzhi Yan, Haotong Lin, Chenxu Zhou, Weijie Wang, Haiyang Sun, Kun Zhan, Xianpeng Lang, Xiaowei Zhou, Sida Peng
- **🏫 单位**：Zhejiang University ⟐ Li Auto
- **🔗 链接**：[[中英摘要](./abs/2401.01339.md)] [[arXiv:2401.01339](https://arxiv.org/abs/2401.01339)] [[Code](https://github.com/zju3dv/street_gaussians)]
- **📝 说明**：✏️

#### [47] FMGS: Foundation Model Embedded 3D Gaussian Splatting for Holistic 3D Scene Understanding
- **🧑‍🔬 作者**：Xingxing Zuo, Pouya Samangouei, Yunwen Zhou, Yan Di, Mingyang Li
- **🏫 单位**：Google
- **🔗 链接**：[[中英摘要](./abs/2401.01970.md)] [[arXiv:2401.01970](https://arxiv.org/abs/2401.01970)] [Code]
- **📝 说明**：✏️

#### [48] PEGASUS: Physically Enhanced Gaussian Splatting Simulation System for 6DOF Object Pose Dataset Generation
- **🧑‍🔬 作者**：Lukas Meyer, Floris Erich, Yusuke Yoshiyasu, Marc Stamminger, Noriaki Ando, Yukiyasu Domae
- **🏫 单位**：Friedrich-Alexander-Universität Erlangen-Nürnberg-Fürth ⟐ Industrial CPS Research Center, National Institute of Advanced Industrial Science and Technology, Japan
- **🔗 链接**：[[中英摘要](./abs/2401.02281.md)] [[arXiv:2401.02281](https://arxiv.org/abs/2401.02281)] [[Code](https://github.com/meyerls/PEGASUS)]
- **📝 说明**：✏️

#### [49] Compressed 3D Gaussian Splatting for Accelerated Novel View Synthesis
- **🧑‍🔬 作者**：Simon Niedermayr, Josef Stumpfegger, Rüdiger Westermann
- **🏫 单位**：Technical University of Munich
- **🔗 链接**：[[中英摘要](./abs/2401.02436.md)] [[arXiv:2401.02436](https://arxiv.org/abs/2401.02436)] [[Code](https://github.com/KeKsBoTer/c3dgs)]
- **📝 说明**：✏️

#### [50] Characterizing Satellite Geometry via Accelerated 3D Gaussian Splatting
- **🧑‍🔬 作者**：Van Minh Nguyen, Emma Sandidge, Trupti Mahendrakar, Ryan T. White
- **🏫 单位**：Florida Institute of Technology
- **🔗 链接**：[[中英摘要](./abs/2401.02588.md)] [[arXiv:2401.02588](https://arxiv.org/abs/2401.02588)] [Code]
- **📝 说明**：✏️

#### [51] AGG: Amortized Generative 3D Gaussians for Single Image to 3D
- **🧑‍🔬 作者**：Dejia Xu, Ye Yuan, Morteza Mardani, Sifei Liu, Jiaming Song, Zhangyang Wang, Arash Vahdat
- **🏫 单位**：The University of Texas at Austin ⟐ NVIDIA
- **🔗 链接**：[[中英摘要](./abs/2401.04099.md)] [[arXiv:2401.04099](https://arxiv.org/abs/2401.04099)] [Code]
- **📝 说明**：✏️

#### [52] DISTWAR: Fast Differentiable Rendering on Raster-based Rendering Pipelines
- **🧑‍🔬 作者**：Sankeerth Durvasula, Adrian Zhao, Fan Chen, Ruofan Liang, Pawan Kumar Sanjaya, Nandita Vijaykumar
- **🏫 单位**：University of Toronto
- **🔗 链接**：[[中英摘要](./abs/2401.05345.md)] [[arXiv:2401.05345](https://arxiv.org/abs/2401.05345)] [Code]
- **📝 说明**：✏️

#### [53] CoSSegGaussians: Compact and Swift Scene Segmenting 3D Gaussians
- **🧑‍🔬 作者**：Bin Dou, Tianyu Zhang, Yongjia Ma, Zhaohui Wang, Zejian Yuan
- **🏫 单位**：Xi’an Jiaotong University
- **🔗 链接**：[[中英摘要](./abs/2401.05925.md)] [[arXiv:2401.05925](https://arxiv.org/abs/2401.05925)] [Code]
- **📝 说明**：✏️

#### [54] TRIPS: Trilinear Point Splatting for Real-Time Radiance Field Rendering
- **🧑‍🔬 作者**：Linus Franke, Darius Rückert, Laura Fink, Marc Stamminger
- **🏫 单位**：Friedrich-Alexander-Universität Erlangen-Nürnberg
- **🔗 链接**：[[中英摘要](./abs/2401.06003.md)] [[arXiv:2401.06003](https://arxiv.org/abs/2401.06003)] [[Code](https://github.com/lfranke/trips)]
- **📝 说明**：✏️

#### [55] Fast Dynamic 3D Object Generation from a Single-view Video
- **🧑‍🔬 作者**：Zijie Pan, Zeyu Yang, Xiatian Zhu, Li Zhang
- **🏫 单位**：Fudan University ⟐ University of Surrey
- **🔗 链接**：[[中英摘要](./abs/2401.08742.md)] [[arXiv:2401.08742](https://arxiv.org/abs/2401.08742)] [[Code](https://github.com/fudan-zvg/Efficient4D)]
- **📝 说明**：✏️

#### [56] GaussianBody: Clothed Human Reconstruction via 3d Gaussian Splatting
- **🧑‍🔬 作者**：Mengtian Li, Shengxiang Yao, Zhifeng Xie, Keyu Chen, Yu-Gang Jiang
- **🏫 单位**：Shanghai University ⟐ Fudan University ⟐ Shanghai Engineering Research Center of Motion Picture Special Effects ⟐ Tavus Inc.
- **🔗 链接**：[[中英摘要](./abs/2401.09720.md)] [[arXiv:2401.09720](https://arxiv.org/abs/2401.09720)] [Code]
- **📝 说明**：✏️

#### [57] Deformable Endoscopic Tissues Reconstruction with Gaussian Splatting
- **🧑‍🔬 作者**：Lingting Zhu, Zhao Wang, Zhenchao Jin, Guying Lin, Lequan Yu
- **🏫 单位**：The University of Hong Kong ⟐  The Chinese University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2401.11535.md)] [[arXiv:2401.11535](https://arxiv.org/abs/2401.11535)] [[Code](https://github.com/HKU-MedAI/EndoGS)]
- **📝 说明**：✏️

#### [58] EndoGaussian: Gaussian Splatting for Deformable Surgical Scene Reconstruction
- **🧑‍🔬 作者**：Yifan Liu, Chenxin Li, Chen Yang, Yixuan Yuan
- **🏫 单位**：Chinese University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2401.12561.md)] [[arXiv:2401.12561](https://arxiv.org/abs/2401.12561)] [[Code](https://github.com/yifliu3/EndoGaussian)]
- **📝 说明**：✏️

#### [59] PSAvatar: A Point-based Morphable Shape Model for Real-Time Head Avatar Creation with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zhongyuan Zhao, Zhenyu Bao, Qing Li, Guoping Qiu, Kanglin Liu
- **🏫 单位**：Pengcheng Laboratory ⟐ Peking University ⟐ University of Nottingham ⟐ Shenzhen University
- **🔗 链接**：[[中英摘要](./abs/2401.12900.md)] [[arXiv:2401.12900](https://arxiv.org/abs/2401.12900)] [Code]
- **📝 说明**：✏️

#### [60] LIV-GaussMap: LiDAR-Inertial-Visual Fusion for Real-time 3D Radiance Field Map Rendering
- **🧑‍🔬 作者**：Sheng Hong, Junjie He, Xinhu Zheng, Hesheng Wang, Hao Fang, Kangcheng Liu, Chunran Zheng, Shaojie Shen
- **🏫 单位**：HKUST
- **🔗 链接**：[[中英摘要](./abs/2401.14857.md)] [[arXiv:2401.14857](https://arxiv.org/abs/2401.14857)] [[Code](https://github.com/sheng00125/LIV-GaussMap)]
- **📝 说明**：✏️  Empty code repo

#### [61] Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting
- **🧑‍🔬 作者**：Yutao Feng, Xiang Feng, Yintong Shang, Ying Jiang, Chang Yu, Zeshun Zong, Tianjia Shao, Hongzhi Wu, Kun Zhou, Chenfanfu Jiang, Yin Yang
- **🏫 单位**：University of Utah ⟐ Zhejiang University ⟐ UCLA
- **🔗 链接**：[[中英摘要](./abs/2401.15318.md)] [[arXiv:2401.15318](https://arxiv.org/abs/2401.15318)] [Code]
- **📝 说明**：✏️

#### [62] Endo-4DGS: Distilling Depth Ranking for Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting
- **🧑‍🔬 作者**：Yiming Huang, Beilei Cui, Long Bai, Ziqi Guo, Mengya Xu, Hongliang Ren
- **🏫 单位**：The Chinese University of Hong Kong ⟐  Shun Hing Institute of Advanced Engineering, CUHK ⟐ Shenzhen Research Institute, CUHK
- **🔗 链接**：[[中英摘要](./abs/2401.16416.md)] [[arXiv:2401.16416](https://arxiv.org/abs/2401.16416)] [Code]
- **📝 说明**：✏️

#### [63] VR-GS: A Physical Dynamics-Aware Interactive Gaussian Splatting System in Virtual Reality
- **🧑‍🔬 作者**：Ying Jiang, Chang Yu, Tianyi Xie, Xuan Li, Yutao Feng, Huamin Wang, Minchen Li, Henry Lau, Feng Gao, Yin Yang, Chenfanfu Jiang
- **🏫 单位**：UCLA ⟐ HKU ⟐ Utah ⟐ ZJU ⟐ Style3D Research ⟐ CMU ⟐ Amazon
- **🔗 链接**：[[中英摘要](./abs/2401.16663.md)] [[arXiv:2401.16663](https://arxiv.org/abs/2401.16663)] [Code]
- **📝 说明**：✏️

#### [64] Segment Anything in 3D Gaussians
- **🧑‍🔬 作者**：Xu Hu, Yuxi Wang, Lue Fan, Junsong Fan, Junran Peng, Zhen Lei, Qing Li, Zhaoxiang Zhang
- **🏫 单位**：The Hong Kong Polytechnic University ⟐ Center for Artificial Intelligence and Robotics, HKISI, CAS ⟐
Institute of Automation, Chinese Academy of Sciences ⟐ University of Chinese Academy of Sciences ⟐ Chongyue Technology
- **🔗 链接**：[[中英摘要](./abs/2401.17857.md)] [[arXiv:2401.17857](https://arxiv.org/abs/2401.17857)] [[Code](https://github.com/Jumpat/SegAnyGAussians)]
- **📝 说明**：✏️

#### [65] StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering
- **🧑‍🔬 作者**：Lukas Radl, Michael Steiner, Mathias Parger, Alexander Weinrauch, Bernhard Kerbl, Markus Steinberger
- **🏫 单位**：Graz University of Technology ⟐ TU Wien, Austria ⟐ Huawei Technologies, Austria
- **🔗 链接**：[[中英摘要](./abs/2402.00525.md)] [[arXiv:2402.00525](https://arxiv.org/abs/2402.00525)] [Code]
- **📝 说明**：✏️

#### [66] Optimal Projection for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Letian Huang, Jiayang Bai, Jie Guo, Yanwen Guo
- **🏫 单位**：Nanjing University
- **🔗 链接**：[[中英摘要](./abs/2402.00752.md)] [[arXiv:2402.00752](https://arxiv.org/abs/2402.00752)] [Code]
- **📝 说明**：✏️

#### [67] 360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming
- **🧑‍🔬 作者**：Jiayang Bai, Letian Huang, Jie Guo, Wen Gong, Yuanqi Li, Yanwen Guo
- **🏫 单位**：Nanjing University
- **🔗 链接**：[[中英摘要](./abs/2402.00763.md)] [[arXiv:2402.00763](https://arxiv.org/abs/2402.00763)] [Code]
- **📝 说明**：✏️

#### [68] GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting
- **🧑‍🔬 作者**：Joanna Waczyńska, Piotr Borycki, Sławomir Tadeja, Jacek Tabor, Przemysław Spurek
- **🏫 单位**：Jagiellonian University ⟐ University of Cambridge
- **🔗 链接**：[[中英摘要](./abs/2402.01459.md)] [[arXiv:2402.01459](https://arxiv.org/abs/2402.01459)] [[Code](https://github.com/waczjoan/gaussian-mesh-splatting)]
- **📝 说明**：✏️

#### [69] SGS-SLAM: Semantic Gaussian Splatting For Neural Dense SLAM
- **🧑‍🔬 作者**：Mingrui Li, Shuhong Liu, Heng Zhou
- **🏫 单位**：Dalian University of Technology ⟐ The University of Tokyo ⟐ Columbia University
- **🔗 链接**：[[中英摘要](./abs/2402.03246.md)] [[arXiv:2402.03246](https://arxiv.org/abs/2402.03246)] [Code]
- **📝 说明**：✏️

#### [70] 4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes
- **🧑‍🔬 作者**：Yuanxing Duan, Fangyin Wei, Qiyu Dai, Yuhang He, Wenzheng Chen, Baoquan Chen
- **🏫 单位**：Peking University ⟐ Princeton University ⟐ NVIDIA ⟐ National Key Lab of General AI, China
- **🔗 链接**：[[中英摘要](./abs/2402.03307.md)] [[arXiv:2402.03307](https://arxiv.org/abs/2402.03307)] [Code]
- **📝 说明**：✏️

#### [71] Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos
- **🧑‍🔬 作者**：Alfredo Rivero, ShahRukh Athar, Zhixin Shu, Dimitris Samaras
- **🏫 单位**：Stony Brook University ⟐ Adobe Research
- **🔗 链接**：[[中英摘要](./abs/2402.03723.md)] [[arXiv:2402.03723](https://arxiv.org/abs/2402.03723)] [Code]
- **📝 说明**：✏️

#### [72] Mesh-based Gaussian Splatting for Real-time Large-scale Deformation
- **🧑‍🔬 作者**：Lin Gao, Jie Yang, Bo-Tao Zhang, Jia-Mu Sun, Yu-Jie Yuan, Hongbo Fu, Yu-Kun Lai
- **🏫 单位**：University of Chinese Academy of Sciences ⟐  City University of Hong Kong ⟐ Cardiff University
- **🔗 链接**：[[中英摘要](./abs/2402.04796.md)] [[arXiv:2402.04796](https://arxiv.org/abs/2402.04796)] [Code]
- **📝 说明**：✏️

#### [73] LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation
- **🧑‍🔬 作者**：Jiaxiang Tang, Zhaoxi Chen, Xiaokang Chen, Tengfei Wang, Gang Zeng, Ziwei Liu
- **🏫 单位**：Peking University ⟐ Nanyang Technological University ⟐ Shanghai AI Lab
- **🔗 链接**：[[中英摘要](./abs/2402.05054.md)] [[arXiv:2402.05054](https://arxiv.org/abs/2402.05054)] [[Code](https://github.com/3DTopia/LGM)]
- **📝 说明**：✏️

#### [74] HeadStudio: Text to Animatable Head Avatars with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zhenglin Zhou, Fan Ma, Hehe Fan, Yi Yang
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2402.06149.md)] [[arXiv:2402.06149](https://arxiv.org/abs/2402.06149)] [[Code](https://github.com/ZhenglinZhou/HeadStudio)]
- **📝 说明**：✏️

#### [75] GS-CLIP: Gaussian Splatting for Contrastive Language-Image-3D Pretraining from Real-World Data
- **🧑‍🔬 作者**：Haoyuan Li, Yanpeng Zhou, Yihan Zeng, Hang Xu, Xiaodan Liang
- **🏫 单位**：Shenzhen campus of Sun Yat-sen University ⟐ Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2402.06198.md)] [[arXiv:2402.06198](https://arxiv.org/abs/2402.06198)] [Code]
- **📝 说明**：✏️

#### [76] GALA3D: Towards Text-to-3D Complex Scene Generation via Layout-guided Generative Gaussian Splatting
- **🧑‍🔬 作者**：Xiaoyu Zhou, Xingjian Ran, Yajiao Xiong, Jinlin He, Zhiwei Lin, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang
- **🏫 单位**：Peking University ⟐ Google Research ⟐ University of California, Merced
- **🔗 链接**：[[中英摘要](./abs/2402.07207.md)] [[arXiv:2402.07207](https://arxiv.org/abs/2402.07207)] [[Code](https://github.com/VDIGPKU/GALA3D)]
- **📝 说明**：✏️

#### [77] GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering
- **🧑‍🔬 作者**：Abdullah Hamdi, Luke Melas-Kyriazi, Guocheng Qian, Jinjie Mai, Ruoshi Liu, Carl Vondrick, Bernard Ghanem, Andrea Vedaldi
- **🏫 单位**：VGG, University of Oxford ⟐ KAUST ⟐ Columbia University ⟐ Snap Inc.
- **🔗 链接**：[[中英摘要](./abs/2402.10128.md)] [[arXiv:2402.10128](https://arxiv.org/abs/2402.10128)] [[Code](https://github.com/ajhamdi/ges-splatting)]
- **📝 说明**：✏️

#### [78] GaussianObject: Just Taking Four Images to Get A High-Quality 3D Object with Gaussian Splatting
- **🧑‍🔬 作者**：Chen Yang, Sikuang Li, Jiemin Fang, Ruofan Liang, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian
- **🏫 单位**：Shanghai Jiao Tong University ⟐ Huawei ⟐ University of Toronto
- **🔗 链接**：[[中英摘要](./abs/2402.10259.md)] [[arXiv:2402.10259](https://arxiv.org/abs/2402.10259)] [[Code](https://github.com/GaussianObject/GaussianObject)]
- **📝 说明**：✏️

#### [79] GaussianHair: Hair Modeling and Rendering with Light-aware Gaussians
- **🧑‍🔬 作者**：Haimin Luo, Min Ouyang, Zijun Zhao, Suyi Jiang, Longwen Zhang, Qixuan Zhang, Wei Yang, Lan Xu, Jingyi Yu
- **🏫 单位**：ShanghaiTech University ⟐ Huazhong University of Science and Technology ⟐ Deemos Technology ⟐ LumiAni Technology
- **🔗 链接**：[[中英摘要](./abs/2402.10483.md)] [[arXiv:2402.10483](https://arxiv.org/abs/2402.10483)] [Code]
- **📝 说明**：✏️

#### [80] Identifying Unnecessary 3D Gaussians using Clustering for Fast Rendering of 3D Gaussian Splatting
- **🧑‍🔬 作者**：Joongho Jo, Hyeongwon Kim, Jongsun Park
- **🏫 单位**：Korea University
- **🔗 链接**：[[中英摘要](./abs/2402.13827.md)] [[arXiv:2402.13827](https://arxiv.org/abs/2402.13827)] [Code]
- **📝 说明**：✏️

#### [81] GaussianPro: 3D Gaussian Splatting with Progressive Propagation
- **🧑‍🔬 作者**：Kai Cheng, Xiaoxiao Long, Kaizhi Yang, Yao Yao, Wei Yin, Yuexin Ma, Wenping Wang, Xuejin Chen
- **🏫 单位**：University of Science and Technology of China ⟐ The University of Hong Kong ⟐ Nanjing University ⟐ The University of Adelaide ⟐ ShanghaiTech University ⟐ Texas A&M University
- **🔗 链接**：[[中英摘要](./abs/2402.14650.md)] [[arXiv:2402.14650](https://arxiv.org/abs/2402.14650)] [Code]
- **📝 说明**：✏️

#### [82] Spec-Gaussian: Anisotropic View-Dependent Appearance for 3D Gaussian Splatting
- **🧑‍🔬 作者**：Ziyi Yang, Xinyu Gao, Yangtian Sun, Yihua Huang, Xiaoyang Lyu, Wen Zhou, Shaohui Jiao, Xiaojuan Qi, Xiaogang Jin
- **🏫 单位**：Zhejiang University ⟐ The University of Hong Kong ⟐ ByteDance Inc.
- **🔗 链接**：[[中英摘要](./abs/2402.15870.md)] [[arXiv:2402.15870](https://arxiv.org/abs/2402.15870)] [Code]
- **📝 说明**：✏️

#### [83] GEA: Reconstructing Expressive 3D Gaussian Avatar from Monocular Video
- **🧑‍🔬 作者**：Xinqi Liu, Chenming Wu, Xing Liu, Jialun Liu, Jinbo Wu, Chen Zhao, Haocheng Feng, Errui Ding, Jingdong Wang
- **🏫 单位**：Baidu Inc.
- **🔗 链接**：[[中英摘要](./abs/2402.16607.md)] [[arXiv:2402.16607](https://arxiv.org/abs/2402.16607)] [Code]
- **📝 说明**：✏️

#### [84] 3D Gaussian Model for Animation and Texturing
- **🧑‍🔬 作者**：Xiangzhi Eric Wang, Zackary P. T. Sin
- **🏫 单位**：The Hong Kong Polytechnic University
- **🔗 链接**：[[中英摘要](./abs/2402.19441.md)] [[arXiv:2402.19441](https://arxiv.org/abs/2402.19441)] [Code]
- **📝 说明**：✏️

#### [85] Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps
- **🧑‍🔬 作者**：Timothy Chen, Ola Shorinwa, Weijia Zeng, Joseph Bruno, Philip Dames, Mac Schwager
- **🏫 单位**：Stanford University ⟐ University of California San Diego ⟐ Temple University
- **🔗 链接**：[[中英摘要](./abs/2403.02751.md)] [[arXiv:2403.02751](https://arxiv.org/abs/2403.02751)] [Code]
- **📝 说明**：✏️

#### [86] Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis
- **🧑‍🔬 作者**：Yuanhao Cai, Yixun Liang, Jiahao Wang, Angtian Wang, Yulun Zhang, Xiaokang Yang, Zongwei Zhou, Alan Yuille
- **🏫 单位**：Johns Hopkins University ⟐ HKUST(GZ) ⟐ Shanghai Jiao Tong University
- **🔗 链接**：[[中英摘要](./abs/2403.04116.md)] [[arXiv:2403.04116](https://arxiv.org/abs/2403.04116)] [[Code](https://github.com/caiyuanhao1998/X-Gaussian)]
- **📝 说明**：✏️

#### [87] BAGS: Blur Agnostic Gaussian Splatting through Multi-Scale Kernel Modeling
- **🧑‍🔬 作者**：Cheng Peng, Yutao Tang, Yifan Zhou, Nengyu Wang, Xijun Liu, Deming Li, Rama Chellappa
- **🏫 单位**：Johns Hopkins University
- **🔗 链接**：[[中英摘要](./abs/2403.04926.md)] [[arXiv:2403.04926](https://arxiv.org/abs/2403.04926)] [[Code](https://github.com/snldmt/BAGS)]
- **📝 说明**：✏️

#### [88] GSEdit: Efficient Text-Guided Editing of 3D Objects via Gaussian Splatting
- **🧑‍🔬 作者**：Francesco Palandra, Andrea Sanchietti, Daniele Baieri, Emanuele Rodolà
- **🏫 单位**：Sapienza University of Rome
- **🔗 链接**：[[中英摘要](./abs/2403.05154.md)] [[arXiv:2403.05154](https://arxiv.org/abs/2403.05154)] [Code]
- **📝 说明**：✏️
