#  new_convert_llama_1p3b.int4.py
A LLaMA 1.3b model([HuggingFace Page](https://huggingface.co/princeton-nlp/Sheared-LLaMA-1.3B)), quanted with w4a8 strategy.

# main(args_in: list[str] | None = None)
## Load params from onnx or pytorch
+ Load from onnx and transfer to pytorch tensors:
```python
onnx_model = onnx.load(args.input)
# onnx initializer -> numpy array -> torch tensor
params = {t.name: torch.from_numpy(onnx.numpy_helper.to_array(t)) for t in onnx_model.graph.initializer}
```
+ Derectly load from pytorch:
```python
params = torch.load(args.input, map_location=torch.device("cpu"))
```

## Rename params
```python
new_params:dict = rename_params(params)
```

# rename_params(params)
Rename params

## Convert running_x and runnning_w to scale
```python
params_fix = {}
for k in params.keys():
    if ".running_w_channel" in k:
        k_scale = k.replace(".running_w_channel", ".scale_w_channel")
        params_fix[k_scale] = 7.0 / params[k] # signed int4
    elif ".running_x_all" in k:
        k_scale = k.replace(".running_x_all", ".scale_x_all")
        params_fix[k_scale] = 127.0 / params[k] # signed int8
params = params_fix
```

## Rename all transformer layers params


# pack_weight(fname, param_list, num_layer, num_head)
Save model weights and params to file(usually .pkg file).
+ fname(str): File name to write
+ param_list(list): list(params.items())
+ num_layers(int): tansformer layer num
+ num_head(int): Fixed to 32