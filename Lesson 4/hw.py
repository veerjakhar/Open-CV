import cv2

img = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson 3/Pikachu.jpg")

startpoint = (20, 20)
endpoint = (200, 400)
color = (0, 0, 0)
colorcir = (0, 0, 250)
colorcir2 = (100, 255, 0)
colorcir3 = (0, 255, 255)
thickness = -1
centercoordinties1 = (100, 100)
centercoordinties3 = (100, 210)
centercoordinties2 = (100, 320)
radius = 50


cv2.rectangle(img, startpoint, endpoint, color, thickness)
cv2.circle(img, centercoordinties1, radius, colorcir, thickness)

cv2.circle(img, centercoordinties2, radius, colorcir2, thickness)

cv2.circle(img, centercoordinties3, radius, colorcir3, thickness)


cv2.imshow('back', img)

cv2.waitKey(0)
cv2.destroyAllWindows()