# 导入需要的库
from PIL import Image, ImageEnhance
import os


def adjust_brightness_contrast(img_path, save_path, brightness_factor=1.0, contrast_factor=1.0):
    """
    调整图片的亮度和对比度并保存新图片
    :param img_path: 原始图片的路径（必填）
    :param save_path: 调整后图片的保存路径（必填）
    :param brightness_factor: 亮度系数，默认1.0（原图亮度）
    :param contrast_factor: 对比度系数，默认1.0（原图对比度）
    """
    # 异常处理：防止图片路径错误、文件损坏等问题
    try:
        # 1. 打开原始图片
        img = Image.open(img_path)

        # 2. 调整亮度
        brightness_enhancer = ImageEnhance.Brightness(img)
        img_bright = brightness_enhancer.enhance(brightness_factor)

        # 3. 基于调整后的亮度，再调整对比度
        contrast_enhancer = ImageEnhance.Contrast(img_bright)
        img_final = contrast_enhancer.enhance(contrast_factor)

        # 4. 保存调整后的图片
        img_final.save(save_path)
        print(f"图片调整完成！已保存至: {save_path}")

    except FileNotFoundError:
        print(f"错误：找不到指定的图片文件，请检查路径 -> {img_path}")
    except Exception as e:
        print(f"程序执行出错：{str(e)}")


# ====================== 你只需要修改这里的配置即可 ======================
if __name__ == "__main__":
    # 配置项：修改为你的图片路径、保存路径、亮度/对比度参数
    SOURCE_IMAGE_PATH = "E:\Project\CrackNex\dataset\KICT\JPEGImages\LCSD_0243.jpg"  # 你的原始图片路径（如：C:/images/photo.png）
    SAVE_IMAGE_PATH = "243.jpg"  # 调整后图片的保存路径
    BRIGHTNESS = 2  # 亮度值
    CONTRAST = 1.2  # 对比度值
    # =====================================================================

    # 调用函数执行调整
    adjust_brightness_contrast(
        img_path=SOURCE_IMAGE_PATH,
        save_path=SAVE_IMAGE_PATH,
        brightness_factor=BRIGHTNESS,
        contrast_factor=CONTRAST
    )