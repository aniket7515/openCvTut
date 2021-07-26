# to show Video
import cv2

cap=cv2.VideoCapture(0)
# set height and width
cap.set(3,640)     # 3 is the id for width
cap.set(4,480)     # 4 is the id for height

# Brightness
cap.set(10,100)   # 10 is the id for brightness


while True:
    success,img=cap.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF==ord('g'):
     break










# To show image
#

#img=cv2.imread('images/RT.jpg')

#cv2.imshow("Image",img)

#cv2.waitKey(0)