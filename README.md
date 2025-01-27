# Deep Learning Frameworks
+ PyTorch
+ Tensorflow

# Inference Frameworks
+ [TNN](https://github.com/Tencent/TNN): Support ARM, OpenCL, Metal, Huawei NPU, Apple NPU, X86, CUDA
+ [NCNN](https://github.com/Tencent/ncnn): A high-performance neural network inference framework optimized for mobile platforms. Support Android(Qualcomm CPU and GPU, ARM CPU and GPU), IOS(Apple CPU and GPU), HarmonyOS, MacOS(Intel CPU, AMD CPU, Apple CPU and GPU), Windows(Intel, AMD, Nvidia GPU), Linux(Intel, AMD, Qualcomm)
+ [TensorRT](https://github.com/NVIDIA/TensorRT)
+ [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)
+ ONNXRuntime
+ [TVM](https://zhuanlan.zhihu.com/p/353660224)
+ [QNN](https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk?redirect=qdn): Qualcomm AI eigine
+ [MNN](https://github.com/alibaba/MNN): [Zhihu Page](https://zhuanlan.zhihu.com/p/64903359). Mobile inference engine from Alibaba.

# Training Frameworks
+ Megatron([GitHub Page](https://github.com/NVIDIA/Megatron-LM), [Paper](https://arxiv.org/abs/1909.08053)): Developed by NVidia, **built on top of PyTorch**, specifically optimized for training large-scale transformer models across multiple GPUs and nodes.Uses model parallelism and data parallelism to maximize GPU utilization. Primarily focused on transformer-based architectures like GPT, BERT, and their variants. 
+ [DeepSpeed](https://blog.csdn.net/myTomorrow_better/article/details/138945584)([Article](https://blog.csdn.net/weixin_53795646/article/details/143674918)): DeepSpeed 是由微软开发并维护的开源深度学习优化库，专注于提高大规模模型训练的效率和可扩展性。

# LLM
+ [LLaMA](https://github.com/meta-llama/llama3)
+ [Baichuan](https://github.com/baichuan-inc/Baichuan2)
+ [QWen](https://github.com/QwenLM/Qwen)

# LLM Related Techniques
+ RAG
+ [RLHF](https://huggingface.co/blog/rlhf)
+ ZeRO
+ [Pipeline Parallelism](https://zhuanlan.zhihu.com/p/613196255): GPipe from Google
+ [Flash Attention](https://zhuanlan.zhihu.com/p/676655352)
+ [LoRA](https://blog.csdn.net/m0_63171455/article/details/139614304): Low-Rank Adaptation

# Develop Frameworks
+ CUDA
+ OpenCL

# Loacalization
+ 寒武纪MLU: [Tutorials](https://developer.cambricon.com/index/curriculum/index/classid/7.html), MagicMind Inference Engine
+ 海光DCU

# Others
+ [ONNX](https://blog.csdn.net/weixin_44878336/article/details/135820896)
+ [NNAPI](https://developer.android.com/ndk/guides/neuralnetworks)
+ [CMake](https://blog.csdn.net/weixin_43717839/article/details/128032486)