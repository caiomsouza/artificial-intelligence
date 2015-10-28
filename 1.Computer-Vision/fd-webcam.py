# -*- coding: utf-8 -*-
"""

Face Recognition With Python, in Under 25 Lines of Code
https://realpython.com/blog/python/face-recognition-with-python/

Face Detection in Python Using a Webcam
https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/


Created on Wed Oct 28 16:19:50 2015

# Press Q to close the Program


@author: caiomsouza
"""

import cv2
import sys


import os

cascPath = os.getcwd()+'/haarcascades/haarcascade_frontalface_alt2.xml'


#cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()