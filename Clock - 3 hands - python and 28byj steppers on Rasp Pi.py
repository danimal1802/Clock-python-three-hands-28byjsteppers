# 3 hand motor clock based on 28BYJ stepper motors 

# Initialize required libraries 
import time
import RPi.GPIO as GPIO	
from time import strftime

# Setting the GPIO pin description to BCM and turning off warnings
GPIO.setmode(GPIO.BCM)			
GPIO.setwarnings(False)	

# Set up and enable the GPIO pin assignments for motors 
#
# Variable   RPi(GPIO)	
# == Second Hand ==
coilA1_hand1   = 21    ; GPIO.setup(coilA1_hand1, GPIO.OUT); 	# IN1  
coilA2_hand1   = 20    ; GPIO.setup(coilA2_hand1, GPIO.OUT);    # IN3
coilB1_hand1   = 16    ; GPIO.setup(coilB1_hand1, GPIO.OUT);	# IN2
coilB2_hand1   = 12    ; GPIO.setup(coilB2_hand1, GPIO.OUT);    # IN4
# == Minute Hand ==
coilA1_hand2   = 1     ; GPIO.setup(coilA1_hand2, GPIO.OUT); 	# IN1  
coilA2_hand2   = 7     ; GPIO.setup(coilA2_hand2, GPIO.OUT);    # IN3
coilB1_hand2   = 8	   ; GPIO.setup(coilB1_hand2, GPIO.OUT);	# IN2
coilB2_hand2   = 25    ; GPIO.setup(coilB2_hand2, GPIO.OUT);    # IN4
# == Hour Hand ==
coilA1_hand3   = 24    ; GPIO.setup(coilA1_hand3, GPIO.OUT); 	# IN1  
coilA2_hand3   = 23    ; GPIO.setup(coilA2_hand3, GPIO.OUT);    # IN3
coilB1_hand3   = 18	   ; GPIO.setup(coilB1_hand3, GPIO.OUT);	# IN2
coilB2_hand3   = 15    ; GPIO.setup(coilB2_hand3, GPIO.OUT);    # IN4

def setStep1(w1, w2, w3, w4):
    # Change the state of the coils for the hand number
    GPIO.output(coilA1_hand1, w1)
    GPIO.output(coilA2_hand1, w2)
    GPIO.output(coilB1_hand1, w3)
    GPIO.output(coilB2_hand1, w4)

def setStep2(w5, w6, w7, w8):
    # Change the state of the coils for the hand number
    GPIO.output(coilA1_hand2, w5)
    GPIO.output(coilA2_hand2, w6)
    GPIO.output(coilB1_hand2, w7)
    GPIO.output(coilB2_hand2, w8)

def setStep3(w9, w10, w11, w12):
    # Change the state of the coils for the hand number
    GPIO.output(coilA1_hand3, w9)
    GPIO.output(coilA2_hand3, w10)
    GPIO.output(coilB1_hand3, w11)
    GPIO.output(coilB2_hand3, w12)    

def CW1(delay, steps):  
	for i in range(0, steps):
		setStep1(1, 0, 0, 1)
		time.sleep(delay)
		setStep1(0, 1, 0, 1)
		time.sleep(delay)
		setStep1(0, 1, 1, 0)
		time.sleep(delay)
		setStep1(1, 0, 1, 0)
		time.sleep(delay)
	setStep1(0,0,0,0)
    
def CW2(delay, steps):  
	for i in range(0, steps):
		setStep2(1, 0, 0, 1)
		time.sleep(delay)
		setStep2(0, 1, 0, 1)
		time.sleep(delay)
		setStep2(0, 1, 1, 0)
		time.sleep(delay)
		setStep2(1, 0, 1, 0)
		time.sleep(delay)
	setStep2(0,0,0,0)

def CW3(delay, steps):  
	for i in range(0, steps):
		setStep3(1, 0, 0, 1)
		time.sleep(delay)
		setStep3(0, 1, 0, 1)
		time.sleep(delay)
		setStep3(0, 1, 1, 0)
		time.sleep(delay)
		setStep3(1, 0, 1, 0)
		time.sleep(delay)
	setStep3(0,0,0,0)

# def calc_newpositions():

motor1pos = 0
motor2pos = 0
motor3pos = 0

while True:
   delay = 4/1000        # milliseconds - minimum delay
   # Get current Time variables for each hand
   hour = strftime("%I")
   minute = strftime("%M")
   second = strftime("%S")
#    print(" "+str(hour)+" ",end="")
#    print(" "+str(minute)+" ",end="")
#    print(int(second))
   # Advance the second hand 
   new_desired_step_position = int((float(second)*(512/60)))
#    print("New desired second step position = ", new_desired_step_position)
#    print("   Current second position = ", motor1pos)
   steps_to_advance =  (new_desired_step_position - motor1pos)
#    print("   Steps to advance second = ", steps_to_advance)
#    print("   If second steps to advance is negative ... then add 512")
   if (steps_to_advance < 0):
       steps_to_advance = steps_to_advance + 512
#        print ("    New second steps to advance is ", steps_to_advance)
#    print("   Advancing seconds ", steps_to_advance, " steps")
   CW1(delay, steps_to_advance )
#    print("   Updating current second position = ", new_desired_step_position)
   motor1pos = new_desired_step_position
#    print("   New second position set to ", motor1pos)
   # Advance the minute hand
   new_desired_step_position2 = int((float(minute)*(512/60)))
#    print("New desired minute step position = ", new_desired_step_position2)
#    print("   Current minute position = ", motor2pos)
   steps_to_advance2 =  (new_desired_step_position2 - motor2pos)
#    print("   Steps to advance minutes = ", steps_to_advance2)
#    print("   If minute steps to advance is negative ... then add 512")
   if (steps_to_advance2 < 0):
       steps_to_advance2 = steps_to_advance2 + 512
#        print ("    New minute steps to advance is ", steps_to_advance2)
#    print("   Advancing minutes ", steps_to_advance2, " steps")
   CW2(delay, steps_to_advance2 )
#    print("   Updating current minute position = ", new_desired_step_position2)
   motor2pos = new_desired_step_position2
#    print("   New minute position set to ", motor2pos)
   # Advance the hour hand
   new_desired_step_position3 = int((float(hour)*(512/12)))
#    print("New desired hour step position = ", new_desired_step_position3)
#    print("   Current hour position = ", motor3pos)
   steps_to_advance3 =  (new_desired_step_position3 - motor3pos)
#    print("   Steps to advance hours = ", steps_to_advance3)
#    print("   If hour steps to advance is negative ... then add 512")
   if (steps_to_advance3 < 0):
       steps_to_advance3 = steps_to_advance3 + 512
#    print ("    New hour steps to advance is ", steps_to_advance3)
#    print("   Advancing hours ", steps_to_advance3, " steps")
   CW3(delay, steps_to_advance3 )
#    print("   Updating current hour position = ", new_desired_step_position3)
   motor3pos = new_desired_step_position3
#    print("   New hour position set to ", motor3pos)
   time.sleep(.1)