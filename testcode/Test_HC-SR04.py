from machine import Pin,PWM,SPI
from hcsr04 import HCSR04
import utime
sensor = HCSR04(trigger_pin=27, echo_pin=24)

while True:
    print("Distance: "+str( int(sensor.distance_cm()))) # je mesure la distance
    utime.sleep(1) #j'attend 2 secondes pour que le servo ce place