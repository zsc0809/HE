# 可执行
grayh.py 灰度图像直方图均衡化
colorh.py 彩色rgb三通道直方图均衡化
hsvh.py hsv v通道直方图均衡化
clahe.py 限制对比度的自适应直方图均衡化
psnr.py PSNR数值求取

# 命令行

运行MSRCR.py文件即可。

usage: python MSRCR.py [-h] -i INPUT -o OUTPUT [-s S] [-n N] [-d D]

optional arguments:
  -h, --help                       show this help message and exit
  -i INPUT, --input INPUT          Input image path
  -o OUTPUT, --output OUTPUT       Output image path
  -s S                             The scale (reference value)
  -n N                             The number of scale
  -d D                             The dynamic, the smaller the value, the higher the contrast
