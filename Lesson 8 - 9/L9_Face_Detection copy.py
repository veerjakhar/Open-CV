import cv2
import sys, numpy, os
print(cv2.__version__)
print(hasattr(cv2, 'face'))

# Setting
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

datasets = 'datasets'
(width, height) = (130, 100)
print("Recognising Face, Please Stay In Suffiecnt Lighting")

#load dataset train model
(images, labels, names, id) = ([], [], {}, 0)
for (subdir, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] =  subdir
        subjectpath = os.path.join(datasets, subdir)

        # Read all images of that person
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename

            # Read img in grayscale
            img = cv2.imread(path, 0)
            images.append(img)
            labels.append(id)
        id = id + 1

# convert list into numpy arrays
(images, labels) = [numpy.array(lis) for lis in [images,labels]]

# Create LBPH face recogniser
model = cv2.face.LBPHFaceRecognizer_create()

# Train Model
model.train(images, labels)

#Start Face Detection

face_cascade = cv2.CascadeClassifier(haar_file)

# start webcam
webcam = cv2.VideoCapture(0)
while True:
    # capture frame
    (_, im) = webcam.read()
    # convert to grayscale
    gsimg = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # detect faces
    faces = face_cascade.detectMultiScale(gsimg, 1.3, 4)
    # loop through all detected faces

    for (x,y,w,h) in faces:
        # Draw rectangle around face
        cv2.rectangle(im, (x,y), (x + w, y + h), (255, 0, 0), 2)
        #crop face
        face = gsimg[y: y + h, x: x + w]
        #resize face to fit in rectangle
        face_resize = cv2.resize(face, (width, height))
        
        #Predict Face
        prediction = model.predict(face_resize)

        # Prediction[0]= label
        #prediction[1] = confidence
        if prediction[1] < 70:
            # show recognised name
            cv2.putText(im, '%s - %.0f' % (names[prediction[0]], prediction[1]), (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
            # Draw rectangle around face
            cv2.rectangle(im, (x,y), (x + w, y + h), (40, 255, 0), 2)
        else:
            cv2.putText(im, 'Not Recognised', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0))
            cv2.rectangle(im, (x,y), (x + w, y + h), (255, 0, 0), 2)

    # Show Webcam Output
    cv2.imshow('frs', im)
    key = cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()