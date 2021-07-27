import cv2
import numpy as np

img=np.zeros((512,512),3),np.uint8

print(img)

img[:]=255,0,0   # Blue color

# to create lines
cv2.line(img,(0,0),(300,306),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

# For circle
cv2.circle(img,(400,50),30,(255,255,0),5)



cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
