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
import shiftpi
import os

GPIO.setmode(GPIO.BOARD)


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

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


def checkUltrasound():    
    if ultrasound.distance()<= 20:
        """stay still until the greeting is done and then restart"""
        turns.stayStill()
        os.system('mpg123 -q hello.mp3 &')   #runs this command through terminal

        
def captureFrames():
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
        maskIm=Image.fromarray(mask.astype('uint8'))

        width = int(maskIm.size[0])
        height = int(maskIm.size[1])
        centerX = width/2

        print("about to go into the loop")
        for x in range(0, (width-1)//5, 5): # looping through the image in five pixel blocks
            print("inside of x loop")
            for y in range(0, (height -1)//5, 5):
                whiteBlock = True
                centerWhiteBlockX = 0
                print("inside of y loop")
                for x1 in range(0,x+4):
                    print("looping through x")
                    for y1 in range(0,y+4):
                        print("x1 is ", x1) 
                        pixel = maskIm.getpixel((x+x1, y+y1))

                        if x1 == 3:             #these are the middle pixels of the white block
                            centerWhiteBlockX = (x1+x) # x dist from origin is (x1+x)
                            print("inside of x ==3")
                        if pixel == (0,0,0): #checks if the pixel is black
                            print("There are black pixels")
                            whiteBlock = False
                if whiteBlock == True:
                    """ find x dist from center line of image and turn right or left accordingly"""
                    print("is going to run leftOrRight")
                    leftOrRight(centerWhiteBlockX, centerX, width)
                    
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    try:
        while True:
            checkUltrasound()
            captureFrames()
            # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program stopped by User")
        #GPIO.cleanup()
        shiftpi.digitalWrite(1, shiftpi.LOW) #D1 was low
        shiftpi.digitalWrite(15, shiftpi.LOW) #D2 was low
        shiftpi.digitalWrite(2, shiftpi.LOW) #DPWM was low
        shiftpi.digitalWrite(5, shiftpi.LOW) #C1 was low
        shiftpi.digitalWrite(4, shiftpi.LOW) #C2 was high
        shiftpi.digitalWrite(3, shiftpi.LOW) #CPWM was low
        shiftpi.shiftRegCleanup()
