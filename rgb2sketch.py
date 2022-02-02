import cv2
import numpy as np

# def img_show(img):
#     cv2.imshow('img',img)
#     cv2.waitKey(0)

#     while cv2.waitKey(100) != 27:# loop if not get ESC
#         if cv2.getWindowProperty('img',cv2.WND_PROP_VISIBLE) <= 0:
#             break
#     cv2.destroyAllWindows('img')

# 传入图片
img_path = "./pic/13.jpg"
raw = cv2.imread(img_path)
# cv2.imshow("img", img)

# 灰度图
gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray", gray)

# 图像取反
inv = 255 - gray
# cv2.imshow("inv", inv)

# 高斯滤波
ksize = 15
sigma = 50
blur = cv2.GaussianBlur(inv, ksize=(ksize, ksize), sigmaX=sigma, sigmaY=sigma)
# cv2.imshow("blur",blur)

# 颜色减淡混合
# res = 255 * gray / (255 - blur_inv_x) 
res = cv2.divide(gray, 255 - blur, scale=255)
# cv2.imshow("res", res)

imgs = {"raw":raw,"gray":gray, "inv": inv, "blur": blur, "res":res}
for s in imgs:
    cv2.imshow(s,imgs[s])
    while cv2.waitKey(100) != ord('n'):
        pass
    cv2.destroyWindow(s)

cv2.imwrite("./docs/pic/res.png", res)