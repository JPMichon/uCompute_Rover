import utime
from machine import Pin

#https://courses.ideate.cmu.edu/16-223/f2021/text/code/pico-motor.html
nsleep=Pin(22, Pin.OUT)
nsleep.value(1)



# Make sure to set the correct pins!
LEFT_abin1 =Pin(15, Pin.OUT)
LEFT_abin2 = Pin(14, Pin.OUT)
Right_abin1 = Pin(13, Pin.OUT)
Right_abin2 = Pin(12, Pin.OUT)


motor1a = Pin(18, Pin.OUT)
motor1b = Pin(19, Pin.OUT)

def forward():
   motor1a.high()
   motor1b.low()
   
def backward():
   motor1a.low()
   motor1b.high()
   
def stop():
   motor1a.low()
   motor1b.low()
   

forward()
utime.sleep(2)
backward()
utime.sleep(2)
stop()