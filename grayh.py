# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('z11.jpg',0)

color = ('b','g','r')
#绘制多通道直方图
for i,col in enumerate(color):
#http://www.runoob.com/python/python-func-enumerate.html	
	histr = cv2.calcHist([img],[0],None,[256],[0,256])
	plt.plot(histr,color = col)
	plt.xlim([0,256])
#flatten()将数组变为一维 返回值为一份拷贝
hist,bins = np.histogram(img.flatten(),256,[0,256])
#计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/cdf.max()

#绘制x，y图像 https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
#plt.plot(cdf_normalized, color = 'b')
#https://www.cnblogs.com/python-life/articles/6084059.html
#plt.hist(img.flatten(),256,[0,256],color = 'r')
#x轴参数 https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlim.html
#plt.xlim([0,256])
#显示图例 https://blog.csdn.net/helunqu2017/article/details/78641290
#plt.legend(('cdf','histogram'), loc = 'upper left')

#构建Numpy掩模数组，cdf为原数组，当数组元素为0时，掩盖（计算时被忽略）。
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min()) * 255/(cdf_m.max() - cdf_m.min())
#对被掩盖的元素赋值，这里赋值为0 https://www.w3cschool.cn/doc_numpy_1_11/numpy_1_11-generated-numpy-ma-filled.html
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]
cv2.imwrite('z11z.jpg',img2)
#plt.show()