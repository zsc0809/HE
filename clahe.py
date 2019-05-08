#import numpy as np
#import cv2


#img = cv2.imread('test6.jpg',0)

# create a CLAHE object (Arguments are optional).
#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

#cl1 = clahe.apply(img)
#cv2.imwrite('test6z.jpg',cl1)



import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('z7.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
h, s, v = cv2.split(hsv)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
v = clahe.apply(v)

img2 = img.copy()
img2 = cv2.merge((h, s, v))
img2 = cv2.cvtColor(img2, cv2.COLOR_HSV2BGR)
cv2.imwrite('z7zz.jpg',img2)