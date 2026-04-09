import cv2
import numpy as np
img1 = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson2/CROSSAINT.jpeg")
img2 = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson2/Pikachu.jpg")
img3 = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson2/textdelete.png")
print(img1.shape)
print(img2.shape)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
print(img2.shape)

#Adding of an image
weightedSum = cv2.addWeighted(img1, 0.9, img2, -0.2, 0)
cv2.imshow('weighted image', weightedSum)
cv2.waitKey(0)

#Subtraction of an image
sub = cv2.subtract(img1, img2)
cv2.imshow('seb', sub)
cv2.waitKey(0)

#Erosion of an image
kernel = np.ones((18, 18), np.uint8)
imge = cv2.erode(img3, kernel)
cv2.imshow('idk', imge)
cv2.waitKey(0)

#Bluring of an image
Gaussian = cv2.GaussianBlur(img2, (15, 15), 0)
cv2.imshow('ikik', Gaussian)
cv2.waitKey(0)

#Median Blur of an image
Median = cv2.medianBlur(img2, 9)
cv2.imshow('asap', Median)
cv2.waitKey(0)

#Bilateral Blur
Bilateral = cv2.bilateralFilter(img2, 15, 150, 150)
cv2.imshow('4E', Bilateral)
cv2.waitKey(0)

#Bordering of an image
#cv2.copyMakeBorder(img1, top, bottom, left, right, borderType, colorValue)
borderimg = cv2.copyMakeBorder(img2, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1)
cv2.imshow('idc', borderimg)

#| Border Type        | Description                         |
#| ------------------ | ----------------------------------- |
#| `BORDER_CONSTANT`  | Adds solid color (black by default) |
#| `BORDER_REFLECT`   | Mirrors the image                   |
#| `BORDER_REPLICATE` | Repeats edge pixels                 |
#| `BORDER_WRAP`      | Wraps around like circular          |

cv2.waitKey(0)
cv2.destroyAllWindows()