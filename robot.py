# Libraries
import RPi.GPIO as GPIO
#import time
import shiftpi
import turns

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#set shift register pins
SER = 22
RCLK = 18
SRCLK = 16

# set GPIO Pins

GPIO_Servo= 37
GPIO_Servo2= 12

GPIO_B1 = 29
GPIO_B2 = 7
GPIO_Bpwm = 15

GPIO_Apwm = 31
GPIO_A2 = 33
GPIO_A1 = 35 

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_Servo, GPIO.OUT)
GPIO.setup(GPIO_Servo2, GPIO.OUT)
GPIO.setup(GPIO_B1, GPIO.OUT)
GPIO.setup(GPIO_B2, GPIO.OUT)
GPIO.setup(GPIO_Bpwm, GPIO.OUT)
GPIO.setup(GPIO_A1, GPIO.OUT)
GPIO.setup(GPIO_A2, GPIO.OUT)
GPIO.setup(GPIO_Apwm, GPIO.OUT)

# set speed to HIGH

GPIO.output(GPIO_Bpwm, True)
GPIO.output(GPIO_B1, True)
GPIO.output(GPIO_B2, True)
GPIO.output(GPIO_Apwm, True)
GPIO.output(GPIO_A1, True)
GPIO.output(GPIO_A2, True)

shiftpi.digitalWrite(3, shiftpi.HIGH)

shiftpi.digitalWrite(2, shiftpi.HIGH) 
shiftpi.digitalWrite(1, shiftpi.HIGH) #D1
shiftpi.digitalWrite(6, shiftpi.HIGH) #D2

shiftpi.digitalWrite(5, shiftpi.HIGH) #C1
shiftpi.digitalWrite(4, shiftpi.HIGH) #C2


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

"""problems: back wheels keep turning after end, D doesn't turn foward"""
if __name__ == '__main__':
    try:
        while True:
            """
            angle=0
            pwm_servo.start(set_duty_cycle(angle))
            pwm_servo2.start(set_duty_cycle(angle))
            print("0")
            GPIO.output(GPIO_B1, False)
            GPIO.output(GPIO_B2, True)
            GPIO.output(GPIO_A1, True)
            GPIO.output(GPIO_A2, False)
            
            #PROBLEM IS HERE!!!!!!!!!!!!!!!! the problem was fixed....
            
            shiftpi.digitalWrite(1, shiftpi.LOW) #D1
            shiftpi.digitalWrite(6, shiftpi.HIGH) #D2 15
            shiftpi.digitalWrite(2, shiftpi.HIGH) #DPWM
            
            shiftpi.digitalWrite(5, shiftpi.HIGH) #C1
            shiftpi.digitalWrite(4, shiftpi.LOW) #C2
            shiftpi.digitalWrite(3, shiftpi.HIGH) #CPWM
            print ("Forward")
            shiftpi.delay(1000)
            
            angle=45
            pwm_servo.start(set_duty_cycle(angle))
            pwm_servo2.start(set_duty_cycle(angle))
            print ("45")
            GPIO.output(GPIO_B1, True)
            GPIO.output(GPIO_B2, False)
            GPIO.output(GPIO_A1, False)
            GPIO.output(GPIO_A2, True)
            
            shiftpi.digitalWrite(1, shiftpi.HIGH) #D1
            shiftpi.digitalWrite(6, shiftpi.LOW) #D2
            shiftpi.digitalWrite(2, shiftpi.HIGH) #DPWM
            
            shiftpi.digitalWrite(5, shiftpi.LOW) #C1
            shiftpi.digitalWrite(4, shiftpi.HIGH) #C2
            shiftpi.digitalWrite(3, shiftpi.HIGH) #CPWM        
            print ("Backward")
            shiftpi.delay(1000)
            
            angle = 90
            pwm_servo.start(set_duty_cycle(angle))
            pwm_servo2.start(set_duty_cycle(angle))
            print ("90")
            GPIO.output(GPIO_B1, False)
            GPIO.output(GPIO_B2, False)
            GPIO.output(GPIO_A1, False)
            GPIO.output(GPIO_A2, False)
            
            
            shiftpi.digitalWrite(1, shiftpi.LOW) #D1 
            shiftpi.digitalWrite(6, shiftpi.LOW) #D2 
            shiftpi.digitalWrite(2, shiftpi.LOW) #DPWM
            
            shiftpi.digitalWrite(5, shiftpi.LOW) #C1 
            shiftpi.digitalWrite(4, shiftpi.LOW) #C2
            shiftpi.digitalWrite(3, shiftpi.LOW) #CPWM 
            
            print ("Stop")
            shiftpi.delay(1000)
            
            turns.left30()
            shiftpi.delay(1000)
            print("turning left")

            turns.right30()
            shiftpi.delay(1000)
            print("turning right")

            turns.forward()
            shiftpi.delay(1000)
            print("going forward")
            """
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
            
