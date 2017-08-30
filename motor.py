# Libraries
import RPi.GPIO as GPIO
import time

 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
# set GPIO Pins
GPIO_Bin1 = 11
GPIO_Bin2 = 13
GPIO_Bpwm = 15

GPIO_Apwm = 31
GPIO_Ain2 = 33
GPIO_Ain1 = 35
 
# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_Bin1, GPIO.OUT)
GPIO.setup(GPIO_Bin2, GPIO.OUT)
GPIO.setup(GPIO_Bpwm, GPIO.OUT)
GPIO.setup(GPIO_Ain1, GPIO.OUT)
GPIO.setup(GPIO_Ain2, GPIO.OUT)
GPIO.setup(GPIO_Apwm, GPIO.OUT)

# set speed to HIGH
GPIO.output(GPIO_Bpwm, True)
GPIO.output(GPIO_Bin1, True)
GPIO.output(GPIO_Bin2, True)
GPIO.output(GPIO_Apwm, True)
GPIO.output(GPIO_Ain1, True)
GPIO.output(GPIO_Ain2, True)
 
if __name__ == '__main__':
    try:
        while True:
            GPIO.output(GPIO_Bin1, True)
            GPIO.output(GPIO_Bin2, False)
            GPIO.output(GPIO_Ain1, True)
            GPIO.output(GPIO_Ain2, False)
            print ("Forward")
            time.sleep(1)

            GPIO.output(GPIO_Bin1, False)
            GPIO.output(GPIO_Bin2, True)
            GPIO.output(GPIO_Ain1, False)
            GPIO.output(GPIO_Ain2, True)
            print ("Backward")
            time.sleep(1)

            GPIO.output(GPIO_Bin1, False)
            GPIO.output(GPIO_Bin2, False)
            GPIO.output(GPIO_Ain1, False)
            GPIO.output(GPIO_Ain2, False)
            print ("Stop")
            time.sleep(1)
            
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program stopped by User")
        GPIO.cleanup()
