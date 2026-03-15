import utime
from machine import Pin

#https://courses.ideate.cmu.edu/16-223/f2021/text/code/pico-motor.html
nsleep=Pin(22, Pin.OUT)

#Pour enabler les modules DRB8833, la pin nsleep doit etre a 1
nsleep.value(1)


#Moteurs Droit
motor1a = Pin(18, Pin.OUT) 
motor1b = Pin(19, Pin.OUT)
#Moteurs Gauche
motor2a = Pin(16, Pin.OUT) 
motor2b = Pin(17, Pin.OUT)

def forward():
   motor1a.high()
   motor1b.low()
   motor2a.high()
   motor2b.low()
   
def backward():
   motor1a.low()
   motor1b.high()
   motor2a.low()
   motor2b.high()
   
def stop():
   motor1a.low()
   motor1b.low()
   motor2a.low()
   motor2b.low()   

forward()
utime.sleep(2)
backward()
utime.sleep(2)
stop()