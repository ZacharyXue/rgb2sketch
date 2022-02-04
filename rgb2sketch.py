import cv2
# import numpy as np
import matplotlib.pyplot as plt
import argparse
import os


# def img_show(img):
#     cv2.imshow('img',img)
#     cv2.waitKey(0)

#     while cv2.waitKey(100) != 27:# loop if not get ESC
#         if cv2.getWindowProperty('img',cv2.WND_PROP_VISIBLE) <= 0:
#             break
#     cv2.destroyAllWindows('img')


parser = argparse.ArgumentParser()

parser.add_argument("--name", default='13')

arg = parser.parse_args()

# 传入图片
img_path = os.path.join("./pic", arg.name + ".jpg")
raw = cv2.imread(img_path)

# 灰度图
gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)

# 图像取反
inv = 255 - gray

# 高斯滤波
ksize = 15
sigma = 50
blur = cv2.GaussianBlur(inv, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)

# 颜色减淡混合
# res = 255 * gray / (255 - blur_inv_x) 
res = cv2.divide(gray, 255 - blur, scale=255)

imgs = {"raw":raw,"gray":gray, "inv": inv, "blur": blur, "res":res}
# for s in imgs:
#     cv2.imshow(s,imgs[s])
#     while cv2.waitKey(100) != ord('n'):
#         pass
#     cv2.destroyWindow(s)

show_base = (10 + len(imgs)) * 10
for i, key in enumerate(imgs):
    plt.subplot(show_base + i + 1)
    plt.title(key)
    plt.axis('off')

    tmp_img = cv2.cvtColor(imgs[key], cv2.COLOR_BGR2RGB)
    plt.imshow(tmp_img)

plt.show()
