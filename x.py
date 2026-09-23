import cv2
import matplotlib.pyplot as plt

# a. 图片左右翻转函数
def flip_left_right(img):
    """
    输入图片，返回左右翻转后的图片
    """
    flipped_img = cv2.flip(img, flipCode=1)
    return flipped_img

if __name__ == "__main__":
    # 读取图片
    img_path = "test.jpg"
    origin_img = cv2.imread(img_path)
    origin_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2RGB)
    
    # 调用翻转函数
    flip_img = flip_left_right(origin_img)

    # b. 同时显示原图和翻转后的图片
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.title("Original 原图")
    plt.imshow(origin_img)

    plt.subplot(1,2,2)
    plt.title("Flipped 左右翻转")
    plt.imshow(flip_img)

    plt.show()