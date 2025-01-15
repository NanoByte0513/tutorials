# toolkit.xpacker_cpu.main
1. Read onnx path from args --graph
2. Pass onnx model to serialize()

# serialize
1. Load onnx model from onnx path
2. Pass model to onnx_serialize()

# toolkit.serializer.onnx_serialize.onnx_serialize
1. Create fbs_model.Model with onnx_model inputs