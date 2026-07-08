import cv2
import numpy as np
img= cv2. imread("input.png")
print(type(img))
print(img.shape)
cv2.imshow("window",img)
cv2.waitKey(0)
