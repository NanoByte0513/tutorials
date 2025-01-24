import torch
import torch.nn as nn
import onnx

def main():
    # # Define a MobileNetV2 model
    # model = torch.hub.load('pytorch/vision:v0.6.0', 'mobilenet_v2', pretrained=True)
    # print(model)

    # # Export the model to ONNX
    # dummy_input = torch.randn(1, 3, 224, 224)
    # torch.onnx.export(model, dummy_input, "mobilenet_v2.onnx")

    # Load the ONNX model
    onnx_model = onnx.load("mobilenet_v2.onnx")

    node = onnx_model.graph.node[0]
    node_name = node.name
    print(node_name)


if __name__ == '__main__':
    main()