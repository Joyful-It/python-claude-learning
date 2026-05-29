import torch
import transformers
import numpy as np

def check_environment():
    print("version:",torch.__version__)
    print("cuda if can use:",torch.cuda.is__available())
    if torch.cuda.is_available():
        print("cuda version:",torch.version.cuda)
        print("cuda shebei:",torch.cuda.get_device_name(0))#0?
        print("GPU shuliang:",torch.cuda.device_count())
    print("transformer version:",transformers.__version__)
    device=torch.device("cuda" if torch.cuda.is_available else "cpu")
    x=torch.random(3,3).to(device)
    y=torch.random(3,3).to(device)
    z=torch.matmul(x,y)
    print("outcome:",z.shape)


if __name__=="main":
    check_environment()