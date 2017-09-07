# Libraries
import RPi.GPIO as GPIO
import time
import shiftpi, servoWheels
turnTime = 1
 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#set shift register pins
SER = 22
RCLK = 18
SRCLK = 16
# set GPIO Pins

GPIO_B1 = 29
GPIO_B2 = 7
GPIO_Bpwm = 15

GPIO_Apwm = 31
GPIO_A2 = 33
GPIO_A1 = 35

# set GPIO direction (IN / OUT)
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

shiftpi.digitalWrite(2, shiftpi.HIGH) 
shiftpi.digitalWrite(1, shiftpi.HIGH) #D1
shiftpi.digitalWrite(6, shiftpi.HIGH) #D2

shiftpi.digitalWrite(3, shiftpi.HIGH)
shiftpi.digitalWrite(5, shiftpi.HIGH) #C1
shiftpi.digitalWrite(4, shiftpi.HIGH) #C2


#stay still
def stayStill():
    GPIO.output(GPIO_B1, False)
    GPIO.output(GPIO_B2, False)
    GPIO.output(GPIO_A1, False)
    GPIO.output(GPIO_A2, False)

    servoWheels.servo2Stop()
    servoWheels.servo3Stop()
    
    shiftpi.digitalWrite(1, shiftpi.LOW) #D1
    shiftpi.digitalWrite(6, shiftpi.LOW) #D2
    shiftpi.digitalWrite(2, shiftpi.LOW) #DPWM
    shiftpi.digitalWrite(5, shiftpi.LOW) #C1 
    shiftpi.digitalWrite(4, shiftpi.LOW) #C2
    shiftpi.digitalWrite(3, shiftpi.LOW) #CPWM 

    print ("Stop")
    time.sleep(1)

def forward():
    GPIO.output(GPIO_B1, False)
    GPIO.output(GPIO_B2, True)
    GPIO.output(GPIO_A1, True)
    GPIO.output(GPIO_A2, False)

    servoWheels.servo2Forward()
    servoWheels.servo3Forward()

    shiftpi.digitalWrite(1, shiftpi.LOW) #D1
    shiftpi.digitalWrite(6, shiftpi.HIGH) #D2 15
    shiftpi.digitalWrite(2, shiftpi.HIGH) #DPWM
    shiftpi.digitalWrite(5, shiftpi.HIGH) #C1
    shiftpi.digitalWrite(4, shiftpi.LOW) #C2
    shiftpi.digitalWrite(3, shiftpi.HIGH) #CPWM
    
    print ("Forward")
    time.sleep(1)


#left 30 degrees
def left30(): 
    #a is going the opposite
    GPIO.output(GPIO_A1, False)
    GPIO.output(GPIO_A2, True)
    shiftpi.digitalWrite(5, shiftpi.LOW) #C1
    shiftpi.digitalWrite(4, shiftpi.HIGH) #C2
    shiftpi.digitalWrite(3, shiftpi.HIGH) #CPWM

    servoWheels.servo2Backwards()
    servoWheels.servo3Forward()
    
    GPIO.output(GPIO_B1, False)
    GPIO.output(GPIO_B2, True)
    shiftpi.digitalWrite(1, shiftpi.LOW) #D1
    shiftpi.digitalWrite(6, shiftpi.HIGH) #D2 15
    shiftpi.digitalWrite(2, shiftpi.HIGH) #DPWM

    print ("Left")
    time.sleep(turnTime)

#right 30 degrees
def right30(): 
    GPIO.output(GPIO_A1, True)
    GPIO.output(GPIO_A2, False)
    shiftpi.digitalWrite(5, shiftpi.HIGH) #C1
    shiftpi.digitalWrite(4, shiftpi.LOW) #C2
    shiftpi.digitalWrite(3, shiftpi.HIGH) #CPWM

    servoWheels.servo2Forward()
    servoWheels.servo3Backwards()
    
    GPIO.output(GPIO_B1, True)
    GPIO.output(GPIO_B2, False)
    shiftpi.digitalWrite(1, shiftpi.HIGH) #D1
    shiftpi.digitalWrite(6, shiftpi.LOW) #D2 15
    shiftpi.digitalWrite(2, shiftpi.HIGH) #DPWM    


    print ("Right")
    time.sleep(turnTime)
            
#left 60 degrees
def left60(): 
    left30()
    left30()
    
#right 60 degrees
def right60():
    right30()
    right30()

 
if __name__ == '__main__':
    try:
        left30()
        right30()
        forward()
        stayStill()
        #left60()
        #right60()
        #stayStill()
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
        

