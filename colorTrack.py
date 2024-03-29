# This script is for continuous video capture
# In addition it uses opencv to transform
# the video frames to HSV and displays the video stream
import RPi.GPIO as GPIO
import time
import turns, ultrasound, servo
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
camera.framerate = 25
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)
'''                                       
def leftOrRight(x, centerX, width):
    distMid = x - centerX
    print("distmid is ", distMid, "centerX ", centerX, "x ", x, "width is ", width)
    if (distMid < 0) & (distMid > -(width//4)) & (distMid < -(width//8)):
        turns.left30()
    if (distMid < 0) & (distMid < -(width//4)):
        turns.left60()
    if (distMid > 0) & (distMid < width//4) & (distMid > width//8):
        turns.right30()
    if (distMid > 0) & (distMid > width//4):
        turns.right60()
    else:
        turns.forward()
'''

def checkUltrasound():
    if ultrasound.distance() <= 20 and ultrasound.distance() > -1:
        """stay still until the greeting is done and then restart"""
        print("GREETING, PLEASE BEND DOWN")
        turns.stayStill()
        os.system('omxplayer Hello.m4a &')
        time.sleep(2)
        os.system('omxplayer Glenn.m4a &')
        time.sleep(5)
        servo.servoHand()
        return True
    else:
        turns.forward()
        turns.stayStill()
        return False
        
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
        #cv2.imshow("Frame", image)
        #cv2.imshow("Mask", mask) # where we want to find the white pixels
        #cv2.imshow("Res", res)
        #key = cv2.waitKey(0) # was waitkey(1)   #& 0xFF
        #maskIm=Image.fromarray(mask.astype('uint8'))

        #width = int(mask.size[0])
        #height = int(mask.size[1])
        #centerX = width/2
        
        leftMostQuarter = mask[0:480, 0: (640//4)+(640//8)]
        leftMidQuarter = mask[0:480, (640//4)+(640//8):320]
        rightMidQuarter = mask[0:480, 320:(320+640//8)]
        rightMostQuarter = mask[0:480, (320+640//8):640]

        leftMostWhite = cv2.countNonZero(leftMostQuarter)
        leftMidWhite = cv2.countNonZero(leftMidQuarter)
        rightMidWhite = cv2.countNonZero(rightMidQuarter)
        rightMostWhite = cv2.countNonZero(rightMostQuarter)
        
        maxWhite = max(max(leftMostWhite, leftMidWhite), max(rightMidWhite, rightMostWhite))
        print("leftMostWhite: ", leftMostWhite, "  leftMidWhite: ", leftMidWhite, "  rightMidWhite: ",
        rightMidWhite, "  rightMostWhite: ", rightMostWhite)
        print("")
        print("maxWhite is ", maxWhite)

        """camera was flipped and hotglued so we are going to switch the directions"""
        if maxWhite == 0:
            turns.stayStill()
        elif maxWhite == leftMostWhite:
            turns.right30()
            turns.stayStill()
        elif maxWhite == leftMidWhite:
            turns.stayStill()
        elif maxWhite == rightMidWhite:
            turns.stayStill()
        else:
            turns.left30()
            turns.stayStill()

        
        
        #checkUltrasound()
        if checkUltrasound() == True:
            shiftpi.digitalWrite(1, shiftpi.LOW) #D1 was low
            shiftpi.digitalWrite(15, shiftpi.LOW) #D2 was low
            shiftpi.digitalWrite(2, shiftpi.LOW) #DPWM was low
            shiftpi.digitalWrite(5, shiftpi.LOW) #C1 was low
            shiftpi.digitalWrite(4, shiftpi.LOW) #C2 was high
            shiftpi.digitalWrite(3, shiftpi.LOW) #CPWM was low
            camera.close()
            shiftpi.shiftRegCleanup()
            break
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        """
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            cv2.destroyAllWindows()
            break
        """

if __name__ == '__main__':
    try:
        while True:
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
        camera.close()
        shiftpi.shiftRegCleanup()
        
