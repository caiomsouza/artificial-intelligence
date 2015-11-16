
# python face_detect_with_request.py haarcascade_frontalface_default.xml


import requests
import cv2
import sys


from cStringIO import StringIO
from PIL import Image




# Get user supplied values
r = requests.get('http://hub.qgis.org/attachments/5368/AM00100M_F1_20110930_1556.jpg')

imagePath = Image.open(StringIO.StringIO(r.content))

#imagePath = i

#imagePath = sys.argv[1]
cascPath = sys.argv[1]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)