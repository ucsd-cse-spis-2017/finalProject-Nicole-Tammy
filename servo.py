import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

GPIO_Servo= 12

GPIO.setup(GPIO_Servo, GPIO.OUT)
# Set PWM parameters
pwm_frequency = 50

def set_duty_cycle(angle):
    pulse =  2*float(angle)/180.0 + 0.5
    duty = 0.1*pulse*pwm_frequency
    #duty = 2.5 + 0.12*float(angle) for frequency of 100
    return duty

    
# set speed to HIGH
pwm_servo = GPIO.PWM(GPIO_Servo, pwm_frequency)

angle = 90

def servoHand():
        angle=0
        pwm_servo.start(set_duty_cycle(angle))
        print("0")
        time.sleep(1)
        
        angle = 100
        pwm_servo.start(set_duty_cycle(angle))
        print ("100")
        time.sleep(1)
        
if __name__ == '__main__':
    try:
        while True:
            servoHand()
            
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Program stopped by User")
        GPIO.cleanup()
