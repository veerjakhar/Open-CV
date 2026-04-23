import cv2
import numpy as np
import time
print(cv2.__version__)
img = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson 7/DELETE.png")

def get_hsv(event, x , y, flagis, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        bgr = img[y, x]
        hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)
        print(f"clicked at ({x}, {y})")
        print("bgr: ", bgr)
        print("hsv:", hsv[0][0])
        print("----------------------------")

#cv2.imshow("click on your cloak", img)
#cv2.setMouseCallback("click on your cloak", get_hsv)

raw_video = cv2.VideoCapture("Delete.mov")
vid = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson 7/Delete.mov")
time.sleep(1)
count = 0
background = 0

for i in range(60):
    returnvalue, background = raw_video.read()
    if returnvalue == False:
        continue

background = np.flip(background, axis = 1)
print("done")

cv2.waitKey(0)
cv2.destroyAllWindows()