import cv2
import os
from PIL import Image

path = "/Users/admin/Documents/OpenCV/Lesson6/L6images"
os.chdir(path)

avgheight = 0
avgwidth = 0
numofimgs = len(os.listdir('.'))

for file in os.listdir('.'):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    avgwidth = avgwidth + width
    avgheight = avgheight + height

avgwidth = avgwidth//numofimgs
avgheight = avgheight//numofimgs
print(avgwidth)
print(avgheight)
print(21//5)

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file))
        width, height = img.size

        print(width, height)
        image = img.resize((avgwidth, avgheight), Image.ANTIALIAS)
        #cv2.imshow('the', image)
        image.save(file, 'JPEG', quality = 95)
        print(img.filename.split('\\')[-1], " is resized")
        #cv2.waitKey(0)
#cv2.destroyAllWindows()