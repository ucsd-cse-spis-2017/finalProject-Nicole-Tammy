# This script is for continuous video capture
# In addition it uses opencv to transform
# the video frames to HSV and displays the video stream
import RPi.GPIO as GPIO
import time
import turns, ultrasound, videocapture
import cv2
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
from PIL import Image

GPIO.setmode(GPIO.BOARD)


def nothing(x):
    pass




# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

if ultrasound.distance()<= 20:
    turns.stayStill()

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define the range of the yellow color in hsv
    lower_yellow = np.array([21, 47, 46])
    upper_yellow = np.array([32, 255, 255])

    # Threshold the hsv image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    #Bitwise AND mask and original image
    res = cv2.bitwise_and(image, image, mask = mask)

    
    # show the frame
    cv2.imshow("Frame", image)
    cv2.imshow("Mask", mask) # where we want to find the white pixels
    cv2.imshow("Res", res)
    key = cv2.waitKey(1) & 0xFF

    width = mask.size(0)
    height = mask.size(1)
    centerX = width/2
    
    for x in range((width-1)/5, 5): # looping through the image in five pixel blocks
        for y in range((height -1)/5, 5):
            
            whiteBlock = True
            centerWhiteBlockX = 0

            for x1 in range(x+4):
                for y1 in range(y+4):
                    pixel = mask.getPixel(x, y)
                    if x1 == 3:             #these are the middle pixels of the white block
                        centerWhiteBlockX = (x1+x) # x dist from origin is (x1+x)
                    if pixel == (0,0,0): #checks if the pixel is black
                        whiteBlock = False
            if whiteBlock = True:
                """ find x dist from center line of image and turn right or left accordingly"""
               leftOrRight(centerWhiteBlockX, centerX, width)
               
def leftOrRight(centerWhiteBlockX, centerX, width):
    distMid = centerWhiteBlockX - centerX
    if (distMid < 0) & (distMid < width/4) & (distMid > width/8):
        turns.left30()
    if (distMid < 0) & (distMid > width/4):
        turns.left60()
    if (distMid > 0) & (distMid < width/4) & (distMid > width/8):
        turns.right30()
    if (distMid > 0) & (distMid > width/4):
        turns.right60()
    else:
        turns.forward()
        
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
