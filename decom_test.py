import torch
from PIL import Image
from torchvision import transforms
from model.DecompNet import DecompNet, load_decomp_ckpt
import numpy as np

# 初始化模型
decomp_net = DecompNet()
ckpt_path = "./model/backbone/DecompNet.tar"  # 确保路径正确
load_decomp_ckpt(decomp_net, ckpt_path)
decomp_net.eval()  # 推理模式

def preprocess_image(img_path):
    img = Image.open(img_path).convert('RGB')
    # 仅转为Tensor，不做归一化（关键修正：DecompNet输入应保持原始像素范围）
    transform = transforms.Compose([
        transforms.ToTensor()  # 输出范围0~1
    ])
    img_tensor = transform(img).unsqueeze(0)  # 增加batch维度
    return img_tensor

# 加载并预处理图像（使用正确路径格式）
img_tensor = preprocess_image("E:/Project/CrackNex/dataset/KICT/JPEGImages/LCSD_0243.jpg")

# 推理得到反射率（DecompNet输出已通过sigmoid限制在0~1）
with torch.no_grad():
    reflectance = decomp_net(img_tensor)  # 形状：(1, 3, H, W)，范围0~1

# 转换为可显示图像（直接映射0~1到0~255，无需反归一化）
reflectance_np = reflectance.squeeze().permute(1, 2, 0).numpy()  # (H, W, 3)
reflectance_np = (reflectance_np * 255).clip(0, 255).astype(np.uint8)  # 确保数值在有效范围

# 保存结果（PIL默认RGB通道，与输出一致）
Image.fromarray(reflectance_np).save("243.jpg")