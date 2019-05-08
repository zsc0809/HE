import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('z6.jpg')
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
color = (b, g, r)

# 对一个列表或数组既要遍历索引又要遍历元素时
# 使用内置 enumerrate 函数会有更加直接，优美的做法
#enumerate 会将数组或列表组成一个索引序列。
# 使我们再获取索引和索引内容的时候更加方便
for i,col in enumerate(color):

	#flatten() 将数组变成一维
	hist_i,bins_i = np.histogram(col.flatten(),256,[0,256])
	# 计算累积分布图
	cdf = hist_i.cumsum()
	cdf_normalized = cdf * hist_i.max()/ cdf.max()

	# 构建 Numpy 掩模数组，cdf 为原数组，当数组元素为 0 时，掩盖（计算时被忽略）。
	cdf_m = np.ma.masked_equal(cdf,0)
	cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
	# 对被掩盖的元素赋值，这里赋值为 0
	cdf = np.ma.filled(cdf_m,0).astype('uint8')
	if i == 0:
		b2 = cdf[col]
	elif i == 1:
		g2 = cdf[col]
	else:
		r2 = cdf[col]

img2 = img.copy()
img2[:,:,0] = b2
img2[:,:,1] = g2
img2[:,:,2] = r2
cv2.imwrite('z6zc.jpg',img2)
