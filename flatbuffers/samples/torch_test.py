import flatbuffers
from Torch import Model, Parameters, Tensor
import numpy as np
import torch

def save_buf():
    # Create a FlatBuffer builder 
    builder = flatbuffers.Builder(0)

    # Create model name
    model_name = builder.CreateString("llama")

    # Create weight param
    weight_name = builder.CreateString("llama.weight")
    # Create weight tensor
    weight_tensor = torch.randn(1, 3, 224, 224)
    weight_tensor_shape = builder.CreateNumpyVector(np.array(weight_tensor.shape, dtype=np.int32))
    weight_tensor_data = builder.CreateNumpyVector(np.array(weight_tensor.data.flatten().tolist(), dtype=np.float32))
    Tensor.Start(builder)
    Tensor.AddShape(builder, weight_tensor_shape)
    Tensor.AddData(builder, weight_tensor_data)
    weight_param_tensor = Tensor.End(builder)
    
    Parameters.Start(builder)
    Parameters.AddName(builder, weight_name)
    Parameters.AddTensor(builder, weight_param_tensor)
    weight_param = Parameters.End(builder)


    # Create bias param
    bias_name = builder.CreateString("llama.bias")
    # Create bias tensor
    bias_tensor = torch.randn(1, 3, 224)
    bias_tensor_shape = builder.CreateNumpyVector(np.array(bias_tensor.shape, dtype=np.int32))
    bias_tensor_data = builder.CreateNumpyVector(np.array(bias_tensor.data.flatten().tolist(), dtype=np.float32))
    Tensor.Start(builder)
    Tensor.AddShape(builder, bias_tensor_shape)
    Tensor.AddData(builder, bias_tensor_data)
    bias_param_tensor = Tensor.End(builder)
    
    Parameters.Start(builder)
    Parameters.AddName(builder, bias_name)
    Parameters.AddTensor(builder, bias_param_tensor)
    bias_param = Parameters.End(builder)

    # Create model table
    Model.Start(builder)
    Model.AddName(builder, model_name)
    Model.AddWeight(builder, weight_param)
    Model.AddBias(builder, bias_param)
    model = Model.End(builder)

    # Finish the buffer
    builder.Finish(model)
    buf = builder.Output()

    # Save buf to file
    with open('model.bin', 'wb') as f:
        f.write(buf)

def read_buf():
    # Load the buffer from the file 
    with open('model.bin', 'rb') as f: 
        buf = f.read()

    model = Model.Model.GetRootAsModel(buf, 0)
    model_name = model.Name().decode('utf-8')
    weight_param = model.Weight()
    bias_param = model.Bias()

    # Weight param
    weight_param_name = weight_param.Name().decode('utf-8')
    weight_param_tensor = weight_param.Tensor()
    weight_param_tensor_shape = tuple(np.array(weight_param_tensor.ShapeAsNumpy(), dtype=np.int32))
    weight_param_tensor_data = torch.tensor(np.array(weight_param_tensor.DataAsNumpy(), dtype=np.float32)).reshape(weight_param_tensor_shape)

    # Bias param
    bias_param_name = bias_param.Name().decode('utf-8')
    bias_param_tensor = bias_param.Tensor()
    bias_param_tensor_shape = tuple(np.array(bias_param_tensor.ShapeAsNumpy(), dtype=np.int32))
    bias_param_tensor_data = torch.tensor(np.array(bias_param_tensor.DataAsNumpy(), dtype=np.float32)).reshape(bias_param_tensor_shape)


    print(f"{model_name}, {type(model_name)}")
    print(f"{weight_param_name}, {type(weight_param_name)}")
    print(f"{weight_param_tensor_shape}, {type(weight_param_tensor_shape)}")
    print(f"{weight_param_tensor_data.shape}, {type(weight_param_tensor_data)}")
    print(f"{bias_param_name}, {type(bias_param_name)}")
    print(f"{bias_param_tensor_shape}, {type(bias_param_tensor_shape)}")
    print(f"{bias_param_tensor_data.shape}, {type(bias_param_tensor_data)}")
read_buf()