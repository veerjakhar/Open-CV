import cv2
import numpy as np

score = 0

img = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson 5/27e464de-d11e-4681-9900-dfa0b3cd21bd.jpeg")

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.blur(grayimg, (3, 3))

detected_cir = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 0, maxRadius = 10000)

if detected_cir is not None:
    detected_cir = np.uint16(np.around(detected_cir))
    for pt in detected_cir[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(img, (a, b), r, (255, 50, 0), 2)
        score += 1
        cv2.imshow("89", img)
        print(score)
        cv2.waitKey(0)
cv2.destroyAllWindows()

