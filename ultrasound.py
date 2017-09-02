# Libraries
import RPi.GPIO as GPIO
import time

 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# Wait for sensor to settle
GPIO.output(GPIO_TRIGGER, False)
print("Waiting for sensor to settle")
time.sleep(2)
print("Start sensing")


# Get the distance from the ultrasound sensor 
def distance():
    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    valid = True
    RefTime = time.time()
    StartTime = RefTime
    # save StartTime
    while (GPIO.input(GPIO_ECHO) == 0) and (StartTime-RefTime < 0.1):
        StartTime = time.time()
    if (StartTime-RefTime >= 0.1):
        valid = False
        
    RefTime = time.time()
    StopTime = time.time()
    # save time of arrival
    while (GPIO.input(GPIO_ECHO) == 1) and (StopTime-RefTime < 0.2):
        StopTime = time.time()
    if (StopTime-RefTime >= 0.1):
        valid = False
        
    
    if (valid):
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime

        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
    else:
        distance = -1
        
    return distance

 
if __name__ == '__main__':
    try:
        
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(0.5)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()import RPi.GPIO as GPIO
