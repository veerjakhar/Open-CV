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

raw_video = cv2.VideoCapture("/Users/admin/Documents/OpenCV/Lesson 7/Delete.mov")
time.sleep(1)
count = 0
background = 0

#Captuering the Background
for i in range(60):
    returnvalue, background = raw_video.read()
    if returnvalue == False:
        continue

background = np.flip(background, axis = 1)
print("done")

while(raw_video.isOpened()):
    return_val, img = raw_video.read()
    if not return_val:
        break
    count = count+1 
    img = np.flip(img, axis = 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_Shade = np.array([135,  40, 50])
    upper_Shade = np.array([155,  255,  255])
    mask = cv2.inRange(hsv, lower_Shade, upper_Shade)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 2)
    mask = cv2.dilate(mask, kernel, iterations = 1)

    mask_inv = cv2.bitwise_not(mask)
    res1 = cv2.bitwise_and(background, background, mask = mask)
    res2 = cv2. bitwise_and(img, img, mask = mask_inv)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow('purpurinvs', final_output)
    key = cv2.waitKey(10)
    if key == 27:
        break

raw_video.release()
cv2.destroyAllWindows()