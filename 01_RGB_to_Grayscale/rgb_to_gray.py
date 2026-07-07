import cv2
import numpy as np
img=cv2.imread("images/img.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img_gray)
print(img_gray.shape)
print(img[100,100])#pixel check
img_save=cv2.imwrite("gray.png",img_gray)

cv2.imshow("window",img_gray)
cv2.waitKey(0)