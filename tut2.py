import cv2
import random

img=cv2.imread('images/RT.jpg',-1)
#print(type(img))

#for i in range(100) :
#    for j in range(img.shape[1]):
 #       img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

#Copy and paste the part of image

tag=img[500:700,600:900]
img[100:300,650:950]=tag

cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
