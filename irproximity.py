import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print ("PIR Module Test (CTRL+C to exit)")
    time.sleep(2)
    print ("Ready")
    while True:
        if GPIO.input(PIR_PIN):
            print ("Motion Detected!")
            time.sleep(1)
except KeyboardInterrupt:
               print (" Quit")
               GPIO.cleanup()
