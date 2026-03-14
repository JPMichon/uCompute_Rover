from machine import Pin, PWM
import utime

# Define the GPIO pin connected to the servo's signal wire
servo_pin = Pin(28) 

# Create a PWM object for the servo pin
pwm = PWM(servo_pin)

# Set the PWM frequency to 50Hz for standard servos
pwm.freq(50)

# Define pulse widths for different positions (adjust these values based on your servo)
# These are typical values for micro servos, representing microseconds
MIN_PULSE = 1000000  # Minimum pulse width (e.g., 0 degrees)
MID_PULSE = 1500000  # Mid-point pulse width (e.g., 90 degrees)
MAX_PULSE = 2000000  # Maximum pulse width (e.g., 180 degrees)

# Function to set the servo angle
def set_servo_angle(angle):
    # Map the angle (0-180) to the corresponding pulse width
    pulse_width = int(MIN_PULSE + (MAX_PULSE - MIN_PULSE) * (angle / 180))
    pwm.duty_ns(pulse_width) # Set duty cycle in nanoseconds

count = 0
set_servo_angle(count)
utime.sleep(1)
while True:
    count = 0
    
    while count <= 180:
        set_servo_angle(count)
        count += 1
        utime.sleep(.01)
 
    count = 180   
    while count >= 0:    
        set_servo_angle(count)
        count -= 1
        utime.sleep(.01)
    
utime.sleep(1)
# De-initialize PWM (optional)
pwm.deinit()