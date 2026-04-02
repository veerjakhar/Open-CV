import cv2

img = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson 3/Pikachu.jpg")
# Line drawing on image
startpoint = (20, 200)
endpoint = (400, 400)
color = (250, 50, 0)
thickness = 1
centercoordinties = (50, 50)
radius = 10
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
fontScale = 1
text = 'Oh look a Fakey-->(😭(BOOOOO))'
#img1 = cv2.line(img, startpoint, endpoint, color, thickness)

# Rectangle command
#cv2.rectangle(img, startpoint, endpoint, color, thickness)

# Circle command
#cv2.circle(img, centercoordinties, radius, color, thickness)

# Drawing the texy on an image
cv2.putText(img, text, centercoordinties, font, fontScale, color, thickness, cv2.LINE_AA)

cv2.imshow('igtg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()