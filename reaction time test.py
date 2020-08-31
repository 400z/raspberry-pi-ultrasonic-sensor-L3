import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import random


TRIG=14
ECHO = 15
LED = 18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(LED,GPIO.LOW)
print ("wait for it")
wait = random.randint(5,20)
time.sleep(wait)
GPIO.output(LED,GPIO.HIGH)

i = 0
while True:
    GPIO.output(TRIG, False)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)


    pulse_start = 0
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    time.sleep(0.1)
    print("distance: ",distance,"cm")
    if i == 0:
        if distance <11:
            GPIO.output(LED,GPIO.LOW)
            print("remove your hand")
            break
        else:
            i= i+1
            reaction_start = time.time()
    elif i == 1:
        if distance <11:
            print("correct")
            reaction_end = time.time()
            GPIO.output(LED,GPIO.LOW)
            react_time = (reaction_end - reaction_start)
            react_time = round(react_time,2)
            print ("your reaction time is: ", react_time)
            break
    
        




GPIO.cleanup()

