import cv2
img1 = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson2/CROSSAINT.jpeg")
img2 = cv2.imread(r"/Users/admin/Documents/OpenCV/Lesson2/Pikachu.jpg")
print(img1.shape)
print(img2.shape)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
print(img2.shape)