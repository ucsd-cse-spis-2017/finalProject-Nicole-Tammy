# This script is for continuous video capture
# In addition it uses opencv to transform
# the video frames to HSV and displays the video stream 
import cv2
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np

def nothing(x):
    pass
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# Create a window for later use
cv2.namedWindow('result')
h, s, v = 100, 100, 100
img_low = np.zeros((15,512,3),np.uint8)

# Create a track bar
cv2.createTrackbar('h','result', 0, 255, nothing)
cv2.createTrackbar('s','result', 0, 255, nothing)
cv2.createTrackbar('v','result', 0, 255, nothing)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cv2.imshow('result', img_low)
    # Get info from trackbar and appy to the result
    h =  cv2.getTrackbarPos('h','result')
    s =  cv2.getTrackbarPos('s','result')
    v =  cv2.getTrackbarPos('v','result')
    img_low[:] = [h,s,v]
    # define the range of the green color in hsv
    lower_green = np.array([h,s,v])
    upper_green = np.array([32, 255, 255])

    # Threshold the hsv image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    #Bitwise AND mask and original image
    res = cv2.bitwise_and(image, image, mask = mask)

    
    # show the frame
    cv2.imshow("Frame", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Res", res)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
