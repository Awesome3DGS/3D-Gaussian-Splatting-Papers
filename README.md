# 3D Gaussian Splatting Papers

[![更新日志](https://img.shields.io/badge/💡-更新日志-informational.svg?style=flat)](Changelog.md)
[![发现错误](https://img.shields.io/badge/🐛-发现错误-yellow.svg?style=flat)](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/issues)
[![提交修改](https://img.shields.io/badge/👐-提交修改-brightgreen.svg?style=flat)](https://github.com/Awesome3DGS/3D-Gaussian-Splatting-Papers/pulls)


**⚡ 快捷链接**: [[10](#10-gaussiandiffusion-3d-gaussian-splatting-for-denoising-diffusion-probabilistic-models-with-structured-noise)]
                 [[20](#20-gaussianeditor-editing-3d-gaussians-delicately-with-text-instructions)]
                 [[30](#30-lightgaussian-unbounded-3d-gaussian-compression-with-15x-reduction-and-200-fps)]
                 [[40](#40-sparsegs-real-time-360-sparse-view-synthesis-using-gaussian-splatting)]
                 [[50](#50-gaussianavatar-towards-realistic-human-avatar-modeling-from-a-single-video-via-animatable-3d-gaussians)]
                 [[60](#60-eagles-efficient-accelerated-3d-gaussians-with-lightweight-encodings)]
                 [[70](#70-text2immersion-generative-immersive-scene-with-3d-gaussians)]
                 [[80](#80-gaussian-splatting-with-nerf-based-color-and-opacity)]
                 [[90](#90-4dgen-grounded-4d-content-generation-with-spatial-temporal-consistency)]
                 [[100](#100-trips-trilinear-point-splatting-for-real-time-radiance-field-rendering)]（最新）

**📚 会议期刊**: [[ICLR2024](./ICLR2024.md)] (2 篇)

---

#### [S0] A Survey on 3D Gaussian Splatting
- **🧑‍🔬 作者**：Guikun Chen, Wenguan Wang
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2401.03890.md)] [[arXiv:2401.03890](https://arxiv.org/abs/2401.03890)]
- **📝 说明**：🔥 首篇综述

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
- **📝 说明**：✍️ 可能是CVPR2024投稿，提出一种建模动态场景的3DGS方法，可以应用的各种密集6-DOF跟踪相关的下游任务，包括第一视角视图合成、动态组合场景合成和4D视频编辑等。

#### [2] Flexible Techniques for Differentiable Rendering with 3D Gaussians
- **🧑‍🔬 作者**：Leonid Keselman, Martial Hebert
- **🏫 单位**：Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2308.14737.md)] [[arXiv:2308.14737](https://arxiv.org/abs/2308.14737)] [[Code](https://github.com/leonidk/fmb-plus)]
- **📝 说明**：✏️

#### [3] Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction
- **🧑‍🔬 作者**：Ziyi Yang, Xinyu Gao, Wen Zhou, Shaohui Jiao, Yuqing Zhang, Xiaogang Jin
- **🏫 单位**： Zhejiang University ⟐ ByteDance Inc.
- **🔗 链接**：[[中英摘要](./abs/2309.13101.md)] [[arXiv:2309.13101](https://arxiv.org/abs/2309.13101)] [[Code](https://github.com/ingra14m/Deformable-3D-Gaussians)]
- **📝 说明**：✏️

#### [4] Text-to-3D using Gaussian Splatting
- **🧑‍🔬 作者**：Zilong Chen, Feng Wang, Huaping Liu
- **🏫 单位**：Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2309.16585.md)] [[arXiv:2309.16585](https://arxiv.org/abs/2309.16585)] [[Code](https://github.com/gsgen3d/gsgen)]
- **📝 说明**：✏️

#### [5] 4d gaussian splatting for real-time dynamic scene rendering
- **🧑‍🔬 作者**：Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Qi Tian, Xinggang Wang
- **🏫 单位**：Huazhong University of Science and Technology ⟐ Huawei Inc.
- **🔗 链接**：[[中英摘要](./abs/2310.08528.md)] [[arXiv:2310.08528](https://arxiv.org/abs/2310.08528)] [[Code](https://github.com/hustvl/4DGaussians)]
- **📝 说明**：✏️

#### [6] GaussianDreamer: Fast Generation from Text to 3D Gaussians by Bridging 2D and 3D Diffusion Models
- **🧑‍🔬 作者**：Taoran Yi, Jiemin Fang, Junjie Wang, Guanjun Wu, Lingxi Xie, Xiaopeng Zhang, Wenyu Liu, Qi Tian, Xinggang Wang
- **🏫 单位**：Huazhong University of Science and Technology ⟐ Huawei Inc.
- **🔗 链接**：[[中英摘要](./abs/2310.08529.md)] [[arXiv:2310.08529](https://arxiv.org/abs/2310.08529)] [[Code](https://github.com/hustvl/GaussianDreamer)]
- **📝 说明**：✏️

#### [7] Dynamic Gaussian Splatting from Markerless Motion Capture can Reconstruct Infants Movements
- **🧑‍🔬 作者**：R. James Cotton, Colleen Peyton
- **🏫 单位**：Shirley Ryan AbilityLab ⟐ Northwestern University
- **🔗 链接**：[[中英摘要](./abs/2310.19441.md)] [[arXiv:2310.19441](https://arxiv.org/abs/2310.19441)] [Code]
- **📝 说明**：✏️

#### [8] Drivable 3D Gaussian Avatars
- **🧑‍🔬 作者**：Wojciech Zielonka, Timur Bagautdinov, Shunsuke Saito, Michael Zollhöfer, Justus Thies, Javier Romero
- **🏫 单位**：Meta Reality Labs Research ⟐ Technical University of Darmstadt ⟐ Max Planck Institute for Intelligent Systems
- **🔗 链接**：[[中英摘要](./abs/2311.08581.md)] [[arXiv:2311.08581](https://arxiv.org/abs/2311.08581)] [Code]
- **📝 说明**：✏️

#### [9] SplatArmor: Articulated Gaussian splatting for animatable humans from monocular RGB videos
- **🧑‍🔬 作者**：Rohit Jena, Ganesh Subramanian Iyer, Siddharth Choudhary, Brandon Smith, Pratik Chaudhari, James Gee
- **🏫 单位**：University of Pennsylvania ⟐ Amazon.com, Inc.
- **🔗 链接**：[[中英摘要](./abs/2311.10812.md)] [[arXiv:2311.10812](https://arxiv.org/abs/2311.10812)] [[Code](https://github.com/rohitrango/splatarmor)]
- **📝 说明**：✏️

#### [10] GaussianDiffusion: 3D Gaussian Splatting for Denoising Diffusion Probabilistic Models with Structured Noise
- **🧑‍🔬 作者**：Xinhai Li, Huaibin Wang, Kuo-Kun Tseng
- **🏫 单位**：Harbin Institute of Technology (Shenzhen)
- **🔗 链接**：[[中英摘要](./abs/2311.11221.md)] [[arXiv:2311.11221](https://arxiv.org/abs/2311.11221)] [Code]
- **📝 说明**：✏️

#### [11] GS-SLAM: Dense Visual SLAM with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Chi Yan, Delin Qu, Dong Wang, Dan Xu, Zhigang Wang, Bin Zhao, Xuelong Li
- **🏫 单位**：Shanghai AI Laboratory ⟐ Fudan University ⟐ Northwestern Polytechnical University ⟐ The Hong Kong University of Science and Technology
- **🔗 链接**：[[中英摘要](./abs/2311.11700.md)] [[arXiv:2311.11700](https://arxiv.org/abs/2311.11700)] [Code]
- **📝 说明**：✏️

#### [12] PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics
- **🧑‍🔬 作者**：Tianyi Xie, Zeshun Zong, Yuxing Qiu, Xuan Li, Yutao Feng, Yin Yang, Chenfanfu Jiang
- **🏫 单位**：UCLA ⟐ Zhejiang University ⟐ University of Utah
- **🔗 链接**：[[中英摘要](./abs/2311.12198.md)] [[arXiv:2311.12198](https://arxiv.org/abs/2311.12198)] [[Code](https://github.com/XPandora/PhysGaussian)]
- **📝 说明**：✏️

#### [13] SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering
- **🧑‍🔬 作者**：Antoine Guédon, Vincent Lepetit
- **🏫 单位**：Univ Gustave Eiffel
- **🔗 链接**：[[中英摘要](./abs/2311.12775.md)] [[arXiv:2311.12775](https://arxiv.org/abs/2311.12775)] [[Code](https://github.com/Anttwo/SuGaR)]
- **📝 说明**：✏️

#### [14] An Efficient 3D Gaussian Representation for Monocular/Multi-view Dynamic Scenes
- **🧑‍🔬 作者**：Kai Katsumata, Duc Minh Vo, Hideki Nakayama
- **🏫 单位**：The University of Tokyo
- **🔗 链接**：[[中英摘要](./abs/2311.12897.md)] [[arXiv:2311.12897](https://arxiv.org/abs/2311.12897)] [Code]
- **📝 说明**：✏️

#### [15] LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes
- **🧑‍🔬 作者**：Jaeyoung Chung, Suyoung Lee, Hyeongjin Nam, Jaerin Lee, Kyoung Mu Lee
- **🏫 单位**：Seoul National University
- **🔗 链接**：[[中英摘要](./abs/2311.13384.md)] [[arXiv:2311.13384](https://arxiv.org/abs/2311.13384)] [[Code](https://github.com/luciddreamer-cvlab/LucidDreamer)]
- **📝 说明**：✏️

#### [16] Depth-Regularized Optimization for 3D Gaussian Splatting in Few-Shot Images
- **🧑‍🔬 作者**：Jaeyoung Chung, Jeongtaek Oh, Kyoung Mu Lee
- **🏫 单位**：Seoul National University
- **🔗 链接**：[[中英摘要](./abs/2311.13398.md)] [[arXiv:2311.13398](https://arxiv.org/abs/2311.13398)] [Code]
- **📝 说明**：✏️

#### [17] Animatable 3D Gaussians for High-fidelity Synthesis of Human Motions
- **🧑‍🔬 作者**：Keyang Ye, Tianjia Shao, Kun Zhou
- **🏫 单位**：Unknown
- **🔗 链接**：[[中英摘要](./abs/2311.13404.md)] [[arXiv:2311.13404](https://arxiv.org/abs/2311.13404)] [Code]
- **📝 说明**：✏️ This paper has been withdrawn by Keyang Ye

#### [18] Compact 3D Gaussian Representation for Radiance Field
- **🧑‍🔬 作者**：Joo Chan Lee, Daniel Rho, Xiangyu Sun, Jong Hwan Ko, Eunbyung Park
- **🏫 单位**：Sungkyunkwan University ⟐ KT
- **🔗 链接**：[[中英摘要](./abs/2311.13681.md)] [[arXiv:2311.13681](https://arxiv.org/abs/2311.13681)] [[Code](https://github.com/maincold2/Compact-3DGS)]
- **📝 说明**：✏️

#### [19] GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting
- **🧑‍🔬 作者**：Yiwen Chen, Zilong Chen, Chi Zhang, Feng Wang, Xiaofeng Yang, Yikai Wang, Zhongang Cai, Lei Yang, Huaping Liu, Guosheng Lin
- **🏫 单位**：Nanyang Technological University ⟐ Tsinghua University ⟐ SenseTime Research
- **🔗 链接**：[[中英摘要](./abs/2311.14521.md)] [[arXiv:2311.14521](https://arxiv.org/abs/2311.14521)] [[Code](https://github.com/buaacyw/GaussianEditor)]
- **📝 说明**：✏️

#### [20] GaussianEditor: Editing 3D Gaussians Delicately with Text Instructions
- **🧑‍🔬 作者**：Jiemin Fang, Junjie Wang, Xiaopeng Zhang, Lingxi Xie, Qi Tian
- **🏫 单位**：Huawei Inc.
- **🔗 链接**：[[中英摘要](./abs/2311.16037.md)] [[arXiv:2311.16037](https://arxiv.org/abs/2311.16037)] [Code]
- **📝 说明**：✏️

#### [21] Relightable 3D Gaussian: Real-time Point Cloud Relighting with BRDF Decomposition and Ray Tracing
- **🧑‍🔬 作者**：Jian Gao, Chun Gu, Youtian Lin, Hao Zhu, Xun Cao, Li Zhang, Yao Yao
- **🏫 单位**：Nanjing University ⟐ Fudan University
- **🔗 链接**：[[中英摘要](./abs/2311.16043.md)] [[arXiv:2311.16043](https://arxiv.org/abs/2311.16043)] [[Code](https://github.com/NJU-3DV/Relightable3DGaussian)]
- **📝 说明**：✏️

#### [22] Animatable Gaussians: Learning Pose-dependent Gaussian Maps for High-fidelity Human Avatar Modeling
- **🧑‍🔬 作者**：Zhe Li, Zerong Zheng, Lizhen Wang, Yebin Liu
- **🏫 单位**：Tsinghua University ⟐ NNKosmos Technology
- **🔗 链接**：[[中英摘要](./abs/2311.16096.md)] [[arXiv:2311.16096](https://arxiv.org/abs/2311.16096)] [[Code](https://github.com/lizhe00/AnimatableGaussians)]
- **📝 说明**：✏️

#### [23] GART: Gaussian Articulated Template Models
- **🧑‍🔬 作者**：Jiahui Lei, Yufu Wang, Georgios Pavlakos, Lingjie Liu, Kostas Daniilidis
- **🏫 单位**：University of Pennsylvania ⟐ UC Berkeley ⟐ Archimedes, Athena RC
- **🔗 链接**：[[中英摘要](./abs/2311.16099.md)] [[arXiv:2311.16099](https://arxiv.org/abs/2311.16099)] [[Code](https://github.com/JiahuiLei/GART)]
- **📝 说明**：✏️

#### [24] GS-IR: 3D Gaussian Splatting for Inverse Rendering
- **🧑‍🔬 作者**：Zhihao Liang, Qi Zhang, Ying Feng, Ying Shan, Kui Jia
- **🏫 单位**：South China University of Technology ⟐ Tencent AI Lab ⟐ The Chinese University of Hong Kong, Shenzhen
- **🔗 链接**：[[中英摘要](./abs/2311.16473.md)] [[arXiv:2311.16473](https://arxiv.org/abs/2311.16473)] [[Code](https://github.com/lzhnb/GS-IR)]
- **📝 说明**：✏️

#### [25] Animatable 3D Gaussian: Fast and High-Quality Reconstruction of Multiple Human Avatars
- **🧑‍🔬 作者**：Yang Liu, Xiang Huang, Minghan Qin, Qinwei Lin, Haoqian Wang
- **🏫 单位**： Tsinghua University ⟐ Gala Sports
- **🔗 链接**：[[中英摘要](./abs/2311.16482.md)] [[arXiv:2311.16482](https://arxiv.org/abs/2311.16482)] [[Code](https://github.com/jimmyYliu/Animatable-3D-Gaussian)]
- **📝 说明**：✏️

#### [26] Mip-Splatting: Alias-free 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zehao Yu, Anpei Chen, Binbin Huang, Torsten Sattler, Andreas Geiger
- **🏫 单位**： University of Tubingen ⟐ Tubingen AI Center ⟐ ShanghaiTech University ⟐ Czech Technical University in Prague
- **🔗 链接**：[[中英摘要](./abs/2311.16493.md)] [[arXiv:2311.16493](https://arxiv.org/abs/2311.16493)] [[Code](https://github.com/autonomousvision/mip-splatting)]
- **📝 说明**：✏️

#### [27] HumanGaussian: Text-Driven 3D Human Generation with Gaussian Splatting
- **🧑‍🔬 作者**：Xian Liu, Xiaohang Zhan, Jiaxiang Tang, Ying Shan, Gang Zeng, Dahua Lin, Xihui Liu, Ziwei Liu
- **🏫 单位**：CUHK ⟐ Tencent AI Lab ⟐ PKU ⟐ HKU ⟐ NTU
- **🔗 链接**：[[中英摘要](./abs/2311.17061.md)] [[arXiv:2311.17061](https://arxiv.org/abs/2311.17061)] [[Code](https://github.com/alvinliu0/HumanGaussian)]
- **📝 说明**：✏️

#### [28] Multi-Scale 3D Gaussian Splatting for Anti-Aliased Rendering
- **🧑‍🔬 作者**：Zhiwen Yan, Weng Fei Low, Yu Chen, Gim Hee Lee
- **🏫 单位**：National University of Singapore
- **🔗 链接**：[[中英摘要](./abs/2311.17089.md)] [[arXiv:2311.17089](https://arxiv.org/abs/2311.17089)] [Code]
- **📝 说明**：✏️

#### [29] Human Gaussian Splatting: Real-time Rendering of Animatable Avatars
- **🧑‍🔬 作者**：Arthur Moreau, Jifei Song, Helisa Dhamo, Richard Shaw, Yiren Zhou, Eduardo Pérez-Pellitero
- **🏫 单位**：Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2311.17113.md)] [[arXiv:2311.17113](https://arxiv.org/abs/2311.17113)] [Code]
- **📝 说明**：✏️

#### [30] LightGaussian: Unbounded 3D Gaussian Compression with 15x Reduction and 200+ FPS
- **🧑‍🔬 作者**：Zhiwen Fan, Kevin Wang, Kairun Wen, Zehao Zhu, Dejia Xu, Zhangyang Wang
- **🏫 单位**：University of Texas at Austin ⟐ Xiamen University
- **🔗 链接**：[[中英摘要](./abs/2311.17245.md)] [[arXiv:2311.17245](https://arxiv.org/abs/2311.17245)] [[Code](https://github.com/VITA-Group/LightGaussian)]
- **📝 说明**：✏️

#### [31] Gaussian Shell Maps for Efficient 3D Human Generation
- **🧑‍🔬 作者**：Rameen Abdal, Wang Yifan, Zifan Shi, Yinghao Xu, Ryan Po, Zhengfei Kuang, Qifeng Chen, Dit-Yan Yeung, Gordon Wetzstein
- **🏫 单位**：Stanford University ⟐ HKUST
- **🔗 链接**：[[中英摘要](./abs/2311.17857.md)] [[arXiv:2311.17857](https://arxiv.org/abs/2311.17857)] [[Code](https://github.com/computational-imaging/GSM)]
- **📝 说明**：✏️

#### [32] CG3D: Compositional Generation for Text-to-3D via Gaussian Splatting
- **🧑‍🔬 作者**：Alexander Vilesov, Pradyumna Chari, Achuta Kadambi
- **🏫 单位**：University of California, Los Angeles
- **🔗 链接**：[[中英摘要](./abs/2311.17907.md)] [[arXiv:2311.17907](https://arxiv.org/abs/2311.17907)] [Code]
- **📝 说明**：✏️

#### [33] HUGS: Human Gaussian Splats
- **🧑‍🔬 作者**：Muhammed Kocabas, Jen-Hao Rick Chang, James Gabriel, Oncel Tuzel, Anurag Ranjan
- **🏫 单位** Apple ⟐ Max Planck Institute for Intelligent Systems ⟐ ETH Zurich
- **🔗 链接**：[[中英摘要](./abs/2311.17910.md)] [[arXiv:2311.17910](https://arxiv.org/abs/2311.17910)] [[Code](https://github.com/apple/ml-hugs)]
- **📝 说明**：Code link 404

#### [34] GaussianShader: 3D Gaussian Splatting with Shading Functions for Reflective Surfaces
- **🧑‍🔬 作者**：Yingwenqi Jiang, Jiadong Tu, Yuan Liu, Xifeng Gao, Xiaoxiao Long, Wenping Wang, Yuexin Ma
- **🏫 单位**：ShanghaiTech University ⟐ The University of Hong Kong ⟐ Tencent America ⟐ Texas A&M University
- **🔗 链接**：[[中英摘要](./abs/2311.17977.md)] [[arXiv:2311.17977](https://arxiv.org/abs/2311.17977)] [Code]
- **📝 说明**：✏️

#### [35] Compact3D: Compressing Gaussian Splat Radiance Field Models with Vector Quantization
- **🧑‍🔬 作者**：KL Navaneet, Kossar Pourahmadi Meibodi, Soroush Abbasi Koohpayegani, Hamed Pirsiavash
- **🏫 单位**：University of California, Davis
- **🔗 链接**：[[中英摘要](./abs/2311.18159.md)] [[arXiv:2311.18159](https://arxiv.org/abs/2311.18159)] [[Code](https://github.com/UCDvision/compact3d)]
- **📝 说明**：✏️

#### [36] Language Embedded 3D Gaussians for Open-Vocabulary Scene Understanding
- **🧑‍🔬 作者**：Jin-Chuan Shi, Miao Wang, Hao-Bin Duan, Shao-Hua Guan
- **🏫 单位**：Beihang University ⟐ Zhongguanchun Laboratory
- **🔗 链接**：[[中英摘要](./abs/2311.18482.md)] [[arXiv:2311.18482](https://arxiv.org/abs/2311.18482)] [[Code](https://github.com/Chuan-10/LEGaussians)]
- **📝 说明**：✏

#### [37] Periodic Vibration Gaussian: Dynamic Urban Scene Reconstruction and Real-time Rendering
- **🧑‍🔬 作者**：Yurui Chen, Chun Gu, Junzhe Jiang, Xiatian Zhu, Li Zhang
- **🏫 单位**：Fudan University ⟐ University of Surrey
- **🔗 链接**：[[中英摘要](./abs/2311.18561.md)] [[arXiv:2311.18561](https://arxiv.org/abs/2311.18561)] [[Code](https://github.com/fudan-zvg/PVG)]
- **📝 说明**：✏

#### [38] Scaffold-GS: Structured 3D Gaussians for View-Adaptive Rendering
- **🧑‍🔬 作者**：Tao Lu, Mulin Yu, Linning Xu, Yuanbo Xiangli, Limin Wang, Dahua Lin, Bo Dai
- **🏫 单位**：Shanghai Artificial Intelligence Laboratory ⟐ The Chinese University of Hong Kong ⟐ Nanjing University ⟐ Cornell University
- **🔗 链接**：[[中英摘要](./abs/2312.00109.md)] [[arXiv:2312.00109](https://arxiv.org/abs/2312.00109)] [[Code](https://github.com/city-super/Scaffold-GS)]
- **📝 说明**：✏️

#### [39] DynMF: Neural Motion Factorization for Real-time Dynamic View Synthesis with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Agelos Kratimenos, Jiahui Lei, Kostas Daniilidis
- **🏫 单位**：University of Pennsylvania
- **🔗 链接**：[[中英摘要](./abs/2312.00112.md)] [[arXiv:2312.00112](https://arxiv.org/abs/2312.00112)] [[Code](https://github.com/agelosk/dynmf)]
- **📝 说明**：✏️

#### [40] SparseGS: Real-Time 360° Sparse View Synthesis using Gaussian Splatting
- **🧑‍🔬 作者**：Haolin Xiong, Sairisheek Muttukuru, Rishi Upadhyay, Pradyumna Chari, Achuta Kadambi
- **🏫 单位**：University of California, Los Angeles
- **🔗 链接**：[[中英摘要](./abs/2312.00206.md)] [[arXiv:2312.00206](https://arxiv.org/abs/2312.00206)] [Code]
- **📝 说明**：✏️

#### [41] FSGS: Real-Time Few-shot View Synthesis using Gaussian Splatting
- **🧑‍🔬 作者**：Zehao Zhu, Zhiwen Fan, Yifan Jiang, Zhangyang Wang
- **🏫 单位**：University of Texas at Austin
- **🔗 链接**：[[中英摘要](./abs/2312.00451.md)] [[arXiv:2312.00451](https://arxiv.org/abs/2312.00451)] [[Code](https://github.com/VITA-Group/FSGS)]
- **📝 说明**：✏️

#### [42] MD-Splatting: Learning Metric Deformation from 4D Gaussians in Highly Deformable Scenes
- **🧑‍🔬 作者**：Bardienus P. Duisterhof, Zhao Mandi, Yunchao Yao, Jia-Wei Liu, Mike Zheng Shou, Shuran Song, Jeffrey Ichnowski
- **🏫 单位**：National University of Singapore ⟐ Stanford University ⟐ Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2312.00583.md)] [[arXiv:2312.00583](https://arxiv.org/abs/2312.00583)] [[Code](https://github.com/momentum-robotics-lab/md-splatting)]
- **📝 说明**：✏️

#### [43] Gaussian Grouping: Segment and Edit Anything in 3D Scenes
- **🧑‍🔬 作者**：Mingqiao Ye, Martin Danelljan, Fisher Yu, Lei Ke
- **🏫 单位**：ETH Zurich
- **🔗 链接**：[[中英摘要](./abs/2312.00732.md)] [[arXiv:2312.00732](https://arxiv.org/abs/2312.00732)] [[Code](https://github.com/lkeab/gaussian-grouping)]
- **📝 说明**：✏️

#### [44] NeuSG: Neural Implicit Surface Reconstruction with 3D Gaussian Splatting Guidance
- **🧑‍🔬 作者**：Hanlin Chen, Chen Li, Gim Hee Lee
- **🏫 单位**：National University of Singapore
- **🔗 链接**：[[中英摘要](./abs/2312.00846.md)] [[arXiv:2312.00846](https://arxiv.org/abs/2312.00846)] [Code]
- **📝 说明**：✏️

#### [45] Segment Any 3D Gaussians
- **🧑‍🔬 作者**：Jiazhong Cen, Jiemin Fang, Chen Yang, Lingxi Xie, Xiaopeng Zhang, Wei Shen, Qi Tian
- **🏫 单位**：Shanghai Jiao Tong University ⟐ Huawei Inc.
- **🔗 链接**：[[中英摘要](./abs/2312.00860.md)] [[arXiv:2312.00860](https://arxiv.org/abs/2312.00860)] [[Code](https://github.com/Jumpat/SegAnyGAussians)]
- **📝 说明**：✏️

#### [46] Neural Parametric Gaussians for Monocular Non-Rigid Object Reconstruction
- **🧑‍🔬 作者**：Devikalyan Das, Christopher Wewer, Raza Yunus, Eddy Ilg, Jan Eric Lenssen
- **🏫 单位**：Saarland University ⟐ Max Planck Institute for Informatics
- **🔗 链接**：[[中英摘要](./abs/2312.01196.md)] [[arXiv:2312.01196](https://arxiv.org/abs/2312.01196)] [Code]
- **📝 说明**：✏️

#### [47] GaussianHead: Impressive 3D Gaussian-based Head Avatars with Dynamic Hybrid Neural Field
- **🧑‍🔬 作者**：Jie Wang, Xianyan Li, Jiucheng Xie, Feng Xu, Hao Gao
- **🏫 单位**：Nanjing University of Posts and Telecommunications ⟐ Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2312.01632.md)] [[arXiv:2312.01632](https://arxiv.org/abs/2312.01632)] [[Code](https://github.com/chiehwangs/gaussian-head)]
- **📝 说明**：✏️

#### [48] GaussianAvatars: Photorealistic Head Avatars with Rigged 3D Gaussians
- **🧑‍🔬 作者**：Shenhan Qian, Tobias Kirschstein, Liam Schoneveld, Davide Davoli, Simon Giebenhain, Matthias Nießner
- **🏫 单位**：Technical University of Munich ⟐ Woven by Toyota ⟐ Toyota Motor Europe NV/SA
- **🔗 链接**：[[中英摘要](./abs/2312.02069.md)] [[arXiv:2312.02069](https://arxiv.org/abs/2312.02069)] [Code]
- **📝 说明**：✏️

#### [49] SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM
- **🧑‍🔬 作者**：Nikhil Keetha, Jay Karhade, Krishna Murthy Jatavallabhula, Gengshan Yang, Sebastian Scherer, Deva Ramanan, Jonathon Luiten
- **🏫 单位**：CMU ⟐ MIT
- **🔗 链接**：[[中英摘要](./abs/2312.02126.md)] [[arXiv:2312.02126](https://arxiv.org/abs/2312.02126)] [[Code](https://github.com/spla-tam/SplaTAM)]
- **📝 说明**：✏

#### [50] GaussianAvatar: Towards Realistic Human Avatar Modeling from a Single Video via Animatable 3D Gaussians
- **🧑‍🔬 作者**：Liangxiao Hu, Hongwen Zhang, Yuxiang Zhang, Boyao Zhou, Boning Liu, Shengping Zhang, Liqiang Nie
- **🏫 单位**：Harbin Institute of Technology ⟐ Beijing Normal University ⟐  Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2312.02134.md)] [[arXiv:2312.02134](https://arxiv.org/abs/2312.02134)] [[Code](https://github.com/huliangxiao/GaussianAvatar)]
- **📝 说明**：✏️

#### [51] MANUS: Markerless Hand-Object Grasp Capture using Articulated 3D Gaussians
- **🧑‍🔬 作者**：Chandradeep Pokhariya, Ishaan N Shah, Angela Xing, Zekun Li, Kefan Chen, Avinash Sharma, Srinath Sridhar
- **🏫 单位**：IIIT Hyderabad ⟐ Brown University
- **🔗 链接**：[[中英摘要](./abs/2312.02137.md)] [[arXiv:2312.02137](https://arxiv.org/abs/2312.02137)] [Code]
- **📝 说明**：✏️

#### [52] GPS-Gaussian: Generalizable Pixel-wise 3D Gaussian Splatting for Real-time Human Novel View Synthesis
- **🧑‍🔬 作者**：Shunyuan Zheng, Boyao Zhou, Ruizhi Shao, Boning Liu, Shengping Zhang, Liqiang Nie, Yebin Liu
- **🏫 单位**：Harbin Institute of Technology ⟐ Tsinghua University
- **🔗 链接**：[[中英摘要](./abs/2312.02155.md)] [[arXiv:2312.02155](https://arxiv.org/abs/2312.02155)] [[Code](https://github.com/ShunyuanZheng/GPS-Gaussian)]
- **📝 说明**：✏️

#### [53] HeadGaS: Real-Time Animatable Head Avatars via 3D Gaussian Splatting
- **🧑‍🔬 作者**：Helisa Dhamo, Yinyu Nie, Arthur Moreau, Jifei Song, Richard Shaw, Yiren Zhou, Eduardo Pérez-Pellitero
- **🏫 单位**：Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2312.02902.md)] [[arXiv:2312.02902](https://arxiv.org/abs/2312.02902)] [Code]
- **📝 说明**：✏️

#### [54] Gaussian Head Avatar: Ultra High-fidelity Head Avatar via Dynamic Gaussians
- **🧑‍🔬 作者**：Yuelang Xu, Benwang Chen, Zhe Li, Hongwen Zhang, Lizhen Wang, Zerong Zheng, Yebin Liu
- **🏫 单位**：Tsinghua University ⟐ NNKosmos
- **🔗 链接**：[[中英摘要](./abs/2312.03029.md)] [[arXiv:2312.03029](https://arxiv.org/abs/2312.03029)] [[Code](https://github.com/YuelangX/Gaussian-Head-Avatar)]
- **📝 说明**：✏️

#### [55] Feature 3DGS: Supercharging 3D Gaussian Splatting to Enable Distilled Feature Fields
- **🧑‍🔬 作者**：Shijie Zhou, Haoran Chang, Sicheng Jiang, Zhiwen Fan, Zehao Zhu, Dejia Xu, Pradyumna Chari, Suya You, Zhangyang Wang, Achuta Kadambi
- **🏫 单位**：University of California, Los Angeles ⟐ University of Texas at Austin ⟐ DEVCOM Army Research Laboratory
- **🔗 链接**：[[中英摘要](./abs/2312.03203.md)] [[arXiv:2312.03203](https://arxiv.org/abs/2312.03203)] [Code]
- **📝 说明**：✏️

#### [56] Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle
- **🧑‍🔬 作者**：Youtian Lin, Zuozhuo Dai, Siyu Zhu, Yao Yao
- **🏫 单位**：Nanjing University ⟐ Alibaba Group ⟐ Fudan University
- **🔗 链接**：[[中英摘要](./abs/2312.03431.md)] [[arXiv:2312.03431](https://arxiv.org/abs/2312.03431)] [Code]
- **📝 说明**：✏️

#### [57] HiFi4G: High-Fidelity Human Performance Rendering via Compact Gaussian Splatting
- **🧑‍🔬 作者**：Yuheng Jiang, Zhehao Shen, Penghao Wang, Zhuo Su, Yu Hong, Yingliang Zhang, Jingyi Yu, Lan Xu
- **🏫 单位**：ShanghaiTech University ⟐ NeuDim ⟐ ByteDance ⟐ DGene
- **🔗 链接**：[[中英摘要](./abs/2312.03461.md)] [[arXiv:2312.03461](https://arxiv.org/abs/2312.03461)] [Code]
- **📝 说明**：✏️

#### [58] Relightable Gaussian Codec Avatars
- **🧑‍🔬 作者**：Shunsuke Saito, Gabriel Schwartz, Tomas Simon, Junxuan Li, Giljoo Nam
- **🏫 单位**：Codec Avatars Lab, Meta
- **🔗 链接**：[[中英摘要](./abs/2312.03704.md)] [[arXiv:2312.03704](https://arxiv.org/abs/2312.03704)] [Code]
- **📝 说明**：✏️

#### [59] MonoGaussianAvatar: Monocular Gaussian Point-based Head Avatar
- **🧑‍🔬 作者**：Yufan Chen, Lizhen Wang, Qijing Li, Hongjiang Xiao, Shengping Zhang, Hongxun Yao, Yebin Liu
- **🏫 单位**：Harbin Institute of Technology ⟐ Tsinghua University ⟐ Communication University of China
- **🔗 链接**：[[中英摘要](./abs/2312.04558.md)] [[arXiv:2312.04558](https://arxiv.org/abs/2312.04558)] [[Code](https://github.com/yufan1012/MonoGaussianAvatar)]
- **📝 说明**：✏️

#### [60] EAGLES: Efficient Accelerated 3D Gaussians with Lightweight EncodingS
- **🧑‍🔬 作者**：Sharath Girish, Kamal Gupta, Abhinav Shrivastava
- **🏫 单位**：University of Maryland
- **🔗 链接**：[[中英摘要](./abs/2312.04564.md)] [[arXiv:2312.04564](https://arxiv.org/abs/2312.04564)] [[Code](https://github.com/Sharath-girish/efficientgaussian)]
- **📝 说明**：✏️

#### [61] Learn to Optimize Denoising Scores for 3D Generation: A Unified and Improved Diffusion Prior on NeRF and 3D Gaussian Splatting
- **🧑‍🔬 作者**：Xiaofeng Yang, Yiwen Chen, Cheng Chen, Chi Zhang, Yi Xu, Xulei Yang, Fayao Liu, Guosheng Lin
- **🏫 单位**：Nanyang Technological University ⟐ OPPO US Research Center ⟐ A*STAR
- **🔗 链接**：[[中英摘要](./abs/2312.04820.md)] [[arXiv:2312.04820](https://arxiv.org/abs/2312.04820)] [Code]
- **📝 说明**：✏️

#### [62] GIR: 3D Gaussian Inverse Rendering for Relightable Scene Factorization
- **🧑‍🔬 作者**：Yahao Shi, Yanmin Wu, Chenming Wu, Xing Liu, Chen Zhao, Haocheng Feng, Jingtuo Liu, Liangjun Zhang, Jian Zhang, Bin Zhou, Errui Ding, Jingdong Wang
- **🏫 单位**：Beihang University ⟐ Peking University ⟐ Baidu VIS
- **🔗 链接**：[[中英摘要](./abs/2312.05133.md)] [[arXiv:2312.05133](https://arxiv.org/abs/2312.05133)] [Code]
- **📝 说明**：✏️

#### [63] ASH: Animatable Gaussian Splats for Efficient and Photoreal Human Rendering
- **🧑‍🔬 作者**：Haokai Pang, Heming Zhu, Adam Kortylewski, Christian Theobalt, Marc Habermann
- **🏫 单位**：Max Planck Institute for Informatics ⟐ ETH Zurich ⟐  Universitat Freiburg ⟐ Saarbrucken Research Center for Visual Computing, Interaction and AI
- **🔗 链接**：[[中英摘要](./abs/2312.05941.md)] [[arXiv:2312.05941](https://arxiv.org/abs/2312.05941)] [Code]
- **📝 说明**：✏️

#### [64] Gaussian Splatting SLAM
- **🧑‍🔬 作者**：Hidenobu Matsuki, Riku Murai, Paul H.J. Kelly, Andrew J. Davison
- **🏫 单位**：Imperial College London
- **🔗 链接**：[[中英摘要](./abs/2312.06741.md)] [[arXiv:2312.06741](https://arxiv.org/abs/2312.06741)] [Code]
- **📝 说明**：✏️

#### [65] COLMAP-Free 3D Gaussian Splatting
- **🧑‍🔬 作者**：Yang Fu, Sifei Liu, Amey Kulkarni, Jan Kautz, Alexei A. Efros, Xiaolong Wang
- **🏫 单位**：UC San Deigo ⟐ NVIDIA ⟐ 3UC Berkeley
- **🔗 链接**：[[中英摘要](./abs/2312.07504.md)] [[arXiv:2312.07504](https://arxiv.org/abs/2312.07504)] [Code]
- **📝 说明**：✏️

#### [66] DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes
- **🧑‍🔬 作者**：Xiaoyu Zhou, Zhiwei Lin, Xiaojun Shan, Yongtao Wang, Deqing Sun, Ming-Hsuan Yang
- **🏫 单位**：Peking University ⟐ Google Research ⟐ University of California, Merced
- **🔗 链接**：[[中英摘要](./abs/2312.07920.md)] [[arXiv:2312.07920](https://arxiv.org/abs/2312.07920)] [Code]
- **📝 说明**：✏️

#### [67] iComMa: Inverting 3D Gaussians Splatting for Camera Pose Estimation via Comparing and Matching
- **🧑‍🔬 作者**：Yuan Sun, Xuan Wang, Yunfan Zhang, Jie Zhang, Caigui Jiang, Yu Guo, Fei Wang
- **🏫 单位**：Xi’an Jiaotong University ⟐ Ant Group
- **🔗 链接**：[[中英摘要](./abs/2312.09031.md)] [[arXiv:2312.09031](https://arxiv.org/abs/2312.09031)] [Code]
- **📝 说明**：✏️

#### [68] Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers
- **🧑‍🔬 作者**：Zi-Xin Zou, Zhipeng Yu, Yuan-Chen Guo, Yangguang Li, Ding Liang, Yan-Pei Cao, Song-Hai Zhang
- **🏫 单位**：Tsinghua University ⟐ VAST
- **🔗 链接**：[[中英摘要](./abs/2312.09147.md)] [[arXiv:2312.09147](https://arxiv.org/abs/2312.09147)] [Code]
- **📝 说明**：✏️

#### [69] 3DGS-Avatar: Animatable Avatars via Deformable 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zhiyin Qian, Shaofei Wang, Marko Mihajlovic, Andreas Geiger, Siyu Tang
- **🏫 单位**：ETH Zürich ⟐ University of Tübingen ⟐ Tübingen AI Center
- **🔗 链接**：[[中英摘要](./abs/2312.09228.md)] [[arXiv:2312.09228](https://arxiv.org/abs/2312.09228)] [[Code](https://github.com/mikeqzy/3dgs-avatar-release)]
- **📝 说明**：✏️

#### [70] Text2Immersion: Generative Immersive Scene with 3D Gaussians
- **🧑‍🔬 作者**：Hao Ouyang, Kathryn Heal, Stephen Lombardi, Tiancheng Sun
- **🏫 单位**：HKUST ⟐ Google
- **🔗 链接**：[[中英摘要](./abs/2312.09242.md)] [[arXiv:2312.09242](https://arxiv.org/abs/2312.09242)] [Code]
- **📝 说明**：✏️

#### [71] Exploring the Feasibility of Generating Realistic 3D Models of Endangered Species Using DreamGaussian: An Analysis of Elevation Angle's Impact on Model Generation
- **🧑‍🔬 作者**：Selcuk Anil Karatopak, Deniz Sen
- **🏫 单位**：Huawei Türkiye R&D Center
- **🔗 链接**：[[中英摘要](./abs/2312.09682.md)] [[arXiv:2312.09682](https://arxiv.org/abs/2312.09682)] [Code]
- **📝 说明**：✏️

#### [72] GauFRe: Gaussian Deformation Fields for Real-time Dynamic Novel View Synthesis
- **🧑‍🔬 作者**：Yiqing Liang, Numair Khan, Zhengqin Li, Thu Nguyen-Phuoc, Douglas Lanman, James Tompkin, Lei Xiao
- **🏫 单位**：Meta ⟐ Brown University
- **🔗 链接**：[[中英摘要](./abs/2312.11458.md)] [[arXiv:2312.11458](https://arxiv.org/abs/2312.11458)] [[Supp](https://lynl7130.github.io/gaufre/static/pdfs/suppl.pdf)] [Code]
- **📝 说明**：✏️

#### [73] GAvatar: Animatable 3D Gaussian Avatars with Implicit Mesh Learning
- **🧑‍🔬 作者**：Ye Yuan, Xueting Li, Yangyi Huang, Shalini De Mello, Koki Nagano, Jan Kautz, Umar Iqbal
- **🏫 单位**：NVIDIA
- **🔗 链接**：[[中英摘要](./abs/2312.11461.md)] [[arXiv:2312.11461](https://arxiv.org/abs/2312.11461)]
- **📝 说明**：✏️

#### [74] pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction
- **🧑‍🔬 作者**：David Charatan, Sizhe Li, Andrea Tagliasacchi, Vincent Sitzmann
- **🏫 单位**：Massachusetts Institute of Technology ⟐ Simon Fraser University ⟐ University of Toronto
- **🔗 链接**：[[中英摘要](./abs/2312.12337.md)] [[arXiv:2312.12337](https://arxiv.org/abs/2312.12337)] [[Code](https://github.com/dcharatan/pixelsplat)]
- **📝 说明**：✏️

#### [75] SpecNeRF: Gaussian Directional Encoding for Specular Reflections
- **🧑‍🔬 作者**：Li Ma, Vasu Agrawal, Haithem Turki, Changil Kim, Chen Gao, Pedro Sander, Michael Zollhöfer, Christian Richardt
- **🏫 单位**：The Hong Kong University of Science and Technology ⟐ Meta Reality Labs ⟐ Carnegie Mellon University
- **🔗 链接**：[[中英摘要](./abs/2312.13102.md)] [[arXiv:2312.13102](https://arxiv.org/abs/2312.13102)] [Code]
- **📝 说明**：✏️

#### [76] Splatter Image: Ultra-Fast Single-View 3D Reconstruction
- **🧑‍🔬 作者**：Stanislaw Szymanowicz, Christian Rupprecht, Andrea Vedaldi
- **🏫 单位**：University of Oxford (VGG)
- **🔗 链接**：[[中英摘要](./abs/2312.13150.md)] [[arXiv:2312.13150](https://arxiv.org/abs/2312.13150)] [[Code](https://github.com/szymanowiczs/splatter-image)]
- **📝 说明**：✏️

#### [77] Repaint123: Fast and High-quality One Image to 3D Generation with Progressive Controllable 2D Repainting
- **🧑‍🔬 作者**：Junwu Zhang, Zhenyu Tang, Yatian Pang, Xinhua Cheng, Peng Jin, Yida Wei, Munan Ning, Li Yuan
- **🏫 单位**：Peking University ⟐ Pengcheng Laboratory ⟐  National University of Singapore ⟐ Wuhan University
- **🔗 链接**：[[中英摘要](./abs/2312.13271.md)] [[arXiv:2312.13271](https://arxiv.org/abs/2312.13271)] [[Code](https://github.com/PKU-YuanGroup/repaint123)]
- **📝 说明**：✏️

#### [78] Compact 3D Scene Representation via Self-Organizing Gaussian Grids
- **🧑‍🔬 作者**：Wieland Morgenstern, Florian Barthel, Anna Hilsmann, Peter Eisert
- **🏫 单位**：Fraunhofer Heinrich Hertz Institute ⟐ Humboldt University of Berlin
- **🔗 链接**：[[中英摘要](./abs/2312.13299.md)] [[arXiv:2312.13299](https://arxiv.org/abs/2312.13299)] [[Code](https://github.com/fraunhoferhhi/Self-Organizing-Gaussians)]
- **📝 说明**：✏️

#### [79] SWAGS: Sampling Windows Adaptively for Dynamic 3D Gaussian Splatting
- **🧑‍🔬 作者**：Richard Shaw, Jifei Song, Arthur Moreau, Michal Nazarczuk, Sibi Catley-Chandar, Helisa Dhamo, Eduardo Perez-Pellitero
- **🏫 单位**：Huawei Noah’s Ark Lab
- **🔗 链接**：[[中英摘要](./abs/2312.13308.md)] [[arXiv:2312.13308](https://arxiv.org/abs/2312.13308)] [Code]
- **📝 说明**：✏️

#### [80] Gaussian Splatting with NeRF-based Color and Opacity
- **🧑‍🔬 作者**：Dawid Malarz, Weronika Smolak, Jacek Tabor, Sławomir Tadeja, Przemysław Spurek
- **🏫 单位**：Jagiellonian University ⟐ University of Cambridge
- **🔗 链接**：[[中英摘要](./abs/2312.13729.md)] [[arXiv:2312.13729](https://arxiv.org/abs/2312.13729)] [[Code](https://github.com/gmum/ViewingDirectionGaussianSplatting)]
- **📝 说明**：✏️

#### [81] Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models
- **🧑‍🔬 作者**：Huan Ling, Seung Wook Kim, Antonio Torralba, Sanja Fidler, Karsten Kreis
- **🏫 单位**：NVIDIA ⟐ Vector Institute ⟐ University of Toronto ⟐ MIT
- **🔗 链接**：[[中英摘要](./abs/2312.13763.md)] [[arXiv:2312.13763](https://arxiv.org/abs/2312.13763)] [Code]
- **📝 说明**：✏️

#### [82] SC-GS: Sparse-Controlled Gaussian Splatting for Editable Dynamic Scenes
- **🧑‍🔬 作者**：Yi-Hua Huang, Yang-Tian Sun, Ziyi Yang, Xiaoyang Lyu, Yan-Pei Cao, Xiaojuan Qi
- **🏫 单位**：The University of Hong Kong ⟐ VAST ⟐ Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2312.14937.md)] [[arXiv:2312.14937](https://arxiv.org/abs/2312.14937)] [Code]
- **📝 说明**：✏️

#### [83] Deformable 3D Gaussian Splatting for Animatable Human Avatars
- **🧑‍🔬 作者**：HyunJun Jung, Nikolas Brasch, Jifei Song, Eduardo Perez-Pellitero, Yiren Zhou, Zhihao Li, Nassir Navab, Benjamin Busam
- **🏫 单位**：Technical University of Munich ⟐ Huawei Noah’s Ark Lab ⟐ 3dwe.ai
- **🔗 链接**：[[中英摘要](./abs/2312.15059.md)] [[arXiv:2312.15059](https://arxiv.org/abs/2312.15059)] [[Code](https://github.com/Junggy/pardy-human)]
- **📝 说明**：Code link 404

#### [84] Human101: Training 100+FPS Human Gaussians in 100s from 1 View
- **🧑‍🔬 作者**：Mingwei Li, Jiachen Tao, Zongxin Yang, Yi Yang
- **🏫 单位**：Zhejiang University
- **🔗 链接**：[[中英摘要](./abs/2312.15258.md)] [[arXiv:2312.15258](https://arxiv.org/abs/2312.15258)] [[Code](https://github.com/longxiang-ai/Human101)]
- **📝 说明**：✏️

#### [85] Sparse-view CT Reconstruction with 3D Gaussian Volumetric Representation
- **🧑‍🔬 作者**：Yingtai Li, Xueming Fu, Shang Zhao, Ruiyang Jin, S. Kevin Zhou
- **🏫 单位**：University of Science and Technology of China ⟐ Chinese Academy of Sciences
- **🔗 链接**：[[中英摘要](./abs/2312.15676.md)] [[arXiv:2312.15676](https://arxiv.org/abs/2312.15676)] [Code]
- **📝 说明**：✏️

#### [86] 2D-Guided 3D Gaussian Segmentation
- **🧑‍🔬 作者**：Kun Lan, Haoran Li, Haolin Shi, Wenjun Wu, Yong Liao, Lin Wang, Pengyuan Zhou
- **🏫 单位**：University of Science and Technology of China ⟐ HKUST(GZ)
- **🔗 链接**：[[中英摘要](./abs/2312.16047.md)] [[arXiv:2312.16047](https://arxiv.org/abs/2312.16047)] [Code]
- **📝 说明**：✏️

#### [87] LangSplat: 3D Language Gaussian Splatting
- **🧑‍🔬 作者**：Minghan Qin, Wanhua Li, Jiawei Zhou, Haoqian Wang, Hanspeter Pfister
- **🏫 单位**：Tsinghua University ⟐ Harvard University
- **🔗 链接**：[[中英摘要](./abs/2312.16084.md)] [[arXiv:2312.16084](https://arxiv.org/abs/2312.16084)] [[Code](https://github.com/minghanqin/LangSplat)]
- **📝 说明**：✏️

#### [88] Spacetime Gaussian Feature Splatting for Real-Time Dynamic View Synthesis
- **🧑‍🔬 作者**：Zhan Li, Zhang Chen, Zhong Li, Yi Xu
- **🏫 单位**：OPPO US Research Center ⟐ Portland State University
- **🔗 链接**：[[中英摘要](./abs/2312.16812.md)] [[arXiv:2312.16812](https://arxiv.org/abs/2312.16812)] [[Code](https://github.com/oppo-us-research/SpacetimeGaussians)]
- **📝 说明**：✏️

#### [89] DreamGaussian4D: Generative 4D Gaussian Splatting
- **🧑‍🔬 作者**：Jiawei Ren, Liang Pan, Jiaxiang Tang, Chi Zhang, Ang Cao, Gang Zeng, Ziwei Liu
- **🏫 单位**：Nanyang Technological University ⟐ Shanghai AI Laboratory ⟐ Peking University ⟐ University of Michigan
- **🔗 链接**：[[中英摘要](./abs/2312.17142.md)] [[arXiv:2312.17142](https://arxiv.org/abs/2312.17142)] [[Code](https://github.com/jiawei-ren/dreamgaussian4d)]
- **📝 说明**：✏️

#### [90] 4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency
- **🧑‍🔬 作者**：Yuyang Yin, Dejia Xu, Zhangyang Wang, Yao Zhao, Yunchao Wei
- **🏫 单位**：Beijing Jiaotong University ⟐ University of Texas at Austin
- **🔗 链接**：[[中英摘要](./abs/2312.17225.md)] [[arXiv:2312.17225](https://arxiv.org/abs/2312.17225)] [[Code](https://github.com/VITA-Group/4DGen)]
- **📝 说明**：✏️

#### [91] Deblurring 3D Gaussian Splatting
- **🧑‍🔬 作者**：Byeonghyeon Lee, Howoong Lee, Xiangyu Sun, Usman Ali, Eunbyung Park
- **🏫 单位**：Sungkyunkwan University ⟐ Hanhwa Vision
- **🔗 链接**：[[中英摘要](./abs/2401.00834.md)] [[arXiv:2401.00834](https://arxiv.org/abs/2401.00834)] [[Code](https://github.com/benhenryL/Deblurring-3D-Gaussian-Splatting)]
- **📝 说明**：✏️

#### [92] Street Gaussians for Modeling Dynamic Urban Scenes
- **🧑‍🔬 作者**：Yunzhi Yan, Haotong Lin, Chenxu Zhou, Weijie Wang, Haiyang Sun, Kun Zhan, Xianpeng Lang, Xiaowei Zhou, Sida Peng
- **🏫 单位**：Zhejiang University ⟐ Li Auto
- **🔗 链接**：[[中英摘要](./abs/2401.01339.md)] [[arXiv:2401.01339](https://arxiv.org/abs/2401.01339)] [[Code](https://github.com/zju3dv/street_gaussians)]
- **📝 说明**：✏️

#### [93] FMGS: Foundation Model Embedded 3D Gaussian Splatting for Holistic 3D Scene Understanding
- **🧑‍🔬 作者**：Xingxing Zuo, Pouya Samangouei, Yunwen Zhou, Yan Di, Mingyang Li
- **🏫 单位**：Google
- **🔗 链接**：[[中英摘要](./abs/2401.01970.md)] [[arXiv:2401.01970](https://arxiv.org/abs/2401.01970)] [Code]
- **📝 说明**：✏️

#### [94] PEGASUS: Physically Enhanced Gaussian Splatting Simulation System for 6DOF Object Pose Dataset Generation
- **🧑‍🔬 作者**：Lukas Meyer, Floris Erich, Yusuke Yoshiyasu, Marc Stamminger, Noriaki Ando, Yukiyasu Domae
- **🏫 单位**：Friedrich-Alexander-Universität Erlangen-Nürnberg-Fürth ⟐ Industrial CPS Research Center, National Institute of Advanced Industrial Science and Technology, Japan
- **🔗 链接**：[[中英摘要](./abs/2401.02281.md)] [[arXiv:2401.02281](https://arxiv.org/abs/2401.02281)] [[Code](https://github.com/meyerls/PEGASUS)]
- **📝 说明**：✏️

#### [95] Compressed 3D Gaussian Splatting for Accelerated Novel View Synthesis
- **🧑‍🔬 作者**：Simon Niedermayr, Josef Stumpfegger, Rüdiger Westermann
- **🏫 单位**：Technical University of Munich
- **🔗 链接**：[[中英摘要](./abs/2401.02436.md)] [[arXiv:2401.02436](https://arxiv.org/abs/2401.02436)] [Code]
- **📝 说明**：✏️

#### [96] Characterizing Satellite Geometry via Accelerated 3D Gaussian Splatting
- **🧑‍🔬 作者**：Van Minh Nguyen, Emma Sandidge, Trupti Mahendrakar, Ryan T. White
- **🏫 单位**：Florida Institute of Technology
- **🔗 链接**：[[中英摘要](./abs/2401.02588.md)] [[arXiv:2401.02588](https://arxiv.org/abs/2401.02588)] [Code]
- **📝 说明**：✏️

#### [97] AGG: Amortized Generative 3D Gaussians for Single Image to 3D
- **🧑‍🔬 作者**：Dejia Xu, Ye Yuan, Morteza Mardani, Sifei Liu, Jiaming Song, Zhangyang Wang, Arash Vahdat
- **🏫 单位**：The University of Texas at Austin ⟐ NVIDIA
- **🔗 链接**：[[中英摘要](./abs/2401.04099.md)] [[arXiv:2401.04099](https://arxiv.org/abs/2401.04099)] [Code]
- **📝 说明**：✏️

#### [98] DISTWAR: Fast Differentiable Rendering on Raster-based Rendering Pipelines
- **🧑‍🔬 作者**：Sankeerth Durvasula, Adrian Zhao, Fan Chen, Ruofan Liang, Pawan Kumar Sanjaya, Nandita Vijaykumar
- **🏫 单位**：University of Toronto
- **🔗 链接**：[[中英摘要](./abs/2401.05345.md)] [[arXiv:2401.05345](https://arxiv.org/abs/2401.05345)] [Code]
- **📝 说明**：✏️

#### [99] CoSSegGaussians: Compact and Swift Scene Segmenting 3D Gaussians
- **🧑‍🔬 作者**：Bin Dou, Tianyu Zhang, Yongjia Ma, Zhaohui Wang, Zejian Yuan
- **🏫 单位**：Xi’an Jiaotong University
- **🔗 链接**：[[中英摘要](./abs/2401.05925.md)] [[arXiv:2401.05925](https://arxiv.org/abs/2401.05925)] [Code]
- **📝 说明**：✏️

#### [100] TRIPS: Trilinear Point Splatting for Real-Time Radiance Field Rendering
- **🧑‍🔬 作者**：Linus Franke, Darius Rückert, Laura Fink, Marc Stamminger
- **🏫 单位**：Friedrich-Alexander-Universität Erlangen-Nürnberg
- **🔗 链接**：[[中英摘要](./abs/2401.06003.md)] [[arXiv:2401.06003](https://arxiv.org/abs/2401.06003)] [[Code](https://github.com/lfranke/trips)]
- **📝 说明**：✏️

#### [101] Fast Dynamic 3D Object Generation from a Single-view Video
- **🧑‍🔬 作者**：Zijie Pan, Zeyu Yang, Xiatian Zhu, Li Zhang
- **🏫 单位**：Fudan University ⟐ University of Surrey
- **🔗 链接**：[[中英摘要](./abs/2401.08742.md)] [[arXiv:2401.08742](https://arxiv.org/abs/2401.08742)] [[Code](https://github.com/fudan-zvg/Efficient4D)]
- **📝 说明**：✏️

#### [102] GaussianBody: Clothed Human Reconstruction via 3d Gaussian Splatting
- **🧑‍🔬 作者**：Mengtian Li, Shengxiang Yao, Zhifeng Xie, Keyu Chen, Yu-Gang Jiang
- **🏫 单位**：Shanghai University ⟐ Fudan University ⟐ Shanghai Engineering Research Center of Motion Picture Special Effects ⟐ Tavus Inc.
- **🔗 链接**：[[中英摘要](./abs/2401.09720.md)] [[arXiv:2401.09720](https://arxiv.org/abs/2401.09720)] [Code]
- **📝 说明**：✏️

#### [103] Deformable Endoscopic Tissues Reconstruction with Gaussian Splatting
- **🧑‍🔬 作者**：Lingting Zhu, Zhao Wang, Zhenchao Jin, Guying Lin, Lequan Yu
- **🏫 单位**：The University of Hong Kong ⟐  The Chinese University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2401.11535.md)] [[arXiv:2401.11535](https://arxiv.org/abs/2401.11535)] [[Code](https://github.com/HKU-MedAI/EndoGS)]
- **📝 说明**：✏️

#### [104] EndoGaussian: Gaussian Splatting for Deformable Surgical Scene Reconstruction
- **🧑‍🔬 作者**：Yifan Liu, Chenxin Li, Chen Yang, Yixuan Yuan
- **🏫 单位**：Chinese University of Hong Kong
- **🔗 链接**：[[中英摘要](./abs/2401.12561.md)] [[arXiv:2401.12561](https://arxiv.org/abs/2401.12561)] [[Code](https://github.com/yifliu3/EndoGaussian)]
- **📝 说明**：✏️

#### [105] PSAvatar: A Point-based Morphable Shape Model for Real-Time Head Avatar Creation with 3D Gaussian Splatting
- **🧑‍🔬 作者**：Zhongyuan Zhao, Zhenyu Bao, Qing Li, Guoping Qiu, Kanglin Liu
- **🏫 单位**：Pengcheng Laboratory ⟐ Peking University ⟐ University of Nottingham ⟐ Shenzhen University
- **🔗 链接**：[[中英摘要](./abs/2401.12900.md)] [[arXiv:2401.12900](https://arxiv.org/abs/2401.12900)] [Code]
- **📝 说明**：✏️

#### [106] LIV-GaussMap: LiDAR-Inertial-Visual Fusion for Real-time 3D Radiance Field Map Rendering
- **🧑‍🔬 作者**：Sheng Hong, Junjie He, Xinhu Zheng, Hesheng Wang, Hao Fang, Kangcheng Liu, Chunran Zheng, Shaojie Shen
- **🏫 单位**：HKUST
- **🔗 链接**：[[中英摘要](./abs/2401.14857.md)] [[arXiv:2401.14857](https://arxiv.org/abs/2401.14857)] [[Code](https://github.com/sheng00125/LIV-GaussMap)]
- **📝 说明**：✏️  Empty code repo

#### [107] Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting
- **🧑‍🔬 作者**：Yutao Feng, Xiang Feng, Yintong Shang, Ying Jiang, Chang Yu, Zeshun Zong, Tianjia Shao, Hongzhi Wu, Kun Zhou, Chenfanfu Jiang, Yin Yang
- **🏫 单位**：University of Utah ⟐ Zhejiang University ⟐ UCLA
- **🔗 链接**：[[中英摘要](./abs/2401.15318.md)] [[arXiv:2401.15318](https://arxiv.org/abs/2401.15318)] [Code]
- **📝 说明**：✏️

#### [108] Endo-4DGS: Distilling Depth Ranking for Endoscopic Monocular Scene Reconstruction with 4D Gaussian Splatting
- **🧑‍🔬 作者**：Yiming Huang, Beilei Cui, Long Bai, Ziqi Guo, Mengya Xu, Hongliang Ren
- **🏫 单位**：The Chinese University of Hong Kong ⟐  Shun Hing Institute of Advanced Engineering, CUHK ⟐ Shenzhen Research Institute, CUHK
- **🔗 链接**：[[中英摘要](./abs/2401.16416.md)] [[arXiv:2401.16416](https://arxiv.org/abs/2401.16416)] [Code]
- **📝 说明**：✏️
