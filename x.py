from PIL import Image
import matplotlib.pyplot as plt

def flip_left_right(input_img):
    """
    a. 图片左右翻转函数
    :param input_img: 输入一张图片对象
    :return: 左右翻转完成后的图片对象
    """
    # 执行左右翻转
    flipped_image = input_img.transpose(Image.FLIP_LEFT_RIGHT)

    # b. 同时展示原图 和 翻转后的图片
    plt.figure(figsize=(10, 4))

    # 左边：原图
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(input_img)
    plt.axis("off")

    # 右边：翻转图
    plt.subplot(1, 2, 2)
    plt.title("Flipped Image (Left-Right)")
    plt.imshow(flipped_image)
    plt.axis("off")

    plt.show()
    return flipped_image


if __name__ == "__main__":
    # 读取同目录下的图片 test.jpg
    img = Image.open("test.jpg")
    result_img = flip_left_right(img)