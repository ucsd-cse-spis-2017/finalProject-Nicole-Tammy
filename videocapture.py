
# This script is for continuous video capture
# In addition it uses opencv to transform
# the video frams to HSV and displays the video stream 
import cv2
import picamera
from picamera.array import PiRGBArray
from picamera import PiCamera
import time


with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.start_recording("my_video.h264")
    camera.wait_recording(60)
    camera.stop_recording()
