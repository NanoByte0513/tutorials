
# Mapping PyTorch OP to ONNX OP
All contents related to ONNX is in torch.onnx([Github page](https://github.com/pytorch/pytorch/tree/master/torch/onnx))

# Components of ONNX Model
## Graph
An ONNX graph(aka model) contains the following items:
1. nodes: Operators, a list of node in this graph.
2. inputs: A list of input Tensors.
3. outputs: A list of output Tensors.
4. **opset(int)**

## Node
A node is an OP.
1. op(str): The operations this node performs, for example Conv2d, Linear... 

## Tensor


# Customed OP for ONNX in PyTorch
[This article](https://mp.weixin.qq.com/s?__biz=Mzk0MDg1MjIwNg==&mid=2247528859&idx=1&sn=54d789a138328b794a8371402ea0ec69&source=41#wechat_redirect) shows how to develop a customed OP in PyTorch to support more ONNX OP.