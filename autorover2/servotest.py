from __future__ import division
import time

from pca9685.pca9685 import PCA9685 



# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
max_pulse = 4095

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')


# Move servo on channel O between extremes.
pwm.set_pwm(15, 0, servo_min)
# pwm.set_channel_off(2)
# pwm.set_channel_on(1)
pwm.set_pwm(0, 0, max_pulse)
pwm.set_pwm(2, 0, 0)
pwm.set_pwm(1, 0, max_pulse)

time.sleep(3)
pwm.set_pwm(0, 0, 2047)
time.sleep(3)
pwm.set_pwm(0, 0, 0)
time.sleep(1)

# pwm.set_channel_off(1)
# pwm.set_channel_on(2)
# pwm.set_pwm(0, 0, max_pulse)
# time.sleep(3)
# pwm.set_pwm(0, 0, 2047)
# time.sleep(3)
# pwm.set_pwm(0, 0, 0)



time.sleep(1)
pwm.set_pwm(15, 0, servo_max)
time.sleep(1)