import cv2

img1 = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson 3/Pikachu.jpg")
grayimg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

(row, col) = img1.shape[0:2]
'''
# Convert into a gray scale using averaging method without using the library
for i in range (row):
    for j in range (col):
        img1[i, j] = sum(img1 [i, j]) * 0.33
'''
hsvImage = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
bgr = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
M = cv2.getRotationMatrix2D((col / 2, row / 2), 104, 0.5)
res = cv2.warpAffine(img1, M, (col, row))
cv2.imshow('rq', bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()