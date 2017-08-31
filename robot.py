# Libraries
import RPi.GPIO as GPIO
import time

 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
# set GPIO Pins
GPIO_Servo= 12
GPIO_Servo2= 16

GPIO_B1 = 13
GPIO_B2 = 11
GPIO_Bpwm = 15

GPIO_Apwm = 31
GPIO_A2 = 33
GPIO_A1 = 35

GPIO_Dpwm = 18
GPIO_D2=  22
GPIO_D1=32

GPIO_Cpwm= 40
GPIO_C2=38
GPIO_C1 = 36

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_Servo, GPIO.OUT)
GPIO.setup(GPIO_Servo2, GPIO.OUT)
GPIO.setup(GPIO_B1, GPIO.OUT)
GPIO.setup(GPIO_B2, GPIO.OUT)
GPIO.setup(GPIO_Bpwm, GPIO.OUT)
GPIO.setup(GPIO_A1, GPIO.OUT)
GPIO.setup(GPIO_A2, GPIO.OUT)
GPIO.setup(GPIO_Apwm, GPIO.OUT)


GPIO.setup(GPIO_D1, GPIO.OUT)
GPIO.setup(GPIO_D2, GPIO.OUT)
GPIO.setup(GPIO_Dpwm, GPIO.OUT)
GPIO.setup(GPIO_C1, GPIO.OUT)
GPIO.setup(GPIO_C2, GPIO.OUT)
GPIO.setup(GPIO_Cpwm, GPIO.OUT)

# set speed to HIGH

GPIO.output(GPIO_Bpwm, True)
GPIO.output(GPIO_B1, True)
GPIO.output(GPIO_B2, True)
GPIO.output(GPIO_Apwm, True)
GPIO.output(GPIO_A1, True)
GPIO.output(GPIO_A2, True)

GPIO.output(GPIO_Dpwm, True)
GPIO.output(GPIO_D1, True)
GPIO.output(GPIO_D2, True)
GPIO.output(GPIO_Cpwm, True)
GPIO.output(GPIO_C1, True)
GPIO.output(GPIO_C2, True)


# Set PWM parameters
pwm_frequency = 50

def set_duty_cycle(angle):
    pulse =  2*float(angle)/180.0 + 0.5
    duty = 0.1*pulse*pwm_frequency
    #duty = 2.5 + 0.12*float(angle) for frequency of 100
    return duty

    
# set speed to HIGH
pwm_servo = GPIO.PWM(GPIO_Servo, pwm_frequency)
pwm_servo2 = GPIO.PWM(GPIO_Servo2, pwm_frequency)

angle = 90
pwm_servo.start(set_duty_cycle(angle))
pwm_servo2.start(set_duty_cycle(angle))
 
if __name__ == '__main__':
    try:
        while True:
            angle=0
            pwm_servo.start(set_duty_cycle(angle))
            pwm_servo2.start(set_duty_cycle(angle))
            print("0")
            GPIO.output(GPIO_B1, False)
            GPIO.output(GPIO_B2, True)
            GPIO.output(GPIO_A1, True)
            GPIO.output(GPIO_A2, False)
            GPIO.output(GPIO_D1, False)
            GPIO.output(GPIO_D2, True)
            GPIO.output(GPIO_C1, True)
            GPIO.output(GPIO_C2, False)
            print ("Forward")
            time.sleep(1)

            angle=45
            pwm_servo.start(set_duty_cycle(angle))
            pwm_servo2.start(set_duty_cycle(angle))
            print ("45")
            GPIO.output(GPIO_B1, True)
            GPIO.output(GPIO_B2, False)
            GPIO.output(GPIO_A1, False)
            GPIO.output(GPIO_A2, True)
            GPIO.output(GPIO_D1, True)
            GPIO.output(GPIO_D2, False)
            GPIO.output(GPIO_C1, False)
            GPIO.output(GPIO_C2, True)
            print ("Backward")
            time.sleep(1)

            angle = 90
            pwm_servo.start(set_duty_cycle(angle))
            pwm_servo2.start(set_duty_cycle(angle))
            print ("90")
            GPIO.output(GPIO_B1, False)
            GPIO.output(GPIO_B2, False)
            GPIO.output(GPIO_A1, False)
            GPIO.output(GPIO_A2, False)
            GPIO.output(GPIO_D1, False)
            GPIO.output(GPIO_D2, False)
            GPIO.output(GPIO_C1, False)
            GPIO.output(GPIO_C2, False)
            print ("Stop")
            time.sleep(1)

            angle = 135
            pwm_servo.start(set_duty_cycle(angle))
            pwm_servo2.start(set_duty_cycle(angle))
            print ("135")
            GPIO.output(GPIO_B1, False)
            GPIO.output(GPIO_B2, True)
            GPIO.output(GPIO_A1, True)
            GPIO.output(GPIO_A2, False)
            GPIO.output(GPIO_D1, False)
            GPIO.output(GPIO_D2, True)
            GPIO.output(GPIO_C1, True)
            GPIO.output(GPIO_C2, False)
            print ("Forward")
            time.sleep(1)

            angle = 180
            pwm_servo.start(set_duty_cycle(angle))
            pwm_servo2.start(set_duty_cycle(angle))
            print ("180")
            GPIO.output(GPIO_B1, True)
            GPIO.output(GPIO_B2, False)
            GPIO.output(GPIO_A1, False)
            GPIO.output(GPIO_A2, True)
            GPIO.output(GPIO_D1, True)
            GPIO.output(GPIO_D2, False)
            GPIO.output(GPIO_C1, False)
            GPIO.output(GPIO_C2, True)
            print ("Backward")
            time.sleep(1)
            
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program stopped by User")
        GPIO.cleanup()
        
