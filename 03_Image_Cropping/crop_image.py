import cv2
import numpy as np
img = cv2.imread("03_Image_Cropping/input.png")
img_crop=img[100:400,100:600]
cv2.imwrite("03_Image_Cropping/output_crop.png", img_crop)
cv2.imshow("window",img_crop)
print(img_crop.shape)
cv2.waitKey(0)