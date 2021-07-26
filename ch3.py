import cv2

img=cv2.imread('images/RT.jpg')

# How to resize the image
# check the shape of the image
print(img.shape)

# Resizing an image

imgResize=cv2.resize(img,(600,500))

# Crop an image
imgcropped=img[0:200,200:500]

cv2.imshow("Imagecropped",imgcropped)
cv2.imshow("ImageReszed",imgResize)
cv2.waitKey(0)