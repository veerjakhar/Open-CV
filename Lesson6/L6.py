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

images = [f for f in os.listdir('.') if f.endswith(('.jpg', '.jpeg', '.png'))]

for file in images:
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    print(width, height)
    image = img.resize((avgwidth, avgheight), Image.LANCZOS)
    #cv2.imshow('the', image)vid of audio when doign it
    image.save(file, 'JPEG', quality = 95)
    print(img.filename.split('\\')[-1], " is resized")
    
def video_gen():
    global path, images
    video_name = "running_boydelete.mp4"
    os.chdir(path)
    print(images)
    frame = cv2.imread(os.path.join('.', images[0]))
    height, width, layers = frame.shape
    #video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    video = cv2.VideoWriter(video_name, fourcc, 2, (width, height))
    ffmpeg -i running_boydelete.mp4 -vcodec libx264 output.mp4
    cv2.destroyAllWindows()
    video.release()


video_gen()
