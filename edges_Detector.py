import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)
img=cv2.imread('images/RT.jpg')
imgCanny=cv2.Canny(img,100,100)

# Increase the tickness of edge
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
# Decrease thickness of edge by erosion

imgEroded=cv2.erode(imgDialation,kernel,iterations=1)



cv2.imshow("Edge img",imgCanny)
cv2.imshow("Dialatio img",imgDialation)
cv2.imshow("Eroded img",imgEroded)
cv2.waitKey(0)