import cv2
# imread is used to read an image by passing the path of image as input
# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged
print("start")
img = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson-1/Pikachu.jpg", 1)
B, G, R = cv2.split(img)
if img is None:
    print("img not found")
else:
    print("Img loaded")
    cv2.imshow("Pickachu Image", R)
    cv2.waitKey(0)
    cv2.destroyAllWindows()