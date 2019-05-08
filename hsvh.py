import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('z6.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
h, s, v = cv2.split(hsv)
#cv2.imshow("Hue", h)
#cv2.imshow("Saturation", s)
#cv2.imshow("Value", v)

#flatten() 将数组变成一维
hist,bins = np.histogram(v.flatten(),256,[0,256])

# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
# 构建 Numpy 掩模数组，cdf 为原数组，当数组元素为 0 时，掩盖（计算时被忽略）。
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# 对被掩盖的元素赋值，这里赋值为 0
cdf = np.ma.filled(cdf_m,0).astype('uint8')
v2 = cdf[v]

img2 = img.copy()
img2 = cv2.merge((h, s, v2))
img2 = cv2.cvtColor(img2, cv2.COLOR_HSV2BGR)
cv2.imwrite('z6zh.jpg',img2)
