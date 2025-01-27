# Fixed Shape(Implicit Batch)
Before TRT 6.0, the input shape is **half-fixed**, for example an image with shape (N, C, H, W), channel, height and width are fixed, batchSize can be any number which is smaller than maxBatchSize.  
For CV, fixed shape can be acceptable, as input images are in the same shape. But for NLP and audio, the length of input text can be variable.
```cpp
//Building phase
IBuilder::createNetwork();
IBuilder::setMaxBatchSize(maxBatchSize);
// Inference phase
enqueue(batchSize, data, stream, nullptr);
```

# Dynamic Shape(Explicit Batch)
TRT later than 6.0 supprts **dynamic shape**.
```cpp
//Building phase
IBuilder::createNetworkV2(...);
builder -> setMaxBatchSize(maxBatchSize);

OptimizationProfile* profile = builder.createOptimizationProfile();
// Min input dim
profile -> setDimensions("foo", OptProfileSelector::kMIN, Dims3(3, 100, 200));
// Normal input dim
profile -> setDimensions("foo", OptProfileSelector::kOPT, Dims3(3, 150, 250));
// Max input dim
profile -> setDimensions("foo", OptProfileSelector::kMAX, Dims3(3, 200, 300));
config.addOptimizationProfile(profile);
context.setOptimizationProfile();

// Inference phase
context -> setBindingDimensions(i, input_dim); // Bind the input i with a dim
context -> allInputDimensionsSpecified(); // Check if all input dims are set
context -> enqueueV2(data, stream, nullptr); // Execute
```

# Some Useful Parser
+ ONNX: [TRT official onnx parser](https://github.com/NVIDIA/TensorRT/tree/main/parsers), this is the **official recommended** parser.
+ PyTorch: pt -> onnx -> trt; pt -> trt with [this parser](https://github.com/NVIDIA-AI-IOT/torch2trt)
+ TensorFlow: [TF official parser](https://github.com/tensorflow)
+ Tencent Forward: [Parser](https://github.com/Tencent/Forward) for pt, tf and onnx


# PolyGraphy
The official DEBUG tool.