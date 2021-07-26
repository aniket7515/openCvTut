import cv2

# image colour conversion
img=cv2.imread('images/images.jfif')

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# To blur the image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)

#cv2.imshow("Image",img)
cv2.imshow("Gray color image",imgGray)
cv2.imshow("Blur image",imgBlur)

cv2.waitKey(0)