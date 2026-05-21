import cv2

cap = cv2.VideoCapture('/Users/admin/Documents/OpenCV/DeleteCarVid.mp4')
# Trained XML file classifiers describes some features of some object we want to detectcar_
car_cascade = cv2.CascadeClassifier('/Users/admin/Documents/OpenCV/haarcascade_car.xml')
# Loop runs if cap is being initialized
while True:
    # Read frame from a video
    ret, frame = cap.read()
    gsvid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detects cars of diffrent sizes in the input image
    cars = car_cascade.detectMultiScale(gsvid, 1.5, 7)
    # To draw a rectangle around each car
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('hehe_cars', frame)
        key = cv2.waitKey(33)
        if key == 27:
            break
cv2.destroyAllWindows()