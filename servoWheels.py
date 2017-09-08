import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO_Servo2 = 37 #GPIO 26
GPIO_Servo3 = 32 #GPIO 12

GPIO.setup(GPIO_Servo2, GPIO.OUT)
GPIO.setup(GPIO_Servo3, GPIO.OUT)

# Set PWM parameters
pwm_frequency = 50

def set_duty_cycle(angle):
    pulse =  2*float(angle)/180.0 + 0.5
    duty = 0.1*pulse*pwm_frequency
    #duty = 2.5 + 0.12*float(angle) #for frequency of 100
    return duty

    
# set speed to HIGH
pwm_servo2 = GPIO.PWM(GPIO_Servo2, pwm_frequency)
pwm_servo3 = GPIO.PWM(GPIO_Servo3, pwm_frequency)

#angle = 90

def servo2Backwards():
        
        angle=0
        #pwm_servo2.start(15)
        pwm_servo2.start(set_duty_cycle(angle))

        
        print ("servo 2 Backwards")
        #time.sleep(1)

def servo3Forward():
        
        angle=0
        pwm_servo3.start(set_duty_cycle(angle))

        print ("servo 3 Forward")
        #time.sleep(1)


def servo2Forward():

        angle=180
        #pwm_servo2.start(78) 
        pwm_servo2.start(set_duty_cycle(angle))

        print ("servo 2 Forward")
        #time.sleep(1)

def servo3Backwards():

        angle=180
        pwm_servo3.start(set_duty_cycle(angle))

        print ("servo 3 Backwards")
        #time.sleep(1)

def servo2Stop():

        pwm_servo2.start(0)

        print ("servo 2 stop")
        #time.sleep(1)

def servo3Stop():

        pwm_servo3.start(0)
        print ("servo 3 stop")
        #time.sleep(1)

if __name__ == '__main__':
    try:
        while True:
            servo3Forward()
            servo2Forward()
            #servo2Backwards()
            #servo2Stop()
            #servo3Backwards()
            #servo3Stop()
            
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program stopped by User")
        GPIO.cleanup()

